class Player:
    @staticmethod
    def init_players():
        player_1_name = ""
        player_2_name = ""
        while player_1_name.strip() == "":
            player_1_name = input("Player 1 Name: ")
        while player_2_name.strip() == "":
            player_2_name = input("Player 2 Name: ")
        player_1_marker = player_1_name[0].upper()
        player_2_marker = player_2_name[0].upper()
        while player_1_marker == player_2_marker or not player_1_marker.isalpha() or not player_2_marker.isalpha():
            print("\nBoth players' names begin with the same letter.")
            player_1_marker = input("\nWhich letter will be the marker for {}? ".format(player_1_name))
            player_2_marker = input("\nWhich letter will be the marker for {}? ".format(player_2_name))
        return Player(player_1_name, player_1_marker), Player(player_2_name, player_2_marker)

    def __init__(self, name, marker):
        self.name = name.capitalize()
        self.marker = marker
