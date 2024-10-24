import pygame

ALTO = 600
ANCHO = 800
ALTO_PALA = 100
ANCHO_PALA = 20
MARGEN = 30

COLOR_FONDO = (0, 0, 0)  # RGB (red, green, blue)
COLOR_OBJETOS = (200, 200, 200)
VELOCIDAD_JUGADOR = 5

"""
    Jugador1 : usa teclas A,Z

    Jugador 2:usa teclas feccha ARR, fecha ABajoJ

"""

class Pintable:

    def __init__(self, x, y, ancho, alto):
        self.rectangulo = pygame.Rect(x, y, ancho, alto)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self.rectangulo)


class Pelota(Pintable):

    tam_pelota = 10

    def __init__(self):
        # definido (construído, instanciado...) el rectángulo
        super().__init__(
            (ANCHO - self.tam_pelota)/2,
            (ALTO-self.tam_pelota)/2,
            self.tam_pelota,
            self.tam_pelota)


class Jugador(Pintable):

    def __init__(self, x):
        arriba = (ALTO-ALTO_PALA) / 2    # ALTO/2 - ALTO_PALA/2
        super().__init__(x, arriba, ANCHO_PALA, ALTO_PALA)


class Pong:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN)
        self.jugador2 = Jugador(ANCHO - MARGEN - ANCHO_PALA)

    def jugar(self):
        salir = False
        
        while not salir:
            # bucle principal (main loop)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT  or (evento.type == pygame.KEYUP  and evento.key == pygame.K_ESCAPE):
                    salir = True

            # renderizar mis objetos

            # 1. borrar la pantalla
            pygame.draw.rect(self.pantalla, COLOR_FONDO, ((0,0), (ANCHO, ALTO)))

            # 2. pintar jugador 1 (izquierda)
            self.jugador1.pintame(self.pantalla)

            # 3. pintar jugador 2 (derecha)
            self.jugador2.pintame(self.pantalla)

            # 4. pintar la red
            self.pintar_red()

            # 5. pintamos la pelota
            self.pelota.pintame(self.pantalla)


            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

    def pintar_red(self):
        pos_x = ANCHO / 2

        tramo_pintado = 20
        tramo_vacio = 15
        ancho_red = 6

        for y in range(0, ALTO, tramo_pintado + tramo_vacio):
            pygame.draw.line(
                self.pantalla,
                COLOR_OBJETOS,
                (pos_x, y),
                (pos_x, y + tramo_pintado),
                width=ancho_red)

