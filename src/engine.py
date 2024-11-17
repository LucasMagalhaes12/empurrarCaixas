from render import Render


map1 = [
    [5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 4, 4, 4, 4, 4, 5],
    [5, 5, 4, 0, 0, 3, 4, 5],
    [5, 5, 4, 0, 0, 0, 4, 5],
    [5, 5, 4, 4, 2, 0, 4, 5],
    [5, 5, 5, 4, 1, 0, 4, 5],
    [5, 5, 5, 4, 4, 4, 4, 5],
    [5, 5, 5, 5, 5, 5, 5, 5],
]

map2 = [
    [5, 5, 5, 5, 5, 5, 5, 5],
    [5, 4, 4, 4, 4, 4, 4, 5],
    [5, 4, 0, 0, 3, 3, 4, 5],
    [5, 4, 0, 2, 0, 0, 4, 5],
    [5, 4, 0, 0, 2, 2, 4, 5],
    [5, 4, 0, 0, 1, 0, 4, 5],
    [5, 4, 4, 4, 4, 4, 4, 5],
    [5, 5, 5, 5, 5, 5, 5, 5],
]

map3 = [
    [5, 5, 5, 5, 5, 5, 5, 5],
    [5, 5, 4, 4, 4, 4, 4, 5],
    [5, 5, 4, 0, 0, 3, 4, 5],
    [5, 5, 4, 0, 0, 4, 4, 5],
    [5, 5, 4, 4, 2, 4, 5, 5],
    [5, 5, 5, 4, 1, 4, 5, 5],
    [5, 5, 5, 4, 4, 4, 5, 5],
    [5, 5, 5, 5, 5, 5, 5, 5],
]


class Engine:
    def __init__(self):
        #                   0: moves       1: player        2: caixas            3: point          4: wall           5: void
        self.__color = [(0.9, 0.9, 0.9), (0.4, 0.6, 1), (0.98, 0.643, 0.086), (1.0, 0.0, 0.0), (0.4, 0.4, 0.4), (0.5, 0.5, 0.5)]
        self.__render = Render() # rectWidth=20, rectHeight=20)
        self.__level = -1
        self.__maps = [map1, map2, map3]
        self.__playerPos = 0, 0
        self.__winPos = []
        
        self.MOVE = 0
        self.PLAYER = 1
        self.BOX = 2
        self.POINT = 3
        self.WALL = 4
        self.VOID = 5


    def startMap(self):
        self.__level += 1
        if self.__level >= len(self.__maps):
            return False
        
        self.__mapCurrent = self.__maps[self.__level]
        self.__winPos = []
        
        for x in range(len(self.__mapCurrent)):
            for y in range(len(self.__mapCurrent[0])):

                if self.__mapCurrent[y][x] == self.PLAYER:
                    self.__playerPos = x, y

                elif self.__mapCurrent[y][x] == self.POINT:
                    self.__winPos.append([x, y])

        return True


    def drawMap(self, mapSet):
        for x in range(len(mapSet)):
            for y in range(len(mapSet[0])):
                self.__render.drawRects(x*self.__render.get_rectWidth(), y*self.__render.get_rectHeight(), self.__color[mapSet[y][x]])


    def get_controls(self):
        inputKeyboard = input("move: ")
        
        moveX = 0
        moveY = 0

        match inputKeyboard:
            case 'w':
                moveY = -1
            case 's':
                moveY = 1
            case 'a':
                moveX = -1
            case 'd':
                moveX = 1   
        return (moveX, moveY)


    def move(self, move:tuple, map):
        moveX, moveY = move
        x, y = self.__playerPos
        
        if map[y+moveY][x+moveX] == self.MOVE or map[y+moveY][x+moveX] == self.POINT:
            map[y+moveY][x+moveX] = self.PLAYER
            self.__playerPos = x+moveX, y+moveY
            if [x, y] not in self.__winPos:
                map[y][x] = self.MOVE
            else:
                map[y][x] = self.POINT
            
        elif map[y+moveY][x+moveX] == self.BOX:
            if map[y+moveY*2][x+moveX*2] == self.MOVE or map[y+moveY*2][x+moveX*2] == self.POINT:
                map[y+moveY*2][x+moveX*2] = self.BOX
                map[y+moveY][x+moveX] = self.PLAYER
                self.__playerPos = x+moveX, y+moveY
                if [x, y] not in self.__winPos:
                    map[y][x] = self.MOVE
                else:
                    map[y][x] = self.POINT
            

    def win(self, map):
        for x, y in self.__winPos:
            if map[y][x] != self.BOX:
                return False
        return True


    def updateScreen(self):
        self.__render.clear()
        self.drawMap(self.__mapCurrent)
        self.__render.save()


    def update(self):
        self.startMap()
        while True:
            # for i in self.__mapCurrent:
            #     print(i)
            self.updateScreen()
            self.move(self.get_controls(), self.__mapCurrent)
            if self.win(self.__mapCurrent):
                self.updateScreen()
                if not self.startMap():
                    break
                
