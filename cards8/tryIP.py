import paramiko
import subprocess

ip_prefix = "10.2.29" 
username = "ai-i-wuaodi"
password = "123456"

for i in range(1,255):
    ip = ip_prefix + "." + str(i)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username, password=password)
        print(f"Found server at {ip}")
        ssh.close()
        break
    except:
        print(f"{ip} is not the server")
