import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from zena_data import ZENA_DATA, ZENA_CONSISTENCY_TUPLES
from sota_data import SOTA_DATA, SOTA_CONSISTENCY_TUPLES
from shauntal_tracker.consistency_tracker import calculate_consistency, save_plot
from plotter import plotter

data = ZENA_DATA + SOTA_DATA
df = pd.DataFrame(data)
df["date"] = pd.to_datetime(df["date"])
df["pace"] = df["time_minutes"] / df["distance_miles"]

zena_data = df[df["name"] == "Zena"]
sota_data = df[df["name"] == "Sota"]

zena_consistency = calculate_consistency(ZENA_CONSISTENCY_TUPLES)
sota_consistency = calculate_consistency(SOTA_CONSISTENCY_TUPLES)
save_plot("Zena Consistency Score", zena_consistency, "zena_score_plot.png")
save_plot("Sota Consistency Score", sota_consistency, "sota_score_plot.png")

zena_line_data = {"line_name": "Zena", "x_data": zena_data["date"], "y_data": zena_data["pace"]}
sota_line_data = {"line_name": "Sota", "x_data": sota_data["date"], "y_data": sota_data["pace"]}
both_lines = [zena_line_data, sota_line_data]

x_label = "Date"
y_label = "Pace (minutes per mile)"
title = "Pace in Minutes per Mile"

plotter(both_lines, title, x_label, y_label, "pace_graph.png")

zena_line_data = {"line_name": "Zena", "x_data": zena_data["date"], "y_data": zena_data["distance_miles"]}
sota_line_data = {"line_name": "Sota", "x_data": sota_data["date"], "y_data": sota_data["distance_miles"]}
both_lines = [zena_line_data, sota_line_data]

x_label = "Date"
y_label = "Distance (miles)"
title = "Distance in Miles"

plotter(both_lines, title, x_label, y_label, "distance_graph.png")
