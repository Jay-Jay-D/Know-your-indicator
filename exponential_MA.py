import numpy as np

def EMA(na_series, period):
    ema = np.copy(na_series)
    alpha = 2.0 / (period + 1)
    for n in range(1, ema.shape[0]):
        ema[n] = alpha * na_series[n] + (1 - alpha)* ema[n-1]
    return ema    