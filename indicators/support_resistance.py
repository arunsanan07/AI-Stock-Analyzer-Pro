def calculate_support_resistance(high, low):

    support = low.tail(20).min()

    resistance = high.tail(20).max()

    return support, resistance