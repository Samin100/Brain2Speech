# Introduction

Brain2Speech turns EEG signals from a Muse headband into user input and utilizes a GUI that turns a unary input into speech.
Here's is a [live demo on Youtube](https://youtu.be/8XR4ANnCEHw).

![Demo image](/demo.JPG)



# How it works
The Muse headband has EEG sensors which read out your EEG values and sends the raw EEG data to [muse-io](http://developer.choosemuse.com/research-tools/museio) via Bluetooth which then sends the data via a local UDP connection to ```OSC.py```. This OSC server then parses the raw EEG data and keeps track of your input and your location on the grid. An input is defined to be a sudden spike in EEG activity, and varies from person to person however the sweet spot for most people seemed to be an upper threshold of about ```900 uV +/- 40 uV```. ```Server.py``` is a Flask server that allows JQuery to make AJAX calls and update the chart 10x per second.

Instead of morse code, we can use a table with the alphabet as a much easier means of working with a unary input. Users can blink or clench their jaw to select a column, then wait 1 second, and then select the row containing their character. Once finished, they can navigate to ```END``` to have their text spoken.

# Installation
Install muse-sdk and run muse-io. Once connected run ```Server.py```. This spins off an OSC server thread concurrently so there's no need to start it separately. Once the server is running, navigate to ```localhost:8000```.
