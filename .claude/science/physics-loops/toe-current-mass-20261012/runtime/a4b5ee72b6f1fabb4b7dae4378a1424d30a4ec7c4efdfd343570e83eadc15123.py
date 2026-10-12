"""Finite representatives of CURRENT_MASS_FILTER_PROBE equations M2--M25.

This module is the source-mutated candidate, never the independent reference.
Ordinary floating point only; analytic domains/locality are not decided here.
"""
import numpy as np


def energy(q, m, v, a):
    q = np.asarray(q, dtype=float)
    return np.sqrt(m*m + 4*v*v/a**2 * np.sin(a*q/2)**2)


def current(q, m, v, a):
    q = np.asarray(q, dtype=float)
    return np.sin(a*q)/a


def mass_squared(q, m, v, a):
    es = energy(q, m, v, a)
    ps = current(q, m, v, a)
    return float(np.sum(es)**2 - v*v*np.sum(ps)**2)


def boost_mass_multiplier(q, m, v, a):
    q = np.asarray(q, dtype=float)
    es = energy(q, m, v, a)
    ps = current(q, m, v, a)
    return float(2*v*v*np.sum(ps)*(np.sum(es)-np.sum(es*np.cos(a*q))))


def window_radius(m, v, a, delta):
    x = a*a*delta/(4*v*v)
    if x >= 1:
        return np.pi/a
    return 2/a * np.arcsin(x**0.25)


def theta(x):
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    out[x >= 1] = 1.0
    inside = (x > 0) & (x < 1)
    z = x[inside]
    u, w = np.exp(-1/z), np.exp(-1/(1-z))
    out[inside] = u/(u+w)
    return out


def compact_symbol(e, p, m, v, delta, cutoff):
    e, p = np.asarray(e), np.asarray(p)
    z = (e*e-v*v*p*p-m*m)/delta
    chi = theta(2*(1-z))*theta(2*(1+z))
    eta = theta(2*e/m-1)*theta(2-e/cutoff)
    return eta*chi


def filtered_matrix(es, ps, seed, m, v, delta, cutoff):
    de = es[None, :]-es[:, None]
    dp = ps[:, None]-ps[None, :]
    return compact_symbol(de, dp, m, v, delta, cutoff)*seed


def gaussian_symbol(e, p, e0, p0, sigma_t, sigma_s):
    return np.exp(-0.5*(sigma_t*(e-e0))**2-0.5*(sigma_s*(p-p0))**2)
