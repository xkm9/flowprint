# flowprint

its a tool  made to analyze - track the code process , adding print statements in targeted points , under if conditions , or def functions or import lines to know what is going on live in your code.

- you set the dir then the targeted file and when typing `-fp scan` it'll show you how many available injecting points are in your code
- and if you type `-fp -s scan` it'll show all points and its line numbers.

- `-fp track` will help you inject print statements into your code with commands like `-fp track def` or `-fp track import` with tags to notice where were the prints written.


the rest of the commands are just base commands to change the dir or the file or to see the menu commands you can find them all after setting the dir and file you want when running the program.

its modularly structured , try `python3 -m flowprint.run` to run your tool and better put in home dir.


make sure you have the libraries: rich , pathlib installed before running the project , it'll auto create an injected file from your same code but with print statements for safety reasons , and will be put in home/results folder. (dont worry if you dont have the file the tool will create it, its made for automated injecting and analyzing anyway.) 


- the tool is in early versions and im just a jr coder in python so the code may not be the best but i will update it with time.

- `git clone git@github.com:xkm9/flowprint.git`

version 1.4.5

**Made by:** AuvaO  
*(I'm not a native English speaker, so sorry if my grammar is not perfect.)*
