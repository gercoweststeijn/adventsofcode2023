import sys
#sys.setrecursionlimit(999)
from collections import deque



def possible_positions (pos_r, pos_c, map):
    ret_pos = []
    for c,r in [[1,0],[0,1],[-1,0],[0,-1]]:
        new_c = c+pos_c
        new_r = r + pos_r
        if (new_c >= 0 and new_c < MAX_COLS 
           and new_r > 0 and new_r < MAX_ROWS
           and map[new_r][new_c] in ['.','S']):
                # then 
                ret_pos.append([new_r,new_c])
    return ret_pos
        


# def positions_walk_world  (pos_c, pos_r,map, n , max): 
#     #print (f'hier gaan we {pos_r} en {pos_c}')
#     if n == max:
#         if not [pos_c,pos_r]  in seen:
#             seen.append([pos_c,pos_r])
#         return 0
#     else:
#         new_n = n+1 
#         positions = possible_positions (pos_c, pos_r,map)
#         #print (f'allemaal positions {positions}')
#         local_score = 0
#         for position in positions: 
            
#             new_r = position[0]
#             new_c = position[1]
#             local_score += (1 + positions_walk_world(pos_c= new_c, pos_r = new_r, map=map,n = new_n, max= max ))
#         return local_score


def positions_walk_world  (pos_r,pos_c, map, max): 
    q = deque( [ (pos_r, pos_c, max) ])
    
    end_stages = []
    seen = []
    seen.append([pos_r,pos_c])



    while q:
        pos_r, pos_c, nr = q.popleft()
        
        # 
        # if this is true one can go back and forth to reach this in the end
        # by takin this here we avoid having to search in loops. 
        if nr % 2 == 0:
            if [pos_r, pos_c] not in end_stages: 
                end_stages.append([pos_r, pos_c])
        if nr == 0: 
            continue
        
        positions = possible_positions (pos_r, pos_c, map)
         #print (f'allemaal positions {positions}')
         
        for position in positions: 
            if position in seen:
                continue
            else:
                seen.append(position)
                q.append((position[0],position[1],nr-1))

    #print (end_stages)
    return len(end_stages)
                


def find_s(map):
    for i,r in enumerate( map):
        if 'S' in r:
            return i, r.index('S')

def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    map = []
    for l in lines:        
        map.append(list(l))

    s_r, s_c = find_s(map)



    
    global MAX_ROWS 
    global MAX_COLS 
    MAX_ROWS = len(map)
    MAX_COLS = len(map[0])



    result = positions_walk_world(pos_c=s_c,pos_r=s_r,map=map,max=64)


    #print (f'result is {result}')



#    for i, r in enumerate(map):
#        for j,c in enumerate (r): 
#            if [j,i] in seen:
#                print ('0', end ='')
#            else: 
#                print (c, end ='')
#        print ()

    return result 



def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    ins_map = []
    for l in lines:        
        ins_map.append(list(l))
    
    result = 0 

    return result 

  

if __name__ == "__main__":
    input_path = "./021/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))