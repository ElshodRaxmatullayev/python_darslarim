# son=["izzat","*","/",388]
# print(son)

# son=["izzat","damir",38]
# son.append("izzat")
# print(son)

# n=int(input())
# s=[]
# k=0
# for i in range(1,n+1,2):
#     k=k+i
#     s.append(k)
# print(s)

# n=int(input())
# s=[]
# for i in range(1,n+1):
#     s.append(i**2)
# print(s,end=" ")


# n=int(input())
# a=[]
# s=0
# for i in range(1,n+1):
#     s=s+1 
#     a.append(s)
# print(a)


# n=int(input())
# a=[]
# for i in range(n+1,0,-1):
#     a.append(i)
# print(a)


# n=int(input())
# a=[]
# s=0
# for i in range(0,n+1,2):
#     s=s+i
# a.append(s)
# print(a)


# n=int(input())
# a=[]
# for i in range(0,n):
#     x=int(input())
#     a.append(x)
# print(a[::-1])

# sonlar1=[2,3,4,5,6]
# sonlar2=list(sonlar1)
# print(sonlar1)

# n=int(input())
# f=[1,1]
# for i in range(2,n):
#     f.append(f[i-2]+f[i-1])
# print(f)

# n=int(input('n='))
# a=int(input('a='))
# b=int(input('b='))
# s=[a,b]
# c=0
# k=0
# for i in range(2,n):
#     c=k+s[i-1]+s[i-2]
#     k+=s[i-2]
#     s.append(c)
# print(s)

# n=int(input())
# m=int(input())
# a=[]
# for i in range(0,n):
#     b=[]
#     for j in range(0,m):
#         x=int(input())
#         b.append(x)
#     a.append(b)
# for i in range(0,n):
#     for j in range(0,m):
#         print(a[i][j],end=' ')
#     print()
# for i in range(0,n):
#     sum=0
#     for j in range(0,m):
#         sum+=a[i][j]
#     print(sum,'\n')

# s=[2,3,4,5]
# t=tuple(s)
# print(s)
# print(t)
# tuple1=(10,30,20,50)
# tuple2=list(tuple1)
# tuple2.reverse()

# print(tuple(tuple2))

# n=int(input())
# ty=()
# r=list(ty)
# r.append(n)
# ty=tuple(r)
# print(ty)

# ty=(50,10,20,50,30,40,50)
# r=list(ty)
# print(r.count(50))

# tuple1=("Orange",[10,20,30],(5,15,25))
# print(tuple1[1][1])

# typel1=()
# typel2=list(typel1)
# typel2.append(50)
# typel1=tuple(typel2)
# print(typel1)


# t=()
# s=list(t)
# for i in range(1,11):
#     s.append(i)
# print(tuple(s))

# t1=("orange",[10,20,30],(5,15,25))
# print(t1[1][2]


# tuple1=(10,20,30,40)
# tuple2=list(tuple1)
# a,b,c,d=tuple2
# print(a,b,c,d)


# tuple1=(11,22)
# tuple2=(98,88)
# t1=list(tuple1)
# t2=list(tuple2)
# t3=list(t1)
# t4=list(t2)
# t5=[]
# for i in t3:
#     t5.append(i)
# t3.clear()
# for i in t4:
#     t3.append(i)
# t4.clear()
# for i in t5:
#     t4.append(i)
# t5.clear()
# print(t3,t4)

# t1=(11,22,33,44,55,66)
# print(t1[2:5])


# t1=(11,[22,33],44,55)
# t1[1][0]=222
# print()


# t1=(("a",23),("b",37),("c",11),("d",29))
# t2=list(t1)
# t3=sorted(t2)
# c=t3[0][1]
# t3[0][1]=t3[0][0]
# t3[0][0]=c
# print(t3)


# def M(a,b):
#     if a>b:
#         max=a
#         return max
#     else:
#         max=b
#         return max 
# a=int(input())
# b=int(input())
# print(M(a,b))

from unicodedata import name


# def M(n):
#     for i in range(0,n+1):
#         if i%2==1:
#             print(i)
# n=int(input())
# M(n)


def k(n):
    a=[]
    for i in range(n+1):
        a.append(i)
    print(a)
n=int(input())
k(n)