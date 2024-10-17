class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.head is None
    
    def search(self, target):
        curr = self.head
        while curr:
            if curr.val == target:
                return curr
            curr = curr.next
        print(f"Value {target} not found in LinkedList.", target)
        return None
    
    def insert(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1

    def delete(self, target):
        if self.is_empty():
            print(f"Empty LinkedList. Nothing to delete.")

        if self.head.val == target:
            self.head = self.head.next
            # If the list is empty after removing the head. Set tail to None
            if self.head is None:
                self.tail = None
                self.size -= 1
            return
        
        curr = self.head
        while curr:
            if curr.next.val == target:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr
                self.size -= 1
                return
            
            curr = curr.next
        
        print(f"Node with value {target} was not found.")


    def to_string(self):
        if self.is_empty():
            print(f"Empty LinkedList.")
        
        curr = self.head
        while (curr):
            print(f'[{curr.val}]', end="->")
            curr = curr.next

        print(f"[None]")






 
class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
