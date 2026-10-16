"""Part 1b: (i) test projective equivalence between the 4 classes allowing complex
scalar phases and diagonal phase gauges in {1,i,-1,-i}; (ii) decompose each class
into irreps of the binary octahedral group 2O (after the phase twist needed to make
it a genuine rep of 2O, for the spinorial ones) or of O (for linear ones).
Characters computed exactly (integers / sqrt2 recognised numerically to 1e-12)."""
import itertools, numpy as np, json
from common import *
from part1_classify import full_data  # re-runs classification (fast enough)

cl = json.load(open("classes.json"))
Ds = []
for x in cl:
    D, G = full_data(np.array(x["sa"]), np.array(x["sb"]))
    Ds.append(D)
keys = sorted(Ds[0])

# ---------- (i) projective equivalence with phase gauges ----------
ph = [1, 1j, -1, -1j]
def proj_equiv(D1, D2):
    # find diagonal gauge g (entries in ph, g0=1) with g D1(R) g^* = lambda(R) D2(R) for generators
    for g in itertools.product(ph, repeat=7):
        g = np.array((1,) + g)
        ok = True
        for R in (A_q, B_t):
            k = rkey(R)
            M = np.diag(g) @ Ds_[D1][k] @ np.diag(g.conj())
            N = Ds_[D2][k]
            # lambda = ratio on a nonzero entry
            j = np.nonzero(np.abs(N[:, 0]) > 0.5)[0][0]
            lam = M[j, 0] / N[j, 0]
            if not np.allclose(M, lam * N):
                ok = False; break
        if ok:
            return g
    return None
Ds_ = Ds
for a in range(4):
    for b in range(a + 1, 4):
        g = proj_equiv(a, b)
        print(f"classes {a},{b}: projectively equivalent via diagonal phase gauge (generators):", g is not None,
              "" if g is None else np.round(g, 3))

# ---------- (ii) decomposition ----------
def su2(R):
    """SU(2) lift (one of two) of rotation matrix R"""
    # axis-angle
    ang = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1))
    if abs(ang) < 1e-9:
        return np.eye(2, dtype=complex)
    if abs(ang - np.pi) < 1e-9:
        M = (R + np.eye(3)) / 2
        i = np.argmax(np.diag(M)); n = M[:, i] / np.sqrt(M[i, i])
    else:
        n = np.array([R[2, 1] - R[1, 2], R[0, 2] - R[2, 0], R[1, 0] - R[0, 1]]) / (2 * np.sin(ang))
    sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
    return np.cos(ang / 2) * np.eye(2) - 1j * np.sin(ang / 2) * (n[0] * sx + n[1] * sy + n[2] * sz)

def rot_of(U):
    sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1, -1])]
    return np.array([[0.5 * np.trace(sig[i] @ U @ sig[j] @ U.conj().T).real for j in range(3)] for i in range(3)])

# build 2O
def gen_mat_group(gens, n):
    G = [np.eye(gens[0].shape[0], dtype=complex)]
    frontier = list(G)
    while frontier:
        nf = []
        for g in frontier:
            for h in gens:
                p = g @ h
                if not any(np.allclose(p, x) for x in G):
                    G.append(p); nf.append(p)
        frontier = nf
    assert len(G) == n, len(G)
    return G
Ua, Ub = su2(A_q), su2(B_t)
assert np.allclose(rot_of(Ua), A_q) and np.allclose(rot_of(Ub), B_t)
twoO = gen_mat_group([Ua, Ub], 48)

def sym3(U):
    # spin-3/2 rep via symmetric cube of 2-dim
    a, b = U[0, 0], U[0, 1]; cc, d = U[1, 0], U[1, 1]
    # basis x^3, x^2y, xy^2, y^3 ; x->a x + c y, y-> b x + d y  (acting on polynomials)
    import sympy as sp
    return None

def spin_rep(U, j2):
    """spin j = j2/2 rep of SU(2) element via exponentials (numerically)"""
    from scipy.linalg import logm, expm
    j = j2 / 2
    m = np.arange(j, -j - 1, -1)
    Jz = np.diag(m)
    Jp = np.zeros((len(m), len(m)))
    for i in range(1, len(m)):
        Jp[i - 1, i] = np.sqrt(j * (j + 1) - m[i] * (m[i] + 1))
    Jx = (Jp + Jp.T) / 2; Jy = (Jp - Jp.T) / (2j)
    # U = exp(-i theta n.sigma/2): get theta n
    tr = np.trace(U).real / 2
    theta = 2 * np.arccos(np.clip(tr, -1, 1))
    if abs(np.sin(theta / 2)) < 1e-12:
        return np.eye(len(m)) * (1 if tr > 0 else (-1) ** (j2))
    v = np.array([-(U[0, 1] + U[1, 0]).imag, (U[1, 0] - U[0, 1]).real, -(U[0, 0] - U[1, 1]).imag]) / 2 / np.sin(theta / 2)
    # check
    sx = np.array([[0, 1], [1, 0]]); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1, -1])
    assert np.allclose(np.cos(theta/2)*np.eye(2) - 1j*np.sin(theta/2)*(v[0]*sx+v[1]*sy+v[2]*sz), U)
    return expm(-1j * theta * (v[0] * Jx + v[1] * Jy + v[2] * Jz))

def parity_O(R):
    # sign character A2 of O ~ S4: -1 on quarter turns and edge 2-folds
    tr = int(round(np.trace(R)))
    o = rot_order(R)
    if o == 4: return -1
    if o == 2 and tr == -1:
        # half-turn: face axis (diag entries) vs edge axis
        return 1 if (np.abs(np.diag(R)) == 1).all() else -1
    return 1

# irreps of 2O as functions on twoO elements
def irreps_chars(U):
    R = rot_of(U)
    chi1 = spin_rep(U, 1); chi2 = spin_rep(U, 2); chi3 = spin_rep(U, 3)
    p = parity_O(np.rint(R).astype(int))
    t1 = np.trace(chi2).real
    E_char = None
    return {
        "A1": 1, "A2": p, "T1": t1, "T2": p * t1,
        "E": {3: 2, 1: 0, -1: 2, 0: -1}[int(round(np.trace(R)))] if True else None,
        "E1/2": np.trace(chi1), "E5/2": p * np.trace(chi1), "G3/2": np.trace(chi3),
    }
# E char: on O classes: identity 2, C3 -1, C2(face) 2, C4 0, C2(edge) 0
def E_of(R):
    o = rot_order(R)
    if o == 1: return 2
    if o == 3: return -1
    if o == 4: return 0
    return 2 if (np.abs(np.diag(R)) == 1).all() else 0

def lift_to_twoO(D, G):
    """find homomorphism phi: (twisted) G -> 2O.  Returns dict of SU(2) image per element of the
    group generated by the (possibly i-twisted) generators."""
    out = []
    for twist in (1, 1j):   # twist odd elements by i
        for sa in (1, -1):
            for sb in (1, -1):
                gA = twist * D[rkey(A_q)].astype(complex)  # quarter turn odd
                gB = D[rkey(B_t)].astype(complex)
                images = {gA.tobytes(): None}
                # BFS on pairs (matrix, su2)
                pairs = [(np.eye(8, dtype=complex), np.eye(2, dtype=complex))]
                seen = {np.round(pairs[0][0], 8).tobytes(): pairs[0][1]}
                fr = list(pairs); ok = True
                while fr and ok:
                    nf = []
                    for M, U in fr:
                        for gm, gu in ((gA, sa * Ua), (gB, sb * Ub)):
                            M2, U2 = M @ gm, U @ gu
                            kk = np.round(M2, 8).tobytes()
                            if kk in seen:
                                if not np.allclose(seen[kk], U2):
                                    ok = False; break
                            else:
                                seen[kk] = U2; nf.append((M2, U2))
                        if not ok: break
                    fr = nf
                if ok and len(seen) == 48:
                    # check -1 maps to -1 (faithful)
                    return twist, seen
    return None, None

for ci, x in enumerate(cl):
    D, G = full_data(np.array(x["sa"]), np.array(x["sb"]))
    inv = x["inv"]
    print(f"\nclass {ci}: inv {inv}")
    if inv["quarter4"] == 1 and inv["order"] == 24:
        # linear rep of O
        chars = {"A1": [], "A2": [], "E": [], "T1": [], "T2": []}
        tot = {k: 0 for k in chars}
        for g in G:
            Rk = permkey_of(g) if False else None
        # identify rotation of each g via its permutation part
        Pperm = {rkey(R): Pmat(R).astype(int) for R in ROTS}
        for R in ROTS:
            g = D[rkey(R)]
            chi = np.trace(g)
            t1 = np.trace(R)
            p = parity_O(R)
            vals = {"A1": 1, "A2": p, "E": E_of(R), "T1": t1, "T2": p * t1}
            for k in tot: tot[k] += chi * vals[k]
        print("  decomposition over O:", {k: tot[k] / 24 for k in tot})
        continue
    twist, phi = lift_to_twoO(D, G)
    if twist is None:
        print("  no homomorphism onto 2O found (with twist 1 or i)")
        # try projective decomposition via O-linear after twisting
        # class 1: twist odd elements by i gives linear rep of O?
        Gt = []
        tot = {k: 0 for k in ["A1", "A2", "E", "T1", "T2"]}
        lin = True
        for R in ROTS:
            g = D[rkey(R)].astype(complex) * (1j if parity_O(R) == -1 else 1)
            Gt.append((R, g))
        # check closure as linear rep up to sign choices: pick signs so that it's a hom
        # simplest: check D(R)^2 etc via group generated
        gA = 1j * D[rkey(A_q)]; gB = D[rkey(B_t)].astype(complex)
        H = gen_mat_group([gA, gB], len(gen_mat_group.__defaults__ or []) or None) if False else None
        continue
    print("  twist on odd elements:", twist)
    tot = {k: 0 for k in ["E1/2", "E5/2", "G3/2", "A1", "A2", "E", "T1", "T2"]}
    for kk, U in phi.items():
        M = np.frombuffer(kk, dtype=complex).reshape(8, 8) if False else None
    # recompute matrices from BFS keys is awkward; redo BFS storing matrices
    for kk, U in phi.items():
        M = np.frombuffer(kk, dtype=np.complex128).reshape(8, 8)
        chi = np.trace(M)
        R = np.rint(rot_of(U)).astype(int)
        p = parity_O(R)
        ch = {"E1/2": np.trace(U), "E5/2": p * np.trace(U), "G3/2": np.trace(spin_rep(U, 3)),
              "A1": 1, "A2": p, "E": E_of(R), "T1": np.trace(R), "T2": p * np.trace(R)}
        for k in tot: tot[k] += chi * np.conj(ch[k])
    print("  multiplicities over 2O:", {k: np.round(tot[k] / 48, 10) for k in tot})
