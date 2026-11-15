# Repo search

The lead's `prior/repo-search-2026-11-08.md` was read in full. It covers
main and PRs #10114, #10133, #10134 and #10141, and concerns older RG
obligations. The closer `prior/gap-lit-bridge-lsi.md` and the existing BBD
read in `prior/gap-fullread-2.md` section 3 supplied the literature map.
`prior/gap-avgcurv-check-astra.md` is absent at the pinned commit.

I fetched main, resolving to `8b11ae2bb95e641494fe75ed83d108ee712fa3a9`,
and PR #10114, resolving to `f76f6c649cff7dffbab664d8976e680e8f287fe9`.
I checked these relevant source ranges, without importing their conclusions:

| Prior hit checked | Closeness to this target |
|---|---|
| main: `research/mass-gap/library/prior/gap-fullread-2.md:47–75` | Same BBD tool and its existing literature read; no application to these bridge marginals. Reused and credited. |
| main: `research/mass-gap/library/gap-form-exercise.md:88–98` | Piazza–Shen's two-dimensional compact-group LSI, a different law and dimension. No four-dimensional bridge bound. |
| PR #10114: `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | Earlier Codex positive one-step loop correlation; it supplies no LSI or uniform gap. |
| main: `docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145` | A noncompact determinant-weighted Dirichlet Maxwell covariance estimate, not the tilted compact two-slice law. |

Target-term searches of `open-registry.md`, `open-core.md` and `l17c.md`
found no separate owner of this check. FINISH row 969 assigns it explicitly.
No new proof attack or registry change is made.

The SA-index README, relevant chunk rows and neighboring rows, and
`obligations.md:98–104` were read first. Searches for Polchinski, Bakry,
Elitzur, Brownian bridge, two-slice, tilt-covariance, log-Sobolev and averaged
curvature found no indexed target theorem, including in the CA 4.12–4.19
index. The temporal-gauge match was followed through chunk 02 to SA
2313–2336 and 2454–2499. These supply the transfer frame and exact layer
coordinates, already credited by row 968. Chunk 03 leads to SA 3712–3722,
which explicitly retains the absence of a proved spectral gap. CA-I
2698–2712 likewise does not assert a mass gap. This is bounded source
checking, not an assertion that the entire account was searched exhaustively.

Checker: OpenAI Codex; requested task configuration gpt-6-astra/xhigh.
The interface does not expose independent runtime model/effort metadata.
Checked source commit: `473f053d9340ceb948e52cb6618eb31f533f4c5b`,
2026-11-15. Research text; not an audit; grants no status. This checks
Claude Fable 5.2's row 968, and leaves its source file unchanged.

The outline and CA-I were each fetched once at `31a47c543775` into the new
scratch directory `/tmp/sa-gap-avgcurv-check-astra.1EvtYO/`. BBD and CE PDFs
were also saved there. Credit Ethan Sussman and Levent Alpoge, with Claude
and Codex as authors of their text, for the account's transfer frame;
Bauerschmidt, Bodineau and Dagallier for the flow criterion; Chen and Eldan
for localization; Palais for the slice construction; and the named earlier
repository authors for the bridge and HC inputs.

## Checkpoint

Completed the requested order: FLOW; BBD and POL-BR; Z; NEC; ANG; AVG(a);
section 6.3; then the remaining claims and GUIDE model/arithmetic.
The first missing load-bearing hypothesis is BBD's lower bound on V_0;
section 2 repairs its use. The second proof repair is AVG(a)'s localization.
The output supplies corrections only; no source, queue, registry or status
file is changed. The target covariance and LSI estimates remain open.
No numerical run discharged a statement. No external post was made.

## 1. Proposition FLOW — HOLDS

Source: row 968, lines 126–146. For fixed bridge time s, write
T=1/beta, s'=T-s, c=ss'/T, and Q=x/s+w/s'. These are finite-dimensional
identities, with the original beta kept inside m.

At Polchinski time t,

    exp(-V_t(phi)) = exp[t L(s^(-2)+s'^(-2))/2]
                    integral exp[phi.Q + t x.w/(ss')] m(dx)m(dw).

This proves (a)–(c), including the signs of both derivatives. In particular,
b_c=c/(ss')=1/T=beta. The additive constant in V_t has no field dependence.
For (d), put d=c-t. The joint density before normalization is

    m(dx)m(dw) exp[t|Q|^2/2 + phi.Q - |phi|^2/(2d)]
    = m(dx)m(dw) exp[c|Q|^2/2] exp[-|phi-dQ|^2/(2d)].

Thus its endpoint marginal is precisely J, and its conditional Gaussian has
mean dQ=(1-t/c)((1-beta s)x+beta s w), covariance d Id.
Conditioning back on phi gives J_(b_t,phi). This density computation applies
for t<c; at t=c the tilt is 0 almost surely and the posterior is J. Values of
a conditional law at other points of that terminal null set are immaterial.
The interpretation as changing only the middle layer is valid.

## 2. BBD and POL-BR — HOLDS AFTER CORRECTION

Primary source read: Roland Bauerschmidt, Thierry Bodineau and Benoît
Dagallier, [*Stochastic dynamics and the Polchinski equation*](https://arxiv.org/pdf/2307.07619),
Section 3.2, (3.10)–(3.13), Theorem 3.6, Remark 3.8, and the proof
through Lemma 3.10 and (3.55), including PDF pages 19–22. Remark 3.8 explicitly permits a finite interval [0,T].
The downloaded PDF's numbering differs by one page from the older digest.
The finite-interval and horizontal readings HOLD. There is, however, a
missing hypothesis check: BBD section 3.2, immediately after (3.10), assumes
V_0 bounded below. Here V_0=-Lambda(phi/s)-Lambda(phi/s') is unbounded below.
Thus Theorem 3.6 cannot be invoked literally as stated in that source.

For C_t=t Id, Lemma 3.10 and duality give exactly

    I'(t) = -2 E Hess V_t(grad sqrt(F_t),grad sqrt(F_t))
            - (1/4) E F_t |Hess log F_t|^2.

The signs and the factor 1/4 in row 968 are correct. The variance identity
also has the stated coefficient 1 before the squared Hessian.

The orthogonal gauge action preserves Gaussian convolution and exp(-V_0).
Consequently P_(0,t) commutes with that action. For invariant F, F_t and
sqrt(F_t) remain invariant, and their gradients annihilate orbit tangents.
BBD uses its tensor inequality only on these gradients in (3.48)–(3.49).
The horizontal hypothesis therefore suffices; a supremum over all vectors
is unnecessary. This argument includes singular orbits.

For endpoint continuity, the kernel formula is

    P_(0,t)F(phi) = [g_t*(exp(-V_0)F)](phi)
                   /[g_t*exp(-V_0)](phi).

FLOW gives phi -> 0 in probability as t -> c. The displayed ratio is jointly
continuous near (c,0), for bounded F, by Gaussian domination of the
at-most-linear exponential growth of exp(-V_0). Its value at (c,0) is
E_(nu_s) F. Bounded convergence supplies BBD (3.31), not just convergence
at the one point phi=0.

Repair: extend the displayed proof to this specific potential. With
R=sqrt(L)(1/s+1/s'), |Q|<=R. Every derivative of log Z_(b_t) of fixed order
is bounded by a finite constant depending on R; exp(-V_t(phi)) is bounded
by a constant times exp(R|phi|). On each compact subinterval of [0,c),
Gaussian decay therefore justifies every differentiation and integration by
parts in (3.43), (3.47), and (3.51). The derivatives of P_(0,t)F obey the
same domination for the stipulated smooth bounded tests, including t=0.
The endpoint argument above then gives the full entropy identity. This is
an analytic extension of BBD's proof, not an extra assumed SU(2) estimate.
It repairs the citation gap without changing the constant or the horizontal
hypothesis.

Writing H_s=integral_0^c exp(2 integral_0^t kbar_(s,u) du) dt, the result is
Ent(F)<=2 H_s E|grad sqrt(F)|^2. Choose alpha_s=H_s^(-1).
This verifies the convention 1/alpha_s<=H_s when alpha_s denotes the
optimal constant. The bridge implication uses row 947, Theorem BR,
lines 129–183, as the named existing input; its exponent is
alpha=(1/2) integral alpha_s ds. No SU(2) covariance bound follows.
The Gaussian-mode calculation in lines 169–172 is also correct.

## 3. Lemma Z — HOLDS

Source: lines 148–156, with b in the defined interval [0,beta]. A side of at
least 3 ensures that distinct unoriented positive links have different
endpoint sets. A vertex sign flip then kills every mixed second moment
between distinct links, including x–w moments. It also kills the first
moments. Independent transformations at the two endpoints of one link give
SO(4) invariance for SU(2), so the diagonal blocks are Id/4 and the cross
block is tau_b Id/4. Cube symmetry makes tau_b independent of the link.

Since d log Z_b/db = L tau_b and its derivative is
Var(sum_l x_l.w_l)>=0, while tau_0=0, one has 0<=tau_b<=1. Thus

    Cov(Q) = (1/4)(s^(-2)+s'^(-2)+2 tau_b/(ss')) Id
           <= Id/(4c^2).

The finite-group variant holds for Q_8 and 2T as well. The cross block is
symmetric by exchanging x and w; a symmetric operator commuting with an
irreducible real orthogonal representation is scalar. Irreducibility alone
without that symmetry would not justify an arbitrary cross block.
At phi=0 the orbit is a point, so all vectors are horizontal. This is a
zero-field statement only.

## 4. Lemma NEC — HOLDS, given the repaired POL-BR and HC

Source: lines 193–199. On the central half of the bridge interval,
3/(16 beta)<=c_s<=1/(4 beta). Therefore

    alpha_s >= 1/[c_s exp(2 k* c_s)]
            >= 4 beta exp[-k*/(2 beta)].

Multiplying by the interval length 1/(2 beta), and by BR's factor 1/2,
gives alpha>=exp[-k*/(2 beta)]. HC implies E_1>=alpha: linearize the
L^p-to-L^2 bound at 1 in a centered invariant eigenfunction and let the
integer step number grow. Hence k*>=2 beta log(1/E_1).
The statement is vacuous if k*=infinity. It concerns the supremum over s
and t, not the covariance at the mid-slice or at t=0.

## 5. Proposition ANG — HOLDS on positive-radius fibres

Source: lines 280–290. The radii are fixed and strictly positive; the polar
Jacobian is constant on such a fibre. For a fibre geodesic with velocity v,
its acceleration in link l is -y_l |v_l|^2/r_l^2. Hence

    Hess_fibre Phi(v,v)
      = Hess Phi(v,v) - sum_l (y_l.grad_l Phi)|v_l|^2/r_l^2.

Substitute grad_l Phi=y_l/c-E[x_l|y]/s-E[w_l|y]/s'. The two copies of
|v|^2/c cancel exactly. Add the product-sphere Ricci tensor
sum_l 2|v_l|^2/r_l^2. This is precisely the tensor displayed in ANG.
There is no hidden radial Jacobian or missing factor of r. For S^1 the
intrinsic Ricci tensor is zero. For one free link, the tangential tilted
variance is A(r/s)/(r/s), so the two mean terms cancel their two covariance
terms, leaving 2/r^2 exactly.

The zero-field explanation in lines 292–296 needs a scope correction.
Along y=epsilon u with fixed nonzero link radii ratios, the mean and
covariance terms cancel at order one, leaving the divergent positive
sphere Ricci term. In the U(1) version the remaining tensor tends to zero.
At r_l=0 itself there is no sphere tangent space or fibre tensor. Nor does
this change the genuine negative Cartesian Hessian of nu_s: log-concavity
is a statement in its specified Euclidean geometry. ANG removes that
particular obstruction for the *conditional angular problem*. It proves
no radial or full-measure LSI, and no seed. The frustrated-link estimates
in lines 297–303 remain heuristic; the formula does not validate them.

## 6. Proposition AVG(a) — HOLDS AFTER CORRECTION

Source: lines 305–316. Primary slice text read: Richard S. Palais,
[*On the Existence of Slices for Actions of Non-Compact Lie Groups*](https://www.researchgate.net/publication/216863585_On_the_Existence_of_Slices_for_Actions_of_Non-Compact_Lie_Groups),
Annals of Mathematics 73 (1961), pp. 309–310: the differentiable near-slice
lemma, Propositions 2.2.1–2.2.2, and Remark 2.2.3. These supply a smooth
normal slice and its tubular neighborhood for this orthogonal compact action.

At a principal point, the isotropy acts trivially on the normal slice.
Indeed nearby slice stabilizers are subgroups of that isotropy and have the
same principal conjugacy type. A compact Lie subgroup contained in another,
with the same dimension and number of components, equals it. Thus all
nearby slice points are fixed. A linear functional on the normal slice
with differential z therefore extends to a smooth invariant f on the tube,
with grad f(y_0)=z. This verifies the use of the slice theorem.

The next step in the printed proof is incomplete: shrinking a cutoff does
not make its gradient negligible. The gradient of cutoff times f generally
retains an order-one term from the cutoff annulus. Replace that step as follows.
Let A=K-rho Id. If A(z,z)<0, shrink the tube so A(grad f,grad f)<0 throughout
it. Choose a nonzero smooth invariant cutoff chi supported inside the tube.
For positive integers n set

    G_1=chi sin(n f)/n,       G_2=chi cos(n f)/n.

Both are admissible invariant smooth functions, extended by zero. Exact
cancellation of their cross terms gives

    sum_(j=1,2) E A(grad G_j,grad G_j)
      = E chi^2 A(grad f,grad f) + n^(-2) E A(grad chi,grad chi).

The first term is strictly negative. The second is finite and tends to zero.
This contradicts AVG(0,rho) for sufficiently large n. No oscillatory-limit
claim or numerical test is needed. Conversely, principal orbits have full
Lebesgue measure here; the horizontal pointwise inequality therefore
integrates to AVG. For this gauge representation the full-measure statement
also follows by excluding zero links and reducible loop holonomies, proper
algebraic conditions. This completes the equivalence.

AVG(b) HOLDS for rho>0, and is trivial for rho<=0. Bochner gives
E(LG)^2=E|Hess G|^2+E K(grad G,grad G). For the self-adjoint operator -L
on invariant functions, its spectral measure then has no support in (0,rho).
The zero eigenspace consists of constants since the density is positive on
connected R^N. Smooth invariant functions form a core by smooth cutoffs,
local smoothing and compact-group averaging. This is precisely Poincare.
AVG(c) HOLDS: linearizing F=1+epsilon G in ABS-flow gives

    E Var(<grad G,Q>|phi) <= kappa E|grad G|^2
                              + (1/2) E|Hess G|^2.

At t=0, K=Id/c-Cov(Q), which gives AVG(1/2,1/c-kappa).
None of these statements proves strict separation between intermediate
criteria; lines 319–321 and 385 must not claim a strict implication without
a separating example.

## 7. Section 6.3 — implication HOLDS; claimed obstruction needs correction

For invariant G, the block norm h_l=|grad_l G| is itself gauge invariant:
the gauge action is orthogonal on each link block. Away from h_l=0,

    |partial_a h_l|^2
      = |sum_i (partial_li G)(partial_a partial_li G)/h_l|^2
      <= sum_i |partial_a partial_li G|^2.

Sum over all coordinates a and links l. This proves the stated inequality
sum_l E|grad h_l|^2<=E|Hess G|^2. At zeros, use
h_(l,epsilon)=sqrt(|grad_l G|^2+epsilon^2) and pass to the limit.
Applying CAP to these invariant functions and LOC-COV to grad G gives

    E(LG)^2 >= [1-(rho+D)A] sum_l E|grad h_l|^2
                 + [rho-(rho+D)delta] E|grad G|^2.

This proves the conclusion, under the stated nonnegative defect-budget
convention. No covariance locality is obtained for free.

The RARE-P calculation HOLDS: splitting h into its mean and fluctuation
and applying (a+b)^2<=(1+1/eta)a^2+(1+eta)b^2 gives
A=(1+eta)/(eta lambda), delta=(1+eta)P(Bad_l). Its absorption condition
actually requires lambda>rho+D (for positive rho+D), stronger than the
claimed output. This is the correct reason that using lambda=gamma_s is
circular. The weaker phrase gamma_s>D alone does not express that comparison.

Lemma WC's conditional Gaussian formula HOLDS. At the mid-slice and
x_l=-w_l, y_l=sqrt(c) xi_l; hence

    P(|y_l|<2/5 | x,w)
      = 1-(1+8 beta/25) exp(-8 beta/25).

The numerical value 0.1684 at beta=23/10 is only GUIDE. This explicit
formula shows that an unconditional free-link rarity estimate need not
survive conditioning on endpoints.

The broader claim in lines 358–366 FAILS as a claimed refutation of
uniform conditional CAP or a proved equivalence of LOC-COV to a mass gap.
The supplied conditioning fixes x,w, not the other y-blocks of nu_s; the
set |y_l|<2/5 is not identified with the Bad_l of LOC-COV; and no A,delta
proposed for conditional CAP are refuted. Even for the displayed event,
h=1 only forces delta to be at least that conditional probability.
A finite conditional Gaussian still has a Poincare inequality. Thus the
valid result is the failure of that *particular rarity transfer*, not the
impossibility of every conditional-capacity scheme. A local-diagonal
covariance estimate is a sufficient proposed input here, with no proved
converse or identification with a transfer mass gap. Both remain open.

## 8. Remaining statements and scope

| Statement in row 968 | Verdict | Exact scope or correction |
|---|---|---|
| 2.1 ID-ent and ID-var | HOLDS | BBD (3.43), (3.47), (3.51), with the domination argument in section 2 above. |
| 2.2 CE Proposition 39 plus Lemma 40 | HOLDS AFTER CORRECTION | These give the stated sufficient tilt-supremum route. The pure-linear-tilt description requires constant norm; it is not the general localization formula. |
| 2.2 stopped-path weak estimate | HOLDS | With a deterministic covariance ceiling alpha before stopping, stopped Gronwall gives the stated bound; on the exit event use Var(f)<=osc(f)^2. It supplies no positive spectral gap by itself. |
| 3.3 Gaussian-mode check | HOLDS | With k as stated and kc<1, integral_0^c (1-kt)^(-2)dt=c/(1-kc). A zero-precision mode is a limiting, non-normalizable case. |
| 3.4 zero-field arithmetic; 4.7 no fixed-beta threshold | HOLDS | These are conditional scalar calculations, not SU(2) estimates. The rounded integration and the suggested size 830 remain approximations. |
| 4.2 FP rate test | HOLDS | 2 asinh(sin(pi/(4a)))<pi/(2a)<1.58/a. For even a>=30, K_a>(12.51+3 log a)/a>22/a, so the stated factor above 8 holds. |
| 4.2 compact U(1), 4.4 SMALL-BOX | HOLDS as implications from the named gap premises | At fixed beta, E_1(B)->0 forces k*->infinity; at fixed box, E_1(beta)->0 forces k*/beta->infinity. No recalled gap premise is proved here. |
| 4.3 finite-group bridge extension | HOLDS | BR's Gaussian convolutions and Jensen kernels require a finite endpoint measure, not a manifold. For atomic m, apply endpoint Jensen and sum over atoms. |
| 4.3 claim that frozen-group failure must occur at nonzero tilt | FAILS as an inference from NEC | The asserted beta limit does not compare the necessary growth with the beta-dependent zero-field bound; see below. |
| 4.5 K7; 4.6 kinetic-only test | HOLDS in the stated models | An adjoint time-like term destroys this chord-Gaussian representation. For product Haar m, link independence makes covariance uniformly bounded in volume at fixed beta. No magnetic interaction is supplied by FLOW. |
| 5.1 ambient tensor | HOLDS | The two conditional endpoint laws are independent at t=0, giving the displayed sum of covariances. |
| 5.2 free-link sign and radial integration by parts | HOLDS | The exact threshold is beta>n/2. The n=2 boundary term is 2 pi times the Cartesian density at zero; it is not identically zero. |
| 5.3 angular formula and free-link cancellation | HOLDS | Positive radii only. Its Cartesian and collective-mode interpretations require the restrictions in section 5 above. |
| 5.4 AVG(a) | HOLDS AFTER CORRECTION | Replace the shrinking-cutoff proof by the exact sine–cosine argument above. |
| 5.4 AVG(b),(c) | HOLDS | Under the stated smooth positive finite-dimensional law and invariant form domain. |
| 6.1 SCHR | HOLDS | Kato's inequality for |grad G| and Bochner prove the claimed sufficient form. A nonpositive sig_s gives no positive lower bound. |
| 6.2 death by volume | HOLDS AFTER CORRECTION | DENS must assert a negative *horizontal* direction. It then proves failure on sufficiently large boxes, with no specified seed-box size. |
| 6.3 direction-resolved implication and RARE-P circularity | HOLDS | Block Kato inequality and the full absorption condition are verified above. |
| 6.3 Lemma WC, narrow Gaussian probability | HOLDS | No general conditional CAP is refuted. The broader impossibility claim FAILS. |
| 7.1 ABS-flow sufficient implication | HOLDS | I'<=2 kappa I followed by entropy integration. The coefficient and the direction of both inequalities are correct. |
| 7.1 claimed strict hierarchy | HOLDS AFTER CORRECTION | The displayed arrows are sufficient implications; strictness and necessity of LOC-COV have not been established. |
| 7.2 horizontal Fourier test | HOLDS | Take real and imaginary parts of the complex mode. A transverse spatial momentum makes its discrete divergence zero. The covariance of one independent endpoint gives the stated lower bound at t=0. |

**CE source check.** Read Yuansi Chen and Ronen Eldan,
[*Localization schemes: A framework for proving mixing bounds for Markov chains*](https://arxiv.org/pdf/2203.04163),
section 2.4.2, Fact 14 (PDF p. 16), Claim 22 (p. 21), section 3.1.1
(p. 23), Proposition 39 and Lemma 40 with their proofs (pp. 28–29).
Fact 14 includes exp(-t|x|^2/2) when the driving matrix is Id.
It cancels for the actual endpoint law on M, where |x|^2=L, and also for J
on M times M. It does not cancel for a general measure or a bridge marginal.
With that restriction, the drift grad Lambda and the full-support tilt
argument in row 968 are correct. The all-tilt covariance assumption belongs
to Lemma 40's sufficient criterion; Proposition 39 itself asks for entropic
stability. The report must not exclude other ways to prove that stability.

**Zero-field interpretations.** Line 180 incorrectly attributes all three
ceilings to zero field. In `gap-lsivac-max.md:175–186`, ceiling (i) is a
flipped spatial link at nonzero endpoint tilt; only (ii) and (iii) use the
zero-field argument. The shared zero-field formula also retains the
model-dependent tau_b: the common upper bound is not an identical value
across groups. The correct surviving claim is narrower: POL-BR itself has
no fixed-beta smallness threshold, and the known zero-field obstruction
does not kill its finite-interval integral. Its actual uniform hypothesis
still requires proof. Section 1.2's seed constants were traced to
`gap-vargeom-opus.md:154–166`; their rounded values have the stated
conditional provenance and are not new estimates.

**Frozen-group growth.** Lines 219–222 prove only k*/beta->infinity from
the assumed E_1(beta)->0. Their own zero-field ceiling is O(beta^2).
The former does not exceed the latter: for example log(1/E_1)=sqrt(beta)
would require only O(beta^(3/2)). This numerical family is a counterexample
to the inference, not a proposed spectrum of Q_8 or 2T. At each fixed finite
box all tilts already obey |Q|<=sqrt(L)/c, hence covariance<=L/c^2.
Thus a literal claim that the covariance hypothesis fails at a finite beta
and box is false. The issue is a useful *uniform rate*, with its quantifiers
kept. No actual nonzero-tilt frozen-group theorem follows from this argument.

**DENS.** A negative angular direction from ANG is not automatically
horizontal for the gauge action. With one nonzero link, endpoint gauge
motions span its three angular directions; a vector supported on that link
is horizontal only in its radial direction. After adding the actual
horizontal premise, the volume argument is valid: K_s<=Id/c everywhere,
so if P(k_s<=-D)->1, then
E k_s<=-D P(k_s<=-D)+(1/c)P(k_s>-D)<0 eventually. The trial h=1 gives
sig_s<0. This does not identify when the seed box becomes large enough.

**No strictness or necessity has been proved.** LOC-COV plus CAP is one
sufficient implementation of an averaged estimate. The text supplies no
argument that every proof of ABS-flow must use LOC-COV, or that Ricci cannot
help any collective horizontal direction. A spherical Ricci contribution
acts on every angular tangent vector, including collective ones. The
negative conclusions in 5.5 and 8.2 must be statements about this attempt,
not exclusions of other mechanisms.

## 9. GUIDE source and arithmetic check

Read the complete committed files `guide/lane968/onelink.py`, `onelink.log`,
`tilt.py`, `batch.zsh`, `logs/batch.log`, `logs/tilt_err.log`, and all 42
records of `logs/tilt_results.jsonl`. No simulation or quadrature was rerun.
The logs contain summaries, not measurement time series, so their block
errors and equilibration cannot be independently reconstructed.

**Model — HOLDS.** The quaternion pair multiplication and dagger implement
SU(2). The forward and backward staples have the correct orientations.
Temporal masks remove plaquettes beyond the two ends. Temporal links on
the last slice are never updated or used by an admitted plaquette.
All spatial side lengths are even, so same-direction checkerboard updates
do not update coupled links simultaneously. Adding kappa/beta to the real
staple gives exp(kappa Re U) on spatial links of slice zero. The Creutz
rejection factor sqrt(1-x_0^2), random imaginary direction, and multiplication
by the normalized staple give the stated SU(2) conditional law for nonzero
staples above the code's clipping thresholds. Exact zero staples are not
handled correctly (normalizing zero would produce a zero quaternion); this
is a null event in the ideal continuous law, not a verified code fallback.
The U(1)
von Mises concentration is beta times the staple magnitude.

The measured imaginary components have zero ensemble mean by global
conjugation symmetry (SU(2)) or complex conjugation (U(1)), so their
unsubtracted squared Fourier sums are connected susceptibilities for this
model. The normalization L^3, transverse momenta and component averages
match section 7.2. The sample model is a finite six-slice slab with open
time, as disclosed. It has no exact identification with m or J of the
vacuum theorem. The mean-real-part variance is estimated within blocks and
is biased low, as the code itself says.

**One-link model — HOLDS at GUIDE level.** Its radial weight is proportional
to r^3 exp(-r^2/s)[2 I_1(r/s)/(r/s)]^2, as required. Its curvature formula,
Bessel orders, and conditional chi-square formula match sections 5.2 and
6.3. The saved probabilities and signs agree with the text's rounding.
The finite Bessel sum and truncation r<=3 have no certified error bound;
they supply no proof of the exact integration-by-parts identity.

**Tables and decisions — HOLDS AFTER CORRECTION.** The 42 records have the
advertised groups, beta, sides, seven tilts, T=6, 2000 measurements and
separation two. The batch specifies 400 thermalization sweeps and 20-block
errors. Its saved start and finish are 14:32:32 and 15:31:57; the error log
is empty. The smoke-test values and advance timing of the written criteria
have no separate raw artifact in this folder and were not verified.

The six zero-tilt chi1 deviations are below 1.5 reported standard errors;
the chi0 deviations are below two. The recorded peak chi1 values are

    U(1): 0.587755, 0.627415, 0.928792;
    SU(2): 0.274743, 0.299722, 0.309125.

Thus V0 passes its arithmetic rule, V1 meets its written finite-sample rule,
and V2 is not triggered. The SU(2) ratios are about 1.091 and 1.031.
For U(1), (0.928792-0.5)/0.034112 is about 12.57; the first increase is only
about 1.82 combined standard errors. These support the cautions in 7.5.
At SU(2) side 16 and kappa=1.4, 0.337897/(1/4)=1.351588.

Corrections to the accompanying arithmetic and implications:

- The chi1/chi0 ratios 0.32,0.59,1.1 and 0.81,0.92,0.91 are at *fixed*
  kappa=0.7 and 1.4, respectively. These are not the maximizing tilt on
  every side: the maxima occur at U(1) kappa=0.5 on sides 8 and 16, and
  SU(2) kappa=1.0 on side 8. The corresponding maximizing-tilt ratios are
  about 0.84,0.95,1.12 and 0.97,0.92,0.91.
- The recorded SU(2) middle plaquettes span about 0.5993–0.6041, not
  0.600–0.604 in all runs. The real-part variance at kappa=1.0 grows from
  0.334130 to 0.367581 between sides 8 and 12, about 10%, so the blanket
  8% statement is not literal arithmetic. No phase diagnosis follows.
- Lines 493–499 cannot locate NEC's lower bound at the mid-slice or t=0.
  Multiplying the *global* k* by the numerical midpoint s^2 is legal;
  replacing k* by a midpoint covariance is not. The stated approximate
  calculation log(1/0.26)/2.6≈0.52 is arithmetically sound, but it does
  not constrain the measured tilt family. Its E_1 value is a free-photon
  estimate, not a measured compact-U(1) vacuum gap.
- Growth by a factor 1.25 on two finite size steps cannot refute existence
  of an unspecified size-uniform upper bound. A bounded sequence can do
  that. V2 can be a GUIDE warning, not a mathematical refutation rule.
  This distinction does not change the observed NOT REFUTED outcome.

The heuristic physics of sections 4.8, 7.3 and the readings in 7.5 carries
no proof weight. The data neither proves divergence in U(1) nor boundedness
in SU(2), and does not verify a seed.

RESULT: FLOW, Z, NEC, the positive-radius ANG formula, AVG(b,c), SCHR and the section 6.3 implication HOLD on their stated inputs; POL-BR and AVG(a) HOLD AFTER CORRECTION by the explicit BBD extension and invariant localization proof above; the frozen-group nonzero-tilt inference and the broad conditional-CAP/LOC-COV obstruction claims FAIL as argued. GUIDE model and main arithmetic agree, with the listed corrections and no proof weight. No SU(2) seed estimate is established; (LSI-J-seed), (LSI-br-seed), ABS-flow-seed and the seed remain OPEN.
