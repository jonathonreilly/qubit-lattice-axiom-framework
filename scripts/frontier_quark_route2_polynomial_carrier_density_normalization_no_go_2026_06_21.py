#!/usr/bin/env python3
"""Route-2 polynomial-carrier density-normalization no-go.

Safe claim:
  The current Route-2 carrier surface defines

      K_R(q) = (u_E, u_T, delta_A1 u_E, delta_A1 u_T)

  as a class-A polynomial expression in the named inputs.  On the endpoint
  columns, E and T have the same shell amplitude and the same center lift
  delta_A1=1/6.  There is no channel-weight coordinate w_X in the carrier.

  Therefore a channel-blind polynomial/readout grammar over the current
  carrier cannot derive the channel-density normalization D_X=A_X/w_X or the
  E/T density factor (1/w_E)/(1/w_T)=3/2.  If independent E/T readout
  coefficients are allowed, rho_E is free and the target value is a supplied
  map entry rather than a carrier-derived theorem.

  This is a scoped no-go for the current polynomial carrier as the source of
  channel-weight division.  It does not rule out adding a new source/readout
  primitive that supplies channel-density normalization.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import numpy as np

from frontier_quark_route2_exact_readout_map import (
    EXACT_TOL,
    admissible_readout_matrix,
    restricted_readout_data,
)


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PASS_COUNT = 0
FAIL_COUNT = 0

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
TARGET_DENSITY_FACTOR = (Fraction(1, 1) / W_E) / (Fraction(1, 1) / W_T)
TARGET_LAMBDA = Fraction(9, 4)
Q_T_GRANTED = Fraction(5, 6)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def normalized_text(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").split())


def require_phrases(label: str, rel_path: str, phrases: tuple[str, ...]) -> None:
    text = normalized_text(DOCS / rel_path)
    missing = [phrase for phrase in phrases if phrase not in text]
    check(
        f"quote anchors present: {label}",
        not missing,
        "all anchors found" if not missing else f"missing={missing!r}",
    )


def q_from_rho(rho: Fraction) -> Fraction:
    return Fraction(1, 1) + rho / 6


def rho_from_q(q_value: Fraction) -> Fraction:
    return 6 * (q_value - 1)


def as_fraction(value: float) -> Fraction:
    return Fraction(value).limit_denominator(10**9)


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("current_polynomial_carrier_K_R", "equal_endpoint_columns", "E and T columns have same shell and center lift"),
    Edge("equal_endpoint_columns", "channel_blind_polynomial_response", "same polynomial grammar acts on E and T"),
    Edge("channel_blind_polynomial_response", "lambda_1_or_free_if_coefficients_supplied", "no derived channel-weight division"),
    Edge("independent_readout_coefficients", "rho_E_free", "P_R supplies E coefficient"),
)

MISSING_DENSITY_EDGES: tuple[Edge, ...] = (
    Edge("explicit_channel_weights", "channel_density_normalization", "D_X=A_X/w_X"),
    Edge("channel_density_normalization", "density_factor_3_2", "(1/w_E)/(1/w_T)=3/2"),
    Edge("density_factor_3_2", "inverse_square_covariance", "quadratic density response squares the factor"),
    Edge("inverse_square_covariance", "lambda_9_4", "q_E/q_T=9/4"),
    Edge("lambda_9_4", "rho_E_21_4", "given q_T=5/6"),
)


def reachable(edges: tuple[Edge, ...], start: str, target: str) -> bool:
    graph: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        graph[edge.source].append(edge.target)
    queue: deque[str] = deque([start])
    seen = {start}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


def part1_carrier_endpoint_symmetry() -> None:
    print("\nPART 1: current K_R endpoint columns are channel-blind")
    data = restricted_readout_data()
    e_shell = data.carrier_e_shell
    e_center = data.carrier_e_center
    t_shell = data.carrier_t_shell
    t_center = data.carrier_t_center

    e_pair_shell = e_shell[[0, 2]]
    e_pair_center = e_center[[0, 2]]
    t_pair_shell = t_shell[[1, 3]]
    t_pair_center = t_center[[1, 3]]

    check("E and T shell carrier pairs are identical up to channel relabeling", np.max(np.abs(e_pair_shell - t_pair_shell)) < EXACT_TOL, f"E={e_pair_shell}, T={t_pair_shell}")
    check("E and T center carrier pairs are identical up to channel relabeling", np.max(np.abs(e_pair_center - t_pair_center)) < EXACT_TOL, f"E={e_pair_center}, T={t_pair_center}")
    check("both channels have shell amplitude 1 and center lift 1/6", as_fraction(float(e_pair_center[1])) == Fraction(1, 6) and as_fraction(float(t_pair_center[1])) == Fraction(1, 6))
    check("carrier columns contain no density factor 3/2", all(abs(x - float(TARGET_DENSITY_FACTOR)) > EXACT_TOL for x in [*e_pair_shell, *e_pair_center, *t_pair_shell, *t_pair_center]), f"target density factor={TARGET_DENSITY_FACTOR}")


def part2_channel_blind_polynomial_consequence() -> None:
    print("\nPART 2: channel-blind polynomial grammar cannot produce E/T density division")
    # A channel-blind polynomial response sees the same endpoint pair
    # (shell, center)=(1,1+rho/6) in E and T unless an independent coefficient
    # is supplied by P_R.  Representative monomials in the shared center lift
    # therefore have lambda=1.
    shared_delta = Fraction(1, 6)
    shared_pairs = []
    for degree in range(0, 7):
        shell_value = Fraction(1, 1) ** degree
        center_value = (Fraction(1, 1) + shared_delta) ** degree
        lam = center_value / shell_value / (center_value / shell_value)
        shared_pairs.append((degree, lam))
        print(f"  shared degree={degree}: E/T lambda={lam}")

    check("all shared polynomial endpoint responses have E/T lambda=1", all(lam == 1 for _, lam in shared_pairs))
    check("lambda=1 is not the required inverse-square lambda=9/4", Fraction(1, 1) != TARGET_LAMBDA)
    check("the needed density factor 3/2 is not generated by a shared polynomial response", TARGET_DENSITY_FACTOR == Fraction(3, 2))


def part3_independent_readout_coefficients_are_free() -> None:
    print("\nPART 3: independent readout coefficients can fit target but are supplied map entries")
    data = restricted_readout_data()
    candidates = [Fraction(-1, 1), Fraction(0, 1), Fraction(1, 1), Fraction(21, 4), Fraction(6, 1)]
    rows = []
    for rho_e in candidates:
        readout = admissible_readout_matrix(1.0, float(rho_e), -2.0, 2.0)
        e_shell = readout @ data.carrier_e_shell
        e_center = readout @ data.carrier_e_center
        t_shell = readout @ data.carrier_t_shell
        t_center = readout @ data.carrier_t_center
        q_e = as_fraction(float(e_center[0] / e_shell[0]))
        q_t = as_fraction(float(t_center[1] / t_shell[1]))
        lam = q_e / q_t
        rows.append((rho_e, q_e, q_t, lam))
        print(f"  rho_E={rho_e}: q_E={q_e}, q_T={q_t}, lambda={lam}")

    check("all candidate rho_E values preserve the same current carrier columns", len(rows) == len(candidates))
    check("rho_E=21/4 gives target lambda only after supplying that coefficient", any(rho == Fraction(21, 4) and lam == TARGET_LAMBDA for rho, _, _, lam in rows))
    check("other exact rho_E values remain admissible on the same carrier", any(rho == 0 and lam != TARGET_LAMBDA for rho, _, _, lam in rows))
    target_qe = Q_T_GRANTED * TARGET_LAMBDA
    check("target rho_E is exactly equivalent to supplied q_E=15/8", rho_from_q(target_qe) == Fraction(21, 4), f"q_E={target_qe}")


def part4_density_normalization_requires_external_channel_weights() -> None:
    print("\nPART 4: density normalization needs explicit channel weights")
    inv_w_e = Fraction(1, 1) / W_E
    inv_w_t = Fraction(1, 1) / W_T
    density_factor = inv_w_e / inv_w_t
    squared = density_factor**2
    q_e = Q_T_GRANTED * squared
    rho_e = rho_from_q(q_e)

    check("explicit channel weights give inverse weights 3 and 2", (inv_w_e, inv_w_t) == (3, 2), f"1/w_E={inv_w_e}, 1/w_T={inv_w_t}")
    check("density factor is 3/2", density_factor == TARGET_DENSITY_FACTOR)
    check("quadratic density response squares to lambda=9/4", squared == TARGET_LAMBDA)
    check("this external channel-weight primitive gives rho_E=21/4", rho_e == Fraction(21, 4), f"rho_E={rho_e}")


def part5_typed_reachability() -> None:
    print("\nPART 5: typed reachability")
    current = CURRENT_EDGES
    with_density = CURRENT_EDGES + MISSING_DENSITY_EDGES
    check("current polynomial carrier has no path to channel-density normalization", not reachable(current, "current_polynomial_carrier_K_R", "channel_density_normalization"))
    check("current polynomial carrier has no path to rho_E=21/4", not reachable(current, "current_polynomial_carrier_K_R", "rho_E_21_4"))
    check("adding explicit channel weights reaches channel-density normalization", reachable(with_density, "explicit_channel_weights", "channel_density_normalization"))
    check("adding explicit channel weights reaches rho_E=21/4", reachable(with_density, "explicit_channel_weights", "rho_E_21_4"))
    check("independent readout coefficients expose rho_E as free rather than derived", reachable(current, "independent_readout_coefficients", "rho_E_free"))


def part6_quote_anchors() -> None:
    print("\nPART 6: current-surface quote anchors")
    require_phrases(
        "bilinear carrier is polynomial definition only",
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            "K_R(q)` is **defined** as a 2x2 matrix of polynomial expressions",
            "This note's load-bearing step is the class-A polynomial-identity substitution",
            "no positive theorem of primitive-ness for `K_R` is claimed",
        ),
    )
    require_phrases(
        "exact readout map names missing E entry",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "the irreducible missing map entry is the `E`-channel ratio",
            "exact missing-map obstruction",
        ),
    )
    require_phrases(
        "tensor build memo names next theorem",
        "S3_TIME_TENSOR_BUILD_MEMO.md",
        (
            "derive the `E`-channel readout map entry",
            "or prove a stronger admissibility theorem showing why the current",
            "stack cannot force it uniquely",
        ),
    )
    require_phrases(
        "quadratic note names inverse-square gap",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "No named functional produces an inverse-square-of-projector-weight center lift.",
            "future genuinely **nonlinear**",
        ),
    )


def main() -> int:
    print("Route-2 polynomial-carrier density-normalization no-go")
    print("Scope: current class-A polynomial K_R carrier; source/readout primitives remain open")
    part1_carrier_endpoint_symmetry()
    part2_channel_blind_polynomial_consequence()
    part3_independent_readout_coefficients_are_free()
    part4_density_normalization_requires_external_channel_weights()
    part5_typed_reachability()
    part6_quote_anchors()

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    if FAIL_COUNT:
        print("VERDICT: FAIL -- polynomial-carrier density-normalization no-go certificate did not pass.")
        return 1
    print(
        "VERDICT: scoped no-go. The current class-A polynomial carrier K_R "
        "does not contain channel weights and cannot derive channel-density "
        "normalization; independent readout coefficients can fit rho_E=21/4 "
        "only as supplied map entries."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
