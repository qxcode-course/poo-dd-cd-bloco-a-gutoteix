class Calculator:
    def __init__(self, batteryMax: int) -> None:
        self.batteryMax = batteryMax
        self.battery = 0
        self.display = 0.00
    
    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self, value: int) -> None:
        self.battery += value
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
    
    def sum(self, a: int, b: int) -> None:
        if self.battery > 0:
            self.battery -= 1
            self.display = float(a + b)
        else:
            print("fail: bateria insuficiente")
    
    def division(self, num: int, den: int) -> None: 
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return

        self.battery -= 1 
            
        if den == 0:
            print("fail: divisao por zero")
            return
        self.display = num / den


def main():
    calculadora = None
    
    while True:
        try:
            line: str = input().strip()
        except EOFError:
            break
            
        if not line:
            continue
            
        print("$" + line)
        args: list[str] = line.split(" ")
        
        if args[0] == "end":
            break
        
        elif args[0] == "init":
            if len(args) < 2: continue
            batteryMax_int = int(args[1])
            calculadora = Calculator(batteryMax_int)
            continue

        if calculadora is None:
            continue
            
        elif args[0] == "show":
            print(calculadora)
        
        elif args[0] == "charge":
            if len(args) < 2: continue
            charge_value = int(args[1]) 
            calculadora.charge(charge_value)
            
        elif args[0] == "sum":
            if len(args) < 3: continue
            a = int(args[1])
            b = int(args[2])
            calculadora.sum(a, b)
            
        elif args[0] == "div":
            if len(args) < 3: continue
            num = int(args[1])
            den = int(args[2])
            calculadora.division(num, den)


main()