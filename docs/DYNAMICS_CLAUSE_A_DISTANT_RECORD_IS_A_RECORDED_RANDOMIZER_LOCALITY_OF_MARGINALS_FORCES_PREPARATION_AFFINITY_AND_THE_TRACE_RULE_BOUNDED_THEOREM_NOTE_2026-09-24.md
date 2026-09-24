---
claim_id: dynamics_clause_a_distant_record_is_a_recorded_randomizer_locality_of_marginals_forces_preparation_affinity_and_the_trace_rule_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Under the dynamics clause of open PR 9040 (supplied, not adopted), with records updating states by compression (open PR 9041), take the reading that a site's marginal record distribution does not depend on whether, or along which axis, a distant record forms (D-loc, recorded and not adopted). (i) The clause carries purifications: the Heisenberg bond at J t = pi is the swap up to phase, and partial swaps prepare every reduced Bloch length, so an entangled partner of a condition qubit can be placed at any distance. (ii) Every two-point pure decomposition of a qubit state is realized by a record on a purifying partner (200 random chords, deviation 1e-15). (iii) Hence a law P(+m | condition state) consistent with D-loc satisfies P(rho) = p P(psi_1) + (1 - p) P(psi_2) on every chord. So it is affine on the Bloch ball, and with a normalized antipodal menu it is (1 + lambda r.m)/2. Repeat certainty gives lambda = 1, the Born law. (iv) The trace rule passes this consistency to 1e-16. A tanh deformation built from the landed exp(k n.m) counterkernel, and a cubic deformation, both of which pass the landed note's conditions, shift the site's marginal by 0.06 to 0.2 with the distant record and its axis. This discharges the landed affine/Born gate's first obligation, an autonomous recorded randomizer that proves preparation affinity, in terms of D-loc and the clause. The Born orientation still needs repeat certainty (D-relax at lambda = 1). No derivation of D-loc from the axiom text, of the menu or of the formation rate is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_a_distant_record_is_a_recorded_randomizer_2026_09_24.py
---

# A distant record is a recorded randomizer

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** a conditional derivation of preparation affinity with finite certificates; unaudited.

## Result

The landed
`ADMISSIBILITY_OPUS_AFFINE_BORN_PUBLIC_EVIDENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-01.md`
finds that the Born law's missing rung is **preparation affinity**: the law
must be affine when the condition it depends on is itself a physical
mixture. Covariance, endpoint normalization and exclusion do not force this.
Nonlinear kernels such as `exp(k n·m)` survive all of them. The landed
note's first obligation asks for "an autonomous recorded randomizer" that
proves affinity.

Under the dynamics clause, a distant record is such a randomizer:
- **Carrying.** The clause can carry an entangled partner of a condition
  qubit to any distance.
- **Steering.** Recording that partner leaves the condition qubit in either
  end of any chord through its state, with the chord's weights.
- **Locality of marginals.** Now read locality as saying that the site's
  marginal record distribution cannot depend on whether, or how, that
  distant record forms (D-loc). Then the law agrees with its chord averages
  everywhere, which means it is affine.
- **The trace rule.** An affine law on an antipodal menu is
  `(1 + λ r·m)/2`, and repeat certainty sets `λ = 1`.

A deformed law, in contrast, lets the distant party signal.

## Setting and decision points

- **The dynamics clause** (open PR 9040; D-dyn).
- **Compression updates** (open PR 9041; D-perm). A record projects the joint
  state. The unrecorded parts take their conditional state.
- **Antipodal menus** (D-menu). The law `P(+m | r)` for a condition state
  with Bloch vector `r` is normalized over `{+m, −m}`.
- **Locality of marginals** (D-loc, new). A site's marginal record
  distribution does not depend on whether, or along which axis, a distant
  record forms.
  - This is how this note reads the Lattice axiom's physical locality
    together with Admissibility's neighbour determination.
  - It is recorded as a decision point, not derived from the axiom text.

None is adopted.

## Theorem 1 — the clause carries purifications

The Heisenberg bond `J s·s = J(SWAP/2 − 1/4)` evolved for `Jt = π` is the
swap, up to a phase. A chain of such steps moves a qubit's entangled
partner as far as needed. The antiferromagnetic pair ground state of open
PR 9043 is a singlet. Partial swaps `e^{−iθ SWAP}` acting on `|↑↓⟩` prepare
every reduced Bloch length from 1 down to 0. So every qubit state has a
purification whose partner the clause can place at any distance.

## Theorem 2 — a distant record steers every chord

Let `ρ = p ψ₁ + (1 − p) ψ₂` be any chord through a qubit state. Its
endpoints are pure, and `p` is fixed by where `ρ` sits.

Purify it as `√p |ψ₁⟩|0⟩ + √(1 − p) |ψ₂⟩|1⟩`. Recording the partner in
`{|0⟩, |1⟩}` then leaves the qubit in `ψ₁` with probability `p` and in `ψ₂`
with probability `1 − p`.

Any such purification is related to one the clause can distribute by a
unitary on the partner, and that unitary only changes which basis the
record uses. ∎

## Theorem 3 — locality of marginals forces affinity

Let the site's law be `P(+m | ρ)`, a function of a condition state `ρ`. That
condition can be the site's own state or a neighbour's.

**Two ways to compute the marginal.**
- If the distant partner forms no record, the site sees the reduced
  state `ρ`, and its marginal is `P(ρ)`.
- If the partner records, the site sees `ψ_b` with probability `p_b`, and
  its marginal is `Σ_b p_b P(ψ_b)`.

D-loc makes these equal on every chord (Theorem 2). A function on the Bloch
ball that equals its chord interpolation everywhere is linear along every
chord, and hence affine.
- With the menu normalized, `P(+m | r) = (1 + λ r·m)/2`.
- Covariance rules out other affine forms, as in the landed note's
  `q = c + b n·m`.
- Repeat certainty, a pure `+m` condition recording `+m`, gives `λ = 1`: the
  Born law. ∎

If the condition is a whole neighbourhood, the same argument applies on its
state space. An affine law there is `Tr(E ρ)` for an effect `E`.

## What deformed laws do

Two nonlinear laws were tested, both with the Born endpoints:
- the landed counterkernel `exp(k n·m)`, normalized over the menu and
  rescaled, `(1 + tanh(k r·m)/tanh k)/2` with `k = 2`;
- a cubic deformation, `(1 + x + ε(x³ − x))/2` with `ε = 0.3`.

The landed note shows that such laws pass its conditions. Under the clause,
both let a distant party signal:
- **Record or not.** Whether the partner is recorded shifts the site's
  marginal by up to 0.201 (tanh) and 0.062 (cubic).
- **Which axis.** The choice of recording axis shifts it by up to 0.166
  (tanh) and 0.057 (cubic).

The shift grows with the deformation: 2.5e-3, 2.3e-2 and 6.2e-2 at
`ε = 0.01, 0.1, 0.3`. It vanishes only at `ε = 0`.

## The landed gate's four obligations

| Obligation (landed note) | Status under the clause |
|---|---|
| 1. An autonomous recorded randomizer that proves affinity | Discharged here: a distant record, given D-loc. |
| 2. The normalized probability identified with the one-neighbour transition density | The antipodal menu normalizes the law directly (D-menu). |
| 3. A repeatability experiment that orients Born rather than anti-Born | Repeat certainty gives `λ = 1`. Open PR 9041 relates it to ferromagnetic ground relaxation (D-relax). |
| 4. An autonomous reset or repeat process for stable frequencies | Open PR 9052: frequencies follow the one-shot odds exactly when correlations cluster. |

So under the clause, the Born law rests on two recorded readings rather
than an assumed functional form:
- D-loc, for affinity;
- repeat certainty (D-relax at `λ = 1`), for orientation.

## Checks

The runner has 6 checks and all pass in under 1 s.

| Check | Result |
|---|---|
| Purifications | `|U − phase·SWAP|` 3.4e-16 at `Jt = π`. Partial swaps give reduced Bloch lengths 1.0, 0.966, 0.866, 0.707, 0.5, 0.259, 0. |
| Steering | 200 random chords, largest deviation 1.1e-15. |
| Trace rule | Largest steered-average discrepancy over 300 chords 1.1e-16. |
| Deformed laws signal | Record-or-not shift: tanh 0.201, cubic 0.062. Axis shift: tanh 0.166, cubic 0.057. |
| Affinity forced | Chord violation 2.2e-16 at `ε = 0`; then 2.5e-3, 2.3e-2 and 6.2e-2. |
| Orientation | `λ = 1`, with `P(+m | m) = 1` and `P(+m | −m) = 0`. |

## What this does not do

- It adopts no decision point. D-loc is a reading, recorded and not derived
  from the axiom text.
- It does not derive the menu, the relaxation profile or the formation rate.
- Its steering uses qubit chords and two-outcome records. The neighbourhood
  version is argued, not computed.
