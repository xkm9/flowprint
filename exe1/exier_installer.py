import os
import shutil
from rich.console import Console
from pathlib import Path

console  = Console()


def fn1():
    try:
        os.system("clear")

        message1 = """hello this is exier installer.\n\nthis file was made as a setter and assistant to help you set exier correctly , it'll collect all the python files you have in the path you are going to write and it'll copy it and put it  in one folder in home/folder, then it'll create create another folder where home/folder2 is where we going to place exier file, so you can manage these copies and lock them or edit them using exier.  please write set so the set operation can start"""
        print(message1)
        
        while True:
            console.print("\nyou can type exit to end the program: ",end="")
            v1 = input()

            if v1 == "exit":
                os.system("clear")
                break
            elif v1 == "set":
                v2 = input("write the path to your python files: ")
                print(f"current path is {os.getcwd()}")
                os.chdir(f"../{v2}")

                # copied 
                fail_check = []
                pass_check = []
                packed = os.listdir('.')
    
                raw_list = []
                for p in packed:
                    raw_list.append(p)

                for word in raw_list:
                    if word.endswith(".py"):
                        pass_check.append(word)
                    else:
                        fail_check.append(word)


                print(f"files are packed from {os.getcwd()}")
                for p in pass_check:
                    print(p)

                home = Path.home()
                os.chdir(home)
                print(f"current path is {os.getcwd()}")
                
                packed2 = os.listdir('.')
                if "source_py" in packed2:
                    pass
                else:
                    os.mkdir("source_py")

                # copy

                src_dir = v2
                dst_dir = "source_py"

                # copy only files (skip subdirectories)
                for item in shutil.os.listdir(src_dir):  # still needs to list contents
                    src_file = f"{src_dir}/{item}"
                    dst_file = f"{dst_dir}/{item}"
                    if shutil.os.path.isfile(src_file):  # ensure it's a file
                        shutil.copy2(src_file, dst_file)


                print("all files are copied now you can play exier and it'll manage these files for you.")







            else:
                console.print("error , please right set or exit.",style="red")

    except Exception as e:
        console.print(f"try error , {e}")

fn1()


def check_libs():
    print("if the code weather exier or the installer is not working please install these libs:")
    print("os\nrich\shutil\npathlib\npyfiglet")
