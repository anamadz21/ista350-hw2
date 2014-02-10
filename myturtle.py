import turtle
class MyTurtle(turtle.Turtle):

    def __init__(self, name, sociality, age, food):

        key = ['name', 'sociality', 'age', 'food']
        if age ==0:
            raise ValueError("0 and any other characters are invalid")
        value = [name, sociality, age, food]
	
        self.my_turtle_dict = dict(zip(key, value))

    def _get_dict(self):

    def report(self):
        
