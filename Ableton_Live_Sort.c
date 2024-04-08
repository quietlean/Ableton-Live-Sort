#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

int main() {
	
	//printf("\n");
    chdir("/Applications/LiveSort"); //Put the path where path to the directoy where the .py files are in there
    //system("pwd");
   //printf("\n");

    system("osascript /Applications/LiveSort/hide_terminal.scpt");
    system("python3 abl_sort_main.py"); //python3 abl_sort_main.py
 
    return 0;
}
