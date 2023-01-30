from os import write, replace
from typing import Pattern, Text
import pygame,sys
import random
from PepePatterns import PatternStyles
from datetime import datetime
import babypepes as bbpp
import babypepesCanvassize as CanvasSize
import importlib


def get_canvas_dimensions():
    with open("twin_text.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if "height" in line:
            altTela = int(line.split("=")[1])
        if "width" in line:
            largTela = int(line.split("=")[1])
        if "canvas_dividend" in line:
            canvas_dividend = int(line.split("=")[1])
    #Programar aqui self.DivLarg
    divLarg = int((largTela/canvas_dividend)/2)    #int(input("Numero de lados:"))
    if divLarg <= 5:
        divLarg = 6
    divAlt = int((altTela/canvas_dividend)/2) 
    screen = pygame.display.set_mode((largTela, altTela))
    return altTela,largTela,divAlt,divLarg,screen
    
def get_final_pepecolors(number_of_colors = 6):
    FinalPepeColors = {}
    with open("twin_text.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if "FinalPepeColors" in line:
            All_Colors = eval(line.split("=")[1])
            print(f"ALLLL COLORS = {All_Colors}")
            break
    x = 0
    while x <= number_of_colors - 1:
        y = random.randrange(0,len(All_Colors))
        FinalPepeColors[x] = All_Colors[y]
        print(f"FINALPEPECOLORS = {FinalPepeColors[x]}")
        z = 0
        while z < x:
            if FinalPepeColors[x] == FinalPepeColors[z]:
                x = x - 1
                break
            z = z + 1
        x = x + 1 
    return(FinalPepeColors)
            



canIgoback = False
canIgobackintoFuture = False
gofoward = True
isdrawn = 0



altTela,largTela,divAlt,divLarg,screen = get_canvas_dimensions()
x = 0
y = 0
steps = 0
cc = 1
cr = 1
PepeQuad = [(0,0),(1,1),(2,2)]
Filletes = []
FilletesCor = []    
PatColorHolder = []
CorFundoHolder = ["#000000","#000000"]
CorPatternHolder = ["#000000","#000000"]
ShapeComandHolder = ["tt"]
ShapeComandList = ["gr","pq","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil"]#,"pepes"]
#ShapeComandSquaresList = ["c","st","gr","pq","cic","l","lp","dl","s","cp","t","tp","tgp","zz","vlp","hlp","45","lil","sqi","pepes"] ## "c","cic,"st","sqi" PATTERNS MISSING HERE
Ypoints = []
points = []

#SavePepes = []
choosePat = False

screen = pygame.display.set_mode((largTela, altTela))
RandomNum = [2,3,4,5]

ADN = []

patternEssencials = [divLarg,divAlt,largTela,altTela,screen]


FinalPepeColors = get_final_pepecolors(8)

def set_new_colors(number_of_colors = 8):
    global FinalPepeColors
    FinalPepeColors = get_final_pepecolors(number_of_colors)

AdnRegistry  = open("babypepes.py", "a+")
CanvasRegistry  = open("babypepesCanvassize.py", "a+")

SavedPepe = []

def set_ADN_to_nothing():
    global ADN
    ADN = []

class GridGenerator:    
    def __init__(self):
        self.background_colour = (255,255,255)
        self.screen = pygame.display.set_mode((largTela, altTela))
        self.name = pygame.display.set_caption('RLBB')
        self.screen.fill(self.background_colour)
        

    def draw(self):
        self.altTela,self.largTela,self.divAlt,self.divLarg,self.screen = get_canvas_dimensions()
        for y in range(self.divAlt):
            for x in range(self.divLarg):
                self.PatColor = random.choice(FinalPepeColors)
                self.imaa = pygame.draw.rect(self.screen,self.PatColor,((self.largTela/self.divLarg)*x,((self.altTela/self.divAlt)*y),self.largTela/self.divLarg,self.altTela/self.divAlt))
                x+=1
            x=0
            y+=1
        #pygame.display.flip()           

class PepeAI:
    def __init__(self):
        self.GetColors()
        self.GetPatternShape()

    def GetColors(self):
        self.pepeCores = FinalPepeColors
        self.colorFundo = random.choice(self.pepeCores)
        self.colorPattern = random.choice(self.pepeCores)

        #print("FUNDO COLOR HOLDER =", CorFundoHolder[-1],"NEW FUNDO COLOR =",self.colorFundo,"OLD PATTERN COLOR =",CorPatternHolder[-1],"NEW PATTERN COLOR",self.colorPattern )

        while self.colorPattern == self.colorFundo: # or self.colorPattern == CorPatternHolder[-1]:# or self.colorFundo == CorFundoHolder[-1] or self.colorFundo == CorPatternHolder[-1] or self.colorPattern == CorFundoHolder[-1]:
            self.colorPattern = random.choice(self.pepeCores)
            self.colorFundo = random.choice(self.pepeCores)
        #    #print("REPEAT MODE ACTIVATED : FUNDO COLOR HOLDER =", CorFundoHolder[-1],"NEW FUNDO COLOR =",self.colorFundo,"OLD PATTERN COLOR =",CorPatternHolder[-1],"NEW PATTERN COLOR",self.colorPattern )
        #        
        #CorFundoHolder.append(self.colorFundo)
        #CorPatternHolder.append(self.colorPattern)
            
    def GetPatternShape(self):
        
        self.ShapeComand = random.choice(ShapeComandList)
        while self.ShapeComand == ShapeComandHolder[-1]:
            self.ShapeComand = random.choice(ShapeComandList)
        
        

class PepeDrawer:
    def __init__(self,CorFundo,CorPattern,PepeQuad1,PepeQuad2,ShapeComand):
        self.CorFundo = CorFundo
        self.CorPattern = CorPattern
        self.FirstX,self.FirstY = PepeQuad1
        self.SecX,self.SecY = PepeQuad2
        self.ShapeComand = ShapeComand      
        
        ###################
        
        self.altTela,self.largTela,self.divAlt,self.divLarg,self.screen = get_canvas_dimensions()

    #### DRAWS FUNDOS    
    def startbyFilette(self):        
        if self.SecX < self.FirstX:
            self.SizeX = (self.FirstX - self.SecX) 
            self.FirstX = self.SecX
          
        else:
            self.SizeX = (self.SecX - self.FirstX) 
          
        if self.SecY < self.FirstY:
            self.SizeY = (self.FirstY - self.SecY) 
            self.FirstY = self.SecY
        
        else:
            self.SizeY = (self.SecY - self.FirstY)     
            
        self.RealDirectionX = self.SizeX * (self.largTela/self.divLarg)
        self.RealDirectionY = self.SizeY * (self.altTela/self.divAlt)

        ### Transforms Square Fillettes Patterns in circles and Stairs
        #if self.SizeX == self.SizeY and choosePat == False:
        #    self.ShapeComand = random.choice(ShapeComandSquaresList)
        #    while self.ShapeComand == ShapeComandHolder[-1]:
        #        self.ShapeComand = random.choice(ShapeComandSquaresList)
        Filletes.append((self.FirstX,self.FirstY,self.RealDirectionX,self.RealDirectionY))

        pygame.draw.rect(screen,self.CorFundo,((self.largTela/self.divLarg)*self.FirstX,((self.altTela/self.divAlt)*self.FirstY),self.RealDirectionX,self.RealDirectionY))
        self.DrawPattern()
        pygame.display.flip()



    ####READS SHAPECOMAND AND DRAWS PATTERNS

    def DrawPattern(self):
        patternEssencials = []
        patternEssencials = [self.divLarg,self.divAlt,self.largTela,self.altTela,screen]
        patrao = PatternStyles(self.CorFundo,self.CorPattern,Filletes,patternEssencials,(self.FirstX,self.FirstY),(self.SecX,self.SecY))
        if self.ShapeComand == "c":
            patrao.MakesCirclesOnFillete()      
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        #elif self.ShapeComand == "pepes":
        #    patrao.pepesAiSignature(FinalPepeColors)    
        #    #pygame.display.flip()
        #    ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "cic":
            patrao.MakesCirclesinCirclesOnFillete()    
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "cp":
            patrao.MakesCirclesPatternOnFillete(self.CorPattern)     
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "t":
            patrao.MakesTriangleOnFillete(self.CorPattern)               
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "tp":
            patrao.MakesTrianglePatternOnFillete()         
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "vlp":
            patrao.MakesVerticalLinePatternOnFillete()     
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "hlp":
            patrao.MakesHorizontalLinePatternOnFillete()   
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "pq":
            patrao.MakesPatternQuadradosOnFillete()        
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "st":
            patrao.MakesStairsonFillete()                  
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "gr":
            patrao.MakesGridonFillete()                  
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "sqi":
            patrao.MakeSquaresInsideSquares()               
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "lil":
            patrao.MakesLosangleInsideLosangle()                
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "l":
            patrao.MakesLosangleFillete()                  
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "lp":
            patrao.MakesLosanglePatternFillete()                  
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "s":                    
            patrao.MakeSetas()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "tgp":                    
            patrao.MakesTriangleGridPatternFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "dl":                    
            patrao.MakesDistortLosanglesPatternFillete()
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "45":
            patrao.Makes45gLinesPatternFillete()                    
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        elif self.ShapeComand == "zz":
            patrao.MakesZigZagPatternFillete()                    
            #pygame.display.flip()
            ShapeComandHolder.append(self.ShapeComand)
        else:
            print("You did nothing BITCH")

    


def check_for_touching_colors(self,ADN,NewPepe,a,y,NewNum):
    print("Checking for color in here !!!!")
    tester_i = 0
    ll = len(ADN)
    touched_colors = []
    while tester_i < ll:
        cor_cobaia, cor2_cobaia, (x1,y1), (x2, y2), pattern_cobaia = ADN[tester_i]
        if (x2 == self.Xpoints[a-1] and (y1 <= y < y2 or y1 < y+NewNum <= y2)) or tester_i == ll - 1:# and (cor_cobaia == NewPepe.colorFundo or cor_cobaia == NewPepe.colorPattern or cor2_cobaia == NewPepe.colorFundo or cor2_cobaia == NewPepe.colorPattern)) or (tester_i == ll - 1 and (cor_cobaia == NewPepe.colorFundo or cor_cobaia == NewPepe.colorPattern or cor2_cobaia == NewPepe.colorFundo or cor2_cobaia == NewPepe.colorPattern)):
            touched_colors.append((cor_cobaia,cor2_cobaia,pattern_cobaia))
            #touched_colors.append(cor2_cobaia)
        tester_i = tester_i + 1
    nbr_touched_colors = len(touched_colors)
    t = 0
    while t < nbr_touched_colors:
        if NewPepe.colorFundo == touched_colors[t][0] or NewPepe.colorFundo == touched_colors[t][1] or NewPepe.colorPattern == touched_colors[t][0] or NewPepe.colorPattern == touched_colors[t][1] or NewPepe.ShapeComand == touched_colors[t][2]:
            print(f"RECOLORING:::: {NewPepe.ShapeComand} = {pattern_cobaia}")
            NewPepe = PepeAI()   
            t = 0
        else:
            t = t + 1
    return(NewPepe)

class StartPepeFunction:
    def __init__(self):
        self.Xpoints = [] 
        set_ADN_to_nothing()
        
        self.altTela,self.largTela,self.divAlt,self.divLarg,self.screen = get_canvas_dimensions()
        
        self.start()
        
    def start(self):
        x = 0
        while x < self.divLarg:
            self.Xpoints.append(x)
            NewNum = random.choice(RandomNum) ### PEPESAI COULD MESS AROUND HERE
            x = x + NewNum
        self.Xpoints.append(self.divLarg) # adds last point of grid
        self.rowNumber = len(self.Xpoints)
        
        a = 0
        while a < self.rowNumber-1:
            a = a + 1
            self.Ypoints = []
            y = 0
            while y < self.divAlt:
                self.Ypoints.append(y)
                #pygame.display.flip
                NewNum = random.choice(RandomNum) ### PEPESAI COULD MESS AROUND HERE
                if y + NewNum > self.divAlt:   ### condition for not going out of the canvas in y direction
                    NewNum = self.divAlt - y
                NewPepe = PepeAI()
                NewPepe = check_for_touching_colors(self,ADN,NewPepe,a,y,NewNum)
                newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),NewPepe.ShapeComand)
                newPepitos.startbyFilette()
                ADN.append((NewPepe.colorFundo,NewPepe.colorPattern,(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum),newPepitos.ShapeComand))
                ### Save Here The Pepe Reference Coordinates
                ###
                y = y + NewNum
            print(self.Xpoints,self.Ypoints)
            

class ClicktoChangePP:
    def __init__(self,x,y):
        self.x,self.y = x,y
        
        self.altTela,self.largTela,self.divAlt,self.divLarg,self.screen = get_canvas_dimensions()
        
        NewX = self.divLarg
        for cc in range(self.divLarg):
            if self.x - (self.largTela/self.divLarg) <= (self.largTela/self.divLarg) * cc: 
                #print("point x:",cc)
                NewX -= 1

        NewY = self.divAlt
        for cr in range(self.divAlt):
            if self.y - (self.altTela/self.divAlt) <= (self.altTela/self.divAlt) * cr: 
                #print("point y:",cr)
                NewY -= 1
        print("this is your click coordinates :",NewX,NewY)


        shitter = 0
        shitterTimes = len(ADN)
        while shitter < shitterTimes:
            newPoints = ADN[shitter]
            newCorF,newCorP,(newPointX,newPointY),(SecnewPointX,SecnewPointY),newShapC = ADN[shitter]
            if newPointX <= NewX < SecnewPointX and newPointY <= NewY < SecnewPointY:
                self.DrawPattern(newPointX,newPointY,SecnewPointX,SecnewPointY,shitter)
                break
            shitter += 1
    
    def DrawPattern(self,newPointX,newPointY,SecnewPointX,SecnewPointY,shitter):
        NewPepe = PepeAI()
        if choosePat == False:   
            newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),NewPepe.ShapeComand)
            newPepitos.startbyFilette()
            ADN[shitter] = NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),newPepitos.ShapeComand

        elif choosePat == True:
            ShapeComand = input("Choose the Pattern of your desire:\nc   for Circle\ncic for Circles Inside Circles\nl   for Losangle\nlp  for Losangle Pattern\ndl  for Distort Losangle Pattern\ngr  for Grid Pattern\ns   for Setas\ncp  for Circle Pattern\nst  for Stairs\nt   for Triangle\npq  for Quadrados Pattern\ntp  for Triangle Pattern\ntgp for Triangle Grid Pattern\nzz  for Zig Zag Triangles Pattern\nvlp for Vertical Lines Pattern\nhlp for Horizontal Lines Pattern\n45  for 45 degrees Lines Pattern\nsqi for SquaresInsideSquares\nlil for Losangles Inside Losangles\n   ")
            newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),ShapeComand)
            newPepitos.startbyFilette()
            ADN[shitter] = NewPepe.colorFundo,NewPepe.colorPattern,(newPointX,newPointY),(SecnewPointX,SecnewPointY),newPepitos.ShapeComand






def check_for_touching_colors_in_recolor(nX,ADN,NewPepe,nY,sY,x):
    print("AHAHHAHAHHAHAHAHAHAHAHHAHAHAHAHAHAHAHAHHAHAHA !!!!")
    tester_i = 0
    ll = len(ADN)
    touched_colors = []
    while tester_i < ll:
        cor_cobaia, cor2_cobaia, (x1,y1), (x2, y2), pattern_cobaia = ADN[tester_i]
        if (x2 == nX and (y1 <= nY < y2 or y1 < sY <= y2)) or tester_i == x - 1:# and (cor_cobaia == NewPepe.colorFundo or cor_cobaia == NewPepe.colorPattern or cor2_cobaia == NewPepe.colorFundo or cor2_cobaia == NewPepe.colorPattern)) or (tester_i == ll - 1 and (cor_cobaia == NewPepe.colorFundo or cor_cobaia == NewPepe.colorPattern or cor2_cobaia == NewPepe.colorFundo or cor2_cobaia == NewPepe.colorPattern)):
            touched_colors.append((cor_cobaia,cor2_cobaia,pattern_cobaia))
            print(f"I Appended : {touched_colors}")
            #touched_colors.append(cor2_cobaia)
        tester_i = tester_i + 1
    nbr_touched_colors = len(touched_colors)
    t = 0
    while t < nbr_touched_colors:
        if NewPepe.colorFundo == touched_colors[t][0] or NewPepe.colorFundo == touched_colors[t][1] or NewPepe.colorPattern == touched_colors[t][0] or NewPepe.colorPattern == touched_colors[t][1] or NewPepe.ShapeComand == touched_colors[t][2]:
            print(f"RECOLORING:::: {NewPepe.ShapeComand} = {pattern_cobaia}")
            NewPepe = PepeAI()   
            t = 0
        else:
            t = t + 1
    return(NewPepe)
    

class ADNprocessor:
    def __init__(self):
        print("You iniciated The Adn Processor:")

    def rewindOnePepe(self, lastPepeAdn):
        print("YOUAREHERE:")

        x = 0
        while x < len(lastPepeAdn):
                    newCorF,newCorP,(nX,nY),(sX,sY),newShapC = lastPepeAdn[x]
                    newPepitos = PepeDrawer(newCorF,newCorP,(nX,nY),(sX,sY),newShapC)
                    newPepitos.startbyFilette()
                    x += 1


    def colorChangeReverse():
        
        x = len(ADN) - 1
        while x >= 0:
            NewPepe = PepeAI()
            newCorF,newCorP,(nX,nY),(sX,sY),newShapC = ADN[x]
            newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(nX,nY),(sX,sY),newShapC)
            newPepitos.startbyFilette()
            x -= 1
            
    def colorChanger():
        x = 0
        while x < len(ADN):
            NewPepe = PepeAI()
            newCorF,newCorP,(nX,nY),(sX,sY),newShapC = ADN[x]
            NewPepe = check_for_touching_colors_in_recolor(nX,ADN,NewPepe,nY,sY,x)
            newPepitos = PepeDrawer(NewPepe.colorFundo,NewPepe.colorPattern,(nX,nY),(sX,sY),newShapC)
            ADN[x] = (NewPepe.colorFundo,NewPepe.colorPattern,(nX,nY),(sX,sY),newShapC)
            newPepitos.startbyFilette()
            x += 1



    def callSavedPepes(self):
        self.printSavedPepes()
        calledPepe = input("Who do Want to Call???")

        ## DRAWS SAVED CANVAS SIZE
        importlib.reload(CanvasSize)
        with open('babypepesCanvassize.py') as cs:
            if calledPepe in cs.read():
                loadCanvasSize = CanvasSize.savedPepesCanvas
                global largTela, altTela, divLarg, divAlt
                largTela, altTela, divLarg, divAlt = loadCanvasSize.get(calledPepe)
                redrawCanvas = GridGenerator()
                redrawCanvas.draw()
            else:
                print("This shit never existed before")


        ## DRAWS SAVED PEPE            
        importlib.reload(bbpp)
        with open('babypepes.py') as f:
            if calledPepe in f.read():
                newPepeLst = bbpp.savedPepes
                newAdn = newPepeLst.get(calledPepe)    
                global ADN 
                ADN = newPepeLst.get(calledPepe)
                x = 0
                while x < len(newAdn):
                    newCorF,newCorP,(nX,nY),(sX,sY),newShapC = newAdn[x]
                    newPepitos = PepeDrawer(newCorF,newCorP,(nX,nY),(sX,sY),newShapC)
                    newPepitos.startbyFilette()
                    x += 1
            else:
                print("This shit never existed before")


    def printSavedPepes(self):
        #CanvasRegistry = open("babypepesCanvassize.py", "r")
        SavedPepes = CanvasSize.savedPepesCanvas
        for x in SavedPepes:
          #stripped_line = line.strip()
          print(x)
        CanvasRegistry.close()
    




            




   
   
            
### KEYBOARD INTERACTION COMMANDS FOR FRONTRUNNING THE MACHINE ::::        

        
#grid = GridGenerator()
#running = True
#while running:
#  for event in pygame.event.get():
#    if event.type == pygame.QUIT:
#      print(steps,"steps")
#      running = False
#      
#
#
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
#        ADN = []
#        grid.draw()
#        canIgoback = True
#        if gofoward == False:
#            if isdrawn >= 0 and isdrawn < 4:
#                isdrawn += 1
#            else :
#                isdrawn == 0 
#        gofoward = True
#        
#        if isdrawn == 0:
#            new0 = StartPepeFunction()
#            new00 = ADN
#            del new0
#            
#            print("you print in :")
#            print(isdrawn)
#            
#            isdrawn = 1
#            
#            print("you leave in :")
#            print(isdrawn)
#
#      
#
#    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#        x,y = pygame.mouse.get_pos()    
#        newPepePattern = ClicktoChangePP(x,y)
#    
#    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
#        choosePat = True
#        x,y = pygame.mouse.get_pos()    
#        newPepePattern = ClicktoChangePP(x,y)
#        choosePat = False
#
#    # Rewind button in R
#    # NOT WORKING YET    
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
#        choosePat = True
#        if gofoward == True:
#            #gofoward = False
#            if isdrawn > 0 and isdrawn <= 4:
#                isdrawn -= 1
#            else :
#                isdrawn == 4
#        if canIgoback == True:
#            if isdrawn == 0 and canIgobackintoFuture == True:
#                ADN = []
#                ADN = new44
#                Call00 = ADNprocessor()
#                Call00.rewindOnePepe(new44)
#                del Call00
#                
#                print("you print in :")
#                print(isdrawn)
#                
#                isdrawn = 4
#
#                print("you leave in :")
#                print(isdrawn)
#
#            
#        choosePat = False
#
#    # elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
#
#
#
#    # Changes IMAGE COLORS with the Adn Processor
#
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
#        choosePat = True
#        adnProcess = ADNprocessor()
#        adnProcess.colorChanger()
#        choosePat = False
#
#    # Calls Saved Pepe
#
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_o:
#        choosePat = True
#        adnProcess = ADNprocessor()
#        adnProcess.callSavedPepes()
#        choosePat = False
#
#
#    #Saves a Pepe as PNG and as Genome
#    
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
#
#        babyPepeName = input("Write Your Baby Pepe Name:")
#        #TimeStamp = str(datetime.now())[:19]
#        #TimeStampuse = list(TimeStamp)
#        #TimeStampuse[16] = "m"
#        #TimeStampuse[13] = "h"
#        #PrintTimeStamp = "".join(TimeStampuse)
#        
#                        ###### FIND A WAY TO DUMP ALLSAVED PEPES IN TERMINAL ????
#        ## Escreve a Canvas Size de cada BabyPepe na sua pagina apropriada
#        CanvasRegistry = open("babypepesCanvassize.py", "r")
#
#        new_file_content = ""
#        for line in CanvasRegistry:
#          stripped_line = line.strip()
#          new_line = stripped_line.replace("}", " ")
#          new_file_content += new_line +"\n"
#        CanvasRegistry.close()
#
#        CanvasRegistry = open("babypepesCanvassize.py", "w")
#        CanvasRegistry.write(new_file_content)
#        canvaSize = (largTela,altTela,divLarg,divAlt)
#        CanvasRegistry.write(",'")
#        CanvasRegistry.write(babyPepeName)
#        CanvasRegistry.write("'")
#        CanvasRegistry.write(" : ")
#        CanvasRegistry.write(str(canvaSize))
#        CanvasRegistry.write("}")
#        CanvasRegistry.close()
#
#
#        ## Escreve o ADN de cada BabyPepe na sua pagina apropriada
#        AdnRegistry = open("babypepes.py", "r")
#
#        new_file_content = ""
#        for line in AdnRegistry:
#          stripped_line = line.strip()
#          new_line = stripped_line.replace("}", " ")
#          new_file_content += new_line +"\n"
#        AdnRegistry.close()
#
#        AdnRegistry = open("babypepes.py", "w")
#        AdnRegistry.write(new_file_content)
#
#        AdnRegistry.write(",'")
#        AdnRegistry.write(babyPepeName)
#        AdnRegistry.write("'")
#        AdnRegistry.write(" : ")
#        AdnRegistry.write(str(ADN))
#        AdnRegistry.write("}")
#        AdnRegistry.close()
#      
#        SavedPepe = ADN
#        realName = "BabyPepe (" + babyPepeName + ").png"
#        pygame.image.save(screen , realName)
#        print("You just created a jpg with your Pepe in your local directory named :", realName)
#    
#    
#    # Spacebar to redraw squares
#
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
#        grid.draw()
#       
#    # Press Arrows for controlling divisions number
#
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
#        divLarg -= 1
#        if divLarg <=5:
#            divLarg = 6
#        grid.draw()
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
#        divLarg += 1
#        grid.draw()
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
#        divAlt -= 1
#        if divAlt <= 3:
#            divAlt = 4
#        grid.draw()
#    elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
#        divAlt += 1
#        grid.draw()
#
#
#
#
#
#
#
#
#
########
# CRIAR UM GUI
#   - 1 BOTAO PARA INICIALIZAR PYGAME
#   - 2 CAIXAS PARA INSERIR MEDIDAS DA PAREDE
#   - 2 CONTADORES PARA NUMERO DE DIVLARG E DIVALT
#   - 1 CONTADOR PARA NUMERO DE CORES
#       - ARRANJAR UM DISPLAY INTERACTIVO
#       - COLOR PICKER




# ###############
#                 #CHECK FOR SAME COLORS IN LINES
#                 tester_i = 0
#                 ll = len(ADN)
#                 while tester_i < ll:
#                     cor_cobaia, cor2_cobaia, (x1,y1), (x2, y2), pattern_cobaia = ADN[tester_i]
#                     if (x2 == self.Xpoints[a-1] and (y1 <= y < y2 or y1 < y+NewNum <= y2) and (cor_cobaia == NewPepe.colorFundo or cor_cobaia == NewPepe.colorPattern or cor2_cobaia == NewPepe.colorFundo or cor2_cobaia == NewPepe.colorPattern)) or (tester_i == ll - 1 and (cor_cobaia == NewPepe.colorFundo or cor_cobaia == NewPepe.colorPattern or cor2_cobaia == NewPepe.colorFundo or cor2_cobaia == NewPepe.colorPattern)):
#                         while cor_cobaia == NewPepe.colorFundo or cor_cobaia == NewPepe.colorPattern or cor2_cobaia == NewPepe.colorFundo or cor2_cobaia == NewPepe.colorPattern:
#                             print(f"RecoloringOG {(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum)} : {NewPepe.colorFundo}, {NewPepe.colorPattern}------- {(x1,y1),(x2,y2)} {cor_cobaia,cor2_cobaia} ")
#                             NewPepe = PepeAI()
#                             print(f"RecoloringOG {(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum)} : {NewPepe.colorFundo}, {NewPepe.colorPattern}------- {(x1,y1),(x2,y2)} {cor_cobaia,cor2_cobaia} ")
#                         print(f"FINAL_OGOG {(self.Xpoints[a-1],y),(self.Xpoints[a],y+NewNum)} : {NewPepe.colorFundo}, {NewPepe.colorPattern}------- {(x1,y1),(x2,y2)} {cor_cobaia,cor2_cobaia} ")
#                     tester_i = tester_i + 1
                    
#                 ###############