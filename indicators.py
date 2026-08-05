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

    ema12 = ema(close, 12)
    ema26 = ema(close, 26)

    macd_line = ema12 - ema26
    signal_line = ema(macd_line, 9)

    return macd_line, signal_line


def atr(close, period=14):

    tr = close.diff().abs()

    return tr.rolling(period).mean()


def bollinger(close, period=20):

    middle = close.rolling(period).mean()

    std = close.rolling(period).std()

    upper = middle + (std * 2)
    lower = middle - (std * 2)

    return upper, middle, lower