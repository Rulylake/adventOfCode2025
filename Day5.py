file = open("./Day5input")

data = file.read().split("\n\n")

ranges = data[0].split("\n")
ingredients = data[1].split("\n")

def part_one(ranges, ingredients):

    total = 0
    for ingredient in ingredients:
        int_ingredient = int(ingredient)
        for range in ranges:
            lower_bound, higher_bound = range.split("-")
            lower_bound, higher_bound = int(lower_bound), int(higher_bound)

            

            if int_ingredient >= lower_bound and int_ingredient <= higher_bound:
                total += 1
                break

    return total

def part_two(ranges):
    accounted_ranges = []
    total = 0
    for the_range in ranges:
        lower_bound, higher_bound = the_range.split("-")
        lower_bound, higher_bound = int(lower_bound), int(higher_bound)

        if lower_bound > higher_bound:
            continue

        new_ids = True

        for acc_range in accounted_ranges:
            acc_lower_bound, acc_higher_bound = acc_range

            # New range is inside acounted range
            if lower_bound >= acc_lower_bound and higher_bound <= acc_higher_bound: 
                new_ids = False
                break
            # acounted range is inside new range
            elif lower_bound <= acc_lower_bound and higher_bound >= acc_higher_bound: 
                if lower_bound != acc_lower_bound:
                    ranges.append(str(lower_bound) + '-' + str(acc_lower_bound-1))
                if higher_bound != acc_higher_bound:
                    ranges.append(str(acc_higher_bound+1) + '-' + str(higher_bound))
                new_ids = False
                break
            # acc to the left of range
            elif lower_bound <= acc_higher_bound and lower_bound > acc_lower_bound:
                lower_bound = acc_higher_bound + 1
            # acc to the right of range
            elif higher_bound >= acc_lower_bound and higher_bound < acc_higher_bound:
                higher_bound = acc_lower_bound - 1

        if new_ids:
            accounted_ranges.append((lower_bound, higher_bound))
            total += higher_bound - lower_bound + 1

    return total

    

        


#print(part_one(ranges, ingredients))

print(part_two(ranges))



