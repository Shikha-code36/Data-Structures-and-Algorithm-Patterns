'''
Given a string S, remove all the consecutive duplicates. Here we keep one character and remove all subsequent same characters.

Examples: 

Input  : aaaaabbbbbb
Output : ab

Input : aabccba
Output : abcba

'''

def removeconsecutivestring(Str):
    if len(Str)<2:
        return Str
    if Str[0]!=Str[1]:
        return Str[0]+removeconsecutivestring(Str[1:])
    return removeconsecutivestring(Str[1:])

print(removeconsecutivestring("aabccba")) #abcba