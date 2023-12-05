# Séance 1 du 05/12/2023
# Prise en main de Pyglet : création d'une fenêtre, détection d'une touche pressée/relâchée

# module pyglet principal (qu'on nenomme en pg pour plus de simplicité)
import pyglet as pg

# création de la fenêtre pour le plan 2D
# résolution : 320x200 (comme le Doom de l'époque)
window2d = pg.window.Window(320, 200, "Plan 2D", vsync=False)

# détection d'un touche pressée au clavier
@window2d.event
def on_key_press(symbol, modifiers):
  print("Touche pressée n°", symbol)
  # Touche Q : on quitte le jeu  
  if symbol == pg.window.key.Q: pg.app.exit() 

# détection d'un touche relâchée au clavier
@window2d.event
def on_key_release(symbol, modifiers):
    print("Touche relâchée n°", symbol)

# évènement principal : rendu graphique
@window2d.event
def on_draw():
    window2d.clear()

# lancement du jeu
pg.app.run()
