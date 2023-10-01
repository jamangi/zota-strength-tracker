import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from zena_data import ZENA_DATA, ZENA_CONSISTENCY_TUPLES
from sota_data import SOTA_DATA, SOTA_CONSISTENCY_TUPLES
from shauntal_tracker.consistency_tracker import calculate_consistency, save_plot

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

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

########################################################################

# Plot Zena's pace over date
ax1.plot(zena_data["date"], zena_data["pace"], label="Zena", color="red")

# Plot Sota's pace over date
ax1.plot(sota_data["date"], sota_data["pace"], label="Sota", color="green")

ax1.set_xlabel("Date")
ax1.set_ylabel("Pace (minutes per mile)")
ax1.set_title("Pace in Minutes per Mile")
ax1.legend()

########################################################################

# Plot Zena's pace over date
ax2.plot(zena_data["date"], zena_data["distance_miles"], label="Zena", color="red")

# Plot Sota's pace over date
ax2.plot(sota_data["date"], sota_data["distance_miles"], label="Sota", color="green")

ax2.set_xlabel("Date")
ax2.set_ylabel("Distance in Miles")
ax2.set_title("Raw Distance")
ax2.legend()

########################################################################

# Adjust layout
plt.tight_layout()

# Save the graph as an image (PNG format)
plt.savefig("pace_graph.png")

# Display the graph (optional, if running in a local environment)
plt.show()



