"""
I am too tired to give any comment to explain my code ;)
This is the version 2. Features as below:
1.Added more user interact words to improve the experience of playing the game.
2.Added error prompt in came user input letters except "f,g,c,m,q"
3.Typographic alignment in output (i.e.the show_location function)
"""
#30.10.2024 ZHANG YAN CHENG
import pyfiglet
import time

class Item:
    def __init__(self, name, location='near'):
        self.name = name
        self.location = location

    def move(self):
        self.location = 'far' if self.location == 'near' else 'near'

class RiverCrossingGame:
    def __init__(self):
        self.fox = Item('fox')
        self.goose = Item('goose')
        self.corn = Item('corn')
        self.boat = Item('boat')
        self.state = 'ongoing'

    def print_goal(self):
        print(pyfiglet.figlet_format("Welcome."))
        time.sleep(1.5)
        print("You must bring the fox, the goose, and the corn across the river.")
        time.sleep(0.5)
        print('Press "f" for the movement of fox, "g" for goose, "c" for corn, "m" for only man on the boat ')
        time.sleep(0.5)

    def near_shore(self):
        print("Fox" if self.fox.location == 'near' else "   ",
              "Goose" if self.goose.location == 'near' else "     ",
              "Corn" if self.corn.location == 'near' else "    ", sep="      ")
    def far_shore(self):
        print("Fox" if self.fox.location == 'far' else "   ",
              "Goose" if self.goose.location == 'far' else "     ",
              "Corn" if self.corn.location == 'far' else "    ", sep="      ")

    def show_locations(self):
        if self.boat.location == 'near':
            self.far_shore()
            print("--------------------------")
            print("")
            print("         Boat             ")
            print("--------------------------")
            self.near_shore()

        if self.boat.location == 'far':
            self.far_shore()
            print("--------------------------")
            print("         Boat             ")
            print("")
            print("--------------------------")
            self.near_shore()

    def move_item(self, item_name):
        item = getattr(self, item_name)
        if item.location == self.boat.location:
            item.move()
            self.boat.move()
        else:
            print("The item is not on the same shore as the boat.")

    def check_game_status(self):
        print("")
        if self.fox.location == self.goose.location and self.boat.location != self.fox.location:
            print("You have failed. The fox has eaten the goose.")
            self.state = 'failed'
        elif self.goose.location == self.corn.location and self.boat.location != self.goose.location:
            print("You have failed. The goose has eaten the corn.")
            self.state = 'failed'
        elif self.fox.location == 'far' and self.goose.location == 'far' and self.corn.location == 'far':
            print("Congratulations! You have brought all the items across the river.")
            self.state = 'succeeded'

    def run(self):
        self.print_goal()
        self.show_locations()

        while self.state == 'ongoing':
            print("")
            command = input("You are now at the {} shore, what do you want to take (f, g, c, m, q)? ".format(self.boat.location))
            if command not in ['f', 'g', 'c', 'm', 'q']:
                print("You have entered an invalid command.")
                print("If you want to quit, pleas press q")
                continue

            if command == 'f':
                self.move_item("fox")

            if command == 'g':
                self.move_item("goose")

            if command == 'c':
                self.move_item("corn")

            if command == 'm':
                self.boat.move()

            if command == 'q':
                break

            self.show_locations()
            self.check_game_status()

if __name__ == "__main__":
    game = RiverCrossingGame()
    game.run()
