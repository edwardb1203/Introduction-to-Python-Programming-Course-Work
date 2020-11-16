"""Practice for quiz02."""

from typing import Dict, List


TEAM: Dict[str, List[int]] = {
        "tom": [10, 30, 80],
        "jack": [20, 50, 100, 30]
    }

data: Dict[int, str] = {
        30: "lebron",
        20: "jordan",
        50: "samuel"
    }
salary: Dict[int, int] = {
        20: 1000,
        30: 500,
        40: 10000
    }

DATA2: Dict[str, int] = {"mary": 1000, "katherine": 350, "amanda": 400}

# Basketball Team


def main() -> None:
    print(find_avg_score(TEAM))
    print(join_salary_data(data, salary))
    print(highest_and_lowest(DATA2))
    


def find_avg_score(players: Dict[str, List[int]]) -> Dict[str, int]:
    """Given a player and their scores, returns the average score."""
    for key in players:
        average: int = (sum(players[key]) / len(players[key]))
        players[key] = average
    return players


def join_salary_data(players: Dict[int, str], salaries: Dict[int, int]) -> Dict[str, int]:
    """Matches player names with salary based off of plaer id."""
    pay_list: Dict[str, int] = {}
    for key in players:
        for identity in salaries:
            if key == identity:
                pay_list[players[key]] = salaries[identity]
            if key not in salaries:
                pay_list[players[key]] = -1
    return pay_list


def highest_and_lowest(items: Dict[str, int]) -> Dict[str, str]:
    """Given player names and average scores, finds highs and lows."""
    tracking_avg: List[int] = []
    score_dict: Dict[str, str] = {}
    for key in items:
        tracking_avg.append(items[key])
    best_score: int = max(tracking_avg)
    worst_score: int = min(tracking_avg)
    for key in items:
        if items[key] == best_score:
            score_dict["maxi"] = key
        if items[key] == worst_score:
            score_dict["mini"] = key
    return score_dict







if __name__ == "__main__":
    main()


