from abc import ABC, abstractmethod


# 🔹 Abstract Base Class
class BaseProcessor(ABC):

    @abstractmethod
    def process(self, data):
        pass


# 🔹 Child Class (Inheritance)
class TextProcessor(BaseProcessor):

    def __init__(self):
        self.count = 0

    def process(self, data):
        self.count += 1
        return data.lower()


# 🔹 Model Class
class Model:

    def __init__(self, factor):
        self.factor = factor
        self.trained = False

    def train(self, data):
        self.trained = True
        self.factor += len(data)

    def predict(self, x):
        if not self.trained:
            raise Exception("Model not trained")
        return x * self.factor


# 🔹 Pipeline (Composition)
class Pipeline:

    def __init__(self, processor: BaseProcessor, model: Model):
        self.processor = processor
        self.model = model

    def run(self, text, num):
        clean = self.processor.process(text)
        self.model.train(clean)
        return self.model.predict(num)


# -------- USAGE --------

p = TextProcessor()
m = Model(2)

pipe = Pipeline(p, m)

output1 = pipe.run("HELLO", 5)
output2 = pipe.run("WORLD", 3)

print(output1)
print(output2)
print(p.count)