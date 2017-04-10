"""
Flask server that serves that interfaces between the OSC server and the JavaScript frontend.
"""

import threading
from flask import Flask, render_template
import OSC

app = Flask(__name__)


def start_OSC():
    OSC.start()


@app.route('/clear')
def clear():
    OSC.clear()
    return render_template('table.html')


@app.route('/string')
def string():
    return OSC.blink_string


@app.route('/next')
def next():
    return str(OSC.in_first)


@app.route('/col')
def col():
    return str(OSC.col_index)


@app.route('/row')
def row():
    return str(OSC.row_index)


@app.route('/')
def index():
    print(OSC.blink_string)
    return render_template('table.html')


def start_flask():
    print('starting flask')
    app.run(port=8000)


if __name__ == '__main__':

    try:
        # launching 2 threads: Flask server and OSC server
        flask = threading.Thread(target=start_flask)
        osc_thread = threading.Thread(target=start_OSC)
        flask.start()
        osc_thread.start()

    except KeyboardInterrupt:
        print("Stopped.")
