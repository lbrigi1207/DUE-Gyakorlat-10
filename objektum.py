import string
import random

class Jelszoobjektum():
    jelszo = ''
    jelszohossz = None
    kell_szamjegy = None
    kell_irasjel = None

    def __init__(self):
        self.jelszohossz = 8
        self.kell_szamjegy = True
        self.kell_irasjel = False

    def jelszogeneralas_alap(self):
        self.jelszo = '123456'

    def jelszogenerator(self):
        karakter_lista = string.ascii_letters
        if self.kell_szamjegy:
            karakter_lista += string.digits

        if self.kell_irasjel:
            karakter_lista += string.punctuation

        for _ in range(self.jelszohossz):
            self.jelszo = self.jelszo + karakter_lista[random.randint(0, len(karakter_lista) - 1)]

#class Felhasznalo(Jelszoobjektum):

if __name__ == '__main__':
    pwd = Jelszoobjektum()
    #pwd.jelszohossz = 15
    pwd.kell_irasjel = True
    pwd.jelszogenerator()

    print(pwd.jelszo)
    print(pwd.jelszohossz)
    print(pwd.kell_szamjegy)
    print(pwd.kell_irasjel)
