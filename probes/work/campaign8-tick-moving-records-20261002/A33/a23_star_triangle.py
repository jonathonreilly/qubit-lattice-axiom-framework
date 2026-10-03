"""A33 a23: elementary triangle loop of the star-vacuum planon Q (plane perpendicular to (1,1,1)):
hops u = (1,-1,0), then w = (0,1,-1), then back by -(u+w) = (-1,0,1) using the mover for u+w.
Exact loop phase for vacuum signs s = +1, -1 (reuses a22's mover and decomposition code)."""
import signal, itertools
signal.alarm(55)
import a22_star_composites as A   # runs a22's checks first (cheap), then reuse its helpers
from p2lib import pauli_exact, translate, P, Elim, LBITS
u, w = (1, -1, 0), (0, 1, -1); uw = (1, 0, -1)
Tu, Tw, Tuw = A.z3_mover(A.Q, u), A.z3_mover(A.Q, w), A.z3_mover(A.Q, uw)
assert None not in (Tu, Tw, Tuw)
# start at 0: hop by u (Tu at 0), then by w (Tw translated by u), then by -(u+w) (Tuw at 0, Hermitian)
W = pauli_exact(Tuw) * pauli_exact(translate(Tw, u)) * pauli_exact(Tu)
pts = A.Q + [A.add(p, u) for p in A.Q] + [A.add(p, uw) for p in A.Q]
lo = [min(p[i] for p in pts) - 4 for i in range(3)]; hi = [max(p[i] for p in pts) + 4 for i in range(3)]
cents = list(itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]))
sites = sorted({A.add(c, d) for c in cents for d in A.star} | set(W.s))
pos = {y: k for k, y in enumerate(sites)}
def vec(pd):
    v = 0
    for y, l in pd.items():
        bx, bz = LBITS[l]; v |= (bx << (2 * pos[y])) | (bz << (2 * pos[y] + 1))
    return v
Eg = Elim()
for i, c in enumerate(cents):
    Eg.add(vec(translate(A.star, c)), 1 << i)
wl = {y: {(1, 0): 1, (1, 1): 2, (0, 1): 3}[b] for y, b in W.s.items()}
r, cmb = Eg.reduce(vec(wl), 0)
assert r == 0
Aset = [cents[i] for i in range(len(cents)) if (cmb >> i) & 1]
prod = P()
for c in Aset:
    prod = prod * pauli_exact(translate(A.star, c))
cP = W * prod
assert not cP.s
c = [1, 1j, -1, -1j][cP.k % 4]
inside = sum(1 for x in Aset if x in set(A.Q))
for s in (1, -1):
    print(f"TRIANGLE loop: W = {c} * product of {len(Aset)} stars ({inside} at Q's own defects); vacuum sign s={s}: loop phase {c * s**len(Aset) * (-1)**inside}")
