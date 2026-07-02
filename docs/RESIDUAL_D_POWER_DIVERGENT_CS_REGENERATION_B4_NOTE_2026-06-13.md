# Residual-D Power-Divergent c_s Regeneration vs the B4-Cut Discrete-Tick Measure

**Date:** 2026-06-13
**Claim type:** positive_theorem
**Type:** positive_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The `positive_theorem` label is a source-side
claim-boundary declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_residual_d_power_divergent_cs_regeneration_b4_2026_06_13.py`](../scripts/frontier_residual_d_power_divergent_cs_regeneration_b4_2026_06_13.py)
**Cached runner output:**
[`logs/runner-cache/frontier_residual_d_power_divergent_cs_regeneration_b4_2026_06_13.txt`](../logs/runner-cache/frontier_residual_d_power_divergent_cs_regeneration_b4_2026_06_13.txt)

---

## Role

This note treats the open **residual D** named in
`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`
section (D). Residual D is the genuine
Collins-Perez-Sudarsky-Urrutia-Vucetich naturalness target: not the logarithmic
running, but the **power-divergent** (`a^-2`) UV regeneration that feeds the
lattice dimension-6 hypercubic anisotropy back into the **marginal**
(dimension-4) velocity coefficient `c_s`. The interacting attractor note is
context for the question, not a premise of the theorem below.

The retained B4 radiative-stability theorem
([`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md`](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md))
gives `Sigma_t = Sigma_s` for the **marginal** velocity-anisotropy operator on the
OS0 (`c_t = c_s`) discrete-tick surface. It establishes the marginal protection
but does not, by itself, address whether the **power-divergent** feed-through is
also blocked. This note asks: does the **same** B4 axis-relabel symmetry that
zeroes the marginal also forbid the power-divergent feed-through **on the
discrete-tick B4 measure** (temporal and spatial Brillouin zone both cut at
`pi/a`), while the **continuous-time** measure (uncut temporal integral over `R`,
spatial BZ cut at `pi/a`) lets it through?

This is a group-theory and finite-lattice statement about a single
power-divergent loop integrand evaluated under two measures. It consumes the
approved `kinetic_isotropy_primitive` (the OS0 kinetic-form surface); it does not
derive that primitive, does not add a dynamics, and does not set an audit
verdict.

## Result

On the OS0 discrete-tick B4 measure, the power-divergent feed-through is
B4-isotropic: its marginal projection vanishes,

```text
    delta_c_s_marginal (B4-cut)  =  6.9e-18   (machine zero).
```

Breaking the temporal direction's B4-covariance regenerates a robustly nonzero
marginal anisotropy,

```text
    delta_c_s (continuous-time)  =  +3.5e-3   (nonzero, stable).
```

The protection is the **B4-covariance of the discrete-tick regulator** -- all four
directions carry the same lattice gluon block and the same cut Brillouin zone, so
the temporal and spatial curvature integrals are exact axis-relabel images. The
runner's block-vs-range decomposition (Part D) shows the **dominant** breaker is
the temporal **block form**, not the integration range: replacing the lattice
temporal block `(2 sin q_0/2)^2` with the continuum `q_0^2` -- even keeping the
measure **fully cut** -- already regenerates a nonzero marginal anisotropy
(`+1.2e-2`), larger than the full continuous-time value; un-cutting the range adds
to it. (So the naive "the difference is only the measure" reading is **incorrect**:
the continuum temporal block is itself non-B4-covariant.)

On the B4-cut measure the power divergence is confined to the dimension-6
B4-invariant cubic harmonic `sum_mu p_mu^4` (the retained `c_4 = -1/3` family):
the dimension-4 marginal `c_t - c_s` operator is projected out of the B4 orbit
average, while the cubic harmonic is B4-invariant and survives. With the approved
scale-reference primitive `a^-1 = M_Pl`, the surviving dimension-6 residual at
`E = 1 GeV` is of order `(1/3)(E/M_Pl)^2`, i.e. Planck-suppressed.

Because the marginal projection of the power-divergent piece vanishes on the
framework's chosen OS0 surface, **the interacting residual D does not hit the
marginal velocity coefficient on that surface; the Collins power divergence is
confined to the Planck-suppressed dimension-6 level.** This is the
`positive_theorem` typing.

## Theorem

Assume the OS0 kinetic-form surface supplied by `kinetic_isotropy_primitive`
(`c_t = c_s`, OS0), and the symmetric `Z^4` (temporal and spatial BZ both cut at
`pi/a`) discrete-tick loop measure used by the retained B4 self-energy machinery.
Let `Sigma_powerdiv` denote the highest-UV-degree (power-divergent) component of
the one-loop velocity self-energy curvature, isolated as the single-gluon
tadpole `cos(q_mu)/qhat^2` that the external `p_mu^2` derivative of the rainbow
self-energy reduces to.

Then:

1. **(Marginal sanity.)** On the cut measure the full marginal curvature
   coefficient satisfies `Sigma_t = Sigma_s` to machine precision, reproducing the
   retained B4 protection (Part A). The diagonal quadratic kinetic form has one
   `B4` invariant coefficient (`c_t = c_s` forced), while the spatial cubic group
   alone leaves two.
2. **(Power-divergent scaling.)** `Sigma_powerdiv(a)` scales as `C / a^2`: the
   numerically fitted log-log slope is `-2.00000`, the halving ratio is `4.0000`,
   and `a^2 Sigma_powerdiv` is constant across the spacing grid to `~1e-13`
   (Part B). This is the genuine power divergence, not the logarithmic running.
3. **(Core.)** On the B4-cut measure the marginal projection of the
   power-divergent piece vanishes, `delta_c_s_marginal = 0` to machine precision
   (`6.9e-18`, Part C). Equivalently, the cut-measure power-divergent curvature
   4-vector is already B4-isotropic: its B4 signed-permutation orbit average
   leaves it unchanged. This zero is **genuine B4-covariance, not an artifact of
   the cut**: breaking B4 with an anisotropic (`xi = 1.5`) temporal block on the
   **same** fully-cut measure gives `Sigma_t - Sigma_s = 1.5e-2`, robustly nonzero.
4. **(B4-covariance breaking on continuous time.)** Continuous time breaks the
   discrete-tick B4-covariance and regenerates `Sigma_t - Sigma_s != 0`, robustly
   nonzero and stable as the temporal range widens (Part D). A block-vs-range
   decomposition isolates the driver: the non-B4-covariant continuum temporal
   block (`q_0^2`), **even with a fully cut measure**, already breaks it (`+1.2e-2`,
   larger than the full continuous-time value `+3.5e-3`), while the lattice block
   on the cut measure stays at machine zero. So the dominant breaker is the
   **block form**, not the integration range; only the fully B4-covariant
   discrete-tick regulator (same lattice block and cut BZ in all four directions)
   protects the marginal.
5. **(Confinement to dimension-6.)** On the B4-cut measure the power-divergent
   piece renormalizes the dimension-6 B4-invariant cubic harmonic `sum_mu p_mu^4`
   (allowed; the operator is B4-fixed under the orbit average), while the
   dimension-4 marginal `c_t - c_s` operator is projected out (no marginal
   regeneration). With `a^-1 = M_Pl`, the surviving dimension-6 residual is
   Planck-suppressed (Part E).

## The mechanism: discrete-tick B4-covariance

The power-divergent curvature density is a B4-covariant object built from lattice
blocks. On the discrete-tick regulator all four directions carry the **same**
gluon block `(2 sin q_mu/2)^2` and the **same** cut Brillouin zone `[-pi, pi]`, so
the `q_0 <-> q_x` axis swap is an exact symmetry of integrand-plus-measure and
`Sigma_t = Sigma_s`. The continuous-time limit (`a_tau -> 0`) breaks this in the
temporal direction two ways, both spoiling the axis swap: the gluon block changes
form (`(2 sin q_0/2)^2 -> q_0^2`) **and** the range un-cuts (`[-pi, pi] -> R`). The
runner's decomposition (Part D) shows the **block-form change is the dominant
breaker**: with the continuum block but a still-fully-cut measure the marginal
regeneration is already `+1.2e-2`, larger than the full continuous-time `+3.5e-3`,
whereas the lattice block on the cut measure is machine zero. So the protection is
the B4-covariance of the discrete-tick regulator -- the temporal direction on the
same hypercubic footing as space (the content of the kinetic-isotropy primitive
realized at the regulator level) -- **not** the integration range alone. This is
the lattice-level sharpening of the Collins-Reisz observation that the
continuous-time-with-spatial-cutoff regulator carries an unprotected
power-divergent marginal piece: here that obstruction is precisely the loss of the
temporal direction's B4-covariance.

## Boundary

This note is **marginal-sector only** on the OS0 discrete-tick surface. It does
**not**:

- close the full interacting theory: n-point functions beyond the two-point
  velocity self-energy, taste/doubler structure, and the `a -> 0` continuum limit
  are out of scope;
- touch the continuous-time horn where the Collins obstruction lives -- it only
  records that on that non-OS0 measure the same power-divergent piece **does**
  regenerate the marginal anisotropy (Part D is the explicit contrast, not a
  closure of that surface);
- supply a spacing-ratio theorem, an absolute clock rate, a physical-time
  theorem, a Lorentz-closure theorem, a Standard-Model-Extension bound
  comparison, or an empirical match;
- promote, derive, or amend the `kinetic_isotropy_primitive` -- it **consumes** the
  primitive (the OS0 kinetic-form surface) and adds no dynamics;
- add any axiom, primitive, repo vocabulary, or class tag;
- set or predict any audit status.

The complementary continuous-time naturalness gap remains as quantified in
`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`; that gap
is computed on the non-OS0 (continuous-time) surface and is unaffected by this
note. What this note adds is that the power divergence which drives that gap is
**locked to the loss of the temporal direction's B4-covariance** (the
non-B4-covariant continuum temporal block): on the framework's chosen OS0
discrete-tick regulator, where all four directions share the same lattice block
and cut BZ, the same UV piece does not reach the marginal coefficient.

## Reprove-and-cite ledger

- **Reproven here** (runner, from B4/lattice primitives): the `B4`/`O_h`
  diagonal-kinetic invariant counts; the cut-measure marginal `Sigma_t = Sigma_s`;
  the `a^-2` scaling of the isolated power-divergent piece (ratio, log-log slope,
  `a^2 Sigma` constancy); the vanishing B4-cut marginal projection and its
  invariance under the explicit B4 signed-permutation orbit average; the nonzero,
  stable continuous-time marginal regeneration; the block-vs-range decomposition
  showing the continuum temporal block (not the integration range) is the dominant
  B4-covariance breaker; the projection of the dimension-4 marginal operator out
  of, and the invariance of
  the dimension-6 cubic harmonic under, the B4 orbit average; the `-a^2/3`
  dimension-6 dispersion coefficient via sympy series; the Planck-suppressed
  dimension-6 size with `a^-1 = M_Pl`.
- **Cited** (comparator/scope only, never a derivation input):
  Collins-Perez-Sudarsky-Urrutia-Vucetich *PRL* **93** (2004) 191301 (the
  power-divergent marginal-regeneration naturalness problem); Reisz *CMP* (1988)
  (lattice power-counting; continuous-time-with-spatial-cutoff measure
  asymmetry). The literature sets the comparator framing; every identity above is
  reproven in the runner from `B4`/Haar/lattice primitives.

## Graph dependencies

- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  -- the approved primitive supplying the OS0 kinetic-form premise (`c_t = c_s`);
  chain-satisfies without bounding. This note consumes it.
- [EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md](EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  -- the retained marginal B4 protection whose self-energy machinery and
  conventions this note reuses; this note extends the marginal result to the
  power-divergent piece on the same cut measure.
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
  -- the approved units conversion `a^-1 = M_Pl` used in the optional dimension-6
  size estimate.
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
  -- the complementary spatial-cubic boundary: with spatial `O_h` alone, the
  marginal anisotropy is allowed.
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
  -- cited only for the axiom boundary: it does not supply time dynamics.

## Context and comparators

The following notes frame the question or comparison surface but are not
theorem premises here: `EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`
names residual D as open; `LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`
quantifies the continuous-time comparator gap; and
`EMERGENT_LORENTZ_INVARIANCE_NOTE.md` records the related dimension-6 cubic
dispersion surface. The identities used by this theorem are reproven in the
runner on the specified B4-cut and continuous-time measures.

## Runner summary

The runner verifies (17 PASS / 0 FAIL):

- Part A: the `B4`/`O_h` invariant counts and the cut-measure marginal
  `Sigma_t - Sigma_s = 0` to machine precision;
- Part B: the isolated power-divergent piece scales as `a^-2` (slope `-2.00000`,
  halving ratio `4.0000`, `a^2 Sigma` constant to `~1e-13`);
- Part C: the B4-cut marginal projection `delta_c_s_marginal = 0` (`6.9e-18`), its
  invariance under the explicit B4 signed-permutation orbit average, and a
  falsification (an anisotropic `xi = 1.5` temporal block on the same cut measure
  gives `Sigma_t - Sigma_s = 1.5e-2`, so the zero is genuine B4-covariance);
- Part D: continuous time regenerates a robustly nonzero, stable
  `Sigma_t - Sigma_s = +3.5e-3`; the block-vs-range decomposition shows the
  non-B4-covariant continuum temporal block (`+1.2e-2`, even with a fully cut
  measure) -- not the integration range -- is the dominant breaker, while the
  discrete-tick lattice block on the cut measure stays at machine zero;
- Part E: the power-divergent piece renormalizes the B4-invariant dimension-6
  cubic harmonic `sum_mu p_mu^4` (allowed) while the dimension-4 marginal operator
  is projected out (no marginal regeneration), the surviving residual being
  Planck-suppressed via `a^-1 = M_Pl`.

### Source-note boundary

**Hypothesis set:** (1) the three axioms + scale primitive; (2) the approved
`kinetic_isotropy_primitive` OS0 kinetic-form surface (`c_t = c_s`); (3) the
symmetric `Z^4` discrete-tick loop measure and its continuous-time counterpart as
the two measures under contrast; (4) standard one-loop self-energy structure with
its isolated power-divergent component. The result is a group-theory + finite
lattice statement on the marginal sector; n-point/taste/`a -> 0` and the
continuous-time horn are out of scope.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class
tag; only standard terms (Brillouin zone, power divergence, signed-permutation
orbit, hypercubic harmonic, lattice power-counting). No fitted / PDG / lattice-MC
/ `beta=6` / `g_bare` value is consumed. The Collins and Reisz references are
comparators, not derivation inputs; every identity is reproven in the runner.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of the retained B4 note, the interacting attractor note, the
naturalness-gap note, the `kinetic_isotropy_primitive`, or any upstream row. The
audit lane is the only status authority.
