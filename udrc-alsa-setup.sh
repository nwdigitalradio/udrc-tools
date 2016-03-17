#!/bin/bash

amixer -c sndrpiudrc -s << EOF
#  Set input and output levels to 0dB
sset 'ADC Level' 24
sset 'LO Driver Gain' 6

#  Turn on AFOUT
sset 'Left Input Mixer IN1_L P' off
sset 'Left Input Mixer CM1_L N' off

#  Turn off DISCOUT
sset 'Right Input Mixer IN1_R P' on
sset 'Right Input Mixer CM1_R N' on 

#  Turn off unnecessary pins
sset 'Left Input Mixer IN2_L P' off
sset 'Left Input Mixer IN2_R P' off
sset 'Left Input Mixer IN3_L P' off
sset 'Left Input Mixer IN3_R N' off
sset 'Right Input Mixer IN1_L N' off
sset 'Right Input Mixer IN2_R P' off
sset 'Right Input Mixer IN3_L N' off
sset 'Right Input Mixer IN3_R P' off

#  Turn on AFIN
sset 'LOL Output Mixer L_DAC' off

#  Turn off TONEIN
sset 'LOR Output Mixer R_DAC' on
EOF
