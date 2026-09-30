#!/usr/bin/env python3
"""T27 test E3: SU(3) one-rishon vertex. Local Gauss kernel by (matter n, rishons p); triality rule;
and whether nested LOCAL Casimirs (quadratic; quadratic+cubic) of partial sums of rishon fields resolve
the multiplicity space.  Conventions as the note 2026-09-04 (each rishon at v transforms with T^A; matter Fock
of 3 colour modes, Jordan-Wigner).  Not pre-registered in PREREG.md as its own test; it is the SU(3) leg of Test E
(pre-registered: 'labels resolved by local invariants'); its pass/fail reading was: kernel dim = M3(n+p) for n+p = 0 mod 3,
0 otherwise, and (for p = 6, n = 0) 5 distinct joint labels from local Casimirs."""
import itertools, json, sys
import numpy as np
import scipy.sparse as sp

OUT = {}
def log(*a): print(*a); sys.stdout.flush()
def check(name, cond, detail=""):
    OUT[name] = bool(cond); log(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))

lam = np.zeros((8, 3, 3), dtype=complex)
lam[0][0, 1] = lam[0][1, 0] = 1
lam[1][0, 1] = -1j; lam[1][1, 0] = 1j
lam[2][0, 0] = 1; lam[2][1, 1] = -1
lam[3][0, 2] = lam[3][2, 0] = 1
lam[4][0, 2] = -1j; lam[4][2, 0] = 1j
lam[5][1, 2] = lam[5][2, 1] = 1
lam[6][1, 2] = -1j; lam[6][2, 1] = 1j
lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
T = lam / 2
# symmetric d_{ABC} = 2 tr({T^A,T^B}T^C)
dabc = np.zeros((8, 8, 8))
for A in range(8):
    for B in range(8):
        for C in range(8):
            dabc[A, B, C] = np.real(2 * np.trace((T[A] @ T[B] + T[B] @ T[A]) @ T[C]))

I2 = sp.identity(2, format="csr", dtype=complex)
SZ = sp.csr_matrix(np.diag([1., -1.]).astype(complex))
SM = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=complex))
I3 = sp.identity(3, format="csr", dtype=complex)
def kron_list(ms):
    out = sp.identity(1, format="csr", dtype=complex)
    for m in ms: out = sp.kron(out, sp.csr_matrix(m), format="csr")
    return out

def build(p):
    """matter: 3 JW modes (8 dims); p rishons, each a colour triplet (3 dims)."""
    def psi(m):
        return kron_list([SZ if k < m else (SM if k == m else I2) for k in range(3)] + [I3] * p)
    ps = [psi(m) for m in range(3)]
    dim = 8 * 3 ** p
    rho = []
    for A in range(8):
        acc = sp.csr_matrix((dim, dim), dtype=complex)
        for a in range(3):
            for b in range(3):
                c = T[A][a, b]
                if abs(c) > 1e-15: acc = acc + c * (ps[a].getH() @ ps[b])
        rho.append(acc.tocsr())
    E = []
    for l in range(p):
        El = []
        for A in range(8):
            mats = [sp.identity(8, format="csr", dtype=complex)] + [sp.csr_matrix(T[A]) if k == l else I3 for k in range(p)]
            El.append(kron_list(mats))
        E.append(El)
    G = [rho[A] + sum((E[l][A] for l in range(p)), sp.csr_matrix((dim, dim), dtype=complex)) for A in range(8)]
    N = sum((ps[m].getH() @ ps[m] for m in range(3)), sp.csr_matrix((dim, dim), dtype=complex))
    return G, E, N, dim

def singlets(G, dim):
    """weight-zero vectors annihilated by the two simple raising operators E_12, E_23 (generate trivial rep)."""
    d3 = G[2].diagonal().real; d8 = G[7].diagonal().real
    zero = np.where((np.abs(d3) < 1e-12) & (np.abs(d8) < 1e-12))[0]
    # raising ops: E12 = G1 + iG2 (over 2 normalisation irrelevant), E23 = G6 + iG7
    R12 = (G[0] + 1j * G[1]).tocsc(); R23 = (G[5] + 1j * G[6]).tocsc()
    M = sp.vstack([R12[:, zero], R23[:, zero]])
    Gram = (M.getH() @ M).toarray()
    ev, U = np.linalg.eigh((Gram + Gram.conj().T) / 2)
    null = U[:, ev < 1e-9]
    Kfull = sp.csr_matrix((null.ravel(), (np.repeat(zero, null.shape[1]), np.tile(np.arange(null.shape[1]), len(zero)))), shape=(dim, null.shape[1]))
    return Kfull

M3 = {0: 1, 1: 0, 2: 0, 3: 1, 4: 0, 5: 0, 6: 5}   # singlets in 3^{(x)k} ... k = number of triplets
# matter n contributes: n=0 -> singlet, n=1 -> 3, n=2 -> 3bar, n=3 -> singlet.  So the kernel dimension is
# (n=0) M(p) + (n=3) M(p) + (n=1) M(3-x) ...: we just compute and compare with the triality rule.
def su3_sing(a, b):
    """number of singlets in 3^{(x)a} (x) 3bar^{(x)b} by brute force over characters is heavy; use the small table"""
    return None
res = {}
for p in range(0, 7):
    G, E, N, dim = build(p)
    K = singlets(G, dim)
    dK = K.shape[1]
    NK = (K.getH() @ N @ K).toarray()
    nv = np.linalg.eigvalsh((NK + NK.conj().T) / 2) if dK else np.array([])
    bym = [int(np.sum(np.abs(nv - n) < 1e-9)) for n in range(4)]
    res[p] = (dK, bym)
    tri_ok = all(bym[n] == 0 for n in range(4) if (n + p) % 3 != 0)
    log("p=%d: Gauss kernel dim %d by matter n=(0,1,2,3): %s; triality rule (n+p)=0 mod 3 %s" % (p, dK, bym, "respected" if tri_ok else "VIOLATED"))
    OUT["p%d" % p] = dict(dim=dK, by_n=bym, triality_respected=bool(tri_ok))
check("E3a the SU(3) Gauss kernel at a vertex is nonzero only when (matter triality n + rishons p) = 0 mod 3, for p = 0..6",
      all(all(res[p][1][n] == 0 for n in range(4) if (n + p) % 3 != 0) for p in range(7)))
check("E3b every allowed (n,p) has at least one singlet (triality is sufficient for existence)",
      all(res[p][1][n] > 0 for p in range(7) for n in range(4) if (n + p) % 3 == 0))

# p = 6, n = 0 : multiplicity space, resolved by nested LOCAL Casimirs?
p = 6
G, E, N, dim = build(p)
K = singlets(G, dim)
NK = (K.getH() @ N @ K).toarray()
w, V = np.linalg.eigh((NK + NK.conj().T) / 2)
K0 = (K @ sp.csr_matrix(V[:, np.abs(w) < 1e-9])).toarray()
log("p=6 n=0 multiplicity:", K0.shape[1])
def partial_ops(k):
    S = [sum((E[l][A] for l in range(k)), sp.csr_matrix((dim, dim), dtype=complex)) for A in range(8)]
    C2 = sum((S[A] @ S[A] for A in range(8)), sp.csr_matrix((dim, dim), dtype=complex))
    C3 = sp.csr_matrix((dim, dim), dtype=complex)
    for A in range(8):
        for B in range(8):
            SAB = S[A] @ S[B]
            for C in range(8):
                if abs(dabc[A, B, C]) > 1e-12:
                    C3 = C3 + dabc[A, B, C] * (SAB @ S[C])
    return C2.tocsr(), C3.tocsr()
ops2, ops3 = [], []
for k in range(2, 6):
    c2, c3 = partial_ops(k)
    ops2.append(c2); ops3.append(c3)
def labels_of(ops):
    mix = sum(np.pi ** (i + 1) * ops[i] for i in range(len(ops)))
    B = K0.conj().T @ (mix @ K0)
    B = (B + B.conj().T) / 2
    ev, U = np.linalg.eigh(B)
    Kn = K0 @ U
    labs = []
    for t in range(Kn.shape[1]):
        v = Kn[:, t]
        labs.append(tuple(round(float(np.real(v.conj() @ (o @ v))), 5) for o in ops))
    return labs, ev
labs_q, evq = labels_of(ops2)
n_q = len(set(labs_q))
log("   quadratic Casimirs C2(1..k), k=2..5: %d distinct joint labels among %d" % (n_q, K0.shape[1]))
labs_qc, evqc = labels_of(ops2 + ops3)
n_qc = len(set(labs_qc))
log("   quadratic + cubic: %d distinct" % n_qc)
# are these operators gauge invariant / commuting on the kernel? (partial sums scalar under total G)
gi = max(abs(o @ g - g @ o).max() for o in ops2[:2] + ops3[:2] for g in G[:3])
log("   [C, G] max entry %.1e (partial-sum Casimirs are invariant under the total gauge rotation)" % gi)
check("E3c the 5-dim SU(3) intertwiner space (p=6, n=0) is resolved by local nested Casimirs: quadratic alone gives %d distinct labels, quadratic+cubic gives %d" % (n_q, n_qc), n_qc == 5 and gi < 1e-12)
OUT["su3_p6_quadratic_labels"] = n_q
OUT["su3_p6_quadratic_cubic_labels"] = n_qc
json.dump(OUT, open("t27_E3_result.json", "w"), indent=1)
