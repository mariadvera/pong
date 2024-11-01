import pygame

ALTO = 600
ALTO_PALA = 100
ANCHO = 800
ANCHO_PALA = 20
COLOR_FONDO = (0,0,0)  
COLOR_OBJETOS = (200, 200, 200)
MARGEN = 30
VEL_JUGADOR = 5




class Pintable:
    def __init__(self, x, y, ancho, alto):
        self.rectangulo  = pygame.Rect(x, y, ancho, alto)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla,COLOR_OBJETOS,self.rectangulo)           



class Pelota(Pintable):
    tam_pelota = 10  
    def __init__(self):
        # definido (construido, insatanciado..) el rectangulo
        super().__init__(       
        (ANCHO-self.tam_pelota )/2,
        (ALTO -self.tam_pelota)/2,
        self.tam_pelota,
        self.tam_pelota
        )


class Jugador(Pintable):
        def __init__(self,x):
            arriba = (ALTO-ALTO_PALA)/2
            super().__init__(x, arriba, ANCHO_PALA, ALTO_PALA)
          




class Pong:
    
    def __init__(self):
      pygame.init()      
      self.pantalla = pygame.display.set_mode((ANCHO ,ALTO))
      self.pelota = Pelota()
      self.jugador1 = Jugador(MARGEN)
      self.jugador2 = Jugador(ANCHO-MARGEN-ANCHO_PALA)


    def jugar(self):
        salir = False
        cont = 0

        while not salir:  # bucle principal(main loop)
            cont = cont + 1
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    print('se ha cerrado la ventan')
                    salir = True
                    cont = 0
        

            # como renderizar mis objetos
            # pintar los objetos en la nueva posición

            #1. borrar la pantalla
            pygame.draw.rect(self.pantalla, COLOR_FONDO, ((0,0), (ANCHO,ALTO,)))

            # 2. pintar jugador 1(izquierdo)            
            # pygame.Rect(izq,arriba,ancho,alto)
            self.jugador1.pintame(self.pantalla)
           

             # 3. pintar jugador 2(derecho)
            self.jugador2.pintame(self.pantalla)

            # 4. pintar la red
            self.pintar_red()

            # 5 pintar pelota
            self.pelota.pintame(self.pantalla)


              


            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

    def pintar_red(self):
        pos_x = ANCHO / 2

        tramo_pintado = 20
        tramo_vacio = 15
        ancho_red = 6

        for y in range(0, ALTO, (tramo_pintado + tramo_vacio)):
            pygame.draw.line(
                self.pantalla,
                (COLOR_OBJETOS),
                (pos_x,y),
                (pos_x, y + tramo_pintado ),
                width =  ancho_red) 

      
   



            

      







