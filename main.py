import random
#
def shuffle(word):
    temp = list(word) # list function used to create a list object (a collection that is ordered and changeable)
    random.shuffle(temp)
    return ''.join(temp)

def random1():
    upper_case1 = chr(random.randint(65, 90))  # generates randon upper case letter based on ASCII code
    upper_case2 = chr(random.randint(65, 90))  # generates randon upper case letter based on ASCII code

    lower_case1 = chr(random.randint(97, 122))  # generates randon lower case letter based on ASCII code
    lower_case2 = chr(random.randint(97, 122))  # generates randon lower case letter based on ASCII code

    number1 = chr(random.randint(48, 57))  # generates randon number based on ASCII code
    number2 = chr(random.randint(48, 57))  # generates randon number based on ASCII code

    xter1 = chr(random.randint(33, 47))  # generates randon character based on ASCII code
    xter2 = chr(random.randint(33, 47))  # generates randon character based on ASCII code

    password = upper_case1 + upper_case2 + lower_case1 + lower_case2 + number1 + number2 + xter1 + xter2
    password = shuffle(password)

    print(password)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    random1()
