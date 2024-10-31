import pygame

ALTO = 600
ALTO_PALA = 100
ANCHO = 800
ANCHO_PALA = 20
COLOR_FONDO = (0,0,0)  #(red, green,blue)
MARGEN = 30

COLOR_OBJETOS = (255, 255, 255)

class Pong:

    
    def __init__(self):
      pygame.init()      
      self.pantalla = pygame.display.set_mode((ANCHO ,ALTO))


    def jugar(self):
        salir = False
        cont = 0

        while not salir:  # bucle principal(main loop)
            cont = cont + 1
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    print('se ha cerrado la ventan')
                    salir = True
                    cont =0
        

            # como renderizar mis objetos
            # pintar los objetos en la nueva posición
            #1. borrar la pantalla

            pygame.draw.rect(self.pantalla, COLOR_FONDO, ((0,0), (ANCHO,ALTO,)))

            # 2. pintar jugador 1(izquierdo)            
            # pygame.Rect(izq,arriba,ancho,alto)
            arriba = (ALTO-ALTO_PALA)/2 # ALTO/2 -ALTO_PALA)
            jugador1 = pygame.Rect(MARGEN, arriba, ANCHO_PALA,ALTO_PALA)
            pygame.draw.rect(self.pantalla,(COLOR_OBJETOS),jugador1)

             # 3. pintar jugador 2(derecho)
            arriba = (ALTO-ALTO_PALA)/2
            izquierda = ANCHO - MARGEN - ANCHO_PALA
            jugador2 = pygame.Rect(izquierda, arriba, ANCHO_PALA,ALTO_PALA)
            pygame.draw.rect(self.pantalla,(COLOR_OBJETOS),jugador2)
              


            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()
            

      








