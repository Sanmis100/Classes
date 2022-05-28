from unicodedata import name


class student:
    def_init_(self, name, age, tracks, score):
self.name = str(name)
self.age = int(age)
self.tracks = tracks
self.score = float(score)

def change_name(self, new_name):
return "The new name of the user is", new_name

def change_age(self, new_age):
return "The new age is", int(new_age)

def add_track(self, new_track):
return "The new track is ", new_track

def get_score(self):
return "The new score is ", self.score

Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

print(Bob.change_name("Peter"))
print(Bob.change_age(34))
print(Bob.add_track("UI/UX"))
print(Bob.get_score())
