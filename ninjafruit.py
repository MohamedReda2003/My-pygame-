import pygame, sys, os
import time
import random

slices=['appleslice1','appleslice2','appleslice3','appleslice4,"bananaslice1','bananaslice2','bananaslice3','pearslice','pearslice2','pearslice3','pearslice4','tomatoslice','tomatoslice2','tomatoslice3','tomatoslice6','watermelonslice']
fruits = ['apple','apple2','apple5','apple4','apple1','banana3','banana4','banana5', 'banana2', 'banana1','blackberry','carrot','carrot2','carrot3','carrot4','cherry','cherry2','cherry3','coconut','damn','damn2','grape','grape2','grape3','lemon','lemon2','orange','orange2','orange3','orange4','pear','pear2','pineapple','strawberry','strawberry1','sweet1','sweet2','sweet3','sweet4','sweet5','sweet6','tomato','tomato2','watermelon']
width = 1000
height = 1000
white = (255,255,255)
black = (0,0,0)
clock = pygame.time.Clock()
g = 1
score = 0
fps = 13


pygame.init()
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(white)
font = pygame.font.Font(os.path.join(os.getcwd(), 'font/SpaceMission-rgyw9.otf'), 32)
score_text = font.render(str(score), True, black, white)

def generate_random_fruits(fruit):

    path = os.path.join(os.getcwd(),'ninja fruit/'+ fruit+'.png')
    data[fruit] = {
        'img' : pygame.image.load(path),
        'x' : random.randint(100, 500),
        'y' : 800,
        'speed_x' : random.randint(-10, 10),
        'speed_y' : random.randint(-80, -60),
        'throw' : False,
        't' : 0,
        'hit' : False,
    }

    if(random.random() >= 0.75):
        data[fruit]['throw'] = True
    else:
        data[fruit]['throw'] = False

data = {}
for fruit in fruits:
    generate_random_fruits(fruit)

pygame.display.update()

while True:
    gameDisplay.fill(white)
    gameDisplay.blit(score_text, (0,0))
    for key,value in data.items():
        if value['throw']:
            value['x'] = value['x'] + value['speed_x']
            value['y'] = value['y'] + value['speed_y']
            value['speed_y'] += (g*value['t'])
            value['t'] += 1

            if value['y'] <= 800:
                gameDisplay.blit(value['img'], (value['x'],value['y']))
            else:
                generate_random_fruits(key)

            current_position = pygame.mouse.get_pos()
            if not value['hit'] and current_position[0] > value['x'] and current_position[0] < value['x']+60 and current_position[1] > value['y'] and current_position[1] < value['y']+60:
                path = os.path.join(os.getcwd(),'ninja fruit/'+key+'.png')
                value['img'] = pygame.image.load(path)
                value['speed_x'] += 10
                score += 1
                score_text = font.render(str(score), True, black, white)
                value['hit'] = True

        else:
            generate_random_fruits(key)

    pygame.display.update()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()