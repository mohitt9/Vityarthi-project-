import math


def get_angle():
    """Read an angle and convert it to radians when the user enters degrees."""
    while True:
        try:
            value = float(input("Enter the angle/value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        unit = input("Is the value in radians? (y/n): ").strip().lower()

        if unit == "y":
            return value
        if unit == "n":
            return math.radians(value)

        print("Please enter y for radians or n for degrees.")


def calculate(choice, angle):
    """Calculate the selected trigonometric function."""
    sin_value = math.sin(angle)
    cos_value = math.cos(angle)

    if choice in ("1", "sin"):
        return "sin", sin_value

    if choice in ("2", "cos"):
        return "cos", cos_value

    if choice in ("3", "tan"):
        if math.isclose(cos_value, 0.0, abs_tol=1e-12):
            return "tan", None
        return "tan", math.tan(angle)

    if choice in ("4", "cosec", "csc"):
        if math.isclose(sin_value, 0.0, abs_tol=1e-12):
            return "cosec", None
        return "cosec", 1 / sin_value

    if choice in ("5", "sec"):
        if math.isclose(cos_value, 0.0, abs_tol=1e-12):
            return "sec", None
        return "sec", 1 / cos_value

    if choice in ("6", "cot"):
        if math.isclose(sin_value, 0.0, abs_tol=1e-12):
            return "cot", None
        return "cot", cos_value / sin_value

    return None, None


def main():
    print("=" * 40)
    print("       TRIGONOMETRIC CALCULATOR")
    print("=" * 40)
    print("Calculate sin, cos, tan, cosec, sec and cot.")
    print()

    while True:
        angle = get_angle()

        print("\nChoose a function:")
        print("1 -> sin")
        print("2 -> cos")
        print("3 -> tan")
        print("4 -> cosec")
        print("5 -> sec")
        print("6 -> cot")
        print("7 -> Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice == "7" or choice == "exit":
            print("Thank you for using Trigonometric Calculator.")
            break

        name, result = calculate(choice, angle)

        if name is None:
            print("Invalid choice. Please select 1-7 or enter a valid function name.")
        elif result is None:
            print(f"{name} is undefined for this value.")
        else:
            # Avoid displaying -0.000000 for values that are effectively zero.
            if math.isclose(result, 0.0, abs_tol=1e-12):
                result = 0.0
            print(f"{name}({angle}) = {result:.10f}")

        print("\nReturning to the main menu...\n")


if __name__ == "__main__":
    main()
