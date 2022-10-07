Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print (first("Hello"))
H
print (middle("Hi"))

print (middle("A"))

print (middle(""))

print (first("A"))
A
print (last("A"))
A

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print (is_palindrome('nate'))
False
print (is_palindrome('bob'))
True
print (is_palindrome('noon'))
True
