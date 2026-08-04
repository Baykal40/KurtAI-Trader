from config import client


def get_usdt_coins(limit=100):

    tickers = client.get_ticker()

    coins = []

    for coin in tickers:

        if coin["symbol"].endswith("USDT"):

            coins.append({
                "symbol": coin["symbol"],
                "volume": float(coin["quoteVolume"])
            })

    coins.sort(
        key=lambda x: x["volume"],
        reverse=True
    )

    return coins[:limit]