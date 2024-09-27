#This function will check whether the given number is neon number or not.
def neon(n):
    a=0
    b=n**2
    for i in str(b):
        a+=int(i)

    if(a==n):
        return True
    else:
        return False
