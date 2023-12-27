import numpy

def part_one (filename):
    with open(filename, encoding="utf-8") as f:
        part1, part2 = f.read().split(("\n"))
    time =  [int(x) for x in part1.split(':')[1].split()]
    distance = [int(x) for x in part2.split(':')[1].split()]

    
    #races = zip(time, distance)
    #print (list(races))

    R = []
    for i in range(len(time)):
        given_time = time[i]
        required_distance = distance[i]
        
        winners = 0

        for j in range (given_time):
            time_traveled = given_time - j
            speed = j
            travelled = speed * time_traveled
            if travelled > required_distance:
                winners = winners +1
        R.append(winners)

    return numpy.prod(R)

def part_two ():
    

    
    
    given_time = 57726992
    required_distance = 291117211762026
    
    winners = 0

    #R = []
    for j in range (given_time):
        
        time_traveled = given_time - j
        speed = j
        travelled = speed * time_traveled
        if travelled > required_distance:
            winners = winners +1
            
            #print (str(j) + 'ja')
        #else:
            
            #print (str(j) + 'nee')
    #R.append(winners)

    return (winners)




if __name__ == "__main__":
    input_path = "./006/input.txt"
    print("---Part One---")
    print(part_one(input_path))

    print("---Part two---")
    print(part_two())