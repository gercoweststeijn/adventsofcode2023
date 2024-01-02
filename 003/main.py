
def determine_surrounding_symbols (line_nr: str, xpos1: str, xpos2: str, lines: list) -> int:
    surrounding_symbols = ''
    
    ret_val = lines[line_nr][xpos1:xpos2]

    # tst top layer
    if (line_nr - 1) >= 0: 
        y_pos = line_nr - 1
        for i in range(xpos1 -1, xpos2+1):
            if i >= 0 and i < len (lines[y_pos]):
                tst_chr = lines[y_pos][i]
                if 1 == 1: #if (not tst_chr.isdigit()) :
                    if (tst_chr != '.'):                        
                        print (ret_val)
                        return int(ret_val)
                    
    # tst bottom layer
    if (line_nr + 1) < len(lines): 
        y_pos = line_nr +1
        for i in range(xpos1 -1, xpos2+1 ):
            if i >= 0 and i < len (lines[y_pos]):
                tst_chr = lines[y_pos][i]
                if 1 == 1: #if (not tst_chr.isdigit()) :
                    if (tst_chr != '.'):                        
                        print (ret_val)
                        return int(ret_val)
                    
    # test neighbours
    y_pos = line_nr
    if xpos1-1 > 0:
        i = xpos1 -1
        tst_chr = lines[y_pos][i]
        if 1 == 1: #if (not tst_chr.isdigit()) :
                    if (tst_chr != '.'):                        
                        print (ret_val)
                        return int(ret_val)
    

    if xpos2 < len(lines[y_pos]):
        i = xpos2 
        tst_chr = lines[y_pos][i]
        if 1 == 1: #if (not tst_chr.isdigit()) :
                    if (tst_chr != '.'):                        
                        print (ret_val)
                        return int(ret_val)
    
    print (ret_val+'   niet gevonden')
    return 0 

def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    sum = 0 

    line_index_start_pos = 0
    for line in lines:
        char_index_start_pos = 0 
        length = 0
        i = 0 
        first_digit = True
        while i < len (line):
            test_char = line[i]

            # is this the last char of the line?
            if i == len(line)-1:
                if test_char.isdigit():
                    if first_digit: 
                        first_digit = False # do we need this? 
                        char_index_start_pos = i
                        length = 0
                    else:
                        length = length + 1

                    print ('line ' + str(line_index_start_pos) + ' x pos ' + str(char_index_start_pos) +' to: '+ str(char_index_start_pos + length)) 
                    sum = sum + determine_surrounding_symbols(  line_nr = line_index_start_pos
                                                                , xpos1= char_index_start_pos
                                                                , xpos2= char_index_start_pos + length +1
                                                                , lines = lines)
                else:
                    if length > 0: 
                        print ('line ' + str(line_index_start_pos) + ' x pos ' + str(char_index_start_pos) +' to: '+ str(char_index_start_pos + length)) 
                        sum = sum + determine_surrounding_symbols(  line_nr = line_index_start_pos
                                                                , xpos1= char_index_start_pos
                                                                , xpos2= char_index_start_pos + length +1
                                                                , lines = lines)
                        length = 0 

            else:
                if test_char.isdigit():
                    # first digit of new number?
                    if first_digit: 
                        first_digit = False
                        char_index_start_pos = i
                        length = 0
                    else:
                        length = length + 1
                # no digit: end of numbe or just noise
                else:
                    first_digit = True

                    if length > 0:
                        print ('line ' + str(line_index_start_pos) + ' x pos ' + str(char_index_start_pos) +' to: '+ str(char_index_start_pos + length)) 
                        sum = sum + determine_surrounding_symbols(  line_nr = line_index_start_pos
                                                                , xpos1= char_index_start_pos
                                                                , xpos2= char_index_start_pos + length +1
                                                                , lines = lines)
                        

                        length = 0
            i = i + 1

        line_index_start_pos = line_index_start_pos+1    
    return  sum



def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    

    return       


if __name__ == "__main__":
    input_path = "./003/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))