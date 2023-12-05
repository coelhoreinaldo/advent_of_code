array = []


def find_numbers_in_word(word: str) -> tuple[str, str]:
    first_number = ""
    last_number = ""
    for letter in word:
        if not first_number and letter.isdigit():
            first_number = letter
        elif letter.isdigit():
            last_number = letter
    return first_number, last_number


def calculate_result(first_number: str, last_number: str) -> int:
    result = first_number + last_number if last_number else first_number + first_number
    return int(result)


def main():
    array: [int] = []
    with open("input.txt", "r") as file:
        for word in file:
            first_number, last_number = find_numbers_in_word(word)
            result = calculate_result(first_number, last_number)
            array.append(result)

    total_sum = sum(array)
    print(total_sum)


with open("input.txt", "r") as file:
    for word in file:
        first_number = ""
        last_number = ""
        for letter in word:
            if not first_number and letter.isdigit():
                first_number = letter
            elif letter.isdigit():
                last_number = letter
        result = first_number + last_number
        if last_number == "":
            result = first_number + first_number
        array.append(int(result))

if __name__ == "__main__":
    main()
