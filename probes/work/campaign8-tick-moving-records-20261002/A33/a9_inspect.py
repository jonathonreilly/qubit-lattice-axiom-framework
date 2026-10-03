"""A33 a9: inspect one P2-A solution given as role coefficients.
usage: python3 a9_inspect.py r2 V C E F [Ls=6,8,10] [boxes=3,4]
Prints the four shapes, which roles' sites each shape touches, single-defect moves per role on
each L (list when few), k(L), and impurity certificates in boxes (torus L chosen > side + 2 r_inf).
"""
import signal, sys, time, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns, role_of, shape_at
from p2lib import pat_str, Elim, BITS2L, pcomm
from p2_tests import build, rank_k, syndrome_span, mobile_moves, box

r2 = int(sys.argv[1])
sol = dict(zip("VCEF", (int(t) for t in sys.argv[2:6])))
Ls = [int(t) for t in sys.argv[6].split(",")] if len(sys.argv) > 6 else [6, 8, 10]
boxes = [int(t) for t in sys.argv[7].split(",")] if len(sys.argv) > 7 else [3, 4]
t0 = time.time()
S = Space(r2)
sh = shapes_of(S, sol)
REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}
print("sol", sol)
for r in "VCEF":
    x0 = REP[r]
    role, axis = role_of(x0)
    _, p = shape_at(sh[r], role, axis, x0)
    touched = sorted({role_of(y)[0] + (str(role_of(y)[1]) if role_of(y)[1] is not None else "") for y in p})
    print(f"  g_{r} at {x0}: {pat_str(p)}\n      touches roles {touched}")
for L in Ls:
    T, gens = build(generator_patterns(sh, L), L)
    k, _ = rank_k(T, gens)
    E = syndrome_span(T, gens)
    out = []
    for r, x0 in REP.items():
        mv = mobile_moves(T, E, x0)
        out.append(f"{r}:{len(mv)}" + (f" {sorted(mv)[:6]}" if 0 < len(mv) <= 6 else ""))
    print(f"  L={L}: k={k}  moves " + ", ".join(out) + f"   ({time.time()-t0:.1f}s)", flush=True)


def certificate(side):
    B = box((2, 2, 2), side)
    Bset = set(B)
    pos = {y: k for k, y in enumerate(B)}
    rad = S.rinf
    xs = {tuple(a + d for a, d in zip(y, dd)) for y in B for dd in itertools.product(range(-rad, rad + 1), repeat=3)}
    E = Elim()
    for x in xs:
        role, axis = role_of(x)
        _, p = shape_at(sh[role], role, axis, x)
        row = 0
        for z, l in p.items():
            if z in pos:
                kk = pos[z]
                bx, bz = {1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
                if bz:
                    row |= 1 << (2 * kk)
                if bx:
                    row |= 1 << (2 * kk + 1)
        if row:
            E.add(row)
    n = 2 * len(B)
    R = {h: v for h, (v, _) in E.rows.items()}
    hs = sorted(R, reverse=True)
    for h in hs:
        for h2 in hs:
            if h2 != h and (R[h2] >> h) & 1:
                R[h2] ^= R[h]
    pats = []
    for f in range(n):
        if f in R:
            continue
        v = 1 << f
        for h, row in R.items():
            if (row >> f) & 1:
                v |= 1 << h
        p = {}
        for kk, y in enumerate(B):
            a_, b_ = (v >> (2 * kk)) & 1, (v >> (2 * kk + 1)) & 1
            if a_ or b_:
                p[y] = BITS2L[(a_, b_)]
        pats.append(p)
    for i in range(len(pats)):
        for j in range(i + 1, len(pats)):
            if pcomm(pats[i], pats[j]):
                return len(pats), (pats[i], pats[j])
    return len(pats), None


for side in boxes:
    dimC, pair = certificate(side)
    print(f"  box {side}^3: dim commutant {dimC}; " + ("IMPURE: anticommuting local logicals\n     P=" + pat_str(pair[0]) + "\n     Q=" + pat_str(pair[1]) if pair else "no anticommuting pair") + f"   ({time.time()-t0:.1f}s)", flush=True)
