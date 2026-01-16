import random , os


def filtered(message,target):


    targeted_commands = target
    targeted_message = message.split()

    for ts in targeted_commands:
        for tm in targeted_message:
            if ts == tm:
                found = "".join(ts)

    return found


def d_filtered(msg,target):
    results = []

    large_list = []

    targeted_letters = target
    targeted_message  = msg.split()

    for tm in targeted_message:
        tm_listing = list(tm)
        large_list.append(tm_listing)

    for word_list in large_list:
        for letter_list in word_list:
            if letter_list in target:
                results.append(letter_list)

    return "".join(results)   

def randomize(name):

    l1 = list(name)
    v1  = []
    
    random_keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@$%^&*"
    l2 = [".","p","y"]
    
    for l in l1:
        if l not in l2:
            v1.append(l)

    r = random.sample(list(random_keys),k=5)
    v1.append("#")
    v1.extend(r)
    v1.append(".py")

    return "".join(v1)


def pickfile(p):

    files = []

    path = p
    os.chdir(path)

    packed_files = os.listdir(".")

    for pf in packed_files:
        if pf.endswith(".py"):
            files.append(pf)

    return files



def search(message,target):

    lines = []
    targeted_commands = target

    for msg in message:
        targeted_message = msg.split()

        for ts in targeted_commands:
            for tm in targeted_message:
                if ts == tm:
                    lines.append(msg)
                    break

    return lines if lines else None
