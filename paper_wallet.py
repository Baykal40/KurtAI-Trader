class PaperWallet:

    def __init__(self):

        self.balance = 1000
        self.positions = []

        self.max_positions = 5
        self.risk_percent = 10

    def show(self):

        print()
        print("Paper Wallet")
        print("Bakiye :", round(self.balance, 2), "USDT")
        print("Pozisyon Sayısı :", len(self.positions))

        if self.positions:

            print()

            for position in self.positions:

                print(
                    f"{position['symbol']}  "
                    f"{round(position['amount'], 2)} USDT"
                )

    def has_position(self, symbol):

        for position in self.positions:

            if position["symbol"] == symbol:
                return True

        return False

    def buy(self, symbol):

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
            "amount": amount
        })

        print()
        print("🟢 SATIN ALINDI")
        print(symbol)
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