# 用于连接远程服务器并执行上传下载
# 方式一：基于用户名密码的上传下载
import paramiko

transport = paramiko.Transport(('192.168.80.111', 22))
transport.connect(username='zhangtong', password='zhangtong')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将F:\test1\ay_video_datas.264 上传到 /home/common/streamax/common/zhangtong/
sftp.put(r'F:\test1\ay_video_datas.264', '/home/common/streamax/common/zhangtong/ay_video_datas.264')
# 将/home/common/streamax/common/zhangtong/PlatformProtocal20170420.tar.gz 下载到本地 F:\test1\cc.tar.gz
sftp.get('/home/common/streamax/common/zhangtong/PlatformProtocal20170420.tar.gz', r'F:\test1\cc.tar.gz')

transport.close()
