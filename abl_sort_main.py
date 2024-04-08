import tkinter as tk
from tkinter import ttk
import subprocess
#import abl_functions #for some reason this doesnt work
import os 
from abl_functions import find_folder
from abl_functions import messagebox
from abl_functions import als_files_ausgeben
from abl_functions import save_filepath
from abl_functions import eingabe
from abl_functions import new_message
from abl_functions import prog_find
	

def main():


	#das Fenster
	root = tk.Tk()
	root.title("Ableton Live Sort")
	root.configure(bg="gray16")
	root.resizable(False, False)
	root.geometry("498x680+600+100")

	#ein canvas was den frame und scrollbar hält
	canvas = tk.Canvas(root, width=420, height=410, scrollregion=(0,0,420,5300))
	canvas.pack(expand=True)
	canvas.place(relx=0.05, rely=0.33)


	#scrollbar wird erstellt
	scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
	scrollbar.place(relx =1, rely = 0.609, relheight=0.79, relwidth=0.04, anchor="e")

	#legt fest, dass das canvas die scrollbar verwendet
	canvas.configure(yscrollcommand=scrollbar.set)
	

	file_frame = tk.Frame(canvas, width=420, height=5300, bg="black", bd=2, relief="ridg")
	file_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

 
	canvas.create_window((0, 0), window=file_frame, anchor=tk.NW)

	text_box_prog = prog_find(root)

	folder_path = find_folder()

	if folder_path == 0: #keine Live Path angegeben
		message = "Enter the path to a folder! "
		text_box = messagebox(root, message, "")
	else: 
		message = "Your current folder is: "
		text_box = messagebox(root, message, folder_path)
		if os.path.exists(folder_path):
			erfolg = als_files_ausgeben(file_frame, folder_path, text_box_prog)

			if erfolg == "0": #wenn der live path keien .als enthält
				print("Keine Ableton Files im Ordner!")
				message = "The given folder does not contain Ableton Live Files."
				new_message(text_box, message, "")
		else:

			if folder_path == "": #wenn die txt datei leer ist
				message = "Enter the path to a folder! "
				new_message(text_box, message, "")
			else:
				message = "The given path does not exist. Enter an existing one!"
				new_message(text_box, message, "")

	#canvas.bind_all("<MouseWheel>", lambda event: scroll_canvas(canvas, event))
			
	entry = eingabe(root)

	txt_file = ".abl_folder_path.txt"
	srt_path = os.getcwd()
	txt_file_full = os.path.join(srt_path, txt_file)

	#save button
	save_button = tk.Button(root, text="Save new path", bd=0, relief="flat" ,command=lambda: save_filepath(entry, txt_file_full, text_box, file_frame, text_box_prog))
	save_button.place(relx=0.57, rely=0.243)
	
	#der event loop
	root.mainloop()

if __name__ == "__main__":
	main()
 