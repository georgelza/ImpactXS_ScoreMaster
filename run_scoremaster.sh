#!/bin/bash

export DEBUGLEVEL=2
export LOGLEVEL=DEBUG
export ECHOJSON=1
export SPLASHTIME=1000

# tree or flat
export SCORE_VIEWER=flat

# Colors
export frame_bg=lightgray
export label_text_bg=lightgray
export label_text_fg=black
export entry_text_bg=white
export entry_text_fg=black
export txtfont=arial
export txtfont_size=14
export lblfont=Consolas
export lblfont_size=16
export lblframefont=Consolas
export lblframefont_size=16

# Consolas or Arial
# Ghost White or cadet blue

python main.py
