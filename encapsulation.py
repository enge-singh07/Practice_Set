class car:
    __topspeed = 100
    tyre = 4

    def work (self):
        print("car is working")
    def __stop(self):
        print("car stopped")
    def setter (self,x):
        self.__topspeed = x
    def getter (self):
        print(self.__topspeed)

    alto = car()
    alto.setter(400)
    alto.getter()
    alto._car__stop()
