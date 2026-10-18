"""R2 / L1: overlaps whose displacements are fixed by symmetry.

(a) Isolated fixed points of the space group of Z^3 with proper cubic rotations
    (rotation group O, 24 elements, plus integer translations): find all points p in
    the unit cell whose stabiliser fixes p only (no free coordinate), and list their
    squared min-image distances.  Claim: they are the 8 half-integer cube points and
    d^2 = hw/4 (hw = number of half coordinates in the difference).
(b) Real C3-equivariant overlap matrices between two C3 orbits are real circulants;
    their two E singular values are exactly equal.  A T-odd phase splits them.
(c) Positions affine in conserved charges + generation integer, flat Higgs, even kernel:
    every sector has the same singular values.
"""
import itertools, numpy as np
from fractions import Fraction as F

rng = np.random.default_rng(1)

# ---------- (a) proper rotation group O as signed permutation matrices with det +1
mats = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((3, 3), int)
        for i, j in enumerate(perm):
            M[i, j] = signs[i]
        if round(np.linalg.det(M)) == 1:
            mats.append(M)
assert len(mats) == 24

def stab_fixed_dim(p):
    """dimension of the common fixed set of the stabiliser of p (mod Z^3)."""
    stab = []
    for M in mats:
        q = M @ p
        d = q - p
        if all((x.denominator == 1) for x in d):
            stab.append(M)
    # fixed set of stabiliser near p: common kernel of (M - I)
    A = np.vstack([np.array(M, float) - np.eye(3) for M in stab])
    rank = np.linalg.matrix_rank(A)
    return 3 - rank, len(stab)

den = 8
iso = []
for c in itertools.product(range(den), repeat=3):
    p = np.array([F(x, den) for x in c], dtype=object)
    dim, ns = stab_fixed_dim(p)
    if dim == 0:
        iso.append((tuple(str(x) for x in p), ns))
print("(a) isolated fixed points (denominator-8 grid):", len(iso))
for x in iso:
    print("    ", x[0], " stabiliser order", x[1], " orbit size", 24 // x[1])

pts = [np.array([float(F(s)) for s in x[0]]) for x in iso]
d2 = set()
for p in pts:
    for q in pts:
        d = p - q
        d = d - np.round(d)
        d2.add(round(float(d @ d), 6))
print("    squared min-image distances:", sorted(d2), "(= hw/4 for hw in 0..3)")
singlets = [x for x in iso if x[1] == 24]
print("    orbit-size-1 (singlet) positions:", [x[0] for x in singlets])

# ---------- (b) real C3-equivariant kernels on C3 orbits
def rot111(v):
    return np.array([v[2], v[0], v[1]])

def orbit(v):
    return [v, rot111(v), rot111(rot111(v))]

worst_real, splits_c = 0.0, []
for trial in range(2000):
    xL = orbit(rng.normal(size=3)); xR = orbit(rng.normal(size=3))
    # arbitrary real C3-invariant kernel: f depends on invariants of the pair
    a, b, c = rng.normal(size=3)
    def K(x, y):
        d = x - y
        return np.exp(-a * a * d @ d) * (1 + b * (x @ y) + c * np.sum(d ** 3))
    M = np.array([[K(x, y) for y in xR] for x in xL])
    s = np.linalg.svd(M, compute_uv=False)
    # the E pair: the two singular values not belonging to the trivial (1,1,1) vector
    gap = lambda sv: min(abs(sv[0]-sv[1]), abs(sv[1]-sv[2])) / sv[0]
    worst_real = max(worst_real, gap(s))
    # add a T-odd (Aharonov-Bohm) phase on the hop i->i+1
    phi = rng.uniform(0.1, 1.0)
    P = np.array([[np.exp(1j * phi * ((j - i) % 3 == 1) - 1j * phi * ((j - i) % 3 == 2)) for j in range(3)] for i in range(3)])
    Mc = M * P
    splits_c.append(gap(np.linalg.svd(Mc, compute_uv=False)))
    # check circulant structure
    assert np.allclose(M[1, :], np.roll(M[0, :], 1)) or np.allclose(M[1, :], np.roll(M[0, :], -1))
print("(b) real C3-equivariant overlaps: max over 2000 of (closest singular-value pair gap)/s_max =", f"{worst_real:.2e}")
print("    with a T-odd phase: median of the same =", f"{np.median(splits_c):.2e}", " 5th pct", f"{np.percentile(splits_c,5):.2e}")

# ---------- (c) charge-affine positions, flat Higgs
Y = dict(Q=1/6, u=2/3, d=-1/3, L=-1/2, e=-1.0)
BL = dict(Q=1/3, u=1/3, d=1/3, L=-1.0, e=-1.0)
worst = 0
for trial in range(500):
    lam = rng.normal(size=(2, 3))  # 2 charges (Y, B-L) mapped to 3D positions
    mu = rng.normal(size=3)        # generation step
    g = {f: rng.integers(-3, 4, size=3) for f in Y}  # arbitrary generation integers, same for all fields? no: per field
    g_common = rng.integers(-3, 4, size=3)
    pos = {f: [lam[0] * Y[f] + lam[1] * BL[f] + mu * g_common[i] for i in range(3)] for f in Y}
    w = rng.uniform(0.3, 2.0)
    def K(x, y):
        d = x - y
        return np.exp(-(d @ d) / w)
    Mu = np.array([[K(pos['Q'][i], pos['u'][j]) for j in range(3)] for i in range(3)])
    Md = np.array([[K(pos['Q'][i], pos['d'][j]) for j in range(3)] for i in range(3)])
    Me = np.array([[K(pos['L'][i], pos['e'][j]) for j in range(3)] for i in range(3)])
    su, sd, se = [np.linalg.svd(M, compute_uv=False) for M in (Mu, Md, Me)]
    worst = max(worst, np.max(np.abs(su - sd) / su[0]), np.max(np.abs(se - sd) / sd[0]))
print("(c) affine-in-(Y,B-L)+common generation step, flat Higgs: max sector spectrum difference =", f"{worst:.2e}")
# note: if generation integers differ per field the spectra differ -> those integers are supplied charges.
g_diff = 0
for trial in range(200):
    lam = rng.normal(size=(2, 3)); mu = rng.normal(size=3)
    gf = {f: rng.integers(-3, 4, size=3) for f in Y}
    pos = {f: [lam[0] * Y[f] + lam[1] * BL[f] + mu * gf[f][i] for i in range(3)] for f in Y}
    K = lambda x, y: np.exp(-((x - y) @ (x - y)))
    Mu = np.array([[K(pos['Q'][i], pos['u'][j]) for j in range(3)] for i in range(3)])
    Md = np.array([[K(pos['Q'][i], pos['d'][j]) for j in range(3)] for i in range(3)])
    g_diff = max(g_diff, np.max(np.abs(np.linalg.svd(Mu, compute_uv=False) - np.linalg.svd(Md, compute_uv=False))))
print("    control, field-dependent generation integers: max difference =", f"{g_diff:.2e}", "(sectors split only via supplied integers)")

# ---------- localized Higgs at a hypercharge-affine position: third-generation ordering
# triple overlap of equal-width Gaussians ~ exp(-sum_{pairs} d^2 / (6 s^2)); positions lam*Y
for name, (yl, yh, yr) in dict(up=(1/6, -1/2, 2/3), down=(1/6, 1/2, -1/3), lepton=(-1/2, 1/2, -1.0)).items():
    s = (yl - yr) ** 2 + (yl - yh) ** 2 + (yh - yr) ** 2
    print(f"    localized Higgs, {name}: pair-sum (in lam^2 units) = {s:.4f}")
print("    -> exponent order down < up < lepton: b heavier than t, ordering wrong")
