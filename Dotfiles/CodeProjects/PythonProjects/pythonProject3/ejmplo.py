class Coche:
    def __init__(self, ruedas, marca):
        self.color = "rojo"
        self.marca = marca
        self.kilometraje = "0 kl"
        self.enmarcha = True
        self.ruedas = ruedas

    def estado(self, arranca):
        self.enmarcha = arranca
        if self.enmarcha:
            print("se mueve brooo!!!")
        else:
            print("coche flojo")

    def ruedas_coche(self):
        print("El coche tiene ", self.ruedas, " ruedas, es de marca ", self.marca, " y es de color ", self.color, end=" ")

    def cuanto(self):
        a = self.ruedas + self.ruedas
        print(a)

"""
if __name__ == "__main__":
    coche1 = Coche(4, "Toyota")
    coche1.estado(True)
    coche1.ruedas_coche()
    coche1.cuanto()
"""


class Moto(Coche):
    def __init__(self, tamano, rueda, marcas):
        super().__init__(rueda, marcas)
        self.tamano = tamano

    def ruedas_coche(self):
        super().ruedas_coche()
        print("tamaño es", self.tamano)


if __name__ == "__main__":
    moto = Moto(12, 4, "toyota")
    moto.ruedas_coche()
