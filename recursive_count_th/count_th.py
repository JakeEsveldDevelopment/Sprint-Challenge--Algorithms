'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    counter = 0
    if "th" in word:
        counter = 1 + count_th(word.replace("th", "x", 1))  
    else:
        return 0
    return counter