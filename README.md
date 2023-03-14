<br/>
  <p align="center">
  <a href="https://www.flaticon.com/free-icons/safe-boxs">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Code Cracker</h3>

  <p align="center">
    Projet Raspberry Pi créé dans le cadre du projet transversal de l'EPHEC
   </p>
</p>

[![license - MIT](https://img.shields.io/badge/license-MIT-green?logo=github&logoColor=white)](https://choosealicense.com/licenses/mit/)

[![langage - pyhton](https://img.shields.io/badge/langage-pyhton-yellow?logo=Python&logoColor=white)](https://www.python.org/)

[![Dependency - art](https://img.shields.io/badge/dependency-art-orange?logo=Raspberry+Pi&logoColor=white)](https://pypi.org/project/art)
[![Dependency - gpiozero](https://img.shields.io/badge/dependency-gpiozero-blue?logo=Raspberry+Pi&logoColor=white)](https://pypi.org/project/gpiozero)
[![Dependency - flask](https://img.shields.io/badge/dependency-flask-red?logo=flask&logoColor=white)](https://pypi.org/project/flask)

## Demo

![](https://github.com/Simon-Fontaine/codecracker/blob/main/images/demo.gif)

## Installation

```bash
  sudo su
  apt update
  apt dist-upgrade -y
  apt install -y python3-pip git bpython

  git clone https://github.com/Simon-Fontaine/codecracker.git
  cd codecracker
  pip install flask art gpiozero
```

## Starting App

Pour démarrer l'application, exécutez la commande suivante dans sons dossier

```bash
  pyhton main.py
```

## Environment Variables

Ce projet utilise certaines variables, elles sont situées dans le fichier `main.py` et se situent entre les lignes 9 et 14.

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
