# PRE-STATED — independent hostile review of OSLEAF55

UTC pre-statement: 2026-10-29 05:29:16 UTC (tool clock at start; recorded before mathematical derivations).

Scope: OSLEAF55.md, including E1 and the overriding errata, reviewed independently of its author's derivations. Deliverable: this file only. No git, no snapshots, no audit ledgers, no numerical approximations. Source locations will be obtained by string search and reported with the observed line numbers. The reviewer is Codex; the requested cross-family assignment is recorded without claiming independent access to backend model metadata.

Prior exposure: before this pre-statement I searched the target's headings/locators and read its errata E1–E8, plus the required SCIENCE_WORKFLOW and applicable review-loop instructions. I have not yet derived any mathematical claim. The owner's restricted scope overrides the skill's branch/landing workflow and additional-reference suggestions.

Targets and pre-stated refutation criteria:

1. FS, the flat test space, partial product, positive half, Lemma P, and OWN-alg: refutation means an admissible ordinary-moment counterexample, an undefined purported operation, a coincidence in an admitted RP test, or a mismatch with the actual OS theorem's domain.
2. REC/ML2 and the growth match s=11, beta=p+3: refutation means a failed null-space/semigroup step, an unproved hypothesis needed for the Wightman import, or an exponent/seminorm that does not dominate the actual OS condition. An unread or unmatched theorem remains NOT-VERIFIED.
3. CLOSURE-sep and CONTRACT-sep: refutation means the finite-lattice reflection identity, extension, limit, or density step does not follow with the stated quantifiers; fixed-radius and infinite-volume domains must remain distinct.
4. X1/MIN/EXT: test whether Banach–Steinhaus gives precisely the claimed uniformities and n-growth, whether all scales/translates are covered, and whether shell/remainder estimates actually sum. A weaker necessary condition does not establish necessity of the stronger sufficient condition.
5. TP/BRIDGE: independently rebuild the tensor expansion, support separation, coefficient summability and n-growth; test whether separated-product convergence determines/extends a positive invariant functional on the exact flat space. A lost n-dependent factor or topology mismatch refutes the printed quantitative bound even if a repaired bridge could survive.
6. TRAJ/ML12: pin each coupling/constant to its local definition, recompute the F-tune inequalities, and test all conflicts within accessible sources. An unevaluated output constant or undocumented uniformity remains NOT-VERIFIED.
7. Seven negative dispositions and ol55_1: test each check's ability to fail, independent expected values, scope and negative controls. Toy checks cannot establish the continuum theorem.

Finding verdicts: CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses: PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED is always restricted to the proposition and premises actually re-derived. Findings are appended incrementally, followed by the summary and an exact bankable subset.

## Findings (incremental)

### F1 — MIN does not establish the claimed global minimality

**REFUTED as a functional-analytic necessity argument; NOT-VERIFIED as a Wilson-specific necessity theorem. Claim: GAP.** Attachments: `OSLEAF55.md:442` (Proposition MIN), `:450` ("So (X1) with SOME n-dependent"), `:785` (E6), `:883` ("Necessity (so this is the minimal bridge)").

The Banach–Steinhaus calculation itself is correct on the fixed Fréchet space of flat tests supported in K^n: pointwise convergence gives `|S_j(G)| <= C_(n,K) max_(|alpha|<=N_(n,K)) ||partial^alpha G||_infty`. Multiplying and dividing by powers of lambda gives the displayed local per-scale bound. E6 correctly handles residual lattice translations by enlarging K.

The next inference changes quantifiers. X1 (`:381`) asks for one A_n,p_n,r_n for cubes Q_1,...,Q_n **anywhere** in the growing volume, including arbitrarily large relative separations. Translating a common ball does not bound its required diameter. MIN produces constants depending on that diameter, not a uniform bound over those configurations. It also concerns the specified convergent sequence, not every independent value of a and R in X1.

Explicit counterexample to the asserted functional-analytic inference: the constant sequence of translation-invariant tempered functionals `T_2(G)=integral |x-y|^2 G(x,y) dx dy` converges on the entire flat Schwartz space. Let f be a smooth compactly supported even bump with integral one, and set `G_d(x,y)=f(x)f(y-d e_1)`. For large d the two supports are separated by at least one, all the unweighted derivative seminorms in X1 at lambda=1 are independent of d, while `T_2(G_d)=d^2+2 integral |x|^2 f(x) dx` is unbounded. This counterexample is not a Wilson model or an RP state; it refutes precisely the claimed deduction from equicontinuity and translation invariance. No such additional Wilson/RP argument is given in MIN. A legitimate necessary statement is local equicontinuity, or a global Schwartz-weighted bound after global equicontinuity; X1's uniform placement condition is a stronger sufficient input. Linear growth in n is separately additional, as the target correctly acknowledges.

### F2 — the check computes an upper envelope, not the SU(N) maximum

**REFUTED for the word "max" and its universal value 24; CONFIRMED for the bound <=24. Claim: PROVEN after narrowing.** Attachments: `OSLEAF55.md:665`, locating string "max a⁴e_a = 24"; `checks/ol55_1_criteria.md`, G1 clause (iii); `checks/ol55_1_conventions.py`, `max_a4_e = Fr(n_ordered_terms * 2, 4)`.

The exact count is `4 binom(4,2)=24` geometric plaquettes, doubled to 48 ordered terms. Thus `48*2/4=24` is a valid upper bound. The code defines its alleged maximum from the single-plaquette envelope and never checks attainability in SU(N).

For SU(3), write the eigenangles as alpha,beta,-alpha-beta. Put `c=cos((alpha+beta)/2)` and `d=cos((alpha-beta)/2)`. Then

`Re tr U = 2cd+2c^2-1 >= 2c^2-2|c|-1 = 2(|c|-1/2)^2-3/2 >= -3/2`.

Consequently `s(U)<=3/2`, with equality for either nontrivial central SU(3) element. The correct SU(3) maximum is **18**, since `48*(3/2)/4=18`. It is attainable locally (and on an even torus with side in lattice units divisible by 3) using constant central plaquette flux; orientation reversal replaces the central element by its inverse and leaves s unchanged. For example use central links `U_nu(m)=z^(sum_(mu<nu) m_mu) I`, `z=exp(2*pi*i/3)`, on a side-6 lattice. Every positively oriented plaquette has flux z. No numerical approximation is used.

The Z^3 control tests the combinatorial dimension; it cannot test this attainability claim. The proof's X0 only requires the universal <=24 bound and is unaffected.

### F3 — omitted factor 2N in the trajectory dictionary (load-bearing symbol collision)

**REFUTED. Claim: GAP in the claimed shared trajectory; the within-FLOW arithmetic survives.** Attachments: `OSLEAF55.md:117–118`, "g_bare = FLOW's g_0 = PROOF §1 S3's g_K"; `:535–537` (TR-0); `:564–570` (TR-9); `:593` and `:607–609` (C-T8). Actual producers: `FLOW.md:24–25`, "u = β_Wilson = 2N/g_std²"; `:134`, "𝒯_0(U) := Σ_p s(U_p)"; `:575–587` (Lemma F-norm); `PROOF.md:799–804` (S1–S3).

This is not just reversed indexing. Both files use `s(U)=1-Re tr(U)/N`. FLOW's bare action is `u_0 sum s`, with `u_0=1/g_FLOW^2`; PROOF's action is `(2N/g_PROOF^2) sum s`. Equality of measures therefore requires

`1/g_FLOW^2 = 2N/g_PROOF^2`, hence **`g_PROOF = sqrt(2N) g_FLOW`**.

The target's equality is false for every N>=2. For SU(3), using the same numerical coupling multiplies PROOF's Wilson coefficient by **6**; the matching coupling is **sqrt(6)** times FLOW's. No smallness bound or index reversal removes this factor.

TR-9 then puts `beta_Q=2N/G^2` but proposes `G^{-2}` as an interpolation of TR-6's FLOW trajectory. That yields `beta_Q=2N u_traj` at the base spacing, not `u_traj`. Correct alternatives: (a) use `beta_Q=G_FLOW^{-2}` with interpolation of u_traj; or (b) keep `beta_Q=2N/G_std^2` and interpolate `G_std^{-2}=u_traj/(2N)`. The same conversion is needed in any target/reference coupling dictionary. This is an additional conflict missing from C-T1–C-T8.

SRCCD's Lemma V uses the FLOW convention internally (`SRCCD55.md:158,247,252`). Its coefficient in front of `g_FLOW^4` is therefore not itself refuted by this collision. If expressed in PROOF's coupling, the same bound's coefficient becomes **`c_v/(4608 N^2)`**, because `(c_v/1152) g_FLOW^4 = (c_v/(4608 N^2)) g_PROOF^4`. FS only needs a positive N-dependent coefficient, so its conditional obstruction survives after this conversion. The direct identification of the measures does not.

### F4 — FS is a valid conditional obstruction, with an essential unnormalised hypothesis

**CONFIRMED in FLOW's coupling convention for real test functions and the stated even tori. Claim: CONDITIONAL.** Attachments: `OSLEAF55.md:128–145` (FS); `SRCCD55.md:217–282` (Lemma V), corrected by `:926–927` (E2); `FLOW.md:433–452` (F-tune).

Independent reconstruction of the needed variance scale: conditioning on all links except direction-1 links based on `(2a Z)^4` leaves independent selected links, since a plaquette contains at most one selected link. For the smeared clover, its coefficient on a selected link's six staples is `2f(x)+O_f(a)`. The conditional circle subgroup `diag(exp(it),exp(-it),1,...)` gives density proportional to `exp(kappa cos t)` with `kappa=u_0 |z|/N`. The Haar-ball lower bound on the partition function and concavity of its negative logarithm give a volume-uniform `E s(U_p)=O_N(log u_0/u_0)`. Hence the event `|z|>=1` has probability at least 1/2 for sufficiently large u_0; always `|z|<=12`.

Two angle intervals of width comparable to `kappa^(-1/2)`, one near zero and one between `2/sqrt(kappa)` and `3/sqrt(kappa)`, each have a positive probability bounded below independently of kappa>=4. Their cosine values differ by at least `1/kappa`. The sine second moment is also bounded below by a positive constant times `1/kappa`, and the mixed cosine/sine covariance vanishes. Thus every shifted cosine has variance >=`c/kappa^2`. The conditional observable variance is consequently >=`c_N u_0^(-2)(2|f(x)|-O_f(a))_+^2`. Summation over the selected grid of cell volume `16a^4` gives `Var O_a(f)>=c_N g_FLOW^4 a^(-4)(||f||_2^2-O_f(a))`. This derivation needs neither a source estimate nor a coarse-field moment hypothesis.

Now bounded normalised variance implies `Z^2>=c g_FLOW^4 a^(-4)`. Nonzero normalised covariance on one separated pair implies `|Cov(O_a(g_1),O_a(g_2))|>=c_0 Z^2`. F-tune's upper bracket gives `u_0<=g_ref^(-2)+R_F+beta_+ log(1/a)`, so the last lower bound diverges as at least `c a^(-4)/(C+beta_+ log(1/a))^2`. A cutoff-uniform **unnormalised** separated upper bound contradicts it.

This does not follow from a bound only on the normalised separated covariance. Nor does conditional SRC-kappa automatically provide the unnormalised unconditional upper bound: F8 below rebuilds that missing step. FS does not prove that the separated limit exists or is nonzero, and its torus proof does not transfer to the sphere. The sharp variance coefficient from the old review is not used as authority here.

### F5 — the flat domain/RP form are sound; OWN-alg must retain its literal scope

**CONFIRMED for the test-space parts of D1–D9, Lemma P, DENSE and the continuous scalar Euclidean action. Claim: PROVEN as test-space statements.** Attachments: `OSLEAF55.md:150–202`; OWN-alg at `:282–288`; `PROOF.md:773–774` (actual T_OS wording). D8's identification of the actual Wilson coupling is subject to F3; its sphere inputs are not included in this confirmation.

At a coincidence inside either half, all derivatives of the corresponding ordered test vanish. A cross-half coincidence forces both times to zero (or into a zero region), where the factors are flat. Thus every derivative of `Theta F^* tensor G` vanishes on every collision plane. The tensor seminorm follows from `1+|x|^2+|y|^2 <= (1+|x|^2)(1+|y|^2)`. Compact strictly ordered supports have a positive distance from these planes. Cutting a flat Schwartz function off at infinity, then off an epsilon-neighbourhood of the diagonals, converges in every Schwartz seminorm: choose Taylor order greater than the derivatives lost by the cutoff. The same construction applies at the ordered-time boundaries. Euclidean motions preserve collision planes; chain-rule and polynomial-weight bounds give continuity. Countable dense determining sets and their countable group orbits therefore exist.

This is a partial test-function algebra, not an ordinary everywhere-defined algebra of smeared random-field polynomials. In particular `f tensor f` is excluded when f is nonzero, and the RP cone is the specified ordered-half cone. It agrees with the conventional distributional OS formulation, rather than weakening that formulation: [Adamo–Moriwaki–Tanimoto, arXiv:2407.18222v2, §2.5, definitions preceding (21)–(24)](https://arxiv.org/html/2407.18222v2#S2.SS5) explicitly uses the same flat space, ordered half, seminorm and reflection form. No sentence is quoted from the literature.

It would weaken a **different**, ordinary Euclidean positive-state requirement. PROOF's phrase "state on an E(4)-covariant algebra" does not by itself identify a partial RP test algebra with such an ordinary state. OWN-alg is an explicit interpretation to record, not a theorem that those two notions of state coincide. There is no obstruction here to importing the correctly scoped scalar OS theorem.

### F6 — REC(a)–(d) survive, but its translation estimate omits the insertion number

**REFUTED for the printed translation-weight inequality; CONFIRMED for REC(a)–(d) after this harmless correction. Claim: PROVEN as an implication from E0, E1 and E2.** Attachment: `OSLEAF55.md:213–258`, especially `:240`.

D3 translates all m insertion points. Its translation vector in R^(4m) has squared length `m u^2`, not `u^2`. Correct:

`|T_u G_m|_k <= 2^(k/2) (1+m u^2)^(k/2) |G_m|_k`.

The underlying printed weight inequality already fails at **m=4, u=1, y=0: 5<=4 is false**. The corrected Peetre bound is `5<=10` at that point. The replacement factor is **1+m u^2**. A finite test sequence still gives a polynomial bound in u, so no reconstruction conclusion is lost.

For completeness, positivity of the sesquilinear form gives Hermiticity by polarisation and Cauchy–Schwarz, and its null space is orthogonal to every vector. Time translation by `-s/2` gives `<F,T_s G>=<T_(s/2)F,T_(s/2)G>`. Repeated Cauchy–Schwarz bounds `||T_sF||` by `||F||^(1-2^(-k)) ||T_(2^k s)F||^(2^(-k))`; polynomial growth makes the second factor tend to one. If F is null, the first Cauchy–Schwarz inequality already makes T_sF null. This proves contraction, positivity, and descent to the quotient. Continuity on the dense test domain plus contraction gives strong continuity; the spectral logarithm of the injective positive contraction P_1 gives H>=0 and P_s=exp(-sH). Spatial motions commute with reflection and translations and preserve the form.

For the separated insertion h, translating by `-tau/2` places h entirely in the negative half, allowing the bra to be written as `Theta K_G^*`. Thus `<G,Phi_tau(h)F>=<P_(tau/2)K_G,F>`. This proves null-space preservation and a densely defined adjoint, hence closability. The vacuum products involve only ordered, separated tests. These steps establish the Euclidean operators claimed in (d); they do not on their own construct tempered Minkowski fields.

### F7 — the proposed conditional-cumulant version of SP repeats the singleton gap

**REFUTED as written for the stated n>=2 bounds. Claim: GAP; repair is explicit singleton control.** Attachment: `OSLEAF55.md:817–824`, especially "the same bound for conditional CUMULANTS (moments then follow by the partition sum, b → b + 1)".

The preceding quantified estimate starts at n=2. Global centring in D8 does not make conditional first cumulants vanish. Already

`E[X_1 X_2 | V] = kappa_2(X_1,X_2 | V) + E[X_1 | V] E[X_2 | V]`.

An exact probabilistic counterexample to the proposed implication: let Y be a fair sign, let the centred lattice field be `X_a(x)=a^(-4)Y`, and condition on Y. Every conditional cumulant of order >=2 is zero, satisfying any proposed higher-order bound. The crude field bound X0 holds with C_X=1,q_X=4. Choose two separated smooth test families with discrete integrals exactly one and uniformly bounded fixed-scale seminorms (normalise fixed bumps by their convergent nonzero Riemann sums). Their unconditional smeared two-point function is exactly **a^(-8)**, which violates SP at any fixed lambda. This is a counterexample to the stated probability argument, not a claim about Wilson dynamics.

The repair is to include uniform conditional **first** cumulant bounds for every single insertion, in addition to all higher orders, with the required a,R,lambda and n uniformities. Then the conditional moment partition formula does prove `b -> b+1`: each block contributes A^|B|(|B|!)^b, their product is <=A^n(n!)^b, and the number of partitions is <=n!. Averaging is then legitimate. The alternative uniform bound on the entire conditional product in (b) is independently sufficient by `|E E[product|V]| <= sup_V |E[product|V]|`; it is not supplied by higher conditional cumulants alone. The primary, **unconditional** SP hypothesis is unaffected.

### F8 — GROW and the actual OS growth match, with two scope limits

**CONFIRMED for Z=1 given the unconditional SEP-pt bound; NOT-VERIFIED from SRC-kappa; NOT-VERIFIED as a Wilson theorem for arbitrary Z. The general two-bound implication with s=11 is REFUTED when q_X is unrestricted. Claim: CONDITIONAL for the repaired statement.** Attachments: `OSLEAF55.md:457–476` (GROW), `:168` (general Z), `:469` (region III), `:264` and `:619` (growth match); `SRCCD55.md:549–573` (E(a)–(c)); `CODEX_REVIEW_SRCCD.md:311–351` used only to locate the disputed inference.

Independent growth derivation: write the capped short-distance weight as `wbar(delta)<=C_q delta^(-5)` for 0<delta<=1. On configurations with minimum separation delta in [c_*a,1), Taylor-expand a flat test from its nearest collision plane to order 5n. Its factor `delta^(5n)` cancels the worst product singularity `delta^(-5n)`. Reserve 5n powers of the Schwartz weight to dominate `product_i (1+|x_i|^2)^(-5/2)` and sum over lattice sites; the resulting bound is `C^n(n!)^b0 |F|_(10n)`. At separation >=1 the same weight alone suffices. On delta<c_*a use X0 and Taylor order q_X n+1, giving `a C^n |F|_((q_X+5)n+1)`. Collision configurations contribute zero.

For the Taylor factorial, an all-n exact argument avoids asymptotics: for m=5n, `m!^2=product_(j=1)^m j(m+1-j)>=m^m>=(2n)^(5n)`, since `j(m+1-j)-m=(j-1)(m-j)>=0`. Thus the printed G2 constant is indeed sufficient for every n, not merely n<=100.

When **Z=1, q_X=4**, the two orders are bounded by 10n+1, which is <=11n. Also `C^n<=exp(C)n!`, directly from one term of the exponential series. Hence `s=11, beta=b0+1` is valid. If the missing total-cumulance hypotheses actually establish b0=p+2, the stated **beta=p+3** follows. Ordered partitions obey `sum_pi |pi|! <= 2^(n-1)n!`: sum over compositions of n and bound each `n!/(k_1!...k_b!)` by n!. The subsequent moment partition sum costs at most another n!. These combinatorial counts do not supply the missing probabilistic bounds.

For **general Z**, GROW silently drops its own region-III seminorm. A safe corrected order is

`N_n=max(10n,(q_X+5)n+1)`, **`s=max(11,q_X+6)`**

using integer upper bounds for derivative orders. A counterexample to the assertion that X0 and SEP-pt alone give s=11: on the lattice take independent fair signs epsilon_x and the local centred field `X_a(x)=a^(-q)(epsilon_x+epsilon_(x+a e_1))/2`, with e_1 spatial and **q=14**. Then |X_a|<=a^(-14), and products at pairwise distances >=2a have zero expectations: their underlying signs are disjoint. Thus SEP-pt holds at every order with c_*=2. But `Cov(X_a(x),X_a(x+a e_1))=a^(-28)/4`. Take `F_a(x,y)=a^N phi(x) psi((y-x)/a-e_1)` with nonnegative bumps, psi(0)>0 and support radius <1/4. Each F_a is compactly supported off the diagonal, with |F_a|_N uniformly bounded. Its two-point value scales as `a^(N+4-28)`: **a^(-3) for N=21**, and **a^(-2) for N=22=11*2**. The claimed uniform bounds fail. This is a counterexample to the analytic implication from the two estimates, not a Wilson configuration model. The safe formula gives **s=20** at q_X=14. Restricting GROW explicitly to Z=1 repairs the lane's intended use.

Finally, E(a) remains a substantive GAP, not a missing citation. Conditional centring does not remove singleton conditional means (F7). Nor does a low-order large-field path bound control all moments: with independent bad-cube probability 1/1024 and bad weight 2, a path of length ell has eleventh moment at least `(1/1024)^ell 2^(11ell)=2^ell`. With good weight 1/12800 the quoted smallness expression is exactly `80(4/1024+1/12800)=51/160<1`; it still does not yield a volume-uniform eleventh moment. A spatially constant coarse sign also has bounded coarse observables but covariance one at every separation, defeating an asserted decaying large-distance weight. These independent examples explain why the repaired capped weight and all-order/singleton estimates are actual extra hypotheses.

### F9 — literature match is confirmed; the Wightman theorem is still an import

**CONFIRMED against the named open sources; NOT-VERIFIED against the primary OS II text in this session. Claim: CONDITIONAL imported reconstruction for one Hermitian scalar.** Attachments: `OSLEAF55.md:95–113`, `:205–231` and `:261–265`.

[Kravchuk–Qiao–Rychkov, arXiv:2104.02090v2, §9.2.2, (9.16)–(9.18)](https://arxiv.org/html/2104.02090v2#S9.SS2.SSS2) gives exactly the flat-Schwartz domain, order sn, and constants bounded by alpha(n!)^beta. The paragraph after (9.18) distinguishes analytic continuation from the additional all-n growth estimate needed for tempered boundary values. Its stronger separately smeared condition (9.19) is on the **full** Schwartz space; it cannot itself be invoked for the contact-free products here. TP/EXT must do that job independently. [Adamo–Moriwaki–Tanimoto, §2.5, (21) and (23)](https://arxiv.org/html/2407.18222v2#S2.SS5) confirms the exact radial seminorm used by D1 and the same growth condition. Thus s=11,beta=p+3, under F8's hypotheses, matches the actual open-source statement.

Direct requests to the [OS I primary PDF](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-2/Axioms-for-Euclidean-Greens-functions/cmp/1103858969.pdf) and [OS II primary PDF](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-42/issue-3/Axioms-for-Euclidean-Greens-functions-II-with-an-Appendix-by/cmp/1103899050.pdf) returned an iframe/security resource, not readable theorem text. I therefore do not upgrade [m-sec] to primary verification. REC(a)–(d) have been independently rebuilt above; the multivariable analytic continuation and tempered-boundary theorem in (e) have not been re-proved here. Multiple/tensor-field reconstruction remains outside this checked import, as the target correctly says. No clustering or unique-vacuum claim is banked.

### F10 — EXT is sufficient; its shell argument needs small domain clarifications

**CONFIRMED as a sufficient implication with the clarifications below; REFUTED as a necessary-and-sufficient claim by F1. Claim: CONDITIONAL.** Attachments: `OSLEAF55.md:371–440` (W/EXT), E5 at `:780–784`.

Pin the symbols: r_n is the derivative order at insertion number n; r in the linear-growth hypothesis is its slope. The proof's local abbreviation `r:=r_n` at line 421 must not be substituted for the slope in beta'=b+7r+1. Likewise p_n is the scale-singularity exponent, not GROW's factorial-growth exponent p. Take integer upper bounds for derivative/Taylor orders, and an integer q_X>=4 (which may always weaken X0 on 0<a<=1), before evaluating the displayed formulas.

Independent reconstruction: subdivide space into side-2 cubes, and use collision cutoffs at dyadic scales lambda_k. Derivatives of the shell cutoff up to order r_n cost at most `C^n C^(r_n) n^(2r_n) (r_n!)^3 lambda_k^(-r_n)`; cube derivatives add `(r_n!)^2`. Taylor order p_n+1 on the flat test leaves a shell factor lambda_k after X1's lambda_k^(-p_n) is applied. A 5n Schwartz weight sums the cube centres, independently of their placement. Thus the shells are summable in k and in the centres. The remaining region has separation O(a), and X0 combined with Taylor order q_X n+1 gives `a C^n |F|_((q_X+5)n+1)`. It vanishes for each fixed test. E5 correctly handles the complementary finite range a>=1/(4c_*), using X0 directly.

For r_n<=rn, the n-growth is `n^(2rn) ((rn)!)^5 <= C^n (n!)^(7r)`; the Taylor coefficients of order proportional to n cost at most C^n. Absorb C^n into one further factorial as in F8. Hence the sufficient parameters **s'=max(r+p+7,q_X+6), beta'=b+7r+1** are valid for the integer majorants just specified. The source's Taylor/cube constants are generous enough; no additional factorial exponent is needed.

Two scope details must be stated. First, the support of a cutoff which is flat at delta=lambda includes its boundary, whereas X1 asks for compact support in the strict shell. Approximate these pieces from inside the strict shell in C^infinity; their flatness at its boundary gives convergence in the finite seminorm, and each fixed-a lattice functional is continuous. The bound then passes with the same constant. This repairs the literal domain assertion at line 421 without using contact values. Second, for finite R the original D8 lattice functional is defined only on tests whose supports fit in the chart. The bankable convergence assertion is convergence on all compact admissible flat tests, followed by the unique continuous extension of the **limit** to the full flat Schwartz space when R_j grows. It is not convergence of undefined finite-R evaluations on arbitrary noncompact tests.

### F11 — TP is sound; the printed BRIDGE(i) loses its boundary domain

**CONFIRMED for Lemma TP and DET-SP. NOT-VERIFIED for BRIDGE(i) on every X1 cube as printed; its asserted application of SP to every displayed factor is REFUTED. CONFIRMED for the sufficient bridge on the interior supports actually needed for H_reg. Claim: CONDITIONAL.** Attachments: `OSLEAF55.md:830–880`.

Independent TP calculation: at scale mu=lambda/16 a nonzero localisation piece has centres separated by more than `lambda-4mu=3lambda/4`. Enlarging their support cubes to half-side 2mu removes at most another 8mu, leaving separation >lambda/4. There are at most `(35/lambda)^(4n)` relevant centre tuples. Fourier-expand on boxes of period 4mu, and multiply each one-point Fourier factor by a bump equal to one on the inner box. Integration by parts to order `M=(r+4)n+2` gives decay `(1+|k|_infty)^(-M)` with cost `C^n C^M(M!)^2 ||G||_(lambda,M)`. The r-derivative factor norms cost at most `C^n (2 sqrt(n))^(rn)(1+|k|_infty)^(rn)`. The frequency sum is <=`2^(4n+1)`. Finally `(M!)^2<=C^n(n!)^(2r+8)` and `n^(rn/2)<=C^n(n!)^(r/2)`. This yields precisely the sufficient TP exponent **5r/2+8** and the factor **lambda^(-4n)**. For each fixed n the series converges with every derivative on a fixed compact support, hence in Schwartz topology. Cutting general flat tests off from infinity and the diagonals proves DET-SP.

But SP only allows factors supported in a side-2 cube **inside B_(R/4)**. TP's enlarged factors need not stay there. An explicit geometry: R=32, lambda=1/2, mu=1/32, and `Q_1=[2-mu/8,4-mu/8]^4`, which lies strictly in B_8. Put a nonnegative bump near `x_1=(4-mu/4,...,4-mu/4)` and a second bump about one unit inward, so their pair separation lies in (lambda,4lambda). The relevant mu-grid centre `c_1=(4,4,4,4)` occurs in TP. Its factor h is nonzero at `c_1+(mu/2,...,mu/2)`, a point of radius **8+mu>8**. The k=0 coefficient is nonzero for such nonnegative product bumps. Thus this is an actual factor in the displayed sum to which SP, as stated, cannot be applied. TP itself never promised to preserve Q_i or B_(R/4).

For the actual H_reg application, `supp G subset (B_(R/8))^n` supplies the missing margin. Every enlarged factor lies within distance `6mu<=3/8` of an insertion point in supp G, and its containing side-2 cube fits inside B_(R/4) for R>=32. Then the displayed argument applies unchanged. It gives `p_X=p+4`, `r_X=r+6`, `b_X=b+5r/2+8`, `c_*=4c_SP` **on those interior tests**. Composing with EXT yields exactly **s=max(p+r+17,q_X+6), beta=b+19r/2+51**. No claim that global X1 follows for every boundary-touching cube is needed for this repaired sufficient route. A proof of that stronger implication would need a separate boundary-preserving expansion.

### F12 — closure, sphere contraction, and the contact-free positivity bridge

**CONFIRMED as implications on the stated domains; NOT-VERIFIED for their actual Yang–Mills analytic inputs. Claim: CONDITIONAL.** Attachments: `OSLEAF55.md:292–368` (RP-lat, CLOSURE-sep, CONTRACT-sep), E2/E7/E8/E9 at `:767–795`, BRIDGE(iii)–(v) at `:865–880` and E10 at `:917–919`.

Re-derive site RP on the even tori used in the continuum sequence: cut at the two time-site planes. Boundary spatial links are shared and fixed by reflection; interior positive and negative links are disjoint, and every plaquette belongs to one half or a fixed plane. Splitting the boundary action equally gives `S_W=S_++Theta S_+`. Conditional on boundary links, the two Haar integrals are reflected copies, so `Z omega(conj(Theta A) A)=integral dU_boundary |integral dU_+ A exp(-S_+)|^2`. The clover's time-coordinate extent is at most a; for a small enough relative to the positive support gap, A_F is an admissible half observable. Variable relabelling gives the claimed lattice RP form exactly. No contact extension is invoked.

Uniform H_reg bounds make each fixed test coordinate bounded. Extract a diagonal subsequence on D. Approximation in |.|_(sn) makes the values on every compact flat test Cauchy, and density extends the limit uniquely to ^0S with the same bound. For a finite sequence F in the compact ordered half, its entire RP quadratic form passes to the limit term by term; approximation of each component in Schwartz topology then proves positivity on all of A_+. Permutation symmetry, reality and normalisation pass in the same finite-sum way. Group invariance first passes for every tested **observable/group pair**, then by continuity in the test and in the group. Separate one-to-one enumerations of observables and group elements would not suffice.

At fixed R, E2 restricts this result to functions supported in `(closed B_(R/8))^n`; no global ^0S state or full translation/rotation action follows there. BRIDGE's later phrase "R_j equiv R" must inherit exactly this restriction. The global bankable statement uses **R_j -> infinity**. This is a substantive domain qualification, not an infinite-volume theorem at fixed radius.

For CONTRACT-sep, assume exactly the stated U-sep, all-order K-inv and pole RP. A sphere boost with parameter e/(2R^2) converges, with every derivative on fixed compact sets, to translation by e. Its test transports preserve separation and converge in the needed seminorm. Subtract the exact Killing identity and apply the **R-uniform** U-sep bound: the limiting translation defect is zero. Pole rotations act linearly, and the assumed reflection symmetry supplies improper rotations as in E7. Passing RP through the ordered compact tests and then density is the same argument. The Ward estimates used to establish K-inv at each fixed R may have R-dependent constants; U-sep itself may not. This independently proves the contraction implication. The sphere's finite-cutoff RP and the Killing/Ward estimates were not re-established from their unread producer files here.

Finally, contact distributions do disappear on this exact domain. If a tempered T is supported on Delta, approximate any flat F by compact tests F_j supported off Delta (F5). Then T(F_j)=0 and continuity gives T(F)=0. This directly proves the E10 conclusion without importing a structure theorem. Hence the nonconstant h(x)delta(x-y) and white-noise examples in SEAM F9 change neither S nor any admitted RP form. DET-SP and continuity similarly extend separated-product invariance to A. They do **not** provide ordinary contact moments, and they do not prove nontriviality. With unconditional SP, the interior repair in F11, exact lattice RP, and all-order symmetry convergence, the contact-free positivity bridge is a valid conditional construction.

### F13 — TRAJ arithmetic is sound; several advertised conflicts need narrower verdicts

**CONFIRMED for the following arithmetic conditional on F-tune's inputs; REFUTED for the missing 2N dictionary (F3), the strict gamma ordering, and the unconditional range-conflict inference. Remaining producer matches are NOT-VERIFIED where their files were not read. Claim: CONDITIONAL; actual common trajectory OPEN.** Attachments: `OSLEAF55.md:532–609`; actual F-tune `FLOW.md:420–455`.

In FLOW units, `g_ref<=g_1=(gamma^(-2)+R_F)^(-1/2)` gives **`u_K-R_F>=gamma^(-2)>0`** exactly, including the endpoint g_ref=g_1. This is not an extra assumption. Write A=u_K-R_F and B=beta_- log L>0. The lower flow bracket gives `g_j^q<=(A+B(K-j))^(-q/2)`. Summing a decreasing positive function and integrating its tail proves

`sum_(j=0)^K g_j^q <= A^(-q/2)+2 A^(1-q/2)/(B(q-2))`, q>2,

which is the displayed envelope with g_*=A^(-1/2). The upper bracket supplies FS's lower bound on g_bare^4. No comparison with geometric R is involved: R_F is the additive flow error, whereas the torus R is a length.

The shooting construction is defined for integer K with a=L^(-K), and its smallest-root choice exists inside the first admissible interval: sufficiently small g_0 are admissible, u_K tends to infinity at zero, and at first exit u_K<=gamma^(-2)+R_F. Continuity gives a root; roots below one such admissible root form a closed set bounded away from zero. This proves the selection **given** SF-cont and the flow inputs. It does not prove those inputs or continuous dependence of that smallest-root selector on a or g_ref. Off the L-adic set, this particular theorem supplies no trajectory; that is not a nonexistence theorem for other constructions.

| Conflict | Independent disposition and required precision |
|---|---|
| C-T1 | **REFUTED as an unconditional range mismatch.** `SRCCD55.md:319–320` really assumes `g_ref<=min(g_thr,gamma_0)`. A missing interval exists only if **min(g_thr,gamma_0)>g_1**. If g_thr<=g_1, the old range already suffices. Also `OSLEAF55.md:584` prints gamma_0>gamma: only **gamma_0>=gamma>=g_1** follows. Replacing by a sink explicitly below the newly computed g_1 is sufficient. The actual g_thr/sink values were not independently read. |
| C-T2 | **CONFIRMED as algebra of the quoted extra condition; source theorem NOT-VERIFIED.** A sufficient ceiling is `gamma_FI=[max{2R_F,2/min(1,kappa)}+R_F+(3/2)beta_0' log L]^(-1/2)`. It is fixed before g_1. Merely reusing a prior numerical sink after shrinking gamma would be a stale-minimum error. Recompute the sink against the new g_1 and any C-T5 ceiling; this has not been certified from SMALLNESS_DAG. |
| C-T3 | **CONFIRMED distinction; actual selection OPEN.** Fixed-point existence does not imply the continuous selection needed by SF-cont. A-Lip is sufficient, not necessary. For instance Phi_t(x)=x has many fixed points and the continuous selection x(t)=0 without a strict contraction. The target's parenthetical "a sufficient condition" is the correct reading of its earlier word "require". |
| C-T4 | **CONFIRMED restricted scope, not an automatic contradiction.** `FLOW.md:134–144` fixes one kappa; `SRCCD55.md:316` permits a sequence in an interval. A constant sequence is allowed by the latter. Existing FLOW results do not automatically cover arbitrary varying sequences. Fix one common kappa or prove the extra uniformity. TR-2 also writes the step stiffness with u_k^ker, then names a fixed point in u_(k+1)^ker; without the FI-1 producer, this index map is NOT-VERIFIED. |
| C-T5 | **CONFIRMED sufficient arithmetic only.** If the actual producer gives q_j<=2 C_b gamma^4/rho, then gamma^4<rho/(2C_b) implies q_j<1. That upper bound does not prove necessity of the ceiling. The source estimate was not independently read. |
| C-T6 | **CONFIRMED domain issue.** A function on L^(-N) does not specify a function on every [a,2a]. An extension is required; interpolation does not prove a local line-of-constant-physics/Ward estimate. The sphere profile also needs F3's factor-2N correction. |
| C-T7 | **CONFIRMED need for a matching theorem.** Solving a Ward ODE with one prescribed base value does not establish matching to the flat RG trajectory at other spacings. The LCS-a/LCS-b producer estimates are NOT-VERIFIED here. Do not infer that two candidates must have unequal values; their equality is unproved. |
| C-T8 | **CONFIRMED odd/even and index issues, but incomplete.** `PROOF.md:799–803` has L^(M+K) sites per side, odd for odd L, while the reviewed sparse-link and two-site-plane proofs use even counts. This is a mismatch of those proofs, not a refutation of all odd-torus RP. R in 2ℕ repairs parity. The coupling indices run oppositely, but the additional sqrt(2N) conversion in F3 is still required. |

TR-8's off-fixed-point source estimates and the claimed Stage-7 sink were not independently established. These are actual missing producer checks, not reasons to infer a false match. The phrase "every input checked" in §6 cannot be inherited wholesale from a list of citations.

### F14 — disposition of the seven REFUTED parts counted by E11

The following table distinguishes the mathematical negative finding from verification of an unread original quotation. Attachments are the current locating strings in OSLEAF; no earlier file's review label is used as proof.

| Target item | Review verdict and exact scope |
|---|---|
| V1, `OSLEAF55.md:612` (F2a bookkeeping) | **CONFIRMED refutation.** For nonzero positive-time f, `(theta f) tensor (theta f) tensor f tensor f` is not flat on same-half collisions. Changing to A_+ changes the domain and needs F12's RP limit/density proof; it is not bookkeeping. The original ASSEMBLY55 quotation was not independently inspected. |
| V4a, `:623` (pointwise necessity) | **CONFIRMED refutation of necessity from OS0 alone.** A distribution such as point evaluation at a separated configuration is continuous on ^0S but need not be an ordinary pointwise kernel. Smeared bounds can supply regularity. The proposed replacement "X1 is necessary and sufficient" is overclaimed, as F1 shows. This does not assert that a nonanalytic example satisfies all other OS axioms. |
| V7b, `:632–634` (extra g_ref condition) | **CONFIRMED refutation within the matched FLOW convention.** g_ref<=g_1 already gives u_K-R_F>=gamma^(-2)>0. Consumers using a weaker range still need a comparison; physical-coupling consumers need F3's conversion. |
| V7c, `:635–636` (item-6 versus item-3 citation) | **NOT-VERIFIED.** CODEX_REVIEW_SRCAN was not read under the file cap. A quotation in OSLEAF cannot independently establish which numbered item currently contains that statement. No PASS on this citation is issued. |
| V10, `:641–642` (ordinary-moment H_reg) | **CONFIRMED only with FS's actual three hypotheses:** bounded normalised variance, nonzero normalised separated covariance, and an unconditional upper bound for unnormalised separated covariance on the F-tune trajectory. Without those qualifications ordinary-moment bounds can be vacuous. HANDOFF's original wording was not read. |
| V16, `:655–656` (declaring G-np sufficient) | **CONFIRMED mathematical insufficiency.** A label gives neither off-grid values nor the local-profile matching/Ward theorem. F3 adds the missing normalisation conversion. Original ASSEMBLY55 wording not independently inspected. |
| V20, `:906` (unquantified U-sep sufficient) | **CONFIRMED mathematical insufficiency.** Let a_j=exp(-j), delta_j=1/j, and a two-point kernel of height a_j^(-8) live in a shell delta_j<|x-y|<2delta_j. Every fixed separated compact test eventually sees zero. A fixed compact test flat at x=y with factor exp(-1/|x-y|) sees a contribution at least c a_j^(-7) j^(-4), which diverges. Thus fixed-separation convergence does not imply the required extension bound. This is a test-space counterexample, not a Wilson model. Original SEAM55 H2 was not read; SEAM's review and OSLEAF's displayed version were inspected. |

Consequently the target's count "REFUTED 7" is not seven independently verified original-source dispositions in this review. Six mathematical negative parts survive with the qualifications above; one citation correction remains NOT-VERIFIED. The attached sufficient replacement also requires F1/F3/F7/F8/F11 repairs.

### F15 — ol55_1: independent exact check and gate discrimination

**CONFIRMED for the scoped counts, factorial inequality, toy reflection identity and toy RP; REFUTED as a sharp-maximum certificate (F2). NOT-VERIFIED for reproduction of the archived 200-sample execution or its registration chronology. Claim: PROVEN for the exact identities below, not a Yang–Mills estimate.** Attachments: `checks/ol55_1_criteria.md` G1–G3 and controls; `checks/ol55_1_conventions.py:32–34,49,99–168`; `checks/ol55_1_out.txt`; `OSLEAF55.md:664–670`.

Executed in this review: short plain-Python calculations using only integer and Fraction arithmetic, with bytecode writing disabled. No NumPy, floating-point sampling, quadrature, long job or additional output file was used. The archived script/output were inspected; its 200 random samples were not rerun. Instead, an independent Markov-transition calculation checked **all 64 entries** of the 8-by-8 Gram matrix for the eight positive-time monomials. It agreed exactly with `M diag(1/3,1/3,1/3) M^T`, proving positivity for **every complex coefficient vector**, not only sampled ones. The row order and exact M are:

| Positive times | M row = conditional expectation given time-zero state |
|---|---|
| empty | (1,1,1) |
| (1) | (1/4,0,-1/4) |
| (2) | (1/16,0,-1/16) |
| (3) | (1/64,0,-1/64) |
| (1,2) | (3/16,1/8,3/16) |
| (1,3) | (3/64,1/32,3/64) |
| (2,3) | (11/64,5/32,11/64) |
| (1,2,3) | (3/64,0,-3/64) |

The independently computed cyclic-chain value is **-1/3**. Dropping conjugation for F_0=i changes the value from **1 to -1**. Dropping reflection for the time-1 field changes **1/24 to 2/3**. Thus those convention/positivity checks can fail. Order reversal is different: permutation symmetry of scalar moments makes reversal invisible in the complete sum. G3 cannot distinguish a missing reversal; the target itself notes its irrelevance for lattice moments at line 304. It is not evidence for a noncommuting or tensor-field convention.

The dimension counts were independently re-derived as `4 binom(d,2)`, giving 24 in d=4 and 12 in d=3. The doubling to 48 is a convention, not an independent gate. The subsequent "max" clause is arithmetically forced by those counts and the inserted bound 2; it cannot discover F2's SU(3) sharpness issue. G2 was re-evaluated exactly for n=1,...,100 and all inequalities held; its false control already fails at n=1, **32>4**. F8 supplies the independent all-n proof. These checks establish no continuum estimate, source hierarchy, symmetry restoration, or trajectory matching.

## Scope receipt and citation audit

The only written path is this deliverable. No git command was run; no .git, snapshot or audit ledger was read. Required methodology was read from SCIENCE_WORKFLOW; the two discretionary local sources were the applicable repository review-loop skill and FLOW.md. Other local reads were the explicitly named target, PROOF ranges, SRCCD55, CODEX_REVIEW_SRCCD, CODEX_REVIEW_ASSEMBLY, CODEX_REVIEW_SEAM, and the named ol55_1 check's criteria/code/output. All scientific source reads used string search and bounded ranges. References to other lane files in this report identify unverified producers, not secretly inspected evidence.

OSLEAF's final locating strings were rechecked against the same displayed lines during review. It contains no numeric `PROOF.md l.NNNN` citation requiring an offset correction; its S1/S3 references currently locate at PROOF lines 799–804 and its T_OS statement at 773–774. The index issue is real; the missed 2N normalisation issue is more serious than line drift. The target's E1 explains the quotation edits; I did not attempt to reconstruct the prior quotation lengths. No direct literature sentence is quoted here.

Last verification clock: **2026-10-29 05:53:35 UTC**. Review complete within the stated source cap; the explicitly named NOT-VERIFIED producer checks remain unresolved.

## Summary table

| Finding | Review verdict | Claim status / bankable boundary |
|---|---|---|
| F1 MIN | REFUTED global-necessity inference; CONFIRMED local Banach–Steinhaus step | PROVEN local equicontinuity; global necessity GAP |
| F2 clover 24 | REFUTED as universal sharp value; CONFIRMED upper bound | PROVEN <=24; SU(3) sharp value 18 |
| F3 coupling dictionary | REFUTED | GAP; replace equality by g_std=sqrt(2N)g_FLOW |
| F4 FS | CONFIRMED conditional obstruction | CONDITIONAL on its raw separated bound and F-tune trajectory |
| F5 domain/P/DENSE/ACT | CONFIRMED | PROVEN partial OS test-space construction; no ordinary positive Euclidean state |
| F6 REC(a)–(d) | REFUTED printed weight factor; CONFIRMED after correction | PROVEN implication with 1+m u^2 |
| F7 conditional SP | REFUTED for higher cumulants alone | GAP until conditional singleton bounds are included |
| F8 GROW | CONFIRMED for Z=1+SEP-pt; REFUTED unrestricted-q_X two-bound inference | CONDITIONAL s=11,beta=p+3; actual E(a) OPEN |
| F9 OS II | CONFIRMED open-source match; NOT-VERIFIED primary text/full imported proof | CONDITIONAL one-scalar reconstruction import |
| F10 EXT | CONFIRMED sufficient route with integer orders/domain clarification | CONDITIONAL; no global-minimality theorem |
| F11 TP/BRIDGE | CONFIRMED TP/density/interior bridge; REFUTED unrestricted factor-domain application | CONDITIONAL interior sufficiency; boundary-wide X1 inference NOT-VERIFIED |
| F12 closure/contraction | CONFIRMED implications; NOT-VERIFIED actual producer inputs | CONDITIONAL globally for growing R; fixed-R result local |
| F13 TRAJ | CONFIRMED u_K-R_F and envelope; REFUTED dictionary/strict ordering/unconditional C-T1 inference | CONDITIONAL; common actual trajectory OPEN |
| F14 seven dispositions | CONFIRMED six scoped mathematical negatives; NOT-VERIFIED citation-only V7c | No blanket inherited count or original-source PASS |
| F15 ol55_1 | CONFIRMED exact identities; REFUTED sharp-max interpretation; NOT-VERIFIED archived run receipt | PROVEN toy Gram certificate, no YM estimate |

## Corrections to quantities and quantifiers

- Coupling equality: **g_PROOF=sqrt(2N)g_FLOW**, not equality. At N=3 the coupling factor is sqrt(6), the action-coefficient factor at equal numerical couplings is 6, and the transported variance coefficient is c_v/41472 rather than c_v/1152 (general coefficient c_v/(4608N^2)).
- Sphere profile: with FLOW's u_traj, **beta_Q=u_traj** at the base point; keeping beta_Q=2N/G_std^2 requires **G_std^(-2)=u_traj/(2N)**.
- Sharp clover value: **18 for SU(3)**, while **24 remains a valid universal upper bound**; the counts 24 and 48 are unchanged.
- Translation weight: **1+m u^2**, not 1+u^2. The printed scalar inequality gives the false comparison **5<=4** for m=4,u=1,y=0.
- General-normalisation growth: replace an unconditional **s=11** by the safe **s=max(11,q_X+6)** (s=20 at q_X=14), or explicitly restrict to Z=1. The intended Z=1 match s=11,beta=p+3 survives.
- Conditional cumulants: the bound must cover **order 1 as well as orders >=2**. The omitted term can produce **a^(-8)** even when every higher conditional cumulant is zero.
- C-T1: **gamma_0>=gamma>=g_1**, and a genuine old-range gap requires **min(g_thr,gamma_0)>g_1**. Recompute g_sink after all new gamma ceilings.
- MIN yields **C_(n,K),N_(n,K)**, not one geometry-independent X1 bound. TP's expanded factors require the spatial margin; fixed-R closure remains on its local test space.

**Single most dangerous unverified item:** an actual unconditional, all-insertion-order SP_lambda (or SEP-pt) estimate for the same correctly normalised Wilson trajectory, uniform in cutoff and radius and in separation down to c*a, including conditional singleton and all-order large-field product control. This is the quantitative input that makes the repaired positivity-compatible bridge usable. It has not been proved by this review, by the toy check, or by the cited total-cumulance argument.

## Exactly what may be banked

1. **PROVEN:** the flat Schwartz domain, partial products used in RP, Lemma P, compact/ordered density, scalar Euclidean action, and separated-product density/uniqueness. Contact-supported tempered distributions vanish on this domain.
2. **PROVEN implication:** REC(a)–(d), using the corrected insertion-number translation factor; even-site-torus lattice RP and passage of RP, symmetry and continuity to the restricted limit. For fixed radius the conclusion is local; a global result requires radii tending to infinity.
3. **PROVEN implication:** EXT sufficiency and the interior version of SP -> TP -> EXT -> CLOSURE, with the stated integer-order convention. The sufficient exponents `s=max(p+r+17,q_X+6)` and `beta=b+19r/2+51` survive. CONTRACT-sep is valid conditional on its U-sep/K-inv/pole-RP inputs. Global minimality of X1 is not banked.
4. **PROVEN implication:** for Z=1 and an actual unconditional SEP-pt estimate, GROW gives s=11,beta=b0+1; if b0=p+2 is separately established, beta=p+3. This matches the open-source OS II growth condition. The primary theorem remains an explicitly identified one-scalar import, not a new proof or a verified Yang–Mills application.
5. **PROVEN conditional arithmetic:** in FLOW units, g_ref<=g_1 gives u_K-R_F>=gamma^(-2)>0, the displayed summability envelope and the L-adic tuning selection. Conversion to PROOF/sphere units requires sqrt(2N). FS's torus incompatibility holds with its actual three hypotheses and the corrected coupling dictionary.
6. **PROVEN exact checks:** the 24/48 clover counts, universal upper bound 24 (SU(3) sharp value 18), the all-n Taylor factorial inequality, and the toy chain's all-coefficient Gram factorisation and explicit negative controls. **No unconditional continuum Yang–Mills construction, nontriviality/non-freeness, all-order source estimate, or sphere/flat trajectory identification is banked.**

