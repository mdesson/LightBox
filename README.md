# LightBox
Side project to get my head around the GPIO board on my Raspberry Pi.

## Setup
* 4 LEDs in the following order, mapped to the pin in parentheses: Blue(23), Red(20), Yellow(24), Green(21)
* Two buttons mapped to the following pins in parenthesis: Input button(12), Selector button(25)

## Purpose
The goal is to use the buttons to record simple light shows, where each light will turn on one at a time. The Selector button cycles through various commands, and the Input button executes the currently select command. When no lightshow is running, the lights will show the currently selected command.

## Commands
Assuming the order is Blue(23), Red(20), Yellow(24), and Green(21):

BRYG  
1000: Add blue to show  
0100: Add red to show  
0010: Add yellow to show  
0001: Add green to show  
1111: Play show  
1001: Clear show and, if show is playing, stop show.  
