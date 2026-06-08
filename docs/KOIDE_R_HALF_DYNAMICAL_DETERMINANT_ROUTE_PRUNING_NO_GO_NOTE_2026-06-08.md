---
claim_id: koide_r_half_dynamical_determinant_route_pruning_no_go_note_2026-06-08
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Koide r=1/2 Dynamical Determinant Route-Pruning No-Go

**Date:** 2026-06-08
**Claim type:** no_go.
**Review boundary:** formal dynamical route-pruning no-go proposal only.
**Primary runners:**
[`scripts/koide_corner_dirac_determinant_2026_06_08.py`](../scripts/koide_corner_dirac_determinant_2026_06_08.py)
and
[`scripts/koide_dynamical_determinant_route_pruning_2026_06_08.py`](../scripts/koide_dynamical_determinant_route_pruning_2026_06_08.py).

## Scope

This packet prunes specific dynamical determinant routes for obtaining
Koide `r=1/2` on the supplied C3 circulant mass matrix
`M = a I + b C + bbar C^2`, with `r=|b|^2/a^2` and
`Q = 1/3 + (2/3)r`.

The supported statement is narrow:

```text
For the supplied C3 circulant matrix M and the tested Dirac/Pfaffian/RP/
Berezin determinant readings, the route does not produce the equal-block
r=1/2 readout. The implemented Hermitian corner Dirac operator reads the
modulus and gives the rank-2 doublet count.
```

This packet does not classify Koide `r=1/2` as a Tier-A admission, does not
claim every possible selector is closed, and does not prove the charged-lepton
mass ratio is underived. Non-tracial, chiral, finite-gap, explicit
block-measure, supersymmetric/holomorphic-superpotential, or other physical
readout routes remain outside this no-go.

## Runner-Backed Results

- For `D = [[0,M],[Mdag,0]]`, the runner verifies
  `det D = -det(M Mdag) = -|det M|^2`. The eigenvalues of `D` are paired
  `+/-` singular values of `M`, so this Dirac route reads the modulus.
- The doublet modulus energy has rank 2 over `(Re b, Im b)`, giving the
  dimension/modulus weighting rather than a one-slot holomorphic count.
- For the block-antisymmetric Majorana/Pfaffian kernel
  `[[0,M],[-M^T,0]]`, the Pfaffian magnitude equals `|det M|`, so it removes
  the outer L/R doubling but does not create an equal-block selector.
- The first-order holomorphic `W_h=aI+bC` is non-self-adjoint for generic
  `b != 0`; the runner records it as not the tested reflection-positive
  transfer object. The Hermitian Dirac construction instead gives a positive
  second-order transfer.
- A uniform Berezin determinant power cancels in the singlet:doublet ratio; it
  does not select `r=1/2`.

## Non-Claims

This note does not claim:

- Koide `r=1/2` is mathematically impossible;
- all static, dynamical, chiral, non-tracial, finite-gap, explicit
  block-measure, or beyond-framework selectors are closed;
- Koide `r=1/2` is a registered or fully resolved Tier-A admission;
- the framework has proven that the charged-lepton mass ratio is underived;
- a physical flavor carrier/readout bridge has been supplied by this packet;
- an audit verdict or effective retained status.

## No-Go Discipline Gate

Status: PASS for the narrow determinant-route-pruning claim only.

### N1 Alternative Route Enumeration

| Route | Attempt | Result |
|---|---|---|
| Hermitian corner Dirac determinant | Use `D=[[0,M],[Mdag,0]]` to count `b` once. | ATTEMPTED: `det D=-|det M|^2` and the singular-value pairing read the modulus. |
| Weyl magnitude | Use one chiral block and read `|det M|`. | ATTEMPTED: the magnitude is still the singular-value product, not an equal-block selector. |
| Pfaffian/Majorana | Use a block-antisymmetric kernel to remove a doubling. | ATTEMPTED: `|Pf|=|det M|`; it does not create one-slot doublet weighting. |
| Reflection positivity | Use RP to justify the first-order holomorphic operator. | ATTEMPTED: the tested first-order `W_h=aI+bC` is non-self-adjoint for generic `b`; the RP-compatible Dirac object is second order. |
| Berezin power/rooting | Change determinant power `p` to alter the singlet:doublet ratio. | ATTEMPTED: a uniform power cancels from the ratio. |
| Non-tracial/chiral/finite-gap/explicit selector | Add extra physical structure that selects equal-block weighting. | OPEN: outside this packet and not ruled out. |

### N2 Wall-Independence Audit

The collapsed wall set is one route wall: the tested determinant-family
readouts do not select equal-block `r=1/2` on the supplied C3 matrix. Physical
carrier/readout, non-tracial selectors, chiral selectors, finite-gap dynamics,
and explicit block-measure rules are open residuals, not independent walls
claimed closed here.

### N3 Hidden-Wall Scan

The proof uses a supplied C3 circulant matrix, a supplied `r`/`Q` coordinate,
and specific determinant/RP/Berezin readings. Those are explicit scope
hypotheses. The note does not use Record, the scale-reference primitive, or
minimal axioms to supply a weighting, occupancy, or physical mass-readout rule.

### N4 Residual Matching

Context rows about static readout or Kähler-Dirac realization are not used to
claim global closure. The residual closed here is only the tested dynamical
determinant-family route on the supplied C3 matrix.

### N5 Rhetoric Audit

Phrases like "does not produce `r=1/2`" apply only to the tested
Dirac/Pfaffian/RP/Berezin determinant readings. They do not apply to all
mathematical or physical routes to `r=1/2`.

### N6 Partial-Closure Path Scan

Open partial-closure paths remain: a non-tracial reference state, chiral
selector, finite-gap dynamics, explicit block-measure rule, or a holomorphic
superpotential-style structure could supply a separate selector. This packet
does not call those new axioms or primitives.

### N7 Steelman

A strong counter-route is that the physical charged-lepton readout may not be
the Hermitian corner-Dirac determinant family tested here. A non-tracial
record state, chiral finite-gap dynamics, or explicit block-measure rule could
select equal-block weighting while remaining outside the determinant family.
That steelman is why this note lands only a route-pruning result.

### N8 Cross-Cycle Echo

Similar Koide selector walls in this repo have been narrowed by separating
finite algebra, readout convention, and physical carrier/readout bridges. This
note follows that pattern and does not promote a local route failure into a
global admission claim.

## Verification

Run:

```text
python3 scripts/koide_corner_dirac_determinant_2026_06_08.py
python3 scripts/koide_dynamical_determinant_route_pruning_2026_06_08.py
```

Expected:

```text
SCORECARD PASS=6 FAIL=0
SCORECARD PASS=4 FAIL=0
```
