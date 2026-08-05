def score(
    ema20,
    close,
    rsi,
    macd_line,
    signal_line,
    upper_band,
    lower_band
):

    points = 0

    if close > ema20:
        points += 25

    if 45 <= rsi <= 65:
        points += 20

    if macd_line > signal_line:
        points += 25

    if rsi < 30:
        points += 15

    if close <= lower_band:
        points += 15

    if close >= upper_band:
        points -= 10

    return points


def signal(score):

    if score >= 70:
        return "🟢 AL"

    elif score >= 40:
        return "🟡 İZLE"

    return "🔴 BEKLE"