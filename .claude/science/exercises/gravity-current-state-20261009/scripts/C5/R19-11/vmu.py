"""R19-11 (a), vectors: mu_E per vector on the root photon edge gGw(2.9435, fw=1) as a function of a Proca-type mass m
(2 transverse polarizations x R14-3's scalar mu_E formula with g -> g + m^2; the R17-9/R17-12/R18-5 convention, whose
regulator 1e-3 is here varied as a mass). Xi and face rows of the vector evaluator are massless (not mass-scanned)."""
import sys, os, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'arch18'))
from r1712_lib import photonGw
from zz import mu_E
law = photonGw(2.9435, np.pi - 2.9435); g, f = law.samples(1 << 14)
for m in (0.04, 0.02, 0.01, 0.005, 0.0025, 1e-3, 1e-4, 1e-5):
    print('m=%-8g muE/vector %+.13e' % (m, 2*mu_E(g, f, m)), flush=True)
