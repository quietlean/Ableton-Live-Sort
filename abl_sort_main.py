import tkinter as tk
import subprocess
#import abl_functions #for some reason this doesnt work
import os 
from abl_functions import find_folder
from abl_functions import messagebox
from abl_functions import als_files_ausgeben
from abl_functions import save_filepath
from abl_functions import eingabe
from abl_functions import new_message
		

	

def main():

	txt_file = "/Users/lengather/Library/Mobile Documents/com~apple~CloudDocs/Code/Ableton Sort/folder_path.txt"

	#das Fenster
	root = tk.Tk()
	root.title("Ableton Live Sort")
	root.configure(bg="gray16")
	root.resizable(False, False)
	root.geometry("498x600")

	file_frame = tk.Frame(root, width=300, height=350, bg="black", bd=2, relief="ridg")
	file_frame.grid(row=15, column=0, pady=40, padx="50", sticky="nsew")
	file_frame.grid_propagate(0)#sorgt dafür, dass sich der frame nicht an die größte des Inhalts anpasst
	#file_frame.grid_rowconfigure(0, weight=1) #Die sorgen dafür, dass der frame in die rows und columns expandieren kann
	#file_frame.grid_columnconfigure(0, weight=1)


	folder_path = find_folder(txt_file)

	if folder_path == "0": #keine Live Path angegeben
		message = "Enter the path to a folder! "
		text_box = messagebox(root, message, "", "1")
	else: 
		message = "Your current folder is: "
		text_box = messagebox(root, message, folder_path, "1")
		if os.path.exists(folder_path):
			erfolg = als_files_ausgeben(file_frame, folder_path)

			if erfolg == "0": #wenn der live path keien .als enthält
				print("Keine Ableton Files im Ordner!")
				message = "The given folder does not contain Ableton Live Files."
				new_message(text_box, message, "")
		else:
			message = "The given path does not exist. Enter an existing one!"
			new_message(text_box, message, "")


			
	entry = eingabe(root)

	#save button
	save_button = tk.Button(root, text="Save", bg="blue", bd=0, relief="flat" ,command=lambda: save_filepath(entry, txt_file, text_box, file_frame))
	save_button.grid(row=11, column=0, pady=2)
	
	
	#der event loop
	root.mainloop()

if __name__ == "__main__":
	main()
 