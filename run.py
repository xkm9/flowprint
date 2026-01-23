# standard libs
import os , random

from rich.console import Console
from rich.markup import escape
from pathlib import Path
from collections import Counter

# summon my homemade lib
from flowprint.lib.homemade import search, randomize , pickfile , pro_felter , pro_felter2

# commands
inject_cmds = ["inject"]
target_funcs = ["class","def", "import","while","if","elif" ]


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
    c.print(f"\ncurrent path is {os.getcwd()}\n",style='bold')


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
    
    msg1 = """ [inj commands] - [fp cmds] - [about] - [exit] """
    c.print(f"\n\ncommands: \n\n{escape(msg1)}\n",style='bold')
    c.print("you can run '-ex cmds' to see an explaination of the commands.",style='color(8)')

   
def interface():

    c = Console()

    i_main = input("\ntype your input: ")
    print('\n')
    inputs.append(f" {i_main} ")



    if i_main == "about":
        
        subject = "     - flowprint:"
        context = """

        its a tool made to analyze - track the code process , adding print statements in targeted inject points under [blue]if[/blue] conditions , or [#800080]def[/#800080] functions or [#af00ff]import[/#af00ff] lines to know what is going on live in your code.

        you set the dir then the targeted file and when typing [bold]-fp scan[/bold] it'll show you how many available injecting points are in your code.

        and if you type [bold]-fp -s scan[/bold] it'll show all points and its line numbers.

        [bold]'-fp inject'[/bold] will help you inject print statements into your code with commands like [bold]'-fp inject def'[/bold] or [bold]-fp inject import[/bold] with tags to notice where were the prints written.

        the rest of the commands are just base commands to change the dir or the file or to see the menu commands you can find them all after setting the dir and file you want when running the program.

        its modularly structured , try [underline]python3 -m flowprint.run[/underline] to run your tool and better put in home dir.

        make sure you have the libraries: [green]rich[/green] , [green]pathlib[/green] installed before running the project , it'll auto create an injected file from your same code but with print statements for safety reasons , and will be put in home/results folder. (dont worry if you dont have the file the tool will create it, its made for automated injecting and analyzing anyway).

        the tool is in early versions and im just a jr coder in python so the code may not be the best but i will update it with time.

        [bold]git clone git@github.com:xkm9/flowprint.git[/bold]

        Made by: [bold]AuvaO[/bold]
        (I'm not a native English speaker, so sorry if my grammar is not perfect.)


        in summary:

        a code analyzer that inject print statements around your code to trace its traffic movement.
        """
        

        c.print(subject , "\n\n" , style="underline bold")
        c.print(context)



        

    elif i_main == "exit":
        check_exit.append("exit")

    elif i_main == "inj commands":
        print("\n")
        c.print("-fp inject [purple]import[/purple]")
        c.print("-fp inject [blue]class[/blue]")
        c.print("-fp inject [purple]def[/purple]")
        c.print("-fp inject [purple]while[/purple]")
        c.print("-fp inject [blue]if[/blue]")
        c.print("-fp inject [blue]elif[/blue]")
        print("\n")
        


    elif i_main == "fp cmds":
        msg1 = """'-fp inject' to inject print statements in your code.\n'-fp scan' to scan and see how many available injecting points are i your code.\n'-fp -s scan' to show you all available injecting places with its line number.\n'-fp -a scan' to show you how many available injecting points in each different targets like def or import and also a list with recommended injections.\n'-fp change-file' to change your current file (!not recommended straight after injecting).\n'-fp add-dir' to dive more inside the dir you're currently in.\n'-fp reset-dir' to reset your to home. """
        c.print(msg1, style='bold')


    elif i_main == "-ex cmds":
        msg = """
        [bold underline]inj commands[/bold underline] does show a list of injection commands you can make.
        [bold underline]fp cmds[/bold underline] does show you -fp commands you can use across the app like -fp change-file or -fp reset-dir
        [bold underline]about[/bold underline] does show you the context of this tool.
        exit to exit the running loop.
        """

        c.print(msg)



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
    
    pro_filter = pro_felter(inputs , ["-s","-a"])
    pro_filter0 = pro_felter(inputs , ["scan"])
    
    if pro_filter == "-s":
        for i ,(index , line , pattern ) in enumerate(tuples_scan):
            msg1 = f"""
            inject {i} - 
            line num. {index} : {line}
            """
            c.print(" ",msg1,style="pink1")

    
    elif pro_filter == "-a":

        s1 = pro_felter2(dic["source code"],target_funcs)
        counter = Counter(s1)

        for word , count in counter.items():
            c.print(f"{count} {word} counted.",style="bold")





    if pro_filter0:
        c.print(f"\ntotal availabe injections are {len(tuples_scan)} points. ",style='bold underline')


    
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
