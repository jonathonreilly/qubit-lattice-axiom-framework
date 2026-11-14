# SPURION — mixed connections, exact Haar elimination and the mass question

**No independent gauge-breaking local gluon-mass counterterm is required by
the exact normalized scheme. Its coefficient in a local, invariant,
single-connection action is zero. Mixed relative-field quadratic terms do
survive, including the prescribed blocking term; their survival does not
imply a new physical tuning parameter. The actual all-history LC1 local
representation and its uniform coefficient bounds remain OPEN.**

The brief's alternatives need one correction: “survives, therefore must
be tuned” is not a valid implication. A fixed reference/blocking term, or
an exactly recorded coefficient of a conditional action, can survive
without an adjustable bare counterterm. Restoring joint covariance does
not remove an independent relative field either. Sections 2–4 prove both
points, including an integrated SU(2) example.

| Requested item | Disposition |
|---|---|
| Classify the actual mixed readers | **PROVEN** finite algebraic classification in §2, closed under the exact operations generating the state. A history-uniform small local expansion of those objects is **OPEN**. |
| Remove coordinate/frame spurions | **PROVEN** when the background is a covariant function of the remaining field and no independent fluctuation/exterior reader remains. BFT's analytic extension keeps its stated hypotheses. |
| Cancel by coarse Haar integration | **PROVEN** for unread normalized outputs and complete partitions. Blanket cancellation in the presence of readers is false, §4. |
| Surviving lower-dimensional terms | **PROVEN** relative quadratic sector, its finite-sector counts and explicit coefficients, §§3–4. General selected-history coefficient functions and budgets are **OPEN**, not declared tunable constants. |
| Assemble Loc, LC1 | **PROVEN** conditional symmetry assembly and finite mixed-chart projector, §6; **ARGUED** their integration into the real RG contract; full LC1 is **OPEN**, §7. |
| Physical mass and AF | **PROVEN** exclusion of a symmetry-breaking local single-field mass and exact preservation under reference splits. Uniform causal AF/other-coefficient estimates are **OPEN**. No physical mass gap or continuum existence conclusion follows. |

PROVEN means a written result at its displayed scope, not an audit or
retained-grade decision. This is a source snapshot without git metadata;
the LOCOP commit named in the brief is not independently certified here.
Source hashes, checks and fresh hostile review are recorded in
[SPURION_LOG.md](SPURION_LOG.md). Only this note, its log and
`checks/spurion_*` are authored. No commits or ledger changes are made.

Method credit: Tadeusz Balaban's gauge RG organization and Jonathan Dimock's
large-field organization, as credited in the supplied sources; LOCOP's
finite-test construction also credits Brydges and Slade. All new algebra
needed below is proved here. No external theorem or memory-only [m] item
carries an argument. The explicit AUTHOR/PROCESS_LIGHT lane contract
governs this bounded task, rather than an unattended campaign workflow.

## 1. Objects, readers and the scope of covariance

Use REALRGA RGA1–RGA7: finite compatible four-dimensional SU(N) lattices,
N>=2, odd L>=3, probability Haar, t_j=kappa u_j>0, original invariant
sources J with the kernels and u_j frozen under their derivatives. The
complete field jet order is six, source order four, with the labelled
source alternative and all original readers. Fine fields include every
still-retained earlier level. Empty/zero history fibres are not logged or
divided by. Constants in the eventual contract must be uniform in history,
depth, volume and cutoff; finite existence is not that estimate.

For U_b^g=g_x U_b g_y^-1 the paired contours have common endpoints at
coarse roots. Their arithmetic mean obeys

    M_c(U^g)=g_(c_X) M_c(U) g_(c_Y)^-1,
    k_t(V;M)=exp[t Re tr(V* M)/N]/Z_t(M),
    Z_t(M)=int exp[t Re tr(W* M)/N] dW.                 (S1)

Interior gauge matrices telescope on each contour. Bi-invariance of Haar
then gives k_t(V^g;M(U^g))=k_t(V;M(U)) and int k_t dV=1.
This proves exact covariance without polar decomposition or an expansion.

The actual transfer and matched reference are

    R_h(V;J)=int rho_(j,h)(U;J) K_j(V,U)dU,
    Z_A(V)=int chi_A(U)b_j(U)K_j(V,U)dU,
    Q_h=R_h/Z_A,     b_j=exp[-u_j sum_p s(U_p)].        (S2)

Here rho, with its full ancestry and absence conditions, is not b_j.
Partial integrations leave eta, the unintegrated fine/hole/collar data,
as arguments. Thus a local returned quotient is generally Q_h(eta,V;J),
not a function of V alone. “Frozen” specifies a conditional evaluation;
it neither deletes eta from its support nor licenses its omission from a
later derivative or gauge transformation.

**S1a — covariance of the specified histories, PROVEN.** RD R2–R3 use
interior plaquette norms, component geometry and the completion minimum
H11 of SOURCE_LOCAL_HISTORY_RETURN_ASTRA:

    min_(Ucirc agrees with exterior eta)
      [max_p ||1-Ucirc_p|| + max_c ||V_c-S_c(Ucirc)||]. (S3)

Joint transformation of eta,V carries completions bijectively to
completions. The first norm is conjugation invariant; the second is
invariant under its common left and right endpoint unitaries. Hence the
minimum, every strict/weak threshold including equality, and every
recorded mask are invariant. Induction over the finite decision tree
proves invariance of each RD history indicator Xi_h. No smoothness of a
hard indicator is inferred. SOURCE_LOCAL_HISTORY_RETURN_ASTRA H20 also
states this joint covariance explicitly.

Products and sums preserve covariance. Integrating any subset of links
preserves covariance of the family in the remaining arguments by Haar
substitution; reciprocals and logarithms preserve it on positive fibres.
Therefore S2 and RD3 D4–D5 are jointly invariant, with their complete
exterior data. Additional chart choices need covariant labels or their
complete complementary sum. RD §4 explicitly retains the tree-averaged
insertion for a non-invariant chart/history factor. We do not identify
another unspecified history convention with RD R3.

These facts exhaust the covariance operations in the finite exact state.
They do not prove that each proposed cluster/logarithm exists or that an
arbitrarily chosen summand is invariant separately.

## 2. Inventory of actual spurions and their disposition

In this table **a** means removal of an artificial fixed-frame choice,
**b** means an actual integration/partition identity, and **c-retain**
means surviving dependence with no automatic claim of free tuning.
These are often successive operations, not exclusive properties of a
whole activity. A single mixed action contains several rows.

| Actual factor or descendant | Which data remain? | Exact disposition and limitation |
|---|---|---|
| Original Wilson plaquettes, invariant source insertions and b_j | One connection; plaquettes may cross an integration boundary | No independent colour spurion on the complete support. At fixed eta they are conditional boundary functions, not interior-only invariant functions. LOCOP L5 applies only after its container/domain hypotheses hold. |
| Numerator of k_t(V;M(U)) | Independent U and V, with shared endpoint gauges | **c-retain:** relative connection term of size t/2, §3. Background covariance does not remove it. **b** only when V is genuinely unread and fully integrated. |
| log Z_t(M(U)) | The complete fine contour reader, no V argument | A single fine-connection invariant function. At real fields it is smooth even when M is singular. Its full C6 norm is not uniformly small: MIXSMALL MS8–MS14 keep polynomial/growing coupling costs. It cancels the numerator integral in **b**, not termwise in the action. |
| Conditional D_h,N_h,r_h and all-cut reference ratios | V plus eta and all inherited readers | **c-retain** until those readers are eliminated. Their joint covariance is **PROVEN** by S1a. RD3 D4's exterior a_B cancels in N/D but remains in D; the outside factor O_B must still be included. No new Wilson replacement for rho is allowed. |
| Fresh-gap factors and future/ancestral readers | Retained fine input plus selected/weighted coarse outputs | Unread outputs: **b**. Read outputs: exact KH and its normalizer survive; §4 and MIXSMALL MS20 rule out automatic cancellation. Fixed-event MS17 does not supply moving-selector or matched-law bounds. |
| RD cuts, completion/size failures, mandatory old histories, chart complements | Complete geometric and field readers, including hole fields | RD histories are covariant families by S3. **b** for a complete outcome sum before the log. A selected term is retained with its original mass; dividing by that mass does not leave its old rarity available again (RD3 D16). Chart-dependent selections require their exact transformed label/average. |
| Covariant lifts Z(V), local frames and pinned background energies with fluctuations eliminated | Background entirely determined by V | **a:** their full pullback is a single-field invariant function, §3. BFT_B §2.4 gives one-step pinned pieces; the general-depth version there is withdrawn. GI-cov is conditional, not all-history regularity. |
| Fluctuation a in U=e^a Z(V), relative residuals, linear terms and Gaussian mismatches | Independent a as well as V, or an exterior connection | **c-retain:** a transforms adjointly, so a^2 is allowed. Eliminating a with every reader can yield a single-field action; simply setting a=0 changes the integral. A linear term vanishes only at an actual critical point. |
| Haar chart density, FP, Gaussian determinants and reference normalizers | Coordinates/background/measure data | Coordinate contributions remain together. -log j has the explicit positive quadratic coefficient in §3. **b** for the exact change-of-variables or admissible COV-GI grouping, §5, not arbitrary deletion of individual determinants. |
| Retained holes, genuine fixed boundary data, winding holonomies | Other independent links or topology | **c-retain** with complete supports; no single local bulk mass classification on a fixed boundary or wrapping support. Physically prescribed boundary data cannot be integrated away without changing the problem. |
| Fully integrated positive R_h(V), Z_A(V), Q_h(V), with no other retained field | One connection, invariant scalar sources | No exterior colour spurion. Any supplied contractible local action pieces can use §6 and LOCOP L5. A global function on a torus is not automatically such a local decomposition. |

**Completeness scope — PROVEN.** RD's opened finite chain consists of
Wilson factors, S1 kernels, the indicators just described and retained
insertions. Its exact elimination multiplies every reader, integrates,
forms positive reference ratios, and, only where justified, takes logs
and additive decompositions. The preceding closure rules classify every
descendant by its remaining arguments. Chart changes add precisely the
measure/reference row. This is an inventory of dependence and symmetry,
not a claim to enumerate an unconstructed convergent polymer expansion.

## 3. Background covariance and genuinely independent relative fields

**S2 — dependent-background removal, PROVEN implication.** Suppose
Z(V^h)=Z(V)^{hhat} with hhat restricting to h at the coarse roots, and
F(U^g,V^h)=F(U,V) for the compatible chain gauge g. Then

    F(Z(V^h),V^h)=F(Z(V),V).                         (S4)

If a covariant change of variables U=e^a Z(V) is used instead, the
coordinate transforms as a -> Ad(hhat)a. Haar changes with its exact
chart density. Only after the whole a integral, or a proved covariant
elimination with all its terms, does one obtain the single-field object.
While a remains, |a|^2 is invariant and S4 does not set it to zero.

Reviewed BFT scope is essential. BFT_A §§7.1,8.0 retain
r_l=Q_l x_l-x_(l+1) and the composite gauge kernel; they do not remove r_l.
BFT_B §16.11 proves lift uniqueness: a gauge stabilizing a connected
level-zero chain and equal to one at a root is one everywhere, by
transport along edges. Thus orbit covariance makes the lift cocycle
automatic, with convention (U^a)^b=U^{ba} giving
hhat(h2 h1,V)=hhat(h2,V^h1)hhat(h1,V). Its review S5 confirms this.
BFT_B §22.12 and review S7 provide CovLift (i)–(iii) for Z^off on
K(epsilon), every gauge, coarse side T>=5, with the stated local range.
The fixed axis order is not hypercubic covariant. The corrected log radius,
clustered-frame margins and local-form hypotheses remain attached.

GI-cov (§13.6) transports the local inverses, fixed-point equation and
densities by conjugation, and uniqueness gives covariant solutions under
its displayed background/analytic hypotheses. Those hypotheses are not
proved merely by (i)–(iii). Frame smallness, residual bounds, higher jets,
general-background inverses and all-history extension must retain their
own status. In particular no later unreviewed assertion about the complete
CovLift (iv) norm is used here. Equation S4 only needs exact covariance.

**S3 — relative terms and their sizes, PROVEN.** For a genuine unitary
fine path T(U) with the same endpoints as V define R=V T(U)^*. Then
R^g=g_x R g_x^-1. On an injective relative-log chart r=log R also transforms
by conjugation. Thus -tr(r^2)/N is invariant under the joint action.
It is not removable by a gauge transformation: the conjugacy class of R
is gauge invariant. The arithmetic M in S1 need not be unitary; a path T
is used here only to exhibit legal relative coordinates, not to replace M.

For the actual kernel at U=1, M=1. With <a,b>=-tr(ab)/N and |t_a|=1,

    -log k_t(exp(z t_a);1)
             =constant + (t/2) z^2 + O(z^4).          (S5)

Consequently the fixed-fine output Hessian is exactly t=kappa u_j, in
each of N^2-1 colour directions on each output link. This is one prescribed
coefficient per kernel family, not N^2-1 adjustable masses. Its weighted
coarse Hessian is t h_(j+1)^2=kappa N u_j/u_(j+1); it is not an O(1/u_j)
remainder. The complete normalized tree functional has the relative
quadratic form (t/2)|QA-B|^2, with Qd=d ev. Additional finite-coupling
fine-only normalizer terms are still present. S5 does not discard them.

Likewise, differentiation of exp gives

    j(a)=det[(1-exp(-ad a))/(ad a)],
    log j(a)=tr_ad((ad a)^2)/24+O(a^4)
            =(N/12)tr(a^2)+O(a^4).

The last equality follows by writing ad a=a tensor 1-1 tensor a^T on
matrices; its squared trace is 2N tr(a^2), and the scalar subspace has
zero eigenvalue. Thus -log j(a)=N^2|a|^2/12+O(a^4), with Hessian N^2/6
in the normalized colour metric. It is a determined measure term.

For a *local smooth-field jet* with one reference connection and q
independent relative one-forms a^alpha (each engineering dimension one),
the source-free, no-additional-spurion dimension-two polynomial is

    (1/2) sum_(alpha,mu,beta,nu)
        M_(alpha mu,beta nu)<a_mu^alpha,a_nu^beta>.    (S6)

Constant conjugation makes the colour bilinear proportional to the trace
form, as proved in LOCOP L4; Hessian symmetry makes M symmetric. Hence
there are (4q)(4q+1)/2 coefficients before spatial symmetries. Full B4
invariance kills mu!=nu and equates the diagonals, leaving q(q+1)/2.
For one relative connection these counts are ten and one. There is no
dimension-one scalar, since su(N) has no invariant linear functional.
At this homogeneous B4-invariant bulk scope odd engineering dimension
is excluded by simultaneous inversion of all four axes: each vector or
derivative index changes sign, whereas a curvature contributes two.
At fixed histories/boundaries this reduction is unavailable; cubic and
derivative mixed jets must be retained. Coloured exterior tensors can
also act as coefficients of linear terms in a partial-field expansion.

These counts are not the number of counterterms of the actual full state.
Independent retained levels, positions, original source labels, boundary
readers and their coefficient functions are not bounded by q=1. Section 6
provides a finite, deliberately overcomplete chart alternative; no
history-independent finite parameter count is asserted for it.

## 4. What exact Haar averaging does and does not cancel

**S4 — complete-reader elimination, PROVEN.** At fixed U, the law of
output links is the product of normalized k_c. For a retained insertion H,

    int K(U,dV)=1,
    int K(U,dV)H(U,V)=KH(U).                         (S7)

Only the first identity applies to an unread output. Every factor reading
an integrated V must first be multiplied into H; fine ancestors are
integrated later with their actual rho. With selectors sum_a chi_a=1,

    sum_a int chi_a H K = KH.                        (S8)

The equality holds before logs and normalizations. For a positive event
p=K(E)>0, the selected normalized law has K(E|E)=1; it does not preserve
a second factor p. RD3 D16 and MIXSMALL MS20 are exactly this issue.
Differentiating S7–S8 is legitimate on fixed smooth domains with dominated
derivatives. Moving cuts retain their boundary terms; measurable partition
identities alone are not C6 estimates.

**S5 — exact surviving integrated relative term, PROVEN.** Consider two
normalized SU(2) *single-unitary-mean* soft factors on three parallel
transporters T,V,W, integrating the middle one:

    I(T,W)=int k_t(V;T) k_s(W;V)dV,   t,s>0.

This is an exact member of the soft-kernel algebra with unitary means,
and a diagnostic for the reader inference. It is not an identification
of a generic multi-contour arithmetic mean with a unitary matrix, nor a
uniform estimate on the actual inherited Wilson law.

Write an SU(2) matrix as q0 I+i q.sigma, q0^2+|q|^2=1. Multiplication
preserves this norm, so probability Haar is normalized round S^3 measure;
its radial density is (2/pi)sin^2(theta)dtheta. Direct multiplication gives
Re tr(V* T)/2=v.t for the four-vectors. Rotational invariance of S^3 thus
proves, without an imported special-function formula,

    Z(r)=(2/pi)int_0^pi exp(r cos theta)sin^2(theta)dtheta,
    I(T,W)=Z(sqrt(t^2+s^2+2ts x))/(Z(t)Z(s)),
    x=Re tr(T*W)/2.                                  (S9)

The rotation here is a change of variables in the round-sphere integral,
not a claimed extra gauge transformation. Put x=cos z, near T=W. Then

    -log I(T,W)=constant+(m_rel^2/2)z^2+O(z^4),
    m_rel^2=ts/(t+s) * Z'(t+s)/Z(t+s),
    0<m_rel^2<ts/(t+s).                              (S10)

Indeed the radial square root is t+s-ts z^2/(2(t+s))+O(z^4).
The mean Z'(r)/Z(r) of q0 is less than one; pairing q0 and -q0 shows
its numerator is the positive integral of q0 sinh(r q0) for r>0.
This proves strict positivity and the displayed bound. For t=2,s=3,
the registered supporting calculation gives m_rel^2=0.8632086976.
Yet int I(T,W)dW=1, by integrating the second normalized kernel first.
The surviving relative term is fully compatible with exact normalization
and gauge covariance. No tuning has been made anywhere in S9.

Gauge-orbit averaging is a different operation from integrating a field.
An invariant relative norm satisfies int dg |Ad_g r|^2=|r|^2. It is not
killed by group averaging. Even when a gauge-variant component has zero
linear orbit average, averaging its exponential can produce a nonzero
second cumulant. Nor is -log int exp(-S) equal to int S. These observations
prevent extending S7 into a termwise cancellation rule for mixed actions.

## 5. Exact physical Ward identities and the Gaussian comparison

**S6 — mass protection, PROVEN at the local scope stated.** Start with
the gauge-invariant original Wilson/source density and iterate the exact
normalized kernels, summing complete current outcomes. Extend any coarse
gauge to a fine gauge and substitute in Haar. Induction proves exact
invariance of the complete output density at every finite depth. A positive
past-history density independent of the new V has the same property for
its unselected transfer by S1a. The unselected output is smooth: its V
derivatives act on finitely many smooth kernels, with domination on the
compact integration domain. The bounds so obtained can be extensive.
Current V-dependent hard selections require a separate regularity proof.

For the complete positive single-field action S_eff=-log R, constant
gauge invariance makes DS_eff(1)=0: an invariant linear functional on each
su(N) link vanishes on commutators, which span su(N). Differentiating the
local gauge identity at 1 then gives

    D^2 S_eff(1)[d omega,B]=0.                       (S11)

On a contractible finite support, a tree subtraction writes
A=d lambda+R_X dA: the residual circulation on a non-tree edge is a finite
sum of plaquette curls filling its fundamental loop. S11 therefore
factors the invariant local Hessian through two curls. Equivalently, the
local nonlinear tree-loop coordinates start at engineering dimension two
for a single smooth connection; their invariant linear functional vanishes.
The first nonconstant scalar has two curvatures, dimension four. This is
LOCOP L2's argument rebuilt at the precise scope used here.

A standalone (m_phys^2/2)sum|B|^2 fails S11 unless m_phys^2=0. For an
exponentially summable translation-invariant bulk Hessian, the analytic
symbol also obeys Pi(p)d(p)=0; taking p=epsilon v and dividing by epsilon
gives Pi(0)v=0 for every v. Thus the local mass coefficient is zero whenever
this bulk-local interpretation exists. A wrapping Wilson loop on a torus,
or a nonanalytic transverse mass projector, is outside that interpretation.
Gauge invariance alone does not prove uniform locality, eliminate physical
mass gaps, or identify the spectrum of the continuum theory.

There is a useful exact form of the cancellation after fine integration.
On a fixed smooth representation R(B)=int exp[-S(U,B)]dmu_0(U), with all
measure/normalizer factors included and dmu_0 independent of B,

    D_B^2(-log R)[v,w]
      =E[S_BB[v,w]]-Cov(S_B[v],S_B[w]).              (S12)

Differentiate the normalized expectation to prove S12. At B=0, putting
v=d omega makes the right side zero by S11 for the complete invariant
integral. The nonzero fixed-input term in S5 thus cannot be read as the
physical mass coefficient of the marginal. Any selector boundary or
coordinate-density derivative needed by a different representation must
be included before S12 is used. This is cancellation in the full integral,
not a claim that a particular isolated term cancels under every coarse
integration.

**S7 — Gaussian comparison and COV-GI, PROVEN conditional algebra.**
For finite admissible Gaussian spaces let H be the fine quadratic form,
T>0 the block precision, Qd=d', Hd=0, and A=H+Q* T Q positive/invertible
on the integration slice, which includes the specified lift d. Eliminating
the fine variable gives the coarse quadratic form

    H_eff=T-TQ A^-1 Q* T,    H_eff d'=0.             (S13)

Proof: A d=Q* T d', so A^-1 Q* T d'=d and Qd=d'. At fixed fine input the
coarse Hessian is T>0. Both assertions hold simultaneously. A gauge-breaking
fine mass invalidates Hd=0 and generally destroys the cancellation.

FLOW §36 COV-GI is the determinant version, with its actual admissible
slice, MJ=D, HJ=0 and positivity hypotheses. Write X=J omega+X_perp.
The change of variables has volume factor det(J*J)^(1/2); the orbit
integral of the Gaussian p_C(MX) contains det(D* C^-1 D)^(-1/2).
In orthonormal gauge/transverse coordinates, Schur elimination gives

    det C=det C_perp det C_G^flat,
    det(D* C^-1 D)=det(D*D)/det C_G^flat.             (S14)

Hence the gauge-covariance determinant appears with opposite half-log
signs in the fine Gaussian action and its normalized coarse covariance;
it cancels exactly. The factors det(D*D), det(J*J), the FP determinant
and the transverse determinant still remain, as FLOW states. This proves
the specific cancellation, not vanishing of every mixed residual or every
transverse coefficient. At a noncritical background the differentiated
Ward identity has the additional gradient term
H(D_0 omega,Y)=-DS[DV_omega Y]; HJ=0 is then unavailable in general.
FLOW's explicit H-H_natural determinant remainder cannot be dropped.

## 6. A conditional assembly of invariant Loc and a mixed-chart projector

**S8 — local Haar symmetrization, PROVEN.** Suppose a complete positive
history action already has a finite or absolutely summable additive
representation S_h=sum_X F_(h,X). Its real domain is invariant under the
joint gauge group, its supported functions have RGA3/RGA4 jets there,
and S_h itself is invariant. Each support includes every argument read,
including independent external fields, not only integrated links. Define

    R_X F(U,V,eta;J)
       =int_(g on endpoints of all read links) F(U^g,V^g,eta^g;J)dg. (S15)

All gauges are restrictions of the same chain gauge at shared roots. The
gauge integrations add no field argument or reader. S15 is the global
product-gauge average with unread vertices integrated to one. Thus

    R_X^2=R_X,     sum_X R_X F_(h,X)=S_h.             (S16)

Every output is invariant. These are averages of *additive activities*;
we are not replacing a density by exp of its averaged logarithm. The
sum identity uses invariance of the original total action.

For group derivatives, transformation by a fixed g conjugates each link
direction by an endpoint unitary, preserving its operator norm and its
level weight. Repeated ordered directions obey the same rule. Taking
the finite Taylor sum, triangle inequality, Haar integral and domain
supremum proves

    ||R F||_(mu,6,4) <= ||F||_(mu,6,4).              (S17)

The proof is identical with labelled sources and inactive roots. A gauge
invariant regulator may also be carried. A frozen-frame chart regulator
or a non-orbit-invariant domain is not covered without its actual frame
conversion. No enlargement or support-rate loss is hidden in S17.

S15 cannot make an independent eta disappear: it transforms eta jointly.
For non-invariant selected chart pieces it cannot be applied branchwise
as an equality without first obtaining an invariant branch action; the
exact inserted/averaged history or complementary sum stays explicit.

On eligible single-connection, nonwrapping contractible containers set

    Loc_X^single = Loc_X^(ten,LOCOP L5) R_X.          (S18)

The L5 range is invariant and L5 is idempotent, so S18 is idempotent on
this domain. It preserves constants and every constant-curvature quadratic
test of R_X F. It retains the full six-plane tensor and source functions.
Only a complete B4-invariant translation bulk may reduce that tensor to
the scalar coupling. This also handles the fixed-axis warning in CovLift.

**S9 — finite complete mixed chart, PROVEN conditional construction.**
Work on an orbit-invariant open real domain of all independent retained
link variables containing the trivial configuration. The only chart
asserted below is a small cycle-log chart after tree gauge fixing; no
global link-log chart is assumed. Form the finite multigraph: identify
common fine/coarse root vertices, but keep the
different-level edges distinct. Dependent background fields Z(V) are
substituted first, and every field they read is included. Choose a rooted
spanning forest of this graph and denote the root-to-x tree product by P_x.
For every non-tree edge e=(x,y) in its component put

    C_e=P_x U_e P_y^-1.                              (S19)

The gauge transformation g_x=P_x makes all tree links one and makes the
remaining links C_e. Under an arbitrary original gauge, C_e changes by
conjugation at the component root. Conversely, arbitrary independent C_e
are reconstructed by setting tree links to one and non-tree links to C_e.
This proves the exact finite reduction to independent cycle coordinates,
with no determinant or gauge-volume approximation.

For sufficiently small invariant cycle-log balls z_e=log C_e in su(N),
write the invariant activity as f(z,J). It is invariant under one constant
conjugation per component. Fix positive radii R_e and a positive margin
so a neighborhood of the product closed balls ||z_e||<=R_e lies in this
chart and in the activity's domain, for every admitted J. For S21 use
ordinary coordinate derivatives with each cycle species' directions
bounded by R_e, all multi-species factorials, total field order at most
six and source order at most four. Equivalently y_e=z_e/R_e ranges over
product unit balls with ordinary unit directions; original source weights
are unchanged and the domain supremum is outside the complete Taylor sum.
These are fixed derivative units, not inferred fluctuation bounds. Define

    P_4 f(z,J)=sum_(r=0)^4 D_z^r f(0,J)[z,...,z]/r!,
    Loc_(X,tree)^mixed F(U;J)=(P_4 f)(log C(U),J).    (S20)

P_4 commutes with these linear conjugations and with source derivatives;
evaluation on the reconstructed graph recovers f. Consequently S20 is
gauge invariant and idempotent in the same fixed tree chart. It includes
every mixed quadratic coefficient and keeps source dependence exactly.
On the coordinate Taylor norm through six, the degree-r reconstruction
costs at most sum_s binom(r,s)=2^r, with the multivariable factorial
version following by the product binomial identity. Therefore

    ||P_4 f||_T<=16||f||_T,    ||(1-P_4)f||_T<=17||f||_T. (S21)

These are coordinate estimates. Tree-path lengths, log margins, chart
and inverse-chart derivatives, weight conversions, and all pulled-back
readers must be paid to obtain an RGA7 group-field bound. No uniform
bound on those conversions is asserted. If graph automorphisms change
the tree, carry the tree as an auxiliary label and transport it with the
support. Alternatively use a finite orbit of tree-labelled copies whose
weights sum to one; idempotence is on that labelled direct sum. Averaging
different unlabelled projectors does not generally preserve idempotence.

For a graph with E edges, V vertices and c components there are
r=E-V+c independent cycles, hence d=(N^2-1)r real log coordinates. At most
binom(d+4,4) scalar monomial coefficient functions are stored per source
argument, before conjugation reduces their number. This grows with the
retained graph. For smooth fields on a fixed finite geometry, pure
single-connection loops start at order spacing^2; mixed cycles can start
at order spacing through relative one-forms. Thus degree-four truncation
is a conservative container for engineering dimensions <=4 when *all*
these fields are simultaneously small and scaled. It also stores higher
engineering dimensions and is not a minimal physical counterterm basis.
Unscaled exterior spurions or macroscopic winding loops do not satisfy
that power-counting premise. There is no assignment of curvature dimension
two to an arbitrary mixed loop merely because it is a loop in this graph.

S18 and S20 give an exact action split F=Loc F+(1-Loc)F for their supplied
domains. Re-exponentiate the complete summed action to preserve the state.
They are not subtractions from multiplicative gas weights. Non-chart and
zero-fibre sectors stay in the original Haar/history representation;
calling the identity operator “Loc” on all such sectors would not solve LC1.

## 7. What this assembles, the remaining LC1 work, and AF compatibility

The algebraic prescription is now explicit: keep all primitive reader
labels; multiply complete readers before eliminating a field; preserve
every reference and complement; obtain the actual positive additive local
action; symmetrize it by S15; use S18 on eligible single-field containers
and S20 on eligible independent mixed charts. Use tensor coefficients
before a complete bulk symmetry reduction. The steps after “obtain” are
proved conditional constructions; the producer before it remains substantive.

| Remaining actual-model obligation | Status and precise reason |
|---|---|
| LC1-P: complete supported additive history actions | **OPEN.** REALRGA RGA-L/H3 and MIXSMALL MS3 do not provide the required matched all-history local logs. Positivity of a finite integral is not a small local expansion. E_comp must be included before any log claimed for the full output. |
| LC1-D: stable real domains for all selected readers | **OPEN.** Failed histories need not contain the trivial-field chart, hard current selectors can move, and complements can carry zero fibres. CovLift's curvature class is not the whole rough/failed state. FR remains a named domain input at its supplied scope. |
| LC1-C: covariance of supplied smooth additive pieces | **PROVEN conditional S15–S17.** This removes a separate covariance-choice problem once LC1-P/D supply an invariant action on an orbit-invariant domain. It does not assume that missing representation. |
| LC1-M: mixed, source, boundary and holonomy accounting | **PROVEN finite classification and chart construction; OPEN uniform implementation.** S6/S20 retain independent relative coefficients. Their number/coordinate costs and long readers are not uniformly bounded by the one-pair count. Non-chart sectors remain exact but unlocalized. |
| LC1-N: full norms and coefficient recursion | **OPEN.** Supply six field/four original-source jets, group/chart conversion, matched differentiated reference bounds and full rooted sums, including inactive roots. Arbitrary-hole support growth is not paid by covariance. KR and TC remain named interaction and original-law inputs. |

The open entries overlap: a matched local producer may solve several
together. No independent-wall count or impossibility theorem is claimed.
The proposal to combine them with S18/S20 is **ARGUED**. LC2 spatial
localization, LC3/EXTCONT E19 contraction, and LC4–LC6 coefficient/trajectory
requirements are not supplied by a finite projector or by exact symmetry.

**S10 — counterterm meaning and causal accounting, PROVEN algebra / OPEN
estimates.** A reference quadratic form Q may be changed to Q+Delta provided
the interaction changes by the opposite quadratic contribution (and its
normalizing determinant is retained). The total density is unchanged.
Similarly extracting c O from an additive activity and putting c O in
the stored coefficient function does not add a bare parameter. Such
choices can be causal: compute the coefficients from the step-j complete
state and its prescribed u_j, with no future terminal value. Whether those
causal coefficients meet uniform balls or allow the desired trajectory
is a further estimate, not an algebraic consequence.

If one literally discards S5 by adding a bare negative quadratic term,
or changes a normalized kernel without its compensating normalization,
one has changed the model/representation. There is no such operation in
S1–S2. In contrast, changing the blocking parameter within a complete
normalized transfer is an auxiliary scheme choice; with all terminal
variables integrated, its unit normalization preserves the original
generating function. This does not identify its intermediate actions.

LOCOP L13's exact convention therefore remains

    u_(j+1)=u_j-b_j-rho_j,    rho_j=-beta[R_j^other]. (S22)

The bulk beta is taken only after a complete single-field translation
bulk action and its summable Hessian moments are supplied. Relative
terms/refinements contribute through their *actual integration*, including
normalizers and measure terms; they are neither discarded nor declared
an extra bulk mass. LOCOP's AF bracket additionally assumes

    |sum_(j<n)b_j-n b_*|<=R0,
    |rho_j|<=C/u_j,  u_j>=u_min,  C/u_min<=b_*/2.     (S23)

Nothing in S10 changes this conditional arithmetic. Nothing here proves
S23, existence of its stable trajectory or FI-1's required causal estimates.
In particular, a weighted mixed activity bound epsilon gives only an
unweighted quadratic coefficient bound of order epsilon/(h_alpha h_beta)
(with the appropriate factorial/chart constants); on one level h^-2=u/N.
An O(1/u) weighted bound can therefore leave an O(1) coefficient. S5's
O(u) unweighted coefficient belongs in the blocking/reference structure,
not in an asserted O(1/u) AF error. Selected coefficient functions require
LOCOP LC6's actual projected budgets.

The physical answer is thus precise. The number of independently tunable
symmetry-breaking *local single-connection gluon-mass* coefficients required
by the exact construction is **zero**. Its mixed conditional actions have
nonzero quadratic coefficients, including S5, the chart contribution and
the exact S10 example; these do not diagnose a loss of gauge protection.
The stronger claim that this scheme already has a controlled all-history
continuum RG with no further analytic work is **OPEN**, for the named
LC1/LC2–LC6 reasons. A physical mass gap is a different question.

## 8. Verification and decisive next work

The preregistered five finite regression groups all PASS in
[checks/spurion_results.json](checks/spurion_results.json): simultaneous
SU(2) covariance with a one-field-only control; Haar reader survival;
rational Gaussian Schur cancellation with a positive-mass mutation; finite
tree reconstruction/projector algebra; and complete-reader/partition
accounting. Peak measured RSS was 22,380,544 bytes, maximum sampled load
2.232421875, memory free 49%, nice 20 and all six thread settings one.
No failed numerical result or post-hoc numerical probe is concealed.
These controls prove no all-history estimate; the written derivations
support the scoped claims. The fresh review and any resulting source fixes
are recorded in the log.

The next useful producer target is a positive RD3 mixed return beside its
actual hole: construct its complete matched local log with one retained
coarse derivative and all original source labels, including the exterior
inverse, normalizers and any moving-selector contribution. Apply S15 and
measure the full mixed quadratic block before trying to delete it. Then
prove its reader/coordinate and coefficient costs in RGA7. This is a
specific subcase toward LC1, not a substitute for its all-history quantifier
and not a request to redo the coordinator's FR/KR/TC work.
