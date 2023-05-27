
class Whale:
    def __init__(self,age,name="dik"):
        Whale.count+=1
        self._name=name
        self._age=age
    def birthday(self):
        self._age+=1
    def get_age(self):
        return self._age
    def get_name(self):
        return self._name
    def set_age(self,age):
        self._age=age
    def set_name(self,name):
        self._name=name


class Pixel:
    """
    _x - x coordinate
    _y - y coordinate
    _red - a value between 0 and 255
    _green - a value between 0 and 255
    _blue - a value between 0 and 255
    """
    def __init__(self,x,y,red=0,green=0,blue=0):
        self._x=x
        self._y=y
        self._red=red
        self._green=green
        self._blue=blue

    def set_coords(self, x, y):
        self._x=x
        self._y=y

    def set_grayscale(self):
        avg=(self._red+self._green+self._blue)/3
        self._red=avg
        self._green=avg
        self._blue=avg

    def print_pixel_info(self):
        only=""
        if(self._red==0 and self._blue==0 and self._green!=0):
            only="Green"
        if (self._green == 0 and self._blue == 0 and self._red != 0):
            only = "Red"
        if (self._red == 0 and self._green == 0 and self._blue != 0):
            only = "Blue"
        print("X: %d, Y: %d, Color:(%d,%d,%d) %s" % (self._x,self._y,self._red,self._green,self._blue,only))

class BigThing:
    def __init__(self,var):
        self._var=var
    def size(self):
        if(isinstance(self.var,int)):
            return self._var
        elif(isinstance(self._var,dict) or isinstance(self._var,list) or isinstance(self._var,str)):
            return len(self._var)

class BigCat(BigThing):
    def __init__(self,var,weight):
        self._weight=weight
        self._var=var
    def size(self):
        if(self._weight>20):
            return "Very Fat"
        elif(self._weight>15):
            return "Fat"
        else:
            return "OK"

class Animal:
    def __init__(self,name,hunger=0):
        Animal.zoo_name="Hayaton"
        self._name=name
        self._hunger=hunger
    def get_name(self):
        return self._name
    def is_hungry(self):
        return self._hunger>0
    def feed(self):
        self._hunger-=1

    def talk(self):
        pass
    def __str__(self):
        return type(self).__name__ + " " + self._name
class Dog(Animal):
    def talk(self):
        print("woof woof")
    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def talk(self):
        print("meow")
    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self,name,hunger=0,color="Green"):
        super().__init__(name,hunger)
        _color= color
    def talk(self):
        print("tsssss")
    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):
    def talk(self):
        print("Good day, darling")
    def sing(self):
        print("It's gonna be phenomen-phemomen-phenomenal!")

class Dragon(Animal):
    def __init__(self,name,hunger=0):
        super().__init__(name,hunger)
        _stink_count=6
    def talk(self):
        print("Raaaawr")
    def breath_fire(self):
        print("$@#$#@$")

def main():
    Whale.count=0
    moby=Whale(2,"moby")
    dik=Whale(10)
    moby.birthday()
    moby.set_name("buli")
    print(moby.get_name())
    print(moby.get_age())
    print(dik.get_name())
    print(dik.get_age())
    print(Whale.count)

    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()

    cutie = BigCat("mitzy", 22)
    print(cutie.size())

    zoo_lst=[]
    dog=Dog("Brownie",10)
    cat=Cat("Zelda",3)
    skunk=Skunk("Stinky",0)
    unicorn=Unicorn("Keith",7)
    dragon=Dragon("Lizzy",1450)
    zoo_lst+=[dog,cat,skunk,unicorn,dragon]
    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()
        print(animal)
        animal.talk()
        if(isinstance(animal,Dog)):
            animal.fetch_stick()
        if(isinstance(animal,Cat)):
            animal.chase_laser()
        if(isinstance(animal,Skunk)):
            animal.stink()
        if(isinstance(animal,Unicorn)):
            animal.sing()
        if(isinstance(animal,Dragon)):
            animal.breath_fire()

    print(Animal.zoo_name)
if __name__ == '__main__':
    main()
