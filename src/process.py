import os

from PIL import ImageFont


from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1322

from open import isRun

def makeFont(name, size):
    font_path = os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            'fonts',
            name
        )
    )
    return ImageFont.truetype(font_path, size)


def drawBlankSignage(device, width, height):
    with canvas(device) as draw:
        welcomeSize = draw.textsize("Not Connected", fontBold)

    with canvas(device) as draw:
        stationSize = draw.textsize("Not Connected 2", fontBold)


try:
    serial = spi()
    device = ssd1322(serial, mode="1", rotate=2)
    font = makeFont("Dot Matrix Regular.ttf", 10)
    fontBold = makeFont("Dot Matrix Bold.ttf", 10)
    fontBoldTall = makeFont("Dot Matrix Bold Tall.ttf", 10)
    fontBoldLarge = makeFont("Dot Matrix Bold.ttf", 20)

    widgetWidth = 256
    widgetHeight = 64

    drawBlankSignage(device, width=widgetWidth, height=widgetHeight)

except KeyboardInterrupt:
    pass
except ValueError as err:
    print(f"Error: {err}")
except KeyError as err:
    print(f"Error: Please ensure the {err} environment variable is set")
