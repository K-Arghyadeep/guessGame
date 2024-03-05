import random
import shutil

terminal_width = shutil.get_terminal_size().columns


def padding(txt):
    padding_value = (terminal_width - len(txt)) // 2
    return padding_value


while True:
    lower_limit = None
    upper_limit = None
    range_flag = True
    message = None

    while range_flag:

        user_input = input("Enter the lower and upper limit of the range separated by a space ' '\t\t")

        try:
            lower_limit, upper_limit = user_input.split()

            lower_limit = eval(lower_limit)
            upper_limit = eval(upper_limit)

        except (ValueError, IndexError):
            message = "Enter STRICTLY 2 values."
            print("#" * terminal_width)
            print(" " * padding(message), message)
            print("#" * terminal_width)
            message = None

        except (TypeError, ValueError, NameError, SyntaxError):
            message = "Enter numbers ONLY."
            print("#" * terminal_width)
            print(" " * padding(message), message)
            print("#" * terminal_width)
            message = None

        else:
            if lower_limit < upper_limit:
                range_flag = False
            else:
                print(f"lower limit:{lower_limit} has to less than upper limit:{upper_limit}")

    num = random.randint(lower_limit, upper_limit+1)

    while True:
        user_guess = int(input(f"Enter your guessed number between {lower_limit} and {upper_limit}\t\t"))
        if num == user_guess:
            print(f"{user_guess} is the correct guess")
            break
        else:
            print(f"{user_guess} is the wrong guess")

    while True:
        continue_confirmation = input("Enter 'y' to play again\nEnter 'n' to exit.\t\t").lower()
        if continue_confirmation in ["y", "n"]:
            break

        message = "Enter only 'y' or 'n'."
        print("#" * terminal_width)
        print(" " * padding(message), message)
        print("#" * terminal_width)
        message = None
    
    if continue_confirmation == "n":
        break