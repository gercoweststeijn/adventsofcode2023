return_set =[]

def fill_blanks(blank_positions, con_list, to_do):
    if to_do == 0:
        return return_set.append(con_list)
    else:
        new_con_list_ht = con_list.copy()
        new_con_list_dt = con_list.copy()
        new_con_list_ht[blank_positions[0]] = '#'
        new_con_list_dt[blank_positions[0]] = '.'
        
        blank_positions.pop(0)
        fill_blanks (blank_positions,new_con_list_ht,to_do-1)
        fill_blanks (blank_positions,new_con_list_dt,to_do-1)



    



def BF_number_arrangements (con, des):
    set = []
    positions_qm = [i for i, c in enumerate(con) if c == '?']
    all_options = fill_blanks(positions_qm,con,len(positions_qm))

    print (all_options)
    # for i,p in enumerate(positions_qm):
    #     if i+1 == len(positions_qm):
    #         last = True
    #     else:
    #         last = False

    #     for symbol in ['#', '.']:
    #         con[p] = symbol
    #         if last: 
    #             set.append(con)
   
            
            




    print (set) 
    return len(set)







def part_one (filename: str) -> str:
    res = 0
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    for line in lines:
      conditions,descr  = line.split()
      description = descr.split(',')
      conditions = list(conditions)
      print (f'{conditions} {description}')
      print ('=========================')
      print( BF_number_arrangements (conditions, descr) )
      print ('=========================')


def part_two (filename: str) -> str:
    
    


    
    return ''


if __name__ == "__main__":
    input_path = "./012/tst.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))