class Ollie:

    like = [
        "pizza",
        "grapes",
        "cherries",
        "bagel"
    ]

    def eat(self, food):
        if food in self.like:
            return "yummy"
        else:
            return "hmmmmm"

class Dad:
    dislike = [
        "grapes"
    ]
    def eat(self, food):
        if food in self.dislike:
            return "hmmmm"
        else:
            return "yummmmmyyyyy"


ollie = Ollie()
dad = Dad()

foods = [
    "pizza",
    "grapes",
    "bagel",
    "cereal",
    "cherries"
]

for food in foods:
    print("Food: ", food)
    print("Ollie says: ", ollie.eat(food))
    print("Dad says", dad.eat(food))
    print("")