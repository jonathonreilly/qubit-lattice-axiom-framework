"""A33 a20: exact loop (flux) phase for a mobile defect of a P2-A vacuum.
usage: python3 a20_flux.py r2 V C E F role ux,uy,uz wx,wy,wz

Movers T_u, T_w: explicit Z^3 Paulis with syndrome delta_x0 + delta_{x0+u} (a10.find_mover); the hops
at other positions are their translates (u, w are role-preserving, so the hopping law is translation-
covariant along the coarse lattice). Loop: W = T_w(x0)^+ T_u(x0+w)^+ T_w(x0+u) T_u(x0) (exact phases,
A20's P class). W commutes with every generator; it is written exactly as W = c * prod_{x in A} g_x
(F2 solve over the generators near the loop; unique when there are no local relations). The phase
picked up by a lone defect at x0 (partner far away) with vacuum signs s_role is
    Phi = c * prod_{x in A} s_{role(x)} * (-1)^{[x0 in A]}.
Reported for all 16 covariant sign choices.
"""
import signal, sys, time, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, role_of, shape_at
from p2lib import Elim, LBITS, pat_str, pauli_exact, P, translate
from a10_mover import find_mover

REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
r2 = int(sys.argv[1]); sol = dict(zip("VCEF", (int(t) for t in sys.argv[2:6]))); role = sys.argv[6]
u = tuple(int(c) for c in sys.argv[7].split(",")); w = tuple(int(c) for c in sys.argv[8].split(","))
t0 = time.time()
S = Space(r2); sh = shapes_of(S, sol)
x0 = REP[role]
add = lambda a, b: tuple(p + q for p, q in zip(a, b))
Tu, _ = find_mover(S, sh, x0, u, 2)
Tw, _ = find_mover(S, sh, x0, w, 2)
assert Tu is not None and Tw is not None, "movers not found"
print("T_u =", pat_str(Tu)); print("T_w =", pat_str(Tw))
Pu0 = pauli_exact(Tu); Pw0 = pauli_exact(Tw)
Puw = pauli_exact(translate(Tu, w)); Pwu = pauli_exact(translate(Tw, u))
# Hermitian Paulis: T^+ = T
W = Pw0 * Puw * Pwu * Pu0
print("loop W =", W)
# generators near the loop
pts = [x0, add(x0, u), add(x0, w), add(add(x0, u), w)]
lo = [min(p[i] for p in pts) - 2 * S.rinf - 2 for i in range(3)]
hi = [max(p[i] for p in pts) + 2 * S.rinf + 2 for i in range(3)]
gens = []
for x in itertools.product(*[range(lo[i], hi[i] + 1) for i in range(3)]):
    rl, ax = role_of(x)
    sg, p = shape_at(sh[rl], rl, ax, x)
    gens.append((x, rl, sg, p))
sites = sorted({y for g in gens for y in g[3]} | set(W.s))
pos = {y: k for k, y in enumerate(sites)}


def vec(pdict):
    v = 0
    for y, l in pdict.items():
        bx, bz = LBITS[l]
        v |= (bx << (2 * pos[y])) | (bz << (2 * pos[y] + 1))
    return v


E = Elim()
for i, g in enumerate(gens):
    E.add(vec(g[3]), 1 << i)
wl = {y: {(1, 0): 1, (1, 1): 2, (0, 1): 3}[b] for y, b in W.s.items()}
res, combo = E.reduce(vec(wl), 0)
assert res == 0, "loop is not a product of generators near it (local logical or impure)"
A = [gens[i] for i in range(len(gens)) if (combo >> i) & 1]
prod = P()
for x, rl, sg, p in A:
    prod = prod * pauli_exact(p, sg)
# W = c * prod  ->  c = W * prod^{-1}; prod is Hermitian with prod^2 = 1
cP = W * prod
assert not cP.s
c = [1, 1j, -1, -1j][cP.k % 4]
cnt = {r: sum(1 for g in A if g[1] == r) for r in "VCEF"}
inA = any(g[0] == x0 for g in A)
print(f"W = c * prod of {len(A)} generators, c = {c}; generators per role in A: {cnt}; defect site in A: {inA}")
for sv in itertools.product((1, -1), repeat=4):
    s = dict(zip("VCEF", sv))
    phi = c
    for r in "VCEF":
        phi *= s[r] ** cnt[r]
    phi *= (-1) ** int(inA)
    print(f"   signs {sv}: loop phase {phi}")
print(f"({time.time()-t0:.1f}s)")
