import webbrowser

class Video():
 	def __init__ (self, title, link):
 		self.title = title
 		self.link = link
 	
def read_video():
	title = input("Enter title: ") + "\n"
	link = input("Enter link: ") + "\n"

	video = Video(title, link)
	return video
def read_videos():
	videos = []
	total = input("How many videos: ")
	for i in range(int(total)):
		print("Video", i+1)
		video = read_video()
		videos.append(video)
	return videos

def write_video_to_txt(video, file):
	# with open("data.txt", "w") as file:
	file.write(video.title)
	file.write(video.link)
def write_videos_to_txt(videos):
	total = len(videos)
	with open("data.txt", "w") as file:
		file.write(str(total) + "\n")
		for i in range(total):
			write_video_to_txt(videos[i], file)
	
def read_video_from_txt(file):
	title = file.readline()
	link = file.readline()
	video = Video(title, link)
	return video
def read_videos_from_txt():
	videos = []
	with open("data.txt", "r") as file:
		total = file.readline()
		for i in range(int(total)):
			video = read_video_from_txt(file)
			videos.append(video)
	return videos 


def print_video(video):
	print("Title video: ", video.title, end ="")
	print("Link video: ", video.link, end ="")
def print_videos(videos):
	print("---")
	for i in range(len(videos)):
		print("Video", i+1)
		print_video(videos[i])

def select_in_range(prompt, min, max):
	choice = input(prompt)
	while not choice.isdigit() or int(choice) < min or int(choice) > max:
		choice = input(prompt)
	choice = int(choice)
	return choice

def del_a_video(videos):
	print_videos(videos)
	if videos == []:
		print("List videos empty!!!")
	else:
		choice = select_in_range("Enter video you want to delete: ",1,len(videos))
		del videos[choice-1]
		print("Delete Successfully !!!")
	
	# choice = select_in_range("Enter video you want to delete: ",1,len(videos))
	# for i in range(len(videos)):
	# 	if i == choice-1:
	# 		videos.remove(videos[i])
		
	return videos

def add_a_video(videos):
	new_title = input("Enter new title: ") + "\n"
	new_link = input("Enter new link: ") + "\n"
	new_video = Video(new_title, new_link)
	videos = videos.append(new_video)
	return videos

def play_video(videos):
	print_videos(videos)
	total = len(videos)
	choice = select_in_range("Select a video (1, " + str(total) + "): ", 1, total)
	print("Open video: " + videos[choice-1].title + " - " + videos[choice-1].link, end="")
	webbrowser.open(videos[choice-1].link)
	

def show_menu():
	print("Main menu:")
	print("--------------------------")
	print("| Option 1: Create videos |")
	print("| Option 2: Show videos   |")
	print("| Option 3: Del a video   |")
	print("| Option 4: Add a video   |")
	print("| Option 5: Play a video  |")
	print("| Option 6: Save & Exit   |")
	print("--------------------------")

