"""Chart for pj02."""

from __future__ import annotations
__author__ = "730312903"

from typing import List
from random import random
from projects.pj02 import constants
from math import sin, cos, pi, sqrt
import sys

def main() -> None:
    """Entrypoint of simulation."""
    args: Dict[str, int] = read_args()
    model = Model(args["cellcount"], args["cellspeed"], args["startinginfected"], args["startingimmune"])

def read_args() -> Dict[str, int]:
    """Check for valid CLI arguments and return them in a dictionary."""
    if len(sys.argv) != 5:
        print("Usage: python -m projects.pj02.chart [cellcount] [cellspeed] [startinginfected] [startingimmune]")
        exit()
    return {
        "cellcount": sys.argv[1],
        "cellspeed": sys.argv[2],
        "startinginfected": sys.argv[3],
        "startingimmune": sys.argv[4]
    }

class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, endpt: Point) -> float:
        """Finds the distance between two points."""
        dist: float = sqrt(((endpt.x) - (self.x))**2 + ((endpt.y) - (self.y))**2)
        return dist


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Updates model."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def contract_disease(self) -> None:
        """Infects cell."""
        self.sickness = constants.INFECTED
    
    def is_vulnerable(self) -> bool:
        """Determines sickness of cell, vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Determines sickness of cell, infection."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def color(self) -> str:
        """Determines color of cell based on sickness."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "blue"

    def contact_with(self, cell2: Cell) -> None:
        """Determines if contact was made between cells."""
        if self.is_infected() and cell2.is_vulnerable():
            cell2.contract_disease()
        if cell2.is_infected() and self.is_vulnerable():
            self.contract_disease()
    
    def immunize(self) -> None:
        """Immunizes cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Determines sickness of cell, immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: List[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, starting_in: int, s_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if starting_in >= cells:
            raise ValueError("THERE MUST BE AT LEAST ONE STARTING INFECTED AND ONE HEALTHY!")
        if starting_in <= 0:
            raise ValueError("THERE MUST BE AT LEAST ONE STARTING INFECTED!")
        if s_immune >= cells:
            raise ValueError("EVERYONE CANNOT BE IMMUNE!")
        if s_immune < 0:
            raise ValueError("CANNOT HAVE NEGATIVE IMMUNE!")
        i: int = 0 
        j: int = 0
        self.population = []
        while i < starting_in:
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            sick_cell = Cell(start_loc, start_dir)
            sick_cell.contract_disease()
            self.population.append(sick_cell)
            i += 1
        while j < s_immune:
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            immune_cell = Cell(start_loc, start_dir)
            immune_cell.immunize()
            self.population.append(immune_cell)
            j += 1
        new_range: int = (cells - len(self.population))
        for _ in range(0, (new_range)):
            start_loc = self.random_location()
            start_dir = self.random_direction(speed)
            self.population.append(Cell(start_loc, start_dir))
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()
        self.is_complete()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle = 2.0 * pi * random()
        dir_x = cos(random_angle) * speed
        dir_y = sin(random_angle) * speed
        return Point(dir_x, dir_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1
        
    def check_contacts(self) -> None:
        """Checks if cells have made contact."""
        pop = self.population
        i: int = 0
        while i < len(pop):
            for j in range(i + 1, len(pop)):
                if pop[i].location.distance(pop[j].location) < constants.CELL_RADIUS:
                    pop[i].contact_with(pop[j])
            i += 1
            
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cells in self.population:
            if cells.is_infected():
                return False
        return True

def chart_data(cells: ticks: List[str]) -> None:
    """Charts the cells infection over time."""
    import matplotlib.pyplot as plt
    plt.plot(ticks, cells)
    plt.plot(ticks, cells2)
    plt.xlabel("Time")
    plt.ylabel("Cells")
    plt.show()

if __name__ == "__main__":
    main()