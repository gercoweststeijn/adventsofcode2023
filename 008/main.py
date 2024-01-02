

def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        steps, bottom = f.read().strip().split("\n\n")
    
    lines = bottom.strip().split('\n')


    #map = {'starter':[],'direction':[]}
    for line in lines:
        starter, direction_str = line.split('=')
        direction_str = direction_str.replace(' (', '')
        direction_str = direction_str.replace(')', '')
        directions = direction_str.split(',')

        a = str(starter.strip())
        print (type(a))
        map[a] = directions

       

        # map['starter'].append(starter)
        # map['direction'].append(directions)
    

        print (map)
    

    return       


if __name__ == "__main__":
    input_path = "./008/tst.txt"
    print("---Part One---")
    print(part_one(input_path))

    #print("---Part Two---")
    #print(part_two(input_path))