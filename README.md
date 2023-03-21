<br/>
<p align="center">
  <a href="https://www.flaticon.com/free-icons/safe-boxs" target="_blank">
    <img src="images/logo.png" alt="Logo" width="120" height="120">
  </a>

  <h1 align="center">Code Cracker</h1>

  <p align="center">
    Projet Raspberry Pi créé dans le cadre du projet transversal de l'EPHEC
   </p>
</p>

[![license - MIT](https://img.shields.io/badge/license-MIT-green?logo=github&logoColor=white)](https://choosealicense.com/licenses/mit/)

[![langage - pyhton](https://img.shields.io/badge/langage-pyhton-yellow?logo=Python&logoColor=white)](https://www.python.org/)

[![Dependency - art](https://img.shields.io/badge/dependency-art-orange?logo=Raspberry+Pi&logoColor=white)](https://pypi.org/project/art)
[![Dependency - gpiozero](https://img.shields.io/badge/dependency-gpiozero-blue?logo=Raspberry+Pi&logoColor=white)](https://pypi.org/project/gpiozero)
[![Dependency - flask](https://img.shields.io/badge/dependency-flask-red?logo=flask&logoColor=white)](https://pypi.org/project/flask)
[![dependency - turbo-flask](https://img.shields.io/badge/dependency-turbo--flask-2ea44f?logo=flask)](https://pypi.org/project/Turbo-Flask/)

## Table Of Contents

- [Demo](#demo)
  - [Console](#console)
  - [Web](#web)
- [Installation](#installation)
- [Connections](#connections)
  - [RotaryEncoder](#rotaryencoder)
  - [RGBLED](#rgbled)
- [Starting App](#starting-app)
  - [Console](#console-1)
  - [Web](#web-1)
- [Environment Variables](#environment-variables)
  - [Console](#console-2)
  - [Web](#web-2)
- [Authors](#authors)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Demo

### Console

![](https://github.com/Simon-Fontaine/codecracker/blob/main/images/demo_console.gif)

### Web

![](https://github.com/Simon-Fontaine/codecracker/blob/main/images/demo_web.gif)

## Installation

```bash
  sudo su
  apt update
  apt dist-upgrade -y
  apt install -y python3-pip git bpython

  git clone https://github.com/Simon-Fontaine/codecracker.git
  cd codecracker
  pip install flask turbo_flask art gpiozero
```

## Connections

![connections](https://github.com/Simon-Fontaine/codecracker/blob/main/images/connections-nobg.png)

[Correct Pin Layout](https://github.com/Simon-Fontaine/codecracker/blob/main/images/rp2_pinout.png)

### RotaryEncoder

- `CLK` **[13]** GPIO 27
- `DT` **[11]** GPIO 17
- `SW` **[15]** GPIO 22
- `+` **[1]** 3.3V PWR
- `GND` **[9]** GND

### RGBLED

- `RED` **[19]** GPIO 10
- `GREEN` **[21]** GPIO 9
- `BLUE` **[23]** GPIO 11
- `GND` **[6]** GND

## Starting App

Pour démarrer l'application, exécutez la commande suivante dans sons dossier

### Console

```bash
  pyhton main.py
```

### Web

```bash
  flask run --host=0.0.0.0
```

## Environment Variables

Ce projet utilise certaines variables,

### Console

Elles sont situées dans le fichier [main.py](https://github.com/Simon-Fontaine/codecracker/blob/main/console/main.py) et se situent entre les lignes 9 et 14.

### Web

Elles sont situées dans le fichier [app.py](https://github.com/Simon-Fontaine/codecracker/blob/main/web/app.py) et se situent entre les lignes 21 et 31.

`code` (default: [0, 0, 0, 0]) _La longueur du code à trouver_

`MAX_STEPS` (default: 30) _Intervalle de nombres possibles trouver_

## Authors

- [@Simon-Fontaine](https://github.com/Simon-Fontaine)
- [@Bistouflere](https://github.com/Bistouflere)
- [@bpatureau](https://github.com/bpatureau)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgements

- [Safe box icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/safe-boxs)
