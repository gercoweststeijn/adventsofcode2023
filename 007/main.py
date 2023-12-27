

def det_hand_J (hand: str, nr_jokers: int) -> int:
#
# rate 10 - 4 pokerhands
# 8
    if nr_jokers == 5:
        return 10 # five
    elif nr_jokers == 4:
        return 10 # five
    elif nr_jokers == 3:
        # five or four
        # remaining str pair or one
        if hand.count(hand[0]) == 2:
            return 10
        else:
            return 9
    elif nr_jokers == 2:
        if hand.count(hand[0]) == 3:
            return 10 # five
        elif hand.count(hand[0]) == 2 or hand.count(hand[1]) == 2:
            return 9 # four 
        else: # three diff in remaining string
            return 7 # three # full house not a score with 2 jokers

    elif nr_jokers == 1:
        if hand.count(hand[0]) == 4:
            return 10 # five
        elif hand.count(hand[0]) ==3 or hand.count(hand[1]) ==3:
            return  9 # four

        elif hand.count(hand[0]) ==2 or hand.count(hand[1]) ==2 or hand.count(hand[2]) ==2:
            pairs = 0
            for card in hand:
                if hand.count(card) == 2:
                    pairs = pairs + 1
            if pairs/2 == 2:
                return 8 #full house
            else:
                return  7 #three
        # two pair not an option -> joker will be use to make trhee not two pair
        else:
            return 5 # pair
    # 0 jokers
    else:
        return (det_hand (hand = hand))

def det_hand (hand: str) -> int:
#
# rate 10 - 4 pokerhands
# 8
    if hand.count(hand[0]) == 5:
        return 10 # five
    elif hand.count(hand[0]) ==4 or hand.count(hand[1]) ==4:
        return 9 # four
    # this will not work for real comparson
    elif hand.count(hand[0]) ==3 or hand.count(hand[1]) ==3 or hand.count(hand[2]) ==3:
        for card in hand:
            if hand.count(card) == 2:
                return 8 # full House
            # not a pair extra 
        return 7   # three
    elif hand.count(hand[0]) ==2 or hand.count(hand[1]) ==2 or hand.count(hand[2]) ==2 or hand.count(hand[3]) ==2:
        pairs = 0
        for card in hand:
            if hand.count(card) == 2:
                pairs = pairs + 1
        if pairs/2 == 2:
            return 6 # two pair
        else:
            return 5 # pair
    else:
        return 4 # one
    
def sorter_f (s: str) -> str:
    s = s.split(' ')[0]
    HV =''
    for i in range(len(s)):
        index_val_char = chr ((65+12) - card_range.index(s[i]))
        HV = HV + index_val_char
    return det_hand(s), HV

def sorter_fj (s: str) -> str:
    s = s.split(' ')[0]
    HV =''
    for i in range(len(s)):
        index_val_char = chr ((65+12) - card_range.index(s[i]))
        HV = HV + index_val_char

    nr_j = s.count('J')
    s = s.replace('J','')
    return det_hand_J(s,nr_j), HV


def part_one(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().split(("\n"))

        lines.sort( key = sorter_f, reverse=False)

        sum = 0
        for i in range(len(lines)):
            sum = sum + (int((lines[i].split(' ')[1])) *  (i+1) )
    return sum

def part_two(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().split(("\n"))

        lines.sort( key = sorter_fj, reverse=False)

        sum = 0
        for i in range(len(lines)):
            
            

            sum = sum + (int((lines[i].split(' ')[1])) *  (i+1) )
            #print (lines [i])
    return sum

if __name__ == "__main__":
    card_range = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

    input_path = "./007/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    card_range = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    print("---Part two---")
    print(part_two(input_path))