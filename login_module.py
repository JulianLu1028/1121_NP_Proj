import sys
import tkinter.messagebox
from tkinter import *
import tkinter as tk
import json

login_success = False   #因為tkinter的執行是loop, 所以確認登入用的變數要放在外面

def start_login_interface():

    window = tk.Tk()
    window.geometry('500x520+500+300')
    window.title('網路撿紅點 - 登入')

    def user_log_in(event = None):
        user_name = uname.get() #获取登录账号
        user_pwd = password.get()#获取登录密码

        try:
            with open('usr_info.json','r') as usr_file: #加载json文件
                users_info = json.load(usr_file)
        except FileNotFoundError :                      #如果文件为空 创建默认账号密码
            with open('usr_info.json','w') as usr_file :
                users_info = {'admin':'admin'}
                json.dump(users_info,usr_file)          #把默认账号密码加载进json中

        if user_name in users_info :                    #判断账号是否存在
            if user_pwd == users_info[user_name] :      #判断账号密码是否正确
                tk.messagebox.showinfo('登入成功 ','歡迎您：'+user_name)  #正确则提示正确

                global login_success    #因為要修改全域變數,要用global
                login_success = True

                window.destroy()  # 關閉 Tkinter 視窗
            else:
                tk.messagebox.showerror('密碼錯誤')               #提示错误
        elif user_name == ''  or user_pwd == '' :                     #判断账号密码是否为空
            tk.messagebox.showerror('錯誤','帳號或密碼為空')            #提示

        else :
            flag = tk.messagebox.askyesno('尚未註冊，是否要註冊') #如果账号存在提示是否注册
            if flag :
                rgister() #调用注册函数


    canvas = tk.Canvas(window,bg='purple',height=300,width=500)
    img_file = tk.PhotoImage(file='login_BG.png')
    img=canvas.create_image(250,150,anchor='center',image=img_file)
    canvas.place(x=0,y=0,anchor='nw')


    #设置登录按钮
    login=tk.Button(window,text='登入', width=8, height=2,command=user_log_in)
    login.place(y=416,x=240)

    rg_name=tk.StringVar
    rg_psd=tk.StringVar
    rg_repsd=tk.StringVar

    def user_register():
            sign_name = rg_name.get()               #获取注册账号
            sign_psw = rg_psd.get()                 #获取注册密码
            pwd_confirm = rg_repsd.get()            #获取注册确认密码

            try:
                with open('usr_info.json', 'r') as usr_file:     #加载json文件 存进usr_file中 with as自动关闭文件
                    exist_usr_info = json.load(usr_file)         #加载usr_file 文件 中的数据赋值给exist_usr_info
                    print(exist_usr_info)                        #这个用打印文件 用来调试 看看数据有没有存在
            except FileNotFoundError:                            #如果数据为空 初始化一个空字典 
                exist_usr_info = {}

            if sign_name in exist_usr_info:                      #判断获取需要注册的账号是否存在
                tk.messagebox.showerror('錯誤', '帳號已存在')     #如果存在则提示
            elif sign_psw == '' or sign_name == '':              #如果账号密码为空则提示
                tk.messagebox.showerror('錯誤', '帳號或密碼為空')  
            elif sign_psw != pwd_confirm:                        #如果俩次密码输入不一致提示
                tk.messagebox.showerror('錯誤', '密碼前後不一致')
            else:
                exist_usr_info[sign_name] = sign_psw             #否则存入字典 
                with open('usr_info.json', 'w') as usr_file:      
                    json.dump(exist_usr_info, usr_file)       
                tk.messagebox.showinfo('註冊成功')   



    #注册topLevel窗口
    def rgister():
        global rg_name
        global rg_repsd
        global rg_psd
        rg=tk.Toplevel(window)
        rg.title('註冊')
        rg.geometry('350x300+550+350')
        Label(rg, text='帳號：').place(x=50,y=20,anchor='nw')
        rg_name=tk.Entry(rg);rg_name.place(x=110,y=20,anchor='nw')

        Label(rg, text='密碼：').place(x=50,y=50,anchor='nw')
        rg_psd = tk.Entry(rg,show='*');rg_psd.place(x=110,y=50,anchor='nw')

        Label(rg, text='確認密碼：').place(x=50,y=75,anchor='nw')
        rg_repsd = tk.Entry(rg, show='*');rg_repsd.place(x=110,y=80,anchor='nw')

        tk.Button(rg, text='確認註冊',command=user_register).place(x=100, y=110, anchor='nw')

        rg.mainloop()




    #设置注册按钮
    regiset=tk.Button(window,text='註冊', width=8, height=2,command=rgister)
    regiset.place(y=416,x=140)

    tk.Button(window,text='退出', width=8, height=2,command=sys.exit).place(y=460,x=190)

    #账号标签及文本框
    Label(window,text='帳號：').place(y=350,x=140)
    uname=tk.Entry(window, width= 20)
    uname.place(y=350,x=175)

    #密码标签及文本框
    Label(window,text='密碼：').place(y=385,x=140)
    password=tk.Entry(window, show='*', width= 20)
    password.place(y=385,x=175)

    window.bind('<Return>', user_log_in)


    window.mainloop()
    print (login_success)
    return login_success