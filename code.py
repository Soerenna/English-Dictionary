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

test = 'braim' # a string to test the code
matches = dict() # create a dictionary which contains keys with their respective ratios if the ratio > 0.5
for key, value in data.items():
    s = SequenceMatcher(a=key,b=test)
    ratio = s.ratio()
    if ratio > 0.5:
        matches[key] = ratio

max_keys = sorted(matches.items(), key=lambda x: x[1], reverse=True)[:10] # timed the code and this third version came out 10 times faster then the previous ones on average
