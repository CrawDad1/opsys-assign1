import subprocess
import shlex

def run_dir(path : str = ""):
    if path:
        print(f"Displaying [dir]ectory entries for: {path}")
    else:
        print("Displaying [dir]ectory entries for the current directory.")

    subprocess.run(args=["dir", path], shell=True)
    input("\n\nplease press enter to continue... ")

def run_cd():
    print("DIsplaying [c]urrent [d]irectory path...")
    subprocess.run(args=["cd"], shell=True)
    input("\n\nplease press enter to continue... ")

def run_mkdir(path : str = ""):
    if not path:
        print("Invalid use of mkdir. A path to the new directory must be provided.")
        input("\n\nplease press enter to continue... ")
        return

    print(f"called mkdir with arg: {path}")
    subprocess.run(args=["mkdir", path], shell=True)
    input("\n\nplease press enter to continue... ")

def run_echo(message : str = ""):
    if not message:
        print("No point using echo without a message. Please include a message.")
        input("\n\nplease press enter to continue... ")
        return

    print(f"called echo with arg: {message}")
    subprocess.run(args=["echo", message], shell=True)
    input("\n\nplease press enter to continue... ")

def run_type(path : str = ""):
    if not path:
        print("type requires a target file path. Please try again.")
        input("\n\nplease press enter to continue... ")
        return

    print(f"called type with arg: {path}")
    subprocess.run(args=["type", path], shell=True)
    input("\n\nplease press enter to continue... ")

def quit_program():
    print("Goodbye!")
    exit()

def main():
    menu_map = {
        1 : (lambda x : run_dir(x)),
        2 : (lambda x : run_cd()),
        3 : (lambda x : run_mkdir(x)),
        4 : (lambda x : run_echo(x)),
        5 : (lambda x : run_type(x)),
        0 : (lambda x : quit_program())
    }
    main_menu_text = (
        "\n\n"
        "Please Select one of the following options:\n"
        "[note: <path> refers to a windows style path eg. '.\\path\\to\\file']\n"
        "[note: <path> and <message> can include whitespace if enclosed in quotations.]\n\n"
        "(1) dir <path>: display contents of directory <path> (defaults to current directory)\n"
        "(2) cd: display current directory (or change current directory to <path>)\n"
        "(3) mkdir <path>: make new directory at <path> (check for successful creation using 'dir')\n"
        "(4) echo <message>: prints <message> to the terminal\n"
        "(5) type <path>: prints contents of text file to the terminal\n"
        "\n"
        "(0) Exit Program\n"
    )

    while True:
        print(main_menu_text)
        user_choice = input("Please enter an int from 1-5 (or 0 to exit): ")
        print(f"You have entered: {user_choice}")

        args = shlex.split(user_choice, posix=False)
        if args:
            try:
                int_choice = int(args[0])
            except ValueError as e:
                print("please try you entry again.\n")
                input("\n\nplease press enter to continue... ")
                continue

            str_choice = args[1] if len(args)>1 else ""
        else:
            print("please try you entry again.\n")
            input("\n\nplease press enter to continue... ")
            continue

        menu_map.get(int_choice, (lambda x : print(f"Invalid choice, Please try again!")))(str_choice)

if __name__ == "__main__":
    main()
