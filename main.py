from gpiozero import RotaryEncoder, RGBLED, Button
from signal import pause
from time import *
from art import tprint
import random
import json
import time

# Variables
code = [0, 0, 0, 0]
maxsteps = 30
inputs = []
index = 0

# Couleurs
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ledcolors:
    YELLOW = (1, 1, 0.2)
    GREEN = (0, 1, 0) 
    BLUE = (0, 0, 1)
    RED = (1, 0, 0)
    OFF = (0, 0, 0)

# GPIO setup
rotor = RotaryEncoder(17, 27, max_steps=maxsteps)
led = RGBLED(red=10, green=9, blue=11)
button = Button(22)

# Génération du code
for i in range(len(code)):
    code[i] = random.randint(-maxsteps,maxsteps)

# Initialisation de la partie
tprint("Code Cracker","3d_diagonal")

username = input(f"\n{bcolors.HEADER}{bcolors.BOLD}>> Entrez votre nom d'utilisateur:{bcolors.ENDC}\n")

print(f"""
{bcolors.OKCYAN}{bcolors.BOLD}Prêt(e) {username}?{bcolors.ENDC}
Essaiez de trouver {bcolors.BOLD}4{bcolors.ENDC} nombres entre {bcolors.UNDERLINE}-30 et 30{bcolors.ENDC} !

{bcolors.OKCYAN}{bcolors.BOLD}Couleurs:{bcolors.ENDC}
{bcolors.OKGREEN}Vert:{bcolors.ENDC} Nombre correcte
{bcolors.FAIL}Rouge:{bcolors.ENDC} Nombre incorrecte
{bcolors.OKBLUE}Bleu:{bcolors.ENDC} Mauvais nombre mais proche du bon
{bcolors.WARNING}Jaune:{bcolors.ENDC} Vous avez cracké le coffre-fort
""")

input(f"\n{bcolors.HEADER}>> Appuiez sur ENTER pour démarrer votre chrono...{bcolors.ENDC}\n")

print(f"\n{bcolors.WARNING}Le chrono a démarré !{bcolors.ENDC}\n")

# Début du chrono
st = time.time()

# Fonctions
def ledColor(compteur):
  global index
  global code

  if compteur == code[index]:
    led.color = ledcolors.GREEN
  elif abs(compteur) == maxsteps:
    led.color = ledcolors.OFF
  elif compteur < (code[index] - 10):
    led.color = ledcolors.RED
  elif compteur > (code[index] + 10):
    led.color = ledcolors.RED
  else:
    led.color = ledcolors.BLUE

startCompteir = rotor.value * maxsteps
ledColor(startCompteir)

def rotated():
  global index
  global code

  compteur = rotor.value * maxsteps

  ledColor(compteur)

  print(f"Valeur actuelle: {compteur}")

def confirm():
  global index
  global st
  global username

  compteur = rotor.value * maxsteps

  if compteur == code[index]:
    inputs.append(compteur)
    index += 1
    print(f"\n{bcolors.OKGREEN}{compteur} est un nombre correcte !{bcolors.ENDC}\n")
    if len(inputs) == len(code):
      newtime = '%.2f' % (time.time() - st)
      newtime = float(newtime)

      print(f"{bcolors.OKGREEN}Vous avez ouvert le coffre-fort !{bcolors.ENDC}\n{bcolors.OKCYAN}Combinaison:{bcolors.ENDC} {code}")
      
      new_player = {'name': f'{username}', 'time': newtime}

      with open('scores.json') as file:
          olddata = json.load(file)

      old_sorted_times = sorted(olddata['players'], key=lambda k: float(k['time']))

      if newtime < old_sorted_times[0]['time']:
        print(f"{bcolors.WARNING}Temps: {bcolors.FAIL}{bcolors.BOLD}{newtime}{bcolors.ENDC}{bcolors.WARNING} secondes{bcolors.ENDC} {bcolors.OKCYAN}({bcolors.OKGREEN}Nouveau Record !{bcolors.OKCYAN}){bcolors.ENDC}")
      elif newtime < old_sorted_times[1]['time']:
        print(f"{bcolors.WARNING}Temps: {bcolors.FAIL}{bcolors.BOLD}{newtime}{bcolors.ENDC}{bcolors.WARNING} secondes{bcolors.ENDC} {bcolors.OKCYAN}({bcolors.OKGREEN}Nouveau Top 2 !{bcolors.OKCYAN}){bcolors.ENDC}")
      elif newtime < old_sorted_times[2]['time']:
        print(f"{bcolors.WARNING}Temps: {bcolors.FAIL}{bcolors.BOLD}{newtime}{bcolors.ENDC}{bcolors.WARNING} secondes{bcolors.ENDC} {bcolors.OKCYAN}({bcolors.OKGREEN}Nouveau Top 3 !{bcolors.OKCYAN}){bcolors.ENDC}")
      else:
        print(f"{bcolors.WARNING}Temps: {bcolors.FAIL}{bcolors.BOLD}{newtime}{bcolors.ENDC}{bcolors.WARNING} secondes{bcolors.ENDC}")

      with open('scores.json', 'r') as file:
          data = json.load(file)  

      data["players"].append(new_player)

      with open('scores.json', 'w') as file:
        json.dump(data, file)

      with open('scores.json') as file:
          newdata = json.load(file)

      sorted_times = sorted(newdata['players'], key=lambda k: float(k['time']))

      print(f"\n{bcolors.HEADER}{bcolors.BOLD}Les 5 meilleurs chronos sont:{bcolors.ENDC}")
      print(f"1. {bcolors.OKGREEN}{sorted_times[0]['name']}{bcolors.ENDC} - {sorted_times[0]['time']} secondes")
      print(f"2. {bcolors.WARNING}{sorted_times[1]['name']}{bcolors.ENDC} - {sorted_times[1]['time']} secondes")
      print(f"3. {bcolors.FAIL}{sorted_times[2]['name']}{bcolors.ENDC} - {sorted_times[2]['time']} secondes")
      print(f"4. {sorted_times[3]['name']} - {sorted_times[3]['time']} secondes")
      print(f"5. {sorted_times[4]['name']} - {sorted_times[4]['time']} secondes")

      exit()
  elif compteur != code[index]:
    print(f"\n{bcolors.FAIL}{compteur} est un nombre incorrecte !{bcolors.ENDC}\n")
  
  ledColor(compteur)

# Event Listener
rotor.when_rotated = rotated
button.when_pressed = confirm

# Petite pause
pause()