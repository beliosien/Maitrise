from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, n_legs: int) -> None:
        self.name = name
        self.n_legs = n_legs

    @abstractmethod
    def run(self) -> None:
        pass


class Dog(Animal):

    def __init__(self, name: str, n_legs: int) -> None:
        super().__init__(name, n_legs)

    def run(self) -> None:
        print("Woof Woof !")


d = Dog("dingo", 4)
d.run()
