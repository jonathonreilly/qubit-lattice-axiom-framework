"""A33 a8: screening pipeline for the large P2-A(r2<=4) solution set.
usage: python3 a8_r4_pipeline.py stage start end
 stage 1 (all candidates): exact label-diversity filter. If every generator touching a site acts there
   with one label l only, the one-site Pauli l commutes with all generators; covariance forbids a
   one-site stabilizer (O moves l through all labels at V/C sites; at E/F sites C4 swaps the two
   transverse labels and the perpendicular C2 flips sigma^axis), so l is a local logical: impure (EXACT).
   Writes survivors to r4_stage1.pkl.
 stage 2/3 (survivors, chunked; stage-3 file r4_stage3.txt escalates L=6 -> 8 -> 10): exact impurity certificate in a 3^3 box (anticommuting local logicals),
   then single-defect mobility on the L=6 torus (immobile there => immobile on Z^3, EXACT).
   Appends lines to r4_stage2.txt.
"""
import signal, sys, time, pickle, itertools
signal.alarm(55)
from p2a_core import Space, shapes_of, generator_patterns, role_of, shape_at, ROLES
from p2lib import combo, pcomm, Elim, BITS2L
from p2_tests import build, syndrome_span, mobile_moves, box

stage = int(sys.argv[1])
t0 = time.time()
S = Space(4)
REP = {"V": (0, 0, 0), "C": (1, 1, 1), "E": (1, 0, 0), "F": (1, 1, 0)}

if stage == 1:
    D = pickle.load(open("p2a_sols_r4.pkl", "rb"))
    sols = D["sols"]
    # label sets at each representative site from generators of each role/shape
    used = {r: sorted({s[r] for s, _ in sols}) for r in ROLES}
    labset = {}
    rad = S.rinf
    for r in ROLES:
        for c in used[r]:
            shape = combo(S.basis[r], [(c >> i) & 1 for i in range(S.dim[r])])
            for rho, y in REP.items():
                labs = set()
                for d in itertools.product(range(-rad, rad + 1), repeat=3):
                    x = tuple(a + b for a, b in zip(y, d))
                    role, axis = role_of(x)
                    if role != r:
                        continue
                    _, p = shape_at(shape, role, axis, x)
                    l = p.get(y, 0)
                    if l:
                        labs.add(l)
                labset[(r, c, rho)] = labs
    surv = []
    for s, ti in sols:
        ok = True
        for rho in REP:
            labs = set()
            for r in ROLES:
                labs |= labset[(r, s[r], rho)]
            if len(labs) < 2:
                ok = False
                break
        if ok:
            surv.append((s, ti))
    pickle.dump(surv, open("r4_stage1.pkl", "wb"))
    print(f"stage 1: {len(sols)} candidates; label-diverse at every role site: {len(surv)} "
          f"(TI among them {sum(t for _, t in surv)}); certified impure by a one-site logical: {len(sols)-len(surv)}"
          f"   ({time.time()-t0:.1f}s)")
    sys.exit()

a, b = int(sys.argv[2]), int(sys.argv[3])
surv = pickle.load(open("r4_stage1.pkl", "rb"))


def commutant_has_pair(sh, B):
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
    vecs = []
    for f in range(n):
        if f in R:
            continue
        v = 1 << f
        for h, row in R.items():
            if (row >> f) & 1:
                v |= 1 << h
        vecs.append(v)
    # symplectic product on interleaved bits (x_k at 2k, z_k at 2k+1)
    ev = int("01" * len(B), 2)   # bits at even positions... build masks explicitly
    xm = sum(1 << (2 * k) for k in range(len(B)))
    zm = xm << 1
    for i in range(len(vecs)):
        for j in range(i + 1, len(vecs)):
            u, w = vecs[i], vecs[j]
            t = bin(((u & xm) << 1) & (w & zm)).count("1") + bin(((w & xm) << 1) & (u & zm)).count("1")
            if t & 1:
                return True, len(vecs)
    return False, len(vecs)


lines = []
for n in range(a, min(b, len(surv))):
    s, ti = surv[n]
    sh = shapes_of(S, s)
    imp, dimC = commutant_has_pair(sh, box((2, 2, 2), 3))
    if imp:
        lines.append(f"{n} ti={int(ti)} sol={s} cert=3 dimC={dimC}")
        continue
    mobs = {}
    for L in (6, 8, 10):
        T, gens = build(generator_patterns(sh, L), L)
        E = syndrome_span(T, gens)
        mobs[L] = {r: len(mobile_moves(T, E, x0)) for r, x0 in REP.items()}
        if not any(mobs[L].values()):
            break
    cert5 = ""
    if 10 in mobs and any(mobs[10].values()):
        imp5, d5 = commutant_has_pair(sh, box((2, 2, 2), 5))
        cert5 = f" cert5={'IMPURE' if imp5 else '-'}"
    final = mobs[max(mobs)]
    lines.append(f"{n} ti={int(ti)} sol={s} cert=- dimC={dimC} mobL={max(mobs)} mob={final}{cert5}")
with open("r4_stage3.txt", "a") as fh:
    fh.write("\n".join(lines) + "\n")
nimp = sum(1 for l in lines if "cert=3" in l)
nmob = sum(1 for l in lines if "mob=" in l and "mob={'V': 0, 'C': 0, 'E': 0, 'F': 0}" not in l)
print(f"stage 2 [{a},{min(b, len(surv))}): {len(lines)} done; certified impure (3^3 box) {nimp}; "
      f"not certified & still mobile on L=10: {nmob}   ({time.time()-t0:.1f}s)")
