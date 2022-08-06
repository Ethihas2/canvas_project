from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("1300x900")
root.title("canvas")
root.configure(background="Orange")

label_startX = Label(root,text="start x:",bg="orange")
label_startX.place(relx=0.1,rely=0.85,anchor=CENTER)
startx_list=[10,50,100,200,300,400,500,600,800,900]
selected_var_startx = StringVar()
entry_startX = ttk.Combobox(root,values=startx_list,textvariable=selected_var_startx)
entry_startX.place(relx=0.17,rely=0.85,anchor=CENTER)

label_startY = Label(root,text="start y:",bg="orange")
label_startY.place(relx=0.3,rely=0.85,anchor=CENTER)
starty_list=[10,50,100,200,300,400,500,600,800,900]
selected_var_starty = StringVar()
entry_startY = ttk.Combobox(root,values=starty_list,textvariable=selected_var_starty)
entry_startY.place(relx=0.37,rely=0.85,anchor=CENTER)

label_oldX = Label(root,text="old x:",bg="orange")
label_oldX.place(relx=0.5,rely=0.85,anchor=CENTER)
oldX_list=[10,50,100,200,300,400,500,600,800,900]
selected_var_oldX = StringVar()
entry_oldX = ttk.Combobox(root,values=oldX_list,textvariable=selected_var_oldX)   
entry_oldX.place(relx=0.57,rely=0.85,anchor=CENTER)

label_oldY = Label(root,text="old y:",bg="orange")
label_oldY.place(relx=0.7,rely=0.85,anchor=CENTER)
oldY_list=[10,50,100,200,300,400,500,600,800,900]
selected_var_oldY = StringVar()
entry_oldY = ttk.Combobox(root,values=oldY_list,textvariable=selected_var_oldY)   
entry_oldY.place(relx=0.77,rely=0.85,anchor=CENTER)

label_color = Label(root,text="Choose Color:",bg="orange")
label_color.place(relx=0.68,rely=0.9,anchor=CENTER)
color_list=["Red","Blue","Green","Yellow","Pink","Gray","Black"]
selected_var_color = StringVar()
entry_color = ttk.Combobox(root,values=color_list,textvariable=selected_var_color,state="readonly")
entry_color.place(relx=0.77,rely=0.9,anchor=CENTER)

canvas = Canvas(root,width=1295,height=740,bg="white",highlightbackground="light gray")
canvas.pack()

root.mainloop()