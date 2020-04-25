'''

BruteForce 
Found all possible substr and find the longest one 
combination (n , n-1)
O( n^3)

If we encounter a repeated character we basically stop

starting building a substring at position i 
find the longest one from position i-1 

finally return the longest one 
'''

def longsubwithoutrepeatedChar(s):
    substr , longest = {} , 1
    for i in s:
        if i in substr.keys():
            substr = {}
        substr[i] = 0
        longest = max(longest, len(substr.keys()))
        # print(substr)
    return longest


testcase = ["abcabcbb", "bbbbb", "pwwkew"]
result = [ 3 , 1 ,3 ]

print(longsubwithoutrepeatedChar(testcase[0]))
print(longsubwithoutrepeatedChar(testcase[1]))
print(longsubwithoutrepeatedChar(testcase[2]))