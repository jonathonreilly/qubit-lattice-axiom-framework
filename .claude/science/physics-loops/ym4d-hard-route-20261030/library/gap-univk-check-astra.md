## Repo search

Searched `/Users/jonreilly/Projects/Physics` with bounded `git grep -n -i -E`,
over `*.md` and `*.tex`, on `origin/main`, `pr/10114`, `pr/10133`,
`pr/10134`, and `pr/10141`. The specific label query
`UNIV-K|ONE-K([^[:alpha:]]|$)|MAPCONV|DENS-K|VAC-ID|cutoff.universality`
returned no hits. The same labels returned no hits outside this lane in
this checkout. The registry has no `univk`, `UNIV-K`, `DENS-K`, `MAPCONV`,
or `gap-chain-ce` entry. No competing owner of this check was found.

The method query was
`vacuum.density compatib|exponentially decaying step|decaying step sources|same endpoint.*horizon|finite.horizon universality|rts-exponential-universality|ET8.*ET10`.
It returned only `research/ym4d/library/tp1.md:588`, on `origin/main` and
`pr/10141`. Its statement is: "The finite-reference transfer criteria
ET8–ET10 are not used, because Lemma 5.5 is uniform in the torus side."
This concerns a different common-normalizer route; it does not supply the
cross-cutoff comparison here. The surrounding source table was read.

A broader `two.tor(us|i)` query reached its display cap and is not an
absence search. Its relevant hit, `origin/main:research/mass-gap/library/
gap-phys-seed.md:408–431`, states BASE-Phi as
`Phi_rho(L_0/a; beta(a)) <= P_0` for all fine spacings a, with fixed
physical sides L_0 and rho L_0. Its E1 explicitly requires exact
nonwrapping cancellation, leaving wrapping terms and the two final
integrals. This is prior recognition of the same normalization difficulty,
not a proof of summable cutoff increments. Credit that prior diagnosis.
Unqualified `ONE-K` also hit unrelated "one-Kraus" text; the refined label
query above removes that collision.

The existing `prior/repo-search-2026-11-08.md` was consulted, particularly
its R2/vacuum-slot comparison. Its sources concern identical signed local
numbers, not cutoff universality. The indexed underlying statement,
`YM4_sketch_500.tex:19065–19086`, cancels sites only when the same signed
local number occurs on both lists. It does not compare arbitrary vacuum
constants. `sa-index/chunk-24.md:110–130` and
`obligations.md:1358–1360` locate ET8–ET10; the actual outline
26868–26932 was read. This is an already supplied conditional vacuum
criterion, reused below. The old index has no fixed-horizon RTS/RDS or
UNIV-K statement; the supplied YM4_1400 locators were used for those.

Within this lane, `gap-chain-ce-check-astra.md:237–268,285–306,345–412`
already gives Lemma 1.1's reduction, the base-set correction, and the need
for common presentation/domain/measure. These are reused, not claimed as
new. The new work checked here is row 924's weighted estimate and its
subsequent implications. Row 925 contains no separate "Repo prior work"
line. Its requested `prior/gap-univk-check-astra.md` is absent.

Research-text check by Codex, requested as gpt-6-astra xhigh, of FINISH row
924 at checkout 4d4f6848ffa903b477e433697f55e5ea7538026f. Not an audit;
this grants no scientific status. No computation discharges a proof step.

Credit: Ethan Sussman and Levent Alpoge for the account, with Claude and Codex
as authors of its text; Claude Opus 5.5 for row 924; row 917 for the prior
two-torus reduction and corrections. The requested prior-check file is absent.

## Checkpoint

Pinned target: `gap-univk-opus.md`, SHA-256
`998c6331dce711738061d63d047dd2ab292d59fefbf352dccb9f6a1c8336d923`.
YM4_1400 source: `/Users/jonreilly/ym4d-lead/sa1400/YM4_1400.tex`, SHA-256
`222ef1bd4b668f88fab33f6edd131b4308fc897eefb112ac5898b8730549f178`.
Its line numbers below are literal file lines, not PDF page numbers.
The outline source is the supplied 31a47c543775 copy under `sa/`.

Repository refs at this check:

| Ref | Commit |
|---|---|
| origin/main | 4d88da5504d356762deb6b1a1c2695336af9fb81 |
| pr/10114 | f76f6c649cff7dffbab664d8976e680e8f287fe9 |
| pr/10133 | 89faef229ff6e6bde42baad15ed8270c2f4087d8 |
| pr/10134 | 1e70c7211a2cdbc39001e619f1dd89db45e25851 |
| pr/10141 | c73ad7b177d94f89ff37b77386936e3d52b48b05 |

Row 924 was read in full. YM4_1400 ranges read: 61178–61224,
61903–61945, 93864–93918, 94034–94280, 94364–94397,
94424–94545, 102529–102631.
The verdicts below complete the requested checks. Outstanding supply is
the admissible predecessor, common physical realization, MAPCONV/CLASS,
VAC-ID, and the full-history comparison. No new attack on their owners'
work was opened. Only this report is written.

## Elementary statements and the linear estimate

**Lemma 1.1 — HOLDS.** Target 41–50, with an existing predecessor map
on every required datum. Set `r=L^4`, `v=vol(T_ell)>0`, and let `u,w`
be the two log-mass differences. The minimax residual is exactly

\[
 \inf_{c\in\mathbb R}\max\{|u-cv|,|w-crv|\}
       =\frac{|ru-w|}{r+1}.
\]

The lower bound follows from `ru-w=r(u-cv)-(w-crv)`; equality holds at
`c=(u+w)/((r+1)v)`. Thus the uniform absolute-increment series is exactly
the required condition, with factor `r+1`. This checks the reduction
already present in row 917. It constructs no predecessor.

**Lemma 4.1 — HOLDS.** Target 185–190; source 94127–94129,
94364–94381, 94455–94512. On each common positive-measure domain, the
pointwise exponent difference is at most
`delta_T=C vol(T) q_2^N ||H-Htilde||`. Integration puts the ratio of
normalizers between `exp(-delta_T)` and `exp(delta_T)`. Taking logarithms,
then adding the two bounds with coefficients `L^4` and `1`, gives exactly
`2C L^4 ell^4 q_2^N ||H-Htilde||`. The shared endpoint cancels the action
term. These are the regular normalizers defined in the source, with their
vacuum factors omitted. No full Wilson-mass comparison follows.

**Proposition 4.3 — HOLDS.** Target 200–214; source 94196–94236 and
94082–94108. The boundary conditions, inverse products, signs and empty
sums agree with the source. Here is a direct geometric-sum check of the
weighted argument. Put `q=q_3`, `e_bar=sup e_j`, `k_bar=sup k_j`,
`U=max q^(-j)|u_j|`, and `V=max q^(-j)||v_j||`. The account gives
`e_bar<=C e_*`, `k_bar<=C e_*/X_0` and `|P_jl|<=C`, uniformly in N.
Since `lambda_0<q` and `q_1<q`,

\[
 \sum_{i<j}q_1^{j-1-i}\lambda_0^i
 \le\sum_{i<j}q_1^{j-1-i}q^i
 =\frac{q^j-q_1^j}{q-q_1}\le\frac{q^j}{q-q_1}.
\]

The exact mixed factorization therefore gives

\[
 U\le \frac{Cs}{1-\lambda_0}+bV,
 \qquad V\le R+\frac{t}{q-q_1}+kU,
 \quad b=\frac{Ce_{\rm bar}}{1-q},\quad
 k=\frac{Ck_{\rm bar}}{q-q_1}.
\]

Their product tends to zero with the floor. Choose `bk<=1/2`, independently
of N, and substitute the second inequality into the first. This bounds
both U and V by `C(s+R+t)`. At `j=N` the backward source sum vanishes;
at `j=0` the forward product is the identity. Thus both endpoint cases
are included. The target's displayed `O((log X_0)^(2m)/X_0^2)` is a loose
upper bound: the product used here is actually
`O((log X_0)^(2m)/X_0^3)`. No correction to the conclusion is needed.

**Lemma 5.2 — HOLDS.** Target 313–319. Write the P-increment bound as
`|P(d)-P(pi d)|<=(r+1)epsilon_K` and `E=sum epsilon_K`.
For `d_0=pi^(K-K_0)d`, telescoping gives

\[
 \Phi(d)-\Phi(d_0)
 =P(d)-P(d_0)+Q(d)-Q(d_0)\le(r+1)E+2\eta.
\]

The assumed base bound proves the conclusion, including all base data.
No increment bound for Q is needed. A bounded alternating Q shows why
this does not prove UNIV-K for Phi itself.

**Lemma 6.4 — HOLDS.** Target 382–385; source 61934–61941.
Integrating the two inequalities in DENS-K preserves their order and
gives `exp(c_d vol(T)-delta_K) Z_(pi d)(T) <= Z_d(T)` and the corresponding
upper bound. Both masses are finite and positive. Their logarithms give
UNIV-K with `epsilon_K=delta_K`, the same c_d and the same existing pi.
The marginals here must remain unnormalized; normalized probabilities
do not retain the partition functions. DENS-K is a sufficient, stronger
measure comparison, not an equivalent reformulation of UNIV-K.

## The consecutive-cutoff bridge

**Finding 4.2 and Observation 3.1 — HOLDS AFTER CORRECTION.** Target
157–164, 192–198. Row 916's use of finite-horizon universality at
`gap-chain-ce-opus.md:325–330` lacks the same-presentation identification.
This was already identified in row 917. Source 94034–94040 explicitly
restricts the theorem to one horizon and one frozen presentation;
94364–94381 imposes those conditions again. Endpoint matching alone
does not supply them. Source 94450–94453 restricts its endpoint derivatives
to that single presentation. Thus the derivation is incomplete as cited.

Correct the stronger assertion that 94534–94545 *proves* the two
presentations differ. Those lines define the transfer index and give
`|b_j-b_infty|+|m_j-b_infty|<=C lambda_0^j`. They give an upper bound,
not nonconstancy. In particular, `b_j=m_j=b_infty` obeys that displayed
bound. The cited Gaussian-jet definition, 61191–61220, also supplies an
asymptotic estimate, not the required inequality between consecutive
scalar increments.

For the proposed reindexing, what follows is only

\[
 |b_{j+1}-b_j|\le C(1+\lambda_0)\lambda_0^j,
 \qquad
 |a_{j+1}^{(K)}-a_j^{(K-1)}|
 \le\frac{C(1+\lambda_0)}{1-\lambda_0}\lambda_0^j.
\]

This permits an error; it neither proves a nonzero error nor controls all
the other maps. Replace "the same frozen presentation does not hold"
by "the required identification has not been established by these
citations." The regular-part estimate is not refuted. MAPCONV is a
possible sufficient route; a verified common-presentation rerun would
also suffice. It is not logically necessary to use MAPCONV specifically.

**Corollary 4.5, including the use of Proposition 4.4 — HOLDS AFTER
CORRECTION.** Target 216–247. The weighted profile response follows from
Proposition 4.3 if CLASS supplies one differentiable family of admitted
tuned trajectories in identified Banach spaces, with uniform R11 bounds.
Use the target's erratum: `H(t)=t h_1^d`. The derivative has `xi=0`,
`eta=h_1^d`, and exactly the sigma and tau displayed at target 228–230.
MAPCONV bounds those sources. Integrating the derivative proves
`||h_N^A-h_N^B||<=C(R+s+t)q_3^N`, with `R` a uniform bound for `h_1^d`.
This part of the argument holds under the specified family hypothesis.

Two further bridges are needed before this is the stated regular UNIV-K:

1. **An admissible predecessor on every datum.** The tuned beta' must
   lie in `W_(K-1)(g)`, with the same coupling construction as the
   first-passage definition. Tuning a regular recursion to an endpoint
   (source 94131–94145) gives neither that first hitting time nor that
   identification. The target itself leaves this open at 241–242.
   Replacing the base set by the image of the chains cannot repair a
   missing intermediate first-passage datum.
2. **A common final integral and profile evaluation.** For each torus,
   identify the endpoint action, final domain, positive measure, and the
   map taking a profile to its physical interaction. Require the common
   evaluation to obey
   `sup|H_N^A-H_N^B|<=C vol(T)||h_N^A-h_N^B||`.
   Source 94455–94488 supplies this within its single presentation.
   MAPCONV bounds the recursions; equivalence of adapted norms alone
   does not identify the physical evaluation or the integration measure
   across presentations. CLASS as printed only asserts tuning bounds.

The second bridge matters even for equal interaction functions: replacing
a positive measure nu by `exp(a)nu` changes log Z by a while leaving the
profile recurrence unchanged. Calling this a vacuum factor requires its
explicit separation and identification. It cannot disappear from the
argument for an actual mass. This is an inference diagnostic, not a
counterexample to the Wilson construction.

With these two additional hypotheses, apply the common-integral estimate
on each torus after the profile comparison. This gives

\[
 |\Delta\Phi^{\rm reg}|\le
   2CL^4\ell^4(R+s+t)q_3^{K-1},\qquad
 \epsilon_K^{\rm reg}\le 2C\ell^4(R+s+t)q_3^{K-1}.
\]

The second bound is a permissible, slightly larger bound after dividing
the first by `L^4+1`. Its tail is at most
`2C ell^4(R+s+t) q_3^(K_0)/(1-q_3)`.
The target's extra factor `q_3^-1` is harmless slack. These corrected
hypotheses yield the claimed implication; their actual-model supply
remains open. Increasing the profile ceiling and then the floor, as in
244–247, must also retain the original datum's admissibility.

## Vacuum comparison

**Lemma 5.1, the requested vacuum bound — HOLDS given VAC-ID and the
full ET8 hypotheses.** Target 305–311. Source 102538–102579 states
the same criterion already present in the outline. With
`delta=kappa_E-kappa_D>0`, cancellation of matched small domains leaves
at most two tails
`C_D C_E sum_(m>=ell/(C_0 a_j)) exp(-delta m)` per root.
The geometric sum is bounded by `C exp(-c ell/a_j)`. Dividing the root
count by physical volume gives `C a_j^-4 exp(-c ell/a_j)`.
The scale sum is uniform: its b-th summand is
`L^(4b) exp(-c ell L^b)`, and after extracting `exp(-c ell/2)` the
remaining series at ell_0 converges. For example, the ratio of consecutive
remaining terms is `L^4 exp(-(c ell_0/2)(L-1)L^b)`, eventually at most
one half. This is a written geometric-tail argument.

Consequently, writing `E_(T,K)=vol(T)A_K+W_T`,

\[
 |L^4E_{\ell,K}-E_{L\ell,K}|
 \le CC_{\ell_0}L^4\ell^4
       \bigl(e^{-c\ell/2}+e^{-cL\ell/2}\bigr)
 \le 2CC_{\ell_0}L^4\ell^4e^{-c\ell/2}.
\]

The sign convention for the scalar does not affect this absolute bound.
The common A_K cancels at each datum and need not converge. Uniformity
over first-passage data additionally means the criterion's constants are
uniform over those data, as VAC-ID must require. Lemma 5.2 then charges
twice this bound to the seed margin; it does not prove summable increments.

The actual identification is still an assumption. Source 61932 distinguishes
E and R on nonwrapping domains with matching step data from the scalar
`Ecal_(k,S)`, which depends on both label and torus. Source 102586–102589
expressly withholds ET9 if actual nonwrapping formation compatibility is
unproved. Thus these citations do not identify the scalar in the full mass
with ET8's E. This is a limitation of the cited argument, not a claim that
no other passage anywhere in the account can address it.

Fix the scalar split before using VAC-ID. For an all-regular reference
term one may set `E=-Ecal_(K,empty)` and put all relative label constants
inside Q. A label-dependent scalar cannot simply be pulled out of the
sum over labels. Nor does equality of field-dependent local E/R terms
make their two log integrals cancel term by term. The inference in
Step 5a, item 2, needs an actual scalar expansion or a comparison of those
integrals. ET8 provides a criterion for such a scalar expansion, not for
arbitrary field-dependent terms.

**Lemma 5.3, if used for literal vacuum increments — HOLDS AFTER
CORRECTION.** Target 320–329. Besides the corrected Proposition 4.4,
require that aligned wrapping terms are evaluations of the *same*
holomorphic formation functional, or separately bound the difference of
those functionals at matched input. Require a uniform inner Cauchy margin
in coordinates whose data differences obey `Cq_3^j`. Holomorphy and a
uniform bound for each of two different functions do not compare them:
the constants `+A` and `-A` satisfy those assumptions at identical input
but differ by `2A`. MAPCONV as printed controls r,T,n,f, not this vacuum
formation rule. VAC-LIP must explicitly include the common-function
identification if it is intended to cover it.

With that addition, Cauchy's estimate gives the wrapping difference
`C vol(T) a_j^-4 exp(-c ell_T/a_j) q_3^j` at aligned levels. Relabeling
with `b=K-j` produces the series

\[
 C\operatorname{vol}(T)q_3^K
 \sum_{b\ge0}L^{4b}q_3^{-b}e^{-c\ell_TL^b}.
\]

It converges by the same ratio argument as ET10. The extra finest level
is bounded by `C vol(T)L^(4K)exp(-c ell_T L^K)` and is also at most
`C' vol(T)q_3^K`. This verifies the summation step, conditional on the
added comparison, without claiming actual vacuum increments are supplied.

## Limits of the adjoining large-field discussion

**Finding 6.2's deduction — FAILS as a proof.** Target 362–370 is marked
ARGUED and explicitly calls its Gaussian-tail lower bound heuristic.
No lower probability bound is proved there. Even a diverging expected
number of failed cells would not imply that the all-regular probability
tends to zero. For example, `Y_K=K^2` with probability `1/K` and zero
otherwise has `E Y_K=K`, but `P(Y_K=0)=1-1/K`. This is a counterexample
to the inference about counts, not to a Yang–Mills claim. A dependence or
concentration estimate would be needed. Further, decay of the all-regular
share alone would still not bound its non-extensive two-torus defect.
The source's exclusion of complementary histories at 94511–94512 is
enough to retain the open full-history comparison; this heuristic adds
no obstruction theorem.

## Verdicts and scope

| Requested statement | Verdict | Scope |
|---|---|---|
| Lemma 1.1 | HOLDS | Existing predecessor graph; reuse row 917's exact reduction. |
| Lemma 4.1 | HOLDS | Same endpoint, horizon, presentation and common final integrals. |
| Proposition 4.3 | HOLDS | The exact linear system and its uniform coefficient bounds. |
| Lemma 5.2 | HOLDS | Uniform bound on Q and summable increments of P. |
| Lemma 6.4 | HOLDS | Ordered unnormalized finite positive measures, with the same c_d. |
| Corollary 4.5 | HOLDS AFTER CORRECTION | Add admissible predecessors and the common final physical realization; interpret CLASS with uniform linearized bounds. |
| Vacuum bound, Lemma 5.1 | HOLDS | Conditional on identifying the chosen scalar with the full uniform ET8 criterion. |
| Finding 4.2 about row 916 | HOLDS AFTER CORRECTION | The cited derivation lacks a presentation identification; the Gaussian estimate does not prove actual mismatch. |

The corrected ONE-K telescope also holds, as already checked in row 917.
The additional vacuum-increment argument needs the common formation
comparison stated above. Finding 6.2 supplies no proof of its proposed
obstruction. These findings change neither the source text nor a registry,
ledger, audit record, or scientific standing.

Checked the named arguments line by line by Codex. This is a cross-provider
text check, not an independent experimental or computational verification.
The source's primitive formation estimates remain cited inputs; their
complete dependency proofs were not rechecked. Step 7's group-specific
fact tests, the seed and Lemma FL were not rechecked. No Balaban paper,
numerical proof, Lean run, network search, or external post was used.
The report is left locally at the requested path, uncommitted and unpushed.

RESULT: Lemmas 1.1, 4.1, 5.2, 6.4 and Proposition 4.3 HOLD; the vacuum bound HOLDS under VAC-ID and uniform ET8; Corollary 4.5 and Finding 4.2 HOLD AFTER CORRECTION as specified above; the adjoining large-field count argument FAILS as a proof. UNIV-K remains open on the cited inputs; no status is granted.
