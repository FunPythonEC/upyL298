"""
Habilitamos el manejo de PWM en los 
pines ENA y ENB
"""

import time 
import machine
from machine import Pin

#Led por incluido por default en el board del ESP32 dev Kit
led = Pin(2,Pin.OUT)

#Configuraciòn de pines oara el ESP32 dev kit

ENA = Pin(13,Pin.OUT)
IN1 = Pin(12,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(27,Pin.OUT)
IN4 = Pin(26,Pin.OUT)
ENB = Pin(25,Pin.OUT)


#Seteo inicial de los pines
ENA.value(0)
IN1.value(0)
IN2.value(0)
IN3.value(0)
IN4.value(0)
ENB.value(0)


#Seteo de frecuencia de trabajo
freq=1000

def retro_m1(vel_m1):
    #Habilito Motor 1
    #ENA.value(1) 
    ena_pwm=machine.PWM(ENA)
    #Dirección1
    IN1.value(1)
    IN2.value(0)
    ena_pwm.freq(1000)
    ena_pwm.duty(vel_m1)

def retro_m2(vel_m2):
    #Habilito Motor 2
    #ENB.value(1) 
    enb_pwm=machine.PWM(ENB)
    #Dirección1
    IN3.value(0)
    IN4.value(1)
    enb_pwm.freq(freq)
    enb_pwm.duty(vel_m2)
    
def avanza_m1(vel_m1):
    ena_pwm=machine.PWM(ENA)
    IN1.value(0)
    IN2.value(1)
    ena_pwm.freq(freq)
    ena_pwm.duty(vel_m1)

def avanza_m2(vel_m2):
    #Habilito Motor 2
    enb_pwm=machine.PWM(ENB)
    #Direccion2
    IN3.value(1)
    IN4.value(0)
    enb_pwm.freq(500)
    enb_pwm.duty(vel_m2)


def stop_m1():
    ENA.value(0)
    #Paro
    IN1.value(0)
    IN2.value(0)
    
def stop_m2():
    ENB.value(0) 
    #Paro
    IN3.value(0)
    IN4.value(0)

def stop_all():
    ENA.value(0)
    ENB.value(0) 
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)

def giro_sent_1(): #derecha.
    avanza_m1()
    stop_m2()

def giro_sent_2(): #izquierda.
    avanza_m2()
    stop_m1()

#Inicia la secuencia que deseamos que realice
#Para una frecuecia de 1kz se requiere un minimo
#de ciclo de trabajo de 400 para poder salir de la
#inercia

for i in range(40,50):
    #avanza_m1(10*i)
    #avanza_m2(10*i)
    #retro_m1(10*i)
    retro_m2(10*i)
    time.sleep_ms(500)
    print(i)
