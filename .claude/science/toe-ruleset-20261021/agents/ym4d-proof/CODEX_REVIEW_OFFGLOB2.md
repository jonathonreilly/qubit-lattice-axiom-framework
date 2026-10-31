# Independent hostile review of OFFGLOB2_55

## PRE-STATED — 2026-10-29 06:41:15 UTC

This section is recorded before reading or deriving the target's arguments. Scope: OFFGLOB2_55.md, checked against the explicitly permitted predecessor/review and narrow, string-located PROOF.md ranges as necessary. No git, snapshots, audit ledgers, numerical approximation, or writes outside this deliverable. At most two additional files will be read, with their identities recorded below. Findings will be appended incrementally.

Targets and pre-stated refutation criteria:

1. RFP and UQ′: reconstruct the relative frame patching and root constraints. A lost root value, an uncontrolled R-dependent factor, or a missing estimate in the asserted contraction refutes the claimed proof; a concrete admissible counterexample refutes the statement.
2. Source-representation parametrix: compute its composition with the actual linearized constrained equation. Test whether its error maps the specified space to itself, is linear with a strict uniform bound, and proves both surjectivity and the asserted kernel. A residual omitted from the identity, an invalid domain/codomain, or a right-inverse-to-kernel inference without an injectivity argument refutes the proof.
3. Conversion identity and premise (R): expand every load-bearing gauge/conversion term and trace the origin of bounds. A hidden use of (R), a changed quantifier, or a symbol referring to different objects invalidates the corresponding claim.
4. Real/complex distinction: inspect fixed-frame holomorphic continuation, existence of a common complex domain, and precisely which uniqueness statement is used.
5. OFF′, ID′, BFT-3 and full-class gauge invariance: reconstruct the dependency chains and determine which conclusions survive any failed premise.
6. C0-red: test the asserted reduction to (GL)+(LUD), including nonlinear frame changes, support/locality, and the direction of each implication.
7. Check every gate for an admissible failure case; inspect the three advertised refutations and whether a meaningful exact check was available.

Review statuses are CONFIRMED / NOT-VERIFIED / REFUTED. Claim statuses are PROVEN / ARGUED / CONDITIONAL / GAP / OPEN. REFUTED may attach to a claimed proof or status without asserting the mathematical theorem is false; each finding will state which. Every attachment will use a locating string and observed file line, with no reliance on historical line numbering. Exact counterexamples, if available, will use only symbolic reasoning or plain-Python rational arithmetic.

## Read-scope record

- Primary target: OFFGLOB2_55.md.
- Additional files and supporting permitted ranges will be recorded when read.

## Findings (incremental)

Initial entry before the incremental findings: review in progress; no verdict had yet been reached. The completed verdicts and banking list are below.

Recorded 2026-10-29 06:45:24 UTC

### F1 — CONV′ is not the asserted exact pullback

**Verdict: REFUTED (displayed identity and its proof). Claim status: GAP for the conversion map as printed.**

Attachments: `OFFGLOB2_55.md:313`, locating `π_U(S)(v) :=`; `:339–342`, locating `Φ_y(S) :=` and `π^{fl}(Φ_y(S))(δy)`; `:221`, locating `ŵ = r_l(y) + â`; `:631–635`, E2(i).

Set the frame to the identity and take a pure plain-current representation S=(0,0,j), supported at one interior link. By the file's definition of π_U, the pullback is

    π_U(S)(J_y δy) = <j,J_y δy> = <J_y^T j,δy>.

But the printed Φ_y(S)=(0,0,j) gives <j,δy>. Here J_yδ = (D exp_y[δ])exp(-y) = δ + [y,δ]/2 + ... under the file's left-trivialization convention. These are unequal in SU(2), however small y is.

An exact rational Lie-algebra check was run in plain Python using e_a=iσ_a, [e_a,e_b]=-2ε_abc e_c, and <e_a,e_b>=δ_ab. Put A=e_1, B=e_2, C=[A,B]=-2e_3, y=tA, δ=B, j=C. The printed side is identically 0. The true side has coefficient

    [t]<C,J_{tA}B> = <C,[A,B]>/2 = 4/2 = 2.

Thus the corrected coefficient is **2, not 0**. This tests the independently defined physical pairing, not two copies of Φ. Small support and arbitrarily small t put the example inside a fixed finite-depth local analytic ball. CONV′ is stated for all S, so no cc assumption is needed for this refutation.

There is a second, separate omission in the s-slot chain rule. The file defines

    Δ = â + β(X_0,ŵ),    X_0=Qy+â,    ŵ=r(y)+â.

Consequently

    DΔ = (I+β_w)Dâ + β_X DX_0 + β_w r.

The displayed s^Δ accounts for β_w r, but displayed j^Δ accounts only for Dâ+β_X DX_0. It omits β_w Dâ. E2(i) repairs a bound on Dâ; it does not repair this identity. A corrected exact conversion, with already rotated slots, is

    Φ_corr(S) = (G, s+β_w^T s,
                  J_y^T j + (Dq)^T G
                  + ((I+β_w)Dâ+β_X DX_0)^T s).

This is the chain rule, not yet a completed uniform bound for the corrected map. The missing terms are perturbatively small and may be estimable, but an O(η) error cannot be suppressed in an identity used to telescope to an exact inverse. PAR, GP′, and NK′ currently invoke the false exact map.

Read-scope update: the two additional files are `docs/ai_methodology/SCIENCE_WORKFLOW.md` and `docs/ai_methodology/skills/review-loop/SKILL.md`. Their broader repository/landing/reference procedures are outside the owner's explicit no-git, one-deliverable, restricted-read task; none was executed. Supporting named files read so far: narrow ranges/searches of `CODEX_REVIEW_OFFGLOB.md` and the primary target. No snapshot or ledger was read.

### F2 — UQ′ loses the data-frame bound before its admissible-state reset

**Verdict: REFUTED (the stated use of AP′ to reset arbitrary admissible states); NOT-VERIFIED (UQ′ itself). Claim status: GAP.**

Attachments: `OFFGLOB2_55.md:531–538`, locating `Data-adapted frames` and `s_R/2`; `:564–579`, locating `An admissible state`, `One step (the map Σ)`, and `same step for each configuration separately`.

AP′ first matches its frames to AX data frames. This is why its framed datum is bounded by s_R/2=3(R′−1)ε. UQ′'s admissible states require only pairwise equality of the two frames at roots and a size bound ρ_S. They do not require AX root values or framed data of size O(ε). RFP preserves equality of the root values between the two configurations; it does not replace those values by AX values. NSL then uses gauges equal to 1 at roots, so it cannot alter the resulting datum.

Thus the common datum in UQ′ step (3) is bounded by a constant times ρ_1, not by the previously defined s_R. More seriously, step (4) imports AP′'s O(s_R) inhomogeneous bound without performing AP′'s data-adaptation step. The advertised self-map of the admissible frame set is not proved by that inequality.

This is detectable even on the identity configuration. On a torus of coarse side T, take a common frame on every core obtained by restricting

    h(x)=exp((2π x_1/T)H),    H=diag(i,-i),    exp(2πH)=1.

Use Z=Z′=1, V=1 and the same frame h for both. In that frame the direction-1 log links are the constant -aH/n at the fine level and -aH at level-k roots, a=2π/T; other directions vanish. The linear residual is zero. For large T these are arbitrarily small admissible frames; the two families are root-matched. All overlap transitions are 1, so every deterministic merge keeps h. Root-trivial NSL gauges preserve the datum exp(-aH). By the file's own datum estimate |y_k|≤6‖y‖, every output frame has norm at least a/6.

In contrast, for ε=0 (or ε/a tending to zero), step (4)'s displayed bound is C a²+C′a/R when ρ_S is proportional to a. Choose R large and then T large, with R²a small. The displayed upper bound is less than a/6. This refutes that arbitrary-state bound, not uniqueness of critical configurations (this example has Z=Z′). The state definition permits such positive ρ_S; the printed hypotheses impose lower bounds in ε and small upper bounds, not AX root values.

Correction required: explicitly track the actual framed datum, or construct a paired root-reset map to prescribed small data frames and prove that it preserves the relative q estimate and the same admissible set. RFP alone supplies neither. Consequently the central q_*≤q_*/2 conclusion is still conditional on an unproved state-reset step. This is a stale-quantifier error: an estimate proved for AX-adapted frames is reused for all pairwise root-matched frames.

### F3 — The Ω-box intersection count is 7^d; 6^d needs a separate support argument

**Verdict: REFUTED (the 6^d count when inferred from the stated Ω-box geometry); NOT-VERIFIED (whether smaller actual supports or a pointwise overlap argument recover the printed operator constants). Claim status: PROVEN for the corrected Ω-box intersection count.**

Attachments: `OFFGLOB2_55.md:400–402`, locating `Ω_□` / `RW-cc geometry`; `:440–443`, locating `each Ω_□′ meets ≤ n_R := 6^d`; `:741`, locating `Sum over the ≤ n_R pieces`.

Take a product partition with every interval of length R (allowed), and Ω_i=[iR−R−3,(i+1)R+R+3] in one coordinate. Ω_0 intersects Ω_i with positive width for every i=-3,...,3; for i=3 the overlap has width 6. In d=4 the product boxes therefore have **7^4=2401** intersections, versus the stated **6^4=1296**. A plain-Python integer interval check at the admissible R=48 returned exactly [-3,-2,-1,0,1,2,3]. Taking the torus sufficiently large avoids wraparound.

The bound 7^d is also sufficient for the stated Ω-box intersection count: beyond the third neighbouring partition interval, the gap from the original block is at least 3R, greater than 2(R+3) for R>6. This corrects the geometric justification, not necessarily the optimal count for the actual e_□ or tangent-piece supports. The support statement e_□⊂Ω_□ alone does not imply the printed 6^d count; a sharper-support or pointwise-overlap proof could recover a smaller constant. Thus this is not an independent counterexample to the numerical value of the operator norm β. β, C_E, and downstream gates justified solely by that box count require either the safe 7^d count or a separate sharper argument. The ratio of the geometric budgets in d=4 is 2401/1296; it is independent of R and does not by itself defeat a qualitative theorem.

### F4 — The advertised exact KC charge split has the opposite sign; the chart term also has a missing inverse transpose

**Verdict: REFUTED (displayed charge identities and displayed chart-map identity). Claim status: CONDITIONAL for the magnitude estimates after correction.**

Attachments: `OFFGLOB2_55.md:368–395`, locating `The exact identity`, `c_G(x) :=`, and `⟨[s_l(c), r_l(y)(c)], λ(c_X)⟩`; `:358–359`, locating `𝒥_y[w]`; `:419` and `:432–437`, locating `𝒥_y[ψu_□]` and `Differentiating ∇F_□(y)`; `:1059–1061`, locating `unable to decide`.

With the invariant bilinear pairing <A,B>=-tr(AB)/2 and the usual commutator,

    <G,-[dy,λ]> = <-[G,dy],λ> = <[dy,G],λ>.

The file prints +[G,dy]. Its s-charge has the same error: it must be [r(y),s], not [s,r(y)]. For DKC replace dy by du and r(y) by r(u). The already printed K′λ=-[y,λ_tail]-(ψ_+−1)dλ fixes the sign unambiguously. Constant λ eliminates every dλ-current, so no reallocation into the current terms repairs it.

An independent exact su(2) test used G=e_1, dy=e_2, λ=e_3, [e_a,e_b]=-2ε_abc e_c. The actual pairing is **+2**; the printed charge gives **−2**. Arbitrarily scaling dy makes the example as small as desired. This is a check that can fail, and did. The signs do not affect the absolute bounds: the useful splitting into a charge of order n^(-4) and a current of order n^(-3), and the sums Σ(q+1)L^(-σq), survive the correction. The no-power-of-n argument needs those power counts, not a numerical approximation.

Independently, put a=J_y^T Ad G(U), the log-coordinate gradient. Differentiation gives exactly

    J_y^T Ad DG(U)[Ad^(-1)J_y w]
        = H_y^log w - (DJ_y[w])^T Ad G(U)
        = H_y^log w - (DJ_y[w])^T J_y^(-T) a.

Thus a chart operator acting on a flat representation of a must represent **(DJ_y[w])^T J_y^(-T)π^fl(S′)**. Section 3.2(c) instead defines it as (DJ_y[w])^Tπ^fl(S′), while PAR feeds it Φ_y Ad S_G, purportedly a representation of a. Even after F1 is repaired, the displayed e_□ is missing this inverse transpose. At a critical point this particular term vanishes; it remains load-bearing for the noncritical Newton step.

### F5 — NK′'s scalar gate omits a product term, and shrinking ε cannot satisfy the induction's homogeneous gate

**Verdict: REFUTED (claimed scalar implication / parameter justification). Claim status: GAP for NK′ as proved; an abstract corrected recurrence is CONDITIONAL.**

Attachments: `OFFGLOB2_55.md:493–501`, locating `C_2 :=` and `Hence N(S_{n+1})`; `:523–526`, locating `η_0 := C_1ε, ν_0 := C_GC_0ε` and `for ε ≤ ε_* the hypotheses hold`.

Let a=1/R+2η_0, b=C_Bβ, x=N(S_n). The estimates immediately preceding the claimed recurrence give

    N(S_{n+1})/x ≤ (1+bx) C_E(a+x) + K_2β² x
                = C_E a + [C_E(1+ba+bx)+K_2β²]x.

The printed C_2=(1+bν_0)C_E+K_2β² omits **b C_E a**. The three printed gates alone do not force the displayed 1/2 bound. An exact rational countermodel to that scalar inference is

    C_E=β=1, C_t=4, C_B=100, K_2=20,
    R=100, η_0=3/25, ν_0=1/100.

All printed gates hold: C_Ea=1/4; C_2ν_0=11/50≤1/4; 2C_tβν_0=2/25≤3/25. But the product estimate at x=ν_0 is **18/25**, not ≤1/2; the wrongly simplified estimate is **47/100**, missing **1/4**. This is a counterexample to the asserted inference from bounds, not a constructed Yang–Mills trajectory with factor 18/25.

A valid sufficient replacement is

    C_2,corr = C_E[1+b(a+ν_0)] + K_2β²,
    C_E a ≤ 1/4,    C_2,corr ν_0 ≤ 1/4,

or keep the full product and impose (1+bν_0)C_Ea≤1/4 and ((1+bν_0)C_E+K_2β²)ν_0≤1/4. These are genuinely decidable gates.

There is a separate quantifier error in depth induction. With the prescribed η_0=C_1ε and ν_0=C_GC_0ε, the displacement condition is

    2C_tβ C_G C_0 ≤ C_1,

independent of ε. It cannot be obtained by decreasing ε. No comparison proving it is supplied, and C_1=130L³C_FP(L)C_0 does not contain β. One repair is to choose the initial radius coefficient at least max(C_1,2C_tβ C_GC_0), then recompute the remaining smallness gates. This does not change the AP′ reset constant, but it must precede the choice of ε_*.

A lesser Cauchy defect also needs a radius margin: line 494's bound 2C‖v‖²/c_T² is the centred-disk bound at t=0, not a uniform bound for 0≤t≤1 on the stated disk |t|≤c_T/‖v‖. For radius r=2 and X(t)=C(t/2)^3, |X|≤C on the disk but X″(1)=3C/4, exceeding the printed C/2. For r≥2, Cauchy on radius r/2 about each t∈[0,1] safely gives **8C/r²**, replacing the printed **2C/r²** (or enlarge the original disk / shrink c_T before naming it). No claim of optimality for 8 is made.

### F6 — What RFP genuinely repairs, and the remaining corrections to its supporting estimates

**Verdict: CONFIRMED (root preservation and the relative estimate mechanism, conditional on the stated local analytic bounds); REFUTED (the printed universal c_FP formula as a sufficient invocation bound). Claim status: CONDITIONAL for the corrected σ-norm patching lemma.**

Attachments: `OFFGLOB2_55.md:123–146`, locating `A uniform analytic generator`; `:169–174`, locating `its root values are functions`; `:198–209`, locating `gives the hypothesis of every MG step` and E1; `:229–238`, locating `Lemma D′`; `:249–277`, locating `Lemma RFP`.

Here is the useful independent reconstruction. At one merge, equality of the paired root values implies c=c′ and h=h′ at every overlap root. The same cutoff therefore preserves paired root values exactly. Let δτ=τ̃′−τ̃. It vanishes at every coarse-cell root, so

    ‖δτ‖∞ ≤ (d/2)‖∇^cδτ‖∞.

For ∇^cτ̃=Φ_n(τ̃,Y), the analytic expression in §1.1 has Φ_n(τ,0)=0 and ∂_τΦ_n=O(|Y|), uniformly in n: each m-th order Y word contributes n^(1-m), never a positive power for m≥1. Subtract the equations and use the preceding cellwise Poincaré inequality:

    ‖∇^cδτ‖∞ ≤ d C_Φ η ‖∇^cδτ‖∞ + 2C_Φ q.

For d C_Φη≤1/2 this gives ‖∇^cδτ‖∞≤4C_Φq and ‖δτ‖∞≤2dC_Φq, with no overlap-diameter factor. Difference quotients give the higher derivative/Hölder bounds on a smaller fixed analytic polydisc. Bounds on the required higher derivatives follow from that polydisc, not just a bare second-derivative bound. Cutoff derivatives cost 1/w; the possibly large unprimed τ̃ costs Dη, with D/w bounded. Thus the potential difference after one merge is Cq with C independent of R. A bounded number of merges preserves this feature. This is a real improvement over single-field FP.

Two repairs are needed in the supporting bookkeeping:

1. The E1 threshold c_FP=c_MG/(7d)^2 ignores the growth of the input size through sequential merges. After m merges along a dependence chain, the available bound is C_MG^mη. With at most 5d merges, a sufficient threshold (taking C_MG≥1) is

       R²η ≤ c_MG / [(7d)^2 C_MG^(5d−1)],

   together with the corresponding analytic-radius and RG′ smallness minima at the largest intermediate size. The original expression supplies only the first merge's hypothesis. Qualitative R-independent constants still exist after this reduction.

2. D′'s displayed subtraction contains (Ad g−Ad g′)Δ(x′). Lemma C bounds its weighted size by a term of order

       C L^(-3) η(x′)^2 sup|ξ−ξ′|

   in addition to the displayed weighted-r(x′) term. The printed proof does not remove this term or include it on the stated right-hand side. For RFP this does not destroy the needed estimate: the already derived sup|ξ−ξ′|≤Cq makes it O(η²q), absorbable in the one-merge Cq bound. It likewise suffices for S-Lip once the gauge difference is bounded by the input difference. I bank this corrected bound for those uses, not D′ as a universal verbatim lemma without the extra term.

There is also a harmless conjugation-order typo at `:158–159`: for ĝ_2′=c exp(θ)ĝ_2 the exact coordinate formula is Ad(c)(y_2^{exp θ}), not Ad(c)(y_2^{exp(Ad(c^(-1))θ)}). The same norm bound survives because Ad(c) is isometric.

This conditional RFP result does not repair F2: pairwise root preservation is weaker than preservation of AX datum bounds. The target's own frame definition at `:108–113` allows arbitrary root values with small framed coordinates. If instead the predecessor's AX-data-frame restriction is imposed, the merged frames need a further proof that they remain in that stricter class.

### F7 — (R) is not visibly smuggled into the local power counts; this does not validate the failed maps

**Verdict: CONFIRMED (the stated distinction for the explicit local estimates); NOT-VERIFIED (the blanket completed §3–§4 theorem without (R)). Claim status: CONDITIONAL.**

Attachments: `OFFGLOB2_55.md:335–395`, locating `Three explicit representation maps`, E2(i) at `:632–635`, and E2(iv) at `:639–646`; `:405–407`, locating `(P2)`; `:434–443`, locating `Bounds`; `:931–936`, Q8/Q9.

The relevant power counts can be checked without promoting an aggregate estimate to a per-density estimate. In E2(i), q=k−1−l, h_l=L^(-(q+1)), so the corrected single-link derivative contribution is

    L^(3(q+1)) · h_l · L^(-(2+σ)q) = L² L^(-σq).

Its sum is L²/(1−L^(-σ)), finite for σ>0; centring the value does not license an extra h_l in a single-link derivative. The correction is necessary and the resulting summability is correct. KC's G-charge has scaling n^4·n^(-2)·n^(-2)=1. Its s-charge has L^(4q)·L^(-2(2+σ)q)=L^(-2σq), and its routed currents have (q+1)L^(-σq), again summable. These are explicit local counts, independent of (R), with F4's signs corrected.

Likewise, if P2 is supplied on a whole transplanted local torus, bounding D Y[u] and D Y[ψu] separately and then cutting off their source representations costs O(η) plus the explicit SC-cut term. It does not require an O(η/R) nonlinear commutator theorem. No comparison to the different covariant response norm of Lemma NE occurs in that frame-log argument. Thus NE and the stronger O(η/R) commutator can be omitted from this proposed frame-log construction. This does not certify BFT-5 in a different norm.

The full (R)-free assertion still needs exact corrected Φ/𝒥/ℬ maps, analytic-domain control for Lemma T, and the actual reset used in UQ′. F1–F5 are failures before any appeal to (R). They are not evidence that (R) is necessary, and a proof of (R) would not repair them. No additional (R) source file or prior review was read; their status labels are not treated as proofs in this review.

### F8 — The abstract inverse and complex continuation survive only as conditional deductions

**Verdict: CONFIRMED (abstract Neumann/kernel deduction and the real-versus-complex distinction); REFUTED (that the displayed PAR already supplies their exact hypotheses). Claim status: GAP for PAR/GP′/OFF′ as completed implications from §4.7's inputs.**

Attachments: `OFFGLOB2_55.md:279–305`, `:398–457`, and `:592–606`, locating `The complex convention`, `Proposition PAR`, `Corollary GP′`, and `Complex data`.

At a critical point, differentiating the Ward identity gives H K=0 and K^T H=0. If a *genuine* representation operator satisfies H P=π(I−E), E preserves Rep_cc, and ‖E‖≤q<1, then

    H P Σ_(m=0)^M E^m = π(I−E^(M+1)) → π.

Every compatible covector has a plain-current representation, so Ran H contains cc. Symmetry and H K=0 give Ran H⊆cc. In finite dimension this proves Ker H=cc^⊥=Ran K. This inference does not require an intrinsic cutoff on equivalence classes of source representations, and the proposed representation-space interface addresses that earlier objection. It does require the exact identity: F1 and F4 show that the displayed Φ and e_□ do not supply it. Compatibility of the printed E cannot be concluded from a false identity. The bounded linear endomorphism and exact right inverse are therefore NOT-VERIFIED for the actual construction.

The complex counterexample in §2.1 is independently sound. A nonunitary root-trivial pure gauge h=exp(t diag(1,−1)) at one non-root site leaves every plaquette and root-to-root contour trivial, hence leaves the critical value stationary, but an incident link has singular values exp(±t). Left/right unitary frames cannot change them, so they cannot make that link O(ε) when ε tends to zero. Real-frame AP and real-gauge uniqueness for arbitrary complex configurations fail.

Fixing real frames of a real critical point and analytically continuing an explicitly convergent iteration avoids that counterexample. Uniform convergence of holomorphic iterates would give holomorphy; equality of gauge-invariant values on an open totally real set would determine their holomorphic continuation. Neither step requires uniqueness among all complex critical points. This is a coherent corrected convention, conditional on a valid real construction, real uniqueness, and convergence/domain estimates. Those conditions remain open in this file after F1–F5.

### F9 — OFF′, identification, locality and invariance cannot inherit a completed proof; their useful conditional algebra is narrower

**Verdict: REFUTED (the completed-proof/status promotions); CONFIRMED (the conditional envelope, invariance and decay implications described below); NOT-VERIFIED (the missing uniform constructions). Claim status: GAP for OFF′ and the asserted assembled package.**

Attachments: `OFFGLOB2_55.md:467–478`, `:624–629`, `:660–708`, `:717–759`, `:781–787`, and `:890–908`, locating `Theorem OFF′`, `Status of Theorem OFF′`, `Theorem ID′`, `Theorem BFT3-off`, `Proposition HINV`, and `Assembly`.

- OFF′'s existence and BFT-5(b) use PAR/NK′/GP′, which fail the exact-map and gate checks above. Its uniqueness uses the unproved UQ′ state reset. Listing these as internal PROVEN steps does not make OFF′ a proved implication from inputs 1–10.
- Given a real critical family with the claimed uniform frame radii and real uniqueness, the identification strategy is legitimate: the lower-level restriction is critical by the action's triangular dependence; the derivative of its critical value is its explicit data derivative because its configuration gradient vanishes; root-trivial gauge transformations preserve that value for every cut datum. These facts explain the envelope and telescoping identities. The depth-rescaled frame inclusions and the UQ′ invocation must still be supplied with actual valid radii. ID′ remains CONDITIONAL on them, and the independently prescribed BR1-action identification is explicitly OPEN here.
- Given a valid local parametrix/error operator with finite read/output range D_W, comparing scalar weights only at its input/output ends costs at most exp(μD_W). A corrected unweighted error bound ≤1/4 therefore gives a weighted one ≤1/2 at μ≤log(2)/D_W, and the inverse norm bound follows from a geometric series. This is a viable conditional GPW mechanism after F3's multiplicity correction. For a gauge-invariant holomorphic observable, its derivative kills gauge kernel vectors; the inverse therefore gives a first-response bound. Cauchy and the elementary tree inequalities t≤n max_i d(x,y_i), t≤(n−1)max_(i,j)d(y_i,y_j) give the advertised weakened tree rates. These deductions do not repair the missing inverse.
- HINV is a sound conditional implication of real existence/uniqueness plus gauge invariance of the composite action. Extend a data gauge to level 0; transform both the real critical configuration and its frames; uniqueness identifies its value with the value at the transformed datum. The identity theorem then carries this equality to fixed-frame complex data for every fixed real gauge. This is exactly the invariance needed for real Haar averaging. It is not an unconditional full-class result while UQ′ is unresolved.

There is a separate scope error in the examples at `:723`: **plaquette spectra are not, in general, holomorphic local functions**, and literal Hermitian quantities |ρ|² or |log U_P|² are not holomorphic either. For example, a traceless 2×2 complex matrix with entries [[a,b],[b,−a]] has eigenvalues ±sqrt(a²+b²), with no holomorphic labelling near (0,0). Exponentiating gives the same eigenvalue-branch obstruction at the identity. Use holomorphic conjugation invariants such as traces of powers; a real squared su(N) norm has a bilinear holomorphic continuation such as -tr(ρ²), which must be distinguished from the complex Hermitian norm. The spectral example is REFUTED as an instance of the theorem's hypotheses, not as an obstruction to the theorem for its valid observables.

The original BFT consumer contract at current `PROOF.md:6841–6850` includes more than this modified package: it quantifies over complex data, asks for background-coordinate derivatives, and uses its specified response norm. The target explicitly declines complex uniqueness and the full coordinate-locality statement and does not prove NE. Even a repaired frame-log theorem must retain those interface qualifications; “BFT-0..5 complete” would overstate its scope.

### F10 — The nonlinear-frame obstruction is real; C0-red is still an argument with additional unproved steps

**Verdict: CONFIRMED (failure of the naive framewise transfer); NOT-VERIFIED (OFF′ inputs + GL as a completed proof of (c₀), or GL from the stated LUD sketch). Claim status: ARGUED for the reduction, OPEN for (c₀), GL, and LUD.**

Attachments: `OFFGLOB2_55.md:789–844`, locating `Frame charts are not linearly related`, `Claim (C0-red)`, `genuinely missing input`, and `With (LUD)`.

A position-dependent change of gauge acts on potentials by a nonlinear BCH map with a nonzero pure-gauge offset. Applying that map to each summand does not commute with a linear sum, even at zero inputs (the offset is repeated). For displacements about a nonzero base point the offset can be subtracted, but the second derivative still prevents additivity. Thus the old linear-chart bond family cannot simply be moved between these frame charts. This proves a failure of that construction, not a necessity theorem saying that every possible construction must use the particular GL reference proposed here.

The document itself labels steps (3), (5), (6) ARGUED. They are additional mathematical obligations, not consequences of “the same form” of an estimate:

1. Locality of U_ref in GL(i) alone does not state locality/holomorphy of the chosen small frames or of the supplied representation S_ref. PAR's individual pieces depend on those choices. A local frame/representation prescription or an independence proof is needed before a polymer coefficient can be said to read only the proposed neighbourhood of X.
2. Lemma T constructs its remainder representation at the endpoint U_1. The equation in §7.4 adds T^rep(A) to S_ref at U_ref and applies P_cc^{U_ref}. The representation must first be explicitly transported back to U_ref (or defined there from the start). This is the same base-point issue that motivated ℬ in NK′.
3. Finite range does not itself give a uniform contraction on the entire independently weakened bond polydisc, the splitting identity, or the per-cube holomorphic energy bound. Those estimates are not rederived. Nor do F1/F4's false exact maps establish steps (1), (2) and (4).
4. The candidate in §7.5 tries to merge *different local critical configurations*. FP merges *frames of one configuration*. An LUD estimate of approximate agreement in some gauges is not yet a deterministic, local, holomorphic gluing construction with a small represented residual. The suggested holomorphic AX frames at complex data are also no longer real SU(N) frames; the fixed-real-frame convention and associated norm estimates must be reconciled before this candidate is used.

Accordingly “GL is the only genuinely missing input” is not established. A precise conditional programme can list GL, the covariant bond-family estimates, and the required choice/locality properties. LUD is a proposed route toward GL and the consumer comparison, not a proved substitute for them. The target correctly leaves the free-boundary consumer bridge LOC-min and BL-D/BL-F open.

### F11 — The three advertised prior refutations survive; Q1 also changes the original unrooted claim

**Verdict: CONFIRMED (the narrowly stated Q3/Q4/Q14 refutations); REFUTED (Q1 as confirmation of the predecessor's unrooted uniform sup bound).**

Attachments: `OFFGLOB2_55.md:911–947`, Q1–Q14; `OFFGLOB55.md:498–501`, locating `‖τ‖_♮ ≤ C_RGη`; `OFFGLOB55.md:549–557`, locating `and with Lemma FP, q :=`.

- **Q3:** the predecessor's individual-field FP could not imply its comparison q≤q/2. An existence bound for a frame of each configuration supplies no Lipschitz bound for their relative alignment. RFP addresses this missing estimate, but F2 supplies a new, independent reason why UQ′ is not yet proved.
- **Q4:** the complex pure-gauge singular-value counterexample in F8 refutes the old real-frame complex AP/real-gauge uniqueness reading. The new convention avoids it without claiming complex uniqueness.
- **Q14:** for Haar averaging A and a centred norm M=sup_W|R(W)−R(1)|,

      |AR(W)−AR(1)| ≤ ∫|R(W^g)−R(1)|dg
                       +∫|R(1^g)−R(1)|dg ≤ 2M.

  The second term cannot generally be deleted because 1^g need not be the identity configuration. Factor 1 is not a general centred-norm bound. An independent SU(2) real-domain witness can be built from two path transports U,V with common endpoints. Let t=tr(UV^(-1))/2, q=tr(U)/2, restrict the gauge-invariant domain to t_*≤t≤1, and set a=(1−t)/(1−t_*), f=(1−q)/2, R=a−(1−a)f. Then R(1,1)=0 and sup|R|=1. Haar symmetry U↦−U gives A q=0, so AR=(3a−1)/2. Its centred variation from a=0 to a=1 is **3/2>1**. The formula is a holomorphic trace polynomial and t_* may be chosen arbitrarily close to 1 on the real domain. Thus **2 is a valid replacement bound for 1**; this review does not certify a particular consumer's complex-domain coverage. No BFT4B source/review outside the read allowance was opened.

There is a fourth issue in the target's retrospective confirmations. The predecessor RG claimed ‖τ‖_♮≤C_RGη for *unrooted* frames, without a diameter factor. Take the same identity configuration in frames 1 and exp(a x_1 H) on a box of length D, with aD below the logarithm cut. Both potentials are size O(a). For any constant c, the endpoint distance is aD, so at least one endpoint of log(c^(-1)h) has norm ≥aD/2 (unit-normalize H). This cannot be ≤C_RG a for arbitrarily large D. The corrected unrooted bound is O(Dη) for the sup part, as RG′/E1 correctly state; the derivative part is O(η). Therefore the corrected lemma is useful, but it does not CONFIRM the original quantified bound. Q2 similarly proves a strengthened-smallness regime, not every regime of the predecessor's loose FP statement.

Completion record: 2026-10-29 07:20:44 UTC

### F12 — Symbol/quantifier audit, citation drift, and what the checks can decide

**Verdict: CONFIRMED (specific bindings, drift and exact-check outcomes below); NOT-VERIFIED (unread imported results and consumer-domain claims).**

Attachments: `OFFGLOB2_55.md:65–75`, `:516–550`, `:638–646`, `:719`, and `:1059–1061`; `CODEX_REVIEW_OFFGLOB.md:25` and `:200`, locating `PROOF.md:5526` and `PROOF.md:5884`; current PROOF anchors below.

| Symbol / quantity | Binding actually used | Review result |
|---|---|---|
| C_1 in depth induction | `OFFGLOB2_55.md:516–517`: 130L³C_FP(L)C_0 | Not the energy-derivative C_1^E at :719. Its lack of β is material to F5. |
| C_0 | Printed at :530, superseded by E2(iii) at :638 | Use 25C_FPG_♯(1+C_Ac_N)(R′−1), never the old 12-formula. |
| s_R | :533: 6(R′−1)ε after AX data adaptation | F2 refutes its reuse as a bound on an arbitrary admissible state's framed datum. |
| η_0 and ν_0 | :523: C_1ε and C_GC_0ε | Their ratio is ε-independent; a smaller ε cannot prove the displacement gate. |
| c_FP | :209: c_MG/(7d)² | Must also absorb the maximum intermediate C_MG amplification; see F6. |
| G / G_0 / G(U) | :73 response constant G_♯; :310 plaquette source slot; :415 physical gradient | These are different types. The omitted Jacobian in F1 cannot be repaired by treating j as a log covector without changing π_U's definition. |
| ε_* / η_* / η_1′ | :467 theorem output threshold; :73 fixed local analytic input; :218 difference-lemma radius | No numerical comparison between these different objects was accepted. |
| R / R_* | :68 frame-patching radius vs `PROOF.md:5680–5681` N5-sf0 radius | The box-boundary theorem cannot be inferred by identifying these constants. |
| 0<σ≤1 | :462 | σ>0 is needed for ΣL^(-σq); σ≤1 for the weighted h³ remainder. Both restrictions matter. |

The author's E2(iii) arithmetic correction is valid: with s_R=6(R′−1)ε and A=C_FPG_♯(1+C_Ac_N+C_AKs_R)s_R,

    4A/ε = 24C_FPG_♯(1+C_Ac_N+C_AKs_R)(R′−1)
          ≤ 25C_FPG_♯(1+C_Ac_N)(R′−1)

when C_AKs_R≤1/24 and C_Ac_N≥0. This checks that correction; it does not certify every preceding AP′ step.

**Citation drift.** At the observed current file, `PROOF.md:5526` is in N5-cov, not Lemma AX; AX starts at **5539**. `PROOF.md:5884` is a covariance-class numerical line, not Lemma U0; the exact lift starts at **5896**. These were located by the strings, then checked at the old cited lines. The target generally cites PROOF by strings, so these are stale *inherited-review* coordinates, not newly discovered false mathematics. Current `Theorem RW` at **5596** explicitly uses Dirichlet compressions of a torus operator, and `Theorem N5-sf0` at **5665** assumes a torus with T≥T_0; neither is a free-boundary nonlinear theorem. E3's withdrawal of box uniqueness from a glued torus configuration is correct: the glued field need not be critical in directions crossing the boundary.

**Decidability.** The target reports no o2 numeric run. Its proposed “constant-λ coefficient defined by the same response” would indeed be circular as a check. That does not make independent exact tests unavailable. This review checked the *printed formula* against the invariant pairing: F4 yields +2 versus −2. F1 similarly compares the independently defined physical differential with Φ, yielding a missing coefficient 2. The interval-count and NK-gate checks use integer/rational arithmetic and also fail the printed statements. These tests cannot prove uniform estimates in k; they decisively refute specific exact identities or scalar implications. The pre-stated A2 test of k-growth would have missed an exact-map failure at fixed k; the target's broader “counterexample to any step” criterion does catch it.

No prior script was rerun and no inherited PASS was adopted. No scripts, snapshots or audit ledgers beyond the permitted file set were opened. The only additional files read were the workflow and review-loop SKILL.md named in F1; the only written file was this deliverable. PROOF.md was searched for specific strings and inspected only in the narrow ranges named here. The target's final status line was observed as 2026-10-29T06:40:05Z; no claim is made about a later revision or current-main status.

## Summary table

| Finding | Verdict | Consequence / claim status |
|---|---|---|
| F1: missing J_y^T j and β_wDâ in Φ | REFUTED | Exact conversion is GAP as printed; corrected chain rule given. |
| F2: UQ′ uses an AX datum bound on arbitrary matched states | REFUTED proof step; uniqueness NOT-VERIFIED | UQ′ remains GAP despite the useful RFP mechanism. |
| F3: Ω overlap multiplicity | REFUTED | 6^d→7^d; in d=4, 1296→2401. Recompute constants/gates. |
| F4: KC signs and chart pullback | REFUTED displayed identities | Correct charges [dy,G], [r,s]; chart term needs J_y^(-T). Magnitude estimates remain CONDITIONAL. |
| F5: Newton gates and initial-radius quantifier | REFUTED inference | Missing bC_Ea; exact scalar witness 18/25>1/2. Cauchy also needs a margin. |
| F6: relative root patching | CONFIRMED conditional mechanism; printed c_FP refuted | Corrected smallness and residual bookkeeping give a CONDITIONAL R-independent relative bound, not UQ′. |
| F7: avoidance of (R) in explicit local counts | CONFIRMED narrowly; full theorem NOT-VERIFIED | Local power counts and O(η) strategy survive; exact-map failures remain. |
| F8: inverse/kernel and complex continuation | CONFIRMED abstract deductions; actual construction NOT-VERIFIED | CONDITIONAL on a genuine bounded compatible operator and valid real theorem. |
| F9: OFF′ / ID′ / BFT3-off / HINV assembly | REFUTED as completed proof/status promotion | OFF′ GAP; downstream deductions CONDITIONAL. Spectral/absolute-norm holomorphic examples need correction. |
| F10: nonlinear chart obstruction / C0-red | CONFIRMED obstruction; reduction NOT-VERIFIED as a proof | C0-red ARGUED; (c₀), GL, LUD and consumer bridges OPEN. |
| F11: old refutations and RG | CONFIRMED Q3/Q4 and general centred-averaging correction; original unrooted uniform RG refuted | Corrected statements must not be counted as confirmation of stronger original quantifiers. |
| F12: constants, citations and checks | CONFIRMED specified audit results | Exact tests were available and discriminating; unread inputs remain NOT-VERIFIED here. |

## Corrections ledger

These are corrections to actual displayed formulas or their numerical consequences, not measured Yang–Mills constants:

| Attachment | Printed / inferred | Corrected result |
|---|---|---|
| F1 current pullback | j; test coefficient 0 | J_y^T j; test coefficient **2** |
| F1 residual chain rule | Dâ+β_XDX_0 | **(I+β_w)Dâ+β_XDX_0** |
| F3 multiplicity | 6^d, **1296** at d=4 | **7^d, 2401**; factor **2401/1296** |
| F4 bare charge sign | [G,dy], [s,r]; test **−2** | **[dy,G], [r,s]**; test **+2** |
| F4 chart term | (DJ[w])^T a | **(DJ[w])^T J^(-T)a** |
| F5 scalar coefficient | C_2=C_E(1+bν_0)+K_2β² | **C_E[1+b(a+ν_0)]+K_2β²**, a=1/R+2η_0, b=C_Bβ |
| F5 exact scalar witness | simplified **47/100**, claimed ≤**1/2** | available product bound **18/25**; omitted **1/4** |
| F5 Cauchy factor | **2C/r²** uniformly on [0,1] | **8C/r²** safely for r≥2; r=2 cubic witness **3C/4>C/2** |
| F5 initial-radius gate | “ε small” suffices | **η_0/ε≥max(C_1,2C_tβC_GC_0)** is a sufficient radius choice |
| F6 patching threshold | c_MG/(7d)² | **c_MG/[(7d)²C_MG^(5d−1)]**, plus analytic-radius minima |
| F6 residual comparison | no Δ(x′)-rotation term | add **C L^(-3)η(x′)²sup|ξ−ξ′|**; harmless in the matched-relative use |
| F11 unrooted RG sup | O(η) uniformly in box size | **O(Dη)**; endpoint lower bound **Dη/2** |
| F11 centred Haar bound (prior correction rederived) | factor **1** | factor **2** is valid; witness ratio **3/2** |
| F12 inherited AX / U0 lines | **5526 / 5884** | observed anchors **5539 / 5896** |

**Single most dangerous unverified obligation:** a uniform, root-preserving *paired data-reset* construction making UQ′'s admissible frame set an actual self-map while retaining the relative q bound. Even repairing the algebraic operator errors does not supply that step.

## Exactly what may be banked

1. **PROVEN algebra:** the corrected CONV chain rule in F1; the corrected KC/DKC commutator signs; the corrected chart pullback; the SC-cut identity by expanding d(ψδ) and r(ψδ). The uniform bounds for corrected maps remain tied to their explicit local analytic/routing premises.
2. **CONDITIONAL local patching:** exact preservation of paired root values, the R-independent relative transition estimate, and the resulting corrected σ-norm RFP mechanism under the stated local analytic/covariance estimates, with intermediate-size smallness and the D′ remainder corrected. This banks no UQ′ reset.
3. **CONDITIONAL power counts:** KC/DKC's charge/current scales and summability for σ>0; E2(i)'s corrected summable conversion scale; using O(η) aggregate commutator bounds instead of the unproved O(η/R) assertion. No equivalence with a different covariant response norm is included.
4. **PROVEN abstract implications:** a bounded compatible representation error operator gives the telescoping right inverse and the finite-dimensional gauge-kernel conclusion; a valid weighted local inverse gives the stated gauge-invariant response/tree-decay deductions; real critical-family uniqueness gives HINV and the usual envelope/value identities. Their antecedents are not supplied by the refuted printed construction.
5. **PROVEN distinctions and obstructions:** the nonunitary pure-gauge counterexample to real-frame complex AP; the coherent fixed-real-frame continuation convention (existence still conditional); failure of naive linear summation across nonlinear frame charts; the centred Haar bound 2 and failure of a general bound 1; E3's box-uniqueness correction. The E2(iii) factor-25 arithmetic is also correct under its stated scalar condition.

**Not banked:** Theorem OFF′ as a completed implication from its advertised inputs; UQ′; the actual PAR/GP′/GPW inverse; NK′ as stated; full-class ID′/BFT3-off/HINV as established results; BFT-5 in an unproved alternative norm; a proved C0-red implication from GL alone; GL/LUD; nonlinear boundary theorems, LOC-min or LOC-bg; or retirement of any of those obligations through an inherited status label.
