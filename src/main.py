import pyglet
from Menu import Menu
from Opciones import Opciones
from Game import Game

# Crea la ventana inicial que contendra todo el juego
# Se define el tamaño inicial de la ventana, si esta se puede cambiar, y el titulo de la ventana
window = pyglet.window.Window(width=1680, 
                            height=900, 
                            resizable=False,
                            caption='Adivina la palabra!')
#Establece el tamaño minimo permitido de la ventana
window.set_minimum_size(1280, 720)
#Establece el tamaño maximo permitido de la ventana
window.set_maximum_size(1680, 900)
#Carga el icono del juego
icon = pyglet.image.load('../images/icon.png')
#Establece el icono cargado
window.set_icon(icon)
#Agrega un tipo de letra externo
pyglet.font.add_file('../fonts/DeliciousHandrawn_Regular.ttf')
#Carga el tipo de letra con el nombre indicado
DeliciousHandrawn_Regular = pyglet.font.load('Delicious Handrawn')
#Carga la cancion del menu principal
main_song = pyglet.media.load('../sounds/creepy_mood.wav', streaming=False)
#reproduce la cancion del menu principal
main_song.play()
#Se crean los objetos de las diferentes pantallas del juego
menu = Menu(window)
opciones = Opciones(window)
game = Game(window)

# Función de dibujo que se llama cada vez que la ventana necesita actualizarse
@window.event
def on_draw():
    window.clear()
    #Recibe el estado del juego el cual define la pantalla a mostrar
    game_state = menu.state
    #Menu principal
    if game_state == 0:
        menu.setBackground()
        window.background.draw()
        menu.menuMenu()
        
    #Gameplay del juego
    elif game_state == 1:
        window.background.draw()
        print('in game')
        #main_song.pause()
        game.test2()
    #Pantalla de opciones
    elif game_state == 2:
        opciones.setBackground()
        window.background.draw()
        opciones.menuOpciones()

        #Comprueba si debe regresar al menu principal
        if opciones.state == 0:
            #Reiniciar las variable de estado de el menu principal
            menu.state = 0
            menu.setFirst = 0
            #Reiniciar las variable de estado de el menu de opciones
            opciones.state = 2
            opciones.setFirst = 0

# Ejecutar la aplicación
pyglet.app.run()
