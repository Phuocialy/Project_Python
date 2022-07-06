
from tkinter import *

# Giao dien dang nhap
window1 = Tk()
window1.title("Login")


# window config
window_height = 600
window_width = 600
username = 'phuocne'
password = '123'

screen_width = window1.winfo_screenwidth() 
screen_height = window1.winfo_screenheight()
padding_top = screen_height // 2 - window_height // 2
padding_left = screen_width // 2 - window_width // 2

window1.geometry('{}x{}+{}+{}'.format(
	window_width, 
	window_height, 
	padding_left,
	padding_top))

main_frame = Frame(window1)
main_frame.place(
	relx = 0.5,
	rely = 0.5,
	anchor= CENTER
)

def login_btn_f():
	input_username = entry_user_name.get()
	input_password = entry_password.get()
	if input_username == username and input_password == password:
		lbl_message.config(text= "login successful")
		window1.destroy()
	else:
		lbl_message.config(text= "login failed")


login_frame = Frame(window1)
login_frame.place(
	relx=0.5,
	rely=0.5,
	anchor= CENTER
)

lbl_user_name = Label(login_frame, text='User name: ')
lbl_password = Label(login_frame, text='Password: ')
entry_user_name = Entry(login_frame)
entry_password = Entry(login_frame)

# ! xử lí khi nhấn nút
login_btn = Button(
	login_frame, 
	text='Login',
	command= login_btn_f
	)


lbl_message = Label(login_frame, text='')

lbl_user_name.grid(row=0, column= 0)
lbl_password.grid(row=1, column= 0)
entry_user_name.grid(row=0, column= 1)
entry_password.grid(row=1, column= 1)
login_btn.grid(row=2, column=0, columnspan=2)
lbl_message.grid(row=3, column=0, columnspan=2)

window1.mainloop()

# Giao dien chinh
window2 = Tk()
window2.title("Main")

window_height = 600
window_width = 600

screen_width = window2.winfo_screenwidth() 
screen_height = window2.winfo_screenheight()
padding_top = screen_height // 2 - window_height // 2
padding_left = screen_width // 2 - window_width // 2

window2.geometry('{}x{}+{}+{}'.format(
	window_width, 
	window_height, 
	padding_left,
	padding_top))

def add_video():
	Lb.insert(END, entry.get())
	entry.delete(0, END)
	Lb.insert(END, entry2.get())
	entry2.delete(0, END)
def remove_video():
	Lb.delete(Lb.curselection())
def play_video():
	pass

Lb = Listbox(window2)
lb = Frame(master=window2, height=80)
Lb.pack(fill=X)

lbl_video_title = Label(window2, text="Video title: ")
lbl_video_title.pack()
entry = Entry(window2)
entry.pack()

lbl_video_link = Label(window2, text="Video link: ")
lbl_video_link.pack()
entry2 = Entry(window2)
entry2.pack()


button = Button(window2, text="Add video", command=add_video)
button.pack()
button = Button(window2, text="Remove video", command=remove_video)
button.pack()
button = Button(window2, text="Play video", command=play_video)
button.pack()

# with open("data.txt", "r") as f:
# 	for x in f:
# 	    Lb.insert(END,x)
# 	    print(x)

window2.mainloop()