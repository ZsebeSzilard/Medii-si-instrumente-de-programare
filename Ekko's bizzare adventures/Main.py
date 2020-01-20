import pygame
from pygame.locals import *
import os
import ctypes
import random

user32 = ctypes.windll.user32
screenwidth = user32.GetSystemMetrics(0)
screenheight = user32.GetSystemMetrics(1)
gamewindowwidth = 960
gamewindowheight = 540
gamewindowpositionx = int((screenwidth-gamewindowwidth)/2)
gamewindowpositiony = int((screenheight-gamewindowheight)/2)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (gamewindowpositionx, gamewindowpositiony)


class Text:
    def __init__(self, text="", pos=(0,0),fontcolor=Color('Black'),fontsize = 72,fontname=None,**options):
        self.text = text
        self.pos = pos
        self.fontcolor = fontcolor
        self.fontsize = fontsize
        self.fontname = fontname
        self.set_font()
        self.render()
    def set_font(self):
        self.font = pygame.font.Font(self.fontname, self.fontsize)
    def render(self):
        self.img = self.font.render(self.text, True, self.fontcolor)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    def draw(self):
        App.screen.blit(self.img, self.rect)


class Scene:
    id = 0
    backgroundcolor = Color('gray')
    caption = None

    def __init__(self, caption='Main Window',  backgroundcolor=Color('blue'), *args, **kwargs):
        self.backgroundcolor = backgroundcolor
        self.caption = caption
        App.scenes.append(self)
        #App.scene = self
        self.id = Scene.id
        Scene.id += 1


class HighScoreHandler:
    def GetHighScores(self):
        scores = list()
        with open("HighScores.txt") as openfileobject:
            for line in openfileobject:
                scores.append(int(line))
        return scores

    def DrawArea(self):
        areawidth=250
        areaheight=400
        pygame.draw.rect(App.screen, Color("red"), ((gamewindowwidth-areawidth)/2, (gamewindowheight-areaheight)/2, areawidth, areaheight))
        pygame.draw.rect(App.screen, Color("yellow"), ((gamewindowwidth-areawidth)/2, (gamewindowheight-areaheight)/2, areawidth, areaheight),8)


    def AddScore(self,newscore):
        newscoreslist = list()
        with open("HighScores.txt") as openfileobject:
            for line in openfileobject:
                newscoreslist.append(int(line))

        if newscore not in newscoreslist:
            newscoreslist.append(newscore)
            newscoreslist.sort(reverse=True)
            newscoreslist.remove(newscoreslist[10])
            f = open("HighScores.txt", 'w')
            for item in newscoreslist:
                f.write(str(item)+'\n')
            f.close()


class Enemy:

    def __init__(self, imagepath, size, enemytype):
        self.enemytype=enemytype
        self.image = pygame.image.load(imagepath)
        self.image = pygame.transform.scale(self.image, size)
        self.EnemyRectangle=self.image.get_rect()
        if enemytype=="Left":
            self.EnemyRectangle.x=0
            self.EnemyRectangle.y= 400
        elif enemytype=="Front":
            self.EnemyRectangle.x = 425
            self.EnemyRectangle.y = 0
        elif enemytype=="Right":
            self.EnemyRectangle.x = 730
            self.EnemyRectangle.y = 400

    def GetEnemyRectangle(self):
        return self.EnemyRectangle

    def Move(self):
        if self.enemytype == "Left":
            self.EnemyRectangle.x = self.EnemyRectangle.x+2;
        elif self.enemytype == "Front":
            self.EnemyRectangle.y = self.EnemyRectangle.y+2;
        elif self.enemytype == "Right":
            self.EnemyRectangle.x = self.EnemyRectangle.x - 2;



class GamePlay:

    def RunScene(self):
        screen = App.screen

        def ImageBlitter(imagepath, scale, rectX, rectY):
            ImageBlitter = pygame.image.load(imagepath)
            ImageBlitter = pygame.transform.scale(ImageBlitter, scale)
            ImageBlitter_rect = ImageBlitter.get_rect()
            ImageBlitter_rect.x = rectX
            ImageBlitter_rect.y = rectY
            screen.blit(ImageBlitter, ImageBlitter_rect)

        def ChangeScene():
            App.screen.fill(App.scene.backgroundcolor)
            pygame.display.set_caption(str(App.scene.caption))

        def  AddButton(positionX,positionY,width,height,color,text,textpositionX,textpositionY,fontsize,textcolor=Color("black")):
            button = pygame.Rect(positionX, positionY, width, height)
            pygame.draw.rect(App.screen,color, button)
            Text(text, pos=(textpositionX, textpositionY), fontsize=fontsize,fontcolor=textcolor).draw()
            return button

        while App.running:

            if App.scene.id==0:

                ChangeScene()

                buttonStartGame=AddButton(380, 80, 200, 65, Color('gray'),"Start Game",400, 100,40)
                buttonHowToPlay = AddButton(380, 180, 200, 65, Color('gray'),"How To Play",400, 200,40)
                buttonHightScores = AddButton(380, 280, 200, 65, Color('gray'), "High Scores", 400, 300,40)
                buttonQuitGame = AddButton(380, 380, 200, 64, Color('gray'), "Quit Game", 400, 400, 40)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        App.running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if buttonStartGame.collidepoint(event.pos):
                                App.scene=App.scenes[2]
                            elif buttonHowToPlay.collidepoint(event.pos):
                                App.scene=App.scenes[1]
                            elif buttonHightScores.collidepoint(event.pos):
                                HighScoreHandler.DrawArea(self)
                                App.scene = App.scenes[4]
                            elif buttonQuitGame.collidepoint(event.pos):
                                App.running = False

            elif App.scene.id==1:

                ChangeScene()

                Text("Use", pos=(25, 60), fontcolor=(Color("black")), fontsize=30).draw()
                ImageBlitter('Assets/Arrow Keys.png', (150, 100), 80, 25, )
                Text("to change directions:", pos=(260, 60), fontcolor=(Color("black")), fontsize=30).draw()
                ImageBlitter('Assets/Ekko Left.png', (60, 120), 600, 15 )
                ImageBlitter('Assets/Ekko Front.png', (60, 120), 700, 15 )
                ImageBlitter('Assets/Ekko Right.png', (60, 120), 800, 15 )

                Text("Press", pos=(25, 230), fontcolor=(Color("black")), fontsize=30).draw()
                ImageBlitter('Assets/Space Bar.png', (300, 50), 120, 215 )
                Text("to use ability:", pos=(450, 230), fontcolor=(Color("black")), fontsize=30).draw()
                ImageBlitter('Assets/Ekko Q.png', (90, 60), 620, 210)

                Text("Destroy the enemy minions:", pos=(25, 400), fontcolor=(Color("black")), fontsize=30).draw()
                ImageBlitter('Assets/Cannon Minion For Right.png', (100,100), 350, 365)

                buttonBack = AddButton(735, 445, 200, 65, Color('gray'), "Back", 780, 463, 50)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        App.running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if buttonBack.collidepoint(event.pos):
                                App.scene=App.scenes[0]

            elif App.scene.id==2:
                ChangeScene()



                BackGround = pygame.image.load('BackGrounds/Town.jpg')
                BackGround = pygame.transform.scale(BackGround, (gamewindowwidth,gamewindowheight))

                MainCharacterRight = pygame.image.load('Assets/Ekko Right.png')
                MainCharacterRight = pygame.transform.scale(MainCharacterRight, (63, 150))

                MainCharacterLeft = pygame.image.load('Assets/Ekko Left.png')
                MainCharacterLeft = pygame.transform.scale(MainCharacterLeft, (63, 150))

                MainCharacterFront = pygame.image.load('Assets/Ekko Front.png')
                MainCharacterFront = pygame.transform.scale(MainCharacterFront, (63, 150))
                MainCharacterHitBox = MainCharacterFront.get_rect();
                MainCharacterHitBox.x =440 # 360
                MainCharacterHitBox.y =340 # 260


                MainCharacterAbility = pygame.image.load('Assets/Ekko Q.png')
                MainCharacterAbility = pygame.transform.scale(MainCharacterAbility, (75, 50))
                MainCharacterAbilityHitBox=MainCharacterAbility.get_rect()
                MainCharacterAbilityHitBox.x = MainCharacterHitBox.x-5# 355
                MainCharacterAbilityHitBox.y = MainCharacterHitBox.y+40# 300

                HealthImage = pygame.image.load('Assets/HealthPointHearth.png')
                HealthImage = pygame.transform.scale(HealthImage, (75, 75))
                HealthImage_rect = HealthImage.get_rect()
                HealthImage_rect.x = gamewindowwidth-HealthImage_rect[2]

                initialX=MainCharacterAbilityHitBox.x
                initialY=MainCharacterAbilityHitBox.y

                directions=["Left","Front","Right"]

                characterdirection=directions[1]
                throwingdirection=directions[1]
                abilityComeback=False

                HealthPoints=3
                Score=0
                isthrowing=False
                EnemyesList=list()

                time=0

                randomNumber=0
                throwingspeed=5;
                while(HealthPoints>0):
                    screen.blit(BackGround, BackGround.get_rect())

                    Text("Score: " + str(Score), pos=(10, 10), fontsize=70, fontcolor=Color("white")).draw()

                    InitialHealthImageX=HealthImage_rect.x
                    for x in range(0, HealthPoints):
                        screen.blit(HealthImage, HealthImage_rect)
                        HealthImage_rect.x = HealthImage_rect.x - HealthImage_rect[2]
                    HealthImage_rect.x=InitialHealthImageX

                    time=time+1
                    if time%70==0:
                        time=0
                        randomNumber=random.randint(0,2)
                        if randomNumber==0:
                            newEnemy = Enemy('Assets/Cannon Minion For Left.png', size=(100, 100), enemytype="Left")
                            EnemyesList.append(newEnemy)
                        elif randomNumber==1:
                            newEnemy = Enemy('Assets/Cannon Minion For Front.png', size=(100, 100), enemytype="Front")
                            EnemyesList.append(newEnemy)
                        elif randomNumber==2:
                            newEnemy = Enemy('Assets/Cannon Minion For Right.png', size=(100, 100), enemytype="Right")
                            EnemyesList.append(newEnemy)

                    for enemy in EnemyesList:
                        enemy.Move()
                        screen.blit(enemy.image, enemy.EnemyRectangle)

                    if characterdirection==directions[0]:
                        screen.blit(MainCharacterLeft, MainCharacterLeft.get_rect().move((MainCharacterHitBox.x-15, MainCharacterHitBox.y)))
                    elif characterdirection==directions[1]:
                        screen.blit(MainCharacterFront, MainCharacterHitBox) # MainCharacterFront.get_rect().move((360, 260))
                    elif characterdirection==directions[2]:
                        screen.blit(MainCharacterRight, MainCharacterLeft.get_rect().move((MainCharacterHitBox.x+15, MainCharacterHitBox.y)))


                    for event in pygame.event.get():
                        if event.type == QUIT:
                            HealthPoints=0
                            App.running = False
                        elif event.type==KEYDOWN:

                            if event.key==K_LEFT:
                                characterdirection=directions[0]
                            elif event.key==K_UP:
                                characterdirection=directions[1]
                            elif event.key==K_DOWN:
                                characterdirection=directions[1]
                            elif event.key == K_RIGHT:
                                characterdirection = directions[2]
                            elif event.key==K_SPACE:
                                if isthrowing==False:
                                    isthrowing=True
                                    throwingdirection=characterdirection

                    if isthrowing:
                        screen.blit(MainCharacterAbility, MainCharacterAbilityHitBox)
                        if throwingdirection==directions[0]:
                            if MainCharacterAbilityHitBox.x<0:
                                abilityComeback=True
                            if abilityComeback==True:
                                MainCharacterAbilityHitBox.x=MainCharacterAbilityHitBox.x + throwingspeed
                                if MainCharacterAbilityHitBox.x>initialX:
                                    isthrowing=False
                                    abilityComeback=False
                            else:
                                MainCharacterAbilityHitBox.x = MainCharacterAbilityHitBox.x - throwingspeed
                        elif throwingdirection==directions[1]:
                            if MainCharacterAbilityHitBox.y<0:
                                abilityComeback=True
                            if abilityComeback==True:
                                MainCharacterAbilityHitBox.y=MainCharacterAbilityHitBox.y + throwingspeed
                                if MainCharacterAbilityHitBox.y>initialY:
                                    isthrowing=False
                                    abilityComeback=False
                            else:
                                MainCharacterAbilityHitBox.y = MainCharacterAbilityHitBox.y - throwingspeed
                        elif throwingdirection==directions[2]:
                            if MainCharacterAbilityHitBox.x>gamewindowwidth-MainCharacterAbilityHitBox[2]:
                                abilityComeback=True
                            if abilityComeback==True:
                                MainCharacterAbilityHitBox.x=MainCharacterAbilityHitBox.x - throwingspeed
                                if MainCharacterAbilityHitBox.x<initialX:
                                    isthrowing=False
                                    abilityComeback=False
                            else:
                                MainCharacterAbilityHitBox.x = MainCharacterAbilityHitBox.x + throwingspeed
                        for enemy in EnemyesList:
                            if MainCharacterAbilityHitBox.colliderect(enemy.EnemyRectangle):
                                EnemyesList.remove(enemy)
                                Score=Score+100
                                abilityComeback = True
                    for enemy in EnemyesList:
                        if MainCharacterHitBox.colliderect(enemy.EnemyRectangle):
                            EnemyesList.remove(enemy)
                            HealthPoints=HealthPoints-1
                    pygame.display.update()
                HighScoreHandler.AddScore(self, Score)
                App.scene = App.scenes[3]
            elif App.scene.id == 3:

                ChangeScene()
                buttonMainMenu = AddButton(25, 445, 200, 65, Color('gray'), "Main Menu", 35, 463, 50)
                buttonPlayAgain = AddButton(735, 445, 200, 65, Color('gray'), "Play Again", 745, 463, 50)
                Text("Game Over", pos=(200, 200), fontsize=150, fontcolor=Color("Black")).draw()
                Text("Your Final Score: " + str(Score), pos=(25, 25), fontsize=40, fontcolor=Color("Black")).draw()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        App.running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if buttonMainMenu.collidepoint(event.pos):
                                App.scene = App.scenes[0]
                            elif buttonPlayAgain.collidepoint(event.pos):
                                App.scene = App.scenes[2]
            elif App.scene.id == 4:
                ChangeScene()

                buttonMainMenu = AddButton(25, 445, 200, 65, Color('gray'), "Main Menu", 35, 463, 50)

                HighScoreHandler.DrawArea(self);
                HighScoreList=HighScoreHandler.GetHighScores(self)
                Text("High Scores", pos=(380,90), fontsize=50,fontcolor=Color("black")).draw()

                i=1
                firstHighscoreTextX=400
                firstHighscoreTextY=150
                distanceBetweenwrites=30
                for item in HighScoreList:
                    Text(str(i)+".  "+str(item), pos=(firstHighscoreTextX, firstHighscoreTextY), fontsize=30, fontcolor=Color("black")).draw()
                    firstHighscoreTextY=firstHighscoreTextY+distanceBetweenwrites
                    i=i+1
                    if i>9:
                        firstHighscoreTextX=389


                for event in pygame.event.get():
                    if event.type == QUIT:
                        App.running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if buttonMainMenu.collidepoint(event.pos):
                                App.scene = App.scenes[0]
            pygame.display.update()
        pygame.quit()


class App:
    scenes = list()
    scene = ""

    def __init__(self):
        pygame.init()
        App.screen = pygame.display.set_mode((gamewindowwidth, gamewindowheight))
        App.running = True

    def RunGame(self):
        GamePlay.RunScene(self)


class Demo(App):
    def __init__(self):
        super().__init__()
        Scene(backgroundcolor=Color('red'), caption='Main Menu')
        Scene(backgroundcolor=Color('green'), caption='How To Play')
        Scene(backgroundcolor=Color('blue'), caption="Ekko's bizzare adventure")
        Scene(backgroundcolor=Color('orange'), caption="Game Over")
        Scene(backgroundcolor=Color('purple'), caption="High Scores")
        App.scene = App.scenes[0]


if __name__ == '__main__':
    Demo().RunGame()
