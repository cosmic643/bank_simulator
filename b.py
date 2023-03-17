import tkinter as tk
import b_operations
'''-------------------------------------------------------------------------------------------'''


'''-------------------------------------------------------------------------------------------'''
window = tk.Tk()
window.geometry("500x400")
window.title("Bank of People")

label_welcome = tk.Label(text = '    Welcome to Bank of People\'s digital gateway')
label_welcome.grid(column = 0,row = 0)
label_1 = tk.Label(text = '      Use Online Banking')
label_1.grid(column = 3,row = 1)

label_2 = tk.Label(text = 'Our Other Online Services')
label_2.grid(column = 0,row = 1)

button_CNA = tk.Button(window,text = ' Create New Account ',command = b_operations.CA)
button_CNA.grid(column = 0,row = 2)
button_HCS = tk.Button(text = 'Help and Customer Services',command = b_operations.HCS)
button_HCS.grid(column = 0,row = 3)
#Online Banking
label_UID = tk.Label(text = "Enter User ID: ")
label_UID.grid(column=3,row=2)
ef_UID = tk.Entry()
ef_UID.grid(column = 3,row = 3)
label_pwd = tk.Label(text = "Enter your password: ")
label_pwd.grid(column = 3,row = 4)
ef_pwd = tk.Entry(show = "*")
ef_pwd.grid(column = 3,row = 5)
def send_data():
    print(ef_pwd.get())
    b_operations.login(ef_UID.get(),ef_pwd.get())
button_login = tk.Button(text = "Login",command = send_data)
button_login.grid(column = 3,row = 6)
def close_mainwindow():
    window.destroy()
button_exit = tk.Button(window,text = "EXIT",command = close_mainwindow)
button_exit.grid(column = 0,row = 4)
window.mainloop()