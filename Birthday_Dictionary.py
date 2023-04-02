#Birthday dictionary of famous people


def birthdays():
    """Print famous people's birthdays"""
    birthdays = {"Albert Einstein": "14/3/1879",
                 "Ada Lovelace": "10/12/1815",
                 "Benjamin Franklin": "1/17/1706"}
    print("Welcome to the birthday dictionary. We know the birthday's of:\n"
          "Albert Einstein\n"
          "Ada Lovelace\n"
          "Benjamin Franklin\n"
          "")
    x = input("Who's birthday do you want to look up? ")
    if x == "Albert Einstein":
        print("Albert Einstein's birthday is ", birthdays[x])
    elif x == "Ada Lovelace":
        print("Ada Lovelace's birthday is ", birthdays[x])
    elif x == "Benjamin Franklin":
        print("Benjamin Franklin's birthday is ", birthdays[x])

if __name__ == '__main__':
    birthdays()


