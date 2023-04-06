import pyglet

# Crea la ventana inicial que contiene el menu principal del juego
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
#Carga ka imagen de fondo del menu principal
background_menu = pyglet.image.load('../images/background.png')
#Crea un sprite a partir de la imagen cargada
background_menu_sprite = pyglet.sprite.Sprite(background_menu)
#Asigna el sprite al background del juego
window.background = background_menu_sprite
#Carga la cancion del menu principal
main_song = pyglet.media.load('../sounds/creepy_mood.wav', streaming=False)
#reproduce la cancion del menu principal
main_song.play()
#Se define y crea la etiqueta label_tittle 
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
#Se define y crea la etiqueta label1
label1 = pyglet.text.Label(
    "Nueva partida",
    font_name="Delicious Handrawn",
    font_size=26,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)
#Se define y crea la etiqueta label2
label2 = pyglet.text.Label(
    "Opciones",
    font_name="Delicious Handrawn",
    font_size=26,
    x=window.width // 2,
    y=window.height // 2.4,
    anchor_x="center",
    anchor_y="center",
)
#Se define y crea la etiqueta label3
label3 = pyglet.text.Label(
    "Salir",
    font_name="Delicious Handrawn",
    font_size=26,
    x=window.width // 2,
    y=window.height // 2.8,
    anchor_x="center",
    anchor_y="center",
)
#Funcion que define que codigo ejecutar cuando se presiona un boton en el mouse
def on_mouse_press(x, y, button, modifiers):
    if button == pyglet.window.mouse.LEFT:
        if (label1.x - label1.content_width/2 < x < label1.x + label1.content_width/2 and 
            label1.y - label1.content_height/2 < y < label1.y + label1.content_height/2):
            print('Comienza el juego')
        elif (label2.x - label2.content_width/2 < x < label2.x + label2.content_width/2 and 
            label2.y - label2.content_height/2 < y < label2.y + label2.content_height/2):
            print('Bienvenido a las opciones')
        elif (label3.x - label3.content_width/2 < x < label3.x + label3.content_width/2 and 
            label3.y - label3.content_height/2 < y < label3.y + label3.content_height/2):
            #Cierra la ventana del juego
            window.close()
        else:
            print('AMONGUS')
#Funcion que define que codigo ejecutar cuando se mueve el mouse
def on_mouse_motion(x, y, dx, dy):
    if (label1.x - label1.content_width/2 < x < label1.x + label1.content_width/2 and 
        label1.y - label1.content_height/2 < y < label1.y + label1.content_height/2):
        label1.color = (102, 102, 255, 255)
    elif (label2.x - label2.content_width/2 < x < label2.x + label2.content_width/2 and 
        label2.y - label2.content_height/2 < y < label2.y + label2.content_height/2):
        label2.color = (102, 102, 255, 255)
    elif (label3.x - label3.content_width/2 < x < label3.x + label3.content_width/2 and 
        label3.y - label3.content_height/2 < y < label3.y + label3.content_height/2):
        label3.color = (102, 102, 255, 255)
    else:
        label1.color = (255, 255, 255, 255)
        label2.color = (255, 255, 255, 255)
        label3.color = (255, 255, 255, 255)
#Agrega los event handlers a el objeto window
window.push_handlers(on_mouse_press, on_mouse_motion)
#Funcion que se encarga de dibujar las etiquetas en pantalla
def labeldraw():
    label_tittle.draw()
    label1.draw()
    label2.draw()
    label3.draw()