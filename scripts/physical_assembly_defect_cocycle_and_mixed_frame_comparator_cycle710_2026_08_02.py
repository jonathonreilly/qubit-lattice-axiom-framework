#!/usr/bin/env python3
"""Cycle-710 runner -- the assembly equivariance defect is an exact cocycle on the
constant-sign sextet, with a finite mixed-frame comparator census.

Paired note:
  docs/PHYSICAL_ASSEMBLY_DEFECT_COCYCLE_AND_MIXED_FRAME_COMPARATOR_CYCLE710_NOTE_2026-08-02.md

Measures, on the cycle-696 compiled chain imported verbatim (never re-implemented):
  C0  frame scope: census of the 24 proper rotations, transport bijections,
      solver scope, identity-frame zero
  C1  transport functoriality on the sextet: m_(a.b) = m_a[m_b] exactly, closure,
      branch product rule
  C2  the exact cocycle identity E_(a.b) = E_b + Pi_b^T E_a Pi_b, with
      transport-order and wrong-branch discriminators
  C3  branch uniformity: within-branch and across-size bitwise equality of the
      defect ceiling, and the derived coset-spread law (spread = plus ceiling,
      bit for bit)
  C4  the first-order response law at every all-minus frame, with plus-branch
      rejectors and the floor-uniformity band
  C5  the finite mixed-frame comparator census: order-one comparator, bitwise
      uniform across all 18 non-sextet frames, its separation, one law-failure
      witness, and the body-diagonal sign-mixing census
  C6  census cross-checks against the landed cycle-700 identification

Read inventory. External/ancestral scientific input: the cycle-696 compiler module
and its transitive scripts/ imports, declared in AUDIT_INPUT_PATHS below and loaded
as a library; every physical quantity below is computed through them. No sibling
cycle's measured value is read or copied in. Package-local write activity: one paired
receipt under outputs/. This runner performs no self-hash or receipt-verification
integrity read.

All floating quantities print through one format ({:.1e}); the receipt carries the
same strings. Honest-miss rule: every gate band was fixed before this runner ran;
a miss prints FAIL and the total line reports it.
"""
import importlib.util
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_c710", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

# The load-bearing repository-source closure: the cycle-696 compiler loaded above
# plus every scripts/ module it imports transitively. Declared so the runner cache
# pins their bytes and rejects input drift.
AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

# Observed runtime is a few seconds at L=7; this margin covers the dense solve on
# a slower independent-review host.
AUDIT_TIMEOUT_SEC = 600

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
EYE3 = np.eye(3, dtype=np.int64)
L_LIST = (3, 7)
SEXTET_EXPECT = [1, 4, 9, 15, 18, 23]
ORDERS_EXPECT = {1: 2, 4: 2, 9: 2, 15: 3, 18: 3, 23: 1}
NFLIP_EXPECT = {0: 3, 1: 9, 2: 9, 3: 3}
BODY_CLASS = 13
RECEIPT_NAME = ("physical_assembly_defect_cocycle_and_mixed_frame_comparator_"
                "cycle710_2026_08_02_receipt_2026-08-02.json")

fmt = "{:.1e}".format
PASS = 0
FAIL = 0


def check(tag, cond, detail):
    global PASS, FAIL
    if cond:
        PASS += 1
        print("ok   {} {}".format(tag, detail))
    else:
        FAIL += 1
        print("FAIL {} {}".format(tag, detail))


def find_frame(R):
    for k, F in enumerate(FRAMES):
        if np.array_equal(F, R):
            return k
    return -1


def dof_perm(index, smap, R):
    dir2class = {tuple(c696.regge.DIRS15[c][:3]): c for c in c696.SPATIAL_CLASSES}
    m = np.empty(len(index), dtype=np.int64)
    for (c, x), i in index.items():
        v = np.asarray(c696.regge.DIRS15[c][:3], dtype=np.int64)
        w = R @ v
        vp = tuple(int(t) for t in np.abs(w))
        xp = tuple(int(t) for t in (np.asarray(smap[x], dtype=np.int64)
                                    + np.minimum(w, 0)))
        m[i] = index[(dir2class[vp], xp)]
    return m


def push(vec, m):
    out = np.empty_like(vec)
    out[m] = vec
    return out


# frame-level combinatorics (size-independent)
CLASS_DIRS = {c: np.asarray(c696.regge.DIRS15[c][:3], dtype=np.int64)
              for c in c696.SPATIAL_CLASSES}


def mixed_classes(R):
    out = []
    for c, v in CLASS_DIRS.items():
        w = R @ v
        if bool((w > 0).any()) and bool((w < 0).any()):
            out.append(c)
    return out


def frame_order(R):
    P = np.array(EYE3)
    for k in range(1, 7):
        P = P @ R
        if np.array_equal(P, EYE3):
            return k
    return 0


nflip = {g: int((FRAMES[g] == -1).sum()) for g in range(24)}
plus_set = sorted(g for g in range(24)
                  if not any((FRAMES[g] @ v < 0).any() for v in CLASS_DIRS.values()))
const_set = sorted(g for g in range(24) if not mixed_classes(FRAMES[g]))
minus_set = sorted(set(const_set) - set(plus_set))
mixed_set = sorted(set(range(24)) - set(const_set))
SEXTET = const_set
NONID = [g for g in SEXTET if g != 23]

print("== frame combinatorics (all 24 proper rotations) ==")
print("constant-sign sextet: {}  plus {}  minus {}  mixed count {}".format(
    const_set, plus_set, minus_set, len(mixed_set)))
nflip_census = {}
for g in range(24):
    nflip_census[nflip[g]] = nflip_census.get(nflip[g], 0) + 1
orders = {g: frame_order(FRAMES[g]) for g in SEXTET}
print("nflip census: {}  sextet orders: {}".format(
    sorted(nflip_census.items()), sorted(orders.items())))

ctx = {}
for L in L_LIST:
    model = c696.assemble_static_hessian(L, wrap=False)
    sol = c696.sector_solve(model)
    A = (L - 1) // 2
    dom0 = c696.build_domain(L, edits={((A, A, A), (A + 1, A, A)): 5})
    rho0 = c696.rho_vector(dom0, model["site_index"])
    b0 = rho0 @ model["G"]
    eps_of = lambda b, _m=model, _s=sol: c696.response(_m, _s, b)["eps"]
    eps0 = eps_of(b0)
    Q = model["Q"]
    n = Q.shape[0]
    reg = sol["regular"]
    lam_min = float(np.abs(sol["w"])[reg].min())
    smaps = {g: c696.frame_site_map(L, FRAMES[g]) for g in range(24)}
    M = {g: dof_perm(model["index"], smaps[g], FRAMES[g]) for g in range(24)}
    E = {g: Q[np.ix_(M[g], M[g])] - Q for g in NONID}
    ctx[L] = {"model": model, "sol": sol, "b0": b0, "eps0": eps0, "Q": Q,
              "n": n, "M": M, "E": E, "eps_of": eps_of, "lam_min": lam_min}
    print("L={} n_dof={} null_dim={} lam_min={} |w|max={} |eps0|_2={}".format(
        L, n, sol["null_dim"], fmt(lam_min), fmt(sol["abs_max"]),
        fmt(float(np.linalg.norm(eps0)))))

meas = {}
for L in L_LIST:
    c = ctx[L]
    M, E, Q, n = c["M"], c["E"], c["Q"], c["n"]
    eps_of, b0, eps0 = c["eps_of"], c["b0"], c["eps0"]

    dq = {g: float(np.abs(E[g]).max()) for g in NONID}
    spread = {g: float(np.abs(E[g] - E[minus_set[0]]).max()) for g in minus_set[1:]}
    print("L={} dQ minus {} plus {} coset spread {}".format(
        L, fmt(dq[minus_set[0]]), fmt(dq[plus_set[0]]),
        fmt(max(spread.values()))))

    coc_worst = 0.0
    coc_pairs = 0
    for a in NONID:
        for b in NONID:
            k = find_frame(FRAMES[a] @ FRAMES[b])
            if k == 23:
                continue
            coc_pairs += 1
            r = float(np.abs(E[k] - (E[b] + E[a][np.ix_(M[b], M[b])])).max())
            coc_worst = max(coc_worst, r)
    a0, b0f = 1, 15
    k_fwd = find_frame(FRAMES[a0] @ FRAMES[b0f])
    k_rev = find_frame(FRAMES[b0f] @ FRAMES[a0])
    rev = float(np.abs(E[k_rev] - (E[b0f] + E[a0][np.ix_(M[b0f], M[b0f])])).max())
    k_sq = find_frame(FRAMES[15] @ FRAMES[15])
    wrong = float(np.abs(E[k_sq] - (E[1] + E[1][np.ix_(M[15], M[15])])).max())
    print("L={} cocycle worst {} over {} pairs; reversed {} wrong-frame {}".format(
        L, fmt(coc_worst), coc_pairs, fmt(rev), fmt(wrong)))

    laws = {}
    for g in NONID:
        m = M[g]
        t2 = eps_of(push(b0, m)) - push(eps0, m)
        pred = push(eps_of(E[g] @ eps0), m)
        den = float(np.linalg.norm(t2))
        pn = float(np.linalg.norm(pred))
        laws[g] = {"resid": float(np.linalg.norm(t2 - pred)) / den,
                   "cos": float(t2 @ pred / (den * pn)), "den": den}
        print("L={} law g={:2d} resid={} cos={} |t2|={}".format(
            L, g, fmt(laws[g]["resid"]), fmt(laws[g]["cos"]), fmt(den)))
    floors = [laws[g]["den"] for g in minus_set]
    floor_spread = (max(floors) - min(floors)) / max(floors)

    mixed_hex = set()
    mixed_emax = None
    mixed_law = None
    mixed_law_frame = None
    for g in mixed_set:
        m = M[g]
        Em = Q[np.ix_(m, m)] - Q
        e = float(np.abs(Em).max())
        mixed_hex.add(e.hex())
        if mixed_emax is None:
            mixed_emax = e
            mixed_law_frame = g
            t2 = eps_of(push(b0, m)) - push(eps0, m)
            pred = push(eps_of(Em @ eps0), m)
            mixed_law = float(np.linalg.norm(t2 - pred)) / float(np.linalg.norm(t2))
        del Em
    print("L={} mixed |E|max {} |Emax-4| {} sep vs minus {} law resid {} floor spread {}".format(
        L, fmt(mixed_emax), fmt(abs(mixed_emax - 4.0)),
        fmt(mixed_emax / dq[minus_set[0]]), fmt(mixed_law), fmt(floor_spread)))

    meas[L] = {"dq": dq, "spread": spread, "coc_worst": coc_worst,
               "coc_pairs": coc_pairs, "rev": rev, "wrong": wrong,
               "k_fwd": k_fwd, "k_rev": k_rev, "laws": laws,
               "floor_spread": floor_spread, "mixed_hex": mixed_hex,
               "mixed_emax": mixed_emax, "mixed_law": mixed_law,
               "mixed_law_frame": mixed_law_frame}

print("== C0 frame scope, census, bijections, solver scope ==")
check("c0.det", all(round(float(np.linalg.det(FRAMES[g]))) == 1 for g in range(24)),
      "24 frames, det=+1 for all")
check("c0.census.plus", plus_set == [15, 18, 23], "all-plus frames {}".format(plus_set))
check("c0.census.minus", minus_set == [1, 4, 9], "all-minus frames {}".format(minus_set))
check("c0.census.mixed", len(mixed_set) == 18, "mixed-sign frames {}".format(len(mixed_set)))
for L in L_LIST:
    c = ctx[L]
    check("c0.bij.L{}".format(L),
          all(len(set(c["M"][g].tolist())) == c["n"] for g in range(24)),
          "all 24 dof transports bijective")
    check("c0.null.L{}".format(L), c["sol"]["null_dim"] == 0, "null_dim=0")
id_ok = np.array_equal(ctx[3]["M"][23], np.arange(ctx[3]["n"]))
check("c0.identity", id_ok and float(np.abs(
    ctx[3]["Q"][np.ix_(ctx[3]["M"][23], ctx[3]["M"][23])] - ctx[3]["Q"]).max()) == 0.0,
      "identity frame: transport trivial, defect 0.0e+00")

print("== C1 transport functoriality and group structure on the sextet ==")
for L in L_LIST:
    M = ctx[L]["M"]
    ok = all(np.array_equal(M[find_frame(FRAMES[a] @ FRAMES[b])], M[a][M[b]])
             for a in SEXTET for b in SEXTET)
    check("c1.func.L{}".format(L), ok, "m_(a.b) = m_a[m_b] on all 36 sextet pairs")
check("c1.closure", all(find_frame(FRAMES[a] @ FRAMES[b]) in SEXTET
                        for a in SEXTET for b in SEXTET),
      "sextet closed under composition")


def branch_sign(g):
    return -1 if g in minus_set else 1


check("c1.coset", all(branch_sign(find_frame(FRAMES[a] @ FRAMES[b]))
                      == branch_sign(a) * branch_sign(b)
                      for a in SEXTET for b in SEXTET),
      "branch product rule: minus.minus=plus, minus.plus=minus")

print("== C2 exact cocycle identity with frame-specific discriminators ==")
for L in L_LIST:
    check("c2.cocycle.L{}".format(L), meas[L]["coc_worst"] <= 1e-20,
          "worst residual {} over composable pairs".format(fmt(meas[L]["coc_worst"])))
    check("c2.pairs.L{}".format(L), meas[L]["coc_pairs"] == 20,
          "non-identity pairs with non-identity product {}".format(meas[L]["coc_pairs"]))
m_rej = int(np.sum(ctx[3]["M"][1][ctx[3]["M"][15]] != ctx[3]["M"][15][ctx[3]["M"][1]]))
check("c2.reject.m", m_rej >= 1 and meas[3]["k_fwd"] != meas[3]["k_rev"],
      "non-commuting pair: {} transport entries differ under reversal".format(m_rej))
for L in L_LIST:
    check("c2.reject.E.L{}".format(L), meas[L]["wrong"] >= 1e-11,
          "wrong-frame bracket misses by {} (cross-branch)".format(
              fmt(meas[L]["wrong"])))
    check("c2.rev.L{}".format(L), meas[L]["rev"] <= 1e-13,
          "reversed-order bracket within coset-spread scale {}".format(
              fmt(meas[L]["rev"])))

print("== C3 branch uniformity and the coset-spread law ==")
for L in L_LIST:
    dq = meas[L]["dq"]
    check("c3.minus.bit.L{}".format(L),
          len({dq[g].hex() for g in minus_set}) == 1,
          "minus-branch ceiling bit-identical across frames {}".format(fmt(dq[1])))
    check("c3.plus.bit.L{}".format(L),
          len({dq[g].hex() for g in [15, 18]}) == 1,
          "plus-branch ceiling bit-identical across frames {}".format(fmt(dq[15])))
check("c3.size.minus", meas[3]["dq"][1].hex() == meas[7]["dq"][1].hex(),
      "minus ceiling bit-identical across sizes {}".format(fmt(meas[3]["dq"][1])))
check("c3.size.plus", meas[3]["dq"][15].hex() == meas[7]["dq"][15].hex(),
      "plus ceiling bit-identical across sizes {}".format(fmt(meas[3]["dq"][15])))
for L in L_LIST:
    sp = meas[L]["spread"]
    check("c3.spread.L{}".format(L),
          {v.hex() for v in sp.values()} == {meas[L]["dq"][15].hex()},
          "coset spread equals plus ceiling bit for bit {}".format(
              fmt(max(sp.values()))))

print("== C4 first-order law at every all-minus frame ==")
for L in L_LIST:
    laws = meas[L]["laws"]
    for g in minus_set:
        check("c4.resid.L{}.g{}".format(L, g), laws[g]["resid"] <= 2e-3,
              "minus law residual {}".format(fmt(laws[g]["resid"])))
    worst_cos = max(1.0 - laws[g]["cos"] for g in minus_set)
    check("c4.cos.L{}".format(L), worst_cos <= 1e-2,
          "worst minus alignment gap {}".format(fmt(worst_cos)))
    rej = min(laws[g]["resid"] for g in [15, 18])
    check("c4.reject.L{}".format(L), rej >= 0.5,
          "plus-branch rejector residual {}".format(fmt(rej)))
    check("c4.floor.L{}".format(L), meas[L]["floor_spread"] <= 1e-2,
          "minus floor relative spread {}".format(fmt(meas[L]["floor_spread"])))

print("== C5 finite mixed-frame comparator census and one response-law witness ==")
for L in L_LIST:
    check("c5.uniform.L{}".format(L), len(meas[L]["mixed_hex"]) == 1,
          "comparator bit-identical across all 18 non-sextet frames")
    check("c5.value.L{}".format(L), abs(meas[L]["mixed_emax"] - 4.0) <= 1e-6,
          "comparator {} within {} of 4".format(
              fmt(meas[L]["mixed_emax"]), fmt(abs(meas[L]["mixed_emax"] - 4.0))))
    check("c5.sep.L{}".format(L),
          meas[L]["mixed_emax"] / meas[L]["dq"][1] >= 1e9,
          "boundary separation {}".format(fmt(meas[L]["mixed_emax"] / meas[L]["dq"][1])))
    check("c5.reject.L{}".format(L), meas[L]["mixed_law"] >= 0.5,
          "first-order law fails at mixed frame {}, residual {}".format(
              meas[L]["mixed_law_frame"], fmt(meas[L]["mixed_law"])))
check("c5.carrier",
      all(BODY_CLASS in mixed_classes(FRAMES[g]) for g in mixed_set),
      "body-diagonal class carries the obstruction at all 18 frames")
check("c5.equiv",
      all((len(mixed_classes(FRAMES[g])) == 0) == (g in SEXTET) for g in range(24)),
      "zero mixed classes iff constant-sign sextet, over all 24")

print("== C6 census cross-checks against the landed cycle-700 identification ==")
check("c6.list", const_set == SEXTET_EXPECT,
      "constant-sign list {}".format(const_set))
check("c6.nflip", nflip_census == NFLIP_EXPECT,
      "nflip census {}".format(sorted(nflip_census.items())))
check("c6.orders", orders == ORDERS_EXPECT,
      "sextet element orders {}".format(sorted(orders.items())))

receipt = {
    "frames": {"sextet": const_set, "plus": plus_set, "minus": minus_set,
               "n_mixed": len(mixed_set),
               "nflip_census": {str(k): v for k, v in sorted(nflip_census.items())},
               "orders": {str(k): v for k, v in sorted(orders.items())}},
    "levels": {
        "L{}".format(L): {
            "n_dof": ctx[L]["n"],
            "lam_min": fmt(ctx[L]["lam_min"]),
            "dq_minus": fmt(meas[L]["dq"][1]),
            "dq_plus": fmt(meas[L]["dq"][15]),
            "coset_spread": fmt(max(meas[L]["spread"].values())),
            "cocycle_worst": fmt(meas[L]["coc_worst"]),
            "cocycle_pairs": meas[L]["coc_pairs"],
            "wrong_frame": fmt(meas[L]["wrong"]),
            "reversed_order": fmt(meas[L]["rev"]),
            "laws": {"g{}".format(g): {"resid": fmt(v["resid"]),
                                       "cos": fmt(v["cos"]),
                                       "floor": fmt(v["den"])}
                     for g, v in meas[L]["laws"].items()},
            "floor_spread": fmt(meas[L]["floor_spread"]),
            "mixed_emax": fmt(meas[L]["mixed_emax"]),
            "mixed_offset": fmt(abs(meas[L]["mixed_emax"] - 4.0)),
            "mixed_sep": fmt(meas[L]["mixed_emax"] / meas[L]["dq"][1]),
            "mixed_law_resid": fmt(meas[L]["mixed_law"]),
            "mixed_law_frame": meas[L]["mixed_law_frame"],
        } for L in L_LIST
    },
    "total": {"PASS": PASS, "FAIL": FAIL},
}
outdir = HERE.parent / "outputs"
outdir.mkdir(exist_ok=True)
with open(outdir / RECEIPT_NAME, "w") as fh:
    json.dump(receipt, fh, indent=2, sort_keys=True)
    fh.write("\n")
print("RECEIPT: outputs/" + RECEIPT_NAME)
print("TOTAL: PASS={} FAIL={}".format(PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
