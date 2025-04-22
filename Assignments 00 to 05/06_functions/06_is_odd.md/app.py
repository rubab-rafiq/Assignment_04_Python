# 06_is_odd.md
def odd_even():
    num1 = int(input("Enter number for Start: "))
    num2 = int(input("Enter number to End: "))

    for i in range(num1, num2 + 1):  # To include num2, use num2 + 1
        if i % 2 == 0:
            print(f"Even {i}", end=" ")
        else:
            print(f"Odd {i}", end=" ")

def main():
    odd_even()  # Calling the odd_even function to execute the logic

if __name__ == '__main__':
    main()  # Run the main function when the script is executed directly
