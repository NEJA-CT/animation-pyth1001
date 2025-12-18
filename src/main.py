import pyxel

GRAVITY = 0.3
BOUNCE = .75
W, H = 160, 120
a = 0
b = 1

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
x, y = W // 2, H // 2
vx, vy = 0, 0

#pyxel.rect(1, 2, 3, 4, 5)
def update():
   global x, y, vx, vy, a, b, figure_frame

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
   figure_frame = int(pyxel.frame_count / 4) % 4

def draw():
   pyxel.cls(1)
   pyxel.circ(x + a, y, 4, 9) # col originally 9 b4 incl_colors=True
   draw_figure(x + a - 45, 62, figure_frame) # Position of figure


pyxel.run(update, draw) # to commit:   git status     git add -A     git commit -m "some message"    git push    git status   clear