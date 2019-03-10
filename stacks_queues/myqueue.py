from collections import deque

class MyQueue(object):
    def __init__(self):
      self.nodes = deque()
      # self.head = None
    
    def peek(self):
      # print the head data
      print(self.nodes[0])
        
    def pop(self):
      self.nodes.popleft()
        
    def put(self, value):
      if value:
        self.nodes.append(value)

if __name__ == "__main__":

  queue = MyQueue()

  data = [
    [1, 42],
    [2],
    [1, 14],
    [3],
    [1, 28],
    [3],
    [1, 60],
    [1, 78],
    [2],
    [2],
  ]

  for value in data:
    if value[0] == 1:
      queue.put(value[1])
    elif value[0] == 2:
      queue.pop()
    else:
      p = queue.peek()
      if p:
        print(p)