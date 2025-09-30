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
        if self.pas < self.pasMax:
            self.pas += 1
        else:
            print("fail: limite de pessoas atingido")
    
    def leave(self) -> None:
        if self.pas > 0:
            self.pas -= 1
        else:
            print("fail: nao ha ninguem no carro")
        
    def fuel(self, increment: int) -> None:
        self.gas += increment
        if self.gas > self.gasMax:
            self.gas = self.gasMax

    def drive(self, distance: int) -> None:
        if self.pas == 0:
            print("fail: nao ha ninguem no carro")
            return
            
        if self.gas == 0:
            print("fail: tanque vazio")
            return 

        if self.gas >= distance:
            self.gas -= distance
            self.km += distance
            
        else:
            self.km += self.gas
            print(f"fail: tanque vazio apos andar {self.gas} km")
            self.gas = 0
        
    
def main():
    carro = Car()
    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "show":
            print(carro)
        elif args[0] == "enter":
            carro.enter()
        elif args[0] == "leave":
            carro.leave()
        elif args[0] == "fuel":
            carro.fuel(int(args[1]))
        elif args[0] == "drive":
            carro.drive(int(args[1]))
        elif args[0] == "end":
            break
main()