file = open("./Day3input")
banks = file.read()

def part_one(banks):
    split_banks = banks.split("\n")
    
    total = 0
    for bank in split_banks:
        bank_length = len(bank)

        max_digit, index = find_biggest_digit(bank)

        print(max_digit)

        if index >= bank_length - 1:
            second_digit, second_index = find_biggest_digit(bank[:index])
            total += int(str(second_digit)+str(max_digit))
        else:
            second_digit, second_index = find_biggest_digit(bank[index+1:])
            total += int(str(max_digit)+str(second_digit))
    
    print(total)

def part_two(banks):
    split_banks = banks.split("\n")
    total = 0
    for bank in split_banks:
        bank_length = len(bank)
        curr_bank = bank
        amount_to_choose = 12

        result = ""
        while (bank_length > amount_to_choose and amount_to_choose > 0):
            amount_to_choose -= 1
            bankHigh = curr_bank[:-(amount_to_choose)]
            bankLow = curr_bank[-(amount_to_choose):]

            first_digit, first_index = find_biggest_digit(bankHigh)
            if first_digit == 0:
                first_digit, first_index = find_biggest_digit(bankLow)
                curr_bank = ""


            result += str(first_digit)
            
            curr_bank = curr_bank[first_index+1:]
            bank_length = len(curr_bank)

        result += curr_bank
        result = result[:12]
        
        total += int(result)
        

    print(total)


    


def find_biggest_digit(numbers):
    biggest = 0,0
    for i, number in enumerate(str(numbers)):
        digit = int(number)

        if digit > biggest[0]:
            biggest = digit,i

    return biggest

# max_digit, index = biggest

part_two(banks)

#part_one(banks)