from structure import Renderer, color, V2
import random

width = 1920
height = 1080

rend = Renderer(width, height) # Los parámetros son pixeles.

v01 = V2(width/6, height/4) # Desde la equina inferior izquierda.
v02 = V2(width/2, height/2) # En medio
v03 = V2(width/2, height/4) # En medio a la izquierda
v04 = V2(width/4, height/2) # En medio a la derecha
# v0 = V2(0,0) # Desde la esquina

# Rectángulo
rend.glLine(v01, V2((width/7)*2,height/4)) # abajo
rend.glLine(v01, V2(width/6,height/2.5)) # vertical izq
rend.glLine(V2(width/6,height/2.5), V2((width/7)*2,height/2.5)) # arriba
rend.glLine(V2((width/7)*2,height/2.5), V2((width/7)*2,(height/4))) # vertical derecha

# Triángulo
rend.glLine(v03, V2(width/2,height/2.5))
rend.glLine(v03, V2((width/2.5),height/4))
rend.glLine(V2((width/2.5),height/4), V2(width/2,height/2.5))

# Pentágono
rend.glLine(V2((width/6)*4.07,height/2),V2((width/3)*2.25, height/2))
rend.glLine(V2((width/3)*2.25, height/2), V2((width/8)*6.3,(height/8)*5))
rend.glLine(V2((width/6)*4.07,height/2), V2((width/8)*5.12  ,(height/8)*5))
rend.glLine(V2((width/8)*5.12 ,(height/8)*5), V2((width/4)*2.87,(height/3)*2.2))
rend.glLine(V2((width/4)*2.87,(height/3)*2.2), V2((width/8)*6.3,(height/8)*5))

# Hexágono
rend.glLine(V2((width/6)*4.07,height/4),V2((width/3)*2.25, height/4))
rend.glLine(V2((width/6)*4.07,(height/5)*2.1),V2((width/3)*2.25, (height/5)*2.1))
## izquierda
rend.glLine(V2((width/6)*4.07, height/4),V2((width/6)*3.9,(height/5)*1.682))
rend.glLine(V2((width/6)*4.07, (height/5)*2.1),V2((width/6)*3.9,(height/5)*1.682))
## derecha
rend.glLine(V2((width/3)*2.25, height/4),V2((width/6)*4.66,(height/5)*1.682))
rend.glLine(V2((width/3)*2.25, (height/5)*2.1),V2((width/6)*4.66,(height/5)*1.682))

# Diamante
rend.glLine(V2((width/6)*1.4,height/2), V2((width/6)*1.7, (height/8)*5))
rend.glLine(V2((width/6)*1.4,height/2), V2((width/6)*1.1, (height/8)*5))
rend.glLine(V2((width/6)*1.4,(height/3)*2.25), V2((width/6)*1.7, (height/8)*5))
rend.glLine(V2((width/6)*1.4,(height/3)*2.25), V2((width/6)*1.1, (height/8)*5))

rend.glFinish('output.bmp')