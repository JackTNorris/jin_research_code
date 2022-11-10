import cmath
import math

def jpt_algo(kMin1, kMin2, kMin3):
    #to find the measurement at time k, take the 3 measurements prior (kMin1 ... KMin3) and plug it into the following to get
    return 3 * kMin1 - 3 * kMin2 + kMin3

#e^ix = cos x + i sin x
def complex_voltage(magnitude, phase_angle):
    #V = magnitude  * e^(j*(wt + -133.94034376773254))

    voltage = complex(math.cos(phase_angle) * magnitude, math.sin(phase_angle) * magnitude) 
    # voltage = magnitude * e




if __name__ == "__main__":
    jpt_algo(0,0,0)
