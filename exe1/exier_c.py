import random
import sys
import os
# main path
main = os.getcwd()
# interface tools
import pyfiglet
from rich.console import Console
c = Console()
###################################
columns = os.get_terminal_size().columns
# delete the path afater the period
os.system("rm -rf new")
# then clear the screen
os.system("clear")
#  create a path and set it
raw = r"../new/path/sandbox"
os.makedirs(raw)
os.chdir(raw)


raw_prompt = []
sandbox_commands = ["q: quit","path: shows current path"]


print("\n")
l1 = pyfiglet.figlet_format("EXIER",font="cyberlarge")
c.print(f"{l1}",style="color(7)")
print("\n")
c.print("            python sandbox player ©",style="bold")
c.print("v1.0.0 alpha",style="bold")
print(f"-"* columns)
print(f"current path: {os.getcwd()}")

code = []
while True:

    prompt = []


    print("\n\n\n")
    print("1. sandbox commands")
    print("2. key generator")
    print("3. play a file")
    print("4. list files")
    print("5. mod files")
    print("6. about exier")


    print("\nenter your prompt: ",end="")
    i1 = input()
    print(f"-"* columns)
    prompt.append(i1)
    raw_prompt.append(i1)
    v1 = prompt[-1]

    # if conditions section
    if v1 == "q":
        print("closing sandbox...")
        os.chdir("../../../")
        os.system("rm -rf new && clear")
        os.chdir("exe1")
        print(f'current path is {os.getcwd()}')
        break

    elif v1 == "path":
        print(f"\ncurrent path is : {os.getcwd()}\n")

    elif v1 == "sandbox commands" or v1 == "1":
        for s in sandbox_commands:
            c.print(s,style="yellow")

    elif v1 == "list files" or v1 == "4":

        fail_check = []
        pass_check = []

        os.chdir(r"../../../source_py")
        packed = os.listdir('.')
    
        raw_list = []
        for p in packed:
            raw_list.append(p)

        for word in raw_list:
            if word.endswith(".py"):
                pass_check.append(word)
            else:
                fail_check.append(word)

        print("files packed from path: home/localtwin/da1")
        print("python files: ")
        for p in pass_check:
            print(f" {p}")

        print("\nother files: ")
        for f in fail_check:
            print(f" {f}")

        c.print("\nyou can write copy it will copy them to new/path/sandbox",style="underline")
        # back to sandbox path
        os.chdir(raw)
        ################################################

    elif v1 == "key generator" or v1 == "2":
        os.chdir("../../../source_py")
        print(f"current direction is {os.getcwd()}")


        key = []

        v2 = "abcdefghijklmnopqrstuvwxyz"
        v3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        v4 = "!@#$%&*"
        v5 = "1234567890"

        lv2 = list(v2)
        lv3 = list(v3)
        lv4 = list(v4)
        lv5 = list(v5)

        def mix():
            target = []
            target.extend(lv2)
            target.extend(lv3)
            target.extend(lv4)
            target.extend(lv5)

            layer1 = []
            layer1.append(random.sample(target, k=15))

            for l in layer1:
                join =''.join(l)

            code.append(join)
        mix()

        code = code[0]

        li =f"""
empty = []
def key_check():
    l1 = ['{code}']
    empty.append(l1[0])
    print('enter the key: ',end='')
    i1 = input()
    if i1 in l1:
        print('key accepted, code successfully passed')
        return True
    else:
        print("error try another key")
        return False

            """
        li2 = f"""

if __name__ == '__main__':
    while True:
        if key_check():
            break

    def value():
        return empty[0]
#########################
    """


        li1 = input("enter file name: ")
        with open(li1,"r") as test2:
            cv1 = test2.read()

        full_version = f"{li}\n{li2}\n{cv1}"
        with open(li1,"w") as new:
            new.write(full_version)


        c.print("key has been added , key is: ",end="")
        c.print(f"{code}",style="yellow")
        c.print("the key will be added to all of your python files and it wont work without typing the key",style="underline")
        c.print("make sure to save the key and do not repeat the process or it might break your files!",style="underline red")


        # back to main dir
        os.chdir(raw)

    elif v1 == "play a file" or v1 == "3":
        try:
            os.chdir("../../../source_py")
            print("\nwrite your file name: ",end="")
            ai1 = input()
        
            compelete = []
            compelete.append(ai1)
            compelete.append(".py")
            ce = ''.join(compelete)
            print("\n")
            print(f"current path: {os.getcwd()}")
            os.system(f"python3 {ce}")
            os.chdir(raw)

        except Exception as e:
            c.print(f"error in choice 3, {e}",style="red")

    elif v1 == "mod files" or v1 == "5":
        print("type the file name: ",end='')
        x1 = input()

        os.chdir("../../../source_py")

        os.system("clear")
        c.print(f"e: edit {x1}",style="bold")
        while True:
            print("choose your choice: ",end='')
            i = input()
            if i == "q" or i == "break":
                print("breaking...")
                break

            elif i == "e":
                os.system(f"nvim {x1}")

    elif v1 == "about exier" or v1 == "6":
        define_exier = f"""
        is playground i made as a file manager that protect-edit-manage python files.

        the code is still in its early versions and its little buggy but i will fix it with better versions later 


        menu choices :-

        as you see the code holds about 6 choices in the menu 


        1. does show you the commands  you can write as input beside the choices in the main menu

        2. does generate a key and add it to the targeted file in your path where you cant play the code without writing the key

        3. where you dont have to change the dir and can run your file directly from inside exier 

        4. does show you the files been collected from the dir where you put your python files in

        5. does show you options where you can edit or delete or manage your python files  (all gonna be updated)

        6. and its about the app where you found this message

        the is going to be updated and will add new features soon

        madeBy_uv0
        """
        c.print(f"\n{define_exier}\n",style="bold") 
