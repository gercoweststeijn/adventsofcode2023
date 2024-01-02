
#Check for two bricks to overlap on thje x and ys 
def bricks_overlap (b1, b2):
    return (    max(b1[0], b2[0]) <= min(b1[3], b2[3])
            and max(b1[1], b2[1]) <= min(b1[4], b2[4]))


def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().replace('~',',',).split("\n")
    
    
    bricks = [x.split(',') for x in lines]
    for i,b in enumerate(bricks):
        bricks[i] = list(map(int,b))
    

    # for b in bricks:
    #     print (b)

    # print ()

    #for l in lines:        
    #    ins_map.append(list(l))
    
    #sort bricks - by Z value
    bricks.sort(key = lambda brick:  brick[2])


    # drop bricks
    for i,brick in enumerate(bricks):
        max_z = 1 # the ground

        height_brick = (brick[5]) - (brick[2])

        for brick_below in bricks[:i]:
            if bricks_overlap(b1=brick_below, b2=brick):
                #if they overlap drop till z of compararative
                max_z = max(max_z, brick_below[5]+1)
        brick[2] = max_z
        brick[5] = max_z + height_brick

    

    # resort #sort bricks - by Z value
    bricks.sort(key = lambda brick:  brick[2])


    # for b in bricks:
    #     print (b)


    bricks_supported_by = {i: set() for i in range(len(bricks))}
    bricks_supports   = {i: set() for i in range(len(bricks))}

    for i,brick1 in enumerate(bricks):
        for j , brick2 in enumerate(bricks[:i]):
            if bricks_overlap(brick1, brick2) and brick1[2] == brick2[5]+1:
                bricks_supported_by[i].add(j) # bricks 1 is supported by 2 
                bricks_supports[j].add(i) # 2 supports 1


    result = 0
    for i in range(len(bricks)):
        if all(len(bricks_supported_by[j]) >= 2 for j in bricks_supports[i]):
            result += 1

    

    return result 

  

if __name__ == "__main__":
    input_path = "./022/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    #print("---Part Two---")
    #print(part_two(input_path))