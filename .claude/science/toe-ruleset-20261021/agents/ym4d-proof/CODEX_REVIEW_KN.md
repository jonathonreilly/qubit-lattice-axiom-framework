# Independent hostile review of KN_ADOPT.md

## PRE-STATED — 2026-10-28T21:49:51Z

Scope: review the proposed KN_ADOPT section 8.1 insertion using the owner's restricted source list and at most two additional files. No git operations; only this deliverable may be written. This statement precedes mathematical derivation and inspection of the target.

Targets and pre-stated refutation criteria:

1. **Transport identity / H1-F2.** Reconstruct the indexed averaged transport used in (R1). Refutation: convex weights apply to a different map, contour indices or translations fail to match, or a load-bearing identification is unsupported in the permitted evidence. Unsupported identification receives NOT-VERIFIED / GAP, not a fabricated counterexample.
2. **Degeneracy.** Enumerate the d=4, L=3 index set using plain Python and exact combinatorics. Refutation: the stated 1944 indices, 633 distinct transporters, or multiplicities/weights disagree with the explicitly defined path object. Distinguish formal paths from possible coincidences for special gauge fields.
3. **Side conditions and exponent.** Derive S1–S4 and the identity (L^2 + 5.5 A_d)c_1=1/2 with symbols tied to their definitions. Refutation: an inequality fails on the claimed input range, a minimum is stale, or a changed kernel estimate is disguised as an unchanged exponent.
4. **Reversals and constants.** Rebuild eta_1/eta_q, the route ratio, and 13/512 with exact arithmetic. Refutation: any quoted ratio uses incompatible definitions, an unstated minimum, or a wrong N/epsilon dependence.
5. **Baseline and gain.** Determine whether RS-lin is actually derived and active at the same interface. Refutation: the claimed incremental gain compares against a superseded quadratic route, or the purported existing linear route lacks its required hypotheses.
6. **Decidability / patch safety.** Inspect each accessible gate for circularity, vacuity, frozen inputs, and omitted branches. Give a yes/no append recommendation and the smallest sufficient correction.

Review findings use CONFIRMED / NOT-VERIFIED / REFUTED. Mathematical claim statuses use PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. CONFIRMED means independently checked within the stated scope; labels in source files are not proof. Arithmetic will be exact rational/symbolic plain Python only. Decimal decade claims will be tested with rational enclosures if needed.

## Findings (appended during review)

### F1 — CONFIRMED for axial-path labels; REFUTED for distinct transporters

**Attaches to:** KN_ADOPT.md §1.6, string `633 distinct (path, y) pairs`, and §6 row `degeneracy of the index→transporter map`; checks/kn1_criteria.md `DEGENERATE-BUT-CONVEX`.

For k nonzero coordinates of y−c_X, the number of distinct (y, axial-path) labels is binom(4,k)2^k k!, each with multiplicity 24/k!. Summing gives 633 labels. Their multiplicity histogram is **{1:384, 4:192, 12:48, 24:9}**, hence exactly the four listed weights. This restricted combinatorial claim is PROVEN.

But these labels are not distinct T transporters. RLARGE.md:989–991 itself says a μ-directed rectangle is degenerate/backtracking. Take y−c_X∈{−e_μ,0,+e_μ}: all 72 indexed terms give the same straight transporter S_c, regardless of σ. Its merged weight is **72/1944=1/27**, absent from the claimed list. Thus the claim about distinct transporters fails even before choosing a gauge field.

Independent plain-Python enumeration of the full word P·μ^3·P_translated^{-1}, cancelling adjacent inverse edges, gives **475 freely reduced transport paths**, with multiplicity histogram

| multiplicity | number of reduced paths | induced weight |
|---:|---:|---:|
| 1 | 288 | 1/1944 |
| 4 | 96 | 1/486 |
| 6 | 48 | 1/324 |
| 12 | 12 | 1/162 |
| 20 | 24 | 5/486 |
| 48 | 6 | 2/81 |
| 72 | 1 | 1/27 |

Counts sum to 475 and multiplicities sum to 1944. A separate counting derivation: with k nonzero transverse coordinates, there are binom(3,k)2^k k! transverse paths; for each, one class with no surviving μ excursion and 2k classes with a signed μ excursion before the last transverse step. Therefore the count is Σ_{k=0}^3 binom(3,k)2^k k!(1+2k)=475. The no-excursion multiplicities are 24/k!+48/(k+1)!; the excursion multiplicities are 24/(k+1)!. This reproduces the histogram without the enumeration algorithm.

These are formal reduced paths on the local lattice, not a claim that their matrix values differ on every field; at the identity field they all coincide. **Convexity survives every merging.** Minimal correction: call 633 the count of `(y, axial-path)` labels only, or replace the distinct-transporter refinement by the reduced-path count and weights above.

### F2 — REFUTED: the proposed minimum has a stale ε_1 crossover

**Attaches to:** KN_ADOPT.md §8.1, string `it would take ε_1 > 814.587 for the other branch, N = 2`.

After η_1=ε_1/117,

    a_RS = ε_1²/N · min{1/27378, κ/256}.

The branch boundary is **κ=128/13689**, independent of ε_1 and N for ε_1>0. At κ=1 the plaquette entry wins at every positive ε_1 for which the lemma applies; there is no ε_1=814.587 crossover. For κ<128/13689 the kernel entry wins at every positive ε_1. This is a PROVEN algebraic refutation and a direct instance of a stale minimum surviving a substitution.

The cited RLARGE.md:1020 defines a symbolic κ; it does not set κ=1. checks/kn1_criteria.md's `a_RS` input row imports κ=1 without a supporting definition in the permitted RLARGE ranges. Numerical gain rows at κ=1 are conditional evaluations, not a discharge for arbitrary κ.

### F3 — REFUTED: these exponent comparisons are live v3 coupling-ceiling gains

**Attaches to:** KN_ADOPT.md §8.1 item 4, string `l.618 must be edited regardless`, and item 7's `honest ledger line`; REVIEW_ARS_EPS_S1.md §1 item 2 / summary RA-17.

RLARGE.md:433–439 explicitly retires the old case split, the 81 and 5⁴ greedy factors, and a_♯ for unreturned defects. RLARGE.md:832 replaces a_♯/n_♯ by a=min{θa_bad,a_A}; :835 says the frozen §7.3 route is not used by RLF-step v3. The actual :616–618 ceiling uses this a, not a_RS. Therefore replacing a by a_RS/625 and declaring :618 false is a change of object, not a correction of its arithmetic.

The second reviewer is right that an existing joint-route baseline must be considered, but **its own phrase “lane's own best proven route” is not established by the PROVEN-HERE list at RLARGE.md:628**. The permitted text supplies neither the RS-lin proof nor a live v3 use of its joint pricing; :434–437 instead explicitly removes that pricing from the unreturned-defect route. The live gain is **NOT-VERIFIED / GAP**, not automatically either 82.1406 or 2.3033 decades. The latter is a valid comparison of the two displayed historical/bare-level exponents under their branch assumptions, evaluated below.

### F4 — CONFIRMED: a linear RS estimate can be re-derived without re-centring; NOT-VERIFIED: HIST's full RS-lin/joint theorem

**Attaches to:** KN_ADOPT.md:353–354 (`PM is what makes the threshold linear`); RLARGE.md:64–65, :973–999, :628; REVIEW_ARS_EPS_S1.md summary RA-17.

Here is an independent proof of the relevant linear one-step estimate, rather than an appeal to `PROVEN-HERE`. Keep the original centre S, let M=S(I+E) with ||E||_op≤A_dη by (R1), put Z=S^{-1}V and x=||I−Z||_HS. Then exactly

    Re tr((S^{-1}−V^{-1})M)
      = Re tr((I−Z^{-1})(I+E))
      ≥ x²/2 − sqrt(N) A_dη x.

For η<η_q≤ε_1/(256NA_d) and x≥ε_1/8,

    4 sqrt(N) A_dη ≤ ε_1/(64 sqrt(N)) ≤ ε_1/8,

so this trace difference is at least x²/4. Comparing the kernel normalizer's SU(N) maximizer with the candidate S gives precisely the same tail coefficient κε_1²/(256N) as the proposal. Also η_q≤ε_1/(2L²) makes the original (R2) dichotomy valid: L²η_q+4(ε_1/8)≤ε_1. An operator-norm mismatch implies this Hilbert–Schmidt mismatch. The extra δ_0/A_d cap only makes the estimate safer.

Thus **availability of a linear-threshold RS-type estimate is CONFIRMED / PROVEN from the displayed (R1), (R2), and normalized-kernel hypotheses**. This proof does not need a polar construction or logarithmic re-centring. It uses the same cancellation in the normalized trace difference that the patch exploits; the patch additionally cancels the *first-order mean error*, replacing O(η) by O(η²) and allowing a larger linear coefficient.

This is not a reconstruction of the unread HIST proof, nor a proof of its 81-cube joint pricing, nor its effective-level plaquette hypothesis. Those remain **NOT-VERIFIED / GAP** here. At effective levels the excerpt itself retains conditional hypotheses (RLARGE.md:434–437 and :1020). There is no basis to call the entire comparison an unconditional live proof improvement.

**Adjudication:** the second reviewer correctly identifies a mathematically available linear baseline, but overstates its live-route/proven-joint status. The appropriate comparison is +2.303258… decades at N=2 **for the two stated bare/per-cube formulas, under their branch and pricing assumptions**. Neither that figure nor +82.140564… establishes an improvement of live v3's a=min{θa_bad,a_A}. The patch is potentially a useful local sharpening; its alleged programme necessity is REFUTED.

### F5 — H1 six-step chain: local algebra CONFIRMED; complete source identification NOT-VERIFIED

**Attaches to:** KN_ADOPT.md:122–170, :180–214, :530–558; RLARGE.md:970, :973, :984–998.

1. In the formula quoted at KN_ADOPT.md:128–130, the *same* σ determines both axial paths. For an axial path γ from c_X to y, the path from c_Y=c_X+Le_μ to y+Le_μ is the translated geometric path γ+Le_μ. This does **not** assert equality of their matrix transporters on an arbitrary field.
2. Consequently T_{σ,y}S_c^{-1} follows γ·leg(y)·(γ+Le_μ)^{-1}·leg(c_X)^{-1}. This is exactly the loop explicitly used in RLARGE.md:985–986, with no averaging yet.
3. Extend γ one edge at a time. A transverse edge adds a width-one, length-L rectangle, hence L conjugated plaquettes; a μ edge adds a backtracking loop and contributes zero. At L=3 each transverse displacement has size at most one, so at most three transverse edges contribute, giving 3·3η=9η. This independently reconstructs the summand bound and explains the additional degeneracy in F1.
4. RLARGE.md:970 takes the maximum over these same `(σ,y)` contours. For the explicitly quoted indexed mean M=(1/1944)ΣT, subtract S and apply the triangle inequality: ||M−S||≤(1/1944)Σ||T−S||≤δ_c≤9η. Also ||M||≤1. Thus (R1)'s displayed second clause *does consume* the convex-mean property.
5. RLARGE.md:995–998 carries that M and S into its trace difference and D4 normalizer. No polar replacement or independently reweighted average appears in the inspected consumer proof.
6. If the quoted decision-4 definition is the actual kernel's definition, its 24·81 positive constant weights prove H1, and the quoted log-average formula gives W'=S exp[(1/1944)Σlog(S^{-1}T)]. These conclusions are **PROVEN for the explicit construction**.

However, PROOF.md itself was not read: the two additional-file slots were used for the required science workflow and local review-loop procedure. The alleged current PROOF.md:712, :714, :1754–1757 contents, the D′ domain identification, and inherited symmetry theorems are therefore **NOT-VERIFIED**, including citation drift. I cannot independently certify the full live-source H1-F2 exclusion by treating KN_ADOPT's own quotations as authenticated source. No actual counterexample to the quoted uniform mean was found. The source-identity conclusion is **CONDITIONAL**, not REFUTED.

**Logical overclaim, REFUTED:** KN_ADOPT.md:187–190 and checks/kn1_criteria.md:58–61 say ||M||≤1 holds *iff* the weights are a probability vector, and that failure of H1 would make (R1) false. Sufficiency is proved; necessity is not. With T_1=T_2=S and weights (2,−1), M=S, ||M||=1 and ||M−S||=0 although that indexed weight vector is not nonnegative. The actual family has duplicates, so this is not an irrelevant model. Even distinct SU(2) terms I and −I with weights 1/2 and −1/2 have M=I despite total weight zero. Existing bounds do not retrospectively prove their hypotheses.

Even the existential version of that necessity claim fails. Let z=(99+20i)/101, T_+=diag(z,conj(z)), T_-=T_+^{-1}, and S=I. The normalized signed combination M=T_++T_-−I=(97/101)I is outside the convex hull of {T_+,T_-,I}, whose diagonal real parts are at least 99/101. Thus no probability vector on this family represents M. Nevertheless ||M||=97/101<1 and ||M−I||=4/101≤max||T_i−I||=2/sqrt(101). Both claimed norm consequences survive despite failure of the convex-hull premise. All entries in this counterexample are exact rational complex numbers.

Likewise KN_ADOPT.md:699–703's claim that any reweighting or field dependence breaks three statements is false: arbitrary pointwise nonnegative normalized weights preserve the two norm bounds and the KN algebra. Covariance may require additional equivariance, but uniformity/field independence is not required for these pointwise inequalities.

### F6 — Side conditions: S1–S3 CONFIRMED as sufficient bounds; the S4 verification claim REFUTED

**Attaches to:** KN_ADOPT.md:545–566, :604–606, :649–657; checks/kn1_sides_out.txt sections (A)–(C).

The scalar in the patch is c_KN:=1/117 (renamed here to avoid the existing coarse link c_1 at RLARGE.md:967). A_d=9, L²=9, and

    (9+(11/2)·9)/117 = (117/2)/117 = 1/2.

This is PROVEN algebra, not an independent test of the choice 5.5. The relevant analytic bound on 5.5 is checked below.

- **S1.** A_d² c_KN²=1/169. Thus the stated ceiling is 169/(106 sqrt(N)), in **[1.127368358684,1.127368358685]** for N=2 and **[0.920492410311,0.920492410312]** for N=3. The exact sufficient condition behind the kernel proof is ε_1≤169/[(32π²/3)sqrt(N)], since 8·12·(π/3)²=32π²/3. This coefficient lies in **[105.275780278286,105.275780278287]**, strictly below 106. Hence the adopted S1 is safely stronger, **not “exactly” equivalent** as :605 says.
- **S2.** (π/3)·9·(ε_1/117)≤1/4 is exactly ε_1≤39/(4π)=351/(36π), in **[3.103521390291,3.103521390292]**. It also ensures A_dη_1≤3/(4π)<1, justifying use of the principal-log chord bound.
- **S3.** For Q=S^{-1}T∈SU(N), the principal eigenangles obey |θ_j|≤(π/3)||Q−I|| when ||Q−I||≤1. Indeed θ∈[−π/3,π/3] and 2 sin(|θ|/2)≥3|θ|/π. Their sum lies in 2πZ; N·max|θ_j|<2π forces it to be zero. Substitution gives ε_1<78/N exactly, so each log is traceless and W'∈SU(N). This independently proves the needed chart implication. It does not authenticate the cited PROOF D′ definition. At N=2,3 the two stated ε_1 values satisfy S1–S3. This is not a uniform assertion for arbitrary N: S3 always retains its N dependence.
- **S4.** This is a separate restriction on R and the coupling, not a consequence of tiny ε_1. The cited output computes S1/S2 and contains **no S4 check, no R value, and no g_K value**. It does not even print a separate S3 check. Therefore the claim “all four hold … by ~40 decades; verified in …kn1_sides_out.txt” is REFUTED as an evidence claim. Actual S4 satisfaction is **NOT-VERIFIED / CONDITIONAL**. Equality g_K²=1/(2R) would leave zero slack while obeying S4.

The flow-cost wording also needs narrowing. For a fixed step and B=log C_ℓ, solving a(1/g²−R)≥B gives the **exact ceiling g²≤a/(B+aR)**. The factor 2 is a conservative sufficient loss when Rg²≤1/2, not an exact cost: for R=0 the cost is 1. Furthermore g_K²≤1/(2R) does not itself imply Rg_j²≤1/2 for every intermediate j. RLARGE.md:833–834 expressly replaces monotonicity by g_j²≤g_K²/(1−Rg_K²).

An exact counterexample to that intermediate implication is R=10, K=1, u_1=20, u_0=21/2, β_-log L=β_+log L=1/2. The displayed (F_R) condition at RLARGE.md:98–100 holds (u_0−u_1=−19/2 is its lower endpoint), and g_K²=1/20=1/(2R), but u_0−R=1/2<u_0/2=21/4. This does not require changing a fixed positive β_-: more generally put b=β_-log L, choose R>b, and take u_1=2R, u_0=R+b. The lower flow bound is saturated, the upper bound holds for β_+≥β_-, and u_0−R=b<u_0/2. Thus the patch cannot silently substitute arbitrary g_j into its half-exponent assertion.

The intended *final-coupling* estimate is repairable: use (F_R) globally to obtain u_i≥u_K−R≥u_K/2. Then g_K²≤a/(2B) suffices for a u_i≥B. Say “a sufficient factor-two tightening at g_K,” not “exactly factor two at every step.” When that same conservative convention is used before and after, it cancels in the reported gain. The value log10(2) lies in [0.301029995663,0.301029995664].

### F7 — CONFIRMED: the local kernel coefficient survives re-centring

**Attaches to:** KN_ADOPT.md:569–620; RLARGE.md:976–999. **Claim status:** PROVEN for the explicitly specified convex average, S1–S3, and the displayed normalized kernel; live-source identification remains CONDITIONAL as in F5.

Let δ=max||X_i||_op, X_i=log(S^{-1}T_i), X̄=Σw_iX_i and W'=S exp X̄. Convexity gives ||X̄||≤δ. Expanding to first order and using Σw_i=1, Σw_iX_i=X̄ gives

    R:=W'^{-1}M−I
      = Σw_i(e^{-X̄}−I)(e^{X_i}−I)
        +(e^{-X̄}−I+X̄)+Σw_i(e^{X_i}−I−X_i).

The exponential series therefore gives

    ||R|| ≤ (e^δ−1)²+δ²e^δ
           ≤ δ²(e^{2δ}+e^δ) < 3δ²  (0<δ≤1/4).

Independent rational bounds give e^{1/2}+e^{1/4}∈[2.932746687387,2.932746687388], establishing the last inequality without floating point. The δ=0 case is exact.

For Z=W'^{-1}V, x=||I−Z||_HS, unitarity gives Re tr(I−Z^{-1})=x²/2. Hence

    Re tr((W'^{-1}−V^{-1})M) ≥ x²/2−3 sqrt(N)δ²x ≥ x²/4

whenever x≥12 sqrt(N)δ². S1 ensures this on x≥ε_1/8, by the coefficient check in F6. W' is a legitimate SU(N) candidate by S3; using the actual maximizer in the normalizer can only improve the bound. Consequently the exponent is

    (κ/(Ng²))·(1/4)·(ε_1/8)² = κε_1²/(256Ng²).

For completeness, the normalization mechanism requires only ||M||≤1: on an operator-norm ball of radius r=g²/κ≤1 around a maximizing V_0, normalized trace energy differs from its minimum by at most r. Its Haar volume lower bound c_N r^{N²−1} yields the displayed e^{-1}c_N r^{N²−1} factor. Neither this step nor its prefactor depends on the chosen comparison centre. The *same* Haar-ball constant can be used before and after.

The old proof uses a different route to the same coefficient: η_old≤ε_1²/(512NA_d) gives 2A_dη_old≤ε_1²/(256N), so ε_1²/(128N)−2A_dη_old≥ε_1²/(256N). Thus invariance is genuinely derived, not just equality of two printed constants.

The dichotomy is also valid: ||W'−S||≤e^δ−1, and the telescoping coefficient is

    4·[(e^{1/4}−1)/(1/4)]·(π/3)
      ∈[4.758891533327,4.758891533328] < 5.5.

Therefore ||I−W'_P||<(L²+5.5A_d)c_KNε_1=ε_1/2 on η<c_KNε_1. Four mismatches each below ε_1/8 cannot then produce a bad plaquette. This is a deterministic implication; “exhaustive by construction” is appropriate as a proof conclusion but is not a separate empirical gate. The HS-tail bound covers the operator-norm event used by the dichotomy, since ||·||_HS≥||·||_op. Multiplication across links is conditional on the fixed U and the product kernel at RLARGE.md:980; no unconditional independence after integrating U is claimed here.

Finally, (R5)'s bare coefficient follows from 1−Re tr(U)/N=||I−U||_HS²/(2N)≥||I−U||_op²/(2N). It does **not** prove an effective-level large-deviation estimate. RLARGE.md:1020–1021 calls a_η an output of (PLD)_k(i); :1025–1026 explicitly qualifies η_1²/(2N) as its **bare-level value**. KN_ADOPT.md:614–616 must retain that distinction instead of setting the effective a_η equal to the bare value unconditionally.

### F8 — Ratios and gains: numbers CONFIRMED on their stated branches; universal equalities REFUTED

**Attaches to:** KN_ADOPT.md:253–292, :305–351, :640–647, :669–676; checks/kn1_criteria.md:88–90; RLARGE.md:64–65.

For ε:=ε_1>0, N≥2, d=4, L=3, retain the actual minimum:

    η_q=min{ε/(2304N), δ_0/9},
    η_lin/η_q=max{256N/13, ε/(13δ_0)}.

The omitted ε/18 entry is larger than ε/(2304N). Omitting δ_0/9 **increases** η_q and **decreases** the ratio, the opposite of KN_ADOPT.md:306 and the pre-registered criteria. Hence 512/13 and 768/13 are exact only when δ_0≥ε/(256N); otherwise they are strict lower bounds. The ordering reversal still holds for all positive ε,δ_0, but exact ε-independence does not. Similarly η_q/η_lin=min{13/(256N),13δ_0/ε}; **13/512=0.025390625** is an upper bound at N=2 unless the chart cap is inactive. At N=3 the corresponding value is **13/768**, not 13/512.

For 0<ε≤2 and inactive chart cap, the old quadratic entry is active and η_old/η_q=ε/2≤1. Thus the earlier endorsement was correct on its stated domain. Adoption invalidates continued use of that old statement; it does not falsify the old theorem with its original definition.

With the new plaquette branch active (κ≥128/13689), the chart cap inactive, and both displayed cube factors applicable:

| quantity | N=2 | N=3 |
|---|---:|---:|
| η_lin/η_q | 512/13 | 768/13 |
| bare exponent ratio | 262144/169 | 589824/169 |
| per-cube ratio, multiplied by 81/625 | 21233664/105625 | 47775744/105625 |
| per-cube ratio, decimal enclosure | [201.028771597633,201.028771597634] | [452.314736094674,452.314736094675] |
| log10 of per-cube ratio | [2.303258218872,2.303258218873] | [2.655440736983,2.655440736984] |

Therefore **201.029×, not 1551×**, is correct for the N=2 comparison of those two formulas. The number 1551.1479… is the bare ratio 262144/169. These are not unconditional route theorems: the chart cap, κ, effective plaquette estimate, and cube pricing must all match. RLARGE.md:1021 itself labels the 625 counting argument ARGUED, and :437 calls RS-joint conditional.

At κ=1 the within-RS gain is exactly

    G=2 log10[4608N/(117ε)].

The 625 and 100 cancel because this compares the same RS convention before/after. Rational log enclosures independently give:

| ε used | N | enclosure for G (decades) | target rounding |
|---|---:|---:|---:|
| 6.7·10^-40 | 2 | [82.140563603264,82.140563603265] | 82.1406 |
| 6.7·10^-40 | 3 | [82.492746121375,82.492746121376] | 82.4927 |
| 9.38495112638·10^-45 | 2 | [91.847849178054,91.847849178055] | 91.8478 |
| 9.38495112638·10^-45 | 3 | [92.200031696165,92.200031696166] | 92.2000 |

All four numerical roundings are CONFIRMED. They compare against the old *quadratic* RS threshold, not the available linear baseline in F4. The “today” value is an evaluated ceiling example, not proof that every allowed ε equals that value. The proposed ε is a transcribed input from KN_ADOPT, not independently authenticated to EPS1_SWEEP. If the new kernel branch binds while the old quadratic branch remains active, replace G by **2 log10(4608N/ε)+log10(κ/128)**. For still smaller κ even the old branch can switch; use the full minimum, not either closed form.

### F9 — Gate audit: several checks can fail arithmetically but cannot decide the claimed interface

**Attaches to:** KN_ADOPT.md:456–492; checks/kn1_criteria.md:37–119; the three kn1 output files. Script implementation itself is **NOT-VERIFIED**: no `.py` source was read or run, because the two extra-file slots were already consumed. The conclusions below concern the specified tests and their printed evidence, not invented claims about code internals.

| gate | could it fail? | what it cannot decide / verdict |
|---|---|---|
| kn1-1 uniform weights | A supplied signed/unnormalized list can fail. The constructed uniform list necessarily passes. | No test authenticates that list to the actual kernel or tests H1-F2. Treating its output as that certification is REFUTED. |
| kn1-1 signed control | Yes; independently shown below. | Valid sensitivity to signed weights, not an independent source-identity control. |
| kn1-1 degeneracy | Incorrect partitioning still gives positive multiplicities summing to 1944. | It accepted 633 axial labels as transporters while the full paths give 475. The normalization gate cannot decide the quotient it claims to validate. |
| kn1-2 gain | Yes: changed ε or c_KN changes the arithmetic. | No variation of κ, δ_0, active consumer, or effective a_η is established. Passing at κ=1 cannot justify the stale crossover or a live gain. |
| kn1-3(a),(c) | Ratios change under the stated controls. | Omitting the chart cap makes ε-independence automatic for two linear formulas. Two-point equality does not check a branch that was removed from the input. |
| kn1-3(b) | Yes: the independent 81/625 comparison distinguishes 201 from 1551. | It checks the formula comparison, not proof or live use of either cube-pricing theorem. |
| kn1-4 identities | Changing 5.5 while freezing 1/117 breaks equality. | With c_KN defined as 1/[2(L²+5.5A_d)], the half identity is unavoidable. The control tests transcription consistency, not sufficiency of 5.5 or H1. The analytic inequalities in F7 do the latter relevant work. |
| kn1-5 precision | A precision discrepancy is possible. | Both precisions can agree on a wrong formula or wrong input. No scientific/source gate is supplied. The actual claimed 4.841e−49 run difference is NOT-VERIFIED here. |
| kn1-6 side conditions | Its S1/S2 comparisons can fail (e.g. ε=10). | It has no S4 test and no current R/g_K inputs. “All four verified” is REFUTED. |

The signed control can be checked exactly without its floating-point complex calculation. For θ=1/4 and weights (4,−3), an eigenvalue of M is cosθ+7i sinθ, so ||M||²=1+48 sin²θ. Since sin(1/4)≥1/4−(1/4)³/6=95/384,

    ||M||² ≥ 12097/3072 > (19/16)².

As W' is unitary, ||W'^{-1}M−I||≥||M||−1>3/16=3δ². Thus the control genuinely violates the desired conclusion. This validates sensitivity to a signed family, while leaving the source-identity defect untouched. A failed control would not by itself prove convexity decorative, either: failure can mean a badly chosen control.

### F10 — REFUTED: “literal and append-ready”; recommendation **NO**

**Attaches to:** KN_ADOPT.md:527, :541–625, and the requested consequential edits :629–665.

The local re-centred estimate is useful mathematics, but the patch contains a false crossover, an unsupported all-four-conditions assertion, an effective/bare exponent conflation, and a claimed mandatory correction to an unrelated live ceiling. A blanket “LANDS” is not supported.

The minimal substantive repair is to retain the proved local estimate and narrow its adoption text as follows (no target source was edited):

1. **Make the object contract explicit.** Insert `For the kernel with M̄_c=(d!L^d)^{-1}Σ_{σ,y}T^σ_y, with the paired translated axial paths of (R1), define c_KN=1/[2(L²+(11/2)A_d)] and η_KN=c_KN ε_1.` Use c_KN rather than the already occupied coarse-link name c_1. Until the defining source is authenticated, label applicability to the actual decision-4 kernel CONDITIONAL; do not infer it from the fact that an old proof already needed convexity. The local theorem is self-contained under that contract. Remove the unverified inherited-symmetry certification from this local append.
2. **Replace the side-condition preamble** by `Assume S1–S3; they hold for the two evaluated ε_1 inputs at N=2,3. S4 is a separate standing flow assumption, not checked by kn1_sides_out.txt.` Replace “S1 is exactly” by “S1 is sufficient.” Keep the final-flow estimate only in the precise g_K form derived in F6, with a sufficient, not exact, factor-two loss.
3. **Replace the consequential-constants paragraph** by `At the bare level a_{η,bare}=ε_1²/(27378N), hence a_{RS,bare}=ε_1²/N·min{1/27378,κ/256}. The plaquette branch is active iff κ≥128/13689 (equality is a tie); for κ=1 it is active throughout the admissible ε_1 range. At effective levels retain a_η from (PLD)_k(i). The kernel coefficient remains κ/(256N).` Delete 814.587.
4. **Replace the gain/consumer claims** by `At κ=1 the frozen RS bare-exponent gain over its old quadratic threshold is 82.1406 decades at ε_1=6.7e−40,N=2 (91.8478 at the stated proposed ε_1). Against the displayed joint linear bare/per-cube formula the comparison is 2.303258… decades, conditional on the inactive chart cap and applicable pricing hypotheses. Neither comparison changes the live v3 exponent a=min{θa_bad,a_A} by itself.` Delete the request to correct RLARGE:618 using a_RS and the unconditional “C2 discharged”/“adoption lands” claims. Scope this as a local Appendix-A corollary, not an automatic global threshold replacement.
5. **Qualify the reversal** by `η_KN/η_q≥256N/13, with equality iff δ_0≥ε_1/(256N).` Correct the direction of omitting a minimum entry. Preserve the old ordering statement as historical under its old η definition.
6. **Correct the supporting degeneracy result:** 633 is the `(y, axial-path)` count; 475 is the freely reduced full-path count with F1's weights. Convexity needs no distinct-path count and is unaffected.

This is a review rejection of the text as written, not a claim that re-centring is false or that the entire Yang–Mills programme is refuted. Remaining downstream source/consumer identification is an explicit GAP.

## Reproduction and read boundary

All new calculations used plain Python integers, `fractions.Fraction`, `itertools`, `collections`, and integer `math.factorial`/`math.isqrt`; no floating-point arithmetic, numerical libraries, or long-running jobs were used. No original check script was executed. Only this deliverable was written; no git command was run and no `.git` content was inspected.

The independent enumeration was:

```python
from itertools import product, permutations
from collections import Counter

labels, full = Counter(), Counter()
for y in product((-1, 0, 1), repeat=4):
    for sigma in permutations(range(4)):
        p = tuple((axis, y[axis]) for axis in sigma if y[axis])
        labels[(y, p)] += 1
        # mu=0; all paths start at the same block centre.
        raw = p + ((0, 1),)*3 + tuple((a, -s) for a, s in reversed(p))
        reduced = []
        for a, s in raw:
            if reduced and reduced[-1] == (a, -s):
                reduced.pop()
            else:
                reduced.append((a, s))
        full[tuple(reduced)] += 1
print(sum(labels.values()), len(labels), len(full))
print(sorted(Counter(labels.values()).items()))
print(sorted(Counter(full.values()).items()))
```

Actual outputs: `1944 633 475`; `[(1,384),(4,192),(12,48),(24,9)]`; `[(1,288),(4,96),(6,48),(12,12),(20,24),(48,6),(72,1)]`. The analytic derivation in F1 checks the enumeration independently.

For the decimal enclosures, π was bounded by the alternating rational series in Machin's identity 16 arctan(1/5)−4 arctan(1/239), using 40 terms and the next-term remainder for each. Exponentials at 1/4 and 1/2 used 32 rational terms and a geometric upper bound on the positive remainder. Square roots used integer square-root bounds with denominator 10^18. Logs used range reduction x=2^k m, 1≤m<2, followed by

    ln m = 2 Σ_{j=0}^{49} z^{2j+1}/(2j+1) + remainder,
    z=(m−1)/(m+1),
    0≤remainder≤2z^101/[101(1−z²)].

ln2 was bounded by the same formula, and ln10=3ln2+ln(5/4). All interval operations were rational; displayed endpoints were rounded outwards to 12 decimal places. The checked inequalities were e^{1/2}+e^{1/4}<3, 32π²/3<106, and (16π/3)(e^{1/4}−1)<11/2. These are mathematical enclosures, not two matching floating-point evaluations.

**Two additional files used:** `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/review-loop/SKILL.md`, for the supplied agent-entry requirements. The later user restrictions overrode their wider source/operational procedures. No PROOF, HIST, ARS_FIX, EPS1_SWEEP, snapshot, or audit-ledger file was opened. In particular, none of their quoted line numbers is certified here. All inspected RLARGE references were located within the six permitted ranges and the decisive ones were checked with original line numbers; its :65, :628, :830–835, :970–998, and :1020–1026 citations still match the inspected text. The label “§6” is itself ambiguous: live §6 at :623 is a status list, while Lemma RS is frozen Appendix-A §6; the patch must name the latter.

**Read-scope deviation disclosed:** an initial heading/location `rg` query on REVIEW_ARS_EPS_S1.md also returned table rows outside its authorized section 1 and summary table. That exceeded the requested excerpt restriction. Subsequent reads were limited to section 1 and the summary; no finding above depends on an additional proof from its other sections. Nevertheless, this run is **not fully compliant with the owner's read-scope rule**, and must not be presented as a clean procedural pass. The mathematical findings and reproducible calculations are provided with that limitation explicit.

## Summary table

| finding | review verdict | mathematical/status conclusion |
|---|---|---|
| F1: 1944 indices and 633 axial labels | CONFIRMED | PROVEN exact count and label weights |
| F1: 633 distinct transporters | REFUTED | 475 reduced full paths; straight-path weight 1/27; convexity preserved |
| F2: ε_1 crossover at 814.587 after adoption | REFUTED | Boundary is κ=128/13689, independent of ε_1,N |
| F3: a_RS forces correction of live :618 ceiling | REFUTED | Different exponent; these routes are retired for unreturned defects |
| F4: linear one-step threshold is mathematically available | CONFIRMED | PROVEN from the displayed local hypotheses by an independent trace-difference proof |
| F4: HIST's complete RS-lin/joint theorem and live use | NOT-VERIFIED | GAP for full source proof; claimed live unreturned-defect use contradicted by :433–439 |
| F5: paired-path/convex-mean local chain | CONFIRMED | PROVEN for the explicit quoted construction |
| F5: actual decision-4 identity, PROOF references, inherited symmetries | NOT-VERIFIED | CONDITIONAL source identification; no H1-F2 counterexample claimed |
| F5: norm bound iff probability weights | REFUTED | Convexity is sufficient, not necessary for a fixed dependent family |
| F6: c_KN, exact half identity, S1–S3 | CONFIRMED | PROVEN sufficient conditions; S1 uses conservative 106 |
| F6: all four side conditions verified by ~40 decades | REFUTED | S4 has no values/check; actual flow satisfaction NOT-VERIFIED |
| F6: exact universal factor-two flow cost | REFUTED | Exact fixed-step ceiling a/(B+aR); factor 2 is a sufficient final-coupling convention |
| F7: re-centred dichotomy and kernel coefficient κ/(256N) | CONFIRMED | PROVEN locally under the explicit mean, chart and kernel hypotheses |
| F7: effective a_η automatically equals its bare value | REFUTED | Effective estimate remains CONDITIONAL on (PLD)_k(i) |
| F8: 512/13, 768/13, 13/512, 201.029 and 452.315 | CONFIRMED | Correct on the stated inactive-cap/active-plaquette branches |
| F8: exact ratios are ε-free with the full η_q minimum | REFUTED | Use max{256N/13,ε/(13δ_0)} and its reciprocal |
| F8: 82.1406 / 91.8478 and N=3 figures | CONFIRMED | Correct evaluated gains over the old quadratic RS formula |
| F8: 2.303258 / 2.655441 are live programme gains | NOT-VERIFIED | CONDITIONAL historical formula comparison, not established live improvement |
| F9: gates certify the source interface/quotient | REFUTED | Source identity, removed minima and full transport degeneracy escape them |
| F9: original script implementations | NOT-VERIFIED | Not read or run; no code-level pass claimed |
| F10: append section 8.1 as written | REFUTED | **NO**; use the narrow replacement text in F10 |

**Single most dangerous unverified item:** whether the actual decision-4 normalized kernel uses exactly the paired indexed mean quoted in KN_ADOPT, and hence whether the proposed W' is its live S4′ coarse link. The local proof cannot authenticate that source identity. Separately, even with it authenticated, the live-v3 gain claim still fails by the explicit retirement of its proposed pricing consumer.
