import util

ZENA_DATA = [
    #{"date": "2023-09-20", "distance_miles": 1.30, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-21", "distance_miles": 2.82, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-23", "distance_miles": 2.91, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-25", "distance_miles": 3.25, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-27", "distance_miles": 3.74, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-29", "distance_miles": 3.80, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-09-30", "distance_miles": 3.94, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-02", "distance_miles": 3.44, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-04", "distance_miles": 3.22, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-05", "distance_miles": 3.96, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-07", "distance_miles": 4.12, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-09", "distance_miles": 1.31, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-11", "distance_miles": 2.44, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-12", "distance_miles": 2.80, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-14", "distance_miles": 5.37, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-16", "distance_miles": 5.32, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-18", "distance_miles": 5.43, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-19", "distance_miles": 5.45, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-21", "distance_miles": 2.66, "time_minutes": 30, "name": "Zena"},
    {"date": "2023-10-23", "distance_miles": 5.34, "time_minutes": 65, "name": "Zena"},
    {"date": "2023-10-25", "distance_miles": 5.66, "time_minutes": 65, "name": "Zena"},
]

ZENA_CONSISTENCY_TUPLES = [(datum['time_minutes'], util.to_date(datum['date'])) for datum in ZENA_DATA]
