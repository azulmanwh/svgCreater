import pygame
import math

(width, height) = (1000, 700)
screen = pygame.display.set_mode((width, height))
global weight
weight = 40
objectsInScene = []

class Polygon():
    def __init__(self, coordinates, colour, numberOfSides):
        self.coordinates = coordinates
        self.colour = colour
        self.numberOfSides = numberOfSides

    def getColour():
        return self.colour

    def getCoordinates():
        return self.coordinates

def createShape(numberOfSides, pos):
    if(numberOfSides == 3):
        pygame.draw.polygon(screen, (0,255,0), (pos, (pos[0]-(weight), pos[1]), (pos[0]-(weight/2), pos[1]-(weight))))
        objectsInScene.append(Polygon((pos,(pos[0]-(weight),pos[1]),(pos[0]-(weight/2),pos[1]-(weight))), (0,255,0), 3))
    elif(numberOfSides == 4):
        pygame.draw.polygon(screen, (255,0,0), (pos, (pos[0],pos[1]+weight), (pos[0]+weight,pos[1]+weight), (pos[0]+weight,pos[1])))
        objectsInScene.append(Polygon((pos, (pos[0],pos[1]+weight), (pos[0]+weight,pos[1]+weight), (pos[0]+weight,pos[1])), (255,0,0), 4))
    elif(numberOfSides == 5):
        pygame.draw.polygon(screen, (255, 192, 203), (pos, (pos[0]-weight,pos[1]), (pos[0]-(weight * 3/2), pos[1]-weight), (pos[0]-(weight/2),pos[1]-(weight*3/2)), (pos[0]+(weight/2),pos[1]-weight)))
        objectsInScene.append(Polygon((pos, (pos[0]-weight,pos[1]), (pos[0]-(weight * 3/2), pos[1]-weight), (pos[0]-(weight/2),pos[1]-(weight*3/2)), (pos[0]+(weight/2),pos[1]-weight)) , (255, 192, 203), 5))

def createSVG():
    svg = '<svg xmlns="http://www.w3.org/2000/svg">'

    for polygon in objectsInScene:
        svg += "\n"
        if(polygon.numberOfSides == 3):
            first = str(polygon.coordinates[0][0]) + "," + str(polygon.coordinates[0][1])
            second = str(polygon.coordinates[1][0]) + "," + str(polygon.coordinates[1][1])
            third = str(polygon.coordinates[2][0]) + "," + str(polygon.coordinates[2][1])
            svg += "<polygon points = '" + first + ", " + second + ", " + third + "' style = 'fill:green;stroke:green;stroke-width:1' />"
        elif(polygon.numberOfSides == 4):
            first = str(polygon.coordinates[0][0]) + "," + str(polygon.coordinates[0][1])
            second = str(polygon.coordinates[1][0]) + "," + str(polygon.coordinates[1][1])
            third = str(polygon.coordinates[2][0]) + "," + str(polygon.coordinates[2][1])
            fourth = str(polygon.coordinates[3][0]) + "," + str(polygon.coordinates[3][1])
            svg += "<polygon points = '" + first + ", " + second + ", " + third + ", " + fourth +  "' style = 'fill:red;stroke:red;stroke-width:1' />"
        elif(polygon.numberOfSides == 5):
            first = str(polygon.coordinates[0][0]) + "," + str(polygon.coordinates[0][1])
            second = str(polygon.coordinates[1][0]) + "," + str(polygon.coordinates[1][1])
            third = str(polygon.coordinates[2][0]) + "," + str(polygon.coordinates[2][1])
            fourth = str(polygon.coordinates[3][0]) + "," + str(polygon.coordinates[3][1])
            fifth = str(polygon.coordinates[4][0]) + "," + str(polygon.coordinates[4][1])
            svg += "<polygon points = '" + first + ", " + second + ", " + third + ", " + fourth + ", " + fifth + "' style = 'fill:pink;stroke:pink;stroke-width:1' />"

    svg += "</svg>"

    print(svg)
    file = open("saved.svg", "w")
    file.write(svg)
    file.close()

def main():
    running = True
    mostRecentButton = 3
    global weight

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:
                    mostRecentButton = 3
                if event.key == pygame.K_4:
                    mostRecentButton = 4
                if event.key == pygame.K_5:
                    mostRecentButton = 5
                if event.key == pygame.K_b:
                    weight *= 2
                if event.key == pygame.K_s:
                    weight /= 2
                if event.key == pygame.K_ESCAPE:
                    createSVG()
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(mostRecentButton)
                print(event.pos)
                createShape(mostRecentButton, event.pos)


        pygame.display.update()
    pygame.quit()

main()