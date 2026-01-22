# standard libs
import os , random

from rich.console import Console
from pathlib import Path

# summon my homemade lib
from flowprint.lib.homemade import search, randomize , pickfile , pro_felter

# commands
inject_cmds = ["inject"]
target_funcs = ["class","def", "import","for","while"]
app_cmds = ['cmd','exit']


# where matches go 
inj_match = []
target_match = []

# where inputs go
inputs = []

# to check when exit command
check_exit = []

# the file lines will be packed - injected here.
packed_files = []

# for the name of the file
targeted_file = []

# here is a tuples list holds a trio of : the line number , the line itself , and pattern to be injected 
tuples_scan = []

# i forgot whats this for
path1 = []

#  file name with random keys added
rnd_f = []

# tuples scan len number will be added here
ts_len = []

# the main dictionary
dic = {
            "command type": inj_match , # inject match
            "fn type": target_match,  # targect funcs
            "source code": packed_files
            }


def path():
    path0 = []
    c = Console()

    paths = os.listdir('.')
    for p0 in paths:
        if not p0.startswith('.'):
            path0.append(p0)

    c.print("paths: ",style='bold underline')
    for p in path0:
        c.print(" ",p,style='bold blue')

    v0 = input("\nplease write your dir: ")
    path1.append(v0)
    os.chdir(f"{Path.home()}/{v0}")

def add_dir():

    path0 = []
    c = Console()

    paths = os.listdir('.')
    for p0 in paths:
        if not p0.startswith('.'):
            path0.append(p0)

    c.print("paths: ",style='bold underline')
    for p in path0:
        c.print(" ",p,style='bold blue')

    v0 = input("\nplease write your dir: ")
    path1.append(v0)
    os.chdir(v0)


def reset_dir():
    c = Console()

    home = Path.home()
    os.chdir(home)
    c.print(f"current path is {os.getcwd()}",style='bold')
    path()

def setup():

    c = Console()
    c.print(f"current path is {os.getcwd()}\n",style='bold')


    files = pickfile(path1[-1])
    
    c.print("\nfiles: ",style='bold underline')
    for f in files:
        print(f" {f}")
        packed_files.append(f)

    print("\n")
    i_first = input("pick up a file: ")
    targeted_file.append(i_first)

    os.system("clear")


def menu():
    
    c = Console()

    # main input
    print('\n')
    print(f"targeted file is ",end='')
    c.print(targeted_file[-1],style="bold underline")
    print(f"\nmenu commands are:\n1. app cmds \n2. injection cmds \n3. fp commands\n")
   
def interface():

    c = Console()

    i_main = input("\ntype your input: ")
    print('\n')
    inputs.append(f" {i_main} ")


    if i_main == "app cmds":

        print("\nabout: about the app.")
        # to be continued 

    elif i_main == "about":
        print("\nabout")
        # print("commands explained")

    elif i_main == "exit":
        check_exit.append("exit")

    elif i_main == "injection cmds":

        c.print("\navalaible injecting commands: ", style='bold')
        for inj in target_funcs:
            print(f"-fp inject {inj}")


    elif i_main == "fp commands":
        print("\n-fp inject\n-fp scan\n-fp -s scan\n-fp change-file\n-fp add-dir\n-fp reset-dir ")




def set_data():


    i_compare = "".join(inputs)
    is_compare = i_compare.split()

    for isc in is_compare:
        if isc in inject_cmds:
            inj_match.append(isc)

        elif isc in target_funcs:
            target_match.append(isc)

    with open(f'{targeted_file[-1]}','r') as f:
        file = f.readlines()
        packed_files.extend(file)


    rnd  = randomize(targeted_file[-1])
    rnd_f.append(rnd)

    sl  = search(dic["source code"], target_funcs)

    for i in range(len(sl["line"])):
        line = sl["line"][i]
        index = sl["index"][i]
        pattern = sl["pattern"][i]
        tuples_scan.append((index , line , pattern))


    if len(file) > 1:
        file.clear()



def run_injecting():
    
    c = Console()

    home = Path.home()
    os.chdir(home)
    packed = os.listdir('.')
    if 'results' in packed:
        os.chdir('results')

    else:
        os.mkdir('results')
        os.chdir('results')

         
    v1 = search(dic["source code"], dic["fn type"]) 

    
    tuples_scan.sort(reverse=True)
    for index , line , pattern in tuples_scan:
        space = len(line) - len(line.lstrip())
        inject = (" "  * space ) + pattern

        dic["source code"].insert(index + 1 , inject)

    
    with open(rnd_f[-1], "w") as f1:
        for dc in dic["source code"]:
            f1.write(dc)

    
    c.print(f"file {rnd_f[-1]} has been made , check path {os.getcwd()} to see your injected file.",style="green")

    

def scan():


    c = Console()    
    c.print(f"file is scanned , availabe injections are {len(tuples_scan)} points. ",style='bold underline')

    pro_filter = pro_felter(inputs , ["-s"])

    if pro_filter != None:
        for i ,(index , line , pattern ) in enumerate(tuples_scan):
            msg1 = f"""
            inject {i} - 
            line num. {index} : {line}
            """
            c.print(" ",msg1,style="pink1")


    
def runner():

    try:
        while True:

            if "exit" in check_exit:
                break

            interface()

            is_compare = ''.join(inputs)
            isc0 = is_compare.split()

            for isc1 in isc0:
                if isc1 == "-fp":
                    for isc2 in isc0:
                        if isc2 == "inject":
                            set_data()
                            run_injecting()



                        elif isc2 == "scan":
                            set_data()
                            scan()

                        elif isc2 == "add-dir":
                            add_dir()

                        elif isc2 == "change-file":
                            setup()

                        elif isc2 == "reset-dir":
                            reset_dir()


                    # cleaning
                    inputs.clear()
                    inj_match.clear()
                    target_match.clear()
                    packed_files.clear()
                    tuples_scan.clear()


                

    except Exception as e:
        c = Console()
        c.print(e,style='red')


if __name__ == "__main__":

    path()
    setup()
    menu()
    runner()
