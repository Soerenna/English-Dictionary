import json
from difflib import SequenceMatcher
import time
with open('C:\\Users\\Soerenna\\Desktop\\Projects\\English Thesaurus\\data.json') as f:
    r = f.read()
data = json.loads(r)

def find_word(word):
    definitions = []
    try:
        return data[word]
    except KeyError:
        return None
 
def matcher(word):
    matches = dict() # create a dictionary which contains keys with their respective ratios if the ratio > 0.5
    for key, value in data.items():
        s = SequenceMatcher(a=key,b=word)
        ratio = s.ratio()
        if ratio > 0.5:
            matches[key] = ratio
    max_keys = [key for key, ratio in sorted(matches.items(), key=lambda x: x[1], reverse=True)[:8]] # the keys with values that correspond to the eight highest similarity ratios in descending order
    return max_keys

def display(result):
    if result:
        if len(result) > 1:
            count = 1
            for definition in result:
                print(f'definition {count}: {definition}'+'\n')
                count += 1
        else:
            for definition in result:
                print(f'definition: {definition}'+'\n')
    else:
        print('Sorry, no such word in my library..')
        
def suggest(matches):
    print('Word not found.')
    print('Did you mean one of these words?\n')
    
    for i in range(len(matches)):
        print(f'({i+1}) {matches[i]}')
    
    while True:
        time.sleep(0.05)
        answer = input('\ntype No or input corresponding number:').lower()
        if answer in ('no', 'n'):
            return None
        else:
            try:
                index = int(answer) - 1
                if index in range(len(matches)):
                    return matches[index]
                else:
                    print('please input correct value.')
            except ValueError:
                print('please input correct value.')

def run_program():
    
    while True:
        run = input('Do you wish to continue? (y/n):').lower()
        if run in ('yes','no','y','n'):
            break
        else:
            print('Please enter (y) to continue or (n) to stop.')
        
    return True if run in ('yes','y') else False

def dictionary():
    
    run = True
    
    while run:
        word = input('please enter a word: ').lower()
        print('\n')
        result = find_word(word)
        
        if result:
            display(result)
            run = run_program()
        else:
            possible_matches = matcher(word)
            if possible_matches:
                match = suggest(possible_matches)
                if match:
                    result = find_word(match)
                    print('\n')
                    display(result)
                    run = run_program()
                else:
                    display(match)
            else:
                display(matches)

