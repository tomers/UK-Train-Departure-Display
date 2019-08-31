import os
import time

from luma.core.interface.serial import spi
from luma.oled.device import ssd1322
from luma.core.legacy import show_message
from luma.core.legacy.font import proportional, SINCLAIR_FONT


try:
    serial = spi()
    device = ssd1322(serial, mode="1", rotate=2)

    show_message(device, "Not Connected", fill="white", font=proportional(SINCLAIR_FONT))
    time.sleep(30)

except KeyboardInterrupt:
    pass
except ValueError as err:
    print(f"Error: {err}")
except KeyError as err:
    print(f"Error: Please ensure the {err} environment variable is set")
