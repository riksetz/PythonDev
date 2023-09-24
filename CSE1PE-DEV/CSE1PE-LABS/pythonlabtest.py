def main():
    print("Welcome to the Name and Age program!")
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))

    if age < 0:
        print("Invalid age. Please enter a valid age.")
    elif age < 18:
        print(f"Hi {name}, you are a minor.")
    elif age < 65:
        print(f"Hi {name}, you are an adult.")
    else:
        print(f"Hi {name}, you are a senior citizen.")

if __name__ == "__main__":
    main()
