import cmath
import math
import numpy as np

wt = 0

#jpt algorithm
def jpt_algo(kMin1, kMin2, kMin3):
    #to find the measurement at time k, take 
    # the 3 measurements prior (kMin1 ... KMin3) and plug it into the following to get
    return 3 * kMin1 - 3 * kMin2 + kMin3

#e^ix = cos x + i sin x
def calculate_complex_voltage(magnitude, phase_angle):
    # V = magnitude  * e^(j*(wt + phase_angle))
    # V = magnitude * cos(wt + phase_angle) + magnitude * i * sin(wt + phase_angle)
    real_portion = math.cos(math.radians(wt + phase_angle)) * magnitude
    imaginary_portion = math.sin(math.radians(wt + phase_angle)) * magnitude
    voltage = complex(real_portion, imaginary_portion)
    return voltage

# based on a voltage in the form V = a + bi, it extracts the magnitude and the voltage
def phase_angle_and_magnitude_from_complex_voltage(voltage):
    phase_angle =  math.atan(voltage.imag / voltage.real) - wt #finds phase angle in radians
    magnitude = voltage.real / math.cos(phase_angle + wt)
    return magnitude, math.degrees(phase_angle)



if __name__ == "__main__":
    # recent to least recent time measurements
    pmu_measurements = [{"magnitude": 253829.86075, "phase_angle": -13.9343335775816}, {"magnitude": 253811.55021, "phase_angle": -14.1348688058774}, {"magnitude": 253793.23967, "phase_angle": -14.3525927680271}]
    kMin = []
    for num in range(0, len(pmu_measurements)):
        complex_voltage = calculate_complex_voltage(pmu_measurements[num]["magnitude"], pmu_measurements[num]["phase_angle"])
        kMin.append(complex_voltage)
    complex_voltage_future_approximation = jpt_algo(kMin[0],kMin[1],kMin[2])
    print(phase_angle_and_magnitude_from_complex_voltage(complex_voltage_future_approximation))