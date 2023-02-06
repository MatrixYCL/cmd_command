# Filename  ：test.py
# Author by ：袁成龙
# Data      ：2023 02 06 21:02
# 执行ipconfig，获取全部内容

import subprocess
proc = subprocess.Popen('ipconfig',shell=True,stdout=subprocess.PIPE)
results = proc.stdout.readlines()

for result in results:
    # print(result)                 # 直接输出会显示乱码
    out = result.decode('gbk')      # 加上 gbk，不会显示乱码
    print(out)