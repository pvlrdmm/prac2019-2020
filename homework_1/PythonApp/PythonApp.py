class Node:

   def __init__(self, data=None):
        self.data = data
        self.next = None

   def __str__(self):
        return str(self.data)
    
 


class LinkedList:

    def __init__(self):
        self.head = None
        self.curr = None
        self.tail = None
       

    def __iter__(self):
        return self

    def next(self):
        if self.head and not self.curr:
            self.curr = self.head
            return self.curr
        elif self.curr.next:
            self.curr = self.curr.next
            return self.curr
        else:
            raise StopIteration

    def append(self, data):
        n = Node(data)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next


    def Del(self,i):
        if (self.head == None):
          return
        curr = self.head
        count = 0
        if i == 0:
          self.head = self.head.next
          return
        while curr != None:
            if count == i:
              if curr.next == None:
                self.last = curr
              old.next = curr.next 
              break
            old = curr  
            curr = curr.next
            count += 1

    def num2list(self, num, l):
        s = str(num)
        for i in range(len(s)):
            l.append(s[i])

    def find(self,i):
        if (self.head == None):
          return
        curr = self.head
        count = 0
        if i == 0:
          self.head = self.head.next
          return
        while curr != None:
            if count == i:
                return curr
            old = curr  
            curr = curr.next
            count += 1

    def list2str(self):
       s = ''
       curr = self.head
       while curr != None:
           s += str(curr.data)
           curr =curr.next
       return s

    def add_num_as_lists(self,l1,l2):
        n1=int(l1.list2str())
        n2=int(l2.list2str())
        res = n1 + n2
        l_res = LinkedList()
        self.num2list(res,l_res)
        return l_res

# Add 5 node
ll = LinkedList()
for i in range(1, 6):
    ll.append(i)

# print out the list
#for n in ll:
 #   print n

ll.Del(3)

for n in ll:
    print n

l = LinkedList()
ll.num2list(1000, l)

for n in l:
    print n

#print l.find(2)
#print l.list2str()

l_add = LinkedList();
l_add = l.add_num_as_lists(l,l)
for n in l_add:
    print n