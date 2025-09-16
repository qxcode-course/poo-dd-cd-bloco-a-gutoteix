class Towel:
    def __init__(self, color: str, size: str):
        self.color = "red"
        self.size = "p"
        self.wetness = 0
    
    def __str__(self):
        return f"color:{self.color}, tam:{self.size}, hum:{self.wetness}"

towel = Towel("green", "G")
towel2 = Towel("black", "GG")


towel.color = "White"
print(towel.color)
print(towel.size)
print(towel.wetness)