"""Checks for the nearest-neighbour theorem (perpendicular-pair step).
Sites m1, m2. T_x lives in span{1,s^a_m1} (x) span{1,s^b_m2}; T_z in span{1,s^b_m1} (x) span{1,s^a_m2}.
Enumerate ALL unital *-subalgebras of each (abelian 4-dim algebras <-> set partitions of 4 joint eigenvalues),
keep pairs that commute and have nontrivial one-site support on BOTH sites; print them.
Also: C4z-invariant Bloch directions; star operator invariance is in t1_compass.py.
"""
import itertools
import numpy as np

I = np.eye(2); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
S = {0: sx, 1: sy, 2: sz}
a, b = 0, 1   # x and y directions


def partitions(seq):
    if not seq:
        yield []
        return
    first, rest = seq[0], seq[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p


def algebra(P1, P2, part):
    """P1 on m1, P2 on m2 commuting-axis Paulis; joint eigenprojectors; block sums."""
    projs = {}
    for s1, s2 in itertools.product([1, -1], repeat=2):
        projs[(s1, s2)] = np.kron((I + s1 * P1) / 2, (I + s2 * P2) / 2)
    pts = list(projs)
    return [sum(projs[pts[i]] for i in blk) for blk in part]


def one_site_nontrivial(gens, site):
    # support on a site is nontrivial iff some generator is not of the form 1 (x) B (site 0) / A (x) 1 (site 1)
    for g in gens:
        G = g.reshape(2, 2, 2, 2)
        if site == 0:   # is g = I (x) B ?  partial trace over site 0 /2 then compare
            B = np.einsum("iaib->ab", G) / 2
            if np.linalg.norm(g - np.kron(I, B)) > 1e-12:
                return True
        else:
            A = np.einsum("aibi->ab", G) / 2
            if np.linalg.norm(g - np.kron(A, I)) > 1e-12:
                return True
    return False


parts = list(partitions([0, 1, 2, 3]))
print("number of subalgebras (set partitions of 4):", len(parts))
found = []
for px in parts:
    Tx = algebra(S[a], S[b], px)
    if not (one_site_nontrivial(Tx, 0) and one_site_nontrivial(Tx, 1)):
        continue
    for pz in parts:
        Tz = algebra(S[b], S[a], pz)
        if not (one_site_nontrivial(Tz, 0) and one_site_nontrivial(Tz, 1)):
            continue
        if all(np.linalg.norm(p @ q - q @ p) < 1e-12 for p in Tx for q in Tz):
            found.append((px, pz))
print("commuting pairs with nontrivial supports on both sites:", len(found))
pts = list(itertools.product([1, -1], repeat=2))
for px, pz in found:
    print("   T_x blocks:", [[pts[i] for i in blk] for blk in px], "  T_z blocks:", [[pts[i] for i in blk] for blk in pz])
# C4z invariant Bloch directions: R = rotation by 90 deg about z
R = np.array([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
w, v = np.linalg.eig(R)
print("C4z fixed Bloch directions (eigenvalue 1):", [np.real_if_close(v[:, i]).round(6).tolist() for i in range(3) if abs(w[i] - 1) < 1e-12])
