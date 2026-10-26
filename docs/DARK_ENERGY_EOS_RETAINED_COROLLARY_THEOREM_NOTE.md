# Dark-Energy EOS Conditional Structural Corollary

**Type:** bounded_theorem
**Status:** conditional on supplied comparison-radius and vacuum premises.
**Script:** `scripts/frontier_dark_energy_eos_retained_corollary.py`

The former inherited-closure and standalone-retained promotion claims are withdrawn.
The corrected parent `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`
distinguishes curvature `ell` from `a_sc(t) = ell cosh(t/ell)`.
The physical slice gap is `Lambda sech^2(t/ell)`, equal to Lambda only at
its minimum slice. This note supplies `R = ell`; it does not derive it.

## Theorem

Let the supplied surface carry:

1. supplied `S^3` spatial topology on the accepted `PL S^3 x R` carrier
   (authority:
   [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md),
   [`S3_GENERAL_R_DERIVATION_NOTE.md`](S3_GENERAL_R_DERIVATION_NOTE.md));
2. the supplied comparison identification `Lambda_vac = lambda_1(S^3_R) = 3/R^2`,
   with `R = ell` the fixed de Sitter curvature radius. The sphere is auxiliary,
   or the minimum spatial slice, not a general evolving physical slice.
   The corrected spectral-gap parent does not independently close this identification;
3. the stationary vacuum condition on the supplied smooth global
   gravitational stationary/Gaussian solution class, which by definition
   has `d R / d t = 0` for the de Sitter curvature scale `R = R_Lambda`
   (authority:
   [`UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md`](UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md),
   [`UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md`](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md)).

In what follows we write `a_sc(t)` for the FRW scale factor and `l_P` for the
fundamental lattice spacing, to keep those separate from the S^3 radius `R`.

**Theorem.** Under conditions (1)–(3), the dark-energy density is exactly
time-independent,

  `rho_Lambda(t) = (c^4 / (8 pi G)) * Lambda = (3 c^4) / (8 pi G R^2) = const`,

and therefore the dark-energy equation of state is

  `w = -1   exactly`,

with CPL parameters `w_0 = -1`, `w_a = 0`. The supplied lattice-discretization
correction is a constant shift `|delta Lambda / Lambda| = (1/4)(l_P / R)^2`
(authority:
[`DARK_ENERGY_EOS_NOTE.md`](DARK_ENERGY_EOS_NOTE.md), Part 2), hence carries
no additional time dependence and does **not** shift `w`.

**Proof.** Conditions (1)–(2) give `Lambda_vac = 3 / R^2` as a supplied
identity. Condition (3) gives `d R / d t = 0`, so `d Lambda_vac / d t = 0`
and `d rho_Lambda / d t = 0`. The
continuity equation for any cosmological fluid on the supplied smooth FRW
target is

  `d rho / d t + 3 H (1 + w) rho = 0`,

which for `rho = rho_Lambda > 0` and `d rho_Lambda / d t = 0` for `H != 0` forces
`(1 + w) = 0`, i.e. `w = -1`. Equivalently,
`w = -1 - (1/3) d ln rho / d ln a_sc` and
`d ln rho_Lambda / d ln a_sc = 0`. The supplied lattice correction enters as
`Lambda_eff = (3 / R^2) * (1 - (1/4)(l_P / R)^2)`, which is
`a_sc(t)`-independent when `l_P` and `R` are both fixed constants, so
`d rho_Lambda / d t = 0` is preserved. □


## Scope and diagnostic limits

All conclusions above are conditional on the supplied constant vacuum density and
FRW conservation, with nonzero H on the interval (and continuity at isolated zeros).
No inherited framework closure, numerical Lambda selection, or publication upgrade
is established. CPL `(w_0, w_a) = (-1, 0)` and absence of phantom crossing describe this supplied
constant-density model, not an unconditional observational prediction.

For fixed lattice spacing and comparison radius the supplied lattice correction
is constant and gives zero drift. The old diagnostic `(l_P/R)^2` is only an amplitude
scale. A varying correction requires a bound on its logarithmic derivative before
it bounds delta w: `delta w = -(1/3) d ln(1+delta)/d ln a_sc`.
For example delta = epsilon sin(N ln a_sc) has amplitude epsilon but derivative
amplitude epsilon N. No such derivative bound is derived here.

The complete prior note, including publication-row proposals and observational
claims, is preserved in the author recovery package and original Git history;
those inherited-closure claims are withdrawn, not silently promoted.
