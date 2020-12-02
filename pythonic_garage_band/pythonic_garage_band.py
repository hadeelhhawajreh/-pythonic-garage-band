from abc import ABC ,abstractmethod

class Band(ABC):
    allmembers=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.allmembers.append(self)
    
    def play_solos(self):
        all=[]
        for i in self.members:
            all.append(i.play_solo())
        return all


    def __str__(self):
        return f'{self.name}.'

    def __repr__(self):
        return f'<Band: {self.name}>'

    @classmethod
    def to_list(cls):
        return cls.allmembers



#  super().__init__()
class Musician(ABC):
    # constructor 
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return f'My name is {self.name} and I play {self.get_instrument()}'
    
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'
    @abstractmethod
    def get_instrument(self):
        pass

    @abstractmethod
    def play_solo(self):
        pass


class Guitarist(Musician):
    def get_instrument(self):
        return 'guitar'

    def play_solo(self):
        return 'face melting guitar solo'

class Bassist(Musician):
    def get_instrument(self):
        return 'bass'

    def play_solo(self):
        return 'bom bom buh bom'


class Drummer(Musician):
    def get_instrument(self):
        return 'drums'

    def play_solo(self):
        return 'rattle boom crash'



if __name__ == "__main__":
  h=Drummer('hadeel')
   
