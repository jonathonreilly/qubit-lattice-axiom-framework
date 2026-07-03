#!/usr/bin/env python3
"""Route-2 two-pole channel-density covariance primitive candidate.

Safe claim:
  The Route-2 endpoint requires q_E/q_T=9/4.  With O_h channel weights
  w_E=1/3 and w_T=1/2, this is the same as q_X proportional to w_X^-2.

  This runner identifies a concrete same-domain primitive that would generate
  that inverse-square rule without importing color or fitted endpoint data:
  first divide the channel amplitude by its channel volume/weight, then take
  a quadratic covariance of that channel density.

      D_X = A_X / w_X
      q_X proportional to D_X^2

  gives q_X proportional to w_X^-2 and hence the endpoint triple.  The runner
  also verifies the firewall: current Route-2 notes do not supply the channel
  density normalization plus density-covariance readout primitive.  This is
  conditional support, not current-surface closure.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PASS_COUNT = 0
FAIL_COUNT = 0

W_E = Fraction(1, 3)
W_T = Fraction(1, 2)
R = W_E / W_T
Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
TARGET_LAMBDA = Fraction(9, 4)


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


def pow_fraction(base: Fraction, power: int) -> Fraction:
    if power >= 0:
        return base**power
    return Fraction(1, 1) / (base ** (-power))


def lambda_for_power(power: int) -> Fraction:
    return pow_fraction(R, power)


def endpoint_from_lambda(lambda_et: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = Q_T * lambda_et
    rho_e = 6 * (q_e - 1)
    c_te = S_TE * Q_T / q_e
    return q_e, rho_e, c_te


def pipeline_power(volume_divisions_per_factor: int, response_degree: int) -> int:
    """Exponent p for q_X proportional to (w_X^-d)^m."""
    return -volume_divisions_per_factor * response_degree


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("oh_channel_weights", "kappa_3_2", "derived O_h leverage"),
    Edge("route2_bilinear_carrier", "polynomial_channel_readout", "current K_R polynomial carrier"),
    Edge("polynomial_channel_readout", "one_pole_or_polynomial_bounds", "no inverse-square primitive supplied"),
    Edge("route2_endpoint_algebra", "rho_E_equivalent_to_lambda_9_4", "endpoint equivalence"),
)

PRIMITIVE_EDGES: tuple[Edge, ...] = (
    Edge("oh_channel_weights", "channel_density_normalization", "D_X=A_X/w_X"),
    Edge("channel_density_normalization", "density_covariance_readout", "q_X proportional to D_X^2"),
    Edge("density_covariance_readout", "lambda_9_4", "two-pole channel metric"),
    Edge("lambda_9_4", "q_E_15_8", "q_E=q_T lambda"),
    Edge("q_E_15_8", "rho_E_21_4", "rho_E=6(q_E-1)"),
    Edge("rho_E_21_4", "c_TE_minus_8_9", "granted T-side algebra"),
)


def reachable(edges: tuple[Edge, ...], start: str, target: str) -> bool:
    graph: dict[str, list[str]] = defaultdict(list)
    for edge in edges:
        graph[edge.source].append(edge.target)
    seen = {start}
    queue: deque[str] = deque([start])
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return False


def part1_endpoint_target() -> None:
    print("\nPART 1: exact target")
    check("channel weights are w_E=1/3 and w_T=1/2", W_E == Fraction(1, 3) and W_T == Fraction(1, 2), f"w_E/w_T={R}")
    check("inverse-square channel law gives lambda=9/4", lambda_for_power(-2) == TARGET_LAMBDA)
    q_e, rho_e, c_te = endpoint_from_lambda(TARGET_LAMBDA)
    check("lambda=9/4 gives q_E=15/8, rho_E=21/4, c_TE=-8/9", (q_e, rho_e, c_te) == (Fraction(15, 8), Fraction(21, 4), Fraction(-8, 9)), f"q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")


def part2_pipeline_variants() -> None:
    print("\nPART 2: pipeline variants")
    variants = {
        "raw amplitude response": 0,
        "single channel-density response": -1,
        "raw channel-volume quadratic response": 2,
        "channel-density covariance response": -2,
    }
    expected = {
        "raw amplitude response": (Fraction(1, 1), Fraction(-1, 1)),
        "single channel-density response": (Fraction(3, 2), Fraction(3, 2)),
        "raw channel-volume quadratic response": (Fraction(4, 9), Fraction(-34, 9)),
        "channel-density covariance response": (Fraction(9, 4), Fraction(21, 4)),
    }
    for label, power in variants.items():
        lam = lambda_for_power(power)
        _, rho_e, _ = endpoint_from_lambda(lam)
        check(label, (lam, rho_e) == expected[label], f"p={power}, lambda={lam}, rho_E={rho_e}")


def part3_two_pole_necessity_in_simple_pipeline() -> None:
    print("\nPART 3: simple normalize-then-power pipeline")
    hits = []
    covariance_hits = []
    one_normalization_hits = []
    for divisions in range(0, 5):
        for degree in range(1, 5):
            power = pipeline_power(divisions, degree)
            lam = lambda_for_power(power)
            if lam == TARGET_LAMBDA:
                hits.append((divisions, degree, power))
                if degree == 2:
                    covariance_hits.append((divisions, degree, power))
                if divisions == 1:
                    one_normalization_hits.append((divisions, degree, power))
            print(f"  divisions={divisions}, degree={degree}: p={power}, lambda={lam}")

    check("simple pipeline reaches target exactly when divisions*degree=2", sorted(hits) == [(1, 2, -2), (2, 1, -2)], f"hits={hits}")
    check("quadratic covariance route needs exactly one channel-volume division", covariance_hits == [(1, 2, -2)], f"covariance_hits={covariance_hits}")
    check("one channel-density normalization needs quadratic response", one_normalization_hits == [(1, 2, -2)], f"one_normalization_hits={one_normalization_hits}")


def part4_reachability_firewall() -> None:
    print("\nPART 4: typed reachability firewall")
    current = CURRENT_EDGES
    with_primitive = CURRENT_EDGES + PRIMITIVE_EDGES
    check("current graph has no path to density covariance readout", not reachable(current, "oh_channel_weights", "density_covariance_readout"))
    check("current graph has no path to rho_E=21/4", not reachable(current, "oh_channel_weights", "rho_E_21_4"))
    check("adding channel-density covariance primitive reaches rho_E=21/4", reachable(with_primitive, "oh_channel_weights", "rho_E_21_4"))
    check("adding channel-density covariance primitive reaches c_TE=-8/9", reachable(with_primitive, "oh_channel_weights", "c_TE_minus_8_9"))


def part5_quote_anchors() -> None:
    print("\nPART 5: current-surface quote anchors")
    require_phrases(
        "exact readout missing entry",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "the irreducible missing map entry is the `E`-channel ratio",
            "exact missing-map obstruction",
        ),
    )
    require_phrases(
        "kappa covariance bridge remains open",
        "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md",
        (
            "single remaining free datum is the covariance bridge",
            "future nonlinear tensor observable",
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
    require_phrases(
        "current bilinear carrier is polynomial definition",
        "S3_TIME_BILINEAR_TENSOR_PRIMITIVE_NOTE.md",
        (
            "is **defined** as a 2x2 matrix of polynomial expressions",
            "no positive theorem of primitive-ness for `K_R` is claimed",
        ),
    )


def main() -> int:
    print("Route-2 two-pole channel-density covariance primitive candidate")
    print("Scope: conditional support; current surface does not supply channel-density covariance primitive")
    part1_endpoint_target()
    part2_pipeline_variants()
    part3_two_pole_necessity_in_simple_pipeline()
    part4_reachability_firewall()
    part5_quote_anchors()

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    if FAIL_COUNT:
        print("VERDICT: FAIL -- two-pole density covariance candidate certificate did not pass.")
        return 1
    print(
        "VERDICT: conditional support. A channel-density covariance primitive "
        "D_X=A_X/w_X followed by q_X proportional to D_X^2 gives the exact "
        "inverse-square law and endpoint triple; the current surface does not "
        "supply that primitive."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
