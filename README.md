# GUI

Use animation functions of matplotlib package, get it animated.

This project including [in.txt](https://github.com/hahatori/GUI/blob/master/in.txt), [data.py](https://github.com/hahatori/GUI/blob/master/data.py), [agentframework.py](https://github.com/hahatori/GUI/blob/master/agentframework.py) and [model.py](https://github.com/hahatori/GUI/blob/master/model.py).

## Contents

- [Details](#details)
- [Theoretical Results](#theoretical-results)
- [Actual Results](#actual-results)
- [Issues](#issues)

## Details

### The key elements:

**in.txt** is a text file with raster data.

**Agent** code can build agents to interact.

**Model** code can creat models for connecting developers and users.

### Tkinter

**Tkinter** is the standard GUI library for Python which is built into the Python installation package. Python uses Tkinter to quickly create GUI applications.

```sh
$ import tkinter
```

### Tkinter components

There are currently 15 Tkinter components, such as **buttons**, **labels**, and **Canvas**.

### root

**root** is a main window object.

Create the main window:

```sh
$ root = tkinter.TK()
```
All the components need to be attached to the interface:

```sh
$ from tkinter import *

  root = tkinter.Tk()
  root.wm_title("Model")
  root.geometry('500x500')
  root.mainloop()
```

## Theoretical Results

The model refers to methods such as ```eat``` ，```move``` and ```share_with_neighbours``` from the **agentframework.py**, which are shown on the animation.

## Actual Results

![GUI](https://github.com/hahatori/Python_Assignment1/blob/master/GUI2.mov)

## Issues

1. 

2. 
