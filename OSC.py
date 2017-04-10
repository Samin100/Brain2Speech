"""
OSC server that receives on osc.udp://localhost:5000 from muse-io.

Command to start the Muse OSC server on UDP port 5000:
muse-io --device Muse-9294 --osc osc.udp://localhost:5000

"""

import argparse
import os
from datetime import timedelta, datetime

from pythonosc import dispatcher
from pythonosc import osc_server

CHARS = [  # select from top then right
    # 1    2    3    4    5    6
    ['A', 'B', 'C', 'D', 'E', 'F'],  # 1
    ['G', 'H', 'I', 'J', 'K', 'L'],  # 2
    ['M', 'N', 'O', 'P', 'Q', 'R'],  # 3
    ['S', 'T', 'U', 'V', 'W', 'X'],  # 4
    ['Y', 'Z', ' ', ' ', '_', 'END']]  # 5

count = 0
past_time = datetime.now()
blink_string = ""
time_since_last_blink = datetime.now()

in_first = True

col_index = 0
row_index = 0
picking_first = True


def audio():
    '''
    Plays the blink_string back as audio.
    '''

    os.system('say ' + str(blink_string))


def process_val(val):
    """
    Main logic behind determining a blink.
    :param val:
    :return:
    """

    # defining global variables to access outer scope variables
    global count, past_time, blink_string, time_since_last_blink, col_index, row_index, picking_first, CHARS

    # a value is considered a valid blink if it's above 900 uV and it's been more than .22 seconds since the last blink
    if val > 900 and (datetime.now() - past_time) > timedelta(milliseconds=220):

        past_time = datetime.now()
        time_since_last_blink = datetime.now()

        count += 1

        if picking_first:
            if col_index == 6:
                # do nothing since there is no more than 6 columns
                pass

            else:
                col_index += 1
                print("Col: " + str(col_index))

        else:
            if row_index == 5:
                # no more than 5 rows
                pass

            else:
                row_index += 1
                print("Row: " + str(row_index))

    # a value is considered a 'non-blink' it's been 1 second since the last blink
    elif val < 9000 and (datetime.now() - time_since_last_blink) > timedelta(milliseconds=1000):

        if picking_first and col_index > 0:  # if we are done picking first
            picking_first = False
            print("Column " + str(col_index) + " selected")
            in_first = False

        elif picking_first and col_index == 0:  # do nothing if we haven't picked a col yet
            pass

        elif not picking_first and row_index > 0:  # if we are done picking a row
            letter = CHARS[row_index - 1][col_index - 1]

            if letter == 'END':
                print(blink_string)
                audio()
                clear()
            else:
                blink_string += letter
                in_first = True

            print(blink_string)  # printing the current blink string

            # resetting our variables
            row_index = 0
            col_index = 0
            picking_first = True

        elif not picking_first and col_index == 0:  # if we are still picking a row
            pass


def clear():
    """
    Resets values afte a letter has been chosen
    """

    global blink_string, col_index, row_index, picking_first
    print("cleared " + blink_string)
    col_index = 0
    row_index = 0
    picking_first = True
    blink_string = ""
    global in_first
    in_first = True


def eeg_handler(unused_addr, args, ch1, ch2, ch3, ch4):
    """
    Event handler that gets called for every data point sent over from the Muse headset.
    We can ignore the other channels since we only need ch4.
    """
    process_val(int(ch4))


def start():
    """
    Starts a UDP server on localhost:5000 listening for incoming OSC data on /muse/eeg.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1",
                        help="The ip to listen on")

    parser.add_argument("--port",
                        type=int,
                        default=5000,
                        help="The port to listen on")

    args = parser.parse_args()
    d = dispatcher.Dispatcher()
    d.map("/debug", print)
    d.map("/muse/eeg", eeg_handler, "EEG")

    server = osc_server.BlockingOSCUDPServer((args.ip, args.port), d)

    print("OSC server started {}".format(server.server_address))

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
