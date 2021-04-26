import temperature
from temperature import to_celsius, to_fahrenheit


def display_menu():
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print()


def convert_temp():
    option = int(input("Enter a menu option "))
    if option == 1:
        f = int(input("Enter degrees in Fahrenheit "))
        c = temperature.to_celsius(f)
        c = round(c, 2)
        print(f"Degrees Celsius {c}")
    elif option == 2:
        c = int(input("Enter degrees in Celsius "))
        f = temperature.to_fahrenheit(c)
        f = round(f, 2)
        print(f"Degrees Fahrenheit {f}")
    else:
        print("Tou must enter a valid menu number")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y|n) ")
        print()
    print("Goodbye!")


if __name__ == "__main__":
    main()
