from tkinter import *
from PIL import ImageTk,Image
admin=Tk()
admin.config(bg="#5e546e")
admin.geometry("800x800+200+0")
admin.title("Admin Dashboard")
admin.resizable(0,0)
spath="images/ti.jpg"
simg = ImageTk.PhotoImage(Image.open(spath))
img=Label(admin, image=simg, bg="#5e546e" )
img.image=simg
img.place(x=60, y=60)

ibl=Label(admin, text="Admin Area", font=("sanseri",50,"bold"), bg="#5e546e", fg="#fff", underline=6)
ibl.place(x=300, y=0)

label1=Label(admin, text="fullname:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=60,y=100)
entry=Entry(admin,width=50)
entry.place(x=120,y=100)

label1=Label(admin, text="fullname:", font=("sanserif",8,"bold"), fg="#fff", bg="#5e546e", underline=5)
label1.place(x=60,y=150)
entry=Entry(admin,width=50)
entry.place(x=120,y=150)
admin.mainloop()