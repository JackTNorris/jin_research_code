import cmath
import math
import numpy as np

def jpt_algo(kMin1, kMin2, kMin3):
    #to find the measurement at time k, take 
    # the 3 measurements prior (kMin1 ... KMin3) and plug it into the following to get
    return 3 * kMin1 - 3 * kMin2 + kMin3

#e^ix = cos x + i sin x
def calculate_complex_voltage(magnitude, phase_angle):
    # V = magnitude  * e^(j*(wt + phase_angle))
    # V = magnitude * cos(phase_angle) + magnitude * i * sin(phase_angle)
    real_portion = math.cos(math.radians(phase_angle)) * magnitude
    imaginary_portion = math.sin(math.radians(phase_angle)) * magnitude
    voltage = complex(real_portion, imaginary_portion)
    return voltage

def phase_angle_and_magnitude_from_complex_voltage(voltage):
    phase_angle =  math.atan(voltage.image / voltage.real) #finds phase angle in radians
    magnitude = voltage.real / math.cos(phase_angle)
    return magnitude, phase_angle



if __name__ == "__main__":
    jpt_algo(0,0,0)

print("hello")
