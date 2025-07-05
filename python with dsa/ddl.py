class node:
    def __init__(self,val):
        self.data=val
        self.prev=self.next=None
class DLL:
    def __init__(self):
        self.head=self.tail=None
    def insert_begin(self,val):
      nn=node(val)
      if self.head is None:
        self.head=self.tail=nn
      else:
        nn.next=self.head
        self.head.prev=nn;
        self.head=nn
    def display(self):
      if self.head is None:
        print('List is empty')
      else:
        i=self.head
        while i:
          print(i.data,end='<->')
          i=i.next
    def display_reverse(self):
      if self.head is None:
        print('List is empty')
      else:
        i=self.tail
        while i:
          print(i.data,end='<->')
          i=i.prev
    def insert_end(self,val):
      nn=node(val)
      if self.head is None:
        self.head=self.tail=nn
      else:
        self.tail.next=nn
        nn.prev=self.tail
        self.tai=nn
    def delete_begin(self):
        if self.head is None:
          print('Nothing to detete')
        elif self.head.next is None:
          print(self.head.data,'deleted')
          self.head=self.tail=None
        else:
          self.head=self.head.next
          self.head.next.prev=None
    def delete_end(self):
      if self.head is None:
        print('Nothing to delete')
      elif self.head.next is None:
        print(self.head.data,'deleted')
        self.head=self.tail=None
      else:
        print(self.tail.data,'deleted')
        self.tail=self.tail.prev
        self.tail.next=None
      
          
      
      
llist=DLL()
while True:
    print('enter ur choice')
    print('1.Insert at begin 2.Insert at end 3.display 4.exit')
    print('5.Display in reverse 6.Delete at begin 7.Delete at end')
    ch=int(input())
    match ch:
        case 1:
            val=int(input())
            llist.insert_begin(val)
        case 2:
          val=int(input())
          llist.insert_end(val)
        case 3:
          llist.display()
        case 4:
          print('Terminated')
          break
        case 5:
          llist.display_reverse()
        case 6:
          llist.delete_begin()
        case 7:
          llist.delete_end()
        
