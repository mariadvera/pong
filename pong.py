import pygame

class Pong:
    

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((800,600))

    def jugar(self):
        salir =False
        cont =0

        while not salir:    #bucle principal (main loop) 
            cont = cont +1
          
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                # print('Se ha cerrado la ventana')
                  salir = True
                
        # print('se ha producido un evento del tipo:', evento)

            # renderizar mis objetos
            # 1. borrar la pantalla
            pygame.draw.rect(self.pantalla, (0,0,0), ((0,0), (800,600)) )

            # 2. pintar los objetos en su nueva posición

            rectangulo = pygame.Rect(50,50,300,150)
            pygame.draw.rect(self.pantalla,(cont % 255, 68,158), rectangulo )

            # mostrar los cambios en la pantalla
            pygame.display.flip()


        pygame.quit()

if __name__== '__main__':
    juego =Pong()
    juego.jugar()