"""
Name: Jashanpreet kaur
Lab 3: This program controls the LEDs on the Adafruit Circuit Playground. 
It prompts the user to enter the number of LEDs (1-10) to turn on in blue. 
Invalid inputs are handled using a try/except block, and after the LEDs are turned on, 
the program switches them all off. The code is tested on the Circuit Playground device.
"""
from adafruit_circuitplayground import cp

blue = (0, 0, 255)

while True:
    try:
        # Get input from the user
        num_leds = int(input("Enter the number of LEDs to turn on (between 1 and 10): "))
        
        # Validate the input range
        if 1 <= num_leds <= 10:
            # Turn off all LEDs first
            for i in range(10):
                cp.pixels[i] = (0, 0, 0)
            
            # Turn on the specified number of LEDs in blue
            for i in range(num_leds):
                cp.pixels[i] = blue
            cp.pixels.show()  # Display changes
        else:
            print("Number out of range. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")
    
    # Ask if the user wants to start again
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    if restart == 'n':
        break
    
    # Turn off all LEDs at the end
for i in range(10):
    cp.pixels[i] = (0, 0, 0)
cp.pixels.show()  # Display changes
