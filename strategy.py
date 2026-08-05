def score(
    ema20,
    close,
    rsi,
    macd_line,
    signal_line
):

    points = 0

    if close > ema20:
        points += 30

    if 45 <= rsi <= 65:
        points += 20

    if macd_line > signal_line:
        points += 30

    if rsi < 30:
        points += 20

    return points


def signal(score):

    if score >= 70:
        return "🟢 AL"

    elif score >= 40:
        return "🟡 İZLE"

    return "🔴 BEKLE"