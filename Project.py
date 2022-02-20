import random
import statistics
import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv('medium_data.csv')
time = df["reading_time"].tolist()

population_mean = statistics.mean(time)
print(population_mean)

def find_sample_mean():
    dataset = []
    for i in range(0, 30):
        index = random.randint(0, len(time) - 1)
        value = time[index]
        dataset.append(value)

    sample_mean = statistics.mean(dataset)
    return sample_mean

def setup():
    global sample_mean_array, mean, std1_start, std1_end, std2_start, std2_end, std3_start, std3_end
    sample_mean_array = []
    for i in range(0, 100):
        mean_array = find_sample_mean()
        sample_mean_array.append(mean_array)

    mean = statistics.mean(sample_mean_array)
    print(mean)

    std = statistics.stdev(sample_mean_array)
    std1_start, std1_end = mean - std, mean + std
    std2_start, std2_end = mean - 2 * std, mean + 2 * std
    std3_start, std3_end = mean - 3 * std, mean + 3 * std

def plot_graph():
    data = sample_mean_array
    fig = ff.create_distplot([data], ["Reading Time"], show_hist = False)
    fig.add_trace(go.Scatter(
        x = [mean, mean],
        y = [0, 1],
        mode = "lines",
        name = "Mean"
    ))
    fig.add_trace(go.Scatter(
        x = [std1_start, std1_start],
        y = [0, 1],
        mode = "lines",
        name = "1st Starting Standard Deviation"
    ))
    fig.add_trace(go.Scatter(
        x = [std1_end, std1_end],
        y = [0, 1],
        mode = "lines",
        name = "1st Ending Standard Deviation"
    ))
    fig.add_trace(go.Scatter(
        x = [std2_start, std2_start],
        y = [0, 1],
        mode = "lines",
        name = "2nd Starting Standard Deviation"
    ))
    fig.add_trace(go.Scatter(
        x = [std2_end, std2_end],
        y = [0, 1],
        mode = "lines",
        name = "2nd Ending Standard Deviation"
    ))
    fig.add_trace(go.Scatter(
        x = [std3_start, std3_start],
        y = [0, 1],
        mode = "lines",
        name = "3rd Starting Standard Deviation"
    ))
    fig.add_trace(go.Scatter(
        x = [std3_end, std3_end],
        y = [0, 1],
        mode = "lines",
        name = "3rd Ending Standard Deviation"
    ))
    fig.show()

setup()
plot_graph()