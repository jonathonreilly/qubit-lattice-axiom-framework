"""GUIDE for row 1085: the face gap m(t = 0) of the plaquette box (n = 2, beta_T = 0) as a minimum over all sheet-sector
cycles (p_1, p_2, p_3, p_4), doubled spins up to PMAX, against m(t = infinity) from P_0 M P_0.
Sector (p, q) of one sheet: basis (j1, j2) with p and q in j1 x j2 (multiplicity free for n = 2);
X entry = (1/2) sqrt(d1 d1' d2 d2') {p j2' j1'; 1/2 j1 j2}{q j2' j1'; 1/2 j1 j2} (Edmonds 7.1.6 once on the left indices, once on the
right; the remaining phase is constant on a sector and X is bipartite, so it does not change the spectrum).
Usage: python3 endpoint2.py JMAX2 A D PMAX"""
import sys, math, itertools, numpy as np
from scipy.special import ive
import tplaq
from tplaq import sixj, ok

def sector(p, q, J2):
    B = [(a, b) for a in range(J2+1) for b in range(J2+1) if ok(a, b, p) and ok(a, b, q)]
    idx = {s: i for i, s in enumerate(B)}
    X = np.zeros((len(B), len(B)))
    for (a, b), i in idx.items():
        for da in (-1, 1):
            for db in (-1, 1):
                t = (a+da, b+db)
                if t in idx:
                    X[idx[t], i] = 0.5 * math.sqrt((a+1)*(a+da+1)*(b+1)*(b+db+1)) * sixj(p, b+db, a+da, 1, a, b) * sixj(q, b+db, a+da, 1, a, b)
    assert np.abs(X - X.T).max() < 1e-12
    return B, X

def tops(B, X, bM, k=2):
    w, U = np.linalg.eigh(X)
    E2 = (U * np.exp(bM * (w - 1.0))) @ U.T / (2.0 * ive(1, bM) / bM)
    u = tplaq.uvec(bM, 400)
    kk = np.array([math.sqrt(u[a] * u[b]) for (a, b) in B])
    return np.linalg.eigvalsh(kk[:, None] * E2 * kk[None, :])[::-1][:k]

if __name__ == '__main__':
    J2, A, D, PM = (int(x) for x in sys.argv[1:5])
    S = tplaq.setup(A, D)
    secs = {(p, q): sector(p, q, J2) for p in range(PM+1) for q in range(p, PM+1) if (p+q) % 2 == 0}
    print(f"# 2Jmax {J2}, A {A} D {D}, sheet spins doubled up to {PM}")
    print("bM  gap_singlet  best cycle (doubled p) and its m   m(t=0)  m(t=inf)  m(inf)-m(0)   second-best cycle m")
    for bM in (0.5, 1.0, 2.0, 2.4, 3.0, 4.0, 6.0, 8.0, 8.5, 9.0, 10.0, 12.0, 16.0, 24.0):
        mu = {}
        for (p, q), (B, X) in secs.items():
            t = tops(B, X, bM); mu[(p, q)] = mu[(q, p)] = t
        m00 = mu[(0, 0)]
        g_s = math.log(m00[0] / m00[1])
        cyc = []
        for c in itertools.product(range(PM+1), repeat=4):
            if c == (0, 0, 0, 0) or any((c[i] + c[(i+1) % 4]) % 2 for i in range(4)): continue
            cyc.append((sum(math.log(m00[0] / mu[(c[i], c[(i+1) % 4])][0]) for i in range(4)), c))
        cyc.sort()
        best = cyc[0]; second = next(x for x in cyc if x[0] > best[0] + 1e-9)
        m0 = min(g_s, best[0])
        o = tplaq.run(S, 2, bM, 0.0)
        minf = math.log(o['lam'][0] / o['lam'][1])
        print(f"{bM:5.1f}  {g_s:.6f}  {best[1]} {best[0]:.6f}   {m0:.6f}  {minf:.6f}  {minf-m0:+.6f}   {second[1]} {second[0]:.6f}", flush=True)
