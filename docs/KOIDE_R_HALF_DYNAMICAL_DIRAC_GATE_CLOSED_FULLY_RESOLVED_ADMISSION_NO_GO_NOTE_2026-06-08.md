# Koide r=1/2 Dynamical Dirac Gate Closed → Fully-Resolved Tier-A Admission — No-Go Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** named-obstruction no-go (gate closure)
**Claim type:** no_go
**Status:** no-go proposal. Closes the **last** open Koide r=1/2 lever — the
dynamical staggered/Kähler-Dirac corner gate (does the realized generation
determinant count first-order `det D` → r=1/2, or second-order `det D†D` →
r=1?). Together with the static-readout no-go this fully resolves r=1/2 as an
admission. Adds no axiom, no fitted/imported value. Audit verdict set by the
independent audit lane.
**Authority role:** no-go source proposal (capstone of the Koide r=1/2 lever).
**Primary runners:**
[`scripts/koide_corner_dirac_determinant_2026_06_08.py`](../scripts/koide_corner_dirac_determinant_2026_06_08.py)
(det D = −|det M|², PASS=6) and
[`scripts/koide_dynamical_gate_closure_2026_06_08.py`](../scripts/koide_dynamical_gate_closure_2026_06_08.py)
(Pfaffian / RP / Berezin-power escape-refutations, PASS=4); exact sympy/numpy.

## The gate

On the C3 generation triplet the mass matrix is `M = a I + b C + b̄ C²` (real
singlet `a`, complex doublet `b`); `r = |b|²/a²`, `Q = 1/3 + (2/3)r`, `r=1/2 ⇔
Q=2/3`. The static-readout reframe space was exhausted (8 lenses, 0 survivors;
the only r=1/2 route — the holomorphic `(1,1)` count — is **measure-neutral** to
the framework-native complex structure `J_cs=(C−C²)/√3`, the companion static
no-go). The one residual was **dynamical**: does the framework's realized
staggered/Kähler-Dirac corner action deliver a **first-order** determinant
`det D` (count `b` once → r=1/2) or the **second-order** modulus `det D†D` →
`Tr log(M†M)` (count `b` twice → r=1)?

## Result: the dynamical gate is CLOSED → r=1

The realized C3 corner Dirac operator `D = [[0, M],[M†, 0]]` is Hermitian (not
antisymmetric); **`det D = −|det M|²`** (second-order, verified symbolically), and
its eigenvalues are `±` the singular values of `M`, so the fermion path integral
counts the **modulus** (`Tr log(D†D) = 2 Tr log(M†M)` → doublet energy `6|b|²`,
rank-2 Hessian) → **r=1**. Six dynamical escape routes were probed and
adversarially verified; **0 survived** (5 collapse to r=1, 1 already refuted):

- **Majorana / Pfaffian.** `Pf([[0,M],[−Mᵀ,0]]) = ±det M`; the Pfaffian removes
  only the outer L/R doubling, never the intra-`M` doublet multiplicity:
  `|Pf| = |det M| = ∏σ_k` → r=1. The only antisymmetric C3-equivariant kernel is
  `J_cs`, which annihilates the singlet and cannot even form `Q`.
- **Weyl / ε-projection.** A chiral half isolates `M`, but its gauge-invariant
  readout is `|det M| = ∏σ_k` (rank-2, counts `b` twice). The ε/γ₅ grading
  commutes with the C3 circulant → sign-blind; `arg(det M)` is
  information-insufficient (distinct sign patterns share a det-phase yet give
  different `r`). Magnitude → r=1; phase → δ.
- **Reflection positivity.** RP is structurally `T = B†B → |det B|²` (second
  order); OS reflection doubles `Θ(M)=M† → |det M|²`. The first-order holomorphic
  `W_h = a I + b C` has a **complex spectrum** for all `b≠0` (non-self-adjoint),
  so it is **not** reflection-positive. RP *structurally forecloses* the
  first-order reading → r=1.
- **Berezin measure power.** Any determinant power `p` (Dirac 2, Majorana 1,
  rooted ½) multiplies every isotype's log-weight **uniformly** → cancels in the
  singlet:doublet ratio → `r` is `p`-independent. The halving comes from
  *polarization*, not statistics.
- **U(1)_b quotient** and **wildcards** (Berry/anomaly/kinetic-stencil): each
  reaches r=1/2 only by **assuming the `(1,1)` polarization it claims to derive**
  (circular), or by deleting a flat mode by fiat (overriding the rank-2 modulus),
  or is a static structure already closed.

This matches the landed
`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08`
(explicit Cl(3)/Kähler-Dirac realization gives `det D = |det M|² → r=1`; the
McKean-Singer index is a signed mode-count `{0,±1,±3}`, the wrong kind of
functional for a continuous magnitude ratio).

## Verdict — both routes closed

The only r=1/2 route is the holomorphic count of `det M`, and it is
measure-neutral (static no-go). Every *realized* determinant reading — Dirac,
Majorana/Pfaffian, Weyl magnitude, any Berezin power — gives r=1, and reflection
positivity forecloses the first-order operator. **Both the static and the
dynamical routes to Koide r=1/2 are now closed.** Koide r=1/2 (`Q=2/3`) is a
**fully-resolved Tier-A admission**
([`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md),
on par with `θ`): **the framework does not derive the charged-lepton mass ratio.**
`r` is a continuous amplitude ratio `|b|²/a²`, orthogonal to every
signed/index/η functional (which carry only sign/integer-count data) and
invariant under the only continuous symmetry (`J_cs`/U(1)_b, which moves only
`arg(b)=δ`, the phase channel). The 45-year open status of `|b|/a = 1/√2`
(Rivero-Gsponer, "not from first principles") stands; the framework's
contribution is a **sharpened structural no-go**, not a derivation.

## What is and is not claimed

- **Is:** the realized corner Dirac determinant is second-order (`|det M|²`) → r=1;
  Pfaffian/Weyl/RP/Berezin-power readings all give r=1; RP forecloses the
  first-order operator; the only r=1/2 route is the measure-neutral holomorphic
  count → the dynamical gate is closed and (with the static no-go) r=1/2 is fully
  admitted.
- **Is not:** does **not** claim r=1/2 is mathematically impossible in some
  beyond-framework theory (a SUSY superpotential, which the framework lacks, would
  count holomorphically). Introduces no axiom; changes no prediction.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the C3 generation
  circulant structure and the Record "no weighting/occupancy rule" disclaimer; all
  determinant/Pfaffian/RP/measure facts are reproven in the two runners.

Companion + context (plain references, not load-bearing deps):
`KOIDE_R_HALF_POLARIZATION_SELECTOR_STATIC_READOUT_EXHAUSTION_NO_GO_NOTE_2026-06-08`
(the static companion — the holomorphic count is measure-neutral),
`KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08`,
`KOIDE_FLUCTUATION_MODULUS_GIVES_R_ONE_CHIRALITY_IS_PHASE_ONLY_FRONTIER_CORRECTION_NOTE_2026-06-04`,
`KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05`.

## Forbidden-imports check

No PDG / fitted / literature numerical comparator is consumed. The C3 circulant
spectrum, `det D = −|det M|²`, the Dirac↔singular-value pairing, the Pfaffian
`= ±det M`, the non-self-adjointness of `W_h`, and the Berezin-power r-neutrality
are reproven in the runners. Rivero-Gsponer and Seiberg are named as
comparator/context, not derivation inputs.
