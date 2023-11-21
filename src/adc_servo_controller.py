from hal import hal_adc as adc
from hal import hal_servo as servo
from threading import Thread
from time import sleep

def get_value():
    while (True):
        x = adc.get_adc_value(1) * 180/1023
        servo.set_servo_position(x)
        #sleep(0.01)
    

def main():
    
    adc.init()
    servo.init()
    #servo.set_servo_position(0)

    adc_thread = Thread(target = get_value)
    adc_thread.start()

    

if __name__ == "__main__":
    main()