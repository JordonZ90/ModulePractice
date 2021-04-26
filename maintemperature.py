from temperature import to_celsius, to_fahrenheit


def main():
    for temp in range(0, 212, 40):
        print(f"{temp}, Fahrenheit = {round(to_celsius(temp))} Celsius")

    for temp in range(0, 100, 20):
        print(f"{temp}, Celsius = {round(to_fahrenheit(temp))} Fahrenheit")


if __name__ == "__main__":
    main()
