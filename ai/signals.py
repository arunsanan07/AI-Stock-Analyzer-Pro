def generate_signal(rsi, macd, signal):

    score = 0

    if rsi < 30:
        score += 2
    elif rsi < 40:
        score += 1
    elif rsi > 70:
        score -= 2
    elif rsi > 60:
        score -= 1

    if macd > signal:
        score += 2
    else:
        score -= 2

    if score >= 3:
        return "🟢 STRONG BUY"

    elif score >= 1:
        return "🟢 BUY"

    elif score <= -3:
        return "🔴 STRONG SELL"

    elif score <= -1:
        return "🔴 SELL"

    return "🟡 HOLD"