# Kinetic-Isotropy 3D Simultaneous-Tick Bounded Theorem

**Date:** 2026-06-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope note:** conditional theorem on the named site-license setup,
the `2^3` Bloch cell, the staggered `eta_mu`/`epsilon` pattern, the
one-Grassmann carrier, and the explicit factorized-realization input. Within
the analyzed 3D single-tick, permutation-equivariant, and factorized surfaces,
covariant polynomial ticks are flat, the linear permutation-equivariant sweep
finds no dispersive unitary, exhibited dispersive ticks have quantized drift,
and the factorized decorated-shift class has exactly linear bands with no
cone at this carrier density.
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py`](../scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py).
**Runner cache:**
[`logs/runner-cache/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.txt`](../logs/runner-cache/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.txt).

---

## Result

For the stated conditional setup, the runner establishes the following bounded
3D structural facts.

1. **Site-license degree table.** Same-component hops are distance-2 moves, so
   every diagonal Bloch entry is momentum-independent. A nonzero off-diagonal
   entry only connects parity partners, and each such entry uses offsets along
   that partner axis only. Unitarity then kills the two-term blend in each
   entry because the cross terms live in independent Fourier modes.
2. **Multivariable monomial lemma.** A finite Laurent polynomial that is
   unimodular on the torus is a monomial. Therefore a unitary finite-range
   permutation tick has determinant `e^{iD} z_1^{w_1} z_2^{w_2} z_3^{w_3}` and
   carries an integer winding vector.
3. **Covariant polynomial flatness.** The staggered nearest-neighbor Bloch
   operator `D(k)` is Hermitian with spectrum
   `+-sqrt(sum_i sin^2(k_i/2))`. If `U(k) = f(D(k))` for polynomial `f`, then
   unitarity requires `|f(lambda)| = 1` on a real continuum, forcing `f` to be
   constant. This analyzed covariant polynomial class is flat.
4. **Linear permutation-equivariant boundary.** Orbit reduction gives four
   component orbits and six hop orbits. The exact polynomial unitarity
   equations contain the per-orbit and opposite-side-hop bilinear kills used by
   the branch pass. The deterministic leaf sweep found no dispersive unitary
   among optimizer endpoints. The endpoint count is diagnostic rather than a
   coverage threshold; the sweep-grade boundary is the absence of a dispersive
   witness, with the exact kill structure as the algebraic backbone.
5. **Quantized drift witnesses.** Site-allowed single-axis shifts, mixed
   four-cycles, and staircase cycles are unitary and dispersive. Their bands
   are monomial roots, so the slopes are rational winding-per-cycle-length
   vectors such as `(1/2, 1/2, 0)` in site units. Face-diagonal and
   body-diagonal comparator geometries are outside the site license at this
   carrier density.
6. **Factorized decorated-shift class.** The eta-decorated per-axis shifts
   satisfy `S_i^2 = e^{-ik_i} I`, are equalized by axis permutations up to the
   staggered sign gauge, and pairwise anticommute. Reordering the three-factor
   cycle changes only a central sign. Unequal protocol weights factor into
   quantized whole-cell translations. Sampled words through length six have
   `W^2` scalar, matching the algebraic expectation from central squares and
   pairwise anticommutation; the class has exactly linear drift bands and does
   not contain the curved staggered cone at this density.

The load-bearing extra input is the **factorized-realization input**: the
realized 3D protocol is the symmetric per-axis decorated-shift cycle. This note
does not derive that selection. It records that, once this input is supplied,
the analyzed surfaces leave quantized drift cells rather than a continuous
speed dial.

## Boundaries

- This note adds no framework premise, primitive, controlled-data action,
  empirical input, weighting rule, probability rule, normalization rule, or
  audit status.
- It does not modify the registered kinetic-isotropy primitive. The approved
  primitive remains only structural OS0 kinetic-form isotropy `c_t = c_s`.
- It does not derive the factorized-realization input. The mixed-cycle,
  staircase, and unequal-weight constructions are explicit competitor cells.
- It does not claim an exhaustive classification of all non-covariant,
  amplitude-mixing single ticks. Those remain a named open surface.
- It does not derive a 3D matter cone. The runner shows the cone is absent
  from the factorized decorated-shift class at this carrier density, so any
  curved matter dispersion requires additional content.
- It does not import the known diagonal-hop automata as evidence. They are used
  only as comparator geometries, and those geometries are checked directly
  against the site license.

## Falsifiers

- A dispersive unitary in the analyzed covariant polynomial class.
- A dispersive unitary in the linear permutation-equivariant leaf systems.
- A site-allowed single tick or factorized decorated-shift composite with a
  curved band or continuously tunable slope inside the analyzed class.
- A derivation selecting a different realized 3D protocol, which would replace
  the factorized-realization input rather than refute the local computations.

## Negative-Claim Discipline Gate

The negative parts are scoped to the analyzed classes above.

- **N1 alternative routes:** polynomial functions of `D(k)` are flat by
  continuum unimodularity; linear permutation-equivariant tuning is swept leaf
  by leaf; diagonal-hop comparator geometries fail the site-license check;
  mixed-cycle and staircase drifts are not excluded and are exhibited;
  amplitude-mixing non-covariant ticks and larger cells remain open.
- **N2 wall independence:** the site-license wall, unitarity wall, covariance
  conditions, and factorized-realization input do separate jobs. The staircase
  witness is site-allowed, unitary, dispersive, and non-covariant, so the
  covariance boundary is not merely the site-license boundary.
- **N3 hidden-wall scan:** the `2^3` Bloch cell, staggered sign pattern,
  linear/projective covariance split, and symmetric per-axis selection are all
  named. The symmetric cycle is not treated as automatic.
- **N4 residual matching:** the residual answered here is the 3D
  simultaneous-tick structural question at this carrier density. The answer is
  quantized drift plus a named realization input, not a derived exhaustive speed
  selector.
- **N5 rhetoric audit:** "flat" is restricted to the covariant polynomial and
  swept linear equivariant classes. "No cone" is restricted to the factorized
  decorated-shift class at this density. "No continuous dial" is restricted to
  the analyzed surfaces.
- **N6 partial-closure scan:** exact algebraic closure of the linear
  permutation-equivariant leaves and the general amplitude-mixing family remain
  possible strengthening targets.
- **N7 steelman:** the theorem does not remove selection content; it relocates
  it into the explicit factorized-realization input while showing that the
  analyzed alternatives are quantized rather than continuously tunable.
- **N8 cross-cycle echo:** the one-dimensional flat/saturating dichotomy
  becomes a 3D quantized-drift family. Quantization survives; uniqueness of the
  dispersive cell does not.

## Reproduction

```bash
PYTHONHASHSEED=0 python3 scripts/kinetic_isotropy_3d_simultaneous_tick_2026_06_10.py
```

Expected scorecard: `PASS=20 FAIL=0`. The full permutation-equivariant leaf
sweep is intentionally heavier than the local symbolic checks. Its
optimizer-distinct endpoint count is a diagnostic detail that may vary across
fresh runs; the pass/fail boundary is whether a dispersive endpoint is found.

## Dependencies

- [STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md](STAGGERED_SITE_LICENSE_TICK_DICHOTOMY_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  supplies the one-dimensional site-license dichotomy and monomial machinery.
- [KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_FROM_STRICT_LICENSE_CHIRAL_QUANTIZATION_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  supplies the strict-license chiral quantization setup.
- [KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md](KINETIC_ISOTROPY_COMPOSITION_CLOSURE_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  supplies the `2^3` cell and prior composition-closure bookkeeping.
- [STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
  supplies the staggered `eta_mu` phase pattern.
- [STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md](STAGGERED_SCHEME_FORCED_BY_ONE_QUBIT_PER_SITE_LOCALITY_NARROW_THEOREM_NOTE_2026-06-06.md)
  supplies the one-Grassmann-per-site carrier.

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency. The independent audit lane is the only status
authority.
