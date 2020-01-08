# GUI

Use animation functions of matplotlib package, get it animated.

This project including [in.txt](https://github.com/hahatori/GUI/blob/master/in.txt), [data.py](https://github.com/hahatori/GUI/blob/master/data.py), [agentframework.py](https://github.com/hahatori/GUI/blob/master/agentframework.py) and [model.py](https://github.com/hahatori/GUI/blob/master/model.py).

## Contents

- [Details](#details)
- [Theoretical Results](#theoretical-results)
- [Actual Results](#actual-results)
- [Issues](#issues)
- [License](#license)

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

### Canvas

**Canvas** provides drawing for Tkinter. Its graphics components include lines, circles, pictures, and other controls.

The Canvas control can draw graphical charts, edit graphics, and customize components for windows.

```sh
$ canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)  # Display the components.
```

## Theoretical Results

Modify the IPython console to run to produce a separate window, called "My Model". The top left corner displays the window menu called "Model". Click on the menu displays a drop-down list named "Run model", continuing to click on it，displays an scatter plot animation.

## Actual Results

![GUI](https://github.com/hahatori/Python_Assignment1/blob/master/GUI2.mov)

## Issues

1. **menu**, equivalent to a menu group \ menu bar, does not add other menus when the default is not displayed, only add other menus, will be displayed. To display menus, you must allow menu objects to be added in config for window objects to add menus, for example, ```root.config(menu=menu_bar)```. Menu has no text.

2. Two windows appeared: **My Model** and **Figure 1**. Tried to remove the Figure 1 window, but failed.

## License

[MIT](https://github.com/hahatori/Python_Assignment1/blob/master/License)© Tori


