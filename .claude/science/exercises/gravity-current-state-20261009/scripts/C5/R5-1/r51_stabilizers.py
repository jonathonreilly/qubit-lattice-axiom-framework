"""C5 R5-1 (1): stabilizers of finite supports S in Gamma = SO+(Q7,Z).

Q7(n) = -7 n0^2 + n1^2 + n2^2 + n3^2 on Z^4 (lattice coords).  For a finite S containing 0,
W = span(S).  Pointwise stabilizer Gamma_S = {g in Gamma : g s = s for all s in S}.
Claim (Lemma K): Gamma_S infinite  <=>  W = 0, or W spacelike of dim 1 or 2.
Here: (a) exact explicit infinite-order elements for the infinite cases;
      (b) BFS ball of Gamma (generators: three axis boosts + cubic rotations), counting
          ball elements fixing S pointwise as the ball grows (growth vs saturation);
      (c) exact enumeration for the timelike link e0 (signed permutations, 24).
"""
import itertools
import numpy as np

G7 = np.diag([-7, 1, 1, 1]).astype(object)

def emb(a, b, c, d, i, j):
    M = np.eye(4, dtype=object)
    M[i, i], M[i, j], M[j, i], M[j, j] = a, b, c, d
    return M

def inGamma(M):
    return (M.T.dot(G7).dot(M) == G7).all() and round(float(np.linalg.det(M.astype(float)))) == 1 and M[0, 0] > 0

# generators
gens = []
for j in (1, 2, 3):
    B = emb(8, 3, 21, 8, 0, j); Bi = emb(8, -3, -21, 8, 0, j)
    assert inGamma(B) and inGamma(Bi) and (B.dot(Bi) == np.eye(4, dtype=object)).all()
    gens += [B, Bi]
cub = []
for perm in itertools.permutations(range(3)):
    for signs in itertools.product([1, -1], repeat=3):
        M = np.zeros((4, 4), dtype=object); M[0, 0] = 1
        for r in range(3):
            M[1 + r, 1 + perm[r]] = signs[r]
        if inGamma(M):
            cub.append(M)
print("(c) cubic rotations in Gamma fixing e0 (exact count):", len(cub))
gens += cub

def Q(v):
    return -7 * v[0] ** 2 + v[1] ** 2 + v[2] ** 2 + v[3] ** 2

# (a) explicit infinite-order elements
e = [np.array(x, dtype=object) for x in np.eye(4, dtype=int).tolist()]
B02 = emb(8, 3, 21, 8, 0, 2); B03 = emb(8, 3, 21, 8, 0, 3)
print("(a) B02 (boost on (n0,n2)) fixes e1, e3:", (B02.dot(e[1]) == e[1]).all(), (B02.dot(e[3]) == e[3]).all(),
      "; B03 fixes e1, e2:", (B03.dot(e[1]) == e[1]).all(), (B03.dot(e[2]) == e[2]).all())
P = np.eye(4, dtype=object)
for k in range(1, 6):
    P = P.dot(B03)
print("    B03^5 entries grow (infinite order):", P[0, 0], " Q7(e1)=", Q(e[1]), " Q7(e2)=", Q(e[2]))

# BFS ball
from collections import deque
def key(M):
    return tuple(int(x) for x in M.flatten())
I = np.eye(4, dtype=object)
seen = {key(I): I}
frontier = [I]
CAP = 10 ** 7
supports = {
    "on-site {0}": [],
    "spacelike link {0,e1}": [e[1]],
    "spacelike link {0,(1,3,0,0)} Q=2": [np.array([1, 3, 0, 0], dtype=object)],
    "spacelike plane {0,e1,e2}": [e[1], e[2]],
    "spacelike 3-space {0,e1,e2,e3}": [e[1], e[2], e[3]],
    "timelike link {0,e0}": [e[0]],
    "timelike link {0,(1,1,1,0)} Q=-5": [np.array([1, 1, 1, 0], dtype=object)],
    "Lorentzian plane {0,e0,e1}": [e[0], e[1]],
    "generic 4-simplex": [np.array(v, dtype=object) for v in ([1, 1, 0, 0], [0, 1, 2, 0], [1, 0, 1, 3])],
}
for name, S in supports.items():
    assert all(Q(s) != 0 for s in S)
print("(b) BFS ball of Gamma; columns = word length r, #ball, then #elements fixing S pointwise")
hdr = "    r  #ball   " + "  ".join(f"{n[:22]:>22}" for n in supports)
print(hdr)
for r in range(1, 6):
    new = []
    for M in frontier:
        for g in gens:
            N = M.dot(g)
            if max(abs(int(x)) for x in N.flatten()) > CAP:
                continue
            k = key(N)
            if k not in seen:
                seen[k] = N; new.append(N)
    frontier = new
    counts = []
    for name, S in supports.items():
        c = sum(1 for M in seen.values() if all((M.dot(s) == s).all() for s in S))
        counts.append(c)
    print(f"    {r}  {len(seen):6d}  " + "  ".join(f"{c:>22d}" for c in counts), flush=True)
    if len(seen) > 400000:
        break
