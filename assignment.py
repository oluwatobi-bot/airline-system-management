# from tkinter import *
# import tkinter.messagebox as message
# import sqlite3

# def signin():
#     email = entry.get()
#     Password = entry1.get()

#     if email == "" or Password == "":
#         message.showinfo("Prompt", "Empty record is not allowed, please fill the form properly")
#         return
    
#     conn = sqlite3.connect('airline.db')
#     cur = conn.cursor()
#     cur.execute(''' CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, email VARCHAR(100), password VARCHAR(15))''')
#     conn.commit()
    
#     try:
#         cur.execute(''' INSERT INTO users( email, password) VALUES(?,?)''', ( email, Password))
#         conn.commit()
#         message.showinfo("Prompt", "Record successfully signed up")
#         victor.destroy()

#     except sqlite3.IntegrityError:
#         message.showerror("Error", "Email already exists")
#     except Exception as e:
#         message.showerror("Error", f"An unexpected error occurred: {e}")
#     finally:
#         conn.close()

# victor = Tk()
# victor.geometry("500x300+500+0")
# victor.title("Sign in")
# victor.config(bg="#5e546e")
# victor.resizable(0, 0)

# label=Label(victor, text="Sign in Here!", font=("sanserif", 20, "bold"), fg="#fff", bg="#5e546e", underline=5)
# label.place(x=150, y=10)


# label=Label(victor, text="email:", font=("sanserif", 8, "bold"), fg="#fff", bg="#5e546e", underline=5)
# label.place(x=40, y=60)
# entry=Entry(victor, width=50)
# entry.place(x=120, y=60)

# label1=Label(victor, text="password:", font=("sanserif", 8, "bold"), fg="#fff", bg="#5e546e", underline=5)
# label1.place(x=40, y=90)
# entry1=Entry(victor, width=50, show="*")
# entry1.place(x=120, y=90)

# btn=Button(victor, text="Sign-in", height=2, width=25, bg="black", fg="#fff", command=signin)
# btn.place(x=170, y=120)

# victor.mainloop()

