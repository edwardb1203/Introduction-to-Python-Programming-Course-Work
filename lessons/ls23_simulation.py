"""Example of stochastic simulation!"""
#from lessons.ls23_simulation import 

from typing import List
from random import randint
from matplotlib import pyplot

TRIALS: int = 312903
MAX_ROLL: int = 12


def main() -> None:
    """Entry point of the simulation."""
    # Simulate N Trials
    results: List[int] = simulate(TRIALS)
    # Count the coutcomes of the trials
    counts: List[int] = count(results)
    # Plot the distribution
    plot(counts)


def simulate(n: int) -> List[int]:
    """Roll a pair of die n times and return a list of summed rolls."""
    rolls: List[int] = []
    # Loop N times and for each iteration:
    for _ in range(0, n):
        # 1. roll a pair of die
        roll: int = randint(1,6) + randint(1,6)
        # 2. keep track of the results
        rolls.append(roll)
    return rolls


def count(results: List[int]) -> List[int]:
    # Establish an empty list for keeping
    #  tallies on each possible result.
    counts: List[int] = []
    for i in range (0, MAX_ROLL + 1):
        counts.append(0)

    # Iterate through each result and 
    #  include its outcome in the tallied
    #  counts.
    for result in results:
        counts[result] = counts[result] + 1

    return counts


def plot(counts: List[int]) -> None:
    """Plot the results of our simulated experiment in a histogram."""
    pyplot.title("Distribution of Rolled Values")
    pyplot.xlabel("Sum of Roll")
    pyplot.ylabel("Frequency")
    xaxis_values: range = range(0, MAX_ROLL + 1)
    pyplot.bar(xaxis_values, counts)
    pyplot.show()


if __name__ == "__main__":
    main()