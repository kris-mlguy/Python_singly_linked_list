# Krishnan Parameswaran

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def reverse(self):
        prev = None
        current = self.head
        
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev

        return self
        
    def display(self):
        curr = self.head
        print('Head')
        print(" |")
        print(" v")
        sll = []
        
        while(curr):
            sll.append(curr.data)
            sll.append('->')
            curr = curr.next
        print(sll)
    
if __name__ == '__main__': 

    input_string = input("Enter the numbers that need to be added to beginning of linked list, separated by space: \n")
    num_list = input_string.split()
    
    llist1 = SinglyLinkedList()
    for num in num_list:
        llist1.push(int(num))

    print("The original linked list: ")
    llist1.display()    

    llist2 = SinglyLinkedList()
    llist2 = llist1.reverse()
    print("The reversed linked list: ")
    llist2.display()