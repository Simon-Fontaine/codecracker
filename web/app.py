import random
import re
import sys
import threading
import time
import json
from flask import Flask, render_template, request
from gpiozero import RotaryEncoder, Button, RGBLED
from turbo_flask import Turbo


MAX_STEPS = 30

rotor = RotaryEncoder(17, 27, max_steps=MAX_STEPS)
led = RGBLED(red=10, green=9, blue=11)
button = Button(22)

class ledcolors:
    YELLOW = (1, 1, 0.2)
    GREEN = (0, 1, 0) 
    BLUE = (0, 0, 1)
    RED = (1, 0, 0)
    OFF = (0, 0, 0)

app = Flask(__name__)
turbo = Turbo(app)

code = [0, 0, 0, 0]
guess = []
sorted_times = []
codeindex = 0
compteur = int(rotor.value * MAX_STEPS)  
confirm_phrase = ""
sorted_times_phrase = ""
color_check = "white"
color_value = "white"
name = ""

started = False
finished = False

start_time = time.time()
stop_time = time.time()

for i in range(len(code)):
    code[i] = random.randint(-MAX_STEPS,MAX_STEPS)

def reset():
  global code
  global guess
  global codeindex
  global compteur
  global confirm_phrase
  global sorted_times_phrase
  global color_check
  global color_value
  global started
  global finished
  global start_time
  global stop_time

  code = [0, 0, 0, 0]
  guess = []
  codeindex = 0
  compteur = int(rotor.value * MAX_STEPS) 
  confirm_phrase = ""
  sorted_times_phrase = ""
  color_check = "white"
  color_value = "white"
  started = False
  finished = False
  start_time = time.time()
  stop_time = time.time()

  for i in range(len(code)):
    code[i] = random.randint(-MAX_STEPS,MAX_STEPS)

  ledColor(compteur)

def ledColor(compteur):
  global codeindex
  global code

  if len(guess) == len(code):
    led.color = ledcolors.YELLOW
  elif compteur == code[codeindex]:
    led.color = ledcolors.GREEN
  elif abs(compteur) == MAX_STEPS:
    led.color = ledcolors.OFF
  elif compteur < (code[codeindex] - 10):
    led.color = ledcolors.RED
  elif compteur > (code[codeindex] + 10):
    led.color = ledcolors.RED
  else:
    led.color = ledcolors.BLUE


ledColor(compteur)

def couleur():
  global color_value
  if len(guess) == len(code):
    color_value = "white"
  elif compteur == code[codeindex]:
    color_value = "green"
  elif abs(compteur) == MAX_STEPS:
    color_value = "white"
  elif compteur < (code[codeindex] - 10):
    color_value = "red"
  elif compteur > (code[codeindex] + 10):
    color_value = "red"
  else:
    color_value = "blue"

def get_time():
  global start_time
  global stop_time

  if finished:
    stop_time = stop_time
  elif started:
    stop_time = '%.2f' % (time.time() - start_time)
    stop_time = float(stop_time)
  else:
    stop_time = 0

def get_sorted_times():
  global sorted_times

  with open('scores.json') as file:
    newdata = json.load(file)

  sorted_times = sorted(newdata['players'], key=lambda k: float(k['time']))

def rotated():
  with app.app_context():
    global code
    global guess
    global codeindex
    global compteur
    global started
    global start_time

    if not started:
      started = True
      start_time = time.time()
      return

    compteur = int(rotor.value * MAX_STEPS)  

    couleur()
    ledColor(compteur)
    get_time()

    turbo.push(turbo.replace(render_template('inputs.html'), 'inputs'))

def confirm():
  with app.app_context():
    global code
    global guess
    global codeindex
    global compteur
    global confirm_phrase
    global color_check
    global started
    global start_time
    global stop_time
    global finished
    global name
    global sorted_times
    global sorted_times_phrase

    if not started:
      started = True
      start_time = time.time()
      return

    compteur = int(rotor.value * MAX_STEPS)

    if len(guess) == len(code):
        confirm_phrase = f"Vous avez déjà ouvert le coffre-fort !"
        color_check = "orange"
    elif compteur == code[codeindex]:
      guess.append(compteur)
      codeindex += 1
      confirm_phrase = f"{compteur} est un nombre correcte"
      color_check = "green"
      if len(guess) == len(code):
        get_time()
        finished = True
        confirm_phrase = f"Vous avez ouvert le coffre-fort !"
        color_check = "orange"

        new_player = {'name': f'{name}', 'time': stop_time}

        with open('scores.json') as file:
            olddata = json.load(file)

        old_sorted_times = sorted(olddata['players'], key=lambda k: float(k['time']))

        if stop_time < old_sorted_times[0]['time']:
          sorted_times_phrase = f"(Nouveau Record !)"
        elif stop_time < old_sorted_times[1]['time']:
          sorted_times_phrase = f"(Nouveau Top 2 !)"
        elif stop_time < old_sorted_times[2]['time']:
          sorted_times_phrase = f"(Nouveau Top 3 !)"
        else:
          sorted_times_phrase = f""

        with open('scores.json', 'r') as file:
          data = json.load(file)  

        data["players"].append(new_player)

        with open('scores.json', 'w') as file:
          json.dump(data, file)

        get_sorted_times()

        turbo.push(turbo.replace(render_template('scores.html'), 'scores'))
        
    elif compteur != code[codeindex]:
      confirm_phrase = f"{compteur} est un nombre incorrecte !"
      color_check = "red"

    couleur()
    ledColor(compteur)
    get_time()
    
    turbo.push(turbo.replace(render_template('inputs.html'), 'inputs'))
    

@app.context_processor
def inject_load():
  global confirm_phrase
  global color_check
  global color_value
  global compteur
  global guess
  global stop_time

  couleur()
  ledColor(compteur)
  get_time()
  get_sorted_times()
  
  return {'name': name, 'sorted_times_phrase': sorted_times_phrase, 'sorted_times': sorted_times, 'rotatedphrase': compteur, 'guess': guess, 'confirmphrase': confirm_phrase, 'timer': stop_time, 'colorcheck': color_check, 'colorvalue': color_value}

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    reset()
    global name
    name =request.form['name']
    turbo.push(turbo.replace(render_template('inputs.html'), 'inputs'))
  return render_template('index.html')

rotor.when_rotated = rotated
button.when_pressed = confirm