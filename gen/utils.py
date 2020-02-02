from . import styles
import subprocess


class Module:
    def __init__(self, height):
        self.lines = [' ' * 34 for _ in range(height)]

    def set_line(self, index, line):
        self.lines[index] = line[:35]

    def get(self, command):
        out = subprocess.Popen(command,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
        return out.communicate()[0]


def bar(length, num, of, color='highlight'):
    n = round(num / of * (length - 2))
    return f"{styles.fg['normal']}[{styles.fg[color]}{'=' * n}{styles.fg['disabled']}{'=' * (length - n)}{styles.fg['normal']}]"
