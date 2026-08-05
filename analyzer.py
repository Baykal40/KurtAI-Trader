import pandas as pd

from candle_service import get_candles
from indicators import ema, rsi, macd, atr
from strategy import score, signal


def analyze(symbol):

    closes = get_candles(symbol)

    close = pd.Series(closes)

    ema20 = ema(close, 20)
    rsi14 = rsi(close)
    macd_line, signal_line = macd(close)
    atr14 = atr(close)

    score_value = score(
        ema20.iloc[-1],
        close.iloc[-1],
        rsi14.iloc[-1]
    )

    trade = signal(score_value)

    return {
        "symbol": symbol,
        "price": close.iloc[-1],
        "score": score_value,
        "trade": trade
    }