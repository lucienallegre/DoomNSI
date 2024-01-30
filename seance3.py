# Séance 3 du 30/01/2024
# création des appuies long pour avancer

# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg
# import des fonctions trigo du module math
from math import cos, sin

# création de la fenêtre pour le plan 2D
# résolution : 320x200 (comme le Doom de l'époque)
window2d = pg.window.Window(320, 200, "Plan 2D", vsync=False)

# variables globales 
x, y, a = 160, 100, 0 # position et angle du joueur
# "batch" du joueur
joueur = pg.graphics.Batch()

actions = { "avancer" : False , "reculer" : False , "left" : False , "right" : False }
# left = gauche right = droite . Pour toujour avancer quand on presse une seul fois 

# détection d'un touche pressée au clavier
@window2d.event
def on_key_press(symbol, modifiers):
  print("Touche pressée n°", symbol)
  # Touche Q : on quitte le jeu  
  if symbol == pg.window.key.Q: pg.app.exit()
  # touches de déplacement
  if symbol == pg.window.key.DOWN:# reculer
      actions["reculer"] = True
      # x -= 20*cos(a)
      # y -= 20*sin(a)
  if symbol == pg.window.key.UP: # avancer
      actions["avancer"] = True
      # x += 20*cos(a)
      # y += 20*sin(a)
  # touches pour pivoter
  if symbol == pg.window.key.LEFT:
      actions["left"] = True
  if symbol == pg.window.key.RIGHT:
      actions["right"] = True

# détection d'un touche relâchée au clavier
@window2d.event
def on_key_release(symbol, modifiers):
    print("Touche relâchée n°", symbol)
    if symbol == pg.window.key.DOWN:
        actions["reculer"] = False
    if symbol == pg.window.key.UP:
        actions["avancer"] = False
    if symbol == pg.window.key.LEFT:
        actions["left"] = False
    if symbol == pg.window.key.RIGHT:
        actions["right"] = False

# évènement principal : rendu graphique
@window2d.event
def on_draw():
    global x, y, a
    window2d.clear()
    # le joueur comme un cercle
    circle = pg.shapes.Circle(x, y, 10, color =(50, 225, 30), batch = joueur)
    # segment "vecteur vitesse" qui pointe vers la direction de visée
    visée = pg.shapes.Line(x, y, x + 20*cos(a), y + 20*sin(a), width=5, batch = joueur)
    # on dessine le "batch"
    joueur.draw()
    
def update(dt):
    global x, y, a
    
    # touches de déplacement
    if actions["reculer"]:
        x -= 20 * cos(a)
        y -= 20 * sin(a)
    if actions["avancer"]:
        x += 20 * cos(a)
        y += 20 * sin(a)
    
    # touches pour pivoter
    if actions["left"]:
        a += 0.5  # rotation gauche
    if actions["right"]:
        a -= 0.5  # rotation droite

# def de la fonctionde mise a jour automatique     
pg.clock.schedule_interval(update, 1/60.0)

# lancement du jeu
pg.app.run()