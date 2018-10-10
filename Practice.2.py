
#ex 1
for x in range (35):
    y= 35-x
    if 4*x + 2*y == 94:
        print("兔子有%s只，鸡有%s只"%(x,y),)


#ex 2
from collections import deque
def person_is_seller(name):
    return name[-1] == "m"

def main():
    search_queue = deque()
    search_queue += graph["you"]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
graph = {}
graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

if __name__ == '__main__':
    main()

# ex 3
import os
class ShenDu:
    def __init__(self,path):
        self.path=path
        self.MyList = []
        self.MyList.append(self.path)
    def BianLi(self):
        while len(self.MyList) != 0:
            path=self.MyList.pop()
            if os.path.isdir(path):
                print(path,".dll")
                myFileList = os.listdir(path)
                for line in myFileList:
                    myPath = path +"\\" + line
                    if os.path.isdir(myPath):
                        self.MyList.append(myPath)
                    else:
                        print(myPath,".dll")
            else:
                print(path,".dll")
    def __del__(self):
        pass
path = "C:\\"
file = ShenDu(path)
file.BianLi()
#
#
#  ex 4
import os
from collections import deque
class GuangDu:
    def __init__(self,path):
        self.path=path
        self.MyList = deque([])
        self.MyList.append(self.path)
    def BianLi(self):
        while len(self.MyList) != 0:
            path=self.MyList.popleft()
            if os.path.isdir(path):
                print(path,".dll")
                myFilePath = os.listdir(path)
                for line in myFilePath:
                    myPath = path +"\\" + line
                    self.MyList.append(myPath)
            else:
                print(path,".dll")
    def __del__(self):
        pass
path = "C:\\"
file = GuangDu(path)
file.BianLi()


# ex 5
import math
goal = 85
state = [-1] * (goal + 1)
state[2] = 0
for k in range(2 , int(goal/2) + 1):
    if state[k] < 0: continue
    for pos, cost in [
        (k*2, k),
        (k*2 + 1, math.floor(k/2)),
        (k*2+2, k+2)]:
        if pos > goal: continue
        if state[pos] == -1 or state[pos] > state[k] + cost:
          state[pos] = state[k] + cost
      # Possibly store k somewhere to build the solution.

print (state[goal])



# 附录 ex 3
## If your code meets the problem of WinError[5],please using try...except to deal the problem
# import os
# import fnmatch
# from collections import deque
# def get(path):
#
#         queue = deque()
#         queue.append(path)
#         while len(queue)>0:
#             temp = queue.popleft()
#             try:
#                 list = os.listdir(temp)
#             except WindowsError as e:
#                 pass
#             for filename in list:
#                 next = os.path.join(temp,filename)
#                 if os.path.isfile(next):
#                     if fnmatch.fnmatch(filename,'*.dll'):
#                         print (filename)
#                 elif os.path.isdir(next):
#                     queue.append(next)
#
# get('C:\\Users\zhangminghong\Desktop')