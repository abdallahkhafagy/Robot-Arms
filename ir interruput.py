import RPi.GPIO as GPIO
BUTTON_GPIO = 16
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#    while True:
#        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.FALLING)
#        print("object detected !! ")
     while True:
        GPIO.wait_for_edge(BUTTON_GPIO, GPIO.BOTH)
        if not GPIO.input(BUTTON_GPIO):
            print("object detected !!")
        else:
            print("free space")