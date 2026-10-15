"""OBS-2 side check (dimension-3 structure of an hw2-momentum off-diagonal mass): lattice Dirac embedding
H(k) = tau_z sigma.sin k + tau_x m (m on-site, both corners), plus a condensate sum_k Psi^dag(k) b tau_x Gam Psi(k+Q) + h.c.,
Q = (pi,pi,0) pairing hw1 corners e_x and e_y. Exact 8x8 Bloch block {k, k+Q} at k = e_x + q.
Lorentz-covariant low-energy theory <=> E(q) depends on |q| only (to O(q^2)) and the q = 0 levels are spin-degenerate pairs.
Gam in {1 (spin-blind, OBS-1 r1_offdiag), sigma_z (third-axis spin), sigma_x}."""
import numpy as np
s0 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]; TX = np.kron(sx, s0); TZ = np.kron(sz, s0)
Q = np.array([np.pi, np.pi, 0.0]); ex = np.array([np.pi, 0, 0])
def h(k, m):
    return sum(np.sin(k[a]) * np.kron(sz, SIG[a]) for a in range(3)) + m * TX
def block(q, m, b, G):
    k = ex + q
    B = b * np.kron(sx, G)
    return np.block([[h(k, m), B], [B.conj().T, h(k + Q, m)]])
m, b, kap = 0.01, 0.004, 0.004
dirs = {'x': [1, 0, 0], 'y': [0, 1, 0], 'z': [0, 0, 1], '111': np.ones(3) / np.sqrt(3), '110': np.array([1, 1, 0]) / np.sqrt(2)}
for gname, G in (('1 (blind)', s0), ('sigma_z', sz), ('sigma_x', sx), ('sigma_y', sy)):
    e0 = np.linalg.eigvalsh(block(np.zeros(3), m, b, G))
    pos0 = np.sort(e0[e0 > 0])
    print(f"Gam = {gname}: positive levels at q=0: {np.round(pos0, 7)}")
    rows = []
    for dn, d in dirs.items():
        e = np.linalg.eigvalsh(block(kap * np.array(d, float), m, b, G)); pos = np.sort(e[e > 0])
        # expected Lorentz form E = sqrt(M_i^2 + kap^2) with M_i the q=0 levels (sorted)
        rows.append((dn, pos))
        print(f"   q = {kap} * {dn:4s}: E = {np.round(pos, 7)};  E^2 - E0^2 - kap^2 = {np.round((pos**2 - pos0**2 - kap**2) / kap**2, 4)} (units kap^2)")
