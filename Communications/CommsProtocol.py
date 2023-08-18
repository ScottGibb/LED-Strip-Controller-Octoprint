# Local Imports
from Communications.Types import COLOUR, CTRL_CMD_ID
from Communications.Types import CHANNEL
from Communications.Types import FADE_TYPE
from Communications.Types import TX_MSG_SIZE


def create_constant_colour_message(channel: CHANNEL, colour: COLOUR, brightness):
    """_summary_: Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): _description_ The channel to change
        colour (COLOUR): _description_ The colour to change to
        brightness (_type_): _description_ The brightness to change to

    Returns:
        _type_: _description_ The message to send to the hardware
    """
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value, channel.value,
                       FADE_TYPE.NONE.value, colour.value, brightness]+ [0] * 4)
    return _add_padding(bytes)


def create_fade_message(channel: CHANNEL, fade_type: FADE_TYPE, colour: COLOUR, brightness, period):
    """_summary_: Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): _description_ The channel to change
        fade_type (FADE_TYPE): _description_ The fade type to use
        colour (COLOUR): _description_ The colour to change to
        brightness (_type_): _description_ The brightness to change to
        period (_type_): _description_ The period of the fade

    Returns:
        _type_: _description_ The message to send to the hardware
    """
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value, channel.value,
                       fade_type.value, colour.value, brightness]) + period.to_bytes(4, "big")
    return _add_padding(bytes)


def create_rgb_message(channel: CHANNEL, red, green, blue):
    """_summary_: Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): _description_ The channel to change
        red (_type_): _description_ the amount of red to use
        green (_type_): _description_ the amount of green to use
        blue (_type_): _description_  the amount of blue to use

    Returns:
        _type_: _description_ The message to send to the hardware
    """
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value,
                       channel.value, FADE_TYPE.RGB_CTRL.value, red, green, blue])
    return _add_padding(bytes)


def create_hsb_message(channel: CHANNEL, hue, saturation, brightness):
    """_summary_: Creates a message to send to the hardware to change the colour of a channel

    Args:
        channel (CHANNEL): _description_ The channel to change
        hue (_type_): _description_ the hue to use
        saturation (_type_): _description_ the saturation to use
        brightness (_type_): _description_ the brightness to use

    Returns:
        _type_: _description_ The message to send to the hardware
    """
    hue_bytes = hue.to_bytes(2, "big")
    bytes = bytearray([CTRL_CMD_ID.LED_CHANGE.value, channel.value, FADE_TYPE.HUE_CTRL.value]) + \
        hue_bytes + bytearray([saturation, brightness])
    return _add_padding(bytes)


def _add_padding(bytes):
    """_summary_: Adds padding to the message to ensure that the message is the correct size
    """
    padding_len = TX_MSG_SIZE - len(bytes)
    if padding_len > 0:
        bytes = bytes + bytearray([0] * padding_len)
    return bytes