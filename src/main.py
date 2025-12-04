import pyxel

GRAVITY = 0.3
BOUNCE = .7
W, H = 160, 120
a = 0
b = 1.15

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
   ground = H - 3 #to change if ball radius changes - radius + 1
   if y > ground:
       y = ground
       vy = -vy * BOUNCE # reverse and lose some energy

def draw():
   pyxel.cls(1)
   pyxel.circ(x + a, y, 2, 9)
pyxel.init(W, H, "Some name")
pyxel.run(update, draw)