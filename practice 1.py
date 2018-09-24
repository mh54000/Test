# Q1
fruits = ["apple","pear","orange","pinapple","mandarin"]

# Q2
for i in range(len(fruits)):
    if fruits[i] == "apple" :
        print(" I found it !")

# Q3
fruits.append("banana"+"kiwi")
print(fruits)

# Q4
empty_fruits = []
for i in range(len(fruits)):
      empty_fruits.append(len(fruits[i]))
      print(str(fruits[i]) + " has " + str(empty_fruits[i]) + " letters" )


# Q5
def half_squared(start,end):
     start2 = float(start**2 / 2)
     end2 = float(end**2 / 2)
     return 'half_squared([' + str(start) + "," + str(end) + ")]" + " == "+ "[" + str(start2) + "," + str(end2) + "]"
print(half_squared(3,3))

# Q6
# 例题演练
# a = int(input("input first number: "))
# b = int(input("input second number: "))
# if (a > b):
#     print(a)
# else:
#     print(b)

# exercise
score_number = int(input("input your score: "))
if 100 >= score_number >= 90 :
     print('A')
elif 90 > score_number > 60:
     print('B')
elif 60 >= score_number >= 0:
     print('C')
else:
     print('it is wrong')

# Q7
def revsort(a,b,c):
    if a >= b:
        if a >= c:
            if b >= c:
                return (a,b,c)
            else:
                b,c = c,b
                return (a, b, c)
        else:
            a,b,c = c,a,b
            return (a, b, c)
    else:
        if a >= c:
            a,b = b,a
            return (a, b, c)
        else:
            if b >= c:
                a,b,c = b,c,a
                return (a, b, c)
            else:
                a,b,c = c,b,a
                return (a, b, c)

# print(revsort(8,10,7))

# Q8
list1 = [1,2,3]
list2 = [4,5,6]
array = [list1,list2]
for i in array:
    for j in i:
        print(j,end= ' ')

# Q9
a = [1,8,17]
sum = 0
def f(x):
    return x**3
for i in map(f,a):
    y = str(i)
    for j in range(len(y)):
        sum += int(y[j])
print(sum)

# Q10
import random
x = random.randint(1,10)
y = random.uniform(1,10)
x,y = y,x
print(x,y)

# Q11
m,b,c=1,1,1
for m in range(5):
    for b in range(5-m):
        print(" ",end="")
    for c in range(2*m-1):
        print("*",end='')
    print('')
for d in reversed(range(4)):
    for b in range(5 - d):
        print(" ", end="")
    for c in range(2 * d - 1):
        print("*", end='')
    print('')

# Q12
for i in range(1,7):
    for j in range(i,7):
        print(j,end="")
    for k in range(1,i):
        print(k,end="")
    print()

# Q13
players = "charles"
print(players.title())
players = ['charles','martina','michael','florence','eli']
for i in range(len(players)):
    print(players[i].capitalize(), end=" ")
