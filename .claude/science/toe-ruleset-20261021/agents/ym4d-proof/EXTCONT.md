# EXTCONT — extraction, selected returns and arbitrary holes in the real contract

**The actual, history-uniform induction closure is OPEN.** There is a
PROVEN conditional continuation theorem below, a real Taylor contraction
with an explicit constant, and a differentiated hole-payment lemma valid
for arbitrary fixed holes. Their actual-model hypotheses are not supplied
by REALRGB or by FLOW's determinant identities. No Yang–Mills existence,
mass-gap, audit promotion or exhaustion of alternative methods is claimed.

| Requested item | Status and delivered result |
|---|---|
| Extraction and next-scale H-bounds | **PROVEN** finite-chart extraction identity and ideal contraction (E1–E7); **ARGUED** physical localization scheme; **OPEN** actual gauge-compatible operator, uniform coefficient recursions and E19. |
| Selected-return regularity | **PROVEN** derivative-acquisition implication E10–E12, including the normalized reference; **OPEN** its all-history moving-sector and exterior-field hypotheses. Discrete masks have uniformity requirements, not unspecified real derivatives. |
| Arbitrary-hole control | **PROVEN** E15–E17 under a complete differentiated hole-volume payment; unweighted saturation is actually unbounded for fixed positive support rate. **OPEN** the required payment, or a different compatible actual-model representation. |

PROVEN means the displayed implication with its hypotheses, not retained
status. The work and evidence are recorded in [EXTCONT_LOG.md](EXTCONT_LOG.md).
The byte inventory is [checks/extcont_inventory_before.json](checks/extcont_inventory_before.json).
This snapshot has no git metadata and no MIXSMALL deliverable or brief;
MS below is an explicitly requested interface, not an assertion about an
unseen parallel result.

Credit: Tadeusz Balaban's large-field organization; Jonathan Dimock's
[exposition of convergence](https://arxiv.org/abs/1304.0705), which treats
scalar phi-four theory in dimension three; and Bauerschmidt, Brydges and
Slade's [real-norm RG methodology](https://arxiv.org/abs/1907.05474).
External references supply methods and attribution only. All additional
lemmas used here are proved below. No memory-only [m] item is load-bearing.

## 1. Fixed contract and the source dictionary

Use REALRGA §§1–4: finite compatible four-dimensional periodic lattices,
SU(N), N>=2, odd L>=3, probability Haar, Decision-4 normalized soft kernels,
and the actual inherited density rho_(j,h), distinguished from the bare
bookkeeping density b_j. Positive fibers are named; zero fibers remain
zero summands. All current selected outcomes, including completion and
chart failures, occur in the exact state. A selected term is not replaced
by the sum over outcomes when estimating its derivatives.

Write T=T^(6,4), or its labelled four-source version, with the frozen
weights and ordered fine/coarse derivatives of REALRGA RGA3–RGA4. The
full norm is

    ||K||_(mu,T)=sup_v sum_(X contains v) exp(mu |X|) sup_D T(K_X).

Supports contain original sources, inactive roots, exterior and normalizer
readers, and any necessary connected hull. Multiplicities in regulators
are added on overlaps. All differentiated functions are defined on open
real domains with the stated interior margins. Only after a variable is
integrated out can its derivative species disappear.

REALRGB G1 is different: total derivative order four with l1 directions,
and frozen exterior eta. RGA3 has total field order six, source order four
(so words of total order ten occur), and l-infinity field directions.
There is no dimension-independent inclusion turning G1 into RGA3.
For a function of n source coordinates, the l1-to-l-infinity conversion
can already cost n at first order. The derivative weights h_j=sqrt(N/u_j)
and original source weights must also be converted explicitly.

Observable J derivatives keep every prescribed kernel and u_l fixed.
FLOW parameter derivatives are separate. In standard coupling units

    u=2N/g_std^2,    beta_0'=11 N^2/(12 pi^2).             (E1)

Indeed s(exp(i a^2 F^a T^a))=a^4 sum_a(F^a)^2/(4N)+O(a^6),
with tr(T^a T^b)=delta_ab/2; summing unoriented planes gives
u/(8N) times sum_(mu,nu,a)(F_mu,nu^a)^2. Comparison with the
1/(4g_std^2) convention gives the first identity. The second is FLOW's
normalization conversion of its stated standard one-loop coefficient,
not a new derivation of universality for this kernel. FLOW's older
g_lattice obeys g_lattice^2=1/u, not g_std^2=1/u.

## 2. An explicit extraction, and the difference between it and closure

### 2.1 Exact bookkeeping on a supplied local real representation

Suppose the complete positive output has first been integrated and has
an exact local action representation, on a declared chart,

    S'_(j,h)=u_j W_(j+1)+F_(j,h),    beta[W_(j+1)]=1.

All prefactors and additive complements must have been included before
taking this logarithm. In particular, -log(A Z+E_comp) is not -log(A Z).
W can be the actual normalized-kernel tree functional when its needed
regularity/local representation has been established. For N>=3 retain
FLOW §3.1's correction: the SU(N) maximizer gives the tree exponent
kappa u phi_M, not an uncancelled U(N) polar deficit. The difference
starts at degree six and matters in a C^6 contract even though beta
cannot see it. No new tree regularity is inferred here.

Assume separately a translation-invariant infinite-volume bulk family at
J=0 whose Hessian has the summability required by FLOW's beta functional.
Define

    delta u_j = beta[F_(j,bulk)(.;0)],
    u_(j+1)=u_j+delta u_j,
    G_(j,h)=F_(j,h)-delta u_j W_(j+1).                   (E2)

The bulk definition is independent of the selected history and torus.
Wrapping, boundaries and inhomogeneous/source-dependent quadratic terms
stay in G. For an input without this bulk limit, E2 is not yet defined;
substituting a history-dependent quadratic coefficient changes the flow.

Here is a completely specified *coordinate* extraction. On each supplied
local chart, collect **all** still-retained field coordinates into z=(f,c),
with z=0 the declared reference and a product of convex unit balls in the
weighted coordinates. Sources are untouched. Put

    P_2 G_X(z,J)=G_X(0,J)+D_z G_X(0,J)[z]
                             +(1/2)D_z^2 G_X(0,J)[z,z],
    C_(j,h)=sum_X P_2 G_X,
    K'_(j,h),X=(1-P_2)G_X.                              (E3)

Thus S'=u_(j+1)W+C+sum_X K'_X exactly, P_2^2=P_2, and K' has
zero field jets of degrees zero, one and two for every J. No Taylor
truncation of the source dependence is made. Each coefficient continues
to read the original source labels in X, even if its field degree is zero.

E3 specifies what is stored: field-independent terms including source
vacua; every linear tensor; every quadratic tensor, including anisotropic,
boundary, mixed fine/coarse and holonomy/chart terms. Nothing is declared
zero just because it is absent in the homogeneous vacuum. The source-free
bulk scalar curvature-quadratic coefficient is already in u by E2.

For the coordinate Taylor norm, at fixed J let A_r be the sum of weighted
derivative terms at (0,J) of total field order r, including the source
Taylor sum. A homogeneous
degree-r coefficient contributes at most 2^r A_r to T after reconstruction:
differentiate the monomial and sum the binomial coefficients. Hence

    ||P_2 G||_T <=4 ||G||_T,
    ||(1-P_2)G||_T <=5 ||G||_T.                          (E4)

All these coefficients are evaluated at the same (0,J), so their sum
is bounded by T_(0,J)(G), then by sup_D T(G). Evaluation and reconstruction
use the same chart balls. With multiple
field species the identity is the product of their binomial identities.
Source derivatives commute with P_2. In original group derivatives,
chart-change and inverse-chart constants must multiply E4; they are not
assumed uniform. A field omitted as a supposedly frozen parameter would
invalidate this claim when that field is later differentiated.

**E2–E4 are PROVEN conditional algebra, not the actual invariant RG map.**
E3 deliberately stores a complete quadratic kernel, which can have
arbitrarily many spatial coefficients. It does not prove a closed,
finite relevant/marginal counterterm system, gauge compatibility, or
smallness of its counterterm evolution. Local gauge transformations need
not fix the chosen chart origin. Averaging over constant conjugations or
the finite lattice symmetry group does not by itself resolve that issue.

### 2.2 Physical localization that is still needed

On a contractible curvature chart, the candidate marginal localization
tests the quadratic kernel on constant transported curvature. If the bulk
at J=0 is gauge, translation and full hypercubic-reflection invariant, its
colour bilinear form is proportional to the invariant trace form. Reflecting
one coordinate changes the sign of each curvature component containing it;
therefore cross-plane quadratic coefficients vanish. Axis permutations
make the six diagonal coefficients equal. The remaining scalar is tr F^2.
An orientation-odd F-dual-F term is excluded by these reflections. There
is no invariant linear su(N) functional. These statements concern this
bulk symmetry sector, not a selected hole with fixed exterior data.

A compatible physical Loc must therefore retain the vacuum and that bulk
coefficient, all source-dependent local counterterms with their original
labels, and every permitted boundary/holonomy term in its chosen sector.
The latter are not classified or set to zero by bulk symmetry. E3 gives
a conservative container until that classification and its bounds exist.

The distinction is mathematical: beta[G]=0 is not D_z^2 G(0)=0. Already
the abelian local quadratic functional sum_(x,nu) |F(x+e_nu)-F(x)|^2 has
zero constant-curvature coefficient and a nonzero Hessian on varying
curvature. In gauge-potential Fourier variables its symbol has an extra
factor sum_nu |exp(ip_nu)-1|^2 multiplying the curvature quadratic form;
its p^2 marginal coefficient is zero. It still needs spatial Taylor
estimates under the background map. A finite field Taylor norm alone
does not turn beta-zero into the zero-jet premise of the next lemma.

### 2.3 A full Taylor-sum irrelevance bound — PROVEN benchmark

Let F on the convex product field balls satisfy P_2 F=0 identically in J.
In these *curvature-dimension* coordinates define the ideal map

    D_L F(f,c,J)=L^4 F(L^-2 f,L^-2 c,J).

Use exactly the factorial split a! b! c! of RGA3 in these coordinates.
Let A_r(z,J;F) be the **pointwise** sum over a+b=r of weighted
directional derivative suprema divided by a! b!, including all source
orders with their factorials. Thus sum_r A_r(z,J;F)=T_(z,J)(F).
The domain supremum remains outside this entire sum, exactly as in RGA7.
For r<3, radial Taylor integration of D_f^a D_c^b F, whose first
3-r Taylor coefficients vanish, gives, for z in the unit balls,

    A_r(s z,J;F) <= binom(3,r) s^(3-r)
                          sup_(0<=t<=1) A_3(t s z,J;F).

Here the left derivative weights are those of the original unit balls.
To check the constant, the radial derivative of order 3-r expands into
fine/coarse words; a third-order multi-index (i,j), i+j=3, contributes
binom(i,a)binom(j,b). Summing a+b=r gives binom(3,r).
The integral remainder contributes exactly 1/(3-r)! before this division.
For r>=3 keep all derivatives at the same evaluation point. Taking
s=L^-2 yields

    sum_(r=0)^2 A_r(z,J;D_L F)
       <=7 L^-2 sup_(0<=t<=1) T_(t s z,J)(F),
    sum_(r=3)^6 A_r(z,J;D_L F)
       <=L^-2 sum_(r=3)^6 A_r(s z,J;F)
       <=L^-2 T_(s z,J)(F).

Taking the domain supremum only now gives

    ||D_L F||_T <=8 L^-2 ||F||_T.                       (E5)

Thus L>=3 gives a
strict coordinate-norm contraction, at most 8/9 at L=3. The labelled
source norm has the identical proof, with subsets replacing factorials.
No seventh field derivative or fifth source derivative is used. This
strengthens the ideal higher-derivative benchmark in RGA-E to the full
Taylor sum; it does not identify D_L with an interacting return.

Original link coordinates have different scaling, retained older fields
need not scale at all, and physical Loc normally subtracts less than P_2.
To use E5 the producer must justify its coordinate/scaling dictionary,
domain margins, transport of all original readers, and the spatial
quadratic remainder described above. Even bounded chart constants matter:
with a support/coordinate conversion C_tr and operator error d_j, the
usable linear estimate has the form

    ||L_j^irr|| <= 8 C_tr L^-2+d_j.                    (E6)

Neither a volume factor L^4 nor a root/hole cost may be counted twice;
E5 already includes the former, but includes no reblocking of supports.
An explicit sufficient comparison is a linear reference operator B_j
with ||B_j||<=8 C_tr L^-2 and

    ||D_K R_j(0)-B_j||_(mu,T -> mu,T)<=d_j.             (E7)

Here D_K differentiates the RG map with respect to an inserted activity,
not a field or source. R_j must be the **actual extracted** return on the
same fixed full norm. E7, with uniform C_tr,d_j and all current selections,
is OPEN. Substituting E5 for E7 is the missing argument, not a proof.

### 2.4 What FLOW supplies and does not supply

| Source | Legitimate role in extraction | Limit that survives |
|---|---|---|
| FP-exact, FLOW §52 | At its admissible critical Gaussian background, use Delta_FP=abs(det chi Gamma) det(hh*)^(-1/2), retaining the ghost determinant exactly. | This is linear FP/coarea algebra with positivity/admissibility hypotheses, not selected-history nonlinear regularity. Replacing it by a background-independent factor changes the marginal coefficient. |
| T-tel, §96 | The transverse identity total_n=(1/2) sum_(k<n) Phi_k^T+G_gh,n cancels the unwanted longitudinal remainder before estimating derivatives. | Determinant telescoping does not bound the local C^(6,4) interacting map or its spatial quadratic remainder. |
| Cartan-T, §105 | Supplies the actual Cartan root-sector derivative, including its phase weights and denominator; the naive contour average is not substituted. | A special-background linearization does not control all real fields, all orders through six, or all selections. |
| SLICE-U, §§106–107 | Pair the slice gradient at U: P_n A^(n)=P_n Q^(n). Only the complete projected expression has the cancellation needed for estimates. | The displayed second-order longitudinal leak grows with depth before cross-term cancellation. VC-T1 covers the C-part through order two, with Pi-loc supplied. |
| Final list, §110 | Names the remaining inputs rather than hiding them in a coupling label. | L-loc2 and Pi-loc are ARGUED; T-a1-M, T-a3, T-b, T-c and the listed rate/causality items remain OPEN. |

For an actually supplied real Hessian bound, FLOW's beta functional can
be estimated without Cauchy: REALRGA §6 gives, in FLOW's graph and coordinate
units,

    |beta[F]| <=64 M_block^6 H
                sum_(n>=1) n^3(6400 exp(-kappa_p))^(n-1),
    kappa_p>log(6400),                                 (E8)

when each unweighted Hessian entry is bounded by H exp(-kappa_p d(X)).
Changing from h-weighted derivatives to these entries costs h^-2 and
the actual factorial constants. E8 bounds a coefficient; it is not E7.

Writing F=Gamma_j+R_j^other, the exact sign convention in E2 is

    b_j=-beta[Gamma_j],
    u_(j+1)=u_j-b_j+beta[R_j^other].                    (E9)

All higher fluctuation terms, returned terms, Jacobians, cutoff and
reference contributions occur exactly once in R^other. In FLOW's RLF
notation its marginal returned contribution is -delta beta_j. Source
vacua remain as source functions. A bound on sum b_j-beta_0' n log L
and a real remainder/causal-flow estimate are separate hypotheses;
the four listed identities do not prove b_j=beta_0' log L at every step.

## 3. Selected-return regularity and genuine derivative acquisition

### 3.1 Fixed or transported sectors — PROVEN conditional lemma

Let y contain all external fields and original sources. For each fixed
discrete history/mask a, suppose its selected integral can be represented
on a fixed measure space E_a by

    Z_a(y)=int_(E_a) w_a(y,x) d lambda_a(x)>0,
    N_a(F)(y)=int_(E_a) F_a(y,x) w_a(y,x) d lambda_a(x),
    n_a=w_a/Z_a.                                       (E10)

Assume domination for every included mixed derivative on compact real
parameter sets. A fixed selector can be part of a nonnegative,
y-independent weight w_0; on its positive support write w=w_0 exp(H).
For every nonempty ordered derivative word I permitted by p=6,q=4,
assume |D_I H|<=B in the frozen weighted units. B can depend on the
specified supported group; it must be budgeted before claiming uniformity.

Let M_0=I_0=C_0=1 and, for m>=1, define

    M_m(B)=sum_(pi partition [m]) B^card(pi),
    I_m(B)=sum_(r=1)^m binom(m,r) M_r(B) I_(m-r)(B),
    C_m(B)=sum_(r=0)^m binom(m,r) M_r(B) I_(m-r)(B),
    P_(6,4)(B)=sum_(a+b<=6,c<=4) C_(a+b+c)(B)/(a! b! c!),
    P_(6;[4])(B)=sum_(a+b<=6,c<=4)
                        binom(4,c) C_(a+b+c)(B)/(a! b!).

Write P_T for the polynomial matching the chosen norm. In the labelled
case each label's weight is absorbed into its differentiation direction
in the score bound B. There are binom(4,c) subsets of size c and no
source factorial in RGA4; P_(6,4) is not used for that norm.

Repeated differentiation of exp(H) partitions derivative positions, with
their order inside each block retained; it proves |D_I w|<=M_m w.
Positive integration gives |D_I Z|<=M_m Z. Differentiating Z Z^-1=1
and solving for the highest derivative proves the reciprocal recurrence.
Leibniz now gives |D_I n|<=C_m n, and therefore

    int T(n_a) d lambda_a <=P_T(B),
    T(N_a(F)/Z_a) <=int T(F_a) T(n_a) d lambda_a.
                                                               (E11)

For example, if T(F_a)<=a_0 G and the complete reference has
E_(n_a) G<=R, then

    sup_y T(N_a(F)/Z_a)<=a_0 P_T(B) R.                  (E12)

For products use the sum of regulator multiplicities and all coefficient
jets, as in RGA14. Every displayed estimate is on the same law and support.
E11 differentiates the normalizer and acquires derivatives from primitive
score bounds. It does not acquire derivatives of an arbitrary F from
its values. Signed F is allowed in the last inequality; positivity is
used only for the reference. Rare mass does not appear as a gratuitous
inverse, but its normalized score/moment estimates are indispensable.

The proof applies through total order ten and to labelled sources. For
the fixed sectors of REALRGB G9 it extends the fourth-order calculation
to all these terminal/source words: derivatives of the matrix exponential
are bounded by the product of direction norms, using ordered simplex
integrals of unitary factors. In l-infinity directions a local group
with n_c terminal links and original source readers S has the sufficient
score bound

    B >= max(2u_0 sum_(p in S) r_p,
             t_j n_c max_(1<=b<=6) h_(j+1)^b).

Source derivatives of H beyond first and source/terminal mixed derivatives
of H vanish. This formula includes the source convention u_0(1+epsilon_p).
It does not bound a global source box by a constant, supply locality, or
differentiate retained earlier-field cuts. Higher history depth can also
increase the number of original readers. Those costs remain in MS/E12.

If the selected domain moves, E10 can instead be obtained from an exact
diffeomorphism x=Psi_a(y,z) from a fixed domain, with its Jacobian. Then
w_a includes the transformed density and Jacobian, F_a is the transported
insertion, and the chain rule proves E11 under the same score/domination
bounds. Source-independent field transports need field derivatives only
through six. A source-dependent transport can require field order 6+4;
either carry that hierarchy or avoid that transport. No boundary term is
discarded by calling the new coordinates real.

### 3.2 What is missing for the actual selections

Uniformity means one set of constants for every admitted discrete failed
set, hole geometry, history depth and volume, on a stable open field
domain. There is no real derivative with respect to membership of a
discrete vertex in a hole. A shape/threshold deformation must first be
parameterized; a finite difference of masks is a separate norm estimate.
If a mask is selected by varying the fields, E10 requires control of that
composition, not treating the indicator as constant.

The actual child reads I_(a|h)(U,V), including the completion minimum.
The sources do not give a uniform C^6 transport of every such domain,
nondegeneracy of each threshold surface, or boundary/intersection estimates
of the required orders. Positivity alone cannot fill the gap: for
|x|<1/2, the strictly positive selected integral

    int_0^1 1_(y<=1/2+|x|) dy=1/2+|x|                 (E13)

is not even C^1. This is a counterexample to an automatic regularity
inference, not evidence that an actual gauge child has that singularity.
Smoothing the hard predicates changes individual histories unless an
exact partition with all complementary terms and derivative bills is
proved. Summing current outcomes removes their selection but proves a
different, unselected statement.

Likewise ||f||_infinity<=epsilon does not imply a C^6 bound: for
f_n(x)=n^-6 sin(nx), the values tend to zero and sup|f_n^(6)|=1 on
[-1,1] for n>=2. These functions already have their degree-zero, one and
two Taylor terms removable without changing the sixth derivative.
Thus neither RD3's scalar bound nor E4 creates the missing jets.

FR remains the named fixed-domain/selector input, KR the complete
interaction/prefactor input, and TC the original-law charge/tail input.
Their selected-sector results are not asserted to establish E10–E12
uniformly over all histories. Actual selected-return H1 is **OPEN**.

## 4. Arbitrary-hole norms, including derivatives

### 4.1 Existing fixed-mask transfer and its exact obstruction

Let Gamma be a finite connected graph of degree <=8, Lambda its fixed
active set, and H the connected components of Gamma minus Lambda. For
connected X meeting Lambda define

    R_Lambda(X)=X union {all H with dist(H,X)<=1}.

Group activities by Y=R_Lambda(X); retain X disjoint from Lambda with
their original supports. This is LIB1's exact reindexing. Fixed masks
commute with all already existing jets. For RD3's single hole
H={-1,0,1}^4, |H|=81, |N[H]|=297, hence

    ||K_inactive+K'||_(mu,T)
        <=(1+297 exp(81mu)) ||K||_(mu,T),
    ||K_inactive+K'||_(mu,T)
        <=730 ||K||_(649mu,T).                          (E14)

The first estimate adds at most 81 vertices and charges an inactive
output root to a root in N[H]. The second uses at most eight incident
holes per input vertex and |N[H]|<=9|H|; these are exactly RD3 D22–D23
and LIB1 L13–L15, now with a supplied Banach-valued jet norm. They do not
acquire any derivative. Repeated use of the stronger input rate requires
regeneration, not an endless rate loss.

For arbitrary holes the unweighted map has no uniform fixed-mu>0 bound.
Take Gamma=(Z/TZ)^4, T>=3, one active vertex v, and constant activity one
on {v}. The complement is connected: keep one nonzero coordinate while
setting a second to one, then set the others to one; this connects every
nonzero vertex to (1,1,1,1) without visiting v after translation.
Saturation fills Gamma, giving the exact ratio exp(mu(|Gamma|-1)).
Constants have zero positive-order jets, so derivative regularity cannot
repair this zeroth-order obstruction to the stated operator. This is
the existing LIB1 L23/REALRGB §3 witness, not a new physical no-go.

### 4.2 A differentiated hole-volume payment — PROVEN sufficient condition

For X meeting Lambda write H_X for the components meeting or adjacent
to X and S_X=sum_(H in H_X)|H|. Suppose an **exactly supplied weighted
representation** gives w_X K_X before saturation, where all readers of
w_X lie in R_Lambda(X), and

    sup_D T(w_X)<=A exp(-tau S_X),
    A>=0, tau>mu>=0.                                  (E15)

The weight is part of the actual coefficient, not something inserted
to improve a bound. The bare K_X reads only X. Define
K'_Y=sum_(R_Lambda(X)=Y) w_X K_X. Put delta=tau-mu and

    C_hole=A max(1,9 sup_(m>=1) m exp(-delta m)).

Then, in the same support rate and full jet norm,

    ||K'||_(mu,T)<=C_hole ||K||_(mu,T),
    ||K_inactive+K'||_(mu,T)<=(1+C_hole)||K||_(mu,T).
                                                               (E16)

Proof. Submultiplicativity of T and |R(X)|-|X|<=S_X give the
per-input weight bound

    exp(mu |R(X)|) T(w_X K_X)
          <= A exp(-delta S_X) exp(mu |X|) T(K_X).

For an active output root v, v in R(X) implies v in X, so its sum is
at most A||K||. For an inactive root v, let H_v be its unique component,
of size m. If v in R(X), H_v belongs to H_X and X meets N[H_v].
Therefore exp(-delta S_X)<=exp(-delta m). Sum the input rooted norm
over at most |N[H_v]|<=9m roots. This gives
9A m exp(-delta m)||K||. Take the supremum over all roots; the
unchanged inactive family costs at most ||K||. No probabilistic
independence is used. Empty/full Lambda endpoints follow directly.

The constant is finite since sup_(s>0) s exp(-delta s)=1/(e delta),
by differentiation. At exp(mu)=2, exp(-tau)=1/4, the exact discrete
supremum m/2^m is 1/2: equality holds at m=1,2, and the ratio of
successive terms is (m+1)/(2m)<1 for m>1. E16 then costs 1+9A/2.

E15 is a **jet** price. For a singleton with a sole hole of size m,
taking K=1 shows that any uniform bound for this weighted map necessarily
requires

    sup T(w_{ {v} }) <= C exp(-mu m).                  (E17)

The strict surplus tau>mu in E15 is sufficient to pay the inactive-root
multiplicity; it is not claimed necessary in every geometry. Paying only
the number of newly added vertices is not E15 when X already occupies a
large part of a touching component. The proof explicitly pays the whole
touching component in S_X.

One route to E15 is E12 for the actual selected weight, with a joint
original-law hole-volume price absorbing its full score, regulator and
reader costs. That price must be allocated once over the complete group.
It cannot be reused for each factor in an overlap product or after dividing
out a mandatory history mass. In fact a normalized mandatory event has
integral one, as RD3 D16 shows. The present lemma proves the geometry
after that valid joint payment; it does not prove the payment itself.

For a sum over histories, E15–E16 must hold on the complete history-labelled
coefficient family with its rooted sum, or on a representation that has
already performed that sum. Uniform per-history bounds do not bound the
sum of history suprema. Actual all-history E15 and derivative acquisition
for those weights are **OPEN**. Keeping unsaturated reader labels or
integrating holes before assigning final supports remain live alternatives.

## 5. Conditional induction-closure theorem

This theorem separates the requested MIXSMALL input from the additional
EXTCONT obligations. Supplying small one-step mixed coefficients alone
does not imply invariant continuation.

Fix N,L,mu,p=6,q=4, all jet weights, regulator allocations and real margins.
Choose an explicit stable class of histories/domains, with its complement
retained in the state. The following hypotheses are uniform in its
histories, volume, cutoff and depth. Constants may depend on N,L,q.

**MS (requested MIXSMALL interface, not supplied here).** For every input
state in the proposed ball x_j=||K_j||_(mu,T)<=M_q, the actual next
reference produces RGA15 with complete overlap factorization and joint
RGA14/RGA16 bounds at support rate mu+2, Q_(j,q)<=q_*<=1/4. All mixed
coefficients and prefactors are included, with compatible marked jets.
The new reference/action satisfies the same regulator and support-reserve
requirements. This is regeneration from the fixed input norm, not reuse
of a previously spent support exponent. Prefactor and source-scalar budgets
are stated separately. A theorem only for a bounded example does not meet MS.

**SEL.** E10–E12, or a direct complete integrated-jet bound of the same
strength, hold for every current return/failure used by MS. Exact real
chart/Haar representations and domain margins reproduce H0,H1,H2.
No unbounded derivative acquisition is hidden in localization. If one
uses STEP55's once-per-box differentiation, supply that larger hierarchy
instead of substituting six derivatives for it.

**HOLE.** Each actual support conversion is bounded in the same full norm,
by E16 on the complete paid family or by another proved compatible
estimate. With bounded holes E14 is allowed only if the stronger needed
input rate is regenerated. Geometric costs, source weight conversions and
inactive contributions have finite, already included constants.

**EXT.** The physical extraction is gauge/symmetry compatible and exact,
with every counterterm and its source dependence recorded as in §2.
Its selected linear return satisfies E7 (or a directly proved contraction)
after all SEL/HOLE costs. If these costs are written separately as D_q,
one sufficient returned coefficient is

    lambda_q <=D_q(8 C_tr L^-2+d_*).

This expression can exceed one; smallness is an inequality to prove.
The completed map has a second derivative with respect to the activity
bounded by 2C_q on the convex activity ball, or an equivalent direct
quadratic remainder bound. This Banach-space differentiability is distinct
from the finite field jets. Differentiating along tK and integrating twice
then gives a remainder at most C_q||K||^2.

Let s_(j,q) bound the genuinely new-gap contribution in the **same** matched
norm, eta_(j,q) every other continuation failure, and e_(j,q) the newly
generated insertion, all nonnegative. With B_q>=0 suppose the preceding
linear and nonlinear estimates give

    x_(j+1,q) <=(lambda_q+B_q s_(j,q)+eta_(j,q))x_(j,q)
                         +C_q x_(j,q)^2+B_q e_(j,q),    (E18)
    theta_q=lambda_q+B_q s_*q+eta_*q+C_q M_q<1,
    B_q e_*q<=(1-theta_q)M_q,    x_(0,q)<=M_q.         (E19)

All starred quantities are uniform upper bounds. Neither a creation
probability nor a scalar no-gap survival bound substitutes for lambda_q
or eta_*q. E16's unchanged inactive contribution must be assigned to
one of these operators, not forgotten in D_q.

**COEFF.** The actual recursion for the bulk coupling is E9, stays in the
declared positive coupling range, and meets any consumed FLOW bracket and
causal FI-1 conditions. The remaining counterterm vector/functions obey
their explicit projected recursion C'=Loc(S'-u'W), including their
source derivatives, with bounds returning them to their specified sets.
For example a supplied recursion v'=A_j v+b_j+r_j(K) with
||A_j||V_*+||b_j||+sup_(||K||<=M_q)||r_j(K)||<=V_*
preserves a vector ball; that inequality is an additional estimate, not
a conclusion from E18. Vacuum scalars can instead have an explicit
additive per-volume recursion with its stated growth budget. No scalar
dependent on original sources may be omitted from H6.

**Theorem — PROVEN conditional implication.** If these hypotheses and
the initial H0–H6 hold, their fixed q=4 real contract holds at every
finite depth, with x_(j,q)<=M_q and the same declared constants.

Proof. Exact transfer and extraction preserve the original generating
function with all history masses and complementary sectors. SEL and
HOLE give the specified real jets and full supports. MS supplies the new
complete integrated coefficients; RGA-C gives the supported log and
consumes its two reserved support units. Its proof uses the product
inequality for T and two positive rooted-tree majorants, so it applies
to these real mixed jets. COEFF accounts for the components removed from
K. For x_j<=M_q, C_q x_j^2<=C_q M_q x_j, and E18–E19 give
x_(j+1)<=theta_q M_q+B_q e_*q<=M_q. Induction proves the claim.
H6's additional all-order, matching, continuum/symmetry modules must be
propagated separately if that larger contract is claimed. q=4 proves
none of the all-n consumer estimates. This concludes only the finite-q
theorem just stated.

To formulate the corresponding theorem at another finite q, replace four
by q in the score/jet hypotheses and polynomials, including binom(q,c) for
labelled sources, and carry every mixed word through total order 6+q.
Those stronger actual-model inputs are not supplied by E10–E12 at q=4.

An alternative to one-step contraction is RENEW R20 on the *extracted*
operators in this same norm: an m-window norm <=theta_win<1, all shorter
prefixes <=B_0, returns <=D_ret. Writing r=km+s gives B_0 theta_win^k
and the continuation sum m B_0/(1-theta_win). A common summable lag
envelope for created activities is another option. Neither is established
by LINEAR_PACKAGE's action contraction (sharp constant one) or its
localized linear L^-2r dilution. RENEW's rough flux tubes specifically
exclude a coupling-uniform plain-forward return margin on all inputs;
they do not exclude these extracted, weighted alternatives.

MS, SEL, HOLE and EXT are coupled hypotheses, not independent walls.
EXT and COEFF still contain substantive parts of the requested induction
theorem. This is a transparent sufficient interface, not a reduction to
a demonstrably weaker missing lemma or a claim that MIXSMALL alone closes it.

## 6. Exact failures, scope and next decisive tests

| Inequality or inference | Disposition | Technique failure or obstruction? |
|---|---|---|
| norm(S_Lambda K)<=C norm(K), arbitrary holes and fixed mu>0 in the full norm | **False**; singleton ratio exp(mu(card(Gamma)-1)). | Actual obstruction to that unweighted saturation map only. E15 is a live weighted escape. |
| Value bound epsilon implies a derivative bound C epsilon in T | **False**; the sixth derivative of n^-6 sin(nx) stays order one. | Actual obstruction to acquiring finite real jets from values alone, not to primitive-density differentiation. |
| Positive selected integral is automatically C^6 | **False as a general inference**, E13. Actual gauge regularity **OPEN**. | Invalid technique without fixed-domain or boundary hypotheses; no actual-child singularity proved. |
| beta[G]=0 implies P_2 G=0 | **False**, spatial curvature-difference quadratic example. | Obstruction to replacing physical marginal extraction by a zero-field-jet hypothesis. Spatial localization remains live. |
| Four FLOW identities imply norm(D_K R_j(0)-B_j)<=d_* with E19 | **OPEN**, E7 not obtained. | Missing derivative/locality science; no operator lower bound or impossibility is established. |
| D_q(8 C_tr L^-2+d_*)+B_q s_*q+eta_*q+C_q M_q<1 | **Unevaluated actual inequality**, E19. | Available ideal gain does not certify the total bill. No failed numeric run is asserted. |
| sup T(w_X)<=A exp(-tau S_X), tau>mu | **OPEN** under the actual matched law. | Needed sufficient input, not an observed obstruction. A mandatory normalized event's old rarity cannot pay it again. |
| RD3 cap bounds certify uniform local selected weights | **Insufficient**: REALRGB G11/G29 retain extensive volume debits. | Failure of those upper majorants only, not a lower bound on the actual weights. |
| RGA16 at one step automatically regenerates mu+2 and all counterterms | **OPEN**; MS and COEFF require new estimates at the next state. | An induction gap, not a consequence of finite exact recursion. |

The next actual-model target is a complete bounded mixed return, with
one coarse derivative and all four original-source labels at minimum,
including its selector-boundary contribution and differentiated matching
reference. That is a diagnostic subcase of SEL/MS, not their full scope.
For arbitrary holes test E15 on the joint history-labelled coefficients
with the unused original-action reserve explicit. For extraction test
E7 on the spatial quadratic and higher remainders after the T-tel and
SLICE-U cancellations, keeping the full matrix/Faddeev–Popov normalization.

Five distinct live approaches have been separated: exact fixed-domain
transport; boundary/shape differentiation of hard sectors; an exact smooth
partition with complementary terms; original-weight hole payment; and
integration of inactive variables before final support assignment.
Only the fixed-domain implication and the abstract hole-payment estimate
are proved here. No approach-exhaustion count is claimed. Diagnostic
examples apply respectively to one scalar parameter, one supported activity
on finite graphs, or a linearized quadratic functional; they assert no
continuum, spectrum or physical-model failure. The strongest counter-route
to a broad negative claim is precisely a matched weighted construction
satisfying SEL/E15/E7. It remains OPEN.

Numerical criteria were registered in
[checks/extcont_criteria.md](checks/extcont_criteria.md). Finite regressions
and the mandatory fresh same-family hostile review are reported in the log;
neither a finite check nor this author status replaces independent review.
