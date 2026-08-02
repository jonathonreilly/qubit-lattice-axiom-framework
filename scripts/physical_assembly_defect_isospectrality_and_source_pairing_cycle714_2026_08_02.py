"""Cycle 714 - assembly-defect isospectrality and the source-pairing collapse.

Self-contained against the landed Cycle-696 open-coframe compiler chain. Establishes
that the 24 coframe relabellings act on the static degrees of freedom by permutations
forming a faithful group action, that the assembly defect is therefore exactly
isospectral with an exact Frobenius law, and that its entire observable content is the
pairing with a source that does not transport - which collapses the 24-frame scan to
four values, one per right coset of the constant-sign sextet.

Class-A finite-dimensional check. Prints TOTAL: PASS=N FAIL=0.
"""

import importlib.util
import json
import os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location(
    "c696_chain",
    os.path.join(HERE,
                 "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"))
c696 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c696)

FRAMES = [np.asarray(F, dtype=np.int64) for F in c696.c576.FRAMES]
DIRS15 = c696.regge.DIRS15
SPC = sorted(c696.SPATIAL_CLASSES)
DIRV = {c: np.asarray(DIRS15[c][:3], dtype=np.int64) for c in SPC}
D2C = {tuple(int(t) for t in DIRV[c]): c for c in SPC}
LT = 2
SEXTET = [1, 4, 9, 15, 18, 23]
MIXED = [g for g in range(24) if g not in SEXTET]
FMAP = {tuple(F.ravel().tolist()): a for a, F in enumerate(FRAMES)}

RECEIPT_NAME = ("physical_assembly_defect_isospectrality_and_source_pairing"
                "_cycle714_2026_08_02_receipt_2026-08-02.json")

PASS = 0
FAIL = 0
GATES = {}
NOTES = {}


def gate(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
    else:
        FAIL += 1
    GATES["g{:02d}".format(len(GATES) + 1)] = {
        "claim": name, "pass": bool(ok), "detail": detail}
    print("[{}] {}{}".format("PASS" if ok else "FAIL", name,
                             (" | " + detail) if detail else ""))


def mul(a, b):
    return FMAP[tuple((FRAMES[a] @ FRAMES[b]).ravel().tolist())]


def dof_perm(L, index, R, anchor=True):
    """Relabelling of the dof set induced by the proper rotation R."""
    smap = c696.frame_site_map(L, R)
    m = np.empty(len(index), dtype=np.int64)
    outside = 0
    for (cls, x), i in index.items():
        w = R @ DIRV[cls]
        vp = tuple(int(t) for t in np.abs(w))
        base = np.asarray(smap[x], dtype=np.int64)
        xp = tuple(int(t) for t in (base + np.minimum(w, 0) if anchor else base))
        key = (D2C[vp], xp)
        if key in index:
            m[i] = index[key]
        else:
            m[i] = -1
            outside += 1
    return m, outside


def model_of(L):
    md = c696.assemble_static_hessian(L, False)
    return np.asarray(md["Q"], dtype=float), md["index"]


def dof_count(L):
    u = L - 1
    return 3 * u * L * L + 3 * u * u * L + u ** 3


def frob_law(L):
    u = L - 1
    return 800.0 * u ** 3 + 224.0 * u ** 2 + 32.0 * u


print("== Cycle 714: assembly-defect isospectrality and the source pairing ==")
print("frames={} constant-sign={} mixed={} LT={}".format(
    len(FRAMES), len(SEXTET), len(MIXED), LT))

# ---------------------------------------------------------------- group action
cache = {}
for L in (3, 4, 5, 6):
    cache[L] = model_of(L)

ok = all(cache[L][0].shape[0] == dof_count(L) for L in (3, 4, 5, 6))
gate("dof count matches the open-box formula", ok,
     "n = " + " ".join(str(cache[L][0].shape[0]) for L in (3, 4, 5, 6)))

perms = {}
bij = True
for L in (3, 4, 5, 6):
    Q, index = cache[L]
    n = Q.shape[0]
    perms[L] = []
    for g in range(24):
        m, outside = dof_perm(L, index, FRAMES[g])
        perms[L].append(m)
        if outside or len(set(m.tolist())) != n:
            bij = False
gate("every frame relabelling is a bijection of the dof set", bij,
     "24 frames at L = 3,4,5,6; zero dofs outside the index")

idg = [a for a in range(24) if np.array_equal(FRAMES[a], np.eye(3, dtype=np.int64))]
ok = (len(idg) == 1
      and all(np.array_equal(perms[L][idg[0]], np.arange(cache[L][0].shape[0]))
              for L in (3, 4, 5, 6)))
gate("identity frame gives the identity relabelling", ok,
     "frame index {}".format(idg[0] if idg else -1))

for L in (3, 4):
    hits = sum(1 for a in range(24) for b in range(24)
               if np.array_equal(perms[L][mul(a, b)], perms[L][a][perms[L][b]]))
    gate("group law m(ab) = m(a) after m(b) at L = {}".format(L), hits == 576,
         "{} of 576 ordered pairs".format(hits))

rej = []
for L in (3, 4):
    Q, index = cache[L]
    n = Q.shape[0]
    bad = []
    for g in (0, 2, 5):
        m, outside = dof_perm(L, index, FRAMES[g], anchor=False)
        bad.append((outside, len(set(m[m >= 0].tolist()))))
    rej.append((L, n, bad))
ok = all(o > 0 and d < n for (L, n, bad) in rej for (o, d) in bad)
gate("rejector: dropping the anchor shift breaks bijectivity", ok,
     "L = 3: {} of {} dofs outside, {} distinct images".format(
         rej[0][2][0][0], rej[0][1], rej[0][2][0][1]))

# ------------------------------------------------------------- isospectrality
inertia = []
least = 1.0e+09
for L in (3, 4, 5):
    ev = np.linalg.eigvalsh(cache[L][0])
    inertia.append("{}/{}".format(int((ev < 0).sum()), int((ev > 0).sum())))
    least = min(least, float(np.abs(ev).min()))
gate("the assembled operator is nonsingular and indefinite", least > 1.0e-03,
     "negative/positive counts at L = 3,4,5: {} ; smallest magnitude {:.1e}".format(
         " ".join(inertia), least))

spec_cover = {3: MIXED, 4: MIXED, 5: MIXED[:4], 6: MIXED[:2]}
for L in (3, 4, 5, 6):
    Q = cache[L][0]
    eq = np.linalg.eigvalsh(Q)
    worst = 0.0
    for g in spec_cover[L]:
        m = perms[L][g]
        worst = max(worst, float(np.abs(
            np.linalg.eigvalsh(Q[np.ix_(m, m)]) - eq).max()))
    gate("spectrum is unchanged by mixed-frame reassembly at L = {}".format(L),
         worst < 1.0e-10,
         "{} frames, worst deviation {:.1e}".format(len(spec_cover[L]), worst))

for L in (3, 4):
    Q = cache[L][0]
    wt = 0.0
    for g in MIXED:
        m = perms[L][g]
        wt = max(wt, abs(float(np.trace(Q[np.ix_(m, m)] - Q))))
    gate("defect is traceless at L = {}".format(L), wt < 1.0e-10,
         "18 mixed frames, worst {:.1e}".format(wt))

Q3 = cache[3][0]
w2 = w3 = 0.0
for g in MIXED:
    m = perms[3][g]
    E = Q3[np.ix_(m, m)] - Q3
    QE = Q3 @ E
    w2 = max(w2, abs(float(np.trace(QE) + 0.5 * np.trace(E @ E))))
    w3 = max(w3, abs(float(3.0 * np.trace(Q3 @ QE) + 3.0 * np.trace(QE @ E)
                           + np.trace(E @ E @ E))))
gate("second power-sum identity holds", w2 < 1.0e-08, "worst {:.1e}".format(w2))
gate("third power-sum identity holds", w3 < 1.0e-06, "worst {:.1e}".format(w3))

Q4, _ = cache[4]
ev4, U4 = np.linalg.eigh(Q4)
worst = 0.0
for g in MIXED[:3]:
    m = perms[4][g]
    Qp = Q4[np.ix_(m, m)]
    for k in (0, -1):
        v = U4[:, k][m]
        worst = max(worst, float(np.abs(Qp @ v - ev4[k] * v).max()))
gate("eigenvectors are transported, not mixed", worst < 1.0e-10,
     "top and bottom, 3 frames, worst residual {:.1e}".format(worst))

for L in (3, 4):
    Q = cache[L][0]
    eq = np.linalg.eigvalsh(Q)
    m = perms[L][MIXED[0]]
    E = Q[np.ix_(m, m)] - Q
    nzp = np.abs(E) > 1.0e-09
    shifts = []
    for seed in (1, 2, 3):
        rg = np.random.default_rng(7140 + seed)
        s = rg.integers(0, 2, size=E.shape) * 2 - 1
        s = np.triu(s) + np.triu(s, 1).T
        Er = np.abs(E) * s * nzp
        Er = Er * np.sqrt(float((E * E).sum()) / float((Er * Er).sum()))
        shifts.append(float(np.abs(np.linalg.eigvalsh(Q + Er) - eq).max()))
    gate("rejector: same pattern, same magnitudes, resigned, at L = {}".format(L),
         min(shifts) > 1.0,
         "smallest spectral shift {:.2e} over 3 seeds".format(min(shifts)))

# ------------------------------------------------------------- Frobenius law
c713_counts = [(16.0, 8, 0, 0), (12.0, 8, 0, 0), (8.0, 12, 16, 0),
               (4.0, 20, -8, 4), (1.0, 0, 16, 0)]
asm = [2.0 * sum(row[0] * row[1 + k] for row in c713_counts) for k in (0, 1, 2)]
gate("Frobenius law reassembles from the landed census", asm == [800.0, 224.0, 32.0],
     "cubic {:.0f}, quadratic {:.0f}, linear {:.0f}".format(*asm))

fnorms = {}
for L in (3, 4, 5, 6, 7, 8):
    if L in cache:
        Q, index = cache[L]
        pl = perms[L]
    else:
        Q, index = model_of(L)
        pl = None
    fnorms[L] = float((Q * Q).sum())
    cover = MIXED if L <= 7 else MIXED[:3]
    worst = 0.0
    for g in cover:
        m = pl[g] if pl is not None else dof_perm(L, index, FRAMES[g])[0]
        E = Q[np.ix_(m, m)] - Q
        worst = max(worst, abs(float((E * E).sum()) - frob_law(L)) / frob_law(L))
        del E
    gate("Frobenius law {:.0f} holds at L = {}".format(frob_law(L), L),
         worst < 1.0e-08,
         "{} mixed frames, worst relative deviation {:.1e}".format(
             len(cover), worst))
    if L not in cache:
        del Q, index

worst = 0.0
for L in (3, 4, 5, 6):
    Q = cache[L][0]
    for g in SEXTET:
        m = perms[L][g]
        E = Q[np.ix_(m, m)] - Q
        worst = max(worst, float((E * E).sum()))
gate("constant-sign frames carry no defect", worst < 1.0e-12,
     "6 frames at L = 3,4,5,6, ceiling {:.1e}".format(worst))

ratios = [frob_law(L) / fnorms[L] for L in (3, 4, 5, 6, 7, 8)]
ok = all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1)) and min(ratios) > 0.1
gate("relative defect grows with box size", ok,
     "ratios " + " ".join("{:.4f}".format(r) for r in ratios))

# ------------------------------------------------------ source-pairing content
def pairings(L, direct):
    Q, index = cache[L]
    n = Q.shape[0]
    rg = np.random.default_rng(714)
    b = rg.normal(size=n)
    b = b / np.linalg.norm(b)
    if direct:
        return b, [float(b @ np.linalg.solve(Q[np.ix_(perms[L][g], perms[L][g])], b))
                   for g in range(24)]
    Qi = np.linalg.inv(Q)
    out = []
    for g in range(24):
        bb = b[np.argsort(perms[L][g])]
        out.append(float(bb @ (Qi @ bb)))
    return b, out


orb = {}
for L in (3, 4):
    b, direct = pairings(L, True)
    _, orbit = pairings(L, False)
    orb[L] = orbit
    dev = float(np.abs(np.asarray(direct) - np.asarray(orbit)).max())
    gate("pairing transfers to the relabelled source at L = {}".format(L),
         dev < 1.0e-09, "24 frames, worst deviation {:.1e}".format(dev))
for L in (5, 6):
    orb[L] = pairings(L, False)[1]

Q4, index4 = cache[4]
rg = np.random.default_rng(714)
b4 = rg.normal(size=Q4.shape[0])
b4 = b4 / np.linalg.norm(b4)
xref = np.linalg.solve(Q4, b4)
wt = wf = 0.0
for g in MIXED[:3]:
    m = perms[4][g]
    Qp = Q4[np.ix_(m, m)]
    wt = max(wt, float(np.linalg.norm(np.linalg.solve(Qp, b4[m]) - xref[m])
                       / np.linalg.norm(xref)))
    wf = max(wf, float(np.linalg.norm(np.linalg.solve(Qp, b4) - xref)
                       / np.linalg.norm(xref)))
gate("a transported source reproduces the reference solution", wt < 1.0e-09,
     "worst relative deviation {:.1e}".format(wt))
gate("a source held fixed does not", wf > 0.5,
     "smallest relative deviation {:.4f}".format(wf))

spreads = []
for L in (3, 4, 5):
    v = np.asarray(orb[L])
    ref = v[idg[0]]
    spreads.append((float(v.max() - v.min()) / abs(float(ref))))
gate("frame spread of the pairing stays order one", min(spreads) > 0.5,
     "spread over reference " + " ".join("{:.4f}".format(s) for s in spreads))

closed = all(mul(a, b) in SEXTET for a in SEXTET for b in SEXTET)
traces = sorted(int(np.trace(FRAMES[a])) for a in SEXTET)
gate("constant-sign frames form a subgroup", closed and idg[0] in SEXTET,
     "order 6, traces {}".format(traces))

cosets = {}
for a in range(24):
    cosets.setdefault(frozenset(mul(s, a) for s in SEXTET), []).append(a)
gate("the subgroup has four right cosets", len(cosets) == 4,
     "sizes " + " ".join(str(len(v)) for v in cosets.values()))

worst_in = 0.0
least_out = 1.0e9
for L in (3, 4, 5, 6):
    v = np.asarray(orb[L])
    reps = []
    for cs in cosets.values():
        w = v[sorted(cs)]
        worst_in = max(worst_in, float(w.max() - w.min()))
        reps.append(float(w.mean()))
    reps = sorted(reps)
    least_out = min(least_out,
                    min(reps[i + 1] - reps[i] for i in range(3)))
gate("the pairing is constant on each right coset", worst_in < 1.0e-08,
     "worst variation within a coset {:.1e}".format(worst_in))
gate("the four coset values are separated", least_out > 1.0e-03,
     "nearest pair of coset values {:.4f} apart".format(least_out))

nd = []
for L in (3, 4, 5, 6):
    v = np.sort(np.asarray(orb[L]))
    nd.append(1 + int((np.diff(v) > 1.0e-06).sum()))
gate("the 24-frame scan takes exactly four values", set(nd) == {4},
     "distinct values at L = 3,4,5,6: " + " ".join(str(k) for k in nd))

def averaged_spread(L, over):
    Q = cache[L][0]
    n = Q.shape[0]
    rg = np.random.default_rng(714)
    b = rg.normal(size=n)
    b = b / np.linalg.norm(b)
    bav = np.zeros(n)
    for a in over:
        bav += b[np.argsort(perms[L][a])]
    bav = bav / np.linalg.norm(bav)
    Qi = np.linalg.inv(Q)
    vals = [float(bav[np.argsort(perms[L][g])]
                  @ (Qi @ bav[np.argsort(perms[L][g])])) for g in range(24)]
    return max(vals) - min(vals)


full = max(averaged_spread(L, range(24)) for L in (3, 4))
part = min(averaged_spread(L, SEXTET) for L in (3, 4))
gate("a fully averaged source is blind to the frame", full < 1.0e-09,
     "spread over 24 frames {:.1e}".format(full))
gate("rejector: averaging over the subgroup alone does not suffice", part > 1.0e-02,
     "smallest remaining spread {:.4f}".format(part))

# ------------------------------------------------------------------- receipt
NOTES["action"] = "m(gh) = m(g) after m(h); Q_g = P Q P^T, P the permutation of m(g)"
NOTES["frobenius_law"] = "|E_g|_F^2 = 800(L-1)^3 + 224(L-1)^2 + 32(L-1)"
NOTES["frobenius_values"] = {str(L): frob_law(L) for L in (3, 4, 5, 6, 7, 8)}
NOTES["dof_counts"] = {str(L): dof_count(L) for L in (3, 4, 5, 6, 7, 8)}
NOTES["pairing_transfer"] = "b . Q_g^-1 . b = (P^T b) . Q^-1 . (P^T b)"
NOTES["coset_sizes"] = [len(v) for v in cosets.values()]
NOTES["sextet_traces"] = sorted(int(np.trace(FRAMES[a])) for a in SEXTET)
NOTES["full_average_spread"] = "{:.1e}".format(full)
NOTES["subgroup_average_spread"] = "{:.1e}".format(part)

receipt = {
    "cycle": 714,
    "object": "assembly-defect isospectrality and the source-pairing collapse",
    "LT": LT,
    "frames": len(FRAMES),
    "constant_sign_frames": len(SEXTET),
    "mixed_frames": len(MIXED),
    "identity_frame": [a for a in range(24)
                       if np.array_equal(FRAMES[a], np.eye(3, dtype=np.int64))][0],
    "sizes": [3, 4, 5, 6, 7, 8],
    "distinct_pairing_values": 4,
    "gates": GATES,
    "notes": NOTES,
    "pass": PASS,
    "fail": FAIL,
}
_out = os.path.join(os.path.dirname(HERE), "outputs", RECEIPT_NAME)
os.makedirs(os.path.dirname(_out), exist_ok=True)
with open(_out, "w") as _fh:
    _fh.write(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
print("receipt: outputs/{}".format(RECEIPT_NAME))

print("")
print("TOTAL: PASS={} FAIL={}".format(PASS, FAIL))
raise SystemExit(0 if FAIL == 0 else 1)
