"""
Types.py file contains all the enums and constants used in the communications protocol
"""
from enum import Enum

# Buffer Sizes
RX_MSG_CNT: int = 14
TX_MSG_SIZE: int = 10


class Colour(Enum):
    """
    Colour Enum specifying each colour the system can do
    Args:
        Colour (Enum): The different colours of the system
    """
    RED = 0
    GREEN = 1
    BLUE = 2
    WHITE = 3
    ROSE = 4
    MAGENTA = 5
    VIOLET = 6
    AZURE = 7
    CYAN = 8
    AQUAMARINE = 9
    CHARTREUSE = 10
    YELLOW = 11
    ORANGE = 12
    NUM_COLOURS = 13


class FadeType(Enum):
    """
    Fade Type enum representing each of the modes the system can do
    Args:
        FadeType (Enum): The different fade types of the system
    """
    NONE = 0
    SINE = 1
    SQUARE = 2
    TRIANGLE = 3
    SAWTOOTH = 4
    COLOUR_CHANGE = 5
    RGB_CTRL = 6
    HUE_CTRL = 7
    SIZE = 8


class Channel(Enum):
    """
    Channel Enum representing each of the channels and there subsequent IDs
    Args:
        Channel (Enum): The different channels of the system
    """
    CHANNEL_NS = 0
    CHANNEL_1 = 1
    CHANNEL_2 = 2
    CHANNEL_3 = 3
    NUM_CHANNELS = 3


class TxMsgId(Enum):
    """
    TX_MSG_ID defines the different tx messages the hardware can send
    Args:
        TxMsgId (Enum): The different tx messages the hardware can send
    """
    LED_UPDATE = 0
    PWR_UPDATE = 1


class CtrlCmdId(Enum):
    """
    CTRL_CMD_ID defines the different messages that can be sent to the hardware
    Args:
        CtrlCmdId (Enum): The different messages that can be sent to the hardware
    """
    LED_CHANGE = 0
