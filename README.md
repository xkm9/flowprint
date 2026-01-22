# flowprint

its a tool  made to analyze - track the code process , adding prints statements in targeted inject points , under if conditions , or def functions or import lines to know what is going on live in your code.

- you set the dir then the targeted file and when typing `-fp scan` it'll show you how many available injecting are in your code
- and if you type `-fp -s scan` it'll show all points and its line numbers.

- `-fp inject` will help you inject print statements into your code with commands like `-fp inject def` or `-fp inject import` with tags to notice where were the prints written.


the rest of the commands are just base commands to change the dir or the file or to see the menu commands you can find them all after setting the dir and file you want when running the program.

its modularly structured , try `python3 -m flowprint.run` to run your tool and better put in home dir.


make sure you have the libraries: rich , pathlib installed before running the project , it'll auto create an injected file from your same code but with print statements for safety reasons , and will be put in home/results folder. (dont worry if you dont have the file the tool will create it, its made for automated injecting and analyzing anyway.) 


- the tool is in early versions and im just a jr coder in python so the code may not be the best but i will update it with time.

- `git clone https://github.com/xkm9/flowprint.com`

**Made by:** AuvaO  
*(I'm not a native English speaker, so sorry if my grammar is not perfect.)*
