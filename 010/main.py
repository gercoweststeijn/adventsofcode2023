import math, sys
from collections import deque


def starting_pos (lines):
    for i,line in enumerate(lines):

        x =  line.rfind('S')
        if x >= 0:
            return x, i

def connecting_squares (tile, x , y):
    match tile:
        case '|':
            return [[x,y-1],[x,y+1]] 
        case '-':
            return [[x-1,y],[x+1,y]]        
        case 'L': # up and right
            return [[x+1,y],[x,y-1]] 
        case 'J': # up and left
            return [[x-1,y],[x,y-1]]         
        case '7': # down and left
            return [[x-1,y],[x,y+1]] 
        case 'F': # down and right 
            return [[x+1,y],[x,y+1]] 

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

def first_step (prev_x, prev_y, prev_tiles,  lines):
    x = prev_x[-1]
    y = prev_y[-1]
    
    # check if going north is possible 
    # check that we are not going outof range
    if y -1 >=0:
        y = y-1
        t = lines[y][x]
        if t in ['|','7','F']:
            return x,y,t
    
    x = prev_x[-1]
    y = prev_y[-1]
    # check if going south is possible 
    # check that we are not going outof range
    if y + 1 <= len (lines):
        y = y+1
        t = lines[y][x]
        if t in ['|','J','L']:
            return x,y,t
        
    x = prev_x[-1]
    y = prev_y[-1]
    # check if going west is possible 
    # check that we are not going outof range
    if x -1 >= 0:
        x = x-1
        t = lines[y][x]
        if t in ['-','L','F']:
            return x,y,t
        
    x = prev_x[-1]
    y = prev_y[-1]
    # check if going east is possible 
    # check that we are not going outof range
    if x + 1 <=  len(lines[y]):
        x = x+1
        t = lines[y][x]
        if t in ['-','J','7']:
            return x,y,t

    return 'ERROR'

def next_squares(X, Y, T,  lines):
    if len (X) > 20000:
        return 'error', '',''
    for option in connecting_squares(tile = T[-1], x=X[-1], y=Y[-1]):
        opt_y = option[1]
        opt_x = option[0]
        opt_t = lines[opt_y][opt_x]
        if opt_x != X[-2] or opt_y != Y[-2]:
            ##print ('x: '+str({opt_x})+' y: '+str({opt_y}) + ' type: '+str(opt_t))
            X.append(opt_x)
            Y.append(opt_y)
            T.append(opt_t)
            if opt_t == 'S':
                return X,Y,T
            else:
                return next_squares(X, Y, T, lines)

    return X,Y,T 

def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = [str(x) for x in   f.read().strip().split("\n") ]
    X = []
    Y = []
    T = ['S']

    x, y = starting_pos(lines)
    X.append(x)
    Y.append(y)
    
    x, y, t = first_step(X,Y,T,lines)
    X.append(x)
    Y.append(y)
    T.append(t)

    X1,Y1,T1 = next_squares(X,Y,T,lines)

    #for i in range (len(X1)):
    #    print (str(X1[i]) + '  ' + str(Y1[i]) )
    
    return (math.floor(len(X1)/2)), X1,Y1,T1, lines

    

def determine_s (X,Y,T):
    req_x = X[-1] - X [1]
    req_y = Y[-1] - Y[1]
    
    if req_y == 0:
        return '-'
    if req_x == 0:
        return '|'
    if req_y == 1 and req_x == 1:
        return 'L'
    if req_y == 1 and req_x == -1:
        return 'J'
    if req_y == -1 and req_x == 1:
        return 'F'
    if req_y == 1 and req_x == -1:
        return '7'

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.

def form_grid (XY,lines, s):
    grid = []
    for y, line in enumerate(lines):
        nl = ''
        for x, ch in enumerate(line):
            if not ((x,y) in XY):
                nl = nl + '.'
            else:
                if ch == 'S':
                    nl = nl + s
                else:
                    nl = nl + line[x]
        grid.append(nl)

                

    return grid

    


def part_two (X,Y,T,lines) -> str:
    
    s = determine_s(X,Y,T)

    print ('S: '+s)

    #lines[Y[0]].replace('S',s)

    print (lines[Y[0]])
    #grid = ["".join(ch if (r, c) in loop else "." for c, ch in enumerate(row)) for r, row in enumerate(lines)]

    XY = list(zip(X,Y))

    #for l in lines:
    #   print (l)


    print ('===================')
    grid = form_grid (XY,lines, s)
    #print (str(XY))
    #
    # print (grid)
    
    for l in grid:
        print (l)

    outside = set()

    for r, row in enumerate(grid):
        within = False
        up = None
        for c, ch in enumerate(row):
            if ch == "|":
                assert up is None
                within = not within
            elif ch == "-":
                assert up is not None
            elif ch in "LF":
                assert up is None
                up = ch == "L"
            elif ch in "7J":
                assert up is not None
                if ch != ("J" if up else "7"):
                    within = not within
                up = None
            elif ch == ".":
                pass
            else:
                raise RuntimeError(f"unexpected character (horizontal): {ch}")
            if not within:
                outside.add((r, c))

    print(len(grid) * len(grid[0]) - len(outside | loop))

    # for r, row in enumerate(lines):
    #     within = False
    #     up = None
    #     for c, ch in enumerate(row):
    #         if ch == "|":
    #             assert up is None
    #             within = not within
    #         elif ch == "-":
    #             assert up is not None
    #         elif ch in "LF":
    #             assert up is None
    #             up = ch == "L"
    #         elif ch in "7J":
    #             assert up is not None
    #             if ch != ("J" if up else "7"):
    #                 within = not within
    #             up = None
    #         elif ch == ".":
    #             pass
    #         else:
    #             raise RuntimeError(f"unexpected character (horizontal): {ch}")
    #         if not within:
    #             outside.add((r, c))

    
    return 






if __name__ == "__main__":
    # more depth required
    sys.setrecursionlimit(100000)

    input_path = "./010/tst6.txt"
    print("---Part One---")
    result, X,Y,T,lines = part_one(input_path)
    print(result)



    print("---Part Two---")
    print(part_two(X,Y,T,lines))