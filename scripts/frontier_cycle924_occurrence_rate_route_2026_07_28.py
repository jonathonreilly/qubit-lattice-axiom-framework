#!/usr/bin/env python3
"""Cycle-924 occurrence-rate-route arithmetic and the cyclic-patch alpha
line (self-contained).

REVISED (review loop iteration 1, Sol reviewer, 2026-08-08).  The original
runner claimed the occurrence-to-threefold-readout route (historically
"route 3" of the R-eta obligation) was "priced shut" / "blocked BY
THEOREM", leaving "route 1" as the sole remaining route.  Review refuted
the promotions: the referent gate was a literal vocabulary scan (absence of
words cannot prove absence of a derivable semantic map); the arity
mismatch had no lemma excluding aggregation across sites, times, or setup
sectors; the terminality leg inherited an invalid prohibition reading of
the realized-state primitive; several checks were false-PASS (a
word-firewall check that could not fail, an "at most one" check testing
">= 1", an "exhaustive" check testing "> 0", a type gate hard-coded False,
a survivor check never evaluating its witnesses); and the legacy
reproduction gate executed a landed runner that hard-loads the gitignored
generated audit-ledger monolith, which a clean checkout does not contain.
The route-closure claims are WITHDRAWN: the occurrence-rate route is OPEN.

This revised runner is SELF-CONTAINED and certifies only:

Q1  EXACT RATIO ARITHMETIC on stipulated recorded values:
    84/164 = 21/41;  2/3 - 21/41 = 19/123;  16/24 = 2/3.

Q2  CYCLIC-PATCH NULLITY: on Z/m (m = 2..6), the declared clauses
    (empty-configuration vanishing, disjoint additivity, cyclic
    translation invariance) leave a solution space of dimension exactly
    1, spanned by the record-count functional -- by exact subset-form
    elimination.

Q3  GROUP EQUALITY: the three-element cyclic rotation group and the Z/3
    translation group are EQUAL AS PERMUTATION SETS (not merely
    isomorphic).

Q4  THE MENU LINE AND THE IMPORTED NORMALIZATION: the five imported
    alpha-menu values {0, 1/9, 1/3, 1, 2/27} are points on the
    one-dimensional solution line of Q2; modulo positive rescaling the
    nonzero members are one projective point; imposing the IMPORTED
    inhomogeneous normalization A(full Z/3 configuration) = 2/9 selects
    alpha = 2/27 uniquely (ablation: without it, the whole line
    survives).  The imported values 2/3, 2/9 and the menu come from
    UNAUDITED sources (the fixed-locus theorem note and the two July
    no-go notes -- landed on main, unaudited on the current ledger) and
    are carried as explicitly conditional imports, never as retained
    facts.

Fail-closed: every certificate binds `pass` to the predicate it names.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
STDOUT_LIMIT_BYTES = 150_000

from fractions import Fraction
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------------------
# IMPORTED VALUES (explicitly conditional; sources landed but UNAUDITED on
# the current ledger -- see the note's imports section):
#   docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md
#   docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md
#   docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md
# ---------------------------------------------------------------------------
PHI_TARGET = Fraction(2, 3)          # imported, unaudited source
L_FIXED_LOCUS = Fraction(2, 9)       # imported, unaudited source
ALPHA_MENU = {
    "alpha_zero": Fraction(0),
    "alpha_ninth": Fraction(1, 9),
    "alpha_third": Fraction(1, 3),
    "alpha_one": Fraction(1),
    "alpha_2_27": Fraction(2, 27),
}

# STIPULATED recorded values (provenance context, non-load-bearing).
RECORDED_SPLIT = (84, 164)           # recorded realized share (uncertified)
RECORDED_PERIOD_PAIR = (16, 24)      # recorded same-artifact candidate

CERTS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> bool:
    CERTS.append((name, bool(ok), detail))
    return bool(ok)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def q1_ratios() -> dict:
    share = Fraction(*RECORDED_SPLIT)
    miss = PHI_TARGET - share
    period_ratio = Fraction(*RECORDED_PERIOD_PAIR)
    ok = (share == Fraction(21, 41)
          and miss == Fraction(19, 123)
          and period_ratio == PHI_TARGET)
    check("Q1_EXACT_RATIOS", ok,
          f"84/164={share} 2/3-21/41={miss} 16/24={period_ratio}")
    return {"share": str(share), "miss": str(miss),
            "period_ratio": str(period_ratio)}


def echelon_dim(m: int) -> tuple[int, bool]:
    """Free dimension of the declared clause family on subsets of Z/m, and
    whether the nullspace is spanned by the popcount (record count)."""
    n_conf = 1 << m
    rows: list[dict[int, Fraction]] = [{0: Fraction(1)}]
    for assign in product((0, 1, 2), repeat=m):
        a = b = 0
        for i, t in enumerate(assign):
            if t == 1:
                a |= 1 << i
            elif t == 2:
                b |= 1 << i
        if a and b and a < b:
            rows.append({a | b: Fraction(1), a: Fraction(-1),
                         b: Fraction(-1)})
    for mask in range(n_conf):
        rot = 0
        for i in range(m):
            if mask >> i & 1:
                rot |= 1 << ((i + 1) % m)
        if rot != mask:
            rows.append({mask: Fraction(1), rot: Fraction(-1)})
    pivots: dict[int, dict[int, Fraction]] = {}
    for row in rows:
        row = dict(row)
        while row:
            lead = max(row)
            if lead in pivots:
                factor = row[lead] / pivots[lead][lead]
                for c, v in pivots[lead].items():
                    row[c] = row.get(c, Fraction(0)) - factor * v
                row = {c: v for c, v in row.items() if v}
            else:
                pivots[lead] = row
                break
    dim = n_conf - len(pivots)
    # solve for the nullspace vector with singleton value 1 and check it is
    # the popcount functional
    if dim == 1:
        vec = [Fraction(0)] * n_conf
        free_cols = [c for c in range(n_conf) if c not in pivots]
        if len(free_cols) == 1:
            vec[free_cols[0]] = Fraction(1)
            # each pivot row's lead is its highest column, so resolve in
            # ASCENDING column order (lower entries already known)
            for col in sorted(pivots):
                row = pivots[col]
                s = sum(v * vec[c] for c, v in row.items() if c != col)
                vec[col] = -s / row[col]
            base = vec[1]
            popcount_ok = base != 0 and all(
                vec[mask] == base * bin(mask).count("1")
                for mask in range(n_conf))
        else:
            popcount_ok = False
    else:
        popcount_ok = False
    return dim, popcount_ok


def q2_nullity() -> dict:
    patches, ok = [], True
    for m in range(2, 7):
        dim, popcount_ok = echelon_dim(m)
        patches.append({"patch": f"Z/{m}", "free_dim": dim,
                        "spanned_by_record_count": popcount_ok})
        ok &= dim == 1 and popcount_ok
    check("Q2_CYCLIC_PATCH_NULLITY", ok,
          f"patches={[(p['patch'], p['free_dim']) for p in patches]} "
          f"all_dim_1_spanned_by_count={ok}")
    return {"patches": patches}


def q3_group_equality() -> dict:
    rot = tuple((i + 1) % 3 for i in range(3))
    c3 = {tuple(range(3))}
    cur = rot
    while cur not in c3:
        c3.add(cur)
        cur = tuple(cur[rot[i]] for i in range(3))
    translations = set()
    for t in range(3):
        translations.add(tuple((i + t) % 3 for i in range(3)))
    equal = c3 == translations
    check("Q3_GROUP_EQUALITY", equal,
          f"C3_rotations={sorted(c3)} Z3_translations={sorted(translations)} "
          f"equal_as_permutation_sets={equal}")
    return {"equal_as_permutation_sets": equal}


def q4_menu_line() -> dict:
    # every alpha gives the solution alpha * count on Z/3; verify the
    # declared clauses directly for each menu member
    m = 3
    n_conf = 1 << m
    results = {}
    all_solutions = True
    for name, alpha in ALPHA_MENU.items():
        vec = [alpha * bin(mask).count("1") for mask in range(n_conf)]
        ok_empty = vec[0] == 0
        ok_add = True
        for a in range(n_conf):
            for b in range(n_conf):
                if a & b == 0:
                    ok_add &= vec[a | b] == vec[a] + vec[b]
        ok_rot = True
        for mask in range(n_conf):
            rot = 0
            for i in range(m):
                if mask >> i & 1:
                    rot |= 1 << ((i + 1) % m)
            ok_rot &= vec[rot] == vec[mask]
        results[name] = bool(ok_empty and ok_add and ok_rot)
        all_solutions &= results[name]
    nonzero = [a for a in ALPHA_MENU.values() if a != 0]
    projective_classes = {(-1 if a < 0 else 1) for a in nonzero}
    one_projective_point = len(projective_classes) == 1
    # imported inhomogeneous normalization: A(full Z/3) = 2/9 selects alpha
    full_count = 3
    forced_alpha = L_FIXED_LOCUS / full_count
    survivors = [n for n, a in ALPHA_MENU.items()
                 if a * full_count == L_FIXED_LOCUS]
    ablation_survivors = list(ALPHA_MENU)
    ok = (all_solutions and one_projective_point
          and forced_alpha == Fraction(2, 27)
          and survivors == ["alpha_2_27"]
          and len(ablation_survivors) == 5)
    check("Q4_MENU_LINE_AND_NORMALIZATION", ok,
          f"all_menu_members_on_the_line={all_solutions} "
          f"nonzero_members_one_projective_point={one_projective_point} "
          f"imported_normalization_forces_alpha={forced_alpha} "
          f"menu_survivors={survivors} ablation_keeps={len(ablation_survivors)}")
    return {"menu_members_are_solutions": results,
            "forced_alpha": str(forced_alpha),
            "survivors_under_imported_normalization": survivors}


def run_all() -> dict:
    a = q1_ratios()
    b = q2_nullity()
    c = q3_group_equality()
    d = q4_menu_line()
    return {"q1": a, "q2": b, "q3": c, "q4": d,
            "science_digest": digest([a, b, c, d,
                                      {k: str(v) for k, v
                                       in ALPHA_MENU.items()}])}


def main() -> int:
    t0 = monotonic()
    first = run_all()
    saved = list(CERTS)
    CERTS.clear()
    second = run_all()
    CERTS.clear()
    CERTS.extend(saved)
    det = first["science_digest"] == second["science_digest"]
    check("Q5_DETERMINISM", det, f"double_run_digest_equal={det}")
    elapsed = monotonic() - t0
    check("Q6_RUNTIME", elapsed < AUDIT_TIMEOUT_SEC,
          f"elapsed_s={elapsed:.1f} budget_s={AUDIT_TIMEOUT_SEC}")

    out: list[str] = []
    w = out.append
    w("=" * 78)
    w("CYCLE 924 -- OCCURRENCE-RATE-ROUTE ARITHMETIC AND THE CYCLIC-PATCH "
      "ALPHA LINE")
    w("=" * 78)
    w("")
    w("SCOPE: self-contained.  The occurrence-to-threefold-readout route is")
    w("OPEN -- no route-closure, terminality, or sole-remaining-route claim")
    w("is made.  The imported values 2/3, 2/9 and the alpha menu come from")
    w("UNAUDITED sources and every Q4 statement is conditional on them.")
    w("")
    w("CLAIMS_JSON: " + compact({
        "share": first["q1"]["share"],
        "miss": first["q1"]["miss"],
        "period_ratio": first["q1"]["period_ratio"],
        "patch_dims": [(p["patch"], p["free_dim"])
                       for p in first["q2"]["patches"]],
        "group_equality": first["q3"]["equal_as_permutation_sets"],
        "forced_alpha": first["q4"]["forced_alpha"],
        "survivors": first["q4"]["survivors_under_imported_normalization"],
        "science_digest": first["science_digest"],
    }))
    w("")
    w("-- CERTIFICATES --------------------------------------------------------")
    for name, ok, detail in CERTS:
        w(f"  {'PASS' if ok else 'FAIL'}  {name:<34} {detail}")
    npass = sum(1 for _, ok, _ in CERTS if ok)
    nfail = len(CERTS) - npass
    w("")
    w(f"TOTAL: PASS={npass} FAIL={nfail}")
    w(f"VERDICT: {'PASS' if nfail == 0 else 'FAIL'}")
    text = "\n".join(out)
    sys.stdout.write(text + "\n")

    receipt = {
        "cycle": 924,
        "claim_type": "bounded_theorem",
        "headline": ("occurrence-rate-route arithmetic: 84/164 = 21/41 "
                     "misses the imported 2/3 target by exactly 19/123; the "
                     "declared clause family on cyclic patches Z/2..Z/6 has "
                     "free dimension 1 spanned by the record count; the "
                     "three-element rotation and translation groups are "
                     "equal as permutation sets; the five imported "
                     "alpha-menu values lie on that one line and the "
                     "imported normalization 2/9 selects 2/27.  The "
                     "occurrence route itself is OPEN; no closure claim"),
        "imported_values": {
            "phi_target": str(PHI_TARGET),
            "fixed_locus_normalization": str(L_FIXED_LOCUS),
            "alpha_menu": {k: str(v) for k, v in ALPHA_MENU.items()},
            "status": ("imported from landed but UNAUDITED sources (the "
                       "fixed-locus theorem note and the two July no-go "
                       "notes); explicitly conditional; not retained, not "
                       "Nature-grade"),
        },
        "stipulated_scope_inputs": {
            "recorded_split": list(RECORDED_SPLIT),
            "recorded_period_pair": list(RECORDED_PERIOD_PAIR),
            "status": "recorded history from uncertified sibling "
                      "computations; arithmetic only",
        },
        "route_status": ("the occurrence-to-threefold-readout route is "
                         "OPEN.  Withdrawn: referent-gap, arity-mismatch "
                         "and terminality closure claims (review findings; "
                         "vocabulary scans and binary local menus do not "
                         "exclude derivable maps or aggregates)"),
        "results": first,
        "certificates": {n: {"pass": ok, "detail": d} for n, ok, d in CERTS},
        "all_certificates_pass": nfail == 0,
        "review_loop": {
            "iteration": 1,
            "disposition": "FIX_THEN_PROCEED",
            "reviewer": "Sol",
            "date": "2026-08-08",
            "fix": ("self-contained rewrite: route-closure claims "
                    "withdrawn; false-PASS checks replaced by fail-closed "
                    "predicates; legacy monolith-loading gate removed; "
                    "imports marked unaudited-conditional"),
        },
        "science_digest": first["science_digest"],
    }
    (ROOT / "outputs" /
     "occurrence_rate_route_cycle924_receipt_2026_07_28.json").write_text(
        json.dumps(receipt, indent=1, sort_keys=True) + "\n")

    if len(text.encode()) > STDOUT_LIMIT_BYTES:
        sys.stderr.write("stdout budget exceeded\n")
        return 1
    return 0 if nfail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
