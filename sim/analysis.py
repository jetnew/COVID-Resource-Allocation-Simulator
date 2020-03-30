import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')


def plot_experiment(factor, filename):
    """Given the factor and filename, plot factor vs transmissions."""
    df = pd.read_csv("experiments/" + filename)
    plt.title(f"{factor} vs transmissions")
    plt.plot(df[factor], df['transmissions'])
    plt.xlabel(factor)
    plt.ylabel("transmissions")
    plt.show()

# plot_experiment("transmission_rate", "transmission_rate.csv")
# plot_experiment("time_req_waiting_area", "time_req_waiting_area.csv")
# plot_experiment("size_waiting_area_x", "size_waiting_area_x.csv")
# plot_experiment("time_req_pharmacy", "time_req_pharmacy.csv")