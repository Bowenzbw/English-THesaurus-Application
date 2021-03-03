import json 
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))
 
def FindMyWord(k):
    k = k.strip()   ## delete the 'space' of typing
    k = k.lower()   ##lowercase the input of the word 
    if k in data:    
        return data[k]
    elif k.title() in data:
        return data[k.title()]
    elif k.upper() in data:
        return data[k.upper()]
    elif len(get_close_matches(k, data.keys(),cutoff= 0.8)) > 0:  ## find the most similar word if mistype
        ask = input('Did you mean %s instead? Y for yes, N for no: '  % get_close_matches(k, data.keys())[0])  ## ask if that mathch the purpose 
        if ask.lower() == 'y':
            k = get_close_matches(k, data.keys())[0]
            return data[k]
        elif ask.lower() =='n':
            return 'No match found, please double check'
        else:
            return 'we do not understand your entry'
    else:
        return 'word not exist, please double check'

word = input("Enter word ")

# print (FindMyWord(word))

output = (FindMyWord(word)) 

if type(output) == list:    ## display the meaning of the words with multiple meaning in different lines 
    for i in output:
        print(i)
else:
    print(output)



    