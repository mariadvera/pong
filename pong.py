import pygame

ANCHO =800
ALTO = 600
ALTO_PALA = 100
MARGEN = 20
ANCHO_PALA = 30

COLOR_FONDO = (0,0,0) # RGB (red, green, blue)
COLOR_OBJETOS = (200,200,200)



class Pong:

  def __init__(self):
     pygame.init()
     self.pantalla = pygame.display.set_mode((ANCHO,ALTO))

  def jugar(self):
    salir = False

    while not salir:
    # bucle principal(main loop)   
        for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
             salir = True

    # renderizar mis objetos

    # 1. borrar la pantalla: pintar un cuadrado con el color de fondo que ocupe todo la pantalla 
        pygame.draw.rect(self.pantalla, COLOR_FONDO,((0,0),(ANCHO,ALTO)) )

    # 2. pintar jugador 1 (izquierda)
    # pygame.Rect(izda, arriba, ancho, alto)
    arriba = (ALTO-ALTO_PALA)/2  # ALTO/2 -ALTO_PALA/2   
    jugador1 = pygame.Rect(MARGEN, arriba, ANCHO_PALA, ALTO_PALA)
    pygame.draw.rect(self.pantalla, COLOR_OBJETOS, jugador1) 

    # Pintar jugador 2(derecha)

    izquierda =  ANCHO -MARGEN -ANCHO_PALA
    jugador2 = pygame.Rect(izquierda, arriba, ANCHO_PALA, ALTO_PALA)
    pygame.draw.rect(self.pantalla, COLOR_OBJETOS, jugador2) 

    # mostrar los cambios en la pantalla 
    pygame.display.flip() 


pygame.quit()


