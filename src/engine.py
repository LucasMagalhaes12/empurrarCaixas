from render import Render


map1 = [
    [4, 4, 4, 4, 4, 4, 4, 4],
    [4, 4, 3, 3, 3, 3, 3, 4],
    [4, 4, 3, 0, 0, 0, 3, 4],
    [4, 4, 3, 0, 0, 3, 3, 4],
    [4, 4, 3, 3, 2, 3, 4, 4],
    [4, 4, 4, 3, 1, 3, 4, 4],
    [4, 4, 4, 3, 3, 3, 4, 4],
    [4, 4, 4, 4, 4, 4, 4, 4],
]

# 0: moves | 1: player | 2: caixas | 3: wall | 4: void

class Engine:
    def __init__(self):
        self.__color = [(0.9, 0.9, 0.9), (0.4, 0.6, 1), (0.98, 0.643, 0.086), (0.4, 0.4, 0.4), (0.5, 0.5, 0.5)]
        self.__render = Render()
        self.__mapCurrent = map1
        self.__playerPos = 0, 0
        self.MOVE = 0
        self.PLAYER = 1
        self.BOX = 2
        self.WALL = 3
        self.VOID = 4


    def updateMap(self, mapSet):
        nL = len(mapSet)
        nC = len(mapSet[0])
        for x in range(nL):
            for y in range(nC):
                if mapSet[y][x] == 1:
                    self.__playerPos = x, y
                self.__render.drawRects(x*50, y*50, color=self.__color[mapSet[y][x]])


    def move(self, map):
        inputKeyboard = input("move: ")
        x, y = self.__playerPos
        moveX = 0
        moveY = 0
        match inputKeyboard:
            case 'w':
                moveX = -1
            case 's':
                moveX = 1
            case 'a':
                moveY = -1
            case 'd':
                moveY = 1
            
        if map[y+moveX][x+moveY] == self.MOVE:
            map[y+moveX][x+moveY] = self.PLAYER
            map[y][x] = self.MOVE
            
        elif map[y+moveX][x+moveY] == self.BOX:
            if map[y+moveX*2][x+moveY*2] == self.MOVE:
                map[y+moveX*2][x+moveY*2] = self.BOX
                map[y+moveX][x+moveY] = self.PLAYER
                map[y][x] = self.MOVE


    def update(self):
        self.__render.clear()
        self.updateMap(self.__mapCurrent)
        self.__render.save()
        while True:
            self.__render.clear()
            self.move(self.__mapCurrent)
            self.updateMap(self.__mapCurrent)
            self.__render.save()
