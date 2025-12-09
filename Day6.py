file = open("./Day6input")
input = file.read().split("\n")

def part_one(homework):
    answers = clear_empty_elements(homework[0].split(" "))
    answers = [int(number) for number in answers]

    operations = clear_empty_elements(homework[-1].split(" "))


    for problem in homework[1:-1]:
        clean_problem = clear_empty_elements(problem.split(' '))
        for i in range(len(clean_problem)):
            
            if operations[i] == '*':
                answers[i] *= int(clean_problem[i])
            elif operations[i] == '+':
                answers[i] += int(clean_problem[i])

    total = 0
    for answer in answers:
        total += answer

    return total

def part_two(homework):
    answers = []

    operations = homework[-1].split(" ")

    column_widths = get_index_length(operations)

    operations = clear_empty_elements(homework[-1].split(" "))

    translated_numbers = clean_array(homework[0].split(" "), column_widths)

    for problem in homework[1:-1]:
        cleaned = clean_array(problem.split(" "), column_widths)

        for i, row in enumerate(cleaned):
            for j, elem in enumerate(row):
                translated_numbers[i][j] += elem

    for i, group in enumerate(translated_numbers):
        curr_opertaion = operations[i]
        answers.append(0)
        if curr_opertaion == '*':
            answers[i] += 1
        for elem in group:
            if curr_opertaion == '*':
                answers[i] *= int(elem)
            elif curr_opertaion == '+':
                answers[i] += int(elem)

    total = 0

    for answer in answers:
        total += answer

    return total





def get_index_length(operations):
    lengths = []

    count = 1

    for elem in operations[1:]:
        if elem == '+' or elem == '*':
            lengths.append(count)
            count = 1
        else:
            count += 1

    lengths.append(count)

    return lengths

    

def clean_array(array, elem_widths):
    cleaned_array = []
    new_elem = []
    index = 0
    for elem in (array):

        if len(elem) > 1:
            new_elem += list(elem)
        else:
            new_elem.append(str(elem))

        if len(new_elem) == elem_widths[index]:
            cleaned_array.append(new_elem)
            new_elem = []
            index += 1
            continue

    return cleaned_array





def clear_empty_elements(array):
    new_array = []
    for elem in array:
        if elem != '':
            new_array.append(elem)

    return new_array



print(part_two(input))
