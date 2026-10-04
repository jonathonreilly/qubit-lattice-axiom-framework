"""A50 t3: two non-product candidates, dense (<= 7 qubits, 128 x 128).
(a) SWAP-type: t_j = raise_out(j) on leg link j (x) SWAP(corner v, far corner v+2d_j).  Junction
    (+x,-x,+z); qubits [v, e+x, e-x, e+z, l+x, l-x, l+z].  Prediction: the hexagon holonomy acts as
    SWAP(v,e-x) SWAP(e+x,e+z) on the corner qubits: not a scalar (exchange of internal states).
(b) CZ-type, O-covariant: t_i = raise_out(i) (x) exp(i sum_{m != i} k(i,m) P_m (x) s_m sigma^{a_m}_v)
    (P_m = outward-up projector of link m; k = k_opp or k_perp)  (x)  prod over unordered link pairs
    {m,m'} not containing i of exp(i J(i;m,m') pi n_m n_m'), J by geometric class.  Qubits
    [v, six links].  All 20 junctions: scalar? theta?
"""
import signal, itertools
import numpy as np
from collections import Counter
from a50lib import *
signal.alarm(250)
rng = np.random.default_rng(5003)

def emb(n, q, m):
    return kron6([m if k == q else I2 for k in range(n)])
def swap(n, a, b):
    d = 2 ** n; M = np.zeros((d, d))
    for s in range(d):
        bits = [(s >> (n - 1 - k)) & 1 for k in range(n)]
        bits[a], bits[b] = bits[b], bits[a]
        M[int(''.join(map(str, bits)), 2), s] = 1
    return M

# (a) SWAP-type
n = 7; legs = [0, 1, 4]; endq = {0: 1, 1: 2, 4: 3}; linkq = {0: 4, 1: 5, 4: 6}
T = {j: emb(n, linkq[j], raise_out(j)) @ swap(n, 0, endq[j]) for j in legs}
i, j, k = 0, 1, 4
X1 = T[i] @ T[j].conj().T @ T[k]; X2 = T[k] @ T[j].conj().T @ T[i]
c, res = phase_fit(X1, X2)
# holonomy on the support: compare with SWAP(v,e-x) SWAP(e+x,e+z) times the link projector
Wd = T[i].conj().T @ T[j] @ T[k].conj().T @ T[i] @ T[j].conj().T @ T[k]
P = Wd.conj().T @ Wd     # support projector (link configuration)
pred = swap(n, 0, 2) @ swap(n, 1, 3) @ P
cov = 0.0
for g in GRP['O']:
    pass   # SWAP commutes with U(x)U; covariance reduces to the link factors (t0 (1))
print("(a) SWAP-type, junction (+x,-x,+z): scalar fit residual %.3f (nonzero = not scalar)" % res)
print("    holonomy = SWAP(v,e-x) SWAP(e+x,e+z) on its support: residual %.1e; support rank %d"
      % (np.linalg.norm(Wd - pred), round(np.trace(P).real)))
ev = np.linalg.eigvals(Wd); ev = ev[abs(ev) > 1e-9]
print("    holonomy eigenvalues on support: %s" % dict(Counter(np.round(ev.real, 6))))

# (b) CZ-type, O-covariant (seed leg +z, transported; classes are O-invariant so build directly)
n = 7
def P_up(m):
    return (I2 + SIGN[m] * PAUL[AXIS[m] + 1]) / 2
def hop_cz(i, k_opp, k_perp, J):
    M = emb(n, 1 + i, raise_out(i))
    H = np.zeros((2 ** n, 2 ** n), complex)
    for m in range(6):
        if m == i:
            continue
        kap = k_opp if AXIS[m] == AXIS[i] else k_perp
        H += kap * emb(n, 0, SIGN[m] * PAUL[AXIS[m] + 1]) @ emb(n, 1 + m, P_up(m))
    w, V = np.linalg.eigh(H)
    M = (V @ np.diag(np.exp(1j * w)) @ V.conj().T) @ M
    for m, mm in itertools.combinations([q for q in range(6) if q != i], 2):
        cls = ('pair-opp' if AXIS[m] == AXIS[mm] else
               ('with-opp' if i ^ 1 in (m, mm) else 'perp-perp'))
        D = np.ones(2 ** n, complex)
        for s in range(2 ** n):
            b = [(s >> (n - 1 - q)) & 1 for q in range(n)]
            # n_m = outward-up occupation: computational basis is the sigma^z basis; use projector diag in field basis
        Pm = emb(n, 1 + m, P_up(m)); Pmm = emb(n, 1 + mm, P_up(mm))
        M = (np.eye(2 ** n) + (np.exp(1j * np.pi * J[cls]) - 1) * Pm @ Pmm) @ M
    return M
def run_cz(k_opp, k_perp, J):
    T = [hop_cz(i, k_opp, k_perp, J) for i in range(6)]
    out = {}
    for tri in TRIPLES:
        i, j, k = tri
        c, r = phase_fit(T[i] @ T[j].conj().T @ T[k], T[k] @ T[j].conj().T @ T[i])
        out[tri] = (c if r < 1e-9 else None)
    # covariance spot check under C4z, C3d
    worst = 0.0
    for g in (C4[2], C3d, C2[0]):
        Ug = kron6([U[g]] * n)
        # place permutation: links permuted by PERM[g]; v fixed
        perm = [0] + [1 + PERM[g][m] for m in range(6)]
        Pm = np.zeros((2 ** n, 2 ** n))
        for s in range(2 ** n):
            b = [(s >> (n - 1 - q)) & 1 for q in range(n)]
            b2 = [0] * n
            for q in range(n):
                b2[perm[q]] = b[q]
            Pm[int(''.join(map(str, b2)), 2), s] = 1
        G_ = Pm @ Ug
        for i in range(6):
            c, r = phase_fit(G_ @ T[i] @ G_.conj().T, T[PERM[g][i]])
            worst = max(worst, r)
    return out, worst
summ = Counter(); covw = 0.0
cases = [(np.pi / 2, np.pi / 2, {'pair-opp': 1, 'with-opp': 1, 'perp-perp': 1}),
         (np.pi / 2, 0.0, {'pair-opp': 0, 'with-opp': 0, 'perp-perp': 1})]
cases += [(rng.uniform(0, np.pi), rng.uniform(0, np.pi), {c_: rng.integers(2) for c_ in ['pair-opp', 'with-opp', 'perp-perp']}) for _ in range(6)]
cases += [(np.pi * rng.integers(4) / 2, np.pi * rng.integers(4) / 2, {c_: rng.integers(2) for c_ in ['pair-opp', 'with-opp', 'perp-perp']}) for _ in range(10)]
for (ko, kp, J) in cases:
    out, w = run_cz(ko, kp, J); covw = max(covw, w)
    tv = Counter('ns' if out[t] is None else complex(np.round(out[t], 6)) for t in T_TRI)
    cv = Counter('ns' if out[t] is None else complex(np.round(out[t], 6)) for t in C_TRI)
    summ[(str(dict(tv)), str(dict(cv)))] += 1
print("(b) CZ-type O-covariant, %d parameter sets; covariance residual (C4z, C3, C2x) %.1e" % (len(cases), covw))
for kk, v in summ.items():
    print("    %2d x  T-junctions %s | corners %s" % (v, kk[0], kk[1]))
print("done")

# (b') pin down every T = -1 case: parameters, full 24-turn covariance, corner residuals
print("(b') T-junction -1 cases:")
for (ko, kp, J) in cases:
    out, w = run_cz(ko, kp, J)
    if all(out[t] is not None and abs(out[t] + 1) < 1e-9 for t in T_TRI):
        T = [hop_cz(i, ko, kp, J) for i in range(6)]
        worst = 0.0
        for g in GRP['O']:
            Ug = kron6([U[g]] * n); perm = [0] + [1 + PERM[g][m] for m in range(6)]
            Pm = np.zeros((2 ** n, 2 ** n))
            for s in range(2 ** n):
                b = [(s >> (n - 1 - q)) & 1 for q in range(n)]; b2 = [0] * n
                for q in range(n):
                    b2[perm[q]] = b[q]
                Pm[int(''.join(map(str, b2)), 2), s] = 1
            G_ = Pm @ Ug
            for i in range(6):
                worst = max(worst, phase_fit(G_ @ T[i] @ G_.conj().T, T[PERM[g][i]])[1])
        cres = [phase_fit(T[a] @ T[b].conj().T @ T[c], T[c] @ T[b].conj().T @ T[a])[1] for (a, b, c) in C_TRI]
        tres = [phase_fit(T[a] @ T[b].conj().T @ T[c], T[c] @ T[b].conj().T @ T[a])[1] for (a, b, c) in T_TRI]
        print("    k_opp/pi %.4f, k_perp/pi %.4f, J %s: 24-turn covariance %.1e; T residual max %.1e; "
              "corner residuals min %.3f max %.3f" % (ko / np.pi, kp / np.pi, J, worst, max(tres), min(cres), max(cres)))
