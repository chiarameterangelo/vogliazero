import pygame
import random

pygame.init()
base_imm = pygame.image.load('immagini/base.PNG')
gameover_imm = pygame.image.load('immagini/gameover.jpg')
sfondo_imm = pygame.image.load('immagini/sfondoo.png')
tubo1_imm = pygame.image.load('immagini/tubo1.PNG')
tubo2_imm = pygame.transform.flip(tubo1_imm,False,True)
uccello_imm = pygame.image.load('immagini/uccelloo.png')
screen = pygame.display.set_mode((280, 384))
fps = 50
velocità_movimento = 3

def inizio():
    # velocità dell'uccello sulla componente y
    global velocita_uccello_y
    global coppia_tubi
    global base
    global uccello

    velocita_uccello_y = 0
    coppia_tubi = CoppiaTubi()
    base = Base()
    uccello = Uccello()
    

def disegna_oggetti():
    screen.blit(sfondo_imm, (0, 0)) # disegna sfondo

    coppia_tubi.aggiorna()

    base.aggiorna() # disegna base
    uccello.aggiorna() # disegna uccello
    
class Base:
    def __init__(self):
        self.x = 0
        self.forma = screen.blit(base_imm, (self.x, 320)) # disegna base

    def aggiorna(self):
        self.x -= velocità_movimento  # riga per far muovere la base
        if self.x < -45:  # riga per far continuare a muovere la base e non farla fermare
            self.x = 0

        self.forma = screen.blit(base_imm, (self.x, 320)) # disegna base

    def scontro(self, uccello):
        if self.forma.colliderect(uccello.forma):
            fine_gioco()

class CoppiaTubi:
    def __init__(self) -> None:
        self.x = 300
        self.y = random.randint(-tubo1_imm.get_height() + 15, -tubo1_imm.get_height() + 150)

        self.forma1 = screen.blit(tubo1_imm, (self.x, self.y))
        self.forma2 = screen.blit(tubo2_imm, (self.x, self.y + tubo2_imm.get_height() + 120))

    def aggiorna(self):
        self.x -= velocità_movimento

        # aggiungo 210 perchè così è in basso
        self.forma1 = screen.blit(tubo1_imm, (self.x, self.y))

        # sottraggo 210 così è in alto
        self.forma2 = screen.blit(tubo2_imm, (self.x, self.y + tubo2_imm.get_height() + 120))

    def scontro(self, uccello):
        # in questo modo vado a verificare se tubo e uccello sono sovrapposti
        if self.forma1.colliderect(uccello.forma) or self.forma2.colliderect(uccello.forma):
            fine_gioco()

class Uccello:
    def __init__(self):
        self.y = 150
        self.forma = screen.blit(uccello_imm, (40, self.y))

    def aggiorna(self):
        self.y += velocita_uccello_y
        self.forma = screen.blit(uccello_imm, (40, self.y))


def aggiornamento_schermo():
    pygame.display.update()
    pygame.time.Clock().tick(fps)
    
def fine_gioco():
    screen.blit(gameover_imm, (90, 150))
    aggiornamento_schermo()
    riniziare = False
    while not riniziare:
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
                inizio()
                riniziare = True
            if i.type == pygame.QUIT:
                pygame.quit()

inizio()

while True:
    disegna_oggetti()
    aggiornamento_schermo()

    velocita_uccello_y += 1

    for i in pygame.event.get():  # i sta ad indicare qualsiasi azione
        if (i.type == pygame.KEYDOWN and i.key == pygame.K_UP):
            velocita_uccello_y = -10
        if i.type == pygame.QUIT:
            pygame.quit()

    # controlla che l'uccello non abbia raggiunto il limite superiore
    if uccello.forma.top < 0:
        fine_gioco()

    # controlla che l'uccello non abbia toccato la base
    base.scontro(uccello)

    # controlla che l'uccello non si sia scontrato con un tubo
    coppia_tubi.scontro(uccello)

    # se il primo tubo è scomparso dallo schermo, rimuovilo
    if coppia_tubi.x <= -tubo1_imm.get_width():
        coppia_tubi = CoppiaTubi()




