import math


class ConversionAngulos:
    def __init__(self, angulo):
        self.angulo = angulo

    def grados_a_radianes(self):
        return self.angulo * math.pi / 180

    def radianes_a_grados(self):
        return self.angulo * 180 / math.pi

    def mostrar_conversion(self):
        angulo_radianes = self.grados_a_radianes()
        angulo_grados = self.radianes_a_grados()
        print(f"{self.angulo} grados son {angulo_radianes:.4f} radianes.")
        print(f"{self.angulo} radianes son {angulo_grados:.4f} grados.")


# Uso de la clase
def main():
    angulo = float(input("Ingrese el ángulo: "))
    conversion = ConversionAngulos(angulo)

    print("Convertir de grados a radianes:")
    print(f"El ángulo en radianes es {conversion.grados_a_radianes():.4f}\n")

    print("Convertir de radianes a grados:")
    print(f"El ángulo en grados es {conversion.radianes_a_grados():.4f}\n")


if __name__ == "__main__":
    main()
