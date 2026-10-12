"""Shared 1D band profiles for C5 R9-9 (copied in form from R8-2's r82_edge.py, parameters B=2.0, B2=3.1).
eps^2 = m^2 + sum_i u(k_i).  Each profile returns (u, u', u'') on a periodic grid.
 L : R7-1 literal  u = s^2,  s = rho k + (1-rho) sin k       (doublers at k_i = pi)
 G : R8-2 gapped   u' = rho 2k + (1-rho) C sin k, u = int u'  (k^2 on the box, monotone edge)
 NN: nearest-neighbour KG control  u = 2 - 2 cos k
"""
import numpy as np
from scipy.interpolate import CubicSpline

B, B2 = 2.0, 3.1

def sstep(x):
    x = np.clip(x, 0.0, 1.0)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        e1 = np.where(x > 0, np.exp(-1.0/np.where(x > 0, x, 1)), 0.0)
        e2 = np.where(x < 1, np.exp(-1.0/np.where(x < 1, 1-x, 1)), 0.0)
    return e1/(e1+e2)

def wrap(k):
    return -(((-k) + np.pi) % (2*np.pi) - np.pi)

def plateau(k, a, b):
    return sstep((b - np.abs(wrap(k)))/(b - a))

def s_L(k):
    k = wrap(k); r = plateau(k, B, B2)
    return r*k + (1-r)*np.sin(k)

Cg = 2*B/np.sin(B)
_NG = 400001
_kg = np.linspace(0, np.pi, _NG)
_up = plateau(_kg, B, B2)*2*_kg + (1-plateau(_kg, B, B2))*Cg*np.sin(_kg)
_ug = np.concatenate([[0.0], np.cumsum(0.5*(_up[1:]+_up[:-1])*np.diff(_kg))])
_ucs = CubicSpline(_kg, _ug)

def up_G(k):
    kw = wrap(k); ka = np.abs(kw); r = plateau(ka, B, B2)
    return np.sign(kw)*(r*2*ka + (1-r)*Cg*np.sin(ka))

def u_G(k):
    ka = np.abs(wrap(k))
    return np.where(ka <= B, ka*ka, _ucs(np.minimum(ka, np.pi)))

def profile(name, k, h=1e-5):
    if name == 'NN':
        return 2-2*np.cos(k), 2*np.sin(k), 2*np.cos(k)
    if name == 'L':
        s = s_L(k); sp = (s_L(k+h)-s_L(k-h))/(2*h); spp = (s_L(k+1e-4)-2*s+s_L(k-1e-4))/1e-8
        return s*s, 2*s*sp, 2*(sp*sp + s*spp)
    if name == 'G':
        return u_G(k), up_G(k), (up_G(k+h)-up_G(k-h))/(2*h)
    raise ValueError(name)
