from ta.trend import EMAIndicator


def calculate_ema(close):
    """
    Returns EMA20, EMA50, EMA200
    """

    ema20 = EMAIndicator(close, window=20).ema_indicator()
    ema50 = EMAIndicator(close, window=50).ema_indicator()
    ema200 = EMAIndicator(close, window=200).ema_indicator()

    return ema20, ema50, ema200