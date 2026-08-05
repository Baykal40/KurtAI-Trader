from config import client


def get_usdt_coins(limit=100):

    tickers = client.get_ticker()

    coins = []

    for coin in tickers:

        symbol = coin["symbol"]

        if not symbol.endswith("USDT"):
            continue

        if (
            "UP" in symbol
            or "DOWN" in symbol
            or "BULL" in symbol
            or "BEAR" in symbol
        ):
            continue

        volume = float(coin["quoteVolume"])

        if volume < 1_000_000:
            continue

        coins.append({
            "symbol": symbol,
            "volume": volume
        })

    coins.sort(
        key=lambda x: x["volume"],
        reverse=True
    )

    return coins[:limit]