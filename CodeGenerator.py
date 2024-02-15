class CodeGenerator:
    def __init__(self):
        self.cont = 0
    def new_temp(self):
        self.cont += 1
        return f"_t{self.cont}"

    def new_label(self):
        self.cont += 1
        return f".l{self.cont}"