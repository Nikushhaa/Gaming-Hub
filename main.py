# main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")
        # main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")
        # main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")
        # main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")
        # main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")
        # main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")
        # main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")
        # main.py

import random
import time


# ----------------------------
# Utility functions
# ----------------------------

def greet_user(name):
    print(f"Hello, {name}!")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def random_number():
    return random.randint(1, 100)


def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Done!")


# ----------------------------
# Class examples
# ----------------------------

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def add_score(self, value):
        self.score += value

    def show(self):
        print(self.name, self.score)


class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        for p in self.players:
            p.show()


# ----------------------------
# More functions
# ----------------------------

def square(x):
    return x * x


def cube(x):
    return x * x * x


def is_even(x):
    return x % 2 == 0


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a)
        a, b = b, a + b


def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total


# ----------------------------
# Random loops
# ----------------------------

for i in range(10):
    print("Loop A:", i)

for i in range(5):
    print("Loop B:", i * 2)

for i in range(3):
    print("Loop C:", i ** 2)


# ----------------------------
# Dummy calculations
# ----------------------------

x = 10
y = 20
z = x + y
print("Sum:", z)

a = 5
b = 3
print("Multiply:", a * b)

print("Random:", random_number())


# ----------------------------
# More filler logic
# ----------------------------

def fake_process():
    for i in range(15):
        print("Processing step", i)
        time.sleep(0.01)


def simulate_game():
    p1 = Player("Alice", 10)
    p2 = Player("Bob", 20)

    game = Game()
    game.add_player(p1)
    game.add_player(p2)

    p1.add_score(5)
    p2.add_score(10)

    game.show_players()


# ----------------------------
# Extra random functions
# ----------------------------

def loop_print():
    for i in range(20):
        print("Number:", i)


def math_operations():
    for i in range(10):
        print(square(i), cube(i))


def random_math():
    for i in range(10):
        print(i, random_number())


def repeat_text():
    for i in range(10):
        print("Hello world", i)


def nested_loops():
    for i in range(5):
        for j in range(5):
            print(i, j)


# ----------------------------
# Main execution
# ----------------------------

if __name__ == "__main__":
    greet_user("Nick")

    countdown(5)

    simulate_game()

    loop_print()

    math_operations()

    random_math()

    repeat_text()

    nested_loops()

    fake_process()

    print("Program finished")


# ----------------------------
# Extra filler section (to reach 200+ lines)
# ----------------------------

def filler_1():
    print("filler 1")

def filler_2():
    print("filler 2")

def filler_3():
    print("filler 3")

def filler_4():
    print("filler 4")

def filler_5():
    print("filler 5")

def filler_6():
    print("filler 6")

def filler_7():
    print("filler 7")

def filler_8():
    print("filler 8")

def filler_9():
    print("filler 9")

def filler_10():
    print("filler 10")


for i in range(20):
    print("Final loop", i)

print("End of file")
import random
import time
import json
from dataclasses import dataclass


# ----------------------------
# Logger
# ----------------------------

class Logger:
    def log(self, msg):
        print(f"[LOG] {msg}")


logger = Logger()


# ----------------------------
# Entity System
# ----------------------------

class Entity:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, dmg):
        self.hp -= dmg
        logger.log(f"{self.name} took {dmg} damage (HP={self.hp})")


class Player(Entity):
    def __init__(self, name):
        super().__init__(name, 100, 10)
        self.inventory = []
        self.level = 1
        self.xp = 0

    def gain_xp(self, amount):
        self.xp += amount
        logger.log(f"{self.name} gained {amount} XP")
        if self.xp >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.power += 2
        self.hp += 10
        logger.log(f"{self.name} leveled up to {self.level}")


class Enemy(Entity):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)


# ----------------------------
# Combat System
# ----------------------------

class CombatSystem:
    def fight(self, player, enemy):
        logger.log(f"Fight started: {player.name} vs {enemy.name}")

        while player.is_alive() and enemy.is_alive():
            enemy.take_damage(player.power)

            if enemy.is_alive():
                player.take_damage(enemy.power)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Player won!")
            player.gain_xp(50)
        else:
            logger.log("Player lost!")


# ----------------------------
# Inventory System
# ----------------------------

class Inventory:
    def add_item(self, player, item):
        player.inventory.append(item)
        logger.log(f"Added {item} to inventory")

    def show(self, player):
        logger.log(f"Inventory: {player.inventory}")


# ----------------------------
# World Events
# ----------------------------

class WorldEvent:
    def trigger(self, player):
        events = [
            "found treasure",
            "met enemy",
            "found healing potion",
            "nothing happened"
        ]

        event = random.choice(events)
        logger.log(f"Event: {event}")

        if event == "found treasure":
            player.gain_xp(20)
        elif event == "found healing potion":
            player.hp += 10
            logger.log("Healed +10 HP")


# ----------------------------
# Game Engine
# ----------------------------

class GameEngine:
    def __init__(self):
        self.player = Player("Hero")
        self.inventory = Inventory()
        self.combat = CombatSystem()
        self.world = WorldEvent()
        self.running = True

    def game_loop(self):
        tick = 0

        while self.running and tick < 50:
            logger.log(f"Tick {tick}")

            action = random.randint(1, 3)

            if action == 1:
                enemy = Enemy("Goblin", 30, 5)
                self.combat.fight(self.player, enemy)

            elif action == 2:
                self.world.trigger(self.player)

            elif action == 3:
                item = random.choice(["sword", "shield", "potion"])
                self.inventory.add_item(self.player, item)

            if not self.player.is_alive():
                self.running = False

            tick += 1
            time.sleep(0.05)

        logger.log("Game Over")


# ----------------------------
# Save System (fake)
# ----------------------------

class SaveSystem:
    def save(self, player):
        data = {
            "name": player.name,
            "hp": player.hp,
            "level": player.level,
            "xp": player.xp,
            "inventory": player.inventory
        }
        logger.log("Game saved (mock)")


# ----------------------------
# MAIN
# ----------------------------

if __name__ == "__main__":
    engine = GameEngine()
    engine.game_loop()
    # ----------------------------
# Skill System
# ----------------------------

class Skill:
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def use(self, user, target):
        logger.log(f"{user.name} uses {self.name}")
        target.take_damage(self.damage)


class SkillBook:
    def __init__(self):
        self.skills = [
            Skill("Slash", 15, 0),
            Skill("Fireball", 25, 10),
            Skill("Ice Spike", 20, 5)
        ]

    def random_skill(self):
        return random.choice(self.skills)


# ----------------------------
# Boss System
# ----------------------------

class Boss(Enemy):
    def __init__(self, name):
        super().__init__(name, 150, 15)
        self.phase = 1

    def update_phase(self):
        if self.hp < 100:
            self.phase = 2
        if self.hp < 50:
            self.phase = 3

        logger.log(f"{self.name} is now in phase {self.phase}")

    def attack(self, player):
        damage = self.power * self.phase
        player.take_damage(damage)


class BossFight:
    def fight(self, player, boss):
        logger.log("⚔ Boss fight started!")

        skills = SkillBook()

        while player.is_alive() and boss.is_alive():
            boss.update_phase()

            action = random.randint(1, 3)

            if action == 1:
                boss.take_damage(player.power)

            elif action == 2:
                skill = skills.random_skill()
                skill.use(player, boss)

            elif action == 3:
                boss.attack(player)

            time.sleep(0.1)

        if player.is_alive():
            logger.log("Boss defeated!")
            player.gain_xp(100)
        else:
            logger.log("Boss won...")


# ----------------------------
# Crafting System
# ----------------------------

class CraftingSystem:
    def craft(self, player):
        if len(player.inventory) >= 2:
            item1 = player.inventory.pop()
            item2 = player.inventory.pop()

            new_item = item1 + "-" + item2
            player.inventory.append(new_item)

            logger.log(f"Crafted {new_item}")
        else:
            logger.log("Not enough items to craft")


# ----------------------------
# Extended Game Engine Hook
# ----------------------------

class ExtendedEngine(GameEngine):
    def __init__(self):
        super().__init__()
        self.boss_system = BossFight()
        self.crafting = CraftingSystem()

    def extra_actions(self):
        action = random.randint(1, 3)

        if action == 1:
            boss = Boss("Dark Lord")
            self.boss_system.fight(self.player, boss)

        elif action == 2:
            self.crafting.craft(self.player)

        elif action == 3:
            self.inventory.add_item(self.player, "rare_gem")

    def game_loop(self):
        tick = 0

        while self.running and tick < 80:
            logger.log(f"Extended Tick {tick}")

            choice = random.randint(1, 4)

            if choice == 1:
                enemy = Enemy("Skeleton", 40, 7)
                self.combat.fight(self.player, enemy)

            elif choice == 2:
                self.world.trigger(self.player)

            elif choice == 3:
                self.extra_actions()

            elif choice == 4:
                self.inventory.add_item(self.player, "gold_coin")

            tick += 1
            time.sleep(0.05)

        logger.log("Extended Game Over")