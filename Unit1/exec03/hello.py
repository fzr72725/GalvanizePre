def hello_world():
  print "hello, cruel world!"

def add_em_up(a, b, c):
  return a + b + c

def power_up(b, e):
  return b ** e

if __name__ == "__main__":
  hello_world()
  a = 22
  import pdb
  pdb.set_trace()
  b = 33
  print add_em_up(3, 4, 5)
