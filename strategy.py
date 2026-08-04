def score(
    ema20,
    close,
    rsi
):

    points = 0

    if close > ema20:
        points += 40

    if 40 <= rsi <= 70:
        points += 30

    return points
def signal(score):

    if score >= 60:
        return "🟢 AL"

    return "🔴 BEKLE"