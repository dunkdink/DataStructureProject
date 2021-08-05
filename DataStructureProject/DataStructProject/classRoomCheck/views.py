from django.shortcuts import render
from django.http import HttpResponse
from DataStructProject import urls
import time
# Create your views here.


""" Creat a Suitable Class"""

class Stack:
    def __init__(self, lis = None):
        if lis == None:
            self.items = []
        else:
            self.items = lis
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def push(self, i):
        self.items.append(i)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def peek2(self):
        return self.items[-2]
    def peekFull(self):
        return self.items

class Node:
    def __init__(self, data, next = None, prev = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
        if prev is None:
            self.prev = None
        else:
            self.prev = prev

    def __str__(self):
        return str(self.data)



class DoublyLk:
    def __init__(self):
        self.font = Node(None)
        self.back = Node(None)
        self.head = self.font
        self.tail = self.back
        self.font.next = self.back
        self.font.prev = None
        self.back.prev = self.font
        self.back.next = None
    def __str__(self):
        t = self.font
        strt = ""
        if t.next is None:
            return strt
        else:
            while t.next is not self.back:
                t = t.next
                strt += str(t.data) + " "
            return strt

    def getlst(self):
        lis = []
        t = self.font
        if t.next is None:
            return lis
        else:
            while t.next is not self.back:
                t = t.next
                lis.append(t.data)
            return lis

    def reversedStr(self):
        t = self.back
        strt = ""
        if t.prev is self.font:
            return strt
        else:
            while t.prev != self.font:
                t = t.prev
                strt += str(t.data) + " "
            return strt

    def isEmpty(self):
        return self.font.next == None

    def size(self):
        t = self.font
        count = 0
        if self.isEmpty():
            return count
        else:
            while t.next is not self.back:
                t = t.next
                count += 1
            return count                    

    def append(self,data):
        t = self.font
        p = Node(data)
        if self.isEmpty():
            self.font.next = p
            p.prev = self.font
            self.back.prev = p
            p.next = self.back
        else:
            while t != self.back:
                t = t.next
            p.next = self.back
            p.prev = self.back.prev
            self.back.prev.next = p
            self.back.prev = p

    def addHead(self, data):
        t = self.font
        p = Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            p.next = self.font.next
            p.prev = self.font
            self.font.next.prev = p
            self.font.prev = None
            self.font.next = p

    def search(self, data):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return "Not Found"
        else:
            while t.next is not self.back:
                if t.data == data:
                    return count
                else:
                    t = t.next
                    count += 1
            if t.data == data:
                return count
            else:
                return "Not Found"

    def index(self, items):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return -1
        else:
            while t is not self.back:
                if t.data == items:
                    return count
                else:
                    t = t.next
                    count += 1
            return count 

    def pop(self, index):
        t = self.font.next
        count = 0
        if self.isEmpty():
            return "Empty"
        else:
            while t is not self.back:
                if self.index(t.data) == index:
                    break
                else:
                    t = t.next
            if t is not self.back:
                t.prev.next = t.next
                t.next.prev = t.prev
                t.next = None
                t.prev = None
            else:
                return "Out of Range"

    def insert(self , index, data):
        t = self.font.next
        p = Node(data)
        if self.isEmpty():
            self.addHead(data)
        else:
            while t is not self.back:
                if self.index(t.data) == index:
                    break
                else:
                    t = t.next
            if t is not self.back:
                p.next = t
                p.prev = t.prev
                t.prev.next = p
                t.prev = p
            else:
                t = t.prev
                self.append(data)


class NodeBsT:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = NodeBsT(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = NodeBsT(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = NodeBsT(data)
                        break
                    curr = curr.right
        return self.root

    def max(self):
        if self.root is None:
            return
        curr = self.root
        while curr.right is not None:
            curr = curr.right
        return curr.data

    def min(self):
        if self.root is None:
            return
        curr = self.root
        while curr.left is not None:
            curr = curr.left
        return curr.data

    def mult(self, k, multiplier):  # bfs then multiply
        q = Queue()
        q.enqueue(self.root)
        while not q.is_empty():
            curr = q.dequeue()
            if curr.data > k:
                curr.data = curr.data*multiplier
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)

    def bfs(self):
        if self.root is None:
            return "Empty Tree"
        q = Queue()
        q.enqueue(self.root)
        out = "Breadth : "
        while not q.is_empty():
            curr = q.dequeue()
            out += str(curr.data) + ' '
            if curr.left is not None:
                q.enqueue(curr.left)
            if curr.right is not None:
                q.enqueue(curr.right)
        return out

    def print_tree(self, node, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)


pre = 'Preorder : '
post = 'Postorder : '
allStudent = Stack()


def preorder(curr):
    global pre
    if curr is not None:
        pre += str(curr.data) + ' '
        preorder(curr.left)
        preorder(curr.right)


def inorder(curr):
    global allStudent
    if curr is not None:
        inorder(curr.left)
        allStudent.push(curr.data)
        inorder(curr.right)


def postorder(curr):
    global post
    if curr is not None:
        postorder(curr.left)
        postorder(curr.right)
        post += str(curr.data)+' '

""" Initial """



buffer = Stack()
buffer2 = Stack()
buffer3 = Stack()
buffer4 = Stack()
buffer5 = Stack()
buffer6 = Stack()
# allStudent = Stack()
allStudentBST = BST()
allStudentDataBase_Stack = Stack()
allId = Stack()
#studentInData = Stack()
studentInData = DoublyLk()
studentInComnet = DoublyLk()
studentInComOrg = DoublyLk()
studentInEpp = DoublyLk()
studentInProb = DoublyLk()
addFormed = False
datafileisEmpty = False
comNetfileisEmpty = False
comOrgfileisEmpty = False
ePPfileisEmpty = False
probfileisEmpty = False


"""" Read TXT File"""

######################################################################################## ตรวจว่า file ว่างรึเปล่า ####################################################################
fl = open('studentInData.txt', encoding="utf8")
while True:
    s = fl.readline()
    if s == '':
        break
    buffer2.push(s)
fl.close()

cnl = open('studentInComnet.txt', encoding="utf8")
while True:
    s = cnl.readline()
    if s == '':
        break
    buffer3.push(s)
cnl.close()

col = open('studentInComOrg.txt', encoding="utf8")
while True:
    s = col.readline()
    if s == '':
        break
    buffer4.push(s)
col.close()

epl = open('studentInEpp.txt', encoding="utf8")
while True:
    s = epl.readline()
    if s == '':
        break
    buffer5.push(s)
epl.close()

prl = open('studentInProb.txt', encoding="utf8")
while True:
    s = prl.readline()
    if s == '':
        break
    buffer6.push(s)
prl.close()
######################################################################################## ตรวจว่า file ว่างรึเปล่า ####################################################################

if buffer2.isEmpty():
    datafileisEmpty = True
else:
    pass

if buffer3.isEmpty():
    comNetfileisEmpty = True
else:
    pass

if buffer4.isEmpty():
    comOrgfileisEmpty = True
else:
    pass

if buffer5.isEmpty():
    ePPfileisEmpty = True
else:
    pass

if buffer6.isEmpty():
    probfileisEmpty = True
else:
    pass


######################################################################################## ตรวจว่า file ว่างรึเปล่า ####################################################################


######################################################################################## Upload file เข้า Stack ##################################################################

if datafileisEmpty == False:
    rl = open('studentInData.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            break
        studentInData.append(s)
    rl.close()
else:
    pass

if comNetfileisEmpty == False:
    rl = open('studentInComnet.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            break
        studentInComnet.append(s)
    rl.close()
else:
    pass

if comOrgfileisEmpty == False:
    rl = open('studentInComOrg.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            print("hi")
            break
        studentInComOrg.append(s)
    rl.close()
else:
    pass

if ePPfileisEmpty == False:
    rl = open('studentInEpp.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            print("hi")
            break
        studentInEpp.append(s)
    rl.close()
else:
    pass

if probfileisEmpty == False:
    rl = open('studentInProb.txt', encoding="utf8")
    while True:
        s = rl.readline()
        if s == '':
            print("hi")
            break
        studentInProb.append(s)
    rl.close()
else:
    pass

######################################################################################## Upload file เข้า Stack ##################################################################

f = open('studentDataBase.txt', encoding="utf8")
while True:
    s = f.readline()

    if s == '': # check file end
        break
    # spliting line to key and value
    d = s.split()
    if d == '':
        pass
    else:
        buffer.push(d)
f.close()
for i in buffer.items:
    ID = i[0]
    nameS = i[1]
    surName = i[2]
    fullName = str(ID) + " " + str(nameS) + " " + str(surName)
    allStudentBST.insert(fullName)
    if allStudent.isEmpty():
        pass
    else:
        while not allStudent.isEmpty():
            allStudent.pop()
    inorder(allStudentBST.root)
for i in buffer.items:
    allId.push(i[0])


print(allStudent.items)
print(studentInData.getlst())

def updateStudentData():
    temp = Stack()
    f = open('studentDataBase.txt', encoding="utf8")
    while True:
        s = f.readline()

        if s == '': # check file end
            break
        # spliting line to key and value
        d = s.split()
        if d == '':
            pass
        else:
            temp.push(d)
    f.close()
    for i in temp.items:
        ID = i[0]
        nameS = i[1]
        surName = i[2]
        fullName = str(ID) + " " + str(nameS) + " " + str(surName)
        allStudentBST.insert(fullName)
        if allStudent.isEmpty():
            pass
        else:
            while not allStudent.isEmpty():
                allStudent.pop()
        inorder(allStudentBST.root)
    if allId.isEmpty():
        pass
    else:
        while not allId.isEmpty():
            allId.pop()
    for i in temp.items:
        allId.push(i[0])






####################################################################################### Views CoreFunction #############################################################################################

def helloUser(request):
    return render(request,'userContact.html')


def information(request):
    numinclass = allStudent.size()
    allClass = Stack(['DataStructure2564',
    'ComputerNetwork2564',
    'ComputerOrganized2564',
    'Probability and Statistic2564',
    'English for Professional Purpose2564'])
    return render(request,'index.html',
    {
        'className':'Data Structure 2564',
        'student':'62010465 นรวิชญ์ อยู่บัว',
        'allClass':allClass.items,
        'numinClass':numinclass
    })


def allStudentName(request):
    return render(request,'allstudent.html',
    {
        'student':'62010465 นรวิชญ์ อยู่บัว',
        'allStudent':allStudent.items
    })

def dataStructlogin(request):
    return render(request,'dataStructlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInData':studentInData.getlst()})

def comNetlogin(request):
    return render(request,'comNetlogin.html',{'allStudent':allStudent.items,'addFormed':addFormed, 'studentInComnet':studentInComnet.getlst()})


def comOrglogin(request):
    return render(request,'comOrglogin.html',{'allStudent':allStudent.items,'addFormed':addFormed,'studentInComOrg':studentInComOrg.getlst()})

def ePPlogin(request):
    return render(request,'epplogin.html',{'allStudent':allStudent.items,'addFormed':addFormed,'studentInEpp':studentInEpp.getlst()})


def problogin(request):
    return render(request,'problogin.html',{'allStudent':allStudent.items,'addFormed':addFormed,'studentInProb':studentInProb.getlst()})


########################################################################## ส่วน login Data ############################################################################################


def dataStructloginAddIDandName(request):
    registerSucess = False
    alreadyRegister = False
    addFormed = True
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
            'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        idandNameOnly = str(idS) + " " + str(name)
        timePlusIdname = str(idS) + " " + str(name) + " login at " + " " + str(time_string)
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInData.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInData.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
                break
            else:
                pass
        if alreadylogin == False and noInDataBase == False:
            if studentInData.isEmpty():
                f = open('studentInData.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInData.append(timePlusIdname)
            else:
                f = open('studentInData.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInData.append(timePlusIdname)
            addFormed = False
        else:
            pass
    
        return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
            'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def dataStructlogout(request):
    registerSucess = False
    addFormed = True
    alreadyRegister = False
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
            'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInData.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInData.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
            else:
                pass
        if alreadylogin == True and noInDataBase == False:
            # f = open('studentInData.txt', 'a', encoding="utf8")
            # f.write(timePlusIdname + '\n')
            # print('Writing to file completed')
            # f.close()
            # studentInData.push(timePlusIdname)
            for i in studentInData.getlst():
                a = i.split()
                if a[0] == idS:
                    studentInData.pop(studentInData.search(i))
            f = open('studentInData.txt', 'w', encoding="utf8")
            for i in studentInData.getlst():
                f.write(i + '\n')
            f.close()
            addFormed = False
        else:
            pass
    
        return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
            'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def registerIDdata(request):
    idS = request.POST['studentID']
    name = request.POST['studentName']
    alreadylogin = False
    noInDataBase = False
    alreadyRegister = False
    registerSucess = False
    ############################################################################ สร้าง Sorted
    if idS == '' or name  == '':
        return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
            'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        if idS in allId.items:
            alreadyRegister = True
            return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
            'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
        else:
            registerSucess = True
            fullName = str(idS) + " " + str(name)
            allStudentBST.insert(fullName)
            allId.push(idS)
            allStudent.push(fullName)
            f = open('studentDataBase.txt', 'a', encoding="utf8")
            f.write(fullName + '\n')
            f.close()
            return render(request,'dataStructlogin.html',{'studentInData':studentInData.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
            'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})


    


########################################################################## ส่วน login Data ############################################################################################

########################################################################## ส่วน login Comnet ############################################################################################

def comNetloginAddIDandName(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        idandNameOnly = str(idS) + " " + str(name)
        timePlusIdname = str(idS) + " " + str(name) + " login at " + " " + str(time_string)
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInComnet.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInComnet.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
                break
            else:
                pass
        if alreadylogin == False and noInDataBase == False:
            if studentInComnet.isEmpty():
                f = open('studentInComnet.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInComnet.append(timePlusIdname)
            else:
                f = open('studentInComnet.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInComnet.append(timePlusIdname)
            addFormed = False
        else:
            pass
        return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def comNetlogout(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInComnet.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInComnet.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
            else:
                pass
        if alreadylogin == True and noInDataBase == False:
            # f = open('studentInData.txt', 'a', encoding="utf8")
            # f.write(timePlusIdname + '\n')
            # print('Writing to file completed')
            # f.close()
            # studentInData.push(timePlusIdname)
            for i in studentInComnet.getlst():
                a = i.split()
                if a[0] == idS:
                    studentInComnet.pop(studentInComnet.search(i))
            f = open('studentInComnet.txt', 'w', encoding="utf8")
            for i in studentInComnet.getlst():
                f.write(i)
            f.close()
            addFormed = False
        else:
            pass
    
        return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def registerIDcomNet(request):
    idS = request.POST['studentID']
    name = request.POST['studentName']
    alreadylogin = False
    noInDataBase = False
    alreadyRegister = False
    registerSucess = False
    ############################################################################ สร้าง Sorted
    if idS == '' or name  == '':
        return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        if idS in allId.items:
            alreadyRegister = True
            return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
        else:
            registerSucess = True
            fullName = str(idS) + " " + str(name)
            allStudentBST.insert(fullName)
            allId.push(idS)
            allStudent.push(fullName)
            f = open('studentDataBase.txt', 'a', encoding="utf8")
            f.write(fullName + '\n')
            f.close()
            return render(request,'comNetlogin.html',{'studentInComnet':studentInComnet.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})


########################################################################## ส่วน login Comnet ############################################################################################



########################################################################## ส่วน login ComOrg ############################################################################################


def comOrgloginAddIDandName(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        idandNameOnly = str(idS) + " " + str(name)
        timePlusIdname = str(idS) + " " + str(name) + " login at " + " " + str(time_string)
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInComOrg.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInComOrg.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
                break
            else:
                pass
        if alreadylogin == False and noInDataBase == False:
            if studentInComOrg.isEmpty():
                f = open('studentInComOrg.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInComOrg.append(timePlusIdname)
            else:
                f = open('studentInComOrg.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInComOrg.append(timePlusIdname)
            addFormed = False
        else:
            pass
    
        return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def comOrglogout(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInComOrg.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInComOrg.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
            else:
                pass
        if alreadylogin == True and noInDataBase == False:
            # f = open('studentInData.txt', 'a', encoding="utf8")
            # f.write(timePlusIdname + '\n')
            # print('Writing to file completed')
            # f.close()
            # studentInData.push(timePlusIdname)
            for i in studentInComOrg.getlst():
                a = i.split()
                if a[0] == idS:
                    studentInComOrg.pop(studentInComOrg.search(i))
            f = open('studentInComOrg.txt', 'w', encoding="utf8")
            for i in studentInComOrg.getlst():
                f.write(i)
            f.close()
            addFormed = False
        else:
            pass
    
        return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def registerIDcomOrg(request):
    idS = request.POST['studentID']
    name = request.POST['studentName']
    alreadylogin = False
    noInDataBase = False
    alreadyRegister = False
    registerSucess = False
    ############################################################################ สร้าง Sorted
    if idS == '' or name  == '':
        return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        if idS in allId.items:
            alreadyRegister = True
            return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
        else:
            registerSucess = True
            fullName = str(idS) + " " + str(name)
            allStudentBST.insert(fullName)
            allId.push(idS)
            allStudent.push(fullName)
            f = open('studentDataBase.txt', 'a', encoding="utf8")
            f.write(fullName + '\n')
            f.close()
            return render(request,'comOrglogin.html',{'studentInComOrg':studentInComOrg.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})


########################################################################## ส่วน login Comorg ############################################################################################



########################################################################## ส่วน login Epp ############################################################################################


def ePPloginAddIDandName(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        idandNameOnly = str(idS) + " " + str(name)
        timePlusIdname = str(idS) + " " + str(name) + " login at " + " " + str(time_string)
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInEpp.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInEpp.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
                break
            else:
                pass
        if alreadylogin == False and noInDataBase == False:
            if studentInEpp.isEmpty():
                f = open('studentInEpp.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInEpp.append(timePlusIdname)
            else:
                f = open('studentInEpp.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInEpp.append(timePlusIdname)
            addFormed = False
        else:
            pass
    
        return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def ePPlogout(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInEpp.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInEpp.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
            else:
                pass
        if alreadylogin == True and noInDataBase == False:
            # f = open('studentInData.txt', 'a', encoding="utf8")
            # f.write(timePlusIdname + '\n')
            # print('Writing to file completed')
            # f.close()
            # studentInData.push(timePlusIdname)
            for i in studentInEpp.getlst():
                a = i.split()
                if a[0] == idS:
                    studentInEpp.pop(studentInEpp.search(i))
            f = open('studentInEpp.txt', 'w', encoding="utf8")
            for i in studentInEpp.getlst():
                f.write(i)
            f.close()
            addFormed = False
        else:
            pass
    
        return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def registerIDePP(request):
    idS = request.POST['studentID']
    name = request.POST['studentName']
    alreadylogin = False
    noInDataBase = False
    alreadyRegister = False
    registerSucess = False
    ############################################################################ สร้าง Sorted
    if idS == '' or name  == '':
        return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        if idS in allId.items:
            alreadyRegister = True
            return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
        else:
            registerSucess = True
            fullName = str(idS) + " " + str(name)
            allStudentBST.insert(fullName)
            allId.push(idS)
            allStudent.push(fullName)
            f = open('studentDataBase.txt', 'a', encoding="utf8")
            f.write(fullName + '\n')
            f.close()
            return render(request,'epplogin.html',{'studentInEpp':studentInEpp.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})


########################################################################## ส่วน login Epp ############################################################################################


########################################################################## ส่วน login Prob ############################################################################################

def probloginAddIDandName(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        idandNameOnly = str(idS) + " " + str(name)
        timePlusIdname = str(idS) + " " + str(name) + " login at " + " " + str(time_string)
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInProb.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInProb.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
                break
            else:
                pass
        if alreadylogin == False and noInDataBase == False:
            if studentInProb.isEmpty():
                f = open('studentInProb.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInProb.append(timePlusIdname)
            else:
                f = open('studentInProb.txt', 'a', encoding="utf8")
                f.write(timePlusIdname + '\n')
                print('Writing to file completed')
                f.close()
                studentInProb.append(timePlusIdname)
            addFormed = False
        else:
            pass
    
        return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})


def problogout(request):
    alreadyRegister = False
    registerSucess = False
    addFormed = True
    idS = request.POST['studentID']
    name = request.POST['studentName']
    if idS == '' or name  == '':
        alreadylogin = False
        noInDataBase = False
        return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        alreadylogin = False
        noInDataBase = False
        classEmpty = False
        if studentInProb.isEmpty():
            classEmpty = True
        else:
            pass
        if idS in allId.items:
            pass
        else:
            noInDataBase = True
        for i in studentInProb.getlst():
            a = i.split()
            if a[0] == idS:
                alreadylogin = True
            else:
                pass
        if alreadylogin == True and noInDataBase == False:
            # f = open('studentInData.txt', 'a', encoding="utf8")
            # f.write(timePlusIdname + '\n')
            # print('Writing to file completed')
            # f.close()
            # studentInData.push(timePlusIdname)
            for i in studentInProb.getlst():
                a = i.split()
                if a[0] == idS:
                    studentInProb.pop(studentInProb.search(i))
            f = open('studentInProb.txt', 'w', encoding="utf8")
            for i in studentInProb.getlst():
                f.write(i)
            f.close()
            addFormed = False
        else:
            pass
    
        return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})

def registerIDprob(request):
    idS = request.POST['studentID']
    name = request.POST['studentName']
    alreadylogin = False
    noInDataBase = False
    alreadyRegister = False
    registerSucess = False
    ############################################################################ สร้าง Sorted
    if idS == '' or name  == '':
        return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
    else:
        if idS in allId.items:
            alreadyRegister = True
            return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})
        else:
            registerSucess = True
            fullName = str(idS) + " " + str(name)
            allStudentBST.insert(fullName)
            allId.push(idS)
            allStudent.push(fullName)
            f = open('studentDataBase.txt', 'a', encoding="utf8")
            f.write(fullName + '\n')
            f.close()
            return render(request,'problogin.html',{'studentInProb':studentInProb.getlst(),'alreadylogin':alreadylogin,'noInDataBase':noInDataBase,'addFormed':addFormed,
        'alreadyRegister':alreadyRegister,'registerSucess':registerSucess})


########################################################################## ส่วน login Prob ############################################################################################


