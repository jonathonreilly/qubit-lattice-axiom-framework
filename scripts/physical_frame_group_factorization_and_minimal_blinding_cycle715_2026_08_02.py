"""Cycle 715 - the frame group factors through the zero-defect stabilizer.

Class-A finite-dimensional checks over the Cycle-696 static assembly.

Theorem I   The 24 proper rotations factor exactly as S . C4, where S is the
            order-6 set of frames that reassemble the operator unchanged and C4
            is the order-4 source stabilizer of the Cycle-707 sign law.
Theorem II  The reassembled operator itself - not merely one source's pairing -
            is a function on the 4-element right-coset space Rot / S. The count
            4 is the index 24 / 6, derived rather than measured.
Theorem III Averaging a source over a subgroup H makes its pairing frame-blind
            whenever S . H is the whole group, equivalently |H| = 4 |H meet S|.
            Hence the minimal blinding order is 4, attained exactly by the four
            complements of S - one of which is the Cycle-707 stabilizer.

Self-contained against the landed compiler chain; no new inputs.
"""
import importlib.util
import itertools
import json
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RECEIPT_NAME = ("physical_frame_group_factorization_and_minimal_blinding_cycle715"
                "_2026_08_02_receipt_2026-08-02.json")
PASS = 0
FAIL = 0
GATES = {}
NOTES = {}


def check(tag, ok, msg=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    GATES[tag] = {"detail": msg, "pass": bool(ok)}
    print("[{}] {} {}".format("PASS" if ok else "FAIL", tag, msg))


def _load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


c696 = _load("c696", "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py")
FRAMES = [np.asarray(F, dtype=np.int64) for F in c696.c576.FRAMES]
DIRS = [tuple(c696.regge.DIRS15[c][:3]) for c in c696.SPATIAL_CLASSES]
CLASS_OF = {DIRS[k]: c for k, c in enumerate(c696.SPATIAL_CLASSES)}
EYE = np.eye(3, dtype=np.int64)
RX = np.asarray([[1, 0, 0], [0, 0, -1], [0, 1, 0]], dtype=np.int64)
QUARTET_C707 = (20, 21, 22, 23)


def fidx(M):
    for a, F in enumerate(FRAMES):
        if np.array_equal(F, M):
            return a
    raise ValueError("frame outside the proper rotations")


MUL = [[fidx(FRAMES[a] @ FRAMES[b]) for b in range(24)] for a in range(24)]
IDENT = fidx(EYE)


def relabel(L, g):
    """Coframe relabelling: site map, class relabel |g v|, negative-part shift."""
    idx = c696.static_variable_index(L, False)
    smap = c696.frame_site_map(L, FRAMES[g])
    m = np.empty(len(idx), dtype=np.int64)
    for (c, x), i in idx.items():
        v = np.asarray(c696.regge.DIRS15[c][:3], dtype=np.int64)
        w = FRAMES[g] @ v
        y = tuple(int(t) for t in (np.asarray(smap[x], dtype=np.int64) + np.minimum(w, 0)))
        m[i] = idx[(CLASS_OF[tuple(int(t) for t in np.abs(w))], y)]
    return m


print("=== Theorem I: exact factorization Rot = S . C4 ===")

L0 = 3
Q0 = c696.assemble_static_hessian(L0, False)["Q"]
SCALE = float(np.abs(Q0).max())
P0 = {g: relabel(L0, g) for g in range(24)}
QG0 = {g: Q0[np.ix_(P0[g], P0[g])] for g in range(24)}

ZERO_TOL = 1.0e-09
S = [g for g in range(24) if np.abs(QG0[g] - Q0).max() < ZERO_TOL]
print("operator scale max|Q| = {:.1f} at L = {}, zero-defect tol {:.1e}".format(
    SCALE, L0, ZERO_TOL))
print("zero-defect frames S = {}".format(S))
check("I.order", len(S) == 6, "|S| = {}".format(len(S)))
check("I.id", IDENT in S, "identity frame {} is zero-defect".format(IDENT))
n_closed = sum(1 for a in S for b in S if MUL[a][b] in S)
check("I.subgroup", n_closed == 36, "S closed under composition {}/36".format(n_closed))

C4 = []
cur = EYE.copy()
for _ in range(4):
    C4.append(fidx(cur))
    cur = cur @ RX
check("I.c4powers", sorted(C4) == sorted(QUARTET_C707),
      "powers of the x-axis rotation = Cycle-707 stabilizer {}".format(sorted(C4)))
check("I.c4order", len(set(C4)) == 4 and MUL[C4[1]][C4[3]] == C4[0],
      "C4 has order 4")

inter = sorted(set(S) & set(C4))
check("I.trivial", inter == [IDENT], "S meets C4 in the identity alone {}".format(inter))

prod = sorted(MUL[s][t] for s in S for t in C4)
check("I.bijective", prod == list(range(24)),
      "product map S x C4 is a bijection onto all 24")
check("I.index", 24 // len(S) == 4, "index of S is 24 / 6 = 4")

BAD4 = (0, 4, 19, 23)
bad_inter = sorted(set(S) & set(BAD4))
bad_prod = sorted(set(MUL[s][t] for s in S for t in BAD4))
check("I.rejector", len(bad_inter) == 2 and len(bad_prod) == 12,
      "non-complement {} meets S twice, product covers {} of 24".format(
          BAD4, len(bad_prod)))

print("=== Theorem II: the operator is a function on Rot / S ===")

COSETS = [sorted(MUL[s][t] for s in S) for t in C4]
for t, blk in zip(C4, COSETS):
    print("right coset of {}: {}".format(t, blk))

for L in (3, 4):
    if L == L0:
        Q, perms, QG = Q0, P0, QG0
    else:
        Q = c696.assemble_static_hessian(L, False)["Q"]
        perms = {g: relabel(L, g) for g in range(24)}
        QG = {g: Q[np.ix_(perms[g], perms[g])] for g in range(24)}
    within = max(np.abs(QG[g] - QG[t]).max() for t, blk in zip(C4, COSETS) for g in blk)
    reps = [QG[t] for t in C4]
    across = min(np.abs(reps[i] - reps[j]).max()
                 for i in range(4) for j in range(i + 1, 4))
    print("L = {} n = {} within-coset {:.1e} across-coset {:.4f}".format(
        L, Q.shape[0], within, across))
    check("II.const.L{}".format(L), within < 1.0e-06,
          "operator constant on each right coset to {:.1e}".format(within))
    check("II.sep.L{}".format(L), across > 1.0,
          "the four representatives differ by at least {:.4f}".format(across))

    seen = []
    for g in range(24):
        if not any(np.abs(QG[g] - QG[h]).max() < 1.0e-06 for h in seen):
            seen.append(g)
    check("II.count.L{}".format(L), len(seen) == 4,
          "exactly {} distinct reassembled operators".format(len(seen)))

    left = [sorted(MUL[t][s] for s in S) for t in C4]
    lw = max(np.abs(QG[g] - QG[blk[0]]).max() for blk in left for g in blk)
    check("II.leftrejector.L{}".format(L), lw > 1.0,
          "left cosets are NOT constancy classes, deviation {:.4f}".format(lw))

print("=== Theorem III: complete blindness classification ===")

subs = {(IDENT,)}
for k in (1, 2, 3):
    for gen in itertools.combinations(range(24), k):
        cur = set(gen) | {IDENT}
        while True:
            new = set(MUL[a][b] for a in cur for b in cur)
            if new <= cur:
                break
            cur |= new
        subs.add(tuple(sorted(cur)))
subs = sorted(subs, key=lambda h: (len(h), h))
check("III.lattice", len(subs) == 30, "subgroup lattice has {} members".format(len(subs)))

law_ok = 0
for H in subs:
    covers = len(set(MUL[s][t] for s in S for t in H)) == 24
    law_ok += int(covers == (len(H) == 4 * len(set(H) & set(S))))
check("III.counting", law_ok == 30,
      "covering <-> |H| = 4 |H meet S| in {}/30 subgroups".format(law_ok))

covering = [H for H in subs if len(set(MUL[s][t] for s in S for t in H)) == 24]
minimal = [H for H in covering if len(H) == 4]
check("III.minorder", min(len(H) for H in covering) == 4,
      "minimal covering order is {}".format(min(len(H) for H in covering)))
check("III.mincount", len(minimal) == 4 and len(covering) == 9,
      "{} of the {} covering subgroups attain it".format(len(minimal), len(covering)))
check("III.c707minimal", tuple(sorted(C4)) in minimal,
      "the Cycle-707 stabilizer is one of the minimal blinders")
print("covering subgroup orders: {}".format(sorted(len(H) for H in covering)))
for H in minimal:
    print("minimal blinder: {}".format(H))

FOUR_IN_S = (1, 4, 9, 23)
check("III.notsubgroup", tuple(sorted(FOUR_IN_S)) not in [tuple(h) for h in subs],
      "the four-element subset {} of S is not a subgroup".format(FOUR_IN_S))

for L in (3, 4):
    if L == L0:
        Q, perms = Q0, P0
        QG = QG0
    else:
        Q = c696.assemble_static_hessian(L, False)["Q"]
        perms = {g: relabel(L, g) for g in range(24)}
        QG = {g: Q[np.ix_(perms[g], perms[g])] for g in range(24)}
    QI = {g: np.linalg.inv(QG[g]) for g in range(24)}
    rg = np.random.default_rng(7150 + L)
    srcs = []
    for _ in range(3):
        b = rg.normal(size=Q.shape[0])
        srcs.append(b / np.linalg.norm(b))

    def spread(over):
        worst = 0.0
        for b in srcs:
            bb = np.zeros(Q.shape[0])
            for a in over:
                bb += b[np.argsort(perms[a])]
            nb = float(np.linalg.norm(bb))
            if nb < 1.0e-08:
                return -1.0
            bb = bb / nb
            vs = [float(bb @ (QI[g] @ bb)) for g in range(24)]
            worst = max(worst, max(vs) - min(vs))
        return worst

    agree = 0
    blindest = 0.0
    sharpest = 1.0e+09
    for H in subs:
        covers = len(set(MUL[s][t] for s in S for t in H)) == 24
        sp = spread(H)
        agree += int((sp < 1.0e-06) == covers)
        if covers:
            blindest = max(blindest, sp)
        else:
            sharpest = min(sharpest, sp)
    print("L = {} covering worst {:.1e} non-covering smallest {:.1e}".format(
        L, blindest, sharpest))
    check("III.scan.L{}".format(L), agree == 30,
          "measured blindness matches the covering law in {}/30".format(agree))
    check("III.gap.L{}".format(L), sharpest > 1.0e+05 * blindest,
          "separation factor {:.1e}".format(sharpest / blindest))
    check("III.sextet.L{}".format(L), spread(S) > 1.0e-03,
          "S alone does NOT blind, spread {:.1e}".format(spread(S)))
    check("III.subset.L{}".format(L), spread(FOUR_IN_S) > 1.0e-03,
          "four-in-S subset does NOT blind, spread {:.1e}".format(spread(FOUR_IN_S)))
    check("III.c707blind.L{}".format(L), spread(C4) < 1.0e-06,
          "Cycle-707 stabilizer average is blind to {:.1e}".format(spread(C4)))
    check("III.all24.L{}".format(L), spread(range(24)) < 1.0e-06,
          "the 24-frame average is blind to {:.1e}".format(spread(range(24))))

NOTES["operator_scale"] = "{:.1f}".format(SCALE)
NOTES["zero_defect_tol"] = "{:.1e}".format(ZERO_TOL)
NOTES["zero_defect_frames"] = list(S)
NOTES["transversal"] = sorted(C4)
NOTES["subgroup_lattice"] = len(subs)
NOTES["covering_orders"] = sorted(len(H) for H in covering)
NOTES["minimal_blinders"] = [list(H) for H in minimal]

receipt = {"box_sizes": [3, 4],
           "fail": FAIL,
           "gates": GATES,
           "notes": NOTES,
           "pass": PASS,
           "runner": os.path.basename(os.path.abspath(__file__))}
outdir = os.path.join(ROOT, "outputs")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, RECEIPT_NAME), "w") as fh:
    fh.write(json.dumps(receipt, sort_keys=True, indent=2) + "\n")

print("TOTAL: PASS={} FAIL={}".format(PASS, FAIL))
raise SystemExit(1 if FAIL else 0)
