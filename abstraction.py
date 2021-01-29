from abc import ABC, abstractmethod
class madrid(ABC):
    @abstractmethod
    def training(self):
        pass
    @abstractmethod
    def marketing(self)
        pass

class myclass(madrid):
    def training(self):
        print("trainign is going on..")
    def marketing(self):
        print("marketing is going on")
m=myclass()
m.training()
m.marketing()