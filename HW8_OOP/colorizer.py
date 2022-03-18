class Colorizer:
    colors = {
        'black': '\033[30m',
        'white': '\033[37m',
        'grey': '\033[90m',
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'turquoise': '\033[96m',
        'RESET': '\033[0m'
    }

    def __init__(self, color, text=None):
        self.color = color
        self.text = text

    def __enter__(self):
        print(f'{self.colors.get(self.color)}', end='')
        return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.colors.get('RESET')}", end='')
        return None


with Colorizer('red'):
    print('printed in red')
print("printed in default color")
