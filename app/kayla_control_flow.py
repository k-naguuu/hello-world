def liam_age(x):
    if x<23:
        return ("WRONG - too young")
    elif 100 > x >23:
        return ("WRONG - too old")
    elif x==23:
        return ("CORRECT")
    else:
        return ("Deceased")

def age_of_liam (x):
    return ("WRONG - too young" if x<23 else
        "WRONG - too old" if 100>x>23 else 
            "CORRECT" if x==23 else
                "Deceased")

def counting (x):
    for n in range(1, x+1):
        print(n)
 
def count (x):
    n=0
    while n < x+1:
        print (n)
        n += 1

def kayla_status(bored, unfocused, revelation_point):
    revelation_timer = 0
    cycle = ["mad", "happy", "sad", "annoyed", "sleepy"]
    n = 0 # start as mad
    while bored:

        revelation_timer += 1

        print(cycle[n])

        if revelation_timer > revelation_point - 1:
            print("Revelation!")
            break

        if unfocused:
            continue 

        if n == len(cycle) - 1:
            n = 0
            continue

        n += 1

        


kayla_status(True, False, 10)

