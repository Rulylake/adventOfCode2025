file = open("./Day4input")
layout = file.read().split("\n")

def part_one(layout):
    total = 0
    for y in range(len(layout)):
        for x in range(len(layout[y])):
            if is_tile_occupied(x,y,layout) and get_surrounding_tiles(x,y,layout) < 4:
                 total += 1

    return total

def part_two(layout):
    working_layout = []
    for row in layout:
        working_layout.append(list(row))

    total = 0
    change = True
    while change:
        change = False
        for y in range(len(working_layout)):
            for x in range(len(working_layout[y])):
                if is_tile_occupied(x,y,working_layout) and get_surrounding_tiles(x,y,working_layout) < 4:
                    working_layout[y][x] = '.'
                    change = True
                    total += 1
                    #print_layout(working_layout)

    return total

def print_layout(layout):
    print("----------------------------------------------")
    for row in layout:
        print(row)
    print("----------------------------------------------")


def get_surrounding_tiles(x,y,layout):
    total = 0
    for i in range(3):
        y_offset = i - 1
        for j in range(3):
            x_offset = j - 1

            if x_offset == 0 and y_offset == 0:
                continue

            if is_tile_occupied(x + x_offset, y + y_offset, layout):
                total += 1

    return total
            


    
def is_tile_occupied(x,y,layout):
    max_x = len(layout[0])
    max_y = len(layout)

    if x < 0 or x >= max_x:
        return False
    
    if y < 0 or y >= max_y:
        return False

    return layout[y][x] == '@'

print(part_two(layout))

goal = 13