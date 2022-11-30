import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mean 


wt = 0

def parse_csv_data():
    data = pd.read_csv("pmu12.csv")
    times = list(map(lambda time: time.replace("2014-01-28 23:00:", ""), data["TimeTag"].values))
    magnitudes = [data["Magnitude01"].values, data["Magnitude02"].values, data["Magnitude03"].values]
    phase_angles = [data["Angle01"].values, data["Angle02"].values, data["Angle03"].values]
    return {"times": times, "magnitudes": magnitudes, "phase_angles": phase_angles}

#jpt algorithm
def jpt_algo(kMin1, kMin2, kMin3):
    #to find the measurement at time k, take 
    # the 3 measurements prior (kMin1 ... KMin3) and plug it into the following to get
    return 3 * kMin1 - 3 * kMin2 + kMin3

# V = magnitude  * e^(j*(wt + phase_angle))
# given the magnitude and phase angle component, we convert he voltage into the form a + bi
def calculate_complex_voltage(magnitude, phase_angle):
    #e^ix = cos x + i sin x
    # V = magnitude * cos(wt + phase_angle) + magnitude * i * sin(wt + phase_angle)
    real_portion = math.cos(math.radians(wt + phase_angle)) * magnitude
    imaginary_portion = math.sin(math.radians(wt + phase_angle)) * magnitude
    voltage = complex(real_portion, imaginary_portion)
    return voltage

# based on a voltage in the form V = a + bi, it extracts the magnitude and the voltage
def phase_angle_and_magnitude_from_complex_voltage(voltage):
    phase_angle =  math.atan(voltage.imag / voltage.real) - wt #finds phase angle in radians
    magnitude = math.sqrt(voltage.real * voltage.real + voltage.imag * voltage.imag)
    return magnitude, math.degrees(phase_angle)

def generate_jpt_predictions(magnitudes, phase_angles):
    predictions = {"magnitudes": [], "phase_angles": []}
    for i in range(len(magnitudes) - 3):
        three_previous = []
        for j in range(i, i + 3):
            three_previous.append({"magnitude": magnitudes[j], "phase_angle": phase_angles[j]})
        k_min = []
        for measurement in three_previous:
            complex_voltage = calculate_complex_voltage(measurement["magnitude"], measurement["phase_angle"])
            k_min.append(complex_voltage)
        complex_voltage_future_approximation = jpt_algo(k_min[0],k_min[1],k_min[2])
        predicted_magnitude, predicted_phase_angle = phase_angle_and_magnitude_from_complex_voltage(complex_voltage_future_approximation)
        predictions["magnitudes"].append(predicted_magnitude)
        predictions["phase_angles"].append(predicted_phase_angle)
    return predictions

def calculate_approximation_error(exact, approximate):
    return abs(exact - approximate) / exact * 100

def calculate_average_approximation_error(exact_measurements, approximate_measurements):
    approximation_errors = []
    for i in range(len(exact_measurements)):
        approximation_errors.append(calculate_approximation_error(exact_measurements[i], approximate_measurements[i]))
    print(approximation_errors)
    return mean(approximation_errors)


if __name__ == "__main__":
    pmu_raw_data = parse_csv_data()
    y1 = pmu_raw_data["magnitudes"][0][3:]
    x = pmu_raw_data["times"][3:]
    fig, ax = plt.subplots()
    ax.plot(x, y1, color="g", label="actual")

    y2 = generate_jpt_predictions(pmu_raw_data["magnitudes"][0], pmu_raw_data["phase_angles"][0])["magnitudes"]

    print("Approximation error average: " + str(calculate_average_approximation_error(y1, y2)))
    ax.plot(x, y2, color="r", label="predicted")
    plt.show()
