"""A33 a6: full classification pass over P2-A candidates (chunked).
usage: python3 a6_classify.py r2 start end
Per candidate (one line appended to p2a_class_r{r2}.txt):
  mob4/mob6/mob8: number of single-defect moves per role on L = 4, 6, 8 (the L=6/8 tests only if
     L=4 is mobile; immobile on any even torus larger than the generators => immobile on Z^3, EXACT);
  cert: an anticommuting pair of local logicals in a 3^3 or 4^3 box (EXACT impurity), else '-';
  CB/SB on a 4^3 box of the L=8 torus (equal => no local logical there: CHECKED purity);
  k(4), k(6), k(8).
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns, role_of, shape_at
from p2lib import Elim, pcomm, BITS2L
from p2_tests import build, rank_k, syndrome_span, mobile_moves, local_logicals, box

r2, a, b = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
t0 = time.time()
D = pickle.load(open(f"p2a_sols_r{r2}.pkl", "rb"))
S = Space(r2)
X0 = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}


def commutant_basis(sh, B):
    Bset = set(B)
    pos = {y: k for k, y in enumerate(B)}
    rad = S.rinf
    xs = {tuple(a_ + d_ for a_, d_ in zip(y, d)) for y in B for d in itertools.product(range(-rad, rad + 1), repeat=3)}
    E = Elim()
    for x in xs:
        role, axis = role_of(x)
        _, p = shape_at(sh[role], role, axis, x)
        row = 0
        for z, l in p.items():
            if z in pos:
                k = pos[z]
                bx, bz = {1: (1, 0), 2: (1, 1), 3: (0, 1)}[l]
                if bz:
                    row |= 1 << (2 * k)
                if bx:
                    row |= 1 << (2 * k + 1)
        if row:
            E.add(row)
    n = 2 * len(B)
    R = {h: v for h, (v, _) in E.rows.items()}
    hs = sorted(R, reverse=True)
    for h in hs:
        for h2 in hs:
            if h2 != h and (R[h2] >> h) & 1:
                R[h2] ^= R[h]
    out = []
    for f in range(n):
        if f in R:
            continue
        v = 1 << f
        for h, row in R.items():
            if (row >> f) & 1:
                v |= 1 << h
        p = {}
        for k, y in enumerate(B):
            x_, z_ = (v >> (2 * k)) & 1, (v >> (2 * k + 1)) & 1
            if x_ or z_:
                p[y] = BITS2L[(x_, z_)]
        out.append(p)
    return out


def certificate(sh):
    for side in (3, 4):
        pats = commutant_basis(sh, box((2, 2, 2), side))
        for i in range(len(pats)):
            for j in range(i + 1, len(pats)):
                if pcomm(pats[i], pats[j]):
                    return side
    return None


lines = []
for n in range(a, min(b, len(D["sols"]))):
    sol, is_ti = D["sols"][n]
    sh = shapes_of(S, sol)
    rec = {}
    for L in (4, 6, 8):
        T, gens = build(generator_patterns(sh, L), L)
        rec[f"k{L}"] = rank_k(T, gens)[0]
        if L == 4 or any(rec[f"mob{L-2}"].values()):
            E = syndrome_span(T, gens)
            rec[f"mob{L}"] = {r: len(mobile_moves(T, E, x0)) for r, x0 in X0.items()}
        else:
            rec[f"mob{L}"] = {r: 0 for r in X0}
        if L == 8:
            rec["CB"], rec["SB"] = local_logicals(T, gens, box((2, 2, 2), 4))
    cert = certificate(sh)
    lines.append(f"{n} ti={int(is_ti)} sol={sol} mob4={rec['mob4']} mob6={rec['mob6']} mob8={rec['mob8']} "
                 f"cert={cert if cert else '-'} CB={rec['CB']} SB={rec['SB']} k=({rec['k4']},{rec['k6']},{rec['k8']})")
with open(f"p2a_class_r{r2}.txt", "a") as fh:
    fh.write("\n".join(lines) + "\n")
print(f"r2<={r2} {a}..{min(b, len(D['sols']))-1}: done {len(lines)}   ({time.time()-t0:.1f}s)")
