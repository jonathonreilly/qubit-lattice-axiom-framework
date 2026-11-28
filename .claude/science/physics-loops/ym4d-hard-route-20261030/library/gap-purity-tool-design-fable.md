lead: anthropic/claude-fable-5-2 laptop subagent
Started Sat Nov 28 14:46:39 UTC 2026, pinned at commit 883c3bff2. Author only, checked by no one.

# Gap purity: tool design (FINISH row 1701)

## 0. Plan (written first, save protocol)

1. Phase 1. Read the inputs named in the brief.
2. Design the chain of tools. For each link: input, deliverable, field, status, cost, trusted base.
3. Name where the running coupling and C_A > 0 enter. Name where the chain can die and the cheapest kill test.
4. Build the first component.
5. Apply the (Y4) filter to the chain output and to the first component. Give the U(1) failure.
6. Phase 2. Compare each link with `library/open-registry.md` and the record.

**Outcome in one paragraph (written last).** The chain I designed in Phase 1 is: a cutoff-uniform count of states at a short physical time (from the renormalisation-group account), then a hypercontractive bound for the vacuum chain of the neutral transfer operator at a physical rate, then one interpolation lemma that spends the two and gives the purity. Phase 2 found the whole chain ON FILE: rows 931, 940, 978, 981, 982, 984, 988 (Lemma IHC, Corollary CU, (TH), (HC-phys)). My first component is Lemma IHC again, in the units of the purity consumer. It is a variant, not progress. The open link is the same one: (HC-phys). No producer for it is designed here beyond its interface. I did not find a new tool.

## 1. Reading done, and what was missing

Read in full: the crux card; `gap-purity-y4-solve-fable.md` (row 1696); `gap-purity-rh-strategy-fable.md` Part 4; `gap-purity-rh-strategy-fable-check-astra62.md` section 4 (the precise (Y4)); `gap-purity-strategy-mine-fable.md` section 4.3; `gap-purity-afield-astra62.md` sections 7-8; the RESULT texts of rows 1682-1700 in FINISH.md. Lean, statement level only: `Purity.lean` L25-L29, `PurIo.lean` L24-L27, L172-L181, L348-L356, `Stage0.lean` L151 (`betaAt`), L228-L231 (`ExpClusters`).

Missing at the time of reading (no RESULT in FINISH.md): rows 1686, 1689, 1697, 1699, 1700. Row 1691 is a Lean reproduction row with no result text. I read `gap-purity-afield-astra62-check-opus.md` only through its RESULT in row 1698. Row 1686's file was in the checkout; I read its RESULT line in Phase 2 only. Row 1700's file landed during the run; see section 2.

## 2. Correction from the lead during the run (check 1700)

The lead sent a correction. I read lines 85-109 of `library/gap-purity-y4-solve-fable-check-astra62.md`. Row 1696's claim that a proof MUST read C_A through a threshold slope β*(n) FAILS as an inference. What survives: with B(n) the supremum of the fixed-box passing set, B(n_K) ≥ β_K at passing indices. It gives no interval, slope or group dependence. My brief stated the withdrawn premise ("a proof must read C_A > 0 through how the threshold coupling β*(n) moves").

Where this design relied on the premise, and what I did:
- Section 3.4 (where C_A enters). My first draft read the cutoff-uniform rate as a threshold β*(n) with slope 11/(3π²). That reading is now marked GUESSED and is not used. The chain asks for estimates at the selected couplings β_K only. It needs no interval of couplings and no monotonicity in β.
- Section 3.5 (the coupling-integral identity). That route integrates over every coupling in [0, β_K] on the fixed box. So it does ask for an interval. It was already outside the chain; it stays outside, with this note.
- The check also records n ≥ 2^2800 at K ≥ 70 (L ≥ 2^40). I use no number of this kind.

## 3. Phase 1: the design (written from the Phase 1 inputs only; Phase 2 verdicts are in section 6)

### 3.1 The measurement in thermal form

Setting (ARGUED from `Transfer.lean`, as in row 1696 section 2; check 1700 reports an operator mismatch at lines 26-32 of that file, so I keep this as a hypothesis, not a Lean fact). T is the transfer operator of the cube Γ of side n. It is positive, self-adjoint, trace class, with a continuous strictly positive kernel. P₀ is `neutralProj`; it commutes with T. Let λ₀ be the top eigenvalue of T and Ω its eigenvector.

(F0) PROVED from the hypothesis. A strictly positive continuous kernel on a compact space gives a simple top eigenvalue with Ω > 0 everywhere (Jentzsch's theorem, CITED: classical, no page). Each centre shift maps Ω to a positive top eigenvector, so P₀Ω = Ω.

Put Z₀(t) = tr(P₀Tᵗ), E(t) = Z₀(t)/λ₀ᵗ − 1 ≥ 0 and X(t) = log(1 + E(t)). E is non-increasing in t.

(F1) PROVED. purity(u) = (1 + E(2u))/(1 + E(u))² ≥ (1 + E(u))⁻². So X(u) ≤ h/2, with h = log(625/457), gives purity ≥ 457/625.

(F2) PROVED. Let π = Ω² dx and (Pf) = Ω⁻¹ (P₀T/λ₀)(Ωf). P is self-adjoint on L²(π), preserves positivity, and P1 = 1. Its s-step kernel p_s(x, y) with respect to π ⊗ π is non-negative and symmetric, with ∫p_s(x, y)π(dy) = 1. For integers s ≥ 1: 1 + E(2s) = tr P^(2s) = ∫∫ p_s(x, y)² π(dx)π(dy). So E(2s) is the mean chi-square distance from π of the chain started at a π-distributed point, at lag s.

In words. The target says: at temperature 512/ℓ the neutral thermal state has excited weight E(u) at most 25/√457 − 1 (about 0.169). Row 1693 proved that a gap does not bound this count. So the tool must control a trace. That fixes the design problem: find a currency that (a) tensorises over the volume, so that an extensive count costs only its logarithm, and (b) is uniform in the cutoff.

### 3.2 The chain (three links)

Notation. Q(t) := sup{q ≥ 2 : ‖Pᵗf‖_(L^q(π)) ≤ ‖f‖_(L²(π)) for all f}. This is the hypercontractive exponent of the neutral vacuum chain at lag t.

| Link | Takes in | Must deliver (exact) | Field | Status | Cost and trusted base |
|---|---|---|---|---|---|
| 1. COUNT | The renormalisation-group account (Sussman-Alpoge release on Balaban's method): stability bounds for torus partition functions, uniform in the cutoff | ∃ S_* < ∞ (depending on L, M, g₀, ℓ only), ∃ K₀, ∀ K ≥ K₀, ∀ Γ of side n = ℓL^K, with u = n/512 and s₀ = u/4: X_Γ(2s₀; β_K) ≤ S_* | Constructive field theory (ultraviolet stability) | Must be ADAPTED: a two-sided stability bound with one vacuum-energy subtraction for all time extents, on a box that may lie above the range of the account | By hand, at the level of the account. No Lean. Trusted base: the release's stability theorems |
| 2. SPEND | S_* from link 1 and Q from link 3 | Lemma HCP (section 4): if s₀ + t ≤ u/2 then purity ≥ exp(−(4/Q(t))·X(2s₀)). So Q(u/4) ≥ 4S_*/h gives purity ≥ 457/625 | Markov chains and constructive field theory (Nelson; Gross; Diaconis and Saloff-Coste) | PROVED here by hand (section 4). ON FILE as Lemma IHC (section 6) | By hand: done. Lean: Hölder for L^p, Hilbert-Schmidt norm as a kernel integral, Jentzsch for (F0) (I do not know that Mathlib has Jentzsch; UNVERIFIED). Trusted base: Lean kernel and Mathlib |
| 3. CONTRACT | The Wilson law at β_K on the cubes of side ℓL^K | ∃ K₀, ∀ K ≥ K₀, ∀ Γ of side ℓL^K: Q_(Γ,β_K)(u/4) ≥ 4S_*/h. Rate form: ∃ ρ > 0, free of K and of ℓ, with Q(t) ≥ 1 + exp(2ρ t L^(−K)) | To be INVENTED. Sources tried in thought: Bakry-Émery with Ric(SU(2)) > 0; two-scale log-Sobolev criteria; finite-size mixing criteria | INVENT. This is the wall | Unknown |

Arithmetic of the budget (PROVED, it is arithmetic). With the rate form, Q(u/4) ≥ 4S_*/h holds when 2ρ·(ℓ/2048) ≥ log(4S_*/h), that is ρℓ ≥ 1024·log(4S_*/h), in the units where L^(−K) is the spacing. If S_*(ℓ) grows at most like a power of ℓ and ρ is free of ℓ, this holds for every large ℓ. The consumer asks for one ℓ. So CONTRACT needs no numerical size. It needs positivity of ρ, uniform in the cutoff and in the volume.

Why COUNT must sit at a physical time (ARGUED). For one Gaussian mode Nelson's exponent is exact: Q(t) = 1 + e^(2ωt) (CITED: E. Nelson, "The free Markoff field", J. Funct. Anal. 12 (1973) 211-227; theorem number UNVERIFIED). So Q is governed by the lowest mode. A count taken at a lattice-scale time grows like a power of n, and its logarithm grows like K. The rate cannot pay that at a fixed physical ℓ. The count must be taken at a fixed fraction of u.

### 3.3 The final output against the (Y4) filter

1. Box and law. L, M, g₀ and ℓ (1024 | ℓ) fixed first; n = ℓL^K, u = n/512, β = β_K; periodic links, the eight-term projection. Observable: Q_(K,Γ) := Q(u/4) of the neutral vacuum chain. PASSES as a specification.
2. Sign and size. s = +1, reference q_K = 4S_*/h with S_* from COUNT (fixed before K). Estimate asked: Q_(K,Γ) ≥ 4S_*/h for all late K (an all-late bound). PASSES as a specification. NOT PROVED.
3. Use of the gain. D := −log purity ≤ 2X(u) ≤ (4/Q(u/4))·X(u/2) ≤ 4S_*/Q ≤ h. PROVED (Lemma HCP). Information beyond the seed: CONTRACT implies a gap, E₁·t ≥ ½ log(Q(t) − 1) (PROVED, section 4, N1), and a gap does not give the purity (row 1693). I do not show that the purity bound implies CONTRACT. So CONTRACT with COUNT is a sufficient condition that is strictly stronger than a gap. It is not shown weaker or easier than the seed.
4. Group and dimension tests. Lemma HCP and COUNT are group-blind; both hold for U(1). The tests fall on CONTRACT alone:
   - Weak 4D compact U(1), cosine action, three half-turn cuts, same aspect: by N1, CONTRACT needs E₁·u ≥ 2 log(4S_*/h − 1). In the massless phase E₁·n stays bounded (ARGUED from the free photon; CITED for the phase: Guth 1980; Fröhlich and Spencer 1982, references from memory, UNVERIFIED), so E₁·u is at most of order 1/512, and S_* is at least the photon count at twice the temperature, which is large (ARGUED). CONTRACT FAILS for U(1) by its necessary condition.
   - Pin(2) at weak coupling; 2I and Q₈ at large β; SU(2) on a box of small physical size: the gap times the side tends to zero or the flat sectors are degenerate (row 1696, Theorem SUB and Theorem SV; ARGUED at fixed physical size). CONTRACT fails by N1.
   - Weak 5D SU(2): conditional on a gapless phase, CONTRACT fails by N1. Conditional comparison only.
   - Strong coupling: CONTRACT is expected for both groups at small β (ARGUED). So a failure for U(1) at weak coupling is dynamical. It is not algebra alone.
   - Neutral spectator: Q of a product chain is the minimum of the two exponents, and X adds. A spectator with many low states lowers Q or raises S_*. The premise detects it. PROVED for products (tensorisation of hypercontractivity, CITED classical).
   - The line of the estimate where a non-commuting weight gives the gain: NONE WRITTEN. This is the item the filter asks for and the chain does not have. The chain FAILS (Y4) item 4 at this point. It is a candidate with its decisive inequality open.

### 3.4 Where the running coupling and C_A > 0 enter

Only in link 3, and only as a requirement. The rate ρ must be positive in physical units at the selected couplings β_K, uniformly in K and ℓ. Links 1 and 2 do not read the group.

Row 1696 found two statements that read the Lie algebra with the sign of C_A: Ric > 0 on the group, and b₀ > 0. A producer for CONTRACT would have to use one of them at the physical scale. My first draft said that C_A must appear as the slope 11/(3π²) of a threshold β*(n). After check 1700 this is GUESSED and not used (section 2). What I can say without it: a group-blind producer is impossible, because CONTRACT is false for U(1), Pin(2) and the finite groups by N1.

### 3.5 An exact identity outside the chain (kept for the record)

Lemma INT (PROVED from the trace formula Z₀(t; β) = (1/8)Σ_k ∫exp(−βA_(k,t)), ARGUED as in row 1696). For a fixed box and u: D(β) := −log purity = ∫₀^β [⟨A⟩_(2u,b) − 2⟨A⟩_(u,b)] db, where ⟨A⟩_(t,b) is the mean total action in the neutral ensemble of period t at coupling b.
Proof. d/dβ log Z₀(t) = −⟨A⟩_(t,β). At β = 0 the transfer operator is the projection on the constants, so Z₀(t; 0) = 1 and D(0) = 0. ∎
This is the integral method of lattice thermodynamics (CITED from memory, UNVERIFIED: Engels, Fingberg, Karsch, Miller, Weber, Phys. Lett. B 252 (1990) 625). It turns the trace ratio into a difference of one local expectation between two tori. It needs a bound at every coupling in [0, β_K]. So it meets every bulk feature of the Wilson axis below β_K, and any proof through it must fail for a mixed fundamental-adjoint weight with a first-order line (ARGUED). It is an identity, group-blind, and equivalent to the seed as an estimate. Not a candidate.

### 3.6 Where the chain can die, and the cheapest kill tests

1. At CONTRACT. It contains the gap at fixed physical size (N1). No producer is known. Expected death point.
2. At COUNT. The account may not give a two-sided bound with one subtraction on a box of non-perturbative size. Kill test KT-A, a reading row with no computation: find in the release the statement that bounds X at a fixed physical time uniformly in K, and its range of box sizes. (Phase 2: row 981 did this reading. One input, a "determinant lemma", was not located.)
3. CONTRACT may be false for SU(2) although the gap is positive. A gap does not give hypercontractivity in general. Kill test KT-B, by thought or by a published-data reading: the persistence test N2 of section 4. If some slice event B has P(X_t ∈ B | X₀ ∈ B) > π(B)^(1/2 − 1/q) at t = u/4 and q = 4S_*/h, CONTRACT is false. Candidates for B: a region held in a metastable state; a slice of high energy density. I found no violating event (ARGUED; SU(2) slices carry no conserved flux in the neutral sector).

KT-A is the earliest test. It costs one reading row.

## 4. The first component: Lemma HCP (hypercontraction of the count to the purity)

**Setting.** (X, π) is a probability space. P is a self-adjoint operator on L²(π) that preserves positivity, with P1 = 1. For one integer s₀ ≥ 1, P^(s₀) has a kernel h ≥ 0 in L²(π ⊗ π): (P^(s₀)f)(x) = ∫h(x, y)f(y)π(dy). Then h is symmetric and ∫h(x, y)π(dx) = 1 for almost every y. Put 1 + E(2s) := ‖P^s‖²_HS for s ≥ s₀.

**Lemma HCP. PROVED.** Let t ≥ 0 be an integer and q ≥ 2 with ‖Pᵗf‖_q ≤ ‖f‖₂ for all f ∈ L²(π). Then

    1 + E(2(s₀ + t)) ≤ (1 + E(2s₀))^(2/q).

**Proof.** (i) Duality. P is self-adjoint, so ‖Pᵗg‖₂ ≤ ‖g‖_(q′) with 1/q + 1/q′ = 1: for f with ‖f‖₂ = 1, ⟨f, Pᵗg⟩ = ⟨Pᵗf, g⟩ ≤ ‖Pᵗf‖_q‖g‖_(q′) ≤ ‖g‖_(q′).
(ii) Interpolation. Fix y and put g = h(·, y). Then g ≥ 0 and ‖g‖₁ = 1. With θ = 2/q, 1/q′ = (1 − θ)/1 + θ/2. Hölder's inequality gives ‖g‖_(q′) ≤ ‖g‖₁^(1−θ)‖g‖₂^θ = ‖g‖₂^(2/q).
(iii) The kernel of P^(t)P^(s₀) is (x, y) ↦ (Pᵗh(·, y))(x). So ‖P^(s₀+t)‖²_HS = ∫‖Pᵗh(·, y)‖₂² π(dy) ≤ ∫(‖h(·, y)‖₂²)^(2/q) π(dy) ≤ (∫‖h(·, y)‖₂² π(dy))^(2/q), by (i), (ii) and Jensen's inequality for the concave map x ↦ x^(2/q). The last integral is ‖P^(s₀)‖²_HS. ∎

**Corollary PUR. PROVED from (F0)-(F2) and Lemma HCP.** For the neutral vacuum chain of section 3.1, let u be even, s₀ ≥ 1, t ≥ 0, s₀ + t ≤ u/2, and ‖Pᵗf‖_q ≤ ‖f‖₂ for all f. Then

    purity(u) ≥ exp(−(4/q)·X(2s₀)).

In particular q ≥ 4X(2s₀)/log(625/457) gives purity(u) ≥ 457/625.
Proof. E is non-increasing, so X(u) ≤ X(2(s₀ + t)) ≤ (2/q)X(2s₀). Then (F1). ∎
(u = n/512 is even when 1024 divides ℓ.)

**Two necessary conditions for the hypothesis. PROVED.**
N1 (gap). If ‖Pᵗf‖_q ≤ ‖f‖₂ for all f, then every eigenvalue μ of P other than the top one has |μ|ᵗ ≤ (q − 1)^(−1/2). Proof: for a bounded real eigenfunction g with ∫g dπ = 0 and ‖g‖₂ = 1, put f = 1 + εg. ‖Pᵗf‖_q² = 1 + (q − 1)ε²μ^(2t) + o(ε²) and ‖f‖₂² = 1 + ε². Let ε → 0. (Eigenfunctions of an operator with a bounded kernel are bounded; in general use a truncation.) ∎
N2 (persistence). Under the same hypothesis, for every event B with π(B) > 0: P(X_t ∈ B | X₀ ∈ B) ≤ π(B)^(1/2 − 1/q), for the stationary chain. Proof: f = 1_B/π(B)^(1/2) has ‖f‖₂ = 1. ⟨1_B, Pᵗf⟩ ≤ ‖1_B‖_(q′)‖Pᵗf‖_q ≤ π(B)^(1 − 1/q). The left side is P(X₀ ∈ B, X_t ∈ B)/π(B)^(1/2). ∎

**Weaker hypothesis that suffices (PROVED by the same proof).** The bound ‖Pᵗg‖₂ ≤ ‖g‖_(q′) is used only for g = h(·, y), π-almost every y.

**Exact check, as a guide (python3 -I, fractions; not a proof step).** Product of N symmetric two-point chains with eigenvalue r. By Bonami's inequality (CITED classical) ‖Pᵗ‖_(2→q) ≤ 1 if and only if r^(2t)(q − 1) ≤ 1. The lemma reads (1 + r^(2(s₀+t)))^(Nq) ≤ (1 + r^(2s₀))^(2N). Checked exactly on 1740 cases (r ∈ {1/2, 1/3, 2/3, 9/10}, t ≤ 7, even q ≤ 64, s₀ ≤ 5, N ∈ {1, 3, 50}): no violation. Example: r = 1/2, t = 1, q = 4, s₀ = 1, N = 1: (17/16)⁴ = 83521/65536 ≤ 25/16. For small r^(2s₀) the two sides differ by a factor near 2, so the lemma is sharp up to that factor.

**(Y4) filter applied to the first component.** Lemma HCP is the spending inequality of item 3. It is group-blind and holds for U(1). It has no gain of its own. Alone it FAILS items 2 and 4, as every consumer lemma does. And it is ON FILE (section 6). It is not progress.

## 5. The tool that is missing

The chain has one unbuilt link, CONTRACT. I state its interface for a later row; I do not have a method.

Producer interface (what a tool for CONTRACT must take in and give out). Input: the Wilson law at β_K on Γ. Output: one of
(a) Q_(Γ,β_K)(u/4) ≥ 4S_*/h for all late K; or
(b) the weaker kernel form: ‖P^(u/4)p_(u/4)(x, ·)‖₂ ≤ ‖p_(u/4)(x, ·)‖_(q′) for π-almost every x, with q = 4S_*/h.
Tests it must pass: N1 and N2 as necessary conditions; failure for U(1), Pin(2), 2I and small boxes (section 3.3).

Sources considered in Phase 1, each with its death point (ARGUED):
- Bakry-Émery on the slice space. Needs a lower bound for the Hessian of −log Ω². Row 1696 records that it dies at the tilt by the ground state and is blind to the scale.
- A two-level step (coarse chain hypercontractive, fine fibres hypercontractive, then the full chain). The simple version needs the fine variables at time 1 to depend on the coarse past only through the coarse present. The block chain does not have this property. No lemma found.
- A finite-size mixing criterion checked by exact computation. The block must be larger than the correlation length at a coupling where the account still works. That block is far beyond exact computation. Dies on cost.

So the honest state is: the design reduces the choice of currency (a hypercontractive exponent, which tensorises and is uniform in the cutoff for free fields). It does not supply the estimate.

One buildable item that I did not build: a Lean statement of Corollary PUR against `purity`, as a third plug-in beside `passingCutoffs` and `ExpClusters`. `grep -i hypercontract` over `lean/gapchain/GapChain/*.lean` finds nothing. It would be a consumer only. I do not recommend it before a producer exists.

## 6. Phase 2: each link against the record

Method. Keyword counts over `library/open-registry.md` and `library/` (grep, bounded), then the RESULT lines and the quoted passages of the nearest files. The registry has no line with "hypercontract", "Nelson", "Doob", "ultraviolet stab" or "integral method". The record is in the attack files.

| # | Item of this file | Nearest record, quoted in a phrase | What differs | Status |
|---|---|---|---|---|
| 1 | Lemma HCP | Row 978, `gap-ladder-max.md` section 5.1, Lemma IHC: "X(2s + 2m; B) <= theta_m X(2s; B), theta_m := 1 - tanh(alpha m) = 2/(1 + e^(2 alpha m))"; checked by rows 981 and 979 ("IHC and 5.6(a) HOLD") | Nothing. With q − 1 = e^(2αm), 2/q = θ_m. The proof is the same three steps (duality, Hölder between L¹ and L², Jensen). | ON FILE |
| 2 | Corollary PUR (the constants 4/q and h for the neutral purity at u = n/512) | Row 978 Corollary CU, for the seed S < 1/5041 on the cube (2n)³; row 1682 C3 "(HB)", `gap-purity-strategy-mine-fable.md` L174: "no supplier of a log-Sobolev inequality for π is known at the physical scale" | The units of the present consumer (P₀, 457/625, u = n/512). | variant in units |
| 3 | (F2), chi-square form of the trace | Row 931, (5.3): "1 + S(2s; B) = E_(u ~ nu) ||p_s(u, .)||_2^2" | Here with P₀ inside the chain. | ON FILE |
| 4 | Link COUNT | Row 978 (TH): "there is Theta < infinity, independent of iota, and ... an even integer t_0 <= tau_0/a_iota with X_iota(t_0; B) <= Theta"; row 981: "(TH) from the account HOLDS AFTER CORRECTION ... OPEN: the 'determinant lemma'" | Nothing. My KT-A is the reading that row 981 did. | ON FILE, one input open |
| 5 | Link CONTRACT | Row 982, `gap-hcphys-max.md` L30: "(HC-phys): there is M_H > 0, free of iota"; RESULT: "The crux lemma (UNIT) failed by three routes ... no counterexample"; row 988: "(U1) and (U2) are NOT proved" | Nothing. | ON FILE, OPEN |
| 6 | N1 (gap is necessary) | Row 978 remark: "Lemma IHC changes the constant in front and never the rate"; row 983: "the spectral necessity M_H <= m_0++" | Nothing. | ON FILE |
| 7 | N2 (persistence test) | Not found in the files of rows 931-988 (grep "persistence", "rare event" in the four hypercontractivity files: no hit). 45 other files hold the word; not read | A one-line necessary condition. Not a gate instance. | not found as stated (bounded search) |
| 8 | Tests for U(1), frozen groups, small box, mixed weight | Row 978 table: "Free photon (FP)", "Compact U(1)", "Frozen Q_8 and 2T", "SMALL-BOX", "K7 (mixed weight, first-order line ending near (1.48, 0.90))" | Nothing. | ON FILE |
| 9 | Lemma INT | Row 1686 RESULT: "the coupling-integral identity with the sign of (D-beta) and (AF-step) (rows 708, 858)"; row 1682 E7: "integral method"; row 988 Identity G | Nothing. | ON FILE |
| 10 | Nelson exactness, the count at a physical time | Row 940: "one Gaussian mode returns Nelson's exponent q - 1 = e^(2 omega m) exactly"; row 978 (R2): "K_a grows like 3 log(1/a) + log beta in physical units" | Nothing. | ON FILE |
| 11 | Published-data refutation test of the rate | Row 983: "does NOT REFUTE any hypercontractive rate M_H <= m_0++" | Nothing. | ON FILE |

Verdict of Phase 2. Every link of the chain is on file, with the same death point. The chain is rows 931-988 written again in the units of the purity consumer. The only item not found is N2, a small necessary condition.

## 7. Labels and limits

- PROVED here (by hand, one author, checked by no one): (F1), (F2), Lemma HCP, Corollary PUR, N1, N2, the budget arithmetic, Lemma INT. Each rests on the hypothesis of section 3.1 on the kernel of T (ARGUED, not checked in Lean) and, for INT, on the trace formula (ARGUED).
- CITED: Lean lines of section 1; lane rows and file lines of section 6 (read in bounded context; I did not read any Phase 2 file in full); Jentzsch, Bonami, Nelson (classical; theorem numbers UNVERIFIED).
- ARGUED: every statement on U(1), Pin(2), the finite groups, five dimensions and strong coupling in 3.3; the death points in 3.6 and 5; that S_* grows at most like a power of ℓ.
- GUESSED: that CONTRACT is true for SU(2); the threshold-slope reading of 3.4 (withdrawn as a necessity by check 1700).
- UNVERIFIED references from memory: Engels et al. 1990; Guth 1980; Fröhlich and Spencer 1982; Nelson 1973 (page range).
- Computation: one exact rational check of Lemma HCP on product chains (python3 -I, fractions, run inline, no file kept). Guide only. No Lean run. No floating-point step.
- Not done: a producer for CONTRACT; a Lean statement of Corollary PUR; a full read of the Phase 2 files; the (Y4) dimension test beyond a conditional sentence.
- By the lane's rule on written proofs, nothing here may land as a proof note in this state.

RESULT: Row 1701 (Claude Fable 5.2, laptop; author only, checked by no one). Chain: a cutoff-uniform count of states at a physical time (account), a hypercontractive exponent of the neutral vacuum chain (to invent), and an interpolation lemma that spends both to give the purity. First component: Lemma HCP with Corollary PUR, proved by hand; it is Lemma IHC of row 978 in purity units, ON FILE, not progress. Every link is on file (rows 931-988); (HC-phys) stays open; no new tool found. C_A enters only as a requirement on the open link; the threshold-slope premise is withdrawn (check 1700). Earliest kill test: the reading for the count's missing determinant lemma; then persistence test N2.
