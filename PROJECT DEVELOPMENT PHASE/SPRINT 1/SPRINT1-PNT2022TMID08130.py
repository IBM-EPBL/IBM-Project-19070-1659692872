from tkinter import*


def register_user():
    username_info = username.get()
    password_info = password.get()

    file=open(username_info+".txt", "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1,text = "Registration success",fg ="green",font =("calibri",11)).pack()
    
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
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text ="Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text ="").pack()
    Button(screen1,text = "register",width =10,height=1,command = register_user).pack()
    Button(screen1,text = "password",width =10,height=1)
    
def login():
    print("login session started")
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text=" Notes 1.0",bg="grey",width ="300",height ="3",font =("calibri",14)).pack()
    Label(text ="").pack()
    Button(text ="login",height="2",width="30").pack()
    Label(text="").pack()
    Button(text ="register",height="2",width="30",comman = register).pack()

    screen.mainloop()
    
main_screen()
