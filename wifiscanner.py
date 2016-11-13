#########################################################################
#     Wifiscanner.py - A simple python script which records and logs wifi probe requests.
#     Author - D4rKP01s0n
#     Requirements - Scapy and Datetime
#########################################################################


from datetime import datetime
from scapy.all import sniff, Dot11
#import numpy
import logging
import time
from notify import *
#Devices which are known to be constantly probing
IGNORE_LIST = set(['00:00:00:00:00:00', '01:01:01:01:01:01'])
#SEEN_DEVICES = set() #Devices which have had their probes recieved, removed due to memory use
d = {'00:00:00:00:00:00':'Example MAC Address'} #Dictionary of all named devices


wificard = 'mon0' #    Change this to your monitor-mode enabled wifi interface
notifications = False #     Change to True and set up in notify.py if you want Pushover notifications

#knownfile = open('knowndevices.txt', 'a')
#knownfile.write(str(d))

#This exports known dictionary to a text file, but should only be used if the existing file is removed and the dictionary has been updated, as otherwise it will append the list to the existing file


#class colors: # These allow for color-coded output
#    HEADER = '\033[95m'    #    An example of using this would be as follows
#    OKBLUE = '\033[94m'    #    print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC
#    OKGREEN = '\033[92m'   #    Credit: Joeld of StackOverflow: http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
#    WARNING = '\033[93m'
#    FAIL = '\033[91m'
#    ENDC = '\033[0m'       #    End every colored line with this, or else everything following will be the same color
#    BOLD = '\033[1m'
#    UNDERLINE = '\033[4m'

def handle_packet(pkt):
	if not pkt.haslayer(Dot11):
		return
	if pkt.type == 0 and pkt.subtype == 4: #subtype used to be 8 (APs) but is now 4 (Probe Requests)
		#logging.debug('Probe Recorded with MAC ' + curmac)
		curmac = pkt.addr2
		curmac = curmac.upper() #Assign variable to packet mac and make it uppercase
		#SEEN_DEVICES.add(curmac) #Add to set of known devices (sets ignore duplicates so it is not a problem)
		if curmac not in IGNORE_LIST: #If not registered as ignored
			if curmac in d:
				logging.info('\033[95m' + 'Probe Recorded from ' + '\033[93m' + d[curmac] + '\033[95m' + ' with MAC ' + curmac + '\033[0m') #Log to file wifiscanner.log with purple color
                                print('\033[95m' + 'Probe MAC Address: ' + pkt.addr2 + ' from device ' + '\033[93m' + d[curmac] + '\033[0m')
                                        #'with SSID: {pkt.info}'.format(pkt=pkt)) #Print to command line with purple color
			else:
				logging.info('\033[92m' + 'Probe Recorded from MAC ' + pkt.addr2 + '\033[0m') #Log to file wifiscanner.log with green color
				print('\033[95m' + 'Device MAC: {pkt.addr2} '
					'with SSID: {pkt.info}'.format(pkt=pkt) + '\033[0m') #Print to command line with green color
				lastnotify = ''
				if lastnotify != curmac:  #  So that notifications don't repeat
					themessage = 'Unknown device with MAC %s sighted!' % curmac
					notify(themessage, "", "")    # Notify via Pushover
					lastnotify = curmac
			#print SEEN_DEVICES #Just for debug, prints all known devices
			#dump()

def main():
	
	logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='wifiscanner.log',level=logging.DEBUG) #setup logging to file
	logging.info('\n' + '\033[93m' + 'Wifi Scanner Initialized' + '\033[0m' + '\n') #announce that it has started to log file with yellow color
	print('\n' + '\033[93m' + 'Wifi Scanner Initialized' + '\033[0m' + '\n') #announce that it has started to command line with yellow color		(/n is newline)
	
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('--interface', '-i', default=wificard, # Change mon0 to your monitor-mode enabled wifi interface
				help='monitor mode enabled interface')
	args = parser.parse_args()
	sniff(iface=args.interface, prn=handle_packet, store=0, count=0) #start sniffin, store=0 makes sniff not save captured packets and count=0 makes sniff continously scan packets
if __name__ == '__main__':
	main()
