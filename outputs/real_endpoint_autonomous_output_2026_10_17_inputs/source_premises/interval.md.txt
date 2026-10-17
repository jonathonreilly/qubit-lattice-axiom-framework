---
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
independent_review: pending
audit_required_before_effective_retained: true
---
# An explicit interval certificate for the fixed old-cap ladder

The frozen old-cap stationary witness satisfies the finite-channel bridge's
scattering hypotheses on the nonzero common interval

    Icert=[k0-10^-3,k0+10^-3],
    k0=2 arctan(1/q), q=4.510351185997098 exactly.           (1)

The following are uniform, rigorously bounded quantities, not values from a
momentum grid:

| Quantity | Sufficient bound on Icert |
|---|---:|
| Gap from each incident energy to every other channel band | >=0.18 |
| Closed root magnitude | <=1/7 |
| Physical-basis 16 by 16 matching inverse, spectral norm | <166 |
| Bridge's 24 by 24 matching inverse, spectral norm | <366 |
| Bridge matching minimum singular value | >1/366 |
| Absolute-site reflection derivative | <=700 |
| Localized correction norm and derivative | <=31 and <=2700 |

Using the root-qualified provisional bridge `THEOREM_V2.md` at frozen SHA256
`db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3`,
these certificates give the finite preparation and complete-output example
in section 7: isometry error below 0.011 for every elapsed time t>=2*10^13
on the infinite half-line. A finite clock of 9*10^14 sites gives error below
0.012 through t=4*10^13. These large sufficient costs are analytic bounds,
not simulated device sizes or optimized resources.

The generic bridge has received a separate check and root acceptance for
conditional provisional use. This concrete composition is a new source-exposed
author calculation awaiting its own separate check. Its interval certificate
is explicit; its wavepacket conclusion remains conditional on the analytic
bridge and on supplying the stated Hamiltonian and preparation. No arbitrary
exact accuracy, native clock generator, all-site cap 2, retained audit status,
or hardware closure is claimed.

## 1. Fixed physical model and exact input identity

Use the square ladder from the frozen `inputs/RESULT.md` and `inputs/ROUTE.md`:
old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0), and clock sites
c_n=(n,2,0). All listed non-onsite blocks are nearest-neighbor two-body blocks.
Let n=(I-Z)/2, a=|0><1|, L_AB=a_A^dagger a_B+a_B^dagger a_A, and

    K=2I+Z1 Z2,
    C=DeltaA nA+DeltaB nB+h(nA+nB-L_AB)+u nA nB,
    G=gA nA(I+X1)+gB nB(I+X2),
    B=K+C+G,
    VA=lambdaA(I+XA)+mu0 I,
    VB=lambdaB(I+XB)+mu1 I.                                (2)

The following terminating decimals are exact:

| Parameter | Value | Parameter | Value |
|---|---:|---|---:|
| J | 0.030021107107032 | gA | 0.996878563816670 |
| gB | 0.599319315560298 | h | 3.999349697888060 |
| lambdaA | 3.801781381581202 | lambdaB | 2.575033765788497 |
| u | 0.544607276405587 | DeltaA | 2.192035527016003 |
| DeltaB | 2.186826508897014 | mu0 | 0.321494607058201 |
| mu1 | -1.459892813020969 | nu=-mu1 | 1.459892813020969 |

In the supplied one-clock-head sector the physical Hamiltonian is

    Hphys=h0 tensor I+I tensor B+P0 tensor VA+P1 tensor VB+nu I,
    h0=2J I-J(S+S*),       Pn=|n><n|.                     (3)

The physical well is nu(I-n_c1), rather than a negative physical block.
The clock's positive bond representation contains the entrance term J n_c0,
which is required for the constant diagonal 2J. C, G, both contact blocks,
mu0 n_c0, the vacancy block, and all clock bonds are positive. Clock number
is conserved by the full qubit Hamiltonian. The supplied one-head and
finite-excitation representation assumptions are those of the frozen route.

For Omega=|00>_AB and iota x=x tensor Omega,

    B iota=iota K,
    (B+nu I)iota=iota(K+nu I).                             (4)

This holds exactly because C+G annihilates the source vacuum. The calculation
checks it in the complete sixteen-dimensional old/source basis, not only at
one incident energy. It also checks exact reduction by p=X1 X2. Within a
parity block use the normalized old vectors proportional to
|00>+p|11> and |10>+p|01>, with s=Z1 Z2=+1 and -1 respectively. There are
two independent incident logical columns per parity block.
The code orders source before old; the fixed tensor-factor swap to iota's
notation is unitary and does not change any of the norms.

No commutator [Hphys,K]=0 is assumed: the contact-excited source allows G to
mix the two old energies locally. The full operator is static; actual old
aging in the comparator will be e^(-itK), for the entire elapsed time t.

## 2. Uniform closed-channel gaps without numerical eigenvectors

Let epsilon(k)=2J(1-cos k), lambda_s(k)=2+s+epsilon(k), with nu added to
both sides for the physical energies. At k0, cos k0 and sin k0 are exactly
(q^2-1)/(q^2+1) and 2q/(q^2+1). The program reads these rational strings
and checks the trigonometric identity and epsilon0 exactly.

Since |epsilon'|<=2J, on Icert one has the exact rational bounds

    epsilon0-2J/1000 <= epsilon(k) <= epsilon0+2J/1000,
    epsilon(k) lies between 0.005566295300504832... and
                            0.005686379728932960....       (5)

The decimals in explanatory displays are not outward interval endpoints;
the rational expressions in (5) and `CERTIFICATE.json` control the proof.
Sin k>=sin k0-1/1000 gives

    epsilon'(k)>=2J(sin k0-1/1000)>0.02531671586811827,
    v=1/40 is a valid lower bound,  E2=2J,  E2/v<5/2.       (6)

The interval is inside (0,pi): sin k0>1/1000, together with the Lipschitz
bound for sine, excludes either endpoint. Each source-excited eigenvalue
of B is at least 1+min(DeltaA,DeltaB), because K>=I, the penalty is at least
min Delta on that subspace, and the other blocks are positive. Source number
is preserved by B. Thus the least source-band gap, occurring for s=+1, is
at least

    min Delta-2-(epsilon0+2J/1000)
      = 0.18114012916808103... > 9/50.                    (7)

The two old-vacuum bands are separated by the exact number
2-4J=1.879915571571872. This is also a valid lower bound for the separation
of each incident energy from the other old-vacuum band on Icert. Every parity
sector therefore has exactly one open channel for each chosen incident energy;
all seven other channels are closed. All source outputs are included.

For any closed eigenchannel b define q_b by

    q_b+q_b^-1=(2J+b-lambda_s(k))/J,   q_b real, |q_b|<1.

The common gap g=9/50 gives

    2+g/J > 1/7+7,
    |q_b|<=kappa=1/7,
    |q_b'|<=2 kappa^2/(1-kappa^2)=1/24.                   (8)

The roots and the underlying spectral projections vary regularly: the
eigenvectors of the fixed B can be chosen once, while no threshold is crossed.
There is no dependence here on the rounded eigenvalue lists in the route.

## 3. From the exact point certificate to a uniform physical inverse

Write M16 for the witness's matching matrix in the physical parity basis:

    M16(k) = [[lambda_s-2J-B_p-VA, J I8],
              [J I8, F_p(lambda_s)-VB]],
    F_open=-J exp(-ik),       F_closed=-J/q_b.             (9)

The companion code replays the point certificate from its exact rational
parameters, with no optimizer or binary64 parameter reconstruction. Mpmath
at 90 digits proposes source square roots, inverses and states; they are
rounded to denominator 10^55. Exact Fraction residuals certify them.

For a positive candidate square root S_hat of A=D^2-4J^2 I, with certified
positive lower bounds a for the true root and b for S_hat, the Sylvester
identity gives ||S_hat-sqrt(A)||2<=||S_hat^2-A||2/(a+b). The code uses
a=d-2J and b=d-||S_hat-D||infinity. Symmetry bounds the residual spectral
norm by the row sum; sqrt(6)<3 converts the six-dimensional F error to an
infinity-norm bound. The other closed vacuum channel is treated by the
scalar analogue. Exact inverse and state residuals then give the Neumann
certificate for the true M16. All root and inverse proposal matrices are
saved in `POINT_WITNESSES.json`.

The replay reproduces the four point inverse bounds:

| (s,p) | Certified infinity-norm ceiling, decimal display |
|---|---:|
| (+1,+1) | 163.9029010203209... |
| (-1,+1) | 154.9928305605314... |
| (+1,-1) | 128.4349384249287... |
| (-1,-1) | 124.1992107742216... |

In particular, exact rational comparisons establish a common ceiling 164.
The true matrix is complex symmetric: B_p and the closed spectral function
are real symmetric, and the open term is diagonal in the real vacuum basis.
Its inverse is complex symmetric too. Consequently its ordinary modulus
induced norms satisfy ||M16^-1||1=||M16^-1||infinity, and

    ||M16(k0)^-1||2
       <=sqrt(||M16^-1||1 ||M16^-1||infinity)<164.          (10)

The certificate's row sums |Re|+|Im| dominate the ordinary modulus row sums.
Thus (10) does not incur an undocumented dimension factor.

On Icert, differentiating the spectral entries gives

    |F_open'|=J,
    F_closed'=2J sin(k)/(1-q_b^2),
    ||M16'(k)||2 <= 2J/(1-kappa^2)
                  = 0.061293093676857 exactly.            (11)

M16' is block diagonal, so this is a spectral-norm bound in the physical
basis, regardless of a numerical eigenvector basis. Therefore

    eta=164*(2J/(1-kappa^2))*10^-3
       =0.010052067363004548...<1,
    sup_Icert ||M16(k)^-1||2
       <=164/(1-eta)=165.6652785395908...<166.             (12)

This Neumann argument proves invertibility at every momentum in the interval.
It is not an extrapolation from a nonsingular grid.

## 4. Conversion to the bridge's exact 24 by 24 convention

The bridge uses unknowns z=(x0,x1,r,alpha) with d=8, dimension 3d=24.
Its exterior wave at n>=2 is

    (exp(-ikn)+r exp(ikn))u + sum_l alpha_l q_l^(n-2) v_l.

To establish the norm conversion without uncertified eigenvectors, choose
any fixed orthonormal B_p eigenbasis with open vector u. On the d-dimensional
coefficient vector y=(r,alpha), define

    Amap y = exp(ik)r u+sum_l q_l^-1 alpha_l v_l,
    Emap y = exp(2ik)r u+sum_l alpha_l v_l,
    Qlead=Emap Amap^-1
         =exp(ik)|u><u|+sum_l q_l |v_l><v_l|.              (13)

Then ||Amap^-1||2=1 and ||Qlead||2=1. For arbitrary right-hand side
f=(f0,f1,f2), the bridge's three matching rows read

    D0 x0-J x1=f0,
    -J x0+D1 x1-J Emap y=f1,
    -J x1+J Amap y=f2,     Da=2J+B_p+Va-lambda_s.          (14)

Eliminating y gives exactly

    M16 [x0;x1] = -[f0; f1+Qlead f2],
    y=Amap^-1 x1+J^-1 Amap^-1 f2.                        (15)

Indeed D1-J Qlead=-(F_p-VB), using q+q^-1 and z+z^-1 in the closed and
open channels respectively. This checks the Schur-complement signs as well
as the norm conversion. The right side for [x0;x1] has norm at most
sqrt(2)||f||. Stacking x and Amap^-1 x1 costs another factor sqrt(2), and
the last term of y costs at most J^-1||f||. Hence

    ||M24^-1||2 <= 2*166+J^-1
                =365.3098974809548...<366.                (16)

All basis changes on the internal rows and x coordinates are unitary, and
the coefficient basis for y is orthonormal. This is the bridge's actual
Euclidean norm convention, not a comparison between unrelated row norms.

Use nu24=1/366. The bridge's matrix derivative estimate gives

    LM24=J sqrt(9+4/(1-kappa^2)^2)<11/100,
    X0=sqrt(2)J/nu24<16,
    X1=[sqrt(5)J+LM24*16]/nu24<700.                        (17)

These exact inequalities certify the scattering unknowns and derivatives.
Conserved flux gives |r|=1, so L=700 bounds |r'|. Substitution in the
bridge's full localized correction (both contact sites and every closed
tail) gives C0=31 and C1=2700 as valid ceilings. The code checks these
inequalities by squaring positive rational bounds, without treating a
floating square root as an enclosure. In particular it includes the
closed-tail derivative sum

    sum_(m>=1) m^2 kappa^(2m-2)
       =(1+kappa^2)/(1-kappa^2)^3.

## 5. Reflection origin and the single common phase

The witness's incident wave is exp[-ik(n-1)] and its reflected wave is
r_site1 exp[ik(n-1)]. Multiplying the entire stationary column by exp(-ik)
normalizes the absolute-site incident wave to exp(-ikn). Thus

    r_abs(k)=exp(-2ik) r_site1(k).                         (18)

The free boundary is at n=-1, so its site-1 reflection is -exp(4ik).
In the bridge's absolute-site convention it is r0(k)=-exp(2ik). An exact
finite algebra check sets the free contact values to x0=z-z^3, x1=1-z^4;
the two rows of (9) give [0;2iJ sin k] identically. The code checks this
with the exact rational z0 and also checks the scalar identity below.

Let alpha be the exact unit-modulus witness coefficient
r_site1_(s=-1,p=-1)(k0). The target is

    W=((9+12i)I+(-16+12i)X1X2)/25,

with eigenvalues w_+=(-7+24i)/25 and w_-=1. It commutes with K, so the
chosen (s,p) basis is their common eigenbasis. The single scalar required
by the bridge is

    zeta=exp(i gamma)=-exp(-4ik0)alpha,     |zeta|=1.       (19)

In fact r0(k0)zeta=exp(-2ik0)alpha. Thus the certified central comparison
is transferred unchanged, in all four old channels, to

    max_(s,p) |r_abs_(s,p)(k0)-r0(k0)zeta w_p|
       <= exact stored rational bound
       =1.752474830885985...*10^-13 < 1.76*10^-13.         (20)

The new replay reproduces the frozen rational bound. It does not assume
exact central matching or fit separate phases for different old energies.
The rational approximation to zeta and its error below 3*10^-52 are stored
in the certificate, but the theorem comparator uses the exact unit scalar
defined in (19). The separate physical scalar remains exp(-i nu t).

On any packet interval |k-k0|<=sigma<=10^-3, (17) and |r0'|=2 give

    Delta <= 1.76*10^-13+702 sigma.                        (21)

At the full certificate width this is a loose 0.702000000000176 ceiling;
the resource example uses sigma=10^-6, giving
Delta<=0.000702000000176. The positive central ceiling remains in every
guaranteed accuracy statement. It is neither an exact fit nor a lower bound
on the true optimum. No arbitrary-accuracy family is inferred.

## 6. Complete wavepacket comparator and bound-state residual

Choose the bridge's normalized parabolic packet on
Ipacket=[k0-10^-6,k0+10^-6]:

    f(k)=sqrt(15)/(4sqrt(sigma))*(1-((k-k0)/sigma)^2),
    sigma=10^-6,           ||f||2=1,
    F0=||f||1<1/750,       F1=||f'||1<2000.                (22)

With (6), (17), C0=31 and C1=2700, valid common packet constants are

    CA=CB=2001,
    Dj <= 2000*31+(2700+(5/2)*31)/750
        =62003.703333333...,
    D=88000 > sqrt(2) max_j Dj.                            (23)

There are two incident old-energy columns per parity block. Their localized
errors need not be orthogonal; (23) explicitly pays the square-sum cost.
Outputs in the two different parity blocks are orthogonal. The propagating
columns, which end in distinct orthonormal vacuum old states, are orthogonal
and use the maximum phase error in (21), with no additional square root.

Define the scalar incoming packet and free outgoing packet by

    a_-T(n)=1/sqrt(2pi) integral f(k)exp[-ikn+i epsilon(k)T] dk,
    b_s^0(n)=1/sqrt(2pi) integral f(k)r0(k)
                                      exp[ikn-i epsilon(k)s] dk,
    chi=a_-T/||a_-T||,    beta_s=b_s^0/||b_s^0||.           (24)

The norms are taken on n>=0 and normalized by positive real numbers.
For the old-independent ready isometry V_ready x=chi tensor iota x, the
bridge supplies, for every elapsed t>=2T,

    ||exp(-it Hphys)V_ready - Uideal(t)||
       <= Delta+2(CA+CB)/sqrt(pi v T)+3D/(sqrt(2pi) v T),
    Uideal(t)x = zeta exp(-i nu t)
                 beta_(t-T) tensor iota exp(-itK) W x.    (25)

This retains all old, source and clock amplitudes. The exact bridge's
incoming-channel intertwining identity supplies the aging in (25); it
does not commute K through the full interaction. Transient source excitation
and all closed-channel tails are bounded by the localized correction.

Its normalization argument does not assume a complete scattering basis or
absence of bound states. The exact packet columns are orthogonal to point
spectrum. The supplied product input can have residual point-spectrum
amplitude at most

    2 delta_in(T),
    delta_in(T)=CB/sqrt(pi v T)+D/(sqrt(2pi) v T).           (26)

This contribution remains for all elapsed times and is already included in
(25). It is not removed by postselection or by discarding the source.
All operator bounds persist with an arbitrary passive reference; the complete
unhalved output trace-norm distance is at most twice the isometry bound.

## 7. One explicit finite readiness and finite-clock example

Take T=10^13 in the dimensionless time units of (2). The code proves the
following ceilings using only pi>3, sqrt(2pi)>12/5, and
866000^2<3vT:

    delta_in(T) <= 75042263/32475000000,
    RHS of (25) <=269134782504763/27062500000000000.        (27)

Their rounded displays are 0.002310770223248653 and 0.009944934226503945.
Both readiness normalization conditions in the bridge are comfortably met.
For eta_p=10^-3 choose the integer

    N=22000000000000,
    chi_N=1_(0<=n<N)a_-T / ||1_(0<=n<N)a_-T||.             (28)

This N satisfies the stronger rational version of the bridge's sufficient
cutoff inequality:

    N-2JT >= max(1,2JT,16(F1+F0)^2/(3 eta_p^2)).           (29)

Since pi>3, the actual omitted norm is at most eta_p/4; positive-real
normalization then gives ||chi_N-chi||<=eta_p. This specifies a finite
one-head vector by finitely many integrals, independent of the old input,
with source exactly Omega. It assumes that vector is supplied. It provides
no native preparation, emission or calibration algorithm. A preparation
isometry error eta_a would add eta_a to the following bounds; the displayed
example uses the specified exact mathematical vector, eta_a=0.

For V_N x=chi_N tensor iota x and the infinite Hamiltonian, the result is

    sup_(t>=2*10^13) ||exp(-it Hphys)V_N-Uideal(t)||
       <=296197282504763/27062500000000000 < 0.011.        (30)

The complete unhalved trace-norm distance is consequently below 0.022.
The infinite apparatus's point-spectrum amplitude is at most
91279763/16237500000<0.005622, uniformly in time, including the truncation
error. This is not an absence-of-bound-states assertion. For a finite clock
its entire spectrum is point spectrum, so that projection statement is
only about the infinite operator.

For a finite-clock version use sites 0,...,M-1, M=900000000000000, and
the compression of (3). The positive clock-bond realization includes the
far endpoint term J n_(M-1), preserving the diagonal 2J there. No additional
old or source contact is introduced. On the complete internal space,

    I<=B<=[3+DeltaA+DeltaB+2h+u+2gA+2gB]I<20I,
    Vmax=max(||VA||,||VB||)=7.925057370220605,
    rho=18>2J+(20-1)/2+Vmax.                              (31)

The physical nu shifts the spectral center by nu and leaves rho unchanged.
The first omitted clock site is M; from support 0,...,N-1 its shortest
path has exactly

    dM=M-N+1=878000000000001

hops. Onsite internal mixing does not shorten that path. The bridge's
Chebyshev bound at mu=1 is

    ||exp(-itHphys)V_N-embed exp(-itHphys_M)V_N||
       <=4 exp[-dM+rho t sinh(1)]/(1-exp(-1)).             (32)

For Tobs=4*10^13, zeta_boundary=10^-3, the exact rational inequalities
sinh(1)<6/5 and log[4/((1-exp(-1))*10^-3)]<9 imply that it suffices to
have dM>rho Tobs*(6/5)+9. The chosen integers satisfy this. The elementary
exponential estimates are checked from 8/3<e<11/4, with the latter obtained
from the first five Taylor terms and a geometric bound on the tail.

For every 2*10^13<=t<=4*10^13, the embedded finite output therefore has

    complete isometry error
       <=323259782504763/27062500000000000 <0.012,
    complete unhalved trace error <0.024.                  (33)

The comparator is the half-line state Uideal(t), with the same scalar and
aging. A finite M is covered through this stated horizon only. No chain of
these sizes was allocated or simulated. The bounds are deliberately loose
finite analytic costs and provide no feasible apparatus claim.

## 8. Resource scope, execution and remaining obligations

The fixed witness's added incident positive-block norm sums remain:

| Site | Added sum |
|---|---:|
| old1 | 1.993757127633340 |
| old2 | 1.198638631120596 |
| source A | 20.332662089993454 |
| source B | 17.078839343776311 |
| c0 | 8.015120691541701 |
| c1 | 6.730044773026091 |
| later clock sites | 0.120084428428128 |

The existing old edge has norm 3 and is additional. The old added cap 2
is met; source and boundary-clock caps of 2 are not. No optimization of
these costs, preparation cost, full-qubit operator norm over all clock
number sectors, or physical units is supplied. Static coefficients have
zero runtime slew but their installation and precision are assumptions.

`certify_interval.py` exited 0 in the single recorded execution; the wrapper
elapsed time was 0.657 seconds. The cap was 60 CPU seconds and 90 wall
seconds. The largest executed matrix was 16 by 16, source square roots were
6 by 6, and the 24-dimensional matching bound was proved by (13)-(17), not
by uncertified eigenvector numerics. Python 3.13.5, NumPy 2.4.4 and mpmath
1.3.0 were used; exact certification arithmetic was Python Fraction.
The requested BLAS/OMP thread counts were 1, without a claim of measured
hardware thread use. No search or interval grid was run.

The exact rational certificate, full stdout/stderr, actual command/runtime,
source hashes and rational point witnesses are preserved in `CERTIFICATE.json`,
`certificate.stdout`, `certificate.stderr`, `EXECUTION.json`,
`SOURCE_MANIFEST.json`, and `POINT_WITNESSES.json`. Numeric JSON displays are
named `display_float`; they are not outward enclosures and are never read
back as proof bounds. The input identities include the complete frozen
route, capped result, point verifier, point certificate and bridge. The
central replay follows the source-exposed point verifier's residual method;
it is not independent discovery or independent review. The phase-convention
algebra and Schur norm reconstruction address distinct additional risks.

The original execution read the immutable generic `THEOREM.md` at SHA256
`fffd7d405935226aba4a5e6528112b984b6dde4580747641159f554e97e2189a`.
Its actual run pins remain unchanged. The subsequent controlling V2 changes
only equation (5) to permit certified bounds 0<v<=min E' and E2>=max|E''|,
with one explanatory sentence. Those are precisely the inequalities already
used by this calculation. `BRIDGE_V2_DELTA.json` records the complete checked
diff and identities, and `inputs/THEOREM_V2.md` saves the controlling source.
No original evidence has been relabeled as a V2 execution. Root qualification
was read from `root_followup_qualification/QUALIFICATION.md` and
`ACCEPTANCE.json`; this note does not claim to have reread its full separate
review reports.

There is no remaining interval-existence, gap or matching-inverse obligation
for these exact coefficients within the stated conditional model: the
explicit bounds above provide them. The remaining dependencies are a separate
check of this concrete composition, exact physical coefficient/symmetry
realization, supplying the independently specified finite
ready vector, and any requested native-generation or physical interpretation.
No new prompt, axiom, retained claim, audit result, Git state or PR was changed.
The note does not assert reset, reuse, exact finite-time capture, a selected
classical Record, noise robustness, an all-site cap, or arbitrary exact
accuracy below the fixed central calibration ceiling.
