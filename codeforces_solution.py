import math

# n = 5
# num = 0
# mid_num = 3
# row_counter = 0
# column_counter = 1
# y = 0
#
# old_str = []
#
# for x in range(n):
#     input1 = input().split()
#     old_str += input1
#
# for u in range(len(old_str)):
#     row_counter += 1
#     if old_str[u] == "1":
#         if row_counter == 6:
#             row_counter = 1
#             column_counter += 1
#         y += abs((3 - row_counter))
#         break
#     if row_counter == 6:
#         row_counter = 1
#         column_counter += 1
#
# z = abs((3 - column_counter))
#
#
# print(y+z)


# ***HOW TO COME OUT FROM TWO LOOPS***

# d={'a':'A','b':'B'}
# inp="AAAb"
# for letter in inp:
#     for word in d:
#         if letter == word:
#             print(d[letter])
#             break
#     else:
#         continue
#     break

# no_of_stones = input()
# colour_of_stones = input()
#
# l = ['R', 'G', 'B']
# empty_str = ''
# empty = ''
#
# x = 0
# firstCounter = 0
# secondCounter = 1
#
# while secondCounter < len(colour_of_stones):
#
#     if colour_of_stones[firstCounter] == colour_of_stones[secondCounter]:
#         for element in l:
#             if element != colour_of_stones[firstCounter]:
#                 empty_str += colour_of_stones[firstCounter]
#                 empty_str += element
#                 break
#         empty = empty_str
#         empty_str += colour_of_stones[secondCounter:]
#         colour_of_stones = empty_str
#         empty_str = empty
#         empty = ''
#         firstCounter = secondCounter
#         secondCounter += 1
#         x += 1
#     else:
#         firstCounter += 1
#         secondCounter += 1
#         empty_str = colour_of_stones[0:secondCounter]
#
# print(x)

# no_of_stops = input()
# emp = []
# stri = []
# max_people = 0
# for x in range(int(no_of_stops)):
#     inp = input().split()
#     emp.append(inp)
#
# for num in emp:
#     for numbs in num:
#         stri.append(numbs)
#
# another_str = []
# first = 0
# second = 1
# q = 0
#
# while second < len(stri):
#     q += 1
#     sum = int(stri[first]) + int(stri[second])
#     second += 1
#     if sum > max_people:
#         max_people = sum
#     if second < len(stri):
#         diff = abs(sum - int(stri[second]))
#     else:break
#     second += 1
#     another_str.append(str(diff))
#     for element in stri[second:]:
#         another_str.append(element)
#     stri = another_str
#     another_str = []
#     first = 0
#     second = 1
#
# print(max_people)


# inp = input().split()
# x = 0
# age1 = int(inp[0])
# age2 = int(inp[1])
#
# while True:
#     age1 *= 3
#     age2 *= 2
#     x += 1
#     if age1 > age2:
#         print(x)
#         break

# inp = input().split()
# inp2 = input()
# a = int(inp[1])
#
# l = []
# first_pos = 0
# second_pos = 1
#
# for letter in inp2:
#     l.append(letter)
#
#
# for num in range(a):
#     while second_pos <= len(l) - 1:
#         if l[first_pos] == "B":
#             if l[second_pos] == "G":
#                 l[first_pos] = "G"
#                 l[second_pos] = "B"
#                 first_pos += 2
#                 second_pos += 2
#             else:
#                 first_pos+=1
#                 second_pos+=1
#
#         else:
#             first_pos += 1
#             second_pos += 1
#     first_pos = 0
#     second_pos = 1
#
# e = ''
# for char in l:
#     e+=char
#
# print(e)


# inp = input()
# inp = inp[1:-1]
# inp = inp.split(',')
# l=[]
# for letters in inp:
#     for num in letters:
#         if num not in l and num != ' ':
#             l.append(num)
# print(len(l))


# inp = int(input())
# x = 0
# y = True
# t = 0
# for num in range(inp):
#     inp1 = input().split()
#     y = True
#     while y:
#         if int(inp1[0]) < int(inp1[1]):
#             x = int(inp1[1]) - int(inp1[0])
#             print(x)
#             x = 0
#             y = False
#         elif int(inp1[0]) % int(inp1[1]) != 0:
#             t = int(inp1[0]) // int(inp1[1])
#             t += 1
#             x = (int(inp1[1])*t) - int(inp1[0])
#             print(x)
#             x = 0
#             t = 0
#             y = False
#         else:
#             print(x)
#             x = 0
#             y = False


# inp = int(input())
# for i in range(inp):
#     inp1 = int(input())
#     y = int(inp1 / 2) + 1
#     print(inp1 - y)


# inp = input().split()
# for x in range(1, int(inp[0]) + 1):
#     if x % 2 != 0:
#         print("#" * int(inp[1]))
#     elif x % 2 == 0 and (x // 2) % 2 == 0:
#         print("#" + "." * (int(inp[1]) - 1))
#     else:
#         print("." * (int(inp[1]) - 1) + "#")


# list = [1, 5, 10, 20, 100]
# inp = int(input())
#
# x = 0
# y = True
#
# counter_1 = 0
# counter_2 = 1
#
# while y:
#     if inp >= 100:
#         x += inp // 100
#         if inp % 100 == 0:
#             y = False
#         else:
#             inp = inp % 100
#             continue
#
#     elif inp in list:
#         x += 1
#         y = False
#
#     elif inp < list[counter_2] and inp > list[counter_1]:
#         x += inp // list[counter_1]
#         inp = inp % list[counter_1]
#         if inp == 0:
#             y = False
#         counter_1 = -1
#         counter_2 = 0
#
#     counter_1 += 1
#     counter_2 += 1
#
# print(x)


# VASYA THE HIPSTER
# inp = input().split()
# x = 0
# y = 0
#
# if int(inp[0]) > int(inp[1]):
#     x = inp[1]
#     y = (int(inp[0]) - int(inp[1])) // 2
#
# elif int(inp[0]) == int(inp[1]):
#     x = inp[0]
#     y = 0
#
# else:
#     x = inp[0]
#     y = (int(inp[1]) - int(inp[0])) // 2
#
# print(str(x) + ' ' + str(y))

# inp = int(input())
# l = []
# e = ''
# for x in range(inp):
#     inp1 = input()
#     for x in range(1, len(inp1) + 1):
#         if inp1[x - 1] != '0':
#             l.append((int(inp1[x - 1])) * (10 ** ((len(inp1)) - x)))
#     print(len(l))
#     for no in l:
#         e = e + str(no) + ' '
#     print(e)
#     l = []
#     e = ''

# inp = input()
# inp1 = input().split()
#
# best = inp1[0]
# worst = inp1[0]
# x = 0
#
# for num in range(1, len(inp1)):
#     if int(inp1[num]) > int(best):
#         best = inp1[num]
#         x += 1
#     elif int(inp1[num]) < int(worst):
#         worst = inp1[num]
#         x += 1
# print(x)


# inp = input().split()
# l = []
# a, b, c = 0, 0, 0
#
# l.sort()
# y = l[-1]
# l = l[:-1]
#
# a = y - l[0]
#
# for num in l:
#     if num == a:
#         l.remove(num)
#
# b = abs(a - l[1])
#
# c = y - (a + b)
#
# print(a,b,c)


# inp = int(input())
# l = []
# t = 0
# num = 0
# bol = True
#
# l.append(inp // 2)
# l.append(inp - (inp // 2))
# while bol:
#     for x in range(1, l[num] + 1):
#         if l[num] % x == 0:
#             t += 1
#             if t >= 3:
#                 break
#     if t >= 3:
#         num += 1
#         t = 0
#         if num == 2:
#             bol = False
#     else:
#         num = 0
#         t = 0
#         l[0] -= 1
#         l[1] += 1
#
# print(str(l[0]) + ' ' + str(l[1]))
# d={}
# inp0 = input('NAME : ')
# d[inp0] =[]
# inp1 = input('TOWER : ')
# d[inp0].append(inp1)
# inp2 = input('NUMBER : ')
# d[inp0].append(inp2)
# inp = []
# inp.append(inp0)
# inp.append(inp1)
# inp.append(inp2)
# l = []
# d = {}
# for num in inp:
#     key = inp[0]
#     l.append(inp[1])
#     l.append(inp[2])
#     break
#
# d[key] = l

# inp3 = input('Name : ')
# inp4 = input('Tower : ')
# inp5 = input('Number : ')

# inp = input().split()
# print(inp)
# d[inp[0]] = inp[1:]
# def tower(name,c):
#     return d[name][0]>c
#
# def no(name):
#     return d[name][1]
#
# def both(name):
#     return d[name]
#
# print(tower('b'))
# if inp4 == '0':
#     print(d[inp3][1])
# elif inp5 == '0':
#     print(d[inp3][0])
# else:
#     print(d[inp3])

# class details:
#     def __init__(self, name, tower, no):
#         self.name = name
#         self.tower = tower
#         self.no = no
#
#     def get_tower(self,p):
#         return self.tower > p
#
#     def get_no(self):
#         return self.no
#
# b = details('e', 3, 4)
# f = details('r', 4, 56)
#
# print(b.get_tower(4))
#
# inp = input().split()
# first_inp = int(inp[0])
# c = 0
# i = 2
# y = True
# while y:
#     if (int(inp[0]) % 10) != 0:
#         if int(inp[1]) == (int(inp[0])) % 10:
#             c += 1
#             y = False
#
#         else:
#             inp[0] = first_inp * i
#             i += 1
#             c += 1
#     else:
#         c+=1
#         y = False
#
# print(c)


# inp = input()
# inp1 = input().split()
# l = []
# for letter in inp1:
#     l.append(int(letter))
#
# police_officer = 0
# crimes = 0
# for num in l:
#     if num == -1:
#         if police_officer == 0:
#             crimes += 1
#         else:
#             police_officer -= 1
#     else:
#         police_officer += num
# print(crimes)

# inp = input().split()
# total = 0
# for x in range(3):
#     inp[x] = int(inp[x])
#
# inp = sorted(inp)
#
# total += abs(inp[1] - inp[0])
# total += abs(inp[2] - inp[1])
#
# print(total)

# inp = int(input())
# inp1 = input().split()
# total = 0
#
# for x in range(len(inp1)):
#     inp1[x] = int(inp1[x])
#
# inp1 = sorted(inp1)
#
# for c in range(len(inp1) - 1):
#     total += abs(inp1[-1] - inp1[c])
#
# print(total)

# inp = int(input())
# inp1 = input().split()
# total = 0
# inp1 = sorted(inp1)
# for x in range(len(inp1) - 1):
#     total += abs(int(inp1[-1]) - int(inp1[x]))
# print(inp1)

# inp = input().split()
# inp1 = input().split()
# l = []
# for x in range(int(inp[0])):
#     if abs(int(inp[1]) + int(inp1[x])) <= 5:
#         l.append(x)
#
# print(int(len(l)/3))

# stri = ''
# inp = int(input())
# for x in range(inp):
#     inp1 = input()
#     stri = inp1[0:2]
#     if len(inp1) <= 2:
#         print(inp1)
#     else:
#         for letter in range(2, len(inp1)):
#             if letter % 2 != 0:
#                 stri += inp1[letter]
#         print(stri)
#     stri = ''


# inp = int(input())
# l = []
# smallest = 0
# largest = 0
# for get_input in range(inp):
#     inp1 = int(input())
#     for num in range(1, inp1 + 1):
#         l.append(2 ** num)
#     largest += l[-1]
#     l.remove(l[-1])
#     for numb in range(int(inp1 / 2) - 1):
#         largest += l[numb]
#         l[numb] = 0
#     for remain_num in l:
#         smallest += remain_num
#     print(largest - smallest)
#     largest = 0
#     smallest = 0
#     l = []

# inp = input()
# inp1 = input().split()
# l = []
# counter = 0
# emp = ''
# for x in range(1, len(inp1) + 1):
#     for num in inp1:
#         counter += 1
#         if x == int(num):
#             l.append(counter)
#             counter = 0
#             break
# for c in l:
#     emp = emp + str(c) + ' '
# print(emp)

# inp = int(input())
# inp1 = input().split()
# l=[]
#
# for num in inp1:
#     l.append(int(num))
# inp1 = l
#
#
# counter_lar = 0
#
# counter_small = 0
#
#
# y = sorted(inp1)
#
# smallest = int(y[0])
# largest = y[-1]
#
# for num in range(len(inp1)):
#     if inp1[num] == largest:
#         counter_lar = num
#         break
#
# for t in range(len(inp1)):
#     if int(inp1[t]) == smallest:
#         counter_small = t
#
# if y[-1]==inp1[0] and y[0]==inp1[-1]:
#     print(0)
# elif y[-1]==inp1[0]:
#     print(((len(inp1)-1) - counter_small))
# elif counter_lar > counter_small:
#     print(counter_lar + ((len(inp1)-1) - (counter_small + 1)))
# else:
#     print(counter_lar + ((len(inp1)-1) - counter_small))


# inp = int(input())
# inp1 = input().split()
#
# list1 = []
# list2 = []
# list3 = []
# one_counter = 0
# two_counter = 0
# three_counter = 0
#
# no_of_1, no_of_2, no_of_3 = 0, 0, 0
#
# for num in inp1:
#     if num == '3':
#         no_of_3 += 1
#     elif num == '2':
#         no_of_2 += 1
#     else:
#         no_of_1 += 1
#
# l = [no_of_3, no_of_2, no_of_1]
# l = sorted(l)
# if l[0] == 0:
#     print(0)
# else:
#     print(l[0])
#     for num in range(len(inp1)):
#         if one_counter > l[0] and two_counter > l[0] and three_counter > l[0]:
#             break
#         if inp1[num] == '1' and one_counter <= l[0]:
#             list1.append(num + 1)
#             one_counter += 1
#         elif inp1[num] == '2' and two_counter <= l[0]:
#             list2.append(num + 1)
#             two_counter += 1
#         elif inp1[num] == '3' and three_counter <= l[0]:
#             list3.append(num + 1)
#             three_counter += 1
#
# for x in range(l[0]):
#     print(str(list1[x]) + ' ' + str(list2[x]) + ' ' + str(list3[x]))

#
# inp = int(input())
# for iter in range(inp):
#     inp1 = int(input())
#     l = input().split()
#     counter = 0
#     even = 0
#     odd = 0
#
#     if inp1 == 1 and int(l[0]) % 2 != 0:
#         counter = -1
#     if inp1 > 1:
#         for x in range(0, len(l)):
#             if int(l[x]) % 2 == 0:
#                 even += 1
#             if int(l[x]) % 2 != 0:
#                 odd += 1
#             if even == len(l) or odd == len(l):
#                 counter = -1
#                 break
#     if counter != -1:
#         for x in range(0, len(l)):
#             if x % 2 == 0 and int(l[x]) % 2 != 0:
#                 temp = int(l[x])
#                 for num in range(x + 1, len(l)):
#                     if int(l[num]) % 2 == 0:
#                         l[x] = l[num]
#                         l[num] = temp
#                         counter += 1
#                         break
#             elif x % 2 != 0 and int(l[x]) % 2 == 0:
#                 temp = int(l[x])
#                 for num in range(x + 1, len(l)):
#                     if int(l[num]) % 2 != 0:
#                         l[x] = l[num]
#                         l[num] = temp
#                         counter += 1
#                         break
#     print(counter)

