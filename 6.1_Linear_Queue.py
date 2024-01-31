# Static implementation of linear queue
front = 0
rear = 0
max_size = 5

def createQueue():
    queue = [None] * max_size  # Empty list with fixed size
    return queue

def isEmpty(queue):
    return front == rear

def enqueue(queue, item):
    global rear
    if isFull(queue):
        print("Queue is full. Cannot enqueue element.")
    else:
        queue[rear] = item
        rear += 1

def dequeue(queue):
    global front
    if isEmpty(queue):
        print("Queue is empty. Cannot dequeue element.")
        return None
    else:
        item = queue[front]
        front += 1
        return item

def display(queue):
    if isEmpty(queue):
        print("Queue is empty.")
    else:
        print("Queue elements:")
        for i in range(front, rear):
            print(queue[i], end=" ")
        print()

# Driver code
queue = createQueue()

while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to enqueue: "))
        enqueue(queue, item)
    elif choice == 2:
        dequeued_item = dequeue(queue)
        if dequeued_item is not None:
            print("Dequeued element:", dequeued_item)
    elif choice == 3:
        display(queue)
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a valid option.")
