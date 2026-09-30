# A rare-hole global source moment and fast-current tails

Status: provisional analytic exact support, pending focused independent check.
This is not a formal review, an audit verdict or a complete microscopic limit.

For the actual supplied finite-spin microscopic law from BARE Omega, the
previous global exponential count bound can be strengthened by an explicit
rare-hole factor. This closes the tilted-hole obligation that was left open
in the earlier cluster route, with an explicit polynomial volume price.
Its new uses are instantaneous original activity weighted by global record
count and fast magnetic-current tails with the required epsilon^2 hole factor.
An integrated late-record consequence is also stated, but is already available
from the previous global count bound and is not claimed as new progress.
Positive-time local cluster uniform integrability remains open.

## 1. Model, target and source binding

Main was fetched and remains30a9461ee19a49b99fa6628fe942f08e504e8903.
Selected procedure7146fe17a76de41badcaca3c3c7cac6d11eb2a00 is unchanged.
CONTRACT and PRE_FREEZE precede the completed proof and control. This route
fully reread GLOBAL_MOMENT_LEMMA, INITIAL_CLUSTER_SEED, LOCAL_TILT_ATTEMPT,
the prior cluster REPORT and APPROACH_REGISTRY, both corresponding focused
receipts, and the original DEFECT_LEMMA. Exact hashes are in SOURCE_IDENTITIES.
The actual main microscopic and primitive sources were fully read earlier in
this continuous campaign; unchanged current-main bodies are bound separately
in MAIN_INPUT_IDENTITIES.json. No source definition is replaced by a title, proxy process or scalar
stress model. Refreshed relevant open heads are unchanged: PR9399 at5bec44a
supplies an effective thermodynamic argument and excludes microscopic
elimination; PR9400 atb0d159b is the bounded finite-ring numerical proposal.
Previously read actual source sections are specified in PRIOR_REFRESH; no
unread part of either proposal is imported.

On a degree-six even cubic torus with the source's finite simple graph
convention (e.g. even side L>=4), put n=|A|, W=sum_A(1-n_a), NB=sum_B n_b, and

    Kd=W+NB=N-n+2W.

The actual finite-spin microscopic law is

    H=delta epsilon^-4(W+epsilon T+epsilon^2 C_S),
    L_mu=sqrt(kappa) epsilon^-1 j_mu,   T=-F-F*,

with the complete gated compensation, normalized spin shifts and Gauss law.
Either original resolved-sign instrument or original coherent edge instrument
is used, separately. Their marks are never split into W-grade channels.
The actual initial state is Omega: occupied plus A, vacant B, zero links,
zero record register. On each actual record-number block,

    N=n+2R,   Kd=2R+2W,                              (1)

where R is the total number of ORIGINAL births. Hamiltonian evolution preserves
N and each original mark raises it by two, including every later birth.

For every fixed theta,delta,kappa>0 there are epsilon_theta>0 and finite
C_theta, independent of spin and volume, such that

    Tr[W exp(theta Kd) rho_micro(t)]
       <=C_theta epsilon^2 (n+n^2 t)
                    exp[C_theta n(t+epsilon^2)], t>=0. (2)

The constants are not practical resource bounds; they may depend strongly
on theta and the fixed normal-form order. The joint scaling

    epsilon^2 S(S+1)=delta/K

may be imposed afterward. No mean-energy cap or electric moment is assumed.
Only finite-spin microscopic generators are asserted. No rotor-generator
extension is made by this theorem.

The carrier, dynamics, compensation, initial state and clock remain supplied
hypotheses. This theorem does not derive them from M2 or a registered primitive.

## 2. Checked input frame and positive count similarity

The checked global moment proof constructs an EXACT finite-depth unitary
V_epsilon, combining a Hamiltonian normal form with the order-epsilon^3
loss-canceling unitary. Every gate has fixed support and uniformly bounded
analytic coefficients; its leading deviation from identity is O(epsilon).
It preserves Gauss and N. In this frame,

    H_V=delta epsilon^-4 W+delta epsilon^-2 D2
                                  +O_local(epsilon^-1),
    [D2,W]=[D2,N]=0,
    J_mu=V j_mu V*=j_mu+epsilon j1_mu+O_local(epsilon^2).
                                                               (3)

The first jump correction has W grades0,-2, so positive jump grades begin at
order epsilon^2. The order-epsilon^-1 Hamiltonian is retained. It is the
necessary loss-canceling coefficient, not an error discarded by this proof.

Set Q=exp(theta Kd) and sigma=V rho V*. The EXACT positive operator

    tau=Q^(1/2) sigma Q^(1/2)

has a completely positive, generally non-trace-preserving evolution. Write
its generator as

    dot tau=A tau+tau A*+sum_mu L_mu tau L_mu*,
    A=Q^(1/2)(-i H_V-kappa epsilon^-2 sum J_mu*J_mu/2)Q^(-1/2),
    L_mu=sqrt(kappa) epsilon^-1 Q^(1/2)J_mu Q^(-1/2).
                                                               (4)

Define Hermitian H_theta and B_theta by

    H_theta=(A*-A)/(2i),
    B_theta=A+A*+sum_mu L_mu*L_mu.

Then (4) is precisely

    dot tau=-i[H_theta,tau]+sum D[L_mu]tau
                                  +{B_theta,tau}/2.             (5)

B_theta is a potential controlling trace growth; it is not a new observed
jump or a physical loss law. The checked global proof gives the TERMwise
local-strength estimate

    B_theta=Q^(-1/2)(L_V* Q)Q^(-1/2)=O_local(1).       (6)

The equality includes gain and both anticommutator terms. Its cancellation
uses D_cross* f(Kd)=[f,X]/2 and the actual Hamiltonian correction with the
opposite sign. In particular, (6) is stronger information than a bare bound
on Tr tau(t): its coefficients are finite-range analytic local interactions.

Bare j commutes with Kd, and D2 commutes with Kd. Thus

    H_theta=delta epsilon^-4 W+delta epsilon^-2 D2
                                     +O_local(epsilon^-1),
    L_mu=sqrt(kappa) epsilon^-1 ell_mu,
    ell_mu=j_mu+epsilon ell1_mu+O_local(epsilon^2),    (7)

where ell1_mu again has grades0,-2. Conjugation by Q is local on every local
term: all remote onsite count factors cancel, and its local norm costs only
exp(theta times the bounded local count capacity). No electric dimension or
volume factor enters a local coefficient. Since all Hamiltonian/potential
terms preserve N, their Q conjugation depends only on their W grade; for a
jump of W grade r and N grade2 it contributes exp(theta(r+1)). This also
checks the unchanged bare grade r=-1 in (7).

## 3. The new step: local positive congruence removes off-grade potential

A merely trace-growing tilted evolution is insufficient for a rare-hole
estimate: the off-grade part of B_theta can couple W=0 to W>0. The remedy
here is a finite local invertible congruence, with an explicit endpoint cost.
It does not claim that the tilted dynamics is trace preserving.

For an integer-grade operator use

    P_W A=(2pi)^-1 integral e^(isW) A e^(-isW) ds,
    I_W A=sum_(r!=0) A_r/r,
    [W,I_W A]=A-P_W A,   ||I_W||<=pi/2.              (8)

Onsite conjugation leaves support unchanged. I_W sends Hermitian off-grade
operators to anti-Hermitian operators. Its bound and locality are the same
ones used in the checked normal form.

First apply a finite-color UNITARY normal form to H_theta at orders
 epsilon^3, epsilon^4, epsilon^5, epsilon^6. For an off-grade Hamiltonian
coefficient h at physical order epsilon^(p-4), use anti-Hermitian generator
I_W(h)/delta at gate order epsilon^p. The commutator with delta W cancels h.
Ordering corrections are retained at subsequent orders. After this step,

    H=delta epsilon^-4 W+H_diag+R_H,
    [H_diag,W]=0,  H_diag=O_local(epsilon^-2),
    R_H=O_local(epsilon^3).                            (9)

More specifically H_diag begins with delta epsilon^-2 D2 and may have
additional W-diagonal coefficients at orders-1,0,1,2. Their presence is
harmless. B remains O_local(1), and the leading two jump coefficients in (7)
are unchanged. No odd-order parity assumption is needed in this tilted frame.

Next use a POSITIVE congruence X=exp(eta D), D=D*, acting on states by
 tau -> X tau X. The exact new coefficients are

    A'=X A X^-1,   L_mu'=X L_mu X^-1.                  (10)

They give a CP evolution because this is similarity by an invertible
congruence of the original CP maps. It is generally not trace preserving.
Different positive gates need not commute; their fixed color ordering is
retained. At eta=0, the complete potential derivative is

    dB'/deta = -2i[D,H]+2 sum_mu D[L_mu]* D.            (11)

Indeed dA=[D,A], dL=[D,L], and differentiating A+A*+sum L*L gives
[D,A-A*]+2 sum L* D L-{sum L*L,D}; A-A*=-2iH.
The recycling contribution in (11) is essential.

Write B=B0+epsilon B1+O_local(epsilon^2). At order epsilon^4 choose

    D0=(i/(2delta)) I_W((1-P_W)B0),  D0=D0*.           (12)

The leading change in B from (11) is

    2i delta[W,D0]=-(1-P_W)B0.                        (13)

The dissipator contribution starts at epsilon^2, because its leading
strength is epsilon^-2. The next Hamiltonian coefficient is at epsilon^-2,
so it also first affects this potential change at epsilon^2. There is no
intermediate epsilon^-3 Hamiltonian coefficient. Hence the order-zero
potential becomes W-diagonal, without changing the order-one potential.
Repeat at gate order epsilon^5 with

    D1=(i/(2delta)) I_W((1-P_W)B1).

This makes B1 diagonal as well. A positive congruence at order epsilon^4
changes the Hermitian Hamiltonian first at physical order epsilon^2: its
leading commutator with -i delta epsilon^-4 W is Hermitian and therefore
belongs to the potential, whereas its commutator with the leading
Hermitian loss -sum L*L/2 contributes to H at order epsilon^2. Remove the
off-grade part of this induced coefficient by one more UNITARY gate layer
at order epsilon^6. Unitary conjugation only conjugates B, so this repair
does not undo (13) or its order-one counterpart.

Let Z be the total finite circuit of these unitary and positive gates, and
hat tau=Z tau Z*. We have proved, with exact finite-range remainders,

    dot hat tau=hat L(hat tau)+{B_d+R_B,hat tau}/2,
    hat L rho=-i[hat H,rho]+sum D[hat L_mu]rho,
    hat H=delta epsilon^-4 W+hat H_d+hat R_H,
    [hat H_d,W]=0,
    hat H_d=delta epsilon^-2 D2+O_local(epsilon^-1),
    hat R_H=O_local(epsilon^3),
    hat L_mu=sqrt(kappa) epsilon^-1 hat ell_mu,
    (hat ell_mu)_r=O_local(epsilon^2) for r>0,
    [B_d,W]=0, B_d=O_local(1), R_B=O_local(epsilon^2).
                                                               (14)

All grade decompositions in (14) are proof operations. No grade-resolved
instrument replaces the original marked maps.

Locality/uniformity details matter here. Every coefficient is a sum of
bounded-support interactions with bounded incidence. Disjoint commutators
vanish, and disjoint dissipator actions cancel between gain and loss in
(11). At any fixed order, grading, finite coloring and a finite product of
local exponentials leave bounded cones. Taylor remainder estimates are on
those cones, not on the full-volume operator norm. The number of colors,
cone cardinalities and local bounds are independent of n and S. Positive
congruence does not change this: similarity by a gate acts trivially on
operators disjoint from its support. Gauss and N are preserved throughout.
This is a finite-order exact change of coordinates, not an infinite normal
form or a spectral inverse on a volume-dependent gap.

Only the positive gates change the global norm of Z. Their orders are4 and5.
There are O(n) gates. For sufficiently small epsilon,

    ||Z||+||Z^-1||<=2 exp(c_theta n epsilon^4),
    ||Z^(-1)w_a Z-w_a||+||Z w_a Z^(-1)-w_a||
                                        <=c_theta epsilon^3.    (15)

The second estimate is a fixed-cone local estimate. It has no factor n.
The first is explicitly allowed to be extensive; it is never replaced by
||Z-I||=O(epsilon^3).

## 4. Defect correctors with the nonconservative volume price retained

The unital adjoint hat L* in (14) satisfies exactly the hypotheses of the
checked two-corrector calculation. To make the reuse explicit, let

    A_epsilon=kappa epsilon^-2 sum D[hat ell_mu]* W,
    R_epsilon=(1-P_W)A_epsilon,
    D_minus=kappa epsilon^-2 sum_(mu,r<0)
                               (-r)hat ell_(mu,r)*hat ell_(mu,r).

Then D_minus>=0, R_epsilon=O_local(epsilon^-1), and

    P_W A_epsilon=kappa epsilon^-2 sum_(mu,r)
                                         r hat ell_(mu,r)*hat ell_(mu,r).

Its positive-grade contribution is O_local(epsilon^2). Put

    Bcal=hat L*-i delta epsilon^-4[W,.],
    K1=(i epsilon^4/delta) I_W R_epsilon,
    K2=(i epsilon^4/delta) I_W((1-P_W)Bcal K1),
    Xcorr=W+K1+K2.                                    (16)

K1 and K2 are Hermitian local interaction sums of strengths O(epsilon^3)
and O(epsilon^5). The leading Bcal coefficient is

    epsilon^-2 (i delta[D2,.]+kappa sum D[j_mu]*),

which preserves W grade; its remainder has strength O(epsilon^-1).
Consequently the apparent O(epsilon) diagonal drift P_W Bcal K1 vanishes
at leading order, exactly as in the checked proof. The remaining terms give

    hat L* Xcorr+D_minus <=c_theta epsilon^2 n I,
    ||Xcorr-W||<=c_theta epsilon^3 n.                  (17)

This statement concerns the unital part of the tilted generator only.
The additional potential cannot be silently discarded. Denote
q=Tr hat tau, w=Tr(W hat tau), y=Tr(Xcorr hat tau). From (14),

    q'<=c_theta n q.

Because B_d commutes with W>=0,

    {B_d,W}/2=B_d W<=||B_d|| W<=c_theta n W.

For the remaining products use their actual extensive norms and W<=n I:

    ||{R_B,W}/2||<=c_theta epsilon^2 n^2,
    ||{B_d+R_B,Xcorr-W}/2||<=c_theta epsilon^3 n^2.

This is precisely where the n^2 price enters. No unsupported local action
bound is used for these disconnected products. Equations (17) therefore give

    y'<=c_theta n y+c_theta epsilon^2 n^2 q.           (18)

In passing from w to y, the extra c n||Xcorr-W|| is O(epsilon^3 n^2)
and is included. Choose the common trace/linear-growth coefficient BEFORE
replacing the nonnegative w by y, so that q'<=a n q and
y'<=a n y+b epsilon^2 n^2 q with the same a. Xcorr need not be positive;
scalar Gronwall applies to this signed y. At the initial endpoint use the
nonnegative upper bound y(0)<=w(0)+c epsilon^3 n q(0), and at the final
endpoint w<=y+c epsilon^3 n q. Only then enlarge positive constants to obtain

    q(t)<=e^(c_theta n t)q(0),
    w(t)<=e^(c_theta n t)
       [w(0)+c_theta epsilon^3 n q(0)
                              +c_theta epsilon^2 n^2 t q(0)].  (19)

D_minus was nonnegative and can be retained in an integrating-factor
version. It is not needed for (2), and no Gamma>=cW assumption enters.
In particular dark fast motion is not bounded by population through a
pointwise-loss substitution.

## 5. Bare preparation and exact physical endpoint conversion

The checked positive local-gate inequality supplies, for fixed theta,
a finite Theta(theta)>theta and constants a_theta such that

    V* Q_theta V <=exp(a_theta n epsilon^2)Q_Theta,
    V Q_theta V* <=exp(a_theta n epsilon^2)Q_Theta.      (20)

This holds on the complete finite carrier, then on Gauss restriction. It
uses a fixed extra-tilt gap, not electric moments or a global small V-I norm.
Since Kd Omega=0, (20) bounds the initial norm after the count similarity.

There is also the required rare-hole factor at this endpoint. Let
D_a=V* w_a V-w_a. It has bounded cone and ||D_a||<=c epsilon. Since
w_a Omega=0,

    ||Q_theta^(1/2) w_a V Omega||^2
       =||Q_theta^(1/2) V D_a Omega||^2
       <=exp(a_theta n epsilon^2)
                                      ||Q_Theta^(1/2)D_a Omega||^2
       <=c_theta epsilon^2 exp(a_theta n epsilon^2).    (21)

The final step uses the bounded count capacity of the support of D_a:
D_a Omega has zero Kd outside that cone. It does not assume factorization of
the evolved state. Summing over a proves an initial weighted W bound with
n rather than n^2. Applying Z then uses (15): w_a Z=Z(Z^-1 w_a Z), and
||u+v||^2<=2||u||^2+2||v||^2. Thus

    q(0)<=exp(c_theta n epsilon^2),
    w(0)<=c_theta epsilon^2 n exp(c_theta n epsilon^2). (22)

The inverse Z is handled identically at any time, using
w_a Z^-1=Z^-1(Z w_a Z^-1). Its local O(epsilon^3) difference produces
O(epsilon^6 n) times the weighted trace; its global norm cost is
exp(c_theta n epsilon^4). These fit inside the stated exponential. Hence
(19)-(22) prove the weighted W bound in the V frame.

For completeness the return to PHYSICAL W and Kd does not commute V past
the count weight without a price. For an arbitrary vector psi, write
E_a=V w_a V*-w_a, a fixed-cone O(epsilon) operator. The second inequality
in (20) and the local weighted norm of E_a give

    ||Q_theta^(1/2) w_a V* psi||^2
       =||Q_theta^(1/2) V* (w_a+E_a)psi||^2
       <=exp(a_theta n epsilon^2)
           [2||Q_Theta^(1/2)w_a psi||^2
                           +c_theta epsilon^2||Q_Theta^(1/2)psi||^2].

The local norm estimate here is
||Q_Theta^(1/2)E_a Q_Theta^(-1/2)||<=c_theta epsilon;
remote count factors cancel. After summing over a this proves the positive
operator inequality

    V(W Q_theta)V*
       <=exp(a_theta n epsilon^2)
                         [2W Q_Theta+c_theta epsilon^2 n Q_Theta]. (23)

Apply the already established V-frame bounds at Theta. The unweighted
Q_Theta moment is bounded either by (19),(15) or by the checked global
moment theorem. Enlarging constants in (23) proves (2). Only finitely many
tilt increments are used; epsilon_theta is their common volume-independent
smallness threshold.

## 6. Instantaneous original activity; integrated counts are older support

Identity (1) and positivity imply

    E[W e^(2theta R(t))]
       <=C_theta epsilon^2(n+n^2 t)
                              exp[C_theta n(t+epsilon^2)].      (24)

This is a joint moment of a quantum diagnostic W and the original classical
record count R, not a new measurement of W. The exact cq state remains block
diagonal in total N and original count R: H preserves N and each original
j raises N by two. V and every subsequent coordinate gate preserve N, but
(24) is a statement about the physical state after all endpoint conversions.

Let Gamma_a=kappa epsilon^-2 sum_(original marks at a) j_mu*j_mu.
The actual source inequality is Gamma_a<=12kappa epsilon^-2 w_a, for both
instruments with their spin weights. Translation invariance of the physical
law and bare Omega, with the translation-invariant TOTAL record count, gives

    E[e^(2theta R(t))Gamma_a(t)]
       <=(12kappa/(n epsilon^2))E[W e^(2theta R(t))]
       <=C_theta kappa(1+n t)exp[C_theta n(t+epsilon^2)]. (25)

Circuit colorings need not be translation invariant: (25) uses only the
physical final state, whose symmetry is exact.

For a fixed finite set F of A centers, let N_F count their original marks.
Take an integer threshold r>=0.
Use R(s-) in the predictable indicator below. The exact counting-intensity
identity, retaining every later mark, yields

    E integral_0^T 1_(R(s-)>=r) dN_F(s)
       <=C_theta kappa |F| integral_0^T
                   (1+n s)exp[C_theta n(s+epsilon^2)-2theta r] ds.
                                                               (26)

No conditional hazard or independent Poisson law is assumed. For r>=a n,
a>0 fixed, choose a common T>0 and epsilon0 so that
C_theta(T+epsilon0^2)<=a theta. Then uniformly in epsilon<=epsilon0,
spin and all t<=T,

    E integral_0^T 1_(R(s-)>=r) dN_F(s)
       <=C_theta kappa |F|(T+n T^2/2)exp(-a theta n).  (27)

This prices an ORIGINAL observed-history tail, but the integrated statement
is NOT new evidence furnished only by this theorem. Cold comparison with the
checked older global moment gives the exact identity

    sum_a integral_0^T 1_(R(s-)>=r) dN_a(s)=(R(T)-r)_+.

Translation invariance and the old E exp(2theta R) estimate alone imply

    E integral_0^T 1_(R(s-)>=r) dN_F(s)
       <= |F|/[n(e^(2theta)-1)]
                            exp[C_theta n(T+epsilon^2)-2theta r]. (27a)

Indeed E(R-r)_+=sum_(j>=r+1)Pr(R>=j), and a geometric Markov bound gives
(27a). Thus (26)-(27) are a consistency/operational consequence, not a new
load-bearing closure. In contrast a bound on the value of a moment at every
time does not bound its instantaneous derivative, so (25) is not obtained by
differentiating the old upper bound. Nor does (27a) bound a magnetic current
in a dark sector. That requires the new joint rare-hole information.

A bounded marked functional dominated by B times this number of late local
marks has absolute expectation bounded by B times either estimate. Neither
estimate bounds arbitrary field-state changes inherited from earlier
excursions or future unmonitored activity. The instrument is not stopped at r.

## 7. High global-count magnetic current, with the exact remaining limit

There is a related signed-current consequence in the fixed Hamiltonian
normal-form coordinates sigma_Y=Y rho_micro Y*, where Hbar is the actual
bounded magnetic fast coefficient obtained by removing the stated finite-spin
diagonal Delta_S. It is not mislabeled as a term of the unrotated microscopic
Hamiltonian. Y may be the order-six circuit of DEFECT_LEMMA; its coloring need
not preserve translations.

The single-site version of the endpoint argument proves

    Y*(w_a Q_theta)Y
       <=exp(a_theta n epsilon^2)
                           [2w_a Q_Theta+c_theta epsilon^2 Q_Theta].

Use physical translation invariance only on the right side, together with
(2) and the checked unweighted global moment. Therefore, with larger constants,

    Tr[w_a Q_theta sigma_Y(t)]
       <=C_theta epsilon^2(1+n t)exp[C_theta n(t+epsilon^2)].

This is a local hole factor with a GLOBAL volume exponent, not a local count
tilt. It holds even when sigma_Y itself is not translation invariant.
The same local projection estimate gives <w_a>_sigmaY<=C epsilon^2(1+t).

Fix a bounded local hole-preserving O_X. The checked source identity gives
J_X=i[Hbar,O_X]=P_X J_X P_X, ||J_X||<=C_X, where P_X requires some hole in a
fixed finite A neighborhood. All expectations in this section are in sigma_Y.
Define the GLOBAL count cutoff

    Pi_n=P_X 1_(Kd>=a n).

This is a proof projection, not an observed record. It commutes with P_X.
By the single-site weighted bound just proved and Markov's inequality,

    epsilon^-2 <Pi_n>
       <=C_X(1+n t)
                     exp[-a theta n+C_theta n(t+epsilon^2)].     (28)

The independently checked mean-hole estimate gives
<P_X><=C_X epsilon^2(1+t). Positive-state Cauchy-Schwarz, without assuming
that J_X commutes with Pi_n, gives

    |<J_X-(1-Pi_n)J_X(1-Pi_n)>|
       <=3||J_X||sqrt(<P_X><Pi_n>).                   (29)

On the same type of short interval, the epsilon^-2-weighted time integral
of (29) is bounded by a polynomial in n times exp(-c n). It therefore tends
to zero as the GLOBAL volume/count threshold tends to infinity, uniformly
in epsilon and spin. This improves the previous combination of an unweighted
global moment with a separate mean hole bound: that combination lost the
needed rare-hole factor and did not control a fast current this way.

The limitation is exact. If a crowded cluster of size m sits in a torus with
n much larger than m, (2) still pays exp(C_theta n t), not exp(C_theta m t).
There is no replacement of n by the cluster size, no positive-time local
conditional tail I3, no microscopic electric uniform integrability, and no
control of the complete marked Duhamel remainder. The local response and
multi-hole cascade theorems are useful response inputs, but they do not
remove this source-weighting gap automatically. In particular (27) suppresses
high GLOBAL record density on an early interval, not a dense island in an
arbitrarily dilute enormous exterior. Fixed-volume sectors are not made
small after division by epsilon^2 merely by taking epsilon to zero in (2).

## 8. Distinct approaches, exact controls and next missing lemma

The successful family is a positive global tilt followed by separate
unitary and positive LOCAL homological corrections. The positive correction
is necessary for the nonconservative potential, while a final unitary
repairs its Hamiltonian side effect. It is materially different from the
failed pointwise local tilt and from a new Fourier-radius scan.

Two other approaches were examined and not used. Holder interpolation of
the checked unweighted exponential count moment with the mean-hole estimate
loses the exact epsilon^2 factor; it cannot yield (26) at the fast scaling.
An actual cascade harmonic/Poisson lift is available on fixed finite global
excitation sectors, but its constants and localization length grow with the
global count. It does not by itself justify a source expansion in an
extensive microscopic state. It is a distinct live route, not an assumed
localization theorem. The actual seven-B dark-to-dark witness continues to
refute instantaneous local-current domination by bare loss; no step here
uses that false inequality.

check_series.py is a new exact Gaussian-rational Laurent-algebra control in
dimension3, with powers-4 through8 and all coherently retained jump entries.
Its35 checks verify the unitary orders3-6, Hermitian positive generators,
zero- and first-order potential cancellation, wrong-sign doubling, the
nonzero induced Hamiltonian order-two term and its repair, absence of
negative-order potential, unchanged leading jump grades, the complete
potential variation formula including recycling, and the phase-diagonal
jump drift identity. It ran in0.669234 CPU seconds,0.669374 wall seconds,
20,692,992 peak RSS bytes, one thread, under a25-second CPU cap with original
deadline/STOP guards. No check failed. This is an abstract coefficient
control, explicitly NOT a physical Gauss-star simulation or a proof of
uniformity. The actual-law count cancellation and physical source identities
are the separately checked, fully read input proofs. The uniformity and
endpoints are the analytic arguments in sections2-5.

No literature theorem is imported. No new source ensemble, rotor law,
record-label refinement, empirical parameter, quantum interpretation or axiom
is adopted. No old pack source, main, audit authority, remote branch or PR
was changed. This report needs a focused independent mathematical check
before downstream reuse.

An attainable next source target remains the true local conditional estimate

    sup_(epsilon,S,L,a,t<=T)
       epsilon^-2 Tr[sigma_epsilon(t) w_a 1_(|C_a|>=m)] ->0.

Here sigma is the fixed exact coordinate state of the actual process, and
C_a is the previously defined occupied-B cluster diagnostic. It would
control the large-local-cluster magnetic current piece, but still would not
be the entire microscopic output theorem. A route using the new response
bridges must now replace the global volume cost in this proof by a controlled
connected source cost, or establish a signed local estimate that avoids this
stronger positive tail. Renaming the full M4 Duhamel estimate is not such a
step. The present result retires the precise rare-hole GLOBAL moment gap,
bounds instantaneous weighted original activity, and suppresses the stated
high-GLOBAL-count fast magnetic current with its full epsilon^-2 prefactor.
Integrated late-record suppression is credited to the older moment theorem.
The local source bridge remains open.
