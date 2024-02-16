class CodeGenerator:
    def __init__(self):
        self.tempCont = 0
        self.labelCont = 0
        self.error = False
    def new_temp(self):
        self.tempCont += 1
        return f"_t{self.tempCont}"

    def new_label(self):
        self.labelCont += 1
        return f".l{self.labelCont}"
    
