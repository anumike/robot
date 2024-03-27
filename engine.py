import RPi.GPIO as GPIO
import time

PIN = 18
PWMA1 = 6
PWMA2 = 13
PWMB1 = 20
PWMB2 = 21
D1 = 12
D2 = 26

PWM = 50

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(PWMA1, GPIO.OUT)
GPIO.setup(PWMA2, GPIO.OUT)
GPIO.setup(PWMB1, GPIO.OUT)
GPIO.setup(PWMB2, GPIO.OUT)
GPIO.setup(D1, GPIO.OUT)
GPIO.setup(D2, GPIO.OUT)
p1 = GPIO.PWM(D1, 500)
p2 = GPIO.PWM(D2, 500)
# p1.start(20)
# p2.start(20)

minimal_speed = 20;
medium_speed = 40;


def soft_start(speed_to, delay):
    # return
    n = 15
    delta = (speed_to - minimal_speed) / n
    run_speed = minimal_speed
    print(delay)
    for i in range(n):
        run_speed = run_speed + delta
        p1.ChangeDutyCycle(run_speed)
        p2.ChangeDutyCycle(run_speed)
        print(i, run_speed)
        time.sleep(delay / n)


def soft_stop(speed_from, delay):
    # return
    n = 15
    delta = speed_from / n
    run_speed = speed_from
    for i in range(n):
        run_speed -= delta
        p1.ChangeDutyCycle(run_speed)
        p2.ChangeDutyCycle(run_speed)
        print(i, run_speed)
        time.sleep(delay / n)


def set_motor(A1, A2, B1, B2):
    GPIO.output(PWMA1, A1)
    GPIO.output(PWMA2, A2)

    GPIO.output(PWMB1, B1)
    GPIO.output(PWMB2, B2)


def forward(delay, speed, velocity):
    set_motor(1, 0, 1, 0)
    soft_start(speed, velocity)
    time.sleep(delay)
    soft_stop(speed, velocity)


def reverse(delay, speed, velocity):
    set_motor(0, 1, 0, 1)
    soft_start(speed, velocity)
    time.sleep(delay)
    soft_stop(speed, velocity)


def left(delay, speed, velocity):
    set_motor(1, 0, 0, 1)
    soft_start(speed, velocity)
    time.sleep(delay)
    soft_stop(speed, velocity)


def right(delay, speed, velocity):
    set_motor(0, 1, 1, 0)
    soft_start(speed, velocity)
    time.sleep(delay)
    soft_stop(speed, velocity)


def stop():
    set_motor(0, 0, 0, 0)

