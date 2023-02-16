class EmobilisStudent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def hello_me(self):
      print(f"my name is {self.name} and I'm {self.age} years old")

#creating an object
myobject=EmobilisStudent("Erick",50)
myobject.hello_me()

myobject2=EmobilisStudent("Antonia", 17)
myobject2.hello_me()



#create a class called magari, it should have mode,make, year properties
#minimum of three objects

class Magari:
    def __init__(self, model, make, year):
        self.model=model
        self.make=make
        self.year=year
    def hey_magari(self):
        print(f"The car is a {self.model},{self.make} made in {self.year}")

mycar=Magari("CX5","Mazda","2019")
mycar.hey_magari()
mycar2=Magari("E350","Benz","2021")
mycar2.hey_magari()

class Games:
    def __init__(self, game, type, site ):
        self.game=game
        self.type=type
        self.site=site
    def new_game(self):
        print(f"{self.game} is an {self.type} game downloaded from {self.site}" )

mygame=Games("GTA","Action","Fitgirl.reparks")
mygame.new_game()
mygame2=Games("COD","Military Action","Telegram")
mygame2.new_game()