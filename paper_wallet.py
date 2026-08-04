class PaperWallet:

    def __init__(self):

        self.balance = 1000

        self.positions = []

    def show(self):

        print()
        print("Paper Wallet")
        print("Bakiye :", self.balance, "USDT")
        print("Pozisyon Sayısı :", len(self.positions))

    def has_position(self, symbol):

        for position in self.positions:

            if position["symbol"] == symbol:
                return True

        return False

    def buy(self, symbol, amount):

        if self.has_position(symbol):
            return

        if self.balance < amount:
            return

        self.balance -= amount

        self.positions.append({
            "symbol": symbol,
            "amount": amount
        })

        print()
        print("🟢 SATIN ALINDI")
        print(symbol, "-", amount, "USDT")

    def sell(self, symbol):

        for position in self.positions:

            if position["symbol"] == symbol:

                self.balance += position["amount"]

                self.positions.remove(position)

                print()
                print("🔴 SATILDI")
                print(symbol)

                return