"""A33 a16: re-certify the P2-A(r2<=4) candidates that stayed mobile on L = 6, 8, 10 without a 5^3
certificate, using larger boxes (6^3, 7^3) at two alignments (corners (2,2,2) and (1,1,1)).
A certificate = the symplectic form is nonzero on the box commutant (two anticommuting Paulis on the
box, each commuting with every Z^3 generator): EXACT impurity. Also k(8), k(16).
usage: python3 a16_recert.py start end      (indices into the todo list of a13)
Appends to r4_recert.txt.
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns, role_of, shape_at
from p2lib import Elim
from p2_tests import build, rank_k, box

a, b = int(sys.argv[1]), int(sys.argv[2])
t0 = time.time()
S = Space(4)
surv = pickle.load(open("r4_stage1.pkl", "rb"))
todo = []
for line in open("r4_stage3.txt"):
    if "mobL=10" in line and "cert5=-" in line and "mob={'V': 0, 'C': 0, 'E': 0, 'F': 0}" not in line:
        todo.append(int(line.split()[0]))


def form_nonzero(sh, B):
    pos = {y: k for k, y in enumerate(B)}
    rad = S.rinf
    xs = {tuple(p + d for p, d in zip(y, dd)) for y in B for dd in itertools.product(range(-rad, rad + 1), repeat=3)}
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
    vecs = []
    for f in range(n):
        if f in R:
            continue
        v = 1 << f
        for h, row in R.items():
            if (row >> f) & 1:
                v |= 1 << h
        vecs.append(v)
    xm = sum(1 << (2 * k) for k in range(len(B)))
    zm = xm << 1
    xs_ = [(v & xm) << 1 for v in vecs]
    zs_ = [v & zm for v in vecs]
    for i in range(len(vecs)):
        for j in range(i + 1, len(vecs)):
            t = bin(xs_[i] & zs_[j]).count("1") + bin(xs_[j] & zs_[i]).count("1")
            if t & 1:
                return True, len(vecs)
    return False, len(vecs)


out = []
for n in todo[a:b]:
    s, ti = surv[n]
    sh = shapes_of(S, s)
    cert = "-"
    dims = []
    for side in (6, 7):
        for corner in ((2, 2, 2), (1, 1, 1)):
            nz, d = form_nonzero(sh, box(corner, side))
            dims.append(d)
            if nz:
                cert = f"{side}^3@{corner}"
                break
        if cert != "-":
            break
    ks = []
    for L in (8, 16):
        T, gens = build(generator_patterns(sh, L), L)
        ks.append(rank_k(T, gens)[0])
    out.append(f"{n} sol={s} cert={cert} dimsC={dims} k8={ks[0]} k16={ks[1]} k16/N={ks[1]/4096:.3f}")
    if time.time() - t0 > 48:
        out.append(f"# stopped early after #{n}")
        break
with open("r4_recert.txt", "a") as fh:
    fh.write("\n".join(out) + "\n")
print(f"recert todo[{a}:{b}]: wrote {len(out)} lines   ({time.time()-t0:.1f}s)")
