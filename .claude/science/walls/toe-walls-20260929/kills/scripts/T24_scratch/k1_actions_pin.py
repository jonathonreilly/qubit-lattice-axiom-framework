"""Kill check k1: which of the four soldering actions of O (common.rho) pin which corners?
Independent of A_pin: uses common.rho for the Bloch-vector action, group-average of random real
trigonometric d(k) so that d(g k) = rho(g) d(k), scalar d0 free.  Report max |d| per Hamming-weight class of corner,
ranges 1 and 2, 100 samples each.  Also checks the pin by explicit SU(2) lifts (spinor) for the full action."""
import itertools, sys
import numpy as np
sys.path.insert(0, "rerun")
from common import O, rho, su2_of_rotation, SIG, I2
rng = np.random.default_rng(777)
corners = [np.array(n) * np.pi for n in itertools.product([0, 1], repeat=3)]
hw = [sum(n) for n in itertools.product([0, 1], repeat=3)]

def rand_symbol(r, kind, group):
    ws = [w for w in itertools.product(range(-r, r + 1), repeat=3) if w != (0, 0, 0)]
    half = []; seen = set()
    for w in ws:
        if tuple(-np.array(w)) in seen: continue
        seen.add(w); half.append(w)
    # coefficients c_w (cos), s_w (sin), each in R^3 (vector of d)
    C = {w: (rng.normal(size=3), rng.normal(size=3)) for w in half}
    c0 = rng.normal(size=3)
    def d(k):
        out = np.zeros(3)
        for g in group:
            R = rho(kind, g)
            gk = g @ k
            v = c0.copy()
            for w, (cc, ss) in C.items():
                ph = gk @ np.array(w)
                v += cc * np.cos(ph) + ss * np.sin(ph)
            out += R.T @ v          # d_av(k) = mean_g rho(g)^-1 d(g k)
        return out / len(group)
    return d

print("max |d(corner)| by Hamming-weight class hw=0,1,2,3 (median over 60 samples of the max over the class)")
for kind in ["trivial", "sign", "axis", "full"]:
    for r in [1, 2]:
        vals = {h: [] for h in range(4)}
        for s in range(60):
            d = rand_symbol(r, kind, O)
            for c, h in zip(corners, hw):
                vals[h].append(np.linalg.norm(d(c)))
        med = [float(np.median(vals[h])) for h in range(4)]
        mx = [float(np.max(vals[h])) for h in range(4)]
        print(f"  action={kind:8s} range {r}: median |d| hw0..3 = {[f'{m:.1e}' for m in med]}")
# spinor-lift version of the pin for the full action, only D2 = {1, C2x, C2y, C2z}
print("spinor-lift check (D2 only): H(k) -> U H(g^-1 k) U^dag averaged, then value at corners")
D2 = [g for g in O if np.array_equal(np.abs(g), np.eye(3, dtype=int)) and round(np.linalg.det(g)) == 1]
print("  |D2| =", len(D2))
def rand_H(r):
    ws = [w for w in itertools.product(range(-r, r + 1), repeat=3) if w != (0, 0, 0)]
    A = {w: (rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))) for w in ws}
    def H(k):
        M = np.zeros((2, 2), complex)
        for w, a in A.items():
            M += a * np.exp(1j * (k @ np.array(w)))
        return (M + M.conj().T) / 2
    return H
worst = 0
for s in range(40):
    H0 = rand_H(2)
    def Hav(k):
        tot = np.zeros((2, 2), complex)
        for g in D2:
            U = su2_of_rotation(g.astype(float))
            tot += U @ H0(g.T @ k) @ U.conj().T      # covariant: H(g k) = U H(k) U^dag
        return tot / len(D2)
    for c in corners:
        Hc = Hav(c)
        off = Hc - np.trace(Hc) / 2 * np.eye(2)
        worst = max(worst, np.abs(off).max())
print(f"  max traceless part of averaged H at any corner = {worst:.1e}")
