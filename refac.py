import os
import time
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import argparse

from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

#parser = argparse.ArgumentParser()
#parser.add_argument('X', type=str, help="What is the first number?")

args = parser.parse_args()
#X = parser.parse_args - 옵션
print(X)

 # Email part
sender = ["<보내는메일 아이디>"] # ex) sender = "saram@naver.com"
toAddrList = ["<보내는메일 아이디>"] # ex) toAddrList = ["myID@naver.com"]
cc_users = [""]

msg = MIMEMultipart('alternative')  
msg['Subject'] = "https://twitter.com/"+X # X는 옵션으로 설정된 유저
msg['From'] = sender
msg['To'] = ",".join(toAddrList)
msg['Cc'] = ",".join(cc_users)

bluebird = "https://twitter.com/"+X
#html = urlopen(bluebird)
#bsObject = BeautifulSoup(html, "html.parser")


browser = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
browser.get(bluebird)

print(browser.text)

ids = driver.find_elements_by_xpath('//*[@id]')

new_exist = False

for ii in dis:
    #print("",link.get('data-image-url'))
    img = link.get('data-image-url')
    img = img.rpartition('/')
    attach = "/home/pi/Desktop/Crawl/"+img[2]
    #
    #urllib.request.urlretrieve(link.get('data-image-url'),"/home/pi/Desktop/"+bluebird+"/"+img[2])        
    if attach != None:
        if not os.path.exists("/home/pi/Desktop/Crawl/"+img[2]):
            print(img[2])
            urllib.request.urlretrieve(link.get('data-image-url'),"/home/pi/Desktop/Crawl/"+img[2])
            #/os.chmod("/home/pi/Desktop/Crawl/"+img[2],509)
            part = MIMEBase('application','octet-stream')
            part.set_payload(open(attach,'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename=%s'%os.path.basename(attach))
            msg.attach(part)
            # mail
            
            
            new_exist = True # 메일 전송 유무
            
if new_exist == True:
    text = 'Thank you,'
    part1 = MIMEText(text, _charset='euc-kr')
    ss = smtplib.SMTP_SSL('smtp.naver.com', 465)
    msg.attach(part1)
    
    ss.ehlo()
    ss.login('<보내는메일 아이디>','<보내는메일 비밀번호>')
    ss.sendmail('<보내는베일>', '<받는메일>', msg.as_string())
    ss.close()


print("done")
