from .config import config
from colorama import Fore, Back, Style


colors_fg = {
    'black': Fore.BLACK,
    'red': Fore.RED,
    'green': Fore.GREEN,
    'yellow': Fore.YELLOW,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'cyan': Fore.CYAN,
    'white': Fore.WHITE,
}

colors_bg = {
    'black': Back.BLACK,
    'red': Back.RED,
    'green': Back.GREEN,
    'yellow': Back.YELLOW,
    'blue': Back.BLUE,
    'magenta': Back.MAGENTA,
    'cyan': Back.CYAN,
    'white': Back.WHITE,
}

styles = {
    'bold': Style.BRIGHT
}

colors = config['colors']

fg, bg = {}, {}
for c in colors.keys():
    fg[c] = colors_fg[colors[c]]
    bg[c] = colors_bg[colors[c]]
