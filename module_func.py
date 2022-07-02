class Video():
 	def __init__ (self, title, link):
 		self.title = title
 		self.link = link

def read_video():
	title = input("Enter title: ")
	link = input("Enter link: ")
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

def print_video(video):
	print("Title video: ", video.title)
	print("Link video: ", video.link)
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
	choice = select_in_range("Enter video you want to delete: ",1,len(videos))
	del videos[choice-1]
	# new_videos = []
	# for i in range(len(videos)):
	# 	if i == choice-1:
	# 		continue
	# 	new_videos.append(videos[i])
	# videos = new_videos
	print("xxx")
	print_videos(videos)
	print("xxx")
	print("Delete Successfully !!!")
	return videos

	

def show_menu():
	print("Main menu:")
	print("--------------------------")
	print("| Option 1: Create videos |")
	print("| Option 2: Show videos   |")
	print("| Option 3: Del a video   |")
	print("| Option 7: Exit          |")
	print("--------------------------")

