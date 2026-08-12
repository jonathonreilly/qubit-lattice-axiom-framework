"""Cycle 716 -- finite classification of frame-blind averaging sets.

Class-A finite check script (stdlib + numpy only).  It executes the landed Cycle-696
open-coframe endpoint compiler chain to assemble the static operator, relabels it by
each of the 24 proper rotations, and then answers ONE question completely: for which
collections A of frames does averaging a source over A erase the frame dependence of
the reassembled operator's pairing?

Cycle 715 answered this for A a SUBGROUP, by a counting identity.  Here A ranges over
every one of the 16777215 nonempty collections, and the subgroup hypothesis is removed.

The derivation this script measures.  Write b for the source, P_a for the relabelling
of frame a, and

    bbar_A = sum over a in A of transpose(P_a) b,   v_A(g) = <bbar_A, inverse(Q_g) bbar_A>
             / <bbar_A, bbar_A>.

Relabelling composes as an anti-homomorphism, P_a P_b = P_{ba}.  Define the LEFT
stabilizer L(A) = {t : tA = A}; it is a subgroup, and A is a union of right cosets of
L(A), so the order of L(A) divides the size of A.  Since transpose(P_t) bbar_A =
bbar_{tA} = bbar_A for t in L(A), and since the operator is unchanged by the sextet S,
every g in the product set S L(A) gives the same value of v_A.  Hence

    S L(A) = whole group  ==>  v_A is constant  (sufficiency, for EVERY source).

Gates:

  G1  the group layer: sextet, subgroup lattice, covering subgroups, complements, the
      24 minimum-size covering-family members, and the family they generate;
  G2  the same family recovered from the left-stabilizer criterion alone, evaluated
      combinatorially on all 16777215 collections;
  G3  the four-representative screen: its representatives are a four-coset
      transversal and therefore a subset of the 24 frames; a bounded comparison
      sample is carried as a consistency check, not as a proof of reduction;
  G4  sufficiency on the nonvanishing-average domain, on five supplied sources and
      two box sizes, for all 231 predicted members;
  G5  complete finite scans of all 16777215 collections at four declared seeded
      standard-normal inputs (two base seeds at each of two box sizes), with every
      screen acceptance re-tested on all 24 frames;
  G6  finite rejector witnesses at the first seeded input;
  G7  finite structured-source witnesses showing that the seeded-scan counts are not
      source-independent;
  G8  a zero-average hostile witness: the normalized response is undefined and must
      return a non-passing NaN rather than be classified as blind.

The exact group statements are conditional on the measured sextet returned by the
supplied compiler.  The full-powerset response counts are finite statements at the four
declared seeded inputs only; they do not establish a generic-source theorem.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import math
import sys
from collections import Counter
from pathlib import Path

import numpy as np

AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 900

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c716", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
DIRS = c696.regge.DIRS15
CLASS_OF = {}
for _c in c696.SPATIAL_CLASSES:
    CLASS_OF[tuple(int(abs(int(t))) for t in DIRS[_c][:3])] = _c

WRAP = False
L_LIST = (3, 4)
NDOF = {3: 98, 4: 279}
SEXTET_EXPECTED = (1, 4, 9, 15, 18, 23)
GENERIC_SEEDS = (7160, 7161)
TOL_BLIND = 1e-8
TOL_STAB = 1e-9
TOL_REDUCE = 1e-8
TOL_ZERO_NORM = 1e-12
SEP_MIN = 1e3
NORM_MIN = 1.0
BLOCK = 20000
KMAX_BOUNDARY = 8
NALL = (1 << 24) - 1
# the full size ladder the complete scan must reproduce: the stated counts on the
# quarter sizes AND zero on every one of the eighteen sizes in between.
LADDER = [(k, {4: 24, 8: 51, 12: 80, 16: 51, 20: 24, 24: 1}.get(k, 0))
          for k in range(1, 25)]

RECEIPT_NAME = ("physical_complete_averaging_set_frame_blindness_classification_cycle716"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.1e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  Every gate below is discriminating: each carries an
    explicit wrong-set, wrong-order, wrong-family, or absent-law rejector."""
    global N_PASS, N_FAIL
    ok = bool(ok)
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES[name] = {"pass": ok, "detail": detail}
    print("{} {} {}".format("PASS" if ok else "FAIL", name, detail))
    return ok


# ---------------------------------------------------------------------------
# frame group layer (written here, not imported from a probe)
# ---------------------------------------------------------------------------
def mul_table():
    keyed = {tuple(f.ravel().tolist()): i for i, f in enumerate(FRAMES)}
    M = np.zeros((24, 24), dtype=np.int64)
    for a in range(24):
        for b in range(24):
            M[a, b] = keyed[tuple((FRAMES[a] @ FRAMES[b]).ravel().tolist())]
    return M


MUL = mul_table()
IDENT = [i for i in range(24) if np.array_equal(FRAMES[i], np.eye(3, dtype=np.int64))][0]


def prod_set(A, B):
    return frozenset(int(MUL[a][b]) for a in A for b in B)


def closure(gens):
    H = set(gens) | {IDENT}
    changed = True
    while changed:
        changed = False
        for a in list(H):
            for b in list(H):
                p = int(MUL[a][b])
                if p not in H:
                    H.add(p)
                    changed = True
    return frozenset(H)


def relabel(L, g):
    """Index permutation induced on the static variables by proper rotation g."""
    idx = c696.static_variable_index(L, WRAP)
    smap = c696.frame_site_map(L, FRAMES[g])
    m = np.zeros(len(idx), dtype=np.int64)
    for (c, x), i in idx.items():
        w = FRAMES[g] @ np.asarray(DIRS[c][:3], dtype=np.int64)
        site = np.asarray(smap[x], dtype=np.int64) + np.minimum(w, 0)
        m[i] = idx[(CLASS_OF[tuple(int(abs(int(t))) for t in w)],
                    tuple(int(t) for t in site))]
    return m


def build_ctx(L):
    Q = c696.assemble_static_hessian(L, WRAP)["Q"]
    n = int(Q.shape[0])
    perms = [relabel(L, g) for g in range(24)]
    QG = [Q[np.ix_(perms[g], perms[g])] for g in range(24)]
    dev = [float(np.abs(QG[g] - Q).max()) for g in range(24)]
    S = tuple(sorted(g for g in range(24) if dev[g] < TOL_STAB))
    seen, reps = set(), []
    for g in range(24):
        cs = frozenset(int(MUL[s][g]) for s in S)
        if cs not in seen:
            seen.add(cs)
            reps.append(g)
    return {"L": L, "Q": Q, "n": n, "perms": perms, "QG": QG, "S": S,
            "reps": reps, "scale": float(np.abs(Q).max()),
            "QI4": [np.linalg.inv(QG[g]) for g in reps],
            "QI24": [np.linalg.inv(QG[g]) for g in range(24)]}


def sources(ctx):
    """Five supplied probes: two declared seeded draws and three structured inputs."""
    n = ctx["n"]
    out = []
    for seed in GENERIC_SEEDS:
        rg = np.random.default_rng(seed + ctx["L"])
        out.append(("seeded-normal-base-{}".format(seed), rg.standard_normal(n)))
    out.append(("unit-slot0", np.eye(n)[0]))
    out.append(("unit-slot7", np.eye(n)[7]))
    out.append(("all-ones", np.ones(n)))
    return out


def pulled(ctx, b):
    """The 24 pulled-back sources transpose(P_a) b, stacked."""
    return np.stack([b[np.argsort(ctx["perms"][a])] for a in range(24)])


def spread_of(A, bp, QIs):
    v = np.zeros(bp.shape[1])
    for a in A:
        v = v + bp[a]
    nrm = float(np.linalg.norm(v))
    if nrm <= TOL_ZERO_NORM:
        return float("nan"), nrm
    v = v / nrm
    vals = [float(v @ Qi @ v) for Qi in QIs]
    return max(vals) - min(vals), nrm


def scan_sizes(bp, QIs, kmax, collect=True):
    """Complete scan over every collection of size 1..kmax.  Returns the measured blind
    family (when collect is set), its size histogram, the worst blind spread, the best
    non-blind spread, the smallest norm of the averaged source encountered, and the
    number of degenerate normalized responses.  A zero average is undefined and belongs
    to neither population.  With collect off only the counts are kept, so a
    source that is blind almost everywhere does not have to be materialised."""
    measured = set()
    by_size = Counter()
    worst_blind, best_non, minnorm, degenerate = (
        0.0, float("inf"), float("inf"), 0
    )
    for k in range(1, kmax + 1):
        it = itertools.combinations(range(24), k)
        while True:
            block = list(itertools.islice(it, BLOCK))
            if not block:
                break
            idx = np.array(block, dtype=np.int64)
            B = bp[idx[:, 0]].copy()
            for j in range(1, k):
                B += bp[idx[:, j]]
            nrm = np.linalg.norm(B, axis=1)
            minnorm = min(minnorm, float(nrm.min()))
            valid = nrm > TOL_ZERO_NORM
            degenerate += int((~valid).sum())
            B /= np.where(valid, nrm, 1.0)[:, None]
            V = np.stack([np.einsum("ij,jk,ik->i", B, Qi, B, optimize=True)
                          for Qi in QIs], axis=1)
            sp = V.max(axis=1) - V.min(axis=1)
            hit = np.flatnonzero(valid & (sp < TOL_BLIND))
            by_size[k] += int(hit.size)
            if collect:
                for h in hit:
                    measured.add(frozenset(int(t) for t in idx[h]))
            if hit.size:
                worst_blind = max(worst_blind, float(sp[hit].max()))
            keep = valid & (sp >= TOL_BLIND)
            if keep.any():
                best_non = min(best_non, float(sp[keep].min()))
    return (measured, sorted(by_size.items()), worst_blind, best_non, minnorm,
            degenerate)


# ---------------------------------------------------------------------------
# G1 -- the group layer
# ---------------------------------------------------------------------------
def group_layer(S):
    Sset = frozenset(S)
    # Exhaust the subgroup lattice constructively.  Starting from {e}, adjoining
    # every group element to every subgroup already found reaches every finitely
    # generated subgroup without assuming a bound on generating rank.
    subs = {frozenset({IDENT})}
    frontier = list(subs)
    while frontier:
        H = frontier.pop()
        for g in range(24):
            K = closure(set(H) | {g})
            if K not in subs:
                subs.add(K)
                frontier.append(K)
    subs = sorted(subs, key=lambda h: (len(h), sorted(h)))
    covering = [H for H in subs if len(prod_set(Sset, H)) == 24]
    comps = [H for H in covering if len(H) == 4]
    noncov4 = [H for H in subs if len(H) == 4 and H not in covering]
    minimal = sorted({frozenset(int(MUL[h][a]) for h in H) for H in comps
                      for a in range(24)}, key=lambda c: sorted(c))
    left = {frozenset(int(MUL[a][h]) for h in H) for H in comps for a in range(24)}
    family = set()
    for H in covering:
        cos = sorted({frozenset(int(MUL[h][a]) for h in H) for a in range(24)},
                     key=lambda c: sorted(c))
        for r in range(1, len(cos) + 1):
            for pick in itertools.combinations(cos, r):
                family.add(frozenset().union(*pick))
    return {"subs": subs, "covering": covering, "comps": comps, "noncov4": noncov4,
            "minimal": minimal, "left": left, "family": family, "Sset": Sset}


def run_group_layer(gl, S):
    Sset = gl["Sset"]
    check("g1_sextet_identity",
          tuple(S) == SEXTET_EXPECTED and len(S) == 6 and closure(S) == Sset,
          "S {} order {} closed".format(list(S), len(S)))
    check("g1_sextet_right_coset_count",
          len({frozenset(int(MUL[s][g]) for s in Sset) for g in range(24)}) == 4,
          "index 4 = 24 over 6")
    check("g1_subgroup_lattice", len(gl["subs"]) == 30,
          "complete lattice by closure {}".format(len(gl["subs"])))
    orders = sorted(len(H) for H in gl["covering"])
    check("g1_covering_subgroups", len(gl["covering"]) == 9
          and orders == [4, 4, 4, 4, 8, 8, 8, 12, 24],
          "orders {}".format(orders))
    check("g1_complements", len(gl["comps"]) == 4
          and all(len(H & Sset) == 1 for H in gl["comps"]),
          "4 complements meeting S in the identity alone")
    check("g1_noncovering_order4_witness", len(gl["noncov4"]) == 3
          and all(len(H & Sset) == 2 and len(prod_set(Sset, H)) == 12
                  for H in gl["noncov4"]),
          "3 order-4 subgroups meet S twice, cover 12 of 24")
    check("g1_minimal_covering_family_members", len(gl["minimal"]) == 24
          and all(len(A) == 4 for A in gl["minimal"]),
          "24 size-4 right cosets of the complements")
    check("g1_left_family_equals_right_family", gl["left"] == set(gl["minimal"]),
          "left and right coset families coincide as sets")
    check("g1_covering_contains_complement",
          all(any(C <= H for C in gl["comps"]) for H in gl["covering"]),
          "every covering subgroup contains a complement")
    hist = sorted(Counter(len(A) for A in gl["family"]).items())
    check("g1_family_size_and_histogram", len(gl["family"]) == 231
          and hist == [(4, 24), (8, 51), (12, 80), (16, 51), (20, 24), (24, 1)],
          "231 members, by size {}".format(hist))
    quarters = sorted({len(A) // 4 * 4 == len(A) for A in gl["family"]})
    check("g1_sizes_are_multiples_of_four", quarters == [True]
          and min(len(A) for A in gl["family"]) == 4,
          "family size support [4, 8, 12, 16, 20, 24], minimum 4")
    decomposes = all(A == frozenset().union(frozenset(),
                                            *[M for M in gl["minimal"] if M <= A])
                     for A in gl["family"])
    check("g1_family_generated_by_minimal", decomposes,
          "every member is a union of minimal covering-family members")
    pairs = [(i, j) for i in range(24) for j in range(i + 1, 24)
             if not (gl["minimal"][i] & gl["minimal"][j])]
    outside = [(i, j) for (i, j) in pairs
               if (gl["minimal"][i] | gl["minimal"][j]) not in gl["family"]]
    check("g1_family_not_union_closed", len(pairs) == 168 and len(outside) == 108,
          "{} disjoint minimal pairs, {} unions outside the family".format(
              len(pairs), len(outside)))
    NOTES["example_disjoint_pair_with_union_outside_family"] = [
        sorted(gl["minimal"][outside[0][0]]), sorted(gl["minimal"][outside[0][1]])]
    overlap = [(i, j) for i in range(24) for j in range(i + 1, 24)
               if gl["minimal"][i] & gl["minimal"][j]]
    check("g1_minimal_cover_overlaps", len(overlap) == 108,
          "108 of 276 pairs overlap")


# ---------------------------------------------------------------------------
# G2 -- the left-stabilizer criterion on the complete powerset
# ---------------------------------------------------------------------------
def stabilizer_classification(gl):
    """Evaluate S L(A) = whole group for every one of the 16777215 nonempty A, using
    a bitmask representation of the powerset."""
    T = np.zeros((24, 3, 256), dtype=np.uint32)
    for t in range(24):
        for blk in range(3):
            for val in range(256):
                acc = 0
                for bit in range(8):
                    if val & (1 << bit):
                        acc |= 1 << int(MUL[t][blk * 8 + bit])
                T[t, blk, val] = acc
    masks = np.arange(1 << 24, dtype=np.uint32)
    b0 = (masks & np.uint32(0xFF)).astype(np.uint8)
    b1 = ((masks >> np.uint32(8)) & np.uint32(0xFF)).astype(np.uint8)
    b2 = ((masks >> np.uint32(16)) & np.uint32(0xFF)).astype(np.uint8)
    stab = np.zeros(1 << 24, dtype=np.uint32)
    for t in range(24):
        img = T[t, 0][b0] | T[t, 1][b1] | T[t, 2][b2]
        stab |= np.where(img == masks, np.uint32(1 << t), np.uint32(0))
    del b0, b1, b2, img
    sub_of = {int(sum(1 << h for h in H)): H for H in gl["subs"]}
    cov_of = {m: (len(prod_set(gl["Sset"], H)) == 24) for m, H in sub_of.items()}
    uniq = [int(u) for u in np.unique(stab)]
    all_subgroups = all(u in sub_of for u in uniq)
    is_blind = np.zeros(1 << 24, dtype=bool)
    for u in uniq:
        if cov_of.get(u, False):
            is_blind |= (stab == np.uint32(u))
    is_blind[0] = False
    picked = [int(m) for m in masks[is_blind]]
    got = {frozenset(a for a in range(24) if m & (1 << a)) for m in picked}
    del masks, stab, is_blind
    return {"got": got, "all_subgroups": all_subgroups, "n_stab_values": len(uniq)}


def run_stabilizer_layer(gl):
    res = stabilizer_classification(gl)
    check("g2_stabilizers_are_subgroups", res["all_subgroups"],
          "every left stabilizer over the complete powerset lies in the "
          "{}-member lattice, {} distinct values".format(len(gl["subs"]),
                                                         res["n_stab_values"]))
    check("g2_criterion_recovers_family", res["got"] == gl["family"],
          "S L(A) = whole group holds for exactly {} of 16777215 collections".format(
              len(res["got"])))
    # order of L(A) divides the size of A, and is at least 4 on the family
    orders = []
    for A in gl["family"]:
        LA = frozenset(t for t in range(24)
                       if frozenset(int(MUL[t][a]) for a in A) == A)
        orders.append((len(LA), len(A)))
    check("g2_stabilizer_order_divides_size",
          all(sz // o * o == sz for o, sz in orders) and min(o for o, _ in orders) >= 4,
          "order of L(A) divides size of A on all 231, minimum order {}".format(
              min(o for o, _ in orders)))
    return res


# ---------------------------------------------------------------------------
# G3-G7 -- the measured layer, per box size
# ---------------------------------------------------------------------------
def run_L(ctx, gl):
    L = ctx["L"]
    tag = "L{}".format(L)
    check("g3_{}_dof_and_scale".format(tag), ctx["n"] == NDOF[L],
          "n {} scale {}".format(ctx["n"], fmt(ctx["scale"])))
    check("g3_{}_sextet_recovered".format(tag), tuple(ctx["S"]) == SEXTET_EXPECTED,
          "S {} at tol {}".format(list(ctx["S"]), fmt(TOL_STAB)))

    # The four representative values form a monotone screen because the selected
    # representatives are a literal subset of the 24 frames.  Agreement below is
    # only a bounded consistency sample; every screen acceptance is separately
    # retested against all 24 frames in G5.
    reps_ok = (len(ctx["reps"]) == 4 and len(set(ctx["reps"])) == 4
               and all(0 <= r < 24 for r in ctx["reps"])
               and len(ctx["QI4"]) == len(ctx["reps"]))
    check("g3_{}_screening_premise".format(tag), reps_ok,
          "four distinct frame representatives {} are a subset of the 24".format(
              ctx["reps"]))
    b = sources(ctx)[0][1]
    bp = pulled(ctx, b)
    worst_red = 0.0
    for k in (1, 2, 3):
        for A in itertools.combinations(range(24), k):
            s4, _ = spread_of(A, bp, ctx["QI4"])
            s24, _ = spread_of(A, bp, ctx["QI24"])
            worst_red = max(worst_red, abs(s4 - s24))
    check("g3_{}_four_representative_sample".format(tag), worst_red < TOL_REDUCE,
          "bounded consistency sample: worst deviation {} over 2324 collections"
          " of size at most 3".format(
              fmt(worst_red)))

    # G4 sufficiency, all five sources, all 231 predicted members
    worst_suf, minnorm_suf = 0.0, float("inf")
    for name, src in sources(ctx):
        sp = pulled(ctx, src)
        for A in gl["family"]:
            s, nrm = spread_of(A, sp, ctx["QI24"])
            worst_suf = max(worst_suf, s)
            minnorm_suf = min(minnorm_suf, nrm)
    check("g4_{}_sufficiency_supplied_sources".format(tag), worst_suf < TOL_BLIND
          and minnorm_suf > NORM_MIN,
          "231 members x 5 supplied inputs on the nonzero-average domain, worst "
          "spread {} smallest norm {}".format(
              fmt(worst_suf), fmt(minnorm_suf)))

    # G5 complete finite scans at the four declared seeded standard-normal inputs.
    for name, src in sources(ctx)[:2]:
        sp = pulled(ctx, src)
        got, hist, wb, bn, mn, nd = scan_sizes(sp, ctx["QI4"], 24)
        sep = bn / wb if wb > 0.0 else float("inf")
        check("g5_{}_{}_finite_scan_family".format(tag, name), got == gl["family"],
              "{} collections, {} classified blind, covering-family match {}".format(
                  NALL, len(got), got == gl["family"]))
        check("g5_{}_{}_separation".format(tag, name),
              sep > SEP_MIN and mn > NORM_MIN and nd == 0,
              "worst blind {} best non-blind {} ratio {} smallest norm {} "
              "degenerate {}".format(fmt(wb), fmt(bn), fmt(sep), fmt(mn), nd))
        check("g5_{}_{}_size_census".format(tag, name), hist == LADDER,
              "counts by size {}".format(hist))
        all24 = [spread_of(A, sp, ctx["QI24"])[0] for A in got]
        check("g5_{}_{}_all_24_acceptance".format(tag, name),
              len(all24) == len(gl["family"])
              and all(math.isfinite(s) and s < TOL_BLIND for s in all24),
              "all {} screen acceptances retested on all 24 frames; worst spread {}"
              .format(len(all24), fmt(max(all24) if all24 else float("inf"))))

    # G6 finite named witnesses at the first seeded input.
    bp0 = pulled(ctx, sources(ctx)[0][1])
    s_sextet, _ = spread_of(ctx["S"], bp0, ctx["QI24"])
    check("g6_{}_sextet_spread_witness".format(tag), s_sextet > TOL_BLIND,
          "the sextet spread is {} at this input".format(fmt(s_sextet)))
    subset = (1, 4, 9, 23)
    s_sub, _ = spread_of(subset, bp0, ctx["QI24"])
    check("g6_{}_non_subgroup_subset_spread_witness".format(tag),
          s_sub > TOL_BLIND,
          "subset {} spread is {} at this input".format(list(subset), fmt(s_sub)))
    worst_nc = float("inf")
    for H in gl["noncov4"]:
        for a in range(24):
            s, _ = spread_of(frozenset(int(MUL[h][a]) for h in H), bp0, ctx["QI24"])
            worst_nc = min(worst_nc, s)
    check("g6_{}_noncovering_coset_spread_witness".format(tag),
          worst_nc > TOL_BLIND,
          "72 cosets of 3 noncovering order-4 subgroups, least spread {}".format(
              fmt(worst_nc)))


def run_boundary(ctx, gl):
    """G7 -- finite structured-source existence witnesses."""
    L = ctx["L"]
    tag = "L{}".format(L)
    pred8 = {A for A in gl["family"] if len(A) <= KMAX_BOUNDARY}
    nsmall = sum(math.comb(24, k) for k in range(1, KMAX_BOUNDARY + 1))
    counts, small = {}, {}
    for name, src in sources(ctx)[2:]:
        sp = pulled(ctx, src)
        got, hist, wb, bn, mn, nd = scan_sizes(
            sp, ctx["QI4"], KMAX_BOUNDARY, collect=(name != "all-ones")
        )
        counts[name] = sum(c for _, c in hist)
        small[name] = sum(c for k, c in hist if k < 4)
        if name == "all-ones":
            orbit = max(float(np.linalg.norm(sp[a] - sp[0])) for a in range(24))
            check("g7_{}_all_ones_orbit_is_one_point".format(tag),
                  orbit < TOL_BLIND and counts[name] == nsmall,
                  "orbit diameter {} blind on all {} collections".format(
                      fmt(orbit), counts[name]))
        else:
            check("g7_{}_{}_additional_blind_witnesses".format(tag, name),
                  got > pred8,
                  "{} blind of {} at size at most {}, family contributes {}, counts "
                  "by occupied sizes {}, counts below size 4 {}".format(
                      counts[name], nsmall, KMAX_BOUNDARY, len(pred8),
                      [k for k, c in hist if c], [(k, c) for k, c in hist if c and k < 4]))
        NOTES["boundary_{}_{}".format(tag, name)] = {
            "blind": counts[name], "worst_blind": fmt(wb), "best_non_blind": fmt(bn),
            "min_norm": fmt(mn), "degenerate": nd}
    check("g7_{}_boundary_ordering".format(tag),
          counts["unit-slot7"] > counts["unit-slot0"] > len(pred8),
          "structured blind counts {} and {} against family {}".format(
              counts["unit-slot7"], counts["unit-slot0"], len(pred8)))
    check("g7_{}_size_two_blind_witness".format(tag),
          small["unit-slot7"] > 0 and small["unit-slot0"] == 0,
          "unit-slot7 has {} blind collections below size 4 in this scan; "
          "unit-slot0 has {}".format(small["unit-slot7"], small["unit-slot0"]))


def run_zero_average_domain(ctx):
    """G8 -- a nonzero input whose full-group average vanishes."""
    b = np.zeros(ctx["n"])
    b[0] = 1.0
    b[35] = -1.0
    spread, norm = spread_of(range(24), pulled(ctx, b), ctx["QI24"])
    check("g8_zero_average_domain_is_nonpassing",
          norm <= TOL_ZERO_NORM and math.isnan(spread),
          "nonzero e0-e35 input, full-group average norm {}, spread {}".format(
              fmt(norm), spread))


def main() -> int:
    print("c716 finite classification of frame-blind averaging sets")
    ctxs = {L: build_ctx(L) for L in L_LIST}
    gl = group_layer(ctxs[L_LIST[0]]["S"])
    print("-- group layer --")
    run_group_layer(gl, ctxs[L_LIST[0]]["S"])
    print("-- left-stabilizer criterion on the complete powerset --")
    run_stabilizer_layer(gl)
    for L in L_LIST:
        print("-- L={} --".format(L))
        run_L(ctxs[L], gl)
    print("-- boundary (structured sources) --")
    run_boundary(ctxs[L_LIST[0]], gl)
    print("-- zero-average domain witness --")
    run_zero_average_domain(ctxs[L_LIST[0]])

    receipt = {"blind_family_size": len(gl["family"]),
               "box_sizes": list(L_LIST),
               "collections_scanned": NALL,
               "covering_orders": sorted(len(H) for H in gl["covering"]),
               "fail": N_FAIL,
               "gates": GATES,
               "minimal_covering_family_members": len(gl["minimal"]),
               "notes": NOTES,
               "pass": N_PASS,
               "runner": Path(__file__).name,
               "sextet": list(SEXTET_EXPECTED),
               "subgroup_lattice": len(gl["subs"]),
               "tolerance": fmt(TOL_BLIND),
               "zero_norm_tolerance": fmt(TOL_ZERO_NORM)}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")

    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
