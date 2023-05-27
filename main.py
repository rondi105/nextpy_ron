from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    greeting_card = GreetingCard()
    greeting_card.greeting_msg()

    birthday_card = BirthdayCard(sender_age=25)
    birthday_card.greeting_msg()


if __name__ == '__main__':
    main()
