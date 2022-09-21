# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#  Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
from random import randint as rd

def player_vs_player():
    player_1=input('Введите имя 1 игрока')
    player_2=input('Введите имя 2 игрока')
    candies=2021
    player_1_candies=0
    player_2_candies=0
    playerChoise=rd(0,1)
    while candies!=0:
        print(f'Всего конфет осталось = {candies}')
        print(f' У {player_1} = {player_1_candies} конфет')
        print(f' У {player_2} = {player_2_candies} конфет')
        if playerChoise==0:
            print(F'Твой ход {player_1}')
            take=int(input())
            if take<=candies and 0<take<29:
                candies-=take
                player_1_candies+=take
                playerChoise=1
            else:
                print('некорректный ввод попробуй еще раз')
                playerChoise=0
        if playerChoise==1:
            print(F'Твой ход {player_2}')
            take=int(input())
            if take<=candies and 0<take<29:
                candies-=take
                player_2_candies+=take
                playerChoise=0
            else:
                print('некорректный ввод попробуй еще раз')
                playerChoise=1       
    else:
        if playerChoise==0:
            print(f'Поздравляю, {player_2}, ты победил ')
        else:  
            print(f'Поздравляю, {player_1}, ты победил ')  

def player_vs_computer():

    player_1=input('Введите имя  игрока')
    player_2='Компьютер'
    candies=121
    player_1_candies=0
    player_2_candies=0
    playerChoise=rd(0,1)
    while candies!=0:
        print(f'Всего конфет осталось = {candies}')
        print(f' У {player_1} = {player_1_candies} конфет')
        print(f' У {player_2} = {player_2_candies} конфет')
        if playerChoise==0:
            print(F'Твой ход {player_1}')
            take=int(input())
            if take<=candies and 0<take<29:
                candies-=take
                player_1_candies+=take
                playerChoise=1
            else:
                print('некорректный ввод попробуй еще раз')
                playerChoise=0
        if playerChoise==1:
            print(F'Твой ход {player_2}')
            if candies<=28:
                take=candies
            else:
                take=rd(1,28)             
            if take<=candies and 0<take<29:
                candies-=take
                player_2_candies+=take
                playerChoise=0
            else:
                print('некорректный ввод попробуй еще раз')
                playerChoise=1       
    else:
        if playerChoise==0:
            print(f'Поздравляю, {player_2}, ты победил ')
        else:  
            print(f'Поздравляю, {player_1}, ты победил ')  

player_vs_computer()

