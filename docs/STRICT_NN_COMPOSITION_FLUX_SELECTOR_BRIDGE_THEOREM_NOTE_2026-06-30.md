# Strict Nearest-Neighbor Composition Selects The Flux(-1) Branch

**Date:** 2026-06-30
**Claim type:** bounded_theorem / bridge theorem candidate
**Type:** theorem support for the PR #4747 axiom reset
**Status authority:** independent audit lane only. This note does not set or
predict an audit outcome, refresh ledgers, or register a primitive.
**Primary runner:**
[`scripts/strict_nn_composition_flux_selector_2026_06_30.py`](../scripts/strict_nn_composition_flux_selector_2026_06_30.py)

## Claim

The updated Lattice/Qubit/Admissibility/Record axioms do not need a broad
Dynamics axiom to reach the staggered-Dirac branch. They need one bridge:

```text
Strict NN composition:
Composing primitive nearest-neighbor availability influences must not create a
direct face-diagonal availability influence.
```

In plain language: if reality only lets a site be constrained through directly
connected neighbors, then two edge steps across a square may not behave like a
new primitive diagonal edge. The two square paths must cancel in the primitive
availability channel whenever the intermediate sites add no distinguishing
record content.

Under this bridge, the kinetic selector is no longer open:

```text
strict NN composition + one-qubit site possibility + cubic covariance
    -> no mixed two-step terms
    -> anticommuting edge coefficients
    -> Pauli/Cl(3) edge frame
    -> plaquette flux(-1)
    -> Kawamoto-Smit / first-order branch K1
```

The scalar `K0` branch is rejected because its two-step square has nonzero
face-diagonal leakage.

## Why This Is The Right Bridge Shape

PR #4747 now says:

- physical locality is nearest-neighbor on `Z^3`;
- each site has one-qubit local possibility;
- nearest-neighbor conditions determine the available subset of possibilities;
- records lock one available local possibility and are readable.

That gives local availability, but not yet how local availability composes.
The bridge above supplies exactly that missing operational sentence. It is not
"insert Dirac." It is a locality-preservation rule for composed availability:
nearest-neighbor influence should remain nearest-neighbor at the primitive
level and should not create a hidden diagonal edge.

## Theorem

Let `D` be a linearized edge-supported availability carrier on the cubic
lattice:

```text
D = sum_mu Gamma_mu nabla_mu
```

where each `Gamma_mu` acts on the one-site possibility carrier `M_2(C)`, and
`nabla_mu` is the nearest-neighbor difference in direction `mu`.

The strict-NN-composition bridge says that `D^2` has no mixed face-diagonal
terms:

```text
D^2 = I * sum_mu nabla_mu^2
```

Equivalently:

```text
Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0     for mu != nu.
```

Inside `M_2(C)`, this forces the three edge coefficients to be a Pauli frame
up to unitary/frame rotation. Their plaquette holonomy is:

```text
Gamma_nu Gamma_mu Gamma_nu Gamma_mu = -I.
```

So the selected branch is exactly flux `-1`, the Kawamoto-Smit/staggered-Dirac
branch already isolated by the two-flux-class theorem.

The scalar branch has `Gamma_mu = I`, so:

```text
Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 2I.
```

Its two-step composition produces a direct face-diagonal term. It is therefore
not compatible with strict nearest-neighbor composition.

## Relation To Existing Blockers

This bridge attacks the exact residual left by
[`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md):

```text
K0: flux(+1), scalar tight-binding
K1: flux(-1), Kawamoto-Smit / Dirac branch
residual: choose flux(-1)
```

The two-flux theorem showed that the prior constraint set left both branches.
This bridge adds a non-circular separator:

```text
K0 leaks face-diagonal influence under composition.
K1 cancels face-diagonal influence under composition.
```

That also matches the residual in
[`INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`](INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md):
first-order Dirac order versus second-order scalar spectator. The bridge
selects first-order order because only the anticommuting edge frame prevents
mixed two-step leakage.

## What This Unlocks If Accepted

If audit/review accepts strict NN composition as the downstream operational
reading of Admissibility, then the main kinetic blocker is no longer an
admission:

- P-KIN narrows from a one-bit flux selector to a theorem;
- P-SD remains discharged by the absorbing-frame theorem on the selected
  flux(-1) branch;
- the staggered-Dirac realization gate can be re-audited with this bridge as
  the missing upstream selector;
- downstream `AC_phi_lambda` pressure is reduced because the carrier/kinetic
  branch is no longer the admitted part.

This still does not derive probability, Born weights, measurement context,
observable selection, source/action coefficients, gauge species, or `theta`.
It attacks the kinetic spine only.

## Boundaries

- The bridge is about **composition of availability influence**, not temporal
  evolution, record production, Hamiltonian choice, or probability.
- The theorem is stated for the linearized nearest-neighbor edge-supported
  carrier. Extending it to interacting, nonlinear, or higher-order sectors is
  downstream work.
- If a reviewer does not accept strict NN composition as a consequence/bridge
  of Admissibility, then this note identifies the exact minimal missing
  primitive: strict NN composition, not a broad Dynamics axiom.
- Finite-volume wrap holonomies and APBC/PBC data remain separate convention
  surfaces, as in the two-flux-class theorem.

## No-Go Discipline Gate For The Bounded Bridge

This is a positive conditional bridge with one named wall: strict NN
composition. The negative subclaim is only that scalar `K0` fails this bridge,
not that scalar branches are impossible under every future theory.

### N1 - Alternative Routes

| Route | Attempt | Result |
|---|---|---|
| Bare nearest-neighbor support | Select `K1` using only support on lattice edges. | Fails: the two-flux-class theorem shows both `K0` and `K1` are edge-supported. |
| Cubic covariance | Select `K1` using proper cubic rotations. | Fails: `K0` is exactly cubic-covariant. |
| One-qubit carrier alone | Select `K1` from `M_2(C)` alone. | Partial: `M_2(C)` supplies the three anticommuting capacity, but does not demand its use without a composition bridge. |
| Strict NN composition | Forbid composed face-diagonal leakage. | Succeeds: it forces anticommutators to vanish and rejects `K0`. |
| Record readout | Select `K1` from additive record readout. | Fails: Record supplies readability/additivity, not kinetic composition. |
| Spectral isolated-zero route | Select `K1` because it has isolated zeros. | Still plausible downstream, but not needed if strict NN composition is accepted. |

### N2 - Wall Independence

The wall set collapses to one bridge wall: strict NN composition. It is
independent of APBC/PBC wrap data, probability, readout-context selection,
`AC_phi_lambda`, and `theta`.

### N3 - Hidden-Wall Scan

"Linearized edge-supported carrier" is explicit scope, not an axiom import.
"Strict NN composition" is the named bridge. The runner imports no probability,
measurement, Hamiltonian, empirical values, or Dirac assumption. Anticommuting
coefficients are derived from no mixed face-diagonal terms.

### N4 - Residual Matching

| Witness | Residual there | Residual here | Match |
|---|---|---|---|
| `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md` | flux(-1) selector over flux(+1) | strict NN composition selects flux(-1) | yes |
| `INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md` | first-order Dirac versus second-order scalar order | no mixed face-diagonal leakage selects first-order order | yes |
| `ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md` | Dirac-square carrier-class reading | strict NN composition supplies the no-cross-term reading | yes |

### N5 - Rhetoric Audit

The claim is not "the axioms alone derive all dynamics." The narrow claim is:
given strict nearest-neighbor composition of availability influence, the scalar
flux(+1) branch is not admissible as the primitive kinetic branch.

### N6 - Partial-Closure Paths

The bridge can be accepted as:

- a retained theorem interpreting Admissibility composition;
- a named bridge principle downstream of the axioms;
- or, if rejected as theorem content, a narrow owner-approved primitive.

It should not be promoted to a broad Dynamics axiom.

### N7 - Steelman

A hostile reviewer can object that Axiom 3 only says nearest-neighbor
conditions determine availability at one step; it does not explicitly say that
linearized two-step composition must have no face-diagonal leakage. On that
reading, strict NN composition is an additional bridge principle, not a theorem
from the axiom text alone. This note accepts that risk and makes the bridge
visible instead of hiding it.

### N8 - Cross-Cycle Echo

Prior kinetic-order no-go work already showed that support, cubic covariance,
and one-qubit carrier do not select `K1`. This bridge adds the missing
separator rather than reusing the failed routes. It also matches the
first-order coframe pattern: first-order structure is not free unless an
incidence/composition law supplies it.

## Command

```bash
python3 scripts/strict_nn_composition_flux_selector_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=12 FAIL=0
VERDICT: bridge theorem verified -- if strict nearest-neighbor composition is
accepted as the operational reading of Admissibility, the flux(-1) /
first-order branch is selected and the scalar flux(+1) branch is rejected.
```
