class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node

    def insert_after(self, prev_node_data, data):
        curr=self.head
        while curr and curr.data != prev_node_data:
            curr=curr.next
        if not curr:
            print("Previous node is not found.")
            return 
        new_node=Node(data)
        new_node.next=curr.next
        curr.next=new_node

    def delete_node(self, key):
        curr=self.head

        if curr and curr.data==key:
            self.head=curr.next
            return
        
        prev=None

        while curr and curr.data != key:
            prev=curr
            curr=curr.next

        if not curr:
            print("Node with data",key," not found.")
            return
        
        prev.next=curr.next

    def print_list(self):
        curr=self.head
        while curr:
            print(curr.data, end=" -> ")
            curr=curr.next
        print("Null")

    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_at_beginning(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beginning(5)
    ll.insert_after(10, 15)
    ll.print_list()  # Output: 5 -> 10 -> 15 -> 20 -> 30 -> Null
    ll.delete_node(5)
    ll.print_list() 
    ll.reverse()
    ll.print_list()  # Output: 30 -> 20 -> 15 -> 10 -> Null
    