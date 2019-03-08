from contextlib import contextmanager

@contextmanager
def foo():
  print("before yield")
  yield 1
  print("after yield")

if __name__ == "__main__":
  with foo() as f:
    print(f)


# "Everything before the call to yield is considered the code for __enter__(). Everything after is the code for __exit__()"