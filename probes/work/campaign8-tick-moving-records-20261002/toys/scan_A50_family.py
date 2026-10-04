"""Coordinator scan of A50's composite family (corner qubit + 6 links, covariant by construction).
hop_i = raise_out(i) x exp(i sum_{m != i} [ku_cls (s_m sigma^{a_m}_v) P_up(m) + kd_cls (s_m sigma^{a_m}_v) P_dn(m)])
        x prod over link pairs {m,m'} not containing i of exp(i pi J_cls n_m n_m'),  cls = geometric class w.r.t. i.
ku, kd in {0, pi/2, pi, 3pi/2} for the opposite and the perpendicular legs; J in {0,1} for pair-opp / with-opp / perp-perp.
A consistent fermion needs all 20 junction relations t_i t_j^+ t_k = theta t_k t_j^+ t_i scalar with theta = -1.
Usage: scan_A50_family.py <batch 0..3> (fixes kd_opp)."""
import sys, signal, itertools, collections
import numpy as np
signal.alarm(280)
b = int(sys.argv[1])
I2 = np.eye(2); S = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1]).astype(complex)]
LEGS = [(a, s) for a in range(3) for s in (1, -1)]
opp = lambda m: m ^ 1
n = 7
def emb(q, M):
    out = np.array([[1.0 + 0j]])
    for k in range(n): out = np.kron(out, M if k == q else I2)
    return out
def eig_pm(a):
    w, v = np.linalg.eigh(S[a]); return v[:, 1], v[:, 0]
def raise_out(m):
    a, s = LEGS[m]; up, dn = eig_pm(a)
    return np.outer(up, dn.conj()) if s == 1 else np.outer(dn, up.conj())
Pu = [emb(1 + m, (I2 + LEGS[m][1] * S[LEGS[m][0]]) / 2) for m in range(6)]
Pd = [np.eye(2**n) - Pu[m] for m in range(6)]
SV = [emb(0, LEGS[m][1] * S[LEGS[m][0]]) for m in range(6)]
RO = [emb(1 + m, raise_out(m)) for m in range(6)]
diagPu = [np.real(np.diag(Pu[m])) for m in range(6)]          # link projectors are diagonal? check below
def hop(i, ku, kd, J):
    H = np.zeros((2**n, 2**n), complex)
    for m in range(6):
        if m == i: continue
        c = 0 if m == opp(i) else 1
        H += ku[c] * SV[m] @ Pu[m] + kd[c] * SV[m] @ Pd[m]
    w, V = np.linalg.eigh(H)
    M = (V * np.exp(1j * w)) @ V.conj().T @ RO[i]
    for m, mm in itertools.combinations([q for q in range(6) if q != i], 2):
        cls = 0 if LEGS[m][0] == LEGS[mm][0] else (1 if opp(i) in (m, mm) else 2)
        if J[cls]:
            M = (np.eye(2**n) - 2 * Pu[m] @ Pu[mm]) @ M
    return M
T_TRI = [(i, opp(i), k) for i in (0, 2, 4) for k in range(6) if LEGS[k][0] != LEGS[i][0]]
C_TRI = [(i, j, k) for i in (0, 1) for j in (2, 3) for k in (4, 5)]
def fit(X1, X2):
    nn = np.vdot(X2, X2).real
    if nn < 1e-12: return None, 1.0
    c = np.vdot(X2, X1) / nn
    return c, np.linalg.norm(X1 - c * X2) / max(np.linalg.norm(X1), 1e-12)
K = [0, np.pi / 2, np.pi, 3 * np.pi / 2]
summary = collections.Counter(); hits = []
for ku_o, ku_p, kd_p in itertools.product(K, K, K):
    for J in itertools.product((0, 1), repeat=3):
        ku, kd = (ku_o, ku_p), (K[b], kd_p)
        T = [hop(i, ku, kd, J) for i in range(6)]
        Td = [t.conj().T for t in T]
        def ph(tri):
            i, j, k = tri
            c, r = fit(T[i] @ Td[j] @ T[k], T[k] @ Td[j] @ T[i])
            return 'ns' if r > 1e-9 else ('+1' if abs(c - 1) < 1e-6 else ('-1' if abs(c + 1) < 1e-6 else str(np.round(c, 4))))
        tv = [ph(t) for t in T_TRI]; cv = [ph(t) for t in C_TRI]
        key = (tuple(sorted(collections.Counter(map(str, tv)).items())), tuple(sorted(collections.Counter(map(str, cv)).items())))
        summary[key] += 1
        if all(x != 'ns' for x in tv + cv) and any(x != '+1' for x in tv + cv):
            hits.append(((ku_o, ku_p, K[b], kd_p), J, tv, cv))
print(f"batch kd_opp = {K[b] / np.pi:.1f} pi: {sum(summary.values())} settings")
for key, v in summary.most_common():
    print(f"  {v:4d} x T {dict(key[0])} | corners {dict(key[1])}")
print(f"  all-20-scalar settings with any phase != +1: {len(hits)}; all 20 = -1: {sum(all(x == '-1' for x in h[2] + h[3]) for h in hits)}")
for h in hits[:3]:
    print("   ", [round(x / np.pi, 2) for x in h[0]], h[1], "T", collections.Counter(map(str, h[2])), "C", collections.Counter(map(str, h[3])))
