import random

class Personaje:
    def __init__(self, nombre, signo):
        self.nombre = nombre
        self.signo = signo
        self.nivel = 1
        self.experiencia = 0
        self.fuerza = 10
        self.defensa = 10
        self.evasion = 10
        self.precision = 10
        self.cosmo = 100
        self.habilidades = []
        self.armadura = None

    def explorar(self):
        # Simulación de exploración
        resultado = random.choice(["enemigo", "nada", "habilidad"])
        if resultado == "enemigo":
            self.enfrentar_enemigo()
        elif resultado == "habilidad":
            self.ganar_habilidad()

    def enfrentar_enemigo(self):
        # Lógica para combatir con un enemigo
        pass

    def ganar_habilidad(self):
        # Lógica para ganar una habilidad
        pass

    def equipar_armadura(self, armadura_nombre):
        # Lógica para equipar una armadura
        self.armadura = armadura_nombre

if __name__ == "__main__":
    personaje = Personaje("Seiya", "Pegaso")

    for _ in range(10):
        personaje.explorar()
        if random.random() < 0.2:  # Simular la obtención de una armadura con un 20% de probabilidad
            armaduras_disponibles = ["Bronce", "Plata", "Oro"]
            armadura_obtenida = random.choice(armaduras_disponibles)
            personaje.equipar_armadura(f"Caballero de {armadura_obtenida}")

    print(f"{personaje.nombre} ha obtenido la armadura: {personaje.armadura}")

