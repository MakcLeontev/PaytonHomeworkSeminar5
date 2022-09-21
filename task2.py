# Создайте программу для игры в ""Крестики-нолики"".
arr=[[1,2,3],
     [4,5,6],
     [7,8,9]]
def print_pole():     
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            print(arr[i][j], end=' ')
        print()
    print()
player_token='X'
empty_place=True
win=False
def filling(player_token,number):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j]==number:
                arr[i][j]=player_token
def winner(array):
    if arr[0][0]==arr[0][1]==arr[0][2] or arr[1][0]==arr[1][1]==arr[1][2]or arr[2][0]==arr[2][1]==arr[2][2] or arr[0][0]==arr[1][0]==arr[2][0] or arr[0][1]==arr[1][1]==arr[2][1] or arr[0][2]==arr[1][2]==arr[2][2] or arr[0][0]==arr[1][1]==arr[2][2] or arr[2][0]==arr[1][1]==arr[0][2]:
        win=True
        print('win')
    else:
        win=False    
    return win   
step=0    
while not win or step==9:
    print_pole()
    number=int(input(f'Ходит {player_token} выбери номер ячейки '))
    filling(player_token,number)
    win=winner(arr)
    if player_token=='X':
        player_token='O'
    else:
        player_token='X'
    step+=1
else:
    print_pole()
    if step==9:
        print('Ничья')
    elif player_token=='X':
        print('O - выиграл')
    else:
        print('X - выиграл')   





