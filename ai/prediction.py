def tomorrow_prediction(price, ema20, ema50, rsi, macd, signal):

    confidence = 50

    if price > ema20:
        confidence += 10

    if ema20 > ema50:
        confidence += 10

    if macd > signal:
        confidence += 15

    if 45 <= rsi <= 65:
        confidence += 10

    if confidence >= 80:
        trend = "📈 Bullish"

    elif confidence >= 60:
        trend = "↗ Mild Bullish"

    elif confidence >= 40:
        trend = "➡ Sideways"

    else:
        trend = "📉 Bearish"

    return trend, confidence