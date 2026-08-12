"""Cycle 717 -- finite body-diagonal action and transversal probe census.

Class-A finite check script (stdlib + numpy only).  It executes the landed Cycle-696
open-coframe endpoint compiler chain, relabels the assembled static operator by each of
the 24 proper rotations, and identifies the invariant that the operator actually depends
on.

The exact layer identifies the body-diagonal action of the supplied 24 proper rotations
and derives the 231-member covering-criterion sufficient family.  The numerical layer
measures operator clustering and transversal blindness at L=3,4 for explicitly named
sources.  It does not claim a source-independent converse or a universal minimum blind
set: structured unit sources below furnish additional blind transversals.

The derivation this script measures.  The four body diagonals of the cubic cell,

    d0 = (1, 1, 1),  d1 = (1, 1, -1),  d2 = (1, -1, 1),  d3 = (-1, 1, 1),

each taken up to overall sign, carry an action of the 24 proper rotations.  That action
is faithful and realises every permutation of the four.  The stabiliser of a single
diagonal therefore has order six.  On the two measured boxes, the numerical sextet of
frames that fixes the assembled static operator is the stabiliser of d0.  Writing

    delta(g) = the body diagonal that g carries onto d0,

the fibres of delta are precisely the right cosets of the sextet.  The numerical
operator clusters depend on the frame only through delta on the measured boxes.  This
is a statement about an axis of the rotation group; the adjacency stencil is untouched
and remains nearest-neighbour.

Two consequences follow, and both are checked here against direct measurement:

  (a) a subgroup H fills the group against the sextet exactly when H acts transitively
      on the four body diagonals, so the covering subgroups are the transitive ones,
      the minimal ones are the four regular ones, and the minimum covering-subgroup
      order is four -- a transitive group on four points has order divisible by four;

  (b) the census of the covering-criterion sufficient family is not a measured number.
      Every transitive subgroup contains a regular one, so the family is the union of four
      coset families of size 63, and inclusion and exclusion over their joins gives
      4*63 - (3*7 + 3*1) + 4*1 - 1 = 231.

For each of two seeded normal vectors at each size, exactly 24 of the 1296 transversals
are blind, namely the right cosets of the four regular subgroups.  This seeded converse
is not source-robust: unit-slot counterexamples add blind transversals at both sizes.

Read inventory.  The Cycle-696 compiler and its four transitive imports are the only
load-bearing repository inputs and are declared in AUDIT_INPUT_PATHS.  Every reported
number is recomputed in this run; the only package-local write is the paired receipt.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c717", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)
AUDIT_TIMEOUT_SEC = 300

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
DIRS = c696.regge.DIRS15
CLASS_OF = {}
for _c in c696.SPATIAL_CLASSES:
    CLASS_OF[tuple(int(abs(int(t))) for t in DIRS[_c][:3])] = _c

WRAP = False
L_LIST = (3, 4)
EXPECTED_LT = 2
EXPECTED_FD_H = 1.0e-4
EXPECTED_SPATIAL_CLASSES = 7
NDOF = {3: 98, 4: 279}
SEXTET_EXPECTED = (1, 4, 9, 15, 18, 23)
DIAGONALS = ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))
GENERIC_SEEDS = (7170, 7171)
TOL_BLIND = 1e-8
TOL_STAB = 1e-9
SEP_MIN = 1e3
NORM_MIN = 1.0
TOL_ZERO_NORM = 1e-12
N_TRANSVERSALS = 6 ** 4
BLIND_TRANSVERSALS = 24
LADDER = [(4, 24), (8, 51), (12, 80), (16, 51), (20, 24), (24, 1)]

RECEIPT_NAME = ("physical_body_diagonal_frame_functional_transversal_law_cycle717"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.1e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  Every gate below is discriminating: each carries an
    explicit wrong-axis, wrong-order, wrong-family, or absent-law rejector."""
    global N_PASS, N_FAIL
    ok = bool(ok)
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES[name] = {"pass": ok, "detail": detail}
    print("{} {} {}".format("PASS" if ok else "FAIL", name, detail))
    return ok


def run_input_layer():
    """Reject direct execution on a silently changed compiler configuration."""
    check("g0_compiler_configuration",
          c696.LT == EXPECTED_LT and c696.FD_H == EXPECTED_FD_H
          and len(c696.SPATIAL_CLASSES) == EXPECTED_SPATIAL_CLASSES
          and len(FRAMES) == len({tuple(f.ravel()) for f in FRAMES}) == 24,
          "LT {} FD_H {} spatial classes {} distinct frames {}".format(
              c696.LT, c696.FD_H, len(c696.SPATIAL_CLASSES),
              len({tuple(f.ravel()) for f in FRAMES})))


# ---------------------------------------------------------------------------
# frame group layer
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


def diag_key(v):
    t = tuple(int(x) for x in v)
    return t if t[0] > 0 else tuple(-x for x in t)


DIAG_ID = {diag_key(d): j for j, d in enumerate(DIAGONALS)}


def diag_perm(g):
    """The permutation of the four body diagonals induced by frame g."""
    return tuple(DIAG_ID[diag_key(FRAMES[g] @ np.asarray(d, dtype=np.int64))]
                 for d in DIAGONALS)


def delta(g):
    """The body diagonal that frame g carries onto d0."""
    return DIAG_ID[diag_key(FRAMES[g].T @ np.asarray(DIAGONALS[0], dtype=np.int64))]


PERM4 = [diag_perm(g) for g in range(24)]
DELTA = [delta(g) for g in range(24)]
FIBRE = {j: tuple(sorted(g for g in range(24) if DELTA[g] == j)) for j in range(4)}


def subgroup_lattice():
    """Enumerate the complete subgroup lattice by closure expansion.

    This does not assume a bound on the size of a generating set: every discovered
    subgroup is expanded by adjoining each group element until no new closure occurs.
    """
    identity = frozenset({IDENT})
    subs = {identity}
    pending = [identity]
    while pending:
        H = pending.pop()
        for g in range(24):
            K = closure(set(H) | {g})
            if K not in subs:
                subs.add(K)
                pending.append(K)
    return sorted(subs, key=lambda H: (len(H), sorted(H)))


def transitive(H):
    return len({DELTA[h] for h in H}) == 4


def regular(H):
    return len(H) == 4 and transitive(H)


def right_cosets(H):
    return {frozenset(int(MUL[h][a]) for h in H) for a in range(24)}


# ---------------------------------------------------------------------------
# physical layer
# ---------------------------------------------------------------------------
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
    return {"L": L, "Q": Q, "n": n, "perms": perms, "QG": QG, "S": S,
            "scale": float(np.abs(Q).max()),
            "QI": [np.linalg.inv(QG[g]) for g in range(24)]}


def sources(ctx):
    out = []
    for seed in GENERIC_SEEDS:
        rg = np.random.default_rng(seed + ctx["L"])
        out.append(("generic-{}".format(seed), rg.standard_normal(ctx["n"])))
    out.append(("unit-slot0", np.eye(ctx["n"])[0]))
    out.append(("unit-slot1", np.eye(ctx["n"])[1]))
    out.append(("unit-slot7", np.eye(ctx["n"])[7]))
    out.append(("unit-slot8", np.eye(ctx["n"])[8]))
    out.append(("all-ones", np.ones(ctx["n"])))
    return out


def pulled(ctx, b):
    """The 24 pulled-back sources transpose(P_a) b, stacked."""
    return np.stack([b[np.argsort(ctx["perms"][a])] for a in range(24)])


def spread_of(A, bp, QIs):
    """Frame spread of the averaged pairing, and the norm of the averaged source."""
    v = bp[list(A)].sum(axis=0)
    nrm = float(np.linalg.norm(v))
    if nrm <= TOL_ZERO_NORM:
        return float("nan"), nrm
    v = v / nrm
    vals = [float(v @ Qi @ v) for Qi in QIs]
    return float(max(vals) - min(vals)), nrm


# ---------------------------------------------------------------------------
# G1 -- the diagonal action and the sextet
# ---------------------------------------------------------------------------
def run_diagonal_layer():
    check("g1_action_faithful_and_full",
          len(set(PERM4)) == 24 and len({tuple(sorted(p)) for p in PERM4}) == 1,
          "24 frames give all 24 permutations of the four body diagonals, faithfully")

    stabs = {j: tuple(sorted(g for g in range(24) if PERM4[g][j] == j)) for j in range(4)}
    others = [stabs[j] for j in (1, 2, 3)]
    check("g1_sextet_is_the_d0_stabiliser",
          stabs[0] == SEXTET_EXPECTED and all(s != SEXTET_EXPECTED for s in others)
          and all(len(s) == 6 for s in stabs.values()),
          "stabiliser of {} is {}, the other three differ".format(
              DIAGONALS[0], list(stabs[0])))

    S = set(SEXTET_EXPECTED)
    cosets = {frozenset(int(MUL[s][g]) for s in S) for g in range(24)}
    fibres = {frozenset(FIBRE[j]) for j in range(4)}
    check("g1_fibres_are_the_right_cosets",
          len(cosets) == 4 and cosets == fibres
          and all(len(FIBRE[j]) == 6 for j in range(4)),
          "four fibres of six, exactly the right cosets of the sextet")
    NOTES["fibre_sizes"] = [len(FIBRE[j]) for j in range(4)]
    return stabs[0]


# ---------------------------------------------------------------------------
# G2 -- covering is transitivity
# ---------------------------------------------------------------------------
def run_transitivity_layer():
    S = set(SEXTET_EXPECTED)
    subs = subgroup_lattice()
    cover = [H for H in subs if prod_set(S, H) == frozenset(range(24))]
    trans = [H for H in subs if transitive(H)]
    check("g2_lattice_and_covering_orders",
          len(subs) == 30 and [len(H) for H in cover] == [4, 4, 4, 4, 8, 8, 8, 12, 24],
          "complete subgroup lattice {}, covering orders {}".format(
              len(subs), [len(H) for H in cover]))
    check("g2_covering_is_transitivity",
          set(cover) == set(trans) and len(trans) == 9,
          "a subgroup fills the group against the sextet exactly when it is "
          "diagonal-transitive, {} of {}".format(len(trans), len(subs)))

    reg = [H for H in subs if regular(H)]
    orb4 = [H for H in subs if len(H) == 4 and not transitive(H)]
    orbs = sorted({len({PERM4[h][j] for h in H}) for H in orb4 for j in range(4)})
    check("g2_minimal_covering_are_regular",
          len(reg) == 4 and all(len({DELTA[h] for h in H}) == 4 for H in reg)
          and len(orb4) == 3 and orbs == [2],
          "the four minimal covering subgroups act simply transitively, the other "
          "three have diagonal orbits of size two")

    small = [H for H in subs if len(H) in (1, 2, 3, 6)]
    check("g2_minimum_transitive_order_is_four",
          len(small) > 0 and not any(transitive(H) for H in small)
          and min(len(H) for H in trans) == 4,
          "no subgroup of order 1, 2, 3 or 6 is transitive, so the minimum of four "
          "is forced")

    check("g2_every_covering_contains_a_regular",
          all(any(set(R) <= set(H) for R in reg) for H in cover),
          "every transitive subgroup contains a regular one")
    NOTES["covering_orders"] = [len(H) for H in cover]
    return subs, cover, reg, orb4


# ---------------------------------------------------------------------------
# G3 -- the census is derived
# ---------------------------------------------------------------------------
def run_census_layer(subs, cover, reg):
    fam_cover = set()
    for H in cover:
        cs = sorted(right_cosets(H), key=lambda c: sorted(c))
        for r in range(1, len(cs) + 1):
            for pick in itertools.combinations(cs, r):
                fam_cover.add(frozenset().union(*pick))
    fam_reg = set()
    for H in reg:
        cs = sorted(right_cosets(H), key=lambda c: sorted(c))
        for r in range(1, len(cs) + 1):
            for pick in itertools.combinations(cs, r):
                fam_reg.add(frozenset().union(*pick))
    check("g3_covering_and_regular_constructions_agree",
          fam_cover == fam_reg and len(fam_cover) == 231,
          "all-covering and four-regular constructions coincide, {} members".format(
              len(fam_cover)))

    joins = {}
    for i, j in itertools.combinations(range(4), 2):
        joins[(i, j)] = len(closure(set(reg[i]) | set(reg[j])))
    triples = {}
    for t in itertools.combinations(range(4), 3):
        triples[t] = len(closure(set().union(*[set(reg[k]) for k in t])))
    quad = len(closure(set().union(*[set(R) for R in reg])))
    check("g3_joins_of_the_regular_subgroups",
          sorted(joins.values()) == [8, 8, 8, 24, 24, 24]
          and sorted(triples.values()) == [24, 24, 24, 24] and quad == 24,
          "pairwise joins {}, triples {}, all four {}".format(
              sorted(joins.values()), sorted(triples.values()), quad))

    singles = sum(2 ** (24 // len(R)) - 1 for R in reg)
    pairs = sum(2 ** (24 // v) - 1 for v in joins.values())
    trip = sum(2 ** (24 // v) - 1 for v in triples.values())
    quads = 2 ** (24 // quad) - 1
    total = singles - pairs + trip - quads
    check("g3_inclusion_and_exclusion_gives_the_census",
          total == len(fam_cover) == 231
          and (singles, pairs, trip, quads) == (252, 24, 4, 1),
          "{} - {} + {} - {} = {}, matching the direct construction".format(
              singles, pairs, trip, quads, total))

    hist = sorted(Counter(len(A) for A in fam_cover).items())
    check("g3_size_ladder",
          hist == LADDER,
          "family by size {}".format(hist))

    proper = {A for A in fam_cover if len(A) < 24}
    comp = {frozenset(set(range(24)) - A) for A in proper}
    counts = [c for s, c in hist if s < 24]
    check("g3_family_is_complement_closed",
          comp == proper and counts == counts[::-1] and len(fam_cover) - len(proper) == 1,
          "an involution on the {} proper members, so the ladder reads the same in "
          "both directions".format(len(proper)))

    order8 = [H for H in cover if len(H) == 8]
    cos8 = set()
    for H in order8:
        cos8 |= right_cosets(H)
    eight = {A for A in fam_cover if len(A) == 8}
    exact4 = eight - cos8
    check("g3_size_eight_decomposition",
          len(cos8) == 9 and len(cos8 & eight) == 9 and len(exact4) == 42
          and len(cos8) + len(exact4) == 51,
          "size eight splits as {} order-eight cosets and {} two-coset unions".format(
              len(cos8), len(exact4)))
    NOTES["census"] = len(fam_cover)
    NOTES["ladder"] = hist
    return fam_cover


# ---------------------------------------------------------------------------
# G4 -- the operator is a function of the body diagonal
# ---------------------------------------------------------------------------
def run_operator_layer(ctx):
    L = ctx["L"]
    tag = "L{}".format(L)
    check("g4_{}_dof_and_scale".format(tag),
          ctx["n"] == NDOF[L] and ctx["scale"] > 1.0,
          "n {} scale {}".format(ctx["n"], fmt(ctx["scale"])))
    check("g4_{}_sextet_is_the_stabiliser".format(tag),
          ctx["S"] == SEXTET_EXPECTED and ctx["S"] == FIBRE[0],
          "frames fixing the operator at tol {} are {}, the stabiliser of {}".format(
              fmt(TOL_STAB), list(ctx["S"]), DIAGONALS[0]))

    same, cross = 0.0, None
    for g, h in itertools.combinations(range(24), 2):
        d = float(np.abs(ctx["QG"][g] - ctx["QG"][h]).max())
        if DELTA[g] == DELTA[h]:
            same = max(same, d)
        else:
            cross = d if cross is None else min(cross, d)
    ratio = cross / same if same > 0.0 else float("inf")
    check("g4_{}_operator_is_a_diagonal_function".format(tag),
          same < TOL_STAB and cross > 1.0 and ratio > SEP_MIN,
          "over 276 frame pairs, same-diagonal at most {}, cross-diagonal at least "
          "{}, ratio {}".format(fmt(same), fmt(cross), fmt(ratio)))
    NOTES.setdefault("operator_separation", {})[tag] = [fmt(same), fmt(cross)]


# ---------------------------------------------------------------------------
# G5 -- the transversal law
# ---------------------------------------------------------------------------
def transversals():
    return [frozenset(t) for t in itertools.product(*[FIBRE[j] for j in range(4)])]


def run_transversal_layer(ctx, reg, srcs, TV):
    L = ctx["L"]
    tag = "L{}".format(L)
    predicted = set()
    for R in reg:
        predicted |= right_cosets(R)
    check("g5_{}_transversal_count".format(tag),
          len(TV) == N_TRANSVERSALS and len(predicted) == BLIND_TRANSVERSALS
          and predicted <= set(TV),
          "{} collections meet each body diagonal once, {} are regular cosets".format(
              len(TV), len(predicted)))

    for name, b in srcs:
        if not name.startswith("generic"):
            continue
        bp = pulled(ctx, b)
        worst_blind, best_open, minnorm = 0.0, None, None
        measured = set()
        for A in TV:
            s, nrm = spread_of(A, bp, ctx["QI"])
            minnorm = nrm if minnorm is None else min(minnorm, nrm)
            if s < TOL_BLIND:
                measured.add(A)
                worst_blind = max(worst_blind, s)
            else:
                best_open = s if best_open is None else min(best_open, s)
        ratio = best_open / worst_blind if worst_blind > 0.0 else float("inf")
        check("g5_{}_{}_transversal_scan".format(tag, name),
              len(measured) == BLIND_TRANSVERSALS and measured == predicted
              and minnorm > NORM_MIN,
              "{} of {} transversals blind, exactly the regular cosets, least norm "
              "{}".format(len(measured), len(TV), fmt(minnorm)))
        check("g5_{}_{}_transversal_separation".format(tag, name),
              worst_blind < TOL_BLIND and best_open is not None and ratio > SEP_MIN,
              "worst blind {} best non-blind {} ratio {}".format(
                  fmt(worst_blind), fmt(best_open), fmt(ratio)))

        wc, bc = 0.0, None
        for A in TV:
            s, _ = spread_of(sorted(set(range(24)) - A), bp, ctx["QI"])
            if A in predicted:
                wc = max(wc, s)
            else:
                bc = s if bc is None else min(bc, s)
        complement_ratio = bc / wc if wc > 0.0 else float("inf")
        check("g5_{}_{}_complement_law".format(tag, name),
              wc < TOL_BLIND and bc is not None and complement_ratio > SEP_MIN,
              "complements of the {} blind are blind at {}, the other {} spread at "
              "least {}".format(len(predicted), fmt(wc), len(TV) - len(predicted),
                                fmt(bc)))


# ---------------------------------------------------------------------------
# G6 -- rejectors
# ---------------------------------------------------------------------------
def run_rejectors(ctx, orb4, reg, srcs, TV):
    tag = "L{}".format(ctx["L"])
    name, b = srcs[0]
    bp = pulled(ctx, b)

    s_fib, _ = spread_of(sorted(FIBRE[0]), bp, ctx["QI"])
    check("g6_{}_one_fibre_is_not_blind".format(tag),
          s_fib > TOL_BLIND,
          "the sextet lies inside one body diagonal and spreads {}".format(fmt(s_fib)))

    predicted = set()
    for R in [H for H in orb4]:
        predicted |= right_cosets(R)
    least = None
    for A in predicted:
        s, _ = spread_of(sorted(A), bp, ctx["QI"])
        least = s if least is None else min(least, s)
    check("g6_{}_intransitive_cosets_are_not_blind".format(tag),
          least is not None and least > TOL_BLIND and len(predicted) == 18
          and not any(A in set(TV) for A in predicted),
          "{} cosets of the three intransitive order-four subgroups, least spread "
          "{}".format(len(predicted), fmt(least)))

    reg_cos = set()
    for R in reg:
        reg_cos |= right_cosets(R)
    witness = next(A for A in TV if A not in reg_cos)
    s_w, _ = spread_of(sorted(witness), bp, ctx["QI"])
    check("g6_{}_a_non_coset_transversal_is_not_blind".format(tag),
          s_w > TOL_BLIND,
          "the transversal {} meets each diagonal once yet spreads {}".format(
              sorted(witness), fmt(s_w)))


# ---------------------------------------------------------------------------
# G7 -- boundary
# ---------------------------------------------------------------------------
def run_boundary(ctx, reg, srcs, TV):
    """Bound the seeded transversal observation with structured counterexamples."""
    tag = "L{}".format(ctx["L"])
    predicted = set()
    for R in reg:
        predicted |= right_cosets(R)
    expected = {
        3: {"unit-slot0": 24, "unit-slot1": 24, "unit-slot7": 24,
            "unit-slot8": 264, "all-ones": N_TRANSVERSALS},
        4: {"unit-slot0": 24, "unit-slot1": 72, "unit-slot7": 24,
            "unit-slot8": 24, "all-ones": N_TRANSVERSALS},
    }
    for name, b in srcs:
        if name.startswith("generic"):
            continue
        bp = pulled(ctx, b)
        diam = float(np.abs(bp - bp[0]).max())
        blind = set()
        for A in TV:
            spread, _ = spread_of(sorted(A), bp, ctx["QI"])
            if np.isfinite(spread) and spread < TOL_BLIND:
                blind.add(A)
        wanted = expected[ctx["L"]][name]
        if diam < TOL_STAB:
            check("g7_{}_{}_orbit_is_one_point".format(tag, name),
                  len(blind) == wanted == len(TV) and name == "all-ones",
                  "orbit diameter {}, all {} transversals blind".format(
                      fmt(diam), len(blind)))
        else:
            check("g7_{}_{}_finite_count".format(tag, name),
                  len(blind) == wanted and predicted <= blind and diam > TOL_STAB,
                  "orbit diameter {}, measured {}/{} blind transversals; the {} "
                  "regular cosets remain sufficient".format(
                      fmt(diam), len(blind), len(TV), len(predicted)))
        NOTES.setdefault("boundary", {})["{}_{}".format(tag, name)] = len(blind)

    if ctx["L"] == 3:
        # Exact integer kernel witness for the average over A={0,1,3,5}.  Its pulled
        # orbit is nontrivial, but the averaged source is exactly zero.  Such a set is
        # outside the normalized-pairing domain and must never be labelled blind.
        b = np.zeros(ctx["n"])
        for i, value in ((2, -1), (3, 1), (6, 1), (7, -1),
                         (10, 1), (11, -1), (14, -1), (15, 1)):
            b[i] = value
        bp = pulled(ctx, b)
        spread, nrm = spread_of((0, 1, 3, 5), bp, ctx["QI"])
        diam = float(np.abs(bp - bp[0]).max())
        check("g7_exact_zero_average_is_out_of_domain",
              nrm <= TOL_ZERO_NORM and np.isnan(spread) and diam > TOL_STAB,
              "nontrivial orbit diameter {}, average norm {}, spread is NaN".format(
                  fmt(diam), fmt(nrm)))
        NOTES["zero_average_witness"] = {
            "set": [0, 1, 3, 5], "norm": fmt(nrm), "orbit_diameter": fmt(diam),
            "classification": "outside normalized-pairing domain",
        }


# ---------------------------------------------------------------------------
def main():
    print("c717 finite body-diagonal action and transversal probe census")
    print("-- supplied compiler configuration --")
    run_input_layer()
    print("-- body diagonals and the sextet --")
    run_diagonal_layer()
    print("-- covering is transitivity --")
    subs, cover, reg, orb4 = run_transitivity_layer()
    print("-- the census is derived --")
    run_census_layer(subs, cover, reg)
    TV = transversals()
    for L in L_LIST:
        print("-- L={} --".format(L))
        ctx = build_ctx(L)
        srcs = sources(ctx)
        run_operator_layer(ctx)
        run_transversal_layer(ctx, reg, srcs, TV)
        run_rejectors(ctx, orb4, reg, srcs, TV)
        run_boundary(ctx, reg, srcs, TV)
    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))

    receipt = {
        "runner": Path(__file__).name,
        "verdict": "PASS" if N_FAIL == 0 else "FAIL",
        "pass": N_PASS,
        "fail": N_FAIL,
        "box_sizes": list(L_LIST),
        "compiler_configuration": {
            "LT": c696.LT, "FD_H": c696.FD_H,
            "spatial_classes": len(c696.SPATIAL_CLASSES), "wrap": WRAP,
        },
        "sextet": list(SEXTET_EXPECTED),
        "body_diagonals": [list(d) for d in DIAGONALS],
        "transversals": N_TRANSVERSALS,
        "regular_coset_transversals": BLIND_TRANSVERSALS,
        "tolerance": {"blind": fmt(TOL_BLIND), "stabiliser": fmt(TOL_STAB),
                      "separation_min": fmt(SEP_MIN)},
        "gates": GATES,
        "notes": NOTES,
    }
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    return 0 if N_FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
