import pyglet

class Opciones:
    def __init__(self, window):
        self.window = window
        self.state = 2
        self.setFirst = 0
        #Recibe el diccionario anidado con la informacion de coordenadas de las etiquetas
        self.di_coor = self.labelSet()
    #Agrega el fondo correspondiente a la pantalla actual
    def setBackground(self):
        if self.setFirst == 0:
            #Carga ka imagen de fondo del menu principal
            background_opciones = pyglet.image.load('../images/background_op.png')
            #Crea un sprite a partir de la imagen cargada
            background_opciones_sprite = pyglet.sprite.Sprite(background_opciones)
            #Asigna el sprite al background del juego
            self.window.background = background_opciones_sprite
    #Funcion que controla la apariencia del menu de opciones
    def menuOpciones(self):
        if self.setFirst == 0:
            self.pushHandler()
            self.setFirst = 1
        self.labeldraw()
    #Agrega los event handlers a el objeto window
    def pushHandler(self):
        self.window.push_handlers(self.on_mouse_press, self.on_mouse_motion)
    #Se crean las etiquetas del menu principal y retornando informacion en un diccionario
    def labelSet(self):
        #Se define y crea la etiqueta label_tittle 
        label_tittle = pyglet.text.Label(
            "¡Opciones!",
            font_name="Delicious Handrawn",
            font_size=46,
            x=self.getWidth() // 2,
            y=self.getHeight() // 1.2,
            anchor_x="center",
            anchor_y="center",
            bold=True,
        )
        #Se define y crea la etiqueta label1
        label1 = pyglet.text.Label(
            "Resolución:",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2.3,
            y=self.getHeight() // 1.50,
            anchor_x="right",
            anchor_y="center",
        )
        #Se define y crea la etiqueta label2
        label2 = pyglet.text.Label(
            "Modo de pantalla:",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2.3,
            y=self.getHeight() // 1.75,
            anchor_x="right",
            anchor_y="center",
        )
        #Se define y crea la etiqueta label3
        label3 = pyglet.text.Label(
            "Volumen musica:",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2.3,
            y=self.getHeight() // 2.05,
            anchor_x="right",
            anchor_y="center",
        )
        #Se define y crea la etiqueta label4
        label4 = pyglet.text.Label(
            "Volumen efectos:",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2.3,
            y=self.getHeight() // 2.45,
            anchor_x="right",
            anchor_y="center",
        )
        #Se define y crea la etiqueta label5
        label5 = pyglet.text.Label(
            "Aplicar",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2,
            y=self.getHeight() // 3.25,
            anchor_x="center",
            anchor_y="center",
        )
        #Se define y crea la etiqueta label6
        label6 = pyglet.text.Label(
            "Regresar",
            font_name="Delicious Handrawn",
            font_size=26,
            x=self.getWidth() // 2,
            y=self.getHeight() // 4.00,
            anchor_x="center",
            anchor_y="center",
        )
        di_coor = {
            "di_la_x": {"label_tittle": label_tittle.x, 
                    "label1": label1.x, 
                    "label2": label2.x,
                    "label3": label3.x,
                    "label4": label4.x,
                    "label5": label5.x,
                    "label6": label6.x},
            "di_la_y": {"label_tittle": label_tittle.y, 
                    "label1": label1.y, 
                    "label2": label2.y,
                    "label3": label3.y,
                    "label4": label4.y,
                    "label5": label5.y,
                    "label6": label6.y},
            "di_la_cw": {"label_tittle": label_tittle.content_width, 
                    "label1": label1.content_width, 
                    "label2": label2.content_width,
                    "label3": label3.content_width,
                    "label4": label4.content_width,
                    "label5": label5.content_width,
                    "label6": label6.content_width},
            "di_la_ch": {"label_tittle": label_tittle.content_height, 
                    "label1": label1.content_height, 
                    "label2": label2.content_height,
                    "label3": label3.content_height,
                    "label4": label4.content_height,
                    "label5": label5.content_height,
                    "label6": label6.content_height},
            "labels": {"label_tittle": label_tittle, 
                       "label1": label1, 
                       "label2": label2, 
                       "label3": label3,
                       "label4": label4,
                       "label5": label5,
                       "label6": label6}
        }
        return di_coor
    #Funcion que se encarga de dibujar las etiquetas en pantalla
    def labeldraw(self):
        labels = self.di_coor["labels"]
        labels["label_tittle"].draw()
        labels["label1"].draw()
        labels["label2"].draw()
        labels["label3"].draw()
        labels["label4"].draw()
        labels["label5"].draw()
        labels["label6"].draw()
    #Funcion que define que codigo ejecutar cuando se presiona un boton en el mouse
    def on_mouse_press(self, x, y, button, modifiers):
        if button == pyglet.window.mouse.LEFT:
            di_la_x = self.di_coor["di_la_x"]
            di_la_y = self.di_coor["di_la_y"]
            di_la_cw = self.di_coor["di_la_cw"]
            di_la_ch = self.di_coor["di_la_ch"]
            if (di_la_x["label5"] - di_la_cw["label5"]/2 < x < di_la_x["label5"] + di_la_cw["label5"]/2 and 
                di_la_y["label5"] - di_la_ch["label5"]/2 < y < di_la_y["label5"] + di_la_ch["label5"]/2):
                print('Configuracion guardada')
            elif (di_la_x["label6"] - di_la_cw["label6"]/2 < x < di_la_x["label6"] + di_la_cw["label6"]/2 and 
                di_la_y["label6"] - di_la_ch["label6"]/2 < y < di_la_y["label6"] + di_la_ch["label6"]/2):
                self.state = 0
                self.window.remove_handlers(self.on_mouse_press, self.on_mouse_motion)
            else:
                print('AMONGUS2')
    #Funcion que define que codigo ejecutar cuando se mueve el mouse
    def on_mouse_motion(self, x, y, dx, dy):
        di_la_x = self.di_coor['di_la_x']
        di_la_y = self.di_coor['di_la_y']
        di_la_cw = self.di_coor['di_la_cw']
        di_la_ch = self.di_coor['di_la_ch']
        labels = self.di_coor["labels"]
        if (di_la_x["label5"] - di_la_cw["label5"]/2 < x < di_la_x["label5"] + di_la_cw["label5"]/2 and 
            di_la_y["label5"] - di_la_ch["label5"]/2 < y < di_la_y["label5"] + di_la_ch["label5"]/2):
            labels["label5"].color = (102, 102, 255, 255)
        elif (di_la_x["label6"] - di_la_cw["label6"]/2 < x < di_la_x["label6"] + di_la_cw["label6"]/2 and 
            di_la_y["label6"] - di_la_ch["label6"]/2 < y < di_la_y["label6"] + di_la_ch["label6"]/2):
            labels["label6"].color = (102, 102, 255, 255)
        else:
            labels["label5"].color = (255, 255, 255, 255)
            labels["label6"].color = (255, 255, 255, 255)
    #Retorna el ancho de la ventana del juego
    def getWidth(self):
        return self.window.width
    #Retorna el alto de la ventana del juego
    def getHeight(self):
        return self.window.height