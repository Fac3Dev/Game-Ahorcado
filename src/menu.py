import pyglet
import resource_managers.sprite_manager
import resource_managers.sound_manager
import resource_managers.font_manager

# Crea la ventana inicial que contiene el menu principal del juego
# Se define el tamaño inicial de la ventana, si esta se puede cambiar, y el titulo de la ventana
window = pyglet.window.Window(width=1680, 
                              height=900, 
                              resizable=True,
                              caption='Adivina la palabra!')
window.set_minimum_size(1280, 720)                                  #Establece el tamaño minimo permitido de la ventana
window.set_maximum_size(1680, 900)                                  #Establece el tamaño maximo permitido de la ventana

icon = pyglet.image.load('../images/icon.png')                      #Carga el icono del juego
window.set_icon(icon)                                               #Establece el icono cargado

pyglet.font.add_file('../fonts/DeliciousHandrawn_Regular.ttf')      #Agrega un tipo de letra externo
#DeliciousHandrawn_Regular = pyglet.font.load('Delicious Handrawn')  #Carga el tipo de letra con el nombre indicado

background_menu = pyglet.image.load('../images/background.png')     #Carga ka imagen de fondo del menu principal
background_menu_sprite = pyglet.sprite.Sprite(background_menu)      #Crea un sprite a partir de la imagen cargada
window.background = background_menu_sprite                          #Asigna el sprite al background del juego

main_song = pyglet.media.load('../sounds/creepy_mood.wav', streaming=False)     #Carga la cancion del menu principal
main_song.play()                                                                #reproduce la cancion del menu principal


# Funcion labeldraw que crea y dibuja una etqueta en pantalla cada vez que se manda a llamar
def labeldraw():
    label_tittle = pyglet.text.Label(
        "¡Adivina la palabra!",
        font_name="Delicious Handrawn",
        font_size=46,
        x=window.width // 2,
        y=window.height // 1.3,
        anchor_x="center",
        anchor_y="center",
        bold=True,
    )
    label1 = pyglet.text.Label(
        "Nueva partida",
        font_name="Delicious Handrawn",
        font_size=26,
        x=window.width // 2,
        y=window.height // 2,
        anchor_x="center",
        anchor_y="center",
    )
    label2 = pyglet.text.Label(
        "Salir",
        font_name="Delicious Handrawn",
        font_size=26,
        x=window.width // 2,
        y=window.height // 2.4,
        anchor_x="center",
        anchor_y="center",
    )
    label_tittle.draw()
    label1.draw()
    label2.draw()