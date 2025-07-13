class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        self.head = new_node

    def insert_after(self, target, data):
        if not self.head:
            print("List is empty.")
            return

        cur = self.head

        while True:
            if cur.data == target:
                new_node = Node(data)
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next
            if cur == self.head:
                break

        print(f"Value {target} not found in the list.")

    def delete(self, key):
        if not self.head:
            return

        cur = self.head

        # Deleting head node
        if cur.data == key:
            if cur.next == self.head:  # only one node
                self.head = None
                return
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
            return

        prev = None
        cur = self.head
        while cur.next != self.head:
            prev = cur
            cur = cur.next
            if cur.data == key:
                prev.next = cur.next
                return
            

    def print_list(self):
        if not self.head:
            print("List is empty")
            return

        cur = self.head
        while True:
            print(cur.data, end=" → ")
            cur = cur.next
            if cur == self.head:
                break
        print("(head)")


if __name__ =="__main__":
    cll=CircularLinkedList()
    cll.insert_at_beginning(10)
    cll.insert_at_end(20)       
    cll.insert_at_end(30)
    cll.insert_after(20, 25)
    cll.insert_at_beginning(50)
    cll.print_list()
    cll.delete(30)
    cll.print_list()