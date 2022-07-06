# Code buoi 2/7
import module_func

def main():

	try:
		videos = module_func.read_videos_from_txt()
		print("---")
		print("Load data successfully!!!")
	except:
		print("---")
		print("Welcome first user!!!")
	while True:
		print("---")
		module_func.show_menu()
		choice = module_func.select_in_range("Select an option (1-6): ", 1, 6)
		if choice == 1:
			videos = module_func.read_videos()
			module_func.write_videos_to_txt(videos)

			input("\nPress Enter to continue.\n")
		elif choice == 2:
			videos = module_func.read_videos_from_txt()
			module_func.print_videos(videos)
			input("\nPress Enter to continue.\n")
		elif choice == 3:
			module_func.del_a_video(videos)
			module_func.write_videos_to_txt(videos)
			input("\nPress Enter to continue.\n")
		elif choice == 4:
			module_func.add_a_video(videos)
			module_func.write_videos_to_txt(videos)
			print("Add video successfully")
			input("\nPress Enter to continue.\n")
		elif choice == 5:
			module_func.play_video(videos)
			input("\nPress Enter to continue.\n")
		elif choice == 6:
			module_func.write_videos_to_txt(videos)
			break

main()
