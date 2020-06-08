class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.cash = 550
        self.state = "select"

    def __str__(self):
        return f"""
The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.cash} of money"""

    def display_action(self):
        print("Write action (buy, fill, take, remaining, exit):")

    def choose_action(self, action):
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 -cappuccino, back - to main menu:")
            self.state = "buy"
        elif action == "fill":
            print("")
            self.display_fill_message("water", "ml")
            self.state = "fill_water"
        elif action == "take":
            print("\nI gave you ${}".format(self.cash))
            self.cash = 0
            self.state = "select"
            self.handle()
        elif action == "remaining":
            print(self)
            self.state = "select"
            self.handle()

    def choose_coffee(self, type_of_coffee):
        self.state = "select"
        if type_of_coffee == "1":
            self.make_coffee(water=250, beans=16, cost=4)
        elif type_of_coffee == "2":
            self.make_coffee(water=350, milk=75, beans=20, cost=7)
        elif type_of_coffee == "3":
            self.make_coffee(water=200, milk=100, beans=12, cost=6)

        self.handle()

    def use_supplies(self, r_water, r_milk, r_beans, r_cups=1):
        if self.water < r_water:
            return "water"
        elif self.milk < r_milk:
            return "milk"
        elif self.beans < r_beans:
            return "beans"
        elif self.cups < r_cups:
            return "cups"
        else:
            self.water -= r_water
            self.milk -= r_milk
            self.beans -= r_beans
            self.cups -= r_cups
        return None

    def make_coffee(self, water=0, milk=0, beans=0, cost=0):
        missed_resource = self.use_supplies(water, milk, beans)
        if missed_resource is None:
            self.cash += cost
            print("I have enough resources, making you a coffee!")
        else:
            print(f"Sorry, not enough {missed_resource}!")

    def display_fill_message(self, resource, measure):
        print(f"Write how many {measure} of {resource} do you want to add:")

    def fill_water(self, n_water):
        self.water += int(n_water)
        self.display_fill_message("milk", "ml")
        self.state = "fill_milk"

    def fill_milk(self, n_milk):
        self.milk += int(n_milk)
        self.display_fill_message("coffee beans", "grams")
        self.state = "fill_beans"

    def fill_beans(self, n_beans):
        self.beans += int(n_beans)
        self.display_fill_message("coffee", "disposable cups")
        self.state = "fill_cups"

    def fill_cups(self, n_cups):
        self.cups += int(n_cups)
        self.state = "select"
        self.handle()

    def handle(self, data=None):
        if self.state == "action":
            self.choose_action(data)
        elif self.state == "buy":
            self.choose_coffee(data)
        elif self.state == "fill_water":
            self.fill_water(data)
        elif self.state == "fill_milk":
            self.fill_milk(data)
        elif self.state == "fill_beans":
            self.fill_beans(data)
        elif self.state == "fill_cups":
            self.fill_cups(data)
        else:
            self.display_action()
            self.state = "action"


coffee_machine = CoffeeMachine()
user_input = ""

while user_input != "exit":
    coffee_machine.handle(user_input)
    user_input = input()
