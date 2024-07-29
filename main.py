class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


## don't touch above this line


class Archer(Human):
    def __init__(self, name, health, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows
        self.__health = health

    def get_num_arrows(self):
        return self.__num_arrows
    
    def get_name(self):
        return super().get_name()
    
    def get_health(self):
        return self.__health

    def shoot(self, target):
        if self.__num_arrows > 0:
            self.__num_arrows -= 1
            target.take_damage(10)
        else:
            raise Exception("not enough arrows")
    
    def take_damage(self, damage):
        self.__health -= damage



class Crossbowman(Archer):
    def __init__(self, name, num_arrows):
        super().__init__(name, num_arrows)

    def triple_shot(self, target):
        if self.get_num_arrows() >= 3:
            self.use_arrows(3)
            return f"{target.get_name()} was shot by 3 crossbow bolts"
        else:
            raise Exception("not enough arrows")

class Wizard(Human):
    def __init__(self, name, health, mana):
        super().__init__(name)
        self.__health = health
        self.__mana = mana
    
    def get_name(self):
        return super().get_name()
    
    def get_health(self):
        return self.__health

    def get_mana(self):
        return self.__mana
    
    def take_damage(self, damage):
        self.__health -= damage

    def cast(self, target):
        if self.get_mana() >= 25:
            target.take_damage(25)
            self.__mana -= 25
        else:
            raise Exception("not enough mana")
