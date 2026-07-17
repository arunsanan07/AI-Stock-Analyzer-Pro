from ta.momentum import RSIIndicator


def calculate_rsi(close):
    """
    Returns RSI Series
    """

    rsi = RSIIndicator(close=close, window=14)

    return rsi.rsi()