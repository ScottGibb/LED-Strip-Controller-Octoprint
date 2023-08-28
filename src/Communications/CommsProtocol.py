"""
    Comms Protocol Functions, which are used to create the messages to send to the hardware
    Returns:
        (bytearray) The message to send to the hardware"""

# Local Imports
from Communications.Types import Colour, CtrlCmdId
from Communications.Types import Channel
from Communications.Types import FadeType
from Communications.Types import TX_MSG_SIZE


def create_constant_colour_message(channel: Channel, colour: Colour, brightness: int) -> bytearray:
    """Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): The channel to change
        colour (COLOUR):  The colour to change to
        brightness (int): The brightness to change to

    Returns:
        (bytearray): The message to send to the hardware
    """
    msg_bytes = bytearray([CtrlCmdId.LED_CHANGE.value, channel.value,
                       FadeType.NONE.value, colour.value, brightness]+ [0] * 4)
    return _add_padding(msg_bytes)


def create_fade_message(channel: Channel, fade_type: FadeType, colour: Colour, brightness: int, period: int) -> bytearray:
    """Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): The channel to change
        fade_type (FadeType): The fade type to use
        colour (COLOUR):  The colour to change to
        brightness (int):  The brightness to change to
        period (int):  The period of the fade

    Returns:
        (bytearray): The message to send to the hardware
    """
    msg_bytes = bytearray([CtrlCmdId.LED_CHANGE.value, channel.value,
                       fade_type.value, colour.value, brightness]) + period.to_bytes(4, "big")
    return _add_padding(msg_bytes)


def create_rgb_message(channel: Channel, red: int, green: int, blue: int) -> bytearray:
    """Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): The channel to change
        red (int):  the amount of red to use
        green (int): the amount of green to use
        blue (int):  the amount of blue to use

    Returns:
        (bytearray): The message to send to the hardware
    """
    msg_bytes = bytearray([CtrlCmdId.LED_CHANGE.value,
                       channel.value, FadeType.RGB_CTRL.value, red, green, blue])
    return _add_padding(msg_bytes)


def create_hsb_message(channel: Channel, hue: int, saturation: int, brightness: int) -> bytearray:
    """_summary_: Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): The channel to change
        hue (int):  the hue to use
        saturation (int): the saturation to use
        brightness (int): the brightness to use

    Returns:
        (bytearray): The message to send to the hardware
    """
    hue_bytes = hue.to_bytes(2, "big")
    msg_bytes = bytearray([CtrlCmdId.LED_CHANGE.value, channel.value, FadeType.HUE_CTRL.value]) + \
        hue_bytes + bytearray([saturation, brightness])
    return _add_padding(msg_bytes)


def _add_padding(msg_bytes : bytearray) -> bytearray:
    """Adds padding to the message to ensure that the message is the correct size
    Args:
        msg_bytes (bytearray): The message to pad
    """
    padding_len = TX_MSG_SIZE - len(msg_bytes)
    if padding_len > 0:
        msg_bytes = msg_bytes + bytearray([0] * padding_len)
    return msg_bytes
