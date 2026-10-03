"""A45 f2: can a fully soldered parton mean field reduce SU(2) to U(1) and keep the eight Weyl nodes?

Spin-1/2 partons, one per site (one qubit per site after projection).  Bond matrices u_d (2x2),
H = sum_x sum_d f_x^dag u_d f_{x+d},  h(k) = sum_d u_d e^{i k.d}.
 (1) solve the covariance constraints for u_d on NN, face-diagonal, axis-2 and body-diagonal bonds;
 (2) Bloch covariance U(R) h(k) U(R)^dag = h(Rk) for NN lambda + face-diagonal lambda';
 (3) eta-SU(2): 2-site Fock check of [eta^+, bond] for opposite / same sublattice signs;
 (4) the 8 nodes stay at E=0; their speeds; no other zeros on a grid.
"""
import itertools, signal
import numpy as np

signal.alarm(55)
rng = np.random.default_rng(3)
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1]).astype(complex)
S = [sx, sy, sz]

def proper_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for i, p in enumerate(perm):
                M[p, i] = signs[i]
            if round(np.linalg.det(M)) == 1:
                out.append(M)
    return out
ROT = proper_rotations()

def lift(R):
    # solve U s_a = (sum_b R_ba s_b) U
    rows = []
    for a in range(3):
        T = sum(R[b, a] * S[b] for b in range(3))
        # vec(U s_a - T U) = (s_a^T kron I - I kron T) vec(U)  (column-major vec)
        rows.append(np.kron(S[a].T, I2) - np.kron(I2, T))
    A = np.vstack(rows)
    _, sv, vh = np.linalg.svd(A)
    U = vh[-1].conj().reshape(2, 2, order='F')
    U = U / np.sqrt(np.linalg.det(U))
    assert sv[-1] < 1e-12 and sv[-2] > 1e-6
    for a in range(3):
        assert np.allclose(U @ S[a] @ U.conj().T, sum(R[b, a] * S[b] for b in range(3)))
    return U
LIFT = [lift(R) for R in ROT]

# (1) covariant bond matrices: real parameters p (8) -> u = sum p_k B_k
BASIS = [I2, 1j * I2, sx, 1j * sx, sy, 1j * sy, sz, 1j * sz]
def covariant_space(d):
    d = np.array(d)
    rows = []
    for R, U in zip(ROT, LIFT):
        Rd = R @ d
        if np.array_equal(Rd, d):
            dag = False
        elif np.array_equal(Rd, -d):
            dag = True
        else:
            continue
        # constraint: U u U^dag - (u or u^dag) = 0, linear in real params
        cols = []
        for B in BASIS:
            img = U @ B @ U.conj().T - (B.conj().T if dag else B)
            cols.append(np.concatenate([img.real.ravel(), img.imag.ravel()]))
        rows.append(np.array(cols).T)
    A = np.vstack(rows)
    _, sv, vh = np.linalg.svd(A)
    null = vh[np.sum(sv > 1e-10):]
    return [sum(c * B for c, B in zip(v, BASIS)) for v in null]
for name, d in [("NN e_x", (1, 0, 0)), ("face diagonal (1,1,0)", (1, 1, 0)), ("axis-2 (2,0,0)", (2, 0, 0)), ("body diagonal (1,1,1)", (1, 1, 1))]:
    sol = covariant_space(d)
    desc = []
    for u in sol:
        coeff = [np.trace(u) / 2] + [np.trace(s @ u) / 2 for s in S]
        desc.append("[" + ", ".join("%.3f%+.3fi" % (c.real, c.imag) for c in coeff) + "]")
    print("(1) covariant u_d for %-24s dim %d; (1, sx, sy, sz) coefficients: %s" % (name, len(sol), "; ".join(desc)))

# (2) Bloch covariance
NN = [np.array(v) for v in [(1,0,0),(0,1,0),(0,0,1)]]
FD = [np.array(v) for v in [(1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1)]]
def h(k, lam=1.0, lamp=0.3):
    H = np.zeros((2, 2), dtype=complex)
    for d in NN + FD:
        dh = d / np.linalg.norm(d)
        c = lam if np.abs(d).sum() == 1 else lamp
        u = 1j * c * sum(dh[a] * S[a] for a in range(3))
        H += u * np.exp(1j * k @ d) + u.conj().T * np.exp(-1j * k @ d)
    return H
dev = 0.0
for _ in range(200):
    k = rng.uniform(-np.pi, np.pi, 3)
    for R, U in zip(ROT, LIFT):
        dev = max(dev, np.abs(U @ h(k) @ U.conj().T - h(R @ k)).max())
print("(2) Bloch covariance over 24 turns x 200 k: max deviation %.1e" % dev)

# (3) eta^+ on two sites, Jordan-Wigner on modes (x up, x dn, y up, y dn)
def jw_ops(n):
    a = np.array([[0, 1], [0, 0]], dtype=complex)
    ops = []
    for j in range(n):
        m = np.array([[1.0 + 0j]])
        for i in range(n):
            m = np.kron(m, sz if i < j else (a if i == j else I2))
        ops.append(m)
    return ops
c = jw_ops(4)
cd = [o.conj().T for o in c]
def bond(M):
    H = np.zeros((16, 16), dtype=complex)
    for al in range(2):
        for be in range(2):
            H += M[al, be] * cd[al] @ c[2 + be]
    return H + H.conj().T
for sxs, sys_, lab in [(1, -1, "opposite sublattices"), (1, 1, "same sublattice")]:
    eta = sxs * cd[0] @ cd[1] + sys_ * cd[2] @ cd[3]
    res = []
    for nm, M in [("t", I2), ("i sx", 1j * sx), ("i sy", 1j * sy), ("i sz", 1j * sz)]:
        Hb = bond(M)
        res.append("%s: %.2e" % (nm, np.abs(eta @ Hb - Hb @ eta).max()))
    print("(3) |[eta+, bond]| %-21s " % lab + ", ".join(res))
Ntot = sum(cd[i] @ c[i] for i in range(4))
print("    |[N, bond(i sx)]| = %.1e" % np.abs(Ntot @ bond(1j * sx) - bond(1j * sx) @ Ntot).max())

# (4) nodes and speeds
nodes = [np.array(n) * np.pi for n in itertools.product([0, 1], repeat=3)]
dirs = rng.normal(size=(300, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
q = 1e-5
for lamp in [0.0, 0.3]:
    out = []
    for n in nodes:
        e0 = np.abs(np.linalg.eigvalsh(h(n, 1.0, lamp))).max()
        sp = [np.linalg.eigvalsh(h(n + q * u, 1.0, lamp))[1] / q for u in dirs]
        out.append("%s |E|=%.0e v=[%.3f,%.3f]" % ("".join(str(int(round(x / np.pi))) for x in n), e0, min(sp), max(sp)))
    print("(4) lambda'=%.1f nodes: " % lamp + "; ".join(out))
# zero scan
g = np.linspace(-np.pi, np.pi, 41)[:-1]
mins = []
for k in itertools.product(g, repeat=3):
    k = np.array(k)
    dist = min(np.linalg.norm(((k - n + np.pi) % (2 * np.pi)) - np.pi) for n in nodes)
    if dist > 0.3:
        mins.append(np.abs(np.linalg.eigvalsh(h(k))).min())
print("    lambda'=0.3: min |E| over a 40^3 grid, farther than 0.3 from every node: %.3f" % min(mins))
print("done")
