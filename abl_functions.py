#Funktionen
import tkinter as tk
import os
import subprocess


def open_live(file_path):
	try:
		subprocess.run(["open", "-a", "Ableton Live 11 Suite", file_path])
	except FileNotFoundError:
		print("Ableton Live wasnt found")
	except subprocess.CalledProcessError:
		print("The File couldnt be opend")

def find_folder(path):
	try: 
		with open(path, 'r') as file:
			first_line = file.readline().strip()
			if first_line.startswith("/"):
				return first_line
			else:
				print("nothing found")
				return "0"

	except FileNotFoundError:
		print("txt file not found")

def save_filepath(entry, txt_file, txt_box, frame):
	file_path = entry.get()
	if file_path.strip() == "":
		print("enter proper Path")
		return

	with open(txt_file, 'w') as file:
		file.write(file_path)

	for widget in frame.winfo_children():
		if isinstance(widget, tk.Button):
			widget.destroy()
	
	if os.path.exists(file_path):
		message = "Your current folder is: "
		#print(message)
		
		new_message(txt_box, message, file_path)

		for widget in frame.winfo_children():
			if isinstance(widget, tk.Button):
				widget.destroy()

		als_files_ausgeben(frame, file_path)
	else:
		message = "The given path does not exist. Enter an existing one!"
		new_message(txt_box, message, "")
	

	#leert das Eingabefeld
	entry.delete(0, tk.END)

	#den Cursor deaktivieren
	#entry.configure(state='readonly')

def messagebox(root, message, folder_path, choice):

	if choice == "1": #neues textfeld erschaffen
		text_box = tk.Text(root, wrap=tk.WORD, height=3, width=70, bg="black", fg="orchid1")
		text_box.insert(tk.END, message + folder_path)
		text_box.grid(row=1, column=0, pady=1)

	return text_box

def new_message(text_box, message, folder_path):
	text_box.delete("1.0", tk.END)
	text_box.insert(tk.END, message + folder_path)


def eingabe(root):
	#Label für das eingabefeld wird erstellt
	label = tk.Label(root, text="Enter the Path to a Folder:")
	label.grid(row=9, pady=2)

	#erstellt das eingabefeld
	entry = tk.Entry(root, width=35)
	entry.grid(row=10, pady=5)

	return entry

def als_files_ausgeben(frame, folder_path):
	ableton_files = []

	for file in os.listdir(folder_path):
		if file.endswith(".als"):
			file_path = os.path.join(folder_path, file) #Damit wird der File path und der name der .als datei zusammengefügt. Dadurch hat man gesammten Path der File
			modified_time = os.path.getmtime(file_path)
			ableton_files.append((file, modified_time)) # packt die modifizierte zeit ans ende der Liste ((File, Time) (File, Time) (File, Time) ...) Man hat Tuples in der Liste. Die tuppel entstehn durch das append

	if len(ableton_files) == 0:
		return "0"

	ableton_files.sort(key=lambda x: x[1], reverse=True) # die Liste wird sortiert

	count = 0
	for file, _ in ableton_files:
		button = tk.Button(frame, text=file, bd=0, relief="flat", bg="blue" ,command= lambda f=file: open_live(os.path.join(folder_path, file)))
		
		
		y_pos = 20 + count
		#button.grid(row=row_pos, column=1, pady=1, sticky="nsew")
		#button.grid_rowconfigure(0, weight=1) #Die sorgen dafür, dass der frame in die rows und columns expandieren kann
		#button.grid_columnconfigure(0, weight=1)
		#Man könnte Grid verwenden, wenn man das Fenster so haben will, dass es sich vertikal an die Menge der Buttons, also der Files, anpasst.

		button.place(x=200, y=y_pos, anchor="center")
		count = count + 30