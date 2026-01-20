import os , json , random , tracemalloc

from rich.console import Console
from pathlib import Path

# summon my homemade lib
from flowprint.lib.homemade import search, randomize , pickfile , p_filtered 

# commands
inject_cmds = ["inject"]
target_funcs = ["class","def", "import","for","while"]
app_cmds = ['cmd','exit']


# where matches go 
inj_match = []
target_match = []

# where inputs go
inputs = []


check_exit = []

packed_files = []
targeted_file = []

tuples = []
tuples_scan = []

path1 = []


rnd_f = []

ts_len = []

dic = {
            "command type": inj_match ,
            "fn type": target_match,
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

def reset():
    c = Console()

    home = Path.home()
    os.chdir(home)
    c.print(f"current path is {os.getcwd()}",style='bold')
    path()

def setup():
    c = Console()
    c.print(f"current path is {os.getcwd()}\n",style='bold')

    print("to change your directory ",end='')
    c.print("-fp change-dir",style='yellow')

    print("to go deeper inside the directory ",end='')
    c.print("-fp add-dir",style='yellow')

    print("to change your directory",end='')
    c.print("-fp change-file",style='yellow')

    print("to reset your directory",end='')
    c.print("-fp reset-dir",style='yellow')



    files = pickfile(path1[-1])
    
    print(f"path {os.getcwd()}")
    c.print("\nfiles: ",style='bold underline')
    for f in files:
        print(f" {f}")
        packed_files.append(f)

    print("\n")
    i_first = input("pick up a file: ")
    targeted_file.append(i_first)

    os.system("clear")

def interface():

    c = Console()
    # main input
    print('\n')
    print(f"targeted file is ",end='')
    c.print(targeted_file[-1],style="bold underline")
    print(f"\nyou can write 'inject cmds' or 'app cmds' to see the avaliabe commands.")
    i_main = input("type your input: ")
    print('\n')
    inputs.append(f" {i_main} ")

    # if conditions 
    if i_main == "app cmds":

        print("\nabout: about the app")
        print("exit: to exit the app")
        print("cmds: to see the app commands")
        print("task : to see what build next in the tool\n")
        # to be continued 

    elif i_main == "about":
        print("\nabout")

    elif i_main == "exit":
        check_exit.append("exit")

    elif i_main == "inject cmds":

        c.print("\nto run and know your commands you must understand this: \n",style='bold')
        print(" the commands wont work without typing -fp first")
        print(" you first write the command type weather inject or else + targeted function to be injected")
        c.print("\navalaible injecting commands: ", style='bold')
        for inj in target_funcs:
            print(f"-fp inject {inj}")

        c.print("\nor you can write -fp scan to see whats availabe to be injected in your file.",style='color(8)')

    elif i_main == "-fp commands":
        print("\n-fp inject ")
        print(f"fp change-file")
        print("-fp add-dir")
        print("-fp reset-dir")
        print("-fp scan")

    elif i_main == "task":
        print("support multiple injection one in command")
        print("edit the structure")
        print("# means make results folder outside flowprint and delete files folder")
        print("upgrade the inject statements")
        print("add more injection statements")
        print("upgrade the interface , add more commands(optional)")



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


def scan():


    c = Console()    
    c.print(f"file is scanned , availabe injections are {len(tuples_scan)} points. ",style='bold underline')

    pro_filter = p_filtered(inputs , ["-s"])

    if pro_filter != None:
        for i ,(index , line , pattern ) in enumerate(tuples_scan):
            msg1 = f"""
            inject {i} - 
            line num. {index} : {line}
            """
            c.print(" ",msg1,style="pink1")



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

    
    tuples.sort(reverse=True)
    for index , line , pattern in tuples:
        space = len(line) - len(line.lstrip())
        inject = (" "  * space ) + pattern

        dic["source code"].insert(index + 1 , inject)

    
    with open(rnd_f[-1], "w") as f1:
        for dc in dic["source code"]:
            f1.write(dc)

    
    c.print(f"file {rnd_f[-1]} has been made , check path {os.getcwd()} to see your injected file.",style="green")

    

    
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


                            tuples.clear()

                        elif isc2 == "scan":
                            set_data()
                            scan()

                        elif isc2 == "add-dir":
                            path()

                        elif isc2 == "change-file":
                            setup()

                        elif isc2 == "reset-dir":
                            reset()


                    # cleaning
                    inputs.clear()
                    inj_match.clear()
                    target_match.clear()
                    tuples.clear()
                    packed_files.clear()
                    tuples_scan.clear()


                

    except Exception as e:
        c = Console()
        c.print(e,style='red')


if __name__ == "__main__":

    path()
    setup()
    runner()
