<!-- Original PR9808 source SHA256 63a08f35e28b4394704c62cffad25c1941d1a16afa01fcb6eeb1d3e4625b6258. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Physical two-column readout of the native neutral pole

Status: conditional-support. Trace: upstream_support to the requested native scalar coupling. No retained proposal or observational identification.

## Setup and dependencies

Use the same periodic R by R by L one-qubit compass Hamiltonian
H=-J sum(ZZ_z+lambda XX_x+lambda YY_y), fixed L=10, even R>=6, J>0,
and weak positive lambda. No term is added. The native action, anisotropy,
geometry, scale and choice of observable remain explicit premises.
[Reflection ground theorem](REFLECTION_GROUND_SECTOR_PROOF.md) supplies an
actual global ground in the all-positive plane sector. The Q4 endpoint pole
and matched local reductions are from
[TEN_LAYER_NEUTRAL_BOUND_PROOF.md](TEN_LAYER_NEUTRAL_BOUND_PROOF.md),
[POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md)
and the global Q-relative extension in
[ISOTROPIC_BOUND_FEATURE_PROOF.md](ISOTROPIC_BOUND_FEATURE_PROOF.md).
[CHARGED_COLUMN_POLE_PROOF.md](CHARGED_COLUMN_POLE_PROOF.md) establishes the
microscopic charged source D_r=product_z X_(r,z). This charge is a plane
symmetry character, not electromagnetic charge.

At zero total transverse momentum the neutral lower endpoint is
B0=(sqrt(2) R)^(-1) sum_r (|r,r+ex>+|r,r+ey>).
Its same-fibre orientation gap is order J lambda14. Its leading shape tails
are order lambda2 into longer thin rectangles. These have more than two
flipped columns. Its normalized endpoint coefficient first changes at
lambda4. The actual eigenvector and sources below are transformed together.

## A physical pair observable and normalization

For a grid momentum k with 2k not reciprocal zero define
O_k=[R^-2 sum_(r!=s) exp(ik.(r-s)) D_r D_s]/sqrt(1-2/R²).
The ordered sum is Hermitian because exchanging r,s conjugates its weight
and the two D commute. It is translation invariant and neutral under every
full plane. Subtract its exact ground expectation if a centered source is
wanted; the matrix element to an orthogonal excited eigenstate is unchanged.
Its norm is at most (R²-1)/sqrt(1-2/R²).

On the flat reference vacuum the unordered pair {r,s} has coefficient
2 cos(k.(r-s))/(R² sqrt(1-2/R²)). The squared norm is one: for N=R²,
sum_(d!=0) cos²(k.d)=N/2-1. Consequently

 <B0|O_k|0>=sqrt(2)/(R sqrt(1-2/R²)) [cos(kx)+cos(ky)].

This is a physical finite-volume spectral form factor, not a phenomenological
Yukawa coefficient. At k=0 the unit-normalized identical-pair source instead
uses sqrt(2(1-1/R²)) in the denominator of the R^-2 ordered sum; its B0
overlap is 2/(R sqrt(1-1/R²)). Do not apply generic-k unit normalization to
self-inverse momenta.

## Second-order source dressing from existing bonds

One transverse bond creates four broken z bonds with energy cost 8J.
Its first-order virtual amplitude has magnitude lambda/8. Conjugation by a
product of column X operators reverses exactly YY bonds crossing the selected
columns. XX and internal YY commute. In the matched initial/final normalized
wall-free overlap each reversed bond contributes -2(lambda/8)². No other
wall-free column pattern is reachable with two bond insertions at L=10.
Unreversed terms cancel against state normalization; this is the canonical
matched-source calculation, not a product of undressed state fidelities.

For an adjacent x pair there are 4L reversed YY bonds. For an adjacent y
pair there are 2L because the shared YY bonds are internal. Thus the respective
amplitudes are 1-Llambda²/8 and 1-Llambda²/16. The order-lambda² endpoint
shape tail has zero overlap with the leading two-column source. Vacuum winding
mixing begins at lambda6. The transverse checkerboard Z transformation sends
lambda to -lambda and commutes with each D for even L, so odd powers are absent.
The resulting actual matrix element, with a continuous real phase convention,
is

 F_k=sqrt(2)/(R sqrt(1-2/R²))
 [(1-Llambda²/8)cos(kx)+(1-Llambda²/16)cos(ky)]+O(lambda4/R).

The expansion is additive, including at form-factor zeros. The original
X-column readout is orientation dependent at second order even though the
leading neutral mode is C4 even. Do not claim that every probe is a scalar.
The spectral atom of O_k has weight |F_k|². For generic nonzero leading
form factor this is 2[cos(kx)+cos(ky)]²/[R²(1-2/R²)] times 1+O(lambda²).
The 1/R² weight is the normalization of a delocalized pair's overlap with a
localized relative bound feature, not disappearance of the local interaction.

## Uniformity on polynomial grids

Fix p>1 and R asymptotic lambda^-p through even integers. Every retained
coefficient of the local transformations of D_r remains charged and supported
in a fixed collar. A nonzero finite charged syndrome has at least four bad
plaquettes. Two disjoint dressed charged collars therefore have at least
eight and cannot overlap Q4. A connected finite-order contribution joining
two collars has bounded relative range. Endpoint tails at each retained order
are bounded-length paths from the compact endpoint, with bounded relative l1
norm. Summing translations and the R^-2 pair normalization preserves 1/R at
each order. Scalar ground pieces are centered or cancel in the excited-state
matrix element. No interacting-vacuum factorization is assumed.

Use a sufficiently high fixed local reduction order. With final absolute
Hamiltonian remainder C R² lambda^M and same-fibre gap c lambda14, the source
norm bound O(R²) gives absolute matrix-element error C R4 lambda^(M-14).
To make it smaller than lambda4/R choose M>18+5p, in addition to the inherited
energy/source reduction requirements. Joint source expansion can be retained
to this same sufficient order. For p=5, M=60 suffices; the crude tail lambda26
is smaller than the retained lambda9 remainder. This is a fixed-p joint limit,
not a fixed-coupling thermodynamic theorem. All constants may depend on p,
fixed L and reduction order. No infinite-order convergence is used.

## What is and is not derived

The same microscopic Hamiltonian supplies charged large features, a neutral
bound pole, and a nonzero physical two-feature source residue with no new
interaction coefficient. Both the leading form factor and its first correction
are fixed by the native model and readout. A finite-volume operator observable
is specified, not a free field or an external environment profile.
This does not establish pair-to-bound on-shell conversion, decay, scattering
cross section, a universal mass coupling, gravity, 3D Lorentz invariance,
fermionic statistics, or cosmological scalar identification. The source is a
product of two extended columns; an experiment measuring it has not been
constructed. All controls are exposed model-development calculations.
