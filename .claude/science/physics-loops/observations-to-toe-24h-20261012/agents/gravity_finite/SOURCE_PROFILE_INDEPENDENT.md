# Independent source-profile derivation, before root-proof inspection

This first section records reasoning from the neutral brief before
reading `SOURCE_PROFILE_TOMOGRAPHY.md`, `source_profile_probe.py`, or
the composition agent's rank lemma. It concerns exact mathematical
identifiability with a known positive mass measure, not observational
recovery or an adopted physical source model.

Let `p_C(da)` and `p_M(da)` be normalized positive radial source measures.
Assume the core radii do not exceed the mantle radii: `a_C <= a_M` for
every pair in their supports, with `a_C < a_M` on a set of positive
product measure. The latter excludes both measures being the same thin
shell at the shared boundary. Let the observation radii exceed every
source radius. Define

\[
 F_j(\mu)=\int \frac{\sinh(\mu a)}{\mu a}\,p_j(da),\qquad
 h_r(\mu)=(1+\mu r)e^{-\mu r},\qquad
 K_j(r)=\int F_j(\mu)h_r(\mu)\nu(d\mu).
\]

The removable values at `mu a=0` are one. Angular averaging of the
Yukawa potential of a spherical shell outside that shell gives
`exp(-mu r) sinh(mu a)/(mu a r)`, so differentiation of `1/r` times
that potential gives exactly `h_r/r^2`, with no missing source factor.

For `mu>0`, the logarithmic derivative of the shell factor is

\[
 m(a,\mu)=a\coth(\mu a)-\frac1\mu.
\]

It is strictly increasing in `a>0`, because
`partial_a m=coth(z)-z csch(z)^2>0` for `z>0`; the value at `a=0`
is zero. The logarithmic derivatives `F'_j/F_j` are averages of `m`
under positive tilted radial measures. Ordered source supports and
strict radial separation therefore imply
`partial_mu log(F_M/F_C)>0`. Consequently `q(mu)=F_C/F_M` is strictly
decreasing for positive mass, and is also strictly smaller than its
value one at mass zero.

Normalize `nu(dmu) F_M(mu) h_r(mu)` to a probability measure `w_r`.
Then

\[
 R(r):=\frac{K_C(r)}{K_M(r)}=E_{w_r}q,
 \quad
 R'(r)=\operatorname{Cov}_{w_r}
 \left(q(\mu),-\frac{r\mu^2}{1+r\mu}\right).
\]

Both covariance arguments are strictly decreasing in mass. Thus
`R'(r)>0` if the positive spectral measure has at least two distinct
support masses, including a possible atom at zero, and the kernel
integrals and derivatives exist. A finite nonzero positive measure and
strict exterior radius suffice: the exponential separation from the
source support controls large mass. A known positive common probe
form factor can be absorbed in `nu` without changing the argument.
Signed spectral weights, sign-changing internal profile shapes, or
unknown probe profiles are outside this proof.

At two distinct exterior radii `r1<r2`, the two-by-two kernel matrix
with rows `(K_C(r_i),K_M(r_i))` has determinant

\[
 \det M=K_M(r_1)K_M(r_2)[R(r_1)-R(r_2)]<0.
\]

This proves exact nonsingularity. For a single mass, both kernels are
constant source form factors times the same function `h_r(mu)`, so
the determinant vanishes exactly. A delta measure at mass zero is
also degenerate. Equality of the two radial source measures, coincident
observation radii, or a zero overall probe coupling are other controls.

## Conditioning and the long-range limit

Nonsingularity does not give a practically usable inverse. To see the
leading loss of conditioning, suppose a normalized mass measure is
scaled to small mass and has the needed moments. Write
`b_j=<a^2>_j/6`, `Delta b=b_M-b_C>0`. Then

\[
 q(\mu)=1-\Delta b\,\mu^2+O(\mu^4),\qquad
 \partial_r\log h_r=-r\mu^2+O(\mu^3),
\]

so

\[
 R'(r)=r\,\Delta b\,\operatorname{Var}_\nu(\mu^2)
 +\hbox{higher orders}.
\]

For fixed exterior radii,

\[
 |\det M|\sim
 \frac{(\langle a^2\rangle_M-\langle a^2\rangle_C)
 (r_2^2-r_1^2)}{12}\operatorname{Var}_\nu(\mu^2).
\]

For the normalized gamma measure, the variance is

\[
 \operatorname{Var}(\mu^2)=
 \frac{2s(s+1)(2s+3)}{\ell^4}.
\]

For the unscaled kernel matrix (each entry tends to one), its largest
singular value tends to two. Hence

\[
 \kappa_2(M)\sim
 \frac{24\ell^4}
 {s(s+1)(2s+3)
 (\langle a^2\rangle_M-\langle a^2\rangle_C)(r_2^2-r_1^2)}.
\]

A physical force matrix additionally has row factors `1/r_i^2` and
may have column source-mass factors. Its numerical condition number
depends on those units and scalings. Noise whitening and parameter
normalization must be specified before calling any condition number
an experimental precision requirement.

The measurement gives an overall known-probe-charge multiple of the
two source amplitudes. If probe charge is unknown, there is an exact
source/probe rescaling degeneracy; only products can be recovered.
Vanishing differential-acceleration/EP contrast does not by itself
fix a common probe charge or imply absence of the new force. Ordinary
background forces, source masses/profile uncertainties, and unknown
couplings must also be included in an actual inference.

## Inspection and numerical comparison

The initial reasoning above was frozen before reading the root proof,
root implementation, or composition lemma. Its hash was
`11ea6c6ab04035ec6edb86bf02b0e367e605d453242747fb3da23a5e69f4a483`;
the timestamp and no-prior-inspection declaration are in runtime
`source_profile_initial_reasoning.json`.

The inspected root proof agrees with the strict covariance argument,
its two-radius inverse, and the stated source/probe limitations. Its
gamma shell kernel and positive uniform-ball series have the correct
finite-source normalization. The geometric remainder bound is valid:
both positive rational coefficient factors decrease with series order.
The supplied benchmark at `r=R` is a surface limit and is safe for the
exponentially decaying gamma measure. For a general finite positive
measure, differentiability at an exact source boundary requires a
separate domination argument; the general proof uses strictly exterior
`r>R`.

An independently implemented force kernel starts from the uniform-ball
mass form factor

\[
 F_{\rm ball}(\mu;R)={}_0F_1\left(;5/2;\mu^2R^2/4\right).
\]

For `s=1`, let `beta=1+r/ell` and `z=(R/(ell+r))^2`. Direct integration
over mass, term by term in the positive `0F1` series, gives

\[
 K_{\rm ball}(r;R)=\frac1\beta
 {}_2F_1(1/2,1;5/2;z)
 +\frac{r/\ell}{\beta^2}{}_2F_1(1,3/2;5/2;z).
\]

This implementation does not import the root's shell or series
functions. Three direct integrals over mediator mass, including one
at the outer source surface, agree with this hypergeometric formula
to better than `1.4e-76` absolute at 75-digit working precision.
The comparison uses independently computed singular values at
110-digit precision, rather than the root's determinant formula for
the condition number.

All 52 compared kernel, ratio, determinant, and condition-number
values agree with the frozen root run. The largest relative difference
is `4.92e-56`. The first pair, `r1=R`, `r2=R+710000 m`, gives:

| `ell`, m | `kappa_2` of the mass-fraction-weighted matrix |
|---:|---:|
| 1e7 | 1701.37962122 |
| 1e9 | 1.65927090344e10 |
| 1e11 | 1.60099423178e18 |
| 1e13 | 1.60041816658e26 |

The geometry is the supplied diagnostic model: `R=6371000 m`,
`R_C=.55R`, `f_C=.32`, `f_M=.68`. For the weighted matrix with rows
`(f_C K_C,f_M K_M)`, the asymptotic expression corresponding to the
unweighted formula above is

\[
 \kappa_2(M)\sim
 \frac{12(f_C^2+f_M^2)\ell^4}
 {f_Cf_Ms(s+1)(2s+3)
 (\langle a^2\rangle_M-\langle a^2\rangle_C)(r_2^2-r_1^2)}.
\]

The exact/asymptotic ratio at the four listed ranges is respectively
`10.6309`, `1.03678`, `1.000364`, and `1.00000364`. The first range
is not yet in the small-mass asymptotic regime; no approximation was
used for its tabulated condition number. A separate positive two-pole
calculation agrees with the covariance derivative, and the single-pole
determinant control vanishes to the declared precision.

The composition lemma's determinant identity and `ell^-4` height
difference follow from the same argument. Its notation should state
whether `C(mu),M(mu)` include the core/mantle mass fractions. The
physical effective core fraction and its final `f_C f_M` coefficient
use `C=f_C F_C` and `M=f_M F_M` when `F_i` are individually normalized
form factors. Interpreting `C,M` instead as two unweighted, individually
normalized form factors would correspond to equal component weights.
This is a normalization clarification, not a failure of the rank
argument. The scalar source rows also require the displayed material
charge vectors and solar row to be independent; distinct geometric
rows alone do not establish that separate charge-space condition.

These checks support the conditional mathematical result. They do not
establish usable observational charge recovery at the enormous listed
condition numbers, nor do they replace a source/probe/measurement
nuisance model.

Artifacts in `agents/gravity_finite/` are this note and
`source_profile_check.py`. Runtime artifacts, all under
`gravity_measurements/finite/`, are `source_profile_results.json`,
`source_profile_comparison_receipt.json`, the initial-reasoning receipt,
and exact snapshots of the compared root/composition files. The checked
root code SHA256 is
`a236621cb350e9b59dea510e31efbc956752ec9eadb8ffa31b068e4ca37e2e73`.
