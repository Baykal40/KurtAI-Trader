import pandas as pd


def ema(close, period):
    return close.ewm(span=period, adjust=False).mean()


def rsi(close, period=14):

    delta = close.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean()
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean()

    rs = avg_gain / avg_loss

    return 100 - (100 / (1 + rs))


def macd(close):

    ema12 = ema(close, 12)
    ema26 = ema(close, 26)

    macd_line = ema12 - ema26
    signal_line = ema(macd_line, 9)

    return macd_line, signal_line


def atr(high, low, close, period=14):

    high = pd.Series(high)
    low = pd.Series(low)
    close = pd.Series(close)

    prev_close = close.shift(1)

    tr = pd.concat(
        [
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs()
        ],
        axis=1
    ).max(axis=1)

    return tr.ewm(alpha=1 / period, adjust=False).mean()


def adx(high, low, close, period=14):

    high = pd.Series(high)
    low = pd.Series(low)
    close = pd.Series(close)

    up_move = high.diff()
    down_move = -low.diff()

    plus_dm = up_move.where(
        (up_move > down_move) & (up_move > 0),
        0.0
    )

    minus_dm = down_move.where(
        (down_move > up_move) & (down_move > 0),
        0.0
    )

    prev_close = close.shift(1)

    tr = pd.concat(
        [
            high - low,
            (high - prev_close).abs(),
            (low - prev_close).abs()
        ],
        axis=1
    ).max(axis=1)

    atr_value = tr.ewm(alpha=1 / period, adjust=False).mean()

    plus_di = (
        plus_dm.ewm(alpha=1 / period, adjust=False).mean()
        / atr_value
    ) * 100

    minus_di = (
        minus_dm.ewm(alpha=1 / period, adjust=False).mean()
        / atr_value
    ) * 100

    dx = (
        (plus_di - minus_di).abs()
        / (plus_di + minus_di)
    ) * 100

    adx_line = dx.ewm(alpha=1 / period, adjust=False).mean()

    return adx_line


def bollinger(close, period=20):

    middle = close.rolling(period).mean()

    std = close.rolling(period).std()

    upper = middle + (std * 2)
    lower = middle - (std * 2)

    return upper, middle, lower