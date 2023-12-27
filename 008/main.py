import sys
import re
from math import gcd
from collections import defaultdict, Counter


# kleinste deler voor lijst
def KD(xs):
  ans = 1
  for x in xs:
    ans = (x*ans)//gcd(x,ans)
  return ans

def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        steps, bottom = f.read().strip().split("\n\n")
    
    lines = bottom.strip().split('\n')


    #map = {'starter':[],'direction':[]}
    map={}
    for line in lines:        
        starter, direction_str = line.split('=')
        direction_str = direction_str.replace(' (', '')
        direction_str = direction_str.replace(')', '')
        directions = direction_str.split(',')

        #a = str(starter.strip())
        map[str(starter.strip())] = directions
        
    count = 0
    found = False
    current_pos = 'AAA'

    while not found:
        for i,step in enumerate(steps):
            count += 1
            L = map[current_pos][0].strip()
            R = map[current_pos][1].strip()
            if step == 'R':
                
                if R == 'ZZZ':
                    return count
                    # found :-) 
                else:
                    current_pos = R
            else:
                if L == 'ZZZ':
                    return count

                    # found ;-) 
                else:
                    current_pos = L
            
    return ''

def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        steps, bottom = f.read().strip().split("\n\n")
    
    lines = bottom.strip().split('\n')


    #map = {'starter':[],'direction':[]}
    map={}
    for line in lines:        
        starter, direction_str = line.split('=')
        direction_str = direction_str.replace(' (', '')
        direction_str = direction_str.replace(')', '')
        directions = direction_str.split(',')

        #a = str(starter.strip())
        map[str(starter.strip())] = directions
        
    count = 0
    found = False
#    current_pos = 'AAA'

    #pattern = r'\D'
    start_pos = (([k for k,v in map.items() if re.search('A$',k)]))


    Results = []
    for pos in start_pos:
        current_pos = pos
        #print (pos)
        found = False
        count = 0 
        while not found:
            for i,step in enumerate(steps):
                count += 1
                L = map[current_pos][0].strip()
                R = map[current_pos][1].strip()
                if step == 'R':                    
                    if R[2] == 'Z':
                        #return count
                        Results.append(count)
                        #print (count)
                        found = True
                        break
                        # found :-) 
                    else:
                        current_pos = R
                else:
                    if L[2] == 'Z':
                        #return count
                        #print (count)
                        found = True
                        break
                        # found ;-) 
                    else:
                        current_pos = L
        
    return KD(Results)


if __name__ == "__main__":
    input_path = "./008/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))