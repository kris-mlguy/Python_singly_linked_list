# Krishnan Parameswaran

# Given a list of elements for the linked list, create another linked list with the sorted elements of original one

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

# CamelCase for class names
class SinglyLinkedList: 
    
    def __init__(self):
        self.head = None
    
    # Function to create new node and insert value to the beginning of linked list    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # Function to load elements of a linked list into a list  
    def to_list(self):
        curr = self.head
        sll = []
        
        while(curr):
            sll.append(curr.data)
            curr = curr.next

        return sll

    
if __name__ == '__main__': 
    
    # Create a linked list instance and take the given list of elements into it 
    input_string = input("Enter the numbers that need to be added to beginning of linked list, separated by space: \n")
    num_list = input_string.split()
    
    sll1 = SinglyLinkedList()
    for num in num_list:
        sll1.push(int(num))

    sll1_list = sll1.to_list()
    print("The given linked list is: ")
    print(sll1_list)
    

    
    # Create another linked list instance and inserted the sorted elements of original linked list 
    sll1_rev_sort_list = sorted(sll1_list, reverse=True)
    sll2 = SinglyLinkedList()
    for num in sll1_rev_sort_list:
        sll2.push(num)

    sll2_list = sll2.to_list()
    print("The sorted version of given linked list is: ")
    print(sll2_list)
