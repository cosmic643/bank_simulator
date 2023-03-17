import tkinter as tk
import random
import pickle
import os
#create account
def CA():
    filecreate = open("BDATA.dat","ab")
    filecreate.close()
    win2 = tk.Toplevel()
    win2.geometry('400x400')
    win2.title("Create new Account - Bank of People")
    label_title = tk.Label(win2,text = "Create new Account: ")
    label_title.grid(column = 1,row = 0)
    label_name = tk.Label(win2,text = "Enter your name: ")
    label_name.grid(column = 0,row = 1)
    name = tk.Entry(win2)
    name.grid(column = 1,row = 1)
    label_DOB = tk.Label(win2,text = "Enter your DOB(DD/MM/YY): ")
    label_DOB.grid(column = 0,row = 2)
    DOB = tk.Entry(win2)
    DOB.grid(column = 1,row = 2)
    label_gender = tk.Label(win2,text = "Enter your Gender: ")
    label_gender.grid(column = 0,row = 3)
    gender = tk.Entry(win2)
    gender.grid(column = 1,row = 3)
    label_mobile = tk.Label(win2,text = "Enter your Mobile number: ")
    label_mobile.grid(column = 0,row = 4)
    mobile = tk.Entry(win2)
    mobile.grid(column = 1,row = 4)
    label_balance = tk.Label(win2,text = "Enter your starting balance: ")
    label_balance.grid(column = 0,row=5)
    s_bal = tk.Entry(win2)
    s_bal.grid(column = 1,row = 5)
    label_UID = tk.Label(win2,text = "Enter the desired User ID: ")
    label_UID.grid(column = 0,row = 6)
    UID = tk.Entry(win2)
    UID.grid(column = 1,row = 6)
    label_pwd = tk.Label(win2,text = "Enter password: ")
    label_pwd.grid(column = 0,row = 7)
    pwd = tk.Entry(win2)
    pwd.grid(column = 1,row = 7)
    def add_data():
        R=[]
        Name = str(name.get())
        dob = str(DOB.get())
        Gender = str(gender.get())
        num= str(mobile.get())
        print(s_bal.get())
        try:
            sbal = int(s_bal.get())
        except Exception:
            sbal = 0
        UserID = str(UID.get())
        password = str(pwd.get())
        fin= open("BDATA.dat","rb") 
        com = UserID
        found=0
        while True:
            try:
                R=pickle.load(fin)
                if R[5]==com:
                    found=1
                    t = "USERNAME ALREADY TAKEN"
                    message = tk.Text(win2,height = 1,width = 25)
                    message.grid(column = 1,row = 9)
                    message.insert(tk.END,t)
            except EOFError:
                fin.close()
                break
        if found==0:
            f = open("BDATA.dat","ab")
            R=[Name,dob,Gender,num,sbal,UserID,password]
            pickle.dump(R,f)
            f.close()
            win2.destroy
    button_save = tk.Button(win2,text = "Create New Account!!",command  = add_data)
    button_save.grid(column = 1,row = 8)
    def close_win():
        win2.destroy()
    button_exit = tk.Button(win2,text = "EXIT",command = close_win)
    button_exit.grid(column = 1,row = 10)
    win2.mainloop()

def login(uid,pwd):
    record = []
    print(uid,pwd)
    print(type(uid),type(pwd))
    win3 = tk.Toplevel()
    win3.geometry("500x400")
    win3.title("Your Account")
    info = tk.Text(win3,height = 10,width = 33)
    info.grid(column = 1 , row = 0)
    filein = open("BDATA.dat","rb")
    msg = "NO ACCOUNT FOUND"
    rvar = 0
    try:
        while True:
            data = pickle.load(filein)
            print(data)
            for record in data:
                if data[5] == uid and data[6] == pwd :
                    print(data)
                    info.insert(tk.END,"Name: " + data[0]+"\n"+"DOB: " + data[1]+"\n"+"Gender: " + data[2]+"\n"+"Mobile: " + data[3])
                    rvar = 1
                    break
    except Exception:
        filein.close()
    if rvar == 0:
        info.insert(tk.END,msg)
    else:
        pass
    label1 = tk.Label(win3,text = "Deposit amount")
    label1.grid(column = 0,row = 1)
    damt = tk.Entry(win3)
    damt.grid(column = 1,row = 1)
    label2 = tk.Label(win3,text = "Withdraw amount")
    label2.grid(column = 0,row = 2)
    wamt = tk.Entry(win3)
    wamt.grid(column = 1,row = 2)
    label3 = tk.Label(win3,text = "RTGS Services")
    label3.grid(column = 0,row = 4)
    label4 = tk.Label(win3,text = "Transfer to(enter username): ")
    label4.grid(column = 0,row = 5)
    tun = tk.Entry(win3)
    tun.grid(column = 1,row = 5)
    label5 = tk.Label(win3,text = "Transfer Amount: ")
    label5.grid(column = 0,row = 6)
    tamt = tk.Entry(win3)
    tamt.grid(column = 1,row = 6)
    
    def deposit():
        dep = int(damt.get())
        fin=open('BDATA.dat','rb')
        fout=open('temp.dat','wb')
        try:
            while True:
                R=pickle.load(fin)
                if R[5] == uid and R[6] == pwd:
                    R[4] += dep
                    pickle.dump(R,fout)
                    found=True
                else:
                    pickle.dump(R,fout)
        except EOFError:
            if found==False:
                pass
            else:
                print("Deposit Successfull")
        fin.close()
        fout.close()
        os.remove('BDATA.dat')
        os.rename('temp.dat', 'BDATA.dat')
    def withdraw():
        wid = int(wamt.get())
        fin=open('BDATA.dat','rb')
        fout=open('temp.dat','wb')
        try:
            while True:
                R=pickle.load(fin)
                if R[5] == uid and R[6] == pwd:
                    R[4] -= wid
                    pickle.dump(R,fout)
                    found=True
                else:
                    pickle.dump(R,fout)
        except EOFError:
            if found==False:
                pass
            else:
                print("Withdraw Successful")
        fin.close()
        fout.close()
        os.remove('BDATA.dat')
        os.rename('temp.dat', 'BDATA.dat')
    def checkbalance():
        fin = open('BDATA.dat','rb')
        try:
            while True:
                R=pickle.load(fin)
                if R[5] == uid and R[6] == pwd:
                    balance = R[4]
        except EOFError:
            pass
        cbal = tk.Text(win3,height = 2,width = 15)
        cbal.grid(column = 1,row = 3)
        cbal.insert(tk.END,balance)
    def transfer():
        tname = tun.get()
        tdep = int(tamt.get())
        twid = int(tamt.get())
        f=open('BDATA.dat','rb')
        try:
            while True:
                rec = pickle.load(f)
                if tname == rec[5]:
                    p = True
                    print("The account exists")
                    f.close()
                    break
                else:
                    p = False
        except EOFError:
            f.close()
        print(p)
        fin=open('BDATA.dat','rb')
        fout=open('temp.dat','wb')
        try:
            while p == True:
                R=pickle.load(fin)
                print(R[5])
                if R[5] == tname :
                    R[4] += tdep
                    pickle.dump(R,fout)
                    found=True
                else:
                    pickle.dump(R,fout)
        except EOFError:
            if found==False:
                pass
            else:
                print("Money recieved from ",uid)
        fin.close()
        fout.close()
        if p == True:
            os.remove('BDATA.dat')
            os.rename('temp.dat', 'BDATA.dat')
        else:
            pass
            info.insert(tk.END,"\n\nACCOUNT DOES NOT EXIST")
        twid = int(tamt.get())
        fin=open('BDATA.dat','rb')
        fout=open('temp.dat','wb')
        try:
            while p == True:
                R=pickle.load(fin)
                if R[5] == uid and R[6] == pwd:
                    R[4] -= twid
                    pickle.dump(R,fout)
                    found=True
                else:
                    pickle.dump(R,fout)
        except EOFError:
            if found==False:
                pass
            else:
                print("Money sent to ",tname)
        fin.close()
        fout.close()
        if p == True:
            os.remove('BDATA.dat')
            os.rename('temp.dat', 'BDATA.dat')
        else:
            pass
            #info.insert(tk.END,"\n\nACCOUNT DOES NOT EXIST")
    def close_window():
        win3.destroy()
    button_dep = tk.Button(win3,text = "DEPOSIT",command = deposit)
    button_dep.grid(column = 2,row = 1)
    button_wid = tk.Button(win3,text = "WITHDRAW",command = withdraw)
    button_wid.grid(column = 2,row = 2)
    button_cb = tk.Button(win3,text = "Check Balance",command = checkbalance)
    button_cb.grid(column = 0,row = 3)
    button_rtgs = tk.Button(win3,text = "Transfer",command = transfer)
    button_rtgs.grid(column = 2,row = 7)
    button_exit = tk.Button(win3,text = "EXIT",command = close_window)
    button_exit.grid(column = 0,row = 8)
    
    win3.mainloop()
def HCS():
    hcs_info = '''Bank Of people is leading private sectorin the world the total conslidated assets stood 6.4 Billion USD as per april 2020\nand has an immense network of 45000 branches and 100000 ATMs across the world
\nContact us at: 1234567890 , 5342392\nemail : bop64@bank.com'''
    hcs_box = tk.Text(height = 10,width = 41)
    hcs_box.grid(column = 0,row = 7)
    hcs_box.insert(tk.END,hcs_info)