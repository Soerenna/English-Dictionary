import json
with open('C:\\Users\\Soerenna\\Desktop\\Projects\\English Thesaurus\\data.json') as f:
    r = f.read()
data = json.loads(r)

def find_word(word):
    try:
        return data[word.lower()]
    except KeyError:
        return 'Not Found'

test = 'braim' # a string to test the code
matches = dict() # create a dictionary which contains all the with their respective ratios if the ratio > 0.5
for key, value in data.items():
    s = SequenceMatcher(a=key,b=test)
    ratio = s.ratio()
    if ratio > 0.5:
        matches[key] = ratio

max_ratios = sorted(matches.values())[-5:] # 5 highest similarity ratios
max_ratios = list(set(max_ratios)) # remove duplicates

# two possible ways of producing a list with the keys that correspond to the five highest similarity ratios
max_keys = [key for key, value in matches.items() if value in max_ratios] # an unsorted list of keys with 
max_keys = [] # a sorted list of keys in descending order, not efficient though will try to optimise if I go with this one.
for ratio in max_ratios[::-1]:
    for key, value in matches.items():
        if value == ratio:
            max_keys.append(key)
print(max_keys)

