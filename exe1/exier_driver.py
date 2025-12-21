import os

def fn1():
    try:
        while True:

            print("\nwelcome to exier driver how can i help you?")
            print("i:install wanted libs    c: clear path   e:exit\n")
            i1 = input("input: \n")
            
            if i1 == "i":
                os.system("pip install rich shutil pathlib pyfiglet")
            elif i1 == "c":
                os.chdir("..")
                os.system("rm -rf new")
                print("path cleared now you can run exier")
            elif i1 == "e":
                break
    except Exception as e:
        print("error, {e}")

fn1()
