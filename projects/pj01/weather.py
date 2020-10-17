"""Weather analysis from Cyril E. King Airport in St. Thomas!"""
__author__ = "730312903"

from csv import DictReader

import sys

from typing import List, Dict


VALID_OP: List[str] = ["avg", "min", "max", "list", "chart"]


def main() -> None:
    """Entrypoint into program."""
    args: Dict[str, str] = read_args()
    valid_column_selection: List[str] = VALID_COLUMN_function(args["file"])
    if sys.argv[2] not in valid_column_selection:
        print("Invalid column: " + sys.argv[2])
        exit()
    if sys.argv[3] not in VALID_OP:
        print("Invalid operation: " + sys.argv[3])
        exit()
    results = list(args["file"], args["column"])
    dates = dates_function(args["file"], args["column"])
    if args["operation"] == "list":
        print(results)
    if args["operation"] == "min":
        minimum: float = min(results)
        print(minimum)
    if args["operation"] == "max":
        maximum: float = max(results)
        print(maximum)
    if args["operation"] == "avg":
        avg(args["file"], args["column"])
    if args["operation"] == "chart":
        chart_data(results, args["column"], dates)


def VALID_COLUMN_function(desired_file: str) -> List[str]:
    """Establishes a list of valid columns."""
    file_handle = open(desired_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    valid_columns: List[str] = []
    for row in csv_reader:
        for key in row:
            valid_columns.append(key)
    return valid_columns

    file_handle.close()


def dates_function(desired_file: str, desired_column: str) -> List[float]:
    """Returns a list of dates in the desired column of desired file."""
    file_handle = open(desired_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    date_list: List[str] = []
    for row in csv_reader:
        if row["REPORT_TYPE"] == "SOD  ":
            compli_date: str = row["DATE"]
            simple_date = (compli_date[0:10])
            try:
                date_list.append(simple_date)
            except ValueError:
                ...
    return date_list

    file_handle.close()    
             

def read_args() -> Dict[str, str]:
    """Stores arguments in dictionary."""
    if len(sys.argv) != 4:
        print("Usage: python -m projects.pj01.weather [FILE] [COLUMN] [OPERATION]")
        exit()
    return {
        "file": sys.argv[1],
        "column": sys.argv[2],
        "operation": sys.argv[3]

    }


def list(desired_file: str, desired_column: str) -> List[float]:
    """Returns a list of values in the desired column of desired file."""
    file_handle = open(desired_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    weather_values: List[float] = []
    for row in csv_reader:
        if row["REPORT_TYPE"] == "SOD  ":
            try:
                weather_values.append(float(row[desired_column]))
            except ValueError:
                ...
    return weather_values
    
    file_handle.close()


def avg(desired_file: str, desired_column: str) -> float:
    """Given a column, returns the average value."""
    results = list(desired_file, desired_column)
    average: float = ((sum(results)) / (len(results)))
    print(average)


def chart_data(data: List[float], column: str, dates: List[str]) -> None:
    """Charts the weather data for desired column."""
    import matplotlib.pyplot as plt
    plt.plot(dates, data)
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.show()


if __name__ == "__main__":
    main()