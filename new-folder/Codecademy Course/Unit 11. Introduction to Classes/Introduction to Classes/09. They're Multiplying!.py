class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print self.name
        print self.age

hippo = Animal("Ania", 3) # Remember to use Animal()
sloth = Animal("Ala", 5)
ocelot = Animal("Jan", 2)

print hippo.health
print sloth.health
print ocelot.health
