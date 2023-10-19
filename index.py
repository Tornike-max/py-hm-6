class Heart:
    def __init__(self, cardio):
        self.cardio = cardio

    def get_state(self):
        if self.cardio > 200:
            return "You are having a heart attack. "
        elif self.cardio > 70:
            return "You are feeling tired."
        else:
            return "You are feeling good!"

class Brain:
    def __init__(self, brain):
        self.brain = brain

    def get_state(self):
        if self.brain > 90:
            return "You are feeling tired."
        else:
            return "You are rested"

class Leg:
    def __init__(self, person):
        self.person = person

    def get_movement(self):
        if self.person.speed > 10:
            return "You are running"
        elif self.person.speed > 0:
            return "You are walking"
        else:
            return "You are standing"

class Person:
    def __init__(self, cardio, brain, speed):
        self.heart = Heart(cardio)
        self.brain = Brain(brain)
        self.speed = speed

    def get_heart_state(self):
        return self.heart.get_state()

    def get_brain_state(self):
        return self.brain.get_state()

    def get_movement(self):
        return Leg(self).get_movement()

def main():
    heart = int(input("heart pressure: "))
    brain = int(input("brain load: "))
    speed = int(input("speed: "))

    person = Person(heart, brain, speed)

    print("Heart state:", person.get_heart_state())
    print("Brain state:", person.get_brain_state())
    print("Movement state:", person.get_movement())
    
main()