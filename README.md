# Shell_menu.py
This program is a submission for programming assignment 1 of Operating Systems. 

The purpose of this script is to provide the user with a basic description of a few basic windows style shell commands, as well as allow the user to execute those commands from a main menu. 

## how to run
ensure that run_shell_menu.bat and shell_menu.py are in the same directory, and simply double click on run_shell_menu.bat. This wil launch a new shell instance running the script. 

### Didn't work?
If running run_shell_menu.bat did not work properly, please ensure your system meets these requirements:
- windows 10 or better
- 'python' is in your PATH
- your version of python supports the 'subprocess' and 'shlex' libraries


## Menu
The following is the menu presented when running the script.

- Please Select one of the following options:
- [note: <path> refers to a windows style path eg. '.\\path\\to\\file']
- [note: <path> and <message> can include whitespace if enclosed in quotations.]
- (1) dir <path>: display contents of directory <path> (defaults to current directory)
- (2) cd: display current directory (or change current directory to <path>)
- (3) mkdir <path>: make new directory at <path> (check for successful creation using 'dir')
- (4) echo <message>: prints <message> to the terminal
    - <message> can include spaces if you use quotations
- (5) type <path>: prints contents of text file to the terminal
- (0) Exit Program

