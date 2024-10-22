from tkinter import *
from PIL import ImageTk,Image
import sqlite3
import tkinter.messagebox as message
from gtts import gTTS
import pygame
import os
conn=sqlite3.connect("arline.db")
cur=conn.cursor()
# flights
cur.execute(''' CREATE TABLE IF NOT EXISTS flights(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  flight_number VARCHAR NOT NULL,
  origin VARCHAR NOT NULL,
  destination VARCHAR NOT NULL,
  departure_time VARCHAR NOT NULL,
  arrival_time VARCHAR NOT NULL
  
)''')
# passengers
cur.execute(''' CREATE TABLE IF NOT EXISTS passengers(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR NOT NULL,
  gender VARCHAR NOT NULL,
  age VARCHAR NOT NULL,
  passport_number VARCHAR NOT NULL,
  contact VARCHAR NOT NULL
  
)''')
# bookings
cur.execute(''' CREATE TABLE IF NOT EXISTS bookings(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  passenger_id INTEGER NOT NULL,
  flight_id INTEGER NOT NULL,
  age VARCHAR NOT NULL,
  seat_number VARCHAR NOT NULL,
  FOREIGN KEY(passenger_id) REFERENCES passengers(id),
  FOREIGN KEY(flight_id) REFERENCES flights(id)
  
  
)''')

def text_to_speech(text):
  tts=gTTS(text=text, lang='en')
  audio_file="flight_info.mp3"
  tts.save(audio_file)
  
  pygame.mixer.init()
  pygame.mixer.music.load(audio_file)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    continue
  pygame.mixer.quit()
  os.remove(audio_file)

# def save_passanger():
#   name=ent.get()
#   age=ent1.get()
#   gender=ent2.get()
#   passport_number=ent3.get()
#   contact_info=ent4.get()
#   if name=="" or age=="" or gender=="" or passport_number=="" or contact_info=="":
#     message.showinfo("Alert", "please fill all the field")
#     return
#   conn=sqlite3.connect("airline.db")
#   conn=conn.cursor()
#   cur.execute('''SELECT COUNT(*) FROM passengers WHERE passport_number=?''', (passport_number,))
#   exists = cur.fetchone()[0]
#   if exists:
#     message.showinfo("Error","A passenger with this passport number already exists!")
#   else:
#     cur.execute('''INSERT INTO passengers(name, age, gender, passport_number, contact) VALUES(?, ?, ?, ?, ?)''', (name, age, gender, passport_number, contact_info)) 
#     conn.commit()
#     message.showinfo("success","passenger information successfully submited!")
#     ent.delete(0,END)
#     age.delete(0,END)
#     gender.delete(0,END)
#     passport_number.delete(0,END)
#     contact_info.delete(0,END)
# conn.close()

def save_passanger():
    name = ent.get()
    age = ent1.get()
    gender = ent2.get()
    passport_number = ent3.get()
    contact_info = ent4.get()
    
    if name == "" or age == "" or gender == "" or passport_number == "" or contact_info == "":
        message.showinfo("Alert", "Please fill all the fields")
        return
    
    # Correct database name
    conn = sqlite3.connect("arline.db")
    cur = conn.cursor()
    
    cur.execute('''SELECT COUNT(*) FROM passengers WHERE passport_number=?''', (passport_number,))
    exists = cur.fetchone()[0]
    
    if exists:
        message.showinfo("Error", "A passenger with this passport number already exists!")
    else:
        cur.execute('''INSERT INTO passengers(name, age, gender, passport_number, contact) VALUES(?, ?, ?, ?, ?)''', 
                    (name, age, gender, passport_number, contact_info)) 
        conn.commit()
        message.showinfo("Success", "Passenger information successfully submitted!")
        
        # Correctly clear the entry fields
        ent.delete(0, END)
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)
    
    conn.close()


user=Tk()
user.config(bg="#5e546e")
user.geometry("1000x1000+200+0")
user.title("user Dashboard")
user.resizable(0,0)
spath="images/tt.jpg"
simg = ImageTk.PhotoImage(Image.open(spath))
img=Label(user, image=simg, bg="#5e546e" )
img.image=simg
img.place(x=0, y=0)

ibl=Label(user, text="user Area", font=("sanseri",50,"bold"), bg="#5e546e", fg="#fff", underline=6)
ibl.place(x=300, y=0)

label1=Label(user, text="passenger name:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=220,y=100)
ent=Entry(user,width=50)
ent.place(x=340,y=100)

label1=Label(user, text="Age:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=220,y=130)
ent1=Entry(user,width=20)
ent1.place(x=340,y=130)

label1=Label(user, text="Gender:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=220,y=160)
ent2=Entry(user,width=20)
ent2.place(x=340,y=160)

label1=Label(user, text="Passport number:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=220,y=190)
ent3=Entry(user,width=50)
ent3.place(x=340,y=190)

label1=Label(user, text="Contact info:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=220,y=220)
ent4=Entry(user,width=50)
ent4.place(x=340,y=220)

label1=Label(user, text="Flight id:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=220,y=250)
ent6=Entry(user,width=50)
ent6.place(x=340,y=250)

label1=Label(user, text="Passenger id:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=220,y=280)
ent5=Entry(user,width=50)
ent5.place(x=340,y=280)

btnsave=Button(user, text="save flight", height=2, width=20, bg="black", fg="#fff", command=save_passanger)
btnsave.place(x=340, y=310)
btns=Button(user, text="book flight", height=2, width=20, bg="red", fg="#fff", )
btns.place(x=500, y=310)
user.mainloop()