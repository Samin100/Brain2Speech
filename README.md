# Introduction

Brain2Speech turns EEG signals from a Muse headband into speech.

![Demo image](/demo.JPG)

Here's is a [live demo on Youtube](https://youtu.be/8XR4ANnCEHw).

# How it works (simplified)
The Muse headband has EEG sensors which read out the values and sends the raw EEG data to [muse-io](http://developer.choosemuse.com/research-tools/museio) which then sends the data via a local UDP connection to ```OSC.py```. This OSC server then parses the raw EEG data and keeps track of your input and your location on the grid. An input is defined to be a sudden spike in EEG activity, and varies from person to person however the sweet spot for most people seemed to be about ```900 uV```. ```Server.py``` is a Flask server that allows JQuery to make AJAX calls and update the chart 10x per second.

Instead of morse code, we can use a table with the alphabet as a much easier means of working with a unary input. Users can blink or clench their jaw to select a column, then wait 1 second, and then select the row containing their character. Once finished, you can navigate to ```END``` with 6 inputs, pause for 1 second, then 5 inputs, and have their text played back to them.

# Installation
Install muse-sdk and run muse-io. Once connected run ```Server.py```. This spins off an OSC server thread concurrently so there's no need to start it separately. Naviagate to ```localhost:8000``` to load the ```table.html```.
