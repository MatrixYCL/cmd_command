# 执行ipconfig，获取IPv4地址
import subprocess
proc = subprocess.Popen('ipconfig',shell=True,stdout=subprocess.PIPE)
results = proc.stdout.readlines()
# print(results)
for result in results:
    out = result.decode('gbk')
    if "IPv4 地址" in out:
        IP_name = out.strip().split(':')[-1].strip()
        print(IP_name)
