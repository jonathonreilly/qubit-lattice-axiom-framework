# CHARGE — original-action credits, flux backgrounds and matched renewal

**Original-action charging bounds the extensive flux family at a precise
real-sector scope; general matched renewal remains OPEN.** The original
action can be allocated across the filled tower without double counting.
Moreover an explicit cap comparison bounds that sector against the actual
real all-cut denominator, uniformly in its terminal real field, under the
coupling/cut conditions in §2.3. The estimate retains the actual denominator.
It does not establish the local complex, mixed-reader norm
or the finite-window operator in RENEW-MATCH(m).

The flux field is not a flat toron or a new twisted boundary condition.
It is a saddle of the bare Wilson action, with a periodic negative mode
computed below. The small-curvature background results cannot simply be
applied to it. A sector-dependent reference remains a possible construction.

| Mechanism | Status for the requested LF-JMBR construction | Result of the probe |
|---|---|---|
| R1: original-weight charging | **OPEN** for arbitrary admitted histories on D_*; **PROVEN** for the filled-tube real-sector bounds below | One-use geometric credits and an actual real all-cut comparison beat a fixed per-step volume factor for this extensive family. Local patches, mixed types and the complex reference remain unpriced. |
| R2: flux-sector/background extraction | **ARGUED** as a renewal mechanism; exact sector algebra **PROVEN**, renewal estimate **OPEN** | Exact sector splitting and background translation are available. Toron/twist identification fails for this witness; a bare positive-Hessian expansion at it fails by an explicit mode. |
| R3: finite-window operator | **OPEN** | Exact real continuation and first-return operators can be written. Their extracted complex full-support norm, especially its coherent no-gap part, is not controlled by the two preceding estimates. |

PROVEN means a written mathematical result under its stated hypotheses;
ARGUED means a proposed application; OPEN means an unmet proof obligation.
These labels confer no audit status or Yang–Mills existence/mass-gap result.
Source identities, reading scope, resource failure and the independent
review are recorded in [CHARGE_LOG.md](CHARGE_LOG.md).

Credit: Tadeusz Balaban for the large-field renormalization organization;
Jonathan Dimock for its exposition in [Large fields](https://arxiv.org/abs/1212.5562)
and [Convergence](https://arxiv.org/abs/1304.0705). Their primary abstracts
specify scalar theory in dimension three. They supply attribution, not a
four-dimensional theorem. All load-bearing calculations here are rebuilt;
no memory-only [m] statement is used.

## 1. Fixed objects and the scope of the flux witness

Use the supplied finite periodic SU(N) model, N>=2, odd L>=3, probability
Haar measures, t_j=kappa u_j>0, and Decision 4's actual arithmetic contour
mean M_c(U), with ||M_c||op<=1. Set b=L^4 (this scalar is not the density
b_j below), n_j=|Lambda_j|=n_0 b^(-j), and

    s(W)=1-Re tr(W)/N=||I-W||HS^2/(2N),
    S_0=u_0 sum_p s(U_0,p),
    k_t(V;M)=exp[t Re tr(V^*M)/N]/Z_t(M),
    Z_t(M)=int exp[t Re tr(W^*M)/N]dW.                  (C1)

There are 4n_j oriented-positive links and 6n_j unoriented plaquettes.
Take even compatible sides at least six at the levels where the explicit
variations below are used. Larger terminal sides as in RENEW are allowed.

At step j the reference remains exactly

    R_h(V)=int rho_(j,h)(U) K_j(V,U)dU,
    Z_(j,A)(V)=int chi_A(U) b_j(U) K_j(V,U)dU,
    b_j(U)=exp[-u_j sum_p s(U_p)],   Q_h=R_h/Z_(j,A).     (C2)

rho_(j,h) contains all earlier fields, kernels and history predicates;
it is not b_j. Current selected predicates, when present, stay inside
R_h. RD3 §§2,5.1 and JMBRA §2 distinguish these integrals. No history
mass is divided out and then spent again. The target full norm is

    ||F||_mu=sup_x sum_(X contains x) e^(mu|X|) sup_(D_*)|F_X|,
    mu>=0,                                             (C3)

on RD4 §1's fixed original-source/coarse domain. Original source readers,
inactive regions, exterior readers and normalizers remain in X. FR, KR
and TC are named coordinator inputs at their actual scopes, respectively
for that domain, the full interaction/prefactors, and joint original-law
charging/tails. No local coercivity or general tail theorem of those lanes
is rederived or extended here.

For the RENEW family put H=diag(1,-1,0,...,0), g=exp(i pi H), and

    U_1(x)=g^(x_2+a), U_2(x)=g^d, U_3=U_4=I,
    a,d in {0,1}.                                      (C4)

Every 12 plaquette is g, all other plaquettes are I, and S_0=4u_0 n_0/N.
For completeness, the paired-contour means are
M_1=g^(X_2+a)P, M_2=g^(d+(L-1)/2)P, M_3=M_4=I,
P=diag(1/L,1/L,1,...). The translated axial legs cancel in direction 1;
in direction 2 their exponent is the signed number r_1-(L-1)/2 of
direction-1 steps. The odd-length offset sum is one. This proves the
display for all coordinate orders. For M=WP, expanding the trace gives

    h_M(W)-h_M(V)=tr[(I-W^*V)^*P(I-W^*V)]/(2N)>=0,

with equality only at V=W. Thus the maximizing tower retains g curvature
and has zero fresh gap at every level. RENEW §§3–4, independently checked
in REVIEW_RENEW, further supplies its positive-measure, finite-horizon
persistence, with the weak-coupling limit taken at fixed horizon/volume.
Only that scope is used; no infinite-horizon probability limit is assumed.

## 2. R1: spend the original action once

### 2.1 Filled histories: a geometric allocation — PROVEN

Let E_delta be the product tube of radius 0<delta<1/4 about one field
(C4) at the original level. Four-factor telescoping gives, on E_delta,

    S_0 >= c_delta u_0 n_0,
    c_delta=(2-4delta)^2/(2N)>0.                         (C5)

The same lower bound holds for the 12-plaquette part of S_0 alone.
This is RENEW's raw charge, rebuilt using (C1). A union of the four
templates also satisfies (C5); use the union indicator, or a disjoint
partition of it, rather than counting its overlaps four times.

For a horizon R and any 0<theta<=1 define actual allocated action pieces

    alpha_l=(1-b^(-1))b^(-l), 0<=l<=R,
    D_l=theta alpha_l u_0 sum_(p of orientation 12) s(U_0,p).
    sum_(l=0)^R alpha_l=1-b^(-(R+1))<1.                 (C6)

Every original plaquette is allocated fractions totaling at most theta.
The remaining action S_0-sum_l D_l is nonnegative. On E_delta,

    D_l >= theta(1-b^(-1))c_delta u_0 n_l.               (C7)

Thus one original reserve can pay a fixed bill per occupied descendant
cell at every level of this filled tower. This does not assert a new
Wilson action u_l sum s(U_l) at each level. The currency is always u_0
times original plaquettes. For disjoint filled birth regions the same
allocation adds; overlapping claims must divide each plaquette's reserve
before making either claim.

Here is the history-level integral, including its entropy rule. Let I_h
be any disjoint complete finite history partition of the whole real
chain, so sum_h I_h=1, with all failures and absences retained. If its
nonnegative bookkeeping costs satisfy w_h<=exp[a sum_(l=0)^R n_l], a>=0,
then, integrating every terminal field,

    sum_h w_h int E_delta I_h e^(-S_0) product_(l<R)K_l
      <= exp[-(theta c_delta u_0-a/(1-b^(-1)))n_0]
           int e^(-(1-theta)S_0) product_(l<R)K_l
      <= exp[-(theta c_delta u_0-a/(1-b^(-1)))n_0].       (C8)

The first inequality uses sum I_h=1 and (C5); the second integrates
normalized kernels backwards and then probability Haar. The cost w_h
may bound a fixed per-cell type/placement factor. Without such costs,
the disjoint physical histories themselves incur no extra multiplicity:
their indicators sum to one. A combinatorial majorant may instead
overcount them, but must declare its a. Continuous field integration
has already occurred; a finite list of flux labels is not its entropy.

For a fixed per-step lineage bill B>=1, B^R<=exp[(log B)sum_l n_l]
because every level is nonempty. Thus the explicit sufficient price test
is theta(1-b^(-1))c_delta u_0>log B, with extra per-cell costs added on
the right. In particular B=L^4 is affordable at sufficiently large u_0.
This proves the raw arithmetic for the filled family, not for an arbitrary
thin or isolated defect whose descendant ancestry has not been charged.

### 2.2 An actual real all-cut comparison — PROVEN

The following specialization of RD3's cap comparison also pays the
denominator. It uses the known global tube and is not a new local TC
coercivity/tail theorem. For j>=0 and U_(j+1)=V fixed, define

    R_(E,j)(V)=int E_delta(U_0)e^(-S_0)
                           product_(l=0)^j K_l dU_0...dU_j.

Any selection of persistent descendants has a smaller nonnegative
numerator; summing disjoint such histories preserves that domination.
Let epsilon_j>0 be a lower bound for all retained interior cuts in A.
Choose 0<zeta<=1 with 4zeta<epsilon_j. Then uniformly in every real V,

    R_(E,j)(V)/Z_(j,A)(V)
      <= exp[-c_delta u_0 n_0+d_j(zeta)n_j],
    d_j(zeta)=48u_j zeta^2
              +8N^2 log(1+4N/zeta)+16 kappa u_j/b.       (C9)

Proof, with all normalization factors retained. Since |h_M|<=1,
e^(-2t)<=k_t<=e^(2t). Strip off only the upper bound for the last
kernel product, and integrate all previous outputs. This gives

    R_(E,j)(V)<=exp[-c_delta u_0 n_0+8 kappa u_j n_(j+1)].

For the denominator put every level-j link in the zeta-cap about I.
Every retained cut passes, for any A. A Haar cap has mass at least
(1+4N/zeta)^(-2N^2): subdivide the 2N^2 real matrix-entry coordinates
into cells of side zeta/(2N); each occupied cell fits in a translated
zeta-ball, and Haar invariance plus the cover proves the bound.
On this product cap ||I-U_p||op<=4zeta and s(U_p)<=8zeta^2, using
||A||HS<=sqrt(N)||A||op in (C1). The 6n_j plaquettes therefore cost
at most 48u_j zeta^2 n_j. All 4n_j link-cap masses and all last-kernel
lower bounds give

    Z_(j,A)(V)>=exp[-(48u_j zeta^2+8N^2 log(1+4N/zeta))n_j
                         -8 kappa u_j n_(j+1)].

Division proves (C9). This is exactly the all-cut denominator (C2),
not the original Wilson partition function or a conditioned history
mass. Neither positivity nor normalization has erased its debit.

### 2.3 What price beats persistence, and what remains — PROVEN / OPEN

Here is a depth-uniform real consequence with its additional conditions
explicit. Suppose u_*<=u_j<=u_0, u_*>=4, and
epsilon_j sqrt(u_j)>=8 at the compared levels. These are supplied
coupling/cut conditions, not a proved RG flow. Set zeta=u_j^(-1/2).
Let j_*>=0 satisfy

    16 kappa b^(-(j_*+1))<=c_delta/4,
    b^(-j_*) sup_(u>=u_*)
       [48+8N^2 log(1+4N sqrt(u))]/u <=c_delta/4.        (C10)

For fixed N,L,kappa,delta such choices exist: choose j_* for the first
condition, then u_* for the second, since log(u)/u tends to zero.
For every j>=j_* equations (C9)–(C10) give

    sup_(real V) R_(E,j)(V)/Z_(j,A)(V)
                           <=exp[-(c_delta/2)u_0 n_0]. (C11)

The omitted finitely many j have the explicit (C9), not an asserted
smallness bound. The usual power cuts epsilon_j=u_j^((delta_c-1)/2),
0<delta_c<1, satisfy the cut condition eventually. Arbitrarily small
cuts need not; their logarithmic cap cost is displayed in (C9).

For a family filling an entire ancestor of a fixed terminal volume
n_R>=1, n_0=b^R n_R. Consequently any fixed bill B^R is beaten by
(C11). More precisely, if additional already justified support/type
costs are <=exp[s n_0], and lambda=c_delta u_*/2-s>0, then

    B^R exp[-lambda b^R n_R]                            (C12)

is summable over R: the ratio of successive displayed terms for fixed
n_R is B exp[-lambda(b-1)b^R n_R], tending to zero. A bound uniform
over n_R>=1 follows by replacing n_R by one. This compares different
compatible finite lattices as R varies; it is not an exchange of the
RENEW persistence limit with an infinite-depth probability limit.

This is a positive answer to whether the explicit extensive flux family
can be paid for once, including this real all-cut reference. It refutes
neither RENEW's forward example nor JMBRB's preservation of old mass.
It pays exponentially many original cells, not a fixed-size singleton
anew at every step. Equation (C6)'s temporal allocations and (C11)'s
final allocation are alternative accountings of the same charge; they
are never multiplied together.

**The unproved step for general R1.** For a localized core with m owned
original witnesses in a much larger torus, the same crude argument leaves

    log(Q_core) <= -tau m+d_j n_j,                       (C13)

whereas a local expansion needs a debit controlled by its complete local
readers, not n_j. This majorant fails to certify a volume-uniform local
price as n_j/m grows. It is not a lower bound on Q_core. Neither the
existence of a backward reader cone nor its volume proves that all its
plaquettes are rough. An all-history argument must prove a charged
ancestor-volume bound for its actual sectors, or obtain return/extraction
for its complement, together with a matched local comparison.

On D_* the precise remaining estimate for each mixed group G is, for
disjointly allocated original fractions omega_(G,p),

    sum_G omega_(G,p)<=1,
    int |complete charged coefficient * readers * return factors|
           d|matched reference_G|
      <=exp[-tau m_G+c_ref m_G+t_ref m_G
                            +b_partial|Bdy_G|].        (C14)

All quantities must refer to the same integral with its actual Z_A
matching. Its full rooted sum must satisfy JMBRA (A13) or (A14)–(A18).
(C11) gives one real extensive-sector instance, not these mixed bounds,
nonzero complex references or local total variations. FR/KR/TC cannot
be assumed to cover this stronger interface.

## 3. R2: what extracting a flux sector actually changes

### 3.1 Torons and twists do not identify the witness — PROVEN

For (C4), all cycle holonomies along coordinate cycles are I, since the
sides are even. The product of its commuting 12 plaquettes over a whole
12 plane is g^(T_1 T_2)=I. Nevertheless a single plaquette is g!=I.
Gauge transformations conjugate a plaquette holonomy, preserving
||I-g||op=2 and its trace. Hence this field cannot be gauge equivalent
to a flat toron, whose every plaquette is I. Polyakov holonomies alone
do not separate it from the identity field.

There is also an explicit path in the unrestricted periodic configuration
space to I: using the site representatives x_2=0,...,T_2-1, replace g
in every link of (C4) by g(t)=exp(i pi t H), 0<=t<=1. This assigns
one matrix to every link of the same finite periodic lattice and varies
continuously. Across the coordinate seam its plaquette is generally
different from the others; no admissibility or constant-flux condition
along that path is asserted. Thus no disconnected topological component
of the unrestricted link space isolates the witness. No continuum
Chern number or admissibility-sector equivalence is inferred.

For N>2, g is not even central in SU(N): a matrix mixing a negative
eigenspace with a positive one does not commute with it. For N=2 it
is central, but its total plane product and cycle holonomies above are
still trivial. Replacing the periodic model by twisted boundary
conditions changes its integration problem unless an exact identity
including all transition weights is supplied.

The existence source is `../ym4d-existence/EXISTENCE.md` (the brief's
additional `E/` directory is absent). Its §17.4, lines 3193–3228, treats
**flat** commuting-holonomy moduli and explicitly leaves WC-tor and the
wrapping SF-bg^tor inputs open. Its §18.1–18.4 Polyakov construction is
a fixed-torus observable argument, conditional in its smallness inputs;
it does not price the nonflat family (C4). Its twisted route §18.6,
lines 3623–3650, is marked ARGUED and lists the changed torus interfaces.
No estimate from these different sectors is imported here.

### 3.2 The bare flux background is a saddle — PROVEN

Take the periodic variation

    U_1^eta(x)=exp(i[pi(x_2+a)+eta(-1)^x_2]H),
    U_2^eta=g^d, U_3^eta=U_4^eta=I.                    (C15)

Even T_2 makes (-1)^x_2 periodic. Every 12 plaquette has phase
-pi+2eta(-1)^x_2 modulo 2pi, including the seam. All other plaquettes
are I. Taking the two nontrivial eigenvalues gives exactly

    s(U_12^eta)=2(1+cos(2eta))/N,
    S_W(U^eta)=2u n(1+cos(2eta))/N,
    d^2/deta^2 S_W(U^eta)|_0=-8u n/N<0.                (C16)

The background is a critical point of the entire bare Wilson action:
each original plaquette is Hermitian, and its first variation has the
trace of an anti-Hermitian matrix times a Hermitian conjugate, with
zero real part. Thus (C16) is a negative Hessian direction, not just
a curve descending away from a nonstationary point. It is not a gauge
direction, since the gauge-invariant plaquette traces change.

An independent local variation gives the opposite sign. Multiply just
one direction-1 link by exp(i eta H). Of its six incident plaquettes,
two are in the 12 plane and four were identity. Their action changes
are respectively -2(1-cos eta)/N and +2(1-cos eta)/N each. Therefore

    Delta S_W=4u(1-cos eta)/N>0                        (C17)

for sufficiently small nonzero eta. This checks that a single-link
positive curvature test would miss the collective negative direction.
The second derivatives have opposite signs: the bare Hessian is
indefinite. These proofs apply to every N>=2 and the stated nondegenerate
even tori. They do not determine the Hessian of a fixed-output full
soft action, which also contains all kernel normalizers and penalties.
Those terms could alter the sign and require their own calculation.

The relevant BFT hypotheses are quantitative smallness, not just the
word background. BFT_A §§3.9–3.10 assumes a small global gauge class or
proved small local frames, with inverse/remainder/slice hypotheses.
BFT_B §1.2 is curvature-small even at one step. Its later §41.6
transport statement requires V in K(epsilon), epsilon<=epsilon_1 and
8c_N C_1 epsilon<=1/2, plus GAP-Z and N1-nd; it is a conditional author
statement, not an unconditional reviewed arbitrary-background theorem.
REVIEW_BFT_B_S9_S10, lines 385–410, specifically rejects promoting the
trivial-background slice identity and incomplete frame argument to that
general scope. None supplies a positive covariance or uniform renewal
bound at plaquette distance two. The remaining curvature/refinement
results concern small residuals around admissible backgrounds, not
removal of the coherent curvature itself.

### 3.3 An exact sector split, with the missing estimate exposed

Let {chi_alpha} be a fixed finite measurable partition of the original
real fields (or a partition of unity with nonnegative weights). This
could isolate the flux tubes and their complement without falsely
calling them topological classes. Then, before any logarithm,

    R_h=sum_alpha R_(h,alpha),
    Q_h=sum_alpha R_(h,alpha)/Z_A.                      (C18)

This is **PROVEN** by linearity. All earlier and current failure
indicators remain. A chosen background Z_alpha gives the exact
Haar-preserving translation U_b=Z_(alpha,b)W_b. It replaces every
plaquette, kernel mean, normalizer and cut by its translated expression;
it is not a gauge transformation making S_W(Z_alpha W)=S_W(W).

If one instead normalizes a sector by its mass p_alpha>0, its weight
is p_alpha times its conditional integral. The conditional indicator
has integral one; p_alpha cannot be spent a second time. For complex
parameters the sector normalizer must first be proved nonzero. Even
if each sector separately has a logarithm, the sum in (C18) still
requires common-domain nonvanishing and mixed support control.

**ARGUED construction.** Use flat/low-curvature holonomy backgrounds
where their precise hypotheses hold, retain genuinely rough tubes as
charged non-Gaussian sectors, and perform return/extraction relative
to those references. For a Gaussian treatment of the rough template,
the unavailable coercivity inequality would be

    D^2 S_full(Z_alpha)[v,v]>=c||v||_slice^2, c>0,       (C19)

on the stated full conditioned action/slice and domain. Its bare-Wilson
version is false by (C16). A sector restriction excluding that direction,
a contour treatment, or exact integration could avoid that version,
but must include its complement and Jacobians/normalizers. Afterward
the required estimate is still (C14) and the residual operator bound
in §4. These are OPEN, not supplied by declaring a sector label.

## 4. R3: exact readers plus fresh gaps, evaluated at the missing step

### 4.1 Exact finite continuation and matching — PROVEN real algebra

Keep a vector of unnormalized history densities f_(j,h)(U). Let
{I_(a|h)(U,V)} be the actual complete decision partition at the next
step. Every size, chart and completion failure is represented. Define

    (T_j f)_(h,a)(V)=int f_(j,h)(U)K_j(V,U)I_(a|h)(U,V)dU.

Choose a specified subset of these outcomes as successful returns;
all other outcomes define the continuation operator C_hat_j. The
successful part is S_hat_j. Splitting by the first successful index
gives the stopped path law as the direct sum of
S_hat_(j+r) C_hat_(j+r-1)...C_hat_j, 0<=r<R, and the all-continuing
terminal product. These outputs have different stopping times. For a
common fixed terminal output the exact identity instead is

    T_(j+R-1)...T_j = C_hat_(j+R-1)...C_hat_j
      + sum_(r=0)^(R-1) T_(j+R-1)...T_(j+r+1)
                          S_hat_(j+r) C_hat_(j+r-1)...C_hat_j.

Empty products are identities. Expand T_l=C_hat_l+S_hat_l at the first
success to prove this formula. The future T factors and all their
readers must remain when a terminal field or observable is fixed.
No failed singleton is deleted; JMBRA §8 exhibits why that matters.

For any chosen strictly positive real reference functions z_(j,h),
define relative operators by multiplying the input by its z and
dividing the output by its z. Choose these to be the actual integrated
all-cut references at their respective output levels in (C2). They
are positive on real fields by the cap argument. Algebraically,

    C_j f=z_(j+1)^(-1) C_hat_j(z_j f),
    C_(j+r-1)...C_j=z_(j+r)^(-1)
                       C_hat_(j+r-1)...C_hat_j z_j.     (C20)

Multipliers cancel only at the intervening levels. They are never
discarded at the two endpoints. This constructs real relative
operators, not operators already bounded in (C3), nor the derivative
of a connected, extracted nonlinear RG map. Complex inverses z^(-1)
need clause 3 before they can define such an operator on D_*.

Equivalently, JMBRA's actual replacement gives

    Q_h=E_(nu_A) sum_(B subset A) T_B J_h,
    J_h=rho_(j,h)/b_j,  dnu_A=chi_A b_j K_j dU/Z_A.     (C21)

For a B summand, the old good interior masses cancel the replacement
denominators; the fresh interiors carry the bad predicates, and the
other cuts stay good. Summing B inserts product_Q(chi_Q+zeta_Q)=1.
All factors reading an integrated variable must first be multiplied;
Fubini then produces a factor on their remaining reader union. Only
unread terminal outputs of a completely specified normalized creator
law integrate to one. Wilson factors, retained cuts, history absences
and fixed-output kernels are integrand factors. Thus (C20)–(C21) keep
the exact clause-1 integration, but neither makes nu_A a product law.

### 4.2 Why the gap estimate does not finish the window — PROVEN diagnostic

For a plain forward link put psi=max h_M-h_M. The 1/t cap at a
maximizer and the 1-Lipschitz bound for h_M give, for t>=1,

    P_K(psi>=a)<=min(1,exp[-q_gap]),
    q_gap=t a-1-2N^2 log(1+4Nt).                        (C22)

Past-adapted distinct outputs can be priced by conditioning from the
last selected step backwards. In an actual selected history, future
cuts/readers change that law. To see the missing factor explicitly,
let H(y)>=0 be the integrated future weight at the next state and
KH(x)>0. The tilted conditional law is

    K^H(x,dy)=K(x,dy)H(y)/KH(x),
    K^H(x,E)<=P_K(x,E) sup_y H(y)/KH(x).                (C23)

This follows directly by bounding H in the numerator. It is useful
only when the last ratio is controlled on the same reader group.
Take H=1_E with P_K(E)>0: then K^H(x,E)=1, regardless of how small
P_K(E) is. This is a diagnostic on normalized conditional laws, not
a claim that the actual all-cut denominator equals this H. Complex
versions additionally use int|w|/|int w|, which real positivity does
not bound. Complete reader integration calculates H and its readers;
it supplies no small upper bound for this ratio.

Similarly an initial scalar creation price epsilon does not improve
a homogeneous operator ratio: ||epsilon C f||/||epsilon f||=||Cf||/||f||
for epsilon>0. On the forward flux tubes the no-gap, no-return
probability tends to one at every fixed horizon. Paying their creation
mass makes their **total contribution** small as in (C11); it does
not prove a uniform contraction on arbitrary insertions conditioned
on those inputs. A state-dependent remaining-credit norm could behave
differently, but its transfer and conversion to (C3) must be proved.

### 4.3 The exact inequality still open, and a concrete alternative

After a connected representation and specified relevant/marginal
extraction have been constructed, denote its continuation and return
linear maps by C_j^irr and S_j^irr. A finite-window proof needs constants
m>=1, B_0>=1, D_ret<infinity and theta<1, uniformly on D_* and the
stable admitted history class, such that

    ||C_(j+s-1)^irr...C_j^irr||<=B_0       (0<=s<m),
    ||C_(j+m-1)^irr...C_j^irr||
        <=theta_coh+sum_(l=0)^(m-1) b_l exp(-q_l)<1,
    ||S_j^irr||<=D_ret.                                (C24)

The first-gap split is disjoint, so the triangle inequality proves the
middle sufficient bound **if** all pieces are estimated in this same
norm. q_l must include (C23)'s tilt/reference, boundary and support
costs. The coherent term includes every no-gap completion failure.
No value theta_coh<1 is established here. (C11) controls one charged
input family, not C_j^irr on its whole space. RENEW's geometric-window
sum then gives mB_0/(1-theta), but its antecedent (C24) is still OPEN.

An explicit alternative asks only for the propagated **creation map**
A_j: prove in the same full complex norm

    sum_(r>=0) ||C_(j+r-1)^irr...C_j^irr A_j||<=D_birth, (C25)

uniformly, instead of an operator contraction for every possible
insertion. This can exploit a large charged ancestor. For example,
if actual mixed-history integration proves
||C...A_j||<=B^r exp[-lambda b^r], lambda>0, the ratio argument in
(C12) proves (C25). That bound is not asserted for localized nonlinear
histories. The unresolved constructive step is the disjoint cover of
their continuations by sufficiently charged ancestors, fresh-gap
sectors, and extracted returns, including all residual failures.

Both routes still need the mixed atom budget

    Q=sup_x sum_(i:x in H_i) e^((mu+2)|H_i|)alpha_i<=1/4, (C26)

where each alpha product bounds the **joint coefficient-weighted
absolute integral** for every selected overlap group, with actual
local TV and full original readers. Disjoint groups must factor before
the logarithm. Separate scalar versions of (C11) cannot establish this.
Finally an invariant residual estimate such as
x'<=theta x+C x^2+e needs theta+CM<1 and
e<=(1-theta-CM)M, with initial x<=M; then Cx^2<=CMx proves invariance.
The vacuum, coupling and any other required relevant/marginal terms
have their own recursions. None has been constructed by this arithmetic.

## 5. Clauses 2–5 and the soft/hard decision

| LF-JMBR clause | Updated status | Exact remaining task |
|---|---|---|
| 2: joint original charge/reference/boundary | **OPEN**, with a new **PROVEN real extensive-sector instance** | Extend (C9)–(C11) from a filled flux tube to the local mixed bound (C14), paying every original fraction once. The crude local bound (C13) has the wrong volume dependence. |
| 3: common nonzero complex reference / local TV | **OPEN** | Establish nonvanishing and local total variations on D_* for these actual references. A real cap lower bound or a finite-volume analytic germ is insufficient. |
| 4: overlap types and full-reader sums | **OPEN quantitatively**; exact finite integration retained | Prove (C26), or JMBRA's weighted-reader alternative, on complete mixed groups. Neither a coarse shadow nor a flux label removes an original reader. |
| 5: every small return, failed branch and next step | **OPEN** | Construct the extraction and prove (C24), or a compatible (C25) plus nonlinear closure. Handle the localized/coherent complement not covered by the filled-sector charge. |

Clause 1 retains its finite algebraic PROVEN scope through (C20)–(C21),
without a new claim of bounded cell size, analytic domain or locality.

**ARGUED decision: keep the soft kernel; change the proposed renewal
accounting.** Renewal after charging has not been shown to fail. For
the displayed extensive family, the real all-cut comparison is positive
evidence for the charging route. The justified change is to retain an
original-action reserve, or a creation-conditioned sum (C25), and to
match/extract coherent sectors instead of demanding unweighted
pointwise smoothing. A bare Gaussian expansion at the rough template
needs a different treatment by (C16). None of this changes Decision 4.

SOFTHARD G1–G2 supplies raw analytic smoothing and a finite seam debit,
not the missing normalized return. Hardening to the same maximizing
map would retain the exact orbit (C4), since its mean has a unique
maximizer; it supplies no curvature return for this example. A different
hard/group-valued map could change that statement but requires its own
symmetry, reference, source and return construction. SOFTHARD §8.1's
HRT remains an OPEN comparison target. There is no demonstrated need
to switch to a hard kernel, and no universal superiority theorem here.

## 6. No-Go Discipline Gate — partial results, no exhaustion certificate

**N1, actual routes.** R1 probes one-use original-action charging, with
raw and actual-real-reference versions. R2 probes sector/background
reorganization. R3 probes complete-reader/fresh-gap operators. These
are three families, not five exhausted routes. Weighted remaining-credit
norms, non-Gaussian sector integration and the creation-map sum remain
live. No five-route packet PASS or all-route NO-GO is claimed.

**N2, dependencies.** Let J be the mixed complex matched bound (C14),
Z the reference nonvanishing/TV requirement, and I invariant extracted
iteration. J together with (C26)'s factorization/envelopes can construct
the reference logarithm and hence that part of Z. Z alone does not here
establish J; their remaining implications are unresolved. I requires
J/Z at its successive admitted states; one-step J or Z does not here
establish I. No pair is counted as independent obstacles.

**N3, premises.** The supplied compact model, even compatible tori,
filled original tube, disjoint partition and charged plaquette fractions
are explicit in (C1)–(C8). (C10) separately supplies a coupling ordering
and lower cut bound. Neither follows from framework axioms. Hypotheses
of all background/inverse/extraction estimates remain visible. The
registered units, kinetic-isotropy and realized-state primitives supply
none of these analytic estimates; no primitive is declared missing.

**N4, residual matches.** RENEW §§3–4 rules out uniform forward return,
not (C11); JMBRB B-MASS rules out repricing unchanged positive mass,
not (C6); BFT's small-curvature restrictions concern application at
(C4), not arbitrary sector mathematics; RD3 RC1–RC3 and RD4 L2–L8
retain the same all-cut denominator and full readers as (C9)/(C14).
The new saddle calculation concerns only the bare action, not a fixed-V
soft Hessian. No mismatched negative witness closes an alternative.

**N5, resolution.** Per plaquette: (C5) and (C16). Per link: the cap and
normalized-kernel inequalities in (C9), and (C17). Per mode: the one
collective negative direction of the bare Hessian. Per block/tower:
(C6)–(C8) and the filled-volume count. Lattice-wide: (C9)–(C12) are
real-sector estimates. No general local, complex, continuum, spectral
mass-gap or all-history impossibility conclusion is drawn.

**N6, partial closure.** Exact sector partitions, different matched
references, extraction maps and compatible weighted norms are mathematical
constructions. They require proof and no new physical axiom. No approved
primitive is reclassified as a missing derivation or an obstruction.

**N7, strongest counter-route.** Charge a large coherent ancestor once,
use a local paired reference to cancel the extensive debit of (C13),
then group every original reader with the small returned residual and
extract its relevant/marginal part. For sectors with no large charged
ancestor, establish nonlinear dilution or a new gap/failed-completion
price. A mixed (C14)/(C26) and (C25) estimate could close the problem
without a pointwise forward window contraction. The results here leave
this route open and give its filled-sector benchmark.

**N8, echo/search.** The named earlier lanes already corrected repeated
history prices, erased cone readers, zero seam bills and incomplete
background promotions. The present result retains those corrections.
Targeted local/main statement searches and their limits are in the log;
no comprehensive literature/open-PR novelty claim is made.

No numerical experiment ran: the required nice priority was denied and
the resource guard was not bypassed. Written proofs and the separate
fresh review supply the mathematical evidence. All source files and
editable prompts outside the allowlist are unchanged; no commit is made.
