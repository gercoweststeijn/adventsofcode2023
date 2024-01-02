RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14


def part_one (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    sum = 0
    for line in lines:
        this_line_counts = True

        # split game and sets
        game, all_sets_per_game = line.split(':')
        # get only number, second part
        game_nr = game.split(' ')[1] 
        
        # eval sets
        sets = all_sets_per_game.split(';')
        for set in sets:
            # split the colors per set
            color_list = set.split(',')
            for c in color_list:
                number, color = c.strip().split(' ')
                match color:
                    case 'red':
                        if int(number) > RED_LIMIT:
                            this_line_counts = False
                    case 'green':
                        if int(number) > GREEN_LIMIT:
                            this_line_counts = False
                    case 'blue':
                        if int(number) > BLUE_LIMIT:
                            this_line_counts = False
        if this_line_counts:
            sum = sum + int(game_nr)

    return sum

def part_two (filename: str) -> str:
    with open(filename, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    sum = 0
    for line in lines:
        
        max_green = 1
        max_blue = 1
        max_red = 1

        # split game and sets
        game, all_sets_per_game = line.split(':')
        # get only number, second part
        game_nr = game.split(' ')[1] 
        
        # eval sets
        sets = all_sets_per_game.split(';')
        for set in sets:
            # split the colors per set
            color_list = set.split(',')
            for c in color_list:
                number, color = c.strip().split(' ')
                match color:
                    case 'red':
                        if int(number) > max_red:
                            max_red = int(number)
                    case 'green':
                        if int(number) > max_green:
                            max_green = int(number)
                    case 'blue':
                        if int(number) > max_blue:
                            max_blue = int(number)
        #            
        power_this_game = max_red*max_green*max_blue
        sum = sum + power_this_game

    return sum           


if __name__ == "__main__":
    input_path = "./002/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))