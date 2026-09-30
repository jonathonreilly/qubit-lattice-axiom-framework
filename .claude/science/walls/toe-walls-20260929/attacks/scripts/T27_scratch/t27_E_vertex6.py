#!/usr/bin/env python3
"""T27 test E2: the Z^3 star. One vertex with up to six rishon doublets (+ a 2-mode matter doublet).

Questions (pre-registered in PREREG.md, Test E):
 (1) local Gauss-kernel dimension c(p) for p = 0..6 rishons at the vertex, split by matter occupation;
 (2) at p = 6 (n = 0 or 2) is the 5-dim intertwiner space resolved by the nested pair Casimirs
     C_k = (sum_{l<=k} E_l)^2, k = 2..5  (local, gauge invariant, commuting)?
 (3) how do the 24 proper cube rotations (permuting the six links) act on that 5-dim space:
     character and decomposition into O ~ S4 irreps; is a monomial orthonormal label basis possible?
 (4) label-register size: ceil(log2 c(6)).
"""
import itertools, json, sys
import numpy as np

OUT = {}
def log(*a): print(*a); sys.stdout.flush()
def check(name, cond, detail=""):
    OUT[name] = bool(cond); log(("PASS " if cond else "FAIL ") + name + ("  | " + detail if detail else ""))

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TAU = [SX, SY, SZ]
SM = np.array([[0, 1], [0, 0]], dtype=complex)   # |0><1| annihilates |1>

def kron_all(ms):
    out = np.array([[1.0 + 0j]])
    for m in ms: out = np.kron(out, m)
    return out

def build(p):
    """Local space: qubits [m0, m1, r1..rp]. Returns G[a], N (matter number), E[l][a]."""
    nq = 2 + p
    def op_at(op, q):
        return kron_all([op if k == q else I2 for k in range(nq)])
    psi0 = kron_all([SM] + [I2] * (nq - 1))
    psi1 = kron_all([SZ, SM] + [I2] * (nq - 2))
    psi = [psi0, psi1]
    rho = []
    for a in range(3):
        acc = np.zeros((2 ** nq, 2 ** nq), dtype=complex)
        for i in range(2):
            for j in range(2):
                c = TAU[a][i, j] / 2
                if c != 0: acc += c * psi[i].conj().T @ psi[j]
        rho.append(acc)
    E = [[op_at(TAU[a] / 2, 2 + l) for a in range(3)] for l in range(p)]
    G = [rho[a] + sum((E[l][a] for l in range(p)), np.zeros_like(rho[a])) for a in range(3)]
    N = psi0.conj().T @ psi0 + psi1.conj().T @ psi1
    return G, N, E, nq

def kernel(Gs):
    A = sum(g.conj().T @ g for g in Gs)
    A = (A + A.conj().T) / 2
    ev, U = np.linalg.eigh(A)
    return U[:, ev < 1e-9]

Mnum = {0: 1, 1: 0, 2: 1, 3: 0, 4: 2, 5: 0, 6: 5, 7: 0}
cvals = []
for p in range(7):
    G, N, E, nq = build(p)
    Kp = kernel(G)
    dims = {}
    NKp = Kp.conj().T @ N @ Kp
    nvec = np.linalg.eigvalsh((NKp + NKp.conj().T) / 2) if Kp.shape[1] else np.array([])
    for n in (0, 1, 2):
        dims[n] = int(np.sum(np.abs(nvec - n) < 1e-9))
    tot = Kp.shape[1]
    pred = {0: Mnum[p], 1: Mnum[p + 1], 2: Mnum[p]}
    cvals.append(tot)
    check("E2.%d p=%d rishons at the vertex: Gauss kernel dim %d = 2M(p)+M(p+1) = %d, by matter n=(0,1,2): %s" % (p, p, tot, 2 * Mnum[p] + Mnum[p + 1], [dims[0], dims[1], dims[2]]),
          tot == 2 * Mnum[p] + Mnum[p + 1] and dims == pred)
log("   c(p) =", cvals)
check("E2.bits register size for the p=6 vertex: ceil(log2 c(6)) = %d qubits" % int(np.ceil(np.log2(cvals[6]))), cvals[6] == 10 and int(np.ceil(np.log2(cvals[6]))) == 4)

# ---------- p = 6 : nested pair Casimirs
p = 6
G, N, E, nq = build(p)
Kp = kernel(G)
# restrict to n = 0
nvec = np.real(np.diag(Kp.conj().T @ N @ Kp))
# make N diagonal within K: diagonalize N restricted
NK = Kp.conj().T @ N @ Kp
w, V = np.linalg.eigh((NK + NK.conj().T) / 2)
K0 = Kp @ V[:, np.abs(w) < 1e-9]
K2 = Kp @ V[:, np.abs(w - 2) < 1e-9]
def Csub(k):
    tot = np.zeros_like(G[0])
    for a in range(3):
        S = sum((E[l][a] for l in range(k)), np.zeros_like(G[0]))
        tot += S @ S
    return tot
Cs = [Csub(k) for k in range(2, 6)]
# commute with G and with each other
comm_G = max(np.abs(C @ g - g @ C).max() for C in Cs for g in G)
comm_C = max(np.abs(Cs[i] @ Cs[j] - Cs[j] @ Cs[i]).max() for i in range(4) for j in range(4))
check("E2.c nested pair Casimirs C_2..C_5 are gauge invariant (max [C,G] = %.1e) and mutually commuting (%.1e)" % (comm_G, comm_C), comm_G < 1e-12 and comm_C < 1e-12)
# joint spectrum on K0
def joint(K):
    M = sum((i + 1) * 0 for i in range(1))
    # generic combination to split the joint eigenspaces
    mix = sum(np.pi ** (i + 1) * Cs[i] for i in range(4))
    B = K.conj().T @ mix @ K
    B = (B + B.conj().T) / 2
    ev, U = np.linalg.eigh(B)
    Kn = K @ U
    labs = []
    for t in range(Kn.shape[1]):
        v = Kn[:, t]
        labs.append(tuple(round(float(np.real(v.conj() @ (C @ v))), 6) for C in Cs))
    return Kn, labs
Kn0, labs0 = joint(K0)
Kn2, labs2 = joint(K2)
check("E2.d the 5-dim intertwiner space (n=0) is resolved by (C_2,C_3,C_4,C_5): %d distinct joint labels" % len(set(labs0)), K0.shape[1] == 5 and len(set(labs0)) == 5)
check("E2.e same for n=2", K2.shape[1] == 5 and len(set(labs2)) == 5)
log("   joint labels (C_2,C_3,C_4,C_5) for n=0:", sorted(set(labs0)))

# ---------- cube rotation group acting on the six links
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
Rz = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
Rx = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
group = {tuple(np.eye(3, dtype=int).ravel())}
frontier = [np.eye(3, dtype=int)]
while frontier:
    g = frontier.pop()
    for gen in (Rz, Rx):
        h = gen @ g
        t = tuple(h.ravel())
        if t not in group:
            group.add(t); frontier.append(h)
group = [np.array(g).reshape(3, 3) for g in group]
check("E2.f the proper cube rotation group has 24 elements", len(group) == 24)
def perm_of(g):
    return [dirs.index(tuple(int(x) for x in g @ np.array(d))) for d in dirs]
def perm_operator(perm, nq, p):
    """Unitary on qubits [m0,m1,r_0..r_{p-1}] moving rishon l to position perm[l]."""
    dim = 2 ** nq
    P = np.zeros((dim, dim), dtype=complex)
    for idx_ in range(dim):
        bits = [(idx_ >> (nq - 1 - k)) & 1 for k in range(nq)]
        newb = list(bits)
        for l in range(p):
            newb[2 + perm[l]] = bits[2 + l]
        j = 0
        for k in range(nq): j = (j << 1) | newb[k]
        P[j, idx_] = 1.0
    return P
# class labels of O by (trace, angle)
def classof(g):
    tr = int(np.trace(g))
    if tr == 3: return 'E'
    if tr == 0: return 'C3'
    if tr == -1: return 'C2'      # half-turn about a face axis (square of C4)
    # tr == 1: quarter turn (C4) or edge-axis half turn (C2')
    # C4 has g^2 != 1... half turn about an edge axis has g^2 == 1
    return 'C2p' if np.array_equal(g @ g, np.eye(3, dtype=int)) else 'C4'
# recheck the class of trace -1: C2 (about face axis) has trace -1; C2' (about edge axis) also has trace -1
def classof2(g):
    tr = int(np.trace(g))
    if tr == 3: return 'E'
    if tr == 0: return 'C3'
    if tr == 1: return 'C4'
    # tr == -1: half-turn; face axis has rotation axis along a coordinate direction
    ev, evec = np.linalg.eig(g.astype(float))
    ax = np.real(evec[:, np.argmin(np.abs(ev - 1))])
    return 'C2' if np.sum(np.abs(ax) > 1e-9) == 1 else 'C2p'
classes = {}
for g in group: classes.setdefault(classof2(g), []).append(g)
check("E2.g class sizes are 1,8,3,6,6 (E,C3,C2,C4,C2')", sorted(len(v) for v in classes.values()) == [1, 3, 6, 6, 8], str({k: len(v) for k, v in classes.items()}))
chars = {}
for cl, gl in classes.items():
    g = gl[0]
    P = perm_operator(perm_of(g), nq, p)
    # P must commute with G (it only permutes rishon qubits) and map K0 into K0
    cg = max(np.abs(P @ gg - gg @ P).max() for gg in G)
    inK = np.abs(K0 @ (K0.conj().T @ (P @ K0)) - P @ K0).max()
    chars[cl] = np.real(np.trace(K0.conj().T @ P @ K0))
    assert cg < 1e-12 and inK < 1e-9, (cl, cg, inK)
log("   characters of the 5-dim intertwiner space:", {k: round(float(v), 6) for k, v in chars.items()})
table = {   # order: E, C3, C2, C4, C2'
    'A1': dict(E=1, C3=1, C2=1, C4=1, C2p=1),
    'A2': dict(E=1, C3=1, C2=1, C4=-1, C2p=-1),
    'E': dict(E=2, C3=-1, C2=2, C4=0, C2p=0),
    'T1': dict(E=3, C3=0, C2=-1, C4=1, C2p=-1),
    'T2': dict(E=3, C3=0, C2=-1, C4=-1, C2p=1),
}
sizes = {k: len(v) for k, v in classes.items()}
mult = {}
for name, row in table.items():
    m = sum(sizes[c] * chars[c] * row[c] for c in sizes) / 24.0
    mult[name] = round(float(m), 6)
log("   decomposition into O irreps:", mult)
check("E2.h the 5-dim intertwiner space decomposes into O irreps with integer multiplicities summing to dimension 5",
      all(abs(m - round(m)) < 1e-9 for m in mult.values()) and abs(sum(mult[n] * table[n]['E'] for n in mult) - 5) < 1e-9)
check("E2.i (reading) every irrep of O ~ S4 has dimension <= 3 and is monomial, so an orthonormal label basis on which the 24 rotations act by signed/phased permutations exists blockwise",
      True, "not a computation; group-theory fact (S4 is an M-group); the phases are the open point")
OUT["chars"] = {k: float(v) for k, v in chars.items()}
OUT["decomposition"] = mult
OUT["c_p"] = cvals
json.dump(OUT, open("t27_E_vertex6_result.json", "w"), indent=1)
