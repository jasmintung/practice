# 遇到IO阻塞时会自动切换任务
from gevent import monkey
monkey.patch_all()
import gevent

from urllib.request import urlopen

save_path = "F:\pachong"

n = 0


def f(url):
    global n
    print("GET: %s" % url)
    resp = urlopen(url, timeout=3)
    data = resp.read()  # 这个read方法默认是阻塞调用,比如url是非法的,那么会阻塞整个程序
    n += 1
    print(n)
    with open(save_path + "\\" + str(n) + ".html", "wb") as wf:
        wf.write(data)
    print("%d bytes received from %s." % (len(data), url))

gevent.joinall(
    [
        gevent.spawn(f, "http://pm.streamax.com/DevSuite/Login.aspx#p-565"),
        gevent.spawn(f, "https://www.yahoo.com/"),
        gevent.spawn(f, "https://github.com")
    ]
)
# gevent.spawn(f, "https://www.python.org/"),