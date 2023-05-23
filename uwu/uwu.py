as# Importing libraries and initializing Pygame
# PS. I accept funding for further development of the game :)
# All credits are in the game
from operator import truediv
from os import kill
import pygame
import time
import random
from pygamefuncts import button, quit_game, text_set
from classes import Player, PlayerBullet, En
import math
# Obtained from Lucien Dao
sprite = pygame.image.load("sprite left.png")
# Constants following enemy
VELOCITY         = 1
LERP_FACTOR      = 0.05
minimum_distance = 0
maximum_distance = 1000
# start pygame and color variables
pygame.init()
black = (0,0,0)
white = (255,255,255)
yellow = (233,196,106)
orange = (244,162,97)
red = (231,111,81)
turq = (175,238,238)
navy = (38,70,83)
sky = (135,206,250)
fc = (42,157,143)
pred = (231,111,81)
# dictionary of all character values
teachers = {"Taposhi": {'HP': 75, 'Attack': 8, 'Speed': 2, 'Exp': 0, 'Cri': 30, 'img': 'gametpspxl.png', 'bimg': 'tpsbullet.png'}, "Bettina": {"HP": 65, "Attack": 10, "Speed": 2.3, "Exp": 0, "Cri": 15, 'img': 'gamebtnpxl.png', 'bimg': 'btnbullet.png'}}

# Storing display width and height in variables to use later
display_width = 800
display_height = 600
camera_group = pygame.sprite.Group()
x, y = display_width/2, display_height/2

# Set up and initialize display width and height
gameDisplay = pygame.display.set_mode((display_width,display_height))
# Set window name (or caption if you call it)
pygame.display.set_caption('UWU')
clock = pygame.time.Clock()
def game_intro():
    # define intro to be true until red X button for close is clicked
    intro = True
    # run program until click close window
    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # fill display with white        
        gameDisplay.fill(navy)
        # set up font text
        text_set("UWU", 80, orange, display_width/2,150)
        # set up a button with our amazing button function
        pygame.draw.rect(gameDisplay, white, (345,245,120,60))
        pygame.draw.rect(gameDisplay, white, (345,320,120,60))
        pygame.draw.rect(gameDisplay, white, (345,395,120,60))
        pygame.draw.rect(gameDisplay, white, (345,470,120,60))
        button("Play",350,250,110,50,fc,pred,white,char_choose)
        button("Tutorial",350,325,110,50,fc,pred,white,tutorial)
        button("Credits",350,400,110,50,fc,pred,white,credit)
        button("Quit",350,475,110,50,fc,pred,white,quit_game)
        # decoration
        pygame.draw.circle(gameDisplay, pred, (200, 200), 75)
        pygame.draw.circle(gameDisplay, pred, (600, 200), 75)
        # frame update
        pygame.display.update()
        clock.tick(15)
def credit():
    c = True
    gameDisplay.fill(navy)
    # while running credit
    while c:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
        # buttons and credit texts
        pygame.draw.rect(gameDisplay, white, (15,15,60,40))
        button('<',20,20,50,30,fc,pred,white,game_intro)
        text_set("Credits", 32, yellow, 100, 100)
        text_set("Inspiration: HoloCure", 24, orange, 170, 160)
        text_set("Enemy Following Function: Rabbid76v- StackOverflow", 24, orange, 389, 200)
        text_set("Player Bullet Idea: ScriptLineStudio - GitHub", 24, orange, 331, 240)
        text_set("Enemy Design: Lucien Dao", 24, orange, 198, 280)
        text_set("Character Design: Me", 24, orange, 174, 320)
        text_set("Music: Me", 24, orange, 91, 360)
        text_set("Graphic/Color: Me", 24, orange, 149, 400)
        text_set("Basically Everything Else: Me", 24, orange, 225, 440)
        pygame.display.update()
        clock.tick(15)
def tutorial():
    t = True
    gameDisplay.fill(navy)
    # while running tutorial
    while t:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
        # buttons and tutorial texts
        pygame.draw.rect(gameDisplay, white, (15,15,60,40))
        button('<',20,20,50,30,fc,pred,white,game_intro)
        text_set("How to play?", 24, orange, 150, 100)
        text_set("1. Kill. The more you kill, the harder the game gets", 20, yellow, 365, 160)
        text_set("2. Dodge the characters and shoot them", 20, yellow, 315, 190)
        text_set("Controls", 24, orange, 125, 250)
        text_set("1. The bullet shoots the direction you turn", 20, yellow, 329, 310)
        text_set("2. Click the mouse to shoot a bullet", 20, yellow, 281, 340)
        text_set("3. ESC for pause", 20, yellow, 172, 370)
        text_set("4. WASD for movement", 20, yellow, 203, 400)
        pygame.display.update()
        clock.tick(15)
def paused():
    global pause
    # fill
    gameDisplay.fill(navy)
    # set up text font and size
    text_set("Paused", 100, fc, (display_width/2),(display_height/2))
    
    # while pause is true
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
        
        # show the two buttons
        pygame.draw.rect(gameDisplay, white, (145,445,135,60))
        pygame.draw.rect(gameDisplay, white, (545,445,135,60))
        button("Continue",150,450,125,50,fc,pred,white,unpause)
        button("Quit",550,450,125,50,fc,pred,white,quit_game)
        # update frames and fps
        pygame.display.update()
        clock.tick(15)
def crash():
    # establish values used in other functions
    global player
    global crashed
    global kill
    # fill
    pygame.mixer.music.stop()
    gameDisplay.fill(navy)
    # set up text font and size
    text_set("GAME OVER", 100, fc, (display_width/2),(display_height*0.35))
    
    # while pause is true
    while crashed:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()    
        
        # show the two buttons and player stats
        pygame.draw.rect(gameDisplay, white, (145,445,135,60))
        pygame.draw.rect(gameDisplay, white, (545,445,135,60))
        text_set(f"Total Kill: {kill}", 24, fc, display_width/2, 300)
        text_set(f"Total Level: {player.wlevel}", 24, fc, display_width/2, 350)
        button("Restart",150,450,125,50,fc,pred,white,game_loop)
        button("Quit",550,450,125,50,fc,pred,white,quit_game)
        # update frames and fps
        pygame.display.update()
        clock.tick(15)
# unpause function
def unpause():
    global pause
    pause = False
# small function for choosing characters
def char1():
    global choose
    choose = 1
    game_loop()
def char2():
    global choose
    choose = 2
    game_loop()
# show character stats and preview image
def preview1():
    player = Player("Taposhi",teachers,x,y)
    pygame.draw.rect(gameDisplay, fc, (50,400,150,150))
    text_set(f"Name: {player.name}", 16, yellow, 300, 410)
    text_set(f"HP: {player.HP}", 16, yellow, 261, 440)
    text_set(f"Attack: {player.Attack}", 16, yellow, 284, 470)
    text_set(f"Speed: {player.speed}", 16, yellow, 273, 500)
    text_set(f"Critical: {player.crit_chance}", 16, yellow, 286, 530)
    char1img = pygame.image.load('taposhipxl.png')
    gameDisplay.blit(char1img, (-20,350))
# show character stats and preview image
def preview2():
    player = Player("Bettina",teachers,x,y)
    pygame.draw.rect(gameDisplay, fc, (50,400,150,150))
    text_set(f"Name: {player.name}", 16, yellow, 300, 410)
    text_set(f"HP: {player.HP}", 16, yellow, 261, 440)
    text_set(f"Attack: {player.Attack}", 16, yellow, 284, 470)
    text_set(f"Speed: {player.speed}", 16, yellow, 280, 500)
    text_set(f"Critical: {player.crit_chance}", 16, yellow, 286, 530)
    char1img = pygame.image.load('bettinapxl.png')
    gameDisplay.blit(char1img, (-25,350))
# choosing character page
def char_choose():
    ch_choose = True
    while ch_choose:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # fill display with white        
        gameDisplay.fill(navy)
        # set up font text
        # buttons for choosing chaarcters and some decorations
        text_set("Choose your character", 32, orange, display_width/2, 100)
        pygame.draw.rect(gameDisplay, white, (15,15,60,40))
        pygame.draw.rect(gameDisplay, white, (220,140,150,150))
        pygame.draw.rect(gameDisplay, white, (410,140,150,150))
        button('<',20,20,50,30,fc,pred,white,game_intro)
        button('',225,145,140,140,fc,pred,white,char1,preview1)
        button('',415,145,140,140,fc,pred,white,char2,preview2)
        char1img = pygame.image.load('taposhipxl.png')
        gameDisplay.blit(char1img, (150,100))
        char2img = pygame.image.load('bettinapxl.png')
        gameDisplay.blit(char2img, (330,100))
        text_set("Taposhi", 24, orange, 295, 315)
        text_set("Bettina", 24, orange, 490, 315)
        pygame.display.update()
        clock.tick(15)
# main game loop
pygame.event.set_grab(True)
def game_loop():
    global kill
    global player
    # random ghost spawn point
    # get initial time
    previous_time = pygame.time.get_ticks()
    i1 = random.randint(5,795)
    i2 = random.randint(5,595)
    follower = (i1, i2)
    j1 = random.randint(5,795)
    j2 = random.randint(5,595)
    follower2 = (j1, j2)
    k1 = random.randint(5,795)
    k2 = random.randint(5,595)
    follower3 = (k1, k2)
    run = True
    # initial player spawn point and coordinate changes
    x = (720 * 0.5)
    y = (540 * 0.5)
    x_change = 0
    y_change = 0
    # initialize character and get speed values
    if choose == 1:
        character = "Taposhi"
    if choose == 2:
        character = "Bettina"
    speed = teachers[character]['Speed']
    # bullet list for keeping track of bullets
    player_bullets = []
    # time chunk before bullet can be shoot again and enemy can spawn again. (milliseconds)
    time_btw = 800
    time_btw2 = 200
    # keeping track of kill numbers
    kill = 0
    # constants
    c = 4
    a = 0
    # initialize player class
    player = Player(character, teachers, display_width/2, display_height/2)
    # initialize enemy player class
    enemy1 = En(player)
    enemy2 = En(player)
    enemy3 = En(player)
    # sprite flip while walking a certain direction initialized
    flip = False
    # music play
    pygame.mixer.music.load('8bit.mp3')
    pygame.mixer.music.play(-1)
    # while the game is running
    while run:
        # establish some variables
        global VELOCITY
        global pause
        global crashed
        pause = False
        crashed = False
        # frame per seconds
        clock.tick(60)
        # get mouse coordinates
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # initiate bullets
        bullet = PlayerBullet(x, y, mouse_x, mouse_y, a)
        for event in pygame.event.get():
            # if mouse is clicked then shoot bullet (append to list)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_bullets.append(bullet)
            # quit if x button is pressed
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            # moving around, change coordinates when certain key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
                if event.key == pygame.K_a:
                    x_change = -1*speed
                    # shooting angle
                    a = 0
                    # flip sprite walking image
                    flip = True
                if event.key == pygame.K_d:
                    x_change =  1*speed
                    a = math.pi
                    flip = False
                if event.key == pygame.K_w:
                    y_change =  -1*speed
                    a = math.pi/2
                    flip = False
                if event.key == pygame.K_s:
                    y_change =  1*speed
                    a = 3*math.pi/2
                    flip = False
            if event.type == pygame.KEYUP:
                # if key is not pressed then character doesnt move
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        x_change = 0
                    if event.key == pygame.K_s or event.key == pygame.K_w:
                        y_change = 0
        # player position change
        x += x_change
        y += y_change
        # player coordinates
        playerc  = (x, y)
        # make enemy follor the player coordinate above with the function
        follower = enemy1.Enemy(playerc, follower, VELOCITY)
        follower2 = enemy2.Enemy(playerc, follower2, VELOCITY)
        follower3 = enemy3.Enemy(playerc, follower3, VELOCITY)
        gameDisplay.fill(navy)
        # Display kill number and level number (level increases once every two kills)
        text_set(f"Kill: {kill}", 32, orange, 100, 75)
        text_set(f"Level: {player.wlevel}", 32, orange, 650, 75)
        # HP Bar
        pygame.draw.rect(gameDisplay, black, (x-10, y-20, teachers[character]['HP'], 7), border_radius = 2)
        pygame.draw.rect(gameDisplay, (0,255,0), (x-10, y-20, player.HP, 7), border_radius = 2)
        # Display the player character
        gameDisplay.blit(pygame.transform.flip(pygame.transform.scale(player.image, (50,50)), flip, False), playerc)
        # Display enemy character
        gameDisplay.blit(pygame.transform.scale(sprite, (50,50)), (round(follower[0]), round(follower[1])))
        gameDisplay.blit(pygame.transform.scale(sprite, (50,50)), (round(follower2[0]), round(follower2[1])))
        gameDisplay.blit(pygame.transform.scale(sprite, (50,50)), (round(follower3[0]), round(follower3[1])))
        # for each bullet appended (each click)
        for bullet in player_bullets:
            # shoot the bullet
            # check if bullet hits the enemy
            bullet.main((display_width,display_height), player)
            if bullet.check((display_width,display_height), follower, follower2, follower3) == 1:
                # new random location for enemy spawn
                i1 = random.randint(5,795)
                i2 = random.randint(5,595)
                current_time = pygame.time.get_ticks()
                # only respawn and count kill when a certain time past.
                if current_time - previous_time > time_btw2:
                    previous_time = current_time
                    # decrease enemy hp when hit
                    enemy1.HP -= player.Attack
                    # if hp is 0 then enemy dies, and kill + 1
                    if enemy1.HP <= 0:
                        kill += 1
                        follower = (i1,i2)
                        enemy1.HP = 20
                    # increase level every 2 kills
                    if kill%c == 0:
                        player.wlevel += 1 
                        # increase velocity every level up until it reaches 3.
                        if VELOCITY < 3:
                            VELOCITY += 0.2
                break
            # the same for other2 enemies
            elif bullet.check((display_width,display_height), follower, follower2, follower3) == 2:
                j1 = random.randint(5,795)
                j2 = random.randint(5,595)
                current_time = pygame.time.get_ticks()
                if current_time - previous_time > time_btw2:
                    previous_time = current_time
                    enemy2.HP -= player.Attack
                    if enemy2.HP <= 0:
                        kill += 1
                        follower2 = (j1,j2)
                        enemy2.HP = 20
                    if kill%c == 0:
                        player.wlevel += 1
                        if VELOCITY < 3:
                            VELOCITY += 0.2
                break
            elif bullet.check((display_width,display_height), follower, follower2, follower3) == 3:
                k1 = random.randint(5,795)
                k2 = random.randint(5,595)
                current_time = pygame.time.get_ticks()
                if current_time - previous_time > time_btw2:
                    previous_time = current_time
                    enemy3.HP -= player.Attack
                    if enemy3.HP <= 0:
                        kill += 1
                        follower3 = (k1,k2)
                        enemy3.HP = 20
                    if kill%c == 0:
                        player.wlevel += 1
                        if VELOCITY < 3:
                            VELOCITY += 0.2
                break
        # if the enemy is in the boundary of the player, aka hitting the player then decrease player HP
        if round(follower[0]) <= round(x) and round(follower[0])+50 >= round(x):
            if round(follower[1]) <= round(y) and round(follower[1])+50 >= round(y):
                # so that player dont instantly die, set time between each hit can deal damage.
                current_time = pygame.time.get_ticks()
                if current_time - previous_time > time_btw2:
                    previous_time = current_time
                    pygame.draw.circle(gameDisplay, red, (playerc[0]+25, playerc[1]+25), 10)
                    player.HP -= 5
        # same for two other enemies
        if round(follower2[0]) <= round(x) and round(follower2[0])+50 >= round(x):
            if round(follower2[1]) <= round(y) and round(follower2[1])+50 >= round(y):
                current_time = pygame.time.get_ticks()
                if current_time - previous_time > time_btw2:
                    previous_time = current_time
                    pygame.draw.circle(gameDisplay, red, (playerc[0]+25, playerc[1]+25), 10)
                    player.HP -= 5
        if round(follower3[0]) <= round(x) and round(follower3[0])+50 >= round(x):
            if round(follower3[1]) <= round(y) and round(follower3[1])+50 >= round(y):
                current_time = pygame.time.get_ticks()
                if current_time - previous_time > time_btw2:
                    previous_time = current_time
                    pygame.draw.circle(gameDisplay, red, (playerc[0]+25, playerc[1]+25), 10)
                    player.HP -= 5
        # plyaer dies then activate crash.
        if player.HP <= 0:
            crashed = True
            crash()
        # display update
        pygame.display.flip()
# run all functions
game_intro()
char_choose()
game_loop()
