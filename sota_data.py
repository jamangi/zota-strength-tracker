import util

SOTA_DATA = [
    {"date": "2023-09-20", "distance_miles": 2.61, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-21", "distance_miles": 2.64, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-23", "distance_miles": 2.84, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-25", "distance_miles": 2.32, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-27", "distance_miles": 2.67, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-29", "distance_miles": 2.79, "time_minutes": 83, "name": "Sota"},
    {"date": "2023-10-01", "distance_miles": 1.62, "time_minutes": 56, "name": "Sota"},
    {"date": "2023-10-02", "distance_miles": 2.49, "time_minutes": 30, "name": "Sota"}
]

SOTA_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in SOTA_DATA]
