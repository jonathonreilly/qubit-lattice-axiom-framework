# Compact rooted-forest disintegration and aligned exchange

Research proof draft, 2026-11-08. A fresh-context mathematical check is recorded
in `../gates/forest-flat-check.md`; this is not formal audit or retained status.
Source checkout: `1e0d3b58dcda7f83152b0bb51729260247454d65`.
Read: SCIENCE_WORKFLOW; bounded two-region note §§1–3,7; historical
MANUSCRIPT_RG at `89faef229ff6e6bde42baad15ed8270c2f4087d8`, lines
3788–3829 and 3869–3925. Preflight: go; model-floor check had no target;
memory cap unavailable. No numerical job. Literature/route-search coverage
is left to the supervisor; this bounded worker performed no literature search.
The proof below uses only normalized Haar invariance and finite integration.

Prior-art reconciliation: the pinned draft's SOURCE_LOCAL_RETURN_ASTRA
lines 315–368 already supplies compact tree-Haar disintegration and exact
orbit averaging. MANUSCRIPT_RG section 4.30 supplies the replica exchange
route and its unsigned pure-orbit obstruction. The contribution here is the
explicit shared gauge at arbitrary finite depth, terminal-root forest,
aligned exchange and two-source orbit-covariance accounting in one proof.
No novelty claim is made for tree gauge or the replica identity separately.

## 1. Precise setting and theorem

Fix a finite depth k>=1 and finite beta>=0. Let E_l be independent oriented links of embedded finite level-l lattices,
l=0,...,k, with level vertices nested in fine vertices X. Put Q=X_k.
Fix U_k=V. Every soft factor is

    k_l,c(b|a)=exp(lambda_l <b,M_l,c(a)>)/Z(lambda_l |M_l,c(a)|),

where M is the stated average of path transporters with common endpoints;
lambda_l is finite and nonnegative. Allow different finite lambdas per edge.
The hidden density against product probability Haar is

    p_V(U)=q_beta(U_0) product_(l=0)^(k-1) product_(c in E_(l+1))
                              k_l,c(U_(l+1,c)|U_l),
    N_V=integral p_V(U)dU,     pi_V=p_V dU/N_V.                 (1)

All Z factors in (1) are present. Strict positivity and compactness give
0<N_V<infinity. One fine-site gauge h(x) acts at every embedded level by
U_l(x,y) -> h(x) U_l(x,y) h(y)^*, with h(q)=I for q in Q.

Partition X into terminal cubical blocks, each containing its one terminal
site. Choose an internal spanning tree per block, rooted at that site; their
union T is the forest. (The assertions also hold for any partition into
connected root-containing sets.) Denote its positive or reversed oriented
fine edges by T. Let J consist of fine non-tree links and all hidden links
at levels 1,...,k-1. Define

    A = SU(2)^J,        H = SU(2)^(X\Q).

There is a globally defined bijective, continuous compact-coordinate map
U <-> (a,h) in A×H, with all tree links of a equal to I. It preserves product
probability Haar, exactly:

    dU = da dh,          p_V(U(a,h))=pbar_V(a)=p_V(a,T=I).
    pi_V(dU) <-> [pbar_V(a)da/N_V] dh.                       (2)

There is no chart, exceptional set, determinant factor, or gauge-volume
constant. Here “product coordinates” refers to reference Haar da, not to
independence under the generally interacting posterior pbar_V da/N_V.

## 2. Construction and measure proof

For the root-to-x oriented path in T let h(x) be its original U_0
transporter, with h(root)=I. Recursively h(y)=h(x)U_0(x,y) along a tree
edge directed away from the root (use U_0(y,x)^* if the independent
orientation is reversed). Set a_l(x,y)=h(x)U_l(x,y)h(y)^*.
Then every tree link is I. Conversely, given (a,h), reconstruct every
hidden link by

    U_l(x,y)=h(x)^* a_l(x,y) h(y),                           (3)

with a=I on T. These operations are mutually inverse, including reversed
orientations and periodic edges. Terminal links remain V since endpoints
are in Q. A tree has exactly |X|-|Q| edges, so dimensions match, but this
count is not the measure proof.

Under independent fine tree-link Haar, the recursively constructed h(x)
are independent Haar: order vertices parents first, condition on earlier
ones, and use left invariance for the fresh tree edge (and inversion
invariance if needed). Given tree variables, all remaining original links
are independent Haar; their transformation uses fixed left/right unitary
multipliers and therefore remains independent Haar, with a distribution
independent of h. Fubini proves dU=da dh for every bounded measurable
integrand. This proves the change of variables without a formal Jacobian.

Every fine plaquette trace is invariant. Telescoping along every path gives
M_l,c(a)=h(x)M_l,c(U)h(y)^*. Quaternion norm and the pairing of its
output with its mean are invariant. Consequently each numerator AND each
Z(lambda |M|) are invariant separately. The final output is unchanged.
This proves (2), including N_V=integral pbar_V da. The root-fixed action
is free: a gauge fixing all tree links must be constant along each tree,
and hence I. No residual stabilizer is divided out.

## 3. Reader sets and locality statement that is actually true

Treat the individual Wilson and normalized kernel factors as w_b with full
hidden-link readers S_b. A fixed output V is a parameter. In particular a
kernel reader set includes every path-mean input read by its normalizer.
In reduced coordinates

    pbar_V(a)=product_b wbar_b(a),
    wbar_b(a)=w_b(a,T=I),       readers(wbar_b) subset S_b\T. (4)

Thus reduced-factor readers do not enlarge. This is an algebraic statement
about the new compact variables; it is not an assertion that a_l depends
locally on original individual fine links at fine-lattice scale.

For the latter question, a_l(x,y) in original variables reads its original
U_l(x,y) and fine tree paths P_x,P_y. Each P_x stays inside x's terminal
block. Define terminal-block support of a set of links as the set of blocks
containing their endpoints. Pullback of any reduced reader set therefore
has terminal-block support contained in its original endpoint-block
support: enlargement radius zero with this explicit convention. If instead
one labels a link only by its tail block, its endpoint block can be one
terminal-block step away for the stated nested nearest-neighbor levels;
the same bound is radius at most one. These statements use the internal
block trees; an arbitrary long spanning tree would not have this property.
They bound spatial diameter in terminal-block distance, not reader count,
fine-link distance, oscillation size, or interaction strength. A whole tree
can be long inside one terminal block. For arbitrary observables support
must be recomputed from their actual formula, not inferred from invariance.

## 4. Exact aligned replica exchange

Write nu_V(da)=pbar_V(a)da/N_V. For R subset J, let tau_R swap just a_R
between a,a', and retain both sets of orbit coordinates h,h'. This is an
involution preserving da da' dh dh'. In original links the received value
at e=(x,y) in R is

    U_new,e = h(x)^* h'(x) U'_e h'(y)^* h(y),              (5)

and analogously with replicas reversed. Fine tree links and all unselected
links are unchanged. Formula (5) follows by reconstruction (3), so this
really is a gauge-aligned exchange. It does not exchange h or use an
independently pinned posterior.

Define, with (b,b')=tau_R(a,a'),

    Delta_R=log[pbar_V(a)pbar_V(a')/(pbar_V(b)pbar_V(b'))]. (6)

Every factor with all readers in R or all outside R cancels from (6).
Only crossing readers from (4) remain; full normalizers remain in those
factors. This is exact for all finite couplings and every fixed V.
For bounded real f=f(a_R), g=g(a_(J\R)), put
D=(f(a)-f(a'))(g(a)-g(a')). Then

    Cov_nu(f,g)=1/2 E_(nu×nu) D
              =1/2 E_(nu×nu)[D tanh(Delta_R/2)].          (7)

Indeed D∘tau_R=-D, Delta_R∘tau_R=-Delta_R. At paired points with
unnormalized densities q and q', tanh(Delta_R/2)=(q-q')/(q+q'). Averaging
the integrand over the measure-preserving involution proves (7).
Fixed points have D=0 and cause no exception. This also follows by direct
symmetrization, without constructing a measurable orbit transversal.

The separate-reader requirement is essential: (7) is not asserted for an
arbitrary pair of overlapping functions. Even an originally local gauge-
variant observable acquires tree-path/orbit readers; its support must be
checked. Gauge invariance under H guarantees no h dependence, but does
not by itself guarantee separate supports after a chosen R is specified.
One may apply the same proof on the full product (a,h) if the actual full
reader sets are separated and the exchange involution makes D odd.

## 5. Source-dependent generating functional, with orbit covariance

For bounded real F,G on the original hidden chain set
F_a(h)=F(U(a,h)), G_a(h)=G(U(a,h)), and

    A_st(a)=integral_H exp[sF_a(h)+tG_a(h)]dh,
    N_V(s,t)=integral_A pbar_V(a) A_st(a)da,
    nu_st(da)=pbar_V(a)A_st(a)da/N_V(s,t),
    eta_st(dh|a)=exp[sF_a(h)+tG_a(h)]dh/A_st(a).          (8)

Equations (2),(8) are the exact full normalized sourced posterior. Let
f_st(a)=E_eta F_a, g_st(a)=E_eta G_a and
c_st(a)=Cov_eta(F_a,G_a). Bounded differentiation gives

    partial_s log A_st=f_st,
    partial_s partial_t log A_st=c_st,
    partial_s partial_t log N_V(s,t)
       = E_nu_st c_st + Cov_nu_st(f_st,g_st).             (9)

At zero sources eta_00=dh, nu_00=nu_V. In particular projecting F and G
separately onto orbit means loses E_nu c_00 unless it is proved zero.
When F,G are H-invariant, A_st=exp[sf+tg], c_st=0, recovering the usual
quotient formula exactly. A source on U_0 is simply a special case.
Source-dependent exterior conditionals use their full numerator and
normalizing denominator; applying (8),(9) to each and subtracting their
log derivatives preserves the two-region note's Q term.

The source-tilted quotient exchange uses
pbar_st=pbar_V A_st and the same (6),(7) for functions with separate
readers under nu_st. A_st can have nonlocal readers and must itself enter
the crossing factors. The functions f_st,g_st likewise require a fresh
reader check. If their readers are separated, (9) and (7) give

    Cov_pi_st(F,G)=E_nu_st c_st
       +1/2 E_(nu_st×nu_st)[(f_st(a)-f_st(a'))
                           (g_st(a)-g_st(a')) tanh(Delta_R,st/2)]. (10)

Without that support condition (9) is still exact, while the last exchange
representation is not claimed. One could instead exchange coordinates in
the full density pbar_V exp[sF_a+tG_a]; all source factors and their
actual orbit readers must then be retained.

## 6. Pure-gauge case and precise quantitative boundary

For V=I consider the exact measure obtained by pushing independent Haar
h through U_l(x,y)=h(x)^*h(y), with h|Q=I. In (2) its quotient is the
single point a=I. This is the same orbit convention as historical RX8
with h there replaced by h^*. All H-invariant functions are constant on
this orbit; their covariances and aligned-exchange response vanish. The
aligned exchange itself is the identity, including on original links:
both replicas have a=I, so reconstruction leaves each original orbit
configuration unchanged. No ratio of singular quotient densities is
needed: Delta=0 is the continuous finite-density expression (6) evaluated
at a=a'=I. Formula (7) has zero integrand for invariant functions.

For arbitrary F,G the exact covariance is instead Cov_H(F_I,G_I).
It need not vanish. Take any fine tree edge and F=G=w(U_e). Its endpoints
include at least one free gauge and U_e is Haar; uniform S^3 gives mean
zero and second moment 1/4. Thus the covariance is 1/4, entirely the
orbit conditional term in (9). Conversely observables whose orbit
readers are disjoint free sites are independent under Haar H. For a
nontrivial compatible pure-gauge terminal V the same statement holds
with any fixed pure-gauge representative a^0 and its H orbit; it is not
an assertion that arbitrary V admits a pure-gauge representative.

These exact pure-orbit statements do not assert that the finite-coupling
posterior is pure gauge. At finite coupling it has a strictly positive
quotient density on all of A. If a separate concentration theorem gives
weak convergence to that orbit, bounded continuous invariant covariance
converges to zero at each fixed finite system. Such qualitative convergence
does not supply a rate or a cutoff-, depth-, boundary-, or volume-uniform
estimate; arbitrary bounded discontinuous tests are not covered by weak
convergence alone.

The compact disintegration and exchange identity supply no small bound
on Delta_R or its mixed derivatives and no summable response in terminal-
block distance. The universal immediate bound from (7) is only
|Cov_nu(f,g)| <= (1/2) E|D|, with |tanh|<=1; the sharper elementary
oscillation bound |Cov|<=osc(f)osc(g)/4 is also distance independent.
Rooted gauge alignment removes the independent pure-orbit coordinates
exactly. It leaves all quotient interactions, all normalizers, and (for
noninvariant sources) the orbit covariance. Estimating the quotient
connected response remains a separate quantitative problem.

## Checkpoint and provenance

Closed in this draft: global Haar disintegration; complete normalized
posterior at arbitrary fixed V; the explicit terminal-block reader bound;
aligned exchange and its exact support hypothesis; complete source/orbit
covariance; pure-orbit evaluation and explicit noninvariant covariance.
No two successive failed reductions occurred. No full response-decay
claim, numerical checks, commits, pushes, or independent check were made.
The model is the inherited supervisor model; its exact identifier is not
exposed by the host tools. Launch metadata supplied by the supervisor:
`fork_turns=none`, reasoning effort `medium`. No model identity is guessed.
