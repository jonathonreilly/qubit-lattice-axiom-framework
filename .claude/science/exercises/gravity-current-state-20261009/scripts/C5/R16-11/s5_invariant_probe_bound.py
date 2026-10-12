"""R16-11 s5 (written before running).  Algebra check of Corollary B-inv in its U(1) form on the 12-link
2D qubit cluster of s2 (open, 2x2 plaquettes).  H = -K sum_p (T_p + T_p^dag) + U sum_v (G_v - g0_v)^2 + mu sum_s S^z_s^2-type
diagonal term (here a random diagonal gauge-invariant potential), exactly gauge invariant.  Ground state |0>.
Probe: the local invariant 'sine-ring' A(k) = sum_p e^{-ik.x_p} i(T_p - T_p^dag) (no conjugate coordinate).
C = sum_s e^{ik.pos_s} eps.E_s, eps transverse.
Pre-registered expectations:
 (i)  Bogoliubov: chi_AA >= |<[C,A]>|^2 / m1(C) at every k (equality not expected).
 (ii) vertex |<[C,A]>| ~ k^1 and m1 ~ k^2 (U(1)), so the lower bound |<[C,A]>|^2/m1 tends to a k-independent constant:
      the bound on a LOCAL INVARIANT probe is O(1), with no division by a vanishing vertex (B-inv; tensor version
      has k^2 and k^4, same cancellation).  This is not a photon measurement (open 2D cluster).
"""
import numpy as np
rng = np.random.default_rng(5)
links = [((i, j), 0) for i in range(2) for j in range(3)] + [((i, j), 1) for i in range(3) for j in range(2)]
n = len(links); D = 2**n
pos = np.array([np.array(v, float) + 0.5*np.eye(2)[d] for (v, d) in links])
bits = ((np.arange(D)[:, None] >> np.arange(n)[None, :]) & 1); sz = bits - 0.5
verts = [(i, j) for i in range(3) for j in range(3)]
def Gv(v):
    g = np.zeros(D)
    for s, (w, d) in enumerate(links):
        if w == v: g += sz[:, s]
        if tuple(np.array(w) + np.eye(2, dtype=int)[d]) == v: g -= sz[:, s]
    return g
Gs = {v: Gv(v) for v in verts}
keys = np.round(np.stack([Gs[v] for v in verts], 1)*2).astype(int)
uniq, inv, cnt = np.unique(keys, axis=0, return_inverse=True, return_counts=True)
ref = int(np.argmax(cnt[inv])); sector = np.all(keys == keys[ref], axis=1)
def L(v, d): return links.index((v, d))
plaqs = []
for i in range(2):
    for j in range(2):
        plus = [L((i, j), 0), L((i + 1, j), 1)]; minus = [L((i, j + 1), 0), L((i, j), 1)]
        plaqs.append((np.array([i + 0.5, j + 0.5]), plus, minus))
def Tp(plus, minus):
    T = np.zeros((D, D))
    for a in range(D):
        if all(bits[a, s] == 0 for s in plus) and all(bits[a, s] == 1 for s in minus):
            b = a
            for s in plus: b |= (1 << s)
            for s in minus: b &= ~(1 << s)
            T[b, a] = 1.0
    return T
Ts = [(x, Tp(pl, mi)) for (x, pl, mi) in plaqs]
# Hamiltonian restricted to the chosen Gauss sector (exactly invariant)
idx = np.where(sector)[0]
K = 1.0
Hs = np.zeros((len(idx), len(idx)))
for x, T in Ts:
    M = T[np.ix_(idx, idx)]; Hs -= K*(M + M.T)
Hs += np.diag(0.3*rng.normal(size=len(idx)))     # random diagonal (gauge-invariant within the sector)
w, V = np.linalg.eigh(Hs); g0 = V[:, 0]; om = w - w[0]
print("sector dim %d ; E0 = %.6f ; gap = %.4f" % (len(idx), w[0], om[1]))
Sz = sz[idx]
for name, d in [('x', [1, 0]), ('gen', [1, 2.3])]:
    d = np.array(d, float); d /= np.linalg.norm(d); e = np.array([-d[1], d[0]])
    print("direction %s" % name)
    for kk in [1e-3, 1e-2, 1e-1, 0.3]:
        k = kk*d
        Cd = Sz @ np.array([e[dd]*np.exp(1j*np.dot(k, pos[s])) for s, (v, dd) in enumerate(links)])
        A = np.zeros((len(idx), len(idx)), complex)
        for x, T in Ts:
            M = T[np.ix_(idx, idx)]; A += np.exp(-1j*np.dot(k, x))*1j*(M - M.T)
        Hc = Hs.astype(complex)
        dc = -np.abs(Cd[:, None] - Cd[None, :])**2*Hc
        m1 = np.vdot(g0, dc @ g0).real
        comm = np.vdot(g0, (Cd[:, None]*A - A*Cd[None, :]) @ g0)
        An0 = V.conj().T @ (A @ g0); Adn0 = V.conj().T @ (A.conj().T @ g0)
        chi = np.sum((np.abs(An0[1:])**2 + np.abs(Adn0[1:])**2)/om[1:])
        lb = abs(comm)**2/m1
        print("  k=%.0e  m1=%.3e  |vertex|=%.3e  chi_AA=%.5f  >=  |vertex|^2/m1=%.5f : %s" % (kk, m1, abs(comm), chi, lb, chi >= lb - 1e-12))
