import sys
#sys.setrecursionlimit(9999)

trav_map = []


def move_east (x,y,ins_map, moves_made):
    moves_made.append(f'E-{x}-{y}')
    c = 'x'
    for i in range(x, len(ins_map[y])):
        x = i

        c = ins_map[y][x]

        # we checked before going in that it os possible to travel here
        trav_map[y][x] += 1
        if c in ['\\','/','|']:
            break        
    match c:
        case '/':
            if y-1 > 0 and f'N-{x}-{y-1}' not in moves_made:
                move_north(x,y-1,ins_map,moves_made)
        case "\\":
            if y+1 < len(ins_map)and f'S-{x}-{y+1}' not in moves_made:
                move_south(x,y+1,ins_map,moves_made)
        case '|':
            if y-1 > 0 and f'N-{x}-{y-1}' not in moves_made:
                move_north(x,y-1,ins_map, moves_made)
            if y+1 < len(ins_map) and f'S-{x}-{y+1}' not in moves_made:
                move_south(x,y+1,ins_map,moves_made)

def move_west (x,y,ins_map, moves_made):
    moves_made.append(f'W-{x}-{y}')
    c = 'x'
    for i in range(x, -1, -1):
        x = i
        c = ins_map[y][x]

        trav_map[y][x] += 1
        if c in ['\\','/','|']:
            break        
    match c:
        case '\\':
            if y-1 > 0 and f'N-{x}-{y-1}' not in moves_made:
                move_north(x,y-1,ins_map,moves_made)
        case "/":
            if y+1 < len(ins_map) and f'S-{x}-{y+1}' not in moves_made:
                move_south(x,y+1,ins_map,moves_made)
        case '|':
            if y-1 > 0 and f'N-{x}-{y-1}' not in moves_made:
                move_north(x,y-1,ins_map, moves_made)
            if y+1 < len(ins_map) and f'S-{x}-{y+1}' not in moves_made:
                move_south(x,y+1,ins_map,moves_made)

def move_north (x,y,ins_map, moves_made):
    moves_made.append(f'N-{x}-{y}')
    c = 'x'
    for i in range(y, -1, -1):
        y = i
        c = ins_map[y][x]

        trav_map[y][x] += 1
        if c in ['\\','/','-']:
            break 
    match c:
        case "\\":
            if x-1 >= 0 and f'W-{x-1}-{y}' not in moves_made:
                move_west(x-1,y,ins_map,moves_made)
        case '/':
            if x+1 < len (ins_map[y]) and f'E-{x+1}-{y}' not in moves_made:
                move_east(x+1,y,ins_map,moves_made)
        case '-':
            if x-1 >= 0 and f'W-{x-1}-{y}' not in moves_made:
                move_west(x-1,y,ins_map,moves_made)
            if x+1 < len (ins_map[y]) and f'E-{x+1}-{y}' not in moves_made:
                move_east(x+1,y,ins_map,moves_made)

def move_south (x,y,ins_map, moves_made):
    moves_made.append(f'S-{x}-{y}')
    c = 'x'
    for i in range(y, len(ins_map)):
        
        y = i
        #print (f'move south {x}:{y}')
        c = ins_map[y][x]

        trav_map[y][x] += 1
        if c in ['\\','/','-']:
            break 
    match c:
        case "/":
            if x-1 >= 0 and f'W-{x-1}-{y}' not in moves_made:
                move_west(x-1,y,ins_map,moves_made)
        case '\\':
            if x+1 < len (ins_map[y]) and f'E-{x+1}-{y}' not in moves_made:
                move_east(x+1,y,ins_map,moves_made)
        case '-':
            if x-1 >= 0 and f'W-{x-1}-{y}' not in moves_made:
                move_west(x-1,y,ins_map,moves_made)
            if x+1 < len (ins_map[y]) and f'E-{x+1}-{y}' not in moves_made:
                move_east(x+1,y,ins_map,moves_made)


def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    ins_map = []
    for l in lines:        
        ins_map.append(list(l))
    
    moves_made = []

    print ('*****************')    
    for i in range(len(ins_map)):
        trav_map.append([0]*len(ins_map[0]))


    print ('**************************')
    move_east(0,0,ins_map, moves_made)

    #print ('123')
    #for l in trav_map:
    #    print (l)
    result = 0
    #for l in ins_map:
    #    res += l.count('#')
    
    for l in trav_map:
        result += len(l) - l.count(0)


    return result 



def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    ins_map = []
    for l in lines:        
        ins_map.append(list(l))
    
    moves_made = []

    for i in range(len(ins_map)):
        trav_map.append([0]*len(ins_map[0]))

    
    result = 0 

    
    for i in range(len(ins_map)):

        tussen_result = 0 
        for j in range(len(ins_map)):
            trav_map[j] = [0]*len(ins_map[0])
        moves_made = []

        move_east(0,i,ins_map, moves_made)
        for l in trav_map:
            tussen_result += len(l) - l.count(0)
        #print (f'y: {i} x:{0} -- {tussen_result}')  

        if tussen_result > result:
            result = tussen_result
  
    print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    for i in range(len(ins_map)):

        tussen_result = 0 
        for j in range(len(ins_map)):
            trav_map[j] = [0]*len(ins_map[0])
        moves_made = []

        move_west(len(ins_map[0])-1,i,ins_map, moves_made)
        for l in trav_map:
            tussen_result += len(l) - l.count(0)
        #print (f'y: {i} x:{len(ins_map[0])-1} -- {tussen_result}')        
        if tussen_result > result:
            result = tussen_result

    print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    for i in range(len(ins_map[0])):

        tussen_result = 0 
        for j in range(len(ins_map)):
            trav_map[j] = [0]*len(ins_map[0])
        moves_made = []

        move_south(i,0,ins_map, moves_made)
        for l in trav_map:
            tussen_result += len(l) - l.count(0)
        #print (f'y: {i} x:{0} -- {tussen_result}')  
        if tussen_result > result:
            result = tussen_result


    print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    for i in range(len(ins_map[0])):
        tussen_result = 0 
        for j in range(len(ins_map)):
            trav_map[j] = [0]*len(ins_map[0])
        moves_made = []

        move_north(i,len(ins_map)-1,ins_map, moves_made)
        for l in trav_map:
            tussen_result += len(l) - l.count(0)
        #print (f'y: {len(ins_map[0])-1} x:{i} -- {tussen_result}')  

        if tussen_result > result:
            result = tussen_result

    return result 

  

if __name__ == "__main__":
    input_path = "./016/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))