import pygame,math

pygame.init()

windowwidth, windowheight = 1240, 700
win = pygame.display.set_mode((windowwidth, windowheight))
pygame.display.set_caption("Fourier")

clock = pygame.time.Clock()
black = (35, 35, 35)
white = (255, 255, 50)
pi = math.pi
X, Y = windowwidth//2, 300



def drawpoints(points):
    for point in points:
        point[0] += 1
        win.set_at(point, white)

def drawcircles():
    tick = pygame.time.get_ticks() / 1000
    centres = [(180, windowheight//2)]
    freq = 50
    xx , yy = 0, 0
    for k in range(terms):
        n = 2 * k + 1                                                     
        radius = round(55 * (4 / (n * pi)))                               
        angle = round(2 * pi * tick*freq* n)                              
        xx = centres[k][0] + math.cos(math.radians(angle)) * radius
        yy = centres[k][1] + math.sin(math.radians(angle)) * radius
        pygame.draw.circle(win, white, centres[k], radius, 1)
        xx = round(xx)
        yy = round(yy)
        pygame.draw.line(win, white, centres[k], (xx, yy), 1)
        centres.insert(k + 1, (xx, yy))
    pygame.draw.line(win, white, (xx, yy), (windowwidth//2, yy), 1)
    Y = yy
    pixels.append([X, Y])

def redrawGameWindow():
    win.fill(black)
    win.blit(message, (100, 60))
    text = font.render(f'Terms = {terms}', 1, white)
    win.blit(text, (windowwidth//2 - text.get_width() // 2, windowheight - 70))
    drawcircles()
    drawpoints(pixels)
    pygame.display.update()

font = pygame.font.SysFont('consolas', 30, True)
msg = pygame.font.SysFont('consolas', 18, True)
terms = 1
pixels = []
presscount = 0

run = True
while run:
    clock.tick(120)
    if presscount > 0:
        presscount += 1
    if presscount > 15:
        presscount = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and terms < 60 and presscount == 0:
        terms += 1
        presscount += 1
    if keys[pygame.K_DOWN] and terms >= 2 and presscount == 0:
        terms -= 1
        presscount += 1

    message = msg.render("press up and down arrow keys to change terms", 1, white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

pygame.quit()
