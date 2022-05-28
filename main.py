
def find_anagrams(word1, word2):
    # [assignment] Add your code here
 word1=input("first word")
 word2=input("second word")

 sorted_word1=sorted(word1)
 sorted_word=sorted(word2)
 
 if word1==word2:
     return True
 else:
    return False

