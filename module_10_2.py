from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int, enemies=100):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = enemies
        self.days = 0

    def battle(self):
        while self.enemies > 0:
            sleep(1)
            self.enemies -= self.power
            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

    def run(self):
        print(f'{self.name}, на нас напали')
        self.battle()
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")
