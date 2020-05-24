import os


print("""
    [1] player One == "X" 
    [1] player Two == "O" 
""")
text = ["1","2","3","4","5","6","7","8","9"]
isEnd = False
counter = 0
def printboard():
    print("\t" +'\n')
    print("\t" + text[0] + '  |  ' + text[1] + '  |  ' + text[2])
    print("\t" +'- - - - - - -')
    print("\t" +text[3] + '  |  ' + text[4] + '  |  ' + text[5])
    print("\t" +'- - - - - - -')
    print("\t" +text[6] + '  |  ' + text[7] + '  |  ' + text[8])
    print("\t" +'\n')

def checking(win : str):
    global count
    global isEnd 
    if (
    (text[0] == win and text[1] == win and text[2] == win) 
    or 
    (text[3] == win and text[4] == win and text[5] == win)
    or 
    (text[6] == win and text[7] == win and text[8] == win)  
    or 
    (text[0] == win and text[4] == win and text[8] == win) 
    or 
    (text[2] == win and text[4] == win and text[6] == win)
    or
    (text[2] == win and text[5] == win and text[8] == win)
    or 
    (text[0] == win and text[3] == win and text[6] == win)
    ) :
        print( win + " win Wow !!")
        print("Good By 😀")
        isEnd = True
        exit
def Check(number: int):
    number -= 1
    global counter
    if counter % 2 == 0:
        text[number] = "X"
        counter+=1
        printboard()
    else:
        text[number] = "O"
        counter+=1
        printboard()
    checking("X")
    checking("O")
def play(number : int):
      if number == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
          Check(number)
printboard()
while isEnd == False:
    number = int(input(f"Tybe Your Number: "))
    play(number)
    

