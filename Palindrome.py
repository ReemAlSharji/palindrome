## output palindrome if the reverse and word are same letters

def palindrome(word):
    pali = word[::-1] #takes reverse of word
    if word == pali:
        print('palindrome')
    else:
        print('not palindrome')

palindrome('madam')
