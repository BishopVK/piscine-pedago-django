def split_numbers():
    with open("../d01/ex01/numbers.txt", "r") as file:
        content = file.read()

    numbers = content.split(",")

    for number in numbers:
        print(number.strip())


if __name__ == "__main__":
    split_numbers()