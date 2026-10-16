import random

rooms = {
    "A": input("Is room A Dirty or Clean? ").capitalize(),
    "B": input("Is room B Dirty or Clean? ").capitalize(),
    "C": input("Is room C Dirty or Clean? ").capitalize()
}

class Agent:
    def __init__(self):
        self.location = "A"

    def display(self):
        print("[A-" + ("Agent" if self.location == "A" else rooms["A"]) + "]", end=" ")
        print("[B-" + ("Agent" if self.location == "B" else rooms["B"]) + "]", end=" ")
        print("[C-" + ("Agent" if self.location == "C" else rooms["C"]) + "]")

    def act(self):
        if rooms[self.location] == "Dirty":
            rooms[self.location] = "Clean"
            print("Room", self.location, "has been cleaned.")
        else:
            if self.location == "A":
                self.location = random.choice(["B", "C"])
            elif self.location == "B":
                self.location = random.choice(["A", "C"])
            else:
                self.location = random.choice(["A", "B"])

            print("Moving to room", self.location)

agent = Agent()

steps = int(input("\nHow many steps should the agent run? "))

for step in range(1, steps + 1):
    print("\nStep " + str(step) + ":")
    agent.display()
    agent.act()
    agent.display()