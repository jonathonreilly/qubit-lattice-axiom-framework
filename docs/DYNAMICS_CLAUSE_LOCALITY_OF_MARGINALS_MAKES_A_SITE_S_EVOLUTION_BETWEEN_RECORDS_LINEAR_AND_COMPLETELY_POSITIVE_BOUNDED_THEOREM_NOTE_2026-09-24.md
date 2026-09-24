---
claim_id: dynamics_clause_locality_of_marginals_makes_a_site_s_evolution_between_records_linear_and_completely_positive_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Setting, all supplied and none adopted: the Hilbert-space kinematics that the dynamics clause of open PR 9040 brings with it; the compression update with its distant part (D-perm); the law as a function of the site's conditional state (D-tr); locality of marginals at equal time (D-loc); and the steering and trace rule of open PR 9083. Consider a qubit site's evolution between records, with a qubit partner decoupled from the site during it (as for a distant record whose site the dynamics does not connect). (i) The evolution is affine on the Bloch ball. A state-dependent precession and a purity-dependent contraction let a distant record shift the site's later marginal by 0.57 and 0.07, and their chord violation vanishes only at zero nonlinearity. Random channels shift nothing. (ii) Tested with the clause's own operations it is completely positive. The transpose on one half of a singlet gives a joint operator with eigenvalue -1/2. A record-field rotation of the site and then a Heisenberg bond with the partner turn it into a negative product-record probability (-0.43). For qubit maps, positivity with one qubit partner is complete positivity. (iii) A channel whose inverse is a channel is unitary: a random non-unitary channel's inverse has a negative Choi eigenvalue. (iv) The two-site form of the generator is imposed, not derived. Nearest-neighbour range is a statement about the generator: the clause's own evolution is not a nearest-neighbour unitary at finite time (weight of U^dag X_2 U outside radius 1 in a five-site Heisenberg chain 7.8e-7, 2.0e-4, 9.8e-2 at t = 0.05, 0.2, 1; zero for a commuting Ising chain). So D-loc excludes nonlinear and non-completely-positive single-site evolution, and the clause is consistent with it; unitarity gives a Hermitian generator. The kinematics, reversibility, continuous time-homogeneous evolution, the range on the generator and covariance stay supplied. These are the standard no-signalling arguments for linear, completely positive dynamics, placed in the framework. No derivation of the clause's form, D-loc, reversibility or the coupling values is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_locality_of_marginals_makes_site_evolution_linear_and_completely_positive_2026_09_24.py
---

# Locality of marginals makes a site's evolution between records linear and completely positive

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** a consistency derivation inside supplied quantum kinematics, with
finite certificates; unaudited.

## Result

Open PR 9083 used one locality reading, D-loc, inside the kinematics the
clause brings and under the compression update. Distant records steer, so
the record law is affine: the trace rule.

The same reading constrains how a site evolves between records, with a
partner decoupled from it:
- **Linear.** An evolution that is not affine lets a distant record signal.
  After evolving, the site's marginal would depend on whether, and how, the
  distant partner was recorded.
- **Completely positive, tested with the clause's own operations.**
  Otherwise a field rotation and a Heisenberg bond, both operations the
  clause provides, turn it into negative record probabilities with an
  entangled partner.
- **Unitary, if also reversible.** A channel whose inverse is also a
  channel is unitary. That gives a Hermitian generator.

**What this is and is not.**
- It shows the clause is consistent with D-loc. It excludes nonlinear and
  non-completely-positive single-site evolution.
- It does not derive the clause's form:
  - The complete-positivity test uses the clause's own entangling step.
  - The two-site form restates nearest-neighbour range imposed on the
    generator.
- The clause's own evolution is not a nearest-neighbour unitary at finite
  time (Theorem 4). So "a group of nearest-neighbour unitaries has a
  two-site generator" is not the clause's situation.

## Setting and decision points

- **Kinematics, D-perm, D-tr and D-loc.** As in open PR 9083:
  - the clause's Hilbert-space kinematics;
  - the compression update with its distant part;
  - the law as a function of the site's conditional state;
  - locality of marginals at equal time.
- **Steering.** Open PR 9083: a record on a purifying partner leaves a qubit
  at either end of any chord through its state.
- **A decoupled partner.** The partner does not interact with the site
  during the evolution. A partner coupled through the dynamics can
  influence the site anyway; that is propagation, not signalling by the
  record.
- **D-rev.** The evolution between records is reversible, runs in
  continuous time, is time-homogeneous, and has a nearest-neighbour
  generator.

None is adopted.

## Theorem 1 — the evolution is affine

Let `Φ` evolve a site's Bloch vector before its record forms.

**Two ways to compute the marginal.**
- If a distant partner is not recorded, the site evolves from `r`. By the
  trace rule of open PR 9083, its marginal along `m` is `(1 + Φ(r)·m)/2`.
- If the partner is recorded, the site evolves from `ψ₁` or `ψ₂` with the
  chord weights, and its marginal is `(1 + [p Φ(ψ₁) + (1 − p) Φ(ψ₂)]·m)/2`.

D-loc makes these equal for every `m` and every chord. So `Φ` equals its
chord averages everywhere, which makes it affine. ∎

Two nonlinear maps were tested:
- **State-dependent precession.** A rotation about a fixed axis `n` by an
  angle proportional to `r·n`, of Weinberg type. It lets the distant party
  shift the site's later marginal by up to 0.572. Its chord violation grows
  from 0 as 0.024, 0.24 and 0.69 at coupling 0.05, 0.5 and 1.5.
- **Purity-dependent contraction** `r(1 − ε|r|²)`. It shifts the marginal
  by 0.074.

Random channels shift nothing (2e-16).

## Theorem 2 — tested with the clause's operations, the evolution is completely positive

Apply `Φ` to one half of a site–partner pair. Later operations that the
clause provides can act on the pair, and records then form. The joint
record probabilities must stay nonnegative.
- **Product records alone never show it.** Right after a partial
  transpose, product records are never negative, because the transpose of
  a product projector is a product projector.
- **Clause bonds alone don't either.** Every clause bond leaves `|Φ+⟩`
  invariant.
- **A field rotation plus a bond does.** A record-supplied field rotates
  the site (open PR 9041), the partner is brought adjacent by swaps, and a
  Heisenberg bond acts on the pair. Some product-record probability then
  reaches −0.43 for the transposed singlet.
- **So positivity forces complete positivity.** For qubit maps, positivity
  with one qubit partner is complete positivity.

Random channels never give a negative eigenvalue. The test uses the
clause's own entangling step, so this is a consistency condition on
single-site evolution given the clause, not a derivation of the clause. ∎

## Theorem 3 — reversible channels are unitary

A channel whose inverse is also a channel is unitary conjugation. The
runner builds the inverse transfer matrix and checks its Choi matrix:
- for a random unitary channel, the smallest Choi eigenvalue is 0 within
  rounding;
- for random non-unitary channels, the inverse has Choi eigenvalue as low
  as −10.2, so it is not a channel.

So under reversibility the evolution between records is unitary, with a
Hermitian generator. ∎

## Theorem 4 — the two-site form is imposed on the generator

Nearest-neighbour range cannot be read off the evolution. In a five-site
Heisenberg chain, the operator `U(t)† X₂ U(t)` spreads beyond radius 1 of
site 2:

| Time | Heisenberg | commuting Ising |
|---|---|---|
| 0.05 | 7.8e-7 | 9e-33 |
| 0.2 | 2.0e-4 | 1e-32 |
| 1 | 9.8e-2 | 0 |

The table gives the fraction of its weight on Pauli strings reaching
beyond radius 1.

A group of unitaries that each keep strict range has a two-site generator,
but the clause's evolution is not such a group. So the range is imposed on
the generator, and the two-site form restates it. Open PR 9040 classifies
the covariant two-site generators: Heisenberg alone under possibility
covariance, and Heisenberg, compass and Moriya under full soldering. ∎

## What this means for the lanes

- **Dynamics.** The campaign supplied the clause as one decision point.
  D-loc excludes nonlinear and non-completely-positive single-site
  evolution with a decoupled partner, and the clause passes.
- **What stays supplied.**
  - The kinematics.
  - Reversibility between records. Open PR 9086 shows it is the same as
    "records are the only irreversible events".
  - Continuous, time-homogeneous evolution.
  - The range on the generator.
  - Covariance.
- **Prior art.** These are the standard no-signalling arguments for linear,
  completely positive dynamics (Gisin 1990; Simon, Bužek and Gisin 2001),
  applied inside the framework and cited as prior art, not as premises.
- **What stays open.** Whether the kinematics, reversibility, the time
  structure or the range can be derived. The coupling values `J`, `K`, `D`
  are not fixed.

## Checks

The runner has 6 checks and all pass in about 1.5 s.

| Check | Result |
|---|---|
| Nonlinear maps signal | Largest marginal shift 0.572 (precession) and 0.074 (contraction). |
| Channels do not | Largest shift over 50 random channels 2.2e-16. |
| Affinity forced | Chord violation 2.8e-16 at zero coupling; 2.4e-2, 2.4e-1 and 6.9e-1 at 0.05, 0.5 and 1.5. |
| Complete positivity | Transpose: smallest joint eigenvalue −0.500. After a field rotation and a Heisenberg bond: product-record probability −0.430. Random channels: −2.2e-16. |
| Reversibility | Inverse Choi eigenvalue: unitary −2.1e-16; random channels as low as −10.18. |
| Range on the generator | Weight outside radius 1: Heisenberg 7.8e-7, 2.0e-4, 9.8e-2 at `t = 0.05, 0.2, 1`; Ising 1e-32 or less. |

## Independent checks

A separate checker wrote its own code without reading this runner. A later
adversarial review of the whole chain ran its own checks.
- **Confirmed.**
  - Chord affinity, and the nonlinear maps' shifts: precession axis shift
    0.594, chord violations 0.025, 0.241 and 0.696.
  - That random channels give no shift.
  - The transpose's −1/2.
  - Non-CP inverses for all 1000 random non-unitary channels.
- **Flagged, now addressed.**
  - Negativity needs an entangling step; the clause's rotation plus bond
    supplies one. So complete positivity is tested with the clause's own
    operations (Theorem 2).
  - The partner must be decoupled during the evolution. Coupled chains
    shift the site through the dynamics itself.
  - The two-site form restates the range, and time-homogeneity is
    assumed. The clause's evolution does not keep strict range
    (Theorem 4), so only the Hermitian generator is derived.
  - The kinematics and the distant update were used but not listed.

## What this does not do

- It adopts no decision point. The kinematics, D-perm, D-tr, D-loc and
  D-rev are supplied, not derived.
- It treats a qubit site with a decoupled qubit partner. The
  general-dimension statements are standard and are argued, not computed.
- It does not derive the clause's form, reversibility, continuous time,
  the range or the coupling values.
