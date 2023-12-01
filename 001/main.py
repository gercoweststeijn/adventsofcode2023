written_numbers = ['zero','one','two','three','four','five','six','seven','eight','nine'] # zero to easily detect position

def left_most_written (s:str):
    ret_num =''
    ret_pos = -1
    for number in written_numbers:
        pos = s.find(number)
        if pos > -1:
            if (pos < ret_pos) or (ret_pos == -1):
                ret_pos = pos
                ret_num = number
    return ret_pos, ret_num

def right_most_written (s:str):
    ret_num =''
    ret_pos = -1
    for number in written_numbers:
        pos = s.rfind(number)
        if pos > -1:
            if (pos > ret_pos) or (ret_pos == -1):
                ret_pos = pos
                ret_num = number
    return ret_pos, ret_num

def part_one(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    sum = 0
    for line in lines:
        part1 = ''
        part2 = ''
        # first number
        for i in range(len(line)):
            a = line [i]
            
            if line[i].isdigit():
                part1 = line[i]
                break

        # second number 
        if len(line) == 1:
            part2 = part1
        else:
            for i in range(len(line)-1,-1,-1):
                    b = line[i]
                    if line[i].isdigit():
                        part2 = line[i]
                        break
        
        additional = part1+part2

        if part1 == '' or part2 == '':
            print('-----------')
            print ('error')
            print (line)
            print('-----------')
        #print (additional)
        sum = sum + int(additional)
    return sum


def part_two(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")


    sum = 0
    for line in lines:

        pos1,part1 = left_most_written(line)
        if part1 != '':
            part1 = str(written_numbers.index(part1))
        else:
            pos1 = len(line)
        
        for i in range(0,pos1,1):
            a = line [i]
            
            if line[i].isdigit():
                part1 = line[i]
                break
            

            

        pos2,part2 = right_most_written(line)
        if part2 !='':
            part2 = str(written_numbers.index(part2))
        else:
            pos2 = 0

        for i in range(len(line)-1,pos2-1,-1):
            b = line [i]
            
            if line[i].isdigit():
                part2 = line[i]
                break       
               
        additional = part1+part2

        if part1 == '' or part2 == '':
            print('-----------')
            print ('error')
            print (line)

            print('-----------')
        #print (additional)
        sum = sum + int(additional)
    return sum




if __name__ == "__main__":
    input_path = "./adventsofcode/2023/001/input.txt"
    #print("---Part One---")
    #print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))