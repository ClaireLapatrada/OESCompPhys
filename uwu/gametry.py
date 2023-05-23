# Importing libraries and initializing Pygame
import pygame
import time
import random
pygame.init()

# Storing display width and height in variables to use later
display_width = 800
display_height = 600
# Set dino dimension
dino_width = 25
# Set up and initialize display width and height
gameDisplay = pygame.display.set_mode((display_width,display_height))
# Set window name (or caption if you call it)
pygame.display.set_caption('Dino')

# Storing color values in a name so it's easier to use later
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
blue = [0,0,255]
bright_green = (0,255,0)
bright_red = (255,0,0)

colors = [black, white, red, green, blue]
# set pause to be False
pause = False
# Set up time in game, for FPS usage
clock = pygame.time.Clock()
# Set up crash to be False at first, to be used to close the app
crashed = False
# Download images
dinoImg = pygame.image.load('dino2.png')
gameIcon = pygame.image.load('dino2.png')
meteor1Img = pygame.image.load('meteor1.png')
meteor2Img = pygame.image.load('meteor2.png')
pygame.display.set_icon(gameIcon)

# button function for future use, easier to create
# This function has the parameters of:
# msg: What do you want the button to say on it.
# x: The x location of the top left coordinate of the button box.
# y: The y location of the top left coordinate of the button box.
# w: Button width.
# h: Button height.
# ic: Inactive color (when a mouse is not hovering).
# ac: Active color (when a mouse is hovering).
def button(msg,x,y,w,h,ic,ac,action=None):
    # get mouse position (x,y)
    mouse = pygame.mouse.get_pos()
    # click is when the mouse get pressed
    click = pygame.mouse.get_pressed()
    # if the mouse is hovered within the button rectangle
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        # draw rectangle with hovered color
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        # if the mouse is clicked ( == 1), and no action is happening, then an action is activate
        if click[0] == 1 and action != None:
            action()     
    else:
        # draw rectangle with normal color
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    # set up text font and size
    smallText = pygame.font.Font("freesansbold.ttf",20)
    # set up text message and rectangle
    textSurf, textRect = text_objects(msg, smallText)
    # set up text center position
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    # display the text
    gameDisplay.blit(textSurf, textRect)
# Showing dodge score on screen function
def things_dodged(count):
    # font and size set up
    font = pygame.font.SysFont(None, 25)
    # make the text set up with the # of dodge count
    text = font.render("Dodged: "+str(count), True, black)
    # display the text on screen, position top left (0,0)
    gameDisplay.blit(text,(0,0))

# takes x, y starting points, width and height variables and color.
def things(thingx, thingy):
    # pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(meteor1Img, (thingx,thingy))

def special_things(sthingx, sthingy):
    # pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
    gameDisplay.blit(meteor2Img, (sthingx,sthingy))

# Start and display a Dino blit function (character that moves upon our action if specified) at a specify coordinate (x,y)
def dino(x,y):
    gameDisplay.blit(dinoImg, (x,y))

# Define text object function to help simplifying the process to render the text and its rectangle
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Function to define parameters in the text (font, size, position, etc.)
def message_display(text):
    # Fonts and size
    largeText = pygame.font.Font('freesansbold.ttf',115)
    # Define text and its rectangle (use to position the text)
    TextSurf, TextRect = text_objects(text, largeText)
    # Position of the text to be displayed
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
# pause function
pause = False
def paused():

    # set up text font and size
    largeText = pygame.font.SysFont("comicsansms",115)
    # establish the text and its rectangle
    TextSurf, TextRect = text_objects("Paused", largeText)
    # center the text at the middle of the screen
    TextRect.center = ((display_width/2),(display_height/2))
    # display the text and its invisible rectangle
    gameDisplay.blit(TextSurf, TextRect)
    
    # while pause is true
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        
        # show the two buttons
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quit_game)
        # update frames and fps
        pygame.display.update()
        clock.tick(15)     
# unpause function
def unpause():
    global pause
    pause = False
# Function to display messay "You Crashed" when the function is called.
def crash():
    # set up text font and size
    largeText = pygame.font.SysFont("comicsansms",115)
    # establish the etxt and its rectangle
    TextSurf, TextRect = text_objects("You Crashed", largeText)
    # center the text position
    TextRect.center = ((display_width/2),(display_height/2))
    # display the text
    gameDisplay.blit(TextSurf, TextRect)
    
    # if x is pressed then qiut game
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #gameDisplay.fill(white)
        
        # show the green and red button like the start screen
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quit_game)
        # update frame and fps
        pygame.display.update()
        clock.tick(15) 
# quit game function
def quit_game():
    pygame.quit()
    quit()
# define game intro
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
        gameDisplay.fill(white)
        # set up font text
        largeText = pygame.font.Font('freesansbold.ttf',115)
        # define game name text and its rectangle
        TextSurf, TextRect = text_objects("Dino Dodge", largeText)
        # position the text center
        TextRect.center = ((display_width/2),(display_height/2))
        # display the text and its invisible rectangle
        gameDisplay.blit(TextSurf, TextRect)

        # set up a button with our amazing button function
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red, quit_game)
        pygame.display.update()
        clock.tick(15)
# Define game function that initializes value each game
def game_loop():
    global pause
    # initial random things
    int = 2
    # Set up the blit position (x,y) in this case I put it in the middle of the screen so its display_dimension/2
    x = (display_width * 0.5)
    y = (display_height * 0.8)
    # Define dimensions and initial speed, random character spawn point
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    sthing_startx = random.randrange(0, display_width)
    sthing_starty = -600
    sthing_width = 50
    sthing_height = 160
    # normal dino speed coefficient
    speed = 1
    # Initial position
    x_change = 0
    # Initialize keeping score of dodges
    dodged = 0
    # game runs until this is turned True
    gameExit = False

    # Run until the button X is clicked on, then close/quit the app
    while not gameExit:
        # loop through all event
        for event in pygame.event.get():
            # close if the X button (close window) has been pressed
            if event.type == pygame.QUIT:
                # quit when the loop is exited.
                pygame.quit()
                quit()
            # Dino movement
            # if the key is pressed check the following:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    speed = 5
                # if left arrow key is pressed, move 5 position left
                if event.key == pygame.K_LEFT:
                    x_change = -5*speed
                # if right arrow key is pressed, move 5 position right
                if event.key == pygame.K_RIGHT:
                    x_change = 5*speed
                # if p is pressed, then pause becomes true, and the pause screen shows.
                if event.key == pygame.K_p:
                    pause = True
                    paused()
            # if nothing is pressed, stop changing position.
            # (Without this statement the characters won't stop moving after a key is pressed)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_SPACE:
                    speed = 1
        # store new position (without this the blit will go back to the initial position)
        x += x_change
        # fill screen with white
        gameDisplay.fill(white)

        # call and update things positions and dimensions
        if int == 1:
            things(thing_startx, thing_starty)
            thing_starty += thing_speed
        else:
            special_things(sthing_startx, sthing_starty)
            sthing_starty += thing_speed

        # activating dino blit function
        dino(x,y)
        things_dodged(dodged)
        
        # if the x value of the dino blit reaches either end of the screen then quit game
        if x > display_width - dino_width or x < 0:
            crash()
        # start a new "thing" at top, random x value after the previous one goes off the screen (>display height)
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            # update dodge and speed by 1 everytime dodge succesfully, and increase thing width by 20% of dodge number
            dodged += 1
            thing_speed += 1
            int = random.randint(1,3)
        if sthing_starty > display_height:
            sthing_starty = 0 - sthing_height
            sthing_startx = random.randrange(0,display_width)
            # update dodge and speed by 1 everytime dodge succesfully, and increase thing width by 20% of dodge number
            dodged += 1
            thing_speed += 1
            int = random.randint(1,3)
        # Check if got hit by the box
        # NORMAL METEOR
        # FIRST CHECK: if the vertical position of the dino is within the box height
        if y < thing_starty+thing_height:
            print('y crossover')
            # SECOND CHECK: check each side of the dino, if the x position is within the box then print x-cross over and game over.
            if x > thing_startx and x < thing_startx + thing_width or x+dino_width > thing_startx and x + dino_width < thing_startx+thing_width:
                print('x crossover')
                # now when both condition are satisfied (both x and y crosses) print "you crash"
                crash()
        # SPECIAL METEOR
        if y < sthing_starty+sthing_height:
            print('y crossover')
            # SECOND CHECK: check each side of the dino, if the x position is within the box then print x-cross over and game over.
            if x > sthing_startx and x < sthing_startx + sthing_width or x+dino_width > sthing_startx and x + dino_width < sthing_startx+sthing_width:
                print('x crossover')
                # now when both condition are satisfied (both x and y crosses) print "you crash"
                crash()
        # update frame
        pygame.display.update()
        # set FPS to 60
        clock.tick(60)
# Start the intro + game
game_intro()
game_loop()
# quit when the loop is exited.
pygame.quit()
quit()