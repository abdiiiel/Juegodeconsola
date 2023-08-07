import time
import itertools

class Personaje:
    def __init__(self, nombre, nivel, puntos_xp, vida, ataque, defensa):
        self.nombre = nombre
        self.__nivel = nivel
        self.__puntos_xp = puntos_xp
        self.__vida = vida
        self.ataque = ataque
        self.defensa = defensa

    def info(self):
        print(self.nombre, ":")
        print("  •Nivel: ", self.__nivel)
        print("  •XP: ", self.__puntos_xp)
        print("  •Vida: ", self.__vida)
        print("  •Ataque: ", self.ataque)
        print("  •Defensa: ", self.defensa)

    def get_nombre(self):
        return self.nombre
    
    def get_ataque(self):
        return self.ataque
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def set_vida(self, vida):
        self.__vida = vida

    def defensa_reducida(self):
        return self.defensa * 10 / 100

    def esta_vivo(self):
        return self.__vida > 0

    def esta_muerto(self):
        if self.__vida == 0:
            print(f'El jugador {self.nombre} ha muerto')
    
    def recibir_danio(self, danio):
        if danio < 0:
            danio = 0
        
        self.__vida = round(self.__vida - danio, 2)

        if self.__vida <= 0:
            self.__vida = 0

    def calcular_xp_ganada(self, jugador2):
        experiencia_ganada = max(jugador2.get_nivel() * 5 - self.get_nivel() * 5, 1)
        return experiencia_ganada
    
    def aumentar_estadisticas(self):
        aumento_ataque = 5
        aumento_defensa = 5

        # Aumenta las estadísticas
        self.ataque += aumento_ataque
        self.defensa += aumento_defensa

    def subir_nivel(self):
        xp_para_subir_nivel = self.__nivel * 100  
        while self.__puntos_xp >= xp_para_subir_nivel:
            self.__nivel += 1
            self.__puntos_xp -= xp_para_subir_nivel
            print(f'El jugador {self.nombre} ha subido de nivel a nivel {self.__nivel}.')
            self.aumentar_estadisticas()
            xp_para_subir_nivel = self.__nivel * 100  

    def atacar(self, jugador1, jugador2):
        if jugador2.esta_vivo():
            print(f'El jugador {jugador1.get_nombre()} ataco a {jugador2.get_nombre()}')

            if isinstance(jugador1, Guerrero):
                danio = jugador1.get_ataque() + 5
            else:
                danio = jugador1.get_ataque()
            danio_reducido = danio - jugador2.defensa_reducida()

            if danio_reducido < 0:
                danio_reducido = 0
            jugador2.recibir_danio(danio_reducido)
            danio = jugador1.get_ataque()
            if not jugador2.esta_vivo():
                xp_ganada = jugador1.calcular_xp_ganada(jugador2)
                jugador2.esta_muerto()
                jugador1.recibir_xp(xp_ganada)
                print(f'El jugador1 ha ganado {xp_ganada} puntos de experiencia')
            else:
                print(f'La vida del jugador {jugador2.get_nombre()} es {jugador2.get_vida()}')
        else:        
            print(f'El jugador {jugador2.get_nombre()} esta muerto, no se puede atacar.')

    def recibir_xp(self, xp_ganada):
        self.__puntos_xp += xp_ganada
        self.subir_nivel()

    @staticmethod
    def jugar(jugador1, jugador2):
        print('Iniciaremos con el juego!!')
        jugador_actual = jugador1
        jugador_objetivo = jugador2
        frames = itertools.cycle(['/', '-', '|', '\\'])
        while jugador1.esta_vivo() and jugador2.esta_vivo():
            for _ in range(20): 
                frame = next(frames)
                print(f"•Turno de {jugador_actual.get_nombre()}: {frame}", end='\r')
                time.sleep(0.1)  
                print(" " * len(f"•Turno de {jugador_actual.get_nombre()}: {frame}"), end='\r')
            print(f"•Turno de {jugador_actual.get_nombre()}:")
            jugador_actual.atacar(jugador_actual, jugador_objetivo)
            jugador_actual, jugador_objetivo = jugador_objetivo, jugador_actual

class Mago(Personaje):
    def __init__(self, nombre, nivel, puntos_xp, vida, ataque_magico, defensa):
        super().__init__(nombre, nivel, puntos_xp, vida, ataque_magico, defensa)
        self.__ataque_magico = ataque_magico

    def recibir_danio(self, danio):
        danio_reducido = danio
        if danio_reducido < 0:
            danio_reducido = 0
        
        super().recibir_danio(danio_reducido)

    def atacar(self, jugador1, jugador2):
        danio = jugador1.__ataque_magico
        super().atacar(jugador1, jugador2, danio)

class Guerrero(Personaje):
    def __init__(self, nombre, nivel, puntos_xp, vida, ataque_fisico, defensa):
        super().__init__(nombre, nivel, puntos_xp, vida, ataque_fisico, defensa)
        self.__ataque_fisico = ataque_fisico

    def recibir_danio(self, danio):
        danio_reducido = danio
        if danio_reducido < 0:
            danio_reducido = 0
        
        super().recibir_danio(danio_reducido)

    def atacar(self, jugador1, jugador2):
        super().atacar(jugador1, jugador2)
            

   


jugador1 = Personaje('Goku', 0, 0, 100, 10, 5)
jugador2 = Personaje('Veggeta', 0, 0, 100, 10, 5)
jugador3 = Mago('Piccolo', 0, 0, 0, 10, 5)
jugador4 = Guerrero('Gohan',0, 0, 100, 10, 5)


Personaje.jugar(jugador1, jugador4)
#jugador3.info()
#Personaje.sistema_de_turnos(jugador1, jugador2)
#jugador1.info()

