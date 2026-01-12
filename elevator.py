#!/usr/bin/env python3

import sys

SINGLE_FLOOR_TRAVEL_TIME = 10  # constant time per floor


class Elevator:
    def __init__(self, start_floor: int):
        self.current_floor = start_floor
        self.total_time = 0
        self.visited_floors = [start_floor]

    def travel_to(self, floor: int):
        distance = abs(self.current_floor - floor)
        travel_time = distance * SINGLE_FLOOR_TRAVEL_TIME

        self.total_time += travel_time
        self.current_floor = floor
        self.visited_floors.append(floor)

    def run(self, destinations):
        for floor in destinations:
            self.travel_to(floor)

        return self.total_time, self.visited_floors


def parse_input(args):
    """
    Expected input format:
    elevator.py start=12 floors=2,9,1,32
    """
    start = None
    floors = []

    for arg in args:
        if arg.startswith("start="):
            start = int(arg.split("=")[1])
        elif arg.startswith("floors="):
            floors = list(map(int, arg.split("=")[1].split(",")))

    if start is None or not floors:
        raise ValueError("Invalid input. Expected start=<int> floors=<comma-separated ints>")

    return start, floors


def main():
    try:
        start_floor, destination_floors = parse_input(sys.argv[1:])
    except Exception as e:
        print(f"Error: {e}")
        print("Usage: python elevator.py start=12 floors=2,9,1,32")
        sys.exit(1)

    elevator = Elevator(start_floor)
    total_time, visited = elevator.run(destination_floors)

    print(f"{total_time} {','.join(map(str, visited))}")


if __name__ == "__main__":
    main()
