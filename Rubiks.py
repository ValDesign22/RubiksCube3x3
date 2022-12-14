import random as rdm
import time
import tkinter as tk
from tkinter import Label, Tk, Canvas

class Cube: 
    def __init__(self):
        self.cube = self.initCube()
        self.scrambleText = ""
    
    def initCube(self):
        cube = [[['white' for i in range(3)] for j in range(3)],
                [['orange' for i in range(3)] for j in range(3)],
                [['green' for i in range(3)] for j in range(3)],
                [['red' for i in range(3)] for j in range(3)],
                [['blue' for i in range(3)] for j in range(3)],
                [['yellow' for i in range(3)] for j in range(3)]]
        return cube

    def resetCube(self):
        self.cube = self.initCube()

    def scrambleCube(self):
        scramble = []

        while len(scramble) < 15:
            face = rdm.randint(0, 5)
            direction = rdm.choice(["clockwise", "counterclockwise"])
            times = rdm.randint(1, 3)

            faceUIndex = 0
            faceUOppositeIndex = 5
            faceLIndex = 1
            faceLOppositeIndex = 3
            faceFIndex = 2
            faceFOppositeIndex = 4
            faceRIndex = 3
            faceROppositeIndex = 1
            faceBIndex = 4
            faceBOppositeIndex = 2
            faceDIndex = 5
            faceDOppositeIndex = 0

            if len(scramble) > 0:
                lastMove = scramble[-1]
                lastFace = lastMove[0]
                lastDirection = lastMove[1]
                lastTimes = lastMove[2]
                
                if lastFace == face:
                    continue
                if lastFace == face and lastDirection == direction:
                    continue
                elif lastFace == face and lastTimes == times:
                    continue
                elif lastFace == face and lastDirection == direction and lastTimes == times:
                    continue
                if lastFace == face and lastDirection == "clockwise" and direction == "counterclockwise":
                    continue
                elif lastFace == face and lastDirection == "counterclockwise" and direction == "clockwise":
                    continue

                elif lastFace == faceUIndex and face == faceUOppositeIndex:
                    continue
                elif lastFace == faceLIndex and face == faceLOppositeIndex:
                    continue
                elif lastFace == faceFIndex and face == faceFOppositeIndex:
                    continue
                elif lastFace == faceRIndex and face == faceROppositeIndex:
                    continue
                elif lastFace == faceBIndex and face == faceBOppositeIndex:
                    continue
                elif lastFace == faceDIndex and face == faceDOppositeIndex:
                    continue
                else:
                    scramble.append([face, direction, times])
            else:
                scramble.append([face, direction, times])

        scrambleText = ""

        for move in scramble:
            face = move[0]
            direction = move[1]
            times = move[2]

            if face == 0:
                scrambleText += "U"
            elif face == 1: 
                scrambleText += "L"
            elif face == 2:
                scrambleText += "F"
            elif face == 3:
                scrambleText += "R"
            elif face == 4:
                scrambleText += "B"
            elif face == 5:
                scrambleText += "D"
            
            if direction == "counterclockwise":
                scrambleText += "'"

            scrambleText += " "

        self.scrambleText = scrambleText

        return scramble

    def rotateFace(self, face, direction):
        if face == 0:
            self.rotateWhiteFace(direction)
        elif face == 1:
            self.rotateOrangeFace(direction)
        elif face == 2:
            self.rotateGreenFace(direction)
        elif face == 3:
            self.rotateRedFace(direction)
        elif face == 4:
            self.rotateBlueFace(direction)
        elif face == 5:
            self.rotateYellowFace(direction)

    def rotateWhiteFace(self, direction):
        orangeTopBar = self.cube[1][0]
        greenTopBar = self.cube[2][0]
        redTopBar = self.cube[3][0]
        blueTopBar = self.cube[4][0]

        whiteCorner1 = self.cube[0][0][0]
        whiteCorner2 = self.cube[0][0][2]
        whiteCorner3 = self.cube[0][2][0]
        whiteCorner4 = self.cube[0][2][2]

        whiteEdge1 = self.cube[0][0][1]
        whiteEdge2 = self.cube[0][1][0]
        whiteEdge3 = self.cube[0][1][2]
        whiteEdge4 = self.cube[0][2][1]

        if direction == "clockwise":
            self.cube[1][0] = greenTopBar
            self.cube[2][0] = redTopBar
            self.cube[3][0] = blueTopBar
            self.cube[4][0] = orangeTopBar

            self.cube[0][0][0] = whiteCorner3
            self.cube[0][0][1] = whiteEdge2
            self.cube[0][0][2] = whiteCorner1
            self.cube[0][1][0] = whiteEdge4
            self.cube[0][1][2] = whiteEdge1
            self.cube[0][2][0] = whiteCorner4
            self.cube[0][2][1] = whiteEdge3
            self.cube[0][2][2] = whiteCorner2
        elif direction == "counterclockwise":
            self.cube[1][0] = blueTopBar
            self.cube[2][0] = orangeTopBar
            self.cube[3][0] = greenTopBar
            self.cube[4][0] = redTopBar

            self.cube[0][0][0] = whiteCorner2
            self.cube[0][0][1] = whiteEdge3
            self.cube[0][0][2] = whiteCorner4
            self.cube[0][1][0] = whiteEdge1
            self.cube[0][1][2] = whiteEdge4
            self.cube[0][2][0] = whiteCorner1
            self.cube[0][2][1] = whiteEdge2
            self.cube[0][2][2] = whiteCorner3        
        else:
            print("Invalid direction")

    def rotateOrangeFace(self, direction):
        whiteCorner1 = self.cube[0][0][0]
        whiteEdge = self.cube[0][1][0]
        whiteCorner2 = self.cube[0][2][0]

        greenCorner1 = self.cube[2][0][0]
        greenEdge = self.cube[2][1][0]
        greenCorner2 = self.cube[2][2][0]

        yellowCorner1 = self.cube[5][0][0]
        yellowEdge = self.cube[5][1][0]
        yellowCorner2 = self.cube[5][2][0]

        blueCorner1 = self.cube[4][0][2]
        blueEdge = self.cube[4][1][2]
        blueCorner2 = self.cube[4][2][2]

        orangeCorner1 = self.cube[1][0][0]
        orangeCorner2 = self.cube[1][0][2]
        orangeCorner3 = self.cube[1][2][0]
        orangeCorner4 = self.cube[1][2][2]

        orangeEdge1 = self.cube[1][0][1]
        orangeEdge2 = self.cube[1][1][0]
        orangeEdge3 = self.cube[1][1][2]
        orangeEdge4 = self.cube[1][2][1]

        if direction == "clockwise":
            self.cube[0][0][0] = blueCorner2
            self.cube[0][1][0] = blueEdge
            self.cube[0][2][0] = blueCorner1

            self.cube[2][0][0] = whiteCorner1
            self.cube[2][1][0] = whiteEdge
            self.cube[2][2][0] = whiteCorner2

            self.cube[4][0][2] = yellowCorner2
            self.cube[4][1][2] = yellowEdge
            self.cube[4][2][2] = yellowCorner1

            self.cube[5][0][0] = greenCorner1
            self.cube[5][1][0] = greenEdge
            self.cube[5][2][0] = greenCorner2

            self.cube[1][0][0] = orangeCorner3
            self.cube[1][0][1] = orangeEdge2
            self.cube[1][0][2] = orangeCorner1
            self.cube[1][1][0] = orangeEdge4
            self.cube[1][1][2] = orangeEdge1
            self.cube[1][2][0] = orangeCorner4
            self.cube[1][2][1] = orangeEdge3
            self.cube[1][2][2] = orangeCorner2
        elif direction == "counterclockwise":
            self.cube[0][0][0] = greenCorner2
            self.cube[0][1][0] = greenEdge
            self.cube[0][2][0] = greenCorner1

            self.cube[2][0][0] = yellowCorner1
            self.cube[2][1][0] = yellowEdge
            self.cube[2][2][0] = yellowCorner2

            self.cube[4][0][2] = whiteCorner2
            self.cube[4][1][2] = whiteEdge
            self.cube[4][2][2] = whiteCorner1

            self.cube[5][0][0] = blueCorner1
            self.cube[5][1][0] = blueEdge
            self.cube[5][2][0] = blueCorner2

            self.cube[1][0][0] = orangeCorner2
            self.cube[1][0][1] = orangeEdge3
            self.cube[1][0][2] = orangeCorner4
            self.cube[1][1][0] = orangeEdge1
            self.cube[1][1][2] = orangeEdge4
            self.cube[1][2][0] = orangeCorner1
            self.cube[1][2][1] = orangeEdge2
            self.cube[1][2][2] = orangeCorner3
        else:
            print("Invalid direction")

    def rotateGreenFace(self, direction):
        whiteCorner1 = self.cube[0][2][0]
        whiteEdge = self.cube[0][2][1]
        whiteCorner2 = self.cube[0][2][2]

        orangeCorner1 = self.cube[1][0][2]
        orangeEdge = self.cube[1][1][2]
        orangeCorner2 = self.cube[1][2][2]

        yellowCorner1 = self.cube[5][0][0]
        yellowEdge = self.cube[5][0][1]
        yellowCorner2 = self.cube[5][0][2]

        redCorner1 = self.cube[3][0][0]
        redEdge = self.cube[3][1][0]
        redCorner2 = self.cube[3][2][0]

        greenCorner1 = self.cube[2][0][0]
        greenCorner2 = self.cube[2][0][2]
        greenCorner3 = self.cube[2][2][0]
        greenCorner4 = self.cube[2][2][2]

        greenEdge1 = self.cube[2][0][1]
        greenEdge2 = self.cube[2][1][0]
        greenEdge3 = self.cube[2][1][2]
        greenEdge4 = self.cube[2][2][1]

        if direction == "clockwise":
            self.cube[0][2][0] = orangeCorner2
            self.cube[0][2][1] = orangeEdge
            self.cube[0][2][2] = orangeCorner1

            self.cube[1][0][2] = yellowCorner1
            self.cube[1][1][2] = yellowEdge
            self.cube[1][2][2] = yellowCorner2

            self.cube[5][0][0] = redCorner2
            self.cube[5][0][1] = redEdge
            self.cube[5][0][2] = redCorner1

            self.cube[3][0][0] = whiteCorner1
            self.cube[3][1][0] = whiteEdge
            self.cube[3][2][0] = whiteCorner2

            self.cube[2][0][0] = greenCorner3
            self.cube[2][0][1] = greenEdge2
            self.cube[2][0][2] = greenCorner1
            self.cube[2][1][0] = greenEdge4
            self.cube[2][1][2] = greenEdge1
            self.cube[2][2][0] = greenCorner4
            self.cube[2][2][1] = greenEdge3
            self.cube[2][2][2] = greenCorner2
        elif direction == "counterclockwise":
            self.cube[0][2][0] = redCorner1
            self.cube[0][2][1] = redEdge
            self.cube[0][2][2] = redCorner2

            self.cube[1][0][2] = whiteCorner1
            self.cube[1][1][2] = whiteEdge
            self.cube[1][2][2] = whiteCorner2

            self.cube[5][0][0] = orangeCorner1
            self.cube[5][0][1] = orangeEdge
            self.cube[5][0][2] = orangeCorner2

            self.cube[3][0][0] = yellowCorner1
            self.cube[3][1][0] = yellowEdge
            self.cube[3][2][0] = yellowCorner2

            self.cube[2][0][0] = greenCorner2
            self.cube[2][0][1] = greenEdge3
            self.cube[2][0][2] = greenCorner4
            self.cube[2][1][0] = greenEdge1
            self.cube[2][1][2] = greenEdge4
            self.cube[2][2][0] = greenCorner1
            self.cube[2][2][1] = greenEdge2
            self.cube[2][2][2] = greenCorner3
        else:
            print("Invalid direction")

    def rotateRedFace(self, direction):
        whiteCorner1 = self.cube[0][0][2]
        whiteEdge = self.cube[0][1][2]
        whiteCorner2 = self.cube[0][2][2]

        greenCorner1 = self.cube[2][0][2]
        greenEdge = self.cube[2][1][2]
        greenCorner2 = self.cube[2][2][2]

        yellowCorner1 = self.cube[5][0][2]
        yellowEdge = self.cube[5][1][2]
        yellowCorner2 = self.cube[5][2][2]

        blueCorner1 = self.cube[4][0][0]
        blueEdge = self.cube[4][1][0]
        blueCorner2 = self.cube[4][2][0]

        redCorner1 = self.cube[3][0][0]
        redCorner2 = self.cube[3][0][2]
        redCorner3 = self.cube[3][2][0]
        redCorner4 = self.cube[3][2][2]

        redEdge1 = self.cube[3][0][1]
        redEdge2 = self.cube[3][1][0]
        redEdge3 = self.cube[3][1][2]
        redEdge4 = self.cube[3][2][1]

        if direction == "clockwise":
            self.cube[0][0][2] = greenCorner1
            self.cube[0][1][2] = greenEdge
            self.cube[0][2][2] = greenCorner2

            self.cube[2][0][2] = yellowCorner1
            self.cube[2][1][2] = yellowEdge
            self.cube[2][2][2] = yellowCorner2

            self.cube[5][0][2] = blueCorner2
            self.cube[5][1][2] = blueEdge
            self.cube[5][2][2] = blueCorner1

            self.cube[4][0][0] = whiteCorner2
            self.cube[4][1][0] = whiteEdge
            self.cube[4][2][0] = whiteCorner1

            self.cube[3][0][0] = redCorner3
            self.cube[3][0][1] = redEdge2
            self.cube[3][0][2] = redCorner1
            self.cube[3][1][0] = redEdge4
            self.cube[3][1][2] = redEdge1
            self.cube[3][2][0] = redCorner4
            self.cube[3][2][1] = redEdge3
            self.cube[3][2][2] = redCorner2
        elif direction == "counterclockwise":
            self.cube[0][0][2] = blueCorner2
            self.cube[0][1][2] = blueEdge
            self.cube[0][2][2] = blueCorner1

            self.cube[2][0][2] = whiteCorner2
            self.cube[2][1][2] = whiteEdge
            self.cube[2][2][2] = whiteCorner1

            self.cube[5][0][2] = greenCorner1
            self.cube[5][1][2] = greenEdge
            self.cube[5][2][2] = greenCorner2

            self.cube[4][0][0] = yellowCorner1
            self.cube[4][1][0] = yellowEdge
            self.cube[4][2][0] = yellowCorner2

            self.cube[3][0][0] = redCorner2
            self.cube[3][0][1] = redEdge3
            self.cube[3][0][2] = redCorner4
            self.cube[3][1][0] = redEdge1
            self.cube[3][1][2] = redEdge4
            self.cube[3][2][0] = redCorner1
            self.cube[3][2][1] = redEdge2
            self.cube[3][2][2] = redCorner3
        else:
            print("Invalid direction")

    def rotateBlueFace(self, direction):
        whiteCorner1 = self.cube[0][0][0]
        whiteEdge = self.cube[0][0][1]
        whiteCorner2 = self.cube[0][0][2]

        redCorner1 = self.cube[3][0][2]
        redEdge = self.cube[3][1][2]
        redCorner2 = self.cube[3][2][2]

        yellowCorner1 = self.cube[5][2][0]
        yellowEdge = self.cube[5][2][1]
        yellowCorner2 = self.cube[5][2][2]

        orangeCorner1 = self.cube[1][0][0]
        orangeEdge = self.cube[1][1][0]
        orangeCorner2 = self.cube[1][2][0]

        blueCorner1 = self.cube[4][0][0]
        blueCorner2 = self.cube[4][0][2]
        blueCorner3 = self.cube[4][2][0]
        blueCorner4 = self.cube[4][2][2]

        blueEdge1 = self.cube[4][0][1]
        blueEdge2 = self.cube[4][1][0]
        blueEdge3 = self.cube[4][1][2]
        blueEdge4 = self.cube[4][2][1]

        if direction == "clockwise":
            self.cube[0][0][0] = redCorner1
            self.cube[0][0][1] = redEdge
            self.cube[0][0][2] = redCorner2

            self.cube[1][0][0] = whiteCorner2
            self.cube[1][1][0] = whiteEdge
            self.cube[1][2][0] = whiteCorner1

            self.cube[5][2][0] = orangeCorner1
            self.cube[5][2][1] = orangeEdge
            self.cube[5][2][2] = orangeCorner2

            self.cube[3][0][2] = yellowCorner2
            self.cube[3][1][2] = yellowEdge
            self.cube[3][2][2] = yellowCorner1

            self.cube[4][0][0] = blueCorner3
            self.cube[4][0][1] = blueEdge2
            self.cube[4][0][2] = blueCorner1
            self.cube[4][1][0] = blueEdge4
            self.cube[4][1][2] = blueEdge1
            self.cube[4][2][0] = blueCorner4
            self.cube[4][2][1] = blueEdge3
            self.cube[4][2][2] = blueCorner2
        elif direction == "counterclockwise":
            self.cube[0][0][0] = orangeCorner1
            self.cube[0][0][1] = orangeEdge
            self.cube[0][0][2] = orangeCorner2

            self.cube[1][0][0] = yellowCorner1
            self.cube[1][1][0] = yellowEdge
            self.cube[1][2][0] = yellowCorner2

            self.cube[5][2][0] = redCorner1
            self.cube[5][2][1] = redEdge
            self.cube[5][2][2] = redCorner2

            self.cube[3][0][2] = whiteCorner2
            self.cube[3][1][2] = whiteEdge
            self.cube[3][2][2] = whiteCorner1

            self.cube[4][0][0] = blueCorner1
            self.cube[4][0][1] = blueEdge4
            self.cube[4][0][2] = blueCorner3
            self.cube[4][1][0] = blueEdge1
            self.cube[4][1][2] = blueEdge2
            self.cube[4][2][0] = blueCorner2
            self.cube[4][2][1] = blueEdge3
            self.cube[4][2][2] = blueCorner4
        else:
            print("Invalid direction")

    def rotateYellowFace(self, direction):
        orangeBottomBar = self.cube[1][2]
        greenBottomBar = self.cube[2][2]
        redBottomBar = self.cube[3][2]
        blueBottomBar = self.cube[4][2]

        yellowCorner1 = self.cube[5][0][0]
        yellowCorner2 = self.cube[5][0][2]
        yellowCorner3 = self.cube[5][2][0]
        yellowCorner4 = self.cube[5][2][2]

        yellowEdge1 = self.cube[5][0][1]
        yellowEdge2 = self.cube[5][1][0]
        yellowEdge3 = self.cube[5][1][2]
        yellowEdge4 = self.cube[5][2][1]

        if direction == "clockwise":
            self.cube[1][2] = blueBottomBar
            self.cube[2][2] = orangeBottomBar
            self.cube[3][2] = greenBottomBar
            self.cube[4][2] = redBottomBar

            self.cube[5][0][0] = yellowCorner3
            self.cube[5][0][1] = yellowEdge2
            self.cube[5][0][2] = yellowCorner1
            self.cube[5][1][0] = yellowEdge4
            self.cube[5][1][2] = yellowEdge1
            self.cube[5][2][0] = yellowCorner4
            self.cube[5][2][1] = yellowEdge3
            self.cube[5][2][2] = yellowCorner2
        elif direction == "counterclockwise":
            self.cube[1][2] = greenBottomBar
            self.cube[2][2] = redBottomBar
            self.cube[3][2] = blueBottomBar
            self.cube[4][2] = orangeBottomBar

            self.cube[5][0][0] = yellowCorner2
            self.cube[5][0][1] = yellowEdge3
            self.cube[5][0][2] = yellowCorner4
            self.cube[5][1][0] = yellowEdge1
            self.cube[5][1][2] = yellowEdge4
            self.cube[5][2][0] = yellowCorner1
            self.cube[5][2][1] = yellowEdge2
            self.cube[5][2][2] = yellowCorner3
        else:
            print("Invalid direction")

class CubeGUI:
    def __init__(self, cube):
        self.cube = cube
        self.initGUI()
    
    def initGUI(self):
        self.root = Tk()
        self.root.title("Rubiks Cube")
        self.root.geometry("1200x600")
        self.root.resizable(False, False)
        self.root.configure(background="black")
        self.canvas = Canvas(self.root, width=1200, height=600, bg="black")
        self.canvas.pack()
        self.scrambleLabel = Label(self.root, text="Scramble: ", bg="black", fg="white", font=("Arial", 20))

        self.scrambleLabel.place(x=600, y=550, anchor="center")

        self.drawMovesAvailable()
        self.bindKeys()
        self.drawCube()
        self.drawScramble()
        
        self.root.mainloop()

    def bindKeys(self):
        self.root.bind("<w>", lambda x:self.rotateFace(0))
        self.root.bind("<W>", lambda x:self.rotateFace(0, "counterclockwise"))

        self.root.bind("<o>", lambda x:self.rotateFace(1))
        self.root.bind("<O>", lambda x:self.rotateFace(1, "counterclockwise"))

        self.root.bind("<g>", lambda x:self.rotateFace(2))
        self.root.bind("<G>", lambda x:self.rotateFace(2, "counterclockwise"))

        self.root.bind("<r>", lambda x:self.rotateFace(3))
        self.root.bind("<R>", lambda x:self.rotateFace(3, "counterclockwise"))

        self.root.bind("<b>", lambda x:self.rotateFace(4))
        self.root.bind("<B>", lambda x:self.rotateFace(4, "counterclockwise"))

        self.root.bind("<y>", lambda x:self.rotateFace(5))
        self.root.bind("<Y>", lambda x:self.rotateFace(5, "counterclockwise"))

        self.root.bind("<Escape>", lambda x:self.refreshCube())
        self.root.bind("<space>", lambda x:self.scrambleCube())

    def refreshCube(self):
        self.canvas.delete("all")
        self.scrambleLabel.config(text="")
        self.drawMovesAvailable()
        self.cube.resetCube()
        self.drawCube()

    def scrambleCube(self):
        cubeScrambled = self.cube.scrambleCube()
        self.canvas.delete("all")

        self.refreshCube()

        for move in cubeScrambled:
            self.rotateFace(move[0], move[1])

        self.drawMovesAvailable()
        self.drawScramble()
        self.drawCube()

    def drawMovesAvailable(self):
        self.canvas.create_text(900, 50, text="Moves Available:", fill="white", font=("Arial", 20))
        self.canvas.create_text(900, 100, text="w or Maj+w: UP", fill="white", font=("Arial", 20))
        self.canvas.create_text(900, 150, text="o or Maj+o: LEFT", fill="white", font=("Arial", 20))
        self.canvas.create_text(900, 200, text="g or Maj+g: FRONT", fill="white", font=("Arial", 20))
        self.canvas.create_text(900, 250, text="r or Maj+r: RIGHT", fill="white", font=("Arial", 20))
        self.canvas.create_text(900, 300, text="b or Maj+b: BACK", fill="white", font=("Arial", 20))
        self.canvas.create_text(900, 350, text="y or Maj+y: DOWN", fill="white", font=("Arial", 20))

    def rotateFace(self, face, direction="clockwise"):
        self.canvas.delete("all")
        self.cube.rotateFace(face, direction)
        self.drawCube()
        self.drawMovesAvailable()

    def drawCenter(self, x, y, color):
        self.canvas.create_rectangle(x, y, x+50, y+50, fill=color, outline="black", width=2)

    def drawEdge(self, x, y, color):
        self.canvas.create_rectangle(x, y, x+50, y+50, fill=color, outline="black", width=2)
        self.canvas.create_line(x, y, x+50, y+50, fill="black", width=2)
        self.canvas.create_line(x+50, y, x, y+50, fill="black", width=2)

    def drawCorner(self, x, y, color):
        self.canvas.create_rectangle(x, y, x+50, y+50, fill=color, outline="black", width=2)
        self.canvas.create_line(x+25, y, x+25, y+50, fill="black", width=2)
        self.canvas.create_line(x, y+25, x+50, y+25, fill="black", width=2)

    def drawFace(self, face):
        if face[1][1] == "white":
            self.drawCorner(275, 25, face[0][0])
            self.drawEdge(325, 25, face[0][1])
            self.drawCorner(375, 25, face[0][2])
            self.drawEdge(275, 75, face[1][0])
            self.drawCenter(325, 75, face[1][1])
            self.drawEdge(375, 75, face[1][2])
            self.drawCorner(275, 125, face[2][0])
            self.drawEdge(325, 125, face[2][1])
            self.drawCorner(375, 125, face[2][2])
        elif face[1][1] == "orange":
            self.drawCorner(125, 175, face[0][0])
            self.drawEdge(175, 175, face[0][1])
            self.drawCorner(225, 175, face[0][2])
            self.drawEdge(125, 225, face[1][0])
            self.drawCenter(175, 225, face[1][1])
            self.drawEdge(225, 225, face[1][2])
            self.drawCorner(125, 275, face[2][0])
            self.drawEdge(175, 275, face[2][1])
            self.drawCorner(225, 275, face[2][2])
        elif face[1][1] == "green":
            self.drawCorner(275, 175, face[0][0])
            self.drawEdge(325, 175, face[0][1])
            self.drawCorner(375, 175, face[0][2])
            self.drawEdge(275, 225, face[1][0])
            self.drawCenter(325, 225, face[1][1])
            self.drawEdge(375, 225, face[1][2])
            self.drawCorner(275, 275, face[2][0])
            self.drawEdge(325, 275, face[2][1])
            self.drawCorner(375, 275, face[2][2])
        elif face[1][1] == "red":
            self.drawCorner(425, 175, face[0][0])
            self.drawEdge(475, 175, face[0][1])
            self.drawCorner(525, 175, face[0][2])
            self.drawEdge(425, 225, face[1][0])
            self.drawCenter(475, 225, face[1][1])
            self.drawEdge(525, 225, face[1][2])
            self.drawCorner(425, 275, face[2][0])
            self.drawEdge(475, 275, face[2][1])
            self.drawCorner(525, 275, face[2][2])
        elif face[1][1] == "blue":
            self.drawCorner(575, 175, face[0][0])
            self.drawEdge(625, 175, face[0][1])
            self.drawCorner(675, 175, face[0][2])
            self.drawEdge(575, 225, face[1][0])
            self.drawCenter(625, 225, face[1][1])
            self.drawEdge(675, 225, face[1][2])
            self.drawCorner(575, 275, face[2][0])
            self.drawEdge(625, 275, face[2][1])
            self.drawCorner(675, 275, face[2][2])
        elif face[1][1] == "yellow":
            self.drawCorner(275, 325, face[0][0])
            self.drawEdge(325, 325, face[0][1])
            self.drawCorner(375, 325, face[0][2])
            self.drawEdge(275, 375, face[1][0])
            self.drawCenter(325, 375, face[1][1])
            self.drawEdge(375, 375, face[1][2])
            self.drawCorner(275, 425, face[2][0])
            self.drawEdge(325, 425, face[2][1])
            self.drawCorner(375, 425, face[2][2])

    def drawCube(self):
        topFace = self.cube.cube[0]
        leftFace = self.cube.cube[1]
        frontFace = self.cube.cube[2]
        rightFace = self.cube.cube[3]
        backFace = self.cube.cube[4]
        bottomFace = self.cube.cube[5]

        # the cube is drawn in the following format:
        #     WWW
        #     WWW
        #     WWW
        # OOO GGG RRR BBB
        # OOO GGG RRR BBB
        # OOO GGG RRR BBB
        #     YYY
        #     YYY
        #     YYY

        self.drawFace(topFace)
        self.drawFace(leftFace)
        self.drawFace(frontFace)
        self.drawFace(rightFace)
        self.drawFace(backFace)
        self.drawFace(bottomFace)

    def drawScramble(self):
        if len(self.cube.scrambleText) > 0:
            self.scrambleLabel.config(text=f"Scramble: {self.cube.scrambleText}")
        else:
            self.scrambleLabel.config(text="")

if __name__ == "__main__":
    # Create a cube
    cube = Cube()
    # Create the GUI
    gui = CubeGUI(cube)