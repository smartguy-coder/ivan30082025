from study_functions.functions import get_greeting, multiply_and_power_numbers


def main():
    welcome_text = get_greeting()
    print(welcome_text)
    result = multiply_and_power_numbers(number1=2, number2=3, power=2)
    print(result)

    result1 = multiply_and_power_numbers(number1=32, number2=33, power=2)
    print(result1)


main()
