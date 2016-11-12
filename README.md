# Python Wifi Probe Monitor
A simple python script which records and logs wifi probe requests.

# Usage
First, set your wifi card to monitor mode

    sudo ifconfig [name of interface] mode monitor

Then, change the wificard variable in wifiscanner.py to the name of your interface

    wificard = "[name of interface]"

Next, add your desired MAC adresses to the ignore list and your known devices to the known dictionary inside wifiscanner.py

    IGNORE_LIST = set(['00:00:00:00:00:00', '01:01:01:01:01:01'])

    d = {'00:00:00:00:00:00':'Example MAC Address'}

Finlly, start the program either normally or inside a screen session if you would like for the script to run constanly

    python wifiscanner.py

The program will then output all recoreded probe requested to the console, as well as to wifiscanner.log with a timestamp

# To-do

* Add notification support for unknown devices via a Telegram Bot, SMS (via carrier email gateway), email, and Pushover
* Add ability to record signal strength (to relativly determine distance)

# Similar Projects

* [Tim Tomes (LaNMaSteR53)'s WUDS](https://bitbucket.org/LaNMaSteR53/wuds/)
