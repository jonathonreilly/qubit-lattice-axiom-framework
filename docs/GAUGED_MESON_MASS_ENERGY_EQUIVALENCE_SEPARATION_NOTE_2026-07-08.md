# Gauged Meson Mass-Energy Equivalence -- Static-Channel Separation And Emergent-Metric Universality On The I-GAUGE Comparator

**Date:** 2026-07-08
**Type:** bounded_theorem (measured-comparator legs only; the gated
statements are exact-diagonalization measurements on the declared I-GAUGE
bridge with printed validity discipline; no equivalence identity is
claimed)
**Claim type:** bounded_theorem (measured-comparator legs)
**Claim scope:** On the d = 1 staggered lattice Schwinger comparator
(import I-GAUGE, validated by the engine note), this note measures the
lowest-meson dispersion and gates two statements. First, static-channel
separation: at every stability-valid grid point the full field-mediated
dynamics places the meson's inertia-to-rest-energy diagnostic at least
0.30 closer to the equivalence value than the two-body static truncation
of the same model, which stays pinned at kinetic-functional values far
from equivalence -- the finite-coupling exhibit of the static-comparator
no-go's mediator requirement. Second, cross-species metric universality:
the emergent speed extracted from the meson band agrees between the two
species to at most 5.4 percent at every gated coupling. The
tautology-free two-band equivalence ratio is REPORTED but not gated: the
second-band identity is unstable across momentum sectors (level
crossings), and its operator-tagged identification is a named follow-up.
Nothing here derives the gauged surface from the axioms, closes a WEP
row, or sets an audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/gauged_meson_mass_energy_equivalence_2026_07_08.py`](../scripts/gauged_meson_mass_energy_equivalence_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/gauged_meson_mass_energy_equivalence_2026_07_08.txt`](../logs/runner-cache/gauged_meson_mass_energy_equivalence_2026_07_08.txt)

## Why This Note Exists

The static-comparator no-go proves that no momentum-independent
interaction can carry binding energy into composite inertia: the
composite mass is a kinetic-band functional, and the named escape is a
dynamical mediator. The record-preservation dynamics-form theorem forces
exactly that escape class -- gauge-covariant hopping through link
variables. This note is the first measurement on an instantiation of the
forced class: it asks whether the field-mediated model behaves
differently from its own static truncation in precisely the way the sum
rule predicts, and whether the emergent kinematics is species-blind.

## Imports And Premises

- **I-GAUGE** (inherited from the engine validation note): Hamiltonian
  staggered fermions on a ring of `N = 16` sites with `U(1)` links,
  electric term, ring Gauss law reduced to a single Wilson-line rotor
  (`W_MAX = 4`). A comparator/bridge instantiation in `d = 1` of the
  forced covariant-hopping class; not a derivation of the framework's
  gauged surface.
- Engine flags inherited and respected: charge-zero ring Gauss sector,
  interior-supported magnetic-translation checks, decoupled `g = 0`
  comparator.
- Mass-lane surface inherited by citation through the static-comparator
  no-go note's dependency chain.

## Convention Note -- Momentum Unit

The magnetic translation symmetry moves TWO staggered sites (one
physical cell). Its eigenphase `theta` therefore corresponds to physical
momentum `P = theta / 2` in staggered-site units, so the three fitted
momenta on the 8-cell ring are `P_k = pi k / 8`, `k in {0, 1, 2}`. The
first draft of this runner used `2 pi k / 8` and produced spuriously
small emergent speeds; the corrected unit is part of the validated
contract and is regression-checked against the engine cache (CHECK-01,
reproduction to `1.4e-13`).

## The Measurement

Grid: `m in {0.2, 0.4}`, `g in {0.6, 1.0, 1.4, 2.0}`, `N = 16`,
momentum-projected sparse Lanczos in the charge-zero sector.

Per grid point, from the lowest meson band `E_2(P_k)`:

- **FIT-REL:** `E_2(P)^2 = E_0^2 + c^2 P^2 + d P^4` (exactly
  determined); extracts the emergent speed `c^2`.
- **FIT-NR:** `E_2(P) = E_0 + P^2 / (2 M_comp) + e P^4`; extracts the
  inertial mass `M_comp`.
- **Diagnostics:** `D := M_comp / E_0` (unit-`c` comparison) for the
  full model and for its two-body truncation `T2` (free vacuum plus
  single particle-hole states at `W = 0`: the static channel -- pair
  creation and holonomy excitation are exactly what it removes).
- **Validity:** a point is stability-valid iff the `N = 12` vs `N = 16`
  drift of `D` is at most `0.03`. Seven of eight points qualify; the
  point `(m = 0.2, g = 2.0)` self-excludes (drift `1.7e12` from
  momentum-projector null columns at strong coupling, printed as
  `projector-null-col` flags). The excluded point is reported, not
  gated.

## Gated Results

**R1 -- static-channel separation (decisive gate).** At every
stability-valid point, `|D_full - D_T2| >= 0.30`. Measured separations:

```text
    m = 0.2:  0.76 (g=0.6)   1.13 (g=1.0)   1.39 (g=1.4)
    m = 0.4:  0.65 (g=0.6)   1.09 (g=1.0)   1.31 (g=1.4)   1.94 (g=2.0)
```

The full-Fock diagnostic sits at `D_full in [1.13, 1.78]` while the
static truncation of the same Hamiltonian sits at `D_T2 in [-0.17,
0.51]` -- pinned far from equivalence, exactly as the kinetic-functional
sum rule requires for a static channel. The separation grows
monotonically with coupling at both masses.

**R2 -- cross-species metric universality (gated at 10 percent).** The
emergent speed extracted independently from each species' meson band
agrees at every coupling with both species valid:

```text
    g = 0.6:  c^2 = (0.9031, 0.8711)   deviation 3.7%
    g = 1.0:  c^2 = (0.7831, 0.7433)   deviation 5.4%
    g = 1.4:  c^2 = (0.6726, 0.6436)   deviation 4.5%
```

Two species with rest energies differing by up to 48 percent propagate
on the same emergent light cone at the few-percent level. This is the
tautology-free equivalence-flavored leg: the two spectra are independent
inputs and nothing in the fit forces their `c^2` to agree.

**R3 -- window trend.** `c^2(g)` is monotone decreasing in `g` at both
masses (from `0.90` at `g = 0.6` to `0.56` at `g = 2.0`), with the
weakest-coupling value gated at `>= 0.85`: the comparator approaches
unit-`c` kinematics as the coupling weakens, and the strong-coupling
metric renormalization is a smooth measured trend, not a breakdown.

**R4 -- fit-consistency isotropy (near-tautological; NOT an equivalence
gate).** The unit-corrected single-band ratio
`R := M_comp c^2 / E_0` satisfies `|R - 1| <= 0.0203` at every point.
With three momenta and two four-parameter-family fits this ratio is
forced toward `1` by fit algebra alone; it is gated only as an internal
consistency check on the two extractions and is explicitly NOT evidence
of equivalence. The honest equivalence evidence in this note is R1 plus
R2.

**R5 -- Fock attribution (mechanism leg).** The pair-fluctuation weight
of the meson state (its projection deficit against the T2 subspace,
range `0.25` to `0.61`) and the static-vs-full discrepancy
`|D_T2 - D_full|` are positively rank-associated across the grid:
Spearman-style correlation `rho = 0.857`. The single point of maximum
pair weight is not the point of maximum discrepancy (printed honestly:
the association is grid-wide, not pointwise), but the gated positive
association attributes the static channel's failure to the
pair-creation channel -- the loose attribution gate this leg was scoped
to, not a precision claim.

**R6 -- finite-size stability spot.** At `(m = 0.3, g = 1.0)`:
`D(N=12) = 1.3281` vs `D(N=16) = 1.3172`, drift `0.011`, gate `0.15`.

## Reported, Not Gated

- **Two-band equivalence ratio (the tautology-free identity test).**
  The design called for `(M_2 / M_1) (E_{0,1} / E_{0,2}) = 1` across
  the first two meson bands. The second-band identity is unstable
  across momentum sectors -- level crossings scramble which eigenstate
  continues the band, and the fitted `M_2` swings through `1.6`, `9.3`,
  `111.6`, and negative values across the grid. Flag printed:
  `BAND2-REPORTED(level-crossing; identity unstable across sectors;
  two-band ratio deferred to operator-tagged follow-up)`. The named
  follow-up is operator-tagged band identification (tag eigenstates by
  matrix elements of a reference excitation operator, not by energy
  ordering).
- **T2 sum-rule cross-check.** Finite-difference curvature of the T2
  band bottom agrees with `1 / M_T2` in sign and to roughly 20-40
  percent; the `W = 0` truncation is not exactly translation-invariant
  (commutator residuals up to `1.02` printed), so exact agreement is
  not expected and none is claimed.
- The excluded point `(m = 0.2, g = 2.0)` with its projector-null-col
  diagnostics.

## What This Does And Does Not Show

It shows: on the forced interaction class's `d = 1` instantiation, the
field-mediated dynamics and its own static truncation are cleanly
separated in exactly the direction the mediator requirement predicts;
the emergent metric is species-universal at the few-percent level; the
mechanism is attributed to pair mixing.

It does not show: mass-energy equivalence as an identity. The
metric-corrected single-band ratio is fit-forced (R4), the two-band
identity test is deferred (level crossings), and `c^2 < 1` at finite
coupling means all equivalence statements are relative to the emergent
metric, not the microscopic unit. The identity-grade test lives in the
named operator-tagged follow-up.

## Boundaries

- `d = 1` comparator; `N = 16` (8 cells); three momenta per fit
  (exactly-determined fits -- the reason R4 is labeled
  near-tautological).
- I-GAUGE is an import/bridge realization, not a derivation from the
  axioms.
- Equal treatment of both species is by construction; no unequal-mass
  composite is measured here.
- No gravitational content is supplied; no WEP row is closed.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md`](GAUGED_SCHWINGER_STAGGERED_ED_ENGINE_VALIDATION_NOTE_2026-07-08.md)
  -- the validated machinery and the I-GAUGE declaration this note
  inherits.
- [`COMPOSITE_MASS_ENERGY_EQUIVALENCE_STATIC_COMPARATOR_NO_GO_NOTE_2026-07-08.md`](COMPOSITE_MASS_ENERGY_EQUIVALENCE_STATIC_COMPARATOR_NO_GO_NOTE_2026-07-08.md)
  -- the sum rule and mediator requirement whose finite-coupling
  exhibit is R1.
- [`DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md`](DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md)
  -- the forced covariant-hopping class that I-GAUGE instantiates.

## Runner And Cache

Primary runner:
[`scripts/gauged_meson_mass_energy_equivalence_2026_07_08.py`](../scripts/gauged_meson_mass_energy_equivalence_2026_07_08.py)

Runner cache:
[`logs/runner-cache/gauged_meson_mass_energy_equivalence_2026_07_08.txt`](../logs/runner-cache/gauged_meson_mass_energy_equivalence_2026_07_08.txt)

Supervisor-executed runner result:

```text
TOTAL PASS elapsed=915.35s
```

with all six checks reporting ok: engine reproduction `1.4e-13`;
separation and universality per R1/R2; window trend per R3; worst
`|R - 1| = 0.0203` per R4; `rho = 0.857` per R5; spot drift `0.011` per
R6.

## Changelog

- **2026-07-08.** Initial note. Three findings from the measurement
  reruns are recorded as part of the result: (1) the momentum-unit fix
  (magnetic translation moves one physical cell = two staggered sites;
  `P = theta / 2`), without which the emergent speeds come out
  spuriously small; (2) the single-band ratio `R = M c^2 / E_0` is
  near-tautological for exactly-determined fits and was demoted from
  decisive gate to fit-consistency check, with the decisive role
  reassigned to static-channel separation plus cross-species metric
  universality; (3) the two-band identity test failed honestly to
  level crossings and is deferred to the operator-tagged follow-up
  rather than gated on unstable data. Local runner result
  `TOTAL PASS`, seven of eight grid points stability-valid.
