import os
from glob import glob
import time
import speech_recognition as sr
from random import shuffle
import pygame, sys
from button import Button

 
pygame.init()
pygame.font.init()


gameDisplay = pygame.display.set_mode((1100, 700))
BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def game():
    gameDisplay.fill((255,255,255))
    BLUE =(0,255,0)
    pngs = [x for x in glob("animals\\*.PNG")]
    names = [x.split(".")[0] for x in glob("animals\\*.PNG")]


    animals = {k:v for k, v in zip(pngs, names)}
    print(animals)
 
 
    print(pngs)
    print(names)
    keys = list(animals.keys())
    shuffle(keys)

    score = 0 
    font = pygame.font.SysFont(None,40)
    for animal in keys:

        guess_counter = 0
        scorel = font.render('score : '+str(score),True,(240,230,100))
        carImg = pygame.image.load(os.path.join('', animal))
        gameDisplay.blit(carImg,(0,0))
        gameDisplay.blit(scorel,(0,0))
        pygame.display.update()

        r = sr.Recognizer()
        with sr.Microphone() as source:
           r.adjust_for_ambient_noise(source)
           print ('What\'s his name!')
           audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)

        except:
            print('Did not get that try Again')
       
        if text == animals[animal].split("\\")[1]:
            print('good job\n=========\n\n') 
            print(text)
            score += 1


        else:
            if guess_counter == 3:
                print('wrong try again')
                print(text)
                guess_counter += 1
        print(text)
        print(f"{score}")
    
def play():
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game()
                main_menu()

        pygame.display.update()

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        gameDisplay.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        gameDisplay.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(gameDisplay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()        

def main_menu():

    while True:
        gameDisplay.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(70).render("ANIMALS QUIZ", True, "#b70f80")
        MENU_RECT = MENU_TEXT.get_rect(center=(550, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(550, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(550, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(550, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        gameDisplay.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(gameDisplay)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

        

    
main_menu()

    
pygame.quit()