Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")



def check_number():
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    c = int(input("Enter value for c: "))
    n = int(input("Enter value for n: "))
    return check_fermat(a, b, c, n)

check_number()

        

