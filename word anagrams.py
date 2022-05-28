# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(god, dog):
    # [assignment] Add your code here
    if (sorted(god) == sorted(dog)):
       answer = True
    else:
     answer = False   
    print (answer)   


strl = input("put in first word")
strl = input("put in the second word")
find_anagram(strl, strl)

    
 