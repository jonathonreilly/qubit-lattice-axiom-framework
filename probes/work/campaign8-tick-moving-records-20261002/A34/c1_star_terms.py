"""A34 c1: does 'calm forces Heisenberg' (A31 D2) survive star terms beyond pairs?

One star of Z^3: centre 0 plus the six neighbours +-e1, +-e2, +-e3 (7 qubits, dim 128).
Candidate star terms (glued: spin rotations act with the SU(2) lift of each proper cubic turn):
  T  = sum over the 8 octant triples (s1 e1, s2 e2, s3 e3) of s1*s2*s3 * chi(three sites),
       chi(i,j,k) = sigma_i . (sigma_j x sigma_k)   (scalar chirality; three NEIGHBOURS, centre unused)
  P3 = sum over ordered pairs a, b of perpendicular neighbour directions of the cyclic permutation
       (0 -> a -> b -> 0) plus its inverse   (SU(2)-invariant three-site exchange through the centre)
Checks:
  (1) covariance under all 24 proper turns about the centre (site permutation + SU(2) lift);
  (2) every aligned product state |m>^7 is an exact eigenvector (calm), for random m;
  (3) compression next to a record: one neighbour locked to +n or -n; aligned |n> on the rest stays an
      eigenvector;
  (4) the terms are not pair Heisenberg terms: their action on one-flip and two-flip states over |up>^7.
Lattice consequence (printed): one-flip band of J s.s + lam*P3 on Z^3 is one analytic band (one site per
cell), still quadratic at k = 0, so A31 D3's single-ripple no-cone result survives while D2's uniqueness
does not.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import itertools, signal
import numpy as np
signal.alarm(28)

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1, -1]).astype(complex)
P = [X, Y, Z]
N = 7
pos = [np.array([0, 0, 0])] + [s * np.eye(3, dtype=int)[a] for a in range(3) for s in (1, -1)]
index = {tuple(p): i for i, p in enumerate(pos)}

def op(ops):
    out = np.array([[1.0]], complex)
    for j in range(N):
        out = np.kron(out, ops.get(j, I2))
    return out

S = [[op({i: P[c]}) for c in range(3)] for i in range(N)]

def chi(i, j, k):
    out = np.zeros((2 ** N, 2 ** N), complex)
    for a, b, c in itertools.permutations(range(3)):
        sgn = np.linalg.det(np.eye(3)[[a, b, c]])
        out += sgn * S[i][a] @ S[j][b] @ S[k][c]
    return out

T = np.zeros((2 ** N, 2 ** N), complex)
for s1, s2, s3 in itertools.product((1, -1), repeat=3):
    i, j, k = index[(s1, 0, 0)], index[(0, s2, 0)], index[(0, 0, s3)]
    T += s1 * s2 * s3 * chi(i, j, k)

def perm_op(cycle):
    """unitary that moves the content of site cycle[0] to cycle[1], cycle[1] to cycle[2], ..."""
    mp = {cycle[n]: cycle[(n + 1) % len(cycle)] for n in range(len(cycle))}
    dim = 2 ** N
    U = np.zeros((dim, dim))
    for b in range(dim):
        bits = [(b >> (N - 1 - j)) & 1 for j in range(N)]
        nb = bits[:]
        for src, dst in mp.items():
            nb[dst] = bits[src]
        U[sum(bit << (N - 1 - j) for j, bit in enumerate(nb)), b] = 1
    return U

P3 = np.zeros((2 ** N, 2 ** N), complex)
dirs = list(range(1, 7))
for a in dirs:
    for b in dirs:
        if abs(np.dot(pos[a], pos[b])) == 0:
            C = perm_op([0, a, b])
            P3 += C + C.T
H_pair = sum(sum(S[0][c] @ S[i][c] for c in range(3)) for i in dirs)   # centre-to-neighbour Heisenberg

# (1) the 24 proper turns: signed permutation matrices with det +1, with SU(2) lifts
def su2(R):
    w, v = np.linalg.eig(R)
    i = int(np.argmin(abs(w - 1)))
    axis = np.real(v[:, i]); axis /= np.linalg.norm(axis)
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    for sgn in (1, -1):
        Ux = np.cos(ang / 2) * I2 - 1j * np.sin(sgn * ang / 2) * sum(axis[c] * P[c] for c in range(3))
        if all(np.allclose(Ux.conj().T @ P[a] @ Ux, sum(R[a, b] * P[b] for b in range(3))) for a in range(3)):
            return Ux
    raise RuntimeError("no lift")

rots = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for r in range(3):
            R[r, perm[r]] = sg[r]
        if np.isclose(np.linalg.det(R), 1):
            rots.append(R)
assert len(rots) == 24
worst = {"T": 0.0, "P3": 0.0, "pair": 0.0}
for R in rots:
    sp = [index[tuple(np.rint(R @ p).astype(int))] for p in pos]   # site i -> sp[i]
    dim = 2 ** N
    Ps = np.zeros((dim, dim))
    for b in range(dim):
        bits = [(b >> (N - 1 - j)) & 1 for j in range(N)]
        nb = [0] * N
        for j in range(N):
            nb[sp[j]] = bits[j]
        Ps[sum(bit << (N - 1 - j) for j, bit in enumerate(nb)), b] = 1
    Ux = su2(R)
    Uspin = np.array([[1.0]], complex)
    for _ in range(N):
        Uspin = np.kron(Uspin, Ux)
    U = Uspin @ Ps
    for name, Hm in (("T", T), ("P3", P3), ("pair", H_pair)):
        worst[name] = max(worst[name], np.linalg.norm(U @ Hm @ U.conj().T - Hm))
print("(1) covariance under the 24 glued turns, max ||U H U^dag - H||:",
      {k: f"{v:.1e}" for k, v in worst.items()})
print("    norms: ||T|| = %.2f, ||P3|| = %.2f, ||T - proj onto pair span|| below" % (np.linalg.norm(T, 2), np.linalg.norm(P3, 2)))

def aligned(m, n_sites=N):
    th, ph = np.arccos(np.clip(m[2], -1, 1)), np.arctan2(m[1], m[0])
    v = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    out = np.array([1.0], complex)
    for _ in range(n_sites):
        out = np.kron(out, v)
    return out, v

def resid(Hm, psi):
    e = np.vdot(psi, Hm @ psi).real
    return np.linalg.norm(Hm @ psi - e * psi), e

rng = np.random.default_rng(11)
w2 = {"T": 0.0, "P3": 0.0}
for _ in range(20):
    m = rng.normal(size=3); m /= np.linalg.norm(m)
    psi, _ = aligned(m)
    for name, Hm in (("T", T), ("P3", P3)):
        w2[name] = max(w2[name], resid(Hm, psi)[0])
print("(2) calm: max residual ||H psi - E psi|| over 20 random aligned states:", {k: f"{v:.1e}" for k, v in w2.items()})

# (3) compression: lock neighbour site 1 (+e1) to |r>, r = +n or -n; aligned |n> elsewhere
w3 = {}
for _ in range(10):
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    _, v = aligned(n, 1)
    vbar = np.array([-np.conj(v[1]), np.conj(v[0])])
    for cname, r in (("+n", v), ("-n", vbar)):
        Q = op({1: np.outer(r, r.conj())})
        psi = np.array([1.0], complex)
        for j in range(N):
            psi = np.kron(psi, r if j == 1 else v)
        for name, Hm in (("T", T), ("P3", P3)):
            key = f"{name}, record {cname}"
            w3[key] = max(w3.get(key, 0.0), resid(Q @ Hm @ Q, psi)[0])
print("(3) calm next to a record (compressed), max residual:", {k: f"{v:.1e}" for k, v in w3.items()})

# (4) action on one- and two-flip states over |up>^7 (n = z)
up = np.array([1, 0], complex); dn = np.array([0, 1], complex)
def basis(flips):
    out = np.array([1.0], complex)
    for j in range(N):
        out = np.kron(out, dn if j in flips else up)
    return out
one = np.array([basis({i}) for i in range(N)]).T
two = np.array([basis({i, j}) for i in range(N) for j in range(i + 1, N)]).T
for name, Hm in (("T", T), ("P3", P3), ("pair", H_pair)):
    B1 = one.conj().T @ Hm @ one
    B2 = two.conj().T @ Hm @ two
    off1 = B1 - np.diag(np.diag(B1))
    print(f"(4) {name:4s}: one-flip block off-diagonal norm {np.linalg.norm(off1):.3f}; "
          f"two-flip block norm {np.linalg.norm(B2 - np.diag(np.diag(B2))):.3f}; "
          f"face-diagonal hop <+e1|H|+e2> = {B1[1, 3]:.3f}")
# Is T or P3 inside the span of the star's pair Heisenberg terms (all 21 pairs) plus identity?
pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
basis_ops = [np.eye(2 ** N)] + [sum(S[i][c] @ S[j][c] for c in range(3)) for i, j in pairs]
Bm = np.array([b.ravel() for b in basis_ops]).T
for name, Hm in (("T", T), ("P3", P3)):
    coef, *_ = np.linalg.lstsq(Bm, Hm.ravel(), rcond=None)
    print(f"    {name}: distance from span(pair Heisenberg terms on the star, identity) = "
          f"{np.linalg.norm(Hm.ravel() - Bm @ coef) / np.linalg.norm(Hm.ravel()):.3f} (relative)")

# Lattice one-flip band of J s.s + lam P3 (n = z): permutations move the flip, so it is a hopping band
J, lam = -1.0, 0.3
def band(k):
    e = 0.0
    # Heisenberg: one-flip hop amplitude 2J to each neighbour, diagonal -4J per bond touched (relative)
    e += sum(2 * J * np.cos(k[a]) * 2 - 4 * J for a in range(3)) * 1.0
    # P3: each perpendicular ordered pair (a,b) at every centre x gives hops x->x+a->x+b->x and reverse
    for a, b in itertools.permutations(range(6), 2):
        da, db = pos[1 + a], pos[1 + b]
        if np.dot(da, db) != 0:
            continue
        for d in (da, db - da, -db):
            e += lam * (2 * np.cos(np.dot(k, d)) - 2)   # hop minus the vacuum's diagonal share
    return e
ks = [np.array([q, 0, 0]) for q in (0.0, 1e-3, 2e-3)]
E0, E1, E2 = (band(k) for k in ks)
print(f"lattice one-flip band (J={J}, lam={lam}): E(0)={E0:.6f}; curvature (E(2h)-2E(h)+E(0))/h^2 = "
      f"{(E2 - 2 * E1 + E0) / 1e-6:.4f}; slope (E(h)-E(0))/h = {(E1 - E0) / 1e-3:.2e}  -> quadratic, no cone")

# (5) full one-flip block of T relative to the vacuum (is T entirely invisible to single ripples?)
vac = basis(set())
e_vac = np.vdot(vac, T @ vac).real
B1T = one.conj().T @ T @ one - e_vac * np.eye(N)
print(f"(5) T: full one-flip block norm relative to the vacuum energy = {np.linalg.norm(B1T):.1e} (0 => single ripples untouched)")
