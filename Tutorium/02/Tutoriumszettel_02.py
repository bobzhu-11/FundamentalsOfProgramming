class Game:
    def __init__(self):
        self.player_name = "Player"
        self.is_game_over = False
        self.current_room = "entrance"
        self.player_inventory = []
        self.player_health = 100

    def setup_game(self):
        print("========================================")
        print("Hello, welcome to the dark dungeon")
        print("========================================")

        name_input = input("What is your name, adventurer? > ")
        if name_input:
            self.player_name = name_input

        print(f"\nGood luck, {self.player_name}...")

    def game_loop(self):
        while not self.is_game_over:
            print("\n--------------------")
            command = input(f"[{self.current_room}] What do you do? > ")
            self.process_command(command.lower().strip())

        print(f"\n--- GAME OVER, {self.player_name} ---")

    def process_command(self, command):
        if command == "quit":
            print("You decide to leave the dungeon. Farewell.")
            self.is_game_over = True

        elif command == "help":
            print("Available commands:")
            print("- look: Look around the room")
            print("- go [direction]: Move (e.g., 'go north')")
            print("- quit: Exit the game")

        elif command == "look":
            if self.current_room == "entrance":
                print("You are at the dungeon entrance.")
                print("It's dark and smells of mildew.")
                print("A narrow path leads 'north'.")
            elif self.current_room == "hallway":
                print("You are in a long hallway.")
                print("The entrance is to the 'south'.")
                print("You see a heavy wooden 'door' to the north.")

        elif command == "go north":
            if self.current_room == "entrance":
                print("You walk north into a long hallway.")
                self.current_room = "hallway"
            elif self.current_room == "hallway":
                print("You push the heavy wooden door. It creeks open...")
                print("Congratulations! You found the exit!")
                self.is_game_over = True
            else:
                print("You can't go north from here.")

                print("you are get attacked, Hp-5")
                self.player_health -= 5

        elif command == "go south":
            if self.current_room == "hallway":
                print("You return to the dungeon entrance.")
                self.current_room = "entrance"
            else:
                print("You can't go south from here.")

        else:
            print("I don't understand that command. Type 'help' for options.")

if __name__ == "__main__":
    my_game = Game()
    my_game.setup_game()
    my_game.game_loop()