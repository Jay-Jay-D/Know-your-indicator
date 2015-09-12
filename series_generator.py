import numpy as np
from numpy import pi

def sinewave_generator(N, level, amplitude, wavelenght):
    return amplitude * np.sin(2 * pi * np.arange(N) / wavelenght) + level


def sawtooth_generator(N, level, amplitude, wavelenght):
    series = np.zeros(N)
    slope = amplitude * 1.0 / wavelenght
    for n in range(N):
        if n % wavelenght == 0:
            series[n] = level - amplitude / 2.0
        else:
            series[n] = series[n-1] + slope
    return series


def add_cauchy_noise(na_series):
    N = na_series.shape[0]
    return na_series + np.random.standard_cauchy(N)
    

def add_trend(na_series, beta):
    N = na_series.shape[0]
    for n in range(N):
        na_series[n] += beta * n
    return na_series
    

def add_jump(na_series, jump):
    jump_point = na_series.shape[0] / 2
    na_series[jump_point:] +=  jump
    return na_series