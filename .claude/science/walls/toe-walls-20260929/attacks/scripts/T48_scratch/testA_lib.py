import numpy as np
from common import *

def observables(R, tu, td):
    Uu, du, ru = dressed_U(R, tu)
    if ru > 1e-8: return None
    Ud, dd, rd = dressed_U(R, td)
    if rd > 1e-8: return None
    a, J = ckm_from(Uu, Ud)
    return dict(Vus=a[0,1], Vcb=a[1,2], Vub=a[0,2], J=J)

