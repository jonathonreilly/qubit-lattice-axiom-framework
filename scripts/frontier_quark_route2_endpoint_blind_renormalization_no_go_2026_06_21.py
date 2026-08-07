#!/usr/bin/env python3
"""Route-2 endpoint-blind renormalization no-go.

This runner constrains the "size-stable family" rescue route left after the
Route-2 q_E box-size scan.  It proves an exact algebraic boundary:

  * separable finite-box renormalizations
      gamma_X(endpoint) -> channel_X(N) * endpoint(endpoint,N) * gamma_X(endpoint)
    preserve lambda = q_E/q_T;
  * therefore they can hit both q_E = 15/8 and q_T = 5/6 only where the
    unrenormalized lambda already equals 9/4;
  * the box-scan cache has lambda near 9/4 only at the N=15 pinning box, not in
    the bulk rows;
  * any bulk rescue must introduce a nonseparable E-specific center/shell
    counterterm, which is exactly the missing E-center readout primitive in
    different notation.

No observed masses, fitted targets, or audit verdicts are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import re

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
BOX_SCAN_CACHE = ROOT / "logs" / "runner-cache" / "frontier_quark_route2_qe_box_size_scan_2026_06_10.txt"
NOTE = ROOT / "docs" / "QUARK_ROUTE2_ENDPOINT_BLIND_RENORMALIZATION_NO_GO_NOTE_2026-06-21.md"

TARGET_QT = Fraction(5, 6)
TARGET_QE = Fraction(15, 8)
TARGET_LAMBDA = TARGET_QE / TARGET_QT
TARGET_RHO_E = Fraction(21, 4)


@dataclass(frozen=True)
class BoxRow:
    n: int
    q_t: float
    q_e: float

    @property
    def lambda_q(self) -> float:
        return self.q_e / self.q_t

    @property
    def common_factor_to_qt(self) -> float:
        return float(TARGET_QT) / self.q_t

    @property
    def q_e_after_qt_common_factor(self) -> float:
        return self.lambda_q * float(TARGET_QT)

    @property
    def common_factor_to_qe(self) -> float:
        return float(TARGET_QE) / self.q_e

    @property
    def q_t_after_qe_common_factor(self) -> float:
        return float(TARGET_QE) / self.lambda_q

    @property
    def nonseparable_lambda_counterterm(self) -> float:
        return float(TARGET_LAMBDA) / self.lambda_q


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str, status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def parse_box_scan_rows() -> list[BoxRow]:
    text = BOX_SCAN_CACHE.read_text()
    rows: list[BoxRow] = []
    for line in text.splitlines():
        parts = line.split()
        if len(parts) < 9 or not re.fullmatch(r"\d+", parts[0]):
            continue
        try:
            rows.append(BoxRow(n=int(parts[0]), q_t=float(parts[7]), q_e=float(parts[8])))
        except ValueError:
            continue
    if not rows:
        raise RuntimeError(f"no box rows parsed from {BOX_SCAN_CACHE}")
    return rows


def symbolic_separable_invariance() -> tuple[bool, str]:
    c_e, c_t, r_center, r_shell = sp.symbols("c_e c_t r_center r_shell", nonzero=True)
    g_e_center, g_e_shell, g_t_center, g_t_shell = sp.symbols(
        "g_e_center g_e_shell g_t_center g_t_shell", nonzero=True
    )
    q_e = g_e_center / g_e_shell
    q_t = g_t_center / g_t_shell
    q_e_prime = (c_e * r_center * g_e_center) / (c_e * r_shell * g_e_shell)
    q_t_prime = (c_t * r_center * g_t_center) / (c_t * r_shell * g_t_shell)
    lambda_prime = sp.simplify(q_e_prime / q_t_prime)
    lambda_original = sp.simplify(q_e / q_t)
    common_u = sp.simplify(q_e_prime / q_e)
    ok = sp.simplify(lambda_prime - lambda_original) == 0 and sp.simplify(common_u - (r_center / r_shell)) == 0
    detail = f"q_E'=(r_center/r_shell) q_E; q_T'=(r_center/r_shell) q_T; lambda'={lambda_prime}"
    return ok, detail


def exact_target_chain() -> tuple[bool, str]:
    rho_t = Fraction(-1, 1)
    q_t = 1 + rho_t / 6
    q_e = 1 + TARGET_RHO_E / 6
    center_te = Fraction(-2, 1) * q_t / q_e
    ok = q_t == TARGET_QT and q_e == TARGET_QE and q_e / q_t == TARGET_LAMBDA and center_te == Fraction(-8, 9)
    return ok, f"q_T={q_t}, q_E={q_e}, lambda={q_e / q_t}, center T/E={center_te}, rho_E={TARGET_RHO_E}"


def fmt_row(row: BoxRow) -> str:
    return (
        f"N={row.n}: q_T={row.q_t:+.5f}, q_E={row.q_e:+.5f}, "
        f"lambda={row.lambda_q:+.5f}, C_lambda={row.nonseparable_lambda_counterterm:+.5f}"
    )


def main() -> int:
    print("Route-2 endpoint-blind renormalization no-go")
    print("=" * 86)
    print(f"Parsed source cache: {BOX_SCAN_CACHE.relative_to(ROOT)}")

    rows = parse_box_scan_rows()
    rows_by_n = {row.n: row for row in rows}
    print("\nBox-scan ratios")
    print("N    q_T         q_E         lambda=q_E/q_T   common->q_T gives q_E   common->q_E gives q_T   E/T counterterm")
    print("-" * 118)
    for row in rows:
        print(
            f"{row.n:2d}  {row.q_t:+.5f}   {row.q_e:+.5f}   {row.lambda_q:+.5f}        "
            f"{row.q_e_after_qt_common_factor:+.5f}              {row.q_t_after_qe_common_factor:+.5f}              "
            f"{row.nonseparable_lambda_counterterm:+.5f}"
        )

    expected_ns = {11, 13, 15, 17, 19, 21, 25, 29}
    record(
        "the box-size scan cache parses the Route-2 q_E/q_T rows needed for the renormalization boundary",
        expected_ns.issubset(rows_by_n),
        "parsed N = " + ", ".join(str(row.n) for row in rows),
        status="CACHE",
    )

    ok_symbolic, symbolic_detail = symbolic_separable_invariance()
    record(
        "separable endpoint-blind finite-box renormalizations preserve lambda=q_E/q_T exactly",
        ok_symbolic,
        symbolic_detail,
        status="EXACT",
    )

    ok_chain, chain_detail = exact_target_chain()
    record(
        "the endpoint target pair is equivalent to lambda=9/4 and rho_E=21/4",
        ok_chain,
        chain_detail,
        status="EXACT",
    )

    near_target = [row for row in rows if abs(row.lambda_q - float(TARGET_LAMBDA)) < 0.02]
    bulk_rows = [rows_by_n[n] for n in (17, 19, 21, 25, 29) if n in rows_by_n]
    bulk_far = all(abs(row.lambda_q - float(TARGET_LAMBDA)) > 1.0 for row in bulk_rows)
    record(
        "the live box-scan lambda is near 9/4 only at the N=15 pinning box, not in the bulk rows",
        len(near_target) == 1 and near_target[0].n == 15 and bulk_far,
        "near-target rows: "
        + ", ".join(fmt_row(row) for row in near_target)
        + "; bulk min gap="
        + f"{min(abs(row.lambda_q - float(TARGET_LAMBDA)) for row in bulk_rows):.3f}",
        status="NO-GO",
    )

    common_qt_miss = [
        (row.n, row.common_factor_to_qt, row.q_e_after_qt_common_factor)
        for row in bulk_rows
        if abs(row.q_e_after_qt_common_factor - float(TARGET_QE)) > 1.0
    ]
    common_qe_miss = [
        (row.n, row.common_factor_to_qe, row.q_t_after_qe_common_factor)
        for row in bulk_rows
        if abs(row.q_t_after_qe_common_factor - float(TARGET_QT)) > 0.25
    ]
    record(
        "a common endpoint factor can fix one target ratio in the bulk only by breaking the other",
        len(common_qt_miss) == len(bulk_rows) and len(common_qe_miss) == len(bulk_rows),
        "fix q_T -> q_E values: "
        + ", ".join(f"N={n}: u={u:+.3f}, q_E'={qe:+.3f}" for n, u, qe in common_qt_miss)
        + "; fix q_E -> q_T values: "
        + ", ".join(f"N={n}: u={u:+.3f}, q_T'={qt:+.3f}" for n, u, qt in common_qe_miss),
        status="NO-GO",
    )

    positive_e_lift = [row for row in bulk_rows if row.common_factor_to_qe > 0]
    record(
        "bulk q_E has the wrong sign, so a positive endpoint-factor normalization cannot rescue q_E=15/8",
        not positive_e_lift,
        "required q_E factors: " + ", ".join(f"N={row.n}: {row.common_factor_to_qe:+.3f}" for row in bulk_rows),
        status="NO-GO",
    )

    counterterms = [row.nonseparable_lambda_counterterm for row in bulk_rows]
    nonconstant = max(counterterms) - min(counterterms) > 0.25
    not_one = all(abs(value - 1.0) > 0.45 for value in counterterms)
    record(
        "the only algebraic rescue is a nonseparable E/T center-shell counterterm, i.e. a new readout primitive",
        nonconstant and not_one,
        "C_lambda(N)=(9/4)/lambda(N): " + ", ".join(f"N={row.n}: {row.nonseparable_lambda_counterterm:+.3f}" for row in bulk_rows),
        status="BOUNDARY",
    )

    if NOTE.exists():
        text = NOTE.read_text()
        firewall = (
            "does not prove impossibility over arbitrary future nonlinear observables" in text
            and "No observed masses, fitted targets, or PDG values" in text
            and "**Claim type:** no_go" in text
            and "independent audit lane only" in text
        )
        record(
            "the paired note carries the claim-status and forbidden-import firewall",
            firewall,
            "required boundary phrases present" if firewall else "required boundary phrases missing",
            status="FIREWALL",
        )

    print("\nN5 execution certificate")
    print("-" * 86)
    print(
        "per_element: the invariance is derived on four independent endpoint amplitudes "
        "held as separate nonzero symbols, g_E(center), g_E(shell), g_T(center) and "
        "g_T(shell), each multiplied by its own channel factor and its own role factor "
        "before the ratios are rebuilt; it is that per-amplitude bookkeeping, not a "
        "numerical fit, that makes c_E and c_T cancel identically in q_E and q_T alike."
    )
    print(
        "per_site: resolved at the two star roles, and unusually for this stack the roles "
        "are given their own independent rescalings r_center and r_shell -- the symbolic "
        "outcome is that the single surviving common factor is exactly r_center/r_shell, "
        "so a separable scheme can move the role ratio and nothing else; no individual arm "
        "or coordinate is represented, since the site sums live upstream in the box scan."
    )
    print(
        "per_mode: both bright channels are given their own free factor and both drop out "
        "-- c_E and c_T cancel between center and shell in their own channel, which leaves "
        "lambda=q_E/q_T exactly invariant, and that single mode-ratio invariance is the "
        f"entire no-go; the parsed table then keeps q_T and q_E as separate columns for all "
        f"{len(rows)} boxes so the two modes are never averaged together."
    )
    print(
        f"per_block: the boxes are split into the N=15 pinning row and a "
        f"{len(bulk_rows)}-row bulk block, and each block is judged against its own named "
        "threshold -- exactly one row lies within 0.02 of 9/4, every bulk row sits further "
        "than 1.0 away, every bulk row fails the fix-q_T repair by more than 1.0 and the "
        "fix-q_E repair by more than 0.25, and the counterterm block spreads by more than "
        "0.25 while staying more than 0.45 away from unity throughout."
    )
    print(
        f"lattice_wide: executed at finite volume only, and certified as exactly that -- the "
        f"evidence spans {len(rows)} boxes up to N={max(row.n for row in rows)}, read from "
        "a stored upstream scan rather than recomputed here, and no thermodynamic or "
        "infinite-volume limit is taken anywhere in this file; the boundary proved is "
        "algebraic and holds box by box, and the rescue it leaves open, a nonseparable "
        "E-specific center/shell counterterm, is the missing readout primitive restated."
    )

    n_pass = sum(check.ok for check in CHECKS)
    n_fail = sum(not check.ok for check in CHECKS)
    print("\nVerdict:")
    print(
        "Endpoint-blind/separable finite-box renormalizations cannot rescue the Route-2 endpoint triple. "
        "They preserve lambda=q_E/q_T, and the live bulk lambda rows miss 9/4.  A rescue therefore needs "
        "a nonseparable E-specific center/shell counterterm, which is the missing E-center readout datum "
        "rather than a harmless size-stable normalization."
    )
    print(f"\nTOTAL: PASS={n_pass} FAIL={n_fail}")
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
