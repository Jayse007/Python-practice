def sequence_detector(sample):
    longest = 0
    for number in sample:
        if number-1 not in sample:
            length = 1
            while (number + length) in sample:
                length += 1
            longest = max(length, longest)
    print(longest)

numbers_test = [1, 4, 2, 3, 6, 7,8, 9, 10]

sequence_detector(numbers_test)            
