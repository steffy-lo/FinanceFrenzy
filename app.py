from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFrame
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTimer

import pandas as pd
import sys

from stock_exchange import StockExchangeDialog
from assets import AssetsDialog
from liabilities import LiabilitiesDialog
from cashflows import CashflowsDialog


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Financial Times")
        self.setWindowIcon(QIcon("./assets/financial-times.png"))
        self.setFixedHeight(1080)
        self.setFixedWidth(1350)
        self.square = QFrame(self)
        self.square.setGeometry(100, 50, 1900, 900)
        self.square.setStyleSheet("QWidget { background-image: url(./assets/news_template.png); background-repeat: no-repeat }")

        self.day = 0
        self.timer = QTimer()
        self.timer.setInterval(3000)
        self.timer.timeout.connect(self.a_day_has_passed)
        self.timer.start()

        self.consumer_dis_data = pd.read_csv("./data/SP-500-Consumer-Discretionary-Historical-Data.csv")
        self.consumer_stp_data = pd.read_csv("./data/SP-500-Consumer-Staples-Historical-Data.csv")
        self.energy_data = pd.read_csv("./data/SP-500-Energy-Historical-Data.csv")
        self.finance_data = pd.read_csv("./data/SP-500-Financials-Historical-Data.csv")
        self.healthcare_data = pd.read_csv("./data/SP-500-Health-Care-Historical-Data.csv")
        self.industrials_data = pd.read_csv("./data/SP-500-Industrials-Historical-Data.csv")
        self.it_data = pd.read_csv("./data/SP-500-Information-Technology-Historical-Data.csv")
        self.materials_data = pd.read_csv("./data/SP-500-Materials-Historical-Data.csv")
        self.real_estate_data = pd.read_csv("./data/SP-500-Real-Estate-Historical-Data.csv")
        self.telecom_data = pd.read_csv("./data/SP-500-Telecom-Services-Historical-Data.csv")
        self.utilities_data = pd.read_csv("./data/SP-500-Utilities-Historical-Data.csv")

        self.inflation_data = pd.read_csv("./data/Inflation.csv")
        self.interest_data = pd.read_csv("./data/Interest_rates.csv")

        self.cashflows = []
        self.cash = 2000
        self.interest_rate = 0
        self.inflation_rate = 0
        self.set_interest_rates()
        self.set_inflation_rates()
        self.news = []

        self.create_widgets()

        self.stock_exchange_dlg = None
        self.cashflows_dlg = None
        self.asset_dlg = None
        self.liabilities_dlg = None

    def create_widgets(self):
        stock_exchange_btn = QPushButton("Stock Exchange", self)
        stock_exchange_btn.setGeometry(1040, 1000, 200, 50)
        stock_exchange_btn.setIcon(QIcon("./assets/stock-exchange.png"))
        stock_exchange_btn.setFont(QFont("Arial", 12))
        stock_exchange_btn.clicked.connect(self.open_stock_exchange)

        stock_exchange_btn = QPushButton("Cashflows", self)
        stock_exchange_btn.setGeometry(720, 1000, 200, 50)
        stock_exchange_btn.setIcon(QIcon("./assets/money.png"))
        stock_exchange_btn.setFont(QFont("Arial", 12))
        stock_exchange_btn.clicked.connect(self.open_cashflows)

        asset_btn = QPushButton("Assets", self)
        asset_btn.setGeometry(100, 1000, 200, 50)
        asset_btn.setFont(QFont("Arial", 12))
        asset_btn.setIcon(QIcon("./assets/assets.png"))
        asset_btn.clicked.connect(self.open_asset)

        liabilities_btn = QPushButton("Liabilities", self)
        liabilities_btn.setGeometry(420, 1000, 200, 50)
        liabilities_btn.setFont(QFont("Arial", 12))
        liabilities_btn.setIcon(QIcon("./assets/liabilities.png"))
        liabilities_btn.clicked.connect(self.open_liabilities)

    def open_stock_exchange(self):
        self.stock_exchange_dlg = StockExchangeDialog(self)
        self.stock_exchange_dlg.exec()

    def open_cashflows(self):
        self.cashflows_dlg = CashflowsDialog(self)
        self.cashflows_dlg.exec()

    def open_asset(self):
        self.asset_dlg = AssetsDialog(self)
        self.asset_dlg.exec()

    def open_liabilities(self):
        self.liabilities_dlg = LiabilitiesDialog(self)
        self.liabilities_dlg.exec()

    def set_interest_rates(self):
        self.interest_rate = self.interest_data.iat[self.day // 20, 1]
        interest_rate_lbl = QLabel("Interest Rate: " + str(self.interest_rate) + "%", self)
        interest_rate_lbl.setFont(QFont("Arial", 12))
        interest_rate_lbl.move(1150, 30)

    def set_inflation_rates(self):
        self.inflation_rate = self.inflation_data.iat[self.day // 365, 1]
        inflation_rate_lbl = QLabel("Inflation Rate: " + str(self.inflation_rate.__round__(2)) + "%", self)
        inflation_rate_lbl.setFont(QFont("Arial", 12))
        inflation_rate_lbl.move(1150, 70)

    def buy_stock(self, stock):
        print(stock)

    def a_day_has_passed(self):
        self.day += 1
        print("A day has passed...")
        if self.stock_exchange_dlg is not None:
            self.stock_exchange_dlg.set_table_values()

        if self.day % 20 == 0:  # a month has passed (5 weekdays * 4 weeks) since we're not counting weekends
            self.cash += 10000
            self.set_interest_rates()
            k = len(self.energy_data.columns) - self.day
            self.cashflows.append({
                "value": 10000,
                "date": self.energy_data.iloc[k]["Date"]
            })
            if self.cashflows_dlg is not None:
                self.cashflows_dlg.set_table_values()

        if self.day % 365 == 0:
            print("A year has passed...")
            self.set_interest_rates()

        if self.day > 52 * 5 + 1:
            self.timer.stop()
            print("GAME OVER!")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
