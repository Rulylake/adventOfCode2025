import math
import random

file = open("./Day8input")
boxes = file.read().split("\n")

def part_one(boxes, nr_of_boxes, nr_of_best):

    clean_boxes = clean_coord_list(boxes)

    coord_count = len(clean_boxes)

    coord_dict = orderd_dict(2*nr_of_boxes)

    for i in range(coord_count):
        coord1 = clean_boxes[i]
        for j in range(i+1,coord_count):
            coord2 = clean_boxes[j]

            distance = distance_between(coord1, coord2)

            coord_dict.insert((coord1, coord2), distance)

    print(coord_dict)

    circuits = []

    i = 0
    while i < nr_of_boxes:

        shortest = coord_dict.pop_smallest()

        shortest = shortest[0]

        circuit_one = False
        circuit_two = False

        usless_round = False
        
        for circiuit in circuits:
            
            
            a = shortest[0] in circiuit
            b = shortest[1] in circiuit

            if a and b:
                #nr_of_boxes += 1
                usless_round = True
                break
            elif a or b:
                if circuit_one:
                    circuit_two = circiuit
                    break
                else:
                    circuit_one = circiuit
                    

                '''
                circiuit.add(shortest[0])
                circiuit.add(shortest[1])
                in_a_circuit = True
                break
                '''

        if circuit_two:
            print("Sätter Samman:")
            print(shortest)
            print(circuit_one)
            print(circuit_two)

            circuits.remove(circuit_one)
            circuits.remove(circuit_two)

            new_set = set()
            for elem in circuit_one:
                new_set.add(elem)

            for elem in circuit_two:
                new_set.add(elem) 

            new_set.add(shortest[0])
            new_set.add(shortest[1])


            circuits.append(new_set)

        elif circuit_one:
            print("Sätter Samman:")
            print(shortest)
            print(circuit_one)
            
            circuits.remove(circuit_one)

            new_set = set()
            for elem in circuit_one:
                new_set.add(elem) 

            new_set.add(shortest[0])
            new_set.add(shortest[1])


            circuits.append(new_set)
        elif not usless_round:
            print("Skapar Nytt set:")
            print(shortest)

            new_set = set()

            new_set.add(shortest[0])
            new_set.add(shortest[1])

            circuits.append(new_set)

        
        print()

        i += 1

    first = []
    second = []
    third = []



    for circut in circuits:
        print((circut))
        if len(circut) > len(third):
            third = circut
            if len(third) > len(second):
                second, third = third, second
                if len(second) > len(first):
                    first, second = second, first

    total = len(first) * len(second) * len(third)

    return total

def part_two(boxes, nr_of_boxes):

    clean_boxes = clean_coord_list(boxes)

    coord_count = len(clean_boxes)

    coord_dict = orderd_dict(1000*nr_of_boxes)

    for i in range(coord_count):
        coord1 = clean_boxes[i]
        for j in range(i+1,coord_count):
            coord2 = clean_boxes[j]

            distance = distance_between(coord1, coord2)

            coord_dict.insert((coord1, coord2), distance)

    #print(coord_dict)

    circuits = []
    shortest = (0,0)

    i = 0
    while i < 5 or not len(circuits[0]) == coord_count:

        shortest = coord_dict.pop_smallest()

        shortest = shortest[0]

        circuit_one = False
        circuit_two = False

        usless_round = False
        
        for circiuit in circuits:
            
            
            a = shortest[0] in circiuit
            b = shortest[1] in circiuit

            if a and b:
                #nr_of_boxes += 1
                usless_round = True
                break
            elif a or b:
                if circuit_one:
                    circuit_two = circiuit
                    break
                else:
                    circuit_one = circiuit
                    

                '''
                circiuit.add(shortest[0])
                circiuit.add(shortest[1])
                in_a_circuit = True
                break
                '''

        if circuit_two:
            print("Sätter Samman:")
            print(shortest)
            print(circuit_one)
            print(circuit_two)

            circuits.remove(circuit_one)
            circuits.remove(circuit_two)

            new_set = set()
            for elem in circuit_one:
                new_set.add(elem)

            for elem in circuit_two:
                new_set.add(elem) 

            new_set.add(shortest[0])
            new_set.add(shortest[1])


            circuits.append(new_set)

        elif circuit_one:
            print("Sätter Samman:")
            print(shortest)
            print(circuit_one)
            
            circuits.remove(circuit_one)

            new_set = set()
            for elem in circuit_one:
                new_set.add(elem) 

            new_set.add(shortest[0])
            new_set.add(shortest[1])


            circuits.append(new_set)
        elif not usless_round:
            print("Skapar Nytt set:")
            print(shortest)

            new_set = set()

            new_set.add(shortest[0])
            new_set.add(shortest[1])

            circuits.append(new_set)

        
        print()

        i += 1



    return shortest[0][0] * shortest[1][0]
        

    


def distance_between(coord1, coord2):
    coord = []
    for i in range(3):
        coord.append(coord1[i] - coord2[i])

    distance = math.sqrt(coord[0]**2 + coord[1]**2 + coord[2]**2)

    return distance

def clean_coord_list(coords):
    clean_coords = []
    clean_coord = []

    for coord in coords:
        split_coord = coord.split(',')
        for i in range(3):
            clean_coord.append(int(split_coord[i]))

        clean_coords.append(tuple(clean_coord))
        clean_coord = []
        

    return clean_coords

class orderd_dict():
    values = []
    keys = []
    length = 0
    max_length = 0
    longest_distance = 0

    def __init__(self, max_length):
        self.max_length = max_length
        

    def insert(self, key, new_number):
        if (self.length == self.max_length):
            if(new_number >= self.longest_distance):
                return
            
            self.pop_biggest()

        failure = True
        self.length += 1
        for i, number in enumerate(self.values):
            if new_number >= number:
                self.values = self.values[:i] + [new_number] + self.values[i:]
                self.keys = self.keys[:i] + [key] + self.keys[i:]
                failure = False
                break

        if failure:
            self.values += [new_number]
            self.keys += [key]

        self.longest_distance = self.values[0]

    def get(self, desired_key):
        for i, key in enumerate(self.keys):
            if key == desired_key:
                return self.values[i]
            
        print("Key not Found")
        return None


    def pop_biggest(self):
        self.length -= 1
        biggest = self.keys[0], self.values[0]
        self.values = self.values[1:]
        self.keys = self.keys[1:]
        if self.values != []:
            self.longest_distance = self.values[0]
        return biggest
    
    def pop_smallest(self):
        self.length -= 1
        smallest = self.keys[-1], self.values[-1]
        self.values = self.values[:-1]
        self.keys = self.keys[:-1]
        if self.values != []:
            self.longest_distance = self.values[0]
        return smallest

    def __str__(self):
        nice_string = ""
        for i in range(self.length):
            nice_string += str(self.keys[i]) + " : " + str(self.values[i]) + "\n"

        nice_string += "Length = " + str(self.length)

        return nice_string
    
#print(part_one(boxes, 10, 3))

print(part_two(boxes, 10))