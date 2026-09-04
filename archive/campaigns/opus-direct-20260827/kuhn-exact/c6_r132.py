"""C6 -- harness cross-check: run MY pipeline with R132's own divergence-form
tensor-product operator (opus_t206.lat_heat) instead of the Kuhn operator, and check
that it reproduces R132's quoted Richardson numbers.  If it does, the only thing that
differs in kx_run.py is the operator.
"""
import math
import numpy as np
from kx_base import CH_T206, N_MODE, XS
from opus_t205 import coeffs
from opus_t206 import cont_heat, lat_heat, e2

n = N_MODE
J = 30
Ls = [32, 48, 64]
xs = XS


def rich(Fa, Fb, a, b, p):
    r = (b / a) ** p
    return (r * (Fb - 1) - (Fa - 1)) / (r - 1) + 1


print("=== C6  R132 reproduction with the DIVERGENCE-FORM operator (opus_t206.lat_heat) ===")
print("x                        : " + " ".join(f"{q:9.2f}" for q in xs))
for name, ch in CH_T206.items():
    V2c, b1, b2 = coeffs(ch, 64, n)
    v2dens = V2c / 64.0
    kr2 = (2 * math.pi * n / 64) ** 2
    svr = xs / kr2
    Rc = (4 * np.pi * svr) ** 2 * e2(lambda e: cont_heat(64, ch, e, n, svr, J)) / (v2dens * 64 ** 4)
    print(f"\n##### {name}  b1={b1:.9f} #####")
    print("  Rcont                  : " + " ".join(f"{q:9.6f}" for q in Rc))
    for imp in (True, False):
        tag = "IMPR " if imp else "plain"
        F = {}
        for L in Ls:
            kap2 = (2 * math.pi * n / L) ** 2
            sv = xs / kap2
            Rl = (4 * np.pi * sv) ** 2 * e2(lambda e: lat_heat(L, ch, e, n, sv, imp)) / (v2dens * L ** 4)
            F[L] = 1.0 + (Rl - Rc) / (b1 * xs)
            print(f"  {tag} L={L:3d} F          : " + " ".join(f"{q:9.5f}" for q in F[L]))
        lg = np.log(np.array(Ls, float))
        p = np.array([-np.polyfit(lg, np.log(np.abs([F[L][i] - 1 for L in Ls])), 1)[0]
                      for i in range(len(xs))])
        print(f"  {tag}       fitted p   : " + " ".join(f"{q:9.3f}" for q in p)
              + f"   [{p.min():.3f}-{p.max():.3f}]")
        for a, b in ((32, 48), (48, 64)):
            rf, r2 = rich(F[a], F[b], a, b, p), rich(F[a], F[b], a, b, 2.0)
            print(f"    Rich {a}->{b} fitted-p : " + " ".join(f"{q:9.5f}" for q in rf)
                  + f"   [{rf.min():.5f}-{rf.max():.5f}]")
            print(f"    Rich {a}->{b} fixed a^2: " + " ".join(f"{q:9.5f}" for q in r2)
                  + f"   [{r2.min():.5f}-{r2.max():.5f}]")
