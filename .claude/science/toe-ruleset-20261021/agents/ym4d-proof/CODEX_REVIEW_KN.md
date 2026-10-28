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

Likewise KN_ADOPT.md:699–703's claim that any reweighting or field dependence breaks three statements is false: arbitrary pointwise nonnegative normalized weights preserve the two norm bounds and the KN algebra. Covariance may require additional equivariance, but uniformity/field independence is not required for these pointwise inequalities.

