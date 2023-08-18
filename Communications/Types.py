from enum import Enum

# Buffer Sizes
RX_MSG_CNT = 14
TX_MSG_SIZE = 10


class COLOUR(Enum):
    """_summary_
    Colour Enum specifying each colour the system can do
    Args:
        Enum (_type_): _description_
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


class FADE_TYPE(Enum):
    """_summary_
    Fade Type enum representing each of the modes the system can do
    Args:
        Enum (_type_): _description_
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


class CHANNEL(Enum):
    """_summary_
    Channel Enum representing each of the channels and there subsequent IDs
    Args:
        Enum (_type_): _description_
    """
    CHANNEL_NS = 0
    CHANNEL_1 = 1
    CHANNEL_2 = 2
    CHANNEL_3 = 3
    NUM_CHANNELS = 3


class TX_MSG_ID(Enum):
    """
    TX_MSG_ID defines the different tx messages the hardware can send
    """
    LED_UPDATE = 0
    PWR_UPDATE = 1


class CTRL_CMD_ID(Enum):
    """
    CTRL_CMD_ID defines the different messages that can be sent to the hardware
    """
    LED_CHANGE = 0