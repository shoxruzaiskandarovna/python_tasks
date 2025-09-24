class Talaba:
    """Talaba nomli class yaratamiz"""

    def init(self, ism, familiya, tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism

    def get_fullname(self):
        return self.familiya

    def get_lastname(self):
        return f"{self.ism} {self.familiya}"

    def tanishtir(self):
        print(f"Ismim {self.ism}. {self.familiya}. {self.tyil} yilda tug`ilganman")

    def get_age(self, yil):
        return yil - self.tyil


talaba1 = Talaba("Alijon", "VAliyev", 2000)
talaba2 = Talaba("Olim", "Olimov", 1955)
talaba3 = Talaba("Hussan", "VAliyev", 2005)
talaba4 = Talaba("Alijon", "Shamsiyev", 2004)

talaba2.tanishtir()
print(talaba3.get_name())
print(talaba3.get_lastname())
print(talaba3.get_fullname())
print(talaba4.get_age(2025))

print(talaba1.ism, talaba1.familiya, talaba1.tyil)