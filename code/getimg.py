import os
import time
import subprocess
import smtplib
#메일
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#웹
from selenium import webdriver
import argparse
#파일
from urllib.request import urlopen
import urllib.request

# UI
from tkinter import *

root = Tk()

root.title("Get Image from Tweet")
root.geometry("640x480")

# 목표 계정
label1 = Label(root, text="계정 주소")
label1.pack()

# txt = Text(root, width=30, height=1)
txt = Entry(root, width=30)
txt.pack()

# 받는 메일 주소
label_mail = Label(root, text="받을 메일 주소")
label_mail.pack()

txt_mail = Entry(root, width=30)
txt_mail.pack()

# SMTP 주소
label_smtp = Label(root, text="SMTP 메일 주소")
label_smtp.pack()

txt_smtp = Entry(root, width=30)
txt_smtp.pack()

# SMTP pwd
label_smtp_pwd = Label(root, text="SMTP 메일 pwd")
label_smtp_pwd.pack()

txt_smtp_pwd = Entry(root, width=30)
txt_smtp_pwd.pack()

# 동작
def btncmd():
    result.delete('1.0', END)
    destiny_user = txt.get() # 1 : 첫라인 0 : 0 번째 컬럼
    destiny_mail = txt_mail.get()
    smtp_mail = txt_smtp.get()
    smtp_id = smtp_mail.split('@')
    smtp_id = smtp_id[0]
    smtp_pwd = txt_smtp_pwd.get()
        
    # 대상 유저 변수선언
    X = destiny_user
    print(X)
    # 받는메일 변수 선언

     # Email part
    sender = smtp_mail
    toAddrList = [destiny_mail]
    cc_users = [""]

    msg = MIMEMultipart('alternative')  
    # 대상 트위터
    msg['Subject'] = "https://twitter.com/"+X
    msg['From'] = sender
    msg['To'] = ",".join(toAddrList)
    msg['Cc'] = ",".join(cc_users)

    bluebird = "https://twitter.com/"+X

    #headless
    webdriver_option = webdriver.ChromeOptions()
    webdriver_option.add_argument('headless')
    webdriver_option.add_argument('window-size=1366x768')
    webdriver_option.add_argument('disable-gpu')

    #print('web')
    browser = webdriver.Chrome('chromedriver.exe',chrome_options=webdriver_option)
    browser.get(bluebird)

    # 로딩 대기시간
    time.sleep(5)

    ids = browser.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div')

    new_exist = False
    #print('crawl')
    for ii in ids:
        img = ii.find_elements_by_xpath(".//div/div/article/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/a/div/div[2]/div/img")
        for test in img:
            src = test.get_attribute('src')
            print(src)
            result.insert(END,src + '\n')
            jpgs = src.split('/')
            names = jpgs[4].split('?')
            attach = ".//GetImg/"+ names[0] + ".jpg"

            if attach != None:
                if not os.path.exists(attach):
                    print(names[0])
                    result.insert(END,names[0] + '\n')
                    urllib.request.urlretrieve(src, attach)
                    part = MIMEBase('application','octet-stream')
                    part.set_payload(open(attach,'rb').read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename=%s'%os.path.basename(attach))
                    msg.attach(part)

                    new_exist = True # 메일 전송 유무

    if new_exist == True:
        print('mail')
        text = 'Thank you,'
        part1 = MIMEText(text, _charset='euc-kr')
        ss = smtplib.SMTP_SSL('smtp.naver.com', 465)
        msg.attach(part1)
    
        ss.ehlo()
        ss.login('lounge_cu',smtp_pwd)
        ss.sendmail(smtp_mail,destiny_mail, msg.as_string())
        ss.close()

    print('done')
    result.insert(END,'done' + '\n')
    browser.close()

    result.insert(END,destiny_user + '\n')
    result.insert(END,destiny_mail + '\n')

btn = Button(root, width=10, text="다운로드", command=btncmd)
btn.pack()

result = Text(root, width=50, height = 10)
result.pack()

root.resizable(False, False)

root.mainloop()


