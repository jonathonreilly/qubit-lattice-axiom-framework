<!-- Original PR9785 source SHA256 aad4aea88d69f2d6742fd2eec1e523fdb43334573ca4ec441ddf0966ce323174. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Every fixed occupation: native neutral-feature ladder

Status: bounded-support. For each fixed integer `M`, the original one-qubit
Hamiltonian and original readout admit `M+1` orthonormal microscopic
energy-window vectors with additive centers and adjacent source ratios
`sqrt(m)`, `1<=m<=M`, in the previously specified joint weak-coupling limit.
This is not an invariant oscillator sector, a full canonical commutation
relation, a finite-density limit, or a particle/scalar identification.

## Fixed premises and statement

Use `TWO_FEATURE_LADDER_PROOF.md`, `LARGE_BOUND_FEATURE_PROOF.md` and
`LOW_ENERGY_SOURCE_BOUND.md`. Fix `0<alpha<2/3`, `delta=lambda^alpha`, an even
cube `L~lambda^-4`, the allowed even COM mesh near the native threshold
family, and **a fixed M independent of lambda and L**. Let the normalized
native bound feature be `chi=Bdag|0>`, with coefficient energy `E`, and
write its canonical all-lowering extension as `Bdag=BHdag+BRdag`. The host
has norm squared `w=1-eta²`, where `eta=O(sqrt(delta) log(1/delta))`. All
conditional ray-length moments are uniformly bounded.

Use the explicit M-dependent ray cutoff `ell<L/(16M)` and transverse cutoff
`L/4`. Their discarded tails are superpolynomial in this family. This
replaces the cutoff adequate for only two rungs; it is essential when
comparing ground-background images of up to M features.

For every actual ground vector `g_s`, there are normalized vectors `psi_m`,
with `psi_0=g_s`, in the disjoint exact spectral windows

\[
H-E_g\in mJ(8+\lambda E)+[-J\lambda\delta/4,J\lambda\delta/4],
\quad 1\le m\le M,
\]

such that, with `a=<chi,Fdag|0>>` the *derived original-readout* coefficient,

\[
|\langle\psi_m,C_Q\psi_{m-1}\rangle|
 =\sqrt m\,\lambda |a|[1+o(1)],\qquad
|a|\sim\sqrt{W_0\delta}\log(1/\delta).
\]

Errors may depend on M. Neither this theorem nor its proof allows M to grow.

## Exact pair algebra as a computational device

Write the host symmetric zero-diagonal pair matrix as `Phi`, with
`Tr(Phi†Phi)=w`. Its site marginals are `w/V`, and
`||Phi†Phi||=O(1/(V delta))`. Introduce formal canonical site bosons solely
to calculate a polynomial identity:

\[
B_b^\dagger=2^{-1/2}\sum_{ij}\Phi_{ij}a_i^\dagger a_j^\dagger.
\]

These are not additional physical degrees of freedom. The projection onto
occupations zero or one satisfies exactly
`P_hc (B_bdag)^m|0>=(BHdag)^m|0>` when the zero/one basis is identified with
physical spin configurations. A direct Takagi-mode expansion, or Gaussian
power-series calculation, gives

\[
\sum_{m\ge0}\frac{t^m}{(m!)^2}\|(B_b^\dagger)^m|0\rangle\|^2
 =\det(1-2t\rho)^{-1/2}
 =\exp\left[\sum_{k\ge1}\frac{2^{k-1}}{k}
                    \operatorname{Tr}(\rho^k)t^k\right],
\quad\rho=\Phi^\dagger\Phi. \tag{1}
\]

Only finite coefficients are used. Since `Tr rho=w` and
`Tr rho^k <= ||rho||^(k-2) Tr rho²` for `k>=2`, the m-th norm is
`m! w^m+O_m(Tr rho²)`.

The hard-core correction is `O_m(1/V)` in squared norm. To see this directly,
expand the coefficient of each boson configuration as a sum over pairings
of its `2m` labeled slots. The number of such pairings, as well as every
occupation factorial, is bounded by a constant depending only on m.
Cauchy-Schwarz bounds its squared coefficient by that constant times the
sum of products of squared pair coefficients. In the corresponding tensor
product of m pairs, each site marginal is uniform. The probability that a
site from one pair equals a site from another is `1/V`; a union bound over
finitely many pairs of slots gives the result. Within-pair repetitions are
absent because `Phi_ii=0`. Therefore

\[
\|(B_H^\dagger)^m|0\rangle\|^2
 =m!w^m+O_m(1/(V\delta)). \tag{2}
\]

For the source pair matrix `Xi` with bounded Hilbert-Schmidt norm, let
`a=Tr(Phi†Xi)`. Take the holomorphic derivative of (1) under
`Phi -> Phi+t Xi`, treating the bra coefficients as fixed, and divide the
m-th norm derivative by m. The leading result is

\[
\langle B_H^{\dagger m}0,F^\dagger B_H^{\dagger(m-1)}0\rangle
 =m!w^{m-1}a+O_m(\|\rho\|)+O_m(V^{-1}). \tag{3}
\]

Indeed, the derivative of the k-th trace is
`k Tr(rho^(k-1) Phi†Xi)`, bounded for `k>=2` by
`k ||rho||^(k-1)||Phi||HS||Xi||HS`. The hard-core mixed correction follows
by applying Cauchy-Schwarz to the two discarded collision vectors. The
source pair has uniform site marginal and bounded norm, so each discarded
squared norm is `O_m(1/V)`. Thus no fitted oscillator rule enters (3).

## Rays, contacts and the native Hamiltonian

For a union of m two-column interval strings of total length S, an ordered
decomposition into such strings has at most `C_m(1+S)^(2m)` possibilities:
choose their column pairs from at most `2m` columns and their interval
endpoints from at most `2S` occupied positions. Weighted Cauchy-Schwarz and
the uniform conditional ray moments then bound a term with j ray factors
by `C_m eta^j` in norm. A term containing any ray has more down spins than
the pure host term. Thus linear-ray cross terms vanish in both the norm
and (3). Consequently

\[
\|B^{\dagger m}0\|^2=m!+O_m(\eta^2+(V\delta)^{-1}),
\]

and the full mixed numerator is
`m! a+O_m(eta²+(V delta)^-1+V^-1/2)`.

Let `Phi_m=P_(4m) Bdag^m|0>`. Independent uniform COMs give contact probability
at most `C_m/V` after averaging the polynomial string lengths. The same
finite-decomposition bounds therefore give projection loss
`||Phi_m-Bdag^m|0>||=O_m(V^-1/2)`. Away from pairwise contact, every native
bond flip acts on one feature and the broken-bond filters act separately.
The difference between `K_(4m)` and the sum of m independent `K_4` actions
is contact-supported. Polynomial predecessor/output counts and the same
weighted bound imply, for normalized `chi_m`,

\[
\|(K_{4m}-mE)\chi_m\|=O_m(V^{-1/2}). \tag{4}
\]

For each fixed higher normal-form coefficient `D_j`, the vacuum-subtracted
local terms missing all down sets annihilate. The number of remaining terms
and predecessors is polynomial in total string length. Thus
`||(D_j-E_j,vac)chi_m||<=C_(j,m)`. The dressed original source's grade `+4`
agrees with its vacuum pair extension `Fdag` except near existing strings,
with vector error `O_m(V^-1/2)`; higher source terms give `O_m(lambda²)`.
Dividing the full mixed numerator by the two norms gives

\[
\langle\chi_m,C_{1,Q}\chi_{m-1}\rangle
 =\sqrt m\,a[1+o(1)]. \tag{5}
\]

Here `eta²/|a|`, `(V delta)^-1/|a|` and `V^-1/2/|a|` all vanish. The source
coupling is inherited from the original operator, not supplied separately.

## Ground backgrounds and actual spectral windows

Apply the existing plane-symmetry ground-orbit maps `T_m` to each `chi_m`.
The M-dependent cutoff ensures a union or difference of up to M strings
from each side, even after fixed-order local changes, cannot reverse an
entire column. Distinct ground-background images are therefore disjoint.
The neutral stabilizer characters and plane covariance make the maps
isometric and the adjacent source matrices scalar on the ground-background
space, exactly as for two rungs. No absolute translation eigenvalue is
assumed for a general ground vector.

With `g` the normalized projection of `U g_s` into the normal-form ground
space, define `Xi_m=U† T_m g`. The previously controlled global remainder
and ground projection errors remain negligible for each fixed M. Equations
(4) and the fixed-order local bounds give

\[
\|(H-E_g-mJ(8+\lambda E))\Xi_m\|\le C_M J\lambda^2.
\]

Projection to the stated exact window loses `O_M(lambda/delta)` in norm.
The whole-low-energy source lemma applies with any buffered fixed cutoff
larger than `8MJ`, and gives `||C_Q P_low||=O_M(lambda)` (also for its
adjoint). The same bound on trial vectors follows from their bounded N and
normal-form energy moments, not from using the global source norm on a
small leakage component. Hence projecting an adjacent matrix element
changes it by `O_M(lambda²/delta)`. Relative to `lambda |a|`, this is

\[
O_M\left(\frac{\lambda}{\delta^{3/2}\log(1/\delta)}\right)=o(1)
\]

for `alpha<2/3`. Normalizing projected vectors has a smaller relative cost.
Their windows are disjoint, so they are exactly orthogonal. This proves the
stated fixed-M ladder.

## Prepared finite-time evolution

The exact window projections commute with H, so their normalized vectors
also have residual at most `C_M J lambda²` about their stated centers.
Let `W_M|m>=psi_m`, let `n|m>=m|m>`, and set
`omega=J(8+lambda E)`. On this fixed finite space,
`||(H-Eg)W_M-W_M omega n||<=C_M J lambda²`; the column-to-operator bound
only changes the M-dependent constant. Duhamel therefore gives

\[
\|e^{-it(H-E_g)}W_M-W_M e^{-it\omega n}\|
 \le C_M J\lambda^2|t|.
\]

For `|t|<=S/(J lambda delta)` the error is `O_(M,S)(lambda/delta)` and tends
to zero. This is approximate harmonic evolution of prepared finite ladder
superpositions on a specified growing time window, not exact invariance
or a closed source-driven oscillator. It uses the same microscopic H.

## What has and has not emerged

The familiar adjacent square-root factors and additive energy centers have
been derived for every fixed finite occupation, using only physical spin
strings and the original Hamiltonian/readout. The formal boson calculation
was a way to evaluate their algebra, not an added interaction or site qubit.
The result does not identify the full source with one oscillator. Its
vacuum pair coefficient has order-one total norm, whereas the selected
mode overlap squared tends to zero as `delta log²(1/delta)`. Source response
outside the selected ladder is therefore not controlled by this theorem.
No nonadjacent operator identity, invariant ladder, full CCR, growing-M
limit, stable scattering particle or cosmological scalar is asserted.
The microscopic Hamiltonian, state/regime/momentum selection, units and
measurement bridge remain conditional. All checks are exposed model
calculations; no observations were fitted or independently tested.
