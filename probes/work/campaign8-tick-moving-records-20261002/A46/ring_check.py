"""A46 ring_check: the four-spin ring operator on a square face (1,2,3,4 in cyclic order).
(1) P + P^-1 equals (1/4)[(12)(34) + (14)(23) - (13)(24)] + (1/4)[sum of the 6 pair dot products] + 1/4
    in Pauli units ((ij) = s_i.s_j);  (2) its spectrum;  (3) product-state values and the classical
minimum of the polynomial over four unit vectors;  (4) the Klein-twisted (soldered-covariant) form."""
import itertools, signal, numpy as np
signal.alarm(60)
s = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1]).astype(complex)]
I2 = np.eye(2)
def op(site, a, n=4):
    m = np.array([[1.]])
    for k in range(n):
        m = np.kron(m, s[a] if k == site else I2)
    return m
def dot(i, j): return sum(op(i, a) @ op(j, a) for a in range(3))
# cyclic permutation: |s1 s2 s3 s4> -> |s4 s1 s2 s3>
P = np.zeros((16, 16))
for b in range(16):
    bits = [(b >> (3 - k)) & 1 for k in range(4)]
    nb = [bits[3], bits[0], bits[1], bits[2]]
    P[int(''.join(map(str, nb)), 2), b] = 1
R = P + P.T
d = {(i, j): dot(i, j) for i in range(4) for j in range(4) if i < j}
poly = (d[(0, 1)] @ d[(2, 3)] + d[(0, 3)] @ d[(1, 2)] - d[(0, 2)] @ d[(1, 3)]) / 4 + sum(d.values()) / 4 + np.eye(16) / 4
print(f"(1) |P + P^-1 - polynomial| = {np.abs(R - poly).max():.1e}")
ev = np.linalg.eigvalsh(R)
print(f"(2) spectrum of P + P^-1: {sorted(set(np.round(ev, 6)))} with multiplicities {[int(np.sum(np.isclose(ev, v))) for v in sorted(set(np.round(ev, 6)))]}")
Hh = d[(0, 1)] + d[(1, 2)] + d[(2, 3)] + d[(0, 3)]
e, v = np.linalg.eigh(Hh); g = v[:, 0]
print(f"    4-site Heisenberg ring ground state: E = {e[0]:+.4f}, <P + P^-1> = {np.vdot(g, R @ g).real:+.4f}, degeneracy {int(np.sum(np.isclose(e, e[0])))}")
def cvec(m):
    th = np.arccos(np.clip(m[2], -1, 1)); ph = np.arctan2(m[1], m[0])
    return np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
def prod(ms):
    v = np.array([1.])
    for m in ms: v = np.kron(v, cvec(m))
    return v
def cpoly(ms):
    D = lambda i, j: ms[i] @ ms[j]
    return (D(0, 1) * D(2, 3) + D(0, 3) * D(1, 2) - D(0, 2) * D(1, 3)) / 4 + sum(D(i, j) for i in range(4) for j in range(i + 1, 4)) / 4 + 1 / 4
rng = np.random.default_rng(3)
dev = 0.
for _ in range(50):
    ms = rng.normal(size=(4, 3)); ms /= np.linalg.norm(ms, axis=1)[:, None]
    pv = prod(ms); dev = max(dev, abs(np.vdot(pv, R @ pv).real - cpoly(ms)))
print(f"(3) product states: |<P+P^-1> - classical polynomial| over 50 random = {dev:.1e}")
z = np.array([0, 0, 1.]); x = np.array([1., 0, 0]); y = np.array([0, 1., 0])
for lab, ms in (("aligned", [z, z, z, z]), ("Neel", [z, -z, z, -z]), ("coplanar 90-degree", [x, y, -x, -y]), ("collinear uudd", [z, z, -z, -z])):
    print(f"    {lab:20s}: {cpoly(np.array(ms)):+.4f}")
best = np.inf
for _ in range(300):
    ms = rng.normal(size=(4, 3)); ms /= np.linalg.norm(ms, axis=1)[:, None]
    for it in range(400):
        g_ = np.zeros((4, 3)); h = 1e-6
        for i in range(4):
            for a in range(3):
                mp = ms.copy(); mp[i, a] += h; g_[i, a] = (cpoly(mp) - cpoly(ms)) / h
        g_ -= (g_ * ms).sum(1)[:, None] * ms
        ms = ms - 0.2 * g_; ms /= np.linalg.norm(ms, axis=1)[:, None]
    best = min(best, cpoly(ms))
    if _ > 40: break
print(f"    classical minimum of the polynomial over four unit vectors (40 gradient starts): {best:+.4f}")
# (4) Klein-twisted form: R_x R_{x+d} = diag((-1)^{|d|-d_a}) per component; for a face in the (a,b) plane:
print("(4) Klein twist on a face in the (a,b) plane: edges along a -> s^T diag(+1 on a, -1 else) s,"
      " edges along b -> +1 on b, diagonals -> +1 on the face normal c only")
