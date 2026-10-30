# INDUCT — a conditional all-scale real-jet induction

The finite-depth implication is written through its fixed-physical-scale
derivative output below. Its hypotheses are not established for the full
SU(N) model: eight numbered steps remain GAP. In particular, a one-step
conditional theorem does not regenerate its own matching reference,
differentiate arbitrary selected histories, or control the other extracted
coefficients. No unconditional Yang–Mills construction is asserted.

The arguments here include a history-summed, paid hole-saturation bound,
charging with the nonmonotone coupling bracket, an explicit causal shooting
construction, the invariant-ball feasibility test, and terminal derivative
bounds. These are author drafts, not an independent check of this packet.

## Source identity, scope and counting convention

This file executes briefs_q/INDUCT/AUTHOR.md, SHA256
a5d9432a7515adc8b3883ad7594f09ddfe56a2b945c3fdb40dbc3cde3e87fd1b.
Only INDUCT.md is an output. No commits, numerical experiments, reviews,
audit/ledger changes, axiom changes or editable-prompt changes are made.

The source checkout is 3cb83ec758849c5b800e5d779d9e484cc94562ee, branch
claude/q-S2. Cached origin/main is
01589af3faf806b736c42dc2f3bd625e9edead9f; cached origin/ai/execution is
56c5c0ab64f532c5784e895b2f9aa6894fa334e0. The read-only remote query failed:
“Could not resolve host: github.com”. No remote freshness is certified.
The science workflow and repository physics-loop entry point match the
cached main. The bounded author brief overrides campaign delivery machinery.

All nine source files below equal their HEAD versions. None exists at its
specified path in cached origin/main. The inspected review records accept
conditional/scoped results, and explicitly do not certify git landing.
Consequently no numbered step is labelled PROVEN(file) under this brief's
literal “already landed” requirement. This does not withdraw the existing
reviews. Their mathematical statements are used with their hypotheses,
with the compositions and arguments here labelled DRAFTED.

| Source | SHA256 |
|---|---|
| [REFMATCH.md](REFMATCH.md) | a7f45d815b6c7c4ed51950e0d3cc30ea3a7cb650e0bcb8e508659d197889729c |
| [REALRGA.md](REALRGA.md) | e9a08eed121b1e05b792afdc4904f0872e31ea0f9e0f7899ccb7edc09492bbed |
| [EXTCONT.md](EXTCONT.md) | b10015bbd6be5fac97fd636fdc79f665800fe9921651575b9d03b0167b534b6e |
| [LOCOP.md](LOCOP.md) | 0295d071a60d0ba3abfa23e4722634c7c2ea54921423cd0451aec7381e2c9253 |
| [SPURION.md](SPURION.md) | 8474bec9faca8b0d9a1318846088e26cf47a06f89748236c8d440bc0ab046667 |
| [FLOW.md](FLOW.md) | 085cd225228a23847b053650fe8bff4c14529d7e630a74565b301d39855e442f |
| [CHARGE.md](CHARGE.md) | 8c5a5ecdb95a32089f2005bf6597d4aedefa660b9b9f8c1cc7b7a01374afc1ef |
| [RENEW.md](RENEW.md) | 42b4d2a16625d4af4f6443a38ff92d63a483485816c4533292b44f867fc978a7 |
| [LIB1.md](LIB1.md) | 1e843c88ae26a2e69241dbdc3fa72c5b54e49a3b1669565f9e869a620a19aad1 |

All nine source files were read in full, including FLOW's 4,851-line
cumulative history and its embedded corrections. Its consumer-relevant
interfaces are §§0–4, 6–10, 25, 96–99 and 104–110; the intermediate
scalar, Gaussian and one-loop results do not close its remaining
actual-model UNIV hypotheses. HOLEPAY.md is absent in this snapshot.
Review headers, source identities and dispositions were inspected; no
claim of a new complete review of those reports is made.

The closest existing results are REFMATCH §6, REALRGA §4 and EXTCONT §5.
The missing obligation is their uniform actual-model production and
regeneration, coupled to FLOW and the coefficient/source recursions.
A cached-main statement search for real multiscale induction,
REFMATCH and EXTCONT found no matching theorem. This is a scoped search,
not an exhaustive novelty claim. The primary-source abstract of
[Brydges–Slade, Approximation by local polynomials](https://arxiv.org/abs/1403.7253)
was checked for method context: it describes relevant/marginal extraction
in a normed algebra, not the required SU(N) all-history theorem. No
external theorem is a load-bearing premise here.

Exactly the twenty numbered S-steps are counted: twelve DRAFTED, eight
GAP, zero PROVEN. Every drafted step states its confidence and its single
most likely failure point. G1–G8 name analytic assumptions, not physical
axioms; they overlap and are not eight independent obstructions.

## S01 — DRAFTED(high): the exact finite chain

**Consumes:** finite compatible four-dimensional periodic lattices,
N>=2, fixed odd L>=3, kappa>0, probability Haar, positive prescribed
u_j, the actual paired-contour means, and four labelled directions in
the original real source space. These are supplied model data.
**Produces:** an exact unnormalized state and its full positive marginal
at every finite depth, without a uniform norm estimate.
**Most likely failure point:** applying the smooth-marginal conclusion
to an individual current hard-selected child.

Fix a physical coarse spacing ell>0 and a compatible terminal torus.
For depth K let a=ell L^(-K), a_j=L^j a, so a_K=ell.
Keep N,L,kappa,ell and the target terminal inverse coupling fixed as K
varies. At a fixed K start with

    rho_0(U;J)=exp[-u_0 W_0(U)+sum_i J_i O_i(U)],
    W_0(U)=sum_p [1-Re tr(U_p)/N],
    rho_(j+1)(V;J)=int rho_j(U;J) calK_j(V,U)dU,
    calK_j(V,U)=product_c exp[t_j h_(M_c(U))(V_c)]/Z_(t_j)(M_c(U)),
    t_j=kappa u_j,   h_M(V)=Re tr(V* M)/N.                 (I01)

The O_i are the specified smooth original observables/coefficient
directions, not newly chosen coarse observables. The coupling trajectory
is defined at J=0; under every observable-source derivative all u_j,
kernel formulas and jet weights are held fixed.

For each finite j, sum the complete decision tree with its original
unnormalized masses. Its indicators sum to one before a logarithm, hence
the sum equals rho_j. Zero children remain zero summands. Every factor
reading an integrated variable is multiplied before integration.
Since int calK_j(V,U)dV=1, Fubini gives

    int rho_j(U_j;J)dU_j = int rho_0(U_0;J)dU_0 = Z_0(J). (I02)

The full marginal is strictly positive. On real compact parameter sets
its derivatives exist to every fixed order: the finite compact integral
can be differentiated, and for j>0 terminal-field derivatives act on
the smooth last kernel. Thus S_j=-log rho_j exists and is smooth.
These elementary bounds can grow with u_j, volume and depth. They do
not give the desired local bounds. Hard selected pieces require S03.

For any actual selected return still keep, separately,

    R_h=int rho_(j,h) calK_j,   Z_A=int chi_A b_j calK_j,
    b_j=exp(-u_j W_j^Wilson),   Q_h=R_h/Z_A.              (I03)

Neither rho_(j,h)=b_j nor Q_h=an expectation under the forward product
law is inferred from I02. A complete state retains the two endpoint
normalizers and all original sources.

## S02 — DRAFTED(high): the enlarged induction hypothesis

**Consumes:** I01–I03 and supplied real domains/representations.
**Produces:** the exact type of IH(j), including data omitted by a
residual-norm-only induction.
**Most likely failure point:** treating the production certificate in
the last row as a consequence of the residual norm.

Use REALRGA's ordered group derivatives, p=6, q=4 and frozen weights
h_l=sqrt(N/u_l) on each still-retained level l. Old fields retain their
own weights. For four original labelled source directions use

    T_j(F)=sum_(a+b<=6) sum_(B subset {1,2,3,4})
       (product_(i in B) r_i)/(a! b!)
          sup_(unit field directions) |D_f^a D_c^b partial_B F|. (I04)

Here r_i>0 are declared original-source jet weights, not analytic
radii. In I04 the field directions already include their frozen
weights: each level-l component of a direction is h_l H_l,
with ||H_l||_infinity=max_b||H_(l,b)||_op<=1.
D_f and D_c denote ordered words of these
weighted derivatives, with each old-field letter using its own h_l.
The ordinary unweighted directions in I32–I35 explicitly restore
the inverse weights. If the factorial source convention is used instead,
retain its c! factors; the two conventions are not interchanged without
conversion.
All mixed words through total order ten are included.

Fix mu>0 once for the entire induction. For a history-labelled family
use the *joint* rooted norm

    ||F||_(mu,T_j)=sup_v sum_(h,X:v in X)
                   exp(mu|X|) sup_(D_j) T_j(F_(h,X)).    (I05)

A representation that has already summed histories can omit h. A bound
on sup_h ||F_h|| is weaker than I05. X contains every actual field,
normalizer, original-source and exterior reader through an explicit
assignment to the ambient block graph; inactive vertices are roots.
Any reblocking/hull conversion is an operator to estimate, not a change
of what “support” means.

Ordered Leibniz distributes derivative positions between factors,
preserving their order. The factorials cancel the binomial coefficients;
disjoint source subsets partition the labels. Hence T(FG)<=T(F)T(G).
For regulators G_m=exp(a_reg sum_v m_v E_v), G_m G_n=G_(m+n);
overlap multiplicities are added. A single copy of G is not an algebra
norm on overlapping products. Fixed-domain differentiation gives

    T(int F n d lambda)<=int T(F)T(n)d lambda.           (I06)

Both statements follow term by term before taking suprema. In
particular, small values alone create no real derivatives.

The following is the proposed state, uniformly over the complete history
family and all compatible volumes. Constants are independent of j and K.

| IH(j) field | Exact object/bound carried |
|---|---|
| H0, exactness | I01–I03, every unnormalized mass, hard complement, normalization, and scalar/source function. Logs only of specified positive sums. |
| H1, domains/jets | Open real domains D_j with supplied inner margins; I04 and the full selector/chart/weight conversions. Original labels remain unchanged. No shrinking margin at each iteration. |
| H2, remaining resources | For each original plaquette p, spent fractions plus remaining fraction <=1. Every overlap regulator multiplicity is recorded, with its actual-law joint integrated-jet bound. |
| H3, local representations | The current integrated gas/log and its full supports; log budget P_*; separately a certificate that the *next* matching/atom construction is callable with the fixed support reserves and joint majorants of S04. |
| H4, action and residual | An exact action split into the main tree/reference, relevant functions v_j, supported prefactors, residual K_j and a separately recorded field-independent c_j(J). x_j=||K_j||<=M, v_j in a specified set V, with an explicit scalar recurrence. |
| H5, transition record | Bounds lambda,B,C,s_j,eta_j,e_j in I24 below, after every conversion, and the causal coupling prefix in I18. eta_j is a failure-operator bound, not the background cluster budget. |
| H6, original-source record | All sixteen source subsets, including the empty one, of the same functions; lower subsets, scalar terms and outer cumulants. No new source choice or retuned kernel. |
| Regeneration certificate | The successor satisfies the same domain, reserve, matching, full-reader, relevant and source conditions. This is a substantive producer statement G2/G5, not reuse of a spent norm. |

For the target here the index set is all complete finite histories;
any restricted chart decomposition must retain its full complement.
“Histories for which these bounds hold” is not a definition of an
admissible physical class.

## S03 — GAP: G1, base state and selected-domain production

**Consumes:** the exact finite model of S01.
**Must produce:** IH(0) for every admitted u_0>=u_base, a fixed real
source neighborhood, and the H1/SEL portions of every next step.

At J=0 the bare Wilson action can be placed wholly in the main action
and the raw residual is zero. With a linear source, store its exact
coefficient function rather than truncating it. This is not the full
base certificate: pinned reference bounds, uniform source budgets,
selector regularity, chart margins and the relevant-function set V
still need construction. Write x_0<=M_init; neither M_init nor the
other base budgets is assigned a numerical value here.

EXTCONT E10–E12 requires a fixed-domain representation with all weighted
score derivatives through total order ten, or a direct bound of equal
strength. A source-dependent field transport can require field order
ten rather than six. It must be avoided or accompanied by that larger
hierarchy. Differentiating a retained-field hard indicator as though its
mask were fixed omits boundary terms. Summing every current outcome first
gives S01's smooth marginal, but does not supply small local selected
coefficients. This is why the elementary base and positivity argument do
not discharge G1. Continue below conditional on G1.

## S04 — DRAFTED(high): the precise one-step logarithm interface

**Consumes:** IH(j), a matching construction on the same integral,
and the joint differentiated budgets below.
**Produces:** a supported real logarithm in the fixed norm at rate mu,
plus separately retained reference/scalar terms.
**Most likely failure point:** factorizing separately normalized
expectations instead of the complete jointly integrated coefficients.

REFMATCH §6 concludes, verbatim:

> Exact transfer, new supported real logarithms, complete extraction and
> finite marked source records yield H0–H4 and finite H6 at j+1, with
> x_(j+1)<=M.

Its preceding five hypotheses, not that conclusion alone, are the input.
The matching part requires an exact positive fixed-domain identity

    dnu_y=exp(Phi_y)dmu_y/Z_y,   dmu_y=product_c n_c(y,W_c)dW_c,
    Phi=sum_X phi_X,   a_X=exp(phi_X)-1,
    T(n_c)<=P_c n_c,   sup T(a_X)<=s_X,
    alpha_X=s_X product_(c read/integrated by X) P_c.     (I07)

The support includes readers of n_c as well as a_X. Hard supports must
match, or their insertions and boundary terms remain explicit. The
background and new atoms are expanded together; every selected overlap
component has one joint majorant and disjoint complete components factor.
At the input support rate mu+2 require

    eta_bg=sup_v sum_(X:v in H_X) e^((mu+2)|H_X|)alpha_X,
    d_new=sup_v sum_(i:v in H_i) e^((mu+2)|H_i|)gamma_i,
    eta_bg<=eta_bar<1/4,   eta_bg+d_new<=1/4.             (I08)

To see the implication, first group atom selections by overlap
components. The rooted-tree supersolution
b_X=e^((mu+2)|H_X|)alpha_X bounds connected components at mu+1:
the sum of incompatible child weights is <=(eta_bg+d_new)|H_X|.
The connected-graph logarithm has a second tree majorant, leaving
rate mu. Ordered Leibniz makes this an estimate of all the I04 jets.
Absolute convergence of the counting series identifies the exponential
of this logarithm with the exact gas at counting parameter one.

Subtract the background logarithm before estimating. Every surviving
cluster contains a new atom. If d_new>0, scale its majorants by
(1/4-eta_bg)/d_new; the total budget becomes 1/4, and each surviving
cluster gains at least that factor. Thus

    ||log int product_i(1+g_i)dnu||_(mu,T)
                         <= d_new/(1-4 eta_bg).         (I09)

For d_new=0 the new logarithm vanishes. This is REFMATCH RM13 with
exactly its joint hypotheses. A source scalar, main-action difference
or endpoint ratio outside that normalized expectation has its own log
budget. I09 alone is not a bound on log Q_h of I03.

If the pinned-reference decoration route RM12 is used, require its
additional unit explicitly: RM2 at sigma+1 means atom rate sigma+3,
and the core budget is at sigma+1. Either use I08's joint route or
carry these stronger rates. Never use RM12 at the weaker rate by
renaming mu. Both rates have to be regenerated, not decreased by two
or three at each successive scale.

## S05 — GAP: G2, actual matching and renewed reserves

**Consumes:** the entire output state at j, in particular its inherited
main action, references, coefficients and original readers.
**Must produce:** I07–I08, all outside-prefactor budgets, the joint
real-jet payment, and the same production certificate at j+1.

A small integrated residual does not bound its pinned integrand.
Even residual zero leaves the main action and hard support in the
reference. A strictly positive product density times a bounded
exponential cannot reproduce an additional hard zero on positive
measure. These are the explicit mismatches identified in REFMATCH §1.
They prevent inferring MATCH(j+1) from x_(j+1)<=M.

For example, REFMATCH computes the actual kernel bill

    P_<=6(u)<=A_<=6 u^3,  u>=1,
    q_gap(u)=kappa a_0 u^delta-1-2N^2 log(1+4N kappa u),
    a_0>0,  0<delta<1,  kappa u>=1 for q_gap.           (I10)

The named A_<=6 is its score-polynomial constant at fixed N,L,kappa.
No fresh gap exists at the M=0 mean. A pointwise regulator or original
charge can pay the polynomial there only when its same-law moment
and unused original fractions are established. Four source jets of
the inherited reference also remain; I10 is not their order-ten bound.

The all-history joint estimate must integrate the multiplicity regulator
and the differentiated normalized density together, as in RGA14. A
finite number of factors, or separate marginal estimates, is not enough.
There is presently no such regenerated producer in the inspected
sources. Continue conditional on G2, without crediting future estimates
or replenishing spent original plaquettes.

## S06 — DRAFTED(high): paid holes with a joint history sum

**Consumes:** the joint input norm I05 on a finite nearest-neighbor
four-dimensional block torus/box; arbitrary fixed masks Lambda_h; and
the differentiated price I11 for the actual coefficients.
**Produces:** a same-rate bound uniform in hole sizes, mergers, number
of histories and lattice volume.
**Most likely failure point:** applying the four-dimensional shell
count to an augmented reader graph without a proved graph conversion.

This extends EXTCONT E16 from one fixed mask to a joint rooted
history family; it does not supply the weight.
For X meeting Lambda_h let Sat_h(X) be LIB1's saturation by all
components H of Gamma\Lambda_h meeting or adjacent to X. Put
S_(h,X)=sum_(H touching X)|H|. Suppose the actual coefficient before
saturation is w_(h,X)K_(h,X), all readers of w lie in Sat_h(X), and

    sup_D T(w_(h,X))<=A_hole exp[-tau S_(h,X)],
    A_hole>=0,   delta_hole=tau-mu>0.                  (I11)

Leave X disjoint from Lambda_h with its original support and coefficient.
The weighted output includes both this inactive family and the saturated
one. Then

    ||output||_(mu,T)<=D_hole ||K||_(mu,T),
    z=exp(-delta_hole),
    D_hole=max(1,A_hole)+16 A_hole[(1-z)^(-4)-1].        (I12)

**Proof.** The product inequality and |Sat_h(X)|-|X|<=S_(h,X) give
e^(mu|Sat_h(X)|)T(wK)<=A_hole e^(-delta_hole S_(h,X))
e^(mu|X|)T(K). Fix an output root v. Inputs already containing v,
including unchanged inactive terms, cost at most
max(1,A_hole) times their joint input rooted sum.

For the remaining inputs v is in the inactive component H_(h,v) but
not in X. Some x in X lies in N[H_(h,v)]. Connectedness gives
d(v,x)<=|H_(h,v)|<=S_(h,X); necessarily x!=v.
Charge that input to all such x, which overcounts a nonnegative sum.
Its weight is at most A_hole exp[-delta_hole d(v,x)]. After summing
histories, for each x the input sum is bounded by the *joint* norm I05.
If output supports coincide, grouping their coefficients only decreases
the bound by the triangle inequality; no history entropy is suppressed.
The number of vertices at distance n>=1 on a four-dimensional box or
torus is at most 16 binom(n+3,3): choose absolute coordinate
displacements of total n and their signs. Unique shortest periodic
representatives give the same upper bound on a torus. Finally

    sum_(n>=1) binom(n+3,3) z^n=(1-z)^(-4)-1.

This identity follows by multiplying four geometric series. It proves
I12, with no separate sum of per-history norm bounds.
At A_hole=0 the active family vanishes and the bound still retains
the inactive family. Empty/full masks are included.

For a general simple graph of degree <=8 the same proof instead gives

    D_hole<=max(1,A_hole)+8 A_hole z/(1-7z),
    delta_hole>log 7.                                 (I13)

The shell bound is 8·7^(n-1). Do not use I12 if only I13's graph
hypothesis has been verified.

**Nested mergers at a fixed scale.** If Lambda_2 is a subset of
Lambda_1 and X meets Lambda_2, then

    Sat_(Lambda_2)(Sat_(Lambda_1)(X))=Sat_(Lambda_2)(X). (I14)

Every old hole belongs to one new hole. An old hole added next to X
belongs to a new hole already meeting/adjacent to X. A different new
hole cannot touch it without being in the same component. Thus no
extra new component appears on the left; the reverse inclusion is
immediate. This proves I14. Retain the inactive terms when X ceases
to meet the active set. Across a change of lattice scale I14 is not
an unproved reblocking identity.

I12 can therefore be applied once to a fully grouped mask at each
scale. Its factor is included in that scale's transition norm, not
multiplied afterward as an additional D_hole^K.

## S07 — GAP: G3, producing the hole jet price

**Consumes:** actual growing/merging hole histories and the unused
original-action resources.
**Must produce:** I11 on the complete history-labelled coefficients,
or a different fully specified support representation with a uniform
bound replacing I12, plus its reblocking/domain conversions.

LIB1 provides the bounded-hole alternative
9M_h ||K||_((1+8M_h)mu), or 1+9M_h when inactive terms are retained.
It neither supplies a uniform M_h for arbitrary histories nor regenerates
that stronger rate. Its active-root norm cannot be substituted for I05.
At one active vertex on a large torus, unweighted saturation sends a
singleton to the whole torus and its full norm gains
exp[mu(|Gamma|-1)]. This is LIB1 L23's exact bookkeeping example.

A merger must be charged for the actual whole touching component in
I11. Pricing only newly added vertices does not imply I11. A mandatory
old event normalized by its mass has conditional mass one; the same old
mass cannot pay again after a merger. Differentiated weights, source
scores, boundary readers and history sums must be paid jointly. HOLEPAY
is absent. The alternatives of integrating holes before assigning final
supports or keeping unsaturated reader labels remain available, with
their own consumer conversion to prove. Continue conditional on G3.

## S08 — DRAFTED(high): persistence, one-use charges and continuation sums

**Consumes:** the scoped RENEW/CHARGE constructions; for the general
continuation formulas, operators already bounded in the same full
real-jet norm.
**Produces:** admissible across-scale accounting and conditional
depth-uniform sums, without assuming forward smoothing.
**Most likely failure point:** extending a filled-ancestor charge to
an arbitrary localized continuation without a charged-ancestor witness.

RENEW's explicit fields have g=diag(-1,-1,1,...), every 12 plaquette
equal to g and paired mean W diag(1/L,1/L,1,...). The unique maximizing
output again has this curvature. Its finite-horizon tube probability
tends to one at fixed horizon/volume as the couplings increase.
Consequently its price is not a new positive kernel gap at each step.
These quantifiers are retained; no infinite-horizon probability limit
is exchanged with the weak-coupling limit.

For the filled original tube of radius 0<eps<1/4 write
c_eps=(2-4eps)^2/(2N), b=L^4 and n_l=n_0 b^(-l). The original 12
plaquettes have action >=c_eps u_0 n_0. For any finite horizon R_hor,
allocate, with 0<omega<=1,

    alpha_l=(1-b^(-1))b^(-l),
    D_l=omega alpha_l u_0 sum_(original 12 plaquettes p) s(U_p),
    sum_(l=0)^R_hor alpha_l=1-b^(-(R_hor+1))<1,
    D_l>=omega(1-b^(-1))c_eps u_0 n_l.                (I15)

This follows by a geometric sum and uses only original plaquettes.
A fixed per-occupied-cell bill c_bill is affordable in this filled
family when omega(1-b^(-1))c_eps u_0>=c_bill. Disjoint complete
history indicators sum to one before integration. If a combinatorial
overcount is used, its entropy belongs to c_bill. Across all other
uses, including regulators and normalizer jets, require
sum_(j,group,use) omega_(j,group,use,p)<=1 for each original p.

**The nonmonotone flow correction.** S12 gives u_j<=u_0+R, not
u_j<=u_0. If u_0>=U_min>=1, put chi=1+R/U_min. Then u_j<=chi u_0.
REFMATCH's polynomial price A_r u_j^(r/2), paid by
D>=omega c u_0 with omega c>0, obeys, for r>0,

    e^(-D) A_r u_j^(r/2)
      <=A_r chi^(r/2)[r/(e omega c)]^(r/2)
                            e^(-omega c u_0/2).       (I16)

Indeed maximize x^(r/2)e^(-omega c x/2) over x>0. This is a
correction to uses of RM22 that would silently require u_j<=u_0.
It remains a bound inside the charged integrand; the matched denominator
and uncharged integral have not been removed.

CHARGE C9 also gives a useful *extensive real-sector* check. With
epsilon_j sqrt(u_j)>=8 and u_j>=U_min>=4, its zeta=u_j^(-1/2) choice
has debit f(u_j)+16kappa u_j/b per level-j site, where
f(u)=48+8N^2 log(1+4N sqrt(u)). Thus its C10 may be replaced by

    16kappa chi b^(-(j_*+1))<=c_eps/4,
    chi b^(-j_*) sup_(u>=U_min) f(u)/u<=c_eps/4.        (I17)

For j>=j_* this yields the same exp[-c_eps u_0 n_0/2] upper bound
against its actual all-cut denominator. Finite choices exist since
f(u)/u tends to zero and b>1; use chi<=1+R at preliminary U_min>=1
when selecting them. The early j<j_* retain C9's unevaluated debit.
A finite number of early levels does not make their supremum over
u_0 bounded. The temporal I15 and final I17 accountings are alternative
uses of the same reserve, never multiplied together.

For a separately constructed extracted continuation C_j, suppose for
one fixed integer m that every length-m product has norm <=vartheta,
with 0<=vartheta<1,
every shorter product <=B_0>=1, and return maps have norm <=D_ret.
Writing r=qm+s bounds a continuation of length r by B_0 vartheta^q.
It follows by summing q,s that its lifetime sum is <=mB_0/(1-vartheta),
and the return sum is <=D_ret mB_0/(1-vartheta).
The same bound holds for the sum over births at a fixed terminal level:
the product ending there has the same length-r bound, uniformly in its
starting level. No stationarity or operator commutation is required.

Alternatively an actual creation map with a common lag envelope a_r,
sum_r a_r<infinity, controls both sums by reindexing r=k-j.
A per-birth summability statement without a common envelope does not
control fixed-terminal accumulation. For the filled-family benchmark,
a_r=B_birth^r exp(-lambda_birth b^r), B_birth>=1 and lambda_birth>0,
is summable
because a_(r+1)/a_r=B_birth exp[-lambda_birth(b-1)b^r] tends to zero.
This is not assigned to general histories without G4.

## S09 — GAP: G4, exhaustive charged or extracted continuation

**Consumes:** all actual persistent, fresh-gap, return, chart and
completion outcomes in the complete state.
**Must produce:** their joint full-norm bounds in I24, or a window
replacement with prefix, nonlinear and coefficient estimates.

RENEW's linear L^(-2r) dilution controls localized noncompact linear
curvature with an l1 input bound. It does not estimate the nonlinear
coherent orbit or an inherited l1 size growing with its readers.
CHARGE's filled-tube comparison is extensive; on an isolated core its
crude denominator estimate leaves a term proportional to the entire
level volume. That upper majorant does not certify the needed local
bound. It is not a lower bound proving the actual coefficient large.

The missing cover must assign every history group either a genuinely
unused charged ancestor, a new gap under the same differentiated
matched law, or a controlled extracted continuation/return. Overlaps,
old mandatory events and no-gap completion failures must all be
included. A scalar creation price does not improve a homogeneous
operator norm. Thus an untouched coherent eta_* cannot be declared
small by taking u_0 large.

For the window option, require the nonlinear window remainder and
relevant-function recursion as well as RENEW R20. Also require a uniform
bound on intermediate states inside each window. A small window-end
residual alone does not keep the intermediate matching hypotheses
valid. Continue via the one-step route conditional on G4.

## S10 — DRAFTED(high): exact extraction and the coefficient types

**Consumes:** a complete positive output with a supplied additive
local action; eligible single-field or mixed chart hypotheses.
**Produces:** an exact action split and an explicit coupling sign,
not a contraction estimate.
**Most likely failure point:** applying single-connection tensor
localization to a mixed or fixed-exterior activity.

Suppose S'_(j,h)=u_j W_(j+1)^tree+F_(j,h), including every
normalizer, determinant, Haar factor and complementary contribution
before the logarithm. The bulk source-free beta functional requires
an infinite-volume translation family with summable Hessian moments;
it is independent of the torus and h. If beta[W^tree]=1, define

    b_j=-beta[Gamma_j],   varrho_j=-beta[R_j^other],
    F_bulk=Gamma_j+R_j^other,
    u_(j+1)=u_j-b_j-varrho_j,
    G_(j,h)=F_(j,h)-(u_(j+1)-u_j)W_(j+1)^tree,
    V'_(j,h)=Loc_j G_(j,h),   K'_(j,h)=(1-Loc_j)G_(j,h). (I18a)

Linearity proves this identity. The returned marginal action
-delta beta_j W contributes +delta beta_j to varrho_j. Here varrho_j
is a scalar coupling remainder, distinct from the density rho_j. All
source-dependent field-independent coefficients remain functions,
not discarded constants.

LOCOP L5 matches the full six-plane curvature tensor on its
single-connection, contractible small-curvature containers. Only a
complete reflection/permutation invariant bulk reduces it to the
scalar tr F^2 coefficient. beta[G]=0 does not imply a zero field
Hessian: curvature differences can have a nonzero spatial quadratic
remainder. Its extra spatial gain requires spatial regularity.

SPURION S15–S17 permits Haar averaging *additive* supported activities
when their sum/domain is invariant; conjugation preserves group
direction norms, so averaging does not enlarge I05. It does not
remove independent old fields. Already at fine U=1 the actual kernel
has fixed-output Hessian t_j=kappa u_j in each normalized colour
direction. Its weighted coarse Hessian is kappa N u_j/u_(j+1).
These relative quadratic terms belong in the main/mixed coefficient
structure. They are not discarded as a forbidden single-field mass
and are not an O(1/u_j) coupling remainder.

For mixed cycle charts SPURION S20 retains all degree <=4 chart
coefficients and the complete source functions. Its finite projector
has norms 16 and 17 for projector and remainder. Chart and tree-path
conversion to I05 and the growing number of mixed coefficients are
still costs. None is assumed uniformly bounded by those two integers.
Use the SU(N)-maximizer tree exponent: the U(N) polar correction can
start at degree six and is visible in the present C6 contract.

## S11 — GAP: G5, actual operator, main action and coefficient budgets

**Consumes:** S10's exact split and all matching/selector/hole costs.
**Must produce:** uniform bounds for the actual extracted map and
every retained coefficient, including the terminal main action.

Let D_other include every conversion not already in D_hole.
LOCOP's appropriate ideal benchmark is
A_L=4/L+8/L^2 when spatial-variation variables occur, or 8/L^2
only under the stronger complete zero-jet hypothesis. A sufficient
actual comparison would give

    lambda<=D_other D_hole [C_tr A_L+d_*],
    ||Ret_j(K)-Ret_j(0)-D_K Ret_j(0)K||<=C ||K||^2.    (I19)

D_K differentiates in activity space, not in a field direction.
C_tr,d_*,D_other,C must be uniform on the whole activity ball and
include I04, all old readers and the source weights. The ideal
coordinate dilation is not the actual returned map. In particular
A_L=20/9,28/25,36/49 at L=3,5,7, respectively; even the value <1
at L=7 is lost if the real conversion costs are too large.

If v'=A_j v+f_j+r_j(K), a sufficient coefficient-ball condition is

    ||A_j||V_*+||f_j||+sup_(||K||<=M)||r_j(K)||<=V_*.

The actual coefficient space, its norm and this inequality must be
supplied; it need not be a finite-dimensional homogeneous bulk space.
Source functions, mixed, boundary and holonomy tensors are included.
A different explicit invariant set can replace this ball.
The main W_j^tree and supported prefactor action also need uniform
local jets at the terminal coupling, denoted W_* and P_* in S19.
P_* bounds the cumulative supported prefactor action at each level.
A bound P_* only on its new increment leaves a possible j P_* loss;
one must instead prove its contraction, resummation or extraction into
the recorded coefficients/scalar. FLOW's Hessian/determinant identities
do not give these C^(6,4) all-history bounds. Continue conditional on G5.

## S12 — DRAFTED(high): a causal trajectory and bare-coupling shooting

**Consumes:** G1–G5 on every admissible prefix, and the additional
causal bulk-flow assumptions stated here.
**Produces:** a volume-independent bare coupling for each finite K,
the coupling bracket, and fixed weight-conversion bounds.
**Most likely failure point:** obtaining the remainder constant from
an estimate that already uses the future terminal coupling.

Fix b_*>0 and R_0>=0 from one-loop data; put R=2R_0. To identify
b_* with this model's standard value would require G6:
b_*=[11N^2/(12pi^2)]log L in the Wilson convention
u=2N/g_std^2. Here g_lat=u^(-1/2); these two couplings are distinct.

Assume, on the chain's own prefixes only,

    B_n=sum_(j<n)b_j,   |B_n-n b_*|<=R_0,
    u_(j+1)=u_j-b_j-varrho_j,   |varrho_j|<=C_rho/u_j,
    u_j>=U_min,   C_rho/U_min<=b_*/2,
    b_-=b_*-C_rho/U_min,   b_+=b_*+C_rho/U_min.          (I18)

The increment/remainder at j is produced from levels <=j; it does
not consume u_K, g_K or a bracket extending past j. Telescoping gives
for 0<=j<n

    b_-(n-j)-R<=u_j-u_n<=b_+(n-j)+R.                  (I20)

Indeed the one-loop error is the difference of two errors bounded
by R_0, and the remainder sum is bounded by C_rho(n-j)/U_min.
This proves I20 also for the first output u_n of an admissible prefix:
its proof uses u_0,...,u_(n-1), not admissibility of u_n.

If U=u_n-R>0, I20 gives u_k>=U+b_-(n-k), hence

    |u_j-u_n-(n-j)b_*|
       <=R+(C_rho/b_-) log[1+b_-(n-j)/U].             (I21)

Use sum_(r=1)^m 1/(U+b_-r)<=int_0^m dx/(U+b_-x).
For an exponent s>1 it similarly gives

    sum_(j=0)^(n-1) u_j^(-s)<=U^(1-s)/(b_-(s-1)).

The sum of 1/u_j is generally only logarithmically bounded; do not
treat it as a cutoff-uniform sum. Coupling drift is kept in u_j.
For causal exponentially suppressed source terms one can also use
u_i>=u_j+b_-(j-i)-R on a prefix, giving
sum_(i<j)e^(-c u_i)<=e^(cR)e^(-c u_j)sum_(r>=1)e^(-c b_- r).
This prefix estimate uses no future endpoint.

**Order of constants.** First supply all producer constants on a
preliminary weak-coupling range, using the fixed weaker slope b_*/2
and defect R. Only afterwards increase U_min to meet I18 and the
other window tests. The same constants must remain valid on the
smaller range. This is FLOW FI-1's causal requirement, not a theorem
that the producers satisfy it.

**Shooting proof, without monotonicity.** Supply finite-step
continuity in the initial g_lat on admissible prefixes, including
their boundary, and the ability to compute the next output from
such a prefix. Put gamma=U_min^(-1/2). Fix a physical inverse
coupling U_ph>=U_min+R and a depth K>=1.
Every initial value

    0<g_lat,0<=[U_min+b_+K+R]^(-1/2)

stays admissible through K: induct on n and use the output version
of I20 to obtain u_n>=u_0-b_+n-R>=U_min.
Moreover u_K tends to infinity as g_lat,0 tends to zero.

Let s^sharp be the supremum of s<=gamma such that all initial
values in (0,s] stay admissible through K. Prefix continuity
inductively shows that s^sharp itself is admissible. All finite
u_j there remain finite by the two-sided prefix bracket. If
s^sharp<gamma and every level were strictly inside u_j>U_min,
finite-step continuity would extend admissibility to a right
neighborhood, a contradiction. Thus some u_k*=U_min at the
boundary; if s^sharp=gamma one can take k*=0.
I20 on [k*,K] gives u_K(s^sharp)<=U_min+R<=U_ph.
The continuous u_K on (0,s^sharp] ranges from infinity to a value
<=U_ph. The intermediate value theorem supplies u_K=U_ph.
Its solution set is closed away from zero and has a smallest
g_lat,0; use that as the deterministic selection.

Define this selected value to be g_lat,0(a;ell,U_ph), for
a=ell L^(-K), and g_std,0=sqrt(2N)g_lat,0. Every trial trajectory
was generated forward from its own initial value. Choosing which
trial hits the terminal target is a boundary-value choice, not
use of future information in the step estimates. No uniqueness
or monotonic response is claimed. For K=0 set u_0=U_ph.

Along the tuned trajectory

    U_ph+b_-(K-j)-R<=u_j<=U_ph+b_+(K-j)+R,
    u_0=U_ph+K b_*+O(log(1+K)),                       (I22)

where the explicit error is I21 with U=U_ph-R, not a hidden
level constant. The bulk definition makes the same selected bare
coupling work for every compatible volume.

Lastly |u_(j+1)-u_j|<=D_u=b_*+R+C_rho/U_min.
Both adjacent weight ratios are <=sqrt(1+D_u/U_min).
A conversion of up to six field derivatives therefore costs at
most (1+D_u/U_min)^3 when that is the required conversion.
It belongs inside the single-step operator bound, not in an
uncontrolled product of K such bounds. Older retained fields
keep their own weights. A directly transported ratio telescopes
only when the actual maps justify that identity.

## S13 — GAP: G6, the actual causal flow inputs

**Consumes:** the complete bulk action after extraction.
**Must produce:** the partial-sum theorem, real unweighted Hessian
remainder, prefix continuity and FI-1 used in S12, uniformly in volume.

FLOW §110 still lists L-loc2 and Pi-loc as argued, T-a1-M,
T-a3, T-b and T-c as open, and the rate/causality items. Its
Cartan C-part bounds through order two do not prove the full
one-loop partial-sum hypothesis for every depth. Exact FP and
transverse telescoping must be performed before estimates; they
do not supply the missing coefficient bound.
The separate convergence-rate claims are not required by I18;
bounded one-loop partial-sum error and the causal remainder are.
TOW's fixed-level locality and the constant-curvature neighborhoods
that shrink with depth also cannot supply H1's fixed margins or
G5's six-field/four-source bounds on general histories.

An O(1/u_j) weighted activity norm alone does not imply
|varrho_j|<=C_rho/u_j. LOCOP L7 loses h_j^(-2)=u_j/N when
extracting an unweighted Hessian. The required bulk moment estimate,
or a correspondingly stronger weighted input, is a distinct
obligation. Uniform continuity and a volume-independent bulk
definition also cannot be inferred from each finite torus's
positive integral. Continue conditional on G6; I22 is not yet
an actual-model asymptotic-freedom theorem.

## S14 — DRAFTED(high): the simultaneous constant window

**Consumes:** fixed producer constants, the chosen graph/representation,
and explicit envelopes for their dependence on U_min.
**Produces:** an exact feasibility test and a conditional selection
order valid for all levels.
**Most likely failure point:** assuming a producer constant stays
fixed when L, the domain, or the charge allocation changes.

Producer constants may depend on N,L,kappa, the chosen source
directions, preliminary coupling range, fixed domain margins and
the prefix slope/defect. Terminal unit conversions also depend on
the fixed ell,U_ph. None may depend on K, volume, j, or an individual
history. The ledger is:

| Window | Test before iteration |
|---|---|
| Flow | U_min>=max(1,u_base), C_rho/U_min<=b_*/2; U_ph>=U_min+R. If U_ph is prescribed, this is also an *upper* bound U_min<=U_ph-R. |
| Domains/orders | One fixed positive margin in each declared coordinate convention; p=6, q=4 reproduced. Any source-dependent field transport supplies the larger order instead. |
| Matched clusters | eta_bg<=eta_bar<1/4, eta_bg+d_new<=1/4, d_new/(1-4eta_bar)<=P_cluster. Full history/tail roots are included. |
| Support | Fresh construction at mu+2 for I08; mu+3 when using RM12's extra reserve. No iteration of a shrinking exponent. |
| Holes | I11 at tau>mu, and D_hole as I12; or delta_hole>log7 and I13 on only a degree-eight graph. |
| Gap/cut applicability | U_min>=kappa^(-1) when I10's t>=1 cap estimate is used; U_min>=4 and epsilon_j sqrt(u_j)>=8 for I17. All further actual small-chart cut bounds remain imposed. |
| Charges | Every original plaquette's total allocations <=1; all polynomial, regulator and entropy uses are in that same ledger. |
| Returned operator | lambda has its actual post-conversion bound, for example I19. A_L alone is insufficient. |
| Residual ball | The simultaneous I23–I25 test below, including M_init and the map's radius of validity. |
| Coefficients | The actual v recursion preserves V, the supported prefactor log <=P_*, the main-action bound at U_ph <=W_*, and the scalar record follows its own recursion. |
| Terminal source units | The original-source direction map and any physical chart conversion have uniform specified norms; no hidden inverse source radius. |

Here is the complete residual test. Let

    a_lin=lambda+B s_*+eta_*,   E=B e_*,   d=1-a_lin,
    0<=s_j<=s_*, 0<=eta_j<=eta_*, 0<=e_j<=e_*,
    lambda,B,C>=0,   0<M<=M_map,   M>=M_init.          (I23)

The actual transition must obey

    x_(j+1)<=(lambda+B s_j+eta_j)x_j+C x_j^2+B e_j.     (I24)

This scalar majorant certifies ball invariance with its strict
linearized-on-the-ball bound exactly when the chosen constants meet

    d>0,   C M<d,   C M^2-d M+E<=0.                  (I25)

These are REFMATCH RM25's inequalities with all losses retained.
For C>0 put Delta=d^2-4CE. A feasible M must lie in

    [M_-,M_+] intersect [M_init,M_map] intersect (0,d/C),
    M_+/-=(d+/-sqrt(Delta))/(2C),   Delta>=0.          (I26)

Conversely every point in that intersection satisfies I25.
If E=0, exclude the endpoint d/C, and M=0 is still excluded.
At Delta=0 and d>0 the midpoint d/(2C) has theta<1 and is
allowed if the other bounds permit it. For C=0 the test is
d>0 and max(M_init,E/d)<=M<=M_map, with M>0.
If d<=0 there is no such strict certificate, even if an
alternative window theorem might work. This is elementary
quadratic algebra, not a computed physical constant.

A useful sufficient selection is: obtain a_lin<1 first, choose
M>=M_init with C M<=d/2 and M<=M_map, then require E<=d M/2.
It proves mutual consistency of these *algebraic* requirements
whenever the supplied envelopes allow these choices.
Increasing U_min cannot shrink an uncontrolled coherent eta_*.

Hole cost and contraction are coupled. For fixed other costs and
a chosen upper allowance D_allow on D_hole, I12 requires

    D_allow>max(1,A_hole),
    delta_hole>=-log{1-[1+(D_allow-max(1,A_hole))/(16A_hole)]^(-1/4)}
                                                               (I27)

when A_hole>0; take strict inequality if strict operator slack
is needed. This is just solving I12 for exp(-delta_hole).
D_allow must itself fit I19 and a_lin+CM<1.
The actual paid tau must exceed mu by at least this much.
One cannot independently choose a large D_hole and a small lambda.
For A_hole=0 there is no active-hole cost and I27 is unnecessary.

Fresh-gap prices have an all-large-u window only with fixed
reader/entropy constants. If their total local debit is
c_0+c_1 log u, then q_gap(u) minus that debit tends to infinity
for I10's 0<delta<1. The assertion is uniform for every
u>=U_gap once that threshold is defined by the displayed
inequality, not merely at a single test value. It supplies
neither the no-gap bound nor the actual joint majorant.

A noncircular choice order is: fix N,L,kappa and the graphs;
fix domain/source conventions and the positive b_*,R from
one-loop data; obtain producer constants on the preliminary
prefix range with slope b_*/2; allocate original resources and
choose the support/hole surpluses; evaluate I19 and I26;
choose a final U_min meeting *all* lower thresholds and
U_min<=U_ph-R. Then freeze the tuple before any depth K is
chosen. If L must change, recompute every L-dependent
constant and restart this test. The limit A_L->0 alone
does not prove it beats D_other(L)C_tr(L).

Two further explicit checks make these tests usable. For power cuts
epsilon(u)=u^((delta_c-1)/2), 0<delta_c<1, and a supplied chart ceiling
0<epsilon_bar<=1, both epsilon(u)sqrt(u)>=8 and
epsilon(u)<=epsilon_bar hold at every u>=U_min if

    U_min>=max(8^(2/delta_c),epsilon_bar^(-2/(1-delta_c))). (I27b)

This follows by the two powers' monotonicity. It is a choice of cut
window, not a proof of selector regularity.

For a finite-reader atom certificate, suppose the actual type count
and support-size bound give
r_type=A_type exp(sigma_in c_s-nu_R), with sigma_in the required
input rate, and the small-field rooted contribution is e^(h_sf)h_sf.
These are supplied joint-majorant data, after all derivative and
reference costs. For q_star<=1/4-eta_bar put
q_tail=q_star-e^(h_sf)h_sf. When q_tail>0 and A_type>0, the complete
test e^(h_sf)h_sf+r_type/(1-r_type)<=q_star is equivalent to

    nu_R>=sigma_in c_s+log A_type+log[(1+q_tail)/q_tail]. (I27c)

Indeed it is r_type<=q_tail/(1+q_tail)<1. Unbounded readers
require their actual summed support weights instead of an invented c_s.
This exhibits how the support reserve and type entropy enter the
same window as the price; it creates no independent source of payment.

## S15 — GAP: G7, an actual nonempty common window

**Consumes:** the actual envelopes and constants from G1–G6.
**Must produce:** one concrete or analytically bounded tuple satisfying
the complete S14 ledger for every u>=U_min and every admitted state.

The source packet does not supply the post-hole returned norm,
coherent eta_*, creation e_*, all mixed coefficient budgets or
the actual paid tau. Thus neither I26 nor I27 has an evaluated
model antecedent. A list of symbols with separately plausible
smallness is not a verification that their windows intersect.
In particular U_ph may be too small for the needed U_min;
no claim here reaches an arbitrary strong physical scale.

The abstract constraints are consistent under the sufficient
conditions in S14; their actual-model intersection is unverified.
No numbers have been assigned to unknown constants. Continue
conditional on G7, with exactly one frozen tuple for all K.

## S16 — DRAFTED(high): the joint induction, including the shooting trials

**Consumes:** G1–G7 and the frozen tuple passing S14, with each
producer quantified on prefixes of the chain's own flow.
**Produces:** IH(j) and I20 at every admissible level, for any
finite K and every compatible volume; the tuned trajectories reach K.
**Most likely failure point:** using the terminal tuned bracket
to establish a hypothesis of an earlier shooting trial.

The base comes from G1, with x_0<=M_init<=M. The coupling prefix
of length zero has no increment condition. Suppose IH(j) and
I20 through j have been obtained. The following is the complete
output-to-input map:

| Input used at j | Operation | Output required as input at j+1 |
|---|---|---|
| H0 and actual rho, Z_A | Exact transfer, complete outcome sum, full-reader integration | Same original generating function; all new and old masses, endpoints and complements retained |
| H1 plus G1 | Fixed-domain/selector construction and real differentiation | The same six-field/four-source orders, fixed margins, old-field weights and full source labels |
| H2 plus G2/G3/G4 | Joint charged/regulator integration with spent-fraction update | Valid remaining fractions; no replenishment of an original charge; moments for every new multiplicity |
| G2's matched atoms | I07–I09 or its explicitly stronger-rate version | Supported local log at mu and its separate prefactors; independently regenerated next-step certificate |
| Hole and persistent groups | I12 with G3; I15–I17 or extracted G4 bounds where applicable | All inactive/tail roots and history sums in the same norm; every failure assigned |
| Complete output action | G5's actual Loc and coefficient recursions | New main/reference, v_(j+1) in V, scalar record, all mixed/source functions, residual K_(j+1) |
| Prefix flow and G6 | I18a and the prefix remainder bound | Computed u_(j+1), and I20 through j+1 using no assumption about u_(j+1) |
| Residual x_j<=M | I24–I25 | x_(j+1)<=theta x_j+E<=theta M+E<=M, theta=a_lin+CM<1 |
| All marked source functions | Differentiate the exact identities, S17 | The same sixteen compatible marked subsets, including all outer and scalar terms |

If the computed next coupling is below U_min, this shooting trial
stops; no claim is made about its successor's admissibility.
If it is >=U_min, G1–G5 and their regeneration clauses give
IH(j+1), with the same constants. This proves the prefix theorem
by ordinary induction. It also justifies the small-bare-coupling
interval used in S12: the output bracket proves those trials
never exit, and only then is the next state constructed.
S12 selects a fully admissible trial with u_K=U_ph.

Iterating the scalar inequality gives the explicit uniform bound

    x_j<=theta^j x_0+E(1-theta^j)/(1-theta)<=M.         (I28)

There is no factor K in I28. All support, hole, derivative and
reader conversions already occur inside theta,E, and the
relevant/prefactor bounds have their own regenerated estimates.
If a source or coefficient in V has only an additive O(1/u_j)
increment and no summable or contracting mechanism, S12's
logarithmic sum is not a uniform V_* bound; G5 has then failed.

This proves a sufficient multiscale implication. G2 and G5
contain substantive construction/extraction work of the original
target, so this is not a reduction to manifestly easier lemmas.

## S17 — DRAFTED(high): source records and scalar accounting

**Consumes:** the exact positive original chain with kernels fixed
under sources, and the compatible finite jets in IH(j).
**Produces:** the complete finite source recursion and an explicit
distinction between supported action and vacuum/scalar budgets.
**Most likely failure point:** replacing a total cumulant by an
average of the inner connected four-source coefficient alone.

Let Phi_j(z;U_j)=log E[exp(sum_i z_i O_i)|U_j] under the
unperturbed actual chain, and J_(j,B)=partial_B Phi_j(0).
The Markov tower property gives
exp Phi_(j+1)=E[exp Phi_j|U_(j+1)].
Work in the finite algebra z_i^2=0. Expanding exp and log and
collecting the coefficient of z_B yields

    J_(j+1,B)=sum_(pi partition B)
                 kappa(J_(j,C):C in pi | U_(j+1)).    (I29)

This is a finite identity, with no analytic continuation or
all-order claim. Initially J_(0,{i})=O_i and the higher distinct
subsets vanish for the specified linear tilt. At final integration
apply the same partition identity once more. All fifteen
nonempty subsets, including singletons and triples, matter.
Distinct-label extraction has no extra 4!. Histories are weighted
by their actual masses before an unconditional statement.

For an exact scalar c_j(J), record its recursion separately.
If e_j^vac=c_j/|Lambda_j| and a_j^vac(J) is the new scalar per
level-(j+1) site, the common convention is

    e_(j+1)^vac=L^4 e_j^vac+a_j^vac,
    e_K^vac=L^(4K)e_0^vac
                   +sum_(j=0)^(K-1)L^(4(K-1-j))a_j^vac. (I30)

This follows by |Lambda_j|=L^4|Lambda_(j+1)|. It displays the
possible vacuum growth instead of hiding it in x_j.
These vacuum densities are distinct from the creation errors e_j
in I24. Lambda_j here denotes the whole level-j site lattice,
not a selected active mask.
The field difference
S_K(V;J)-S_K(1;J) removes c_K(J) exactly, but the generating
identity I02 still retains c_K(J). Source derivatives of an
unsubtracted effective action or of Z_0(J)/Z_0(0) cannot
discard c_K(J)-c_K(0).

## S18 — GAP: G8, terminal assembly and physical source/scalar bounds

**Consumes:** the history-labelled local pieces and all coefficient
records at level K.
**Must produce:** the exact terminal representation I31 in S19,
its terminal graph/domain dictionary, and any raw scalar or
physical-source uniformity being claimed.

A bound on every conditional action does not bound the logarithm
of their weighted sum. Either the complete history mixture has
already been included in G2's exact connected construction, or
a final differentiated matched expansion must do so. The latter
is an additional required operation; replacing
-log(sum_h R_h) by a sum or average of -log R_h is invalid.
This terminal assembly is unnecessary as a *new* step only when
the producer explicitly outputs I31 already.

Similarly, a full norm on a multilevel reader graph does not by
itself give a local norm on the terminal physical block graph.
The exact mapping must keep every original source label while
paying its actual geometric reader support and all norm changes.
Four-source weights r_i fixed along j may still depend on the
cutoff a; no uniform physical derivative follows if the required
original direction norms or inverse weights diverge. These
quantities must be bounded for the particular physical sources.

Finally I30 is not a uniform raw scalar budget. If one wants
unsubtracted action values or source-only derivatives, supply
a bound on those derivatives of c_K per physical volume, or
specify explicit counterterms/subtractions while retaining
their exact source response. The endpoint below states field
derivatives and field-difference bounds without assuming such
a scalar bound. Continue to that endpoint conditional on the
terminal representation/domain portion of G8.

## S19 — DRAFTED(high): fixed-scale real derivatives of the effective action

**Consumes:** S16 at u_K=U_ph and the exact fully assembled terminal
representation below, with all its bounds uniform in K and volume.
**Produces:** explicit bounds through six real field derivatives
and four marked original-source derivatives.
**Most likely failure point:** asserting the representation of
the fully summed action from bounds only on conditional pieces.

After every nonterminal field has been integrated, require on
the declared terminal real domain

    S_K(V;J)=c_K(J)+sum_(X subset Gamma_K) A_(K,X)(V;J),
    A_K=U_ph W_K^tree+V_K+P_K+K_K,
    ||W_K^tree||_(mu,T_K)<=W_*,
    ||V_K||_(mu,T_K)<=V_*,  ||P_K||_(mu,T_K)<=P_*,
    ||K_K||_(mu,T_K)<=M,
    A_*=U_ph W_*+V_*+P_*+M,   h_ph=sqrt(N/U_ph).       (I31)

P_K is the supported prefactor *action*, with its actual sign;
it is not a discarded normalization. Constants multiplying
W_* are stated in the chosen tree convention. The exact
reference field 1 and the evaluation fields lie in the
supplied domain. All scalar source terms not in supported
coefficients remain in c_K.

For 0<=r<=6, B a subset of the four labels, and ordinary
group directions H_1,...,H_r, the coefficient of that word in
the positive Taylor sum I04 immediately gives

    sup_v sum_(X:v in X)e^(mu|X|)
       sup_D |D_(H_1)...D_(H_r) partial_B A_(K,X)|
      <= r! A_* h_ph^(-r)
                    product_l ||H_l||_infinity
                    product_(i in B) r_i^(-1).        (I32)

For the direction-supremum version, take each H_l of ordinary
sup norm <=1; homogeneity gives the displayed general form.
Only one terminal field species remains, so the field divisor
is r!. These are real derivatives of the same effective action,
not Cauchy estimates from value bounds.

If r>=1, take one H_l supported on a set S of terminal blocks.
Every contributing X intersects S. Root its sum at all vertices
of S, an overcount by nonnegative terms. The scalar drops out.
Thus

    |D_(H_1)...D_(H_r) partial_B S_K|
       <= |S| r! A_* (U_ph/N)^(r/2)
                    product_l ||H_l||_infinity
                    product_(i in B) r_i^(-1).        (I33)

This is uniform in K and in the total volume for fixed S.
For directions spread over the entire lattice replace |S|
by |Gamma_K|. An extensive action with arbitrary extensive
directions is not claimed to have an absolute volume-independent
derivative; its bound per terminal block is uniform.

Set S_K^flat(V;J)=S_K(V;J)-S_K(1;J).
The family A_(K,X)(V;J)-A_(K,X)(1;J) has norm <=2A_*:
evaluation at the same source point preserves all source jets,
and the second term has zero positive field derivatives.
This gives the corresponding r=0 value/source bound

    |partial_B S_K^flat(V;J)|
        <=2 |Gamma_K| A_* product_(i in B)r_i^(-1).   (I34)

For r>=1 the sharper I33 is unchanged. A source-only derivative
can be localized when its original reader assignment has a
specified bounded support, using that support as the root.
For the raw S_K at r=0 add |partial_B c_K|; S18 explains why
this term has no asserted uniform bound.

There is also a direct separation bound when G8 certifies connected
terminal supports X, including any paid connecting hulls. Suppose
the derivative directions and/or source labels force a contributing X to
meet sets S_1,...,S_m. Let
ell_conn=min{|X|: X connected and X meets every S_i}.
For any anchor S_i the same proof of I33 gains
exp(-mu ell_conn), since every nonzero summand has that many
vertices. If no such support exists the derivative vanishes.
This concerns locality of the effective action, not decay of
Schwinger functions or a spectral gap.

## S20 — DRAFTED(high): physical units, scope of the endpoint and recovery

**Consumes:** I31–I34, fixed ell,U_ph and the explicit physical
direction/source maps.
**Produces:** a cutoff-independent fixed-physical-scale formulation
of the real field-derivative bound, with remaining assumptions visible.
**Most likely failure point:** suppressing the norm of a cutoff-dependent
map from a physical source to original lattice coefficients.

Define a physical connection direction H on terminal links by the
actual group variation V_b(s)=exp(s ell H_b)V_b. Ordered such
variations are ell times the corresponding invariant derivative.
For r>=1, I33 becomes

    |D_phys,H1 ... D_phys,Hr partial_B S_K|
      <= |S| r! A_* [ell sqrt(U_ph/N)]^r
                    product_l ||H_l||_infinity
                    product_(i in B) r_i^(-1),
    1<=r<=6,  B subset {1,2,3,4}.                    (I35)

Every factor on the right is fixed as a=ell L^(-K) tends to
zero. This proves the requested *conditional* real-derivative
output at one fixed weak physical scale.
For ordinary Frechet derivatives of a chart A -> exp(ell A),
apply the real chain rule with its actual chart derivative
constants on the fixed inner domain. Through order six those
are a finite Bell-polynomial conversion; their uniform
domain bounds must be supplied in G1/G8. I35 itself uses
group variations and needs no uncomputed chart conversion.

If a physical source coordinate z_i instead acts by an original
direction v_i(a), use its explicitly computed weighted norm
L_i(a) in place of r_i^(-1) for a unit coordinate direction.
The bound is uniform only if these L_i(a) have uniform upper
bounds. This replacement is valid only when those very directions
were carried in I04 from the start, or the full RGA3 source-direction
supremum is supplied. Four fixed labelled jets do not control
unrelated source directions chosen afterwards.
No rescaling of sources or kernels is performed during
differentiation. In the factorial q-source norm the corresponding
mixed estimate has r!q! and the actual source direction norms.

For a terminal torus of physical volume Vol, let the certified
support graph use blocks of fixed side m_blk terminal lattice
spacings. Then |Gamma_K|=Vol/(m_blk ell)^4, and the global
version of I35 divided by Vol has factor (m_blk ell)^(-4).
For a unit-cell support graph m_blk=1; for blocks of L^4 terminal
sites m_blk=L. The graph/direction conversion in G8 must establish
which convention is used rather than silently equating these counts.
The local version for fixed S has no volume factor.
The tunable bare coupling is g_lat,0(a;ell,U_ph) of S12,
with the explicit logarithmic correction I21; it is not
chosen by imposing a future coupling inside any local estimate.

This endpoint provides neither convergence of these actions
as K tends to infinity nor an all-order hierarchy, continuum
Euclidean symmetry, matching coefficient or mass gap.
The raw source-dependent scalar remains an exact recorded
component, with its unproved uniform bound identified in G8.

The current recovery checkpoint is this file and its source
table. The next discriminating work is an actual complete
mixed-core construction satisfying G2, carrying at least one
coarse derivative and all four original labels, and then its
regeneration test. The returned-operator/hole/charge budget in
G3–G5 and the causal bulk estimates in G6 must also produce a
common S14 tuple. Reopen the claimed endpoint only when the
relevant source bytes or one of these estimates changes.

## Author verification record

The complete argument was read back after reaching the endpoint;
the amended definitions and scopes were then checked again. The
written checks covered the joint history/root sum and nested-mask
identity, the nonmonotone charge correction, the causal first-exit
shooting proof, the quadratic window including C=0 and zero
discriminant, the cumulative coefficient/prefactor requirement, and
the terminal derivative units and scalar subtraction. These are
author checks, not an independent scientific review.

Deterministic file checks confirmed all nine source SHA256 values
and their equality to HEAD, the unchanged author brief, twenty
consecutive steps (zero PROVEN, twelve DRAFTED, eight GAP), every
step's required interfaces, all eight named gap definitions,
35 unique equation labels with no undefined references, and all
nine local links. The REFMATCH quotation matches its source after
whitespace folding. The new-file whitespace check produced no
diagnostics. Tracked files have no diff; the only new output is
INDUCT.md, alongside the pre-existing untracked author-brief
directory. No numerical experiment or independent review was run.

The mathematical outcome remains conditional: G1–G8 are not
discharged, and the actual-model common constant window is not
established. Remote freshness remains limited by the recorded DNS
failure. No landing or retained scientific status is asserted.
