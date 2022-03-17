arr = [['P','_','_'],['_','_','_'],['_','_','K']]
t = 0

playerpos = [0,0]
killerpos = [2,2]

def pri():
    print()
    print("\t\tThe Current Board ")
    print()
    for i in range(0,3,1):
        print(arr[i][0] + " " + arr[i][1] + " "+ arr[i][2] )

pri()


def boarderror(pos,mov):
    if mov == "R":
        if pos[0] < 3 and pos[1] < 2:
            return True
        else:
            return False
    if mov == "L":
        if pos[0] < 3 and pos[1] > 0:
            return True
        else:
            return False
    if mov == "T":
        if pos[0] > 0 and pos[1] < 3:
            return True
        else:
            return False
    if mov == "B":
        if pos[0] < 2 and pos[1] < 3:
            return True
        else:
            return False


def kill():
    if playerpos == killerpos:
        print("KILLED ...")
        global t
        t = 1

def right(cur,pos):
    if boarderror(pos,"R"): 
        arr[pos[0]][pos[1]] = '_'
        pos[1] += 1
        arr[pos[0]][pos[1]] = cur
    else:
        print("error move play again : ")
def left(cur,pos):
    if boarderror(pos,"L"):
        arr[pos[0]][pos[1]] = '_'
        pos[1] -= 1
        arr[pos[0]][pos[1]] = cur
    else:
        print("error move play again : ")

def top(cur,pos):
    if boarderror(pos,"T"):
        arr[pos[0]][pos[1]] = '_'
        pos[0] -= 1
        arr[pos[0]][pos[1]] = cur
    else:
        print("error move play again : ")

def bottom(cur,pos):
    if boarderror(pos,"B"):
        arr[pos[0]][pos[1]] = '_'
        pos[0] += 1
        arr[pos[0]][pos[1]] = cur
    else:
        print("error move play again : ")


c = 'f'
def movemaker(cur,c,pos):
    if c == "R":
        right(cur,pos)
    elif c == "L":
        left(cur,pos)
    elif c == "T":
        top(cur,pos)
    elif c == "B":
        bottom(cur,pos)
    else:
        print("invalid")

while t != 1:
    print()
    c = input("Player Move : ")
    movemaker("P",c,playerpos)
    pri()
    print()
    kill()
    c = input("Killer Move : ")
    movemaker("K",c,killerpos)
    kill()
    pri()

print()
print()
print("\t\t\tGAME FINISHED ")









