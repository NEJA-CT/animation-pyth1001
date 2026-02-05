import pyxel
import math
#import time

GRAVITY = 0.3
BOUNCE = .75
switchbnce = 0
bncemax = 3 #This makes it so space being held won't do any thing if just tapped for a second
W, H = 160, 120
a = 0
b = 0 #set back to 1 for forwards motion at beginning
Shooting = False
Shootingforce = 0
Shootingangle = 0
spacebar = False
variables = True
wallbounce = .75
draw_line = False

pyxel.init(W, H, "Some name")

figure_image = pyxel.Image.from_image("../assets/even_newer_piskel.png", incl_colors=False)
pyxel.images[0] = figure_image

def draw_figure(figure_x, figure_y, figure_tile):
   figure_height = figure_image.height / 4
   pyxel.blt(
      figure_x,
      figure_y,
      0,
      0,
      figure_height * figure_tile,

      figure_image.width,
      figure_height,
      colkey=0
   )

figure_frame = 0


# initial position and velocity
x, y = W // 2, H // 1.5
vx, vy = 0, 0

#pyxel.rect(1, 2, 3, 4, 5)
def update():
   global x, y, vx, vy, a, b, player_x, player_y, figure_frame, Shooting, switchbnce, Shootingforce, Shootingangle, draw_line, BOUNCE, spacebar, variables

   # Apply gravity
   vy += GRAVITY
   y += vy
   a += b
   if b >= 0:
      b -=0.01
   # Bounce when hitting the ground
   ground = H - 5 #to change if ball radius changes - radius + 1

   player_x = x + a
   player_y = 70

   if Shooting == False:
      BOUNCE = 1
   else:
      BOUNCE = .75


   if y > ground:
       y = ground
       vy = -vy * BOUNCE # reverse and lose some energy
 
 
   if pyxel.btn(pyxel.KEY_D):# No more max speed
      b += .2
   elif pyxel.btn(pyxel.KEY_A):
      b -=.2
   
#   if pyxel.btn(pyxel.KEY_S) and b >= .4:
#      b -= .4

#   if pyxel.btn(pyxel.KEY_S) and b <= -.4:
#      b += .4
   #if pyxel.btn(pyxel.KEY_SPACE):
      #pyxel.line(a + x - 43, 62, 75, -50, 3)
   if pyxel.btn(pyxel.KEY_S):
      b = b / 2
      if b >= -.5 and b <= .5:
         b = 0
 

   if a <= -60: # Left wall 
      b = -wallbounce * b + .5
   if a >= 80: # Right wall
      b = -wallbounce * b - .5 


   if b >= .2 or b <= -.2 and not pyxel.btn(pyxel.KEY_S) : #need parentheses around the "or"??
      figure_frame = int(pyxel.frame_count / 4) % 4
      
   
   spacebar = pyxel.btn(pyxel.KEY_SPACE)
      
   if not spacebar and switchbnce >0:
      if switchbnce == bncemax:
         Shooting = True
         switchbnce = 0
      else:
         switchbnce -=1

   if switchbnce < bncemax and spacebar:
      switchbnce +=1
   elif switchbnce == bncemax and spacebar and Shootingangle <= 1.55: #added Shootingangle limit
      Shootingangle += 3.14 / 50
      if Shootingforce <= 29:
         Shootingforce += 1
      draw_line = True

   if pyxel.btnp(pyxel.KEY_V):
      variables = not variables

   if b == 0:
      figure_frame = 0
   if b == -0:#??? somehow speed comes to rest at "-0" - this should fix???
      b = 0
    


   #if Shooting:
      #pyxel.cls(1)
      #pyxel.text(50, 10, f"OH SHOOT!!!!", 9)
      #stuff. . . .
      #time.sleep(2)
      #Shooting = False
      #Shootingforce = 0
      #Shootingangle = 0
      #don't uncomment this. . . .



def draw_shot_angle():
#   player_x = x + a
#   player_y = 70
   shot_line_length = 30

   pyxel.line(
      player_x - 5,
      player_y + 10,
      player_x + shot_line_length * math.cos(Shootingangle),
      player_y - shot_line_length * math.sin(Shootingangle),
      col=10
   )

def draw(): ###### ALL drawings must occur in this function or will be erased...
   pyxel.cls(1) ## because of this line here
   pyxel.rectb(78, 15, 30, 12, 13)
   if switchbnce == bncemax and not Shooting:
      pyxel.text(80,20,f"{Shootingforce}" , 3)
   if Shooting:
      pyxel.text(80, 20, "Shoot!!", 3)
   text_col = 9
   line_height = 8
   if variables:
      pyxel.text(10, 10, f"x{x:.1f}; y={y:.1f}, vx={vx:.1f}, vy={vy:.1f}", col=text_col)# For
      pyxel.text(10, 10 + line_height, f"a={a:.1f}; b={b:.1f}", col=text_col)# De
      pyxel.text(10, 10 + line_height * 2, f"shooting: {Shooting}; force: {Shootingforce}", col=text_col)# bug
      pyxel.text(10, 10 + line_height * 3, f"Shootingangle: {(180*Shootingangle/3.14)}", col=text_col)# ing
      pyxel.text(10, 10 + line_height * 4, f"switchbnce: {switchbnce}, BOUNCE: {BOUNCE}", col=text_col)# Temp
      pyxel.text(10, 10 + line_height * 5, f"spacebar: {spacebar}", col=text_col)# ora
      pyxel.text(10, 10 + line_height * 6, f"figure_frame: {figure_frame}", col=text_col)# ry
   if Shooting == False:
      pyxel.circ(x + a, y, 4, 9) #
   else: 
      pyxel.circ(x + a, y, 4, 9) # fill in what ball does when thrown
   draw_figure(x + a - 42            , 62, figure_frame) # Position of figure
   if draw_line:
      draw_shot_angle()
   netxpos = 155
   pyxel.line(netxpos, 120, netxpos, 50, 12) #Post
   pyxel.line(netxpos, 50, netxpos, 15, 7) #backboard
   pyxel.line(netxpos + 1, 50, netxpos + 1, 15, 7) #backboard thickness
   pyxel.line(netxpos, 40, 133, 40, 8) #Hoop
   pyxel.line(netxpos - 5, 41, 150, 50, 7)#N
   pyxel.line(netxpos -10, 41, 145, 50, 7)#E
   pyxel.line(netxpos - 15, 41, 140, 50, 7)#T
   pyxel.line(netxpos -20, 41, 135, 50, 7)
   pyxel.line(netxpos, 42, 133, 42, 7)#crossnet (horizontal) threads
   pyxel.line(netxpos, 45, 133, 45, 7)
   pyxel.line(netxpos, 48, 133, 48, 7)

pyxel.run(update, draw          ) # to commit:   git status     git add -A     git commit -m "some message"    git push    git status   clear