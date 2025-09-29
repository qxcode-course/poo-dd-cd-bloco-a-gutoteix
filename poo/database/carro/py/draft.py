class Car:
    def __init__(self):
        self.gas = 0
        self.gasMax = 100
        self.pas = 0
        self.pasMax = 2
        self.km = 0

    def __str__(self) -> str:
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def enter(self) -> None:
        if self.pas < self.pasMax :
            self.pas += 1
    
    def leave(self) -> None:
        self.pas -= 1
        
    def fuel(self, increment: int) -> None:
        if increment <= self.gasMax:
            self.gas = increment
    
    def drive(self, distance: int) -> None:
        if 
        
    
def main():
    carro = Car()     
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        
        if args[0] == "show":
            print(carro)
        elif args[0] == "end":
            break
        
main()