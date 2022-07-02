# Code buoi 2/7
import module_func


def main():
	
	while True:
		module_func.show_menu()
		choice = module_func.select_in_range("Select an option (1-7): ", 1, 7)
		if choice == 1:
			videos = module_func.read_videos()
			input("\nPress Enter to continue.\n")
		elif choice == 2:
			module_func.print_videos(videos)
			input("\nPress Enter to continue.\n")
		elif choice == 3:
			module_func.del_a_video(videos)
		elif choice == 7:
			break

main()
