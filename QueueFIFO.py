class QueueError(IndexError):  # Choose base class for the new exception.
    pass
    #  Write code here

class Queue:
    def __init__(self):
        self.queue =[]
        # Write code here
        

    def put(self, elem):
        self.queue.insert(0,elem)
        # Write code here

    def get(self):
        if len(self.queue)>0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
             raise QueueError        
        # Write code here
       


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
