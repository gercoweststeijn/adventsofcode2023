def vertical_rows_above(rows, fs):
    
    # print ('**************************')
    # print (rows)
    # print ('**************************')
    transposed =  [''.join(s) for s in zip(*rows)]
    
    # print ('**************************')
    # print (transposed)
    # print ('**************************')
    #print ('*********************************************************')
    retval = horizontal_col_to_left (transposed, fs)
    return retval 
                    

                            
#   '# .##. .##.'


def horizontal_col_to_left (rows, fs):
    

    # we only inspect the top row - reflection must be on all rows
    row = rows[0]

    # left side 
    half_row_len = round (int((len(row)/2)))

    for left in range(half_row_len):
        right = left+1
        
        #if (left+1)*2 > len(row):
        #    ref_length = int(len(row))-(left+1)
        #else:
        ref_length = left+1

        left_part = row[0:right]
        right_part_str = row[right:right+ref_length] 
        right_part = right_part_str[::-1]

        #print (f'compare L0,{right}: {left_part} R{right},{right+ref_length}: {right_part}')
        if right_part == left_part:
            # search for more rows with this 
            no_counter_example = True
            for row in rows: 
                left_part = row[0:right]
                right_part_str = row[right:right+ref_length] 
                right_part = right_part_str[::-1]
        
                if right_part != left_part:
                    no_counter_example = False
                    break
                #print (f'gevonden bij left:  {left}')
            if no_counter_example and (fs!=left+1 or fs is None) :
                return left +1
    #print ('------------------------')
    # second half 
    for left in range(half_row_len, len(row)):
        right = left+1
        
        ref_length = int(len(row))-(right)
        if ref_length > 0: 
            left_part = row[(left-(ref_length))+1:right]
            right_part_str = row[right:right+ref_length]       
            right_part = right_part_str[::-1]

            #print (f'compare L{(left-(ref_length))+1},{right}: {left_part} R{right},{right+ref_length}: {right_part}')

            if left_part == right_part:
                # search for more rows with this 
                no_counter_example = True
                for row in rows:
                    left_part = row[(left-(ref_length))+1:right]
                    right_part_str = row[right:right+ref_length]       
                    right_part = right_part_str[::-1]
                    
                    if  left_part != right_part:
                        no_counter_example = False
                        break
                    #print (f'gevonden bij left:  {left}')
                if no_counter_example and (fs!=left+1 or fs is None):
                    return left +1
    return 0    


def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        parts = f.read().strip().split("\n\n")

    result = 0
    for part in parts:
        #print ('Part------------------------------')
        rows = part.split('\n')
        horizontal = horizontal_col_to_left (rows, None)
        #print (f'horizontal left: {horizontal} ')
        result += horizontal
        vertical = vertical_rows_above(rows, None) * 100 
        #print (f'vertical top : {vertical} ')

        if horizontal> 0 and vertical>0: 
                print ('Beide in 1')
        result += vertical
    return result


def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        parts = f.read().strip().split("\n\n")

    
    result = 0
    for x,part in enumerate (parts):
        #print ('part')
        part_result = 0
        for i,c in enumerate (part):
            rows = part.split('\n')
            filty_score_horizontal = horizontal_col_to_left (rows, None)
            filty_score_vertical    = vertical_rows_above (rows, None )

            horizontal = 0
            vertical = 0

            #print (f'{i} in {c} voor orgineel: {part}' )
            if c == '#':
               cleaned_part = part[0:i]+'.'+part[i+1:]
            elif c== '.':
               cleaned_part = part[0:i]+'#'+part[i+1:]
            else:
                continue
            #print (cleaned_part)
            #print ('===')
            #print (f'{i} in {c} // optie: {cleaned_part}' )
            rows2 = cleaned_part.split('\n')
            #print (f'rows: {rows}')
            horizontal = horizontal_col_to_left (rows2, filty_score_horizontal)
            #print (f'horizontal left: {horizontal} ')
            part_result += horizontal

            #if horizontal == 0: 
            vertical = vertical_rows_above(rows2, filty_score_vertical) * 100 
            #print (f'vertical top : {vertical} ')
            
            part_result += vertical
            
            if horizontal> 0 and vertical>0: 
                for i in rows:
                    print (i)
                print ('Beide')
                print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                for i in rows2:
                    print (i)
                print (f'horizontal: {horizontal} vertical: {vertical/100}')
            
            if part_result > 0:
                #print (f'gevonden bij wijziging: {i}')
                #print (f'horizontal: {horizontal} vertical: {vertical}')
                break
        if part_result == 0: 
            print (f'ERROR!!!!  part:{X}')
            
        result = result + part_result
    return result


if __name__ == "__main__":
    input_path = "./013/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))