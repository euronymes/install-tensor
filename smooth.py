#!/usr/bin/python3

import numpy
import scipy.signal
from collections import deque
from itertools import islice
from numpy import append
from scipy.signal import butter, filtfilt
from scipy.integrate import cumtrapz
from bisect import insort, bisect_left


def integre(var_in, f_ech, npts, npts2):
    """Integration, filtrage passe haut, et zero padding sur la fin"""

    # Première étape, on lisse sur le nombre de points
    b2, a2 = butter(4, 2.0 / float(npts), btype="low")
    bx = filtfilt(b2, a2, var_in - numpy.mean(var_in))
    var = cumtrapz(bx, dx=1.0 / f_ech)

    b2, a2 = butter(4, 2.0 / float(npts2), btype="high")
    var2 = filtfilt(b2, a2, var)
    var3 = append(var2, var2[-1])

    var3 = var3 - numpy.mean(var3)

    # On annule l'effet sur les premiers points, (effets de bord)
    var3[0 : int(npts2)] = 0.0

    return var3


def smooth(interval, window_size):
    window = numpy.ones(int(window_size), dtype=numpy.float32) / float(window_size)

    hy = numpy.convolve(interval, window, "valid")
    return append(hy, hy[-1] + numpy.zeros(len(interval) - len(hy)))


def c_smooth(interval, window_size):
    window = numpy.ones(int(window_size)) / numpy.double(window_size)

    ar = numpy.convolve(interval.real, window, "same")
    ai = numpy.convolve(interval.imag, window, "same")

    return ar + ai * 1j


def bandpass(var, cutoff_bas, cutoff_haut, freq):
    b, a = butter(4, (cutoff_bas / (freq / 2.0)), btype="low")
    b2, a2 = butter(4, (cutoff_haut / (freq / 2.0)), btype="low")
    bx = filtfilt(b, a, var)
    bx2 = var - bx

    return filtfilt(b2, a2, bx2)


def lowpass(var, cutoff_haut, freq):
    b, a = butter(4, (cutoff_haut / (freq / 2.0)), btype="low")
    bx = filtfilt(b, a, var)
    return bx


def highpass(var, cutoff_haut, freq):
    b, a = butter(4, (cutoff_haut / (freq / 2.0)), btype="high")
    bx = filtfilt(b, a, var)
    return bx


def highpass2(var, cutoff_haut, freq):
    norm_pass = cutoff_haut / (freq / 2)

    # Never used
    # norm_stop = 1.5 * norm_pass

    # N, Wn = buttord(wp=norm_pass, ws=norm_stop, gpass=5, gstop=30)

    b, a = butter(3, norm_pass, btype="high")

    # print('fitltre :', N, wn)
    print("b=" + str(b) + ", a=" + str(a))

    return scipy.signal.lfilter(b, a, var)


def running_median_insort(seq, window_size):
    """Contributed by Peter Otten"""

    seq = iter(seq)
    d = deque()
    s = []
    result = []

    for item in islice(seq, window_size):
        d.append(item)
        insort(s, item)
        result.append(s[len(d) // 2])

    m = window_size // 2

    for item in seq:
        old = d.popleft()
        d.append(item)
        del s[bisect_left(s, old)]
        insort(s, item)
        result.append(s[m])

    return result

