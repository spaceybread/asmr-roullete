import webbrowser
import random

while True:
    input('Pull the trigger')

    time = random.randrange(2, 1163)

    asmr = "https://www.youtube.com/watch?v=3Q2QDwQXOZA&t={}".format(str(time))
    ting = "https://www.youtube.com/watch?v=okuTl9MGxgI&t=1"

    revolver = [asmr, asmr, asmr, asmr, asmr, ting, asmr, asmr, asmr, asmr, asmr]

    bullet = random.choice(revolver)

    webbrowser.open(bullet)
