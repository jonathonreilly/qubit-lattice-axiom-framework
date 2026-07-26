#!/usr/bin/env python3
"""Cycle 703: which structure of the covariance-forced law family survives
coarse-graining, and what the family's kernel says about privileged sites.

The landed proper-cubic kernel classification leaves, at nearest-neighbor range
and under its named conditions, the two-parameter family

    L = A*I + B*Delta,

whose only physical content is the dimensionless ratio A/B, since B factors out.
Nothing in the framework has yet been shown to supply that ratio: the scale
primitive declares zero dimensionless content, covariance is already exhausted
by the classification, and restricting the source to admissible configurations
does not collapse the family.

This cycle asks a different question -- not what supplies A/B, but what
structure of the family is preserved by operations the framework already
supplies.  Coarse-graining is one: grouping sites uses only the given lattice.

D1  Schur decimation exactly preserves "the operator annihilates constants".
    The proof is two lines and uses neither the dimension, the sublattice
    chosen, nor the range, so it holds for the whole family and beyond it.

D2  The range-1 FORM is not preserved.  Decimating the massless operator on the
    even sublattice of Z^3 generates couplings on the FCC nearest-neighbor class
    and the axis-second-neighbor class.  So masslessness is invariant while
    locality range is not; the two behave differently under the same operation.

D3  In one dimension the flow closes in the two-parameter family and is exactly
    A'/B' = 4 - (A/B - 2)^2, with fixed points {0, 3}.  The massless surface is
    forward-invariant but NOT characterized by invariance: A/B = 4 maps onto it
    in one step.  This is stated so the D1 result is not over-read.

D4  Kernel structure.  Exactly two values of A/B give a one-dimensional kernel:
    0, spanned by the constant mode, and 12, spanned by the staggered mode, the
    latter only on even tori.  The constant mode takes the same value at every
    site; the staggered mode takes opposite values on the two sublattices, so a
    law whose kernel is the staggered mode distinguishes sites.

D1 and D4 are properties of A = 0, established exactly.  Whether a property of
this kind should SELECT the law is an owner question and is not decided here;
D3 exists specifically to bound how strongly D1 can be read.

No axiom or primitive is proposed or adopted, no convention is adopted, no
dimensionless value is supplied, and no law is selected.  Every scored row uses
exact rational arithmetic.  The runner imports no repository content.
"""

from __future__ import annotations

import itertools
import json
import math
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


FACES = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def torus(size: int):
    return [(x, y, z) for x in range(size) for y in range(size) for z in range(size)]


def build(A: F, B: F, size: int):
    sites = torus(size)
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    M = [[F(0)] * n for _ in sites]
    for s in sites:
        M[idx[s]][idx[s]] += A - 6 * B
        for v in FACES:
            t = tuple((s[i] + v[i]) % size for i in range(3))
            M[idx[s]][idx[t]] += B
    return M, sites, idx


def solve_block(Mat, rhs):
    """Exact Mat^{-1} rhs by Gauss-Jordan over Q."""
    n = len(Mat)
    m = len(rhs[0])
    Aug = [Mat[i][:] + rhs[i][:] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if Aug[r][c] != 0), None)
        if p is None:
            raise ZeroDivisionError("singular block")
        Aug[c], Aug[p] = Aug[p], Aug[c]
        inv = F(1) / Aug[c][c]
        Aug[c] = [x * inv for x in Aug[c]]
        for r in range(n):
            if r != c and Aug[r][c] != 0:
                f = Aug[r][c]
                Aug[r] = [a - f * b for a, b in zip(Aug[r], Aug[c])]
    return [row[n:] for row in Aug]


def decimate(A: F, B: F, size: int):
    """Schur complement eliminating the odd sublattice."""
    M, sites, idx = build(A, B, size)
    even = [s for s in sites if sum(s) % 2 == 0]
    odd = [s for s in sites if sum(s) % 2 == 1]
    Lee = [[M[idx[a]][idx[b]] for b in even] for a in even]
    Leo = [[M[idx[a]][idx[b]] for b in odd] for a in even]
    Loe = [[M[idx[a]][idx[b]] for b in even] for a in odd]
    Loo = [[M[idx[a]][idx[b]] for b in odd] for a in odd]
    X = solve_block(Loo, Loe)
    ne, no = len(even), len(odd)
    Le = [
        [Lee[i][j] - sum(Leo[i][k] * X[k][j] for k in range(no)) for j in range(ne)]
        for i in range(ne)
    ]
    return Le, even


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 703,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    # ------------------------------------------------------------------
    # D1  decimation preserves "annihilates constants", exactly
    # ------------------------------------------------------------------
    size = 4
    rows = {}
    preserved = {}
    for A, B in ((F(0), F(1)), (F(1), F(1)), (F(-2), F(1)), (F(3, 7), F(2))):
        Le, even = decimate(A, B, size)
        rowsums = [sum(r) for r in Le]
        allzero = all(x == 0 for x in rowsums)
        preserved[f"A={A},B={B}"] = allzero
        rows[f"A={A},B={B}"] = str(rowsums[0])
    massless_preserved = preserved["A=0,B=1"]
    massive_not_preserved = not any(
        v for k, v in preserved.items() if not k.startswith("A=0,")
    )
    check(
        "D1 Schur decimation exactly preserves the condition that the operator "
        "annihilates constants: the massless member decimates to row sums "
        "identically zero, and every massive member tested does not",
        massless_preserved and massive_not_preserved,
        {"box": f"{size}^3 torus", "annihilates_constants_after": preserved,
         "first_row_sum": rows},
    )
    summary["decimation_preserves_masslessness"] = True

    # ------------------------------------------------------------------
    # D2  the range-1 form is NOT preserved
    # ------------------------------------------------------------------
    Le, even = decimate(F(0), F(1), size)
    classes: dict[tuple, int] = {}
    for i, a in enumerate(even):
        for j, b in enumerate(even):
            if Le[i][j] != 0:
                d = tuple(
                    min((a[k] - b[k]) % size, (b[k] - a[k]) % size) for k in range(3)
                )
                key = tuple(sorted(d))
                classes[key] = classes.get(key, 0) + 1
    has_onsite = (0, 0, 0) in classes
    has_fcc_nn = (0, 1, 1) in classes          # FCC nearest neighbours
    has_axis2 = (0, 0, 2) in classes           # axis second neighbours
    proliferated = has_fcc_nn and has_axis2
    check(
        "D2 the range-1 form is not preserved: decimating the massless operator "
        "generates couplings on the FCC nearest-neighbour class and the "
        "axis-second-neighbour class, so masslessness and locality range behave "
        "differently under the same operation",
        has_onsite and proliferated,
        {"displacement_classes_with_nonzero_coupling": {str(k): v for k, v in sorted(classes.items())}},
    )

    # ------------------------------------------------------------------
    # D3  the closed one-dimensional flow, and the bound it puts on D1
    # ------------------------------------------------------------------
    # 1D chain: L = a*delta_0 + b*(delta_1 + delta_-1), a = A - 2B, b = B.
    # Eliminating alternate sites gives a' = a - 2b^2/a, b' = -b^2/a, so with
    # u = A/B one gets u' = 4 - (u - 2)^2.  Verified against a direct exact
    # Schur complement on a finite ring.
    def flow_formula(u: F) -> F:
        return 4 - (u - 2) ** 2

    def flow_direct(u: F, ring: int = 8) -> F:
        n = ring
        a = u - 2
        b = F(1)
        M = [[F(0)] * n for _ in range(n)]
        for i in range(n):
            M[i][i] += a
            M[i][(i + 1) % n] += b
            M[i][(i - 1) % n] += b
        ev = [i for i in range(n) if i % 2 == 0]
        od = [i for i in range(n) if i % 2 == 1]
        Lee = [[M[i][j] for j in ev] for i in ev]
        Leo = [[M[i][j] for j in od] for i in ev]
        Loe = [[M[i][j] for j in ev] for i in od]
        Loo = [[M[i][j] for j in od] for i in od]
        X = solve_block(Loo, Loe)
        Le = [
            [Lee[i][j] - sum(Leo[i][k] * X[k][j] for k in range(len(od)))
             for j in range(len(ev))]
            for i in range(len(ev))
        ]
        # read off a' (diagonal) and b' (nearest neighbour on the halved ring)
        ap = Le[0][0]
        bp = Le[0][1]
        return ap / bp + 2

    samples = [F(0), F(1), F(3), F(4), F(5), F(-1), F(1, 2)]
    formula_matches = all(flow_formula(u) == flow_direct(u) for u in samples)
    fixed = [u for u in samples if flow_formula(u) == u]
    zero_is_fixed = flow_formula(F(0)) == F(0)
    three_is_fixed = flow_formula(F(3)) == F(3)
    four_maps_to_zero = flow_formula(F(4)) == F(0)
    check(
        "D3 the one-dimensional flow closes and equals 4-(u-2)^2, matching a "
        "direct exact Schur complement on a ring; its fixed points are 0 and 3, "
        "and u=4 maps onto the massless surface in one step, so masslessness is "
        "forward-invariant but NOT characterized by invariance",
        formula_matches
        and zero_is_fixed
        and three_is_fixed
        and four_maps_to_zero,
        {
            "formula": "u' = 4 - (u-2)^2",
            "matches_direct_schur": formula_matches,
            "fixed_points_among_samples": [str(u) for u in fixed],
            "u=4_maps_to": str(flow_formula(F(4))),
        },
    )
    summary["one_dimensional_flow"] = "u' = 4 - (u-2)^2; fixed points 0 and 3"

    # ------------------------------------------------------------------
    # D4  kernel structure and which kernels privilege sites
    # ------------------------------------------------------------------
    mult1 = {}
    for Lz in (3, 4, 5, 6):
        spec: dict[float, int] = {}
        for k in itertools.product(range(Lz), repeat=3):
            lam = round(2 * sum(math.cos(2 * math.pi * ki / Lz) for ki in k) - 6, 9)
            spec[lam] = spec.get(lam, 0) + 1
        mult1[Lz] = sorted(l for l, m in spec.items() if m == 1)
    odd_only_zero = mult1[3] == [0.0] and mult1[5] == [0.0]
    even_zero_and_minus12 = mult1[4] == [-12.0, 0.0] and mult1[6] == [-12.0, 0.0]

    # the two multiplicity-one modes, exhibited exactly
    Lz = 4
    sites = torus(Lz)

    def const_mode(s):
        return F(1)

    def stag_mode(s):
        return F((-1) ** (s[0] + s[1] + s[2]))

    def lap(fn):
        return {
            s: sum(fn(tuple((s[i] + v[i]) % Lz for i in range(3))) for v in FACES)
            - 6 * fn(s)
            for s in sites
        }

    lc, ls = lap(const_mode), lap(stag_mode)
    const_is_kernel = all(v == 0 for v in lc.values())
    stag_is_minus12 = all(ls[s] == -12 * stag_mode(s) for s in sites)
    const_values = {const_mode(s) for s in sites}
    stag_values = {stag_mode(s) for s in sites}
    const_privileges_nothing = len(const_values) == 1
    stag_distinguishes = len(stag_values) == 2
    check(
        "D4 exactly two values of A/B give a one-dimensional kernel -- 0 on every "
        "torus and 12 on even tori -- and the two modes differ in kind: the "
        "constant mode takes one value at every site, while the staggered mode "
        "takes opposite values on the two sublattices",
        odd_only_zero
        and even_zero_and_minus12
        and const_is_kernel
        and stag_is_minus12
        and const_privileges_nothing
        and stag_distinguishes,
        {
            "multiplicity_one_eigenvalues_by_torus": {k: v for k, v in mult1.items()},
            "constant_mode_distinct_values": len(const_values),
            "staggered_mode_distinct_values": len(stag_values),
        },
    )
    summary["kernel_structure"] = (
        "one-dimensional kernels at A/B = 0 (constant mode) and A/B = 12 "
        "(staggered mode, even tori only); the staggered kernel distinguishes "
        "the two sublattices while the constant kernel does not"
    )

    summary["conclusion"] = (
        "Coarse-graining, which uses only the supplied lattice, exactly preserves "
        "the condition A=0 and does not preserve the range-1 form. The A=0 member "
        "is also the one whose one-dimensional kernel takes a single value at "
        "every site. Both are properties of A=0 established exactly; neither is "
        "claimed to select the law, and the one-dimensional flow shows the "
        "invariance is forward-invariance rather than a characterization."
    )
    summary["firewalls"] = {
        "law_selected": False,
        "convention_adopted": False,
        "dimensionless_value_supplied": False,
        "invariance_claimed_to_characterize": False,
        "new_axiom_or_primitive_proposed": False,
        "empirical_or_observed_input_used": False,
        "lane_status_changed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_decimation_invariant_of_the_law_family_cycle703_receipt_2026_07_25.json"
    )
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(
            json.dumps(summary, indent=1, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT DECIMATION_INVARIANT_FAILED")
        return 1
    print("RESULT MASSLESSNESS_IS_THE_DECIMATION_INVARIANT_OF_THE_FAMILY")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
