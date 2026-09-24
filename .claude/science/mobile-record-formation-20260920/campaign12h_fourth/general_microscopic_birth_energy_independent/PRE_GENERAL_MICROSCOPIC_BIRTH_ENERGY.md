# PRE reconstruction: microscopic birth energy beyond a one-center star

This is an independent reconstruction from the permitted local operators and
canonical cluster convention. The original gated compensation C_S and original
resolved/coherent jump instruments are fixed throughout. No general-microscopic
author packet, campaign CHECKPOINT, or external reservoir plan was read before
this PRE. Source identities and complete reproducible controls accompany the
note. This is a conditional mathematical result for the supplied model, not an
audit, landing verdict, energy-source model, or new primitive.

The principal finding is that the small high-energy component of an actual
birth is controlled by the marked A center, not by the number of all available
outward hops. For the cube its probability is of order epsilon^2 and its energy
is of order epsilon^-4. It contributes order epsilon^-2 to the mean and order
epsilon^-6 to the variance. Flux proportional to S also gives an order
epsilon^-2 low-band mean. A degree-two ring removes the first high-band
coefficient, but does not universally remove microscopic variance: a six-cycle
has a smaller epsilon^-2 variance divergence, while a four-cycle's terminal
output has exactly zero energy and variance.

## 1. Model, domain and source boundary

Let G be a fixed finite simple bipartite graph, with hard-core charges
q_x in {0,+1,-1}, integer S>=1 on every link, and div E=q-1_A. Edges are
oriented from their smaller to larger numbered endpoint. Write C=S(S+1),
P=1_(W=0), W=sum_(a in A)(1-n_a), and F_a for the unsigned legal outward
hop sum from a to vacant B neighbors. An allowed shift k=+/-1 has amplitude

    sqrt(1-E_e(E_e+k)/C).

The shift is k=-q_a when a is the lower endpoint, and +q_a otherwise. At a
forbidden spin boundary its amplitude is zero. The hopping is
T=-sum_a(F_a+F_a*). The compensation is exactly

    C_S=sum_a [F_a*F_a-D_(a,S)+D_(a,infinity)] Q_a,
    Q_a=product_(c in A, c!=a, distance(c,a)<=2) n_c.

The microscopic Hamiltonian and original jumps are

    H=delta epsilon^-4 (W+epsilon T+epsilon^2 C_S),
    L_j=sqrt(kappa) epsilon^-1 j_S,                       (1)

with delta,K,kappa>0 fixed and epsilon^2 C=delta/K in the joint limit.
The sigma=+/- resolved mark below means charge sigma at the A endpoint;
the coherent edge mark is the sum of those two original j operators.
There is no projection or filter in the applied formation instrument.

The permitted compensation source establishes the uniform fixed-graph operator
bounds and the canonical low-band expansion. Its accompanying correction is
included: only the two effective Hamiltonian coefficients, not every displayed
operator, are asserted self-adjoint. The electric-completion note and its scope
correction were read as context; its additional lambda R_S interaction is not
adopted here. This note uses lambda=0, the originally supplied C_S above.
The high-flux source supplies only the graph/circulation convention. None of
its effective-target energy moments is used as a microscopic moment theorem.

`SOURCE_BINDINGS.json` records the exact allowed originals and local copies.
The local-primitive reference is
`local_compensation_independent/model.py`, SHA256
`686529f4cd3dd5d73e3373f2604e56615c83228b5813a3848f2a194db00ae128`.
The principal compensation note is
`42ec5430a0f49c9b6e70577be601df72e23d881b7ef152186de2cdb1ff3faba4`;
the canonical-target note is
`9bc691a07fd70c1a813852aa0cac55832065b3c95cf3d50e5528845f6613e0b0`.
No campaign builder is imported by the new path or complete-matrix engines.

## 2. Canonical dressing and the first energy leakage

Put A=Pi_1 T P, M=A*A, Z=Pi_2 T Pi_1 A. Let U(epsilon) be the positive-overlap
all-cluster rotation in the permitted target theorem. For a normalized input
x in P, the preparation in this question is d=U x, not the bare x. In the
initial and final record-number sectors use the corresponding blocks of U.

The graph of the low spectral subspace is X=epsilon X1+epsilon^2 X2+... with
X1=-A and X2=Z/2. Its canonical isometry is
(P+X)(I+X*X)^(-1/2), hence

    U P=P-epsilon A+epsilon^2(Z/2-M/2)+O(epsilon^3).      (2)

Since jP=0 and [W,j]=-j, expansion of the actual rotated jump gives

    U_post* j U_pre P
      =epsilon B+epsilon^2 R+O(epsilon^3),
    B=-j A,
    R=(1/2)j Z+A_post B,       Pi_1 R=R.                 (3)

The sign of the second term is fixed by U_post* Pi_0 to Pi_1 having derivative
+A_post. Omitting this final rotation gives jZ/2, which is not the energy-band
leakage of the actual output.

On P put F=sum_a F_a. Then A=-F P and Z=F^2 P. For a mark on edge (a,b),
jF P=jF_a P because only the hop that vacates a can enable j. Two outward
hops from distinct A centers commute on P: when they target the same empty B
site both orders vanish, and otherwise they act on distinct links and allowed
sites. A hop at a different center c survives the subsequent birth exactly
when it survives after the birth. In either order it must avoid the newborn
B site and the first old record's destination. The link factors commute too.
Consequently, including finite-spin weights and boundaries,

    (1/2)jF^2 P=sum_(c!=a) F_c B,
    R=-F_a B.                                           (4)

This is an operator identity on P, so it applies by linearity to superpositions.
The following explicit numerical coefficients specialize it to the all-A-plus,
B-empty basis input. F_a B is an operator path in the energy calculation; it
is not an additional recorded hop or a second birth inserted into the process.

Let w=||Bx||^2>0, beta=Bx/sqrt(w), ell=||Rx||^2/w. All normalized uniform
estimates below require w bounded away from zero along the sequence considered.
The parity Xi=(-1)^W makes each cluster block of U*hU even in epsilon and
gives alternating grades in the jump expansion. Therefore

    birth intensity =kappa w+O(kappa epsilon^2),
    probability in energy cluster near W=1
                       =epsilon^2 ell+O(epsilon^4),
    probability in clusters W>=2=O(epsilon^4).            (5)

The low-cluster output vector in canonical coordinates, normalized only for
this bookkeeping decomposition, is beta+O(epsilon^2). No such normalization
or energy measurement is performed by the original instrument.

On a rotor basis input with all A charges plus and B vacant, let z be the
degree of the marked A site. For z>=2, B has z-1 old-record destinations.
For a plus mark, two ordered choices of distinct remaining destinations give
the same final two-plus state in F_a B. Thus its squared norm is
4 choose(z-1,2), while w=z-1. For a minus mark those destinations are
distinguished by the negative charge, giving squared norm (z-1)(z-2).
The two orientations of a coherent edge mark remain orthogonal at B's and
R's fixed newborn B charge. Hence

    ell_plus=2(z-2),  ell_minus=z-2,
    ell_coherent=(3/2)(z-2).                             (6)

For degree one the leading birth itself vanishes; it is not a normalized
case of (6). Degree two is a genuine vanishing-leakage case, discussed below.

## 3. Uniform microscopic moment accounting

On P the compensation identity gives

    Delta_S=C_0-M=D/C,
    H_low=delta epsilon^-2 Delta_S+delta H4_S+O(delta epsilon^2),
    H4_S=M^2-{M,C_0}/2+A*C_1 A-Z*Z/2.                  (7)

All coefficient and remainder bounds in the dimensionless cluster expansion
are uniform in S at fixed graph. In particular Delta_S and H4_S are uniformly
bounded. In a cluster near W=r>=1 the energy is
delta epsilon^-4[r I+O(epsilon^2)]. Denote
mu_S=<beta,Delta_S beta> and v_S=Var_beta(Delta_S). Direct substitution of
(3)-(7), before taking any density limit, gives

    <H>_after =delta epsilon^-2(ell+mu_S)+O(delta),
    <H^2>_after=delta^2 epsilon^-6 ell+O(delta^2 epsilon^-4),
    Var_after(H)=delta^2 epsilon^-6 ell+O(delta^2 epsilon^-4). (8)

The low-band component separately has mean
delta epsilon^-2 mu_S+O(delta) and variance
delta^2 epsilon^-4 v_S+O(delta^2 epsilon^-2). The latter is not automatically
the coefficient of epsilon^-4 in the full variance: corrections to the small
high-band component and subtraction of the full mean squared also contribute.

For an initial charge/field basis state x, Delta_S x=d_S x exactly. Thus

    <H>_before=delta epsilon^-2 d_S+delta<x,H4_S x>+O(delta epsilon^2),
    Var_before(H)=delta^2 Var_x(H4_S)+O(delta^2 epsilon^2). (9)

In particular a large initial low-band mean need not imply a large initial
variance. The scalar Delta_S eigenvalue cancels exactly when computing the
variance of H_low x.

These formulas require the canonically dressed input. The bare all-A-plus,
B-empty basis state has exactly zero initial formation intensity because
jP=0. If m is the number of graph edges and E2=sum_e E_e^2, its energy and
variance instead are exactly

    <H>_bare=m delta epsilon^-2,
    Var_bare(H)=delta^2 epsilon^-6(m-E2/C).              (10)

Here C_0 x=m x and ||T x||^2=m-E2/C; the linear electric terms cancel by
div E=0. Its initial dissipative energy derivative is zero. These are different
preparations and cannot be substituted in (8).

For the full initial GKLS derivative, the Hamiltonian part leaves its own
energy expectation constant. Recycling and the anticommutator give, on a
dressed basis input,

    d<H>/dt at0=(kappa delta/epsilon^2)
      sum_j [||R_j x||^2+<B_j x,Delta_post B_j x>-w_j d_S]
      +O(kappa delta).                                 (11)

For a general x, replace w_j d_S by
Re<B_j*B_j x,Delta_pre x>. This retains the leading loss contribution; it is
not the sum of conditional output energies alone. Similarly,

    d Var(H)/dt at0=(kappa delta^2/epsilon^6)
                         sum_j ||R_j x||^2
                         +O(kappa delta^2 epsilon^-4).  (12)

The initial H^2 loss and the subtraction 2<H>d<H>/dt are of order epsilon^-4,
so they do not remove the displayed fast contribution. Statements (8),
(11), and (12) are meaningful with zero leading coefficient too, but their
remainders then do not identify the first nonzero term.

## 4. Cube at fixed circulation: complete leading and finite-part results

Use vertices 0,...,7, A={0,3,5,6}, and edges at binary Hamming distance one.
Let x=Omega_n have all A charges plus, B empty, and

    E01=n, E13=n, E23=-n, E02=-n,

with all other edges zero. This is a normalizable physical field basis state.
The selected edge is (0,1), with birth charge sigma at 0. Keep n fixed while
epsilon^2 C=delta/K and S tends to infinity.

The fixed-field leading coefficients are w_plus=w_minus=2,
w_coherent=4 and ell_plus=2, ell_minus=1, ell_coherent=3/2. In particular,
the leading variance is not the effective electric variance K^2 n^4.
The actual conditional microscopic moments have the sharper expansions

| Mark | Full microscopic mean | Full microscopic variance |
|---|---|---|
| plus | 2delta/epsilon^2-K n-18delta+O(epsilon^2) | 2delta^2/epsilon^6-[delta K n(n+1)+2delta^2]/epsilon^4+O(epsilon^-2) |
| minus | delta/epsilon^2+(K/2)n(n-1)-13delta+O(epsilon^2) | delta^2/epsilon^6-[delta K n(n-1)/2]/epsilon^4+O(epsilon^-2) |
| coherent | 3delta/(2epsilon^2)+K(n^2-5n)/4-31delta/2+O(epsilon^2) | 3delta^2/(2epsilon^6)-[3delta K n(n+1)/4+3delta^2/4]/epsilon^4+O(epsilon^-2) |

Constants in these fixed-n remainders may depend on n, delta and K. These are
not uniform formulas for n proportional to S. The initial dressed cube has

    <H>_before=4K n^2-84delta+O(epsilon^2),
    Var_before(H)=48delta^2+O(epsilon^2).               (13)

The negative bounded term illustrates that this many-center H is not asserted
nonnegative; the one-center star's exact positivity factorization cannot be
transferred to it.

For comparison, the low-band component of the actual marked output tends in
its first two energy moments to the specified target h=KD+delta H4_infinity.
Direct four-hop path reconstruction gives the following limiting moments:

| Mark | Low-band mean limit | Low-band variance limit |
|---|---|---|
| plus | K n^2-20delta | K^2 n^4+392delta^2 |
| minus | K n(n-1)-14delta | K^2 n^2(n-1)^2+296delta^2 |
| coherent | K(n^2-n/2)-17delta | K^2(n^4-n^3+3n^2/4)+353delta^2-3Kdelta n |

This decomposition explains why even the finite part of the full microscopic
mean need not equal the target mean. There is no microscopic equality obtained
by simply adding a universal epsilon^-2 term to the target expectation.

On this cube C_1=0 on both record sectors. At rotor order H4=-Z*Z/2.
For the initial field basis state, its diagonal coefficient is -84 and its
twelve single-face neighbors have coefficient -2, giving variance48.
For the plus/minus outputs direct local path products give respectively
(mean H4, Var H4)=(-20,392),(-14,296); their D-H4 covariance is zero.
For the coherent output the two equally weighted charge orientations have
mean H4=-17 and variance353. Their branch covariance is -3n/2, giving the
last term in the coherent variance table. These are physical flux paths,
not flat Fourier vectors.

The low-band moment convergence just used follows from the canonical operator
expansion, not the density theorem. Its normalized vector is
beta_S+epsilon^2 b_(2,S)+O(epsilon^4). The coefficients beta_S and b_(2,S)
have uniformly finite field support for fixed n. Therefore applying
delta epsilon^-2 Delta_S=KD to these terms is controlled on that support;
the remainder, even using ||H_low||=O(epsilon^-2), tends to zero after applying
H_low. Together with H4_S's finite-product limit this proves convergence of
the energy-vector norm and hence of both low-band moments.

### Derivation of the finite parts

The additional coefficients can be audited without numerical extrapolation.
At rotor order on this cube write F=sum_a F_a, G=F*, M=GF, Z=F^2. On input x
the canonical column has grade-one and grade-three epsilon^3 coefficients

    V31=(1/2)G F^2 x-(1/2)F M x,
    V33=(1/6)F^3 x,

and grade-two epsilon^4 coefficient

    V42=(1/4)F G F^2 x+(1/12)G F^3 x-(1/4)F^2 M x.     (14)

These follow by matching the graph invariance equation degree by degree and
then multiplying by (I+X*X)^(-1/2). In particular the final terms in (14)
come from canonical normalization.

Put B=jFx, Y=jF^2x/2, V0=jV31, V2=jV33, Y4=jV42, R=Y-FB. Let

    nu=||Y||^2+2Re<B,V0>,
    N6=2Re<R,Y4-FV0>+2||V2||^2-2Re<FY,V2>,
    U0=-G R, U2=2V2-FY, Q4=Y4-FV0-GV2.                (15)

Expanding <jUx,h jUx> through epsilon^6 and ||h jUx||^2 through epsilon^6
gives the rotor finite mean coefficient and second-moment coefficient

    b=N6/w-ell nu/w,
    c2=(||U0||^2+||U2||^2+2Re<R,Q4>-ell nu)/w.         (16)

The variance coefficient is c2-ell^2. The exact physical path sums are

| Mark | w | nu | N6 | b | c2 | c2-ell^2 |
|---|---:|---:|---:|---:|---:|---:|
| plus | 2 | 14 | -8 | -18 | 2 | -2 |
| minus | 2 | 14 | -12 | -13 | 1 | 0 |
| coherent | 4 | 28 | -20 | -31/2 | 3/2 | -3/4 |

`CUBE_SUBLEADING_RESULTS_01.json` contains the complete finite physical vectors
in (15), not just the summary constants. The same formulas after Fourier
projection match direct complete-matrix canonical calculations; the differing
fiber constants are retained and are not substituted for this table.

For finite S set a=1-n(n+1)/C, b_s=1-n(n-1)/C. Direct application of the
spin shifts gives, exactly,

    w_+=a(1+a),     ell_+=4a/(1+a),
    w_-=b_s(1+a),   ell_-=(a+b_s)/(1+a),
    w_coh=(a+b_s)(1+a),
    ell_coh=[4a^2+b_s(a+b_s)]/[(a+b_s)(1+a)].            (17)

The two old destinations are 2 and4. Their D values are 0 and2n^2 for the
plus mark, 0 and2n(n-1) for the minus mark. Their relative weights within
either orientation are a:1. Thus

    mu_+=2n^2/[C(1+a)],
    mu_-=2n(n-1)/[C(1+a)],
    mu_coh=[2a n^2+2b_s n(n-1)]/[C(a+b_s)(1+a)].        (18)

Expand (17)-(18) in 1/C=K epsilon^2/delta. The order-1/C coefficients in
ell+mu are -n, n(n-1)/2, (n^2-5n)/4. Those in ell are -n(n+1),
-n(n-1)/2, -3n(n+1)/4. Combining these with (16) gives both full microscopic
tables above. The required next canonical coefficients are bounded uniformly
in S, and their fixed-support spin limits are the rotor coefficients, which
controls the displayed remainders.

Summing all original marks yields, for either instrument and fixed n,

    total intensity=48kappa+O(epsilon^2),
    d<H>/dt at0=72kappa delta/epsilon^2+O(1),
    d Var(H)/dt at0=72kappa delta^2/epsilon^6+O(epsilon^-4). (19)

The exact rotor path sums behind (19) are sum w_j=48,
sum ||R_j x||^2=72, and sum <B_jx,D B_jx>=96n^2. Thus an effective target
energy drift of order one does not determine the actual microscopic drift.

## 5. Flux of order S: a different joint limit

Now let n=n(S) be integral with n/S->alpha, |alpha|<1, and put u=1-alpha^2>0.
The finite shift amplitudes on the selected high-flux face approach sqrt(u),
not one. Equations (17)-(18), with the uniform expansion (8), imply

| Mark | Intensity limit divided by kappa | ell limit | Slow mean coefficient mu | Full mean coefficient |
|---|---:|---:|---:|---:|
| plus | u(1+u) | 4u/(1+u) | 2(1-u)/(1+u) | 2 |
| minus | u(1+u) | 2u/(1+u) | 2(1-u)/(1+u) | 2/(1+u) |
| coherent | 2u(1+u) | 3u/(1+u) | 2(1-u)/(1+u) | (2+u)/(1+u) |

The full mean column is lim epsilon^2 <H>_after/delta. The variance statement
is lim epsilon^6 Var_after(H)/delta^2=ell from the same row. The initial
scaled mean tends to 4(1-u)=4alpha^2 and its variance remains O(delta^2).
For example the selected plus mean change has coefficient

    lim (epsilon^2/delta)(<H>_after-<H>_before)
                         =2-4alpha^2.                  (20)

It is negative when alpha^2>1/2. An individual original birth therefore need
not increase microscopic energy from its already energetic dressed input.
This does not identify heat or a reservoir transfer.

In all three rows the low-band scaled variance tends to

    lim epsilon^4 Var_low(H)/delta^2
                          =4u(1-u)^2/(1+u)^2.           (21)

It is smaller in order than the full epsilon^-6 variance for fixed interior u.
Equation (21) describes the low-band bookkeeping component only. No full
epsilon^-4 variance coefficient is claimed from it for this moving input.

The all-mark sums can also be evaluated without fitting. The two A centers
on the circulated face have outgoing squared weights (u,u,1); the two other
A centers have (1,1,1). Each degree-three center contributes 18 times the
product of these three weights to sum ||R_j x||^2. Consequently

    lim total intensity/kappa=8(u^2+2u+3),
    lim sum_j ||R_j x||^2=36(1+u^2).                    (22)

Each occupied high-face B site removes two active face links from Delta.
Counting the two birth signs and the two orders of the old/new destinations
gives weighted occupancy count16(u^2+u+1). The leading slow energy change
sum in (11) is therefore -32(1-u)(u^2+u+1)=-32(1-u^3). Thus

    lim [epsilon^2/(kappa delta)] d<H>/dt at0
                           =4+36u^2+32u^3,
    lim [epsilon^6/(kappa delta^2)] d Var(H)/dt at0
                           =36(1+u^2).                 (23)

The leading total energy drift in this cube family is positive even when the
selected plus energy change in (20) is negative. Original resolved and coherent
instruments have the same displayed leading sums, not necessarily identical
finite-epsilon higher moments or later histories.

These are scaled limits; replacing the exact finite-S coefficients by their
limits inside an O(1) remainder would be invalid without a convergence rate
for n/S. At n=S the selected plus leading norm a(1+a) is zero. The normalized
uniform expansion used here does not cover such vanishing-rate boundary marks.
No boundary conditional conclusion is inferred by setting u=0 in the table.

The moving flux basis states have no trace-norm convergent normalizable rotor
input when |n| grows without bound. They are outside the fixed-input common
density theorem. Even sublinear but unbounded n is not a fixed rotor input;
the exact finite-S coefficient formulas, rather than a uniform fixed-n target
claim, are the appropriate account.

## 6. Degree-two controls and a smaller variance divergence

For every degree-two marked center, both neighboring B sites are occupied
after its leading birth. Hence F_a B=0, and (4) gives R=0 exactly, including
spin weights. A positive universal coefficient in (8) is false on this class.

On the four-cycle with two A sites, a first birth raises N from2 to4. Every
site is then occupied throughout the entire output sector, so W=T=C_S=0
there. Every nonzero exact microscopic first output, dressed or otherwise,
has exactly

    <H>_after=Var_after(H)=0.                           (24)

The original marks have nonzero leading rates on interior field inputs.
This is a concrete actual-birth counterexample, not an inaccessible terminal
sector. At flux n/S->alpha its initial dressed scaled energy tends to4alpha^2,
so the corresponding scaled mean change is -4alpha^2.

The six-cycle has three A sites. Its first birth produces N=5, not full
occupation. It is also the parity example where a fully occupied N=6 sector
cannot have total charge3. Vanishing R therefore does not permit the
four-cycle argument. Here the postbirth sector has only W=0,1 and C_1=0.

For a zero-field initial basis state and the plus mark on (0,1), write F,G,M
as above on the prebirth sector and Delta=D/C. The graph recurrence gives

    X31=(1/2)G F^2 x+F Delta x,       X33=(1/6)F^3 x,
    X42=(1/2)F X31+(1/2)G X33+(1/4)F^2 Delta x,
    V31=X31-(1/2)FMx,   V42=X42-(1/4)F^2Mx.             (25)

In the postbirth W=0,1 sector the low graph has
X_post=epsilon F_post+epsilon^3 F_post Delta_post+O(epsilon^5).
Subtracting this graph from the jumped vector yields the first nonzero
high-coordinate amplitude, epsilon^4 G4, where

    G4=jV42-F_post jV31-F_post Delta_post B.             (26)

The leading jump norm is epsilon sqrt(w), with w=1 here. The additional
orthogonal graph normalization changes (26) only at higher order. Thus the
actual normalized high-band probability is
epsilon^6 ||G4||^2+O(epsilon^8).

For the six-cycle edges ordered
(01,05,12,23,34,45), (26) has exactly the following physical basis support:

| Charge word q | Field word E | Amplitude |
|---|---|---:|
| (0,-1,1,1,1,1) | (0,-1,-1,-1,0,0) | -1 |
| (0,-1,1,1,1,1) | (1,-2,0,0,1,1) | -sqrt(1-2/C) |

The second state is absent at S=1, where its coefficient is zero. These are
distinct flux states with the same charges, not a single coherently identified
state. The table gives the exact finite-spin coefficient
||G4||^2=2-2/C. It was reconstructed with the symbolic substitution
C=2/(1-t^2), 0<=t<1, and also checked against complete finite-spin Gauss
matrices. Therefore at the stipulated joint limit

    Var_after(H)~2delta^2/epsilon^2.                    (27)

The mean in this example obeys <H>_after~2delta epsilon^2 and tends to zero.
To see the mean coefficient, the high band contributes
delta epsilon^2(2-2/C)+O(epsilon^4). The low-band component has zero D on
its leading B vector and zero rotor H4 on this postbirth sector. Its canonical
correction is O(epsilon^2) with finite field support. Since the finite-S low
Hamiltonian's remaining coefficients are O(1/C) on that support, its energy
expectation is O(epsilon^4) in the joint limit. The same support estimate
keeps its variance negligible relative to (27).

This example disproves the inference that R=0 or convergence of the mean
implies convergence of the energy variance. It does not state that every
degree-two graph has the coefficient in (27). Exact paths also check R=0 on
the eight-cycle; no next nonzero coefficient is claimed there.

## 7. Evidence, representation limits and preserved development

The new path engine is independently written from the stated charge/link
actions. It keeps complete charge and integer-field tuples and sums amplitudes
only when both tuples agree. It checks Gauss after the relevant operations.
The complete-matrix engine separately assembles site transitions, compensation
and original jumps. It enumerates the entire finite-spin physical Gauss sectors
of the four- and six-cycles, constructs the low Riesz subspace spectrally, and
uses its positive-overlap polar isometry. The cube controls use all70 initial
charge states and all168 postbirth charge states in specified rotor Fourier
fibers, including their complete 36-dimensional postbirth P sector.

| Control | Completed coverage |
|---|---|
| PATH_RESULTS_01 | 375 exact checks: local cancellation, finite-spin formulas, all original marks, macroscopic-flux polynomials, slow-band moments and degree-two examples |
| MATRIX_RESULTS_01 | 201 complete-matrix checks: canonical projection/isometry and cluster separation, all three cube mark types at two fibers, complete physical four/six-cycle sectors |
| RING_HIGHER_RESULTS_01 | 22 exact recurrence, Gauss-support, symbolic-C and independent-matrix comparisons |
| FROZEN_CUBE_RESULTS_01 | 58 checks plus60 matrix-support checks: full weighted charge operators, conditional moments and complete GKLS energy/variance derivatives at three interior flux weights |
| CUBE_SUBLEADING_RESULTS_01 | 25 checks plus recorded matrix-support checks: physical finite parts, full path certificates, exact fixed-n spin expansions and independent full-matrix contrasts |

Counts include routine consistency checks; they do not establish independence
by quantity. Analytic operator expansion and exact finite path identities prove
the asymptotics. Floating complete-matrix cases corroborate the canonical
convention and scaling; they are not proofs by extrapolation. The largest
complete physical ring matrices in the principal run have dimensions158 and219.
No complete finite-spin cube diagonalization is claimed.

The weighted cube matrices use face-edge amplitude sqrt(u), other-edge
amplitude1, and the corresponding full compensation diagonal. They are Fourier
fibers of the locally translated moving-flux limit, not the complete finite-S
cube. Their role is to check the independent path coefficient and GKLS algebra.
For example at u=1/4, epsilon=.005, the complete matrix gives scaled mean
1.99938 for the selected plus output against limit2, and scaled total energy
derivative6.79635 against limit6.75. The principal proof uses the exact
finite-S formulas and uniform cluster expansion, not this finite tolerance.

A diagnostic on the six-cycle found coefficient4 in the zero Fourier fiber
where the normalizable zero-field input gives coefficient2 in (27). This is
the constructive interference of the two distinct flux states in the table.
It is preserved as a representation/scope warning. The cube finite-part
coefficients likewise depend on the Fourier fiber; the physical coefficients
were not replaced by those easier matrix values. The direct Fourier projection
of each physical path vector reproduces the matching matrix values exactly
at coefficient level, with finite-epsilon differences tending to zero.

No scientific control execution failed in this bounded reconstruction. A
packaging patch was rejected before writing and retried; its operational
failure is recorded in DEVELOPMENT_RECORD.md. The initial
matrix runner and its results remain fixed as `matrix_control_run01.py` after
the current engine gained optional edge weights for the moving-flux control.
Exploratory ring and cube finite-part diagnostic logs are retained. Their
formulas and stronger reproducible versions are in the final control sources.
The source correction and failures in earlier allowed packets remain in those
unchanged packets; none is overwritten here.

Reproduce with fresh attempt names from this directory:

    python3 path_control.py --attempt reproduction
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 matrix_control_run01.py --attempt reproduction
    python3 ring_higher_order.py --attempt reproduction
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 frozen_cube_control.py --attempt reproduction
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 cube_subleading_control.py --attempt reproduction

Existing result files are never overwritten by these runners. The ring
higher-order runner compares to the frozen MATRIX_RESULTS_01. Each result
records its executed source hash; source bindings and the PRE seal authenticate
the complete packet and its declared comparison inputs.

## 8. What density convergence does and does not establish

For a fixed physical input the microscopic conditional output can approach its
low-band density while its high-band probability tends to zero. The energy
operator itself scales with epsilon. The cube's order-epsilon^2 fast probability
therefore carries divergent mean and variance; the six-cycle's smaller
order-epsilon^6 probability carries vanishing mean but divergent variance.
Trace-norm density convergence alone controls neither example's unbounded
microscopic moments. Our moment statements were derived before taking the
density limit, with explicit coefficient and domain estimates.

Nothing here supplies a reservoir, an energy-conserving formation mechanism,
heat interpretation, arbitrary-time autonomous model, native selection,
thermodynamic or growing-volume limit. A positive total drift is not a
universal per-event energy cost, and the four-cycle is an exact counterexample
to universal positive output energy. The selected high-flux cube event can
decrease energy from the dressed input. Each scope restriction is part of the
mathematical statement, not a conjectured external implementation.

All writing is confined to `general_microscopic_birth_energy_independent`.
No editable prompt, author source, original instrument, current-main science,
commit, publication or audit status was changed. The fixed campaign deadline
remains 2026-09-24 04:59:48 UTC. This PRE is to be sealed before requesting the
withheld author packet; later comparison belongs in new files.
