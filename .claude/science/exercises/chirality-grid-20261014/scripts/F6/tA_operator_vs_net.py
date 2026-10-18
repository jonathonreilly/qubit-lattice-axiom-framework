"""T-A: operator versus net chirality.  F6 route agent, 2026-10-14.

A1: walker on the site qubit has an exact lattice chirality operator (body-diagonal shift T_d).
A2: random finite-range carriers with N = 2 and N = 4 bands per site (M2(C), M4(C)) have zero net
    monopole charge at the half-filling gap (discrete Stokes), with nodes of both hands present.
"""
import numpy as np
import itertools

rng = np.random.default_rng(20261014)
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2)

# ---------------- A1: real-space walker, L = 4 ----------------
L = 4
n = L ** 3
def idx(x, y, z):
    return ((x % L) * L + (y % L)) * L + (z % L)

def shift(d):
    T = np.zeros((n, n))
    for x, y, z in itertools.product(range(L), repeat=3):
        # (T psi)(r) = psi(r + d)
        T[idx(x, y, z), idx(x + d[0], y + d[1], z + d[2])] = 1.0
    return T

Tx, Ty, Tz = shift((1, 0, 0)), shift((0, 1, 0)), shift((0, 0, 1))
def sinop(T):
    return (T - T.T) / (2j)  # eigenvalue sin p for T psi = e^{ip} psi

H = np.kron(sinop(Tx), sx) + np.kron(sinop(Ty), sy) + np.kron(sinop(Tz), sz)
Td = np.kron(Tx @ Ty @ Tz, I2)
eps = np.kron(np.diag([(-1.0) ** (x + y + z) for x, y, z in itertools.product(range(L), repeat=3)]), I2)
herm = np.abs(H - H.conj().T).max()
comm = np.abs(H @ Td - Td @ H).max()
anti_eps = np.abs(Td @ eps @ Td.T + eps).max()
anti_H_eps = np.abs(H @ eps + eps @ H).max()
m = 0.37
E = np.linalg.eigvalsh(H + m * eps)
print("A1  hermiticity |H-H^+| =", herm)
print("A1  |[H, T_d]| =", comm)
print("A1  |T_d eps T_d^-1 + eps| =", anti_eps)
print("A1  |{H, eps}| =", anti_H_eps, "(so (H+m eps)^2 = H^2 + m^2)")
print("A1  min |E(H + m eps)| =", np.abs(E).min(), " m =", m)

# Berry monopole charge of the lower band of h(k) = sum sigma_a sin k_a around each corner
def hk_walker(k):
    return np.sin(k[0]) * sx + np.sin(k[1]) * sy + np.sin(k[2]) * sz

def lower_vecs(hfun, ks, nocc):
    out = []
    for k in ks:
        w, v = np.linalg.eigh(hfun(k))
        out.append(v[:, :nocc])
    return out

def link(u, v):
    d = np.linalg.det(u.conj().T @ v)
    return d / abs(d)

def cube_charge(hfun, k0, h, nocc, M=6):
    """Discrete Stokes: total Berry flux out of the cube [k0-h, k0+h]^3 / 2pi, using an M x M grid per face."""
    total = 0.0
    g = np.linspace(-h, h, M + 1)
    for axis in range(3):
        for sgn in (+1, -1):
            o1, o2 = [a for a in range(3) if a != axis]
            # face at k_axis = k0_axis + sgn*h, outward normal sgn * e_axis
            vecs = {}
            for i, j in itertools.product(range(M + 1), repeat=2):
                k = np.array(k0, float).copy()
                k[axis] += sgn * h
                k[o1] += g[i]
                k[o2] += g[j]
                w, v = np.linalg.eigh(hfun(k))
                vecs[i, j] = v[:, :nocc]
            flux = 0.0
            for i, j in itertools.product(range(M), repeat=2):
                U = link(vecs[i, j], vecs[i + 1, j]) * link(vecs[i + 1, j], vecs[i + 1, j + 1]) \
                    * link(vecs[i + 1, j + 1], vecs[i, j + 1]) * link(vecs[i, j + 1], vecs[i, j])
                flux += np.angle(U)
            # orientation: (o1, o2, axis) right-handed?  sign of permutation
            perm = [o1, o2, axis]
            par = np.linalg.det(np.eye(3)[perm])
            total += sgn * par * flux
    return total / (2 * np.pi)

rows = []
for c in itertools.product((0, 1), repeat=3):
    k0 = np.pi * np.array(c, float)
    q = cube_charge(hk_walker, k0, 0.3, 1)
    td = (-1) ** sum(c)
    rows.append((c, sum(c), td, q, td * np.rint(q)))
    print(f"A1  corner {c} hw={sum(c)}  T_d eigenvalue={td:+d}  monopole charge={q:+.6f}  product={td*np.rint(q):+.0f}")
prods = {r[4] for r in rows}
print("A1  sign relation holds at all corners:", len(prods) == 1, prods)
print("A1  net monopole charge over corners:", sum(np.rint(r[3]) for r in rows))

# ---------------- A2: random finite-range N-band carriers ----------------
nbrs = [d for d in itertools.product((-1, 0, 1), repeat=3) if d != (0, 0, 0)]
half = [d for d in nbrs if d > (0, 0, 0)]  # one of each +-d pair

def random_carrier(N, scale=1.0):
    h0 = rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))
    h0 = (h0 + h0.conj().T) / 2
    hops = {d: scale * (rng.normal(size=(N, N)) + 1j * rng.normal(size=(N, N))) / 2 for d in half}
    return h0, hops

def H_batch(h0, hops, K):  # K: (...,3)
    out = np.broadcast_to(h0, K.shape[:-1] + h0.shape).astype(complex).copy()
    for d, t in hops.items():
        ph = np.exp(1j * (K @ np.array(d, float)))[..., None, None]
        out += ph * t + np.conj(ph) * t.conj().T
    return out

def census(h0, hops, N, G=20):
    g = 2 * np.pi * np.arange(G) / G
    K = np.stack(np.meshgrid(g, g, g, indexing="ij"), -1)
    w, v = np.linalg.eigh(H_batch(h0, hops, K))
    occ = v[..., : N // 2]  # (G,G,G,N,nocc)
    gapmin = (w[..., N // 2] - w[..., N // 2 - 1]).min()
    def U(mu):
        vs = np.roll(occ, -1, axis=mu)
        d = np.linalg.det(np.einsum("...ai,...aj->...ij", occ.conj(), vs))
        return d / np.abs(d)
    Ux, Uy, Uz = U(0), U(1), U(2)
    def F(Ua, a, Ub, b):  # plaquette in (a,b) plane at k
        return np.angle(Ua * np.roll(Ub, -1, axis=a) * np.conj(np.roll(Ua, -1, axis=b)) * np.conj(Ub))
    Fyz, Fzx, Fxy = F(Uy, 1, Uz, 2), F(Uz, 2, Ux, 0), F(Ux, 0, Uy, 1)
    div = (np.roll(Fyz, -1, 0) - Fyz) + (np.roll(Fzx, -1, 1) - Fzx) + (np.roll(Fxy, -1, 2) - Fxy)
    q = np.rint(div / (2 * np.pi)).astype(int)
    resid = np.abs(div / (2 * np.pi) - q).max()
    return int((q > 0).sum()), int((q < 0).sum()), int(q.sum()), int(np.abs(q).sum()), resid, gapmin

for N in (2, 4):
    both = 0
    nets = []
    for s in range(20):
        h0, hops = random_carrier(N)
        npos, nneg, net, tot, resid, gapmin = census(h0, hops, N)
        nets.append(net)
        if npos > 0 and nneg > 0:
            both += 1
        print(f"A2  N={N} sample {s:2d}: +nodes={npos:3d} -nodes={nneg:3d} net={net:+d}  (integrality resid {resid:.1e}, min gap {gapmin:.2e})")
    print(f"A2  N={N}: all nets zero = {all(x == 0 for x in nets)}; samples with both hands = {both}/20")
