import pyglet #importando la libreria
import menu #importa el menu principal

# Se define que se debe hacer cada vez que el tamaño de la ventana cambia
#@window.event
#def on_resize(width, height):

# Función de dibujo que se llama cada vez que la ventana necesita actualizarse
@menu.window.event
def on_draw():
    menu.window.clear()
    menu.window.background.draw()
    menu.labeldraw()

# Ejecutar la aplicación
pyglet.app.run()
