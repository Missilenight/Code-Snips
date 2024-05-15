import os
import re

input = "./inputs/day2/input.txt"

def task1(data):
    games = []
    
    for game in data:
        gameStr = re.search(r'Game \d+\:', game).group()
        gameId  = re.search(r'\d+', gameStr)
        
        new = {"id": gameId.group(), "green": 0, "red": 0, "blue": 0}
        
        gameplay = game[len(gameStr):]
        draws = gameplay.split(';')
        
        for draw in draws:
            cubes = draw.split(',')
            
            for cube in cubes:
                quantity = int(re.search(r'\d+', cube).group())
                color = re.search(r'[a-zA-Z]+', cube).group()
                
                if new[color] < quantity:
                    new[color] = quantity
        
        games.append(new)
        
    sum = 0
    
    for game in games:
        if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
            sum += int(game['id'])
            
    print(sum)
    
    return games

def task2(games):
    sum = 0
    
    for game in games:
        sum += game['red'] * game['blue'] * game['green']
    
    return sum
    

with open(input, "r") as file:
    data = file.readlines()
    
    games = task1(data)
    
    print(task2(games))
    
    
    
