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

def btncmd():
    destiny_user = (txt.get()) # 1 : 첫라인 0 : 0 번째 컬럼
    destiny_mail = (txt_mail.get())
    print(destiny_user)
    print(destiny_mail)
    result.insert(END,destiny_user + '\n')
    result.insert(END,destiny_mail + '\n')

btn = Button(root, width=10, text="다운로드", command=btncmd)
btn.pack()

result = Text(root, width=50, height = 10)
result.pack()

root.resizable(False, False)

root.mainloop()


