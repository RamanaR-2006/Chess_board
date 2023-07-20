#Board, array
Board = []

#dictionary translates Horizontal letters to numbers which can work inside the array
dictionaryRow = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

def isRookLegalVert(n1,n2):
    step = 1
    if n2<n1:
        step = -1
    for i in (n1,n2):
        

def rook(orig,final):
    number1 = dict(orig[0])
    number2 = int(orig[1])
    final1 = dict(final[0])
    final2 = dict(final[1])
    if number1 == final1:
        isRookLegalVert(number1,number2)
    elif number2 == final2:


for i in range(8):
    if i == 7:
        Board.append(['rB','nB','bB','qB','kB','bB','nB','rB'])
    elif i == 0:
        Board.append(['rW','nW','bW','qW','kW','bW','nW','rW'])
    elif i == 6:
        Board.append(['pB','pB','pB','pB','pB','pB','pB','pB'])
    elif i == 1:
        Board.append(['pW','pW','pW','pW','pW','pW','pW','pW'])
    else:
        Board.append(['.','.','.','.','.','.','.','.'])

for i in Board:
    print(i)

end = False
p1=True
p2=False
while end == False:
    for i in Board:
        print(i)
    if p1==True: