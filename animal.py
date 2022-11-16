from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, n_legs: int) -> None:
        self.name = name
        self.n_legs = n_legs


    @abstractmethod
    def run(self) ->None:
        pass
