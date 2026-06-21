"""Route-2 q_E box-path interpolation family check.

This runner tests a bounded rescue route for the Route-2 E-center lift:
instead of only the fixed-radius boundary-removal path (p=0) and the
box-proportional path (p=1), scan the rational interpolation family

    r_N(p) = 4.25 * ((N - 2) / 13)^p,  p in {0, 1/4, 1/2, 3/4, 1}.

The target q_E = 15/8 appears only as a comparator.  No quark masses, fitted
values, or nearest-rational selectors are used.  The conclusion is deliberately
bounded: this finite grid does not prove anything about every possible
radius/path functional; it prunes the specific interpolation-family rescue of
the N=15 measured-calibration coincidence.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Dict, Iterable, List, Tuple

import frontier_quark_route2_qe_box_size_scan_2026_06_10 as box

PASS = 0
FAIL = 0

TARGET_QE = 15.0 / 8.0
TARGET_QT = 5.0 / 6.0
P_GRID: Tuple[Fraction, ...] = (
    Fraction(0, 1),
    Fraction(1, 4),
    Fraction(1, 2),
    Fraction(3, 4),
    Fraction(1, 1),
)
N_GRID: Tuple[int, ...] = (17, 21, 25)


@dataclass(frozen=True)
class Row:
    N: int
    p: Fraction
    radius: float
    q_T: float
    q_E: float
    beta_E_shell: float
    beta_E_center: float


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def plabel(p: Fraction) -> str:
    return "0" if p == 0 else "1" if p == 1 else f"{p.numerator}/{p.denominator}"


def radius_for(N: int, p: Fraction) -> float:
    return box.PROBE_RAD * ((N - 2) / 13.0) ** float(p)


def rows_by_p(rows: Iterable[Row]) -> Dict[Fraction, List[Row]]:
    out: Dict[Fraction, List[Row]] = {p: [] for p in P_GRID}
    for row in rows:
        out[row.p].append(row)
    for p in out:
        out[p].sort(key=lambda r: r.N)
    return out


def main() -> int:
    print("ROUTE-2 q_E BOX-PATH INTERPOLATION FAMILY: BOUNDED NO-GO CHECK")
    print("=" * 82)
    print("family: r_N(p) = 4.25 * ((N - 2)/13)^p")
    print("p-grid:", ", ".join(plabel(p) for p in P_GRID))
    print("N-grid:", ", ".join(str(N) for N in N_GRID))
    print("comparator targets: q_E=15/8, q_T=5/6; comparators are not proof inputs")
    print()

    boxes = {N: box.make_box(N) for N in (15, *N_GRID)}
    anchor = box.gammas(boxes[15], rad=box.PROBE_RAD)

    rows: List[Row] = []
    for p in P_GRID:
        for N in N_GRID:
            rad = radius_for(N, p)
            g = box.gammas(boxes[N], rad=rad)
            rows.append(
                Row(
                    N=N,
                    p=p,
                    radius=rad,
                    q_T=float(g["q_T"]),
                    q_E=float(g["q_E"]),
                    beta_E_shell=float(g["beE_shell"]),
                    beta_E_center=float(g["beE_center"]),
                )
            )

    by_p = rows_by_p(rows)

    check(
        "I1 (common N=15 origin): every interpolation path passes through the same N=15 radius, and "
        "the landed measured-calibration coincidence is reproduced before varying N",
        abs(anchor["q_E"] - TARGET_QE) < 2.0e-3 and abs(anchor["q_T"] - TARGET_QT) < 3.0e-5,
        f"N=15 q_E={anchor['q_E']:+.9f} vs 15/8={TARGET_QE:+.9f}; "
        f"q_T={anchor['q_T']:+.9f} vs 5/6={TARGET_QT:+.9f}; r_15(p)=4.25 for all p",
    )

    print("\n  p      N    radius       q_T          q_E        beta_E(shell)")
    for p in P_GRID:
        for row in by_p[p]:
            print(
                f"  {plabel(p):>4s}  {row.N:3d}  {row.radius:9.5f}  "
                f"{row.q_T:+11.6f} {row.q_E:+12.6f} {row.beta_E_shell:+.6e}"
            )

    fixed = by_p[Fraction(0, 1)]
    prop = by_p[Fraction(1, 1)]
    fixed_ok = (
        all(row.q_E < 0 for row in fixed)
        and fixed[-1].q_E < fixed[0].q_E
        and abs(fixed[-1].q_E - TARGET_QE) > 5.0
    )
    prop_ok = (
        abs(prop[-1].q_E - 1.0) < 0.05
        and abs(prop[-1].q_T - 1.0) < 0.05
        and abs(prop[-1].q_E - TARGET_QE) > 0.75
    )
    check(
        "I2 (endpoint consistency): the p=0 and p=1 endpoints reproduce the known failure modes "
        "rather than hiding the target",
        fixed_ok and prop_ok,
        f"p=0 q_E over N={['%+.3f' % r.q_E for r in fixed]} (runs negative); "
        f"p=1 terminal (q_T,q_E)=({prop[-1].q_T:+.3f},{prop[-1].q_E:+.3f}) near (1,1)",
    )

    tracking_details = []
    sampled_paths_fail = True
    for p in P_GRID:
        qes = [row.q_E for row in by_p[p]]
        terminal_error = abs(qes[-1] - TARGET_QE)
        span = max(qes) - min(qes)
        tracks_target = all(abs(q - TARGET_QE) < 0.25 for q in qes)
        terminal_close = terminal_error < 0.5
        sampled_paths_fail = sampled_paths_fail and not (tracks_target or terminal_close)
        tracking_details.append(
            f"p={plabel(p)}: q_E={['%+.3f' % q for q in qes]}, "
            f"N25 gap={terminal_error:.3f}, span={span:.3f}"
        )
    check(
        "I3 (sampled interpolation paths): no sampled p-path tracks q_E=15/8 across N or lands near "
        "15/8 at the largest sampled box",
        sampled_paths_fail,
        "; ".join(tracking_details),
    )

    denom_details = []
    denominator_unstable = True
    for p in P_GRID[1:]:
        vals = [row.beta_E_shell for row in by_p[p]]
        sign_flip_or_near_zero = (min(vals) < 0.0 < max(vals)) or min(abs(v) for v in vals) < 2.0e-6
        denominator_unstable = denominator_unstable and sign_flip_or_near_zero
        signs = ["+" if v > 0 else "-" if v < 0 else "0" for v in vals]
        denom_details.append(f"p={plabel(p)} signs={signs}, min|beta_E(shell)|={min(abs(v) for v in vals):.2e}")
    check(
        "I4 (mechanism check): the non-fixed interpolants inherit sign/near-zero denominator sensitivity "
        "rather than a stable E-center source primitive",
        denominator_unstable,
        "; ".join(denom_details),
    )

    terminal = [(abs(by_p[p][-1].q_E - TARGET_QE), p, by_p[p][-1]) for p in P_GRID]
    terminal.sort(key=lambda item: item[0])
    best_gap, best_p, best_row = terminal[0]
    check(
        "I5 (bounded verdict): within this rational exponent grid, the best largest-box q_E is still "
        "far from 15/8, so the interpolation-family rescue is pruned",
        best_gap > 0.5,
        f"best N=25 entry: p={plabel(best_p)}, q_E={best_row.q_E:+.6f}, "
        f"gap to 15/8={best_gap:.6f}; bounded to this p-grid and N-grid",
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: bounded no-go/support boundary.  The N=15 q_E ~= 15/8 coincidence is common to the "
        "interpolation family because all paths have r_15=4.25, but the sampled rational exponent "
        "paths p in {0,1/4,1/2,3/4,1} do not carry that value toward a stable large-box target.  The "
        "p=0 endpoint runs negative, p=1 tends toward (q_T,q_E) near (1,1), and the interior paths are "
        "dominated by beta_E(shell) sign/near-zero sensitivity.  This prunes the finite box-path "
        "interpolation rescue of the Route-2 E-center lift; it does not derive beta_E/alpha_E=21/4 "
        "and does not rule out a genuinely new source-domain or readout-map primitive."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
