import random

def load_quotes(filename):
    quotes = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            quotes.append(line)
    return quotes

def random_quote(quotes):
    random_quote = random.choice(quotes)
    return random_quote

def print_quote(quote):
    print(quote)

def view_quotes(quotes):
    for quote in quotes:
        print_quote(quote)

main.py

from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Exit")

def main():
    while True:
        quotes = load_quotes("quotes.txt")
        menu()

        choice = input("Choose your an action (1-3): ")

        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2":
            view_quotes(quotes)
        elif choice == "3":
            print("Good bye...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
