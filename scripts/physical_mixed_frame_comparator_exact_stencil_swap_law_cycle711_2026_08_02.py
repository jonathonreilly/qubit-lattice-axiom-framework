"""Cycle 711 -- bounded exact stencil swap identity behind the mixed-frame comparator.

Finite exhaustive and symbolic check (stdlib + numpy + sympy only).  It re-derives, from the
landed Cycle-696 open-coframe endpoint compiler chain alone, the mixed-frame
comparator value 4 that Cycle 710's covariance-boundary census measured but did not
derive.  The chain has four exact stages:

  C1  substitution dichotomy: the bounding-box transport substitutes a diagonal
      class at frame R exactly when the rotated direction has mixed signs; the
      substituted set is empty exactly on the constant-sign sextet, and every one
      of the 18 mixed frames substitutes exactly 2 face classes + 1 body class;
  C2  incidence decomposition: the disjoint complementary face-diagonal pair
      carries exactly 2 path-simplex incidences whose local-Hessian sum times the
      tick multiplier reproduces the assembled stencil entry bit-for-bit, while
      the shared-vertex complementary pair carries 0 incidences and an exactly
      zero entry;
  C3  exact per-simplex value: the mixed second derivative of the per-simplex
      deficit action at the flat background is exactly -1 for both incident
      configurations (symbolic, all surviving per-hinge terms rational), with a
      perturbed-background rejector showing the gate discriminates;
  C4  swap attainment: at every mixed frame the argmax family of the assembly
      defect E = P^T Q P - Q consists solely of 0 <-> 4 swaps on face-face pairs
      with exactly one substituted endpoint, so the comparator equals
      |LT * (-1 - 1)| = 4 exactly at stencil level, and the measured deviation
      is central-difference truncation with a convergence-ratio certificate and
      a closed error budget.

The frame-uniform rounded census of |E| > 2 entries, the both-clean block
ceiling, and the off-integer-distance witness are measured, not derived.  Every
number printed here is recomputed from the declared compiler-source closure in
this run; no sibling cycle's measured value or pinned result table is consumed.

Read inventory. External/ancestral scientific inputs: the Cycle-696 compiler
and its transitive scripts/ imports, declared in AUDIT_INPUT_PATHS below and
loaded as source. Package-local write activity: one paired receipt under
outputs/. This runner performs no self-hash or receipt-verification integrity
read.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
_MODULE = HERE / "physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py"
_SPEC = importlib.util.spec_from_file_location("c696_compiler_for_c711", _MODULE)
c696 = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(c696)

# The load-bearing repository-source closure: the Cycle-696 compiler loaded
# above plus every scripts/ module it imports transitively. The cache binds all
# five files and fails stale when any of their bytes drift.
AUDIT_INPUT_PATHS = (
    "scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py",
    "scripts/physical_dynamical_metric_source_law_bridge_tournament_cycle576_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_regge_support_2026_07_22.py",
    "scripts/physical_dynamical_metric_source_law_bridge_cycle576_plaquette_support_2026_07_22.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

# Declared audit timeout in seconds. The observed run is well below this bound;
# the margin accommodates slower symbolic algebra on an independent audit host.
AUDIT_TIMEOUT_SEC = 300

FRAMES = [np.asarray(m, dtype=np.int64) for m in c696.c576.FRAMES]
SEXTET = (1, 4, 9, 15, 18, 23)
PLUS = (15, 18, 23)
MINUS = (1, 4, 9)
SPC = tuple(c696.SPATIAL_CLASSES)
DIRV = {c: np.asarray(c696.regge.DIRS15[c][:3], dtype=np.int64) for c in SPC}
PAIRS5 = c696.regge.PAIRS5
L_LIST = (3, 7)
PAIR_M4 = ((5, (2, 1, 0)), (11, (1, 1, 0)))
PAIR_Z = ((5, (0, 0, 0)), (11, (0, 0, 0)))
REPRESENTATIVE_CONFIGS = ((0, 5, 1), (18, 8, 5))
DEV_TOL = 2e-8
SWAP_LO = 1e-9
SURD_TOL = 2e-7
RATIO_LO = 3.4
RATIO_HI = 4.6

RECEIPT_NAME = ("physical_mixed_frame_comparator_exact_stencil_swap_law_cycle711"
                "_2026_08_02_receipt_2026-08-02.json")

N_PASS = 0
N_FAIL = 0
GATES: dict = {}
NOTES: dict = {}


def fmt(x) -> str:
    return "{:.1e}".format(float(x))


def check(name: str, ok: bool, detail: str = "") -> bool:
    """Record and print one gate.  The symbolic gates carry an explicit
    perturbed-background rejector; the FD gates carry a convergence-ratio
    requirement; the census gates compare recomputed multisets exactly."""
    global N_PASS, N_FAIL
    ok = bool(ok)
    if ok:
        N_PASS += 1
    else:
        N_FAIL += 1
    GATES[name] = {"pass": ok, "detail": detail}
    print("{} {} {}".format("PASS" if ok else "FAIL", name, detail))
    return ok


def substituted(R: np.ndarray) -> set:
    """Classes whose rotated direction has mixed signs: canonical bounding-box
    edge differs from the geometric rotated edge."""
    out = set()
    for c in SPC:
        w = R @ DIRV[c]
        if (w > 0).any() and (w < 0).any():
            out.add(c)
    return out


def constant_sign(R: np.ndarray) -> bool:
    nz = R[R != 0]
    return bool(np.all(nz == 1) or np.all(nz == -1))


def support(c: int) -> int:
    return int(np.abs(DIRV[c]).sum())


def dof_perm(L: int, index: dict, R: np.ndarray) -> np.ndarray:
    smap = c696.frame_site_map(L, R)
    dir2class = {tuple(int(t) for t in DIRV[c]): c for c in SPC}
    m = np.empty(len(index), dtype=np.int64)
    for (c, x), i in index.items():
        w = R @ DIRV[c]
        vp = tuple(int(t) for t in np.abs(w))
        xp = tuple(int(t) for t in (np.asarray(smap[x], dtype=np.int64) + np.minimum(w, 0)))
        m[i] = index[(dir2class[vp], xp)]
    return m


def incidences(L: int, A, B):
    """All (template, cell, slot_i, slot_j) with dof key A at slot i and B at slot j."""
    hits = []
    for p, tmpl in enumerate(c696.CELL):
        cls, anc = tmpl["cls"], tmpl["anc"]
        for b in itertools.product(range(L - 1), repeat=3):
            keys = [(cls[i], (b[0] + anc[i][0], b[1] + anc[i][1], b[2] + anc[i][2]))
                    for i in range(10)]
            for i in range(10):
                if keys[i] != A:
                    continue
                for j in range(10):
                    if keys[j] == B:
                        hits.append((p, b, i, j))
    return hits


def pair_key(A, B):
    """Canonical unordered pair of global dof keys."""
    return tuple(sorted((A, B)))


def incidence_config_map(L: int) -> dict:
    """Map each unordered dof-key pair to all local template/slot incidences.

    The slot ordering follows the canonical global-key ordering so a translated
    occurrence of one local configuration has the same tuple at every box size.
    """
    out = {}
    for p, tmpl in enumerate(c696.CELL):
        cls, anc = tmpl["cls"], tmpl["anc"]
        for b in itertools.product(range(L - 1), repeat=3):
            keys = [(cls[i], (b[0] + anc[i][0], b[1] + anc[i][1], b[2] + anc[i][2]))
                    for i in range(10)]
            for i in range(10):
                for j in range(i + 1, 10):
                    A, B = keys[i], keys[j]
                    cfg = (p, i, j) if A <= B else (p, j, i)
                    out.setdefault(pair_key(A, B), set()).add(cfg)
    return out


# --------------------------------------------------------------------------
# exact symbolic per-simplex machinery (rebuilt per the landed construction)
# --------------------------------------------------------------------------
QSYM = {e: sp.Symbol("q{}{}".format(e[0], e[1]), positive=True) for e in PAIRS5}


def _qq(i, j):
    return QSYM[(min(i, j), max(i, j))]


def _dot(i, j, base):
    if i == j:
        return _qq(base, i)
    return (_qq(base, i) + _qq(base, j) - _qq(i, j)) / 2


def hinge_term(a, b):
    """A_hinge * theta_(a, b) for the missing pair (a, b), symbolic."""
    hinge = [v for v in range(5) if v not in (a, b)]
    p, qv, r = hinge
    G11, G12, G22 = _dot(qv, qv, p), _dot(qv, r, p), _dot(r, r, p)
    det = G11 * G22 - G12 ** 2

    def proj_pair(wi, wj):
        ai1, ai2 = _dot(qv, wi, p), _dot(r, wi, p)
        aj1, aj2 = _dot(qv, wj, p), _dot(r, wj, p)
        return _dot(wi, wj, p) - (G22 * ai1 * aj1 - G12 * (ai1 * aj2 + ai2 * aj1)
                                  + G11 * ai2 * aj2) / det

    theta = sp.acos(proj_pair(a, b) / sp.sqrt(proj_pair(a, a) * proj_pair(b, b)))
    qa, qb, qc = _qq(p, qv), _qq(p, r), _qq(qv, r)
    A = sp.sqrt((2 * qa * qb + 2 * qa * qc + 2 * qb * qc
                 - qa ** 2 - qb ** 2 - qc ** 2) / 16)
    return A * theta


def flat_background(p: int) -> dict:
    flat = {}
    for k in range(10):
        q2 = c696.CLASS_ELL[c696.CELL[p]["cls"][k]] ** 2
        qi = round(q2)
        if abs(q2 - qi) > 1e-12:
            raise RuntimeError("non-integer flat squared length")
        flat[QSYM[PAIRS5[k]]] = sp.Integer(qi)
    return flat


def exact_mixed_d2(p: int, si: int, sj: int, sub: dict):
    """Exact mixed second derivative in the two slot LENGTHS at background sub.
    Returns (exact value, all-rational flag, acos-free flag)."""
    qA, qB = QSYM[PAIRS5[si]], QSYM[PAIRS5[sj]]
    acc = sp.Integer(0)
    all_rat = True
    acos_free = True
    for (a, b) in PAIRS5:
        d2 = sp.diff(hinge_term(a, b), qA, qB)
        if d2 == 0:
            continue
        v = d2.subs(sub)
        if v.atoms(sp.acos):
            acos_free = False
        v = sp.radsimp(sp.simplify(v))
        if not v.is_rational:
            all_rat = False
        acc += v
    ellA, ellB = sp.sqrt(sub[qA]), sp.sqrt(sub[qB])
    exact = sp.simplify(4 * ellA * ellB * (-acc))
    return exact, all_rat, acos_free


def main() -> int:
    LT = c696.LT
    print("c711 exact stencil swap law behind the mixed-frame comparator")
    print("tick multiplier LT = {}  FD step = {}  frames = {}  sextet = {}".format(
        LT, fmt(c696.FD_H), len(FRAMES), list(SEXTET)))

    # -- C1: substitution dichotomy over all 24 frames (exact combinatorics) --
    empty_frames = []
    mixed_ok = True
    nn_ok = True
    for g, R in enumerate(FRAMES):
        S = substituted(R)
        if not S:
            empty_frames.append(g)
        else:
            nface = sum(1 for c in S if support(c) == 2)
            nbody = sum(1 for c in S if support(c) == 3)
            if not (len(S) == 3 and nface == 2 and nbody == 1):
                mixed_ok = False
        if any(support(c) == 1 for c in S):
            nn_ok = False
    check("c1_empty_iff_sextet", tuple(empty_frames) == SEXTET,
          "empty-substitution frames {}".format(empty_frames))
    check("c1_constant_sign_iff_empty",
          all((len(substituted(R)) == 0) == constant_sign(R) for R in FRAMES),
          "all 24 frames")
    check("c1_mixed_two_face_one_body", mixed_ok, "18 mixed frames: 2 face + 1 body")
    check("c1_nn_never_substituted", nn_ok, "axis classes never substituted")

    # -- C2: incidence decomposition at L = 3 ------------------------------
    L = 3
    model = c696.assemble_static_hessian(L, wrap=False)
    Q3, index3 = model["Q"], model["index"]
    HLOC = {p: c696.simplex_local_hessian(p) for p in range(24)}

    hits4 = incidences(L, *PAIR_M4)
    q_entry = float(Q3[index3[PAIR_M4[0]], index3[PAIR_M4[1]]])
    stencil = LT * sum(float(HLOC[p][i, j]) for p, b, i, j in hits4)
    check("c2_pair_two_incidences", len(hits4) == 2,
          "disjoint complementary face-diagonal pair: {} incidences".format(len(hits4)))
    check("c2_pair_bit_match", float(stencil).hex() == float(q_entry).hex(),
          "LT * sum(local) equals assembled entry bit-for-bit, entry {}".format(fmt(q_entry)))
    check("c2_pair_each_near_minus_one",
          all(abs(float(HLOC[p][i, j]) + 1.0) <= 5e-9 for p, b, i, j in hits4),
          "each per-simplex mixed value within {} of -1".format(fmt(5e-9)))
    check("c2_pair_incidence_classes",
          {(p, i, j) for p, b, i, j in hits4} == {(0, 5, 1), (18, 8, 5)},
          "(template, slot_i, slot_j) = (0,5,1) and (18,8,5)")
    hits0 = incidences(L, *PAIR_Z)
    z_entry = float(Q3[index3[PAIR_Z[0]], index3[PAIR_Z[1]]])
    check("c2_shared_vertex_zero", len(hits0) == 0 and z_entry == 0.0,
          "shared-vertex pair: 0 incidences, entry exactly 0.0")

    # -- C3: exact symbolic closure of the full finite -4 family -----------
    rev3 = {i: key for key, i in index3.items()}
    incmap3 = incidence_config_map(3)
    family_pairs = {
        pair_key(rev3[i], rev3[j])
        for i in range(Q3.shape[0])
        for j in range(i + 1, Q3.shape[1])
        if abs(float(Q3[i, j]) + 4.0) <= DEV_TOL
    }
    family_classes = {
        tuple(sorted((A[0], B[0]))) for A, B in family_pairs
    }
    family_configs = set().union(*(incmap3[key] for key in family_pairs))
    check("c3_family_entry_count", len(family_pairs) == 48,
          "L=3 has 48 unordered assembled entries in the measured -4 family")
    check("c3_family_class_pairs", family_classes == {(5, 9), (5, 11), (9, 11)},
          "all three complementary face-diagonal class pairs and no others")
    check("c3_family_config_count", len(family_configs) == 12,
          "12 distinct translated local template/slot configurations")
    for (p, si, sj) in sorted(family_configs):
        flat = flat_background(p)
        exact, all_rat, acos_free = exact_mixed_d2(p, si, sj, flat)
        tag = "p{}_s{}_s{}".format(p, si, sj)
        check("c3_exact_family_{}".format(tag),
              sp.simplify(exact + 1) == 0 and all_rat and acos_free,
              "mixed d2 = {}; rational hinges; no surviving acos".format(exact))
    p, si, sj = REPRESENTATIVE_CONFIGS[0]
    pert = dict(flat_background(p))
    pert[QSYM[(3, 4)]] = pert[QSYM[(3, 4)]] + 1
    exact_p, _, _ = exact_mixed_d2(p, si, sj, pert)
    dist = abs(float(exact_p) + 1.0)
    check("c3_rejector_perturbed_background",
          dist > 1e-1 and sp.simplify(exact_p + 3 * sp.sqrt(7) / 7) == 0,
          "perturbed background gives {} (distance {} from -1)".format(exact_p, fmt(dist)))

    # -- C4: FD provenance of the measured deviation -----------------------
    errs_h = []
    for (p, si, sj) in REPRESENTATIVE_CONFIGS:
        e1 = abs(float(c696.simplex_local_hessian(p, c696.FD_H)[si, sj]) + 1.0)
        e2 = abs(float(c696.simplex_local_hessian(p, c696.FD_H / 2.0)[si, sj]) + 1.0)
        errs_h.append(e1)
        ratio = e1 / e2
        check("c4_fd_ratio_p{}".format(p), RATIO_LO <= ratio <= RATIO_HI,
              "err(h) {} err(h/2) {} ratio {:.2f}".format(fmt(e1), fmt(e2), ratio))
    budget = LT * sum(errs_h)
    dev = abs(abs(q_entry) - 4.0)
    check("c4_budget_matches_entry", abs(budget - dev) <= 1e-3 * dev,
          "LT * (err0 + err1) = {} vs entry deviation {}".format(fmt(budget), fmt(dev)))
    check("c4_deviation_scale", dev <= DEV_TOL,
          "|entry magnitude - 4| = {} le {}".format(fmt(dev), fmt(DEV_TOL)))

    # -- C5 + C6: swap census over all 18 mixed frames, both sizes ---------
    emax_hex_by_L = {}
    for L in L_LIST:
        model = c696.assemble_static_hessian(L, wrap=False)
        Q, index = model["Q"], model["index"]
        rev = {i: key for key, i in index.items()}
        incmap = incidence_config_map(L)
        cls_of = np.empty(len(index), dtype=np.int64)
        for (c, x), i in index.items():
            cls_of[i] = c
        emax_hexes, argmax_counts = set(), set()
        swaps_ok, endpoint_ok, exact_cover_ok = True, True, True
        observed_configs = set()
        orient = {True: 0, False: 0}
        censuses = set()
        bcm, offmax = 0.0, 0.0
        for g, R in enumerate(FRAMES):
            if g in SEXTET:
                continue
            S = substituted(R)
            m = dof_perm(L, index, R)
            E = Q[np.ix_(m, m)] - Q
            A = np.abs(E)
            emax = float(A.max())
            emax_hexes.add(emax.hex())
            sub = np.isin(cls_of, sorted(S))
            clean = ~sub
            bcm = max(bcm, float(A[np.ix_(clean, clean)].max()))
            offmax = max(offmax, float(np.abs(E - np.round(E)).max()))
            ii, jj = np.where(A > 3.5)
            argmax_counts.add(len(ii))
            for i, j in zip(ii, jj):
                lo = min(abs(Q[i, j]), abs(Q[m[i], m[j]]))
                hi = max(abs(Q[i, j]), abs(Q[m[i], m[j]]))
                if lo > SWAP_LO or abs(hi - 4.0) > DEV_TOL:
                    swaps_ok = False
                q0, q1 = float(Q[i, j]), float(Q[m[i], m[j]])
                if abs(q0) <= SWAP_LO and abs(q1 + 4.0) <= DEV_TOL:
                    nz_key = pair_key(rev[m[i]], rev[m[j]])
                elif abs(q1) <= SWAP_LO and abs(q0 + 4.0) <= DEV_TOL:
                    nz_key = pair_key(rev[i], rev[j])
                else:
                    swaps_ok = False
                    exact_cover_ok = False
                    nz_key = None
                if nz_key is not None:
                    cfgs = incmap.get(nz_key, set())
                    observed_configs.update(cfgs)
                    if not cfgs or not cfgs.issubset(family_configs):
                        exact_cover_ok = False
                si_, sj_ = bool(sub[i]), bool(sub[j])
                if si_ == sj_ or support(int(cls_of[i])) != 2 or support(int(cls_of[j])) != 2:
                    endpoint_ok = False
                else:
                    orient[si_] += 1
            vals, cnts = np.unique(np.round(E[A > 2.0]).astype(int), return_counts=True)
            censuses.add(tuple(zip(tuple(int(v) for v in vals), tuple(int(c) for c in cnts))))
        Ltag = "L{}".format(L)
        check("c5_emax_bitwise_uniform_{}".format(Ltag), len(emax_hexes) == 1,
              "one emax bit pattern across 18 mixed frames")
        emax_hex_by_L[L] = next(iter(emax_hexes))
        emax_val = float.fromhex(emax_hex_by_L[L])
        check("c5_emax_value_{}".format(Ltag), abs(emax_val - 4.0) <= DEV_TOL,
              "comparator {:.10e}".format(emax_val))
        want = {3: 128, 7: 3456}[L]
        check("c5_argmax_count_uniform_{}".format(Ltag), argmax_counts == {want},
              "argmax family size {} at every mixed frame".format(sorted(argmax_counts)))
        check("c5_all_swaps_{}".format(Ltag), swaps_ok,
              "every argmax entry is an assembled 0 <-> -4 swap")
        check("c5_exact_family_coverage_{}".format(Ltag),
              exact_cover_ok and observed_configs == family_configs,
              "argmax nonzero sides use all and only the 12 symbolically closed configs")
        check("c5_one_substituted_endpoint_{}".format(Ltag),
              endpoint_ok and orient[True] == orient[False] and orient[True] > 0,
              "face-face pairs, exactly one substituted endpoint, orientations {}".format(
                  dict(orient)))
        check("c6_census_frame_uniform_{}".format(Ltag), len(censuses) == 1,
              "rounded census of entries above 2: {}".format(sorted(next(iter(censuses)))))
        keys = {v for v, c in next(iter(censuses))}
        check("c6_census_keys_{}".format(Ltag), keys == {-4, -3, -2, 2, 3, 4},
              "swap family values")
        check("c6_both_clean_sqrt8_{}".format(Ltag),
              abs(bcm - 2.0 * np.sqrt(2.0)) <= SURD_TOL,
              "both-clean ceiling {} matches 2*sqrt(2) within {}".format(fmt(bcm), fmt(SURD_TOL)))
        check("c6_offint_sqrt12_{}".format(Ltag),
              offmax > 0.1 and abs(offmax - (2.0 * np.sqrt(3.0) - 3.0)) <= SURD_TOL,
              "largest integer distance {} matches 2*sqrt(3) - 3".format(fmt(offmax)))
        NOTES["emax_{}".format(Ltag)] = fmt(emax_val)
        NOTES["both_clean_{}".format(Ltag)] = fmt(bcm)
    check("c5_emax_bitwise_size_stable",
          emax_hex_by_L[3] == emax_hex_by_L[7],
          "same comparator bit pattern at both box sizes")

    # -- C7: sextet cross-checks at L = 3 ----------------------------------
    plus_max, minus_max, id_max = 0.0, 0.0, None
    for g in SEXTET:
        m = dof_perm(3, index3, FRAMES[g])
        E = Q3[np.ix_(m, m)] - Q3
        v = float(np.abs(E).max())
        if g == 23:
            id_max = v
        if g in PLUS:
            plus_max = max(plus_max, v)
        else:
            minus_max = max(minus_max, v)
    check("c7_sextet_ceilings", plus_max <= 1e-13 and minus_max <= 1e-9,
          "plus branch {} minus branch {}".format(fmt(plus_max), fmt(minus_max)))
    check("c7_identity_exact_zero", id_max == 0.0, "identity frame defect exactly 0.0")
    check("c7_supplied_constants", LT == 2 and float(c696.FD_H) == 1e-4,
          "tick multiplier and FD step as supplied by the compiler")

    receipt = {"box_sizes": list(L_LIST),
               "configs": [list(c) for c in sorted(family_configs)],
               "fail": N_FAIL,
               "gates": GATES,
               "notes": NOTES,
               "pass": N_PASS,
               "runner": Path(__file__).name}
    out = ROOT / "outputs" / RECEIPT_NAME
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, sort_keys=True, indent=2) + "\n")

    print("TOTAL: PASS={} FAIL={}".format(N_PASS, N_FAIL))
    return 1 if N_FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
