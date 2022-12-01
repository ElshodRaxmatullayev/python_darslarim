# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# if a<0 and b<0 and c<0 and d<0:
#     print(4)
# elif a<0 and b<0 and c<0 and d>0 or a<0 and b<0 and c>0 and d<0 or a<0 and b>0 and c<0 and d<0 or a>0 and b<0 and c<0 and d<0:
#     print(3)
# elif a<0 and b<0 and c>0 and d>0 or a<0 and b>0 and c<0 and d>0 or a<0 and b>0 and c>0 and d<0 or a>0 and b<0 and c<0 and d>0 or a>0 and b<0 and c>0 and d<0:
#     print(2)
# elif a<0 and b>0 and c>0 and d>0 or a>0 and b<0 and c>0 and d>0 or a>0 and b>0 and c<0 and d>0 or a>0 and b>0 and c>0 and d<0:
#     print(1)
# else:
#     print(0)
# s=[1,2,3,4,5,1]
# a=s[0]
# b=s[5]
# if a==b:
#     print(True)
# else:
#     print(False)
    

# class K:
#     def __init__(self,son1,son2,f):
#         self.son1=son1
#         self.son2=son2
#         self.f=f
#     def Hisobla(self):
#         if self.f=='+':

#             return self.son1+self.son2
#         elif self.f=='-':
#             return self.son1-self.son2
#         elif self.f=='*':
#             return self.son1*self.son2
#         else:
#             return self.son1/self.son2
# t1=K(son1=23,son2=24,f='*')
# print(t1.Hisobla())

# def natija(n):
#     s=0
#     k=1
#     for i in range(1,n+1):
#         k*=i
#         s+=(-1)**(i+1)*k
#     return s
# n=int(input())
# print(natija(n))
# def hisobla(n):
#     s=0
#     t=1
#     for i in range(1,n+1):
#         t*=(2*i-1)*(2*i)
#         s+=(-1)**(i)*t
#     return s
# n=int(input())
# print(hisobla(n))

# import math
# def qiymat(x,a):
#     if a>0:
#         y=x**x*(math.log(x)+1)
#     else:
#         print('takror urinib kuring')
#     return y
# x=float(input())
# a=int(input())
# print(qiymat(x,a))

# n=int(input('n='))
# a=[]
# for i in range(0,n):
#     b=[]
#     for j in range(0,n):
#         x=int(input())
#         b.append(x)
#     a.append(b)
# for i in range(0,n):
#     for j in range(0,n):
#         print(a[i][j],end=' ')
#     print()

# 3-movzu 9
# a1=int(input('a1='))
# a2=int(input('a2='))
# a3=int(input('a3='))
# a4=int(input('a4='))
# if a1==a2 and a2==a3 and a3!=a4:
#     n=4
# elif a2==a3 and a3==a4 and a4!=a1:
#     n=1
# elif a3==a4 and a4==a1 and a1!=a2:
#     n=2
# else:
#     n=3
# print(n)

# 4-movzu 9
# n=int(input('n='))
# son=[]
# k=0
# for i in range(n):
#     x=int(input())
#     son.append(x)
# for i in range(n):
#     if son[i]>n:
#         k+=1
# print(k,end=' ')

# 5-movzu 9
# n=int(input('n='))
# a=int(input('a='))
# b=int(input('b='))
# while n>7:
#     if 3*a+5*b==n:
#         print('a=',a,'b=',b)
#         break
#     else:
#         print('bu sonlar mos kelmadi')
#         break

# 7-movzu 9
# n = int(input("Ketma-ketlikdagi sonlar miqdori : "))
# a = []
# for i in range(n):
#     a.append(0)
# for i in range(n):
#     print("m",(i+1),end="=")
#     x = input()
#     a[i] = x
# p1=int(input("p1="))
# p2=int(input("p2="))
# s="0."
# for i in range(n):
#     s+=str(a[i])
# b=float(s)
# print("Natija : ",b*(10**(p1*p2)))

# # 8-movzu 9
# print("Massiv o`lchamlarni kiriting : ")
# n = int(input("n="))
# m = int(input("m="))
# print("Massiv elementlarini kiriting : ")
# mat = []
# for i in range(n):
#     col1 = []
#     for j in range(m):
#         col1.append(0)
#     mat.append(col1)
# for i in range(n):
#     for j in range(m):
#         print("[", i, ",", j, "]=", end="")
#         x = int(input())
#         mat[i][j] = x
# print("Matritsa : ")
# for i in range(n):
#     for j in range(m):
#         print(mat[i][j], end=" ")
#     print()
# k = 0
# s1 = 0
# for i in range(n):   # usundan tekshirish
#     for j in range(m):
#         s1 += mat[i][j]
#     for l in range(m):
#         if mat[i][l] > s1-mat[i][l]:
#             k += 1
# print("a) shart bo`yicha maxsus sonlar soni : ", k)
# s2 = 0
# s1 = 0
# k = 0
# for i in range(m):   # satrdan tekshirish
#     for j in range(n):
#         for a in range(j):
#             if mat[j][i] > mat[a][i]:
#                 s1 += 1
#         for b in range(j+1, n):
#             if mat[j][i] < mat[b][i]:
#                 s2 += 1
#     if s1 == j-1 and s2 == n-j-1:
#         k += 1
# print("b) shart bo`yicha maxsus sonlar soni : ", k)

# 2-movzu 16
# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# hisobla=bool(a+b>c and a+c>b and b+c>a)
# print(hisobla)

# 3-movzu 16
# k=int(input('k='))
# num=list(range(10,100))
# if k>=1 and k<=180:
#     print(num[k])
# else:
#     print('xatolik ruy berdi qaytadan kiriting')

# # 4-movzu 16
# n=int(input('n='))
# son=[]
# ekub=1
# for i in range(n):
#     x=int(input())
#     son.append(x)
# print(son,end=' ')
# print()
# for i in range(n-1):
#     if (son[i] < son[i + 1]):
#         while(True):
#             ekub = son[i + 1] - son[i]
#             if (ekub < son[i]):
#                 son[i + 1] = son[i]
#                 son[i] = ekub
#             elif (ekub > son[i]):
#                 son[i + 1] = ekub
#             else:
#                  break
#     elif (son[i] > son[i+1]):
#         while(True): 
#             ekub = son[i] - son[i + 1]
#             if (ekub < son[i + 1]):
#                 son[i] = son[i + 1]
#                 son[i + 1] = ekub
#             elif (ekub > son[i + 1]):
#                 son[i] = ekub
#             else:
#                  break
#     else:
#         ekub = son[i + 1]
#         break
#     son[i + 1] = ekub
# print(ekub)

# 5-movzu 16
# def ikkilik(p):
#     x=''
#     while p!=0:
#         x=(p%2)+x
#         p/=2
#     return x
# p=int(input('p='))
# print(ikkilik(p))

# 6-movzu 16
# import math
# def programma():
#     p=1
#     w=1
#     x1=[]
#     y1=[]
#     z1=[]
#     for i in range(1,4):
#         s=int(input())
#         x1.append(s)
#     for i in range(1,4):
#         s=int(input())
#         y1.append(s)
#     for i in range(1,4):
#         s=int(input())
#         z1.append(s)
#     for i in range(1,4):
#         p*=(1-y1[i]**2)
#     if p>0.5:
#         for i in range(1,4):
#             w*=math.sin(x1[i]+2)
#     else:
#         for i in range(1,4):
#             w*=(1-z1[i]**2)
#     print(w)
# programma()

# 5-movzu 16
# print('O\'nlik sanoq sistemasidagi sonni kiriting')
# n=int(input('n='))
# x=""
# t=n
# while t>0:
#     x=str(t%2)+x
#     t//=2
# print(x)
# x=' '
# r=str(x)
# t=n
# while (t != 0):
#     r = str(t % 8) + r
#     t /= 8
# print(f"Sakkizlik ko'rinishi : {r}")
# x = ""
# r=str(x)
# t = n
# while (t != 0):
#     if (t % 16 == 10):
#         r = 'A' + r
#     if (t % 16 == 11):
#         r = 'B' + r
#     if (t % 16 == 12):
#         r = 'C' + r
#     if (t % 16 == 13):
#         r = 'D' + r
#     if (t % 16 == 14):
#         r = 'E' + r
#     if (t % 16 == 15):
#         r = 'F' + r
#     elif (t % 16 < 10):
#         r = str(t % 16) + r
#         t /= 16
# print(f"O'n oltilik ko'rinishi : {r}")

# n=int(input('n='))
# x=''
# while n!=0:
#     t=n%2
#     x=str(t)+x
#     n/=2
# print(x)

# print('10 ta son uchun ixtiyoriy son kiriting:')
# a=int(input('a='))
# b=int(input('b='))
# if a<b:
#     a=b
# b=int(input('b='))
# if a<b:
#     a=b
# b=int(input('b='))
# if a<b:
#     a=b
# b=int(input('b='))
# if a<b:
#     a=b
# b=int(input('b=')) 
# if a<b:
#     a=b
# b=int(input('b='))
# if a<b:
#     a=b
# b=int(input('b='))
# if a<b:
#     a=b
# b=int(input('b='))
# if a<b:
#     a=b
# b=int(input('b=')) 
# if a<b:
#     a=b
# b=int(input('b='))
# if a<b:
#     a=b
# print('max=',a)

# 2-movzu 17
# x=int(input('x='))
# y=int(input('y='))
# natija=bool(y>=3 and y<=8 and x>=1 and x<=8)
# print(natija)

# n=3
# m=2
# son=[]
# for i in range(n):
#     b=[]
#     for j in range(m):
#         x=int(input())
#         b.append(x)
#     son.append(b)
# for i in range(n):
#     for j in range(m):
#         print(son[i][j],end=' ')
#     print()

# # 3-movzudan 17
# n=101001000
# k=int(input('k='))
# if k==1:
#     t=n//100000000
# elif k==2:
#     t=(n//10000000)%10
# elif k==3:
#     t=(n//1000000)%10
# elif k==4:
#     t=(n%1000000)//100000
# elif k==5:
#     t=(n%100000)//10000
# elif k==6:
#     t=(n%10000)//1000
# elif k==7:
#     t=(n%1000)//100
# elif k==8:
#     t=(n%100)//10
# elif k==9:
#     t=n%10
# print(t)

# 4-movzu 17
# n=int(input('n='))
# for i in range(2,n+1):
#     k=0
#     for j in range(1,i+1):
#         if i%j==0:
#             k+=1
#     if k==2:
#         print(i)

# 5-movzu 17
# " O'nlik Sanoq sistemasidan qolgan barcha sistemaga utkazish"
# print('O\'nlik sanoq sistemasidagi sonni kiriting')
# n=int(input('n='))
# x=''
# t=n
# while t!=0:
#     x=str(t%2)+x
#     t//=2
# print(f"ikkilik ko'rinishi : {x}")
# x=''
# t=n
# while t!=0:
#     x=str(t%3)+x
#     t//=3
# print(f"uchlik ko'rinishi : {x}") 
# x=''
# t=n
# while t!=0:
#     x=str(t%4)+x
#     t//=4
# print(f"To'rtlik ko'rinishi : {x}")  
# x=''
# t=n
# while (t != 0):
#     x = str(t % 8) + x
#     t //= 8
# print(f"Sakkizlik ko'rinishi : {x}")
# x = ''
# t = n
# while (t != 0):
#     if (t % 16 == 10):
#         x = 'A' + x
#     if (t % 16 == 11):
#         x = 'B' + x
#     if (t % 16 == 12):
#         x = 'C' + x
#     if (t % 16 == 13):
#         x = 'D' + x
#     if (t % 16 == 14):
#         x = 'E' + x
#     if (t % 16 == 15):
#         x = 'F' + x
#     elif (t % 16 < 10):
#         x = str(t % 16) + x
#     t //= 16
# print(f"O'n oltilik ko'rinishi : {x}")

# # 6-movzu 17
# import math
# def program(x):
#     e=0.001
#     a1=1/(1+x**2)-x
#     a2=3*(math.e**x)+x
#     a3=x*(math.log(1+x))-0.5
#     while a1>e and a2>e and a3>e:
#         if a1>a2 and a2>a3:
#             print('a3=',a3,'a2=',a2,'a1=',a1)
#         elif a2>a3 and a3>a1:
#             print('a1=',a1,'a3=',a3,'a2=',a2)
#         elif a1>a3 and a3>a2:
#             print('a2=',a2,'a3=',a3,'a1=',a1)
#         elif a2>a1 and a1>a3:
#             print('a3=',a3,'a1=',a1,'a2=',a2)
#         elif a3>a2 and a2>a1:
#             print('a1=',a1,'a2=',a2,'a3=',a3)
#         else:
#             print('a2=',a2,'a1=',a1,'a3=',a3)
# x=float(input('x='))
# program(x)

# # 2-movzudan 11
# import math
# p=int(input('p='))
# a=int(input('a='))
# b=int(input('b='))
# x=math.log2(math.tan(math.sqrt(2))+math.fabs(p))
# natija=bool(x>=a and x<=b)
# print(natija)

# # 3-movzudan 11
# x=float(input('x='))
# y=float(input('y='))
# z=float(input('z='))
# if x+y+z<1:
#     if x>y and y>z or y>x and x>z:
#         z=(x+y)/2
#         print('z=',z)
#     elif x>z and z>y or z>x and x>y:
#         y=(x+z)/2
#         print('y=',y)
#     elif y>z and z>x or z>y and y>x:
#         x=(z+y)/2
#         print('x=',x)
# else:
#     print('qaytadan kiriting')

# # 4-movzudan 11
# n=int(input('n='))
# x=[]
# s=1
# for i in range(0,n):
#     y=int(input())
#     x.append(y)
# l=1 
# ll=0
# s=0
# p=1
# for i in range(0,n):
#     t=i+l
#     if t<=n:
#         for j in range(ll,t):
#             s+=x[j]
#             ll+=1
#         l+=1
#         p*=s
#         s=0
# print(p)

# # 5-movzu 11
# i=1
# s=0
# l=0
# while(True):
#     print(i, " - son : ", end="")
#     x = int(input())
#     if x==0 : break
#     if i==2 or i==3 : s+=x
#     if i!=1 : 
#         for j in range(2,round(i**(1/2))+2):
#             if i%j!=0 : l+=1 
#     if l==round(i**(1/2)) : s+=x
#     l=0
#     i+=1
# print("Natija : ",s)

# print(s)

# # 7-movzu 11
# n = int(input("n = "))
# a = []
# for i in range(n):
#     a.append(0)
# for i in range(n):
#     print((i+1), " - son : ", end="")
#     x = int(input())
#     a[i] = x
# l=0
# for i in range(n-1):
#     if a[i+1]>a[i] : l+=1
# if l==n-1 : t=True
# else : t=False
# print("a) shart : ",t)
# for i in range(n):
#     if a[i]!=0 :
#         t=False
#         break
# l=0
# for i in range(0,n-1,2):
#     if a[i]>0 and a[i+1]<0:
#             l+=1
# if l==n-1 : t=True
# else : t=False
# print("b) shart : ",t)

# # 8-movzu 11
# n=int(input('n='))
# m=int(input('m='))
# son=[]
# for i in range(n):
#     a=[]
#     for j in range(m):
#         x=int(input())
#         a.append(x)
#     son.append(a)
# for i in range(n):
#     for j in range(m):
#         print(son[i][j],end=' ')
#     print()
# for i in range(n):
#     if son

# 8-movzudan 5
# n=int(input("Nuqtalar soni : "))
# arr = []
# for i in range(n):
#     col = []
#     for j in range(2):
#         col.append(0)
#     arr.append(col)
# print("Koordinatalarni kiriting : ")
# for i in range(n):
#     for j in range(2):
#         if j==0 :
#             print((i+1),"-nuqta x= ",end="")
#             x=int(input())
#             arr[i][j]=x
#         else :
#             print((i+1),"-nuqta y= ",end="")
#             x=int(input())
#             arr[i][j]=x
#     print()
# d = []
# for i in range(round(n*(n-1)/2)):
#     d.append(0)
# k=0
# for i in range(n):
#     for j in range(i+1,n):
#         d[k]=((arr[i][0]-arr[j][0])**2+(arr[i][1]-arr[j][1])**2)**(1/2)
#         k+=1
# print("Natija : ",max(d))

# # 3-movzudan 5
# print("Boshlang`ich koordinatalar : ")
# while(True):
#     k=int(input("k="))
#     if k>=1 and k<=8 : break
# while(True):
#     l=int(input("l="))
#     if l>=1 and l<=8 : break
# print("Oxirgi koordinatalar : ")
# while(True):
#     m=int(input("m="))
#     if m>=1 and m<=8 : break
# while(True):
#     n=int(input("n="))
#     if n>=1 and n<=8 : break
# if k==m or l==n : print("Bir yurishda o`tish mumkin !")
# else :
#     print("Bir yurishda o`tib bo`lmaydi !")
#     print("Yordamchi koordinatalar : ")
#     if k<m : 
#         print("( ",m," , ",l," ) ",end="")
#     else :
#         print("( ",k," , ",l," ) ",end="")
#     if l<n : 
#         print("( ",k," , ",n," )",end="")
#     else :
#         print("( ",k," , ",l," )",end="")

# # 8-movzu 17
# n=int(input('n='))
# arr=[]
# for i in range(n):
#     ar=[]
#     for j in range(n):
#         x=int(input())
#         ar.append(x)
#     arr.append(ar)
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j],end=' ')
#     print()

# 5-movzudan 5
# import math

# n=int(input('n='))
# x=float(input('x='))
# u=0
# e=0.0001
# while math.fabs(x)<1:
#     for i in range(1,n+1):
#         x=((-1)**(i)*(x**(2*i+1)))/(2*i+1)
#         u+=x
#         if x<e :
#             break
#     print(u)
#     break
    
# print("Elementlar soni n=",end="")
# n=int(input())
# arr=[]
# for i in range(n):
#     arr.append(0)
# print("Elementlarni kiriting : ")
# for i in range(1,n+1):
#     print(i,")",end=" ")
#     x=int(input())
#     arr[i-1]=x
# print("Kiritilgan massiv : ",arr)
# arr.sort()
# print("Tartiblangan massiv : ",arr)
# u=int(input("Izlanadigan son : "))
# try:
#     k=arr.index(u)
#     print("Izlangan sonning yangi tartib raqami : ")
#     print("k=",k+1)

# except:
#     print("Bunday element yo`q!")
#     print("Demak k=0")

# def utkazish(x):
#     s=''
#     k=''
#     k=str(hex(x))
#     k=k.replace("0x","")
#     return k
# x=int(input("1-son : "))
# y=int(input("2-son : "))
# amal=str(input("Amalni tanlang(*,+,-) : "))
# print("Natija : ",end=" ")
# if amal=='+':
#     print(utkazish(x+y))
# elif amal=='-':
#     print(utkazish(x-y))
# elif amal=='*':
#     print(utkazish(x*y))
# else : print("Xato amal !")


# import math
# def program(x):
#     E=0.0001
#     a1=1/(1+x**2)-x
#     a2=3*(math.e**x)+x
#     a3=x*(math.log(1+x))-0.5
#     if math.fabs(a1)>E and math.fabs(a2)>E and math.fabs(a3)>E:
#         if a1>a2 and a2>a3:
#             print('a3=',a3,'a2=',a2,'a1=',a1)
#         elif a2>a3 and a3>a1:
#             print('a1=',a1,'a3=',a3,'a2=',a2)
#         elif a1>a3 and a3>a2:
#             print('a2=',a2,'a3=',a3,'a1=',a1)
#         elif a2>a1 and a1>a3:
#             print('a3=',a3,'a1=',a1,'a2=',a2)
#         elif a3>a2 and a2>a1:
#             print('a1=',a1,'a2=',a2,'a3=',a3)
#         else:
#             print('a2=',a2,'a1=',a1,'a3=',a3)
# x=float(input('x='))
# program(x)

# # 6-movzu 16
# import math
# def progsss():
#     p=1
#     w=1
#     x1=list()
#     y1=list()
#     z1=list()
#     for i in range(1,4):
#         x=int(input())
#         x1.append(x)
#     for i in range(1,4):
#         y=int(input())
#         y1.append(y)
#     for i in range(1,4):
#         z=int(input())
#         z1.append(z)
#     for i in range(len(y1)):
#         p*=(1-(y1[i])**2)
#     if p>0.5:
#         for i in range(len(x1)):
#             w *= math.sin(x1[i] + 2)
#     else:
#         for i in range(len(z1)):
#             w*=(1-(z1[i])**2)
#     print(w)

# progsss()

# # 5-movzu 11
# i=1
# s=0
# l=0
# while(True):
#     print(i, " - son : ", end="")
#     x = int(input())
#     if x==0 : 
#         break
#     if i==2 or i==3 :
#         s+=x
#     if i!=1 : 
#         for j in range(2,round(i**(1/2))+2):
#             if i%j!=0 : 
#                 l+=1 
#     if l==round(i**(1/2)) : 
#         s+=x
#     l=0
#     i+=1
# print("Natija : ",s)

# n=int(input('n='))
# son=[]
# s=0
# for i in range(2,n):
#     x=int(input())
#     son.append(x)
# print(son)

# while(True):
#     for i in range(2,n):
#         k=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 k+=1
#         if k==2:
#             s+=son[i]
#     print(s)
#     break

# 2-movzu 4
# a1=int(input('a1='))
# b1=int(input('b1='))
# c1=int(input('c1='))
# a2=int(input('a2='))
# b2=int(input('b2='))
# c2=int(input('c2='))
# D=a1*b2-b1*a2
# delta_x=c1*b2-b1*c2
# delta_y=a1*c2-c1*a2
# x=D//delta_x
# y=D//delta_y
# print('x=',x,'y=',y)

# # 3-movzu 1
# import math
# x=int(input('x='))
# a1=((math.e)**x+(math.e)**(-x))//2
# a2=1+math.fabs(x)
# a3=(1+x**2)**x
# if a1>a2 and a2>a3:
#     print('a3=',a3,'a2=',a2,'a1=',a1)
# elif a2>a1 and a1>a3:
#     print('a3=',a3,'a1=',a1,'a2=',a2)
# elif a1>a3 and a3>a2:
#     print('a2=',a2,'a3=',a3,'a1=',a1)
# elif a2>a3 and a3>a1:
#     print('a1=',a1,'a3=',a3,'a2=',a2)
# elif a3>a2 and a2>a1:
#     print('a1=',a1,'a2=',a2,'a3=',a3)
# else:
#     print('a2=',a2,'a1=',a1,'a3=',a3)

# # 5-movzu 21
# a=int(input('a='))
# b=int(input('b='))
# a1=''
# t1=a
# i=0
# while t1!=0:
#     a1=str(t1%3)+a1
#     t1//=3
#     i+=1
# print(f"Uchlik kurinishidagi : {a1}")
# a2=''
# t2=b
# j=0
# while t2!=0:
#     a2=str(t2%3)+a2
#     t2//=3
#     j+=1
# print(f"Uchlik kurinishidagi : {a2}")
# if (int(a1))//(10**i)==(int(a2))//(10**j):
#     print('Mos tushadi ')
# else:
#     print('Mos tushmaydi')

# 6-movzu 21
# import math
# def Uchburchak(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6):
#     a1=math.sqrt((x1-x2)**2+(y1-y2)**2)
#     b1=math.sqrt((x2-x3)**2+(y2-y3)**2)
#     c1=math.sqrt((x1-x3)**2+(y1-y3)**2)
#     a2=math.sqrt((x4-x5)**2+(y4-y5)**2)
#     b2=math.sqrt((x5-x6)**2+(y5-y6)**2)
#     c2=math.sqrt((x4-x6)**2+(y4-y6)**2)
#     p1=(a1+b1+c1)//2
#     p2=(a2+b2+c2)//2
#     s1=math.sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1))
#     s2=math.sqrt(p2*(p2-a2)*(p2-b2)*(p2-c2))
#     if s1>s2:
#         return s1
#     else:
#         return s2
# x1=int(input('x1='))
# y1=int(input('y1='))
# x2=int(input('x2='))
# y2=int(input('y2='))
# x3=int(input('x3='))
# y3=int(input('y3='))
# x4=int(input('x4='))
# y4=int(input('y4='))
# x5=int(input('x5='))
# y5=int(input('y5='))
# x6=int(input('x6='))
# y6=int(input('y6='))
# print(Uchburchak(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6))

# # 8-movzudan 11
# print("Massiv o`lchamlarini kiriting : ")
# n=int(input("n="))
# m=int(input("m="))
# arr=[]
# for i in range(n):
#     col=[]
#     for i in range(m):
#         col.append(0)
#     arr.append(col)
# print("Massiv elementlarini kiriting : ")
# for i in range(n):
#     for j in range(m):
#         print("[",i,",",j,"]=",end="")
#         x=int(input())
#         arr[i][j]=x
#     print()
# print("\nKiritilgan massiv : ")
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=" ")
#     print()
# tartib=[]
# for i in range(n):
#     tartib.append(0)
# print("b shart uchun : ")
# for i in range(n):
#     for j in range(m):
#         tartib[i]+=arr[i][j]
# for i in range(n):
#     for j in range(n):
#         if(tartib[i]>tartib[j]):
#             col=arr[j]
#             arr[j]=arr[i]
#             arr[i]=col
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=" ")
#     print()
# tartib1=[]
# for i in range(n):
#     tartib1.append(arr[i][0])
# for i in range(n):
#     for j in range(n):
#         if(tartib1[i]<tartib1[j]):
#             col=arr[j]
#             arr[j]=arr[i]
#             arr[i]=col
# print("a shart uchun : ")
# for i in range(n):
#     for j in range(m):
#         print(arr[i][j],end=" ")
#     print()

# # 4-movzudan 18
# n=int(input('n='))
# for i in range(2,n+1):
#     k=0
#     for j in range(1,i+1):
#         if i%j==0:
#             k+=1
#     if k==2:
#         for t in range(1,n+1):
#             if n%t==0:
#                 if i==t:
#                     print(t,end=' ')



# # 5-movzudan 18
# m=int(input('m='))
# x=''
# k=0
# while m!=0:
#     x=str(m%2)+x
#     m//=2
#     k+=1
# print(x)
# y=''
# for i in x:
#     if i=='1':
#         y+="0"
#     else:
#         y+='1'
# print(y)
# s=0
# t=k-1
# for i in y:
#     s+=int(i)*(2**t)
#     t-=1
# print(s)
# 3-movzu 16
# k=int(input('k='))
# num=list(range(10,100))
# print(str(num))
# if k>=1 and k<=180:
#     print(num[k])
# else:
#     print('xatolik ruy berdi qaytadan kiriting')
# k=int(input('k='))
# x=''
# for i in range(10,100):
#     x+=str(i)
# print(x)
# print(x[k])

# # 4-movzudan 18
# import math
# n=int(input('n='))
# while n%2==0:
#     print(2,end=' ')
#     n//=2
#     break
# for i in range(3,int(math.sqrt(n+1)),2):
#     while n%i==0:
#         print(i,end=' ')
#         n//=i
#         break
# if n>2:
#     print(n)

#25
# x=int(input("x="))
# y=int(input("y="))
# d=bool(y>0)
# print(d)

#26
# x=int(input('x='))
# y=int(input('y='))
# c=(x+y)%2
# natija= c==0
# print(natija)

#27
# x=int(input('x='))
# y=int(input('y='))
# z=int(input('z='))
# l=int(input('l='))
# c=bool(x+y)%2
# s=bool(z+l)%2

import math
x1=int(input('x1='))
y1=int(input('y1='))
x2=int(input('x2='))
y2=int(input('y2='))
x3=int(input('x3='))
y3=int(input('y3=')) 
x4=int(input('x4='))
y4=int(input('y4='))
a=math.sqrt((x1-x2)**2+(y1-y2)**2)
b=math.sqrt((x3-x4)**2+(y3-y4)**2)
d1=math.sqrt((x3-x1)**2+(y3-y1)**2)
d2=math.sqrt((x2-x4)**2+(y2-y4)**2)
if x1==x2 and y2>y1 and x3==x4 and y3>y4:
    print('kvadrat')
elif d1==d2:
    print('To\'g\'riturtburchak')
elif x2>x1 and y2>y1 and x3>x4 and y3>y4:
    print('parallegram')
elif x2>x1 and y2>y1 and x3>x4 and y3>y4 and a==b:
    print('romb')

