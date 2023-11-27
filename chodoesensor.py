import RPi.GPIO as g
import time
import spidev
LedPin = 12

g.setmode(g.BCM)
g.setwarnings(False)
g.setup(LedPin, g.OUT)



spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

def ReadVol(vol):
    adc = spi.xfer2([1, (0x08+vol) << 4, 0])
    data = ((adc[1]&0x03) << 8) + adc[2]
    return data

while True:
    a = ReadVol(0)
    print(a)
    if a<60 :
        g.output(12, True)
        time.sleep(0.5)
    else:
        g.output(12, False)
        time.sleep(0.5)
        
    time.sleep(0.5)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
