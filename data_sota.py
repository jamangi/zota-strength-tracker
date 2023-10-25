import util

SOTA_DATA = [
    {"date": "2023-09-20", "distance_miles": 2.61, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-21", "distance_miles": 2.64, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-23", "distance_miles": 2.84, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-25", "distance_miles": 2.32, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-27", "distance_miles": 2.67, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-09-29", "distance_miles": 2.79, "time_minutes": 83, "name": "Sota"},
    {"date": "2023-10-01", "distance_miles": 1.62, "time_minutes": 56, "name": "Sota"},
    {"date": "2023-10-02", "distance_miles": 2.49, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-04", "distance_miles": 2.12, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-05", "distance_miles": 1.99, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-07", "distance_miles": 2.48, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-09", "distance_miles": 2.84, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-11", "distance_miles": 2.75, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-12", "distance_miles": 2.71, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-14", "distance_miles": 1.37, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-16", "distance_miles": 2.84, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-18", "distance_miles": 2.56, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-19", "distance_miles": 2.42, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-21", "distance_miles": 3.01, "time_minutes": 30, "name": "Sota"},
    {"date": "2023-10-23", "distance_miles": 2.80, "time_minutes": 30, "name": "Sota"},
]

SOTA_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in SOTA_DATA]
