import pyxel

GRAVITY = 0.3
BOUNCE = .75
switchbnce = 0
W, H = 160, 120
a = 0
b = 1
Shooting = False
Shootingforce = 0
Shootingangle = 0
spacebar = False

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
   global x, y, vx, vy, a, b, figure_frame, Shooting, switchbnce, Shootingforce, Shootingangle, BOUNCE, spacebar

   # Apply gravity
   vy += GRAVITY
   y += vy
   a += b
   if b >= 0:
      b -=0.01
   # Bounce when hitting the ground
   ground = H - 5 #to change if ball radius changes - radius + 1
  
  
   if Shooting == False:
      BOUNCE = 1
   else:
      BOUNCE = .75


   if y > ground:
       y = ground
       vy = -vy * BOUNCE # reverse and lose some energy
 
 
   if pyxel.btnp(pyxel.KEY_D):
      b += .2
   elif pyxel.btnp(pyxel.KEY_A):
     b -=.2 
   
   
   if b >= 0 :
      figure_frame = int(pyxel.frame_count / 4) % 4
      
   
   if not spacebar:
      spacebar = pyxel.btnp(pyxel.KEY_SPACE)
      switchbnce = 0

   if switchbnce <25 and spacebar:
      switchbnce +=1
   elif switchbnce == 25 and spacebar:
      switchbnce = 0
      if Shootingforce <= 10:
         Shootingforce += 1
      if not pyxel.btnp(pyxel.KEY_SPACE):
         Shooting = True
         spacebar = pyxel.btnp(pyxel.KEY_SPACE)
      


  
 #  switchbnce=0
   #if pyxel.btnp(pyxel.KEY_SPACE):

      #switchbnce+=1
      
#      if Shootingforce <= 10:
 #        Shootingforce += 1
            
  #    if Shootingforce >= 1:
   #   Shooting = True

      
def draw():
   pyxel.cls(1)
   if Shooting == False:
      pyxel.circ(x + a, y, 4, 9) # col originally 9 b4 incl_colors=True
   else: pyxel.circ(x + a, y, 4, 9) # fill in what ball does when thrown 
   draw_figure(x + a - 43, 62, figure_frame) # Position of figure


pyxel.run(update, draw) # to commit:   git status     git add -A     git commit -m "some message"    git push    git status   clear