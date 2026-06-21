#!/usr/bin/env python3
"""Route-2 inverse-square covariance primitive candidate.

Safe claim:
  The same-domain O_h shell weights w_E=1/3 and w_T=1/2 give kappa=w_T/w_E=3/2.
  If, as a new source/readout primitive, the E/T center lift uses the dual
  inverse-square channel metric q_X proportional to w_X^-2, then

      lambda = q_E/q_T = (w_T/w_E)^2 = 9/4

  and the granted T-side Route-2 endpoint algebra gives
      q_E=15/8, rho_E=21/4, c_TE=-8/9.

  The runner also verifies the firewall: this inverse-square primitive is not
  supplied by the current repo notes. This is conditional support / target
  characterization, not current-surface closure.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from math import log


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PASS_COUNT = 0
FAIL_COUNT = 0


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


N_ARMS = Fraction(6, 1)
DIM_E = Fraction(2, 1)
DIM_T = Fraction(3, 1)
W_E = DIM_E / N_ARMS
W_T = DIM_T / N_ARMS
KAPPA = W_T / W_E
Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
TARGET_LAMBDA = Fraction(9, 4)


def lambda_for_power(power: int) -> Fraction:
    # q_X proportional to w_X^p gives q_E/q_T = (w_E/w_T)^p.
    base = W_E / W_T
    if power >= 0:
        return base ** power
    return Fraction(1, 1) / (base ** (-power))


def endpoint_from_lambda(lambda_et: Fraction) -> tuple[Fraction, Fraction, Fraction]:
    q_e = Q_T * lambda_et
    rho_e = 6 * (q_e - 1)
    c_te = S_TE * Q_T / q_e
    return q_e, rho_e, c_te


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    label: str


CURRENT_EDGES: tuple[Edge, ...] = (
    Edge("oh_shell_weights", "kappa_3_2", "same-domain O_h leverage"),
    Edge("route2_endpoint_algebra", "target_lambda_9_4_equivalent", "endpoint equivalence"),
    Edge("quadratic_invariant_route", "free_E_T_ratio", "Sym^2 trivial multiplicity leaves ratio free"),
    Edge("record_positivity_route", "norm_not_direction", "record/positivity fixes norm or bound"),
)

PRIMITIVE_EDGES: tuple[Edge, ...] = (
    Edge("inverse_square_covariance_primitive", "lambda_9_4", "q_X proportional to w_X^-2"),
    Edge("lambda_9_4", "q_E_15_8", "q_E=q_T lambda"),
    Edge("q_E_15_8", "rho_E_21_4", "rho_E=6(q_E-1)"),
    Edge("rho_E_21_4", "c_TE_minus_8_9", "granted T-side algebra"),
)

NEW_EDGE = Edge("oh_shell_weights", "inverse_square_covariance_primitive", "new dual-channel source/readout primitive")


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


def part1_weights_and_endpoint() -> None:
    print("\nPART 1: exact O_h weights and endpoint consequence")
    check("E projector per-arm weight is 1/3", W_E == Fraction(1, 3), f"w_E={W_E}")
    check("T1 projector per-arm weight is 1/2", W_T == Fraction(1, 2), f"w_T={W_T}")
    check("same-domain leverage kappa is 3/2", KAPPA == Fraction(3, 2), f"kappa={KAPPA}")

    dual_metric_ratio = (Fraction(1, 1) / (W_E * W_E)) / (Fraction(1, 1) / (W_T * W_T))
    q_e, rho_e, c_te = endpoint_from_lambda(dual_metric_ratio)
    check("inverse-square dual metric gives lambda=9/4", dual_metric_ratio == TARGET_LAMBDA)
    check("lambda=9/4 gives q_E=15/8", q_e == Fraction(15, 8), f"q_E={q_e}")
    check("lambda=9/4 gives rho_E=21/4", rho_e == Fraction(21, 4), f"rho_E={rho_e}")
    check("lambda=9/4 gives c_TE=-8/9", c_te == Fraction(-8, 9), f"c_TE={c_te}")


def part2_power_law_uniqueness() -> None:
    print("\nPART 2: unique power-law characterization")
    hits = []
    for power in range(-6, 7):
        lam = lambda_for_power(power)
        q_e, rho_e, c_te = endpoint_from_lambda(lam)
        print(f"  p={power:>2}: lambda={lam}, q_E={q_e}, rho_E={rho_e}, c_TE={c_te}")
        if lam == TARGET_LAMBDA:
            hits.append(power)

    base = float(W_E / W_T)
    target = float(TARGET_LAMBDA)
    real_power = log(target) / log(base)
    check("integer power scan hits only p=-2", hits == [-2], f"hits={hits}")
    check("real power-law solution is p=-2", abs(real_power + 2.0) < 1.0e-12, f"p={real_power:.12f}")
    check("equal, linear, quadratic, and inverse-linear laws miss target", all(lambda_for_power(p) != TARGET_LAMBDA for p in (0, 1, 2, -1)))


def part3_falsifier_table() -> None:
    print("\nPART 3: common same-domain laws are falsifiers")
    expected = {
        "equal response p=0": (0, Fraction(1, 1), Fraction(-1, 1)),
        "dimension-weight response p=1": (1, Fraction(2, 3), Fraction(-8, 3)),
        "quadratic response p=2": (2, Fraction(4, 9), Fraction(-34, 9)),
        "inverse-linear response p=-1": (-1, Fraction(3, 2), Fraction(3, 2)),
        "inverse-square response p=-2": (-2, Fraction(9, 4), Fraction(21, 4)),
    }
    for label, (power, expected_lambda, expected_rho) in expected.items():
        lam = lambda_for_power(power)
        _, rho_e, _ = endpoint_from_lambda(lam)
        check(label, lam == expected_lambda and rho_e == expected_rho, f"lambda={lam}, rho_E={rho_e}")


def part4_reachability() -> None:
    print("\nPART 4: typed reachability")
    current = CURRENT_EDGES
    with_primitive = CURRENT_EDGES + (NEW_EDGE,) + PRIMITIVE_EDGES
    check("current graph has no path to inverse-square primitive", not reachable(current, "oh_shell_weights", "inverse_square_covariance_primitive"))
    check("current graph has no path from O_h weights to rho_E=21/4", not reachable(current, "oh_shell_weights", "rho_E_21_4"))
    check("adding exactly the primitive reaches rho_E=21/4", reachable(with_primitive, "oh_shell_weights", "rho_E_21_4"))
    check("adding exactly the primitive reaches c_TE=-8/9", reachable(with_primitive, "oh_shell_weights", "c_TE_minus_8_9"))


def part5_quote_anchors() -> None:
    print("\nPART 5: current-surface firewall quote anchors")
    require_phrases(
        "kappa squared covariance gap",
        "QUARK_ROUTE2_QE_KAPPA_SQUARED_COVARIANCE_SHARPER_NO_GO_NARROW_NOTE_2026-06-10.md",
        (
            "single remaining free datum is the",
            "equivariance provably does not supply",
            "could still supply",
        ),
    )
    require_phrases(
        "quadratic route does not supply inverse square",
        "QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md",
        (
            "No named functional produces an inverse-square-of-projector-weight center lift.",
            "genuinely quadratic `O_h`-invariant functional does not force the covariance",
            "A future genuinely **nonlinear**",
        ),
    )
    require_phrases(
        "record positivity leaves direction free",
        "ROUTE2_READOUT_RECORD_POSITIVITY_DOES_NOT_FIX_RHO_E_NARROW_NO_GO_NOTE_2026-06-08.md",
        (
            "Selecting `rho_E` requires a shell-vs-center **distinguishing** input",
            "not a generic registration principle",
            "`rho_E` is the readout direction",
        ),
    )
    require_phrases(
        "readout map keeps endpoint triple open",
        "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md",
        (
            "it still does not derive the exact dimensionless readout triple",
            "the irreducible missing map entry is the `E`-channel ratio",
        ),
    )


def main() -> int:
    print("Route-2 inverse-square covariance primitive candidate")
    print("Scope: conditional target characterization; current surface does not supply primitive")
    part1_weights_and_endpoint()
    part2_power_law_uniqueness()
    part3_falsifier_table()
    part4_reachability()
    part5_quote_anchors()

    total = PASS_COUNT + FAIL_COUNT
    print(f"\nPASS={PASS_COUNT} FAIL={FAIL_COUNT} TOTAL={total}")
    if FAIL_COUNT:
        print("VERDICT: FAIL -- inverse-square primitive candidate certificate did not pass.")
        return 1
    print(
        "VERDICT: inverse-square covariance is an exact conditional primitive "
        "that would derive lambda=9/4 and rho_E=21/4, uniquely among power-law "
        "channel-weight rules; the current surface does not supply the primitive."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
