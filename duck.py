from abc import ABC, abstractmethod

class Quackable(ABC):
    @abstractmethod
    def quack(self):
        pass
        
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass
    
class Observer(ABC):
    @abstractmethod
    def update(self, duck: "Duck"):
        pass
    
class Duck(Quackable, Flyable):
    
    def __init__(self, name):
        self.name = name
        self.observable = Observable(self)
        
    def quack(self):
        print("coin")
        self.observable.notify_observers()
        
    def fly(self):
        print("vole")
        
    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)  

    
class Observable:
    def __init__(self, duck: "Duck"):
        self.duck = duck
        self.observers = []
    
    def register_observer(self, observer: Observer):
        self.observers.append(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.duck)
    
class DuckSimulator:
    def simulate(self, duck: Duck):
       duck.fly()
       duck.fly()
       duck.quack()
       duck.fly()
       duck.fly()
       duck.fly()  
        
class Goose:
    
    def honk(self):
        print('Honk')
        
class GooseAdapter(Quackable, Flyable):
    def __init__(self, goose: Goose, name = "oie"):
        self.name = name
        self.goose = goose
        
    def fly(self):
        print('vole')
    def quack(self):
        self.goose.honk()
    
        
class QuackCounter(Quackable, Flyable):
    count = 0
    def __init__(self,duck : Quackable):
        self.duck = duck
        
    def quack(self):
        QuackCounter.count += 1
        self.duck.quack()
        print(f'Le {self.duck.name} a cancane {QuackCounter.count} fois: {self.duck.name}')
        
    def fly(self):
        self.duck.fly()   
            
    def register_observer(self, observer: Observer):
        self.duck.register_observer(observer)
        
class Quackologist(Observer):
    def update(self, duck: Duck):
        print(f'Quackologist: {duck.name} a cancane')
        
if __name__ == '__main__':
    canard = QuackCounter(Duck("Canard"))
    quackologist = Quackologist()
    canard.register_observer(quackologist)
    goose =QuackCounter(GooseAdapter(Goose()))
    
    simulator = DuckSimulator()
    print("Simulation canard :")
    simulator.simulate(canard)

    print("Simulation oie :")
    simulator.simulate(goose)

    print(f"Nombre total de coins : {QuackCounter.count}")
    

