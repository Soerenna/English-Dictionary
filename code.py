import json
from difflib import SequenceMatcher
with open('C:\\Users\\Soerenna\\Desktop\\Projects\\English Thesaurus\\data.json') as f:
    r = f.read()
data = json.loads(r)

def find_word(word):
    try:
        return data[word.lower()]
    except KeyError:
        return 'Not Found'
 
def matcher(word):
    matches = dict() # create a dictionary which contains keys with their respective ratios if the ratio > 0.5
    for key, value in data.items():
        s = SequenceMatcher(a=key,b=word)
        ratio = s.ratio()
        if ratio > 0.5:
            matches[key] = ratio
    max_keys = sorted(matches.items(), key=lambda x: x[1], reverse=True)[:8] # the keys with values that correspond to the eight highest similarity ratios in descending order
    return max_keys

def dictionary():
    
    import json
    from difflib import SequenceMatcher
    with open('C:\\Users\\Soerenna\\Desktop\\Projects\\English Dictionary\\data.json') as f:
        r = f.read()   
    data = json.loads(r)
    
    while True:
        word = input('please enter a word: ').lower()
        print('\n')
        lookup = find_word(word)
        
        if lookup: # this should probably be a function 
            if len(lookup) > 1: 
                count = 1
                for definition in lookup:
                    print(f'definition {count}: {definition}'+'\n')
                    count += 1
            else:
                for definition in lookup:
                    print(f'definition: {definition}'+'\n')
            break
        else:
            # run search for similar words
            break
    
    return word

