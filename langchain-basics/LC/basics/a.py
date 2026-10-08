
class Model:
    def __init__(self):
        self.trained = False

    def play(self, sport):
        self.sport = sport

m1 = Model()
print(m1.trained)

m2 = Model()
print(m2.play("cricket"))

m3 = Model()
print(m3)