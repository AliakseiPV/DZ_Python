#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: 
#- На столе лежит 2021 конфета. 
#- Играют два игрока делая ход друг после друга. 
#- Первый ход определяется жеребьёвкой. 
#- За один ход можно забрать не более чем 28 конфет. 
#- Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#a) Добавьте игру против бота
#b) Подумайте как наделить бота ""интеллектом""


sweets = 101
answer = input("Enter - '1'. If you want to play alone\nEnter - '2'. If you want to play with bot\n")

def Game(sweets):
        print(f"sweets: {sweets}")

        while(sweets > 0):

            if(sweets < 29): 
                winner = 1  
                break
            first_player = int(input("First player take candy but less than 29: "))
            if (first_player > 0 and first_player < 29):
                sweets -= first_player
                print(f"Number of sweets:{sweets}")
                winner = 1        
            else: 
                print("Error: You can take less that 29 sweets")
                break

            if(sweets < 29): 
                winner = 2  
                break
            second_player = int(input("Second player take candy but less than 29: "))
            if (second_player > 0 and second_player < 29):
                sweets -= second_player
                print(f"Number of sweets:{sweets}")
                winner = 2
            else: 
                print("Error: You can take less that 29 sweets")
                break
        return winner 


def Bot(sweets):
    print("Bot walks first")

    while(sweets > 0):
        print(sweets)

        if(sweets < 29):
            bot = sweets  
            print(f"Bot take {bot} sweets")
            sweets -= bot  
            winner = 1  
            break
        else:
            bot = int(sweets%(28+1)) 
            print(f"Bot take {bot} sweets")               
            sweets -= bot
        
        print(f"Number of sweets:{sweets}")

        second_player = int(input("Second player take candy but less than 29: "))
        if (second_player > 0 and second_player < 29):
            sweets -= second_player
            print(f"Number of sweets:{sweets}")
            winner = 2
        else: 
            print("Error: You can take less that 29 sweets")
            break
    return winner 


if(answer == "1"):
    winner = Game(101)
    if(winner == 1):
        print("Congratulations first player")
    if(winner == 2):
        print("Congratulations second player")
    
if(answer == "2"):
    winner = Bot(101)
    if(winner == 1):
        print("You loose")
    


       

    

