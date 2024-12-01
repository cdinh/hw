def main():
    while input('Do you want to enter a sequence of numbers? ').lower() == 'y':
        sequence = input('Enter a sequence of numbers: ')
        sum = 0
        for digit in sequence:
            sum += int(digit)
        print(f'The sum of all digits in your sequence is {sum}')

main()