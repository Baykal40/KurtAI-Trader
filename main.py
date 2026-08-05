from analyzer import analyze
from paper_wallet import PaperWallet
from scanner import get_usdt_coins

import time

wallet = PaperWallet()

coins = get_usdt_coins(100)

start = time.time()

results = []

for coin in coins:

    result = analyze(coin["symbol"])

    results.append(result)

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print()
print("=" * 50)
print(f"{'Coin':12} {'Score':>6} {'Karar':>12}")
print("=" * 50)

for coin in results[:10]:

    print(
        f"{coin['symbol']:12}"
        f"{coin['score']:>8}"
        f"{coin['trade']:>12}"
    )

for coin in results:

    wallet.update_price(
        coin["symbol"],
        coin["price"]
    )

    if coin["trade"] == "🟢 AL":

        wallet.buy(
            coin["symbol"],
            coin["price"]
        )

wallet.check_positions()

end = time.time()

print()
print("Analiz Süresi:", round(end - start, 2), "saniye")

wallet.show()