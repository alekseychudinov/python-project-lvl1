import prompt


def greetings(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    if game == "calc":
        print("What is the result of the expression?")
    elif game == "even":
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif game == "gcd":
        print("Find the greatest common divisor of given numbers.")
    elif game == "prime":
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
    elif game == "progression":
        print("What number is missing in the progression?")
    return name
