# from tkinter import *
# import tkinter.messagebox as message
# import sqlite3
# # conn=sqlite3.connect('airline.db')
# # conn.commit()
# # conn.close()

# def signup():
#     fullname=entry.get()
#     position=entry.get()
#     email=entry.get()
#     password=entry.get()

#     if fullname=="" or position=="" or email=="" or password=="":
#         message.showinfo("Empty record is not allow, please fill the form properly")
#         return
#     conn=sqlite3.connect("airline.db")
#     cur=conn.cursor()
#     cur=conn.cursor()
#     cur.execute(''' CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, fullName VARCHAR (50), email VARCHAR (10), position VARCHAR(10), password VARCHAR(15))''')


#     try:
#         cur.execute(''' INSERT INTO users(FullName,position,email,password) VALUES (?,?,?,?)''',(fullname,position,email,password))
#         conn.commit()
#         message.showinfo("PROMPT","record sucessfully signup")
#         # clear_fields()
#         victor.destroy()

#     except sqlite3.integrityError:
#         message.showerror("Error", "Email already exist")
#     finally:
#         conn.close()


# victor=Tk()
# victor.geometry("500x350+500+0")
# victor.title("sign up")
# victor.config(bg="#5e546e")
# victor.resizable(0,0)

# label=Label(victor, text="Sign Up Here!", font=("sanserif",20,"bold"), fg="#fff", bg="#5e546e", underline=5)
# label.place(x=150, y=8)
# label1=Label(victor, text="fullname:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
# label1.place(x=60,y=50)
# entry=Entry(victor,width=50)
# entry.place(x=120,y=50)

# label2=Label(victor, text="position:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
# label2.place(x=50,y=80)
# entry=Entry(victor,width=50)
# entry.place(x=120,y=80)

# # label3=Label(victor, text="description:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
# # label3.place(x=80,y=150)
# # text=Text(victor,width=40,height=10)
# # text.place(x=150,y=110)

# label4=Label(victor, text="Email:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
# label4.place(x=70,y=110)
# entry=Entry(victor,width=50)
# entry.place(x=120,y=110)

# label5=Label(victor, text="password:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
# label5.place(x=55,y=140)
# entry=Entry(victor,width=50,show="*")
# entry.place(x=120,y=140)

# btn=Button(victor, text="Submit", height=2, width=25, bg="black", fg="#fff")
# btn.place(x=120,y=170)
# victor.mainloop()

from tkinter import *
import tkinter.messagebox as message
# from PIL import ImageTk,Image
# signup=Tk()
import sqlite3
import subprocess

def signup():
  fullname=entry.get()
  position=entry1.get()
  email=entry2.get()
  password=entry3.get()
  
  if fullname=="" or position=="" or email=="" or password=="":
    message.showinfo("Prompt","Empty record is not allowed, please fill the form properly")
    return
  conn=sqlite3.connect('arline.db')
  cur=conn.cursor()
  # cur=conn.cursor()
  cur.execute(''' CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,fullName VARCHAR (50), email VARCHAR (10), position VARCHAR(10), password VARCHAR (15))''')
  
  try:
    cur.execute(''' INSERT INTO users(fullNAme,position,email,password) VALUES(?,?,?,?)''',(fullname,position,email,password))
    conn.commit()
    message.showinfo("PROMPT","Record Successfully Signup")
    # clear_fields()
    victor.destroy()
    sign_in_page()
  except sqlite3.IntegrityError:
    message.showerror("Error","email already exists")
  finally:
    
    conn.close()
def sign_in_page():
  victor=Tk()
  victor.geometry("500x200+500+0")
  victor.title("Sign in")
  victor.config(bg="#5e546e")
  lbl=Label(victor, text="Sign In Here",font=("sanserif",20,"bold"), bg="#5e546e", fg="#fff")
  lbl.place(x=150, y=10)
  lbl1=Label(victor,text="userName: ", font=("sanserif",12), bg="#5e546e", fg="#fff")
  lbl1.place(x=60,y=50)
  ent1=Entry(victor, width=50)
  ent1.place(x=150,y=50)
  
  lbl2=Label(victor,text="Password: ", font=("sanserif",12), bg="#5e546e", fg="#fff")
  lbl2.place(x=60,y=80)
  ent2=Entry(victor, width=50, show="*")
  ent2.place(x=150,y=80)
  
  lbl3=Label(victor,text="Position: ", font=("sanserif",12), bg="#5e546e", fg="#fff")
  lbl3.place(x=60,y=110)
  ent3=Entry(victor, width=20, show="*")
  ent3.place(x=150,y=110)
  
  # victor.destroy()
  
  def login():
      email=ent1.get()
      password=ent2.get()
      position=ent3.get()
      
      if(email=="" or password==""):
        message.showinfo("Prompt","you are yet to fill your login details completely")
      elif(email=="d@gmail.com" or password==""):
        message.showinfo("Prompt","UNAUTHORIZED USER")
        return
      conn=sqlite3.connect('arline.db')
      cur=conn.cursor()
      cur.execute(''' select * from users WHERE email=? AND password=? ''', (email,password))
      result=cur.fetchone()
      if result:
        message.showinfo("Alert"," Login Successful")
        victor.destroy()
        if position.lower()=="admin":
          open_admin_page()
        elif position=="secretary":
          open_user_page()
        else:
          message.showinfo("Alert","UNAUTHORIZE ACCESS")
      conn.close
  def open_admin_page():
    subprocess.Popen(["python", "admin.py"])
    
  def open_user_page():
    subprocess.Popen(["python", "user.py"])
    
  
  btn=Button(victor, text="Sign-in", height=2, width=25, bg="blue", fg="#fff", command=login)
  btn.place(x=150, y=140)
  victor.mainloop()
    
  # sign_in_page()

victor=Tk()
victor.geometry("500x400+500+0")
victor.title("Sign up")
victor.config(bg="#5e546e")
victor.resizable(0,0)
# spath="images/tt.jpg"
# simg =ImageTk.PhotoImage(Image.open(spath))
# img=Label(signup, image=simg, bg="#5e546e")
# img.image=simg
# img.place(x=60, y=60)
label=Label(victor, text="Sign Up Here!", font=("sanserif",20,"bold"), fg="#fff", bg="#5e546e", underline=5)
label.place(x=150,y=10)
label1=Label(victor, text="Full Name:", font=("sanserif",8), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=100, y=50)
entry=Entry(victor, width=50)
entry.place(x=150, y=50)
label2=Label(victor, text="Position:", font=("sanserif",8), fg="#fff", bg="#5e546e", underline=5)
label2.place(x=100, y=80)
entry1=Entry(victor, width=50)
entry1.place(x=150, y=80)

# label3=Label(victor, text="Description:", font=("sanserif",8), fg="#fff", bg="#5e546e", underline=5)
# label3.place(x=90,y=110)
# text=Text(victor, width=40, height=10)
# text.place(x=150, y=110)
label4=Label(victor, text="Email:", font=("sanserif",8), fg="#fff", bg="#5e546e", underline=5)
label4.place(x=100, y=110)
entry2=Entry(victor, width=50)
entry2.place(x=150, y=110)
label5=Label(victor, text="Password:", font=("sanserif",8), fg="#fff", bg="#5e546e", underline=5)
label5.place(x=100,y=140)
entry3=Entry(victor, width=50, show="*")
entry3.place(x=150, y=140)

btn=Button(victor, text="Sign-up", height=2, width=25, bg="black", fg="#fff", command=signup)
btn.place(x=150, y=170)
lbtn=Button(victor, text="Already registered! sign-in", font=("sanserif",12), command=sign_in_page)
lbtn.place(x=150, y=200)

victor.mainloop()