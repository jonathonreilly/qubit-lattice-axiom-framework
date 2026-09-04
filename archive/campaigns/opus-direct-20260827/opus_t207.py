"""
T207 - final: induced Einstein-Hilbert ratio per channel, measured against the
EXACT continuum reference instead of a truncated series.

   F(L,x) = 1 + (Rlat - Rcont)/(b1 x)
          = (measured a1 response) / (continuum a1 response)

with the entire a2/a3/... content removed exactly rather than approximately.
Reports F, its convergence rate, and the Richardson extrapolation.
"""
import numpy as np, sys, time
from opus_t205 import coeffs
from opus_t206 import cont_heat, lat_heat, e2

n = 2; J = 30
xs = np.array([0.4, 0.6, 0.8, 1.0, 1.4, 2.0])
CH = {"CONFORMAL": {0: 1, 1: 1, 2: 1, 3: 1}, "TRACELESS-TT": {1: 1, 2: -1}}
Ls = [int(a) for a in sys.argv[1:]] or [32, 48, 64]

print("x                    : " + " ".join(f"{q:8.2f}" for q in xs))
for name, ch in CH.items():
    V2c, b1, b2 = coeffs(ch, 64, n)
    v2dens = V2c/64.0          # Vol_2 = v2dens * L^4  (V2c is per-column, prop to L)
    # exact continuum ratio is L-independent (T202); evaluate once
    Lr = 64; kr = 2*np.pi*n/Lr
    Rc = (4*np.pi*(xs/kr**2))**2*e2(lambda e: cont_heat(Lr, ch, e, n, xs/kr**2, J))/(v2dens*Lr**4)
    print(f"\n===== {name}   b1={b1:.6f} =====")
    print("  Rcont exact        : " + " ".join(f"{q:8.5f}" for q in Rc))
    F = {}
    for imp in (True, False):
        for L in Ls:
            t0 = time.time(); kap = 2*np.pi*n/L; sv = xs/kap**2
            Rl = (4*np.pi*sv)**2*e2(lambda e: lat_heat(L, ch, e, n, sv, imp))/(v2dens*L**4)
            F[(imp, L)] = 1.0 + (Rl-Rc)/(b1*xs)
            print(f"  {'IMPR ' if imp else 'plain'} L={L:3d} F        : "
                  + " ".join(f"{q:8.4f}" for q in F[(imp, L)]) + f"   [{time.time()-t0:.0f}s]")
        lg = np.log(np.array(Ls, float))
        p = [-np.polyfit(lg, np.log(np.abs([F[(imp, L)][i]-1 for L in Ls])), 1)[0]
             for i in range(len(xs))]
        print(f"  {'IMPR ' if imp else 'plain'}       rate p   : " + " ".join(f"{q:8.3f}" for q in p))
        a, b = Ls[-2], Ls[-1]
        rich = [( (b/a)**pi*(F[(imp,b)][i]-1) - (F[(imp,a)][i]-1) )/((b/a)**pi - 1) + 1
                for i, pi in enumerate(p)]
        print(f"  {'IMPR ' if imp else 'plain'}   Richardson   : " + " ".join(f"{q:8.5f}" for q in rich))
