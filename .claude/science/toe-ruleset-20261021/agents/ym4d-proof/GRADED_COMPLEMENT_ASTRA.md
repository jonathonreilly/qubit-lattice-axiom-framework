# Graded hard witnesses with a paid chart-collar comparison

**Author proposal; fresh independent review required.** This advances two
specific gaps left by [CS](CUT_SECTOR_COERCIVITY_ASTRA.md): the location and
complete reader size of a whitening witness, and the reference cost when the
actual exterior collar is in a small chart. It proves a normalized ORIGINAL-
CUT conditional bound for local hard witnesses, without resetting the field
to U0 or assuming that the strong-good event G is convex.

The resulting connected labels have a summable, support-weighted EXPECTATION
majorant. They are a cover, not an exact polymer representation or a local
original-source logarithm. The bounds cover both pieces of the original
complement within a specified small chart. The older G and Omega remain
unchanged; an extra stated margin is needed to place all of G in that chart. The complete complement divided
by the selected sector is not controlled. Fields outside the small chart,
arbitrary failure readers, and the probability-sensitive expansion needed
to use these hard witnesses remain open. Full 4D existence and the physical mass gap remain open.

```yaml
actual_current_surface_status: bounded-support
author_proposal_status: pending_fresh_independent_review
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

Bałaban and Dimock are the antecedents of the local-minimizer, buffer and
localization architecture. The specialized steps used here are rebuilt below.
This author also wrote CS and previously reviewed CC. CS's fresh independent
[LAND review](REVIEW_CUT_SECTOR_COERCIVITY_ASTRA.md) was read in full; it is
not an independent review of this new unit. All predecessors remain frozen.

## 1. Actual phase and a smaller full chart

Keep CS1--CS6 and SA1--SA2: d=4, SU(N), D=N^2-1, odd L>=3, coarse side T>=2,
fixed real coarse V of small plaquette curvature delta_V, and
`0<kappa_-<=kappa<=kappa_+`. Arbitrary compatible holonomies remain. Set
`m0=3L^4+1`, `n0=D m0`, `sigma^2=N/u`; below u>=N. All positive free links
in the exact pinned axial-tree gauge remain. Their probability-Haar product
has no extra FP factor; the integrated nonroot gauge volume is one.
The supplied Wilson/normalized paired S4-prime model is mathematical input,
not a derivation from the framework axioms or an adopted physical primitive.

Use U(a)=exp(a)U0(V) and the actual scaled coordinate action

    F_e(a)=sigma^2[-log w_e(U(a),V)-sum_free_links log j_N(a_e)],
    w_e=exp[-u sum_p(1+e_p)s(U_p)] product_c k_(kappa u)(V_c;M_c),
    F_e=F_0+sum_p e_p W_p(a),    W_p=N s(U_p) on real fields.       (GC1)

Here e denotes REAL original Wilson coefficients. The kernel coupling is
fixed. Additive constants in F_e may be retained; only an identical local
constant cancels in an explicitly displayed conditional ratio. Haar's
constant h_N is outside F_e and its density j_N occurs once inside it.
The exact compact kernel normalizer, its vacuum and all finite-u terms stay
in F_e. The classical/tree energy of CS3 is a different function.

The needed full-chart fact is already CB8--CB14; it is not new convexity of
G. Here is its actual specialization, including a source interval fixed
before p or u. At zero the real Hessian is

    K_b=H_V+E_V+kappa(1-c_N(kappa u)) B_V+N^2/(6u) I,
    K_b>=gamma I,   ||K_b||_(row,HS),||K_b||_(column,HS)<=b1.       (GC2)

H_V is the covariant Wilson/mean-path form, B_V the nonnegative path spread,
and the last term is Haar. CB's flat lifted brick proof retains the T=2 seam
qualification; its Wilson curvature error is <=24 delta_V in both row and
column block norms. No mode is deleted. The fixed-real-t single-normalizer
and Haar analytic vertices give finite constants C,B_epsilon,G,R_K with

    ||F_e''(a)-K_b||_(row,HS) <= C r+B_epsilon rho,
    ||F_e'(0)||_(infinity,HS) <=G(1+rho)delta_V,
    ||K_b^(-1)||_(infinity,HS)<=R_K                         (GC3)

on the full real product HS ball ||a||_(infinity,HS)<=r and |e_p|<=rho.
The column bound is the same by symmetry. These are CB9--CB14's constants:
C from its finite local third-derivative sum, G=6sqrt(N), and R_K from CB11.
Every local vertex reads finitely many actual links; the normalizer is
controlled after its identical vacuum is subtracted, not discarded.

Choose r>0 and a fixed rho>0 so that

    r<=min(r_CB,epsilon_1/8),   C r<=gamma/4,   R_K C r<=1/4,
    rho<=min(1/2,rho_SA,rho_FR,gamma/(4B_epsilon),
                                      1/(4R_K B_epsilon)),
    lambda=gamma/2,   B=max(1,b1+C r+B_epsilon rho),
    B_b=2R_K G(1+rho),   B_b delta_V<=r/4.                         (GC4)

rho_FR refers only to the corrected, independently confirmed FR domain when
that selected-sector comparison is used; omitting FR leaves the real theorem
unchanged. All constants are chosen before u,T,p. Also retain the supplied
CB/SA curvature domain. The map a -> a-K_b^(-1)F_e'(a) has contraction constant
<=1/2 on the r ball and sends zero to norm <=B_b delta_V/2. Thus it maps the
ball into itself, and its unique critical point b_e satisfies

    ||b_e||_(infinity,HS)<=B_b delta_V,
    lambda I<=F_e''(a),    ||F_e''(a)||_(row,HS)<=B
                   throughout that full real r ball.                    (GC5)

Uniqueness identifies it with the admitted CB/SA branch. These are statements
about the complete finite-u coordinate density on a convex product of HS
balls, not the hard event G or a global compact-group minimizer.
The Hessian has range at most two coarse graph steps. Actual coefficient
readers fit inside the radius-three coarse collar; these are distinct facts.

Write C_s(A) for the condition that all free links owned by coarse blocks A
have the unique relative traceless HS logs of norm <=s. The original interior
cut is automatic on C_r(A) for its blocks: internal U0 links are I and four-
factor telescoping gives defect <=4r<=epsilon_1/2. Strict-cut boundaries cause
no problem. Keep the original strong-good thresholds delta_f,eta and the
original G unchanged. Define the additional full-chart event

    C_ch=C_(r/2)(all blocks),   G_r=G intersect C_ch.                           (GC6)

The main cover below is proved on C_ch itself, so it applies to both pieces
of the original complement inside C_ch. There is an OPTIONAL stronger
parameter margin: CB21--CB24 imply G subset C_ch if the already chosen
thresholds satisfy 2sqrt(N)(30L^2 delta_f+eta)<r/2, together with their
trace and curvature margins. We do not rechoose the older thresholds to
invoke this. If that inequality is unavailable, G\C_ch remains explicitly
in the unestimated outside-chart portion. For sufficiently large u the
actual selected cube lies in G intersect C_ch: retain its original SA/FR G
margins and also impose `B_b delta_V+sqrt(D)sigma p M_C<r/2`, with
M_C a scalar absolute row bound for C_0 from SA14. No cube rotation
invariance is used; a component cube generally changes under colour rotation.

## 2. Full-reader graded whitening witnesses

Fix one SA box construction at a fixed input support rate beta>8. Denote
its fixed box side parameter by R_A, its maximal population by
`n_A=n0(2R_A)^4`, and `v_A=(2R_A)^4`. The periodic product-box adjacency graph
has degree at most eight, also when some directions contain one or two boxes.
Here adjacency means sharing a face: SA5--SA14 assign the full rectangular
D_q collars and the full radius-three local vertex stencils, already
charged in their e^(beta s) bounds. These labels are face connected; their
products share an index box. No merely diagonal support or diameter bound
is substituted for these full labels. Use the actual full-colour matrices

    K_*=F_0''(b_0),  C_0=K_*^(-1/2),  T_*=K_* C_0=K_*^(1/2).              (GC7)

SA14 supplies connected atoms for C_0 and K_*=K_b+Delta_0 with finite scalar
row, column and full marked-reader bounds Q_beta. K_b's local entries are
assigned their complete original-V stencil; the Delta_0 atoms retain every
background/read connector. In a product, both labels contain the summed
index, so their union is connected and contains the two surviving endpoints.
Directly summing the intermediate index gives

    M(AB)<=M(A)M(B),
    Bmark(AB)<=Bmark(A)M(B)+M(A)Bmark(B),
    Q_beta(T_*)<=Q_beta(K_*)Q_beta(C_0)=:M_*,  M=max(1,M_*).               (GC8)

Here Bmark is SA's full scalar reader-incidence norm, not the block row
constant B of GC4. Aggregating absolutely convergent terms with the same
label S gives T_(ij;S), with connected S containing the boxes of i,j and
all original coarse data read by that coefficient. The complete colour
count is already in Q_beta. No operator-norm-to-row-norm replacement occurs.

For any fixed 0<nu<=beta,

    sup_i sum_(j,S) |T_(ij;S)| exp(nu(|S|-1)) <=M,
    sup_i sum_j |T_ij| exp(nu d_box(i,j)) <=M.                            (GC9)

Connectedness gives d_box(i,j)<=|S|-1, proving the second estimate from the
first. In particular a white violation y=sigma^(-1)T_*(a-b_0), |y_i|>p,
implies some pair (j,S), S containing i,j, with

    |a_j-b_0,j|>theta_k,   theta_k=theta_0 exp(nu(k-1)),
    k=|S|,                 theta_0=sigma p/M.                            (GC10)

Otherwise absolute summation with GC9 bounds |y_i| by p. This proves a cover,
including the strict inequality issue. The weaker distance-graded version
follows by using the second row estimate. We retain S itself rather than
replacing it by a shortest path: a path need not contain the matrix atom's
original-data readers.

Assume the explicit curvature margin

    B_b delta_V<=theta_0/(4pi).                                          (GC11)

It also bounds every scalar component of b_0. A violation in GC10 implies
||a_link(j)||HS>3theta_k/4. On the admitted traceless chart,
`|exp(A)-I|_n>=2||A||HS/(pi sqrt(N))`, where |.|_n=HS/sqrt(N).
Consequently the following local, source-independent group event covers it:

    E_(j,k)={|W_link(j)-U0_link(j)|_n>theta_k/(pi sqrt(N))}.               (GC12)

Repeated colour coordinates on one link are counted below, not identified
with independent events. This invariant chord cover does not make the
original white cube invariant or alter its definition.

## 3. Conditional minimizers with their actual boundary displacement

Let R be any set of coarse blocks, J_R all free positive links owned by R,
and m_R=m0|R|. Take the exact original-cut conditional on these free variables,
as in CS6. Its local action contains every Wilson plaquette and normalized
kernel reading J_R, and its chart phase F_(e,R) also contains the Haar logs
of J_R. No frozen original ungauged exterior conditional is substituted.

Let N_s(R) be the periodic coarse sup-distance-s enlargement. Require only
that the actual exterior free variables in N_2(R)\R satisfy C_(r/2).
All nonlinear field readers of the local action lie there or in R. Values
farther away may be arbitrary admissible compact fields. Original-V readers
and the fine tree paths used to compute these free coordinates are included
in N_3(R). These enlarged collars intentionally overcount the exact readers.

Minimize the ACTUAL phase F_(e,R)(a_R;z,V) over the closed product C_r(R).
Its unique minimizer q_R can be at the chart boundary. Let
`d=q_R-b_e|_(J_R)`. Fill the irrelevant far exterior by b_e and interpolate
linearly from b_e to (q_R,z) on the complete local field readers. All values
stay in the full r chart. Integrating the exact Hessian along this segment
and using F_e'(b_e)=0 gives

    H_RR d+f+n=0,
    f=H_(R,Rc)(z-b_e),
    H>=lambda I,  ||H||_(row,HS),||H||_(column,HS)<=B.                    (GC13)

The normal n belongs to the product-ball outward normal cone at q_R.
For each whole HS link block i, <n_i,q_R,i-b_e,i> >=0, since b_e is inside
that ball. The vector f vanishes more than two graph steps from R^c and
||f_i||HS<=B r. H is a segment-averaged Hessian, not a constant Gaussian
precision or a Hessian evaluated only at b_e.

Choose a fixed m>0 with B(exp(2m)-1)<=lambda/2. For a core block x in R,
put W_i=exp[-m d_graph(owner(i),x)] on each entire colour block. The range-two
row and column bounds give

    ||W H_RR W^(-1)-H_RR||op<=B(exp(2m)-1)<=lambda/2.

Multiplying GC13 by W and pairing with Wd, the normal term is nonnegative
because W is scalar on each HS ball. Therefore

    ||Wd||_2 <= (2/lambda)||Wf||_2.                                      (GC14)

No coordinatewise maximum principle is assumed. The nonnegative KKT term
is retained rather than declaring q_R an unconstrained critical point.
The periodic lattice sum is bounded by
`Q_m=sum_(Z in Z^4)exp(-m|Z|_1)=coth(m/2)^4`. If the core distance to the
exterior boundary is at least ell, the boundary layer has distance at least
ell-2. Splitting its squared exponential into two factors proves

    ||q_R,i-b_e,i||HS<=C_bd r exp[-m(ell-2)/2],
    C_bd=(2B/lambda)sqrt(m0 Q_m),                                        (GC15)

for a free link owned at x. Every periodic point is counted by a nearest
lift; the infinite sum is an upper bound, not a discarded winding sum.
If R is the whole torus, f=0 and q_R=b_e exactly. Thus no extensive vacuum
or curvature cost is introduced by this comparison.

## 4. Paying the original denominator, including a boundary minimum

Denote the true conditional denominator by D_R(z,V,e). It integrates the
original compact variables with their original interior cut. The convex
chart C_r(R) is a subset of that cut. We use it only as a lower bound for
D_R, not as a replacement domain or a cap required to stay in nonconvex G.

The exact coordinate density there is `h_N^(m_R) exp(-F_(e,R)/sigma^2) da_R`,
up to a common exterior factor. Put a_cap=r/8 and eps=a_cap sigma^2; u>=N
ensures eps<=r/8. Center an independent Euclidean D-ball of radius eps at
`(1-2eps/r)q_R,i` for every free link. Every ball is strictly inside C_r(R),
and its points are within 3eps of q_R,i. By GC5 and the critical equation at
b_e, each local gradient along these segments is bounded by 2B r. Thus

    D_R>=h_N^(m_R) exp[-F_(e,R)(q_R)/sigma^2-6B r a_cap m_R]
                         [v_D a_cap^D sigma^(2D)]^(m_R),                 (GC16)

where v_D is the Euclidean unit-ball volume. The possible linear KKT cost
has been paid. A sigma-radius quadratic cap at a constrained boundary
minimum has NOT been assumed.

Strong convexity and the variational inequality at q_R imply throughout
C_r(R)

    F_(e,R)(a)>=F_(e,R)(q_R)+(lambda/2)||a-q_R||_2^2.                      (GC17)

On an event ||a_i-q_R,i||HS>=t for a specified free link, reserve half this
quadratic decay for the event. Bounding the remaining ordinary Lebesgue
integral by its full Gaussian integral, and dividing by the actual cap in
GC16, proves

    nu_(R,cut)^e(C_r(R) and ||a_i-q_R,i||HS>=t | z,V)
       <= min{1, P_R(u) exp[-lambda t^2/(4sigma^2)]},
    P_R(u)=[C_cap sigma^(-D)]^(m_R),
    C_cap=max{1, exp(6B r a_cap)(4pi/lambda)^(D/2)/(v_D a_cap^D)}.          (GC18)

The Gaussian integral is an upper bound derived from GC17, not the
conditional law. Its covariance has not replaced any group kernel.
The factors h_N and exp[-F_(e,R)(q_R)/sigma^2] cancel IDENTICALLY in this
conditional ratio. The compact normalizer was kept inside both phases;
no u-dependent normalizer or source vacuum was dropped or renamed harmless.
Source-only factors outside the reader set remain in the exterior measure.

More generally, for any nonnegative bounded exterior factor B_out and any
fixed exterior event C_ext imposing the above chart collar, disintegration
gives the GC18 factor times `E_(nu_cut^e)[B_out 1_C_ext]` on the right.
This is an actual original-cut probability comparison. At exterior points
of zero history mass only the raw integral version is asserted.

## 5. Local witnesses, complete labels and their summable expectation

Choose the common buffer

    ell=2+ceil[(2/m) log_+(4pi C_bd r/theta_0)],
    R_j={X:d_infinity(X,owner(j))<=ell},
    v_ell=(2ell+7)^4,
    P_ell(u)=[C_cap sigma^(-D)]^[m0(2ell+1)^4].                           (GC19)

The ceiling applies to the whole nonnegative expression; log_+ t=max(0,log t).
The torus may wrap or the region may be the whole torus; its population is
at most the displayed cube count. GC11 and GC15 give
`||q_(R_j),link(j)||HS<=theta_0/(2pi)` whenever the exterior collar is small.
On the chart, GC12 implies `||a_link(j)||HS>theta_k/pi` by the opposite
inequality `|exp(A)-I|_n<=||A||HS/sqrt(N)`. Consequently its displacement
from q_R is greater than theta_k/(2pi).

Define the genuinely local hard witness

    H_(j,k)=1_(C_(r/2)(N_2(R_j))) 1_(E_(j,k)),
    c=lambda/(16pi^2 M^2).                                              (GC20)

All original fine-variable and original-V readers of H_(j,k) are contained
in N_3(R_j), including the trees at the endpoints of crossing free links.
Its threshold and chart indicator are independent of the original source e.
Condition on J_(R_j), use the exterior part of its chart indicator, apply
GC18 and retain that exterior factor. In particular

    E_(nu_cut^e)[B_out H_(j,k)]
       <=P_ell(u) exp[-c p^2 exp(2nu(k-1))]
          E_(nu_cut^e)[B_out 1_(C_(r/2)(N_2(R_j)\R_j))]                  (GC21)

for B_out independent of J_(R_j). This formula pays the conditional
reference cost under its stated collar. It does not assume such a collar
for arbitrary fields. For a numerator restricted to C_ch, this local collar
condition is a consequence of that numerator event itself. This includes G_r, and
includes all of G only under the optional stronger GC6 margin.

For each (i,j,S) of GC10 assign the complete connected original-block label

    Gamma(i,j,S)=fill(S) union N_3(R_j),
    |Gamma|<=v_A |S|+v_ell.                                             (GC22)

Here fill(S) fills every original block in every SA box of S. The two pieces
meet at j's box. The full matrix-atom readers stay in fill(S), and the
actual hard witness, phase and tree readers stay in the other piece.
The pointwise cover is

    1_(C_ch) 1_(|y_i|>p) <=sum_(S contains box(i),j in I(S)) H_(j,|S|).         (GC23)

Because the real affine map is invertible on the relative chart, a point
of C_ch outside the actual Omega has a white-coordinate violation. Thus the
cover concerns the actual selected sector, including (G\Omega) intersect C_ch.
The sum may include labels with zero matrix coefficient; this only enlarges
it. It is not an equality, a partition, or an analytic pullback of a hard
indicator. Selecting a first successful witness would impose extra readers
and is not silently done. On C_(r/2), |W-U0|_n<=r/(2sqrt(N)); thus witnesses
are empty once theta_k>=pi r/2, but the upper bounds may harmlessly sum all k.

The label multiplicities are explicit. A connected k-set in the box graph
containing one given box has at most A^(k-1) possibilities, A=8^2=64:
a deterministic spanning-tree depth-first walk has length 2(k-1), at most
eight choices per step, and its visited set determines the set. Each such
set has at most n_A k scalar coordinates. For a fixed ORIGINAL block v,
labels containing v have the following bound at size k:

    N_v(k)<=A^(k-1)[n_A^2 k^2+n0 n_A v_ell k].                           (GC24)

The first term is v in fill(S). In the second, j is within ell+3 of v,
giving at most n0 v_ell choices, then S contains j and i lies in S.
This counts both endpoints, all colours, repeated labels and the full
remote support incidence. Short tori only reduce these upper counts.

For any fixed original-block support rate tau>=0 define the positive
support-weighted EXPECTATION sum

    B_tau=sup_v sum_(i,j,S:v in Gamma) exp(tau|Gamma|)
                                      E_(nu_cut^e) H_(j,|S|).            (GC25)

It is uniform in admitted real V and real original sources. If

    2nu c p^2>=log A+tau v_A+2,

then GC21 and exp(2nu(k-1))>=1+2nu(k-1), followed by the geometric sums of
k and k^2, give, for example,

    B_tau<=C_tau(1+v_ell) P_ell(u) exp[tau v_ell-c p^2],
    C_tau=10(n_A^2+n0 n_A) exp(tau v_A).                                 (GC26)

This is stronger than losing the white root in an all-volume union. It is
still NOT a norm bound for local analytic activities: the normalized
expectations themselves depend on the exterior measure and its full source
normalization. Only their unintegrated hard witnesses have the declared
local readers. No locality of an integrated probability is asserted.

## 6. Buffer entropy, fixed sources and simultaneous witnesses

All constants above are fixed independently of u,p,T. Since p>=1 and
sigma=sqrt(N/u), GC19 gives ell<=c_ell(1+log u), where one may take
`c_ell=3+(2/m)log_+(4pi C_bd r M/sqrt(N))+1/m`. In d=4,

    log[C_tau(1+v_ell)P_ell(u)]+tau v_ell
                                      <=C_entropy(1+log u)^5.            (GC27)

Indeed m_R=O(ell^4), log sigma^(-D)=(D/2)log(u/N), and the extra support
weight costs O(ell^4). This explicitly pays both buffer growth and the
linear-cap penalty. No uniform constant-size buffer was assumed.

For p=(log(2+u))^alpha with ANY fixed alpha>5/2, the finite threshold u0 can
be chosen so that the first condition preceding GC26 and
`C_entropy(1+log u)^5<=c p^2/2` both hold. Then

    B_tau<=exp(-c p^2/2).                                               (GC28)

At alpha=5/2 a sufficiently large fixed leading amplitude would also suffice
for these bounds. The choice p=sqrt(log u) does not absorb our proved cap
entropy. This is a limitation of this bound, not a theorem that that cutoff
can never work. Every fixed logarithmic power still has sigma p^3 ->0.
Choose delta_V<=min(delta_A,delta_CB,r/(4B_b),sigma p/(4pi M B_b)) and,
when matching FR, its c_* sigma p window. All selected-sector chart/G/cut
margins then hold for large enough u. The OPTIONAL G subset C_ch condition is a fixed
threshold condition; it does not follow from increasing u. The original
source disc stays FIXED: it was selected in GC4, and corrected FR3/FR22 admit this logarithmic p. No rho p^2 condition
is reintroduced as if it were a fixed-radius conclusion.

The same logarithmic p satisfies the frozen [IC20](INTERACTING_SELECTED_CORE_ASTRA.md)
conditions `sigma p^3<=r_z/2` and `sigma^2 p^12<=1` for sufficiently large
u, since u^(-1/2)(log(2+u))^(3alpha) and
u^(-1)(log(2+u))^(12alpha) both tend to zero. Its additional analytic
margin still has to hold. This is only compatibility with IC's source-free
selected-sector domain; no IC theorem is a premise here and no white-ball
sector is substituted for the cube. It supplies none of the missing
source/history, outside-chart or selected-reference comparisons.

There is also a genuine simultaneous-event statement. If the local witness
reader sets N_2(R_j) for different chosen links are disjoint from every
other integration region R_i, then their hard factors are exterior factors
for each other's conditional integration. Apply GC21 successively and drop
only its remaining indicator, which is <=1. This proves

    E_(nu_cut^e) product_(a=1)^s H_(j_a,k_a)
       <=product_(a=1)^s min{1,P_ell(u)
                            exp[-c p^2 exp(2nu(k_a-1))]}.                (GC29)

No independence assumption is used. The minimum with one is valid by using
the trivial conditional bound when needed. For distinct underlying free
links, coarse sup-distance greater than 2ell+6 between owners suffices. A conflict
neighborhood has at most `m0(4ell+13)^4` such links, so greedy selection
keeps at least that reciprocal fraction of any set. Coincident colour tags
or levels on the same link must first be coalesced (retain the largest
threshold); they cannot be counted as independent defects. For sufficiently
large u, an intersection of s distinct underlying-link witnesses of any
levels k>=1 is therefore bounded by
`exp[-c p^2 s/(2m0(4ell+13)^4)]`. The packing loss is O((log u)^4),
explicit. GC29 is not an all-orders connected source expansion for the
nonlocal white violation set.

## 7. The portion of G^c inside the chart, and the remaining large fields

Both complementary integrals remain. There is a second direct application
of the same conditional estimate to `C_(r/2) intersect G^c`. Assume also
`delta_V<=delta_f/2`. If a fine plaquette violates delta_f, four-factor
telescoping about U0 gives a free link in that plaquette with HS log norm
at least delta_f/8. Tree logs are zero. If an actual straight root path
violates eta, its length L and its reference product V_c give a free link
on that path with HS log norm at least eta/L. Set

    a_def=min(delta_f/8,eta/L)>0,
    B_b delta_V<=a_def/4,
    ell_def=2+ceil[(2/m)log_+(4C_bd r/a_def)].                            (GC30)

The corresponding constrained minimizer has core norm <=a_def/2. A local
witness consisting of the full C_(r/2) collar and the event
`||a_link||HS>=a_def` therefore has the actual original-cut bound

    P_(ell_def)(u) exp[-lambda a_def^2 u/(16N)].                         (GC31)

Here ell_def and its complete support size are fixed independently of u.
The local log is only evaluated on that chart. For a specified bad plaquette
there are at most four edge choices; for a specified root mismatch at most
L. Counting positive plaquettes and coarse links per block gives the crude
marked incidence constant `(24L^4+4L)(2ell_def+9)^4` (the extra layer
allows the defect base to differ from its witness owner); any additional fixed
support weight is also explicit. These bounds concern this chart portion
of G^c, not all dirty or failed histories.

The whole `C_ch^c` inside the original cut remains unestimated. It includes
`G\C_ch` if the optional stronger GC6 margin is unavailable, as well as
`G^c intersect C_ch^c`. The original G is not enlarged or shrunk to hide either
piece. Since Omega subset C_ch on the stated margins, both are actual
complement contributions. There GC5 is unavailable. CS25's
absolute-energy/reference comparison still retains its actual boundary cost.
This unit has not shown that a connected organization of those large regions
pays that cost. Enlarging a region without charging its volume or applying
GC5 outside its chart would not supply the missing estimate.

## 8. Histories, complex sources and the unchanged return identity

For H24's actual positive returned gas, including its empty term, the
conditional log oscillation under changes of J_R is <=2|K_R|d_q, with K_R
the complete changed-link endpoint block set. On H's exact source/u/
completion domain, and only when K_R avoids every complete retained-failure
reader, multiply GC18, GC21 and their raw integrated forms by
`exp(2|K_R|d_q)`. This is the same positive tilt proof as CS33: conditional
numerator and denominator differ by at most the log oscillation. Its
O(ell^4) cost fits GC27. Failure factors intersecting K_R are not covered.
A noninvariant retained insertion requires its exact tree average, or a
uniform statement at each fixed nonroot gauge before integration.

For complex original epsilon in the fixed disc, e=Re epsilon is in GC4's
real interval and `|w_epsilon|=w_e`. Each final hard witness and its chart
collar is independent of epsilon. The raw complex integral is therefore
bounded by the corresponding positive real-source integral. If H is used,
its exact numerator/compensator/finite-gas inequality retains the positive
Re(epsilon) HISTORY mass. A source-dependent global vacuum is not removed.
There is no complex conditional normalization or conclusion of its
nonvanishing. The source-dependent constrained minimum is used only inside
the real proof; no hard indicator is transported through it analytically.

The exact identity remains

    Z_cut(V,epsilon)=Z_sec(V,epsilon)
       +integral Haar chi_cut 1_(G minus Omega) w_epsilon
       +integral Haar chi_cut 1_(G^c) w_epsilon.                           (GC32)

Corrected FR proves nonvanishing for the first term on its admitted fixed
source domain, not for the sum. Our real estimates use Z_cut(V,e) as the
reference mass; replacing it by Z_sec(V,epsilon) or Z_cut(V,0) is an unpaid
comparison. This remains true even for the G-minus-Omega contribution.
After an H8 return, an insertion reading a replaced interior must occur
inside H8's JOINT replacement integral to identify the pre-return event.
H14 with no additional insertion does not erase that requirement.

## 9. Exact missing consumer, literature and evidence

[RD's fresh review](REVIEW_RD.md) gives HOLD for the requested returned-
denominator theorem. Its B2 applies here: a hard indicator attaining zero
has ||Theta-1||infinity=1. Our integrated majorants do not satisfy RD18's
small supremum-defect hypothesis. A probability-sensitive expansion with
actual interacting exterior integration, or another proved consumer norm,
is still required. RD's exact effective-level/history identity and full
hole-norm/reference comparison (B1/B3) are not supplied by this unit.

This work does not differentiate a hard indicator in a complex covariance
weakening parameter. It gives a positive cover and real integrated prices.
[Dimock1212.5562v2, sections3.12--3.13](https://arxiv.org/html/1212.5562v2#S3.SS13)
uses a product fluctuation normalization, then analytic weakening of both
the propagator/square root and the background. Lemma3.15 separates bulk and
boundary terms; stepH attaches entire exterior components but measures tree
length modulo those holes. Here every attached original block is charged.
That distance-modulo-holes estimate and its analytic hypotheses are not a
full-cardinality hard-history theorem for this gauge cut.

[Bałaban, CMP122(1989), printed355--358](https://scispace.com/pdf/large-field-renormalization-ii-localization-exponentiation-h8b7ih93xo.pdf)
explicitly analyzes the dangerous denominator action, stationarity and a
localized quadratic comparison before exponentiation. His hard-block
constraints, minimizer estimates and coupling assumptions are different.
Our KKT comparison, original-cut cap and its log^5 entropy are derived above;
no theorem or constant from that paper is used as an unproved replacement.

No new numerical experiment was needed or run. Mechanical hash, source and
link checks are identity evidence only. Prior CC/CS/FR failures, corrections
and evidence are unchanged; none is relabelled as a check of this unit.
The read manifest records complete versus partial coverage and the confirmed
FR polynomial-moment correction. No third-party PDF is committed.

The remaining load-bearing steps are: a connected original-reader expansion
that accepts the proved probability-sensitive hard witnesses; the actual
exterior payment for fields outside C_(r/2); the selected-sector reference
comparison and complex nonvanishing of 1+B_comp; and the full H8/effective-
level/hole interfaces. Nonlinear multilevel flow, continuum existence and
the physical mass gap remain open. These are not impossibility claims.

[PROCESS_LIGHT](PROCESS_LIGHT.md) and the coordinator's file boundary govern.
Only this source and checks/graded_complement_* are authored. The
[read manifest](checks/graded_complement_read_manifest.json) and
[receipt](checks/graded_complement_receipt.json) freeze the scoped source for
a new independent review. No Git, shared status, lock, audit or ledger edit
is part of this author unit.
