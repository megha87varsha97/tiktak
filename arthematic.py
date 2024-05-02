lst=[0,0,0,0,0,0,0,0,0]
def board():
    count=0

    for j in range(3):
        for i in range(3):
            if lst[count]==0:
                print("__|",end=' ')
            else:
                print(lst[count]+"|",end=' ')
            count+=1
        print()
board()
user='x'
game=True
def swap_user():
    if globals()['user']=='x':
         globals()['user']='o'
    else:
        globals()['user']='x'
def win():
    if lst[0]=='x' and lst[1]=='x' and lst[2]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[3]=='x' and lst[4]=='x' and lst[5]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[6]=='x' and lst[7]=='x' and lst[8]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[0]=='x' and lst[3]=='x' and lst[6]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[1]=='x' and lst[4]=='x' and lst[7]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[2]=='x' and lst[5]=='x' and lst[8]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[0]=='x' and lst[4]=='x' and lst[8]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[2]=='x' and lst[4]=='x' and lst[6]=='x':
        globals()['game']=False
        print('x wins')
    elif lst[0]=='o' and lst[1]=='o' and lst[2]=='o':
        globals()['game']=False
        print('o wins')
    elif lst[3]=='o' and lst[4]=='o' and lst[5]=='o':
        globals()['game']=False
        print('o wins')
    elif lst[6]=='o' and lst[7]=='o' and lst[8]=='o':
        globals()['game']=False
        print('o wins')
    elif lst[0]=='o' and lst[3]=='o' and lst[6]=='o':
        globals()['game']=False
        print('o wins')
    elif lst[1]=='o' and lst[4]=='o' and lst[7]=='o':
        globals()['game']=False
        print('o wins')
    elif lst[2]=='o' and lst[5]=='o' and lst[8]=='o':
        globals()['game']=False
        print('o wins')
    elif lst[0]=='o' and lst[4]=='o' and lst[8]=='o':
        globals()['game']=False
        print('o wins')
    elif lst[2]=='o' and lst[4]=='o' and lst[6]=='o':
        globals()['game']=False
        print('o wins')
        
    
def over():
    if lst[0]!=0 and lst[1]!=0 and lst[2]!=0 and lst[3]!=0 and lst[4]!=0 and lst[5]!=0 and lst[6]!=0 and lst[7]!=0 and lst[8]!=0 and lst[9]!=0:
        globals()['game']=False
        print("game is over")
        
while game:
    n=int(input("enter the selection: "))
    if lst[n-1]==0:
        lst[n-1]=user
    board()
    swap_user()
    win()
    over()












