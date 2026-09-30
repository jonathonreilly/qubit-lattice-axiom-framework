# A Neumann-pin dilute lower bound on the actual qubit carrier

Author discovery candidate, September 30, 2026. **Status: conditional-support**
for the supplied native Hamiltonian. This is not formal review, audit, a
selected physical law, a leading equation of state, or a phase theorem.
The new all-state lower bound requires a focused independent check before
substantial downstream reuse. Earlier frozen artifacts are unchanged.

The result materially strengthens the model's dilute lower energy bound.
Let a=min(tau,mu/12)>0 and

    g=(2pi)^(-3) integral_[-pi,pi]^3 [4 sum_j sin^2(k_j/2)]^(-1) dk
       <=sqrt(3)pi/8.

For arbitrary states on the physical L-cubed qubit torus, write rho=<N>/V
and e=<H0>/V. There are universal constants C and rho0>0 such that, for
0<rho<rho0, ell=floor(rho^(-3/8)), and L>=4ell,

    e >= a rho^2 [1/(4g)-C rho^(1/16)-C ell/L].          (1)

The constants are independent of volume, the state, mu and tau; the latter
enter through a. Equivalently, volume first at fixed density, followed by
the dilute limit, gives the all-state lower coefficient

    liminf e/rho^2 >= a/(4g) >=2a/(sqrt(3)pi).           (2)

This is a lower coefficient, not equality with the relaxed full T0
interaction. It uses neither an all-N dimer isometry nor a scalar particle
gas. Scalar Neumann estimates are applied to the nine *actual pair
annihilation amplitudes*, which retain their complete occupation output.
Positive energy of omitted clusters may be discarded: only the associated
particle loss is estimated. No small global defect projection is needed.

## 1. Authority, exposure and actual premises

CONTRACT.md was frozen before computation at SHA256
2792b717fbd4153040464dc322d8243ceb18182126b8b519c684946a5d371a7c.
The tentative matrix-cell route was reasoned about before that freeze; no
computation preceded it. Main was refreshed to
30a9461ee19a49b99fa6628fe942f08e504e8903; selected procedure remains
7146fe17a76de41badcaca3c3c7cac6d11eb2a00. The complete landed density law,
the complete root lower check, and the relevant previously complete
threshold/upper checks were read. SOURCE_BINDINGS.json records exact bytes.

A current-main native Neumann/Dyson/lower search found the landed point-pin
argument and results on other carriers, not this comparison. Open PRs9398
(supplied analytic gravity),9397 (supplied record apparatus),9008 (ice
covariance) have different laws and are not mathematical inputs. No
exhaustive or historical novelty assertion is made. No external theorem,
data or fitted constant is imported. The elementary Fourier and counting
arguments used here are supplied below.

The carrier is the full tensor product of one qubit per site, with actual
b_x=|0><1|, n_x=b_x^dagger b_x, commuting operators at distinct sites, and
N=sum n_x. The unchanged supplied law is

    H0=mu N-2mu sum PE-mu sum PT+V3+W,
    V3=mu sum_x n_x binom(m_x,2),
    m_x=sum_(d in G)n_(x+d), G={+/-2e_i,+/-e_i+/-e_j},
    W=tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|^2.

The fifteen bare words are d_i(x)=b_(x+e_i)b_(x-e_i) and
v_ij^(s,t)(x)=s t b_(x+s e_i)b_(x+t e_j). The E doublet is the normalized
traceless combination of the three d_i and Q_Tij=(1/2)sum v_ij^(s,t).
The full-carrier positive identity is

    H0=S+mu D+W,
    S=(2mu/3)sum|d1+d2+d3|^2+(mu/4)sum_plane sum_(r<s)|v_r-v_s|^2,
    D=(1/2)sum_x n_x(m_x-1)(m_x-2)>=0.

The landed gradient inequality and the checked mesoscopic isolation bound
are the two load-bearing many-particle premises:

    H0>=a Egrad,
    <B_R><=C_B R^3 <H0>/a, C_B=28000322.                 (3)

Here Egrad sums all fifteen bare-gradient norms, and B_R counts particles
outside actual R-isolated graph dimers: a selected dimer is a graph edge
and no other occupied site lies within Chebyshev distance R of either
endpoint. The bound holds for R>=10 and L>=10R. It was derived and
independently checked on the full carrier; it is not a gap above an
extensive background. This report does not reclassify it as a phase result.

Use the nine forward fields B_d(x)=b_x b_(x+d), where d=2e_i or
e_i+/-e_j (i<j). Summed axial gradients are translations of the centered
ones; each forward plane field occurs twice among the centered plane words.
Therefore Egrad dominates the nine forward gradient sum. For every output
occupation eta containing y, all nine amplitudes
f_(eta,d)(y)=<eta|B_d(y)psi> vanish exactly. The checked single-pin extension
established these normalization facts; the present proof extends the use
of the pins to actual many-particle states, not by importing its N4 bound.

## 2. Finite Neumann Green function with controlled boundary

Let Lambda={0,...,ell-1}^3. Its scalar free-path Laplacian Delta_N has
quadratic form E_N(f)=sum_(x,x+e_j in Lambda)|f(x+e_j)-f(x)|^2. Its kernel
is constants and its first positive eigenvalue is

    lambda1=4 sin^2(pi/(2ell))>=4/ell^2.                 (4)

Let G_N=Delta_N^+ on the mean-zero subspace. Put
ell(k)=4sum sin^2(k_j/2), and let G_Z(r) be the Fourier coefficients of
ell(k)^(-1). They exist in dimension three and obey

    G_Z(0)=g, |G_Z(r)|<=C/(1+|r|).                      (5)

For x,y at least w lattice layers from every face, 1<=w<ell/2,

    |G_N(x,y)-G_Z(x-y)|<=C/w.                          (6)

Here and below C may increase but is universal. To prove these estimates,
choose once a smooth radial cutoff chi, zero up to radius one and one from
radius two. On a Fourier annulus of radius s, ell(k)^(-1) has derivative
bounds C_j s^(-2-j). Integration by parts bounds its shell coefficient by
C_j s(1+s|r|)^(-j). Summing dyadic shells proves (5). Applying the same
argument to chi(k/kappa)/ell(k), with j>=5, gives

    |G^kappa(r)|<=C(1+|r|)^(-1)(1+kappa|r|)^(-4).       (7)

The smooth outer part of the periodic symbol has the same bound. For a
period-2ell torus choose kappa=1/ell. Every nonzero discrete momentum has
length at least pi/ell>2kappa. Its inverse-Laplacian symbol is therefore
exactly the sampled cutoff symbol, with zero mode zero. The absolute
summability in (7) justifies periodization. For the nearest representative
r in [-ell,ell]^3, every nonzero image r+2ell n has distance at least
ell(2||n||_infinity-1). Summing (7) over those images costs O(1/ell).
The removed Fourier ball also costs O(1/ell), since 1/ell(k) is bounded
by C/|k|^2 there. Thus

    |G_(2ell torus)(r)-G_Z(r)|<=C/ell                  (8)

uniformly in that representative. The uncut 1/r kernel is never periodized.

The exact Neumann reflection formula is

    G_N(x,y)=sum_(sigma in {+,-}^3) G_(2ell torus)(x-y^sigma),
    y_i^+=y_i, y_i^-=-y_i-1.                           (9)

It follows either from the free-path cosine eigenvectors
sqrt((2-delta_n0)/ell) cos(pi n(x+1/2)/ell), or by reflecting the discrete
heat equation. The eight stationary torus contributions sum to the one Neumann
constant mode, so (9) has exactly the mean-zero inverse normalization.
There is no division by eight. For an interior pair x,y, every nonidentity
image has nearest periodic distance at least 2w+1 in a reflected coordinate.
Equations (5) and (8) prove (6).

## 3. Separated pins and a finite-volume norm inequality

Choose m pin sites in the w-interior of Lambda, pairwise more than R apart
in Chebyshev distance, ell>=R>=10. Their scalar Green matrix Gamma is the
compression of G_N. Packing disjoint translates of the integer cube [0,R]^3
gives

    m<=M:=8 ell^3/R^3.                                 (10)

Shell packing also gives, for each selected site,
sum_(other pins)(1+distance)^(-1)<=C ell^2/R^3. The image error (6) costs
C m/w in a row. Since w<=ell, Gershgorin bounds the largest eigenvalue by

    lambda_max(Gamma)<=B:=g+C ell^3/(R^3 w).            (11)

The positive semidefinite matrix need not be inverted. Let f be any
nine-component field vanishing at all pins, and write f=c+q with mean q=0.
Cauchy-Schwarz in the inverse-Laplacian form, applied to the sum of the
pin evaluations, yields

    m^2||c||^2 <= (1^T Gamma 1) E_N(f) <=m B E_N(f).

For m=0 the ensuing inequality is trivial. The Neumann Poincare estimate
from (4) gives ||q||^2<=ell^2 E_N(f)/4. Since
||f||^2=ell^3||c||^2+||q||^2, this proves

    E_N(f) >= m||f||^2/[ell^3 D_cell],
    D_cell=B+M/(4ell)=g+C ell^3/(R^3 w)+2ell^2/R^3.     (12)

This is a quantitative finite-domain capacity/gap bridge. All nine
components remain actual bond amplitudes. The mean-zero scalar gap is
used only to price their variance, not as a many-body spectral gap.

## 4. Literal many-particle extraction count

Tile floor(L/ell)^3 complete anchor cubes in the torus, leaving a remainder
if necessary. For each cell j and each residual occupation eta, take one
endpoint of every actual R-isolated dimer of eta whose two endpoints lie
in that cell's w-interior. Use a fixed choice, for example the local
lexicographically earlier endpoint. These sites are valid common pins of
f_(eta,d)(x), for all nine d, and are more than R apart. Apply (12) to the
restriction of these amplitudes to the anchor cube.

Within-cell forward differences are distinct members of the global positive
gradient sum. Though a bond near an anchor boundary can reach outside that
cube, no disjoint physical Hilbert factors are assumed. We select each
gradient row at most once. The original D(m) is untouched. Summing over
cells, residual occupations and components is therefore legitimate under
H0>=a Egrad.

For an original occupation S, let g_j(S) count its R-isolated dimers with
both endpoints in cell j's w-interior. If one is removed, every other one
remains R-isolated in the residual and inside that interior. The removed
graph bond has exactly one forward anchor there. Thus, denoting the number
of selected residual pins by m_(eta,j),

    sum_eta m_(eta,j)||f_(eta,j)||^2 >= <g_j(g_j-1)>.     (13)

This is direct occupation counting. For each selected input dimer, there
are at least g_j-1 residual pins; there are g_j such removed dimers. A
single B_d(x) has at most one input word for any specified output eta,
so its squared amplitude is diagonal in that input word. Every other
removed bond contributes nonnegatively. There is no matching choice,
exchange sign, division by two, or repeated approximate pair isometry.
The argument applies to mixed states by linearity, or by retaining a
purifying index in the amplitudes.

## 5. Particle loss, without an energy-smallness requirement

Let A_bad be the sites outside the w-interiors of the complete cubes. Their
fraction theta obeys

    theta<=3ell/L+6w/ell.                              (14)

Average the whole tiling over torus translations. The expected number of
particles in A_bad has average theta<N>, so one translate has no larger
expectation. Fix it. Let G=sum_j g_j. A graph edge has Chebyshev length at
most two, while distinct cell interiors are separated by at least three
sites when w>=1. Hence if a dimer has both endpoints in the union of those
interiors, both belong to the same cell. Every omitted original R-isolated
dimer therefore has an endpoint in A_bad. Such dimers are disjoint, giving

    <G> >= (<N>-<B_R>)/2-theta<N>,   G<=N/2.             (15)

The factor theta counts lost dimers, not lost particles; the corresponding
relative loss in 2<G>/<N> is 2theta. This is where the prior checked
mesoscopic bound (3) enters. Nothing requires the energy of excluded
clusters to be o(rho^2 V). No erasure channel is applied to the state, and
there is no claim that its global isolated-dimer projection is close to one.

Cauchy/Jensen, with n_cells complete cubes, implies

    sum_j<g_j(g_j-1)> >= <G>^2/n_cells-<N>/2.           (16)

Since n_cells ell^3<=V, equations (12)-(16) prove the finite inequality

    e >= (a/D_cell)[rho^2(1-beta)_+^2/4-rho/(2ell^3)],
    beta=C_B R^3 e/(a rho)+2theta.                     (17)

It holds for arbitrary states, rho>0, provided L>=4ell, ell>=3R>=30 and
1<=w<ell/2. These conditions ensure the reused requirement L>=10R.
The selected tiling depends on the state only through a particle-count
average. The positive energy comparison holds for every tiling, so this
selection does not change its direction.

## 6. Ordered scales and the unconditional lower coefficient

For sufficiently small rho, choose

    ell=floor(rho^(-3/8)), R=ceil(rho^(-7/24)),
    w=ceil(rho^(1/16) ell).                             (18)

They satisfy the conditions above for every L>=4ell. The relevant errors are

    ell^3/(R^3 w)=O(rho^(1/16)),   w/ell=O(rho^(1/16)),
    ell^2/R^3=O(rho^(1/8)), rho R^3=O(rho^(1/8)),
    1/(rho ell^3)=O(rho^(1/8)).                         (19)

For states with e<=(a/g)rho^2, beta in (17) is bounded by
(C_B/g)rho R^3+2theta. For every beta>=0, (1-beta)_+^2>=1-2beta.
Using D_cell>=g and
1/D_cell>=1/g-(D_cell-g)/g^2 in the positive term of (17), while bounding
its negative terms by 1/g, gives (1). All implicit constants are universal.
States with e>(a/g)rho^2 already satisfy (1), so the low-energy assumption
is removed rather than left as a hidden hypothesis. This proof also covers
states with fluctuating particle number and prescribed *mean* density.

The ell/L term requires the stated limit order. In particular, no positive
bound is asserted for the exact zero-energy uniform two-particle state when
N=2 is kept fixed and V grows; that sequence has ell larger than the torus
scale in (18). The adverse term rho/(2ell^3) in (17) is kept until after
the mesoscopic scale has been chosen. The result is uniform over states
at each fixed density, before the thermodynamic and then dilute limits.

For the already defined chemical-potential ground problem, the old
coercivity bound first ensures every thermodynamic ground-state density
tends to zero with nu. Applying (1), then minimizing the lower quadratic
c rho^2-nu rho with c tending to a/(4g), yields the additional lower bound

    liminf_(nu down to0) e0(H0-nu N)/nu^2 >=-g/a.       (20)

Here the thermodynamic limit or accumulation lower energy is taken first.
Since the vacuum trial gives e0<=0, the same estimate gives
limsup rho_ground/nu<=4g/a for thermodynamic ground-state accumulation
densities. These are improved bounds, not a differentiable EOS, a matching
upper coefficient or an order parameter. The checked threshold upper
construction retains its separate coherent variational scope.

## 7. Boundary pitfalls and a genuine nine-component cell gap

The proof did not replace D(m) by a count using deleted neighbors. That
replacement would fail even on one graph dimer: its two vertices have
m=1 and D=0, whereas deleting their edge gives m=0 and D=2. Nor does
simply keeping the actual complete S/W rows inside an anchor cell supply
the expected five-dimensional kernel. The forward axial corner variable
B_1(0) is absent from every such retained row: its center is e1, and each
relevant E or singlet row also has an anchor e1-e2 or e1-e3 outside the
cube. A shifted E-gradient row cannot cancel that outside variable.
Its coordinate vector is consequently an exact extra zero mode.

A safe auxiliary nine-component operator is nevertheless available. Let
K_cut be the sum of all complete actual N2 S/W rows whose nonzero forward
anchors lie in Lambda. For 0<epsilon<=1/2 put

    K_(Lambda,epsilon)=(1-epsilon)K_cut
                          +epsilon a (Delta_N tensor I9).       (21)

It is a lower comparison obtained by splitting the global S+W form and
using the bare-gradient inequality on the epsilon part. Thus no new
physical boundary law is postulated. Its kernel consists exactly of the
five constant normalized soft vectors U, and

    gap(K_(Lambda,epsilon)) >= epsilon a/(14ell^2), ell>=3. (22)

Here is a direct proof. Write f=m+q with spatial mean q=0, and let P_high
be the four-dimensional internal complement of U at zero momentum.
On centers in {1,...,ell-2}^3 all S rows are retained. For a constant m,
their value is 2mu(ell-2)^3||P_high m||^2. For arbitrary q their value
is at most 2mu||q||^2: extend q by zero and use the actual infinite N2
bound S<=2mu I. The latter follows directly from the axial singlet and
plane difference symbol, whose largest eigenvalues are at most 2mu.
The triangle inequality squared gives, since (ell-2)^3>=ell^3/27,

    ell^3||P_high m||^2 <=27 S_inner(f)/mu+54||q||^2.

Therefore the distance from the constant soft space obeys

    dist(f,ker)^2 <=55||q||^2+27 S_inner(f)/mu
       <=[55ell^2/(4epsilon a)+27/((1-epsilon)mu)] <f,K f>.

For ell>=3, epsilon<=1/2 and a<=mu/12 the bracket is at most
14ell^2/(epsilon a), proving (22). Vanishing energy first makes every
component constant, after which one interior S cell imposes precisely the
four high constraints. This proves the kernel as well as the gap.

For a common nine-component pin at one cell site, the mean-soft-complement
Green compression is strictly positive: K<=b I, b=2mu+24tau, and its
lower bound is (1-ell^(-3))I9/b. This follows from K^+>=Q/b and the
constant soft projection at that site being U U^dagger/ell^3.

Equation (22) is not used to prove (1). A proposed quantitative convergence
of the *matrix* pin Green function would require more work. In particular,
cutting its infinite Green response without a corrector can leave an internal
first-order commutator of size O(ell^-2). The derivative of the forward-cell
axial singlet symbol at zero maps a soft E vector into the high singlet, so
the scalar O(ell^-3) residual estimate does not follow from the gap alone.
An internal high-channel corrector can plausibly repair it,
but that estimate is not claimed here. The scalar proof above avoids this
unproved step completely.

## 8. Actual controls and the remaining full-threshold problem

The frozen new primary `check_neumann.py` uses no earlier author numerical
implementation. It reconstructs actual S/W rows from literal endpoints,
Neumann cosine modes, reflection images, and occupation-set removals.
The 243- and 576-dimensional unregularized cell matrices have respectively
58 and107 numerical zero modes, including the exact zero corner column.
At epsilon=0.05 and0.25, all four tested regularized matrices have exactly
five zero modes and satisfy (22) and the common-pin lower bound. Their
first positive eigenvalues range from0.0021316065 to0.0118771941; these are
finite controls, not extrapolated gap values.

On a seven-cubed scalar cell, 500 independently selected cosine/image
comparisons have maximum error3.06e-16. An erroneous division of the image
sum by eight gives error0.14219 and is rejected. A pinned nine-component
complex field satisfies the finite mean-capacity and norm inequalities.
Eight literal 29-particle configurations containing isolated dimers,
boundary particles and a triangle give extraction counts40>=36. Three
isolated dimers give exactly6=3(3-1); inserting an extra one-half fails.
These tests verify local formulas, not the analytic uniform constants.

The single managed run was priced at30 CPU seconds/150 MB, used1.859389
CPU seconds,1.924527 wall seconds and77,676,544 bytes peak RSS, and passed
without a failed assertion or repair. Numerical thread caps were one;
deadline/STOP checks were active. No full Fock box, many-body ground state,
full T0 matrix, limiting Green value g, or long-range-order observable was
computed. The complete pre-control derivation is preserved separately.
The final finite-domain statement requires ell>=3R, sharpening the initial
draft's ell>=R so that L>=4ell implies the reused L>=10R condition. The
chosen dilute scales already obey this stronger condition. No test source,
equation normalization or expected diagnostic value was changed.

The stronger target is still open for a precise reason. The passage from
H0 to a times the bare gradients deliberately discards its internal
interaction and polarization information. It cannot identify the coefficient
with the full T0 form. Even replacing the scalar Green function by a static
nine-bond pin matrix would independently minimize each removed-pair fiber.
The physical fibers satisfy compatibility identities whenever two different
removals have the same input occupation. These constraints participate in
the actual four-particle relaxation and cannot be replaced by an assumed
many-pair isometry.

The next useful route is a finite-cell *compatible two-pair* replacement
retaining the actual N4 threshold form and pricing its many-body boundary
and variance errors. A simple sum of arbitrary four-particle restrictions
does not supply it: after normalization to keep the two-body terms fixed,
it overcounts the one-body mu N term and undercounts V3. For N>4 the exact
difference is (N-4)[V3/(N-2)-mu N/3], which is negative on any occupation
of separated graph dimers. Thus that direct lower comparison already fails.
This is a restricted template failure, not a no-go for another replacement.
Precisely, let T_(N,4) resolve four removed particles with the complete
N-4 residual, just as the earlier two-particle extraction did. Divide
T_(N,4)^dagger (direct_sum H4) T_(N,4) by binom(N-2,2). Each normal-ordered
two-body term then has coefficient one, a one-body term has coefficient
(N-1)/3, and a three-body occupation term has coefficient 2/(N-2).
These are counts of the additional spectator sites, proving the displayed
difference without using a tensor-product boson lift.

The present result resolves a different concrete obstruction: positive
order-density-squared cluster energy need not be shown negligible to obtain
a substantial actual lower coefficient. Positive row selection, particle
loss and the literal count (13) suffice. The leading multichannel EOS,
fragmentation/polarization problem and extensive physical pair order remain
unresolved. No original-record, gravity or foundational conclusion follows.
