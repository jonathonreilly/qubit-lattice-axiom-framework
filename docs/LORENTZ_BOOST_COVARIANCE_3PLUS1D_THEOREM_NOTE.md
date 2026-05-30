# 3+1D SO(3,1) Boost Covariance of the Path-Sum 2-Point Function

**Date:** 2026-04-25
**Date of scope repair:** 2026-05-29
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** bounded theorem candidate on the supplied continuum-limit
free-scalar Hamiltonian-lattice surface, with a structural finite-`a`
cubic-harmonic `K_4` correction statement. This row does not claim a
Planck-unit phenomenological readout or a finite-`a` strict light-cone
theorem.
**Script:** `scripts/frontier_lorentz_boost_3plus1d.py` (PASS=57, FAIL=0)
**Companions:**
[LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md](LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md),
`ANGULAR_KERNEL_UNDERDETERMINATION_NO_GO_NOTE.md`,
[EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)

## 2026-05-29 Audit Repair

The audit verdict was `audited_conditional` because the previous packet mixed
the supported free-scalar continuum-covariance theorem with physical-readout
sentences that required unretained Planck-pin and light-cone authorities. The
repair takes the narrow route requested by audit:

```text
dependency_not_retained:
narrow the audited row to the free-scalar continuum covariance plus structural
K4 statement, or supply retained-grade Planck-pin and light-cone framing
authorities for the broader physical-readout sentences.
```

This revision binds only the supplied free-scalar Hamiltonian-lattice theorem:
continuum `SO(3,1)` covariance of the spacelike two-point function and the
finite-`a` structural `O(a^2 p^4)` cubic-harmonic `K_4` anisotropy. The
Planck-scale unit conversion, strict finite-`a` light-cone readout,
experimental sensitivity comparison, and physical framework-substrate
identification are explicit non-claims here.

## Audit-status note (2026-05-09)

The 2026-05-05 audit verdict (`audited_conditional`, chain_closes=false)
ratified the narrow free-scalar continuum-limit covariance core but
flagged that claims beyond that core invoke dim-6 LV inheritance,
CPT/P protection, and Planck-scale suppression from cited authorities
that were not yet independently closed. Specifically:

- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
  is `audited_conditional` (now narrowed to bounded conditional
  structural-dispersion support per the PR #803 salvage).
- the light-cone framing row is context only here. It is not a
  load-bearing authority for the narrowed free-scalar covariance theorem.
- [LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md](LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md)
  is `audited_conditional` (blocked on the same emergent-Lorentz cite).
- the Planck-scale lane status row is context only here. It is not a
  load-bearing authority for the narrowed free-scalar covariance theorem.

Audit boundary: only the free-scalar Hamiltonian-lattice continuum core and
the structural finite-`a` `K_4` anisotropy are binding in this row. Physical
unit conversion, strict finite-`a` causal-cone claims, and SME/experimental
readout language must be supplied by separate retained rows before they can be
used downstream.

## Theorem

**Theorem (3+1D SO(3,1) boost covariance, Phase 4).**
Let `W_lat(Δt, Δx⃗; a, m)` be the free-scalar Wightman 2-point function
on a 3+1D Hamiltonian lattice with spatial spacing `a` and bare mass `m`,

```text
W_lat(Δt, Δx⃗; a, m) = ∫_BZ d^3p/(2π)^3
                          * exp(-i E_lat(p) Δt + i p⃗·Δx⃗) / (2 E_lat(p)),
```

with the bosonic Laplacian dispersion

```text
E_lat^2(p) = m^2 + sum_i (4/a^2) sin^2(p_i a / 2).
```

Then in the continuum limit `a -> 0` with `(Δt, Δx⃗, m)` held fixed in
physical units,

```text
W_lat(Δt, Δx⃗; a, m)  ->  W_cont(s^2; m)
                          := m K_1(m sqrt(-s^2)) / (4π² sqrt(-s^2))
```

for spacelike separations `s^2 = Δt^2 - |Δx⃗|^2 < 0`. The continuum
limit `W_cont` depends on `(Δt, Δx⃗)` only through the SO(3,1) invariant
`s^2`, hence the path-sum 2-point function is fully SO(3,1) boost-
covariant in the continuum limit.

At finite `a > 0`, the leading boost-covariance violation is the structural
cubic-harmonic `K_4` correction computed below: `W_lat` is `O_h`-covariant but
not strictly SO(3,1)-covariant, with finite-`a` violation scaling as
`O(a^2 p^4)` in the supplied free-scalar model. This row does not convert
`a` into `M_Pl^-1` and does not make an experimental-sensitivity claim.

This is the 3+1D analogue of
[LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md](LORENTZ_BOOST_COVARIANCE_2D_THEOREM_NOTE.md)
and **strictly extends** the dispersion-isotropy theorem: where the
dispersion theorem closes the on-shell relation `E^2(p)`, this closes
the **off-shell 2-point function** itself.

## Why this matters

The dispersion-isotropy theorem
[EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
(37/37 PASS) shows the leading dispersion is `E^2 = p^2` plus a
structural `O(a^2 p^4)` cubic-harmonic correction. That is a statement
about the *on-shell relation* `E(p)`, not about the **two-point function**
`W(Δt, Δx⃗)`.

The Phase 4 theorem lifts the claim from on-shell to off-shell:

> The continuum-limit 2-point Wightman function on the supplied
> free-scalar `Z^3 x R` Hamiltonian-lattice model is
> exactly SO(3,1)-covariant, depends only on `s^2`, and has the closed
> form `m K_1(m sqrt(-s^2))/(4π² sqrt(-s^2))` for spacelike separations.

This converts the emergent-Lorentz program from "the dispersion is
isotropic at leading order with bounded LV corrections" into "the full
two-point correlator transforms as a Lorentz scalar in the continuum
limit". That is the relativistic-invariance statement Nature-class
referees expect to see.

## Proof structure

### Step 1 -- Microscopic spacetime symmetry is `O_h x Z`

The 3+1D `Z^3 x Z` lattice (Hamiltonian formulation: `Z^3` spatial,
continuous time evolution by the Laplacian) has microscopic spacetime
symmetry group

```text
G_micro = O_h (cubic point group, 48 elements) x R (time translations).
```

There is no microscopic boost. SO(3,1) is **non-compact** and cannot
live as a finite lattice automorphism. Boost covariance must emerge in
the continuum limit or not at all (cf. Bombelli-Henson-Sorkin 2009 for
the causal-set analogue with Poisson sprinkling).

### Step 2 -- Lattice dispersion is `O_h`-symmetric and parity-even

Direct verification (runner Part 1):

- `E_lat(p)` invariant under cubic permutations of `(p_x, p_y, p_z)`;
- `E_lat(p)` invariant under per-axis sign flips `p_i -> -p_i`;
- All 48 `O_h` group elements are exact symmetries.

No SME operator-classification or phenomenological protection theorem is
load-bearing in this narrowed row. The runner directly computes the
parity-even Taylor expansion and the first structural anisotropy
`sum_i p_i^4`, i.e. the `O(a^2 p^4)` cubic-harmonic correction.

### Step 3 -- Continuum dispersion is the unique relativistic limit

Taylor-expanding `(4/a^2) sin^2(p_i a / 2)` for `p_i a << 1`:

```text
(4/a^2) sin^2(p_i a / 2) = p_i^2 - (a^2/12) p_i^4 + O(a^4 p_i^6).
```

Summing over `i = 1, 2, 3`:

```text
E_lat^2(p) = m^2 + |p⃗|^2 - (a^2/12) sum_i p_i^4 + O(a^4 p^6).
```

The leading correction `sum_i p_i^4` is the cubic harmonic at `l = 4`
(see EMERGENT_LORENTZ_INVARIANCE_NOTE Step 4 for the
`Σn_i⁴ = 3/5 + (4√π/15) K_4` decomposition with `K_4 = Y_{40} +
sqrt(5/14)(Y_{4,4} + Y_{4,-4})`, in the standard normalized
spherical-harmonic basis `Y_lm` -- the `scipy.special.sph_harm` /
`sympy.Ynm` convention, under which the `m = ±4` combination
`Y_{4,4} + Y_{4,-4}` is real-valued and `K_4` is the real cubic harmonic).

**Convention note (normalization correction, 2026-05-29).** With
*normalized* `Y_lm` the coefficient on `K_4` is `4√π/15 ≈ 0.4727`, NOT
`4/5`. An earlier revision wrote `4/5`; that value holds only for an
unnormalized angular convention and is inconsistent with the normalized
`K_4` above and with the sibling decomposition in
EMERGENT_LORENTZ_INVARIANCE_NOTE Step 4. With `f = Σn_i⁴`, sympy gives the
isotropic projection `<f|Y_{00}> Y_{00} = 3/5`, the norm
`<K_4|K_4> = 12/7`, and the exact projection
`<f|K_4>/<K_4|K_4> = 4√π/15`, with
`trigsimp(f - [3/5 + (4√π/15) K_4]) = 0` identically; a numeric check over
5×10⁴ directions gives `max|LHS - RHS| = 7.8×10⁻¹⁶` for `4√π/15` versus
`2.8×10⁻¹` for `4/5` (runner Part 6, checks 6.6-6.7). The correction sets
only the magnitude of the `l = 4` anisotropy operator: the isotropic
average `3/5`, the factor-of-3 axis/diagonal anisotropy, the
parity-even/no-odd-power structure, the dim-6 classification, and the
continuum boost-covariance conclusion are all unchanged.

In the strict continuum limit `a -> 0`, `E_lat^2 -> m^2 + |p⃗|^2`, the
unique `SO(3) x R`-invariant relativistic dispersion. The convergence is
`O(a^2)` (verified numerically: at `p = 0.5`, `m = 1`, `a = 0.01`, the
relative error matches the predicted `(a^2 p^4)/(12 E^2) = 4.17e-7` to
two significant figures).

Verified runner check 1.4: at `a = 0.5`, `p = 0.5`,
`E^2([100]) - E^2([111]) = -8.66e-4` matches the predicted
`-(a^2 p^4)/18 = -8.68e-4` to 0.3% (the cubic-anisotropy split between
axis and diagonal directions).

### Step 4 -- 3+1D Lorentz-invariant on-shell measure

Under SO(3,1) boost along an arbitrary unit vector `n̂` with rapidity `η`,

```text
(E', p⃗') = (cosh(η) E + sinh(η) (n̂·p⃗),
            sinh(η) E n̂ + p⃗ + (cosh(η) - 1)(n̂·p⃗) n̂),
```

the on-shell measure `d^3p / (2 E_p)` is invariant
(Liouville-invariant measure on the mass-shell hyperboloid). The
runner verifies (Part 2):

- mass-shell preserved `E'^2 - |p⃗'|^2 = m^2 = E^2 - |p⃗|^2` to machine
  precision under boosts along `[1,0,0]`, `[1,1,0]`, `[1,1,1]` (cubic
  diagonal), and arbitrary `[1, 0.5, 0.3]`;
- boost composition `B(η_1) B(η_2) = B(η_1 + η_2)` along the same axis
  (the non-Abelian structure for boosts along different axes appears as
  a Wigner rotation, also automatic);
- reverse boost `B(-η) B(η) = identity`.

### Step 5 -- Continuum 2-point function depends only on `s^2`

Substituting `(E, p⃗) -> (E', p⃗')` in the continuum integral

```text
W_cont(Δt, Δx⃗; m) = ∫ d^3p/(2π)^3 * exp(-i E(p) Δt + i p⃗·Δx⃗) / (2 E(p))
```

and using the invariant measure, the integral transforms covariantly to

```text
W_cont(Δt', Δx⃗'; m) = ∫ d^3p'/(2π)^3 * exp(-i E'(p') Δt' + i p⃗'·Δx⃗')
                          / (2 E'(p'))
```

with `(Δt', Δx⃗')` the SO(3,1) boost of `(Δt, Δx⃗)` by `-η n̂`. Therefore
`W_cont(Δt, Δx⃗) = W_cont(Δt', Δx⃗')`.

The closed form (standard 3+1D massive scalar Wightman function for
spacelike separation) is

```text
W_cont(Δt, Δx⃗; m) = m K_1(m sqrt(-s^2)) / (4π² sqrt(-s^2)),
                                          s^2 = Δt^2 - |Δx⃗|^2 < 0,
```

with `K_1` the modified Bessel function of the second kind. Manifestly
SO(3,1)-covariant.

The runner verifies (Part 3) this analytic form to relative error
`3.2e-9` against radial oscillatory quadrature across 5 spacelike radii.

### Step 6 -- Lattice -> continuum convergence (Euclidean Schwinger function)

Direct numerical verification of `W_lat -> W_cont` in Lorentzian signature
is hampered by Minkowski oscillation (the integrand `exp(-i E_lat Δt)`
oscillates rapidly over the BZ for `Δt > 0`). The standard lattice-QFT
workaround is the Euclidean Schwinger function

```text
G_E(τ, Δx⃗; m) = ∫_BZ d^3p/(2π)^3 * exp(-E_lat(p) τ + i p⃗·Δx⃗) / (2 E_lat(p)),
```

with continuum limit

```text
G_E_cont(τ, Δx⃗; m) = m K_1(m R)/(4π² R),    R = sqrt(τ^2 + |Δx⃗|^2),
```

which is SO(4)-rotation invariant. Lorentzian boost covariance of `W`
is equivalent to SO(4) Euclidean rotation invariance of `G_E` via Wick
rotation `t -> -i τ`, and `G_E` is well-conditioned numerically.

Runner Part 4 verifies:

| `a` | `|G_E_lat - G_E_cont|/G_E_cont` at `(τ, dx⃗) = (2, (1,0,0))` |
|-----|-------------------------------------------------------------|
| 0.4 | 2.40e-2                                                     |
| 0.2 | 5.39e-3                                                     |
| 0.1 | 1.34e-3                                                     |

Convergence is monotone, ratio per halving consistent with `O(a^2)`.

The SO(4) Euclidean rotation invariance is verified directly:
`G_E_lat(τ=2, dx=(1,0,0))` and `G_E_lat(τ=1, dx=(2,0,0))` (both at
Euclidean radius `R = sqrt(5)`) agree to relative spread `4.1e-3` at
`a = 0.2`, fully consistent with `O(a^2)` continuum convergence.

The Lorentzian `W_lat(Δt = 0, ·)` is also tested directly (no Minkowski
oscillation in the spacelike `Δt = 0` slice) and converges with the
same `O(a^2)` rate.

### Step 7 -- Cubic-harmonic `K_4` structure at finite `a`

At finite `a > 0`, the lattice 2-point function is *not* strictly
SO(3,1)-covariant: the lattice dispersion induces a structural
`O(a^2 p^4)` cubic-harmonic correction. Direct verification (runner Part 6,
Euclidean):

| `a` | `|G_E([100]) - G_E([111])|` at `r = 1.5`, `τ = 1` |
|-----|---------------------------------------------------|
| 0.4 | 1.35e-4                                           |
| 0.3 | 1.18e-4                                           |
| 0.2 | 4.87e-5                                           |

The anisotropy decreases under `a`-refinement, with the smallest-`a`
relative anisotropy `1.9%` of the continuum value. The angular pattern
follows the cubic harmonic `K_4` with the factor-of-3 anisotropy
between axis `[1,0,0]` and diagonal `[1,1,1]/sqrt(3)` directions
(`f_4 = sum_i n_i^4 = 1` along axis, `1/3` along diagonal -- exact
ratio 3, verified to machine precision).

This is the same structural `K_4` signature used by the dispersion row, now
computed directly at the 2-point function level.

### Step 8 -- Combined SO(3,1) statement

Steps 1-7 together prove the Phase 4 theorem:

> Octahedral cubic symmetry plus continuous time translation, combined
> with the relativistic continuum dispersion `E^2 = m^2 + |p⃗|^2`
> (recovered as the unique `a -> 0` limit), imply that the continuum-limit
> path-sum 2-point function is fully SO(3,1) boost-covariant, depending
> only on the invariant interval `s^2`, with closed form
> `m K_1(m sqrt(-s^2))/(4π² sqrt(-s^2))` for spacelike separations and
> finite-`a` structural `O(a^2 p^4)` correction with cubic-harmonic `K_4`
> angular structure.

## What is and is not claimed

### What is claimed

- **Continuum limit, free scalar.** The free-scalar 2-point function on
  the 3+1D Hamiltonian lattice (`Z^3` spatial, continuous time)
  converges in the continuum limit to the standard SO(3,1)-covariant
  Wightman function.
- **Spacelike form.** For `s^2 < 0` the limit is exactly
  `m K_1(m sqrt(-s^2)) / (4π² sqrt(-s^2))`.
- **Mechanism.** The covariance follows from
  (a) `O_h`-symmetry and parity-evenness of the lattice dispersion,
  (b) `O(a^2)` convergence of the lattice dispersion to the relativistic
      dispersion,
  (c) SO(3,1) invariance of the on-shell Liouville measure `d^3p/(2 E_p)`,
  (d) standard Källén-Lehmann reduction in the continuum.
- **Finite-`a` structural correction.** The runner directly verifies the
  `O(a^2 p^4)` cubic-harmonic `K_4` angular structure and factor-of-3
  anisotropy between `[100]` and `[111]/sqrt(3)`.
- **Decoupling from angular kernel.** Phase 4 lives entirely on the
  staggered/Laplacian Hamiltonian construction, which has no angular-
  kernel parameter. The directional-measure walk
  (`ANGULAR_KERNEL_UNDERDETERMINATION_NO_GO_NOTE.md`)
  does not enter.

### What is NOT claimed

- **Finite-`a` boost covariance.** The lattice 2-point function at any
  finite `a > 0` is NOT strictly SO(3,1)-covariant: it has explicit
  cubic-harmonic anisotropy at `O(a^2 p^4)`. Only the strict continuum limit
  is fully covariant.
- **Interacting theory.** The proof is for the free scalar; interactions
  may introduce loop-level lattice corrections that need separate
  treatment (standard lattice-QFT renormalisation).
- **Timelike Wightman form.** The runner verifies the spacelike Macdonald
  form. The timelike `s^2 > 0` form requires the standard `iε`
  prescription and gives Hankel functions, related to the spacelike
  result by analytic continuation.
- **Strict v=1 light cone at finite `a`.** This row does not prove a strict
  finite-`a` causal cone or use a light-cone framing authority. It proves only
  continuum covariance of the supplied free-scalar two-point function.
- **Planck pin or experimental readout.** This row does not promote any
  Planck-scale unit map, does not identify `a^-1` with `M_Pl`, and does not
  compare finite-`a` corrections with experimental sensitivity.
- **Framework substrate identification.** This row does not identify the
  supplied free-scalar Hamiltonian-lattice model with the full physical
  framework substrate.

## Relation to existing notes

| Note                                      | Dimension | Covariance level             | This note's relation        |
|-------------------------------------------|-----------|------------------------------|-----------------------------|
| `EMERGENT_LORENTZ_INVARIANCE_NOTE`        | 3+1D      | dispersion isotropy          | strict extension            |
| `LORENTZ_BOOST_COVARIANCE_2D_THEOREM`     | 1+1D      | full SO(1,1) on 2-pt         | 3+1D analogue               |
| `ANGULAR_KERNEL_UNDERDETERMINATION_NO_GO` | -         | Phase 3 decoupling           | applies (kernel irrelevant) |
| Lorentz-violation companion row           | 3+1D      | bounded finite-`a` companion | context only                |
| light-cone framing row                    | -         | Lieb-Robinson framing        | context only                |
| lattice nearest-neighbor light-cone row   | -         | retired topological row      | context only                |

This note **strictly extends** the dispersion theorem: every PASS check
in `frontier_emergent_lorentz_invariance.py` remains valid; this note
adds the off-shell 2-point function statement. It does NOT supersede
any retained note.

## Relation to the literature

- **Bombelli-Lee-Meyer-Sorkin 1987 / Bombelli-Henson-Sorkin 2009**
  (causal sets): SO(3,1) Lorentz invariance achieved at the lattice
  scale by Poisson sprinkling. Phase 4 instead proves the standard
  lattice-QFT continuum-limit version: full SO(3,1) on a regular `Z^3`
  lattice in the continuum limit, with explicit structural `K_4` anisotropy
  at finite `a`.
- **Wiese; Rothe; Montvay-Münster** (lattice QFT references): the
  underlying lattice-QFT continuum-limit machinery is standard. This
  note is the rigorous statement of "continuum-limit Lorentz invariance"
  for the framework's path-sum 2-point function, with explicit closed
  form `m K_1/(4π²r)` and explicit characterisation of the leading
  finite-`a` LV correction.
- The combined statement is exact SO(3,1) covariance of the continuum
  two-point function on the supplied free-scalar Hamiltonian-lattice model.
  A separate retained bridge is still required before this can be used as a
  physical framework-substrate claim.

## What this changes in the program

This theorem upgrades the supplied free-scalar "Lorentz from discrete" claim
from

> "the leading on-shell dispersion is isotropic, and the first LV
> correction is structurally `O(a^2 p^4)`" (dispersion-level, on-shell)

to

> "the continuum-limit 2-point function transforms as a Lorentz scalar
> under the full SO(3,1) group, with closed form
> `m K_1(m sqrt(-s^2))/(4π² sqrt(-s^2))` for spacelike separations and
> structural cubic-harmonic K_4 anisotropy at finite `a`" (correlator-level,
> off-shell)

The 1+1D and 3+1D statements provide bounded support for the
boost-covariance Phase 2/4 program. They do not by themselves close the
physical emergent-Lorentz lane.

## Verification

```bash
python3 scripts/frontier_lorentz_boost_3plus1d.py
# PASS=57  FAIL=0
# Exit code: 0
```

The 57 checks span 8 parts:

| Part | Coverage                                                            | PASS |
|------|---------------------------------------------------------------------|------|
| 1    | 3D lattice dispersion structure and continuum limit (incl. cubic split) | 5  |
| 2    | SO(3,1) on-shell measure (3 axes + composition + reverse)          | 6    |
| 3    | Continuum 2-point function (analytic K_1 form, cluster, asymptotic) | 7   |
| 4    | Lattice -> continuum convergence (Euclidean + spacelike Lorentzian) | 4   |
| 5    | SO(3,1) boost covariance: 5 rapidities along [100] + [110] + [111] + arbitrary + composition | 13 |
| 6    | Cubic-harmonic `K_4` structure at finite `a` plus normalized identity | 7   |
| 7    | Combined SO(3,1) theorem statement                                 | 10   |
| 8    | Connection to existing dispersion theorem (strict extension)       | 5    |

Total: 57/57 PASS.

## Commands run

```bash
git checkout -b lorentz-boost-covariance 59f7e4f0  # main head
python3 scripts/frontier_lorentz_boost_3plus1d.py
# Exit code: 0  PASS=57  FAIL=0
```
