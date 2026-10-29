"""sp55_seam: combinatorics of the digital ball D_R, its boundary dD, and the prism-seam complex with cube-based weights
(criteria: sp55_seam_criteria.md). Exact integer arithmetic. Faces are encoded by doubled centre coordinates c in Z^4:
coordinate even = the face extends in that direction, odd = fixed at that (doubled) vertex coordinate; dim = #even."""
from fractions import Fraction as Fr
from itertools import product, permutations
from collections import Counter, defaultdict

def faces_of(C):            # C: doubled centre of a 4-cube (all even); all 81 faces
    return [tuple(C[m] + d[m] for m in range(4)) for d in product((-1, 0, 1), repeat=4)]
def dim(c): return sum(1 for t in c if t % 2 == 0)
def subfaces(c):            # all faces of the face c (including itself)
    opts = [((t - 1, t, t + 1) if t % 2 == 0 else (t,)) for t in c]
    return [tuple(p) for p in product(*opts)]

def analyse(cubes, label, verbose=True):
    """cubes: set of integer centres k (cube = k + [-1/2,1/2]^4). Returns dict of results."""
    C2 = {tuple(2*t for t in k) for k in cubes}
    cellsD = set()
    for C in C2: cellsD.update(faces_of(C))
    nD = Counter(dim(c) for c in cellsD)
    chiD = sum((-1)**k * nD[k] for k in range(5))
    # boundary 3-faces: 3-faces in exactly one cube of D
    def cubes_containing_3face(f):
        m = next(i for i in range(4) if f[i] % 2 != 0)
        a = list(f); a[m] -= 1; b = list(f); b[m] += 1
        return [t for t in (tuple(a), tuple(b)) if t in C2]
    bd3 = [f for f in cellsD if dim(f) == 3 and len(cubes_containing_3face(f)) == 1]
    cellsB = set()
    for f in bd3: cellsB.update(subfaces(f))
    nB = Counter(dim(c) for c in cellsB)
    chiB = sum((-1)**k * nB[k] for k in range(4))
    # S3: each square of dD in exactly 2 boundary 3-faces; S4: vertex links, k_e
    sq_in3 = Counter(); edge_in3 = Counter(); vert_cnt = defaultdict(lambda: [0, 0, 0])
    bd3set = set(bd3)
    for f in bd3:
        for s in subfaces(f):
            d = dim(s)
            if d == 2: sq_in3[s] += 1
            if d == 1: edge_in3[s] += 1
    for s in cellsB:
        d = dim(s)
        if d in (1, 2, 3):
            for v in subfaces(s):
                if dim(v) == 0: vert_cnt[v][d - 1] += 1
    S3 = all(sq_in3[s] == 2 for s in cellsB if dim(s) == 2)
    link_chi = Counter(e - q + t for (e, q, t) in vert_cnt.values())
    S4 = (set(link_chi) == {2}) and all(edge_in3[e] >= 3 for e in cellsB if dim(e) == 1)
    # glued complex counts: n_k(P) = 2 n_k(D) + n_{k-1}(dD)
    nP = [2*nD[k] + (nB[k-1] if k >= 1 else 0) for k in range(5)]
    chiP = sum((-1)**k * nP[k] for k in range(5))
    # weights: number of 4-cells containing each square
    m_in_D = Counter()
    for C in C2:
        for s in faces_of(C):
            if dim(s) == 2: m_in_D[s] += 1
    ke = Counter(edge_in3[e] for e in cellsB if dim(e) == 1)
    bsq = Counter(m_in_D[s] + 2 for s in cellsB if dim(s) == 2)       # total weight x4 of boundary squares
    near = Counter(m_in_D[s] for s in cellsD if dim(s) == 2 and s not in cellsB and m_in_D[s] != 4)
    positive = all(m_in_D[s] >= 1 for s in cellsD if dim(s) == 2) and min(ke) >= 1
    # S8 valence of seam vertices in P: edges of D at v + 1 crossing link
    degD = Counter()
    for c in cellsD:
        if dim(c) == 1:
            for v in subfaces(c):
                if dim(v) == 0: degD[v] += 1
    seam_vertices = [v for v in cellsB if dim(v) == 0]
    val = Counter(degD[v] + 1 for v in seam_vertices)
    out = dict(chiD=chiD, chiB=chiB, chiP=chiP, S3=S3, S4=S4, link_chi=dict(link_chi), ke=dict(ke), bsq=dict(bsq),
               near=dict(near), positive=positive, val=dict(val), ncubes=len(C2), nbd3=len(bd3),
               nseamv=len(seam_vertices))
    if verbose:
        print(f"[{label}] cubes={len(C2)} boundary3faces={len(bd3)} seam vertices={len(seam_vertices)}")
        print(f"   chi(D)={chiD} chi(dD)={chiB} chi(P)={chiP}  S3(closed pseudomanifold)={S3}  S4(vertex links chi=2, k_e>=3)={S4}")
        print(f"   vertex-link chi distribution={dict(link_chi)}")
        print(f"   k_e distribution (crossing plaquette weight = k_e/4)={dict(sorted(ke.items()))}")
        print(f"   boundary-square total weight x4 (m_D + 2) distribution={dict(sorted(bsq.items()))}")
        print(f"   non-boundary squares of D with m_D != 4 (weight m_D/4) distribution={dict(sorted(near.items()))}")
        print(f"   all plaquette weights > 0: {positive}")
        print(f"   seam-vertex valence in P (bulk = 8) distribution={dict(sorted(val.items()))}")
    return out

def ball(R2):   # R2 = R^2 as Fraction; cube centred at k inside closed ball iff sum (2|k|+1)^2 <= 4 R^2
    K = 0
    while (2*K + 1)**2 <= 4*R2: K += 1
    return {k for k in product(range(-K, K + 1), repeat=4) if sum((2*abs(t) + 1)**2 for t in k) <= 4*R2}

def H4_invariant(S):
    for perm in permutations(range(4)):
        for sg in product((1, -1), repeat=4):
            if {tuple(sg[m]*k[perm[m]] for m in range(4)) for k in S} != S: return False
    return True
def down_closed(S):
    for k in S:
        for m in range(4):
            if k[m] != 0:
                k2 = list(k); k2[m] -= (1 if k[m] > 0 else -1)
                if tuple(k2) not in S: return False
    return True

allpass = True
for Rs in ["23/10", "37/10", "9/2", "26/5", "61/10"]:
    R2 = Fr(Rs)**2
    S = ball(R2)
    # degeneracy report: any vertex exactly on |x| = R?  vertices are odd doubled coords: |x|^2 = sum v^2 / 4
    verts_on = sum(1 for C in S for d in product((-1, 1), repeat=4)
                   if Fr(sum((2*C[m] + d[m])**2 for m in range(4)), 4) == R2)
    s1 = H4_invariant(S) and down_closed(S)
    r = analyse(S, f"R={Rs}")
    ok = s1 and r["chiD"] == 1 and r["S3"] and r["chiB"] == 0 and r["S4"] and r["chiP"] == 2 and r["positive"]
    print(f"   S1(H4-invariant & down-closed)={s1}; vertices exactly on |x|=R: {verts_on}; item verdict {'PASS' if ok else 'FAIL'}")
    allpass &= ok
# controls
S = ball(Fr(37, 10)**2); S.discard((0, 0, 0, 0))
c1 = not down_closed(S); print("C1 (remove central cube -> down-closure fails):", "fired" if c1 else "DID NOT FIRE")
r2 = analyse({(0, 0, 0, 0), (1, 1, 1, 1)}, "C2 two cubes sharing a vertex", verbose=True)
c2 = not r2["S4"]; print("C2 (vertex-pinched pair fails S4):", "fired" if c2 else "DID NOT FIRE")
r3 = analyse({(0, 0, 0, 0)}, "C3 single cube", verbose=True)
c3 = (r3["chiD"] == 1 and r3["chiB"] == 0); print("C3 (single cube chi(D)=1, chi(dD)=0):", "PASS" if c3 else "FAIL")
print("S7 is bookkeeping (k_e=4 => weight 1; m_D=2 => (2+2)/4=1); it cannot fail and is not counted as evidence.")
print("VERDICT:", "PASS" if (allpass and c1 and c2 and c3) else "FAIL")
