#!/usr/bin/env python3
"""Checks for fresh-site Record constraints and conditional persistence algebra.

The runner keeps three layers separate:

* T1 checks a necessary consequence of the Record clauses in an explicitly
  site-tagged monotone history whose events are already specified as successive
  record formation. It does not derive that representation, identify physical
  self-composition with record formation, or prove the converse from injective
  sites to full Admissibility.
* T2 checks the fixed-point/constant-orbit identity under the supplied map and
  a common epoch-comparable readout rule.
* T3 checks exact finite-horizon offset bounds. It explicitly demonstrates that
  a nonzero offset survives every selected finite window, so finite observation
  does not imply exact fixed-point siting.

All derivation-path quantities are exact symbolic or high-precision Decimal
calculations. Numerical pairs are illustrative test parameters, not empirical
comparators.
"""

from decimal import Decimal, ROUND_CEILING, getcontext
from itertools import product
from pathlib import Path

import sympy as sp


getcontext().prec = 90

PASS = 0
FAIL = 0


def check(num: int, ok: bool, desc: str, detail: str = "") -> None:
    """Record and print one failing-capable check."""
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"; {detail}" if detail else ""
    print(f"CHECK {num:02d}: {tag} -- {desc}{suffix}")


def norm(text: str) -> str:
    """Whitespace-normalize source text for line-wrap-stable quote guards."""
    return " ".join(text.split())


def record_clause_trace(history: tuple[str, ...]) -> tuple[bool, list[dict[str, str]]]:
    """Apply the Record clauses in the supplied site-tagged representation.

    Each event creates content with a unique event identifier. A repeated site
    is rejected; otherwise every snapshot contains all prior site/content
    assignments unchanged.
    """
    records: dict[str, str] = {}
    snapshots: list[dict[str, str]] = []
    for epoch, site in enumerate(history):
        if site in records:
            return False, snapshots
        records[site] = f"record-{epoch}"
        snapshots.append(records.copy())
    return True, snapshots


def coexistence_violates_one_per_site(history: tuple[str, ...]) -> bool:
    """Test the policy that keeps both contents at a repeated site."""
    records: dict[str, list[str]] = {}
    for epoch, site in enumerate(history):
        records.setdefault(site, []).append(f"record-{epoch}")
        if len(records[site]) > 1:
            return True
    return False


def overwrite_violates_permanence(history: tuple[str, ...]) -> bool:
    """Test the policy that replaces old content at a repeated site."""
    records: dict[str, str] = {}
    for epoch, site in enumerate(history):
        if site in records:
            prior_content = records[site]
            records[site] = f"record-{epoch}"
            return prior_content not in records.values()
        records[site] = f"record-{epoch}"
    return False


def full_admissibility_toy(history: tuple[str, ...]) -> bool:
    """Toy extra-veto model showing Record compatibility is not sufficient.

    The `s2` veto stands for additional content of the unknown nearest-neighbor
    Admissibility rule. It is a negative control, not a physical proposal.
    """
    record_compatible, _ = record_clause_trace(history)
    return record_compatible and "s2" not in history


def decimal_escape_steps(epsilon: Decimal, band: Decimal, sign: int) -> int:
    """Directly iterate r -> 2 r^2 until the fixed-point band is left."""
    half = Decimal(1) / Decimal(2)
    r_value = half + Decimal(sign) * epsilon
    steps = 0
    while abs(r_value - half) < band:
        r_value = Decimal(2) * r_value * r_value
        steps += 1
        if steps > 10000:
            raise RuntimeError("escape iteration exceeded guard")
    return steps


def closed_escape_steps(epsilon: Decimal, band: Decimal, sign: int) -> int:
    """Use q_n=q_0^(2^n) to compute the exact band-exit index."""
    two = Decimal(2)
    q_initial = Decimal(1) + two * Decimal(sign) * epsilon
    q_boundary = Decimal(1) + two * Decimal(sign) * band
    doubling_threshold = q_boundary.ln() / q_initial.ln()
    real_step = doubling_threshold.ln() / two.ln()
    return int(real_step.to_integral_value(rounding=ROUND_CEILING))


def persistence_bounds(steps: int, band: Decimal) -> tuple[Decimal, Decimal]:
    """Return the exact open interval of offsets still in band at `steps`."""
    two = Decimal(2)
    inverse_power = Decimal(1) / (two**steps)
    lower_q = ((Decimal(1) - two * band).ln() * inverse_power).exp()
    upper_q = ((Decimal(1) + two * band).ln() * inverse_power).exp()
    return (lower_q - Decimal(1)) / two, (upper_q - Decimal(1)) / two


def stays_in_band(epsilon: Decimal, band: Decimal, steps: int) -> bool:
    """Check the orbit at every epoch from zero through `steps`."""
    half = Decimal(1) / Decimal(2)
    r_value = half + epsilon
    for _ in range(steps + 1):
        if abs(r_value - half) >= band:
            return False
        r_value = Decimal(2) * r_value * r_value
    return True


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    axiom_path = root / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    axiom_norm = norm(axiom_path.read_text(encoding="utf-8"))

    quote_form = "Records form."
    quote_lock = "When present, a record locks exactly one admissible local possibility."
    quote_permanence = "A site never carries more than one record; records are permanent."
    quote_readout = "A readout value is determined by record content alone."
    quote_additivity = (
        "For any finite collection of pairwise-disjoint records, scalar readout "
        "`I` is additive, with `I(empty)=0`."
    )

    check(1, norm(quote_form) in axiom_norm, "live Record quote: records form")
    check(
        2,
        norm(quote_lock) in axiom_norm,
        "live Record quote: a record locks one admissible local possibility",
    )
    check(
        3,
        norm(quote_permanence) in axiom_norm,
        "live Record quote: one record per site and permanence",
    )
    check(
        4,
        norm(quote_readout) in axiom_norm,
        "live Record quote: readout is determined by record content",
    )
    check(
        5,
        norm(quote_additivity) in axiom_norm,
        "live Record quote: scalar readout I is additive over disjoint records",
    )

    sites = ("s0", "s1", "s2")
    histories = [
        history
        for length in range(1, 4)
        for history in product(sites, repeat=length)
    ]
    traces = {history: record_clause_trace(history) for history in histories}

    necessary_freshness = all(
        (not compatible) or len(set(history)) == len(history)
        for history, (compatible, _) in traces.items()
    )
    check(
        6,
        necessary_freshness and any(compatible for compatible, _ in traces.values()),
        "T1 necessary direction: every Record-clause-compatible history uses fresh sites",
    )

    full_retention = True
    for history, (compatible, snapshots) in traces.items():
        if not compatible:
            continue
        for epoch, snapshot in enumerate(snapshots, start=1):
            expected = {
                site: f"record-{index}" for index, site in enumerate(history[:epoch])
            }
            full_retention = full_retention and len(snapshot) == epoch and snapshot == expected
    check(
        7,
        full_retention,
        "T1 compatible histories retain every earlier site/content assignment",
    )

    repeated_histories = [
        history for history in histories if len(set(history)) < len(history)
    ]
    policy_checks = [
        coexistence_violates_one_per_site(history)
        and overwrite_violates_permanence(history)
        for history in repeated_histories
    ]
    check(
        8,
        bool(policy_checks) and all(policy_checks),
        "T1 repeated-site negative control: coexistence and overwrite fail different Record clauses",
    )

    injective_but_vetoed = ("s2",)
    compatible, _ = record_clause_trace(injective_but_vetoed)
    check(
        9,
        compatible
        and len(set(injective_but_vetoed)) == len(injective_but_vetoed)
        and not full_admissibility_toy(injective_but_vetoed),
        "T1 converse guard: injective Record compatibility need not imply full Admissibility",
    )

    matrix_symbol = sp.MatrixSymbol("M", 3, 3)
    matrix = sp.Matrix(matrix_symbol)
    projector_s = sp.diag(1, 0, 0)
    projector_d = sp.diag(0, 1, 1)

    def pinch(value: sp.MatrixBase) -> sp.MatrixBase:
        return projector_s * value * projector_s + projector_d * value * projector_d

    idempotence_difference = sp.simplify(pinch(pinch(matrix)) - pinch(matrix))
    check(
        10,
        idempotence_difference == sp.zeros(3, 3),
        "same-site pinch support check: D(D(M))=D(M)",
    )

    r = sp.symbols("r", nonnegative=True)
    probability_s = 1 / (1 + 2 * r)
    probability_d = 2 * r / (1 + 2 * r)
    normalizer = probability_s**2 + probability_d**2
    next_s = probability_s**2 / normalizer
    next_d = probability_d**2 / normalizer
    derived_next_r = sp.simplify(next_d / (2 * next_s))
    check(
        11,
        sp.simplify(derived_next_r - 2 * r**2) == 0,
        "T2 supplied agreement filter reduces exactly to f(r)=2r^2",
        detail=f"r_next={derived_next_r}",
    )

    fixed_solutions = set(sp.solve(sp.Eq(2 * r**2, r), r))
    check(
        12,
        fixed_solutions == {sp.Integer(0), sp.Rational(1, 2)},
        "T2 complete finite nonnegative fixed set is {0,1/2}",
        detail=f"fixed={sorted(fixed_solutions)}",
    )

    grid = (
        sp.Integer(0),
        sp.Rational(1, 4),
        sp.Rational(1, 3),
        sp.Rational(1, 2),
        sp.Integer(1),
        sp.Integer(2),
    )

    def orbit_is_constant(value: sp.Expr, epochs: int = 6) -> bool:
        current = value
        for _ in range(epochs):
            current = sp.simplify(2 * current**2)
            if current != value:
                return False
        return True

    biconditional = all(
        orbit_is_constant(value) == (value in fixed_solutions) for value in grid
    )
    check(
        13,
        biconditional,
        "T2 on the test grid, constant supplied-map orbit iff fixed point",
    )

    nonfixed_orbit = [sp.Integer(1)]
    for _ in range(2):
        nonfixed_orbit.append(sp.simplify(2 * nonfixed_orbit[-1] ** 2))
    check(
        14,
        nonfixed_orbit == [sp.Integer(1), sp.Integer(2), sp.Integer(8)],
        "T2 negative control: a nonfixed value does not persist",
        detail=f"orbit={nonfixed_orbit}",
    )

    a1_sq, b1_sq = sp.Integer(2), sp.Integer(1)
    a2_sq, b2_sq = sp.Integer(1), sp.Integer(1)
    r1 = sp.Rational(b1_sq, a1_sq)
    r2 = sp.Rational(b2_sq, a2_sq)
    pooled_a = a1_sq + a2_sq
    pooled_b = b1_sq + b2_sq
    pooled_ratio = sp.Rational(pooled_b, pooled_a)
    check(
        15,
        len({r1, r2, pooled_ratio}) == 3
        and pooled_ratio == sp.Rational(2, 3),
        "readout-rule exhibit: two per-record ratios and pooled ratio are distinct observables",
        detail=f"values={r1,r2,pooled_ratio}",
    )

    ratio_nonadditivity = pooled_ratio != r1 + r2
    check(
        16,
        pooled_a == 3
        and pooled_b == 2
        and ratio_nonadditivity,
        "additive quadratic aggregates do not make their ratio additive or select a cross-epoch rule",
    )

    equal_ratio_pool = sp.Rational(1 + 2, 2 + 4)
    check(
        17,
        equal_ratio_pool == sp.Rational(1, 2),
        "positive control: equal per-record ratios pool to their common value",
    )

    q = sp.symbols("q", positive=True)
    q_next = sp.simplify(2 * (2 * (q / 2) ** 2))
    q_after_three = q
    for _ in range(3):
        q_after_three = sp.expand(q_after_three**2)
    check(
        18,
        q_next == q**2 and q_after_three == q**8,
        "T3 exact conjugacy: q=2r gives q_next=q^2 and q_3=q_0^8",
    )

    multiplier = sp.diff(2 * r**2, r).subs(r, sp.Rational(1, 2))
    check(
        19,
        multiplier == 2,
        "T3 local multiplier at r*=1/2 is 2",
    )

    parameter_pairs = (
        (Decimal("1e-5"), Decimal("0.1"), 14),
        (Decimal("1e-8"), Decimal("0.2"), 25),
    )
    escape_results = []
    for epsilon, band, expected in parameter_pairs:
        row = {
            "epsilon": epsilon,
            "band": band,
            "positive_direct": decimal_escape_steps(epsilon, band, 1),
            "positive_closed": closed_escape_steps(epsilon, band, 1),
            "negative_direct": decimal_escape_steps(epsilon, band, -1),
            "negative_closed": closed_escape_steps(epsilon, band, -1),
            "expected": expected,
        }
        escape_results.append(row)
    check(
        20,
        all(
            row["positive_direct"]
            == row["positive_closed"]
            == row["negative_direct"]
            == row["negative_closed"]
            == row["expected"]
            for row in escape_results
        ),
        "T3 direct Decimal iteration matches both exact escape formulas",
        detail=str(escape_results),
    )
    check(
        21,
        escape_results[0]["expected"] != escape_results[1]["expected"],
        "T3 discriminator: changing (epsilon,band) changes the escape count",
    )

    finite_windows = (5, 14, 25)
    band = Decimal("0.1")
    bounds = {steps: persistence_bounds(steps, band) for steps in finite_windows}
    shrinking = all(
        lower < 0 < upper for lower, upper in bounds.values()
    ) and all(
        bounds[later][1] < bounds[earlier][1]
        for earlier, later in zip(finite_windows, finite_windows[1:])
    )
    check(
        22,
        shrinking,
        "T3 finite-horizon allowed-offset intervals are nonzero and shrink with the window",
        detail=str(bounds),
    )

    lower_14, upper_14 = bounds[14]
    nonzero_witness = upper_14 / Decimal(2)
    check(
        23,
        lower_14 < nonzero_witness < upper_14
        and nonzero_witness != 0
        and stays_in_band(nonzero_witness, band, 14),
        "T3 counterexample: a nonzero offset survives the 14-step finite window",
        detail=f"offset={nonzero_witness}",
    )

    epsilon = Decimal("1e-5")
    half = Decimal(1) / Decimal(2)
    orbit_values = [half + epsilon]
    for _ in range(18):
        orbit_values.append(Decimal(2) * orbit_values[-1] * orbit_values[-1])
    first_out = next(
        index for index, value in enumerate(orbit_values) if abs(value - half) >= band
    )
    fresh_records: dict[str, Decimal] = {}
    value_snapshots: list[dict[str, Decimal]] = []
    for index, value in enumerate(orbit_values):
        fresh_records[f"epoch-{index}"] = value
        value_snapshots.append(fresh_records.copy())
    out_record_site = f"epoch-{first_out}"
    out_record_content = orbit_values[first_out]
    retained_after_escape = all(
        snapshot.get(out_record_site) == out_record_content
        for snapshot in value_snapshots[first_out:]
    )
    check(
        24,
        first_out == 14
        and abs(out_record_content - half) >= band
        and retained_after_escape,
        "T3 permanence role: once an out-of-band fresh-site record forms, later snapshots retain it",
        detail=f"first_out={first_out}",
    )

    probability_s_star = probability_s.subs(r, sp.Rational(1, 2))
    probability_d_star = probability_d.subs(r, sp.Rational(1, 2))
    agreement_probability = sp.simplify(
        probability_s_star**2 + probability_d_star**2
    )
    n = sp.symbols("n", integer=True, nonnegative=True)
    survival_identity = sp.simplify(
        agreement_probability**n - sp.Rational(1, 2) ** n
    )
    check(
        25,
        probability_s_star == probability_d_star == sp.Rational(1, 2)
        and agreement_probability == sp.Rational(1, 2)
        and survival_identity == 0,
        "conditional agreement arithmetic: per-filter probability 1/2 and n-filter fraction 2^-n",
    )

    psi_fixed = set(sp.solve(sp.Eq(r**2, r), r))
    psi_multiplier = sp.diff(r**2, r).subs(r, sp.Integer(1))
    check(
        26,
        psi_fixed == {sp.Integer(0), sp.Integer(1)}
        and psi_multiplier == 2
        and sp.Rational(1, 2) not in psi_fixed,
        "flow-class boundary: psi(r)=r^2 has fixed set {0,1} and is not selected here",
    )

    print(
        "SUMMARY T1: in the site-tagged monotone model, fresh sites and full "
        "retention are necessary after events are identified as record formation; "
        "no converse to full Admissibility."
    )
    print(
        "SUMMARY T2: constant orbit iff fixed point under the supplied map and "
        "common epoch-comparable readout rule."
    )
    print(
        "SUMMARY T3: exact finite-horizon bounds replace the withdrawn finite-time "
        "exactness claim; nonzero offsets survive every finite window."
    )
    print(
        "SUMMARY files: "
        "docs/RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md; "
        "scripts/frontier_record_permanence_double_registration_2026_07_11.py"
    )
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
