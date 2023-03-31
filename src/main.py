import pyglet

# Crear una ventana
window = pyglet.window.Window()

# Crear un objeto label para mostrar el texto "Hello, World!"
label = pyglet.text.Label(
    "Hello, World!",
    font_name="Times New Roman",
    font_size=36,
    x=window.width // 2,
    y=window.height // 2,
    anchor_x="center",
    anchor_y="center",
)


# Función de dibujo que se llama cada vez que la ventana necesita actualizarse
@window.event
def on_draw():
    window.clear()
    label.draw()


# Ejecutar la aplicación
pyglet.app.run()
