import random


def ask_question() -> bool:
    """Generate and ask one addition question. Return True if correct."""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = input(f"What is {a} + {b}? ")

    try:
        return int(answer) == a + b
    except ValueError:
        return False


def main() -> None:
    print("Welcome to the Math Game!")
    total_questions = 5
    points = 0

    for i in range(1, total_questions + 1):
        print(f"\nQuestion {i} of {total_questions}")
        if ask_question():
            points += 1
            print("Correct! +1 point")
        else:
            print("Incorrect.")

    print(f"\nGame over! You scored {points} point(s) out of {total_questions}.")


if __name__ == "__main__":
    main()
