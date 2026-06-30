while True:
    print("\n================================")
    print("      UNIT CONVERTER TOOL")
    print("================================")

    print("\nChoose Conversion Type")
    print("1. Temperature")
    print("2. Length")
    print("3. Weight")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Temperature Converter
    if choice == "1":
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        temp = input("Choose (1-2): ")

        if temp == "1":
            c = float(input("Enter Celsius: "))
            f = (c * 9/5) + 32
            print("Fahrenheit =", f)

        elif temp == "2":
            f = float(input("Enter Fahrenheit: "))
            c = (f - 32) * 5/9
            print("Celsius =", c)

        else:
            print("Invalid Choice")

    # Length Converter
    elif choice == "2":
        print("\nLength Converter")
        print("1. Meter to Kilometer")
        print("2. Kilometer to Meter")

        length = input("Choose (1-2): ")

        if length == "1":
            meter = float(input("Enter Meters: "))
            print("Kilometers =", meter / 1000)

        elif length == "2":
            km = float(input("Enter Kilometers: "))
            print("Meters =", km * 1000)

        else:
            print("Invalid Choice")

    # Weight Converter
    elif choice == "3":
        print("\nWeight Converter")
        print("1. Kilogram to Gram")
        print("2. Gram to Kilogram")

        weight = input("Choose (1-2): ")

        if weight == "1":
            kg = float(input("Enter Kilograms: "))
            print("Grams =", kg * 1000)

        elif weight == "2":
            g = float(input("Enter Grams: "))
            print("Kilograms =", g / 1000)

        else:
            print("Invalid Choice")

    # Exit
    elif choice == "4":
        print("\nThank you for using the Unit Converter Tool!")
        break

    else:
        print("Invalid Main Menu Choice")

    input("\nPress Enter to continue...")