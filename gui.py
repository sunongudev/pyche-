

import pygame, sys
from pygame.locals import *

pygame.init()
#START
rows=('a','b','c','d','e','f','g','h')
cols=('8','7','6','5','4','3','2','1')
class Piece:
    def __init__(self,kind,col,row):
        self.surf=pygame.transform.scale(pygame.image.load('src/'+kind+'.png'),(60,60)).convert_alpha()
        self.row=row
        self.col=col
        self.kind=kind

    def row_move(self,row):
        self.row=row

    def col_move(self,col):
        self.col=col

    def move(self,col,row):
        row_move(row)
        col_move(col)

screen = pygame.display.set_mode((480,480))
pygame.display.set_caption('Chess')

board=pygame.image.load('src/board.png')
play=True
temp=['r','n','b']
piecesKind=['p']*8 + temp + ['k','q'] + temp[::-1]
print(piecesKind)
whitePiecesKind=['w'+i for i in piecesKind]
blackPiecesKind=['b'+i for i in piecesKind]
pieces=[Piece(i,'a','1') for i in whitePiecesKind + blackPiecesKind]
k=0
for i in range(0,len(pieces)):
    itskind=pieces[i].kind
    tRow=0
    if k==8:
        k=0
    if itskind[1]=='p':
        tRow=1
    if itskind in whitePiecesKind:
        pieces[i].row=rows[tRow]
    else:
        pieces[i].row=rows[7-tRow]
    pieces[i].col=cols[k]
    k+=1

while play:
    for e in pygame.event.get():
        if e.type==QUIT:
            play=False
            pygame.quit()
            sys.exit()
    screen.fill(Color('white'))
    screen.blit(board,(0,0))
    for i in pieces:
        board.blit(i.surf,pygame.rect.Rect(cols.index(i.col)*60,rows[::-1].index(i.row)*60,60,60))
    pygame.display.flip()


























