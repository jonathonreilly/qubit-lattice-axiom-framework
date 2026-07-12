# Locked Record Outcomes and the Conditional Statistical-Slot Bridge

**Date:** 2026-07-03
**Repair update:** 2026-07-12
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets no
audit outcome and changes no premise-registry or audit-owned surface.
**Primary runner:**
[`scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py`](../scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.txt`](../logs/runner-cache/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.txt)

The filename is retained for citation stability. The repaired claim is narrower
than the historical title encoded in that filename.

> **Bounded claim.** On four explicitly enumerated reciprocal real-channel
> matrices, conjugate mixed curvature enters the determinant after the
> K-real restriction `c = conjugate(b)` and is absent while `b` and `c` are
> independent. Separately, if the statistical rule “one locked admissible
> possibility is one statistical slot” is supplied, one locked complex
> outcome and its two Cartesian component labels have slot counts one and two.
> The Record axiom does not supply that statistical rule and does not forbid
> two component readouts determined by the same record content. Neither result
> selects a physical slotting, derives `r = 1/2`, or attributes `r` to a
> partition-function ratio.

## Repair finding and disposition

The earlier source inherited the withdrawn map

```text
rho = (pi/g)/Z_d,
r = 1/(2 rho),
```

and treated a factor-two ratio between partition/kernel cells as a route to
the two `r` endpoints. That attribution is withdrawn. The repaired companion
note
[`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md)
establishes the consistent replacement:

- for the same density `exp[-beta(3a^2+6|b|^2)]`, Cartesian and polar
  integration both give `<|b|^2>/<a^2> = 1`;
- multiplicative normalization cancels from a normalized moment;
- older `2 pi/g` and `pi/g` cells use different quadratic kernels or
  determinant powers and are support-only arithmetic;
- `r = 1/2` follows only after supplying the aggregate outcome-cell condition
  `E_s = E_d`, whereas the aggregate real-dimension condition
  `E_d = 2 E_s` gives `r = 1`.

This note reproduces those facts without using any partition value on the
`r` derivation path. It also narrows the former Record “collision” claim: the
runner now exhibits a countermodel to any inference from Record content alone
to a one-slot rule.

## Inputs and question

The two Record sentences used here are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and guarded by
the runner:

> “When present, a record locks exactly one admissible local possibility.”

> “A readout value is determined by record content alone.”

The question is whether these sentences also imply the proposed statistical
rule

> one locked admissible local possibility is one statistical slot.

They do not state that rule. It is tested below only as an explicit supplied
condition. The relevant outcome indexing is also supplied context from
[`KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md),
not generic Record-axiom content.

## Result 1 — K-real-section determinant localization on four channels

For the four displayed real matrices `X`, define

```text
A_X(a,b,c) = a I + b X + c X^T.
```

The runner computes the determinants symbolically:

```text
cycle:          a^3 + b^3 + c^3 - 3abc
two-step path:  a^3 - 2abc
single edge:    a^3 - abc
two-edge star:  a^3 - 2abc
```

With `c` independent, these polynomials contain no `conjugate(b)` symbol and
are harmonic as functions of `b = x+iy`. After the K-real restriction
`c = conjugate(b)`, their mixed derivatives are, respectively,

```text
d_b d_bbar det = -3a, -2a, -a, -2a.
```

A conjugate-contaminated negative control has nonzero mixed curvature before
the restriction, so the test can fail. The result is exact on the four named
channels. It is not an enumeration of all `C_3`-equivariant couplings and does
not show that K-reality selects a statistical slotting.

## Result 2 — conditional locked-record slot-count mismatch

The Record sentences allow one record content `b = x+iy` to determine both
component readouts

```text
f_Re(b) = x,
f_Im(b) = y.
```

Thus one locked possibility can have two distinct readout functions while
each readout remains determined by record content alone. The runner constructs
this countermodel explicitly. Record content-determination by itself neither
equates the number of readout functions with the number of locked
possibilities nor identifies either number with a statistical slot count.

Now condition on the additional rule

```text
statistical slots = locked admissible possibilities.
```

The full supplied bridge is retained verbatim for downstream source guards:

one record locking one admissible local possibility is one statistical slot,
and the relevant locked possibilities for the generation doublet are the
K/CPT record-outcome orbits rather than the real components of the fluctuation
coordinate.

For one locked complex outcome, outcome slotting has count one. Assigning one
slot to each Cartesian component label has count two, so it fails that supplied
equality. This is a conditional count mismatch, not a contradiction with the
Record axiom alone and not a derivation that outcome slotting is physical.

The distinction is physically consequential rather than a relabeling: after
one separately supplies the aggregate channel-energy law

```text
E_s = epsilon,
E_d = n_d epsilon,
```

the exact algebra `E_s=3a^2`, `E_d=6|b|^2` gives

```text
n_d = 2  ->  r = 1,   Q = 1,
n_d = 1  ->  r = 1/2, Q = 2/3.
```

The runner also checks a wrong-count discriminator `n_d=3`, which gives
`r=3/2`. These are conditional consequences of the supplied aggregate law;
the Record sentences and determinant localization do not choose `n_d`.

## Gaussian and partition/kernel checks

For the diagnostic density

```text
exp[-beta(3a^2+6|b|^2)], beta > 0,
```

independent Cartesian and polar integrations give

```text
<a^2> = 1/(6 beta),
<|b|^2> = 1/(6 beta),
r_moment = 1.
```

The same-density Cartesian and polar partition integrals are both
`pi/(6 beta)`. There is no factor two between coordinate descriptions of this
density.

For parity with the repaired companion note, the runner separately reproduces
the older support-only cells:

```text
real two-coordinate Gaussian with kernel g/2:  Z = 2 pi/g,
polar complex Gaussian with kernel g:          Z = pi/g.
```

These are different kernels. Their factor-two ratio is not a normalization
choice for one density and supplies no equation for `r`.

## Import and support inventory

- **Approved foundation:** `minimal_axioms`; its Record sentences supply no
  statistical-slot rule.
- **Bounded supplied context:** K/CPT outcome indexing from the linked
  supplied-context bridge.
- **Exact local algebra:** the four determinant formulas, their mixed
  derivatives, the conditional slot counts, Gaussian integrals, and the
  conditional maps from `n_d` to `(r,Q)`.
- **Support-only arithmetic:** the decoupled `2 pi/g` and `pi/g` cells.
- **Not consumed:** PDG values, fitted numbers, empirical thresholds, or an
  imported physical species/readout bridge.

## No-Go Discipline Gate

The negative content is limited to current-source nonselection: the enumerated
inputs do not themselves supply the statistical-slot rule or choose `n_d`.

### N1 — Alternative-route enumeration

1. **Record text — ATTEMPTED.** The runner guards both quoted sentences and
   constructs two component readouts determined by one record content. Record
   therefore does not entail one statistical slot per possibility.
2. **K-real determinant localization — ATTEMPTED.** The four exact formulas
   localize conjugate dependence but contain no slot-count equation.
3. **Static complex structure — ATTEMPTED.** The bounded
   [`tested-static-readout no-go`](KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md)
   already shows that the static structure does not select between the two
   countings on its stated surface.
4. **Gaussian moment and partition normalization — ATTEMPTED.** The honest
   moment gives `r=1`; multiplicative normalization cancels. Different-kernel
   partition cells do not select `r`.
5. **Orbit indexing — ATTEMPTED.** The supplied-context bridge names outcome
   cells but expressly supplies no weighting or energy equality.
6. **Dynamics, Admissibility, and record production — OPEN.** No concrete
   construction of those routes is tested here.

### N2 — Wall-independence audit

After conditioning on the supplied K/CPT outcome context, one operative
selection residual remains: the map from a locked possibility to a statistical
slot. The aggregate energy law is an explicit downstream condition used only
to show why the count matters; it is not claimed as a second independently
derived wall.

### N3 — Hidden-wall scan

K/CPT outcome indexing and the one-slot rule are labeled supplied conditions;
the Gaussian is diagnostic; the four channels are enumerated rather than
universalized; the `Q` map is exact conditional algebra; no empirical input,
probability law, standard-QFT measure, or physical species bridge is hidden in
the conclusion.

### N4 — Residual matching

| source | source role | residual used here | match |
|---|---|---|---|
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | Record locking and content-determination sentences | whether Record also equates possibilities and statistical slots | yes |
| [`KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md`](KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md) | supplied orbit indexing and orbit-constant readout | whether orbit labels also fix statistical weights | yes |
| [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md) | repaired Gaussian and conditional equipartition arithmetic | whether partition values derive `r=1/2` | yes |
| [paired runner](../scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py) | exact local checks and Record countermodel | whether the displayed conditional implications hold | yes |

### N5 — Rhetoric audit

“Does not supply” refers only to the named current-source surface. The note
does not claim that Record-compatible future dynamics, Admissibility, or a
physical action cannot derive a slot rule. “Mismatch” is always conditioned on
the supplied one-slot equality and is not called an axiom contradiction.

### N6 — Partial-closure path scan

The residual changes the conditional value of `r` and `Q`, so it is not a
naming convention. A concrete retained derivation from record-production
dynamics, Admissibility, or a physical measure could close it. Explicit owner
approval through a reviewed premise-registry change is a separate governance
path, but this note neither requests nor infers such approval.

### N7 — Steelman

A record can determine many readout functions; a future theory could then give
those functions independent statistical weight through its action or measure.
Conversely, record-production dynamics could make the orbit outcome, rather
than its coordinates, the physical sample space. The present runner constructs
neither route. This blocks any universal no-go or physical-selection claim.

### N8 — Cross-cycle echo

The repaired companion note found the same distinction: orbit labels can be
supplied while equal energy per outcome cell remains unselected. The static
readout note likewise leaves dynamical selection open. Historical admission or
campaign language is not reused because no admission premise class exists.

**No-Go Discipline result:** `PASS` for the narrow current-source
nonselection boundary. It would be `FAIL` for a universal claim that no future
Record-compatible dynamics can derive the outcome-cell rule; this note makes
no such claim.

## What this note does not claim

- no derivation, adoption, or empirical validation of `r=1/2`;
- no inference from a partition-function ratio to `r`;
- no contradiction between two content-determined component readouts and the
  Record axiom;
- no enumeration of all reciprocal or `C_3`-equivariant channels;
- no new axiom, approved primitive, audit verdict, or effective-status change;
- no derivation of the generation Yukawa form, species content, or R-eta
  readout obligations.

## Reproduction ledger

The paired runner checks the two live Record quotations, four determinant
formulas, off-section harmonicity, K-real mixed derivatives, a conjugate-
contaminated negative control, the Record countermodel, conditional slot
counts, same-density Gaussian moments in Cartesian and polar coordinates,
decoupled different-kernel partition cells, both conditional endpoints, and a
wrong-count discriminator.

Run:

```bash
python3 scripts/frontier_koide_occupancy_locked_record_outcomes_2026_07_03.py
```

Exit code is zero iff `FAIL=0`. Independent audit is required before any
status promotion.
