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
        fahrenheit = int(input("Enter degrees in Fahrenheit "))
        celsius = temperature.to_celsius(fahrenheit)
        celsius = round(celsius, 2)
        print(f"Degrees Celsius {celsius}")
    elif option == 2:
        celsius = int(input("Enter degrees in Celsius "))
        fahrenheit = temperature.to_fahrenheit(celsius)
        fahrenheit = round(fahrenheit, 2)
        print(f"Degrees Fahrenheit {fahrenheit}")
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
