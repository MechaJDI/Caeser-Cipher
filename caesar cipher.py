# The purpose of this project is to encrypt a user inputted word or sentence into
# a new set of characters based on the ciper text given. 

start = raw_input('Please input a word or sentence in all capital letters: ')

word = ''

encrypt_dict = {  # cipher text dictionary; done so that no letter is equal to itself
        'A':'E',
        'B':'N',
        'C':'C',
        'D':'R',
        'E':'Y',
        'F':'P',
        'G':'T',
        'H':'Z',
        'I':'A',
        'J':'B',
        'K':'D',
        'L':'F',
        'M':'G',
        'N':'H',
        'O':'I',
        'P':'J',
        'Q':'K',
        'R':'L',
        'S':'M',
        'T':'O',
        'U':'Q',
        'V':'S',
        'W':'U',
        'X':'V',
        'Y':'W',
        'Z':'X',
        ' ':'0',
        '.':'1',
        ',':'2',
        ';':'3',
        '?':'4',
        '!':'5'}

def wordencode(word):
    results = ''
    for letter in word:
        results += encrypt_dict[letter]  # adds each translated letter to 'results'
    return results

encodedword = wordencode(start)

print 'The encrypted word/sentence is', encodedword

# the following section was from a code found from a forum discussing how to
# reverse dictionaries on stackoverflow.com

from collections import defaultdict
reversed_dict = defaultdict(list)
for key,value in encrypt_dict.iteritems():
    reversed_dict[value].append(key)

def worddecode(word):
    decresults = ''
    for letter in word:
        subword = str(reversed_dict[letter]) # converts list into string
        decresults += subword[2]  # it is necessary to write it in this fashion
# because the function reversed_dict[letter] will return each individual character
# separated by brackets and quotations
    return decresults

decodedword = worddecode(encodedword)

print 'The decrypted word/sentence is', decodedword
        
