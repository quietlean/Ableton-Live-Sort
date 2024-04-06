Yo welcome to _Ableton Live Sort_. 

I made this because I thought I'd be a handy tool. There might be extensions in the future for further functionality.

You can drop the program anywhere you want on your machine.

I think the programm is pretty much self-explanatory. 

You open it and enter the path to a folder. For example `/Users/AngelaMerkel/Music/Ableton_Files`. Ideally there are **.als** files in there. If not it will let you know. 

You have to enter the Live Version you are using. For example **Ableton Live 11 Suite**. If you enter a wrong program-name the files can not be opend.

The existing Live Files will be displayed and sorted acording to the time of the last edit. The 175 most recently edited files will be displayed.

**For those who dont use the python executable:**

You need **Python3** to run the py file. The makefile uses **cmake** to compile the c file. You also need Tkinter for The GUI but it should be included in your Python3 version.

In the _Ableton_Live_Sort.c_ file you need to put the path to the directory where the .py files are in the **chdir** call. For example: `chdir("/Users/Applications/Ableton_Live_Sort")`.

You also need to enter the path of the **hide_terminal.scpt** which hides the terminal which pops up. For example `system("osascript /Users/AngelaMerkel/Scripts/hide_terminal.scpt");`

If you want to call the python file on a windows system you have to modifie **Ableton_Live_Sort.c** since its using an AppleScript.

If you find a bug or want to participate on the repository let me know 💋