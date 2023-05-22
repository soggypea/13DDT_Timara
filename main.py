from tkinter import *
from tkinter import messagebox


root=Tk()
root.title('login') 
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()
#entering the app
    if username=='admin' and password=='123':
       screen=Toplevel(root)
       screen.title("App")
       screen.geometry('950x500+300+200')
       screen.config(bg="white")
       #hello everyone not printing
       Label(screen,text='Hello Everyone!',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)


       screen.mainloop()
#if username and password are wrong
    elif username!='admin'and password!='123':
        messagebox.showerror("Invalid","Invalid username and password")

    elif password!='123': 
        messagebox.showerror("Invalid","Invalid password")

    elif username!='admin': 
        messagebox.showerror("Invalid","Invalid username")
 

#PICTURE not working 
img = PhotoImage(file="/Users/timaradukkan/Documents/Speed Typing Test/Pictures/login People.png")
Label(root,image=img,bg='white').place(x=40,y=48)

#frame for background
frame=Frame(root,width=350,height=350,bg="white") 
frame.place(x=480,y=70)

#Sign name 
heading=Label (frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light', 23, 'bold')) 
heading.place(x=100,y=5)

#username 
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user = Entry(frame,width=25, fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light', 11))
user.place (x=30, y=80)
user. insert(0, 'Username') 
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>',on_leave)

#underline username
Frame(frame,width=295, height=2,bg='black').place(x=25,y=107)

#password
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code = Entry(frame,width=25, fg='black',border=0,bg="white",font=('Microsoft Yahei UI Light', 11))
code.place (x=30, y=150)
code. insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>',on_leave) 
#underline for password
Frame(frame,width=295, height=2,bg='black').place(x=25,y=177)

#colour of sign in button not turning blue(#5386c2) colour
Button(frame,width=25,pady=7,text='Sign in',bg='#5386c2',fg='#5386c2',border=0,command=signin ).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='Black',bg='white',font=('Microsoft Yahei UI Light', 9))
label.place(x=75,y=270)

#Button to sign up
sign_up= Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=215,y=270)

root.mainloop()