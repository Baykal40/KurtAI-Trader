class PaperWallet:

    def __init__(self):

        self.balance = 1000
        self.positions = []

        self.max_positions = 10
        self.risk_percent = 10

        self.stop_loss = -5
        self.take_profit = 10

        self.trade_history = []

        self.total_profit = 0
        self.total_loss = 0

    def show(self):

        print()
        print("Paper Wallet")
        print("Bakiye :", round(self.balance, 2), "USDT")
        print("Pozisyon Sayısı :", len(self.positions))
        print("Toplam Kar :", round(self.total_profit, 2), "USDT")
        print("Toplam Zarar :", round(self.total_loss, 2), "USDT")

        if self.positions:

            print()

            for position in self.positions:

                pnl_percent = (
                    (position["current_price"] - position["buy_price"])
                    / position["buy_price"]
                ) * 100

                pnl_usdt = (
                    position["amount"] * pnl_percent / 100
                )

                print(
                    f"{position['symbol']}"
                    f" | Alış: {position['buy_price']:.4f}"
                    f" | Güncel: {position['current_price']:.4f}"
                    f" | %{pnl_percent:.2f}"
                    f" | {pnl_usdt:.2f} USDT"
                )

    def has_position(self, symbol):

        for position in self.positions:

            if position["symbol"] == symbol:
                return True

        return False

    def update_price(self, symbol, price):

        for position in self.positions:

            if position["symbol"] == symbol:

                position["current_price"] = price
                return

    def buy(self, symbol, buy_price):

        if self.has_position(symbol):
            return

        if len(self.positions) >= self.max_positions:
            return

        amount = self.balance * (self.risk_percent / 100)

        if amount <= 0:
            return

        self.balance -= amount

        self.positions.append({
            "symbol": symbol,
            "buy_price": buy_price,
            "current_price": buy_price,
            "amount": amount
        })

        print()
        print("🟢 SATIN ALINDI")
        print(symbol)

    def check_positions(self):

        closed = []

        for position in self.positions:

            pnl_percent = (
                (position["current_price"] - position["buy_price"])
                / position["buy_price"]
            ) * 100

            pnl_usdt = (
                position["amount"] * pnl_percent / 100
            )

            if (
                pnl_percent <= self.stop_loss
                or
                pnl_percent >= self.take_profit
            ):

                self.balance += (
                    position["amount"] + pnl_usdt
                )

                if pnl_usdt >= 0:
                    self.total_profit += pnl_usdt
                else:
                    self.total_loss += abs(pnl_usdt)

                self.trade_history.append({
                    "symbol": position["symbol"],
                    "pnl_percent": round(pnl_percent, 2),
                    "pnl_usdt": round(pnl_usdt, 2)
                })

                print()
                print("🔴 POZİSYON KAPANDI")
                print(position["symbol"])
                print("PnL :", round(pnl_percent, 2), "%")
                print("Kar/Zarar :", round(pnl_usdt, 2), "USDT")

                closed.append(position)

        for position in closed:

            self.positions.remove(position)