import random , os
from flowprint.lib.patterns import built_in_patterns as bip


def felter(message,target):


    targeted_commands = target


    targeted_message = message.split()

    for ts in targeted_commands:
        for tm in targeted_message:
            if ts == tm:
                found = "".join(ts)

    return found if found else None


def pro_felter(l,t):
    found = []
    list1 = l
    target = t

    for l1 in list1:

        l2 = l1.split()
        for l3 in l2:
            for t1 in target:
                if l3 == t1:
                    found.append(l3)

    return "".join(found) if found else None



def deep_felter(msg,target):

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


    if os.path.exists(path):
        os.chdir(path)


    packed_files = os.listdir(".")

    for pf in packed_files:
        if pf.endswith(".py"):
            files.append(pf)

    return files



def search(message,target):

    lines = []
    patterns = []
    places = []
    targeted_commands = target

    for msg in message:
        targeted_message = msg.split()

        for ts in targeted_commands:
            for tm in targeted_message:
                if ts == tm:
                    place = message.index(msg)
                    places.append(place)
                    pattern = bip[tm]
                    lines.append(msg)
                    patterns.append(pattern)

                    result = {
                            "line": lines,
                            "index": places,
                            "pattern": patterns


                            }
                    break

    return result if result else None
