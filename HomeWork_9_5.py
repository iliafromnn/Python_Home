class Sttionery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Start drawing')

class Pen(Sttionery):
    def draw(self):
        return f'{self.title} start drawing'

class Pencil(Sttionery):
    def draw(self):
        return f'{self.title} start drawing'

class Handle(Sttionery):
    def draw(self):
        return f'{self.title} start drawing'

pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

print(pen.draw())
print(pencil.draw())
print(handle.draw())