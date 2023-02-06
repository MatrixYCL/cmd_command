# Filename  ：test.py
# Author by ：袁成龙
# Data      ：2023 02 06 21:09
# 执行任意命令，获取全部内容,如 ipconfig、whoami

import subprocess
cmd = input("请输入指令：")
proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE)
results = proc.stdout.readlines()

for result in results:
    # print(result)                 # 直接输出会显示乱码
    out = result.decode('gbk')      # 加上 gbk，不会显示乱码
    print(out)