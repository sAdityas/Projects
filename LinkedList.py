class Node:
    def __init__(self , data , next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertathead(self , data):
        node = Node(data , self.head)
        self.head = node
    
    def insertatend(self,data):
        if self.head is None:
            self.head = Node(data , None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data , None)

    def insertat(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insertathead(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data , itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1      

    def printLL(self):
        if self.head is None:
            print("Empty linked list")
            return
        else:
            itr = self.head
            llstr = ""
            while itr:
                llstr += str(itr.data) + "-->"
                itr = itr.next
            print(llstr)

    def insertaftervalue(self,data_after,data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert , self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert , itr.next)
                break
            itr = itr.next

    def insert_vals(self,data_list):
        self.head = None
        for data in data_list:
            self.insertatend(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next


    def reverse(self):
        if self.head is None:
            return
        itr = self.head
        prev = None
        while itr:
            next = itr.next
            itr.next = prev
            prev = itr
            itr = next
            self.head = prev
    
        
            

if __name__ == "__main__":
    ll = LinkedList()
    ll.insertathead(2)
    ll.insertathead(1)
    ll.insertatend(3)
    ll.insertatend(4)
    ll.insertaftervalue(3,19)
    ll.printLL()
    ll.reverse()
    ll.printLL()