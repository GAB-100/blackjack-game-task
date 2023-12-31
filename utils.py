import os


class Utils:
    # Reformatted terminal clearing
    @staticmethod
    def terminal_clear():
        os.system("clear")

    # Function to print the cards
    @staticmethod
    def print_cards(cards, hidden):
        s = ""
        for card in cards:
            s = s + "\t ________________"
        if hidden:
            s += "\t ________________"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            if card.value == '10':
                s = s + "\t|  {}            |".format(card.value)
            else:
                s = s + "\t|  {}             |".format(card.value)
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|      * *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|    *     *     |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|   *       *    |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|   *       *    |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|       {}        |".format(card.suit)
        if hidden:
            s += "\t|          *     |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|         *      |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|        *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|                |"
        if hidden:
            s += "\t|                |"
        print(s)

        s = ""
        for card in cards:
            if card.value == '10':
                s = s + "\t|            {}  |".format(card.value)
            else:
                s = s + "\t|            {}   |".format(card.value)
        if hidden:
            s += "\t|        *       |"
        print(s)

        s = ""
        for card in cards:
            s = s + "\t|________________|"
        if hidden:
            s += "\t|________________|"
        print(s)

        print()
