# Repo search

Writer: Codex, task-configured gpt-6-astra xhigh (the runtime identifier is
not independently exposed), 2026-11-17. Source commit
`506875a5eb43c3c77253eef37c1f476817aad9cc`. This checks row 1096 by
Claude Fable 5.2 medium. It is research text, not an audit; it grants no
status and claims no Yang–Mills mass gap. It does not cover row 1097,
a new attack on PIN-U or EV, or Lean formalization. No computation
discharges a mathematical step.

The target-specific prior file is absent. The lead's 2026-11-08 digest
covers earlier UV/RG targets across main and PRs 10114, 10133, 10134 and
10141. It reports no supplier of this later sheet-field statement.
I read that digest and checked its closest relevant hits at their sources:

| Source checked | Closeness |
|---|---|
| Main `research/ym4d/library/fp1.md:235–258`, at `8b11ae2bb95e641494fe75ed83d108ee712fa3a9` | Fixed-scale free Gaussian covariance and conditioning; a different law, not a small-field O(4) estimate. |
| PR 10114 `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149`, at `f76f6c649cff7dffbab664d8976e680e8f287fe9` | Positive one-step plaquette correlation; neither decay nor field stability. |
| Rows 1091 and 1094, read in full | Direct suppliers of the face specification, conditional block theorem, covariance identity and scope corrections. Credited and used at their stated conditional scope. |

Exact sheet-field/FST/PIN-U/Heisenberg searches in `open-registry.md`
found no competing check owner. The open PIN-U/EV proof work is a different
assignment (FINISH 1099); this file does not attack it. The outline's
full-read index was searched first. Its nearest scope entries are
`chunk-01.md:66–73` and `obligations.md:16–30`; outline 580–600 distinguishes
polynomial decay from a positive spectral gap. CA-I 2700–2715 explicitly
excludes a mass-gap assertion. Searches of the index, including 4.12–4.19,
found no FST/PIN-U/Heisenberg supplier under those names. This bounded
search is not an exhaustive absence theorem. Credit Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text. Their
account and Balaban's ultraviolet work supply context, not a premise of
the sign-cluster estimates below.

## Checkpoint

The six planned stages are complete: prior/source checks; full row-1096
and row-1091/1094 readings; primary-source verification; hand checks of
the consumer and counterexamples; checks of the cluster split and stopped
routes; verdicts and corrections. Line numbers below refer to row 1096
at the pinned commit unless a source is named. The checked source files
were not edited. The source receipt and next obligations are at the end.

## 1. FST-F1 and the face consumer

**HOLDS**, as a conditional theorem for real observables, with positive
`h_0,a,X_1` and constants uniform in the torus. Empty local supports give
zero covariance and can be omitted from the maximum defining `X_B`.
Row-1096 lines 45–60, 161–167 respect row 1094's all-observable requirement
and its periodic-local-limit restriction.

FST-F gives (R) by taking `G=e.Phi(u)`, whose sole Lipschitz constant is
at most one. For (L), sum over `b in B`, use
`Lip_b(G)<=L°_G` and `|w-b|_1>=d(w,B)`. This gives
`X(B)=X|B|`. This is a non-strict implication; no strict separation of
these hypotheses is proved.

Here is a direct check of the consumer, without the tilted-measure proof.
Let `P` average the whole-sheet conditional kernels and `h_n=P^n f`.
The conditional covariance identity is

    Cov_mu(f,g) = (1/K) sum_{n>=0} sum_e
                   mu[Cov_{mu_e^eta}(h_n,g)],   K=|E_T|.

M1 and M2 give `|H|<=2lambda` and a one-site field change of size at most
`lambda rho(q,q')`. Integrating its response gives the influence kernel
`lambda X_1 exp(-2a|u-w|_1)`. There are six neighbouring sheets.
The weighted column sum is at most `gamma=6lambda X_1 e^a S_a`:
each periodic one-dimensional shell has at most two points at each positive
distance, and the two geometric series multiply to `S_a`.
Thus `Delta_W(Pf)<=theta Delta_W(f)` with
`theta=1-(1-gamma)/K` and `W(x)=exp(-a d(x,B))`.

Terms for sheets missing B vanish. On a remaining sheet, (L) bounds its
conditional covariance by
`X(B_e)L°_g sum_{u in V_e} Lip_u(h_n) exp(-a d_D(u,B_e))`.
Since `d((u,e),B)<=d_D(u,B_e)`, the sum of these terms is at most
`X_B L°_g Delta_W(h_n)`. Each site belongs to one sheet. Summing the
geometric series gives exactly line 54, including `1/(1-gamma)`.
On the stated lambda interval `gamma<=1/2`. For fixed local supports
separated by n, pass through tori large enough to avoid wrapping, then
through a local weak limit. This gives (17), uniformly on that interval.
It gives no assertion for arbitrary pinned Gibbs states.

## 2. RN, MK and the bond law

**RN: HOLDS.** Put `W=sum_v(H_v-H'_v).Phi_v`, so `|W|<=D`.
The normalized derivative is `exp(W)/E_{H'}exp(W)`, in
`[exp(-2D),exp(2D)]`. A common auxiliary kernel leaves it unchanged.
For `N>=2`, `(4N+1)^2/N^2=(4+1/N)^2<=81/4<21`.
The factor `exp(42 h_0 N^2)` is therefore valid. State this N floor
at line 72; it is already present in T2 and Pei's annulus definition.

**MK: HOLDS AFTER CORRECTION at lines 74–80.** Add: “Conditionally on the
spins, the auxiliary variables used by distinct events are independent,
and each event uses a disjoint set of these variables.” Pei's independent
bond kernels on disjoint annuli satisfy this. Local dependence of each
kernel alone does not imply joint independence. For example, use two
isolated sites and the same external fair bit for both events. At zero
field each event has probability 1/2, their intersection 1/2, whereas
the printed product is 1/4. With the added hypothesis, condition on all
outside spins, factor the interiors and bond kernels, and apply RN to
each factor. This proves precisely the all-pins transfer used in T2.
The “if and only if” in line 82 describes this proof's sufficient
supremum bound; it is not a necessity theorem for transfer in general.

**B: HOLDS for nonnegative bonds and unpinned systems; clarify pins.**
The expansion in line 107 gives independent cluster signs with weights
`exp(s h(C))`, hence mean `tanh h(C)`. The bond weight and the conditional
two-point and covariance identities in lines 103–109 follow. With pins,
replace `2cosh h(C)` by `exp(s_C h(C))` for a cluster forced to sign
`s_C`; incompatible pinned signs give weight zero. An unpinned cluster
keeps `2cosh h(C)`. The printed unrestricted product over clusters must
be labelled “without pins”. Pins with zero first component cannot be
joined by a positive-probability first-component bond. Negative couplings,
allowed in RN, are not allowed in this bond construction.


## 3. P1, A1 and Pei's sign-cluster steps

**P1: HOLDS with its quantified small-field range.** Fix any `beta>0`.
Integrating the free B-spin yields `Z_S3(b)`, independent of the unit
spin at x. Write `X=sigma_x^1`, `Y=sigma_y^1`, `t=XY`,
`k=phi(t)=(1-exp(-2beta t))1_{t>0}`, and let `E_h` have density
proportional to `exp(beta sigma_x.sigma_y-hY)`.
The pinned-minus-free probability is

    D(b,h)=E_h[k exp(bX)]/E_h[exp(bX)]-E_h[k].

At `b=0`, `D=0` and `partial_b D=c(h)=Cov_h(k,X)`.
At zero field, simultaneous first-coordinate reflection makes
`E_0 X=E_0 Y=E_0(kX)=E_0(kY)=0`. Differentiating all three terms of the
normalized covariance therefore gives

    c(0)=0,
    c'(0)=-E_0[kXY]+E_0[k]E_0[XY]=-Cov_0(phi(t),t)<0.

For independent copies t,t', twice this last covariance is
`E[(phi(t)-phi(t'))(t-t')]`. Its integrand is nonnegative, and positive
on a set of positive measure: the spin density is strictly positive and
t takes distinct positive values on open sets. Bounded spins justify the
derivatives and Taylor remainders by dominated exponential series.
Consequently there is `h_*(beta)>0` such that, for each
`0<h<h_*(beta)`, some `b_*(beta,h)>0` satisfies
`D(b,h)<0` for `0<b<min(beta,b_*(beta,h))`.
These are existential analytic constants, not numerical estimates.

Line 117 and the RESULT must say **“arbitrarily small nonzero fields
opposing the chosen pin direction”**, not “every nonzero field strength”.
The proof fixes beta but gives only a small-h interval. P1 uses a single
field direction and an oppositely aligned pin; spatial variation among
unpinned field directions is not itself necessary. Neither this example
nor A1 is a counterexample to the homogeneous sheet's mixing estimate.

**A1: HOLDS.** Here the spin space is S^2, as stated, and h is any fixed
positive real number. At b=0 the amplitudes are independent with positive
density `a(dr) proportional to cosh(hr) dr` on `[0,1]`.
Summing the signs gives the printed `Z_I`. The complementary planar factor
has derivative zero at b=0, because the Haar mean of its cosine is zero.
The derivative of the log weight is exactly `-g(r_x)g(r_y)`, where
`g(r)=r tanh(hr)`. If `m=E_a r`, `z=E_a g`, `t=E_a(rg)`, differentiating
the normalized covariance gives

    partial_b Cov_b(r_x,r_y)|_0
      =-(t^2-m^2z^2)+2m(tz-mz^2)=-(t-mz)^2<0.

Indeed `g'(r)=tanh(hr)+hr sech^2(hr)>0` for r>0; the independent-copy
covariance formula makes `t-mz>0`. Analyticity on this compact domain
gives `Cov_b(r_x,r_y)<0` for `0<b<b_*(h)`.
For any prescribed positive coupling ceiling, intersect that interval
with the ceiling. At h=0 the displayed derivative is zero. No assertion
at homogeneous coupling 2.3–2.6 follows from this small-b example.

Pei source labels identify the statements unambiguously. His downloaded
v2 source has the coarse-orientation material in **Section 7**: row 1096's
“Theorem 6.1, Lemmas 6.2–6.6, Proposition 6.7” mean respectively
`thm:main4`, `lem:celltransfer`, `lem:badsite`, `lem:pm1`, `lem:odd`,
`lem:coupling`, `prop:pinneddecay` (7.1–7.7). The field remark is 7.10.
The Section-2 and Section-3 numbers used in the note are correct.

The following checks concern proposed extensions to fields, never errors
in Pei's zero-field statements.

| Source step and row-1096 use | Verdict and exact reason |
|---|---|
| Projection, `lem:gauss`, source 891–910; line 145 | HOLDS. Condition the fourth coordinate of an S^3 spin. The first three coordinates are rho times a uniform S^2 spin, independent of the fourth coordinate under the reference law. Couplings become `b_xy rho_x rho_y<=beta`; pole pins have rho=1. The first-sign bond kernel agrees exactly. Thus the pole-pinned annulus estimate lifts, with the same N and p. |
| Lemma 2.1, line 90 | HOLDS as the field decomposition: signs acquire `H^1 r`, and the complementary directions acquire their projected field. S^3's amplitude reference is not the uniform S^2 reference; none of B/RN requires it to be. |
| Lemma 2.2, lines 91,109 | HOLDS as the diagnosis. The coupling survives; fair cluster signs and the untruncated spin/connection identity do not. |
| Lemma 2.4, line 92 | HOLDS as a failure of the field extension. At K=0 opposite fields give `E(tau_x tau_y)=-tanh(h)^2<0`; continuity preserves this for sufficiently small K>0. The sign-spin FKG lattice condition still holds and is a different assertion. |
| Lemma 2.5, line 93 | HOLDS as scoped by row 1091 G1: opposite XY fields make the indicated cosine expectation negative. This violates an extension beyond Pei's nonnegative cosine-character coefficients. |
| Lemmas 2.6–2.7, lines 94–95 | HOLDS as a failure of the general extension. A1 already disproves amplitude association, hence also association of the larger amplitude/bond collection. P1 separately disproves pinning monotonicity. |
| Proposition 2.8, lines 95,99 | HOLDS as the P1 diagnosis with the range above. The first pin-to-pole line of Lemma 3.4 is therefore unavailable for arbitrary fields. |
| Lemma 2.9, line 96 | HOLDS as a failure of the general extension. Correct “cosh factors” to “the weights of clusters attached to changed pins”. Free clusters have cosh factors in both pin systems; a forced cluster instead has `exp(s_C h(C))`. |
| Proposition 3.1, line 97 | HOLDS as a cited zero-field input, conditional on Ding–Huang–Yang. It is a pole-pinned estimate, not PIN-U. |
| Lemma 3.3, line 98 | HOLDS AFTER clarifying that RN replaces its proof. Pei's printed anisotropy proof uses a partition-function crossing identity and changes the bond kernel. A field leaves the bond kernel fixed, so RN directly supplies the different, multiplicative bound. |
| Lemma 3.4 and Proposition 3.5, lines 99–100 | HOLDS for the diagnosis: the former's first line fails; its needed product bound is supplied by corrected MK and PIN-U; the latter is a probability/path-counting argument. |

For an explicit hand check of the crossing-identity failure, take the
three-site chain with its two end spins pinned to +e_1, equal strengths
b>0, and field `h e_1`, h>0, at the middle spin. Conditional on its first
amplitude r, put K=br and t=hr. The sign numerator for *no crossing* is

    2cosh(2K+t)-exp(2K+t)(1-exp(-2K))^2.

The numerator after changing the left pin to -e_1 is `2cosh(t)`.
Their difference is `(exp(t)-exp(-t))(1-exp(-2K))>0` for r>0.
Integrating against the positive S^3 amplitude density preserves the
strict inequality. Thus the field crossing identity fails even for an
aligned positive field; this is separate from pinning monotonicity.

## 4. PIN-U, T2 and PIN+

**PIN-U: HOLDS as a well-defined proposed input**, after importing Pei's
annulus definition explicitly: `D_N(z)={N<=|v-z|_infinity<=2N}`, integer
N>=2, all nearest-neighbour subgraphs and strengths in `[0,beta]`, all
vertices on both layers pinned, independent first-sign bonds, and crossings
using actual edges, not artificial boundary wiring. This is a zero-field
O(4) assertion. It is not proved by row 1096.

**T2 on finite subgraphs: HOLDS AFTER the endpoint correction
`0<p'=exp(42h_0N^2)p<4^{-25}`.** The constants for positive p' are right.
For separated annuli, the unpinned interiors have no connecting edge.
A crossing contains a segment between its last inner-layer visit and first
outer-layer visit. That segment uses only edges incident to the interior;
therefore layer-only bonds may be omitted from the crossing test.
Corrected MK bounds the joint event by `(p')^k`.

Partition the plane into N-by-N boxes as Pei does. A connection at
maximum-norm distance d>4N visits a simple nearest-neighbour coarse path
of k edges with `k>=d/N-1`. Every visited box forces the annulus about its
lower corner to be crossed: a visited point is at distance <N from that
corner, and at least one endpoint is at distance >2N. Among k+1 distinct
corners, one residue class modulo 5 contains at least `(k+1)/25`.
Its closed 2N-boxes are disjoint. Choose that class deterministically.
There are at most `4^k` candidate paths from the first box, whence

    P(x<->y) <= (p')^(1/25) sum_{k>=ceil(d/N-1)} alpha'^k
             <= [1/(4(1-alpha'))] alpha'^(d/N),
    alpha'=4(p')^(1/25),
    m'=log(1/alpha')/(sqrt(2)N).

Because `d>=|x-y|_2/sqrt(2)`, this is T2 with exactly its A' and m'.
If p=0, its printed quotient and logarithm are undefined. In that case
MK makes every forced annulus crossing impossible; connections with
`|x-y|_infinity>4N` have probability zero. Alternatively replace 0 by
any positive upper bound below `exp(-42h_0N^2)4^{-25}` before applying
T2. To obtain h_0>0 from a positive p, one needs `p<4^{-25}`; for example
`h_0=log(4^{-25}/p)/(84N^2)` works. The scale assertion is conditional
on this strictly positive slack.

**Corollary SS: finite-subgraph part HOLDS; the printed torus extension
is not proved.** `A''=max(A',exp(4sqrt(2)Nm'))` covers the short-distance
case by the trivial probability bound. A union bound over B then gives
its stated kernel. The sentence at line 183 that the proof “is local”
does not verify the same constants on every rectangular torus with sides
at least 10N. Pei's path count uses a planar N-grid and a modulo-5 coloring.
On a general cyclic grid, that coloring need not respect distances across
the seam; arbitrary side lengths also need a specified partition. Pei's
source proof 770–790 is on subgraphs of Z^2. His separate rectangular-torus
charged bound is truncated at half the shorter side (source 983–987,
1364–1368,1418); it does not supply this missing periodic connectivity bound.
This is an unproved extension, not a counterexample to it. Preserve its
ARGUED label and do not silently consume it as a proved theorem.

**PIN+: HOLDS GIVEN Pei `thm:main4(a)` at theta=0**, hence his stated
(I1)–(I3). Set `sgn(0)=0`; this is a bounded odd one-site function.
At zero field, clusters unattached to pins have fair signs; those attached
to positive-first-component pins have positive sign; zero-component pins
have no open incident first-sign edge. Thus
`E sgn(Phi_x^1)=P(x<->pins)`. A crossing hits the ring of radius
`floor(3N/2)`, containing `8floor(3N/2)<=12N` sites. Each lies at distance
at least `N/2-1` from the pinned layers. Union bounding the one-site theorem
proves line 151, with no Lipschitz requirement on the sign test. The
couplings for this bond argument are nonnegative even though the cited
odd-observable theorem allows signed couplings.

For mixed signs, compatible clusters cannot join opposite pins. Hence

    E sgn(Phi_x^1)=P(x<->P_+)-P(x<->P_-).

OpenAI's (3.61), `eq:pre:10-3`, applies to this Haar-centered one-site test
and bounds the absolute difference. An upper bound on an absolute
difference gives no upper bound on the sum. This diagnosis HOLDS.
It identifies the missing estimate in this direct application; it does
not prove that no other consequence of the paper can give PIN-U.

## 5. SS, EV and the precise conditional conclusion

**Proposition SS: HOLDS.** Fix X and order the finitely many clusters by
their least vertex. Their signs form a product law, with possibly unequal
biases. For its coordinate-reveal filtration, martingale increments
`D_iF,D_iG` have zero cross expectations when their indices differ.
Thus `Cov(F,G|X)=sum_i E[D_iF D_iG|X]`.
If cluster i misses B, independence makes `D_iG=0`. Otherwise
`|D_iG|<=osc(G)`. Averaging over unrevealed signs does not increase a
coordinate oscillation, so
`|D_iF|<=sup|F(s)-F(s with cluster i flipped)|`.
Changing the spins of that cluster one at a time bounds this supremum by
`pi sum_{w in C_i}Lip_w(F)`. This uses the diameter pi of the round S^3
metric and is valid for nonlocal F. Summing and then averaging over X
proves line 177 by the law of total covariance. No fairness, association,
or rotation symmetry is needed.

**EV: HOLDS as a precise covariance hypothesis**, provided its constants
are explicitly uniform in volume and H. It concerns conditional means
under a particular first-sign decomposition, not the common-left-neutral
observables of row 1091's FST-N. In particular
`(Phi_u^1)_X=r_u tanh h(C_u)` need not vanish. It is correct that these
conditional means do not change when the remaining random cluster signs
are flipped. This does not make their covariance small.

For the periodic conclusion, state the extra premise actually used:

    CB-T(A_c,m_c): on all sufficiently large rectangular tori and all
    |H|<=h_0, P_H(v<->w)<=A_c exp(-m_c d_{2,T}(v,w)),
    with A_c,m_c>0 independent of the torus and field.

**SS+EV: HOLDS AFTER this premise is made explicit and the singleton
constant is made uniform.** Given CB-T and EV, set

    r=min(a,m_c/sqrt(2)),  a'=r/2,
    X(B)=X_ev(B)+pi |B| A_c,
    X_1=3[X_ev({0})+pi A_c].

The sum of the two covariance pieces is bounded at rate r. This proves
(L) at rate a' and, with `G=e.Phi(u)` and `L°_G<=3`, (R) at rate 2a'.
Translation maps u to 0, preserves the homogeneous sheet and the
first-sign construction, and maps the full allowed field class into
itself. It therefore justifies the single constant `X_ev({0})` for every
u. If translation is not available in a more general formulation, require
`sup_u X_ev({u})<infinity` instead. The printed `3X({u})` is otherwise
not a single uniform X_1. For the proposed torus corollary, take
`A_c=A''`, `m_c=m'` only once that corollary has been supplied.

Theorem FST-F1 then gives (17) with a' and this X_1 on its positive
lambda interval. The conjunction of **the original annular PIN-U and EV**
is not yet a fully written torus reduction: line 183 is still owed.
The conjunction **CB-T and EV** is the exact sufficient split verified
here. With CB-T fixed, the triangle inequality also derives EV from an
all-observable local covariance bound and derives that bound from EV,
with changed constants and the minimum rate. Thus this is a splitting,
not a strictly weaker remaining analytic problem.

One further correction concerns line 60: delete “the two parts cannot be
dropped”. Uniform (L) alone gives (R) at half its rate by the same one-site
test and translation argument. Both are used at the displayed constants,
but they are not independent necessary inputs for existence of a positive
interval. Nothing here orders the resulting hypothesis strictly below
FST-F or revives the unquantified FST-N.

## 6. Pei's coarse orientations and CO

**The field transfer in lines 125–130 HOLDS**, conditional on Pei's
(I1)–(I3), with the claimed constants. Give each site term nonnegative
cell weights summing to one. A cell has at most `(2s+1)^2<=9s^2` sites
for integer s>=1. Hence `|A_c^H-A_c^0|<=9h_0s^2`, and integrating its
interior gives `|F_c^H-F_c^0|<=9h_0s^2`. Two evaluations of at most
K_coll cell free energies cost `18K_coll h_0s^2`.
The conditional density comparison over a collar has this same exponent.
Under `18K_coll h_0s^2<=epsilon_*/4`, Pei's deterministic event inclusion,
conditional reference bound, and iterated conditioning therefore remain
valid. These arguments do not use a spin-flip symmetry.

`lem:pm1(a)` instead becomes `A_c^H(-rho,-iota)=A_c^{-H}(rho,iota)`.
The fixed-field equality fails. The Haar change of variables and the
locality/norm assertions of `lem:odd(a),(b)` survive for arbitrary bounded
observables; its assertion (c) does not. `lem:coupling` is an abstract
comparison of positive clique-factor densities with a Haar minorization;
its proof needs equality of the two systems' factors on cliques meeting U,
not a global physical symmetry. This verifies precisely the distinction
made at lines 126–131. A single free spin with density `exp(h Phi^1)`
already has positive mean for h>0, by pairing positive and negative first
coordinates. It disproves the extension of `thm:main4(a)` to fields when
P is empty. Thus the failure also occurs for aligned fields.

**CO: HOLDS AFTER specifying the common ring-coordinate space; its
“neutral quasi-local” interpretation is unsupported.** Use the free ring
coordinates `tilde omega_Rf` as the common space for m^1,m^2, inserting
the two systems' fixed boundary pins separately. Fix the same graph,
couplings, tiling, and interpolation branch in both systems. The distance
condition puts every cell meeting A in the set where the fields agree.
It makes `O*` the same function, with norm at most `||O||` and at most
`16|A|` orientation sites. The two conditional orientation densities have
identical cell factors at all tested vertices. Their bad/good sets on U
also agree. Apply the abstract coupling at each fixed free ring value.
Its remainder is at most `2||O|| P_p(A*<->W)`.

Average under m^2. The transferred bad-site estimate bounds the weight of
a path of m tested sites by `16^{-m}`; there are at most `8^{m-1}` paths
from each initial site. As in Pei's geometry, m is at least
`d/(2s)-1-w`. Thus

    sum_paths average(path weight)
      <= |A*| 2^{-(d/(2s)-1-w)}/4
      <= 2^{3+w}|A| exp(-(log 2)d/(2s)).

Multiplication by `2||O||` gives exactly `2^{4+w}|A|||O||` in CO.
Adding and subtracting `integral Psi^1 dm^2` proves its displayed identity.
No symmetry cancellation is used. This verifies CO without assuming the
false field version of `lem:pm1` or `lem:odd(c)`.

Replace line 139's first two sentences by: “Psi is the conditional
orientation mean of the observable, as defined in CO. The displayed
identity leaves its integral against the difference of free-ring
marginals uncontrolled.” The identity `Phi(kg)=kPhi(g)` alone proves
neither a quantitative quasilocality bound nor a common-left-invariance
claim for this conditional mean in a field. Bad-site estimates were
averaged over the ring law; they are not uniform mixing estimates at
every fixed ring configuration. No such additional property is needed
for CO, and this check does not certify the ARGUED interpretation.

## 7. The seven stopped routes in 5.3

The source prints seven bullets, rather than six. All seven are covered
below. A failed proposed estimate is not an impossibility theorem.

| Route; first relevant line | Verdict and correction |
|---|---|
| Association for PIN-U; 203 | HOLDS as the conditional FK comparison and the identified missing proof. At fixed amplitudes, the mixed-sign bond law is the all-positive-pin law conditioned on no cluster joining opposite pins. The conditioning event is decreasing, while connection to pins is increasing. Its probability is a decreasing tilt of the all-positive-pin amplitude law. Association of that law would complete the comparison. It is not supplied: arbitrary complementary pin directions lie outside the stated Ginibre class. A1 is not itself a counterexample to association **under one-signed first-coordinate pins**, since its opposing first-coordinate fields do not meet that restriction. Keep the comparison OPEN and describe the failed application of the general inequality; do not present A1 as refuting this more restricted premise. |
| OpenAI (3.61) for PIN-U; 204 | HOLDS. Its direct sign observable gives a difference; no estimate of the sum is deduced. PIN+ is the valid one-signed special case. |
| Ding–Huang–Yang for PIN-U; 205 | HOLDS AFTER the boundary-law qualification below. Their xy local-time theorem is not an all-spin-pin theorem. Opposite monotonicities obstruct the indicated direct FKG argument; the source does not prove that every possible use of its results fails. |
| OpenAI Section 3.11 for EV; 206 | HOLDS as a failed general field extension. G1/G2 and A1 invalidate the amplitude-association inputs in their stated small-coupling examples. Conditional sign FKG and Newman's bound still hold with arbitrary real Ising fields: the field is linear in the signs and does not change log-supermodularity. No failure at homogeneous beta in [2.3,2.6] is inferred. |
| Pei orientations for EV; 207 | HOLDS. Corrected CO leaves a difference of free-ring marginal integrals. The orientation comparison estimates no such marginal covariance. |
| Differentiation in the field; 208 | HOLDS AFTER scoping the rate claim to this estimate. Differentiating the finite normalized integral gives exactly the displayed sum of third cumulants. Applying the two-group covariance bound to each isolation gives the largest-isolation-distance estimate. At a midpoint that distance is half the two-point separation, losing rate. Summation can add polynomial factors; allow an additional rate loss to absorb them. Do not claim a sharp derivative kernel at exactly a, or that a different third-cumulant estimate cannot close. This is a failure of the proposed fixed-rate differential inequality only. |
| Typical boundary data to all pins; 209 | HOLDS AFTER deleting the unverified numerical comparison and “only”. Theorem 3.1 can control `Var(E[F|ring])` under the free ring law: use `Cov(F,E[F|ring])` and bound the ring mean's individual derivatives through its boundary bonds. This is average control. A crude boundary-density bound grows exponentially in the boundary size. The note tracks neither the ring convention nor the constants c and Xi well enough to prove its asserted inequality is false throughout the window. Replace the last comparison by: “No constants in this argument are verified to make the boundary-density cost smaller than the mixing gain; it yields no all-pins bound.” The exact factor 16 and the one-dimensional aside are not used as a theorem. |

For the third route, the source is more precise than the shorthand in
line 205. Ding–Huang–Yang, `prelim_1029.tex:110–136`, specify x/y local
times summing to the prescribed total, zero z boundary local time, and
copywise boundary partitions with a parity constraint. Their spin-boundary
conversion at 211–229 includes the factor

    2^(-kappa_x-kappa_y)
      1_{no x-cluster joins opposite x pins}
      1_{no y-cluster joins opposite y pins}.

The cluster-count factors must be retained for general valid partitions.
For the **edge/local-time marginal**, relative to the law with all boundary
signs positive and all boundary vertices wired, they cancel except for a
constant; conditioning on the two no-opposite-connection events then is a
valid equivalent description. This does not identify every loop/excursion
law with arbitrary boundary partitions. In the source's x-preferred order
(`FKG.tex:284–292`), the first event is decreasing and the second increasing.
Also arbitrary S^3 pins need not lie in the xy boundary class at all.
Theorem 5.2 (`Fractality_1025.tex:17–22`) therefore supplies no literal PIN-U
input through the step written here. Remark 1.3 (`intro_new.tex:38–40`)
explicitly leaves the all-spin-boundary extension unestablished.
The full proofs of those cited theorems are not being reverified here.

## 8. Model 5.4 and remarks 6.1–6.2

**Model 5.4: HOLDS GIVEN the stated torus Ising long-range-order input,
with scope corrections.** Under S^3 Haar measure,
`t=(sigma^1)^2+(sigma^2)^2` is uniform on [0,1]. For example, split a
four-dimensional standard Gaussian into two two-dimensional blocks.
Their squared lengths have independent exponential densities; the
change of variables to their sum and ratio has Jacobian equal to the
sum and yields a constant ratio density. The sphere direction is Haar.
Thus `phi=sgn(t-1/2)` is a fair sign, and at b=0 its joint law is exactly
the nearest-neighbour Ising law at coupling J.

Conditional on all phi values the individual spins are independent,
and integration over either half-interval gives
`E[psi_x|phi]=phi_x/4`, for `psi=t-1/2`.
For **distinct** x,y the law of total covariance gives exactly
`Cov(psi_x,psi_y)=Cov(phi_x,phi_y)/16`. The restriction x!=y matters:
there is an additional conditional variance at x=y. The function psi is
Lipschitz (its spherical gradient has norm `2sqrt(t(1-t))<=1`) and
measurable with respect to X in the first-sign decomposition, so
`psi_X=psi`. The assumed positive long-distance Ising covariance on
zero-field tori directly contradicts EV with one-site F,G and a>0.
If Peierls is the only imported ordering theorem, choose J sufficiently
large; an assertion for every J above the exact critical coupling needs
that stronger Ising input. No critical value is calculated or imported
as a numerical certificate here.

Each coordinate sign is independently flippable at b=0 because the
J-interaction reads only coordinate squares. Its embedded bonds all have
p_e=0, also with pins or fields. The analogues of RN, MK, B and SS apply;
all nontrivial sign connections and all annulus crossings vanish.
Thus the analogue of PIN-U holds with p=0. Use T2's separately stated
zero-p case, not its undefined logarithm at zero.

Replace “has no pair coupling” (215) by **“has no bilinear dot-product
coupling; it has the pair interaction J phi_x phi_y.”** Replace “satisfies
every input” by “satisfies the sign-representation, locality and crossing
inputs, without the O(4) bilinear Hamiltonian”. It is not an instance of
the literal O(4) hypothesis PIN-U; it is a counterexample to the proposed
universal deduction from those sign-cluster properties alone. Nor does
it prove that an eventual proof *must* use rotation invariance specifically.
It proves that additional control of the remaining variables is needed.
This restriction is consistent with row 1094 and with the note's admission
that its example does not refute the O(4) sheet statement.

**Remark 6.1: HOLDS GIVEN Ding–Song–Sun's theorem, with “correlation”
read as covariance.** Their Corollary `C:corr` at `ising.tex:482–487`
states exactly

    Cov_g(tau_u,tau_v) <= E_0(tau_u tau_v)

for a finite ferromagnetic Ising graph and arbitrary external fields,
including limiting pins. It does not bound the untruncated product by
its zero-field value. Conditioned on all four amplitudes, the sign species
are independent Ising systems with the printed couplings and fields;
this statement of the source therefore matches the proposed conditional
covariance use. It controls no change in the amplitude law and no mixed-pin
connection sum. The cited theorem's proof was not independently checked,
and it is not used to discharge PIN-U or EV.

**Remark 6.2: HOLDS AFTER CORRECTION; “survives in full” and “not the
field” are false readings.** For the first sign chosen along e, nonnegative
aligned fields can be represented by a positive pinned ghost. The Ising
GKS inputs extend to its edge and singleton terms; the complementary
sector has no field. Mixed amplitude derivatives are nonnegative, since
all derivatives of the Ising edge couplings and ghost couplings have the
same sign. The Ising coefficients are nondecreasing in the amplitudes; the planar
coefficients are nonincreasing. Each partition function is differentiated
separately, so products of its first derivatives are nonnegative.
The conditional physical-bond law is a marginal of the ghost FK law.
Its association and monotonicity, and the pin-to-pole argument, therefore
survive for this direction. Alternatively its pin-event probability given
physical clusters is a product of
`f(h(C))=exp(h(C))/(2cosh h(C))` over clusters meeting the pin set.
For nonnegative h(C), f is increasing and
`f(a+b)>=f(a)f(b)`; merging clusters and increasing amplitudes cannot
lower that probability. This supplies the needed pinning monotonicity.
After the same conditional projection as above, it covers O(4).

RN and annulus separation then give **physical first-sign cluster decay**
for a sufficiently small aligned field. But free cluster signs are biased,
the crossing partition-function identity fails by the chain calculation
in section 3, and Pei's odd one-point conclusion fails even for one spin.
Two independent spins in the same positive field have a positive
untruncated product expectation and no connecting bond. Replace the last
two sentences of 6.2 by: “Aligned nonnegative fields retain the pinning
comparison used for the first-sign crossing bound. They still break the
fair-sign identity and the odd-observable cancellation. The face does not
restrict its conditional fields to this aligned class.” This case supplies
neither EV nor the face's arbitrary-direction estimate.

## 9. Verdicts, remaining obligations and source receipt

| Row-1096 statement | Verdict | First failure or qualification |
|---|---|---|
| FST-F implies FST-F1; FST-F1 implies (17), 45–58 | HOLDS | Positive constants, all observables, periodic distances and periodic local limits. The proof above checks the prefactor and interval. |
| Necessity of both FST-F1 clauses, 60 | HOLDS AFTER CORRECTION | The stated necessity fails: (L) yields (R) with half the rate and a uniform singleton constant. Keep sufficiency only. |
| RN, 68–72 | HOLDS | The annulus constant 42 uses N>=2. |
| MK for arbitrary auxiliary kernels, 74–80 | FAILS as written | First failing inference is 80: interior-spin independence does not imply independence of arbitrarily coupled auxiliaries. The common-bit counterexample applies. The independent-bond version HOLDS. |
| B, 103–109 | HOLDS AFTER CORRECTION | Its product of cosh factors is unpinned; pinned clusters have the forced weights specified above. |
| P1, 111–117 | HOLDS | For each beta>0, sufficiently small h>0, then sufficiently small b>0. The wider RESULT wording at 281 does not follow. |
| A1, 119 | HOLDS | Every fixed h>0 and sufficiently small b>0, in the stated S^2 model. |
| Pei step tables, 88–101,123–131 | HOLDS AFTER CORRECTION | Use actual Section-7 labels, the RN replacement proof, and the scope distinctions above. The source results themselves are not refuted. |
| CO, 133–139 | HOLDS AFTER CORRECTION | Identity and constant hold on common free-ring coordinates. Line 139 supplies no quantified neutral/quasilocal theorem. |
| PIN-U, 143 | HOLDS as a definition | It remains OPEN, with the explicit annulus and bond conventions above. |
| T2, 147–149 | HOLDS AFTER CORRECTION | Positive p' constants hold; p'=0 needs the separate case. |
| PIN+, 151–155 | HOLDS GIVEN the cited odd-observable theorem | The mixed-sign difference-versus-sum calculation is exact. |
| SS and finite-subgraph Corollary SS, 175–185 | HOLDS | The martingale, pi flip bound, union bound and A'' are correct. |
| Torus Corollary SS, 183 | FAILS as a completed deduction | First missing step is 183's appeal to locality. Preserve the source's ARGUED label: general cyclic partitions and the disjoint-box/path count are not written. The proposed conclusion is not refuted; no torus counterexample is claimed. |
| EV and SS+EV, 189–199 | HOLDS AFTER CORRECTION | Use an explicit periodic connectivity premise CB-T and a uniform singleton constant. EV is the remaining covariance part, not a weaker mixing theorem. |
| Seven routes, 203–209 | HOLDS AFTER CORRECTION | The stops survive; restrict the first and third boundary-law arguments and remove untracked fixed-rate/numerical assertions in the last two. |
| Model 5.4, 211–215 | HOLDS AFTER CORRECTION, GIVEN the stated Ising input | Distinct sites; sufficiently large J under a Peierls-only input; analogues of sign-cluster hypotheses, not the O(4) Hamiltonian; no claim that rotation invariance is logically necessary. |
| Remark 6.1, 227 | HOLDS GIVEN Ding–Song–Sun | Their exact bound is for the truncated covariance; the amplitude-law issue remains. |
| Remark 6.2, 229 | HOLDS AFTER CORRECTION | First-sign pinning and crossing estimates survive aligned fields. “In full” fails already at the fair-sign identity and odd one-point conclusion. |

The correction groups, ranked by what they affect, are: the unproved
periodic connectivity input; MK's auxiliary independence; the uniform
singleton constant and the unnecessary necessity claim about (R); the
unsupported interpretation of CO; the aligned-field symmetry claim;
P1's parameter overstatement; the three stopped-route scope/constant
repairs; the model's Hamiltonian and logical scope; and the endpoint,
pin-weight and source-label corrections. No correction establishes PIN-U,
EV, FST-F1 or (17) for the actual homogeneous O(4) sheet in the window.

There is no conflict with row 1094's central corrections. Row 1096 keeps
all sheet observables, uses no unquantified FST-N premise, and confines
(17) to periodic local limits. FST-P implies FST-F and FST-T implies
FST-F remain the conditional results of row 1094; this check does not
reopen them or infer an ordering between P and T. The rate discussion
in 5.3 must retain row 1094's metric and rate-loss qualifications.
The five-dimensional control retains twelve neighbours, `|H|<=4lambda`
and `lambda<=h_0/4`; it also needs the half-margin bound
`lambda<=1/(24X_1 e^a S_a)` if that interval is written explicitly.
The U(1) and high-temperature controls furnish no hypothesis in the
stated coupling window. The U(1) discussion remains conditional on the
cited power-law input: a sufficiently small annulus probability would
contradict that input through the same zero-field cluster argument.
The unverified guide-run numbers in P1 were not used or rerun.

Primary sources and actual read ranges:

- [Yan Ru Pei, arXiv:2611.01532v2](https://arxiv.org/abs/2611.01532v2),
  `aniso-heisenberg.tex`: 1–71 (numbering), 148–173,195–241,
  460–803,855–919,942–1420,1526–1541. The sources cited in his
  (I1)–(I3) remain named conditional inputs; this is not a check of the
  whole OpenAI stiffness iteration or the whole Ding–Huang–Yang proof.
- [OpenAI, O(4) Section 3 at the row's pin](https://raw.githubusercontent.com/openai/math/4eaee87548250b2682affda7d05d947c05554bae/preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/build/sections/preliminary.tex):
  1–66,833–1182. The copy at Pei's cited revision
  `adc7f1241b42e322a6451854ab7e4b4c146bf78a` is byte-identical to this
  section. SHA-256: `15daad116aadd0d8e951d80c65b52493a8fcbc6e1894e81c2d2157288a7a379b`.
- [Jian Ding, Fenglin Huang and Peng Yang, arXiv:2611.04908v1](https://arxiv.org/abs/2611.04908v1):
  `prelim_1029.tex:110–156,211–231`, `Fractality_1025.tex:1–105`,
  `FKG.tex:275–313`, and `intro_new.tex:38–40`. These verify the
  boundary-law and theorem-scope uses, not the full annulus theorem.
- [Jian Ding, Jian Song and Rongfeng Sun, arXiv:2107.09243v3](https://arxiv.org/abs/2107.09243v3):
  `ising.tex:450–499`, including Theorem 1.1 and Corollary 1.3.
  The covariance statement was checked against their text; its proof is
  a cited input only.
- [Ethan Sussman and Levent Alpoge, outline at 31a47c543775](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/YM4_sketch_500.tex):
  580–600; [complete account I at that revision](https://raw.githubusercontent.com/ethanwsussman/Yang--Mills-LLM-experiment/31a47c543775/theorem_0_complete_account_raw_I.tex):
  2700–2715. Their text is authored with Claude and Codex. No Balaban
  PDF or OCR was needed for this check.

The row-1096 SHA-256 is
`9cc524caf99a4c9c438df80677e46712fce3588cff6d32b61978958cec6aafc1`.
The full receipt is
`/tmp/sa-gap-sheet-field-check-astra.32wKuy/source-receipt.json`.
Downloads are confined to the new scratch directories named there.
No numerical computation, machine enumeration, Lean check, audit, status
update, external post, or row-1097 read was performed. The mathematical
checks above are written finite-measure identities, hand inequalities,
and conditional implications. No omitted proof is counted as supplied.
Only this output file changed. It is local, uncommitted and unpushed on
`check/gap-sheet-field-astra-20261117`. The lead's next obligations are to
apply these corrections and supply the periodic connectivity estimate
before treating original PIN-U plus EV as a completed torus reduction.

RESULT: FST-F implies FST-F1 and FST-F1 conditionally gives (17); RN, the independent-bond version of MK, P1/A1 in their stated ranges, finite-subgraph T2, PIN+ conditional on the cited odd-observable theorem, and SS hold after the explicit corrections above; SS+EV gives the face bound conditional on a uniform periodic connectivity estimate and uniform singleton constants, but original annular PIN-U plus EV is not yet a fully written torus reduction; the stopped routes and model retain only their corrected restricted scopes, FST-F1/PIN-U/EV and the actual sheet target remain OPEN, and no audit status or Yang–Mills mass gap is claimed.
