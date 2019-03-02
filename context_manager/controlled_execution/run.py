class controlled_execution:
  def __init__(self, name):
    self.name = name
    self.status = "initialized"

  def __enter__(self):
    # set things up
    self.status = "running"
    return self

  def __exit__(self, type, value, traceback):
    self.status = "stopped"
    print(self.status)

if __name__=="__main__":
  with controlled_execution("John") as ce:
    print(ce.name + ": " + ce.status)

# execute with python run.py
# output
#        running
#        stopped