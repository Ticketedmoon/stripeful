# Problem Statement
# Remove any '-' or ' '
# Add all digits in the odd places from right to left
# Double every second digit from right to left
#   If result is a two-digit number, add the two-digit number together to get single number.
# Sum the totals of step {2, 3}
# if sum % 10, then we are valid, otherwise not valid

class CreditCardValidator:

    def __init__(self):
        pass

    def is_valid_card_number(self, card_number):
        card_number = card_number.replace("-", "")
        card_number = card_number.replace(" ", "")

        sum_odd = 0
        for num in card_number[::-2]:
            sum_odd += int(num)
        
        sum_even = 0
        for num in card_number[len(card_number)-2::-2]:
            num = int(num) * 2
            if num >= 10:
                sum_even += (1 + (num % 10))
            else: 
                sum_even += num

        total = sum_odd + sum_even
        return total % 10 == 0


def main():

    valid_credit_card_numbers = [
        "378282246310005",
        "371449635398431",
        "378734493671000",
        "5610591081018250",
        "30569309025904",
        "38520000023237",
        "6011111111111117",
        "6011000990139424",
        "3530111333300000",
        "3566002020360505",
        "5555555555554444",
        "5105105105105100",
        "4111111111111111",
        "4012888888881881",
        "4222222222222",
        "76009244561",
        "5019717010103742",
        "6331101999990016"
    ]

    c = CreditCardValidator()

    # My own custom testing
    print("Custom Testing:")
    print(c.is_valid_card_number("1234-5678-9101-1121"))
    print(c.is_valid_card_number("1234-5678-9101-1131"))

    print("-----\nWeb Credit Card Number Validation:")
    # valid card numbers from web: https://www.paypalobjects.com/en_GB/vhelp/paypalmanager_help/credit_card_numbers.htm
    for card_number in valid_credit_card_numbers:
        print(card_number, c.is_valid_card_number(card_number))
        
if __name__ == "__main__":
    main()
