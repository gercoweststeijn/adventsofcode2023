""" import sys
import re
from math import gcd
from collections import defaultdict, Counter
D = open(sys.argv[1]).read().strip()
L = D.split('\n')

def f(xs,part2):
  D = []
  for i in range(len(xs)-1):
    D.append(xs[i+1]-xs[i])
  if all(y==0 for y in D):
    return 0
  else:
    return xs[0 if part2 else -1] + (-1 if part2 else 1)*f(D,part2)

for part2 in [False,True]:
  ans = 0
  for line in L:
    xs = [int(x) for x in line.split()]
    ans += f(xs,part2)
  print(ans)
 """
 #################### 

def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    sum = 0
    for line in lines:

        #print ('=========')
        #print (line)
        numbers = [int(x) for x in line.split()]
        x = next_in_seq(numbers)
        #print (x)
        sum = sum +  x 
    return sum      


def next_in_seq (n : list) -> int:
   if all(y==0 for y in n):
      return 0
   else: 
      next_seq = []
      for i in range(len(n)-1):
          next_seq.append( n[i+1]-n[i] )
      else: # go one deeper
          #print (n[-1])
          return   n[-1] + next_in_seq(next_seq)



def f(xs,part2):
  part  = False
  D = []
  for i in range(len(xs)-1):
    D.append(xs[i+1]-xs[i])
  if all(y==0 for y in D):
    return 0
  else:
    return xs[0 if part2 else -1] + (-1 if part2 else 1)*f(D,part2)

  
def pref_in_seq (n : list) -> int:
   if all(y==0 for y in n):
      return 0
   else: 
      next_seq = []
      for i in range(len(n)-1):
          next_seq.append( n[i+1]-n[i] )
      else: # go one deeper
          #print (n[-1])
          return   n[0] - pref_in_seq(next_seq)     



def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    sum = 0
    for line in lines:

        #print ('=========')
        #print (line)
        numbers = [int(x) for x in line.split()]
        x = pref_in_seq(numbers)
        #print (x)
        sum = sum +  x    
    
    return sum      


if __name__ == "__main__":
    input_path = "./009/input.txt"
#    print("---Part One---")
#    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))