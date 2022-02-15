# Sum function
def add(x,y):
  s = x+y
  return s

# TO-DO add multiplication function

def multiply(x,y):
  return (x*y)


def subtract(x,y):
  return x-y

def summ (x):
  if x==0:
    return 0
  return x+summ(x-1)
