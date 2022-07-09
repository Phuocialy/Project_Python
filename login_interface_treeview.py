from tkinter import *
from tkinter import ttk
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
window2.title('Main Interface')
window2.geometry("500x800")


# Create Treeview Frame
tree_frame = Frame(window2)
tree_frame.pack(pady=20)

# Treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Create Treeview
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
# Pack to the screen
my_tree.pack()

#Configure the scrollbar
tree_scroll.config(command=my_tree.yview)

# Define Our Columns
my_tree['columns'] = ("Stt", "Video title", "Video link")

# Formate Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Stt", anchor=W, width=80)
my_tree.column("Video title", anchor=CENTER, width=140)
my_tree.column("Video link", anchor=W, width=300)

# Create Headings 
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Stt", text="Stt", anchor=W)
my_tree.heading("Video title", text="Video title", anchor=CENTER)
my_tree.heading("Video link", text="Video link", anchor=W)

# Add Data
data = [
	[1, "Hello VietNam", "https://www.youtube.com/watch?v=j9VLOXdx9VQ"],
	[2, "Relax music", "https://youtu.be/qZZm5rej9Zw"],
	[3, "One Last Time", "https://youtu.be/xf1F5Frzzbg"],
	[4, "With You", "https://youtu.be/3KadWjpqDXs"],
	[5, "Two Steps From Hell", "https://youtu.be/pICAha0nsb0"],
	[6, "Call your name", "https://youtu.be/8Gj1yuVBJiY"],
]

# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count=0

for record in data:
	if count % 2 == 0:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('evenrow',))
	else:
		my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0], record[1], record[2]), tags=('oddrow',))

	count += 1

add_frame = Frame(window2)
add_frame.pack(pady=20)

#Labels
nl = Label(add_frame, text="Stt")
nl.grid(row=0, column=0)
il = Label(add_frame, text="Video title")
il.grid(row=0, column=1)
tl = Label(add_frame, text="Video link")
tl.grid(row=0, column=2)

#Entry boxes
stt_box = Entry(add_frame)
stt_box.grid(row=1, column=0)

title_box = Entry(add_frame)
title_box.grid(row=1, column=1)

link_box = Entry(add_frame)
link_box.grid(row=1, column=2)

# Add Record
def add_video():
	my_tree.tag_configure('oddrow', background="white")
	my_tree.tag_configure('evenrow', background="lightblue")
	my_tree.insert(parent='', index='end', iid=count, text="", values=(stt_box.get(), title_box.get(), link_box.get()), tags=('evenrow',))
	# Clear the boxes
	stt_box.delete(0, END)
	title_box.delete(0, END)
	link_box.delete(0, END)

# Remove one selected
def remove_one():
	x = my_tree.selection()[0]
	my_tree.delete(x)

# Remove many selected
def play_a_video():
	pass

# Select Record
def select_record():
	# Clear entry boxes
	stt_box.delete(0, END)
	title_box.delete(0, END)
	link_box.delete(0, END)

	# Grab record number
	selected = my_tree.focus()
	# Grab record values
	values = my_tree.item(selected, 'values')
	stt_box.insert(0, values[0])
	title_box.insert(0, values[1])
	link_box.insert(0, values[2])

# Create Binding Click function
def clicker(e):
	select_record()

add_video = Button(window2, text="Add Video", command=add_video)
add_video.pack(pady=10)

# Remove One
remove_one = Button(window2, text="Remove One Video", command=remove_one)
remove_one.pack(pady=10)

# Remove Many Selected
play_a_video = Button(window2, text="Play a Video", command=play_a_video)
play_a_video.pack(pady=10)

temp_label = Label(window2, text="")
temp_label.pack(pady=20)

# Bindings
my_tree.bind("<ButtonRelease-1>", clicker)


window2.mainloop()