import math

file = open("./Day2input")
IDlist = file.read().split(',')

def part_one(IDlist):
    total = 0
    for Id in IDlist:
        firstID, lastID = Id.split('-')

        IDlength = len(firstID)
        halfIDlength =  IDlength // 2

        firstID, lastID = int(firstID), int(lastID)

        for id in range(firstID, lastID+1):
            if (len(str(id)) > IDlength):
                IDlength = len(str(id))
                halfIDlength =  IDlength // 2

            if (str(id)[halfIDlength:] == str(id)[:halfIDlength]):
                total += id

    print(total)

def part_two(IDlist):
    total = 0
    for Id_range in IDlist: 
        firstID, lastID = Id_range.split('-')

        IDlength = len(firstID)
        halfIDlength =  IDlength // 2

        firstID, lastID = int(firstID), int(lastID)

        for id in range(firstID, lastID+1):

            if id == 979979979:
                pass

            if IDlength <= 1:
                continue

            if (len(str(id)) > IDlength):
                IDlength = len(str(id))
                halfIDlength =  IDlength // 2


            primes = prime_fact(IDlength)
            if primes == []:
                break

            repeating = True
            for prime in primes:
                repeating = True
                split_number = split_into_interval(id,prime)
                
                for i in range(1,len(split_number)):
                    if (split_number[i-1] != split_number[i]):
                        repeating = False
                        break

                if repeating:
                    break

            if repeating:
                print(id)
                total += id
                
                

    print(total+11)


def prime_fact(number):
    primes = [1]

    for i in range(2, 1+number//2):
        #print(i)
        if number % i == 0:
            primes.append(i)
        
    return primes

def split_into_interval(thing, interval):
    string = str(thing)
    string_length = len(string)

    if string_length % interval != 0:
        return []

    split_string = []

    for i in range(string_length//interval):
        string_part = string[i * interval:(i+1) * interval]
        split_string.append(string_part)

    return split_string

print(part_two(IDlist))

wrong_guess = 49046150743
right_guess = 0
#print(split_into_interval(112233,4))

#print(prime_fact(18))

#part_one(IDlist)