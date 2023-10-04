from src.accounting import products_and_share as ps
from src.accounting import users_and_wallets as uw
from src.accounting import system_and_wallet as sw
# import time

"""
Main Simulator - Calculating the system balance sheet for a period of time
"""


class SimulationEngine:
    working_days_month = 21
    working_days_year = 250

    def __init__(self, meta_data):
        self.meta = meta_data

    def simulationRun(self):
        return self.working_days_year, self.working_days_month
        pass

    def subsystem_runner(self):
        pass


if __name__ == "__main__":
    product_share = ps.get_app_meta()
    users_info = None
    system_info = None

    # Metadata
    simulation_meta = {
        "daily_trade_vol": 4e12,  # 1e12 = 1 Hemmat
        "brokerage_fee": 0.0025,  # Income source
        "discount_buble": 0.5,  # The discount rate we are announcing to give to customers
        "discount_real": 0.3,  # The discount rate we are actually going to give to customers
        "score_tax": 0.5,  # the Pellekan V.02 tax system - goes to system treasury
        "simulation_duration": 2,  # in year
        "product_share": product_share,
        "users_meta": users_info,
        "system_meta": system_info
    }
    print("Meta:\n", simulation_meta, "\n")

    se = SimulationEngine(simulation_meta)
    report = se.simulationRun()
    print("report: ", report)
