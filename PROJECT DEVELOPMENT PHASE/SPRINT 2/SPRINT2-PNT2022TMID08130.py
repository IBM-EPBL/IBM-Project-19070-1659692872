from tkinter import*
import os

def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
    
def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("success")
    screen3.geometry("150x100")
    Label(screen3,text ="login success").pack()
    Button(screen3,text = "ok",command = delete2)

    
def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("success")
    screen4.geometry("150x100")
    Label(screen4,text ="password error").pack()
    Button(screen4,text = "ok",command = delete3)
    
def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("success")
    screen5.geometry("150x100")
    Label(screen5,text ="user not found ").pack()
    Button(screen5,text = "ok",command = delete4)
     
def register_user():
    print("working")
    
    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text = "Registration success",fg ="green",font =("calibri",11)).pack()


def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)


    list_of_files = os.listdir()
    if username1 == list_of_files:
        file1 = open(username1,"r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            pasword_not_recognised()
    else:
        user_not_found() 
            
            
    
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username =StringVar()
    password =StringVar()
    
    Label(screen1 ,text ="Please enter the details below ").pack()
    Label(screen1, text = "").pack()
    Label(screen1 ,text ="Username * ").pack()
    global username_entry
    global password_entry
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text ="Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text ="").pack()
    Button(screen1,text = "register",width =10,height=1,command = register_user).pack()
    
    
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("login")
    screen2.geometry("300x250")
    Label(screen2 ,text ="Please enter the details below to login ").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    
    username_verify =StringVar()
    password_verify =StringVar()

    global username_entry1
    global password_entry1
    
    Label(screen2 ,text ="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text ="").pack()
    Label(screen2, text ="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2 ,text = "Login",width =10,height=1,command = login_verify).pack()

     
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text=" Notes 1.0",bg="grey",width ="300",height ="3",font =("calibri",14)).pack()
    Label(text ="").pack()
    Button(text ="login",height="2",width="30",command = login).pack()
    Label(text="").pack()
    Button(text ="register",height="2",width="30",comman = register).pack()

    screen.mainloop()
    
main_screen()
