import json
with open('C:\\Users\\Soerenna\\Desktop\\Projects\\English Thesaurus\\data.json') as f:
    r = f.read()
data = json.loads(r)

def find_word(word):
    try:
        for definition in data[word.lower()]:
            return definition
    except KeyError:
        return 'Not Found'
