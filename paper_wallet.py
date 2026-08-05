class PaperWallet:

    def __init__(self):

        self.balance = 1000
        self.positions = []

        self.max_positions = 10
        self.risk_percent = 10

        self.stop_loss = -5
        self.take_profit = 10

        self.trade_history = []

    def show(self):

        print()
        print("Paper Wallet")
        print("Bakiye :", round(self.balance, 2), "USDT")
        print("Pozisyon Sayısı :", len(self.positions))

        if self.positions:

            print()

            for position in self.positions:

                pnl_percent = (
                    (position["current_price"] - position["buy_price"])
                    / position["buy_price"]
                ) * 100

                print(
                    f"{position['symbol']}"
                    f" | Alış: {position['buy_price']:.4f}"
                    f" | Güncel: {position['current_price']:.4f}"
                    f" | %{pnl_percent:.2f}"
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

            if (
                pnl_percent <= self.stop_loss
                or
                pnl_percent >= self.take_profit
            ):

                self.balance += position["amount"]

                self.trade_history.append({
                    "symbol": position["symbol"],
                    "pnl": round(pnl_percent, 2)
                })

                print()
                print("🔴 POZİSYON KAPANDI")
                print(position["symbol"])
                print("PnL :", round(pnl_percent, 2), "%")

                closed.append(position)

        for position in closed:

            self.positions.remove(position)