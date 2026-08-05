class PaperWallet:

    def __init__(self):

        self.balance = 1000
        self.positions = []

        self.max_positions = 10
        self.risk_percent = 10

    def show(self):

        print()
        print("Paper Wallet")
        print("Bakiye :", round(self.balance, 2), "USDT")
        print("Pozisyon Sayısı :", len(self.positions))

        if self.positions:

            print()

            for position in self.positions:

                pnl = position["current_price"] - position["buy_price"]
                pnl_percent = (pnl / position["buy_price"]) * 100

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
        print("Alış Fiyatı :", buy_price)
        print("Tutar :", round(amount, 2), "USDT")

    def sell(self, symbol):

        for position in self.positions:

            if position["symbol"] == symbol:

                self.balance += position["amount"]

                self.positions.remove(position)

                print()
                print("🔴 SATILDI")
                print(symbol)

                return