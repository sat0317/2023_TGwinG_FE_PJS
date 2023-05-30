class PrintVarAlgorithm:
    def __init__(self, number, var) -> None:
        self.number = number
        self.var    = var
    def makeAndPrintAlgorithm(self):
        for times in tuple(range(1, self.number+1))+tuple(range(self.number-1, 0, -1)):
            print(" " * (self.number-times) + self.var * (times*2-1))

PrintVarAlgorithm(5, "^").makeAndPrintAlgorithm()
PrintVarAlgorithm(4, "1").makeAndPrintAlgorithm()
