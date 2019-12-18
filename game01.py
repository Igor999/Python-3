import os.path, sys
import pygame
import random
from pygame import *
# Инициализируем загруженную библиотеку.
import pygame.mixer, pygame.time
mixer = pygame.mixer
time = pygame.time
Font = None
init()
#Размер окна
xscr = 800
yscr = 800
#Координаты пистолета
zx = 312
zy = 300
score = 0
level = 1
#Шаг перемещения пистолета
step = 40
#fon = 240, 240, 250
xpos = zx
ypos = zy
flag = 1
# flag - переменная ,маркер выхода
temp = 100
#задержка 100=0,1секунды
dulo= 'left'
screen = display.set_mode((xscr, yscr))
# Создаем окно разрешением xscr х yscr
background = image.load('fon1.jpg')
screen.blit(background, (0,0))
#грузим фоновый рисунок и помещаем его на screen 
key.set_repeat(1,1)
#Уменьшаем время отклика клавиатуры
pygame.mixer.music.load('dnb.wav')
pygame.mixer.music.play()

def boom():
	# звук выстрела
    file = os.path.join('vistrel.wav')
    sound = mixer.Sound(file)
    channel = sound.play()



class Sprite:
#Этот класс я стащил у Майкла Сондерса из его Pilvanders	
	def __init__(self,xpos,ypos,filename):
		#инициализация j,]trnf
		self.x = xpos
		self.y = ypos
		pik = image.load(filename)		
		pik = pik.convert()
		self.bitmap = pik
		self.bitmap.set_colorkey((0,0,0))
	def set(self, xpos, ypos):
		#установить спрайт по координатам
		self.x = xpos
		self.y = ypos
	def render(self):
		#отрисовать спрайт
	    screen.blit(self.bitmap, (self.x, self.y))
		
#------------------------------------------------------------
akr1 = Sprite (zx,zy, 'akr1.png') 
akr2 = Sprite (zx,zy, 'akr2.png')
akr3 = Sprite (zx,zy, 'akr3.png')
akl1 = Sprite (zx,zy, 'akl1.png') 
akl2 = Sprite (zx,zy, 'akl2.png')
akl3 = Sprite (zx,zy, 'akl3.png')
#это спрайты пистолета 

#--------------------------------------------------------------

class Kalash (Sprite):
	def __init__(self,xpos,ypos,naprav):
		global ak1, ak2, ak3
		self.x = xpos
		self.y = ypos
		if naprav == 'right':
		# Дуло смотрит вправо	
		  ak1 = akr1
		  ak2 = akr2
		  ak3 = akr3
		  ak1 = Sprite.__init__(self,xpos,ypos, 'akr1.png') 
		else:
		  # Дуло смотрит влево	
		  ak1 = akl1 
		  ak2 = akl2
		  ak3 = akl3
		  ak1 = Sprite.__init__(self,xpos,ypos, 'akl1.png') 
		# в зависимости от 'naprav
	def put(self,xpos, ypos):
		# установить по координатам
		self.x = xpos
		self.y = ypos
		self.render()	
		
#----------------------------------------------------------------
class Vrag(Sprite):
	def __init__(self,xpos,ypos,naprav):
		global vrg
		self.x = xpos
		self.y = ypos
		if naprav == 'left':
		 	  vrg = Sprite.__init__(self,xpos,ypos, 'botr1.png')
		else:
		  	  
			  vrg = Sprite.__init__(self,xpos,ypos, 'zombi.png')
			
	def put(self,xpos, ypos):
		# отрисовываем пингвина
		global flag
		if 0 <  xpos < pr+1 :
			# проверка на границы окна,если пингвин в пределах границ он отрисовывается.
			self.x = xpos
			self.y = ypos
			self.render()
			#Проверка достижения середины	
			if (flag > 0) and (182< xpos < 500) :
				flag = 0
			
#-------------------------------------------------------------------
def bah(xpos, ypos):
	#процедура выстрела
	global vlx, vly, score
	ak2.set(xpos ,ypos)
	ak2.render()
	for i in range (6):
		vlx[i] = vlx[i] + 1
		vrx[i] = vrx[i] - 1
		vrgl[i].put(vlx[i],vly[i])
		vrgr[i].put(vrx[i],vry[i])
		if 0 < vlx[i] :
			if (dulo == 'left') and ((vly[i]-20) < ypos < (vly[i]+60 )):
				score = score + 1
				vlx[i] = - random.randrange (50 , 300, 25)
		if vrx[i]  < pr :		
			if (dulo == 'right') and ((vry[i]-20) < ypos < (vry[i]+60 )):
				score = score + 1
				vrx[i] = pr+random.randrange (50 , 300, 25)	
		#проверка поподания в ботинок в цикле если дуло влево проверяются правые/ вправо левые	
		#при выстреле все ботинки все равно смещаются на пиксел к центру
		#это защита от постоянно нажатого пробела
		#вместо убитого ботинка за пределами экрана генерируется новый по случайному X.
		display.update()
		ak3.set(xpos ,ypos )
		ak3.render()
		boom()
		#звук выстрела
		display.update()
#-------------------------------------------------------------------
while 1:
  #основной цикл программы	
  score = 0
  #счет
  level = 1	
  #уровень
  xpos = zx
  ypos = zy
  flag = 1
  #эта переменная предназначена для выхода из циклов при flag=0
  speed = 1
  temp = 100
  #задержка в микросекундах 
  dulo= 'left'

  zx = 250
  zy = 300
  #Координаты пистолета
  #-----------------------------------------------
  vlx = [ 0, -200 ,0, -400,-150 ,0]
  vly = vry = [100,200, 300,400, 500,  600 ]
  pr= xscr - 118
  vrx = [ pr+100, pr, pr+300,pr, pr+200,pr ]
  #начальные координаты 6-ти пингвинов
  vrgl = []
  vrgr = []
  #создаем 2  списка для пингвинов справа и слева 
  flag = 1
  for i in range (6):
     #заполняем списки в цикле	
     vrgl.append (Vrag(vlx[i],vly[i],'left'))
     vrgr.append (Vrag(vrx[i],vry[i],'right'))
		
  kalashnik = Kalash( zx,zy,dulo)
  #определяем пистолет(дуло вправо/влево)
  screen.blit ( background, (0,0) )
  kalashnik.put(zx,zy)
  display.flip()
  #заливаем экран обоями, ставим пистолет по координатам и отрисовываем все это на дисплее
  #-----------------------------------------------------------------
  while 1:
      #основной цикл игры	
      for i in range (6):
	 #смещение всех пингвинов на пиксел к центру и их отрисовка
	      vlx[i] = vlx[i] + 1
	      vrx[i] = vrx[i] -1
	      vrgl[i].put(vlx[i],vly[i])
	      vrgr[i].put(vrx[i],vry[i])
      kalashnik.put(zx,zy)
      #устанавливаем пистолет
      display.flip()
      screen.blit ( background, (0,0) )
      Font = font.Font(None, 32)
      rez = score // 20
      #rez  = счет нацело поделить на сто
      level = 1 + rez
      #уровень до 100 очков 1-ый, дальше за каждые 100 добавляется 1
      if temp > 19 :
	      temp = 100 - rez*20
	#определяем задержку,здесь по if защита от ухода в минус
      textimg = Font.render(str(level), 1,(255,0,0), (0,255,255))
      screen.blit(textimg, (700,9))
      #печатаем уровень
      textimg = Font.render(str(score), 1,(255,0,0), (0,255,255))
      screen.blit(textimg, (500,9))
      #печатаем счет(кол-во убитых пингвинов)
      pygame.time.wait(temp)
      #задержка,чем выше уровень тем она меньше
      if flag == 0:
          break
      #выход из основного игрового цикла
      for event in pygame.event.get ():
	#опрос клавиатуры, мыши
       if event.type == QUIT:
        sys.exit()
         #выход по нажатию креста на рамке окна
       if event.type == KEYDOWN:
             #если нажата клавиша то

              if event.key == K_ESCAPE:
                  flag = 0
		 #по esc выход из игрового цикла через установку flag в  0
              if event.key == K_DOWN:
                  zy = zy + step
                  if zy >= (yscr - 100):
                     zy = zy - step
                 #перемещение пистолета вниз если не достигнута нижняя граница
              if event.key == K_UP:
                  zy = zy - step
                  if zy <= 0:
                     zy = zy + step
                   #перемещение пистолета вверх если не достигнута верхняя граница  
              if event.key == K_LEFT:
                  dulo = 'left'
              kalashnik.__init__(zx, zy ,'left') 
                   #дуло влево
              if event.key == K_RIGHT: dulo = 'right'
              kalashnik.__init__(zx, zy ,dulo)
		   #дуло вправо	    
              if event.key == K_SPACE: bah(zx, zy)
                   #выстрел
#-------------------конец основного цикла-------------------------		
  flag = 1            
  boom()
  boom()
  boom()
  #большой бум символизирующий конец игры !
  Font = font.Font(None, 72)
  #определяем фонт
  textimg = Font.render('                               ', 1,(0,255,255), (255,0,0))	
  screen.blit(textimg, (180,250))
  textimg = Font.render('  GAME  OVER  !!! ', 1,(0,255,255), (255,0,0))
  screen.blit(textimg, (180,300))
  textimg = Font.render('                               ', 1,(0,255,255), (255,0,0))
  screen.blit(textimg, (180,350))
  Font = font.Font(None, 36)
  textimg = Font.render('-----------------------------------------------------', 1,(0,255,255), (255,0,0))	
  screen.blit(textimg, (180,575))
  
  textimg = Font.render('     Esc - Exit    ', 1, (255,0,0))
  screen.blit(textimg, (180,600))
  textimg = Font.render('-----------------------------------------------------', 1,(0,255,255), (255,0,0))
  screen.blit(textimg, (180,625))
  display.flip()
  #пишем на экране Game Over и прочую инфу			
  while 1:
	 # этот цикл на окончание программы    
         for event in pygame.event.get ():
          if event.type == QUIT: sys.exit(1)
          if event.type == KEYDOWN:
           if event.key == K_SPACE:
               flag = 0
               if flag == 0: break
			#по Space выход из внутреннего цикла через break 			           
           if event.key == K_ESCAPE:
              sys.exit(1) 
			#по Esc выходим из программы

             # по break мы выходим из этого цикла и попадаем в начало основного цикла программы
