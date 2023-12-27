import numpy

def expand (universe):
    # rows
    U = []

    ER = []
    
    for ul in universe: 
        if ('#' in ul):
            U.append(ul)
        else:            
            U.append([ul])
            U.append([ul])

    # collumns
    # transpose
    U = list(map(list, zip(*U)))
    U2 = []
    for ul in U: 
        if ('#' in ul):
            U2.append(ul)
        else:            
            U2.append(ul)
            U2.append(ul)
    # transpose back to roiginal
    U = list(map(list, zip(*U2)))

    return U


def expand_m (universe):
    # rows
    U = []
    ER = []    
    for ul in universe: 
        if ('#' in ul):
            U.append(ul)
        else:            
            U.append(['M']*(len(ul)))

    # collumns
    # transpose
    U = list(map(list, zip(*U)))
    U2 = []
    for ul in U: 
        if ('#' in ul):
            U2.append(ul)
        else:            
            U2.append(['M']*(len(ul)))
    # transpose back to roiginal
    U = list(map(list, zip(*U2)))

    return U

def get_locations (U):
    L = []
    for i,row in enumerate(U):
        for j, ch in enumerate(row):
            if ch == '#':
                L.append([i,j])
    return L


def part_one (filename: str) -> str:
    dist = 0
    with open(filename, encoding="utf-8") as f:
        listed_Uni = f.read().strip().split("\n")

    listed_Uni = [list(x) for x in listed_Uni]

    listed_ex_uni = expand (listed_Uni)


    print (len(listed_ex_uni))
    print (len(listed_ex_uni[0]))

    # test expanded uni
    #for i in listed_ex_uni:
    #    print(''.join(i))

    locations = get_locations(listed_ex_uni)
    #print (len(locations))
    #print (locations)


    for i in range(len(locations)):
        #print ('gala: '+str(i+1))
        #print ('----------------')
        for j in range(i+1,len(locations),1):
            #print ('gala: '+str(j+1))
            distance_y = (locations[i][0] - locations[j][0])
            if distance_y < 0:
                distance_y = distance_y*-1
            
            distance_x =  (locations[i][1] - locations[j][1])

            if distance_x < 0:
                distance_x = distance_x *-1
            distance = distance_x+distance_y
            #print (distance)
            dist += distance
        #print ('===================')

    return dist


def part_two (filename: str) -> str:
    # multiplier
    M = 1000000
    dist = 0
    
    with open(filename, encoding="utf-8") as f:
        listed_Uni = f.read().strip().split("\n")

    listed_Uni = [list(x) for x in listed_Uni]

    uni = expand_m (listed_Uni)

    #print (len(listed_ex_uni))
    #print (len(listed_ex_uni[0]))

    # test expanded uni
    for i in uni:
        print(''.join(i))

    locations = get_locations(uni)
    #print (len(locations))
    #print (locations)

    uni_T = list(map(list, zip(*uni)))

    for i in range(len(locations)):
        #print ('gala: '+str(i+1))
        #print ('----------------')
        for j in range(i+1,len(locations),1):
            #print ('naar gala: '+str(j+1))
            x1 = locations[i][1]
            y1 = locations[i][0]
            x2 = locations[j][1]
            y2 = locations[j][0]
            
            #print (f"{x1} , {y1} naar {x2}, {y2}")

            x_line_all = uni[y1]
            y_line_all = uni_T[x2]

            d = 0
            if (x1 <x2):
                x_line = x_line_all[x1:x2]
            else:
                x_line = x_line_all[x2:x1]

            if (y1 < y2):
                y_line = y_line_all[y1:y2]
            else:
                y_line = y_line_all[y2:y1]

            #print (y_line)
            #print (X_line)
            #print()

            bij = (( y_line.count('M') * M) + (len(y_line)-y_line.count('M')) ) + (( x_line.count('M') * M) + (len(x_line)-x_line.count('M')) )
            #print (bij)
            dist = dist + bij
    return dist


if __name__ == "__main__":
    input_path = "./011/input.txt"
    #print("---Part One---")
    #print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))