# x=int(input('x='))
# y=int(input('y='))
# d=bool(x<0 and y>0)
# print(d)

# #26 misol
# x=int(input('x='))
# y=int(input('y='))
# d=bool(x>0 and y<0)
# print(d)

def kompleks(a1,b1,a2,b2):
    a=input('a=')
    i=-1
    if a=='+':
        s=a1+i*b1+a2+i*b2
    elif a=='-':
        s=a1+i*b1-a2-i*b2
    elif a=='*':
        s=(a1+i*b1)*(a2+i*b2)
    elif a=='/':
        s=(a1+i*b1)//(a2+i*b2)
    else:
        s='bunaqa amal yo\'q'
    print(s)

a1=int(input('a1='))
b1=int(input('b1='))
a2=int(input('a2='))
b2=int(input('b2='))  
kompleks(a1,b1,a2,b2)

# from random import randint


# n=int(input('n='))
# son=[]
# for i in range(n):
#     son.append(randint(-10,2))
# print(son)
# man=[]
# for i in son:
#     if i<0:
#         man.append(i)
# d=max(man)
# print(d)