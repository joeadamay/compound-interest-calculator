# Display output and attempt to get a floating-point value from the user
def get_value(output):
    while True:
        try:
            user_input = float(input(output))
            return user_input
        except:
            print("Please enter a number.")


# Compute the sum x^i for all whole numbers i <= n
def power_series(x, n):
    total = 1.0
    last = 1.0

    for i in range(1, n + 1):
        last *= x
        total += last

    return total


if __name__ == "__main__":
    principle = get_value("Principle: ")
    rate = get_value("Rate: ")
    payments = get_value("Payments: ")
    n = get_value("Number of Cycles: ")

    # Adjust inputs
    payments = -payments
    rate *= 100.0 # Change to percent
    n = int(n)

    balance = principle * (1.0 + rate) ** n + \
        rate * payments * power_series(1.0 + rate, n - 1)

    print(f"Balance: {balance}")


