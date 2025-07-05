class node:
  def _init_(self,val):
    self.data=val
    self.next=None
class SLL:
  def _init_(self):
    self.head=self.tail=None
  def insert_begin(self,val):
    nn=node(val)
    if self.head is None:
      print(nn.data,'inserted')
      self.head=self.tail=nn
    else:
      print(nn.data,'inserted')
      nn.next==self.head
      self.head=nn
  def display(self):
    if self.head is None:
      print("List is empty")
    else:
      i=self.head
      while i is not None:
        print(i.data,end='->')
        i=i.next
      print('None')
  def insert_end(self,val):
    nn=node(val)
    if self.head is None:
      print(nn.data,'inserted')
      self.head=self.tail=nn
    else:
       print(nn.data,'inserted')
       self.tail.next=nn
       self.tail=nn
  def delete_begin(self):
    if self.head is None:
      print("ntg 2 delete")
    elif self.head==self.tail:
      print(self.head.data,'deleted')
      self.head=self.tail=None:
    else:
        print(self.head.self.data,'deleted')
        slef.head=self.head.next
  def Delete_end(self):
    if self.head is None:
      print('Nothing to delete')
    elif self.head==self.tail:
      print(self.head.data,'deleted')
      self.head=self.tail=None
    else:
      i=self.head
      j=self.head.next
      while j.next is not None:
        i=i.next
        j=j.next
      print(j.data,'deleted')
      i.next=None
      self.tail=i
        
list=SLL()
while True:
  print('enter ur choice')
  print("1.inser at bengin 2.insert at end 3.siaplay")
  print('5.delete at begin 6.Delete_end')
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
      print("terminated")
      break
    case 5:
      list.delete_begin()
    case 6:
      list.Delete_end()
