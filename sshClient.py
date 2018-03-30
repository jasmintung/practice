# 基于用户名密码的连接
# 方式1
# import paramiko
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='192.168.80.111', port=22, username='zhangtong', password='zhangtong')
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# print(result.decode())
# # 关闭连接
# ssh.close()
# 方式2
# import paramiko
#
# transport = paramiko.Transport(('192.168.80.111', 22))
# transport.connect(username='zhangtong', password='zhangtong')
#
# ssh = paramiko.SSHClient()
# ssh._transport = transport
#
# stdin, stdout, stderr = ssh.exec_command('pwd')
# print(stdout.read().decode())
#
# transport.close()

# 基于公钥秘钥的连接,只在不同Linux系统环境下的连接

# import paramiko
#
# private_key = paramiko.RSAKey.from_private_key_file('/home/zhangtong/.ssh/id_rsa')
#
# # 创建SSH对象
# ssh = paramiko.SSHClient()
# # 允许连接不在know_hosts文件中的主机
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # 连接服务器
# ssh.connect(hostname='192.168.80.111', port=22, username='zhangtong', pkey=private_key)
#
# # 执行命令
# stdin, stdout, stderr = ssh.exec_command('df')
# # 获取命令结果
# result = stdout.read()
# print(result.decode())
#
# # 关闭连接
# ssh.close()
