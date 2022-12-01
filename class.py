# class GM:
#     def __init__(self,nomi,narxi,tyili,rangi):
#         self.nomi=nomi
#         self.narxi=narxi
#         self.tyili=tyili
#         self.rangi=rangi
#     def nom(self):
#         return f'{self.nomi}'
#     def info(self):
#         return 'nomi:{}; narxi:{}; tyili:{}; rangi:{}; '.format(self.nomi , self.narxi , self.tyili , self.rangi)
#         # return f"{self.nomi},{self.narxi},{self.tyili},{self.rangi}"
# t1=GM(nomi="Ravon3",narxi=109,tyili=2019,rangi="qizil")
# print(t1.nom())


# class shaxs:
#     def __init__(self,ism,familiyasi,otasi_ism):
#         self.ism=ism
#         self.familiyasi=familiyasi
#         self.otasi_ism=otasi_ism
#     def ismi(self):
#         return f"ismi"
#     def familiya(self):
#         return f"familiya"
#     def otasi_ismi(self):
#         return f"otasi_ismi"
# t1=shaxs(ism="Damir",familiyasi="Garifullin",otasi_ism="Aydarovich")
# print(t1.ismi())
# print(t1.familiya())
# print(t1.otasi_ismi())    

#1
# n=int(input())
# k=int(input())
# for i in range(n):
#     print(k, end=' ')

#2
# a=int(input())
# b=int(input())
# n=0
# for i in range(b,a+1):
#     print(i,end=' ')
#     n+=1
# print(n)

#3
# a=int(input())
# b=int(input())
# n=0
# for i in range(b,a,-1):
#     print(i,end=' ')
#     n+=1
# print(n)

#4
# n=float(input())
# for i in range(1,11):
#     k=n*i
#     print(k,end=' ')

#5
# n=float(input())
# for i in [i/10 for i in range(1,11)]:
#     k=n*i
#     print(k,end=' ')

#1
# a=int(input())
# b=int(input())
# while  a>b:
#     s=a-b
#     a=s
# print(s)

#2
# a=int(input())
# b=int(input())
# k=0
# while  a>b:
#     s=a-b
#     a=s
#     k+=1
# print(k)

#3
# n=int(input())
# k=int(input())
# t=0
# while n>k:
#     s=n-k
#     n=s
#     t+=1
# print(s,t)

#5
# n=int(input())
# k=1
# while 2**k!=n:
#     k+=1
# print(k)

#4
# n=int(input())
# k=1
# while 3**k!=n:
#     k+=1
# print(True)

#1
# def ka(x):
#     if x<0:
#         return -1
#     elif x==0:
#         return 0
#     else:
#         return 1
# a=int(input())
# b=int(input())
# print(ka(a))
# print(ka(b))

#2
# def funk(a,b,c):
#     d=b**2-4*a*c
#     if d>0:
#         return 2
#     elif d==0:
#         return 1
#     else:
#         return 0
# a=int(input())
# b=int(input())
# c=int(input())
# print(funk(a,b,c))

#3
# import math
# def doira(r):
#     s=math.pi*r**2
#     return s
# r1=int(input())
# r2=int(input())
# r3=int(input())
# print(doira(r1))
# print(doira(r2))
# print(doira(r3))

#4
# import math
# def doir(r1,r2):
#     s=math.pi*(r1**2-r2**2)
#     return s
# r1=int(input())
# r2=int(input())
# print(doir(r1,r2))

#1
# class User:
#     def __init__(self,ism,foydalanuvchi_ismi,email):
#         self.ism=ism
#         self.foydalanuvchi_ismi=foydalanuvchi_ismi
#         self.email=email
    
#     def ismi(self):
#         return f'ismi: {self.ism}'
    
#     def foy(self):
#         return f'foydalanuvchi: {self.foydalanuvchi_ismi}'
    
#     def emal(self):
#         return f'email: {self.email}'
#     def get_info(self):
#         return f"Foydalanuvchi: {self.foydalanuvchi_ismi}, {self.ism} , {self.email}"
# t1=User(foydalanuvchi_ismi='alijon1994',ism='Izzat farmonov',email='izzat2006@gmail.com')
# print(t1.get_info())
# print(t1.ismi())
# print(t1.foy())
# print(t1.emal())
