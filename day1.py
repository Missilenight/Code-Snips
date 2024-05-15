import os
import re

input = "./inputs/day1/input.txt"
 
values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

def task1(data):
    count = 0
    for line in data:
        numbers = re.findall(r'\d', line)
        
        start = numbers[0]
        finish = numbers[-1]
        
        count += int(start + finish)
    
    return count

def splitString(text):
    return re.split(r'(\d+)', text)

def stringToNumbers(split):
    numbers = [] 
    
    for entry in split:
        if entry.isdigit():
            for i in entry:
                numbers.append(i)
        else:
            entries = []
            
            for key, value in values.items():
                searchIter = re.finditer(key, entry, re.IGNORECASE)
                for search in searchIter:
                    start, _ = search.span()
                    entries.append((start, value))
                    
            entries.sort()
            sortedValues = [entry[1] for entry in entries]
            
            numbers.extend(sortedValues)
    
    return numbers
    
def task2(data):
    count = 0
    
    for line in data:
        split = splitString(line)
        
        strToNumbers = stringToNumbers(split)
        
        start = strToNumbers[0]
        finish = strToNumbers[-1]
        
        count += int(start + finish)
        
    return count

with open(input, "r") as file:
    data = file.readlines()
    
    print(task1(data))
    print(task2(data))