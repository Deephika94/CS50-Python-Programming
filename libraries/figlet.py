import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv)==1:
    txt = input("Text: ")
    input_font = random.choice(fonts)
elif len(sys.argv)==3:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":
        txt = input("Text: ")
        if sys.argv[2] in fonts:
            input_font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")


figlet.setFont(font=input_font)
print(figlet.renderText(txt))



