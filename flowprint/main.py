import os , json , random

from rich.console import Console
from pathlib import Path

# summon my homemade lib
from lib.homemade import search, randomize , pickfile 

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

ind = []

def setup():

    c = Console()

    print("path is randomly set to flowprint/files if you want a file from another path please type ",end='')
    c.print("-fp change dir",style='yellow')


    files = pickfile("files")

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
        print("cmds: to see the app commands\n")
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


def run_injecting():
    
    c = Console()

    i_compare = "".join(inputs)
    is_compare = i_compare.split()

    for isc in is_compare:
        if isc == "inject":
            inj_match.append("inject")

        elif isc in target_funcs:
            target_match.append(isc)



    with open(f'{targeted_file[-1]}','r') as f:
        file = f.readlines()


    rnd  = randomize(targeted_file[-1])
    os.chdir("../results") 



    dic = {
            "command type": inj_match ,
            "fn type": target_match,
            "source code": file
            }



    
    search1 = search(dic["source code"],dic["fn type"])

    for s1 in search1:
        place = dic["source code"].index(s1)
        ind.append(place)



    from lib.patterns import built_in_patterns

    for fn in dic["fn type"]:
        bip = built_in_patterns
        pattern_msg = bip[fn]




    ind.sort(reverse=True)
    for ind1 in ind:
        original_line = dic["source code"][ind1]

        space = len(original_line) - len(original_line.lstrip())
        injected_line = (" " * space) + pattern_msg

        dic["source code"].insert(ind1 + 1 ,injected_line)

    with open(rnd, "w") as f1:
        for dc in dic["source code"]:
            f1.write(dc)


    c.print(f"file {rnd} has been made , check path flowprint/results to see your injected file.",style="green")
    os.chdir(f"{Path.home()}/flowprint/files")
    
    
    
    
    
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
                    run_injecting()

                    # cleaning
                    inputs.clear()
                    inj_match.clear()
                    target_match.clear()
                    ind.clear()

                

    except Exception as e:
        c = Console()
        c.print(f"error from async runner : {e}",style='red')


if __name__ == "__main__":

    setup()
    runner()
