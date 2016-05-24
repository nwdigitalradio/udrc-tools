#!/usr/bin/env python3

import locale
import sys
import re
from dialog import Dialog
from subprocess import call

locale.setlocale(locale.LC_ALL, '')

mixer_settings = {
	'ADC Level':					'0dB',
	'LO Driver Gain':				'0dB',
	'PCM':							'0dB',
	'Left Input Mixer IN1_L P':		'on',
	'Left Input Mixer CM1_L N':		'on',
	'Right Input Mixer IN1_R P':	'on',
	'Right Input Mixer CM1_R N':	'on',
	
	#  Turn off unnecessary pins
	'Left Input Mixer IN2_L P':		'off',
	'Left Input Mixer IN2_R N':		'off',
	'Left Input Mixer IN3_L P':		'off',
	'Left Input Mixer IN3_R N':		'off',
	'Right Input Mixer IN1_L N':	'off',
	'Right Input Mixer IN2_R P':	'off',
	'Right Input Mixer IN3_L N':	'off',
	'Right Input Mixer IN3_R P':	'off',
	
	'Mic PGA':						'off',
	'PGA Level':					'0',
	
	# Disable and clear AGC
	'ADCFGA Right Mute':			'off',
	'ADCFGA Left Mute':				'off',
	'AGC Attack Time':				'0',
	'AGC Decay Time':				'0',
	'AGC Gain Hysteresis':			'0',
	'AGC Hysteresis':				'0',
	'AGC Max PGA':					'0',
	'AGC Noise Debounce':			'0',
	'AGC Noise Threshold':			'0',
	'AGC Signal Debounce':			'0',
	'AGC Target Level':				'0',
	'AGC Left':						'off',
	'AGC Right':					'off',

	# Turn off High Power output
	'HP DAC':						'off',
	'HP Driver Gain':				'0',
	'HPL Output Mixer L_DAC':		'off',
	'HPR Output Mixer R_DAC':		'off',
	'HPL Output Mixer IN1_L':		'off',
	'HPR Output Mixer IN1_R':		'off',

	#  Turn on the LO DAC
	'LO DAC':						'on',

	'LOL Output Mixer L_DAC':		'on',
	'LOR Output Mixer R_DAC':		'on',
}

dstarrepeater_settings = {
	'callsign':						'N0CALL B',
	'gateway':						'N0CALL G',
	'mode':							'0',
	'ack':							'1',
	'restriction':					'0',
	'rpt1Validation':				'1',
	'dtmfBlanking':					'1',
	'errorReply':					'1',
	'gatewayAddress':				'127.0.0.1',
	'gatewayPort':					'20010',
	'localAddress':					'127.0.0.1',
	'localPort':					'20011',
	'networkName':					'UDRC',
	'modemType':					'Sound Card',
	'timeout':						'180',
	'ackTime':						'200',
	'beaconTime':					'600',
	'beaconText':					'D-Star Repeater UDRC',
	'beaconVoice':					'0',
	'language':						'9',
	'announcementEnabled':			'0',
	'announcementTime':				'480',
	'announcementRecordRPT1':		'',
	'announcementRecordRPT2':		'',
	'announcementDeleteRPT1':		'',
	'announcementDeleteRPT2':		'',
	'controlEnabled':				'0',
	'controlRPT1':					'',
	'controlRPT2':					'',
	'controlShutdown':				'',
	'controlStartup':				'',
	'controlStatus1':				'',
	'controlStatus2':				'',
	'controlStatus3':				'',
	'controlStatus4':				'',
	'controlStatus5':				'',
	'controlCommand1':				'',
	'controlCommand1Line':			'',
	'controlCommand2':				'',
	'controlCommand2Line':			'',
	'controlCommand3':				'',
	'controlCommand3Line':			'',
	'controlCommand4':				'',
	'controlCommand4Line':			'',
	'controlCommand5':				'',
	'controlCommand5Line':			'',
	'controlCommand6':				'',
	'controlCommand6Line':			'',
	'controlOutput1':				'',
	'controlOutput2':				'',
	'controlOutput3':				'',
	'controlOutput4':				'',
	'controllerType':				'UDRC',
	'serialConfig':					'2',
	'pttInvert':					'1',
	'activeHangTime':				'4',
	'output1':						'0',
	'output2':						'1',
	'output3':						'0',
	'output4':						'0',
	'logging':						'0',
	'windowX':						'993',
	'windowY':						'275',
	'dvapPort':						'',
	'dvapFrequency':				'145500000',
	'dvapPower':					'10',
	'dvapSquelch':					'-100',
	'gmskAddress':					'768',
	'dvrptr1Port':					'',
	'dvrptr1RXInvert':				'0',
	'dvrptr1TXInvert':				'0',
	'dvrptr1Channel':				'0',
	'dvrptr1ModLevel':				'20',
	'dvrptr1TXDelay':				'150',
	'dvrptr2Connection':			'0',
	'dvrptr2USBPort':				'',
	'dvrptr2Address':				'127.0.0.1',
	'dvrptr2Port':					'0',
	'dvrptr2TXInvert':				'0',
	'dvrptr2ModLevel':				'20',
	'dvrptr2TXDelay':				'150',
	'dvrptr3Connection':			'0',
	'dvrptr3USBPort':				'',
	'dvrptr3Address':				'127.0.0.1',
	'dvrptr3Port':					'0',
	'dvrptr3TXInvert':				'0',
	'dvrptr3ModLevel':				'20',
	'dvrptr3TXDelay':				'150',
	'dvmegaPort':					'',
	'dvmegaVariant':				'0',
	'dvmegaRXInvert':				'0',
	'dvmegaTXInvert':				'0',
	'dvmegaTXDelay':				'150',
	'dvmegaRXFrequency':			'145500000',
	'dvmegaTXFrequency':			'145500000',
	'dvmegaPower':					'100',
	'mmdvmPort':					'',
	'mmdvmRXInvert':				'0',
	'mmdvmTXInvert':				'0',
	'mmdvmPTTInvert':				'0',
	'mmdvmTXDelay':					'50',
	'mmdvmRXLevel':					'100',
	'mmdvmTXLevel':					'100',
	'soundCardRXDevice':			'hw:CARD=sndrpiudrc,DEV=0',
	'soundCardTXDevice':			'hw:CARD=sndrpiudrc,DEV=0',
	'soundCardRXInvert':			'1',
	'soundCardTXInvert':			'0',
	'soundCardRXLevel':				'1.0000',
	'soundCardTXLevel':				'1.0000',
	'soundCardTXDelay':				'100',
	'soundCardTXTail':				'50',
	'splitLocalAddress':			'',
	'splitLocalPort':				'0',
	'splitTXName0':					'',
	'splitTXName1':					'',
	'splitTXName2':					'',
	'splitTXName3':					'',
	'splitTXName4':					'',
	'splitRXName0':					'',
	'splitRXName1':					'',
	'splitRXName2':					'',
	'splitRXName3':					'',
	'splitRXName4':					'',
	'splitRXName5':					'',
	'splitRXName6':					'',
	'splitRXName7':					'',
	'splitRXName8':					'',
	'splitRXName9':					'',
	'splitRXName10':				'',
	'splitRXName11':				'',
	'splitRXName12':				'',
	'splitRXName13':				'',
	'splitRXName14':				'',
	'splitRXName15':				'',
	'splitRXName16':				'',
	'splitRXName17':				'',
	'splitRXName18':				'',
	'splitRXName19':				'',
	'splitRXName20':				'',
	'splitRXName21':				'',
	'splitRXName22':				'',
	'splitRXName23':				'',
	'splitRXName24':				'',
	'splitTimeout':					'0',
}

def set_alsa_mixer(key, value, device='sndrpiudrc'):
	call(['/usr/bin/amixer', '-c', 'sndrpiudrc', '-q', '--', 
              'sset', key, value])

def setup_mixer():
	for key, value in mixer_settings.items():
		set_alsa_mixer(key, value)

def quit():
	if d.yesno('Do you really want to quit?') == d.OK:
		sys.exit(0)
		
def complete():
	d.msgbox('Setup complete.', title="Done!");
	call('/usr/bin/clear')
	sys.exit(0)

d = Dialog()

d.set_background_title('UDRC Setup Utility')

welcome_text = """
Welcome to the Universal Digital Radio Controller setup utility.  This program will assist \
you in the initial setup of your UDRC.

If you would like to set up a D-STAR repeater using the UDRC, this program can help you \
get things initially set up.  This verbiage is going to need some work.
"""

menu_text = """
Select a type of install.  You may choose to install the OpenDV components \
(ircDDBGateway and DStarRepeater) to implement a D-STAR repeater, or to just do the \
basic setup for the UDRC.
"""
d.msgbox(welcome_text, title='Welcome!', height=20, width=60)

code, install_type = d.menu(menu_text, 
         	       title='Install Type',
                   choices = [ ('Full', 'DStarRepeater & ircDDBGateway'),
                               ('RepeaterOnly', 'DStarRepeater only'),
                               ('Base', 'Base configuration only') ]);
                               
if code == d.ESC or code == d.CANCEL:
	quit()
	
d.infobox("Setting up the audio mixer...")
setup_mixer()

if install_type == 'Base':
	complete()
		
#  Disable unused channels because we're going to be a repeater
#  Turn off AFOUT
set_alsa_mixer('Left Input Mixer IN1_L P', 'off')
set_alsa_mixer('Left Input Mixer CM1_L N', 'off')
#  Turn off AFIN
set_alsa_mixer('LOL Output Mixer L_DAC', 'off')

code = d.CANCEL
while code != d.OK:
	code, call = d.inputbox("Input the repeater's callsign", title = 'Repeater Callsign');
	if code == d.ESC or code == d.CANCEL:
		quit()
	call = call.upper()
	callre = re.compile('^[A-Z0-9]{1,3}[0-9]{1}[A-Z0-9]{0,3}[A-Z]{1}$')
	if not callre.match(call):
		code = d.CANCEL
		d.msgbox('The callsign you entered is invalid', title = 'Invalid Callsign');

code, module = d.radiolist("Repeater Module", title = 'Repeater Module', choices = [ ('A', 'Usually 23cm/1.2GHz', False), 
                                                                      ('B', 'Usually 70cm/440MHz', True),
                                                                      ('C', 'Usually 2m/144MHz', False),
                                                                      ('D', 'Testing Module', False) ])

dstarrepeater_settings['callsign'] = "{:7.7s}{:1.1s}".format(call, module)
dstarrepeater_settings['gateway'] =  "{:7.7s}G".format(call)                                   

#  Probably should see if this exists and throw an error
dstarrepeater_conf = open('dstarrepeater_1', 'w');

for key, value in sorted(dstarrepeater_settings.items()):
		dstarrepeater_conf.write("{0}={1}\n".format(key, value))
		
if install_type == 'RepeaterOnly':
	complete()
			
d.msgbox('ircDDBGateway configuration needs to happen here!', title = 'TO DO!')



