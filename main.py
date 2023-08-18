# Imports
import argparse
import socket
import logging

from Communications.Types import CHANNEL, COLOUR, FADE_TYPE
from Communications.CommsProtocol import create_constant_colour_message

# Configure the logging system
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Script Arguments
parser = argparse.ArgumentParser(description='A Simple IP Script for controlling the Server Rack LED Controller')
parser.add_argument("--on", action="store_true", help="Turns the Led on")
parser.add_argument("--off", action="store_true", help="Turns the Led off")

# IP Credentials
IP_ADDRESS = "192.168.0.68"
PORT_NUM = 6000

# Channel Configuration
TOP_SHELF_CHANNEL = CHANNEL.CHANNEL_2
TOP_SHELF_COLOUR = COLOUR.WHITE
TOP_SHELF_BRIGHTNESS_ON = 100
TOP_SHELF_BRIGHTNESS_OFF = 0


def turn_lights_on() -> None:
    """
    Turns the Printer Enclosure Lights On
    """
    tx_msg = create_constant_colour_message(TOP_SHELF_CHANNEL, TOP_SHELF_COLOUR, TOP_SHELF_BRIGHTNESS_ON)
    send_control_message(tx_msg)
    logger.info("Turned Lights On!")


def turn_lights_off() -> None:
    """
    Turns the Printer Enclosure Lights Off
    """
    tx_msg = create_constant_colour_message(TOP_SHELF_CHANNEL, TOP_SHELF_COLOUR, TOP_SHELF_BRIGHTNESS_OFF)
    send_control_message(tx_msg)
    logger.info("Turned Lights Off!")


def send_control_message(message: bytearray) -> None:
    """
    Sends the control message to the LED Strip Controller Hardware
    :param message: the control message
    """
    try:
        communicator = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        communicator.connect((IP_ADDRESS, PORT_NUM))
        logger.debug("Opened socket")

        communicator.sendall(message)
        logger.debug("Sent Lights message")
    finally:
        communicator.close()
        logger.debug("Socket Closed")

def main() -> None:
    """
    Main Execution
    """
    args = parser.parse_args()

    if args.on:
        turn_lights_on()
    elif args.off:
        turn_lights_off()
    else:
        logger.error("No action specified. Use --on or --off.")

if __name__ == "__main__":
    main()

