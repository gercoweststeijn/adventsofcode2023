def count_A (xl, xh , ml,mh, al,ah, sl, sh, workflow, workflows):
    if rule == 'A':
        return (xh-xl)* (mh-ml)*(al-ah)*(al-ah)
    if rule == 'R':
        return 0
    
    cr = rule[0]
    
    if cr.count == 1:
        

    else:
        # true
        cr_letter = cr[0]
        cr_sign = cr[1]
        cr_amount = cr[2]
        if cr_sign == '<':
            if cr_sign == 'x':
                if cr_amount < xl:
                    break
                else:
                    return count_A (cr_amount, xh , ml,mh, al,ah, sl, sh, cr[3], workflows) + 
            if cr_sign == 'm':
                if cr_amount < ml:
                    break
                else:
                    return count_A (xl, xh , cr_amount,mh, al,ah, sl, sh, cr[3], workflows)

            if cr_sign == 'a':
                if cr_amount < al:
                    break
                else:
                    else count_A (xl, xh , ml,mh, cr_amount,ah, sl, sh, cr[3], workflows)
            if cr_sign == 's':
                if cr_amount < ml:
                    break
                else: 
                    else count_A (xl, xh , ml,mh, al,ah, cr_amount, sh, cr[3], workflows)
    
            
        
        count_A 

        


def part_two(filename):


    with open(filename, encoding="utf-8") as f:
       wf_block, item_block = f.read().strip().split("\n\n")

    workflows = {}
    for line in wf_block.splitlines():
        name, rest = line[:-1].split("{")
        rules = rest.split(",")
        workflows[name] = ([], rules.pop())
        for rule in rules:
            comparison, target = rule.split(":")
            key = comparison[0]
            cmp = comparison[1]
            n = int(comparison[2:])
            workflows[name][0].append((key, cmp, n, target))
    
    ret_val (count_A ())

    return 


def part_one(filename):


    with open(filename, encoding="utf-8") as f:
       wf_block, item_block = f.read().strip().split("\n\n")

    # get workflow rules
    wf = {}
    for wfi in wf_block.strip().split('\n'):
        name,r_str = wfi.split('{')
        rules = [x for x in r_str[:-1].split(',')]
        wf[name] = rules


    ret_val = 0
    items = item_block.strip().split("\n")                          
    for it in items:
        # strip to only have values remain -> we remember x=0,m=1,a=2,s=3
        item_vals =  [int(x[2:]) for x in (it[1:-1].split(','))]

        x = item_vals[0]
        m = item_vals[1]
        a = item_vals[2]
        s = item_vals[3]
        rule = 'in'
        while rule: 
            #print (f'zoeken voor regel {rule}')
            wf_rules = wf[rule]
            #print (wf_rules)
            for r in wf_rules:
                #print (r)
                if ':' in r:
                    apply, result = r.split(':')
                    if eval(apply):
                        if result == 'A':
                            ret_val += x+m+a+s
                            rule = ''
                            break
                        elif result == 'R':
                            ret_val += 0
                            rule = ''
                            break
                        else:
                            rule = result
                            break # on to the next
                else:
                    if r == 'A':
                        ret_val += x+m+a+s
                        rule = ''
                        break
                    elif r == 'R':
                        ret_val += 0
                        rule = ''
                        break
                    else:
                        rule = r
                        break # on to the next
    
    return ret_val

 

if __name__ == "__main__":
    input_path = "./019/input.txt"
    #print("---Part One---")
    #print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))