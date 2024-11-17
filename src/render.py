import cairo

class Render:
    def __init__(self, WIDTH:int=400, HEIGHT:int=400, rectWidth:int=50, rectHeight:int=50):
        self.__surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
        self.__context = cairo.Context(self.__surface)
        self.__rectWidth = rectWidth
        self.__rectHeight = rectHeight


    def get_rectWidth(self):
        return self.__rectWidth
    

    def get_rectHeight(self):
        return self.__rectHeight


    def clear(self, color:tuple=(0,0,0)):
        self.__context.set_source_rgb(*color)
        self.__context.paint()


    def drawRects(self, x:int, y:int, color:tuple):
        self.__context.set_source_rgb(*color)
        self.__context.rectangle(x, y, self.__rectWidth, self.__rectHeight)
        self.__context.fill()


    def drawPoints(self,x, y, color:tuple, width:int=15):
        self.__context.set_source_rgb(*color)
        self.__context.arc(x, y, width, 0, 2 * 3.14)
        self.__context.fill()


    def save(self):
        self.__surface.write_to_png("main.png")
