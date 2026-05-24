class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1

    def enqueue(self,data):
        # Full condition
        if (self.rear+1)%self.size==self.front:
            print("Queue is full")
            return
        # First element 
        if self.front==-1:
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data

    def dequeue(self):
        # Empty condition
        if self.front==-1 and self.rear==-1:
            print("Queue is empty")
            return
        # Only one element
        if self.front==self.rear:
            print("Removed element:", self.queue[self.front])
            self.front=-1
            self.rear=-1
        else:
            print("Removed element:", self.queue[self.front])
            self.front=(self.front+1)%self.size
    def display(self):
        if self.front==-1 and self.rear==-1:
            print("Queue is empty")
            return
        else:
            if self.front<=self.rear:
                print("Queue elements:", end=" ")
                for i in range(self.front,self.rear+1):
                    print(self.queue[i], end=" ")
                print()
            elif self.front>self.rear:
                print("Queue elements:", end=" ")
                for i in range(self.front,self.size):
                    print(self.queue[i], end=" ")
                for i in range(0,self.rear+1):
                    print(self.queue[i], end=" ")
                print()


cq = CircularQueue(3)

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)

cq.display()

cq.enqueue(40)

cq.dequeue()

cq.display()

cq.enqueue(40)

cq.display()