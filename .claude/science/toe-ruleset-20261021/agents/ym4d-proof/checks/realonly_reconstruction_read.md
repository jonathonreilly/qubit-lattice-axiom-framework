# REALONLY source inspection: H_reg, H_Euc, REC

Author-side bounded inspection, 2026-10-30. Source HEAD:
`71ff1c12a33734f8ae305540916c117f7fceb664`. This is a source/consumer map,
with elementary implications rebuilt below; it is not the fresh hostile
review of REALONLY, a new audit, or verification of actual Yang–Mills
estimates. Only this file is authored. No numerics, source changes, commits,
or subagents were used. Constructive RG method credit remains with
Tadeusz Balaban and Jonathan Dimock.

All source paths below are relative to the `ym4d-proof` working folder.
Line numbers identify the bytes in the closing hash table, rather than the
historical line numbers quoted inside older reviews.

## 1. Consumer decisions

| Consumer | What it actually consumes | Real-source decision |
|---|---|---|
| H_reg / OS0 / E0′ | A common hierarchy on collision-flat Schwartz tests; derivative order linear in insertion number and factorial constants, uniform in cutoff/volume | **REAL-SUFFICES, conditional implication.** All-order real separated derivatives or fully unconditional separated moments with explicit scale weights suffice. Raw-clover ordinary MGF bounds do not supply an applicable shortcut. Actual estimates **OPEN**. |
| H_Euc via TQ2 | Real pressures for translated whole products; NC, PC, COMMON, compatible common diagonal | **REAL-SUFFICES, conditional implication already written in TQ2.** No complex-source zero-free input appears. NC and product-source SP/VAC remain **OPEN**. |
| H_Euc via N5B | Positive-chain covariance decomposition, seam transparency, actual-law image and covariance estimates, bulk/profile/domain inputs | **REAL-SUFFICES for the stated conditional reduction.** All-product estimates and prism-regulator transfer remain **OPEN**. Preserve REVIEW_N5B's averaged-versus-every-terminal-datum correction. |
| REC(a)–(d) | E0, time/spatial covariance, ordered-half RP, S_0=1 | **REAL-SUFFICES.** The hierarchy, not a source generating function, is the input. |
| REC(e) / L-CONT / Wightman continuation | Same hierarchy's E0′–E3, reality, normalization, and explicit finite Cartesian tensor dictionary when used | **REAL-SUFFICES at the RG/source interface.** **Complex spacetime continuation remains part of the reconstruction.** This is not complex source analyticity or a complex partition-function ratio. |
| Existing SRCAN SA-TC / SA-S proof | Holomorphic cross-support covariance envelope plus real-tilt CD | Its existing proof still needs its complex hypothesis. Deleting (A) while retaining only (B) is not justified. Replacing it by a proved real derivative/moment contract is a new sufficient producer, not a consequence of the old statement. |

## 2. H_reg is a separated-distribution contract

`OSLEAF55.md:158–186` fixes the test domain and normalization;
`:214–222` fixes the axioms. In particular

    E_n = {F in S(R^(4n)): every derivative of F vanishes on every x_i=x_j},
    |F|_k = max_(|gamma|<=k) sup_x (1+|x|^2)^(k/2) |partial^gamma F(x)|,
    |S_n(F)| <= alpha (n!)^beta |F|_(s n),  n>=1,                 (E0′)

with one `(s,alpha,beta)` for the entire hierarchy. E2 uses finite sums of
`S_(n+m)(Theta F_n* tensor F_m)` with each factor in the strictly ordered
positive-time domain. An ordinary same-half `f tensor f` is generally
excluded (`OSLEAF55:171–174`). Complex coefficients in that sesquilinear
form do not constitute a complex source tilt.

Two sufficient real contracts are available.

**Pointwise unconditional contract.** `REC_LIB.md:960–1054`, equations
(16.1)–(16.4), has the complete corrected implication. At Z=1 assume
`|e_hat_a(x)|<=C_X a^-4`, and for all cutoffs, volumes, placements and
`n>=2`, whenever `delta=min_(i<j)|x_i-x_j|>=c_*a`,

    |E product_i e_hat_a(x_i)| <= A_0^n (n!)^b0 product_i wbar(delta_i),
    wbar(r) = min(r,1)^-4 [log(2+1/min(r,1))]^q.                (R-PT)

The constants are independent of n as well as cutoff, volume and
placement. This gives `|S_n^a(F)|<=C^n(n!)^b0 |F|_(10n+1)`, hence E0′ with
`s=11`, `beta=b0+1`. For crude power `q_X`, use `Q=ceil(q_X)` and safe
`s=max(11,Q+6)`, not automatically 11 (`REC_LIB:1050–1054`).

The key calculation does not use a source domain. For `0<delta<1`,
`wbar(delta_i)<=C_q delta^-5`, so the moment envelope is at most
`C^n(n!)^b0 delta^(-5n)`. Project a closest pair onto its coincidence
plane. That displacement has l1 norm at most `2 delta`. Flat Taylor
order `5n` cancels the singularity; a further `5n` Schwartz weight is
integrable in the n spatial variables. At `delta<c_*a`, flat Taylor order
`4n+1` times the crude envelope gives `O(a) C^n |F|_(9n+1)`; at an exact
coincidence the test is zero. Finally `C^n<=exp(C)n!`. These are the
load-bearing steps in `REC_LIB:980–1016`; they identify a sufficient
real-data input, not a bound for Wilson theory.

If R-PT is to be deduced through conditional cumulants, the needed
all-order condition is explicit in `REC_LIB:1018–1048`: for every
partition pi with r blocks, including singleton blocks, bound its outer
joint cumulant of conditional block cumulants by

    A^n r! product_(B in pi) (|B|!)^p product_i wbar(delta_i). (R-OUTER)

Then `sum_pi |pi|! <= 2^(n-1)n!` yields unconditional cumulant exponent
`p+1`, and a further moment partition sum yields `b0=p+2`. The missing
probabilistic hypothesis is R-OUTER itself; the combinatorial count does
not establish it. `CODEX_REVIEW_SRCCD.md:311–349` identifies all three
original gaps: missing conditional singleton means, missing all-order LF
path moments, and an uncapped weight that accidentally demanded coarse
decay. In particular its eleventh-moment example at `:325–339` satisfies
the low-order Peierls smallness condition yet has unbounded high moments.

**Separated smeared contract.** `OSLEAF55.md:919–940` gives the current
corrected SP_lambda statement. For real or complex `f_i` in side-2 cubes
inside the chart, pairwise separated by `lambda`, require

    |E product_i O_tilde_a(f_i)|
      <= A^n(n!)^b lambda^(-p n) product_i ||f_i||_(lambda,r),
    ||f||_(lambda,r)=max_(|gamma|<=r) lambda^|gamma| ||partial^gamma f||inf,
    c_SP a <= lambda <= 1,                                  (R-SP)

with the same constants for all n, cutoffs, volumes and placements, and
the same bound at lambda=1 for larger separations. This is an
**unconditional** bound. A sufficient real-derivative replacement is:
under the actual conditional law and coarse marginal, let

    K_V(t)=log E[exp(sum_i t_i O_tilde_a(f_i)) | V].

For every nonempty block B of the separated family, including singletons,
assume

    ess sup_V |partial_B K_V(0)|
      <= A^|B| (|B|!)^b lambda^(-p|B|)
                           product_(i in B) ||f_i||_(lambda,r). (R-JET)

At finite cutoff the compact Wilson integral is smoothly differentiable
for real t, its positive denominator never vanishes, and
`partial_B K_V(0)` is exactly the conditional joint cumulant. No Cauchy
formula or complex source is required for this identity. The same lambda
is used for each block; singleton separation is vacuous but its displayed
bound is an additional hypothesis. The conditional moment partition
formula and `product_B |B|!<=n!` give R-SP with exponent `b+1`, after
averaging. This is exactly the corrected argument in
`OSLEAF55:926–935`, independently checked in
`REVIEW_REC_CONSUMER_ALIGNMENT_ASTRA.md:51–65`. A uniform conditional
**product** bound gives R-SP directly with exponent b (`OSLEAF55:937–940`).

R-JET at zero is the consumer requirement. If a proposed real RG induction
uses a real source window, it must prove the needed derivatives on that
entire actual window, at every order used, with explicit order/radius/
scale dependence. Such a window estimate is stronger than R-JET and is
not established by writing the derivative identity. Repeated derivatives
in one source direction are not among these separated distinct-support
jets: they can see the divergent contacts.

The tensor-product/Whitney extension from R-SP is sufficient on interior
tests in `(B_(R/8))^n`; `CODEX_REVIEW_OSLEAF.md:147–169` repairs a boundary
support loss in the original global assertion. With integer majorants
for derivative orders, it supplies
`s=max(p+r+17,Q+6)`, `beta=b+19r/2+51` (b here is R-SP's exponent).
The underlying X1/EXT contract and proof are `OSLEAF55:436–495`.
The global hierarchy requires `R_j -> infinity`; fixed R gives only its
admissible chart domain. X1 is a sufficient uniform-placement condition,
not a proved necessary-and-sufficient characterization: the claimed
necessity is corrected by `CODEX_REVIEW_OSLEAF:23–31`. Fixed-separated
convergence without uniform scale estimates cannot replace this bridge
(`CODEX_REVIEW_SRCAN:199–223`).

## 3. Exactly what real MGFs give, and where they do not apply

Let X be a real random variable under a positive probability law. If
`E exp(rX)<=M` and `E exp(-rX)<=M`, with r>0, then

    E exp(r|X|) <= 2M,
    E |X|^n <= 2M n! r^-n.                                 (M1)

The proof is pointwise: `exp(r|x|)<=exp(rx)+exp(-rx)` and
`(r|x|)^n/n!<=exp(r|x|)`. Thus this implication is fully real. If the same
two-sided bound holds for `X_i/q_i`, with positive q_i and common r,M,
Holder with exponent n gives

    E product_i |X_i| <= 2M n! r^-n product_i q_i.           (M2)

Under conditional laws, the same calculation with M(V) and
`sup_(a,R) E_nu M(V)<infinity` suffices for this **absolute product**
bound after averaging. This does not assert that the relevant
conditional MGF envelope exists. Complex tests can be split into real
and imaginary parts, costing at most `2^n` in such a bound.

For raw centered clover smears this would bound their ordinary second
moments. `SRCCD55.md:215–282`, with corrected remainder at `:926–927`,
instead gives, in FLOW's convention `u_0=1/g_0^2`,

    Var(O_a(f)) >= c g_0^4 a^-4 (||f||_2^2-O_f(a)),

for fixed nonzero real f on the stated even hypercubic tori at sufficiently
large u_0. Along the stipulated logarithmic trajectory this diverges.
Centering or a deterministic linear subtraction does not alter variance.
Consequently a fixed uniform M1 window for this raw centered variable
is incompatible with that scoped lower bound. For a differently normalized
field, the non-vacuity obstruction additionally needs the unconditional
**unnormalized** separated upper bound; this qualification is explicit in
`CODEX_REVIEW_OSLEAF.md:61–71`. The coupling convention must remain matched:
`g_PROOF=sqrt(2N) g_FLOW` (`CODEX_REVIEW_OSLEAF:47–59`). No sphere variance
theorem or blanket theorem for every dimension-four composite is inferred.

Subtracting contact counterterms from log Z does not in general produce
the log MGF of another positive law. Holder/convexity therefore cannot
simply be applied to a counterterm-subtracted object. Its separated mixed
derivatives may still be the desired real cumulants because local
counterterms of range below the support separation have zero such
derivatives (`SRCCD55:448–453`). That cancellation must be stated with
the actual range; mere locality is insufficient.

Conversely E0′ allows any finite factorial power beta, and need not imply
an ordinary source MGF at all. Even for ordinary random variables,
`Y=X^4`, X standard Gaussian, has all moments and
`E Y^n=(4n)!/(2^(2n)(2n)!) <= 16^n(n!)^2`, while `E exp(tY)=infinity`
for every t>0. The factorial bound follows from two central-binomial
bounds; divergence follows from `tx^4-x^2/2 >= tx^4/2` at large x.
This also explains TQ2's product-source admissibility caution
(`TQ2.md:433–444`).

Real positivity proves `Z_V(t)>0` for finite real-source integrals; it
does not prove a complex zero-free polydisc. A fair sign has
`Z(z)=cosh z`, with nonreal zeros. Strong real exponential integrability
can imply a smaller complex neighborhood, but that is an additional
quantitative deduction, not positivity alone and not automatically a
radius uniform in the insertion number.

## 4. SRCAN's surviving obligations

The exact tilt changes only the fine Wilson coefficient and leaves every
soft kernel fixed (`SRCAN55.md:129–147`). Its real version has precisely
the same fixed-kernel requirement (`:883–887`;
`CODEX_REVIEW_SRCAN:225–249`). Retuning kernels changes the generating
function. SA-S's hypothesis (A) is a zero-free complex polydisc with a
cross-second-derivative envelope; (B) is uniform real-tilt cross covariance
decay (`SRCAN55:440–479`). SA-TC then supplies its particular all-order
bound (`:412–435`). Its source radius and envelope constants require
explicit permitted dependence on n; the printed cutoff/volume uniformity
alone did not give geometric growth (`CODEX_REVIEW_SRCAN:40–54`).

SA-MOM is a valid Holder inequality but still needs moments of its
complex envelope and the **expectation of a supremum over real tilts**
under the original coarse marginal (`SRCAN55:618–635`;
`CODEX_REVIEW_SRCAN:237–249`). A first-moment estimate at zero tilt, or
separately at each tilt, does not supply that supremum. Likewise the
singleton LOC-e is not implied by cross-cumulant bounds or scalar flow
derivatives (`SRCAN55:558–574,842–852`;
`CODEX_REVIEW_SRCAN:180–197`). R-JET/R-OUTER preserve these obligations in
real form rather than eliminating them.

For a concrete abstract check on retaining only real cross covariance,
take M>=2, lambda=(4/3)log M, sigma^2=M^2/lambda, k=lambda/M. On three
independent N(0,sigma^2) variables multiply the density by
`1+(1/2)product_i sin(kX_i)`. It is positive and normalized. Direct
Gaussian integration gives

    K(t)=sigma^2 |t|^2/2 + log(1+epsilon product_i sin(Mt_i)),
    epsilon=1/(2M^2).

For i!=j the mixed second derivative is at most
`epsilon M^2/(1-epsilon)+epsilon^2 M^2/(1-epsilon)^2 < 1` at every real
t, but `partial_1 partial_2 partial_3 K(0)=M/2`. Symmetric compact
truncations preserve, on any fixed real cube, a cross-second bound 2
and third derivative greater than M/4: all MGF derivatives through order
3 converge uniformly there by exponential Gaussian domination, and
the limiting denominator has a positive minimum. Thus even positive
bounded-variable laws can have uniform real cross-second bounds and
unbounded third mixed derivative. On a fixed separated triple the
second bound can be written with any fixed decay rate and an adjusted
constant. This tests the bare all-order inference from (B), not a Wilson
field, a full spatial clustering theorem, or the real derivative transfer
with its additional higher-derivative hypotheses.

## 5. Exact real H_Euc contracts

**Flat route: TQ2.** LOC requires bounded finite-range, translation-covariant
approximants at each fixed cutoff with the actual common subtraction
prescription (`TQ2.md:183–211`). For every real determining product F,

    A_(a,R,F)=a^4 sum_x tau_x Y_a(F),
    p_(a,R,F)(t)=V^-1 log omega(exp(t A)),
    p'(0)=omega(Y_a(F)),   p''(t)=V^-1 Var_t(A)>=0.           (P)

The source is for the **entire translated product**, not just a linear
point-energy source. At fixed cutoff the period-independent thermodynamic
pressure exists by the bounded finite-range argument (`:213–260`).
For the chosen cutoff sequence a_j and source sequence t_l decreasing
to zero, the theorem uses

    lim_l limsup_j [p^I_(a_j,F)(t_l)+p^I_(a_j,F)(-t_l)]/t_l = 0,  NC
    |p^I_(a_j,F)(t)-p^Q_(a_j,F)(t)| <= epsilon_(j,F)(t)->0,
                                      t in {+/-t_l},          PC

plus COMMON: LOC, common algebra/sequence, compatible trajectories and
subtractions, hierarchy extraction/extension, and any simultaneously
consumed RP/nontriviality estimates (`:284–315`). The secant inequality
`-p(-t)/t <= p'(0) <= p(t)/t` proves period independence and then rotation
invariance on one common volume-first diagonal; continuity extends it
to H_Euc (`:317–390`). It neither exchanges uncontrolled derivatives and
limits nor uses complex source analyticity.

The real SP/VAC producer compares unnormalized conditional functions
for **all coarse data**, including large fields (`:489–538`):

    sup_Vc |log Z^I_t-log Z^Q_t-c(t)| <= N_b eta_a,F(t),
    |c(t)-c(0)|/V <= v_a,F(t),
    |p^I(t)-p^Q(t)| <= v_a,F(t)
                         +ell_0^-4 [eta_a,F(t)+eta_a,F(0)]. (16)

The source-dependent scalar difference survives normalization and cannot
be discarded. The right side tends to zero for each required real source.
For moving radii `t_(j,F)->0`, both the NC width and comparison error must
be `o(t_(j,F))`, using the **same actual radius** for F and transported
F_Q and pressure-approximation errors `<=t_(j,F)/j`
(`:446–466`; `REVIEW_TQ2.md:212–235`). Shrinking radii do not beat a
thermodynamic slope jump bounded below along cutoffs; a cusp appearing
only after a cutoff limit is a different quantifier.

SUS, `sup_(a,R,|u|<=t0) Var_u(A)/V <= K_F`, is a sufficient stronger
real input: double integration gives `p(t)+p(-t)<=K_F t^2`
(`TQ2:406–428`). Its covariance sum includes overlapping translates and
long distances. Separated regularity bounds do not supply it. NC itself
is an infrared thermodynamic response condition, not a physical mass-gap
claim. Clipped product sources additionally need TAIL on the same
diagonal (`:468–485`). The review confirms the conditional pressure
theorem and leaves all these actual YM producers OPEN
(`REVIEW_TQ2:18–34,142–221`).

**Sphere route: N5B.** The actual target and Ward split are
`N5B.md:50–84`: normalized covariance of every admissible cap product F
with the specified **net seam flux**, uniformly along a fixed compact
Killing path, must vanish at fixed R. At cut k=n-J the exact positive-chain
identity is

    Cov(F,S)=sum_(i<k) E Cov(F_i,S_i|U_(i+1)) + Cov(F_k,S_k). (4)

Assume at every fixed J, uniformly in that path and for all sufficiently
small a,

    Z_a^-q ||F_k-EF||_2 <= C_(R,F,v)(J),                    E
    tau_R(a,J)=inf_c sup_(U_k)|S_k-c| ->0 as a->0,          T
    Z_a^-q sum_(i<k) E|Cov(F_i,S_i|U_(i+1))|
                         <=delta_(R,F,v)(J)->0 as J->inf. D

Then the target is bounded by `delta(J)+C(J)tau_R(a,J)`; first fix J,
then take a small (`:153–207`). A sufficient fine tail is equation (7),
whose summed series is (8), at `:215–237`. ST is exactly T for arbitrary
boundary/chart/crossing data at every fixed resolution (`:475–506`).
CD-K, IMG-K, W0/W1/W3, profile matching, domain/extension and
radius-uniform regularity are still separate inputs (`:135–149,498–506`).
The covariance identities and positive-kernel contractions do not need
complex sources (`:169–174`). The linear-insertion SRCCD clause stops at
two further e insertions (`SRCCD55:358–359`); all-product N5B requires the
corresponding higher orders, images, and contacts rather than inheriting
them from the pair theorem.

The binding correction is `REVIEW_N5B.md:28–75`: E is an actual-marginal
L2 norm and D is an actual-law expectation. The result proves a route
with **no coarse-law decorrelation estimate**, not automatically a fully
conditional UV-only theorem. To assert the latter, add explicitly

    inf_b sup_(U_k)|F_k-b| <= C(J) Z_a^q,
    sup_V E[sum_(i<k)|Cov(F_i,S_i|U_(i+1))| | V]
                                      <=Z_a^q delta(J),

with all cutoff/path uniformities, and analogous conditional bulk inputs.
Typical-field alternatives need insertion-weighted tails, not just a
small bad-event probability (`N5B:284–315`). F13's actual prism source,
linear, large-field and normalization estimates remain OPEN (`:382–395`).
These qualifications do not make complex sources necessary.

## 6. Reconstruction uses complex spacetime, not complex sources

`OSLEAF55.md:224–255` is the current REC consumer. E0, time/spatial
covariance and E2 give the Hilbert space and contraction semigroup.
Full REC(e) uses the SAME hierarchy's E0′–E3, reality and S_0=1.
`REC_LIB.md:298–326` explicitly limits single-cut semigroup analyticity:
`<v,exp(-zH)w>` is holomorphic for Re z>0; unbounded insertion products
do not automatically follow from this. E0′ is used for full continuation,
not merely its boundary estimate.

The exact L-CONT input/output is `REC_LIB:328–364` and
`REC_CONT.md:17–70`. Output functions are holomorphic for
`Im(z_(j+1)-z_j) in V_+` and satisfy

    |W_n(x+iy)|<=C_n(1+|x|+|y|)^B_n(1+d_n(y)^-1)^A_n,       (6.1)

matching the Schwinger distributions on the Wick slice. These z are
spacetime coordinates. There is no source eta, complex partition
function or zero-free source normalization in the reconstruction
antecedent. Finite real Cartesian tensors require the printed sum norm,
all mixed words, reflection matrix J and Wick matrix C; unspecified
representations/spinors are not covered (`REC_CONT:43–64`).

`REC_CONT:982–1018` states the completed continuation interface;
`checks/reccont2_review.md:25–60` records the independently checked seed
and exhaustion. The later consumer correction is independently checked
in `REVIEW_REC_CONSUMER_ALIGNMENT_ASTRA.md:33–47`. Some REC_LIB historical
paragraphs still describe the former open producer or former unrepaired
consumers (`:366–384,1273–1297`); use the updated exact contract and
current OSLEAF source rather than reviving that stale status. This
inspection did not re-prove every REC_CONT lemma. It checked its exact
antecedents, completed conclusion and applicable review corrections.

The source-independent implication is therefore: any valid real producer
of E0′ and the same hierarchy's remaining axioms can feed REC, which
then constructs the complex **spacetime** continuation. No claim about
unique vacuum, nonzero excited sector, full YM observable identification
or physical mass threshold follows from this replacement.

## 7. Source identities and read coverage

The following are SHA-256 of the complete observed files. A hash is an
identity receipt, not a statement that every line was substantively read.
Initial oversized inventory/combined outputs were truncated; decisive
argument ranges were recovered in bounded reads. The coverage below is
deliberately narrower than a full re-review of all named libraries.

| Source | Substantive inspected coverage | SHA-256 |
|---|---|---|
| root AGENTS.md | full | `febf3a1aaabd4bd13f87b052ab5eacb75f46be535985425bae4d400f509bc7d0` |
| root docs/ai_methodology/SCIENCE_WORKFLOW.md | full | `71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3` |
| PROCESS_LIGHT.md | full | `b61be8245d68af0952d123ed3c1ce602ba948cbe3c5d22c951848f1805e619ab` |
| briefs_q/REALONLY/AUTHOR.md | full | `b19b45d85f31015e0ee1dd9747af9035bccc706bb3647a99c13ecd42089930d2` |
| SRCAN55.md | 129–155,389–647,738–782,832–899 | `7d6770a75318f6f9368428d1a01e36c2de5f56ea008071b531d71318ad78faa4` |
| CODEX_REVIEW_SRCAN.md | full, with bounded recovery reads | `a3ec6ab90f36bbd567d9b4a739deb7e2f223b55c0fe5905ae8a1fe2a19a2ab52` |
| SRCCD55.md | 162–404,436–580,922–952,991–1017 | `80a347f5d2bc801fc0395b6d61aa5c0661dd098ae4430bcf760b874729761d03` |
| CODEX_REVIEW_SRCCD.md | 210–351; closing banking list | `2c74ba185d4fefe657fc2bdb35a042361aff9dd8d9676af0c18f2990ec3a222f` |
| OSLEAF55.md | 134–255,426–521,904–990; headings and selected surrounding context | `c261a0c5eb300052445a05b3041b5ddf6e518445d3eacac36fc4421e60f66b78` |
| CODEX_REVIEW_OSLEAF.md | 1–169, with boundary correction recovered; later context partial | `cc19dc83485bfbac0d3b7f8186fea27918b522783af4ffe7e1f8bb257d4625e3` |
| REC_LIB.md | 93–146,298–385,960–1054,1080–1121,1271–1316 | `47dd75c7ca3c4f9f1af43139292d1fcfa6774b10f8e6ea2babc05ad67a48e29a` |
| REC_CONT.md | 1–71,982–1019; heading/contract search | `ac7ac0854fb320f183779f67be136063dfb750ee3f13b869acad10a7ac12a278` |
| checks/reccont2_review.md | full, with seed calculation recovered | `d5489fd797470a76479a4467beb844215489bc55a16dd34bf7a1d07d841e7b5c` |
| REVIEW_REC_CONSUMER_ALIGNMENT_ASTRA.md | full | `c95f494986341ffb802621d0639827b10673b382650ee45e3e51697b26a1afbf` |
| TQ2.md | 1–540; remaining headings/context search | `3d9342a392f01d3e705e5fe381ca88aed20e4dd06c8138751be23e768e96e38a` |
| REVIEW_TQ2.md | 1–240 | `ee21ea013cd4b467091405da44103ddfe3417a79f601fe93e4fbed88b3a95922` |
| N5B.md | full | `317a1ba0a08ccd188e4c9c15bb7eeb8894e646a6521b3b4e8de6961e8d9693da` |
| REVIEW_N5B.md | 1–220 | `ae7eb7264f61d316d0dab20d1b01819b77e2502984901d3f563ce9711c6eb407` |

Checkpoint: the source interfaces above permit real-only replacements
conditionally; all actual YM producer estimates remain OPEN. No consumer
result in this file closes the mixed-reader RG induction, source-radius,
finite-coupling remainder, original-law tail, witness matching, or coupling
flow tasks assigned elsewhere. Next decision: match the main REALONLY
real derivative contract against R-JET/R-OUTER or R-PT, and preserve the
TQ2/N5B quantifier boundaries in its consumer table.
