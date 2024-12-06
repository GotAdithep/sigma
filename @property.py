class Location:
    def __init__(self,person,room,floor):
        self.person = ""
        self.room = room
        self.floor = floor

    @property
    def get_person(self):
        return self.person
    @get_person.setter
    def get_person(self, x):
        self.person = x
    @property
    def get_room(self):
        return self.room
    @get_room.setter
    def get_room(self, y):
        self.room = y
    @property
    def get_floor(self):
        return self.floor
    @get_floor.setter
    def get_floor(self, z):
        self.floor = z


    def __str__(self):
        if self.person == "":
            return f"{self.room} on floor {self.floor}. No one is in this room."
        else:
            return f"{self.room} on floor {self.floor}. {self.person} is in this room."

location = Location("Teddy", "ICU", 3)
print(location)

