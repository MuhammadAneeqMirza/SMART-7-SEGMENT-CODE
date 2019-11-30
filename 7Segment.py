import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

segments = (3,5,7,11,13,15,19)
digits = (21,23,29,31)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment,1)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)

s_0 = (0,0,0,0,0,0,1)
s_1 = (1,0,0,1,1,1,1)
s_2 = (0,0,1,0,0,1,0)
s_3 = (0,0,0,0,1,1,0)
s_4 = (1,0,0,1,1,0,0)
s_5 = (0,1,0,0,1,0,0)
s_6 = (0,1,0,0,0,0,0)
s_7 = (0,0,0,1,1,1,1)
s_8 = (0,0,0,0,0,0,0)
s_9 = (0,0,0,0,1,0,0)

disp_1 = 0
disp_2 = 0
disp_3 = 0
disp_4 = 0

#=========================== Function define ============
def sel_Numeric_Val():
    global segment_val
    if num_val == 0:
        segment_val = s_0
    elif num_val == 1:
        segment_val = s_1
    elif num_val == 2:
        segment_val = s_2
    elif num_val == 3:
        segment_val = s_3  
    elif num_val == 4:
        segment_val = s_4 
    elif num_val == 5:
        segment_val = s_5  
    elif num_val == 6:
        segment_val = s_6  
    elif num_val == 7:
        segment_val = s_7  
    elif num_val == 8:
        segment_val = s_8  
    elif num_val == 9:
        segment_val = s_9  
    
            
def display_Val ():
    sel_Numeric_Val()
    for a in range(0,7):    
            GPIO.output(segments[a], segment_val[a])
    GPIO.output(digits[d_pos],1)
    time.sleep(0.001)
    GPIO.output(digits[d_pos],0)
    

def display_4_digit ():
    global num_val
    global d_pos
    
    num_val = disp_1  # for digit 1
    d_pos = 0
    display_Val ()

    num_val = disp_2  # for digit 2
    d_pos = 1
    display_Val ()

    num_val = disp_3  # for digit 3
    d_pos = 2
    display_Val ()

    num_val = disp_4  # for digit 4
    d_pos = 3
    display_Val ()
    

def Run_counter ():
    global disp_1
    global disp_2
    global disp_3
    global disp_4
    
    disp_1 = disp_1 + 1
    if disp_1 == 10:
        disp_1 = 0
        
        disp_2 = disp_2 + 1
        if disp_2 == 10:
            disp_2 = 0
            
            disp_3 = disp_3 + 1
            if disp_3 == 10:    
                disp_3 = 0

                disp_4 = disp_4 + 1
                if disp_4 == 10:
                    disp_4 = 0
        
    
    
#============================= Main program =====================

while True:
    Run_counter ()
    for delay in range(0,100):   
         display_4_digit ()
    
    
