import pandas as pd

from candle_service import get_candles
from indicators import ema, rsi, macd, atr, bollinger
from strategy import score, signal


def analyze(symbol):

    candles = get_candles(symbol)

    close = [c["close"] for c in candles]
    high = [c["high"] for c in candles]
    low = [c["low"] for c in candles]

    close_series = pd.Series(close)

    ema20 = ema(close_series, 20)
    rsi14 = rsi(close_series)
    macd_line, signal_line = macd(close_series)
    atr14 = atr(high, low, close)
    upper_band, middle_band, lower_band = bollinger(close_series)

    score_value = score(
        ema20.iloc[-1],
        close_series.iloc[-1],
        rsi14.iloc[-1],
        macd_line.iloc[-1],
        signal_line.iloc[-1],
        upper_band.iloc[-1],
        lower_band.iloc[-1]
    )

    trade = signal(score_value)

    return {
        "symbol": symbol,
        "price": close_series.iloc[-1],
        "score": score_value,
        "trade": trade,
        "atr": atr14.iloc[-1],
        "candles": candles
    }