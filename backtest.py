class Backtest:

    def __init__(self):

        self.total_trades = 0
        self.win_trades = 0
        self.loss_trades = 0

        self.total_profit = 0

    def add_trade(self, pnl):

        self.total_trades += 1

        self.total_profit += pnl

        if pnl >= 0:
            self.win_trades += 1
        else:
            self.loss_trades += 1

    def show(self):

        print()
        print("=" * 40)
        print("BACKTEST RAPORU")
        print("=" * 40)

        print("Toplam İşlem :", self.total_trades)
        print("Kazanan      :", self.win_trades)
        print("Kaybeden     :", self.loss_trades)

        if self.total_trades > 0:

            win_rate = (
                self.win_trades
                / self.total_trades
            ) * 100

            print("Win Rate     :", round(win_rate, 2), "%")

        print("Toplam PnL   :", round(self.total_profit, 2), "USDT")