import time
import RPi.GPIO as gp

class Sdata:
    min_us = 600
    current_us = None
    current_angle = None
    max_us = 2400
    servos = 0
    pins = []
    servo_objs = []

class Servo:
    def __init__(self):
        self.data = Sdata()
        gp.setmode(gp.BCM)
    """"

            self.data.pins.append(pin_number)
    """
    def add_servo(self, pin:list):
        for servo in pin:
            gp.setup(servo, gp.OUT)
            pwm = gp.PWM(servo, 50)  # Set frequency to 50 Hz
            pwm.start(0)  # Start PWM with 0% duty cycle
            self.data.servo_objs.append(pwm)
            self.data.pins.append(servo)
            self.data.servos += 1
    """
    def write2(self, us_or_degrees_list: list, degrees_true_or_us_false: list):

        for is_degrees, value in zip(degrees_true_or_us_false, us_or_degrees_list) :
            if is_degrees :
                self.dakia.current_angle = self.data.min_us + (value / 180) * (self.data.max_us - self.data.min_us)
                self.data.servo_objs[i].duty_u16(int(self.data.current_angle * 65535 / 20000))
            else:
                self.data.current_us = us_or_degrees_list[i]
                self.data.servo_objs[i].duty_u16(int(self.data.current_us * 65535 / 20000))
    """
    def write(self,angles:list,micro_us:list):

        for i in range(len(micro_us)):
            @staticmethod
            def duty(d):
                self.data.servo_objs[i].ChangeDutyCycle(d)
            if micro_us[i]:
                self.data.current_angle = self.data.min_us + (angles[i] / 180) * (self.data.max_us - self.data.min_us)
                duty(int(self.data.current_angle / 20000 * 100))
            else:
                self.data.current_us = angles[i]
                duty(int(self.data.current_us / 20000 * 100))

#optional- can be removed just import the python file then you can do soemthing like this.
s = Servo()
s.add_servo([18,19])

while True:
    s.write([90,0],[True,True])
    time.sleep(1)
    s.write([0,180],[True,True])
    time.sleep(1)



