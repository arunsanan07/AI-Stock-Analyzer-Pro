from ta.trend import MACD


def calculate_macd(close):
    """
    Returns MACD, Signal and Histogram
    """

    macd = MACD(close)

    return (
        macd.macd(),
        macd.macd_signal(),
        macd.macd_diff()
    )