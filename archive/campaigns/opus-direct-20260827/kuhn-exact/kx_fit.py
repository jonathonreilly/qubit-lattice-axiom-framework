"""kx_fit.py -- rate fits and the two Richardson schemes on the saved F(L,x).

usage: python3 kx_fit.py kx_F_32_48_64_96.npz
"""
import sys
import numpy as np

z = np.load(sys.argv[1] if len(sys.argv) > 1 else "kx_F_32_48_64_96.npz")
xs = z['xs']; Ls = list(z['Ls'])
NX = len(xs)


def rich(Fa, Fb, a, b, p):
    r = (b / a) ** p
    return (r * (Fb - 1) - (Fa - 1)) / (r - 1) + 1


def rng(v):
    return f"{np.min(v):.5f}-{np.max(v):.5f}"


hdr = "x                        : " + " ".join(f"{q:9.2f}" for q in xs)
for name in ("CONFORMAL", "TRACELESS-TT"):
    b1 = float(z[f"{name}|b1"][0]); b2 = float(z[f"{name}|b2"][0])
    print(f"\n########## {name}   b1={b1:.9f}  b2={b2:.9f} ##########")
    print(hdr)
    print("Rcont exact              : " + " ".join(f"{q:9.6f}" for q in z[f"{name}|Rc"]))
    for imp in (True, False):
        tag = "IMPR " if imp else "plain"
        F = {L: z[f"{name}|{imp}|{L}|F"] for L in Ls}
        print(f"\n--- {tag} ---")
        for L in Ls:
            print(f"  F   L={L:3d}               : " + " ".join(f"{q:9.5f}" for q in F[L]))
        for L in Ls:
            print(f"  F-1   L={L:3d} (signed)    : " + " ".join(f"{q:9.2e}" for q in F[L] - 1))
        sgn = np.array([len(set(np.sign(np.array([F[L][i] - 1 for L in Ls])))) > 1
                        for i in range(NX)])
        print("  sign change in F-1?      : " + " ".join(f"{'  **YES**' if q else '        .':>9s}"
                                                         for q in sgn))
        # two-term model  F-1 = c2 (a/a0)^2 + c4 (a/a0)^4,  a = 1/L, a0 = 1/64
        A = np.stack([(64.0 / np.array(Ls, float)) ** 2, (64.0 / np.array(Ls, float)) ** 4], 1)
        cs = np.array([np.linalg.lstsq(A, np.array([F[L][i] - 1 for L in Ls]),
                                       rcond=None)[0] for i in range(NX)])
        res = np.array([np.max(np.abs(A @ cs[i] - np.array([F[L][i] - 1 for L in Ls])))
                        for i in range(NX)])
        print("  2-term fit c2 (a^2@L=64) : " + " ".join(f"{q:9.2e}" for q in cs[:, 0]))
        print("  2-term fit c4 (a^4@L=64) : " + " ".join(f"{q:9.2e}" for q in cs[:, 1]))
        print("  2-term max residual      : " + " ".join(f"{q:9.2e}" for q in res))
        # local pairwise rates
        for a, b in zip(Ls[:-1], Ls[1:]):
            pl = np.log(np.abs(F[a] - 1) / np.abs(F[b] - 1)) / np.log(b / a)
            print(f"  local rate p {a}->{b:3d}   : " + " ".join(f"{q:9.3f}" for q in pl))
        for Lset in ([32, 48, 64], list(Ls)):
            if not all(L in F for L in Lset) or len(Lset) < 3:
                continue
            lg = np.log(np.array(Lset, float))
            p = np.array([-np.polyfit(lg, np.log(np.abs([F[L][i] - 1 for L in Lset])), 1)[0]
                          for i in range(NX)])
            print(f"  FITTED p over {Lset}: " + " ".join(f"{q:9.3f}" for q in p))
            for a, b in zip(Lset[:-1], Lset[1:]):
                rf = rich(F[a], F[b], a, b, p)
                r2 = rich(F[a], F[b], a, b, 2.0)
                print(f"     Rich {a:3d}->{b:3d} fitted-p : " + " ".join(f"{q:9.5f}" for q in rf)
                      + f"   [{rng(rf)}]")
                print(f"     Rich {a:3d}->{b:3d} fixed a^2: " + " ".join(f"{q:9.5f}" for q in r2)
                      + f"   [{rng(r2)}]")
