import util

ZENA_DATA = [
    #{"date": "2023-09-20", "distance_miles": 1.30, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-21", "distance_miles": 2.82, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-23", "distance_miles": 2.91, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-25", "distance_miles": 3.25, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-27", "distance_miles": 3.74, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-29", "distance_miles": 3.80, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-30", "distance_miles": 3.94, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-02", "distance_miles": 3.44, "time_minutes": 65, "name": "Zena"}
]

ZENA_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in ZENA_DATA]
