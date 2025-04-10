import random

class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        damage = self.attack_power + random.randint(-5, 5)  # случайный урон в пределах ±5 от базовой силы атаки
        other.health -= damage
        print(f"{self.name} атаковал {other.name} и нанес {damage} урона.")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name="Игрок", computer_name="Компьютер"):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        round_number = 1
        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_number}")
            if round_number % 2 == 1:  # нечетный раунд - ход игрока
                self.player.attack(self.computer)
            else:  # четный раунд - ход компьютера
                self.computer.attack(self.player)
            print(f"У {self.player.name} осталось {self.player.health} здоровья.")
            print(f"У {self.computer.name} осталось {self.computer.health} здоровья.")
            round_number += 1

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")


if __name__ == "__main__":
    game = Game()
    game.start()