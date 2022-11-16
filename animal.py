class Animal:
    def __init__(self, name: str, n_legs: int) -> None:
        self.name = name
        self.n_legs = n_legs


class Dog(Animal):

    def __init__(self, name: str, n_legs: int) -> None:
        super().__init__(name, n_legs)

    def run(self):
        print("Woof Woof !")
