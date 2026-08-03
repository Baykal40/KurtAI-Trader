import pandas as pd

from candle_service import get_candles
from indicators import ema, rsi, macd

closes = get_candles("BTCUSDT")

close = pd.Series(closes)

ema20 = ema(close, 20)
rsi14 = rsi(close)
macd_line, signal_line = macd(close)
print("Son Fiyat :", close.iloc[-1])
print("EMA20     :", round(ema20.iloc[-1], 2))
print("RSI14     :", round(rsi14.iloc[-1], 2))
print("MACD    :", round(macd_line.iloc[-1], 2))
print("Signal  :", round(signal_line.iloc[-1], 2))