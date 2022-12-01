# k=int(input('k='))
# n=int(input('n='))
# for i in range(n):
#     print(k,' ')

#2
# a=int(input('a='))
# b=int(input('b='))
# n=0
# for i in range(b,a+1):
#     n+=1
#     print(i,end=' ')
# print(n)

#4
# n=float(input('n='))
# s=1
# for i in range(1,11):
#     s=n*i
#     print(s,end=' ')

#5
# n=int(input('n='))
# s=1
# for i in range(1,n+1):
#     s=(i/10)*10
#     print(s,end=' ')

#13
# n=int(input())
# s1=0
# s2=0
# for i in range(1,5*n+1):
#     if i%2==0:
#         s1+=(1+i/10)
#     else:
#         s2+=(1+i/10)
# print(s2-s1)
#14
# n=int(input())
# for i in range(1,n+1):
#     print(i**2,end=' ')
#15
# a=float(input())
# n=int(input())
# s=1
# for i in range(n):
#    s*=a
# print(s) 

#1
# import math
# n=int(input())
# s=0
# k=0
# for i in [1+i/10 for i in range(1,n+1)]:
#     s+=math.pow(-1,k)*i
#     k+=1
#     print(s)
# n=int(input())
# for i in range(1,n+1):
#     print(i**2,end=' ')
# n=int(input())
# a=int(input())
# s=1
# for i in range(1,n+1):
#     s+=a**i
# print(s)

# n=int(input())
# for i in range(1,n+1):
#     print(i,end=" ")

# n=int(input())
# for i in range(0,n+1,2):
#     print(i)

# n=int(input())
# s=0
# for i in range(n+1):
#     s=s+i
# print(s)

# n=int(input())
# s=0
# for i in range(0,n+1,2):
#     s=s+i
#     print(s)

# n=int(input())
# s=0
# for i in range(1,n+1,2):
#     s=s+i
#     print(s)


# n=int(input())
# s1=0
# for i in range(1,n+1,2):
#     s1=s1+i
# s2=0
# for i in range(0,n+1,2):
#     s2=s2+i
# print(s2-s1)

# a=int(input())
# n=int(input())
# for i in range(1,n+1):
#     s=a**i
#     print(s)



# a=int(input())
# n=int(input())
# k=0
# s=0
# for i in range(1,n+1):
#     k=a**i
#     s=s+k
#     print(s)


# n=int(input())
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,end=" ")

# n=int(input())
# s=0
# for i in range(1,n+1):
#     if i%2==1:
#         s=s+i
# print(s)


# n=int(input())
# i=1
# while i<n:
#      print(i)
#      i+=1





# n=int(input())
# i=1
# s=0
# while i<n:
#     s=s+i
#     i+=2
#      print(s)
# import math
# x=int(input('x='))
# y=int(input('y='))
# z=int(input('z='))
# b=y**(math.pow(math.fabs(x),1/3))+(math.cos(y)**3)*(math.fabs(x-y)*(1+(math.sin(z)**2)/math.sqrt(x+y)))/(math.e**(math.fabs(x-y))+x/2)
# print(b)

# import math
# x=int(input('x='))
# if x<-2:
#     y=math.cos(x)+3.215*math.sqrt(math.fabs(x+2))
# elif x>=-2 and x<=5:
#     y=(13.85**2)*math.cos(math.pi)
# elif x>5:
#     y=((x-2)**(2/3))*math.sin((math.pi*x)/2)
# print(y)

# n=int(input('n='))
# m=int(input('m='))
# a=[]
# for i in range(3,n-1):
#     b=[]
#     for j in range(2,m-3):
#         x=int(input())
#         b.append(x)
#     a.append(b)
# for i in range(3,n-1):
#     for j in range(2,m-3):
#         print(str(a[i][j]),end=' ')
#     print()
# p=1
# for i in range(3,n-1):
#     for j in range(2,m-3):
#         t=2*i+j
#     p*=t
# print(p)

# 3
# from random import randint
# def tasodifiy(n):
#     mas=[]
#     for i in range(n):
#         mas.append(randint(1,100))
#     print(mas,' ')
#     for i in range(n):
#         k=0
#         for j in range(i+1,n):
#             if i==j:
#                 k+=1
#         if k<1:
#             print(mas[i]," ")
# n=int(input('n='));
# tasodifiy(n)

# k=float(input('k='))
# soat=k//3600
# minut=k//60
# print('soat=',soat,'minut=',minut,'sekund=',k)

# def manfiy(n):
#     mas=[]
#     for i in range(n):
#         x=int(input())
#         mas.append(x)
#     k=0
#     for i in mas:
#         if i<0:
#             k+=1
#     return k
# n=int(input('n='))
# print(manfiy(n))

# from random import randint
# def miqdor(n):
#     mas=[]
#     for i in range(n):
#         mas.append(randint(1,10))
#     k=0
#     print(mas)
#     for i in range(n-2):
#         if mas[i+1]>mas[i] and mas[i+1]<mas[i+2]:
#             k+=1
#     return k
# n=int(input('n='))
# print(miqdor(n))

# s1=0
# s2=0
# n=int(input("n="))
# for i in range(1,n+1):
#     for l in range(1,round(i/2)+2):
#         if i%l==0:
#             s2+=l
#     for j in range(1,n+1):
#         for k in range(1,round(j/2)+2):
#             if j%k==0 :
#                 s1+=k
#         if(i==s2 and j==s1):
#             print(i," ",j)
#     s1=0
#     s2=0

# from random import randint

# massiv=[]
# for i in range(5):
#     mas=[]
#     for j in range(5):
#         mas.append(randint(1,9))
#     massiv.append(mas)
# print("Massiv Elementlari : ")
# for i in range(5):
#     for j in range(5):
#         print(massiv[i][j],end=' ')
#     print()
# print("Massivning 5- darajasi : ")

# nusxa=[]
# for i in range(5):
#     nusxa.append([0]*5)
# test=[]
# for i in range(5):
#     test.append([0]*5)
# nx=[]
# for i in range(5):
#     nx.append([0]*5)
# xxx=[]
# for i in range(5):
#     xxx.append([0]*5)

# for i in range(5):
#     for j in range(5): 
#         s=0 
#         for k in range(5): 
#             s += massiv[i][k]*massiv[j][k]
#         nusxa[i][j]=s

# for i in range(5):
#     for j in range(5): 
#         s=0 
#         for k in range(5): 
#             s += massiv[i][k]*massiv[j][k]
#         test[i][j]=s

# for i in range(5):
#     for j in range(5): 
#         s=0 
#         for k in range(5): 
#             s += nusxa[i][k]*test[j][k]
#         xxx[i][j]=s
# for i in range(5):
#     for j in range(5): 
#         s=0 
#         for k in range(5): 
#             s += xxx[i][k]*massiv[j][k]
#         nx[i][j]=s

# for i in range(5):
#     for j in range(5):
#         print(nx[i][j],end=' ')
#     print()

# import math

# n=int(input('n='))
# a=float(input('a='))
# b=float(input('b='))
# x=[a,]
# y=[b,]
# e=0.0001
# for i in range(1,n+1):
#     x.append((x[i-1]+y[i-1])//2)
#     y.append(math.sqrt(x[i-1]*y[i-1]))
# for i in range(1,n+1):
#     if math.fabs(x[i]-y[i])<e:
#         print(x[i]," ")
#         break

# def arfimitek(a1,b1,a2,b2,amal):
#     if amal=='+':
#         s1=a1+b1
#         s2=a2+b2
#     elif amal=='-':
#         s1=a1-b1
#         s2=a2-b2
#     elif amal=='*':
#         s1=a1*b1
#         s2=a2*b2
#     elif amal=='/':
#         s1=a1//b1
#         s2=a2//b2
#     return s1,s2
# a1=int(input('a1='))
# b1=int(input('b1='))
# a2=int(input('a2='))
# b2=int(input('b2='))
# amal=input()

# print(arfimitek(a1,b1,a2,b2,amal))

# def binomial(n, r):
#     p = 1    
#     for i in range(1, min(r, n - r) + 1):
#         p *= n
#         p //= i
#         n -= 1
#     return p
# n=int(input('n='))
# r=int(input('r='))
# print(binomial(n,r))

from random import randint
n=int(input('n='))
massiv=[]
for i in range(n):
    mas=[]
    for j in range(n):
        mas.append(randint(1,10))
    massiv.append(mas)
for i in range(n):
    for j in range(n):
        print(massiv[i][j],end=' ')
    print()
max=massiv[0][0]
l=0
for i in range(n):
    for j in range(n):
        if max<massiv[i][j]:
            max=massiv[i][j]
            l+=1
min=massiv[0][0]
t=0
for i in range(n):
    for j in range(n):
        if min>massiv[i][j]:
            min=massiv[i][j]
            t+=1
k=max*min
print(max,min)
print('k=',k)
