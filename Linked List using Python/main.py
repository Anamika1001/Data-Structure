class Node:
    def __init__(self,data): 
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head =None

    def create(self, number):
        pointer = Node(input("Enter Data: "))
        self.head = pointer
        while(number-1>0):
            pointer.next=Node(input("Enter Data: "))
            pointer = pointer.next
            number-=1

    def display(self):
        pointer = self.head
        while pointer is not None:
            print(pointer.data)
            pointer = pointer.next
        print()

    def count(self):
        pointer = self.head
        count = 0
        while pointer is not None:
            count +=1
            pointer = pointer.next
        return count

    def AtBegin(self, data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp

    def AtLast(self, data):
        pointer = self.head
        temp=Node(data)
        if self.head==None:
            self.head=temp
            return
        while pointer.next is not None:
            pointer = pointer.next
        pointer.next=temp

    def InBetween(self, position, data):
        temp = Node(data)
        pointer=self.head
        if position >=1 and position<=self.count():
            if position == 1:
                temp.next=self.head
                self.head=temp 
                return 
            for _ in range(2,position):
                pointer=pointer.next
            temp.next=pointer.next
            pointer.next=temp
    def RemoveNode(self, key):
        pointer = self.head

        if self.head==None:
            return

        if(pointer.data == key):
            self.head=pointer.next
            pointer = None
            return

        while(pointer is not None):
            if pointer.data == key:
                break
            prev = pointer
            pointer = pointer.next 

        if pointer == None:
            return

        prev.next = pointer.next
        pointer = None    

def printMenu():
    print("Enter 1 for Display Data: ")    
    print("Enter 2 for data input At Begin: ")    
    print("Enter 3 for data input At End: ")    
    print("Enter 4 for data input In Between: ")    
    print("Enter 5 for Remove Data: ")    
    print("Enter 6 for Length: ")    
    print("Enter 9 for Menu: ")  
    print("Enter 0 for Exit: ")

#Driver Code
if __name__=="__main__":
    list1 = SLinkedList()
    num =int(input("Enter Number of Data to Create Linked List: "))
    list1.create(num)

    printMenu()
    while(True):
        choice = int(input("\nEnter your choice: "))
        
        if choice==1:
            list1.display()
        elif choice==2:
            list1.AtBegin(input("Enter Data: "))
        elif choice==3:
            list1.AtLast(input("Enter Data: "))
        elif choice==4:
            list1.InBetween(int(input("Enter Index: ")), input("Enter Data: "))
        elif choice==5:
            list1.RemoveNode(input("Enter Key: "))
        elif choice==6:
            print("Total Count:", list1.count())
        elif choice==0:
            exit('Good Bye')
        else:
            printMenu()
