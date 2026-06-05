# Flavor hw=1 Staggered Projection Gives Zero Generation Hopping - Narrow No-Go

**Date:** 2026-06-02
**Claim type:** no_go
**Claim scope:** for the specified three-corner-qubit staggered single-bit-flip operator `K = G1 + G2 + G3` on `C^8`, projection and Schur-complement reduction to the hw=1 generation sector induce zero off-diagonal generation hopping, so this projection route gives `r = |b|^2/a^2 = 0` and does not source the charged-lepton `r=1/2` value; no claim is made about other action terms, bivector sources, dynamics, or sector-factorization routes.
**Primary runner:** [`scripts/flavor_hw1_staggered_projection_democratic_r0_2026_06_02.py`](../scripts/flavor_hw1_staggered_projection_democratic_r0_2026_06_02.py)
(SCORECARD PASS=5 FAIL=0).

This note sets no audit verdict and proposes no new axiom, primitive, or value
selector.

---

## Question

Door A asks whether a framework-internal action can geometrically fix the
charged-lepton ratio

```text
r = |b|^2 / a^2 = 1/2
```

instead of leaving the on-site/hopping ratio as a separate value input. This
note tests one concrete route: start from three corner qubits, use the specified
staggered single-bit-flip generators, and reduce the full `C^8` operator to the
three-dimensional hw=1 single-excitation sector.

## Construction

Let

```text
G1 = sigma_x tensor I tensor I
G2 = sigma_z tensor sigma_x tensor I
G3 = sigma_z tensor sigma_z tensor sigma_x
K  = G1 + G2 + G3.
```

The hw=1 generation sector is

```text
span{|100>, |010>, |001>}
```

with basis indices `{1,2,4}` in the runner convention.

## Result

The runner verifies:

- the direct hw=1 block of `K` has exactly zero off-diagonal entries;
- the Schur-complement induced hw=1 hopping remains zero across the tested
  reference-energy sweep;
- the induced diagonal term is nonzero;
- therefore the induced hopping ratio is `r=0`, and the Koide line gives
  `Q = 1/3 + (2/3)r = 1/3`.

The cancellation mechanism is concrete: second-order paths through the vacuum
state and a doubly-excited state carry opposite staggered signs, so their
off-diagonal contributions cancel.

## Consequence

This specified projection route reaches the democratic endpoint, not the
charged-lepton point. It is useful route-pruning: the charged-lepton value
`r=1/2` must come from some other source, such as a separate bivector/action
term, a value selector, dynamics, or sector-factorization. This note does not
say those other routes fail.

## No-Go Discipline Gate

**Status:** PASS for the scoped projection route only. The claim closed here is
not "no action can source `r=1/2`"; it is only that this specified staggered
single-bit-flip projection does not.

### N1 - Alternative Route Enumeration

| route | what it would attempt | outcome | marker |
|---|---|---|---|
| Direct hw=1 block | Get generation hopping directly from `K` restricted to hw=1. | The direct off-diagonal block is zero. | ATTEMPTED |
| Schur-induced path | Get hopping through eliminated non-hw=1 states. | The vacuum and double-excitation paths cancel by staggered sign. | ATTEMPTED |
| Reference-energy tuning | Choose a Schur reference energy that makes a nonzero hopping. | The tested sweep keeps the induced off-diagonal below numerical tolerance. | ATTEMPTED |
| Diagonal-only read | Use the nonzero diagonal as the charged-lepton ratio source. | With `b=0`, the ratio is `r=0`, not `r=1/2`. | ATTEMPTED |
| Add a bivector/action term | Source a separate nonzero hopping term. | Open and outside this projection-only claim. | OPEN |
| Dynamical or sector-factorized route | Select `r=1/2` by a later value principle. | Open and outside this projection-only claim. | OPEN |

### N2 - Wall-Independence Audit

The collapsed wall is the same in the direct and Schur routes: the specified
staggered single-bit-flip structure does not create an off-diagonal hw=1
hopping. The direct zero and the induced cancellation are two checks of that
route, not independent universal walls.

### N3 - Hidden-Wall Scan

The load-bearing inputs are explicit: the three displayed generators, the
hw=1 basis indices, and the finite Schur-complement computation. No empirical
mass, physical species bridge, source/action identification beyond this
candidate operator, or arbitrary value selector is consumed.

### N4 - Residual Matching

The residual addressed here is only the projection-geometry route for sourcing
`b != 0`. It matches the Door A projection sub-question, not the broader
action-axis/equal-block measure question.

### N5 - Rhetoric Audit

"Does not source `r=1/2`" means "does not source it through this specified
projection route." The note does not make a claim about all actions, all
native operators, all bivectors, or all dynamics.

### N6 - Partial-Closure Path Scan

A separate action term, bivector source, measure principle, record readout, or
dynamical selector could still source `r=1/2`. This note does not call any of
those paths a new axiom and does not foreclose them.

### N7 - Steelman

A hostile reviewer could argue that the tested `K` is only one candidate and
that the physically relevant action may include additional Clifford or lattice
terms whose projection creates nonzero hopping. That objection is correct as a
broader research route. It does not break the narrow result for the displayed
single-bit-flip staggered operator.

### N8 - Cross-Cycle Echo

The recurring failure mode in this lane is to turn a failed route into a global
value no-go. This note avoids that by landing only the finite projection
cancellation and explicitly leaving other value-sourcing routes open.

## Verification

Run:

```bash
python3 scripts/flavor_hw1_staggered_projection_democratic_r0_2026_06_02.py
```

Expected result:

```text
SCORECARD PASS=5 FAIL=0
```
