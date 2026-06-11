# The Site-Licensed Tick Dichotomy Holds At Every Period: The Larger-Cell Mass-Hosting Residual Discharges

**Date:** 2026-06-11
**Claim type:** bounded_theorem (extends the landed period-2 flat-or-saturating
dichotomy to every finite period; discharges the dichotomy note's
larger-periodicity steelman for the one-component carrier class)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/site_license_tick_dichotomy_all_periods_2026_06_11.py`](../scripts/site_license_tick_dichotomy_all_periods_2026_06_11.py)
(SCORECARD: PASS=18, FAIL=0; cached:
[`logs/runner-cache/site_license_tick_dichotomy_all_periods_2026_06_11.txt`](../logs/runner-cache/site_license_tick_dichotomy_all_periods_2026_06_11.txt))

---

## What this closes (relative to the landed dichotomy)

The landed period-2 dichotomy
([`STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md`](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md))
proved flat-or-saturating for site-licensed unitary 2-site-periodic ticks and
named, as its strongest residual, the **larger-periodicity open**: a
larger-cell composite tick might host mass or a tunable cone slope,
localizing the kinetic-isotropy primitive's content in the periodicity scope.

This note discharges that residual at **every finite period**: the dichotomy
is periodicity-robust, the winding budget does not grow with the cell, no
licensed tick hosts curvature (mass) at any period, and the kinetic-isotropy
retirement chain's dichotomy leg loses its periodicity conditionality.

## The theorem (1D / per-axis, exact, all `p >= 1`)

**Setting.** Radius-1-in-sites, period-`p` translation-covariant unitary
one-tick updates of the one-component-per-site chain. Bloch form: a
`p x p` unitary `U(z)` whose entry `(j', j)` carries `z^c` only for cell
displacement `c` with `|j' + p c - j| <= 1`.

**Displacement-sum lemma.** The license confines `z`-dependence to the
two boundary corners `(0, p-1; z)` and `(p-1, 0; z^{-1})`. For any `k x k`
principal minor with `k < p`, every permutation term has total displacement
`p * (sum of c's)` bounded in magnitude by `k < p`, hence the `c`-sum is
zero: **all proper principal minors — in particular every symmetric function
`e_1 .. e_{p-1}` of the band values — are momentum-independent.** For
`k = p`, `|p * sum(c)| <= p` gives `det = A + B z + C z^{-1}` (runner
symbolic-minor section: fully symbolic for `p = 2..5`, numeric spot-check at
`p = 6`). This generalizes the period-2 note's constant-trace check in one
stroke.

**Winding budget.** Unitarity makes `det` a unimodular Laurent polynomial,
hence a monomial (block01's monomial lemma): `det = e^{iD} z^w` with
`w in {-1, 0, +1}` — **the winding budget does not grow with the period**
(runner winding-budget section).

**Self-inversive forcing.** Unimodular band values satisfy
`e_{p-k} = det * conj(e_k)` pointwise in `z` (runner self-inversive check).
For `w != 0`, evaluating at two momenta forces **every** intermediate
symmetric function to vanish (runner vanishing-forcing check):

```text
    chi(mu; z) = mu^p + (-1)^p e_p(z)  =  mu^p - (-1)^{p+1} e^{iD} z^w,
```

so the `p` bands are `omega_j(K) = (D' + 2 pi j + w K)/p` exactly (the
constant sign absorbed into `D'`), with **site-unit slope `w` at every
momentum** (runner band-formula section: spectrum = `p`-th roots of
`(-1)^{p+1} det`, set-exact at every sampled fiber, `p = 1..6`; second
differences identically zero).

**All-period dichotomy.**

```text
    { FLAT (w = 0: constant bands, no transport) }
                 or
    { SATURATING (w != 0: |v| = 1 site/tick at every momentum) }
```

No third cell at any period (runner flat/saturating checks).

**Mass-hosting corollary.** A massive dispersion has strictly nonzero
curvature at the band bottom; licensed dispersive bands have curvature
exactly zero. **No single site-licensed unitary tick hosts mass at any
finite period.** Mass enters only outside this class — a second per-site
component, interactions, or the separate factor — coherent with the
separate-factor chirality surface
([`CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md`](CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md))
and with the adjacency-rank note's on-site saturation (runner mass-corollary
section).

## Effect on the kinetic-isotropy retirement chain

The chain's dichotomy leg previously carried "2-site periodicity" as a
declared scope with the larger-cell composite as its strongest steelman.
After this note the leg reads: **for every finite periodicity**, dispersive
implies saturating. The retirement residual becomes:

```text
  spectrum-reflection transport + channel-envelope reading
  + one-component/site-license carrier reading + record-stack spectral reading
  + finite-periodicity covariance
```

with the periodicity item reduced from "the realized period might differ
from 2" to "the realized tick is translation-covariant at some finite
period" — a strictly weaker reading (any `p` now works), with
aperiodic/quasi-periodic ticks the surviving named open.

## Hostile witnesses (wall-independence)

| dropped wall | witness | outcome |
|---|---|---|
| site license | split-step walk (distance-2-in-sites moves) | curved band, slope range `[0.03, 0.77]`, max curvature `1.15`, tunable `|cos theta|` |
| unitarity | bosonic positive-transfer family | `xi` sweeps continuously (the irreducibility support's witness family; cited, not rebuilt) |
| finite period | aperiodic/quasi-periodic ticks | not covered — the surviving named open |

## No-Go Discipline Gate (for the negative leg)

The negative claim: "no dispersive site-licensed unitary tick of the
one-component carrier has a tunable or curved band at any finite period."

- **N1 alternative routes:** (1) momentum-dependent intermediate symmetric
  functions — RULED OUT structurally by the displacement-sum lemma;
  (2) winding growth with cell size (`|w| >= 2` at large `p`) — RULED OUT by
  the determinant degree bound + monomial lemma; (3) nonzero constant
  `e_k` coexisting with winding — RULED OUT by the self-inversive forcing
  lemma; (4) two components per site — outside the stated carrier class
  (block01's regime), inherited from the scheme-forcing row; (5)
  aperiodic/quasi-periodic ticks — NOT ruled out: NAMED OPEN, stated in
  scope.
- **N2 wall independence:** the collapsed wall set is {site license,
  unitarity, one-component density, finite periodicity}. Pairwise
  independent: dropping the license restores the split-step witness;
  dropping unitarity restores the positive-transfer sweep; dropping
  one-component returns the two-component-cell regime; dropping finite
  periodicity exits the Bloch setting (named open).
- **N3 hidden-wall scan:** "translation covariance at some finite period" —
  declared; "one component per site" — the landed scheme-forcing row, cited
  with its live status; "radius-1 in sites" — the license reading,
  fourth rung of the per-plaquette/block01/dichotomy lineage.
- **N4 residual matching:** the dichotomy's reduced periodicity residual
  ("the realized tick is dispersive") is inherited unchanged; the periodicity
  residual is replaced by the strictly weaker finite-covariance reading.
- **N5 rhetoric audit:** "no third cell at any period" is scoped to
  site-licensed unitary finite-period ticks of the one-component carrier in
  1D/per-axis; nothing is claimed about aperiodic ticks, two-component
  cells, or 3D simultaneity.
- **N6 partial-closure scan:** the `p = 2` case is the landed dichotomy;
  this note's displacement, winding, and self-inversive lemmas reduce to its
  constant-trace + two-circles mechanism at `p = 2` (the two-circles lemma is
  the `p = 2` shadow of the self-inversive forcing).
- **N7 steelman:** "the realized tick may be aperiodic, or a
  radius-growing composite that escapes every fixed-period Bloch
  decomposition." Acknowledged as the surviving named open — strictly
  narrower than the prior steelman (which needed only `p > 2`).
- **N8 cross-cycle echo:** same strict-license reading as per-plaquette
  (generator level), block01 (2-component cell), the dichotomy
  (realized-carrier density), now at all periods — fourth rung, same
  mechanism, declared.

## What this does not do

- It does not enumerate the licensed-unitary variety: the theorem classifies
  the **spectra** of licensed ticks; instances witness non-vacuity at every
  tested period (runner scope-honesty section).
- It does not cover aperiodic or quasi-periodic ticks (the named open), 3D
  simultaneity (the landed separate row
  `KINETIC_ISOTROPY_3D_SIMULTANEOUS_TICK_BOUNDED_THEOREM_NOTE_2026-06-10.md`),
  or interacting/radiative orders (the velocity-RG row).
- It does not derive unitarity or the license: both are the landed chain's
  readings, inherited with their conditionality.
- It does not add an axiom or primitive, and it does not set audit status.

## Falsifiers

- A site-licensed unitary period-`p` tick with a momentum-dependent proper
  principal minor (would refute the displacement-sum lemma).
- A licensed tick whose determinant has winding `|w| >= 2` (would refute
  the winding-budget lemma).
- A dispersive licensed tick with a nonzero intermediate symmetric function
  (would refute self-inversive forcing).
- A dispersive licensed tick with nonzero band curvature at any momentum
  (would refute the all-period dichotomy and re-open single-tick mass
  hosting).

## Dependencies

- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — the period-2 case and the residual this note discharges; landed but
  unaudited, conditionality inherited.
- [KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  — block01: the monomial lemma (consumed by the winding-budget step) and the
  split-step witness family; landed but unaudited, conditionality inherited.
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md)
  — the one-component carrier density; landed but unaudited, conditionality
  inherited.
- [TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  — the unitarity reading's grounding (the C/N readings); landed but
  unaudited, conditionality inherited.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  and
  [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md)
  — the retirement chain's target and independence surface (the
  positive-transfer witness family cited at the unitarity wall).
- [CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md](CHIRALITY_SEPARATE_FACTOR_DIRAC_MASS_ALGEBRA_SUPPORT_BOUNDED_NOTE_2026-06-08.md)
  — the surface the mass-hosting corollary points at.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.
