import cairo

class Render:
    def __init__(self, WIDTH:int=400, HEIGHT:int=400):
        self.__surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        self.__context = cairo.Context(self.__surface)


    def clear(self, color:tuple=(0,0,0)):
        self.__context.set_source_rgb(*color)
        self.__context.paint()


    def drawRects(self, x:int, y:int, width:int=50, heitght:int=50, color:tuple=(0, 1, 0)):
        self.__context.set_source_rgb(*color)
        self.__context.rectangle(x, y, width, heitght)
        self.__context.fill()


    def drawPoints(self, width:int=15, color:tuple=(1, 1, 1)):
        self.__context.set_source_rgb(*color)
        self.__context.arc(200, 200, width, 0, 2 * 3.14)
        self.__context.fill()


    def save(self):
        self.__surface.write_to_png("main.png")
