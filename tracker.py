import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Sample data (replace this with your actual data)
data = [
    {"date": "2023-09-20", "distance_miles": 1.30, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-21", "distance_miles": 2.82, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-23", "distance_miles": 2.91, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-25", "distance_miles": 3.25, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-27", "distance_miles": 3.74, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-29", "distance_miles": 3.80, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-20", "distance_miles": 2.61, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-21", "distance_miles": 2.64, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-23", "distance_miles": 2.84, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-25", "distance_miles": 2.32, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-27", "distance_miles": 2.67, "time_minutes": 30, "name": "Sota"}
]

# Create a Pandas DataFrame from the data
df = pd.DataFrame(data)

# Convert the date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Calculate pace (minutes per mile)
df["pace"] = df["distance_miles"] / df["time_minutes"]

# Separate data for Zena and Sota
zena_data = df[df["name"] == "Zena"]
sota_data = df[df["name"] == "Sota"]

# Create a single plot for both Zena and Sota's pace over date
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

########################################################################

# Plot Zena's pace over date
ax1.plot(zena_data["date"], zena_data["pace"], label="Zena", color="red")

# Plot Sota's pace over date
ax1.plot(sota_data["date"], sota_data["pace"], label="Sota", color="green")

ax1.set_xlabel("Date")
ax1.set_ylabel("Pace (miles per minute)")
ax1.set_title("Pace in Miles per Minute")
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



