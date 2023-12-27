def nvl_str(input):
    if input is None:
        return ''
    else:
        return input
                
def drop_stone(line):
    if line=="":
        return ''
    else:
        dots = 0
        boulders = 0
        for i,c in enumerate(line): 
            if c == '#':
                return 'O'*boulders + '.'*dots + '#' +  drop_stone (line[i+1:])
            if c == '.':
                dots += 1
            if c == 'O':
                boulders +=1
        return 'O'*boulders + '.'*dots 

                


def drop_stones (lines):
    R = []
    for l in lines:
        #print (f'org: {l}   {len(l)}')
        new_l = drop_stone(l)
        #print (f'new: {new_l}    {len(new_l)}')
        #print ('')
        R.append(new_l)

    return R


def jump_stone(line):
    if line=="":
        return ''
    else:
        dots = 0
        boulders = 0
        for i,c in enumerate(line): 
            if c == '#':
                return '.'*dots + 'O'*boulders + '#' +  drop_stone (line[i+1:])
            if c == '.':
                dots += 1
            if c == 'O':
                boulders +=1
        return  '.'*dots + 'O'*boulders


def jump_stones (lines):
    R = []
    for l in lines:
        #print (f'org: {l}   {len(l)}')
       
        new_l = jump_stone(l)
        #new_l = new_l[::-1]
      
       
        #print (f'new: {new_l}    {len(new_l)}')
        #print ('')
        R.append(new_l)

    return R

def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")


    result = 0 
    # to let grafity do its work we go by 'drop lines'
    transposed =  [''.join(s) for s in zip(*lines)]
    
    #for l in transposed:
    #    print (l)
    #print (transposed)
    grav_lines_t = drop_stones (transposed)

    grav_lines = [''.join(s) for s in zip(*grav_lines_t)]

    for i,l in enumerate(grav_lines[::-1]):
        result += (i+1) * l.count('O')

    return result 



def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")


    for l in lines:
        print (l)
    print ('---------------')
    print ('---------------')

    result = 0 
    # to let grafity do its work we go by 'drop lines'
    NR_to_go_round = 0
    S = []
    #loop
    first = True
    for i in range(1):
        # north 
        print ('------------North--------------')
        if first:
            grav_lines =  [''.join(s) for s in zip(*lines)]
            first = False
        else: 
            grav_lines =  [''.join(s) for s in zip(*grav_lines)]
        grav_lines = drop_stones (grav_lines)
        grav_lines = [''.join(s) for s in zip(*grav_lines)]

        for l in grav_lines:
            print (l)
        print ('---')

        print ('------------West--------------')
        # west 
        grav_lines = drop_stones (grav_lines)

        for l in grav_lines:
            print (l)
        print ('---')


        print ('------------South--------------')

        # south 
        grav_lines =  [''.join(s) for s in zip(*grav_lines)]
        print ('--T-')
        for l in grav_lines:
            print (l)
        print ('---')

        grav_lines = jump_stones (grav_lines)

        print ('--jumped-')
        for l in grav_lines:
            print (l)

        print ('--re transpos-')
        grav_lines = [''.join(s) for s in zip(*grav_lines)]

        for l in grav_lines:
            print (l)
        print ('---')

        print ('------------East--------------')
        # east 
        grav_lines = jump_stones(grav_lines)
        for l in grav_lines:
            print (l)

        print ('==========one cycle =========')
        # print ('------------====--------------')
        # if i<3:
        #     for l in grav_lines:
        #         print (l)
        #     print ('')
        #     print ('')

        if grav_lines in S:
            NR_to_go_round = i -1
        else: 
            # write end_result see when the cycle repeats
            S.append(grav_lines)

        if i<3:
            for l in grav_lines:
                print (l)
            print ('')
            print ('')

    
    print (NR_to_go_round)


    times_to_go = 1000000000%NR_to_go_round

    for i in range(times_to_go):
        # north 
        grav_lines =  [''.join(s) for s in zip(*lines)]
        grav_lines = drop_stones (grav_lines)
        grav_lines = [''.join(s) for s in zip(*grav_lines)]

        # west 
        grav_lines = drop_stones (grav_lines)

        # south 
        grav_lines =  [''.join(s) for s in zip(*lines)]
        grav_lines = jump_stones (grav_lines)
        grav_lines = [''.join(s) for s in zip(*grav_lines)]
        # east 
        grav_lines = jump_stones(grav_lines)


    for i,l in enumerate(grav_lines[::-1]):
        result += (i+1) * l.count('O')
    
    return result 

  

if __name__ == "__main__":
    input_path = "./014/test.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))