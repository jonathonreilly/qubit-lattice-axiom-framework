# PRE-STATED hostile review of COFUN.md

Recorded UTC: 2026-10-28 22:03:10 UTC.

Written before inspecting the target or deriving its mathematics. Review only; no git commands, source edits, audit-ledger access, snapshots, or long numerical jobs. The only writable file is this deliverable. Findings use CONFIRMED / NOT-VERIFIED / REFUTED; claim assessments use PROVEN / ARGUED / CONDITIONAL / GAP / OPEN.

## Targets and advance refutation criteria

1. Rebuild CO-pin on its exact composite-co-closed domain. Refutation: an admissible current and gauge parameter with nonzero pairing, an adjoint/domain mismatch, or a conclusion about minimization that does not follow from vanishing.
2. Test the obstruction relocation and the alleged second independent growth route. Refutation: a retained blockwise condition, a change of class or normalization, dependence on the same witness/estimate, or incompatible growth factors.
3. Resolve session-9/session-10 staleness and the three CO-fun classes. Refutation: the quoted clauses are absent, the classes coincide, or the decision selects a stronger class than alleged.
4. Check BFT_B line claims and symbol identities using fresh string matches. Refutation: mismatched objects, stale citations, or a bound evaluated at a parameter no longer fixed.
5. Rebuild both sharp operator norms with exact arithmetic and attack the universal assertion about the level factor. Refutation: a row/column sum or extremizer disagrees, or an admissible scale-dependent/canceling family avoids the asserted factor.
6. Inspect every cf1 gate and the failed registration/control/provenance disclosures. Refutation: a gate is tautological, impossible, underpowered for its claimed conclusion, or a reported run cannot be supported by its output.

Success is a concrete counterexample, corrected exact computation, or a fully reconstructed implication on the stated domain. A source label, repeated expected value, finite numerical agreement, or absence of a counterexample does not establish a theorem. Unavailable definitions or source citations remain NOT-VERIFIED.

## Access record

Named sources: COFUN.md; checks/cf1_*; only S10-6, S10-11, RS10-1, RS10-6 in REVIEW_BFT_B_S9_S10.md; only bounded BFT_B.md ranges located from the authorized strings. Two additional files are the required methodology and review procedure: docs/ai_methodology/SCIENCE_WORKFLOW.md and docs/ai_methodology/skills/review-loop/SKILL.md. No other scientific files will be opened. PROOF.md cross-citations cannot be verified within this allocation and will be marked accordingly.

## Findings (appended as established)

### F1 — CO-pin's restricted cancellation is valid; it does not supply the pinned estimate

**Verdict: CONFIRMED** for the cancellation and conditional norm inequality in COFUN.md:389-400. **Claim status: PROVEN** on the specified gauge space, with the norm conclusion **CONDITIONAL** on YH-pin. This is not confirmation of the advertised relocation.

Reconstruction: write E_l for restriction to level-l roots. Root covariance is Q_l d = d E_l: on a gradient, each path integral telescopes to its endpoint values; subtracting the two root-to-endpoint funnels from the straight block average leaves the difference of the two root values. Iteration and transposition give d*(Q^(0→l))^T = E_l^T d*. Thus, for the plain-current source, d*C(j) = sum_l E_l^T d*j_l. Divergence-form slots contribute zero since d*d* = 0. Residual slots annihilate the allowed chain gauge directions by the defining residual covariance. Consequently, on the allowed gauge space, <C(j),dλ> = <S,Ξλ> = 0. Equivalently, when using the target's identity d*C(j)=D(S), root support and total neutrality give <D(S),λ>=c sum_X D(S)(c_X)=0. The first argument only needs equality of the functionals on Λ_0; it does not promote restricted annihilation to pointwise zero divergence for another source slot.

In finite dimension, dΛ_0 is a closed subspace, so the ℓ¹ distance to it is attained. Taking its infimum gives n²|<C,Y>| ≤ n²||C||∞ N_Λ(Y). With π_0(C)=n³||C||∞ and N_Λ(Y)≤C_pin n, the factors multiply to n² n^-3 n=1. The unit conversion is correct. BFT_B.md:3961 fixes Λ_0 as functions with a common value at all level-k roots; it does not mean arbitrary root values or separate constants per root/block.

### F2 — The new “independent blow-up route” is the old defect estimated by another norm

**Verdict: REFUTED** for the independence and common falsity verdict asserted at COFUN.md:438-445, 572. **Claim status: GAP** for a refutation of (CO-fun)[cc].

Let A(j)=sum_l (Q_str^(0→l))^T ĵ_l and B(D)=sum_i (Q_str^(0→i))^T h_i^T R_(i+1)D. The exact identity at BFT_B.md:4045 is C=A-B. Moving the operators across the pairing gives, without estimates,

    <B(D),Y> = sum_i <R_(i+1)D, h_i Q_str^(0→i)Y>
              = <D, sum_i E_(i+1→k) h_i Q_str^(0→i)Y>
              = <D, Φ_k Y>.

This is precisely BFT_B.md:4118-4120's tent term. COFUN estimates the norm of the same B; COF-res pairs it against Y. They are not independent mechanisms. The exponent 3k-3 versus 2k-3 records an additional factor n in the upper estimate, not a second lower bound on curvature.

Moreover X≤U with U unbounded proves no blow-up of X, and an unbounded term in a signed decomposition proves no blow-up of its sum. COFUN.md:447-460 explicitly admits both defects, yet retains “FALSE”, “refuted”, and “not an open item” at 155, 501-502, 589-590. The correction is: the supplied refutation is NOT-VERIFIED; the full estimate remains OPEN in this reviewed packet. This does not prove the estimate true. S10-11 at REVIEW_BFT_B_S9_S10.md:589-593 repeats the term-level argument and supplies no cancellation exclusion. There is an earlier issue too: neutrality forces a dipole contribution n²q[Φ_k(Y)(c_Y)−Φ_k(Y)(c_X)], not an independently selectable single-root term n²qΦ_k(Y)(c_X). A nonzero single coefficient does not prove a lower bound on that difference. The claimed response-specific asymptotic L^(2k−3) is itself NOT-VERIFIED within the allowed sources.

### F3 — “One linear constraint” is actually T^4−1 independent root constraints

**Verdict: REFUTED. Claim status: GAP** for using YH-pin as an already harmless replacement. Attaches to COFUN.md:417-422, 462-468, 571, 625.

There are R=T^4 level-k roots in d=4. Fix one root c_0. Requiring λ(c_X)=λ(c_0) at every other root imposes R−1 independent scalar constraints: root values can be assigned independently by one-site functions. Thus the corrected count is **T^4−1**, already **624 at T=5**, per Lie-algebra component; for su(N) it is (T^4−1)(N²−1) real constraints. Quotienting by global constants does not remove these differences.

The source's own inequality N_Λ≥N supplies no upper bound on N_Λ. For an explicit separation, take an arbitrary field Y=da with a=A at one root and 0 at another. Then N(Y)=0 by λ=−a, but every λ∈Λ_0 leaves a root-to-root path integral of magnitude |A|, so N_Λ(Y)≥|A|. This is a counterexample to transferring the unrestricted norm bound by gauge invariance alone, not a counterexample to YH-pin for actual plaquette responses. That response-specific estimate is OPEN. CO-pin therefore does not establish that the gauge-side obstruction has disappeared or that RS10-6 is discharged.

### F4 — The root-norm obstruction is real, but its quoted inequality is reversed

**Verdict: CONFIRMED** that ROOT-sup fails for the source-norm ball; **REFUTED** for the comparison at COFUN.md:440-441. **Claim status: PROVEN** for the following explicit root-norm counterexample, not for curvature blow-up.

Take k≥2, T≥5 and a single current j_(k−1) carrying amplitude q along the L consecutive level-(k−1) edges joining two adjacent level-k roots. Put all other j, G, s and B_k equal to zero. Interior vertices have one incoming and one outgoing q, so the only divergence is the neutral endpoint dipole ±q. This is an admissible (cc) source, not (CC-0). Exactly,

    max|Q_X|=|q|,
    π_(k−1)(j_(k−1))=L³|q|,
    ||j||_Pc=L^(θ_c+3)|q|,
    n³ max|Q_X| / ||j||_Pc = L^(3k−3−θ_c).

For fixed θ_c this is unbounded. No assumption that the 2d-term divergence upper bound is attained is necessary. Moreover |d*C(z)|≤2d||C||∞ gives π_0(C)≥n³ max|Q_X|/(2d), so the **push-down norm itself**, not merely the displayed upper bound, is unbounded in this example. This still gives no lower bound on its pairing with the particular response Y^p or on full curvature, whose right side also includes a top-residual term.

The norm definition gives π_(k−1)≤L^-θ_c||j||_Pc, whereas line 441 prints ≥. Correct **≥ to ≤**. Equality holds for the top-only witness above. For a counterexample to the printed universal comparison, take k=3, a nonzero co-closed j_1 and j_2=0: the left side is zero and the right side is positive.

The numerical root coefficient is sound as an upper bound. With a=(L−1)/(2L), the finite sum is

    a sum_(i=0)^(k−1) L^(3(k−i))
      = a L³/(L³−1) (n³−1)
      = (9/26)(n³−1)  at L=3.

Thus 0.3462 n³ is a conservative decimal upper bound: 0.3462−9/26=3/65000>0. It is not an erroneous number and is not the exact finite-k coefficient.

### F5 — RS10-6 concerns a different paired object; pinning does not cure that object

**Verdict: REFUTED** for the claimed discharge/relocation at COFUN.md:404-410, 425-426, 462-468, 573, 606-610. **Claim status: GAP** for that conclusion. The restricted cancellation of F1 is unaffected.

The actual binding item, REVIEW_BFT_B_S9_S10.md:897-899, asks for the divergence and representative freedom of **A=sum_l(Q_str^(0→l))^T ĵ_l**. COFUN.md:405 instead presents it as an objection about **C(j)** and an unrestricted optimizer. These objects differ by B(D). Pinning makes C orthogonal to dΛ_0; it need not make A orthogonal.

A complete counterexample to the latter inference already occurs at k=1. Put a unit current on the three edges joining adjacent block-centre roots X and Y, so D=δ_cY−δ_cX. Take λ=1 at one nonroot site in block Y and zero elsewhere; all root values are zero, so λ∈Λ_0. Path telescoping gives <C,dλ>=0. But h_0(dλ)(Z)=average_(B(Z))λ−λ(c_Z), hence

    <h_0^T R_1(D),dλ>=1/3^4=1/81,
    <A,dλ>=<C+h_0^T R_1(D),dλ>=1/81≠0.

Equivalently d*A is the signed uniform block-average density, not zero. This is precisely why a bound on C after introducing ROOT-sup is a different proof obligation from licensing Theorem COF's old argument for A. The old unrestricted norm estimate is not restored by CO-pin; YH-pin is new and OPEN. Also the literal source fact “the funnel pieces are co-closed only collectively” is not refuted by any orthogonality statement for C. BFT_B.md:4005 already separates that true fact from the invalid piecewise-superposition inference.

### F6 — A sufficient reduction is not an equivalence, and its residual terms must be retained

**Verdict: REFUTED** for “(TENT-Q) equivalently (ROOT-sup)” at COFUN.md:498-500, 589-590. **Verdict: NOT-VERIFIED** for an unconditional full analytic theorem; the claimed sufficient route at 435-436, 570 can be reconstructed **CONDITIONAL** on the imported response/residual and local Hölder estimates, as follows.

TENT-Q controls the weighted functional n² sum_X |Q_X||Φ_k(Y^p)(c_X)| for a named representative (BFT_B.md:4124). ROOT-sup controls n³ max_X|Q_X|. A functional estimate supplies no inverse lower bound for the response coefficients and hence no bound on every charge. None of the allowed sources proves those inverse bounds. Different powers of n and different spatial norms cannot be equated by the transpose identity. No converse to the displayed sufficient implication is established.

To check the forward route rather than merely object to it, write R_Q=n³ max|Q_X| and a=(L−1)/(2L). The same transpose/regrouping identity at an intermediate level gives

    P_m := sum_(l>m)(Q^(m+1→l))^T j_l
         = sum_(l>m)(Q_str^(m+1→l))^T ĵ_l − B_m(D),
    ||B_m(D)||∞ ≤ a/(1−L^-3) max|Q_X|.

Using the quoted response estimate n²||r_m(Y^p)||_1≤A_r L^(k−1−m) from BFT_B.md:4092, the extra residual contribution is at most

    A_r a/[(1−L^-3)(L−1)] n max|Q_X|
      = A_r a/[(1−L^-3)(L−1)] R_Q/n².

It is therefore uniform if ROOT-sup holds. The direct pairing is bounded by F1 with π_0(C)≤sum_lπ_l(ĵ_l)+aL³/(L³−1)R_Q. The j-only level-0 equation uses J_0=A−(Q_str^(0→k))^Tρ_(k−1), from BFT_B.md:3799, so the quoted local Hölder step can use the controlled A and top residual. This supplies the missing bookkeeping for a **conditional sufficient estimate**; it neither proves YH-pin nor makes ROOT-sup necessary. ROOT-sup is false on the unrestricted source-norm ball by F4, so the sufficient implication cannot decide (CO-fun)[cc] there.

### F7 — Textual staleness is real; “already mathematically refuted” is not established

**Verdict: CONFIRMED** for the distinct quantifiers and stale session-9 label. **Verdict: NOT-VERIFIED** for two fully rebuilt analytic theorems or a false unrestricted theorem. **Claim status: CONDITIONAL** for imported analytic results; **OPEN** for the unrestricted estimate in this packet.

Fresh string locations give BFT_B.md:3802 (session-9 OPEN statement over every LIN^cc source), 4074-4077 (Theorem COF explicitly adds CC-0), and 4112-4126 (the asserted session-10 refutation and its narrowing erratum). These are genuinely different claims. In the zero-residual source subclass, strict inclusions can be exhibited without citing status labels:

- (lw)⊂(CC-0): levelwise d*j_l=0 gives zero total divergence. Strictness: take a j_1 with d*j_1≠0 and j_0=−Q_0^Tj_1, all other slots zero. Root covariance gives total divergence zero, although j_1 is not co-closed.
- (CC-0)⊂(cc): the neutral root dipole of F4 has nonzero D supported at roots and annihilates Λ_0.

The older BFT-5 decision actually quantifies over **every** composite-co-closed source at BFT_B.md:3831, with no CC-0 restriction. Thus a theorem restricted to CC-0 does not discharge that decision. What cannot be certified is the claim that the chosen broad class is already FALSE: S10-11 uses the unresolved term-to-total inference of F2. COFUN's own narrowing exposes this, so continuing to call the item “not open” is untenable. The corrected report is “the session-9 formulation has later conditional results and an incomplete proposed refutation.” RTARGET, handoff/decision files and ledger entries were not opened; assertions about their current text are NOT-VERIFIED.

### F8 — The l.3810 erratum is supported, but a later line is not wholly validated

**Verdict: CONFIRMED** for the divergence correction at COFUN.md:366-371, 602-605. **Claim status: PROVEN** as algebra from the displayed correction-operator identity. **Verdict: NOT-VERIFIED** for the independent construction of Γ_E or its full operator bounds.

Freshly located BFT_B.md:3810 still says D(S+Γ_E^TD(S))=0; line 3812 states d*Γ_E^TD=−D+sum_XQ_Xδ_cX. Addition immediately gives

    D(S+Γ_E^TD(S))=sum_XQ_Xδ_cX,

which vanishes only if every charge vanishes. BFT_B.md:4202 states precisely this corrected divergence. The citation to l.4203 does not drift, but the divergence formula is at **4202**; line 4203 says “except for ... residue.” That latter assertion is itself qualified by RS10-6, so it must not be accepted wholesale merely because its treatment of root support is correct. The displayed formulas allow nonzero compensation charges, but the actual cutoff functions defining Q_X were not opened in this restricted review. Thus a concrete nonzero output of that particular correction map is NOT-VERIFIED here; the nonempty gap class itself is proved by F4. The source equations do not justify substituting CC-0 for cc.

### F9 — The sharp handle norms are correct; the general improvement factor is not L

**Verdict: CONFIRMED** for COFUN.md:217-249, 291-310 at the stated centre-root convention. **Claim status: PROVEN** by the following count, independently compared against the script's path enumeration. **Verdict: REFUTED** for the unrestricted “factor L” wording at line 251 if intended beyond L=3.

Put r=(L−1)/2 (not the script's block-count M). For coordinate μ=1,...,d, a positive link z_μ=c_μ+t with 0≤t<r is traversed by (r−t)L^(d−μ) endpoints with its previous μ−1 coordinates fixed. Its coefficient is (r−t)/L^μ. On the negative side z_μ=c_μ−t−1 the coefficient is −(r−t)/L^μ. Later coordinates must be at the root. The largest absolute coefficient is r/L. All paths stay in their block; disjoint blocks give one owner per nonzero link. Therefore the transpose ℓ∞ norm is exactly r/L, attained by a source on the maximizing block/link.

For the ℓ¹ norm, the monotone paths never contribute opposite signs on one link, so the sum of absolute coefficients is the mean path length. Each coordinate has mean absolute displacement [2 sum_(t=1)^r t]/L=r(r+1)/L. Thus

    ||h^T||_(∞→∞)=(L−1)/(2L),
    ||h^T||_(1→1)=d(L²−1)/(4L).

At d=4,L=3 these are exactly **1/3 and 8/3**; the original 1 and 8 are both three times larger. At general odd L>1 the improvement factors are **2L/(L−1)** and **4L/(L+1)**, respectively, not L; at L=5 they are **5/2 and 10/3**. The sharp divergence/convolution prefactor is 2d·(L−1)/(2L)=d(L−1)/L. Multiplying the raw current by L^(3(k−l)) gives exactly L^(-3(l−l′)); no k-dependent conversion survives. The finite convolution sum is (1−L^(-3(l+1)))/(1−L^-3), below 27/26 at L=3. The finite checks corroborate these algebraic identities, not a general chain-response theorem.

### F10 — The “only adds” premise is false, and the universal level-count conclusion exceeds the estimate

**Verdict: REFUTED** for COFUN.md:328, 483-488's monotonicity premise and the proposed proof of the universal no-go. **Verdict: NOT-VERIFIED** for that universal negative itself; **CONFIRMED** that the particular positive triangle-bound proof has an O(k) loss. **Claim status: OPEN** for an unavoidable lower bound on the consumer's response.

An upper estimate ||j+h^Tψ||≤||j||+||h^Tψ|| is not a monotonicity theorem. Here is an admissible exact counterexample at d=4,L=3,k=2, with only the level-1 current nonzero. Use roots a=(1,1,1,1), b=(4,1,1,1). Put unit current on the three edges a→b in direction 1. Add the unit oriented plaquette loop

    (1,1,1,1) → (2,1,1,1) → (2,2,1,1)
      → (1,2,1,1) → (1,1,1,1).

The loop has zero divergence, so d*j_1=δ_b−δ_a and the source is (cc). The raw sup of j_1 is 2 on the first path edge. Its funnel correction there is −1/3; direct coefficient counting gives raw sup of ĵ_1 exactly 5/3. Consequently **π_1(j_1)=54 whereas π_1(ĵ_1)=45**. The funnel decreases the norm. To place the same example in (CC-0), take k=3, retain this j_1, and add j_2 equal to minus the unit coarse edge joining those two level-2 roots. Its placed divergence cancels d*j_1 exactly; ψ_1 and the strict decrease of its level-1 norm are unchanged (both coarse norms acquire the same additional factor L³). Thus the counterexample is not confined to the root-charged class. All numbers were recomputed with exact Fractions from a closed-form kernel, separately from cf1's path-walk implementation.

For the narrower valid assertion, if all one retains is a_l≤A and a bound by a positive constant times sum_l a_l, then choosing a_l=A makes that bound proportional to the number of levels. Lowering the funnel coefficient cannot remove the direct j_l term from this particular argument. But these are upper estimates, not lower bounds on actual rows or their responses. The stated row hypothesis π_l(V_l)≤A does not imply π_l(V_l)≈A at every level. A geometric improvement a_l≤A L^(-ε(k−l)) would sum uniformly; cancellations between pushed-down levels are another possibility. Neither is excluded by the two handle estimates. The justified correction is “constant-factor sharpening of these same absolute-value bounds does not remove their level-count loss,” not “no per-level sharpening can ever remove it.”

### F11 — Two exponent errors: an omitted endpoint condition and an infeasible optimizer

**Verdict: REFUTED** for COFUN.md:191-198, 477-479 as written. **Claim status: GAP** for the advertised full-window/optimal-constant claims.

1. Line 192 quotes α≤θ≤1−α≤3/4. Its last inequality forces α≥1/4. Intersecting with α<θ gives **α∈[1/4,1/2), θ_c∈(α,1−α]**, not α∈(0,1/2). An exact counterexample to the reported intersection is α=1/8, θ_c=1/4: it lies in the reported window but 1−α=7/8>3/4. This corrects the intersection of the inequalities actually printed. The underlying BFT_A theorem was not opened, so the accuracy of that imported inequality itself is NOT-VERIFIED.
2. For fixed Hölder exponent α>0, the required θ>α rules out θ*=1/[(k−1)log L] once (k−1)α log L≥1. Thus this k-dependent “best θ” is outside the admissible domain for all sufficiently large k. Allowing α to vary with k would change a fixed exponent and introduces untracked dependence of the analytic constants on α. The valid O(k) upper estimate comes from the direct level sum, not this inadmissible optimization.

Even ignoring α, that θ* only optimizes the leading approximation. For the actual printed factor C_C=A[1+(1−L^-θ)^−1], set r=k−1>0 and z=L^θ. The objective divided by A is

    F(z)=z^r(2z−1)/(z−1),
    F′(z)/F(z)=r/z−1/[(2z−1)(z−1)].

The unique unconstrained minimum is therefore at

    z_0=[3r+1+sqrt(r²+6r+1)]/(4r),
    θ_0=log(z_0)/log L.

On α<θ<1, use this point only if it lies in the interval; otherwise take the infimum at the appropriate boundary. In particular for large k the lower boundary α controls it. The leading 1/(r log L) formula is only an asymptotic unconstrained approximation. This is a stale-quantifier error, not a harmless change of symbol from θ_w to θ_c.

### F12 — The gates reproduce, but the registered control logic does not

**Verdict: REFUTED** for treating cf1's “ALL PASS”/“C2 FIRED” summary as satisfaction of its registered contract. **Verdict: CONFIRMED** for the recorded raw kernel values and disclosed C3 failure. **Claim status: PROVEN** for the following code-level defects; the kernel mathematics remains covered by F9.

A fresh `python3 -B .../checks/cf1_funnel.py` run completed with exit code 0 and reproduced the recorded values. It wrote no files. The gate audit is:

| Gate | Exact location in checks/cf1_funnel.py | Can it decide its stated target? |
|---|---|---|
| A1 | 85-93, 153 | Inspects both link endpoints. The registered C3 changes paths but leaves the entire signed kernel unchanged. Thus its registered evidence is unsupported under criteria:55,67-68; the geometric proof and a separately labelled post-hoc mutation can support it. |
| A2 | 95-97, 150,154 | Measured maximum compared with an independently derived formula; C1 changes 1/3 to 2/3. Discriminating on these cases. |
| A3 | 99-101,151,155-156 | Measured row norm; C1 changes 8/3 to 4. C2 can never affect the signed kernel and cannot be its second control. |
| A4 | 103-108,157 | Counts owners. Given A1 and disjoint blocks it is a consequence, not independent evidence. Its registered C3 does not fire. |
| A5 | 110-112,158 | Recomputes matrix norms but is logically derived from A2-A4, as disclosed. |
| A6 | 114-121,159 | Checks signed action on constant coordinate forms. C1 gives 1 rather than 0. Discriminating. |
| A7 | 129-145,160 | Counts unsigned traversals. C2 attains **3**, not its registered **2**, and fails the ≤1 property. |
| B1 | 199-212 | Compares 3(k−l)−3(k−l′) with its algebraic expansion. It cannot catch an omitted operator normalization because no actual operator scaling enters. It is an identity, not empirical validation of the scaling premise. |
| B2 | 214-221,263-277 | Computes the finite geometric sum. C4's positive exponent violates the same cap. Useful arithmetic check; does not test the cascade or actual consumer. |
| B3 | 189-190 | An AND of the finite A results. No independent evidence for arbitrary dimension or a d=4 theorem. The general count in F9, not this conjunction, establishes the formula. |

Two exact reasons the controls fail their registration:

- C2 inserts an edge followed by its reverse; their signed kernel contribution is zero for every endpoint. Its entire kernel equals the baseline kernel. If the ordinary path then traverses that edge again, the unsigned multiplicity is **3**, explaining the correction from criteria:60's **2**. The registration requires **A3 AND A7 to fail**, but script:251 computes an **OR**. The correct conjunction is **False**, not the printed “C2 FIRED: True” (output:74). The narrative honestly acknowledges the A3 failure; the machine summary still uses the weakened condition.
- C3 replaces positive-direction paths by a path with one negative full winding and negative-direction paths by one positive winding. A central odd block has equal endpoint counts on either side, so those winding contributions cancel exactly. **The whole signed kernel equals the axial kernel**, as independently checked; this is stronger than merely zero exterior coefficients. It cannot break A1 or A4 as preregistered. Criteria:55,67-68 explicitly require unsupported status, but script:283-284 still prints “ALL PASS” solely from the base gates.

A1/A4's failed registration leaves them unsupported **by that control protocol**, not mathematically undecidable. A3 also has the valid C1 control. Independently replaying corner+wrap through the inspected cf1 functions gives **567 support violations and 3 owners** at d=4,L=3,M=3, agreeing with the target's post-hoc C6 claim. This does not retroactively make C3 fire. The files `cf1b_*` are outside the allowed `cf1_*` glob and were not opened; their detailed provenance and the reported C5 run remain NOT-VERIFIED.

A further undisclosed registration change is exact: **criteria:38 specifies M=3 for every run**, but **script:166 and output:32,41 use M=2 for (d,L)=(5,3),(4,5)**. The corrected record is M=3 for the first three runs, M=2 for the last two. This does not change the analytically local kernel norms, but “every verdict below is pre-registered” and the stated run list do not match.

### F13 — Timestamp errata are disclosed; the original pre-registration order is not recoverable from current mtimes

**Verdict: CONFIRMED** for the presence of the disclosures and the current measured timestamps. **Verdict: NOT-VERIFIED** for the historical order/content assertions at COFUN.md:644-675 and criteria:93-96. **Claim status: GAP** for an independently authenticated pre-registration claim.

At this review the measured mtimes, in UTC on 2026-10-28, are:

| File | Current mtime |
|---|---|
| COFUN.md | 21:54:13 |
| checks/cf1_criteria.md | 21:53:55 |
| checks/cf1_funnel.py | 21:46:33 |
| checks/cf1_out.txt | 21:46:47 |
| checks/cf1_err.txt | 21:46:46; zero bytes |

COFUN.md:631-677 explicitly admits planned header times, an overwritten first-draft history, and repeated erroneous timestamps. The script/output times match current metadata. But the current criteria file was modified **after** the script and output. It cannot independently authenticate what its thresholds, controls or run list were before the script existed. The earlier amendment mtime 21:45:08 and the resulting 85-second margin are a historical assertion in the same mutable note, not recovered states. The described chronology may be true; this review cannot verify it. This does not alter any exact mathematical identity, but it removes pre-registration as independent evidence for those identities.

### F14 — A live symbol collision survives: ĵ_0 has two incompatible definitions

**Verdict: REFUTED** for importing the regrouping identity without specifying the level-0 convention. **Claim status: GAP** in source consistency. Attaches to COFUN.md:427-432's import and BFT_B.md:3590,3964,4045-4046.

BFT_B.md:3590 defines ĵ_l=j_l+h_l^Tψ_l and then expressly says **ĵ_0:=j_0**. BFT_B.md:3964 and the identity at 4045 instead require the formula including the funnel also at l=0. At k=1 the identity C=A−B becomes

    j_0 = ĵ_0 − h_0^T R_1(D).

For the neutral dipole of F5, R_1(D)=ψ_0≠0 and h_0^Tψ_0≠0. Therefore this identity is true only with **ĵ_0=j_0+h_0^Tψ_0**, not with the exception at 3590. All reconstructions in this review explicitly use the full-funnel convention when defining A. The level-0 term written separately in BFT_B.md:3799 avoids the ambiguity. A consumer importing “as in §27.1” can silently drop that term; this is a genuine symbol-collision hazard, separate from the three CO-fun quantifiers.

Additional symbol checks: θ_c is the estimate's level weight, whereas α is fixed Hölder regularity; optimizing the former cannot silently vary the latter (F11). Q_X in the root bound is a raw divergence value, not a coarse current or the block operator Q_l. π_l=L^(3(k−l))||·||∞ fixes its unit conversion (COFUN.md:114-117,296-299). The half-width called M in COFUN.md:227 is distinct from the number of blocks called M in cf1_criteria.md:31-38. The three uses of the CO-fun name have been separated in F7; no comparison of their constants was accepted merely because they share a label.

### F15 — Do not replace annihilation of Λ_0 by pointwise zero divergence

**Verdict: NOT-VERIFIED** for the unrestricted pointwise identity d*C(j)=D(S) for every residual-slot source in COFUN.md:396-399. **Claim status: GAP** in the cited all-slot justification; the actual restricted CO-pin cancellation remains PROVEN by F1.

The proof of Lemma SPLIT at BFT_B.md:4035 infers D(S^s)=0 from invariance of the residual slots under the allowed gauge changes. On this pinned gauge space, that implication only gives D(S^s)∈Λ_0^⊥, i.e. a neutral root-supported function. F4 gives nonzero elements of that annihilator. To conclude pointwise zero for the residual slots, one must explicitly expand their chain sources, including any terminal fixed-B_k boundary term, or establish invariance under arbitrary unpinned level-0 functions. Neither expansion is present in the inspected proof. This is a missing justification, not a claimed counterexample to the actual residual convention, which is outside the permitted source allocation. It does not obstruct F1: both the residual slots and C(j) have the required functional pairing on Λ_0 regardless of any such root remainder.

## Summary table

| Finding | Review verdict | Correct claim status / consequence |
|---|---|---|
| F1: CO-pin cancellation and units | CONFIRMED | PROVEN on Λ_0; norm consequence CONDITIONAL on YH-pin |
| F2: independent blow-up route / settled falsity | REFUTED; actual curvature blow-up NOT-VERIFIED | Same defect and its transpose; unrestricted estimate OPEN in this packet |
| F3: one pinning constraint / harmless pin | REFUTED; actual YH-pin NOT-VERIFIED | T^4−1 scalar constraints; YH-pin OPEN |
| F4: ROOT-sup and comparison sign | Root-norm failure CONFIRMED; printed ≥ REFUTED | Explicit neutral dipole; correct comparison ≤; no curvature lower bound |
| F5: RS10-6 discharge and relocation | REFUTED | A and C differ; admissible gauge change gives 1/81 versus 0 |
| F6: ROOT-sup ↔ TENT-Q | REFUTED | Only a CONDITIONAL sufficient route reconstructed; no equivalence |
| F7: three classes / staleness | Text and distinct classes CONFIRMED; full statuses NOT-VERIFIED | Consumer uses broad class; “already decided false” unsupported |
| F8: divergence erratum | Algebra and exact source locations CONFIRMED; concrete map reach NOT-VERIFIED | Corrected source has root-supported divergence, not automatically zero |
| F9: sharp handles | CONFIRMED; general factor-L reading REFUTED | Exact norms 1/3, 8/3 at L=3; general improvement factors corrected |
| F10: funnel monotonicity / unavoidable k | Monotonicity REFUTED; universal negative NOT-VERIFIED | Existing absolute-value proof loses k; no proved response lower bound |
| F11: exponent window / optimizer | REFUTED | α≥1/4 for printed window; enforce θ>α before optimizing |
| F12: gates and registration | Raw values CONFIRMED; control-contract compliance REFUTED | C2 needs AND; C3 leaves kernel unchanged; two M values differ from registration |
| F13: timestamp history | Disclosure/current times CONFIRMED; original order NOT-VERIFIED | Current metadata cannot authenticate overwritten criteria contents |
| F14: ĵ_0 collision | REFUTED as a consistent imported definition | Regrouping needs ĵ_0=j_0+h_0^Tψ_0 |
| F15: all-slot pointwise divergence identity | NOT-VERIFIED | Restricted annihilation does not prove zero at roots; CO-pin's restricted identity survives |

## Numeric and formula corrections

- Pinning is **T^4−1**, not one, independent scalar root constraints: **624 at T=5**, per Lie-algebra component.
- The printed exponent-window intersection is **[1/4,1/2)** for α, not **(0,1/2)**; θ_c∈(α,1−α]. This correction is conditional on the imported inequalities as quoted.
- **1/[(k−1)log L]** is an unconstrained leading approximation, not an admissible optimizer for all k at fixed α. For the actual displayed C_C factor use **log([3r+1+sqrt(r²+6r+1)]/(4r))/log L**, r=k−1>0, only when it lies in α<θ<1; otherwise the relevant boundary infimum controls.
- The two general improvement factors are **2L/(L−1)** and **4L/(L+1)**, not L; at L=5: **5/2 and 10/3**. At L=3 the claimed **3× and 3×** are correct.
- C2's registered unsigned multiplicity **2** is **3** for the specified control. Its registered joint firing verdict is **False**, not True.
- The last two cf1 runs use **M=2**, not registered **M=3**: (d,L)=(5,3),(4,5).
- COFUN.md:441's comparison must be **≤**, not **≥**. Equality is available for a top-only source, not every source.
- **0.3462 is not refuted:** the exact asymptotic coefficient is **9/26**, and the exact finite-k term is **(9/26)(n³−1) max|Q_X|**. The rounded-up decimal is safe.

## Reproduction and access limits

Independent work consisted of the complete restricted-gauge derivation, root-dipole and signed-current constructions, symbolic minimization, closed-form kernel counting, exact Fraction comparisons, and the unchanged cf1 rerun. No floating point, BLAS, quadrature, long jobs, git commands, source changes, audit ledgers, snapshots, or extra scientific files were used. Only this deliverable was written. The two extra reads were the methodology and review-procedure files named in the pre-stated access record; the user's narrower scope controlled any broader skill routing.

The two decisive sparse-current checks used d=4,L=3,T=5 and exact path/plaquette coefficients: <C,dλ>=0, <A,dλ>=1/81; max|j|=2, max|ĵ|=5/3. Independent closed-form counts matched cf1's five raw pairs (max coefficient, row norm): (1/3,4/3), (1/3,2), (1/3,8/3), (1/3,10/3), (2/5,24/5). These are reproduced values, not newly granted science statuses.

Reviewed COFUN.md SHA-256: `aeda6b72dda729b5994ba33ab9b53fd9525222f6e6468d0d219ca4e72b6f116d`.
Reviewed cf1_funnel.py SHA-256: `bf1002b4f6f50e284ff5c22acdab8547c012317e1226a3564ebb79562f042ab6`.
Reviewed cf1_criteria.md SHA-256: `016757d0adf507e3eacc7b22a78eacc7532aadb4f3f92fac1688a0f647e59496`.

Fresh source matches support the cited BFT_B locations 3802,3810,3812,4076-4077,4112-4126,4202-4203. They have not drifted in this reviewed copy. Citations into PROOF.md, BFT_A, other reviews, RTARGET, decision files and ledger entries are **NOT-VERIFIED**, not presumed current. The all-source analytic theorems and actual plaquette-response coefficients are not granted confirmation from their status labels.

**Single most dangerous unverified issue:** whether a normalized admissible neutral root-dipole source actually makes the *full* curvature response grow relative to the *entire* claimed right-hand side, including the top residual. Neither an upper bound on C nor one unbounded tent summand excludes the two possible cancellations (within the neutral root pair and against the complementary response term). Calling (CO-fun)[cc] refuted while that is unresolved can prematurely discard a valid route.
