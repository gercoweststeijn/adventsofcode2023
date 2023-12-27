from collections import defaultdict

def part_two(filename: str) -> str:
    
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
        N = defaultdict(int)
        for i,line in enumerate(lines): 
            N[i] += 1
            part1, part2 = line.split('|')
            card_nr, mynums =part1.strip().split(':')
            card_nums = [int(x) for x in mynums.strip().split()  ]
            winning_nums = [int(x) for x in part2.split()]  
        
            overlap = len(set(card_nums) & set (winning_nums))
            for j in range (overlap):
                N[i+1+j] += N[i]        
    return sum(N.values())

def part_one(filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    result = 0        
       
    for i,line in enumerate(lines): 
        part1, part2 = line.split('|')
        card_nr, mynums =part1.strip().split(':')
        card_nums = [int(x) for x in mynums.strip().split()  ]
        winning_nums = [int(x) for x in part2.split()]  
    
        overlap = len(set(card_nums) & set (winning_nums))
        if overlap > 0:
            result+=2**(overlap-1)
    return result

if __name__ == "__main__":
    input_path = "./004/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part two---")
    print(part_two(input_path))