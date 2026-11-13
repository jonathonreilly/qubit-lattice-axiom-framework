## Repo search

The requested prior file `library/prior/gap-chain-ce-check-astra.md` is
absent. The earlier `prior/repo-search-2026-11-08.md` concerns different
targets; it supplies no check of this bridge. No matching owner was found
by `gap-chain-ce|gap-os-equiv|ONE-K|UNIV-K|SEED-FP` in `open-registry.md`.
FINISH 916 is the author row; 917 explicitly owns this check.

Searched `/Users/jonreilly/Projects/Physics`, outside this lane, on
`origin/main` (`4d88da5504d356762deb6b1a1c2695336af9fb81`), `pr/10114`
(`f76f6c649cff7dffbab664d8976e680e8f287fe9`), `pr/10133`
(`89faef229ff6e6bde42baad15ed8270c2f4087d8`), `pr/10134`
(`1e70c7211a2cdbc39001e619f1dd89db45e25851`), and `pr/10141`
(`c73ad7b177d94f89ff37b77386936e3d52b48b05`). Commands used bounded
`git grep -n -i -E` over Markdown and TeX, piped to `head`.

- Initial broad terms included `SEED-FP`, `ONE-K`, `finite.energy.*local`,
  `periodic lifts`, and `volume.first.*gap`. This hit its cap and unrelated
  one-Kraus statements; it supplies no absence claim.
- The narrower `gap-chain-ce|\(ONE-K\)|\(UNIV-K\)|periodic lifts|finite-horizon
  universality|positive.time convergence` search, excluding this lane and
  `ROWS.md`, returned no hits on all five refs.
- `Lemma FE` and `Proposition P` found
  `origin/main:research/mass-gap/library/gap-seed-limit.md:124-126,200-202`:
  the local marginal is bounded by `exp(12 beta |Gamma|)` times Haar;
  a uniform physical gap passes to a continuum datum given (H2), (TOT),
  (P1)-(P3), and (P4) for the Hamiltonian. These are the existing inputs,
  not a proof that the account supplies their hypotheses.
- `research/mass-gap/library/gap-seed-limit-check.md:139-190` already
  extends the argument to every integer spatial side. Its symmetric
  tori are admissible; the limiting transfer rate remains unchanged.
- `research/mass-gap/library/gap-limit-astra.md:365-403` already proves
  that positive-time (H2) suffices and lists the remaining continuum
  identification and totality requirements. The target's lines 65-67
  repeat this existing argument. Credit that earlier Codex check.
- `research/mass-gap/library/gap-crux-fp-check.md:141-153` names precisely
  the missing datum inputs, (H2), (TOT), (P1)-(P4). Its claim is a
  conditional reduction, not their verification on the account's objects.

These hits supply prior inputs. None found in the completed narrow search
duplicates the requested account comparison. No earlier seed theorem or
abstract OS theorem is re-proved here.

The checkout search also found `library/lg1.md:425-431`: its Theorem 13
already states exact barycentre covariance and fixed-cutoff DLR limits.
These are prior ingredients, not a check of Theorem E. The other direct
ONE-K hit is `library/gap-target-max.md:198`, the row 913 proposal that
row 916 is refining. Geometry hits in `c0-loc.md` and `fan-ext.md` concern
periodic fields, not convergence of probability laws.

Provenance: Codex, gpt-6-astra, xhigh (task configuration), checking
`c81a8aa5cfb8afc7b8eb49b14b75ee2da5e20749`. Research text; not an audit;
this check grants no scientific status. Credit: Ethan Sussman and Levent
Alpoge, with Claude and Codex as authors of their account text.

## Checkpoint

Task: FINISH row 917, cross-provider check of row 916. Read the target
line by line and compare Lemma C, Lemma FE, Theorem E, every Proposition
P' hypothesis, (ONE-K), and the specified account passages. Use written
mathematics only. Save each completed comparison here before proceeding.

Complete: repository search, source/index mapping, Lemma C, the datum
comparison, ONE-K, and its account comparison. Only this report was
written. The author note, FINISH, registry and scientific status files
were not changed.

## 1. Lemma C and Lemma FE — HOLDS

Target lines 127-170. Account means `sa1400/YM4_1400.tex` below.
The account's definitions at 1690 and 99109-99122 use weak limits of
periodic lifts of the bare Wilson law at fixed spacing and coupling.
Lines 99172-99174 retain the same cofinal torus family. This is exactly
the object required, not merely a limit law of a blocked field.

| Statement | Verdict | Check |
|---|---|---|
| C(i) | HOLDS | Weak probability topology on the compact metrizable configuration space is metrizable. A limit point as the period tends to infinity therefore has a convergent sequence of periods tending to infinity. |
| C(ii) | HOLDS | The finite-window quotient is injective eventually. Weak convergence gives continuous local tests. Lemma FE and Haar approximation give all bounded Borel local tests, as below. |
| C(iii) | HOLDS | Row 703 B4 allows all integer sides. Its `a_N <= N/2` gives `N-a_N >= N/2 -> infinity` on symmetric tori. |
| C(iv) | HOLDS, given the cited seed-to-lattice results | With `n=ell/(2a_K)` and `q=5041 s_*<1`, the lattice rate is at least `log(1/q)/n = M_* a_K`, where `M_*=2 log(1/q)/ell`. Row 703 B4 gives the infinite-volume transfer bound and unique vacuum in each coordinate direction. |
| Lemma FE, as used | HOLDS | A bond belongs to six plaquettes; each action term is in `[0,2 beta]`. Conditioning on the other bonds bounds the density by `exp(12 beta card(Gamma))`. No cutoff-uniform value of this constant is claimed or needed. |

For C(ii), write `E=exp(12 beta |Gamma|)` and `h` for product Haar.
The continuous-test inequality `nu(phi)<=E h(phi)` for nonnegative `phi`
implies `nu_Gamma<=E h` as measures. If `h(|F-F'|)<epsilon` with `F'`
continuous, then

\[
 \limsup_i|\widetilde\mu_{N_i}(F)-\nu(F)|\le 2E\epsilon.
\]

Let epsilon tend to zero. Only sufficiently large tori are needed, so
possible finite early failures of the window embedding do not enter.
The account itself gives a stronger alternate argument at 99176-99193:
the marginal densities converge uniformly, using a compact family of
continuous conditional densities. Neither argument requires its RG
hypotheses. C(iv) separately retains the seed and lane theorem premises.

Index used first: `sa-index/chunk-06.md` rows for SA 6879,
`chunk-22.md` rows for SA 24411-24467 and their neighbours. The cited
outline definition and compactness passage were read directly. The
existing `gap-seed-limit.md:118-126` and row 703 B1-B4 supply the lane
definition, FE, and integer-side extension. This checks the composition;
it does not confer a new status on those inputs.

## 2. Theorem E: the datum comparison

Target lines 174-251. This is an implication under the account's hypotheses,
not their verification. Account 1748-1754 assumes the background,
interaction, history, flow and ordinary-source estimates, on their stated
domains and with their normalization. The uniformity needed here is at
1724 and 1785, including `0<g<=gamma_J`. No short-distance, Ward, or O(4) conclusion is used to
pass the transfer bound.

Use the account's **free formal** tuple space before the null quotient
(115125-115141). This is one of its expressly allowed conventions.
It makes the target's tuple-dependent early-cutoff choices and linear
extension legitimate. If multilinearity relations are imposed first,
the early assignment `iota_j X=1` need not respect them; use the free
space instead. For each fixed finite collection of tuples, all its
representatives are the actual centered products for sufficiently large j.
The empty tuple always maps to 1.

| Statement | Verdict | Check |
|---|---|---|
| E1, positive-time member observables | HOLDS | Account 1726 places every contributing bond on the positive side once `C a_j<delta_X`; 99284-99295 gives bounded continuous finite-bond observables. Compact support is essential here. |
| E2(a)-(b), exact covariance after centering | HOLDS AFTER CORRECTION of domain notation | The product evaluation is defined on all compact tuples; its positive-time restriction is the member representative. With that convention reflection and lattice translation commute exactly with centered evaluation. See below. |
| E2(c), reflected pairing | HOLDS | It is the expectation of the product of the reflected centered factors and translated centered factors, in the same state `nu_j`. |
| E2(d), moment/cumulant identity | HOLDS | The moment partition sum has no singleton blocks; centering changes no cumulant of order at least two. The empty moment is 1 and the singleton moment is 0. |
| E3(i), fixed separated tests | HOLDS, given the account | The defining cumulants converge at 1690. The finite partition sum converges to exactly the centered functional at 1709. |
| E3(ii), moving tests | HOLDS, given the uniform bounds | The finite moment bound and telescoping estimate below control moving tests in fixed separated neighborhoods. Account 99518-99541 and 99568-99594 give this same method. |

**The domain correction.** At target 194, `theta X-bar` is not in the
positive-time class C, so `iota_j(theta X-bar)` is not defined by 185-187.
Define, for any compact tuple Z,

\[
 J_j(Z)=\prod_{f\in Z}\bigl(\mathcal O_j(f)-\nu_j(\mathcal O_j(f))\bigr).
\]

Replace E2(a) by `conj(Theta iota_j X)=J_j(theta X-bar)` for sufficiently
large j. In E2(b) the translated tuple stays positive, so the original
formula applies. Account 1726 gives the exact observable covariance;
99150-99156 gives invariance of `nu_j`; the plaquette action is real.
Thus centering and complex conjugation commute with those actions. This
supplies the intended identity without assigning a negative-time tuple
to the member space V_j.

**The finite moment bound.** For real tests put

\[
 B_0=1,\quad B_1=0,\qquad
 B_n(d,R)=\sum_{\pi\in\operatorname{Part}_{\ge2}([n])}
                 \prod_{J\in\pi} C^\infty_{|J|}(d;R).
\]

Then `|M_j(f_1,...,f_n)| <= B_n(d,R) prod_i ||f_i||_sharp`.
For complex tests, replacing B_n by `2^n B_n` is sufficient by expansion
into real and imaginary parts. All constants are finite, independent of
j, and nonincreasing in d. Consequently

\[
 |M_j(\mathbf f)-M_j(\mathbf h)|
 \le \widehat B_n(d,R)\sum_i\|f_i-h_i\|_\sharp
       \prod_{r\ne i}\max(\|f_r\|_\sharp,\|h_r\|_\sharp).
\]

Here the union of the two supports for each entry lies in its fixed
neighborhood, and different neighborhoods are separated. This proves
E3(ii) from E3(i). It also explains the small correction to target 231:
the moment functional sigma has these **partition-sum constants**;
the cumulant constants in (c)(2) cannot simply be used unchanged.

### Every input of Proposition P'

Proposition P' is at `gap-seed-limit.md:200-202`. The abstract inputs are
`gap-os-equiv.md:38-52,218-227`. There are seven named conditions in the
target's list, despite its heading saying six.

| Condition | Verdict | Verification |
|---|---|---|
| (H2) | HOLDS | For `t>=0`, choose `t_j=2a_j floor(t/(2a_j))`. E2 and E3 apply to the reflected pair and both separate moment factors. At `t=0` the support gap is still `2 delta_X>0`; no contact limit occurs. Thus the truncated diagonal pairing converges, including zero time. |
| (P1) | HOLDS | For any finite sum F, choose j large enough for all its tuple representatives. Each reflected Gram matrix is positive; its entries converge, hence `b(F,F)>=0`. Includes constants and mixed degrees. |
| (P2) | HOLDS | Real translation invariance follows by rounding a translation to the lattice and using E3(ii). With `theta tau_t=tau_(-t) theta`, translate the whole reflected tuple to obtain `b(F,tau_t G)=b(tau_t F,G)`. |
| (P3) | HOLDS with `k_F=0`, `C_F=b(F,F)` | For `s_j` in `a_j Z_+` tending to `2t`, member contraction gives `abs(b_j(F_j,tau_(s_j)F_j))<=b_j(F_j,F_j)`. Both sides converge. With (P2) and (P1), this is `0<=b(tau_t F,tau_t F)<=b(F,F)`. |
| (P4) | HOLDS AFTER CORRECTION of the bound cited in its proof | Use the partition-sum constants above, rather than asserting (c)(2) directly for moments. For each fixed reflected pair, small translations remain in fixed separated neighborhoods and converge in C1 by 99578-99586. Finite sums give the required continuity at zero. |
| (TOT) | HOLDS | The class consists of all positive-time separated tuples and 1. Its span is the free V_+; its images are dense in the completion of V_+/N by definition. Account 1768 and 115178-115205 identify precisely this H(S). This is totality in the scalar curvature-density sector only. |
| (H1) | HOLDS, given the seed and lane inputs | Take `S_j=Omega_j^perp` and `m_j=M_*`. C(iv) supplies the bound in physical time `t in a_j Z_+`. This subspace is invariant, and every vacuum-subtracted vector `Q_j[iota_j X]` belongs to it. |

For (H2), the exact expression is

\[
 u_j=M_j(\theta\overline X\cdot\tau_{t_j}X)
        -M_j(\theta\overline X)M_j(X).
\]

The supports within each tuple remain separated. Negative and positive
groups are separated even when t=0. Uniform continuity of the first
derivatives suffices for the translation modulus; no C2 regularity or
cutoff-uniform sup norm of the lattice product is needed.

**Theorem E — HOLDS AFTER CORRECTION** of E2's domain notation and the
moment-bound sentence. Its conclusion and constant are unchanged:

\[
 \ker H=\mathbb C\Omega,\qquad
 \operatorname{spec}(H|_{\Omega^\perp})\subset[M_*,\infty),\qquad
 M_*={2\over\ell}\log {1\over5041s_*}.
\]

This follows by P' with the seven conditions above. The account's
existence theorem is not needed for the conditional assertion about any
given volume-first limit. Existence of such limits remains among the
account's conditional conclusions. Neither this argument nor the seed
alone proves nontriviality of the excited sector.

**Canonical-component corollary — HOLDS, given account 1895 with its
own hypotheses.** That theorem assumes the inputs at 1884-1892,
including D1 and F2-F3 on the stated full test class, and
`g<=min(gamma_W(vartheta),gamma_W(vartheta_0))` at 1893. These are
additional premises of this corollary; 1748-1751 alone is not its full
assumption list. The unitary `ker H -> L2(X,lambda)` then makes the
latter one-dimensional. If the support had two points, disjoint
neighborhoods of those points would both have positive measure. Their
indicators would be two nonzero orthogonal vectors. Thus the support
is one point and sigma_S is that component. No uniqueness across
different volume-first limits follows.

Index/source route: `chunk-06.md` rows SA 6897, 6928-6935, 7025;
`chunk-22.md` moving-tests and centered-functional rows; `chunk-23.md`
HB1-HB2 and compact reconstruction rows; corresponding entries and
neighbours in `obligations.md`. Bounded outline reads confirmed the
definitions and moving-test method. The actual comparison used account
1640-1785, 1884-1895, 99284-99295, 99518-99594 and 115120-115207.

## 3. ONE-K and its quantifiers

**The telescoping implication — HOLDS.** Target 290-302. Write
`r=L^4`, `v=ell^4`, and

\[
 F_d(T)-F_{\pi d}(T)=c_d\operatorname{vol}(T)+r_d(T),
 \qquad |r_d(T)|\le\epsilon_K.
\]

Since the large volume is rv,

\[
 \Phi(d)-\Phi(\pi d)=r\,r_d(T_\ell)-r_d(T_{L\ell}),
 \qquad |\Phi(d)-\Phi(\pi d)|\le(r+1)\epsilon_K.
\]

The finite telescope gives exactly the target's bound. Its base margin
must dominate the **whole** tail `(r+1)E(K_0)`, not just be positive.
The predecessor map must exist on every datum to which the conclusion
is applied. This includes existence of each intermediate first-passage
datum; nonempty windows for infinitely many K alone would not supply it.

For complete precision at the base: the seed is assumed for all terminal
data reached from higher cutoffs. The conclusion then covers every
`K>K_0` and those terminal data at `K_0`. To assert it for **every**
datum with `K>=K_0`, also assume it for every base datum, or explicitly
include zero-fold iterates in the base set. This has no effect on the
limsup seed condition. The exact correction to target 298-300 is:

> Assume the displayed base bound for every datum of cutoff K_0. Then
> Phi(d)<=phi_* for every first-passage datum with K>=K_0.

**The full Lemma ONE-K wording — HOLDS AFTER CORRECTION** of this base-set
quantifier. Its algebra and `(L^4+1)` constant need no change.
The further conversion to SEED-FP remains conditional on Lemma FL, as
the target says. This check does not supply a new check of FL.

**“One cutoff” versus “one datum” — HOLDS AFTER CORRECTION.** The target
correctly rejects the unrestricted one-datum conclusion in row 913.
What is needed is a seed on the image of the predecessor chains at K_0.
This may be a proper subset of W_(K_0), and could in principle be a
singleton. A seed on the whole window is sufficient, not logically
necessary. For one chosen continuum sequence, only chains covering its
data are required.

**“pi must match final couplings; unmatched chains fail” — FAILS as a
deduction from the cited statements.** Target 309-318, 369 and the
stronger wording in its final summary. No endpoint equality enters the
telescoping proof. The account's 1833-1836 gives continuity and common
limits at a common *frozen-run* coupling `x_K^natural`. It supplies no
injectivity or nonzero difference of Phi at different couplings. The
claimed lower bound at 315 therefore does not follow. The scaling
discussion is labelled GUIDE, and must remain an expectation, not a
necessary condition or a Wilson counterexample.

As a logical check, take abstract masses
`F_d(T)=b_d vol(T)+A(T)`, with arbitrary endpoint labels and arbitrary
predecessors. Then UNIV-K holds with epsilon_K=0 and
`c_d=b_d-b_(pi d)`, regardless of the labels. This is a counterexample
to a claimed algebraic necessity, not a model of Wilson Yang-Mills.

Corrected statement: matching the endpoint is a hypothesis of the
**particular finite-horizon account theorem one proposes to use**.
Using it on consecutive physical cutoffs also needs a common frozen
presentation, horizon, domain, measure, and an admitted initial profile.
Matching the self-run `x_K` by itself neither establishes those facts
nor identifies it with `x_K^natural` of clause (d).

**W_0(g) is a singleton — HOLDS.** Account 1663, 1666-1667 gives
`x_0=beta`, `K=0 iff beta<=g^-2+B_sharp` on the permitted half-line,
so `W_0(g)={g^-2+B_sharp}`.
**“K_0=0 is not usable” — HOLDS AFTER CORRECTION** to a limitation of
the proposed exact-endpoint route. Such a route cannot send a datum
with a different endpoint to this singleton while preserving its endpoint.
That is not a proof that the abstract UNIV-K or ONE-K implication cannot
hold with K_0=0. Neither its existence nor its quantitative error is proved.

**The strict decimal upper bounds — FAILS as written.** Target 321 and
347 replace `(1/2)log(13/10)` by the smaller number 0.131. The correct
bounds retain the logarithm:

\[
 {\phi_*\over L^4+1}
 < {L\log(13/10)\over2(L^4+1)},\qquad
 (L^4+1)E(K_0)<{L\over2}\log(13/10)
\]

when the relevant nonnegative base seed leaves that margin. The latter
is not a substitute for the actual base-margin inequality.
For a hand check of the rounding error, the positive series
`log((1+x)/(1-x))=2(x+x^3/3+...)` at `x=3/23` gives

\[
 {1\over2}\log(13/10)>{3\over23}+{9\over12167}
 ={1596\over12167}>{1311\over10000}>0.131.
\]

For example `phi_*=1311 L/10000` is allowed. For `L>=25` its ratio
to `L^4+1` exceeds `0.131 L^-3`, since `L^4>1310`. Thus the first
strict decimal inequality is not justified either. No numerical run
is used in this check.

## 4. What the universality passages actually supply

| Target statement | Verdict | Account comparison |
|---|---|---|
| U1: clause (d) covers separated connected functions, not log Z, and states no rate | HOLDS | 1831-1836 states convergence at converging frozen-run coupling. The `n>=2` restriction is at **1746**, not 1726. A rate is absent from this statement. |
| U2: the displayed exponential estimates | HOLDS | 94364-94381 requires the smaller initial-profile ball and the **same endpoint, horizon and frozen presentation**. It gives the two displayed bounds uniformly in horizon and compatible volume. |
| U2: scalar vacuum factors are not controlled | HOLDS | 94474-94475 says they may differ and cancel from a normalized final law. This is a genuine missing input for full Wilson masses. |
| U2: no complementary-history comparison | HOLDS | 94511-94512 says no such measure has been introduced. Also retain 94509-94510: the comparison proves neither clustering nor **consistency between horizons**. |
| U2: no unnormalized-mass estimate at all | HOLDS AFTER CORRECTION | 94495-94496 explicitly bounds the ratio of regular integrands and of their normalizers. What is missing is the full Wilson mass with the omitted scalar factors and complementary histories restored. |
| U3: RF62 is a vacuum requirement | HOLDS | 86303-86313 gives an error `C N_0`; it is not a comparison of two physical volumes with a shared density and a summable cutoff error. |
| U4: ST5 bounds log Z relative to a vacuum number | HOLDS | 98404-98417 gives the floor and upper bound with V_(a,ell); it does not assert that V is proportional to physical volume. |
| U5: the label constant can depend on the torus | HOLDS | 61932 expressly distinguishes local nonwrapping families from the label-and-torus-dependent scalar. |
| Claimed regular contribution to UNIV-K | HOLDS AFTER CORRECTION of its prerequisites | The field-dependent integral comparison holds on the common domain specified below. Identifying the one-step RG output with an admitted profile in that same presentation is still open, as is consistency of the two runs. |
| An n=0 form of (d)(3) is “equivalent” to UNIV-K | HOLDS AFTER CORRECTION | It must be a **two-volume comparison after one common extensive subtraction**, with uniformly summable consecutive errors. Separate convergence of two normalizers is not this statement. |

For the regular comparison, use exactly the common endpoint X, domain D
and positive measure nu of 94456-94488. If the interaction difference
is bounded by delta, then pointwise integration gives

\[
 e^{-\delta}Z_{\widetilde H}^{\rm reg}
 \le Z_H^{\rm reg}\le e^\delta Z_{\widetilde H}^{\rm reg},
 \qquad
 |\log Z_H^{\rm reg}-\log Z_{\widetilde H}^{\rm reg}|\le\delta.
\]

Here `delta=C V q_2^N ||H-Htilde||`. If N=K-1, the profile norm is
uniformly bounded, and every common-domain/presentation identification
has been supplied, this gives the proposed geometric error, with the
factor `q_2^-1` absorbed into C. The account does not make those
cross-cutoff identifications in 94364-94512. A bound on normalized laws
also cannot recover an omitted scalar: multiplying either weight by
an arbitrary positive number preserves its normalized law.

**The precision claim at target 346-347 — FAILS from U3/U4 as cited.**
ST5 yields, at zero source,

\[
 \Phi(d)=L^4 V_{a,\ell}-V_{a,L\ell}+R_d,\qquad
 |R_d|\le(C_++C_-)L^4\ell^4.
\]

It does **not** give `Phi=O(L^4 ell^4)` without control of the displayed
vacuum defect. RF62 only bounds its own remainder by `C N_0`, where
N_0 is the fine-lattice site count. No cross-volume cancellation of that
remainder follows. Correct the sentence to the displayed formula and
retain the unknown vacuum defect. The conclusion that UNIV-K has not
been supplied is unchanged.

For clarity, on just these two tori the algebra can be expressed entirely
in Phi. If `u=F_d(T_ell)-F_(pi d)(T_ell)` and
`w=F_d(T_(L ell))-F_(pi d)(T_(L ell))`, choose
`c_d=(u+w)/((L^4+1)ell^4)`. The two residuals are exactly
`+DeltaPhi/(L^4+1)` and `-DeltaPhi/(L^4+1)`. Thus UNIV-K is equivalent,
on an existing predecessor graph, to uniformly summable absolute
increments of Phi, with this factor. Plain convergence, or normalized
correlation universality, supplies no such bound. Even convergent real
sequences need not have summable absolute increments, as `(-1)^K/K`
shows. This is a check of the claimed equivalence, not a new supply
theorem for the Wilson defect.

**UNIV-K remains OPEN — HOLDS as the disposition of these sources.**
The cited account results do not furnish it. This is not a theorem
that no result elsewhere in the account could do so. In particular,
99834-99840 limits the *compactness argument*, not every matched-cutoff
result in the book. This check makes no global absence claim.

The index search located RF62 at `chunk-20.md`, SA 22292-22302,
and ST5 at `chunk-22.md`, SA 23769-23797, with their obligations.
Those source lines and SA 17280-17285 were read. The old outline and
CA full-read index returned no hit for “finite-horizon exponential
universality”; the supplied new account locator was used directly.
No Balaban paper or unprovided source is imported.

## 5. Coverage and source identity

The complete 386-line target was read. Its source inventory O1-O10 is
faithful on the objects needed for links (c)/(e), subject to the explicit
conditional scope above. The historical provenance and task-plan lines
are not mathematical claims. The source statements and dependency uses
were checked; the account's full RG proofs and the already checked seed
and abstract OS theorems were not re-proved. Lemma FL remains an imported
implication not checked in this item. GUIDE claims about asymptotic
scaling are not promoted to theorems.

The account hash is recorded because its 1400-page file is a different
source from the older three-part account at `31a47c543775`:

- Target SHA-256: `505de19f547c22b8f59bebb812464e382937b43b9692d49c2350d76bf764b9df`.
- `sa1400/YM4_1400.tex` SHA-256: `222ef1bd4b668f88fab33f6edd131b4308fc897eefb112ac5898b8730549f178`.
- Checkout HEAD remained `c81a8aa5cfb8afc7b8eb49b14b75ee2da5e20749`.

Verification was written mathematics and source comparison. Shell tools
only retrieved text, hashed sources, and checked the output file. No
computer-assisted proof, numerical experiment, audit, commit, push, or
external post was performed. An initial checkout `rg -E` locator failed
because `-E` denotes an encoding in rg; it was corrected and rerun.
Capped discovery searches were not treated as complete absence evidence.

RESULT: Lemma C and FE HOLDS; Theorem E HOLDS AFTER CORRECTION of the reflected-representative notation and the moment-bound constants, with all seven P' conditions verified under the named seed, lane and account premises and the same M_*; its one-component corollary HOLDS with account 1895's full premises; ONE-K HOLDS AFTER CORRECTION of the base-set quantifier; endpoint-matching necessity, the strict 0.131 bounds, and the claimed raw-Phi precision FAIL as deductions stated; the account's regular universality comparison does not supply full UNIV-K, which remains OPEN; no unconditional mass gap or scientific status is claimed.
