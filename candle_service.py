from config import client


def get_candles(symbol, interval="1h", limit=200):

    klines = client.get_klines(
        symbol=symbol,
        interval=interval,
        limit=limit
    )

    closes = []

    for k in klines:
        closes.append(float(k[4]))

    return closes