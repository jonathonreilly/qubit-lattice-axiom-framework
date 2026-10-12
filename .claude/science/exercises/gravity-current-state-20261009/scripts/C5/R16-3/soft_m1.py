"""Lemma V check at m = 1: abstract T2g-symmetric vertex 4 g_x g_y exp(-(g_x+g_y)/eta) on W08/W14 (I(B) > 0 just above B = 1)."""
import numpy as np, sys; sys.path.insert(0, '.')
from zz import *; from laws import W08, W14
from verify_w import xi_soft
for law in [W08(), W14()]:
    g, f = law.samples(1 << 15)
    print(law.name, 'I(B) at B=1, 1.1, 1.3:', Icurve(g, f, [1.0, 1.1, 1.3]), '| m=1 soft vertex:', ' '.join('eta=%g: %+.3e' % (eta, xi_soft(g, f, 1.0, eta)) for eta in [1, 0.3, 0.1, 0.03]))
