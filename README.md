```

░█████╗░██╗██████╗░██████╗░███╗░░██╗██████╗░  ░█████╗░██╗░░░░░░█████╗░███╗░░██╗███████╗
██╔══██╗██║██╔══██╗██╔══██╗████╗░██║██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔════╝
███████║██║██████╔╝██████╦╝██╔██╗██║██████╦╝  ██║░░╚═╝██║░░░░░██║░░██║██╔██╗██║█████╗░░
██╔══██║██║██╔══██╗██╔══██╗██║╚████║██╔══██╗  ██║░░██╗██║░░░░░██║░░██║██║╚████║██╔══╝░░
██║░░██║██║██║░░██║██████╦╝██║░╚███║██████╦╝  ╚█████╔╝███████╗╚█████╔╝██║░╚███║███████╗
╚═╝░░╚═╝╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚══╝╚═════╝░  ░╚════╝░╚══════╝░╚════╝░╚═╝░░╚══╝╚══════╝
```

![AirBnB](assets/hbnb_logo.png)

## DESCRIPTION

**AirBnB** is a *complete web application*, integrating database storage, a back-end API, and front-end interface.

This is part 1 of our AirBnb Clone project. The purpose of this project is to make a command interpreter that manages our AirBnb objects.

#### Data Diagram

![data_diagram](assets/data_diagram.jpg)

## CONCEPTS LEARNT

-    How to create a Python package
-    How to create a command interpreter in Python using the `cmd` module
-    What is Unit testing and how to implement it in a large project
-    How to serialize and deserialize a Class
-    How to write and read a JSON file
-    How to manage `datetime`
-    What is an `UUID`
-    What is `*args` and how to use it
-    What is `**kwargs` and how to use it
-    How to handle named arguments in a function

## SYNOPSIS

#### Starting the Commandline Interpreter
The Commandline Interpreter can be started by executing the command `./console.py`. The `console` can `create`, `destroy`, and `update` objects. Type `help` within the console to get a list of command options and its function.

**Example:**
```bash
firdaus@ubuntu:~$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  create  help  quit

Undocumented commands:
======================
all  destroy  show  update

(hbnb) help quit
Quit command to exit the program
(hbnb) quit
firdaus@ubuntu:~$
```
### OBJECTS IMPLEMENTED
This repository contains the following files:

| Folder | File | Description |
| :--- | :--- | :--- |
| tests |  | Contains test files for AirBnb Clone |
|  | console.py | Command line Interpreter for managing AirBnB objects |
| models | base_model.py | Defines all common attributes/methods for other classes |
| models | amenity.py | Creates class `amenity` |
| models | city.py | Creates class `city` |
| models | place.py | Creates class `place` |
| models | review.py | Creates class `review` |
| models | state.py | Creates class `state` |
| models | user.py | Creates class `user` |
| models/engine/ | file_storage.py | Serializes instances to a JSON file and deserializes JSON file to instances |
| To be updated |

