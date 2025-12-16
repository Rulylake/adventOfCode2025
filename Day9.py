import OrderedDict as OD

file = open("./Day9input")
corners = file.read().split('\n')

def part_one(corners):
    biggest = 0

    cleaned_corners = clean_corners(corners)

    for i in range(len(cleaned_corners)):
        cor1 = cleaned_corners[i]
        for j in range(i+1, len(cleaned_corners)):
            cor2 = cleaned_corners[j]
            size = size_of_square(cor1, cor2)
            if size > biggest:
                biggest = size

    return biggest

def clean_corners(corners):
    clean = []

    for corner in corners:
        split_corner = corner.split(',')
        clean.append((int(split_corner[0]), int(split_corner[1])))

    return clean

def size_of_square(cor1, cor2):
    x = abs(cor1[0] - cor2[0]) + 1
    y = abs(cor1[1] - cor2[1]) + 1

    return x * y

print(part_one(corners))