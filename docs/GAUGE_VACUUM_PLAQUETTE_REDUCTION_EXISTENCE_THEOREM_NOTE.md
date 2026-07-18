# Finite-Volume Wilson Plaquette Inverse-Coordinate Theorem

**Date:** 2026-04-16
**Revised:** 2026-07-18
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only
**Scope:** finite periodic `SU(3)` Wilson `L^4` evaluation surfaces with
integer `L >= 2`; no physical interpretation of `beta` and no canonical
plaquette value
**Primary runner:**
[`scripts/frontier_gauge_vacuum_plaquette_reduction_existence_theorem.py`](../scripts/frontier_gauge_vacuum_plaquette_reduction_existence_theorem.py)

## Result

The substantive finite-volume theorem is an inverse-coordinate theorem.  The
one-plaquette response is a real-analytic strictly increasing bijection

`P_1plaq : [0, infinity) -> [0, 1)`.

The finite-volume Wilson response `P_L` is also real analytic and strictly
increasing, has values in `[0,1)` at finite nonnegative `beta`, and tends to
`1` as `beta -> infinity`.  Consequently the formula

`beta_eff,L(beta) := P_1plaq^(-1)(P_L(beta))`

defines a unique real-analytic strictly increasing coordinate.  Substitution
then gives

`P_L(beta) = P_1plaq(beta_eff,L(beta))`.

The last equality is true **by the displayed definition**.  It is not an
independently specified reduction law, a dynamical reduction mechanism, or a
physical replacement of the finite Wilson theory.

## Wilson finite-volume definitions

Let

`Lambda_L = (Z / L Z)^4`, with `L >= 2`,

and retain one positively oriented link in each of the four directions from
each site.  The configuration space and reference measure are

`Omega_L = SU(3)^(4 L^4)`,

`d mu_H(U) = product_(positive links ell) dH(U_ell)`,

where every `dH` is normalized Haar probability measure.  For a positively
oriented elementary plaquette `p = (x; mu,nu)`, `mu < nu`, write

`U_p = U_(x,mu) U_(x+mu,nu) U_(x+nu,mu)^dagger U_(x,nu)^dagger`.

There are

`N_plaq = binom(4,2) L^4 = 6 L^4`

such plaquettes.  Define the normalized local observable and the unnormalized
Wilson source sum by

`X(U) = (1/3) Re Tr U`,

`S_L(U) = sum_p X(U_p)`.

The one-plaquette and finite-volume partition functions are

`Z_1plaq(beta) = integral_SU(3) exp(beta X(U)) dH(U)`,

`Z_L(beta) = integral_(Omega_L) exp(beta S_L(U)) d mu_H(U)`.

The responses in this note use the derivative with respect to exactly this
source parameter `beta`:

`P_1plaq(beta) = d/d beta log Z_1plaq(beta)`,

`P_L(beta) = (1/N_plaq) d/d beta log Z_L(beta)`.

Thus `S_L` already contains `X = (1/3) Re Tr`; there is no additional factor
of `1/3` in the exponential, and the factor `1/N_plaq` occurs once in `P_L`.

## Theorem 1: analyticity and strict variance identities

The functions `X` and `S_L` are bounded on compact domains.  Expanding the
exponential and integrating term by term, uniformly on compact subsets of
complex `beta`, proves that both partition functions are entire.  They are
strictly positive on the real axis, so their logarithmic derivatives are
real analytic there.

Differentiation with respect to the source parameter defined above gives

`P_1plaq'(beta) = Var_beta(X)`,

`P_L'(beta) = (1/N_plaq) Var_beta(S_L)`.

Both variances are strictly positive at every finite real `beta`.

In particular, `Var_beta(X) > 0`.

`P_1plaq(beta)` is strictly increasing on `beta >= 0`.

For the local observable, `X(I) = 1`, whereas for the nontrivial center element
`z I`, `z = exp(2 pi i/3)`, one has `X(z I) = -1/2`.  The tilted density is
strictly positive, hence has the same support as Haar measure; the local
observable cannot have zero variance.

For the finite lattice, compare the identity link field with a field in which
only `U_(0,mu)` is replaced by

`V_theta = diag(exp(i theta), exp(-i theta), 1)`,

where `theta` is not a multiple of `2 pi`.  For `L >= 2`, exactly two
plaquettes in each direction `nu != mu` contain that link.  Their holonomies
are `V_theta` or `V_theta^dagger`; all other plaquettes remain the identity.
Therefore

`S_L(U_deformed) = N_plaq - 6 (1 - X(V_theta)) < N_plaq`.

At least six plaquette holonomies really change, so this deformation is not a
gauge-pure cancellation.  Continuity gives positive-Haar-measure
neighborhoods with different `S_L` values, and the strictly positive tilted
density then gives `Var_beta(S_L) > 0`.

It follows that both response functions are strictly increasing.

## Theorem 2: endpoints, range, and bijectivity

At `beta = 0`, character orthogonality gives

`P_1plaq(0) = integral X dH = 0`.

For `L >= 2`, the four positive link variables around any elementary
plaquette are distinct.  Their product is Haar distributed under the product
measure, so every plaquette has zero mean and

`P_L(0) = 0`.

Every `SU(3)` matrix obeys `X(U) <= 1`, with equality only at `U = I`.
The positive finite-`beta` density and the nonconstancy witnesses above imply

`0 <= P_1plaq(beta) < 1`,

`0 <= P_L(beta) < 1`

for every finite `beta >= 0`.

The endpoint at infinity follows from a compact Laplace lemma.  If `f` is
continuous on a compact probability space, has maximum `M`, and
`d mu_beta` is proportional to `exp(beta f) d mu` with full-support `mu`, then
`E_beta[f] -> M`.  Indeed, for any `epsilon > 0`, a positive-measure
neighborhood on which `f > M - epsilon/2` bounds the tilted mass of
`{f <= M-epsilon}` by a constant times `exp(-beta epsilon/2)`; boundedness of
`f` finishes the expectation estimate.

Apply the lemma first to `f = X`, whose maximum is `1`, and then to
`f = S_L`, whose maximum is `N_plaq` and is attained by the identity field.
This proves

`lim_(beta -> infinity) P_1plaq(beta) = 1`,

`lim_(beta -> infinity) P_L(beta) = 1`.

Strict increase, continuity, and the two endpoints prove—not merely
assume—that both maps are bijections from `[0,infinity)` onto `[0,1)`.

## Theorem 3: the defined inverse coordinate

Since `P_L(beta)` lies in the range of `P_1plaq`, define

`beta_eff,L(beta) := P_1plaq^(-1)(P_L(beta))`.

This coordinate exists and is unique for every finite `beta >= 0`.  Since
`P_1plaq'` never vanishes, the real-analytic inverse-function theorem applies
at every point of its range.  At the endpoint `beta = 0`, the same theorem
applies on an open real neighborhood because `P_1plaq` and `P_L` extend
analytically across zero.  Hence `beta_eff,L` is real analytic on its
finite-volume domain.

Differentiating the definition gives

`beta_eff,L'(beta)
 = P_L'(beta) / P_1plaq'(beta_eff,L(beta)) > 0`.

Thus the coordinate is strictly increasing.  The equality

`P_L(beta) = P_1plaq(beta_eff,L(beta))`

contains no further dynamical content: it is the coordinate identity obtained
by applying `P_1plaq` to the definition.

## Independently reconstructed zero-source slope

The linear onset is included because both slopes follow directly from the
same product-Haar definitions.

For one plaquette,

`X = (Tr U + Tr U^dagger)/6`.

Center invariance kills `integral (Tr U)^2 dH` and its conjugate, while
fundamental character orthogonality gives
`integral Tr U Tr U^dagger dH = 1`.  Therefore

`P_1plaq'(0) = integral X^2 dH = 1/18`.

For the finite lattice, expand `X_p X_q` into its four trace orientations.
Independent multiplication of any link by an `SU(3)` center element forces
zero expectation unless the oriented link charges cancel modulo three.  With
two elementary plaquette insertions the charges are in `{-2,-1,0,1,2}`, so
mod-three neutrality requires exact linkwise cancellation.  On the periodic
cellulation with `L >= 2`, distinct positive elementary plaquettes have
neither equal nor opposite oriented link boundaries.  Hence only `p = q`
with opposite trace orientations survives, and

`E_0[X_p X_q] = delta_(p,q) / 18`.

It follows that

`Var_0(S_L) = N_plaq / 18`,

`P_L'(0) = (1/N_plaq) Var_0(S_L) = 1/18`.

The inverse-coordinate derivative is consequently

`beta_eff,L(0) = 0`,

`beta_eff,L'(0) = P_L'(0) / P_1plaq'(0) = 1`.

No higher-order onset coefficient is part of this theorem.  In particular,
this row does not import a mixed-cumulant output and does not use such an
output as proof of the inverse-coordinate result.

## Exact boundary

This theorem establishes only finite-volume Wilson mathematics:

- compact-domain analyticity of the two partition functions and real
  analyticity of their responses;
- strict variance/nonconstancy and strict monotonicity;
- the proved `[0,1)` ranges and endpoint limits;
- existence, uniqueness, analyticity, and monotonicity of the defined inverse
  coordinate;
- `beta_eff,L(0) = 0` and the independently reconstructed
  `beta_eff,L'(0) = 1`.

It does not establish:

- an independently specified plaquette-reduction law or physical reduction
  mechanism;
- a thermodynamic-limit theorem;
- a physical identification of `beta`, including a framework-point value;
- an explicit nonperturbative value or closed form for `beta_eff,L`;
- a canonical plaquette value, a canonical inverse-coordinate value, or an
  old-candidate comparison;
- any plaquette closure, coupling extraction, or downstream physical
  prediction.

No staggered-Dirac gate, `g_bare` input, framework axiom, new admission,
primitive, carrier, or physical premise is used.  The theorem is a
zero-physical-input statement about the explicitly defined finite Wilson
probability spaces.

## Verification

```bash
python3 scripts/frontier_gauge_vacuum_plaquette_reduction_existence_theorem.py --mode normal
python3 scripts/frontier_gauge_vacuum_plaquette_reduction_existence_theorem.py --mode independent
python3 scripts/frontier_gauge_vacuum_plaquette_reduction_existence_theorem.py --mode hostile
```

The hostile mode rejects a wrong source normalization, omission of
`1/N_plaq`, reversed monotonicity, a constant-action witness, an invalid or
reversed inverse branch, and a wrong derivative factor.  It does not mutate
the coordinate identity, which is a definition rather than an independent
theorem.
