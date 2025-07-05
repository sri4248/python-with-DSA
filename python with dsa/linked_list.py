class node:
  def __init__(self,val):
    self.data=val 
    self.next=None
class SLL:
  def __init__(self):
    self.tail=None
  def insert_begin(self,val):
    nn=node(val)
    if self.head is None:
      print(nn.data,'inserted')
      self.head=self.tail=nn 
    else:
      print(nn.data,'inserted')
      nn.next=self.head 
      self.head=nn 
  def display(self):
    if self.head is None:
      print('List is empty')
    else:
      i=self.head 
      while i is not None:
        print(i.data,end='->')
        i=i.next
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
      print('Nothing to delete')
    elif self.head==self.tail:
      print(self.head.data,'deleted')
      self.head=self.tail=None
    else:
      print(self.head.data,'deleted')
      self.head=self.head.next

    
list=SLL()
while True:
  print('\nEnter your choice')
  print('1.Insert at begin 2.insert at end 3.display')
  print('5.Delete at begin')
  ch=int(input())
  match ch:
    case 1:
      val=int(input())
      list.insert_begin(val)
    case 2:
      val=int(input())
      list.insert_end(val)
    case 3:
      list.display()
    case 4:
      print('terminated')
      break
    case 5:
      list.delete_begin()
