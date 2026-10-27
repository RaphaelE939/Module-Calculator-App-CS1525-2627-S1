def get_user_number()-> float:
    """
    :return: player_response is returned as number,
             and goes back to main.py to be added, subtracted, multiplied, or divided
    """
    while True:
        player_response1 = input("Pick a number:")
        try:
            number = float(player_response1)
            return number
        except ValueError:
            print("Try again")



def get_operation()->str:
    """
    :return: The picked option goes back to main.py to be applied as an operation to number_1 and number_2
    """

    while True:
        player_response2 = input("Which operation would you like to use: + - * /?").strip()
        if player_response2 == "+":
            return "+"
        elif player_response2 == "-":
            return "-"
        elif player_response2 == "*":
            return "*"
        elif player_response2 == "/":
            return "/"
        else:
            print("Invalid input, try again!")