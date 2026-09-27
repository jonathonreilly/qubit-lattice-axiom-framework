---
claim_id: admissibility_rule_the_stretch_rules_hops_decay_exponentially_below_root_two_and_its_decay_length_diverges_only_at_the_rules_ends_bounded_theorem_note_2026-09-28
claim_type: bounded_theorem
claim_scope: "WITHIN block 69's two-step coupling as landed, for block 184's stretch rule (pushed; the rule fixed by the free-particle law of block 185): (T1) with M = 2k, E = 2k0 and e = 1 - l^2 the rule is the inversion relation M = E - e sin E, and the slope of its squared energy u = F^2 is du/dk = sin E = sum_n (2/(n e)) J_n(n e) sin(nM), so the hops of du/dk of range 2n are (2/(n e)) J_n(n e) (the classical series, checked here through e^7 by exact inversion); (T2) the nearest singularity of E(M) off the real line is the fold 1 - e cos E = 0, at |Im M| = kappa = arccosh(1/|e|) - sqrt(1 - e^2), so u is analytic for |Im k| < kappa/2 and its hops of range 2n decay like exp(-n kappa); (T3) kappa > 0 for every 0 < l^2 < 2 (and the reach is finite at l = 1), kappa depends only on |1 - l^2|, kappa = ln(2/|e|) - 1 + O(e^2) near l = 1, and kappa = s^3/3 + s^5/5 + ... with s = sqrt(1 - e^2) near the rule's ends l -> 0 and l -> sqrt 2, where the decay length diverges like 3/s^3. So the rule is exponentially local at every stretch strictly inside its domain, but not uniformly so. The exact decay rates of the walk's own hops F are not computed. The supervisor's own derivation, unrefereed. Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
runner: scripts/admissibility_rule_the_stretch_rules_hops_decay_exponentially_2026_09_28.py
---

# The stretch rule's hops decay exponentially below √2, and its decay length diverges only at the rule's ends

**Date:** 2026-09-28
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 69 as landed; block 184 is pushed and placed, and the facts used from it are re-derived; the supervisor's own derivation, unrefereed; nothing adopted or registered; unaudited)

This note works within block 69 as landed on main and asks how local block 184's stretch rule is: how fast its hops fall off with range; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 184 (pushed) found the stretch rule under which every wave slows as a free particle does (block 185). It showed that the rule has hops of every length at every stretch `ℓ ≠ 1`, and that they decay exponentially. It did not say how fast. A same-family strategy panel (2026-09-27) named that as the decisive test: is the rule a local law, and uniformly so?

- **T1: the hops in closed form.** With `M = 2k`, `E = 2k₀` and `e = 1 − ℓ²`, the rule is the inversion relation `M = E − e sin E`. The slope of its squared energy is `du/dk = sin E = Σ_n (2/(ne)) J_n(ne) sin(nM)`. So the hop of range `2n` is `(2/(ne)) J_n(ne)`.
- **T2: the decay rate.** The nearest singularity is the fold `1 − e cos E = 0`, at distance `κ = arccosh(1/|e|) − √(1 − e²)` from the real line in `M`. So the hops of range `2n` fall off like `exp(−nκ)`.
- **T3: where it is local.** `κ > 0` at every stretch with `0 < ℓ² < 2`, and it depends only on `|1 − ℓ²|`. Near `ℓ = 1`, `κ = ln(2/|e|) − 1 + O(e²)`, and at `ℓ = 1` the reach is finite. Near the rule's ends, `ℓ → 0` or `ℓ → √2`, `κ ≈ s³/3` with `s = √(1 − e²)`. So the decay length grows without bound there.

In plain terms: the stretched walk hops to every distance, but the long hops are exponentially weak, and a formula says exactly how weak. For small stretches they are weak indeed. As the stretch approaches √2 (or the lattice is squeezed toward nothing), the hops reach farther and farther, and at the ends they stop being exponentially weak. So the rule is a local law everywhere inside its range, but not uniformly: how far it reaches depends on how far the lattice has been stretched.

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-27) is used for three things: no possibility or site is privileged; the Lattice axiom's sites, bonds and translations; and the memo's silence on amplitude dynamics. Block 69 is used as landed on main; block 184 is pushed and placed, and the facts used from it are re-derived (runner B1).

- **The coupling** (block 69), quoted: "For a uniform strain, `H(k) = Σ_a σ_a[s_a + c_a Σ_j B_a^j s_jc_j]`"; and "Common corner quadratic forms are a leading-order result and do not determine a nonlinear completion."
- **The rule** (block 184, pushed). Per axis `k = k₀ + ((ℓ² − 1)/2) sin 2k₀` and `F = sin k₀ (sin² k₀ + ℓ² cos² k₀)^{1/2}`, with `u = F²` and `du/dk = sin 2k₀`.
- **Hops.** A hop of range `r` is the coefficient of `sin(rk)` or `cos(rk)` in the trigonometric series of a dispersion or its slope.

In the literature, `M = E − e sin E` is Kepler's equation. Its solution has the series `sin E = Σ_n (2/(ne)) J_n(ne) sin(nM)` in Bessel functions, and `J_n(ne)` behaves like `exp(−nκ)/√(2πn√(1 − e²))` for large `n` (Carlini's formula). This note uses none of it as authority. It checks the series through order `e⁷` exactly, and derives the rate from the fold.

## Domain qualifications

- The rule's domain, `0 < ℓ² < 2`.
- Decay rates are computed for the squared energy `u = F²` and its slope. The walk's own `F = √u` and `E = (u + μ²)^{1/2}` are real-analytic on a strip (block 184 T3), so their hops also decay exponentially. Their exact rates are not computed: `F` has further branch points where `sin² k₀ + ℓ² cos² k₀ = 0`.

## Theorem T1 — the hops in closed form

*Statement.* With `M = 2k`, `E = 2k₀` and `e = 1 − ℓ²`, the rule is `M = E − e sin E`, and `du/dk = sin E`. The series `sin E = Σ_{n ≥ 1} (2/(ne)) J_n(ne) sin(nM)` holds. So `du/dk` has hops `b_n = (2/(ne)) J_n(ne)` of range `2n`, and `u = const − Σ_n (b_n/(2n)) cos(2nk)`.

*Proof.*
- The map is direct (runner B1).
- The inversion series for a function of `E`, `f(E) = f(M) + Σ_m (e^m/m!) d^{m−1}/dM^{m−1}[sin^m M f′(M)]`, applied to `f = sin`, is compared term by term with the series of `J_n(ne)` through order `e⁷` (runner B2).
- The full series is the classical one, named under Imports. ∎

## Theorem T2 — the decay rate

*Statement.* For `0 < |e| < 1`, `E(M)` is real-analytic on the real line. Its nearest singularities are the folds `1 − e cos E = 0`: at `E = i arccosh(1/e)` for `e > 0`, and at `E = π + i arccosh(1/|e|)` for `e < 0`. There `|Im M| = κ = arccosh(1/|e|) − √(1 − e²)`. So `u` is analytic for `|Im k| < κ/2`, and its hops of range `2n` are bounded by `C_δ exp(−n(κ − δ))` for every `δ > 0`.

*Proof.*
- `dM/dE = 1 − e cos E` vanishes only at the folds. Runner C1 evaluates `M` there for both signs of `e`.
- Away from the folds `E(M)` is analytic by the inverse function theorem.
- The bound is the standard decay of the coefficients of a function analytic on a strip. ∎

## Theorem T3 — where it is local

*Statement.* Put `y = 1/|e|`. Then `κ = arccosh y − √(1 − 1/y²)` vanishes at `y = 1` and has derivative `√(y² − 1)/y² > 0`. So:
- `κ > 0` at every stretch with `0 < ℓ² < 2` other than `ℓ = 1`, where `e = 0` and the reach is finite (`u = sin² k`);
- `κ` depends only on `|1 − ℓ²|`, so a stretch and a compression with the same `|1 − ℓ²|` are equally local;
- near `ℓ = 1`, `κ = ln(2/|e|) − 1 + O(e²)`;
- near the ends `|e| → 1`, that is `ℓ → 0` or `ℓ → √2`, `κ = s³/3 + s⁵/5 + …` with `s = √(1 − e²)`, so the decay length `1/κ` diverges like `3/s³`.

*Proof.* Runner D1. `arccosh(1/e) = ln((1 + √(1 − e²))/e)`, and with `s = √(1 − e²)` it is `artanh s`. ∎

## What this settles and what it does not

- **Settled.**
  - Block 184's rule is exponentially local at every stretch strictly inside its domain, with an explicit rate for its squared energy (T1–T3).
  - It is not uniformly local: the decay length diverges at both ends.
- **For the third column (the coupling axis).** If the owner answers yes to "must a stretch slow every wave as it slows a free particle?", the walk that results is a local law at each stretch below `√2`. How far it reaches depends on the stretch, growing without bound as the stretch nears `√2`.
- **Not settled.**
  - The exact decay rates of the walk's own hops `F` and `E`.
  - Uniform bounds on a compact part of the domain, beyond the continuity of `κ`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 184 T5 (pushed): infinite reach with exponential decay at every l != 1, rate not computed; the 2026-09-27 strategy lens's decisive test"
source_of_blocker_text: admissibility_rule_reach_three_a_momentum_that_is_the_same_for_all_eight_species_gives_a_coupling_with_the_exact_current_and_one_geometry_for_all_bounded_theorem_note_2026-09-21
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "an other-family referee; the walk's own decay rates"
conditional_surface_status: "exact within block 69, for block 184's rule"
hypothetical_axiom_status: "the rule is supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 69 (landed): the coupling.
  - Block 184 (pushed): the rule, its infinite reach, and qualitative exponential decay.
  - Block 185 (pushed): the free-particle law that fixes the rule.
- **In the literature.**
  - Kepler's equation and its Bessel series.
  - Carlini's asymptotic formula for `J_n(ne)`.
  - The decay of coefficients of functions analytic on a strip.
  - None is used as authority.
- **New here.**
  - The identification of block 184's rule with the inversion relation, and its hops in closed form (T1).
  - The rate (T2) and its limits (T3).
- **Provenance.** The supervisor's own (Claude Opus 5.5), unrefereed. The question came from a same-family strategy lens (Claude Fable 5.1, not a referee). A floating-point check in scratch matched the series at five stretches before the exact runner was written.

## Exact target and obligation graph

Target: how local block 184's rule is. The obligations are:
- (O1) the premises (A3);
- (O2) the map and the series (B1, B2);
- (O3) the fold and the rate (C1);
- (O4) positivity and the limits (D1).

## No-Go Discipline Gate

The note's negative sentence: the rule is not uniformly local on its domain.

### N1 — Attack routes and the scope they leave
Attack routes, each examined:
1. *A nearer singularity.* The only points where `dM/dE = 0` are the folds, and `E(M)` is entire in `M` away from them. ATTEMPTED; closed for `u`.
2. *The walk's own hops.* `F` has further branch points; not computed.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- The following are declared: the rule, and hops as series coefficients.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; sites, bonds, translations; silence on amplitude dynamics | yes |
| block 69 (landed) | the coupling | yes (quoted, A3) |
| block 184 (pushed) | the rule | re-derived (B1) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "hops `(2/(ne))J_n(ne)`, rate `arccosh(1/|e|) − √(1 − e²)`, diverging decay length at the ends" | executed: the map | executed: the series through `e⁷` | executed: the fold for both signs | executed: positivity and the limits | not executed: the walk's own rates |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "A decay length that diverges at the ends means the rule is not local."
  - *Reply:* At every stretch strictly inside the domain it is exponentially local. The divergence is at the ends, where block 184 already found that the rule stops.

### N8 — Cross-cycle echo
- Block 184: infinite reach, qualitatively exponential decay.
- This note: the rate, and its divergence at the ends.

## Falsifiers

- A hop of `du/dk` differing from `(2/(ne))J_n(ne)`.
- A singularity of `E(M)` nearer the real line than the fold.

## Boundaries and non-claims

- The rule's domain; the squared energy's hops.
- The rule is supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Block 69 (landed), quoted. Block 184 (pushed), placed and re-derived.
- Named standard imports, at definition level:
  - Kepler's equation, its Bessel series, and Carlini's asymptotic formula for `J_n(ne)`;
  - the inversion series for implicit relations (Lagrange's), used here only to check through `e⁷`;
  - the inverse function theorem;
  - the decay of coefficients of functions analytic on a strip;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block (Claude Opus 5.5), 2026-09-28, near the close of the owner's second 12-hour campaign.
- **Provenance.** The supervisor's own derivation, unrefereed.
- **Before writing.** Block 184 names Kepler's equation and the Bessel series in its Premises, and only the qualitative decay in T5. The rate and its limits are new here.
- **Mutation census.** One mutation per science family, each failing only in its own family, and two in family G.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_stretch_rules_hops_decay_exponentially_2026_09_28.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
