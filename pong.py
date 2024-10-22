import pygame

pygame.init()
pantalla = pygame.display.set_mode((800,600))

salir =False
cont =0

while not salir:    #bucle principal (main loop) 
    cont = cont +1
    print(cont)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
          # print('Se ha cerrado la ventana')
           salir = True
        
   # print('se ha producido un evento del tipo:', evento)

    # renderizar mis objetos
    # 1. borrar la pantalla
    pygame.draw.rect(pantalla, (0,0,0), ((0,0), (800,600)) )

    # 2. pintar los objetos en su nueva posición

    rectangulo = pygame.Rect(50,50,300,150)
    pygame.draw.rect(pantalla,(cont % 255, 68,158), rectangulo )

    # mostrar los cambios en la pantalla
    pygame.display.flip()


pygame.quit()