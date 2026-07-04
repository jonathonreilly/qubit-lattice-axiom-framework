# Theta SU(3) Star Central-Sector Projection Exact-Support Note

**Date:** 2026-07-04
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** exact-support source-side split; independent audit required
before any effective-status change. This note does not retire theta, does
not set `theta_bar = 0`, does not edit any Tier-A registry, axiom,
primitive, audit verdict, or publication-status surface, and does not claim
that a physical SU(3) sector/readout bridge or phase-source theorem has been
derived.
**Primary runner:**
[`scripts/theta_su3_star_central_sector_projection_exact_support_2026_07_04.py`](../scripts/theta_su3_star_central_sector_projection_exact_support_2026_07_04.py)

## Purpose

Block31 pruned the shortcut that SU(3) even star data reduce to separate
and pairwise composite classes. It left the live positive route:

```text
derive sector-level handling of SU(3) triple joint-star data and physical
readout registration.
```

This note splits out the exact finite algebra for the first half of that
route on a supplied central-sector projection. It shows that the triple
joint datum exposed by Block31 is not amorphous. On the finite SU(3)
clock/shift witness surface, a supplied central-sector projection kills
nonclosed triples and records a central cocycle for closed triples. That is
the exact sector-level object a future physical SU(3) readout theorem would
need to license.

## Inputs

- [`THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md`](THETA_SU3_STAR_PAIRWISE_REDUCTION_OBSTRUCTION_NO_GO_NOTE_2026-07-04.md)
  proves that pairwise composite class data do not determine SU(3) triple
  joint-star data.
- [`THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  leaves the sector-level closed-surface statement open after resolving
  pair and chain frame transport.
- [`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md`](THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md)
  keeps G2 nonabelian sector/readout registration and G3 phase insertion as
  open theta gauge-side gates.
- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  current axiom boundary and withholds source/action, physical-observable
  identification, sector generation, readout-context selection, and
  measurement dynamics.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta live through the gauge-side winding account and mass-side
  determinant-readout bridge.

## Supplied Surface

Let `X` and `Z` be the standard SU(3) clock/shift matrices

```text
X^3 = Z^3 = I,     Z X = omega X Z,     omega = exp(-2 pi i / 3),
det X = det Z = 1.
```

Write `E(a,b)=X^a Z^b`, with `(a,b)` in `F_3^2`. The product law is

```text
E(a,b) E(c,d) = omega^(-b c) E(a+c, b+d).
```

This note studies the supplied central-sector star projection

```text
P_c(A,B,C) = (1/3) tr(A B C).
```

It does not derive that the physical gauge surface supplies this projection
as a record/readout channel. It computes exactly what follows if that
sector projection is supplied.

## Exact Support Theorem

For triples of noncentral Heisenberg staples

```text
A = E(a1,b1),  B = E(a2,b2),  C = E(a3,b3),
```

the central-sector projection has the form

```text
P_c(A,B,C) =
  omega^k    if (a1+a2+a3, b1+b2+b3) = (0,0),
  0          otherwise,
```

where `k` is the ordered Heisenberg cocycle accumulated by the product.
Equivalently, the projection is nonzero exactly on the closed Heisenberg
vector-sum sector, and on that sector it records the central phase.

The dagger-even triple datum used by Block31 is therefore

```text
Re(tr(ABC) + tr(ACB))
  = 3 Re(P_c(A,B,C) + P_c(A,C,B)).
```

It is controlled by two ordered central projections, not by pairwise class
data.

## Block31 Witness Revisited

Block31 used the pairwise-degenerate triples

```text
T_closed = (E(1,0), E(0,1), E(2,2))
T_open   = (E(1,0), E(0,1), E(1,1)).
```

Their separate and pairwise class signatures match. The central-sector
projection separates them:

```text
T_closed:
  P_c(ABC) = omega,     P_c(ACB) = 1,
  Re(tr(ABC) + tr(ACB)) = 3/2.

T_open:
  P_c(ABC) = 0,         P_c(ACB) = 0,
  Re(tr(ABC) + tr(ACB)) = 0.
```

So the sector-level route does not need to guess an arbitrary extra scalar.
It needs a physical theorem saying that closed central-sector star data, or
the corresponding cocycle, are record/readout content on the SU(3) gauge
surface.

## What This Moves

| Before | After |
|---|---|
| Block31 showed pairwise data are insufficient for SU(3) star reduction. | The missing triple datum is localized to a central closure/cocycle projection on the finite SU(3) witness surface. |
| The sector-level route was broad: kill, control, or register triple joint-star data. | A supplied central-sector projection controls the data exactly: nonclosed triples vanish, closed triples carry a center phase. |
| It was unclear what the next positive G2 theorem would have to license. | It must license the central-sector star projection/cocycle as physical sector/readout content, or prove a sector projection that removes it. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No physical SU(3) theta sector is registered.
- No G3 phase-source theorem is supplied.
- No G1 defect-closure or defect-suppression theorem is supplied.
- No mass-side determinant-channel bridge is supplied.
- No audit status or effective status is changed.

## Remaining Live Routes

1. **Physical SU(3) sector/readout theorem.** Derive that the central-sector
   star projection or cocycle is actual record/readout content on the
   physical SU(3) gauge surface.
2. **Closed-surface sector projection theorem.** Show that the closed
   surface projection removes or controls the triple data globally, not only
   in the finite Heisenberg witness.
3. **G1 defect closure or suppression.** The abelianized carrier still needs
   a physical closedness/suppression premise.
4. **G3 phase-source theorem.** The odd-branch-sensitive multi-plaquette
   phase insertion remains open.
5. **Theta mass-side bridge.** The determinant-channel readout bridge remains
   a separate live atom.

## Scope Discipline

This is exact support, not a retirement authority. The result is conditional
on a supplied central-sector projection. The Record axiom can discipline a
readout once record content exists; it does not by itself create the SU(3)
sector record, select this projection, or identify it as the physical theta
gauge-side sector. Those remain separate theorem or governance routes.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_su3_star_central_sector_projection_exact_support_2026_07_04.py
```

Expected close: `FAIL=0`.
