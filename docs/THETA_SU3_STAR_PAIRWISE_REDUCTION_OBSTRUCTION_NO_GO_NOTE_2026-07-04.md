# Theta SU(3) Star Pairwise-Reduction Obstruction No-Go Note

**Date:** 2026-07-04
**Type:** no_go
**Claim type:** no_go
**Status:** source-side no-go; independent audit required before any
effective-status change. This note does not retire theta, does not set
`theta_bar = 0`, does not edit any Tier-A registry, axiom, primitive, audit
verdict, or publication-status surface, and does not claim that future
sector-level, phase-source, or owner-governance routes are impossible.
**Primary runner:**
[`scripts/theta_su3_star_pairwise_reduction_obstruction_2026_07_04.py`](../scripts/theta_su3_star_pairwise_reduction_obstruction_2026_07_04.py)

## Target

[`THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_LINK_STAR_GLUING_FRAME_CORRELATION_PAIR_COMPOSITE_DAGGER_EVENNESS_AND_ODD_BRANCH_PHASE_RESIDUAL_BOUNDED_THEOREM_NOTE_2026-07-02.md)
left a finite algebra question inside the theta gauge-side route:

```text
(i-b''-a) SU(3) star reduction: does the even invariant ring of SU(3)
          staple tuples reduce to pairwise composite data?
```

This block answers that reduction shortcut in the negative. The SU(2)
pairwise-reduction theorem does not transfer to SU(3). There are exact
SU(3) triples whose separate classes and all pairwise composite classes are
the same, but whose dagger-even triple invariant is different. Therefore a
sector/readout theorem for the SU(3) star cannot be replaced by pairwise
composite bookkeeping alone.

## Inputs

- [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
  current Lattice, Qubit, Admissibility, and Record surface and withholds
  source/action, physical-observable identification, sector generation,
  readout-context selection, and measurement dynamics.
- [`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md`](ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md)
  keeps theta live through the gauge-side winding account and mass-side
  determinant-readout bridge.
- [`THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md`](THETA_GAUGE_POSITIVE_ROUTE_STRETCH_STATUS_2026-07-04.md)
  factors the gauge-side theta residual into G1 defect closure, G2
  nonabelian sector/readout registration, G3 phase insertion, and G4
  assembly.
- [`THETA_CARTAN_VALUED_CROSS_PLANE_PAIRING_DIAGONAL_WEYL_FRAME_THEOREMS_AND_TRIALITY_FRACTIONAL_VALUES_BOUNDED_THEOREM_NOTE_2026-07-02.md`](THETA_CARTAN_VALUED_CROSS_PLANE_PAIRING_DIAGONAL_WEYL_FRAME_THEOREMS_AND_TRIALITY_FRACTIONAL_VALUES_BOUNDED_THEOREM_NOTE_2026-07-02.md)
  sharpened the frame residual to joint diagonal-Weyl data rather than
  independent per-plane orbit data.
- The link-star theorem cited above proved pair/chains frame transport and
  SU(2) pairwise reduction, but explicitly left SU(3) star reduction open.
- [`THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md`](THETA_G3_PHASE_INSERTION_CURRENT_SURFACE_NO_GO_NOTE_2026-07-04.md)
  keeps the phase-type insertion route open.

## Exact Witness

Let `X` and `Z` be the standard SU(3) clock/shift matrices

```text
X^3 = Z^3 = I,     Z X = omega X Z,     omega = exp(2 pi i / 3),
det X = det Z = 1.
```

Write `E(a,b)=X^a Z^b`, with exponents in `F_3^2`. The product law is

```text
E(a,b) E(c,d) = omega^(b c) E(a+c, b+d).
```

Every noncentral `E(a,b)` has SU(3) conjugacy class with eigenvalues
`{1, omega, omega^2}` up to a center phase, hence `tr E = tr E^2 = 0`.
Center phases multiply this multiset by `omega^k` and do not change the
noncentral class.

Consider two triples:

```text
T_closed = (E(1,0), E(0,1), E(2,2))
T_open   = (E(1,0), E(0,1), E(1,1)).
```

In both triples:

- each individual staple is noncentral;
- every pair sum is noncentral;
- every pair difference is noncentral.

Thus the separate class data and the pairwise composite class data
(`S_i S_j`, `S_i^dag S_j`, `S_j^dag S_i`) are identical at the class level:
all probes lie in the same traceless noncentral SU(3) conjugacy class.

But the dagger-even triple invariant

```text
E_3(A,B,C) = Re(tr(ABC) + tr(ACB))
```

differs:

```text
T_closed:
  ABC = omega^2 I,   ACB = I,      E_3 = 3/2

T_open:
  ABC and ACB are noncentral,      E_3 = 0.
```

The runner verifies both the exponent arithmetic and the explicit matrix
identities. This is a direct obstruction to the pairwise-reduction shortcut:
the even SU(3) triple data are not determined by separate-plus-pairwise
classes.

## No-Go Statement

The implication

```text
real-weight link-star gluing is dagger-even
+ SU(2) stars reduce to pairwise composite classes
+ SU(3) pair and chain frame data are configurational
therefore SU(3) star/readout data reduce to pairwise composite classes
```

is invalid.

The SU(3) star has a genuine even triple joint-data surface that pairwise
classes do not determine. Therefore the SU(3) portion of G2 cannot be closed
by citing the SU(2) pairwise simplification or by keeping only pair
composites. A future positive route must either derive a sector-level
projection that kills or controls the triple branch, derive a physical
record/readout theorem for the full joint data, or explicitly approve a
narrow primitive/governance premise.

## What This Moves

| Before | After |
|---|---|
| The open `(i-b''-a)` question was whether SU(3) even star data might reduce to pairwise composites as in SU(2). | The pairwise-reduction shortcut is pruned by an exact SU(3) finite witness. |
| Pair/chains frame transport could be overread as enough for full SU(3) star registration. | Pair/chains remain useful, but SU(3) stars carry extra triple joint data unless a sector-level theorem removes it. |
| The G2 residual was split into frame correlation and a vague SU(3) star question. | The remaining target is sharper: derive sector-level handling of SU(3) triple joint data and physical readout registration. |

## What Does Not Move

- Theta is not retired.
- The Tier-A registry is not edited.
- No axiom, primitive, audit verdict, or publication surface is changed.
- No physical SU(3) theta sector is registered.
- No phase-source theorem is supplied.
- No claim is made that future sector-level SU(3) star/readout work is
  impossible.
- No mass-side determinant-channel bridge is supplied.

The sector-level SU(3) star/readout route remains open.

## Remaining Live Routes

1. **Sector-level SU(3) star/readout theorem.** Derive whether the closed
   surface sector projection kills, controls, or physically registers the
   triple joint-star data exposed here.
2. **G1 defect closure or suppression.** The closed-branch carrier still
   needs a physical closedness/suppression premise.
3. **G3 phase-source theorem.** The phase-source theorem remains open:
   derive the odd-branch-sensitive multi-plaquette `F cup F` insertion, not
   merely its carrier reduction.
4. **G4 theta-bar assembly.** Assemble gauge and mass only after the
   gauge-side carrier/readout/phase gates and mass-side determinant channel
   are supplied.
5. **Owner governance.** Approve a narrow sector/readout or phase-source
   primitive if derivation is not required.

## No-Go Discipline Gate

**N1 alternative route enumeration.** Pairwise SU(2) reduction, SU(3)
pairwise reduction, full SU(3) triple joint data, sector-level projection,
G1 defect closure, G3 phase source, G4 assembly, and owner governance are
separated.

**N2 wall independence.** This block targets only `(i-b''-a)`, the SU(3)
star pairwise-reduction shortcut inside the gauge-side winding account. It
does not decide G1, G3, G4, or the mass-side determinant bridge.

**N3 hidden-wall scan.** The proof imports no neutron-EDM bound, no observed
theta value, no fitted selector, no axion premise, no topological-sector
primitive, no action-class primitive, no branch/section primitive, no
sector-readout primitive, and no registry edit.

**N4 residual matching.** The result matches the link-star note's named
open subquestion. It blocks exactly the transfer of the SU(2) pairwise
reduction to SU(3), and leaves the sector-level and phase-source routes open.

**N5 proven surface.** Proven here is a finite SU(3) obstruction to a
pairwise-reduction theorem. It is not a universal no-go against physical
SU(3) sector registration, sector projection, or phase insertion.

**N6 partial closure.** The target is sharpened: do not try to close G2 with
pair composites alone. Supply the sector-level triple joint-data theorem or
keep the gauge-side winding account admitted.

**N7 steelman.** A reviewer can say the finite Heisenberg witness is a
special subgroup, not the whole physical star. Correct. A single exact
witness is enough to refute a universal pairwise-reduction theorem; it does
not decide which subgroup data survive a future physical sector projection.

**N8 cross-cycle echo.** As in AC, R-eta, and theta mass-side work, a useful
structural carrier or low-rank simplification is not a physical readout
bridge unless the framework derives or explicitly supplies the bridge.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/theta_su3_star_pairwise_reduction_obstruction_2026_07_04.py
```

Expected close: `FAIL=0`.
