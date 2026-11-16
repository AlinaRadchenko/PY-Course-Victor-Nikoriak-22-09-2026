# AI log: none
class Ball:
    def __init__(self, color):
        self.color = color

    def __repr__(self):
        return f"Ball('{self.color}')"

    def __str__(self):
        return f"a {self.color} ball"


b = Ball("red")
print(b)          # a red ball
print(repr(b))    # Ball('red')

print(b) # a red ball
print([b, Ball("blue")]) # [Ball('red'), Ball('blue')]
print(f"I have {b}") # I have a red ball
