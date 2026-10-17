"""Item 1/3: cycle classes, gauge, PSG of O and inversion, affine action on momentum, fixed points,
direct unitary-equivalence check H(Rk + pi S_R) = W_R H(k) W_R^T, Kramers antiunitary."""
import itertools, collections, sys
import numpy as np
from model import *

print("enumerated 3/4-cycles through cell 0, by class:", collections.Counter(CYCCLASS))

# ---- rank of local cycles on the L=4 torus (do they generate all contractible cycles?)
L = 4
def tor(n): return tuple(x % L for x in n)
eidx = {}
for n in itertools.product(range(L), repeat=3):
    for j, (c1, c2, sh, kind) in enumerate(ETYPES):
        eidx[(n, j)] = len(eidx)
NE = len(eidx); NV = 12 * L**3
rows = []
for n in itertools.product(range(L), repeat=3):
    for cyc, cl in zip(ALLCYC, CYCCLASS):
        if cl == 'two_triangles': continue
        x = 0
        for i in range(len(cyc)):
            (m1, a), (m2, b) = cyc[i], cyc[(i+1) % len(cyc)]
            j = edge_type(cyc[i], cyc[(i+1) % len(cyc)])
            # representative: the edge type is stored with c1 at the base cell
            c1, c2, sh, kind = ETYPES[j]
            base = m1 if (a == c1 and tuple(y - x_ for x_, y in zip(m1, m2)) == sh) else m2
            x ^= 1 << eidx[(tor(tuple(p + q for p, q in zip(base, n))), j)]
        rows.append(x)
piv = {}
for x in rows:
    while x:
        p = x.bit_length() - 1
        if p in piv: x ^= piv[p]
        else: piv[p] = x; break
print(f"L=4 torus: E={NE}, V={NV}, cycle space dim={NE-NV+1}, rank of local (square,triangle,plaquette,tube) cycles={len(piv)}"
      f"  (expect dim-3 = {NE-NV+1-3})")

# ---- affine action for all flux patterns with commuting translations
def affine_data(F, seed=None):
    u = solve_gauge(F, seed)
    if u is None: return None
    out = []
    for R in ROTS:
        r = psg(u, R)
        if r is None: return u, None
        eta, s = r
        S = (R @ s) % 2
        out.append((R, eta, s, S))
    return u, out

def fixed_points(data, den=8):
    pts = []
    for m in itertools.product(range(den), repeat=3):
        k = np.array(m) * 2 * np.pi / den
        ok = True
        for R, eta, s, S in data:
            d = (R @ k + np.pi * S - k) / (2 * np.pi)
            if np.max(np.abs(d - np.round(d))) > 1e-9: ok = False; break
        if ok: pts.append(tuple(int(x) for x in np.array(m) * 4 // den))  # in units pi/2
    return pts

rng = np.random.default_rng(1)
for Fb in itertools.product((0, 1), repeat=4):
    F = dict(zip(FLUXNAMES, Fb))
    if F['square'] != F['plaquette']: continue
    u, data = affine_data(F)
    if data is None: print(F, 'no translation-invariant PSG'); continue
    fp = fixed_points(data)
    # verify unitary equivalence for this pattern with generic params
    err = 0
    for R, eta, s, S in data:
        W = Wmat(R, eta)
        for _ in range(3):
            k = rng.uniform(-np.pi, np.pi, 3)
            H1 = bloch(u, R @ k + np.pi * S, -1.0, 0.23, -0.41)
            H0 = bloch(u, k, -1.0, 0.23, -0.41)
            err = max(err, np.abs(H1 - W @ H0 @ W.T).max())
    shifts = sorted({tuple(S) for R, eta, s, S in data})
    print(F, ' fixed momenta (units pi/2, grid pi/4):', fp, ' distinct shifts S_R:', shifts, f' max|H(Rk+piS)-W H W^T| = {err:.1e}')

# ---- gauge dependence: another translation-invariant solution
F = dict(square=1, triangle=0, plaquette=1, tube=1)
for seed in (None, 3, 5, 11):
    u, data = affine_data(F, seed)
    print('gauge seed', seed, 'u-links =', ''.join(str(x) for x, e in zip(u, ETYPES) if e[3] == 'l'),
          ' fixed momenta:', fixed_points(data))

# ---- shifts per class for the default pattern
u, data = affine_data(F)
print("\nper-rotation shift S_R (default gauge), tube = pi:")
for R, eta, s, S in data:
    tr = int(np.trace(R))
    print('  trace', tr, 'w1', w1(R), 'axis', [int(x) for x in np.round(np.real(np.linalg.eig(R.astype(float))[1][:, np.argmin(np.abs(np.linalg.eig(R.astype(float))[0]-1))]*10))], 'S_R', S)

# ---- inversion and antiunitary inversion*K
Iv = -np.eye(3, dtype=int)
r = psg(u, Iv)
print("\ninversion PSG solvable for u:", r is not None)
if r is not None:
    etaI, sI = r; SI = (Iv @ sI) % 2; WI = Wmat(Iv, etaI)
    print("  inversion momentum shift S_I =", SI)
    for lam in (-0.5, 0.5):
        e1 = e2 = e3 = 0
        for _ in range(20):
            k = rng.uniform(-np.pi, np.pi, 3)
            H0 = bloch(u, k, -1.0, 0.17, lam)
            # unitary inversion: H(-k + pi S_I) vs W H(k) W^T  (should FAIL for lam != 0: maps lam -> -lam)
            e1 = max(e1, np.abs(bloch(u, -k + np.pi * SI, -1.0, 0.17, lam) - WI @ H0 @ WI.T).max())
            e3 = max(e3, np.abs(bloch(u, -k + np.pi * SI, -1.0, 0.17, -lam) - WI @ H0 @ WI.T).max())
            # antiunitary I*K: H(k + pi S_I) = W H(k)^* W^T
            e2 = max(e2, np.abs(bloch(u, k + np.pi * SI, -1.0, 0.17, lam) - WI @ H0.conj() @ WI.T).max())
        print(f"  lam={lam:+}: |I H I^-1 - H| = {e1:.2e} (I maps lam->-lam: residual {e3:.1e});  |IK H (IK)^-1 - H| = {e2:.2e}")
    sq = np.array([etaI[c] * etaI[rot_corner(Iv, c)] for c in range(12)])
    print("  (IK)^2 per corner = eta(c) eta(-c):", sq)
    # time reversal alone
    e4 = 0
    for _ in range(10):
        k = rng.uniform(-np.pi, np.pi, 3)
        e4 = max(e4, np.abs(bloch(u, -k, -1.0, 0.17, -0.5) - bloch(u, k, -1.0, 0.17, -0.5).conj()).max())
    print(f"  plain K (H(-k) = H(k)^*): residual {e4:.2e} (nonzero: T broken by the chiral term)")
