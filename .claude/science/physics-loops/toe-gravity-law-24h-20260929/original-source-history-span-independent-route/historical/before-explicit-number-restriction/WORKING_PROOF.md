# Actual history spans, source time intervals and common winding support

Author analytic route under CONTRACT20283817. This proves an exact
history-span characterization and a time-support consequence for the supplied
rotor model. It does NOT prove the projected-input density in source-frame
section6. No scientific computation was used. Statements below concern the
actual complete histories from Omega and the derived positive-grade source,
not a chosen field wavepacket or an extra observed instrument.

## 1. Exact operator and preparation domain

Fix an even cubic torus L>=8, n=L^3/2 A sites, supplied three-state charges
0,+,-, integer rotors, and div E=q-1_A. Omega has A+, vacant B and E=0.
In the all-A-occupied sector let H_r denote NB=2r, total charge n. The
number of minus charges is r. Let P_r be its projection, 0<=r<=n/2.
These are orthogonal number sectors; they do not add observed marks.

With every primitive shift and charge retained, the landed local pair form
and compensation give

    Q=2 sum_{unordered a,c, dist(a,c)=2}(Fc Fa P0)*Fc Fa P0,
    h=KD-delta Q,             R=sum_mu b_mu* b_mu,
    b_mu=j_mu Fa P0,          A=-iKD+i delta Q-kappa R/2.       (1)

Here P0 in Fa P0 denotes W=0, rather than P_r with r=0. D is the actual
vacant-B-weighted electric multiplication operator:

    D=sum_{a~b, b vacant} E_ab(E_ab-q_a),                    (2)

with links oriented A to B. Integer E and q_a=+/-1 make each summand
nonnegative. D is self-adjoint on its multiplication domain in the physical
Hilbert space. No ellipticity or control of every field direction is assumed.
Q and R are bounded, positive and number preserving on this fixed graph.
For example the read sources give ||Q||<=38880n and ||R||<=300n.
All claims allow their actual smaller values. K,delta,kappa>0 are fixed.

The resolved mark is (edge,nu), nu=+/-1. The coherent alternative is the
original unnormalized j_edge,+ + j_edge,-, one label per edge. Both have
the same R, but their b_mu and history sums remain different. A resolved
b has norm<=5 and a coherent one <=10. Every b maps H_r to H_(r+1).
No path or sign component replaces a complete original coherent mark.

Write D_r,Q_r,R_r for the number restrictions, V_r=i delta Q_r-kappa R_r/2,
A_r=-i K D_r+V_r, and S_r(t)=exp(t A_r). h_r is self-adjoint and bounded
below by -delta||Q_r||. The real positive-time S_r is contractive. One
self-contained construction is to replace D_r by min(D_r,N), apply the
bounded dissipative exponential estimate, and take the strong limit in the
bounded-perturbation Dyson series. The free unitary groups converge strongly
on each compact real-time interval on each vector; the Dyson majorant is
summable. This proves contractivity and the actual no-event propagator
without differentiating arbitrary input vectors.

The source at center h with original local mark mu is

    T_(h,mu)=-F_h j_mu F_h P_(W=0).                       (3)

It is bounded (72 is a safe common bound) and maps H_r into W1, NB=2r+3.
It is a normal-form coefficient, not an additional measured jump. For
orientation, the positive-grade second commutator has
(1/2)[F,[F,j_mu]]P0=-F j_mu F P0+(1/2)j_mu F^2P0.
Outward hops at distinct A centers commute, including hard-core blocked
terms. The cross-center terms cancel, leaving exactly (3). The source
frame packet also independently reconstructs its complete local columns.
No microscopic finite-epsilon equality is asserted here.

## 2. Complete original history formula

For a label string m=(mu_1,...,mu_r) and strictly positive independent gaps
 g=(g_0,...,g_r), define

    v_m(g)=S_r(g_r)b_mu_r S_(r-1)(g_(r-1)) ...
                         b_mu_1 S_0(g_0)Omega.             (4)

The exact number block of the original rotor target state is

    rho_r(s)=kappa^r sum_m int_{g_i>0, sum g_i=s}
                           |v_m(g)><v_m(g)| dg_0...dg_(r-1). (5)

For r=0 this is the single no-event vector. In (5), g_r=s-sum_{i<r}g_i;
there is no additional surface-measure factor. Formula (5) follows by
iterating variation of constants for the bounded recycling maps in the
interaction picture of KD. The finite number of allowed births makes it
a finite sum over number blocks. Every no-event loss is already in S_r,
and every same-mark coherent alternative is inside b_mu. The factors
kappa^r are strictly positive and do not affect closed spans.

This construction gives trace-norm continuous rho_r(s)>=0, with trace<=1.
For any bounded map T out of H_r, T rho_r(s) T* is positive trace class and
trace-norm continuous. Equation (3), its dark/full-star compression, the
first-hop map F_h P_(h,3), and an ordinary bounded test observable are all
permitted T. No new field moment assumption on Omega is needed below.

## 3. Lower-half-plane extension with the actual loss

Set M_r=||V_r||, M=max_{0<=j<=r} M_j. For Im z<0 define S_r(z) by the
Dyson expansion along the straight segment from 0 to z:

    sum_{m>=0} z^m int_{0<u_1<...<u_m<1}
       e^{-izKD_r(1-u_m)} V_r e^{-izKD_r(u_m-u_(m-1))}
                         ... V_r e^{-izKD_r u_1} du.       (6)

Every free factor has norm<=1 because D_r>=0 and Im z<=0. Therefore

    ||S_r(z)|| <= exp(M_r |z|).                            (7)

The series converges in operator norm, uniformly on compact z sets in the
lower half-plane; the strong integrals have this same majorant. It is
holomorphic there and has strongly continuous real boundary values equal
to S_r(t). For example the free derivative bound
||alpha KD_r exp(-iz alpha KD_r)||<=1/(e|Im z|), for alpha>=0,
controls differentiation away from the real boundary; the value at alpha=0
is zero. Products and the uniformly convergent series then give the stated
holomorphy. Real boundary convergence follows from strong continuity of the
free groups and dominated convergence, without a norm-continuity assertion.

The complex semigroup agrees with real translation:

    S_r(x-iy)=S_r(x) S_r(-iy),       x,y>=0.                 (8)

For fixed x this follows from the real semigroup identity and scalar
boundary uniqueness, proved in the next paragraph, or directly from
Dyson composition. Contractivity on x>=0 and (7) imply the useful bound

    ||S_r(x-iy)|| <= exp(M_r y).                           (9)

The bounded loss is not dropped in either (6) or (9). Its contribution is
included in M_r. Constants may grow with n; no volume-uniform statement is
being extracted from them.

Here is the boundary uniqueness used above. A scalar function holomorphic
below an open real interval, continuous to it, and zero on that interval
extends to the reflected upper half-neighborhood by f(z)=overline(f(bar z)).
The two pieces are continuous and holomorphic across the interval: splitting
small contour integrals and taking their boundary limits proves this by
Morera's theorem. Its zero interval is then inside its holomorphy domain,
so the identity theorem makes it zero. In particular it is zero throughout
its connected lower half-plane domain and on its real boundary. This uses
zero boundary data, not an unjustified analytic extension of a probability.

## 4. A time window has the complete all-time history span

Let C_r(U) be the closed complex span of (4), all original label strings,
with g in any nonempty open U subset (0,infinity)^(r+1). Let C_r be the
corresponding all-positive-gap span. Then

    C_r(U)=C_r.                                           (10)

Indeed, if eta annihilates C_r(U), each scalar <eta,v_m(g)> vanishes on
an open real box inside U. Fixing all but one real gap, (6) makes it a
continuous lower-half-plane boundary function in that gap. Boundary
uniqueness extends its zero values to every positive value of that gap.
Repeating for all gaps proves zero on the full positive orthant. The same
argument applies after any fixed bounded T:

    closure span{T v_m(g):g in U}=closure(T C_r).           (11)

For every bounded nonempty open interval I subset (0,infinity), put

    Sigma_(r,T)(I)=int_I T rho_r(s) T* ds.                  (12)

By (5), this is the sum of positive rank-one integrals on
U_I={g_i>0:sum g_i in I}. Passing from (s,g_0,...,g_(r-1)) to all r+1 gaps
has Jacobian one. It is trace class, with trace<=|I| ||T||^2. A test vector
is in its kernel precisely when every scalar history pairing vanishes
almost everywhere on U_I. Continuity then gives vanishing everywhere on
that open set. Equations (10)-(11) prove

    closure Ran Sigma_(r,T)(I)=closure(T C_r),              (13)

independently of I. Finite sums over final source labels give the closed
span of their separate image spaces, not their coherent recombination.
Equation (13) is a support identity, not a positive uniform lower bound on
an infinite-dimensional range.

A fixed total time sum g=s is NOT an open set of independent gaps. If one
gap is varied complexly while keeping this sum, another must have opposite
imaginary part. Thus (10)-(13) do not prove fixed-time density or equal
support of rho_r(s) for every s. This distinction remains load-bearing.

## 5. Stronger scalar alternative along one history ray

For a fixed bounded T and test vector eta, define

    p_eta(s)=<eta,T rho_r(s)T* eta>.                        (14)

Either p_eta is identically zero for s>0, or p_eta(s)>0 for almost every
s>0 and its positive set is open dense. This scalar statement does NOT
say that the whole density is faithful almost everywhere.

To prove it, suppose p_eta(s_0)>0. Equation (5) supplies one original label
string and one interior gap tuple g* at total time s_0 with nonzero pairing.
Set u_i=g_i*/s_0, so u_i>0 and sum u_i=1. Consider

    f(z)=<eta,T S_r(u_r z)b_mu_r ... b_mu_1 S_0(u_0 z)Omega>.

It is holomorphic for Im z<0 and continuous to the real axis. In the fourth
quadrant, (9) gives |f(x-iy)|<=C exp(M y), with
C=||eta|| ||T|| product_j ||b_mu_j||. It is nonzero, since f(s_0)!=0.
Consequently g(z)=exp(-iMz) f(z) is a bounded nonzero holomorphic function
on that quadrant. Its positive-real boundary zeros have measure zero.

For completeness that last elementary fact can be seen without an
analytic-vector assumption. The map z -> z^2 sends the fourth quadrant
to the lower half-plane, and w -> (w+i)/(w-i) sends the latter to the unit
disk. On each compact positive-real interval the boundary change of
variables is smooth with nonzero derivative. A bounded nonzero analytic
disk function G cannot have zero radial boundary values on a positive-
measure boundary set: move a nonzero interior value to the disk center;
Jensen's formula gives the circle average of log|G| at radius t at least
log|G(0)|. With H>=sup|G|, the nonnegative functions log(H/|G|) therefore
have uniformly bounded circle integral. Fatou's lemma forbids an infinite
boundary value on a positive-measure set. Continuity at the boundary arcs
in question identifies those values with the given zero set. This proves
the fact and hence that f(s)!=0 for almost every positive s.

For each such s, continuity in the ratio tuple u supplies a positive-measure
neighborhood inside its r-dimensional simplex on which the complete
history amplitude stays nonzero. Its strictly positive kappa^r weight in
(5) implies p_eta(s)>0. For r=0 the same conclusion follows directly from
the single squared amplitude. Trace-norm continuity makes the positive set
open; its null complement makes it dense. This proves the alternative.

The same argument works for Tr(O T rho_r(s)T*) with bounded O>=0: choose
one nonzero vector pairing after O^(1/2). It never analytically continues
the positive expectation itself. For a countable collection of such fixed
nonzero tests, all are positive simultaneously on a dense G_delta set
whose complement has Lebesgue measure zero.

This mechanism has classical prior art: Hegerfeldt, 'Causality, particle
localization and positivity of the energy', quant-ph/9806036, section2,
proves the scalar alternative for unitary semibounded-H evolution. Its
complete displayed proof was read. The argument above supplies the actual
bounded-loss complex extension, sector changes, complete original marks
and positive history integration needed here; it does not directly apply
a unitary theorem to a nonunitary propagator. No historical novelty or
relativistic-localization claim is made.

## 6. Application to the actual checked winding family

Now require L divisible by4. Fix 4<=b<=n/4 and use exactly the dark-input
preparation label string, final source mark at c0=(4,2,0), and physical words
Xi_(b,w), w=1,2,..., in the checked winding proof633126b7 and receiptc9d99fc4.
For clarity that construction first births at (0,0,0) toward +e_y with its
selected outward +e_x component, then uses disjoint y-grid births, plus the
specified z birth, to occupy three neighbors of c0. The other three are
filled by the final complete source. A four-hop Q word transports the B+
on the x ring by four sites; L/4 such terms restore matter and add one
physical ring circulation. The proof retains the complete marked sums and
isolates a noncancelling extremal-field Taylor coefficient. It supplies,
for each w, an actual strictly positive source diagonal at sufficiently
small w-dependent time. Its no-event loss and electric-domain estimates
were read in full; no selected path is substituted for the actual history.

Write rho_b(s) for the exactly b-birth block of the actual target and T_mu
for that same final complete source. Then the fixed physical word test

    p_w(s)=<Xi_(b,w),T_mu rho_b(s)T_mu* Xi_(b,w)>             (15)

is not identically zero. Section5 applies separately to every w. Therefore
there is a set E_(L,b,mu) subset (0,infinity) that is dense G_delta and has
full Lebesgue measure such that

    p_w(s)>0 for EVERY integer w>=1 and EVERY s in E_(L,b,mu). (16)

The set is the countable intersection of the open dense full-measure
positive sets of (15). At each such COMMON source time, the actual source
has arbitrarily large noncontractible electric-circulation diagonal support
at one fixed matter configuration. The same is true of its dark compression,
since G Xi_(b,w)=0. Different w are orthogonal physical electric words.
An analogous conclusion holds for the non-dark family1<=b<=n/4.

This improves the earlier separate w-dependent-time statement without
asserting positivity at every time, a lower weight uniform in w, infinite
rank, phase-fiber faithfulness, or survival after a positive fast duration.
A rank-one state can have infinitely many nonzero basis diagonals. No tail
moment, mean residence, finite-spin transfer or microscopic energy/UI
conclusion follows from (16). All limits here keep the finite graph fixed.

## 7. Bounded resolvent words and the exact remaining consumer

Fix lambda0>0 and J_r=(lambda0-A_r)^(-1). These are actual bounded no-event
resolvents, ||J_r||<=1/lambda0, from contractivity. For a vector v in H_r,

 closure span{S_r(t)v:t>0}
   =closure span{J_r^m v:m=1,2,...}.                       (17)

One direction follows from the Laplace integrals of the semigroup and
its convolution powers. For the other, if eta annihilates every J_r^m v,
the norm-convergent resolvent expansion around lambda0 shows
<eta,(lambda-A_r)^(-1)v>=0 near lambda0. Analytic continuation in Re lambda>0
extends this to the whole right half-plane. Its Laplace representation and
uniqueness imply <eta,S_r(t)v>=0 for all t>0. For explicit uniqueness, fix
c>0 and take lambda=c+i y; these are Fourier transforms of the integrable
function1_(t>=0)e^(-ct)<eta,S_r(t)v>. Vanishing transforms imply that
continuous function is zero. The strong limit lambda(lambda-A_r)^(-1)v->v
also includes zero gaps by closure.

Applying (17) successively through bounded marks proves the exact countable
representation

 C_r=closure span{J_r^(m_r)b_mu_r J_(r-1)^(m_(r-1)) ...
                        b_mu_1 J_0^(m_0)Omega : all m_j>=1}. (18)

No converse from unbounded Taylor/Krylov powers has been assumed. Finite
field vectors permit individual derivatives, but that fact alone would not
justify density of polynomial-generator words in the semigroup orbit.

For P3=P_(h,3), put A_h=F_h P3 and M_h=closure Ran A_h. The separately
focused-checked input-kernel result45ef5bcb shows why A_h has a nontrivial
physical kernel and gives the sufficient consumer

    closure(A_h C_r)=M_h.                                 (19)

Equation (18) replaces C_r in (19) by explicit bounded resolvent words.
Equivalently, (19) says that no nonzero eta in M_h annihilates all those
A_h-images. More economically, only the relevant vectors j_mu*F_h*psi
from the dark source adjoints need be separated. By (13), the support of
int_I A_h rho_r(s)A_h* ds is exactly closure(A_h C_r), for any open I.
This identifies the actual positive operator whose faithfulness on M_h
would suffice, with the complete original history law retained.

For an actual dark vector psi, T_(h,mu)*psi=P3 T_(h,mu)*D_h psi.
Thus orthogonality to every actual source is precisely the bounded-word
condition obtained by pairing these adjoints against (18), for every
original mu. If (19), or its stated smaller adjoint-range separation,
were proved, the source frame lower bound removes D_(h,mix)psi. At present
neither (19) nor full projected-input density has been established by this
route. The common-time diagonal conclusion (16) does not establish either.

## 8. A diagnostic against the forbidden fixed-time inference

This is a finite-dimensional logical control, not the supplied rotor model.
Take two number sectors each C^2, a jump b=I between them, no later jump,
h_0=h_1=I+sigma_x>=0, R_0=I, R_1=0, and Omega=e_0. A one-birth history at
fixed total s is a scalar exp(-kappa g_0/2) times e^(-is h)e_0. Its fixed-time
span is one-dimensional, while varying s gives C^2. Projection onto e_0
has weight proportional to cos^2 s and vanishes at s=pi/2. All no-event
losses are the actual losses for this toy jump. This shows that even the
bounded-loss, semibounded-H, complete-history hypotheses do not upgrade
(13) to pointwise fixed-time support equality. Section5 allows such null
exceptional times and still applies correctly.

## 9. Scope of the attempted actual density attack

No additional exact linear symmetry restriction was found. Number, total
charge and Gauss constraints are already built into H_r. Spatial symmetries
permute observed labels and make the whole history span invariant; they do
not make each labeled history invariant. Zero winding after the first birth
is ruled out by the actual winding witness. Finite field bandwidth bounds
individual products but supplies no finite cutoff on the closed all-history
span. These observations do not constitute an exhaustive no-go search.

The literal input first-hop kernel is not an unreachable subspace: it need
not be invariant under KD, Q, the complete loss, or births at other centers.
Likewise high-density frozen occupation masks cannot be declared unreachable
without checking every incoming mark and coherent charge/field component.
No such invariant inaccessible physical subspace was constructed here.

The useful completed results are (10)-(13), the actual scalar time alternative,
(16), and the bounded-word consumer (18)-(19). The original strong target
remains open: show actual first-hop image reachability/separation, or exhibit
an actual source-invisible coherent subspace. Full fast invariant-module
elimination, uniform long-age estimates, growing-volume limits and physical
law/clock/record selection are outside this result. No formal review, audit,
retained status, source-branch mutation or scientific execution is claimed.
