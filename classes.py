class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # instanciated
        self.age = age

    def run(self):
        print('run mate')
        return 'ok'


player1 = PlayerCharacter('Gaucho', 27)
player2 = PlayerCharacter('Lauro', 26)

print(player1.run())
print(player2.name)
