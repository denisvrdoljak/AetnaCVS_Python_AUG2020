# empty .py file

def count_letters_numbers4(input_string):
    """input: input_string: any string of letters or numbers
    output: string containing the counts of the numbers and letters in input_string"""

    letters = 0
    digits = 0
    valid_letters = list('abcdefghijklmnopqrstuvwxyz')
    valid_digits = list('0123456789')


    try:
        for letter in input_string.lower():
            if letter in valid_letters:
                letters += 1
            elif letter in valid_digits:
                digits += 1
        return_string = f'Letters: {letters}\n Digits: {digits}'
    except:
        return_string = "error, bad input (from try/except block)"

    return return_string


def count_letters_numbers(input_string):
    """input: input_string: any string of letters or numbers
    output: string containing the counts of the numbers and letters in input_string"""


    letters = 0
    digits = 0
    valid_letters = list('abcdefghijklmnopqrstuvwxyz')
    valid_digits = list('0123456789')


    for letter in input_string.lower():
        if letter in valid_letters:
            letters += 1
        elif letter in valid_digits:
            digits += 1
    return f'Letters: {letters}\n Digits: {digits}'


