def sum(a,b,c):
    return a+b+c

def printBoard(xState,zState):
    A='X' if xState[0] else('O' if zState[0] else 0)
    B='X' if xState[1] else('O' if zState[1] else 1)
    C='X' if xState[2] else('O' if zState[2] else 2)
    D='X' if xState[3] else('O' if zState[3] else 3)
    E='X' if xState[4] else('O' if zState[4] else 4)
    F='X' if xState[5] else('O' if zState[5] else 5)
    G='X' if xState[6] else('O' if zState[6] else 6)
    H='X' if xState[7] else('O' if zState[7] else 7)
    I='X' if xState[8] else('O' if zState[8] else 8)
    print(f" {A} | {B}  |{C}")
    print(f"-- |--- |---")
    print(f" {D} | {E}  |{F}")
    print(f"-- |--- |---")
    print(f" {G} | {H}  |{I}")

def checkWin(xState,zState):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xState[win[0]],xState[win[1]],xState[win[2]])==3):
            print("X  won the match")
            return 1
        if(sum(zState[win[0]],zState[win[1]],zState[win[2]])==3):
            print("Y won the match")
            return 0
    return -1       

if __name__=="__main__":
        xState=[0,0,0,0,0,0,0,0,0]
        zState=[0,0,0,0,0,0,0,0,0]
        turn=1 
        print("Welcome to TIC TAC TOE")
        print("Enter the box no in which u want ur sign")
        while (True):
            printBoard(xState,zState)
            if(turn==1):
                print("X's Chance")
                value=int(input("Enter a value: "))
                xState[value]=1
            else:
                print("0's Chance")
                value=int(input("Enter a value: "))
                zState[value]=1
            cwin=checkWin(xState,zState)
            if(cwin!=-1):
                print("Match Over")
                break
            turn=1-turn
            
