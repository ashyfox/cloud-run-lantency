from ipaddress import ip_address
from queue import Empty
import subprocess
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime
import os
import json
import random
import time
message_tmp = []
tonow=datetime.datetime.now()
email_time = str(tonow.month) + '/' + str(tonow.day)
i=0


#content["Cc"]=""
message_tmp.append(f"Hi all,\n測試郵件\n")
message ='\n'.join(message_tmp)


while i < 50:
    content = MIMEMultipart()  #建立MIMEMultipart物件
    rand_num=str(random.randint(1,1000))
    content["subject"] = (rand_num)+ " " + (email_time) + " 測試信件"  #郵件標題
    content["from"] = "example@xxx.com"  #寄件者
    content["to"] = "example@xxx.com,example@xxx.com" #收件者
    content.attach(MIMEText(message))  #郵件內容 
    print(i)
    i=i + 1
    time.sleep(5)
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("example@xxx.com", "example_password")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)  
