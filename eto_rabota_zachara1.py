from time import time



# from itertools import count
# from random import randint
# import time   
# antanta=['Sovet union','America','Britan']
# print(antanta)
# print(antanta[1])
# print(antanta[1:3])
# antanta.append('Franch')
# print(antanta)
# oci={'main_country':'Germani','second':'Japan','third':'Itali'}
# print(oci)
# print(oci.keys())
# randint
# antanta_wins_in_the_ww2=True
# Germani_win_in_the_battle_of_stalingrat=False
# if antanta_wins_in_the_ww2:
#     pass
# else :
#     pass
# # while antanta_wins_in_the_ww2== True:
# #     pass
# count=0
# start_time = time.time()
# for i in range(10):
#     count+=i
# print(count)
# print(time.time() - start_time)
# class  Ancient_Slavs:
#     def __init__(self) -> None:
#         self.eyes_color='brown'
#         self.hair_color='dark'
#         ''.join 
# human=Ancient_Slavs()
# print(human)
# print(human.eyes_color)
#    100//33
# from tkinter import W


# def creator(func):
#     def wrapper():
#         print('before')
#         func()
#         print('after')
#     return wrapper

# @creator
# def print_name():
#     print('mike')

# print_name()        
q = (i for i in range(10))


def my_gen():
yield 1 
    yield 2
    yield 3
    
    
gen= my_gen()
    
    
for i in gen:
    print(i)    
def timer(n):
    print('Starting generator')
    while n > 0 :
        yield n
        n-=1
        
countdown=timer(3)        
print(countdown)        
        
for i in countdown:
    print(i)


