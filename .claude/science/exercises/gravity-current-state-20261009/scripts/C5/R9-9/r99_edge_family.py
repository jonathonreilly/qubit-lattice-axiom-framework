"""C5 R9-9: can one edge choice remove the TT speed shift (both polarizations) and the TT mass together?
Edge family u_t = (1-t) u_L + t u_G (box part k^2 fixed for every t), as in R9-2's r92_shear_tune.py.
Speed:  Xi(t) = (1/32) <|V|^2 A_zz / eps^5>,  A_zz = u_t''/2 - 1   (identity checked in r99_tt_selfenergy.out)
Mass (metric seagull, this note's prescription): Dmu(t) = mu_E - mu_T2 = -(1/8) <(u_x^2 + u_y^2 - 6 u_x u_y)/eps^3>
R9-2's flow-seagull mu_E zero: t* = 0.287922 (m=1), 0.297708 (m=0.3)  [R9-2 r92_shear_tune.out, unrefereed]
"""
import numpy as np, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from r99_profiles import profile
from scipy.optimize import brentq
N = 96
k = 2*np.pi*(np.arange(N) - N//2)/N
uL, upL, uppL = profile('L', k); uG, upG, uppG = profile('G', k)

def quantities(t, m):
    u = (1-t)*uL + t*uG; up = (1-t)*upL + t*upG; upp = (1-t)*uppL + t*uppG
    A = upp/2 - 1; p = up/2
    ux, uy, uz = u[:, None, None], u[None, :, None], u[None, None, :]
    px, py = p[:, None, None], p[None, :, None]
    eps = np.sqrt(m*m + ux + uy + uz)
    w = A[None, None, :]/eps**5
    out = {}
    for vn, V2 in [('M,T2g', 4*ux*uy), ('M,Eg', (ux-uy)**2), ('U,T2g', 4*px**2*py**2), ('U,Eg', (px**2-py**2)**2)]:
        out[vn] = np.mean(V2*w)/32
    out['Dmu(metric)'] = -0.125*np.mean((ux**2 + uy**2 - 6*ux*uy)/eps**3)
    return out

for m in (1.0, 0.3):
    ts = np.linspace(0, 1, 21)
    tab = [quantities(t, m) for t in ts]
    print('m = %.1f' % m)
    for key in tab[0]:
        vals = np.array([d[key] for d in tab])
        s = '   %-12s t=0: %+.4e  t=1: %+.4e' % (key, vals[0], vals[-1])
        roots = []
        for i in range(len(ts)-1):
            if np.sign(vals[i]) != np.sign(vals[i+1]):
                roots.append(brentq(lambda t: quantities(t, m)[key], ts[i], ts[i+1], xtol=1e-7))
        s += '   zeros at t* = %s' % (', '.join('%.5f' % r for r in roots) if roots else 'none in [0,1]')
        print(s)
