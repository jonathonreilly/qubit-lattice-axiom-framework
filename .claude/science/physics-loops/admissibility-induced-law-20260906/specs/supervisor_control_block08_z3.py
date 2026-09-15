"""Supervisor control, block 08: the three-dimensional monotone formation law.
Exact arithmetic (fractions) only. Items:
  (1) K, K^2, K_3 at a triple; the one-neighbor sensitivities c_1, c_2, c_3 (max TV over a single recorded-neighbor change);
  (2) the 2x2 plane transfer does not preserve the 2D monotone law (TV, count of differing states); side facts;
  (3) K_3 is not pair-additive (third difference);
  (4) P1 in 3D: the 48 linear extensions of the 2x2x2 product order share recorded sets;
  (5) the sweep-direction rate c/(1-2c) at the triples.
"""
from fractions import Fraction as F
from itertools import product, permutations
import sys, time

AXES = ["+x", "-x", "+y", "-y", "+z", "-z"]
M = 6
def orbit(s, t):
    if s == t: return "p"
    if s[1] == t[1]: return "q"
    return "r"

def phi_table(tr):
    p, q, r = map(F, tr)
    w = {"p": p, "q": q, "r": r}
    return [[w[orbit(AXES[s], AXES[t])] for t in range(M)] for s in range(M)]

def kernels(tr):
    phi = phi_table(tr)
    Z1 = sum(phi[0])
    K = [[phi[s][a] / Z1 for s in range(M)] for a in range(M)]  # K[a][s] = phi(s,a)/Z1
    K2 = [[sum(K[a][s] * K[s][b] for s in range(M)) for b in range(M)] for a in range(M)]
    K3 = {}
    for a in range(M):
        for b in range(M):
            for c in range(M):
                K3[(a, b, c)] = sum(K[a][s] * K[b][s] * K[c][s] for s in range(M))
    return phi, Z1, K, K2, K3

def cond(K, K2, K3, rec):
    """r(s | recorded values rec) as a list over s."""
    k = len(rec)
    if k == 0:
        return [F(1, 6)] * M
    if k == 1:
        a, = rec
        return [K[a][s] for s in range(M)]
    if k == 2:
        a, b = rec
        return [K[a][s] * K[b][s] / K2[a][b] for s in range(M)]
    a, b, c = rec
    return [K[a][s] * K[b][s] * K[c][s] / K3[(a, b, c)] for s in range(M)]

def tv(u, v):
    return sum(abs(x - y) for x, y in zip(u, v)) / 2

def sensitivities(tr):
    phi, Z1, K, K2, K3 = kernels(tr)
    out = {}
    for k in (1, 2, 3):
        best, arg = F(0), None
        for rec in product(range(M), repeat=k):
            base = cond(K, K2, K3, rec)
            for i in range(k):
                for a2 in range(M):
                    if a2 == rec[i]:
                        continue
                    rec2 = list(rec); rec2[i] = a2
                    d = tv(base, cond(K, K2, K3, tuple(rec2)))
                    if d > best:
                        best, arg = d, (rec, i, a2)
        out[k] = (best, arg)
    return out

def mu2d_square(K, K2):
    """The 2D monotone law on the 2x2 square: sites (0,0),(0,1),(1,0),(1,1) as (row, col)."""
    law = {}
    for v in product(range(M), repeat=4):
        v00, v01, v10, v11 = v
        law[v] = F(1, 6) * K[v00][v01] * K[v00][v10] * K[v01][v11] * K[v10][v11] / K2[v01][v10]
    return law

def plane_transfer_2x2(K, K2, K3, w, v):
    """P(w -> v): plane x1=n+1 (v) given plane x1=n (w); plane coordinates (x2, x3): sites 00,01,10,11.
    v00 records w00; v01 records w01, v00; v10 records w10, v00; v11 records w11, v01, v10."""
    w00, w01, w10, w11 = w
    v00, v01, v10, v11 = v
    return (K[w00][v00]
            * K[w01][v01] * K[v00][v01] / K2[w01][v00]
            * K[w10][v10] * K[v00][v10] / K2[w10][v00]
            * K[w11][v11] * K[v01][v11] * K[v10][v11] / K3[(w11, v01, v10)])

def main():
    triples = [(3, 1, 2), (5, 2, 4), (7, 3, 5), (2, 1, 2), (3, 2, 2), (5, 4, 4), (11, 10, 10), (2, 2, 2)]
    print("=== (1) one-neighbor sensitivities c_1, c_2, c_3 and the branching numbers")
    for tr in triples:
        s = sensitivities(tr)
        c = max(s[k][0] for k in (1, 2, 3))
        rate = c / (1 - 2 * c) if 2 * c < 1 else None
        print(f"{tr}: c1={s[1][0]} ({float(s[1][0]):.5f}) c2={s[2][0]} ({float(s[2][0]):.5f}) c3={s[3][0]} ({float(s[3][0]):.5f}); "
              f"c=max={c} ({float(c):.5f}); 2c={float(2*c):.4f} 3c={float(3*c):.4f}; c/(1-2c)={None if rate is None else float(rate):.4f}")
        if s[3][1] is not None:
            print(f"      argmax c3: rec={[AXES[i] for i in s[3][1][0]]} change slot {s[3][1][1]} -> {AXES[s[3][1][2]]}")
    print()
    print("=== (2) the 2x2 plane transfer against the 2D monotone law")
    for tr in [(3, 1, 2), (5, 2, 4), (2, 2, 2)]:
        t0 = time.time()
        phi, Z1, K, K2, K3 = kernels(tr)
        mu = mu2d_square(K, K2)
        states = list(product(range(M), repeat=4))
        assert sum(mu.values()) == 1
        # push forward
        nu = {v: F(0) for v in states}
        for w in states:
            mw = mu[w]
            for v in states:
                nu[v] += mw * plane_transfer_2x2(K, K2, K3, w, v)
        assert sum(nu.values()) == 1
        diff = sum(1 for v in states if nu[v] != mu[v])
        tvd = sum(abs(nu[v] - mu[v]) for v in states) / 2
        # side facts on nu: one-site marginals; the row x3=0 pair (v00,v10)?? careful: coordinates (x2,x3): 00,01,10,11.
        # rows of the plane at fixed x3: x3=0 -> sites 00,10 ; x3=1 -> sites 01,11 ; columns at fixed x2: x2=0 -> 00,01 ; x2=1 -> 10,11
        def pair_law(law, i, j):
            out = {}
            for v in states:
                out[(v[i], v[j])] = out.get((v[i], v[j]), F(0)) + law[v]
            return out
        def is_K_pair(pl):
            return all(pl[(a, b)] == F(1, 6) * K[a][b] for a in range(M) for b in range(M))
        one = [sum(law for v, law in nu.items() if v[i] == s) for i in range(4) for s in range(M)]
        uniform = all(x == F(1, 6) for x in one)
        print(f"{tr}: nu = mu P differs from mu on {diff}/1296 states, TV = {tvd} ({float(tvd):.6g}); one-site marginals uniform: {uniform}; "
              f"row x3=0 (00,10) K-pair: {is_K_pair(pair_law(nu,0,2))}; row x3=1 (01,11): {is_K_pair(pair_law(nu,1,3))}; "
              f"col x2=0 (00,01): {is_K_pair(pair_law(nu,0,1))}; col x2=1 (10,11): {is_K_pair(pair_law(nu,2,3))}; anti-diag (01,10) K^2-pair: "
              f"{all(pair_law(nu,1,2)[(a,b)] == F(1,6)*K2[a][b] for a in range(M) for b in range(M))}; {time.time()-t0:.1f}s")
    print()
    print("=== (3) K_3 is not pair-additive: third difference of log K_3 (as a ratio of products)")
    for tr in [(3, 1, 2), (5, 2, 4), (2, 2, 2)]:
        phi, Z1, K, K2, K3 = kernels(tr)
        x, y, z = 0, 2, 4  # +x, +y, +z
        num = K3[(x, x, x)] * K3[(y, y, x)] * K3[(y, x, z)] * K3[(x, y, z)]
        den = K3[(y, x, x)] * K3[(x, y, x)] * K3[(x, x, z)] * K3[(y, y, z)]
        print(f"{tr}: product ratio = {num/den} -> pair-additive would give 1; not pair-additive: {num != den}")
    print()
    print("=== (4) P1 in 3D: linear extensions of the 2x2x2 product order share the recorded sets")
    sites = list(product(range(2), repeat=3))
    def preds(x):
        return [tuple(x[i] - (1 if j == i else 0) for i in range(3)) for j in range(3) if x[j] > 0]
    def extensions(remaining, chosen):
        if not remaining:
            yield tuple(chosen); return
        for x in list(remaining):
            if all(p in chosen for p in preds(x)):
                yield from extensions(remaining - {x}, chosen + [x])
    exts = list(extensions(set(sites), []))
    recsets = set()
    for e in exts:
        pos = {s: t for t, s in enumerate(e)}
        rec = tuple(tuple(sorted(y for y in sites if sum(abs(a - b) for a, b in zip(x, y)) == 1 and pos[y] < pos[x])) for x in sites)
        recsets.add(rec)
    print(f"linear extensions of the 2x2x2 product order: {len(exts)}; distinct recorded-set families: {len(recsets)}; "
          f"recorded sets = predecessors: {list(recsets)[0] == tuple(tuple(sorted(preds(x))) for x in sites)}")

if __name__ == "__main__":
    main()
