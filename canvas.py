from tkinter import *

root = Tk()
root.geometry("1300x900")
root.title("canvas")
root.configure(background="Orange")

label_startX = Label(root,text="start x:",bg="orange")
label_startX.place(relx=0.1,rely=0.85,anchor=CENTER)
entry_startX = Entry(root)
entry_startX.place(relx=0.17,rely=0.85,anchor=CENTER)

label_startY = Label(root,text="start y:",bg="orange")
label_startY.place(relx=0.3,rely=0.85,anchor=CENTER)
entry_startY = Entry(root)
entry_startY.place(relx=0.37,rely=0.85,anchor=CENTER)

label_oldX = Label(root,text="old x:",bg="orange")
label_oldX.place(relx=0.5,rely=0.85,anchor=CENTER)
entry_oldX = Entry(root)
entry_oldX.place(relx=0.57,rely=0.85,anchor=CENTER)

label_oldY = Label(root,text="old y:",bg="orange")
label_oldY.place(relx=0.7,rely=0.85,anchor=CENTER)
entry_oldY = Entry(root)
entry_oldY.place(relx=0.77,rely=0.85,anchor=CENTER)

label_color = Label(root,text="Choose Color:",bg="orange")
label_color.place(relx=0.68,rely=0.9,anchor=CENTER)
entry_color = Entry(root)
entry_color.place(relx=0.77,rely=0.9,anchor=CENTER)

canvas = Canvas(root,width=1295,height=740,bg="white",highlightbackground="light gray")
canvas.pack()

root.mainloop()