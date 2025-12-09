import pyxel

GRAVITY = 0.3
BOUNCE = .7
W, H = 160, 120
a = 0
b = 1

pyxel.init(W, H, "Some name")

figure_image = pyxel.Image.from_image("../assets/New Piskel.png", incl_colors=True)
pyxel.images[0] = figure_image

def draw_figure(figure_x, figure_y, figure_tile):
   figure_height = figure_image.height / 8
   pyxel.blt(
      figure_x,
      figure_y,
      0,
      0,
      0,

      figure_image.width,
      figure_height,
   )

figure_frame = 0


# initial position and velocity
x, y = W // 2, H // 1.2
vx, vy = 0, 0

#pyxel.rect(1, 2, 3, 4, 5)
def update():
   global x, y, vx, vy, a, b

   # Apply gravity
   vy += GRAVITY
   y += vy
   a += b
   if b >= 0:
      b -=0.01
   # Bounce when hitting the ground
   ground = H - 5 #to change if ball radius changes - radius + 1
   if y > ground:
       y = ground
       vy = -vy * BOUNCE # reverse and lose some energy

def draw():
   pyxel.cls(1)
   pyxel.circ(x + a, y, 4, 9)
   draw_figure(x + a - 65, 55, 0) # Position of figure


pyxel.run(update, draw)