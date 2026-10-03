"""A34 c11: is A38's patterned calm background H8 the lowest state of its calm pair law, or a stationary state
in the middle of the spectrum?  (own code)

H8: m(r) = ((-1)^rx, (-1)^ry, (-1)^rz)/sqrt3 on Z^3 (period 2). Pair law on a-bonds: J(s.s + s^a s^a) (A38 D2).
One-flip (harmonic) sector on an L^3 torus: hop amplitudes <up_i dn_j|h|dn_i up_j> and on-site costs
sum_bonds [<dn_i up_k|h|dn_i up_k> - <up_i up_k|h|up_i up_k>]. Calm => no 0->1 and 0->2 flip terms, so this block
alone gives the harmonic ripple energies relative to the background. Reported for J = +1 and J = -1:
lowest and highest one-flip energies, number below zero, and symmetry of the spectrum.
"""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[v] = "1"
import itertools, signal
import numpy as np
signal.alarm(28)
X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1.0 + 0j, -1.0]); S = [X, Y, Z]
def m_of(r):
    return np.array([(-1) ** (r[0] % 2), (-1) ** (r[1] % 2), (-1) ** (r[2] % 2)]) / np.sqrt(3)
def kets(m):
    th = np.arccos(np.clip(m[2], -1, 1)); ph = np.arctan2(m[1], m[0])
    up = np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)])
    dn = np.array([-np.exp(-1j * ph) * np.sin(th / 2), np.cos(th / 2)])
    return up, dn
def bond_h(a, J, K):
    return J * sum(np.kron(s, s) for s in S) + K * np.kron(S[a], S[a])
L = 4
sites = list(itertools.product(range(L), repeat=3)); idx = {s: i for i, s in enumerate(sites)}
for J in (1.0, -1.0):
    K = J
    Hm = np.zeros((len(sites), len(sites)), complex)
    dbl = 0.0
    for r in sites:
        for a in range(3):
            r2 = list(r); r2[a] = (r2[a] + 1) % L; r2 = tuple(r2)
            u1, d1 = kets(m_of(r)); u2, d2 = kets(m_of(r2))
            h = bond_h(a, J, K)
            e0 = (np.kron(u1, u2).conj() @ h @ np.kron(u1, u2)).real
            Hm[idx[r], idx[r]] += (np.kron(d1, u2).conj() @ h @ np.kron(d1, u2)).real - e0
            Hm[idx[r2], idx[r2]] += (np.kron(u1, d2).conj() @ h @ np.kron(u1, d2)).real - e0
            Hm[idx[r2], idx[r]] += np.kron(u1, d2).conj() @ h @ np.kron(d1, u2)
            Hm[idx[r], idx[r2]] += np.kron(d1, u2).conj() @ h @ np.kron(u1, d2)
            dbl = max(dbl, abs(np.kron(d1, d2).conj() @ h @ np.kron(u1, u2)))
    assert np.allclose(Hm, Hm.conj().T)
    ev = np.linalg.eigvalsh(Hm)
    print(f"J={J:+.0f} (K=J, D=0): double-flip amplitude max {dbl:.1e}; one-flip energies relative to H8: "
          f"min {ev.min():+.4f}, max {ev.max():+.4f}; below zero {np.sum(ev < -1e-9)} of {len(ev)}; "
          f"spectrum symmetric about 0: {np.allclose(np.sort(ev), np.sort(-ev), atol=1e-9)}")
