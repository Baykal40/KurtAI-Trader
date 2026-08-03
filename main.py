import pandas as pd

from candle_service import get_candles
from indicators import ema, rsi

closes = get_candles("BTCUSDT")

close = pd.Series(closes)

ema20 = ema(close, 20)

print("Son Fiyat :", close.iloc[-1])
print("EMA20     :", round(ema20.iloc[-1], 2))