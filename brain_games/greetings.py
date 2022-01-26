import prompt


def greetings(greeting):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print("Hello, {0}!".format(name))
    print(greeting)
    return name
