import pygame
import random

pygame.init()
base = pygame.image.load('immagini/base.PNG')
gameover = pygame.image.load('immagini/gameover.jpg')
sfondo = pygame.image.load('immagini/sfondoo.png')
tubo1 = pygame.image.load('immagini/tubo1.PNG')
tubo2 = pygame.transform.flip(tubo1,False,True)
uccello = pygame.image.load('immagini/uccelloo.png')
screen = pygame.display.set_mode((280, 384))
fps = 50
velocità_movimento = 3


def inizio():
    # velocità dell'uccello sulla componente y
    global uccellox, uccelloy, velocitauccy
    global basex
    global tubi
    uccellox, uccelloy = 40, 150
    velocitauccy = 0
    basex = 0
    tubi = []
    tubi.append(insieme_tubi())

def disegna_oggetti():
    screen.blit(sfondo, (0, 0))
    for tubo in tubi:
        tubo.disegna_vaiavanti()
    screen.blit(uccello, (uccellox, uccelloy))
    screen.blit(base, (basex, 300))

class insieme_tubi:
    def __init__(self) -> None:
        self.x = 300
        self.y = random.randint(-75, 150)

    def disegna_vaiavanti(self):
        self.x -= velocità_movimento
        # aggiungo 210 perchè così è in basso
        screen.blit(tubo1, (self.x, self.y+210))
        # sottraggo 210 così è in alto
        screen.blit(tubo2, (self.x, self.y-210))

    def scontro(self, uccello, uccellox, uccelloy):
        tol = 5
        ucc_destra = uccellox+uccello.get_width()-tol
        ucc_sinistra = uccellox+tol
        tubi_destra = self.x+tubo2.get_width()
        tubi_sinistra = self.x
        ucc_su = uccelloy+tol
        ucc_giu = uccelloy+uccello.get_height()-tol
        tubi_su = self.y+110
        tubi_giu = self.y+210
        # in questo modo vado a verificare se tubo e uccello sono sovrapposti
        if ucc_destra > tubi_sinistra and ucc_sinistra < tubi_destra:
            if ucc_su < tubi_su or ucc_giu > tubi_giu:
                fine_gioco()

def aggiornamento_schermo():
    pygame.display.update()
    pygame.time.Clock().tick(fps)
    
def fine_gioco():
    screen.blit(gameover, (90, 150))
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
    basex -= velocità_movimento  # riga per far muovere la base
    if basex < -45:  # riga per far continuare a muovere la base e non farla fermare
        basex = 0
    velocitauccy += 1
    uccelloy += velocitauccy
    for i in pygame.event.get():  # i sta ad indicare qualsiasi azione
        if (i.type == pygame.KEYDOWN and i.key == pygame.K_UP):
            velocitauccy = -10
        if i.type == pygame.QUIT:
            pygame.quit()
    if tubi[-1].x < 150:
        tubi.append(insieme_tubi())
        # con questa riga si continuano ad aggiungere i tubi man mano che si va avanti
        for tubo in tubi:
            tubo.scontro(uccello, uccellox, uccelloy)
    if uccelloy > 280:  # 280 è il livello della base
        fine_gioco()

    disegna_oggetti()
    aggiornamento_schermo()





