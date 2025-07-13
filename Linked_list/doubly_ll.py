class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

    def insert_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        if not self.head:
            return

        cur = self.head

        # delete head
        if cur.data == value:
            if cur.next:
                cur.next.prev = None
            self.head = cur.next
            return

        while cur:
            if cur.data == value:
                if cur.next:
                    cur.next.prev = cur.prev
                if cur.prev:
                    cur.prev.next = cur.next
                return
            cur = cur.next

    def print_forward(self):
        cur = self.head
        while cur:
            print(cur.data, end=" → ")
            tail = cur  # store last node for backward print
            cur = cur.next
        print("None")

    def print_backward(self):
        # Traverse to tail first
        cur = self.head
        if not cur:
            print("Empty")
            return

        while cur.next:
            cur = cur.next

        # Now print in reverse
        while cur:
            print(cur.data, end=" ← ")
            cur = cur.prev
        print("None")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_beginning(10)
    dll.insert_end(20)
    dll.insert_end(30)
    dll.insert_end(5)

    dll.print_forward()   # 5 → 10 → 20 → 30 → None
    dll.print_backward()  # 30 ← 20 ← 10 ← 5 ← None

    dll.delete(20)
    dll.print_forward()   # 5 → 10 → 30 → None
