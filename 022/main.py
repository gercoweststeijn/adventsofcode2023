def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")
    ins_map = []
    for l in lines:        
        ins_map.append(list(l))
    
    result = 0 

    return result 

  

if __name__ == "__main__":
    input_path = "./022/tst.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))