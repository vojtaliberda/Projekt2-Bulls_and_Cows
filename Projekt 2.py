"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Vojtěch Liberda
email: vojtech.liberda@gmail.com
discord: vojtaliberda#0829
"""

import random

print("Hi there!")
oddelovac = "-" * 50
print(oddelovac)
print("I've generated a random 4 digit number for you. \nLet's play a bulls and cows game.")
print(oddelovac)

def generate_unique_number():
    while True:
        number = random.sample(range(1, 10), 4)
        unique_number = int(''.join(map(str, number)))
        if unique_number not in generated_numbers:
            generated_numbers.add(unique_number)
            return unique_number

generated_numbers = set()
unique_number = str(generate_unique_number())

def main():
    unique_number
    guesses = []

    while True:
        input_uz = input("Enter a number: ")
        
        guesses.append(input_uz)

        if not input_uz.isnumeric():
            print("Not a number, terminating the program...")
            quit()
        if len(input_uz) != 4:
            print ("Number is too short or long, terminating the program...")
            quit()
        def opakovana_cisla(number):
            digit_str = str(number)
            return len(set(digit_str)) < len(digit_str)
        if opakovana_cisla(input_uz) == True:
            print("You repeated numbers. Terminating the program...")
            quit()
        def zacina_nulou(input_uz):
            cislo = str(input_uz)
            return cislo[0] == "0"
        if zacina_nulou(input_uz) == True:
            print("First number cannot be zero, terminating the program...")
            quit()

        def get_feedback(secret, input_uz):
            bulls = 0
            cows = 0

            for i in range(len(secret)):
                if secret[i] == input_uz[i]:
                    bulls += 1
                elif secret[i] in input_uz:
                    cows += 1

            return bulls, cows

        if input_uz == unique_number:
            print(oddelovac)
            print(f"Correct, you've guessed the right number: {guesses[-1]}.")
            print(oddelovac)
            if len(guesses) <= 3:
                print(f"You guessed the number in {len(guesses)} guesses. That's amazing !!! \nHere are your guesses: {guesses}")
            elif 3 < len(guesses) <= 6:
                print(f"You guessed the number in {len(guesses)} guesses. That's great! \nHere are your guesses: {guesses}")
            elif 6 < len(guesses) <= 9:
                print(f"You guessed the number in {len(guesses)} guesses. That's not bad :) \nHere are your guesses: {guesses}")
            elif 9 < len(guesses):
                print(f"You guessed the number in {len(guesses)} guesses. That's quite bad :( \nHere are your guesses: {guesses}")
            print(oddelovac)
            break
        else:
            print(oddelovac)
            bulls, cows = get_feedback(unique_number, input_uz)
            print(f">>>  {guesses[-1]}")
            print(f"Bulls: {bulls}, Cows: {cows}")
            print(oddelovac)

if __name__ == "__main__":
    main()