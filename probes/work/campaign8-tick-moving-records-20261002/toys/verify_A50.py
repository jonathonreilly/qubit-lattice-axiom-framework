"""Coordinator check of A50, written from scratch (no a50lib).
(a) Lemma F'' step 2: a corner factor covariant under the leg's 90-degree turn is a rotation about the leg,
    u_d = exp(-i phi s.d/2); the T-junction word u1 u2^+ u3 u1^+ u2 u3^+ is scalar only for phi = 0 mod pi, with +1.
(b) SWAP-type composite: the 4-site permutation word is two disjoint swaps (eigenvalues +1 x10, -1 x6), not a scalar.
(c) CZ-type composite (corner qubit + 6 links): hop_i = raise_out(i) x [i s_o sigma^{a}_v controlled by the opposite
    link being outward-up] x CZ(pi) on perpendicular non-opposite link pairs.  Check 24-turn covariance, all 12
    T-junctions = -1, the 8 corner junctions non-scalar; control: bare hops give +1 on all 20."""
import itertools
import numpy as np
from scipy.linalg import expm

I2 = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
S = [sx, sy, sz]
O = [np.array(M) for M in {tuple(map(tuple, s[:, None] * np.eye(3, dtype=int)[list(p)]))
     for p in itertools.permutations(range(3)) for s in map(np.array, itertools.product((1, -1), repeat=3))}
     if round(np.linalg.det(np.array(M))) == 1]
def lift(R):                                      # SU(2) element with U sigma.v U^+ = sigma.(R v)
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if ang < 1e-9: return np.eye(2, dtype=complex)
    if abs(ang - np.pi) < 1e-9:
        w, v = np.linalg.eigh((R + np.eye(3)) / 2); n = v[:, np.argmax(w)]
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    U = expm(-1j * ang / 2 * sum(n[k] * S[k] for k in range(3)))
    for k in range(3):                            # sanity: rotates sigma as R
        assert np.allclose(U @ S[k] @ U.conj().T, sum(R[l, k] * S[l] for l in range(3)))
    return U
LEGS = [(a, s) for a in range(3) for s in (1, -1)]          # 0:+x 1:-x 2:+y 3:-y 4:+z 5:-z
vec = lambda m: LEGS[m][1] * np.eye(3)[LEGS[m][0]]
def gleg(R, m):
    w = R @ vec(m); return [k for k in range(6) if np.allclose(vec(k), w)][0]
opp = lambda m: m ^ 1
T_TRI = [(i, opp(i), k) for i in (0, 2, 4) for k in range(6) if LEGS[k][0] != LEGS[i][0]]
C_TRI = [(i, j, k) for i in (0, 1) for j in (2, 3) for k in (4, 5)]
assert len(T_TRI) == 12 and len(C_TRI) == 8
def phase_fit(X1, X2):
    c = np.vdot(X2, X1) / np.vdot(X2, X2)
    return c, np.linalg.norm(X1 - c * X2) / np.linalg.norm(X1)
ok = True

# (a) corner step of lemma F''
scal = []
for phi in np.linspace(0, 2 * np.pi, 73):
    u = {}
    for m in range(6):
        a, s = LEGS[m]
        u[m] = expm(-1j * phi / 2 * s * S[a])           # rotation about the leg direction by phi
    for g in O:                                        # covariance of the seed family under the 24 turns
        Ug = lift(g)
        for m in range(6):
            c, r = phase_fit(Ug @ u[m] @ Ug.conj().T, u[gleg(g, m)])
            assert r < 1e-12
    good = True; lam = []
    for (i, j, k) in T_TRI:
        W = u[i] @ u[j].conj().T @ u[k] @ u[i].conj().T @ u[j] @ u[k].conj().T
        c, r = phase_fit(W, np.eye(2))
        good &= r < 1e-9; lam.append(c)
    if good: scal.append((round(phi / np.pi, 4), sorted(set(np.round(np.real(lam), 6)))))
ok_a = all(abs(p - round(p)) < 1e-9 and l == [1.0] for p, l in scal)
ok &= ok_a
print(f"(a) corner factor scalar only at phi/pi = {[p for p, _ in scal]}, lambda {sorted({x for _, l in scal for x in l})} {'OK' if ok_a else 'FAIL'}")

# (b) SWAP word on 4 qubits (corner 0, far corners 1, 2, 3)
def swap(n, a, b):
    M = np.zeros((2**n, 2**n))
    for st in range(2**n):
        bits = [(st >> (n - 1 - q)) & 1 for q in range(n)]; bits[a], bits[b] = bits[b], bits[a]
        M[int(''.join(map(str, bits)), 2), st] = 1
    return M
A, B, C = swap(4, 0, 1), swap(4, 0, 2), swap(4, 0, 3)
W = A @ B @ C @ A @ B @ C
ev = np.round(np.linalg.eigvals(W).real, 9)
ok_b = (ev == 1).sum() == 10 and (ev == -1).sum() == 6
ok &= ok_b
print(f"(b) SWAP word eigenvalues +1 x{(ev == 1).sum()}, -1 x{(ev == -1).sum()} (not scalar) {'OK' if ok_b else 'FAIL'}")

# (c) CZ-type composite on 7 qubits: q0 = corner, q(1+m) = link of leg m
n = 7
def emb(q, M):
    out = np.array([[1.0 + 0j]])
    for k in range(n): out = np.kron(out, M if k == q else I2)
    return out
def eig_pm(a):
    w, v = np.linalg.eigh(S[a]); return v[:, 1], v[:, 0]       # +1 and -1 eigenvectors of sigma^a
def raise_out(m):
    a, s = LEGS[m]; up, dn = eig_pm(a)
    return np.outer(up, dn.conj()) if s == 1 else np.outer(dn, up.conj())
P_up = lambda m: (I2 + LEGS[m][1] * S[LEGS[m][0]]) / 2
def hop(i, k_opp, J_pp):
    M = emb(1 + i, raise_out(i))
    o = opp(i); a, s = LEGS[o]
    ctrl = emb(1 + o, P_up(o))
    M = (np.eye(2**n) - ctrl + ctrl @ emb(0, expm(1j * k_opp * s * S[a]))) @ M
    for m, mm in itertools.combinations([q for q in range(6) if q not in (i, o)], 2):
        if LEGS[m][0] != LEGS[mm][0]:                              # perpendicular, non-opposite pair
            Pm, Pmm = emb(1 + m, P_up(m)), emb(1 + mm, P_up(mm))
            M = (np.eye(2**n) + (np.exp(1j * np.pi * J_pp) - 1) * Pm @ Pmm) @ M
    return M
def perm_op(R):
    perm = [0] + [1 + gleg(R, m) for m in range(6)]
    P = np.zeros((2**n, 2**n))
    for st in range(2**n):
        b = [(st >> (n - 1 - q)) & 1 for q in range(n)]; b2 = [0] * n
        for q in range(n): b2[perm[q]] = b[q]
        P[int(''.join(map(str, b2)), 2), st] = 1
    return P
def analyse(k_opp, J_pp):
    T = [hop(i, k_opp, J_pp) for i in range(6)]
    cov = 0.0
    for R in O:
        G = perm_op(R)
        Ug = lift(R); full = np.array([[1.0 + 0j]])
        for _ in range(n): full = np.kron(full, Ug)
        G = G @ full
        for i in range(6):
            cov = max(cov, phase_fit(G @ T[i] @ G.conj().T, T[gleg(R, i)])[1])
    res = {}
    for tri in T_TRI + C_TRI:
        i, j, k = tri
        res[tri] = phase_fit(T[i] @ T[j].conj().T @ T[k], T[k] @ T[j].conj().T @ T[i])
    return cov, res
cov, res = analyse(np.pi / 2, 1)
tph = [np.round(res[t][0], 9) for t in T_TRI if res[t][1] < 1e-9]
cres = [res[t][1] for t in C_TRI]
ok_c = cov < 1e-12 and len(tph) == 12 and all(abs(x + 1) < 1e-9 for x in tph) and min(cres) > 0.5
ok &= ok_c
print(f"(c) composite: 24-turn covariance {cov:.1e}; T-junctions scalar {len(tph)}/12 all -1 {all(abs(x + 1) < 1e-9 for x in tph)}; "
      f"corner residuals {min(cres):.3f}-{max(cres):.3f} (non-scalar) {'OK' if ok_c else 'FAIL'}")
cov0, res0 = analyse(0.0, 0)
ok0 = all(r < 1e-12 and abs(c - 1) < 1e-12 for c, r in res0.values())
ok &= ok0
print(f"(c) control, bare hops: all 20 junctions +1 {ok0}, covariance {cov0:.1e}")
print("TOTAL:", "PASS" if ok else "FAIL")
