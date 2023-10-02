import time

"""
Main Simulator
"""


class SimulationEngine:

    def __init__(self):
        self.num = 1

    def simulationRun(self):
        pass

    def simulationReporter(self):
        return self.num
        pass


if __name__ == "__main__":
    # Metadata
    a = 1
    b = 2
    c = 3

    se = SimulationEngine()
    se.simulationRun()
    report = se.simulationReporter()
