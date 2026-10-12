#!/usr/bin/env python3
"""Independent whole-line Fourier diagnostic for a nonsmooth cell indicator."""
import json
import sys
import time

import numpy as np
from numpy.polynomial.legendre import leggauss


def integrate(nodes):
    x, w = leggauss(nodes)
    intervals = np.arange(2048)[:, None]
    q = (intervals + (x[None, :]+1)/2)*np.pi
    weights = w[None, :]*np.pi/2
    indicator_power = np.sinc(q/(2*np.pi))**2
    m, v = 0.9, 1.4
    continuum = np.sqrt((m-1j*v*q)/np.hypot(m, v*q))
    rows = []
    for n in range(1, 10):
        a = 2.**(-n)
        sig = np.hypot(m/2, v/a)
        g, j = sig/2+m/4, sig/2-m/4
        band = g-j*np.exp(-1j*a*q)
        lattice = np.sqrt(np.conj(band)/np.abs(band))
        good = float(np.sum(weights*indicator_power*np.abs(lattice-continuum)**2)/np.pi)
        wrong = float(np.sum(weights*indicator_power*np.abs(lattice-1)**2)/np.pi)
        rows.append(dict(n=n, a=a, squared_error_correct=good, squared_error_missing_continuum_unrotation=wrong))
    return rows


started = time.time()
low, high = integrate(24), integrate(48)
max_difference = max(abs(a[key]-b[key]) for a, b in zip(low, high)
                     for key in ("squared_error_correct", "squared_error_missing_continuum_unrotation"))
qmax = 2048*np.pi
gates = dict(quadrature_agreement=max_difference < 1e-7,
             correct_final_below_first=high[-1]["squared_error_correct"] < high[0]["squared_error_correct"],
             missing_unrotation_detected=(high[-1]["squared_error_missing_continuum_unrotation"]
                                         - high[-1]["squared_error_correct"]) > 1e-3)
result = dict(kind="finite_quadrature_diagnostic_for_exact_dominated_convergence_proof",
              parameters=dict(m=0.9, v=1.4, indicator_interval=[0, 1], qmax=qmax),
              omitted_squared_error_tail_upper_bound=16/(np.pi*qmax),
              low_rule=low, high_rule=high, maximum_quadrature_difference=max_difference,
              seconds=time.time()-started, gates=gates,
              limitations="Tail bound is analytic; quadrature difference is diagnostic, not a rigorous quadrature certificate. No fitted convergence rate.")
print(json.dumps(result, indent=2))
passed = sum(gates.values())
print(f"TOTAL: PASS={passed} FAIL={len(gates)-passed}")
sys.exit(0 if all(gates.values()) else 1)
