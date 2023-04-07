import pyglet

class Menu:
    #Constructor de la clase Menu
    def __init__(self, window):
        self.window = window
        self.state = 0
        #Agrega un tipo de letra externo
        pyglet.font.add_file('../fonts/DeliciousHandrawn_Regular.ttf')
        #Carga el tipo de letra con el nombre indicado
        DeliciousHandrawn_Regular = pyglet.font.load('Delicious Handrawn')
        #Carga ka imagen de fondo del menu principal
        background_menu = pyglet.image.load('../images/background.png')
        #Crea un sprite a partir de la imagen cargada
        background_menu_sprite = pyglet.sprite.Sprite(background_menu)
        #Asigna el sprite al background del juego
        self.window.background = background_menu_sprite
        #Carga la cancion del menu principal
        main_song = pyglet.media.load('../sounds/creepy_mood.wav', streaming=False)
        #reproduce la cancion del menu principal
        main_song.play()
        #Recibe el diccionario anidado con la informacion de coordenadas de las etiquetas
        self.di_coor = self.labelSet()
        #Agrega los event handlers a el objeto window
        self.window.push_handlers(self.on_mouse_press, self.on_mouse_motion)
    #Se crean las etiquetas del menu principal y retornando informacion en un diccionario
    def labelSet(self):
        #Se define y crea la etiqueta label_tittle 
        label_tittle = pyglet.text.Label(
            "¡Adivina la palabra!",
            font_name="Delicious Handrawn",
            font_size=46,
            x=self.getWidth() // 2,
            y=self.getHeight() // 1.3,
            anchor_x="center",
            anchor_y="center",
            bold=True,
        )
        #Se define y crea la etiqueta label1
        label1 = pyglet.text.Label(
            "Nueva partida",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2,
            y=self.getHeight() // 2,
            anchor_x="center",
            anchor_y="center",
        )
        #Se define y crea la etiqueta label2
        label2 = pyglet.text.Label(
            "Opciones",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2,
            y=self.getHeight() // 2.4,
            anchor_x="center",
            anchor_y="center",
        )
        #Se define y crea la etiqueta label3
        label3 = pyglet.text.Label(
            "Salir",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2,
            y=self.getHeight() // 2.8,
            anchor_x="center",
            anchor_y="center",
        )
        di_coor = {
            "di_la_x": {"label_tittle": label_tittle.x, 
                    "label1": label1.x, 
                    "label2": label2.x,
                    "label3": label3.x},
            "di_la_y": {"label_tittle": label_tittle.y, 
                    "label1": label1.y, 
                    "label2": label2.y,
                    "label3": label3.y},
            "di_la_cw": {"label_tittle": label_tittle.content_width, 
                    "label1": label1.content_width, 
                    "label2": label2.content_width,
                    "label3": label3.content_width},
            "di_la_ch": {"label_tittle": label_tittle.content_height, 
                    "label1": label1.content_height, 
                    "label2": label2.content_height,
                    "label3": label3.content_height},
            "labels": {"label_tittle": label_tittle, 
                       "label1": label1, 
                       "label2": label2, 
                       "label3": label3}
        }
        return di_coor
    #Funcion que se encarga de dibujar las etiquetas en pantalla
    def labeldraw(self):
        labels = self.di_coor["labels"]
        labels["label_tittle"].draw()
        labels["label1"].draw()
        labels["label2"].draw()
        labels["label3"].draw()
    #Funcion que define que codigo ejecutar cuando se presiona un boton en el mouse
    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            di_la_x = self.di_coor["di_la_x"]
            di_la_y = self.di_coor["di_la_y"]
            di_la_cw = self.di_coor["di_la_cw"]
            di_la_ch = self.di_coor["di_la_ch"]
            if (di_la_x["label1"] - di_la_cw["label1"]/2 < x < di_la_x["label1"] + di_la_cw["label1"]/2 and 
                di_la_y["label1"] - di_la_ch["label1"]/2 < y < di_la_y["label1"] + di_la_ch["label1"]/2):
                print('Comienza el juego')
                self.state = 1
            elif (di_la_x["label2"] - di_la_cw["label2"]/2 < x < di_la_x["label2"] + di_la_cw["label2"]/2 and 
                di_la_y["label2"] - di_la_ch["label2"]/2 < y < di_la_y["label2"] + di_la_ch["label2"]/2):
                print('Bienvenido a las opciones')
                self.state = 2
            elif (di_la_x["label3"] - di_la_cw["label3"]/2 < x < di_la_x["label3"] + di_la_cw["label3"]/2 and 
                di_la_y["label3"] - di_la_ch["label3"]/2 < y < di_la_y["label3"] + di_la_ch["label3"]/2):
                #Cierra la ventana del juego
                self.window.close()
            else:
                print('AMONGUS')
    #Funcion que define que codigo ejecutar cuando se mueve el mouse
    def on_mouse_motion(self, x, y, dx, dy):
        di_la_x = self.di_coor['di_la_x']
        di_la_y = self.di_coor['di_la_y']
        di_la_cw = self.di_coor['di_la_cw']
        di_la_ch = self.di_coor['di_la_ch']
        labels = self.di_coor["labels"]
        if (di_la_x["label1"] - di_la_cw["label1"]/2 < x < di_la_x["label1"] + di_la_cw["label1"]/2 and 
            di_la_y["label1"] - di_la_ch["label1"]/2 < y < di_la_y["label1"] + di_la_ch["label1"]/2):
            labels["label1"].color = (102, 102, 255, 255)
        elif (di_la_x["label2"] - di_la_cw["label2"]/2 < x < di_la_x["label2"] + di_la_cw["label2"]/2 and 
            di_la_y["label2"] - di_la_ch["label2"]/2 < y < di_la_y["label2"] + di_la_ch["label2"]/2):
            labels["label2"].color = (102, 102, 255, 255)
        elif (di_la_x["label3"] - di_la_cw["label3"]/2 < x < di_la_x["label3"] + di_la_cw["label3"]/2 and 
            di_la_y["label3"] - di_la_ch["label3"]/2 < y < di_la_y["label3"] + di_la_ch["label3"]/2):
            labels["label3"].color = (102, 102, 255, 255)
        else:
            labels["label1"].color = (255, 255, 255, 255)
            labels["label2"].color = (255, 255, 255, 255)
            labels["label3"].color = (255, 255, 255, 255)
        #Cambia el valor de la variable state
    #Retorna el ancho de la ventana del juego
    def getWidth(self):
        return self.window.width
    #Retorna el alto de la ventana del juego
    def getHeight(self):
        return self.window.height