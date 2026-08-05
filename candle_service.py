from config import client


def get_candles(symbol, interval="1h", limit=200):

    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    candles = []

    for k in klines:

        candles.append({
            "open": float(k[1]),
            "high": float(k[2]),
            "low": float(k[3]),
            "close": float(k[4]),
            "volume": float(k[5]),
            "time": int(k[0])
        })

    return candles