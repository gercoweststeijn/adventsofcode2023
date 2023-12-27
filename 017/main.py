from heapq import heappop, heappush


def part_one (filename: str) -> str:
    #with open(filename, encoding="utf-8") as f:
    #   lines = f.read().strip().split("\n")

    # grid = []
    # for l in lines:        
    #     grid.append(list(l))

    grid = [list(map(int, line.strip())) for line in open(input_path)]

    #print (grid)
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        # heatloss
        # current row
        # current possition
        # direction rows
        # direction collumns
        # nr of times same direection


        # always pop the top contender - current minimal heatloss
        hl, r, c, dr, dc, n = heappop(pq)
        
        # this will always be minimal as the list is sorted and 
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return hl

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 3 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # not the current direction (covered above) or reverse - not allowed
            if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                # new position col and row
                nr = r + ndr
                nc = c + ndc
                # check if they are inbound 
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))



def part_two (filename: str) -> str:
    #with open(filename, encoding="utf-8") as f:
    #   lines = f.read().strip().split("\n")

    # grid = []
    # for l in lines:        
    #     grid.append(list(l))

    grid = [list(map(int, line.strip())) for line in open(input_path)]

    #print (grid)
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]

    while pq:
        # heatloss
        # current row
        # current possition
        # direction rows
        # direction collumns
        # nr of times same direection


        # always pop the top contender - current minimal heatloss
        hl, r, c, dr, dc, n = heappop(pq)
        
        if r == len(grid) - 1 and c == len(grid[0]) - 1 and n >= 4:
            return (hl)
            

        if (r, c, dr, dc, n) in seen:
            continue

        seen.add((r, c, dr, dc, n))
        
        if n < 10 and (dr, dc) != (0, 0):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(pq, (hl + grid[nr][nc], nr, nc, dr, dc, n + 1))

        # note steps of 4 ... n wehere n> 4
        if n >= 4 or (dr, dc) == (0, 0):
            for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
                    nr = r + ndr
                    nc = c + ndc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        heappush(pq, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))

    

  

if __name__ == "__main__":
    input_path = "./017/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))