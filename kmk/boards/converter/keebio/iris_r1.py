import board

from kmk.consts import DiodeOrientation
from kmk.mcus.circuitpython_samd51 import Firmware as _Firmware
from kmk.pins import Pin as P


class Firmware(_Firmware):
    col_pins = (P.A2, P.A3, P.A4, P.A5, P.SCK, P.MOSI)
    row_pins = (P.D11, P.D10, P.D9, P.D7, P.D13)
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.TX
    uart_pin = board.SCL
    split_type = 'UART'
    split_flip = True
    split_offsets = [6, 6, 6, 6, 6]
