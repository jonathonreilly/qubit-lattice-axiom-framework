"""Spin action on the matter pair, built from definitions (independent)."""
AUDIT_TIMEOUT_SEC = 1800
import itertools, numpy as np
from scipy.linalg import expm

I2 = np.eye(2); X = np.array([[0, 1], [1, 0]], complex); Y = np.array([[0, -1j], [1j, 0]]); Z = np.diag([1., -1.]).astype(complex)
SIG = [X, Y, Z]
# matter Majoranas on qubits (4,5) of a site, JW inside the matter pair
CHI = [np.kron(X, I2), np.kron(Y, I2), np.kron(Z, X), np.kron(Z, Y)]   # chi6..chi9
c_up = (CHI[0] + 1j * CHI[1]) / 2
c_dn = (CHI[2] + 1j * CHI[3]) / 2
C = [c_up, c_dn]
Cd = [c.conj().T for c in C]
P_up = -1j * CHI[0] @ CHI[1]; P_dn = -1j * CHI[2] @ CHI[3]
Nop = Cd[0] @ C[0] + Cd[1] @ C[1]
S = [0.5 * sum(Cd[s] @ C[t] * sig[s, t] for s in range(2) for t in range(2)) for sig in SIG]

def quat_2O():
    units = [np.array(v, float) for v in np.eye(4)]
    Q = []
    for u in units:
        Q += [u, -u]
    for sg in itertools.product([1, -1], repeat=4):
        Q.append(0.5 * np.array(sg, float))
    for a, b in itertools.combinations(range(4), 2):
        for sa, sb in itertools.product([1, -1], repeat=2):
            v = np.zeros(4); v[a] = sa; v[b] = sb; Q.append(v / np.sqrt(2))
    return Q

def su2(q):
    """q = (w, x, y, z) -> w I - i (x X + y Y + z Z)"""
    return q[0] * I2 - 1j * (q[1] * X + q[2] * Y + q[3] * Z)

def so3(D):
    return np.array([[np.real(np.trace(SIG[a] @ D @ SIG[b] @ D.conj().T)) / 2 for b in range(3)] for a in range(3)])

def fock(D):
    """U(D) = exp(-i theta n.S) with D = exp(-i theta n.sigma/2)"""
    w = np.clip(np.real(np.trace(D)) / 2, -1, 1)
    theta = 2 * np.arccos(w)
    if abs(np.sin(theta / 2)) < 1e-12:
        # D = +-1
        return expm(-1j * theta * S[2]) if w > 0 else expm(-1j * 2 * np.pi * S[2])
    nvec = np.array([np.real(1j * np.trace(SIG[a] @ D)) / (2 * np.sin(theta / 2)) for a in range(3)])
    G = sum(nvec[a] * S[a] for a in range(3))
    return expm(-1j * theta * G)

def so4(U):
    """U chi_j U^dag = sum_k M[k,j] chi_k"""
    M = np.array([[np.trace(CHI[k] @ U @ CHI[j] @ U.conj().T) / 4 for j in range(4)] for k in range(4)])
    assert np.allclose(M.imag, 0, atol=1e-10)
    return M.real

def qmul(p, q):
    a1, b1, c1, d1 = p; a2, b2, c2, d2 = q
    return np.array([a1*a2 - b1*b2 - c1*c2 - d1*d2, a1*b2 + b1*a2 + c1*d2 - d1*c2,
                     a1*c2 - b1*d2 + c1*a2 + d1*b2, a1*d2 + b1*c2 - c1*b2 + d1*a2])

if __name__ == '__main__':
    Q = quat_2O()
    assert len(Q) == 48
    Ds = [su2(q) for q in Q]; Us = [fock(D) for D in Ds]
    ok = True
    # group closure and rep property (exact, no phase)
    def find(D):
        for i, E in enumerate(Ds):
            if np.allclose(D, E, atol=1e-10): return i
        return None
    nrep = 0
    for i in range(48):
        for j in range(48):
            k = find(Ds[i] @ Ds[j]); assert k is not None
            if not np.allclose(Us[i] @ Us[j], Us[k], atol=1e-9): nrep += 1
    print('rep failures (U(a)U(b) != U(ab)):', nrep)
    m1 = find(-I2)
    print('U(-1) == P_up P_dn :', np.allclose(Us[m1], P_up @ P_dn))
    # SO(3) images are proper cubic rotations, 2-to-1 onto O
    Rs = [np.rint(so3(D)).astype(int) for D in Ds]
    assert all(np.allclose(so3(D), R) for D, R in zip(Ds, Rs))
    print('distinct SO(3) images:', len({tuple(R.flatten()) for R in Rs}))
    # N and matter parity conserved
    print('N conserved:', all(np.allclose(U @ Nop @ U.conj().T, Nop) for U in Us))
    print('P_up P_dn conserved:', all(np.allclose(U @ P_up @ P_dn @ U.conj().T, P_up @ P_dn) for U in Us))
    print('P_up + P_dn conserved:', all(np.allclose(U @ (P_up + P_dn) @ U.conj().T, P_up + P_dn) for U in Us))
    print('P_up alone conserved for all:', all(np.allclose(U @ P_up @ U.conj().T, P_up) for U in Us))
    # c^dag transforms as doublet: U c_s^dag U^dag = sum_t c_t^dag D_ts
    dbl = all(np.allclose(U @ Cd[s] @ U.conj().T, sum(Cd[t] * D[t, s] for t in range(2))) for U, D in zip(Us, Ds) for s in range(2))
    print('U c_s^dag U^dag = sum_t c_t^dag D_ts :', dbl)
    # spin vector transforms with the SO(3) image: U S_b U^dag = sum_a R_ab S_a
    vec = all(np.allclose(U @ S[b] @ U.conj().T, sum(R[a, b] * S[a] for a in range(3))) for U, R in zip(Us, Rs) for b in range(3))
    print('U S_b U^dag = sum_a R_ab S_a :', vec)
    # vacuum singlet
    vac = np.zeros(4, complex); vac[0] = 1
    print('vacuum invariant:', all(np.allclose(U @ vac, vac) for U in Us))
    # C2 lifts: trace 0
    c2 = [i for i, D in enumerate(Ds) if abs(np.trace(D)) < 1e-12]
    print('#C2 lifts:', len(c2), ' all square to -1 on doublet:',
          all(np.allclose(Ds[i] @ Ds[i], -I2) for i in c2))
    # Clifford-ness on the matter Majoranas: signed permutation?
    ncliff = sum(1 for U in Us if np.allclose(np.abs(so4(U)), np.rint(np.abs(so4(U)))))
    print('#2O elements acting as signed perm of matter Majoranas:', ncliff, '/48')
    for name, cond in [('axis C2', lambda q: abs(q[0]) < 1e-9 and np.sum(np.abs(q[1:]) > 1e-9) == 1),
                       ('edge C2', lambda q: abs(q[0]) < 1e-9 and np.sum(np.abs(q[1:]) > 1e-9) == 2)]:
        idx = [i for i, q in enumerate(Q) if cond(q)]
        cl = [np.allclose(np.abs(so4(Us[i])), np.rint(np.abs(so4(Us[i])))) for i in idx]
        print(f'  {name}: {len(idx)} lifts, Majorana-Clifford: {sum(cl)}')
    # 1/2+0+0 decomposition: character
    chars = [np.trace(U) for U in Us]
    print('characters of the 4-dim matter rep (distinct):', sorted({round(c.real, 6) for c in chars}))
