#!/bin/bash

export DEBUGLEVEL=2
export LOGLEVEL=DEBUG
export SPLASHTIME=1000

# Colors
export frame_bg=lightgray
export frame_fg=black
export label_text_bg=lightgray
export label_text_fg=black
export entry_text_bg=white
export entry_text_fg=black
export txtfont=arial
# Consolas
export txtfont_size=14
export lblfont=Consolas
export lblfont_size=16
export lblframefont=Consolas
export lblframefont_size=16

# Ghost White
# cadet blue

python main.py
