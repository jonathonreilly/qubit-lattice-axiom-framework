# Pre-control derivation: scalar Neumann pins on the actual nine fields

This is an author derivation before the new finite controls. It uses only
the original full-carrier H0>=a Egrad and the checked B_R bound. It does not
change the microscopic law, delete neighbors inside D(m), or create a gas
of independently normalized pairs. Constants C below are universal positive
constants, allowed to increase; all fixed cutoff profiles are selected once.

Let Lambda be an ell by ell by ell cube of forward bond anchors, and Delta_N
its free-path scalar Laplacian. Its kernel is constants and its first
positive eigenvalue is 4 sin^2(pi/(2ell))>=4/ell^2. Let G_N=Delta_N^+.
For x,y at distance at least w from every cube face,

    G_N(x,y)=G_Z3(x-y)+O(1/w),
    |G_Z3(r)|<=C/(1+|r|), G_Z3(0)=g.                    (A)

Proof of the uniform boundary error: on the period-2ell torus, cut the
infinite symbol 1/ell(k) smoothly below kappa=1/ell, with the cutoff already
one above 2/ell. Every nonzero torus momentum has size at least pi/ell, so
its sampled symbol is unchanged. A dyadic Fourier bound gives the cut
kernel C(1+|r|)^(-1)(1+|r|/ell)^(-4). Its absolutely convergent periodization
differs from the infinite Green function by O(1/ell), uniformly in a nearest
periodic representative. The removed ball contributes O(1/ell) as well.
The exact free-path reflection formula sums eight period-2ell kernels at
the images y_i or -y_i-1. The seven reflected images have periodic distance
at least 2w from x. This proves (A), including the mean-zero normalization.
The dyadic bound follows by integration by parts on shells: a shell radius
s contributes C_j s(1+s|r|)^(-j); summing s>=1/ell proves the displayed
cutoff estimate. No uncut 1/r kernel is periodized.

Choose m pin sites in the w-interior, separated by more than R in Chebyshev
distance, with ell>=R>=10 and 1<=w<ell/2. Their Green matrix Gamma obeys

    lambda_max(Gamma)<=B:=g+C ell^3/(R^3 w),
    m<=M:=8 ell^3/R^3.                                  (B)

Indeed disjoint translates of [0,R]^3 give the count. Shell packing gives
sum_(other pins)1/(1+distance)<=C ell^2/R^3. The image error in (A) sums to
C m/w; since w<=ell it dominates that shell term. Gershgorin then proves
(B). For no pins the later inequalities have zero right side.

For a nine-component amplitude f on Lambda, pinned to zero at each site,
write f=c+q with mean q=0. Scalar Green Cauchy for the sum of its pin
evaluations gives m||c||^2<=B E_N(f), where E_N is the sum of its nine
Neumann gradient energies. Also ||q||^2<=ell^2 E_N(f)/4. Consequently

    E_N(f)>=m||f||^2/[ell^3 (B+M/(4ell))].               (C)

This is a finite-dimensional exact inequality once B bounds the pin Green
matrix. No inverse conditioning or scalar-gas interpretation is needed.

Apply (C) separately to the actual amplitudes
f_(eta,d)(x)=<eta|b_x b_(x+d)psi>, d in the nine forward graph directions.
For each residual eta, select one endpoint of every R-isolated actual graph
dimer whose two endpoints lie in the w-interior of this anchor cell. These
are common hard-core pins for all nine components and obey (B). The original
fifteen bare gradients dominate the nine forward gradients, including their
within-cell Neumann differences. Sum (C) over eta and disjoint anchor cells;
no physical tensor-factor disjointness of the extended bond supports is
required, since the positive gradient rows are merely selected once.

Let g_j(S) count such R-isolated dimers of the ORIGINAL occupation S in
cell j. If one of those dimers is removed, every other remains R-isolated
in the residual and inside the same interior. That removed bond has one
unique forward anchor in the cell. Therefore the literal diagonal counting
identity/inequality is

    sum_eta m_eta,j ||f_eta,j||^2 >= <g_j(g_j-1)>.        (D)

All other removed edges add nonnegative terms. The norm at a single removed
edge has just one input occupation, so interference is not lost by (D).
No matching multiplicity divides this count.

Tile floor(L/ell)^3 complete cubes in the torus and average their common
translation. The fraction theta of sites outside their w-interiors obeys
theta<=3ell/L+6w/ell. Choose one translate for which the expected particle
number in that region is at most theta <N>. If G=sum_j g_j, every discarded
original isolated dimer has at least one endpoint in that region. Hence

    <G> >= [<N>-<B_R>]/2-theta<N>,
    <B_R> <= C_B R^3 E/a, C_B=28000322.                 (E)

The factor theta here is per lost dimer; equivalently the relative loss in
2<G>/<N> is 2theta. By Cauchy/Jensen and G<=N/2,
sum_j<g_j(g_j-1)> >= <G>^2/n_cells-<N>/2. Combining (C)-(E) gives, with
rho=<N>/V and e=E/V,

    e >= a/D [rho^2(1-beta)_+^2/4-rho/(2ell^3)],
    D=g+C ell^3/(R^3 w)+2ell^2/R^3,
    beta=C_B R^3 e/(a rho)+2theta.                     (F)

Here L>=4ell, ell>=R>=10, and w<ell/2. This applies to arbitrary coherent
or mixed states with rho>0; it does not require fixed N. The only use of
the selected translation is the particle-count estimate. The energy rows
remain bounded above by the original global positive gradient sum for
every translation. The actual D(m) was never recomputed.

For fixed small rho, take volume large first and choose

    ell=floor(rho^(-3/8)), R=ceil(rho^(-7/24)),
    w=ceil(rho^(1/16) ell).

For sequences e<=C_E rho^2 with fixed C_E, the Green error and boundary
particle fraction are O(rho^(1/16)); rho R^3, ell^2/R^3 and
1/(rho ell^3) are O(rho^(1/8)). Equation (F) therefore gives

    e/rho^2 >= a/(4g)-O(rho^(1/16))-O(ell/L).           (G)

The low-energy qualification can be removed by separating states with
e> (a/g)rho^2, which already obey the desired bound. Thus (G) is a candidate
unconditional dilute lower theorem for all mean-density states in the
thermodynamic-first order. Its explicit asymptotic constant is at least
2a/(sqrt(3)pi). It is not the full relaxed T0 coefficient or an exact EOS.

This explains how positive order-rho^2 cluster energy can be discarded:
only positive gradient rows/pins are selected, while (E) pays the omitted
particle fraction. No deletion channel, nearly global isolated-pair
projection, or claim that the omitted energy is o(rho^2) is made.

The initial nine-component internal-mass cell route remains a separate
possible auxiliary result: (1-epsilon) times the complete actual S/W rows
inside Lambda plus epsilon a Delta_N. Its constant soft kernel should have
dimension five and gap at least epsilon a/(14ell^2), for epsilon<=1/2.
The naive row cut alone has axial corner zero modes. A quantitative matrix
Green convergence argument requires an internal high-channel corrector;
without it a first-order commutator need only be O(ell^-2), not ell^-3.
Neither that matrix convergence nor any full-T0 many-particle replacement
is used in (A)-(G).
