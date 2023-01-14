import pygame
import pygame.midi
import threading
import sys
import RLBB as pepesmachine
import time
import random

# Initialize Pygame and the MIDI module
pygame.init()
pygame.midi.init()

looper_on = False


def chg_looper(looper):
    global looper_on
    if looper == True:
        looper_on = False
    else :
        looper_on = True
    print(f"global looper_on : {looper_on}, local looper : {looper}")

tempo = 2
tempo_color = 2

def chg_tempo(temporale):
    global tempo
    tempo = temporale

def chg_tempo_color(temporale):
    global tempo_color
    tempo_color = temporale
## Get a list of all MIDI devices
#device_info = [pygame.midi.get_device_info(i) for i in range(pygame.midi.get_count())]
#
## Print the list of MIDI devices
#print("MIDI Devices:")
#for i, info in enumerate(device_info):
#    print(f"{i}: {info[1]}")
#
## Prompt the user to select a MIDI device
#device_id = int(input("Enter the number of the MIDI device you want to use: "))
#
# Open an input stream to the MIDI device
input_stream = pygame.midi.Input(1)
    ## START PEPEWINDOW HERE
PepesMachina = pepesmachine
PepesMachina2 = pepesmachine
PepesMachina2.StartPepeFunction()
colorlooper = False

def chg_colorlooper(looper):
    global colorlooper
    if looper == True:
        colorlooper = False
    else :
        colorlooper = True
    print(f"global colorlooper : {colorlooper}, local colorlooper : {colorlooper}")
    
    
def loop_color():
    if colorlooper:
        PepesMachina.ADNprocessor.colorChanger()
    loopPepecolor = threading.Timer(tempo_color, loop_color)
    loopPepecolor.start()
    
    
def startlooping():
    if looper_on:
        x = random.randrange(0,500)
        y = random.randrange(0,500)
        PepesMachina.ClicktoChangePP(x,y)
        #PepesMachina2.StartPepeFunction()
    loopPepe = threading.Timer(tempo, startlooping)
    loopPepe.start()
    
firstimepressed = True
def chg_press():
    global firstimepressed
    firstimepressed = False

def run_on_second_event(first_time_stamp, second_time_stamp):
    print(f"This is you timing {second_time_stamp - first_time_stamp}")

# Run the game loop
while True:
    # Check if there are any MIDI events available to read
    if input_stream.poll():
        # Read the MIDI events
        events = input_stream.read(1)

        # Process the MIDI events
        for event in events:
            event_type = event[0][0]
            data = event[0][1:]
            timestamper = event[1]
            print(f"Event type: {event_type}")
            print(f"Data: {data}")
            
            ## TOUCH PAD ACTIVATION 1 ---> 36
            if event_type == 153 and data[0] == 36:
                first_time_stamp = event[1]
                if looper_on == False:
                   while True:
                       if input_stream.poll():
                           event = input_stream.read(1)[0]
                           if event[0][0] == 153 and event[0][1] == 36:
                               second_time_stamp = event[1]
                               new_tempo = (second_time_stamp - first_time_stamp) * 0.001
                               run_on_second_event(first_time_stamp, second_time_stamp)
                               break
                chg_tempo(new_tempo)
                chg_looper(looper_on)
                if firstimepressed == True:
                    chg_press()
                    startlooping()
                    loop_color()
                
                
            if event_type == 153 and data[0] == 37:
                first_time_stamp = event[1]
                if colorlooper == False:
                   while True:
                       if input_stream.poll():
                           event = input_stream.read(1)[0]
                           if event[0][0] == 153 and event[0][1] == 37:
                               second_time_stamp = event[1]
                               new_tempo = (second_time_stamp - first_time_stamp) * 0.001
                               break
                chg_tempo_color(new_tempo)
                chg_colorlooper(colorlooper)
                  
            
            
            
                    
            ## PIANO KEY ACTIVATION
            if event_type == 144:
                x = random.randrange(0,500)
                y = random.randrange(0,500)
                PepesMachina.ClicktoChangePP(x,y)
                
            ## UPDATE PEPEWINDOW HERE
            
    # Check for quit events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Close the input stream and MIDI module
            input_stream.close()
            pygame.midi.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            chg_looper(looper_on)
