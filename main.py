
class Clothing():
    def __init__(self, name, clothing_type, desc="", colour="#ffffff", clean=True):
        self.name = name
        self.desc = desc
        self.clothing_type = clothing_type.upper()
        self.colour = colour
        self.clean = clean

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.desc}")

    def get_info(self):
        info_str = f"Name: {self.name}\nDescription: {self.desc}\nType: {self.clothing_type}"
        return info_str

    def get_name(self):
        return self.name

    def is_clean(self):
        return self.clean 

class Top(Clothing):
    def __init__(self, name, desc="", colour="#ffffff", sleeves=True, clean=True):
        super().__init__(name, "TOP", desc, colour, clean)
        self.sleeves = sleeves

class Bottom(Clothing):
    def __init__(self, name, desc="", colour="#ffffff", clean=True):
        super().__init__(name, "BOTTOM", desc, colour, clean)

class Shoes(Clothing):
    def __init__(self, name, desc="", colour="#ffffff", clean=True):
        super().__init__(name, "SHOES", desc, colour, clean)
        
def main():
    pass

if __name__ == "__main__":
    main()