from random import randint
import pygame


ALTO = 600
ANCHO = 800
ALTO_PALA = 100
ANCHO_PALA = 20
MARGEN = 30

COLOR_FONDO = (0, 0, 0)  # RGB (red, green, blue)
COLOR_OBJETOS = (200, 200, 200)
VEL_JUGADOR = 10   # un jugador se mueve a 10 px cada 1/40 de segundo
FPS = 40

VEL_PELOTA = 10


class Pintable(pygame.Rect):

    # def __init__(self, x, y, ancho, alto):
    #     super().__init__(x, y, ancho, alto)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, COLOR_OBJETOS, self)


class Pelota(Pintable):

    tam_pelota = 10

    def __init__(self):
        # definido (construído, instanciado...) el rectángulo
        super().__init__(
            (ANCHO - self.tam_pelota)/2,
            (ALTO-self.tam_pelota)/2,
            self.tam_pelota,
            self.tam_pelota)
        
        self.vel_y = randint(-VEL_PELOTA, VEL_PELOTA)
        self.vel_x = 0
        while self.vel_x == 0:
            self.vel_x = randint(-VEL_PELOTA, VEL_PELOTA)

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.y <= 0:
            self.vel_y = -self.vel_y
        if self.y >= (ALTO-self.tam_pelota):
            self.vel_y = -self.vel_y

        if self.x <= 0:
            self.reiniciar(True)
        if self.x >= (ANCHO - self.tam_pelota):
            self.reiniciar(False)

    def reiniciar(self, haciaIzquierda):
        self.x = (ANCHO - self.tam_pelota)/2
        self.y = (ALTO-self.tam_pelota)/2
        self.vel_y = randint(-VEL_PELOTA, VEL_PELOTA)
        if haciaIzquierda:
            self.vel_x = randint(-VEL_PELOTA, -1)
        else:
            self.vel_x = randint(1, VEL_PELOTA)

        


class Jugador(Pintable):

    def __init__(self, x):
        arriba = (ALTO-ALTO_PALA) / 2    # ALTO/2 - ALTO_PALA/2
        super().__init__(x, arriba, ANCHO_PALA, ALTO_PALA)

    def subir(self):
        posicion_minima = 0
        self.y -= VEL_JUGADOR
        if self.y < posicion_minima:
            self.y = posicion_minima

    def bajar(self):
        posicion_maxima = ALTO - ALTO_PALA
        self.y += VEL_JUGADOR
        if self.y > posicion_maxima:
            self.y = posicion_maxima


class Pong:

    def __init__(self):
        pygame.init()

        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.reloj = pygame.time.Clock()

        self.pelota = Pelota()
        self.jugador1 = Jugador(MARGEN)
        self.jugador2 = Jugador(ANCHO - MARGEN - ANCHO_PALA)


    def jugar(self):
        salir = False
        
        while not salir:
            # bucle principal (main loop)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True

                # if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:
                #     self.jugador1.rectangulo.y = self.jugador1.rectangulo.y - VEL_JUGADOR
                # if evento.type == pygame.KEYDOWN and evento.key == pygame.K_z:
                #     self.jugador1.rectangulo.y = self.jugador1.rectangulo.y + VEL_JUGADOR
                # if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                #     self.jugador2.rectangulo.y = self.jugador2.rectangulo.y - VEL_JUGADOR
                # if evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                #     self.jugador2.rectangulo.y = self.jugador2.rectangulo.y + VEL_JUGADOR

            estado_teclas = pygame.key.get_pressed()
            if estado_teclas[pygame.K_a]:
                self.jugador1.subir()
            if estado_teclas[pygame.K_z]:
                self.jugador1.bajar()
            if estado_teclas[pygame.K_UP]:
                self.jugador2.subir()
            if estado_teclas[pygame.K_DOWN]:
                self.jugador2.bajar()

            # renderizar mis objetos

            # 1. borrar la pantalla
            # pygame.draw.rect(self.pantalla, COLOR_FONDO, ((0,0), (ANCHO, ALTO)))
            self.pantalla.fill(COLOR_FONDO)

            # 2. pintar jugador 1 (izquierda)
            self.jugador1.pintame(self.pantalla)

            # 3. pintar jugador 2 (derecha)
            self.jugador2.pintame(self.pantalla)

            # 4. pintar la red
            self.pintar_red()

            # 5. calculamos posición y pintamos la pelota
            # x, y
            # posición inicial es el centro de la pantalla
            # iniciar el movimiento en una dirección aleatoria
            self.pelota.mover()
            self.pelota.pintame(self.pantalla)

            # comprobar colisión pelota con jugadores
            if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(self.jugador2):
                self.pelota.vel_x = -self.pelota.vel_x
                    
            # mostrar los cambios en la pantalla
            pygame.display.flip()
            self.reloj.tick(FPS)

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

