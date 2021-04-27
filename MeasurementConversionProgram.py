import measurements


def display_menu():
    print("MENU")
    print("1. Inches to Centimeters")
    print("2. Centimeters to inches")
    print("3. Feet to Yards")
    print("4. Yards to Feet")
    print()


def convert_temp():
    option = int(input("Enter a menu option "))
    if option == 1:
        inches = float(input("Enter measurement in inches "))
        centimeters = measurements.to_centimeters(inches)
        centimeters = round(centimeters, 2)
        print(f"Measurement in inches {inches} converted to {centimeters} centimeters")
    elif option == 2:
        centimeters = float(input("Enter measurement in centimeters "))
        inches = measurements.to_inches(centimeters)
        inches = round(inches, 2)
        print(f"Measurement in centimeters {centimeters} converted to {inches} inches")
    elif option == 3:
        feet = float(input("Enter amount of feet "))
        yards = measurements.to_yards(feet)
        yards = round(yards, 2)
        print(f"Measurement in feet {feet} converted to {yards} yards")
    elif option == 4:
        yards = float(input("Enter amount of yards "))
        feet = measurements.to_feet(yards)
        feet = round(feet, 2)
        print(f"Measurement in yards {yards} converted to {feet} feet")
    else:
        print("Tou must enter a valid menu number")


def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another measurement? (y|n) ")
        print()
    print("Goodbye!")


if __name__ == "__main__":
    main()
