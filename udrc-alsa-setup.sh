#!/bin/bash

amixer -c sndrpiudrc -s << EOF
#  Set input and output levels to 0dB
sset 'ADC Level' 0dB
sset 'LO Driver Gain' 0dB
sset 'PCM' 0dB

#  Turn on AFOUT
sset 'Left Input Mixer IN1_L P' off
sset 'Left Input Mixer CM1_L N' off

#  Turn off DISCOUT
sset 'Right Input Mixer IN1_R P' on
sset 'Right Input Mixer CM1_R N' on 

#  Turn off unnecessary pins
sset 'Left Input Mixer IN2_L P' off
sset 'Left Input Mixer IN2_R N' off
sset 'Left Input Mixer IN3_L P' off
sset 'Left Input Mixer IN3_R N' off
sset 'Right Input Mixer IN1_L N' off
sset 'Right Input Mixer IN2_R P' off
sset 'Right Input Mixer IN3_L N' off
sset 'Right Input Mixer IN3_R P' off

sset 'Mic PGA' off
sset 'PGA Level' 0

# Disable and clear AGC
sset 'ADCFGA Right Mute' off
sset 'ADCFGA Left Mute' off
sset 'AGC Attack Time' 0
sset 'AGC Decay Time' 0
sset 'AGC Gain Hysteresis' 0
sset 'AGC Hysteresis' 0
sset 'AGC Max PGA' 0
sset 'AGC Noise Debounce' 0
sset 'AGC Noise Threshold' 0
sset 'AGC Signal Debounce' 0
sset 'AGC Target Level' 0
sset 'AGC Left' off
sset 'AGC Right' off

# Turn off High Power output
sset 'HP DAC' off
sset 'HP Driver Gain' 0
sset 'HPL Output Mixer L_DAC' off
sset 'HPR Output Mixer R_DAC' off
sset 'HPL Output Mixer IN1_L' off
sset 'HPR Output Mixer IN1_R' off

#  Turn on the LO DAC
sset 'LO DAC' on

#  Turn on AFIN
sset 'LOL Output Mixer L_DAC' off

#  Turn off TONEIN
sset 'LOR Output Mixer R_DAC' on
EOF
