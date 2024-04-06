#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main() {

    //const char* command = "python3 abl_sort_main.py > /dev/null 2>&1";
    //FILE *null_output = freopen("/dev/null", "w", stdout);
    //FILE *null_error = freopen("/dev/null", "w", stderr);
	
	//printf("\n");
    chdir("/Users/lengather/Library/Mobile Documents/com~apple~CloudDocs/Code/Ableton Sort"); //Put the path where path to the directoy where the .py files are in there
    //system("pwd");
   //printf("\n");

    system("osascript /Users/lengather/Scripts/hide_terminal.scpt");
    system("python3 abl_sort_main.py"); //python3 abl_sort_main.py
    //system("xdotool search --onlyvisible --class Terminal windowmap");

    //fclose(null_output);
    //fclose(null_error);    
    return 0;
}
