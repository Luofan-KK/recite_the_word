import _thread
import win32com.client
import numpy as np
import pygame
import pickle
import random
from pygame.locals import *
import time

pygame.init()
running=True
screen = pygame.display.set_mode((800, 640), 0, 32)
pygame.font.init()
font=pygame.font.SysFont(None,24)
font2=pygame.font.SysFont('SimHei',12)
WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
BLUE=(0,0,128)
sspeaker=win32com.client.Dispatch("SAPI.SpVoice")
sspeaker.rate=1
def my_speak(string):
    time.sleep(0.5)
    sspeaker.Speak(string)
class words:
    def __init__(self,screen):
        self.speaker=win32com.client.Dispatch("SAPI.SpVoice")
        self.speaker.rate=2
        words.screen=screen
        f=open('result.pickle','rb')
        word_list=pickle.load(f)
        random.shuffle(word_list)
        self.word_list=word_list
        f.close()
        self.step=0
        self.words=[word(0),word(200),word(400),word(600)]
        self.flags=[False,False,False,False]
        self.strings=['','','','']

    def down(self,speed):
        for i,r in enumerate(self.words):
                self.words[i].top=r.top+speed

    def send_word(self):
        for i,f in enumerate(self.flags):
            if not f:
                self.flags[i]=True
                self.words[i].generate(self.word_list[self.step])
                self.strings[i]=self.word_list[self.step]
                self.step+=1


    def print(self):
        for i,w in enumerate(self.words):
            w.blit(self.screen)

    def check_string(self,string):
        for i,w in enumerate(self.strings):
                try:
                    eng=w[0]
                    cn=w[1]
                except:
                    return string
                if string==eng.lower():
                        self.flags[i]=False
                        string=''
                        self.speaker.Speak(eng)
                        _thread.start_new_thread(my_speak,(cn,))
        return string

    def check_all(self):
        for i,w in enumerate(self.words):
                if w.top>650:
                        return True
        return False



class word:
    def __init__(self,left):
        self.rend=[]
        self.left=left
        self.top=0

    def generate(self,word):
        self.top=0
        self.rend=[font.render(word[0],True,BLACK,WHITE),
                    font2.render(word[1],True,BLACK,WHITE)]
        self.rect=[]
        for i,r in enumerate(self.rend):
                self.rect.append(r.get_rect())
                self.rect[i].top=self.top+20*i
                self.rect[i].left=self.left

    def blit(self,screen):
        for i,r in enumerate(self.rend):
                self.rect.append(r.get_rect())
                self.rect[i].top=self.top+20*i
                self.rect[i].left=self.left

        for i in range(2):
            screen.blit(self.rend[i],self.rect[i])

w=words(screen)
type_string=''
while running:
    screen.fill(BLACK)
    time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_F3:
                running= False
            if event.key == K_F4:
                type_string=''
            if event.key == K_BACKSPACE:
                type_string=type_string[:-1]
            if event.key == K_a:
                type_string=type_string+'a'
            if event.key == K_b:
                type_string=type_string+'b'
            if event.key == K_c:
                type_string=type_string+'c'
            if event.key == K_d:
                type_string=type_string+'d'
            if event.key == K_e:
                type_string=type_string+'e'
            if event.key == K_f:
                type_string=type_string+'f'
            if event.key == K_g:
                type_string=type_string+'g'
            if event.key == K_h:
                type_string=type_string+'h'
            if event.key == K_i:
                type_string=type_string+'i'
            if event.key == K_j:
                type_string=type_string+'j'
            if event.key == K_k:
                type_string=type_string+'k'
            if event.key == K_l:
                type_string=type_string+'l'
            if event.key == K_m:
                type_string=type_string+'m'
            if event.key == K_n:
                type_string=type_string+'n'
            if event.key == K_o:
                type_string=type_string+'o'
            if event.key == K_p:
                type_string=type_string+'p'
            if event.key == K_q:
                type_string=type_string+'q'
            if event.key == K_r:
                type_string=type_string+'r'
            if event.key == K_s:
                type_string=type_string+'s'
            if event.key == K_t:
                type_string=type_string+'t'
            if event.key == K_u:
                type_string=type_string+'u'
            if event.key == K_v:
                type_string=type_string+'v'
            if event.key == K_w:
                type_string=type_string+'w'
            if event.key == K_x:
                type_string=type_string+'x'
            if event.key == K_y:
                type_string=type_string+'y'
            if event.key == K_z:
                type_string=type_string+'z'
    type_string=w.check_string(type_string)
    if w.check_all():
            break
    w.send_word()
    w.print()
    w.down(0.2)
    tf=font.render(type_string,True,BLACK,WHITE)
    rect=tf.get_rect()
    rect.top=600
    screen.blit(tf,rect)
    pygame.display.update()

