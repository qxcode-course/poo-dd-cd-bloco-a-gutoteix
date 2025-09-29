class Animal:
    def __init__(self, species: str, sound: str):
        self.species = species
        self.sound = sound
        self.age = 0  

    def __str__(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

    def toString(self) -> str:
        return self.__str__()

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"
        elif self.age >= 4:
            return "RIP"
        return self.sound

    def ageBy(self, increment: int) -> None:
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            return
        self.age += increment
        if self.age >= 4:
            self.age = 4
            print(f"warning: {self.species} morreu")

def main():
    animal = None
    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if not line:
            continue

        print(f"${line}")
        parts = line.split()
        cmd = parts[0]
        if cmd == "end":
            break
        elif cmd == "init":
            species, sound = parts[1], parts[2]
            animal = Animal(species, sound)
        elif cmd == "show":
            print(animal)
        elif cmd == "grow":
            inc = int(parts[1])
            animal.ageBy(inc)
        elif cmd == "noise":
            print(animal.makeSound())

if __name__ == "__main__":
    main()