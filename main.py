#Board, array
Board = []

#User, is the starting place
user = 'W'

#dictionary translates Horizontal letters to numbers which can work inside the array
dictionaryRow = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

#Note: 1 refers to rows (numbers) while 2 refers to column (letters)


def isRookLegalVertical(n1,n2,f2,user):
    step = 1
    if f2<n2:
        step = -1
    check = True
    for i in (n2+step,f2+step,step):
        temp = Board[n1,i]
        if i != f2:
            if temp != '.':
                check = False
        else: 
            if temp[1] == user:
                check = False
    return check

def isRookLegalHorizontal(n1,n2,f1,user):
    step = 1
    if f1<n1:
        step = -1
    check = True
    for i in (n1+step,f1+step,step):
        temp = Board[i,n2]
        if i != f1:
            if temp != '.':
                check = False
        else: 
            if temp[1] == user:
                check = False
    return check
    
def pawn(orig,final,user):
    number2 = dict(orig[0])
    number1 = int(orig[1])
    final2 = dict(final[0])
    final1 = dict(final[1])
    if number2 == final2:
        


def rook(orig,final,user):
    number2 = dict(orig[0])
    number1 = int(orig[1])
    final2 = dict(final[0])
    final1 = dict(final[1])
    if number2 == final2:
        if (isRookLegalVertical(number1,number2,final2,user)):
            Board[final1][final2] = orig + user
            Board[number1][number2] = '.'
            return True
    elif number1 == final1:
        if (isRookLegalHorizontal(number1,number2,final1,user)):
            Board[final1][final2] = orig + user
            Board[number1][number2] = '.'
            return True
    else:
        return False


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
        "To be continued"