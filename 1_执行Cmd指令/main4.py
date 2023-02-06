# Filename  ：test.py
# Author by ：袁成龙
# Data      ：2023 02 06 21:48
# 执行任意命令(如：ipconfig、systeminfo)，获取指定内容

import subprocess
cmd = input("请输入指令：")                # systeminfo
content = input("请输入过滤内容：")         #  物理内存总量:
proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
results = proc.stdout.readlines()
# print(results)
for result in results:
    out = result.decode('gbk')
    if content in out:
        IP_name = out.strip().split(':')[-1].strip()
        print(IP_name)

