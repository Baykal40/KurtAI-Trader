import pandas as pd


def ema(close, period):
    return close.ewm(span=period, adjust=False).mean()
def rsi(close, period=14):

    delta = close.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))
def macd(close):

    ema12 = close.ewm(span=12, adjust=False).mean()

    ema26 = close.ewm(span=26, adjust=False).mean()

    macd_line = ema12 - ema26

    signal_line = macd_line.ewm(span=9, adjust=False).mean()

    return macd_line, signal_line