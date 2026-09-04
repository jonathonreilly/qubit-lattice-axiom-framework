"""kx_run.py -- R132's instrument applied to the KUHN SIMPLICIAL operator.

    F(L,x) = 1 + (Rlat - Rcont)/(b1 x),     x = s kappa^2,  kappa = 2 pi n / L

Rlat  : Kuhn P1-FEM lumped-mass operator (conformal/recheck/kuhn.py), Bloch-reduced,
        improved (B -> B + B diag(C) B / 24, C = tr g / 4) and plain.
Rcont : exact continuum operator on the same perturbed torus, plane-wave
        diagonalisation (opus_t206.cont_heat), NO Seeley-DeWitt truncation.
b1    : analytic, from the Riemann tensor (opus_t205.coeffs).

usage: python3 kx_run.py 32 48 64 [96]
"""
import math, sys, time
import numpy as np
from kx_base import CH_P, CH_T206, N_MODE, XS, lat_trace, e2_sym, fmt
from opus_t205 import coeffs
from opus_t206 import cont_heat

n = N_MODE
J = 30
Ls = [int(a) for a in sys.argv[1:]] or [32, 48, 64]
xs = XS
out = {}

print(f"=== KUHN-EXACT  n={n} J={J} Ls={Ls} ===")
print("x                       : " + " ".join(f"{q:9.2f}" for q in xs))
for name in ("CONFORMAL", "TRACELESS-TT"):
    ch, P = CH_T206[name], CH_P[name]
    V2c, b1, b2 = coeffs(ch, 64, n)
    v2dens = V2c / 64.0
    Lr = 64
    kr2 = (2 * math.pi * n / Lr) ** 2
    svr = xs / kr2
    t0 = time.time()
    Rc = (4 * np.pi * svr) ** 2 * e2_sym(
        lambda e: cont_heat(Lr, ch, e, n, svr, J)) / (v2dens * Lr ** 4)
    print(f"\n===== {name}   b1={b1:.9f}  b2={b2:.9f}  Vol2/L^4={v2dens:.9f} =====")
    print("  Rcont exact           : " + " ".join(f"{q:9.6f}" for q in Rc)
          + f"   [{time.time()-t0:.0f}s]")
    out[(name, 'Rc')] = Rc
    out[(name, 'b1')] = b1
    out[(name, 'b2')] = b2
    for imp in (True, False):
        tag = "IMPR " if imp else "plain"
        for L in Ls:
            t0 = time.time()
            kap2 = (2 * math.pi * n / L) ** 2
            sv = xs / kap2
            K2 = e2_sym(lambda e: lat_trace(L, P, e, n, sv, imp)[0])
            Rl = (4 * np.pi * sv) ** 2 * K2 / (v2dens * L ** 4)
            F = 1.0 + (Rl - Rc) / (b1 * xs)
            out[(name, imp, L, 'Rl')] = Rl
            out[(name, imp, L, 'F')] = F
            print(f"  {tag} L={L:3d} Rlat      : " + " ".join(f"{q:9.6f}" for q in Rl))
            print(f"  {tag} L={L:3d} F         : " + " ".join(f"{q:9.5f}" for q in F)
                  + f"   [{time.time()-t0:.0f}s]", flush=True)

np.savez(f"kx_F_{'_'.join(map(str,Ls))}.npz",
         xs=xs, Ls=np.array(Ls),
         **{("%s|%s" % (k[0], "|".join(map(str, k[1:])))): np.atleast_1d(v)
            for k, v in out.items()})
print("\nsaved kx_F_%s.npz" % "_".join(map(str, Ls)))
