"""C5 R3-2: checks for Theorem T_Gamma (covariant charge on LRL) and the
single-shell kernel's low-q behaviour.

(1) Gamma_L7 ball (exact integer lattice matrices), acting on covectors by
    M^{-T}.  Orbit of an in-band rest momentum p0=(m,0,0,0): growth of |p|_E
    (= |tau| for a covariant charge tau = lambda p, lambda=1), and the
    distribution of the orbit mod the reciprocal lattice 2*pi*diag(1/sqrt7,1,1,1)Z^4.
(2) Unboundedness of Gamma_L7 . v for random, null and spacelike v.
(3) Continuum shell transform: int_{H_1} e^{i k x1} d^3x/x0 = 4 pi K_1(k)/k,
    so k^2 * F -> 4 pi as k -> 0 (a 1/q^2 non-analyticity per orbit shell).
"""
import numpy as np
import mpmath as mp

# ---------------------------------------------------------------- group ball
def spatial(M3):
    M = np.eye(4, dtype=np.int64)
    M[1:, 1:] = M3
    return M


Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
g = np.eye(4, dtype=np.int64)
g[0, 0], g[0, 1], g[1, 0], g[1, 1] = 8, 3, 21, 8
ginv = np.eye(4, dtype=np.int64)
ginv[0, 0], ginv[0, 1], ginv[1, 0], ginv[1, 1] = 8, -3, -21, 8
assert (g.dot(ginv) == np.eye(4)).all()
G7 = np.diag([-7, 1, 1, 1])
assert (g.T.dot(G7).dot(g) == G7).all()

gens = [g, ginv, spatial(Rz), spatial(Rz.T), spatial(Rx), spatial(Rx.T)]

ball = {tuple(np.eye(4, dtype=np.int64).ravel()): 0}
frontier = [np.eye(4, dtype=np.int64)]
MAXN = 60000
length = 0
while frontier and len(ball) < MAXN:
    length += 1
    new = []
    for M in frontier:
        for s in gens:
            P = s.dot(M)
            if np.abs(P).max() > 10**7:
                continue
            key = tuple(P.ravel())
            if key not in ball:
                ball[key] = length
                new.append(P)
    frontier = new
elems = [np.array(k, dtype=np.int64).reshape(4, 4) for k in ball]
lens = np.array(list(ball.values()))
print(f"Gamma_L7 ball: {len(elems)} elements, word length <= {lens.max()}")

D = np.diag([np.sqrt(7.0), 1, 1, 1])
Dinv = np.linalg.inv(D)
ETA = np.diag([-1.0, 1, 1, 1])


def ortho(M):
    return D.dot(M.astype(float)).dot(Dinv)


Lams = [ortho(M) for M in elems]
G7o = G7.astype(object)
assert all((M.astype(object).T.dot(G7o).dot(M.astype(object)) == G7o).all() for M in elems)
print('exact check: every ball element preserves Q7')

# covector action p -> Lambda^{-T} p  (= eta Lambda eta p for Lorentz Lambda)
m = 0.05                      # in-band mass, units with |G^2| >= (2 pi)^2/7 = 5.64
p0 = np.array([m, 0.0, 0.0, 0.0])
orbit = np.array([ETA.dot(L).dot(ETA).dot(p0) for L in Lams])
normE = np.linalg.norm(orbit, axis=1)
print("\n(1) orbit of in-band rest covector p0 = (m,0,0,0), m =", m)
print("    shell check max |p^2 + m^2| =", np.abs(-orbit[:, 0]**2 + (orbit[:, 1:]**2).sum(1) + m**2).max() / m**2, "(relative)")
for Lw in range(0, lens.max() + 1, 2):
    sel = lens <= Lw
    print(f"    word length <= {Lw:2d}: {sel.sum():6d} points, max |tau| = max |p|_E = {normE[sel].max():.4e}")

# reduce mod reciprocal lattice 2 pi diag(1/sqrt7,1,1,1) Z^4
frac = np.mod(D.dot(orbit.T).T / (2 * np.pi), 1.0)
for nb in [4, 6]:
    cells = np.floor(frac * nb).astype(int)
    keys = cells[:, 0] * nb**3 + cells[:, 1] * nb**2 + cells[:, 2] * nb + cells[:, 3]
    occ = len(np.unique(keys))
    # in every occupied cell, the largest |tau| found
    order = np.argsort(keys)
    ks, idx = np.unique(keys[order], return_index=True)
    maxima = np.maximum.reduceat(normE[order], idx)
    big = (normE > 1e3)
    occ_big = len(np.unique(keys[big]))
    print(f"    {nb}^4 = {nb**4} cells of T^4: occupied by orbit {occ}; occupied by points with |tau|>1e3: {occ_big}; "
          f"median over occupied cells of max|tau| = {np.median(maxima):.3e}")

# (2) unboundedness of orbits of arbitrary nonzero vectors
rng = np.random.default_rng(3)
print("\n(2) max |Lambda v|_E over the ball, |v|_E = 1:")
tests = {"random": rng.normal(size=4), "null (1,1,0,0)/sqrt2": np.array([1, 1, 0, 0]) / np.sqrt(2),
         "null (1,0,0,1)/sqrt2": np.array([1, 0, 0, 1]) / np.sqrt(2), "spacelike e3": np.array([0, 0, 0, 1.0])}
for name, v in tests.items():
    v = v / np.linalg.norm(v)
    vals = np.array([np.linalg.norm(L.dot(v)) for L in Lams])
    print(f"    {name:22s}: max {vals.max():.3e}, min {vals.min():.3e}")

# (3) continuum shell transform and its 1/k^2 behaviour
print("\n(3) shell transform F(k) = (4 pi/k) int_0^inf r sin(k r)/sqrt(1+r^2) dr vs 4 pi K1(k)/k:")
mp.mp.dps = 20
for k in [2.0, 0.5, 0.1, 0.02]:
    I = mp.quadosc(lambda r: r * mp.sin(k * r) / mp.sqrt(1 + r * r) - mp.sin(k * r), [0, mp.inf], omega=k) + 1 / k
    F = 4 * mp.pi / k * I
    Fk = 4 * mp.pi * mp.besselk(1, k) / k
    print(f"    k={k:5.2f}: quad {mp.nstr(F, 10)}, Bessel {mp.nstr(Fk, 10)}, k^2 F / (4 pi) = {mp.nstr(k*k*Fk/(4*mp.pi), 8)}")
