#Funktionen
import tkinter as tk
import os
import subprocess


def open_live(file_path, text_box):

	print("+ ")
	print(file_path)

	with open(new_prog_path, 'r') as file:
		program = file.readline().strip()


	try:
		subprocess.run(["open", "-a", program, file_path])
	except FileNotFoundError:
		print("+ 0")
	except subprocess.CalledProcessError:
		print("The File couldnt be opend")
		message = "Live files can not be opend with the given program. Enter a valid program-name!"
		new_prog_message(text_box, message, "")

	#print("+ programm öffnen ende")

def old_find_folder(path):
	try: 
		with open(path, 'r') as file:
			first_line = file.readline().strip()
			if first_line.startswith("/"):
				return first_line
			else:
				#print("nothing found")
				return "0"

	except FileNotFoundError:
		#print("txt file not found")
  		pass

def find_folder():

	txt_file = ".abl_folder_path.txt"
	srt_path = os.getcwd()
	#srt_path_only = os.path.dirname(srt_path)
	txt_file_full = os.path.join(srt_path, txt_file)

	if os.path.exists(txt_file_full):
		#print("+ txt path exists")
		#print(txt_file_full)
		pass
	else:

		#print("+ txt file dosnt exist")
		
		with open(txt_file_full, 'w') as file:
			#file.write("created")
			pass

		return 0
	
	try: 
		with open(txt_file_full, 'r') as file:
			first_line = file.readline().strip()
			return first_line

	except FileNotFoundError:
		print("txt file not found")
		return ""




def save_filepath(entry, txt_file, txt_box, frame, text_box_prog):
	file_path = entry.get()
	if file_path.strip() == "":
		#print("enter proper Path")
		return

	with open(txt_file, 'w') as file:
		file.write(file_path)

	for widget in frame.winfo_children(): #destroying existing buttons of old folder files
		if isinstance(widget, tk.Button):
			widget.destroy()
	
	if os.path.exists(file_path):
		message = "Your current folder is: "
		#print(message)
		
		new_message(txt_box, message, file_path)

		for widget in frame.winfo_children():
			if isinstance(widget, tk.Button):
				widget.destroy()

		als_files_ausgeben(frame, file_path, text_box_prog)
	else:
		message = "The given path does not exist. Enter an existing one!"
		new_message(txt_box, message, "")
	

	#leert das Eingabefeld
	entry.delete(0, tk.END)

def messagebox(root, message, folder_path):

	text_box = tk.Text(root, wrap=tk.WORD, height=3, width=70, bg="black", fg="olivedrab1") #orchid1
	text_box.insert(tk.END, message + folder_path)
	text_box.place(relx=0, rely=0.15)

	return text_box

def new_message(text_box, message, folder_path):
	text_box.delete("1.0", tk.END)
	text_box.insert(tk.END, message + folder_path)


def eingabe(root):
	#Label für das eingabefeld wird erstellt
	#label = tk.Label(root, text="Enter the Path to a Folder:")
	#label.place(relx=0.3, rely=0.1)
	#label.grid(row=9, pady=2)

	#erstellt das eingabefeld
	entry = tk.Entry(root, width=25)
	entry.place(relx=0.05, rely=0.24)
	#entry.grid(row=10, column=0, pady=5)

	return entry

def als_files_ausgeben(frame, folder_path, text_box):
	count = 0
	ableton_files = []
	exclude = "Backup"
	for root, dirs, files in os.walk(folder_path):
		#print(files)
		#if exclude in dirs:
			#print(dirs)
			#dirs.remove(exclude) #So wird backup ordner nicht berücksichtigt
			#continue
		for file in files:
			if file.endswith(".als"):
				file_path = os.path.join(root, file) #Damit wird der File path und der name der .als datei zusammengefügt. Dadurch hat man gesammten Path der File
				modified_time = os.path.getmtime(file_path)
				ableton_files.append((file_path, modified_time))
				count = count + 1

			if count == 10000:
				break
		
		if count == 10000:
			break

	#for file in os.listdir(folder_path):
	#	if file.endswith(".als"):
	#		file_path = os.path.join(folder_path, file) #Damit wird der File path und der name der .als datei zusammengefügt. Dadurch hat man gesammten Path der File
	#		modified_time = os.path.getmtime(file_path)
	#		ableton_files.append((file, modified_time)) # packt die modifizierte zeit ans ende der Liste ((File, Time) (File, Time) (File, Time) ...) Man hat Tuples in der Liste. Die tuppel entstehn durch das append

	if len(ableton_files) == 0:
		return "0"

	ableton_files.sort(key=lambda x: x[1], reverse=True) # die Liste wird sortiert

	count2 = 0
	count = 0
	for file, _ in ableton_files:

		file_name = os.path.basename(file)
		 
		y_pos = 20 + count

		#create_buttons(frame, file, filename)
		#print(file)
		button = tk.Button(frame, text=file_name, bd=0, relief="flat" ,command= lambda f=file: open_live(f, text_box)) #nicht nötig: os.path.join(folder_path, file)
		

		button.place(x=200, y=y_pos, anchor="center")
		count = count + 30
		count2 = count2 + 1

		if count2 == 175:
			
			#print(files)
			#print(len(files))
			break

def prog_find(root):

	filename = ".abl_prog.txt"
	srt_path = os.getcwd()

	file_path = os.path.join(srt_path, filename)

	global new_prog_path #da wird der neue programname gespeichert
	new_prog_path = file_path 
	
	if os.path.exists(file_path):
		#print("+ path exists")
		pass
	else:

		#print("+ file dosnt exist")
		
		with open(file_path, 'w') as file:
			file.write("created")

	with open(file_path, 'r') as file:
		first_line = file.readline().strip()
		
		if first_line == "created":
			message = "Enter the name of the Live Version you want to use!"
			text_box = prog_message(root, message, "")
			programm = ""
			#return "0"
		else:
			message = "Your stated program is: "
			text_box = prog_message(root, message, first_line)
			program = first_line
			#return first_line
		
	

	entry = tk.Entry(root, width=25)
	entry.place(relx=0.05, rely=0.087)

	save_button = tk.Button(root, text="Save new program", bd=0, relief="flat" ,command=lambda: save_program(entry, file_path, text_box))
	save_button.place(relx=0.57, rely=0.09)

	return text_box


def prog_message(root, message, program):

	text_box = tk.Text(root, wrap=tk.WORD, height=3, width=70, bg="black", fg="olivedrab1")
	text_box.insert(tk.END, message + program)
	text_box.place(relx=0, rely=0)	

	return text_box

def new_prog_message(text_box, message, program):
	text_box.delete("1.0", tk.END)
	text_box.insert(tk.END, message + program)

def save_program(entry, path, text_box):

	#print("+ saving program")

	program = entry.get()

	with open(path, 'w') as file:
		file.write(program)

	entry.delete(0, tk.END)

	message = "Your stated program is: "
	new_prog_message(text_box, message, program)

	
