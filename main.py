from fizzbuzz import fizzbuzz

def main():
    print ("Fizz Buzz Application")
    try:
        number = int(input("Enter a number: "))
        result = fizzbuzz(number)
        print(result)

    except ValueError:
        print ("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()