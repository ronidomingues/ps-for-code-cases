from typing import Optional
class Colors:
    def __init__(self) -> None:
        self.ANSI_COLORS = {
            # Cores padrão ANSI (8 normais)
            "BLACK": "\033[30m",
            "RED": "\033[31m",
            "GREEN": "\033[32m",
            "YELLOW": "\033[33m",
            "BLUE": "\033[34m",
            "MAGENTA": "\033[35m",
            "CYAN": "\033[36m",
            "WHITE": "\033[37m",
            # Cores brilhantes (Bright)
            "BLACK_BRIGHT": "\033[90m",   # Também conhecido como cinza/gray
            "RED_BRIGHT": "\033[91m",
            "GREEN_BRIGHT": "\033[92m",
            "YELLOW_BRIGHT": "\033[93m",
            "BLUE_BRIGHT": "\033[94m",
            "MAGENTA_BRIGHT": "\033[95m",
            "CYAN_BRIGHT": "\033[96m",
            "WHITE_BRIGHT": "\033[97m",
            # Estilo
            "BOLD": "\033[1m",
            "RESET": "\033[0m"
        }
    def style(self, property: str) -> Optional[str]:
        if type(property) == str:
            property = property.strip()
            property = property.upper()
            property = property.split()
        else:
            return None
        apply_prop = ""
        for prp in property:
            if prp in self.ANSI_COLORS.keys():
                apply_prop += self.ANSI_COLORS[prp]
        return apply_prop
    def apply(self, text: str, property: str) -> str:
        return f"{self.style(property)}{text}{self.ANSI_COLORS['RESET']}"

obj = Colors()
print(obj.style("green"))
print("Olá Mundo!")