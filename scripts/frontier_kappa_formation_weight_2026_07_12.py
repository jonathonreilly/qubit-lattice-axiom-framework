#!/usr/bin/env python3
"""Exact checks for the kappa/formation-weight coordinate theorem."""

from __future__ import annotations

import sys

from sympy import Eq, Float, Integer, Symbol, diff, simplify, solve


checks: list[tuple[str, bool]] = []


def check(label: str, condition: object) -> None:
    """Record and print one numbered exact check."""
    passed = bool(condition)
    checks.append((label, passed))
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] ({len(checks):02d}) {label}")


# Structural counts, not endpoint values.
singlet_directions = ("s",)
doublet_directions = ("d_plus", "d_minus")
registration_draws = ("first", "second")
n_s = Integer(len(singlet_directions))
n_d = Integer(len(doublet_directions))
n_registrations = Integer(len(registration_draws))
energy_ratio = simplify(n_d / n_s)

w = Symbol("w", positive=True)
r = Symbol("r", positive=True)
kappa = Symbol("kappa", positive=True)
q = Symbol("q", positive=True)

# Relocation companion's energy dictionary, with its factor derived from the
# supplied doublet-direction count.
r_of_w = simplify((1 - w) / (energy_ratio * w))
w_of_r = solve(Eq(r, r_of_w), w)[0]

# Kappa companion's positive, nonzero fixed-point branch.
flow = kappa * r**n_registrations
r_star = solve(Eq(flow, r), r)[0]
kappa_of_r = solve(Eq(flow, r), kappa)[0]
kappa_of_w = simplify(kappa_of_r.subs(r, r_of_w))
w_of_kappa = solve(Eq(kappa, kappa_of_w), w)[0]

check(
    "relocation dictionary inverts exactly",
    simplify(w_of_r.subs(r, r_of_w) - w) == 0,
)
check(
    "positive fixed branch is derived as r_star = 1/kappa",
    simplify(r_star - 1 / kappa) == 0,
)
check(
    "fixed-point substitution derives kappa = 2w/(1-w)",
    simplify(kappa_of_w - energy_ratio * w / (1 - w)) == 0,
)
check(
    "coordinate inversion derives w = kappa/(2+kappa)",
    simplify(w_of_kappa - kappa / (energy_ratio + kappa)) == 0,
)
check(
    "the two positive-domain coordinate maps compose to identity",
    simplify(w_of_kappa.subs(kappa, kappa_of_w) - w) == 0,
)
check(
    "the kappa flow fixes its symbolically solved interior branch",
    simplify(flow.subs(r, r_star) - r_star) == 0,
)
check(
    "the interior fixed-point multiplier is exactly two",
    simplify(diff(flow, r).subs(r, r_star) - n_registrations) == 0,
)

# Derive the two supplied-menu weights from their share laws. No endpoint is
# inserted on a derivation path.
w_cell = solve(Eq(w, 1 - w), w)[0]
w_carrier = solve(Eq(w / n_s, (1 - w) / n_d), w)[0]


def coordinate_triple(weight: object) -> tuple[object, object, object]:
    return (
        weight,
        simplify(kappa_of_w.subs(w, weight)),
        simplify(r_of_w.subs(w, weight)),
    )


cell_triple = coordinate_triple(w_cell)
carrier_triple = coordinate_triple(w_carrier)

expected_cell = (
    n_s / (n_s + n_s),
    energy_ratio,
    1 / energy_ratio,
)
expected_carrier = (
    n_s / (n_s + n_d),
    n_s / n_s,
    n_s / n_s,
)

check(
    f"equal-cell law maps exactly to (w,kappa,r_star) = {cell_triple}",
    cell_triple == expected_cell,
)
check(
    f"carrier-direction law maps exactly to (w,kappa,r_star) = {carrier_triple}",
    carrier_triple == expected_carrier,
)
check(
    "both derived menu images satisfy kappa*r_star = 1",
    all(
        simplify(k_value * r_value - 1) == 0
        for _, k_value, r_value in (cell_triple, carrier_triple)
    ),
)

# Direct i.i.d. composition of the same formation weights.
agreement_denominator_w = w**n_registrations + (1 - w) ** n_registrations
p_s_prime_w = w**n_registrations / agreement_denominator_w
p_d_prime_w = (1 - w) ** n_registrations / agreement_denominator_w
odds_w = simplify((1 - w) / w)
odds_prime_w = simplify(p_d_prime_w / p_s_prime_w)
r_prime_from_w = simplify(odds_prime_w / energy_ratio)
r_prime_in_r = simplify(r_prime_from_w.subs(w, w_of_r))
kappa_direct = solve(Eq(kappa * r**2, r_prime_in_r), kappa)[0]

check(
    "agreement-conditioned i.i.d. formation odds square exactly",
    simplify(odds_prime_w - odds_w**n_registrations) == 0,
)
check(
    "the relocation dictionary sends direct composition to r_prime = 2*r^2",
    simplify(r_prime_in_r - energy_ratio * r**n_registrations) == 0,
)
check(
    "the direct same-weight flow coefficient is derived as the doublet count",
    simplify(kappa_direct - energy_ratio) == 0,
)

# General-kappa reproduction uses a separately supplied registration law q.
odds_q = simplify((1 - q) / q)
q_required = solve(Eq(odds_q, kappa * r), q)[0]
agreement_denominator_q = q**n_registrations + (1 - q) ** n_registrations
p_s_prime_q = q**n_registrations / agreement_denominator_q
p_d_prime_q = (1 - q) ** n_registrations / agreement_denominator_q
odds_prime_q = simplify(p_d_prime_q / p_s_prime_q)
r_prime_general = simplify((odds_prime_q / kappa).subs(q, q_required))

check(
    "general-kappa registration law is q = 1/(1+kappa*r)",
    simplify(q_required - 1 / (1 + kappa * r)) == 0,
)
check(
    "separately identified general registration odds still square exactly",
    simplify(odds_prime_q - odds_q**n_registrations) == 0,
)
check(
    "general odds identification reproduces r_prime = kappa*r^2",
    simplify(r_prime_general - kappa * r**n_registrations) == 0,
)
check(
    "the general-kappa registration weight is equal-cell on its fixed graph",
    simplify(q_required.subs(r, r_star) - w_cell) == 0,
)

# If q and w are identified while retaining the relocation dictionary, the
# odds comparison itself derives kappa_direct; it is not kappa(w) generically.
kappa_same_law = solve(Eq(odds_w, kappa * r_of_w), kappa)[0]
w_overlap = solve(Eq(kappa_of_w, kappa_same_law), w)[0]
r_cell = cell_triple[2]
r_carrier = carrier_triple[2]
kappa_carrier_coordinate = carrier_triple[1]

check(
    "q=w plus the relocation dictionary forces only the direct coefficient",
    simplify(kappa_same_law - kappa_direct) == 0,
)
check(
    "direct and fixed-surface kappa coordinates overlap only at the derived equal-cell weight",
    simplify(w_overlap - w_cell) == 0,
)
check(
    "the overlap point is stationary under direct same-weight composition",
    simplify(r_prime_in_r.subs(r, r_cell) - r_cell) == 0,
)
check(
    "the carrier-share image is kappa=1 only on the fixed graph, not under direct composition",
    simplify(kappa_carrier_coordinate - kappa_direct) != 0
    and simplify(r_prime_in_r.subs(r, r_carrier) - r_carrier) != 0,
)

exact_expressions = (
    r_of_w,
    w_of_r,
    r_star,
    kappa_of_w,
    w_of_kappa,
    w_cell,
    w_carrier,
    odds_prime_w,
    r_prime_in_r,
    kappa_direct,
    q_required,
    r_prime_general,
    w_overlap,
)
check(
    "every derivation-path expression is exact (no SymPy Float atoms)",
    all(not expression.atoms(Float) for expression in exact_expressions),
)

pass_count = sum(passed for _, passed in checks)
fail_count = len(checks) - pass_count
verdict = "PASS" if fail_count == 0 else "FAIL"

print()
print(
    f"VERDICT: {verdict} — the fixed-surface coordinate identity and its "
    "direct-composition limitation are exact."
)
print(
    "T3 EXACT SURVIVING BRIDGE: i.i.d. composition of the same formation "
    "weights plus the relocation dictionary gives only r -> 2*r^2; a "
    "general kappa requires separately supplied odds (1-q)/q = kappa*r, "
    "while kappa = 2*w/(1-w) is the positive fixed-surface coordinate."
)
print(f"CHECK COUNT: {len(checks)} numbered exact checks")
print(
    "PROPOSED CLAIM_SCOPE: bounded_theorem — conditional coordinate identity "
    "and residual consolidation on the positive interior fixed-point surface; "
    "direct i.i.d. bridge restricted to the kappa=2 member."
)
print(
    "HOSTILE-AUDIT UNCERTAINTIES: the energy dictionary remains at Residual "
    "Atom 2 grade; the independence atom, SOCMLC-conditional menu "
    "classification, fixed-point applicability, and member-selection "
    "conditionals remain undischarged."
)
print(f"TOTAL: PASS={pass_count} FAIL={fail_count}")

sys.exit(0 if fail_count == 0 else 1)
