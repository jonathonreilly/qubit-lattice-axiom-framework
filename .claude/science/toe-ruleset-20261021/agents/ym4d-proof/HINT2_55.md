Reviewer model: claude-opus-5-5

# HINT2_55 — the non-freeness witness, repaired: the comparator side for the observable actually used, the Yang–Mills side as named bounds, and the soft-branch inputs

Worker file (Opus 5.5, worker role; the binding rules of REVIEW_BRIEF_55 apply). This worker writes only this file and
`checks/h2_55_*` (the pre-existing `checks/h2_{constfield.py,criteria.md,out.txt,time.txt}` belong to an older, unrelated
HIST.md check and are not touched). No git. Append-only after this PRE-STATED block. Labels: **PROVEN-HERE** (complete
argument written here), **CONDITIONAL** (implication proven here; every input named with owner file and owner's status),
**ARGUED** (reason given, hole named), **OPEN**, **IMPORTED-standard** (textbook fact, named, not re-derived), **[m]**
(literature from memory, not re-read). Statuses quoted from other files are those files' labels unless this file says it
re-derived them. Line numbers drift; citations carry a locating string.

## PRE-STATED (written 2026-10-29T01:51:41Z UTC, before any criteria file, script or written derivation of this file)

*Provenance.* Before this block I read: REVIEW_BRIEF_55 (all); HINT55.md (all 603 lines); CODEX_REVIEW_HINT.md (all 293
lines, including "Exactly what may be banked"; its last line is complete); UIR55.md (all; it is still at its PRE-STATED
block); FLOW55.md §0-§1 and §7-§12; CODEX_REVIEW_FLOW55.md (its verdict lines and "Exactly what may be banked", by grep).
Exploratory reasoning, not written down, preceded this block. It covered: the pairing formula for the one-point function of
the comparator's quadratic energy density; a matrix-valued (colour) spectral class; a scalar generalised-free-field example
of a non-canonical identification; and a preliminary hand evaluation of the order-e⁴ ultraviolet logarithm of ⟨E(t)⟩ for a
centred Gaussian su(N) connection pushed through the NONABELIAN flow (preliminary value: −Nξe²/(16π²)·log(t/s₀) times the
tree value, ξ the Gaussian's gauge parameter). That value is a hypothesis to be tested here, not a result.

*Symbol pins (systemic defect 1), fixed now.* t = continuum flow time; f_ω(t) := t²ω(E(t,0)); 𝓔 := t²E. e_a, e² =
comparator couplings (not the lane's E_k, E_2, not Euler's e — written exp where needed). ξ = gauge parameter of a Gaussian
connection's covariance (δ − (1−ξ)p̂p̂)/p²; α₀ = gauge-fixing parameter of the flow (Lüscher's). M = a positive semidefinite
COLOUR matrix (not FLOW's M-cubes, not Balaban's M). (F-tune), β_±, R_F, U_±(m), u_k, m := K − k, t^{(m)} := c_tL^{−2m} as in
HINT55 §"Symbol table". (UIR^♮), (UNIV-1L), (SF-g), (RLF-δ), (SF-cont), (SF-∞) as in FLOW55 §0/§8.

**Targets.**
- **T1 (comparator side covers the observable as realised).** (a) The exact one-point formula for the comparator's flowed
  energy density, for ANY law (Gaussian or not) with finite second moments and any positive semidefinite colour metric — the
  correct argument for a one-point function of a composite, not a composite Källén–Lehmann statement. (b) Repair the
  unequal-colour normalisation: a colour class defined by matrix-valued (or every-positive-contraction) spectral data, closed
  under every linear colour map; show Codex's counterexample is excluded; transfer KLM, UV-D, SEP. (c) Exact f(t) and its
  t-dependence for canonical Maxwell fields with any colour coupling matrix, Proca fields with colour-dependent masses,
  generalised free fields, contact representatives, and mixtures. (d) Coverage of every Euclidean representative whose
  linear-field two-point function agrees with a class member at non-coincident points. (e) "Free nonabelian-colour fields":
  decide whether the nonabelian flowed density is an observable of a free abelian theory; compute (or fail to compute) the
  order-e⁴ logarithm for the Gaussian-connection realisation and its α₀-independence. (f) State what no one-point witness
  can do (identification; bounded observables), with explicit examples.
- **T2 (Yang–Mills side).** Name the bounds on t²⟨E(t)⟩ at short flow time that the RG must deliver; prove
  H_int ⇐ (F-tune) + (named bounds) with every link stated (including Codex's semicontinuity correction and an inter-scale
  step for continuous t); connect (F-tune) to FLOW55's reduction ((UIR^♮) + layer-1 inputs); say which named bounds no
  existing layer-1 statement supplies.
- **T3 (soft-branch inputs).** Verdicts on (NOISE-ADD), (ANTI-♭) and its route (β)/(W-AF2_r), and whether the bare-observable
  witness or the deterministic S4c branch needs them.

**What would count as a refutation (fixed now).**
- Of the one-point formula: a law in the class, finite second moments, with ω(𝓔(t,0)) ≠ the pairing formula.
- Of the colour repair: a member of the repaired class and a linear colour map (or positive colour metric) leaving the class,
  or a member with finite ultraviolet liminf and f(t₀) > liminf.
- Of an exact value: an exact-arithmetic mismatch, or a designed-FAIL control that does not fire.
- Of the Gaussian-connection coefficient: dependence on α₀ of the logarithm of ⟨E⟩ (E is α₀-independent configuration by
  configuration, so a correct computation must give an α₀-independent coefficient), or disagreement with an independent
  re-evaluation; if I cannot make the α₀ test, the coefficient stays ARGUED.
- Of an obstruction example: failure of its positivity/reflection positivity, of its claimed monotonicity, or of its claimed
  rate.
- Of the reduction: an input used but not listed; a constant depending on the cutoff K or the torus; an input that is H_int
  restated (a lower bound on a quantity that already separates Yang–Mills from the comparator class).
- Of a T3 verdict: an explicit model in which the claimed implication fails (or holds, for a claimed failure).

**Checks planned.** Ids `h2_55_<x>`; `checks/h2_55_<x>_criteria.md` written before each script; exact rational arithmetic
(`fractions`) and exact symbolic algebra (`sympy`, pure Python) only, no floats in any verdict; nice 10; each with a
designed-FAIL control. Planned: h2_55_a (comparator one-point values, colour repair, Codex's counterexample, Proca/GFF
monotonicity at rational points), h2_55_b (Gaussian-connection order-e⁴ logarithm: tensor contractions and the
α₀-independence test), h2_55_c (obstruction examples: scalar GFF identification, wrapped-normal monotonicity),
h2_55_d (reduction arithmetic with the inter-scale step). Ids may be added; none removed.

---

## RESUMED 2026-10-29T02:46:10Z

Resumed by claude-opus-5-5 (same model ID as the first line; no extra model line needed). The draft above stops at the end
of its PRE-STATED block: no derivation, criteria file or script of this deliverable existed at resume time (only the four
older `checks/h2_{constfield.py,criteria.md,out.txt,time.txt}`, which this file does not touch). Everything below is new.
The PRE-STATED targets, symbol pins and refutation criteria above are adopted unchanged. Before writing below I re-read the
inputs named in the brief (listed in §R0).

### §R0. Inputs re-read by this run, and the Codex verdicts used (agree/disagree stated explicitly)

*Read before any derivation below:* the resume brief (go_HINT2_55.md); REVIEW_BRIEF_55 (all); this file (draft = first
line + PRE-STATED only); HINT55.md (all 603 lines); CODEX_REVIEW_HINT.md (all 293 lines; complete, ends with "Exactly what
may be banked" items 1-5); CODEX_REVIEW_FLOW55.md (PRE-STATED, "Review result", §3.2-§3.3, §6, "Exactly what may be banked"
items 1-6; complete); FLOW55.md §0-§2 (head), §5.5-§12; UIR55.md as on disk at 02:46Z (PRE-STATED, §1, and its own
RESUMED heading: (UIR^♮) is still OPEN there); FLOW.md §4 (hypotheses block, `(SF-g)_k`, `(RLF-δ)`, `(UNIV-1L)`), §6.2
(Prop. F-rem), §7 (Theorem F-flow), §8 (Theorem F-tune), §9 (Lemma F-ind); PANEL_P1 §3 (the contract, item 4 = the H_int
bar); EXISTENCE.md `X-FLOW`, `X-FLOW-NL`, `H-src-flow`, `X-ARP`/`H-loc` (by grep + sed); PROOF.md `L5. Large-field
R-operation` (the large-field factor e^{−c p(g)²}, p(g) = (−log g)^p); HANDOFF row `H_int`.
No Balaban-corpus paper was needed for this file (nothing below rests on a Balaban/Dimock statement).

*Codex verdicts used, and my position (each re-derived or re-checked where marked):*
| Codex verdict (CODEX_REVIEW_HINT.md, locating string) | My position |
|---|---|
| CONFIRMED: `(2.1)`, `Theorem KLM`, UV-D, SEP, CT for the quadratic abelian realisation and 𝔊₀ ∪ 𝔊₁ ("This is not an application of the KL representation of the composite") | **Agree.** Re-derived as Lemma PAIR (§R1.4) and extended (§R1.6) |
| NOT-VERIFIED: "as an inference from composite positivity"; must not be promoted "to an identification theorem about every free realization" | **Agree.** §R1.2 makes the identification an explicit named definition (ID♮) and §R1.10 proves no one-point witness can do without one |
| REFUTED: `(N1) Constant normalisations cannot` (summed-covariance class not closed under unequal colour rescaling) | **Agree.** Re-verified exactly (check h2_55_a A1); repaired by the matrix class 𝔊^col (§R1.5) |
| Twice-subtracted S₂ example: "refute[s] unqualified completeness of 𝔊" | **Agree**; and the gap is closed: UV-D and SEP hold for every finite number of subtractions (§R1.6, PROVEN-HERE) |
| NOT-VERIFIED: bounded S4c comparator transfer ("linearization alone ⇒ the quadratic comparator dichotomy for a bounded compact observable" refuted by compound-Poisson contact noise) | **Agree with the refutation as stated.** §R1.2's contraction realisation does not use that implication: the comparator observable of a bounded block observable is its quadratic contraction, for which SEP holds (§R3.3) |
| NOT-VERIFIED: `survives the OS quotient` (heat-kernel tails; CT shows OS-equivalent linear fields with different flowed one-point functions) | **Agree.** §R1.9 gives a time-zero variant whose comparator value IS a reconstructed-theory number; §R1.10 (ii) states exactly what the 4D witness does and does not say |
| REFUTED as general continuity: `continuous under (MOM-E)/(CONV-E)` (only upper semicontinuity) | **Agree** (Codex's X_j example is correct: E X_j = b, X_j → 0 in law). Used in §R2.2 |
| NOT-VERIFIED: `f(t) → 0 as t → 0` from grid bounds alone (spike example); suggested inter-scale bound f(t) ≤ L⁴f(t_{m+1}) from dissipation | **Agree**; the suggested bound is proved here as Lemma INT (§R2.2) with the normalisation fixed |
| REFUTED: `Lüscher's k₁` (α- vs g²-expansion; k_g = k_α/(4π); 4k_g/b₀ = 4γ_E + 208/33 − (36/11)log 3) | **Agree** with the conversion: 4·(N/16π²)/(11N/48π²) = 12/11 and (12/11)(52/9) = 208/33, (12/11)·3 = 36/11 (hand arithmetic). The value of k_α itself is not re-derived here ([m]) |
| NOT-VERIFIED: `(NOISE-ADD)`, `(ANTI-♭)`, `(W-AF2_r)` (NOISE-ADD transfers only upper bounds) | **Agree**; §R3 |
| CONFIRMED: H-RED, H-RED′, H-RED-sharp (conditional), Lemma EV, NA-lin, Lemma BARE, KER-fwd failure | **Agree**; H-RED is re-used in §R2 with the corrections above |

*CODEX_REVIEW_FLOW55, used:* item 4 ("(UNIV-1L) ⇔ (UIR♮), at that coefficient level ... (UIR♮) itself remains
NOT-VERIFIED") and §3.3 ("(F-1) with an unspecified positive slope is not equivalent to (UNIV-1L)"). **Agree with both.**
This file uses only the direction (UIR^♮) ⇒ (UNIV-1L) ⇒ (B-BR) (§R2.3) and names (UIR^♮) as an OPEN input owned by
UIR55/FLOW55.

## §R1. T1 — the comparator side for the observable actually used (appended from 2026-10-29T03:36Z; checks h2_55_a/a2/b
ran 03:20-03:23Z, h2_55_d 03:34Z, each after its criteria file — see §R4)

### R1.1 The gap, stated exactly; the flow normalisation fixed
The Yang–Mills observable (HINT55 §1.1) is a fixed functional of the **bare links** U: the nonabelian Wilson flow V(τ;U)
and a lattice energy density of V. HINT55's comparator theorems (Codex: CONFIRMED) are about a *different* functional,
the abelian quadratic composite 𝓔^ab(t,x) = (t²/4)Σ_aΣ_{μν}(K_t∗F^a_{μν})(x)² of an abelian field strength. Two things are
therefore needed, and nothing less will do (R1.10 (i) proves the first cannot be skipped): **(I)** a fixed rule assigning
to the Yang–Mills observable its counterpart in a free theory; **(II)** the comparator theorem for the counterpart so
assigned, for every free theory in the class, by a correct one-point argument.

*Normalisation (fixes Codex §3 "NOT-VERIFIED normalization match").* Flow: V̇ = −{∂S_fl(V)}V with
S_fl := Σ_{oriented p}tr(1 − V_p) = 2Σ_{unoriented p}Re tr(1 − V_p) = 2N·S_geo = g₀²S_W, and ∂ = T^a∂^a with
tr(T^aT^b) = −½δ^{ab} (Lüscher's convention, [m]); energy density E_pl(τ,x) := 2Σ_{μ<ν}Re tr(1 − V_{μν}(τ,x)) (lattice
units); 𝓔(t,x) := τ²E_pl(τ,x), τ = t/a². Then Σ_x E_pl(τ,x) = S_fl(V(τ)) exactly (each unoriented plaquette once), and
for V_{μν} = exp(a²G_{μν} + …), 2Σ_{μ<ν}Re tr(1 − V_{μν}) = a⁴·¼Σ_{μν}G^a_{μν}G^a_{μν} + O(a⁶) (Re tr(1 − e^X) = −½tr X²
+ O(X⁴) for X ∈ su(N)). HINT55 §1.1's "S_geo without the factor β" has the wrong diffusion coefficient (Codex); everything
below uses the convention just fixed. The plaquette (not clover) density is chosen because Lemma INT (§R2.2) needs
Σ_xE_pl = S_fl.

### R1.2 Lemma CONTR and the identification (ID♮). PROVEN-HERE (jet identities: h2_55_b B1)
*Continuum.* For c ∈ R, let B_c(t)[A] solve ∂_tB_μ = D^c_νG^c_{νμ} + α₀D^c_μ∂_νB_ν, B(0) = A, with D^c = ∂ + c[B,·],
G^c = ∂_μB_ν − ∂_νB_μ + c[B_μ,B_ν], and E_c(t)[A] := ¼Σ_{μν}Σ_a(G^{c,a}_{μν}(t))². For data where the flows exist uniquely
on [0, t]: (i) B_c(t)[A] = c^{−1}B_1(t)[cA] (c ≠ 0); (ii) E_c(t)[A] = c^{−2}E_1(t)[cA]; (iii) at c = 0 the flow is
abelian and, for every α₀, G^0(t) = K_t∗dA, so E_0(t)[A] = ¼|K_t∗dA|² — the comparator composite 𝓔^ab/t².
*Proof.* Every commutator in G^c, in D^cG^c and in the α₀-term carries exactly one factor c, so substituting cB into the
c = 1 expressions gives c times the c-expressions (field and all jets scaled; h2_55_b B1.1-B1.3, α₀ symbolic; the
control B1-F — the same expressions with the commutator of G stripped of its c — violates the identity). So if B solves
the 1-flow from cA, B/c solves the c-flow from A; uniqueness gives (i), and (ii) follows. At c = 0, ∂_tB = −d^*dB −
α₀ d(d^*B) (a gradient correction), hence ∂_t dB = −dd^*dB = Δ(dB) (Bianchi), i.e. G^0(t) = K_t∗dA (B1.4). ∎
*Lattice.* U = 1 is a fixed point of the Wilson flow, the flow is smooth in (τ, U) (EXISTENCE `X-FLOW`), and its derivative
at U = 1 is the linearised flow Ȧ = −d^*dA (EXISTENCE `X-FLOW-NL`). Hence for links e^{cA},
E_pl(τ)[V(τ; e^{cA})] = c²·¼Σ_{μν}|(e^{τΔ}dA)_{μν}(x)|² + O(c³), the free lattice Maxwell composite.

**Definition (ID♮, the contraction identification).** For a gauge-invariant lattice observable O ≥ 0 with O(1) = 0, its
free counterpart is the second-order contraction O^♮[A] := lim_{c→0}c^{−2}O(e^{cA}) = ½D²O(1)[A, A]. O^♮ depends on A
only through the abelian field strength dA: gauge invariance of O with Ω = e^{cλ} gives O(e^{c(A + dλ) + O(c²)}) = O(e^{cA}),
and DO(1) = 0 (O ≥ 0, O(1) = 0), so the second-order terms agree. A free theory's value of the Yang–Mills observable is the
expectation of O^♮ in that theory. For the energy density, O^♮ is exactly the comparator composite of HINT55 (Lemma CONTR
(iii)); for the S4c block energy it is the squared linearised block flux (§R3.3). (ID♮) is the identification under which
"Yang–Mills is N² − 1 free gluons" is the g → 0 statement of perturbation theory (tree level: ⟨𝓔⟩_YM = g²·⟨𝓔^♮⟩_free + O(g⁴),
HINT55 §3.1 / §9.2, standard). It is a **definition**, named as such.

### R1.3 The other candidate — the nonabelian flow of a free gauge field — is not an observable of the free theory (T1(e))
**Lemma NOBS. PROVEN-HERE (exact core: h2_55_b B5).** On any finite periodic lattice, N ≥ 2, let λ: sites → su(N) be a
centred Gaussian with nondegenerate covariance (constant mode removed), A_b := λ_y − λ_x for b = (x, y), and U_b := e^{cA_b},
c ≠ 0. Then dA ≡ 0 (every abelian observable O^♮ vanishes, i.e. this is the free theory with F ≡ 0 in a gauge), but for
every τ ≥ 0, ⟨S_fl(V(τ;U))⟩ > 0, hence ⟨E_pl(τ, x)⟩ > 0 at every x (translation invariance).
*Proof.* dA = 0 by telescoping (B5.0). Around one plaquette with corner values (0, X, X + Y, Y) the holonomy is
e^{cX}e^{cY}e^{−cX}e^{−cY}; for SU(2) with cX = iaσ₁, cY = ibσ₂ one gets 2 − tr = 4 sin²a sin²b (B5.1; commuting X, Y give 0,
control B5-F); embed SU(2) for N ≥ 3. So the set of λ with a non-flat plaquette is open and non-empty, of positive Gaussian
probability. The Wilson flow is the gradient flow of the smooth S_fl on a compact manifold; flat configurations (S_fl = 0,
the minimum) are equilibria; by uniqueness of ODE solutions a trajectory reaching an equilibrium at some τ₁ is constant,
so S_fl(V(τ)) > 0 for all τ whenever S_fl(U) > 0. ∎
**Proposition GC-ξ (continuum, order e⁴).** For the covariant-gauge Gaussian A = A_T + ∂λ (covariance
e²(δ − (1 − ξ)pp/p²)/p² times a UV regulator r(p) at scale s₀; λ with covariance ξe²r(q)/q⁴, IR-regulated), the formal
c-expansion is ⟨t²E_c(t)[A]⟩ = c²·(tree) + c⁴e⁴·Q_t(ξ) + O(c⁶) with Q_t a polynomial of degree ≤ 2 in ξ (a Wick-quartic
expectation). (a) **PROVEN-HERE (formal-expansion level):** the ξ²-coefficient is
κ₂ := t²·¼Σ_{μν}⟨|K_t∗[∂_μλ,∂_νλ]|²⟩/(ξe²)² > 0, UV- and IR-finite and t-independent once s₀/t → 0. (b) **ARGUED:** the
ξ¹-coefficient contains −(N/(16π²))·log(t/s₀)·(tree)/e² + O(1). The ξ⁰ part (the transverse flow-only terms) is NOT computed.
*Derivation.* Gauge invariance: E_c[A] = E_c[A^Ω] for Ω = e^{cλ} (constants of λ are global rotations, so the IR regulator
drops out of every gauge-invariant quantity). By h2_55_b B2.2, A^Ω = A_T + cY₁ + c²Y₂ + O(c³) with
Y₁ = [λ, A_T] + ½[λ, ∂λ], Y₂ = ½[λ,[λ, A_T]] + ⅓[λ,[λ, ∂λ]]. Writing E_c[X] = 𝔈₀[X] + c𝔈₁[X] + c²𝔈₂[X] + … (𝔈_j homogeneous
of degree j + 2; 𝔈₀[X] = ¼|K_t∗dX|², bilinear form 𝔅₀), the c² coefficient of E_c[A^Ω] is
𝔈₀[Y₁] + 2𝔅₀(A_T, Y₂) + 3𝔈₁(A_T, A_T, Y₁) + 𝔈₂[A_T]. Sorting the expectation by powers of ξ (one ξ per λ–λ contraction): the
ξ² part is ⟨𝔈₀[½[λ,∂λ]]⟩ = (1/16)⟨|K_t∗d[λ,∂λ]|²⟩ = ¼Σ⟨|K_t∗[∂_μλ,∂_νλ]|²⟩ (d[λ,dλ] = 2[∂λ∧∂λ]); every other candidate is
odd in A_T or contains f^{abb} = 0. It is the mean square of a non-zero second-chaos variable, hence > 0; its vertex is
antisymmetric, q_μ(p−q)_ν − (p−q)_μq_ν = q_μp_ν − p_μq_ν (B6.1), so its momentum integrand is O(p²/q⁶) at large q and
O(q^{−2}) at small q (finite), and the homogeneity of ∂λ's covariance (degree −2) and of the flow makes t²× it
t-independent: (a). The ξ¹ part is ¼⟨|K_t∗d[λ, A_T]|²⟩ + ⟨𝔅₀(A_T, [λ,[λ, A_T]])⟩ (3𝔈₁(A_T, A_T, ½[λ,∂λ]) vanishes: the
λ–λ contraction inside [λ,∂λ]^a is f^{abc}δ^{bc} = 0). With Ĝ_λ(q) = ξe²r(q)/q⁴ and
𝒦(q) := ¼(N² − 1)∫_p e^{−2tp²}·2(p²δ − pp):D̂(p − q) (D̂ the A_T covariance), Σf^{abc}f^{abc} = N(N² − 1) and
Σ_{bd}f^{abd}f^{dbe} = −Nδ^{ae} (B3) give ξ¹-part = N∫_q Ĝ_λ(q)[𝒦(q) − 𝒦(0)] — the q → 0 cancellation is exact (B4; with
the BCH coefficient 1 in place of ½ the sum is −N ≠ 0, control B4-F). 𝒦 is smooth and even, so the integrand is O(q^{−2})
at small q; (p²δ − pp):Π^T ≤ 3p² gives 0 ≤ 𝒦(q) = O(𝒦(0)/(tq²)) at large q; hence
N∫Ĝ_λ(𝒦 − 𝒦(0)) = −N𝒦(0)ξe²[(8π²)^{−1}∫^{Λ}dq/q + O(1)] = −(Nξe²/(16π²))log(t/s₀)·𝒦(0) + O(ξe²𝒦(0)), Λ² ≍ 1/s₀. The hole
in (b): the large-q bound on 𝒦 and the regulator bookkeeping are written, not independently re-evaluated; the PRE-STATED
α₀-test is vacuous for this derivation (it never uses the flow's α₀), so (b) stays ARGUED as pre-registered.
**Decision on T1(e).** The nonabelian flowed density of a free gauge field is **not an observable of the free abelian
theory**: on every lattice its value is not a function of the free theory's gauge-invariant data (Lemma NOBS: the theory with
F ≡ 0 gives a positive value in one gauge and 0 in another), and in the continuum at order e⁴ it depends on the gauge
parameter ξ (GC-ξ (a)), whereas every function of F is ξ-independent (HINT55 Lemma TR(iii), Codex CONFIRMED). It is excluded
from the comparator class by definition; the counterpart of the Yang–Mills observable is fixed by (ID♮). By-product (ARGUED,
via (b)): HINT55 §2.3's formal claim that covariant-gauge Gaussian-connection realisations are scale invariant fails for
ξ > 0 (the λ-variance's ultraviolet logarithm keeps the regulator) — HINT55 labelled that claim ARGUED and did not use it.

### R1.4 Lemma PAIR — the correct argument for the one-point function. PROVEN-HERE
Let F = (F^a_{μν}), a = 1..n, be any family of real generalised random fields on R⁴ (any law, Gaussian or not), antisymmetric
in μν, with E[F(φ)²] < ∞ for Schwartz φ and a translation-invariant two-point function whose Fourier transform is a
matrix-valued tempered measure Ŝ^{ab}_{μν,ρσ}(dp) (Bochner–Schwartz). For a positive semidefinite colour matrix M, put
𝓔^♮_M(t,x) := (t²/4)Σ_{ab}M_{ab}Σ_{μν}F^a_{μν}(K_t^x)F^b_{μν}(K_t^x), K_t^x := K_t(x − ·). Then
  E[𝓔^♮_M(t,x)] = (t²/4)∫(2π)^{−4}e^{−2tp²}Σ_{μν}Tr(M Ŝ_{μν,μν}(dp)) ∈ [0, ∞].
*Proof.* E[F^a(φ)F^b(ψ)] = (2π)^{−4}∫φ̂(p)^*Ŝ^{ab}(dp)ψ̂(p) by definition of the two-point function; take
φ = ψ = K_t^x e_{μν} (|K̂_t|² = e^{−2tp²}) and sum with M (linearity of E). ∎
No Wick factorisation, no Gaussianity, no positivity of any composite enters; the only spectral object is the two-point
function of the **linear** field F. So the comparator theorem needs a Källén–Lehmann representation of the linear field
(a property of the free theory), never one of the composite — this is the argument Codex confirmed inside HINT55's explicit
definition, now stated for every law and every colour metric.

### R1.5 The colour class repaired: 𝔊^col, Lemma COL, and (N1) corrected. PROVEN-HERE (h2_55_a A1, A2)
**Definition (𝔊^col).** n colours (n = N² − 1 for SU(N)). Laws of n-colour antisymmetric tensor fields, O(4)-invariant,
Bianchi (ε_{λμνκ}∂_μF_{νκ} = 0), finite second moments, with Ŝ(p) = T^I(p) ⊗ Ŝ_s(p²),
  Ŝ_s(u) = ∫_{[0,∞)}dρ(s)[1/(u + s) − Σ_{j<K}(1 − u)^j/(1 + s)^{j+1}] + P(u),
ρ a positive-semidefinite-matrix-valued Radon measure with ∫Tr dρ/(1 + s)^{K+1} < ∞ for some integer K ≥ 0, P a polynomial
with real symmetric n×n coefficients, and Ŝ_s(u) ⪰ 0 for all u > 0. 𝔊^col_∞ := ∪_K. (HINT55's 𝔊₀, 𝔊₁ are the scalar K ≤ 1
cases.)
**Lemma COL.** (i) Every real n′×n matrix Λ maps 𝔊^col(n) into 𝔊^col(n′) (ρ ↦ ΛρΛᵀ ⪰ 0, P ↦ ΛPΛᵀ, Ŝ_s ↦ ΛŜ_sΛᵀ ⪰ 0). (ii)
For PSD M, Tr(MŜ_s) is a scalar member with ρ_M := Tr(Mρ) ≥ 0, P_M := Tr(MP). (iii) Ŝ(p) ⪰ 0 ⇔ Ŝ_s(p²) ⪰ 0 (T^I(p) ⪰ 0,
Lemma TR(i); Kronecker product). ∎ (A2: 60 exact triples, 0 violations; control A2-F fires.)
**(N1), corrected.** I agree with Codex's REFUTED: the colour-1 component of Codex's law has spectral weight δ₀ − δ₁, so the
law lies in HINT55's summed class but not in 𝔊^col (A1.2: ρ(1) = diag(−1, 1) not PSD); after the rescaling,
h_new = 1/4 + 3/(4(1 + u)), h_new′ = −3/(4(1 + u)²) < 0, UV value 3/(512π²) (A1.3-A1.4; a colour-RP pair under the same
rescaling has h′ = 1/(4(1 + u)²) ≥ 0, control A1-F). **Corrected statement:** every linear colour map, in particular every
colour-dependent constant normalisation, and every positive colour metric in the energy density preserve 𝔊^col (Lemma COL),
so none of them can fake the witness. Nothing physical is lost: an n-component reflection-positive free field has a PSD
matrix spectral measure (RP applied to every combination Σv_aF^a); what 𝔊^col drops are laws whose colour components are
not themselves reflection positive.

### R1.6 Theorem UV-D_∞ and Theorem SEP^col — every number of subtractions. PROVEN-HERE (h2_55_a A4)
For a scalar member (apply Lemma COL (ii)), f(t) = (3/32π²)∫_0^∞ve^{−2v}h(v/t)dv, h(u) = uŜ_s(u) (HINT55 (2.1) = Lemma PAIR).
Let K₀ be the least K with ∫dρ/(1 + s)^{K+1} < ∞; rewriting Ŝ_s with K₀ subtractions only changes P by a polynomial (A4.1).
**Theorem UV-D_∞.** Exactly one holds: (a) K₀ = 0 and Ŝ_s = ∫dρ/(u + s) + p₀, p₀ ≥ 0: f is non-increasing and
f(0+) = 3ρ([0,∞))/(128π²) + ∞·1[p₀ > 0]; (b) otherwise f(t) → +∞ as t ↓ 0.
*Proof.* K₀ = 0: HINT55's 𝔊₀ argument (Codex CONFIRMED). K₀ = K ≥ 1: S_K(u) := (1 − u)^K∫dρ(s)/((u + s)(1 + s)^K) (A4.1). (α)
For u ≥ 2, |1 − u| ≥ u/2 and u + s ≤ 2u on s ≤ u, so |S_K(u)| ≥ 2^{−K−1}u^{K−1}∫_{[0,u]}dρ/(1 + s)^K, and |S_K|/u^{K−1} → ∞
because ∫dρ/(1 + s)^K = ∞. (β) For u ≥ 1, |S_K(u)|/u^K ≤ ∫dρ(s)/((u + s)(1 + s)^K) → 0 (dominated by (1 + s)^{−K−1}). The sign of
S_K on u > 1 is (−1)^K. Positivity Ŝ_s = S_K + P ≥ 0 then forces Ŝ_s(u) ≥ cu for u ≥ U₀, some c > 0: K odd — S_K → −∞
faster than u^{K−1}, so P must dominate it, deg P = d ≥ K with positive leading coefficient, and by (β) Ŝ_s ≥ (p_d/2)u^d;
K even (≥ 2) — if d ≥ K the leading coefficient is positive (else Ŝ_s → −∞ by (β)) and Ŝ_s ≥ (p_d/2)u^d; if d ≤ K − 1, (α)
gives Ŝ_s/u^{K−1} → ∞, so Ŝ_s ≥ u^{K−1} ≥ u. Finally f(t) ≥ (3c/32π²)t²∫_{U₀}^∞u³e^{−2tu}du ≥ (3c/32π²)(3/(8t²) − t²U₀⁴/4) → ∞. ∎
(Codex's S₂: A4.2 re-derives S₂(u) = u log((u + 1)/2) − (u − 1)/2 by partial fractions; A4.3: S₂/u → ∞, S₂/u² → 0 —
case (b).) The same proof gives UV-D_∞ for any self-similar quadratic smearing Q(s) = ∫w(v)h(|v|²/s²)d⁴v (HINT55 KLM) as
soon as w ≢ 0 on some annulus (in case (b), h(u) ≥ cu², so Q(s) ≥ cs^{−4}∫_{|v|≥s√U₀}w(v)|v|⁴d⁴v → ∞).
**Theorem SEP^col.** For every PSD colour metric M and every mixture μ̄ = ∫μ_α dν(α) of members of 𝔊^col_∞ ∪ 𝔖 with
f_μ̄(t) ∈ [0, ∞]: if ℓ := liminf_{t↓0}f_μ̄(t) < ∞, then f_μ̄(t₀) ≤ ℓ for every t₀ > 0. *Proof.* HINT55's Fatou argument
(Codex CONFIRMED) with UV-D_∞ in place of UV-D. ∎ Hence **(AF-W) excludes conv(𝔊^col_∞ ∪ 𝔖) for every colour normalisation,
every number of Källén–Lehmann subtractions, every contact polynomial, and every law (Gaussian or not) with such a
two-point function.** This closes Codex's "higher-subtraction comparators require an additional theorem". Given the
IMPORTED Källén–Lehmann theorem for tempered reflection-positive Bianchi field strengths, 𝔊^col_∞ contains the (ID♮)
energy-density sector of every reflection-positive abelian theory, interacting or not, with no subtraction limit; the free
ones need no import.

### R1.7 Exact free values (T1(c)). PROVEN-HERE (Lemma PAIR + (2.1); h2_55_a A5)
J(σ) := ∫_0^∞v²e^{−2v}(v + σ)^{−1}dv is decreasing, J(0) = 1/4 (J(σ) = 1/4 − σ/2 + σ²e^{2σ}E₁(2σ)). M PSD throughout.
| free comparator | ρ, P | f(t) | behaviour |
|---|---|---|---|
| canonical Maxwell, any colour coupling matrix C ⪰ 0 (covariance C/p², any gauge) | ρ = Cδ₀, P = 0 | 3Tr(MC)/(128π²) | constant |
| Proca, colour masses m_a and couplings C_a ⪰ 0 (F-covariance T^IΣ_aC_a/(p² + m_a²)) | ρ = Σ_aC_aδ_{m_a²} | (3/32π²)Σ_aTr(MC_a)J(tm_a²) | non-increasing, strictly if some m_a > 0 with Tr(MC_a) > 0; f(0+) = 3ΣTr(MC_a)/(128π²) |
| generalised free field | ρ | (3/32π²)∫Tr(M dρ(s))J(ts) | non-increasing |
| contact representative (K₀ = 0) | ρ, P = ΣP_ku^k | (3/32π²)[∫Tr(Mdρ)J(ts) + Σ_kTr(MP_k)(k+2)!/(2^{k+3}t^{k+1})] | → ∞ as t ↓ 0 if P_M ≢ 0; CT: f/C = 1/4 − ε/(4t) + 3ε²/(8t²), F(8) − F(4) = 7/512, F(1) − F(1/2) = −7/8 |
| K₀ ≥ 1 subtractions | any | — | → ∞ (UV-D_∞) |
| mixtures | ν | ∫f_α dν | (AF-W) impossible (SEP^col) |

### R1.8 Coverage of Euclidean representatives (T1(d)). Lemma REP. PROVEN-HERE given two IMPORTED-standard facts
*Statement.* If μ ∈ 𝔊^col_∞ and μ′ is any O(4)-invariant, Bianchi, finite-second-moment law of n-colour antisymmetric tensor
fields whose two-point function agrees with μ's on φ ⊗ ψ with disjoint supports, then μ′ ∈ 𝔊^col_∞ with the same ρ and
P′ = P + Q, Q a symmetric-matrix polynomial.
*Proof.* The difference D of the two-point functions is translation invariant and supported on the diagonal, so D̂ is a
polynomial [IMPORTED-standard: a distribution supported at a point is a finite sum of derivatives of δ]. O(4)-equivariant
polynomial tensors in one vector are generated by δ and p [IMPORTED-standard: Weyl's first fundamental theorem for O(4)];
of the ten rank-4 structures only I and T^I survive antisymmetrisation in both pairs (A3.2: coefficients (±2, 0) for two
δδ structures, (0, ±1) for four δpp structures, 0 for the rest), so D̂ = α(p²)I + β(p²)T^I. Bianchi for both laws gives
εpD̂ = 0; Bi[T^I] ≡ 0 while Bi[I] ≠ 0 (A3.3; h2_55_a2 C1, C3), so α = 0. Finally β(p²)T^I polynomial forces β polynomial
(component T^I_{12,13} = p₂p₃, A3.5). ∎
*Consequence.* SEP^col does not depend on which Euclidean representative of a free theory one compares with: contact terms of
every polynomial degree are inside the class. This is the precise (and only) sense in which the 4D witness "survives the OS
quotient" on the comparator side; see R1.10 (ii) and R1.9.

### R1.9 Proposition T0 — a time-zero witness whose comparator value is a reconstructed-theory number. PROVEN-HERE for
generalised free fields; for interacting abelian Wightman theories CONDITIONAL on the IMPORTED tensor Källén–Lehmann theorem
*Observable.* 𝓑(t, x⃗) := τ²·2Σ_{i<j≤3}Re tr(1 − V_{ij}(τ, x⃗)), where V is the **3D** Wilson flow (flow action Σ_{oriented
spatial p in the slice}tr(1 − V_p)) of the spatial links of the time slice x₀ = 0. It is a gauge-invariant function of the
time-zero spatial links only; for site reflection it lies in 𝔄₊ (and 𝔄₋), and its translate to time δ > 0 is strictly
positive-time local. So ω(𝓑) = ⟨Ω, [𝓑]⟩ for Yang–Mills as for any OS state — no H-loc estimate (contrast EXISTENCE
`X-FLOW-NL` / `H-loc` for 4D-flowed observables). Its contraction is 𝓑^♮(t) = (t²/4)Σ_{i,j≤3}Σ_{ab}M_{ab}(K³_t∗F^a_{ij})(K³_t∗F^b_{ij})
(the 3D abelian flow acts on F_{ij} as the 3D heat kernel, by Bianchi).
*Statement.* In the reconstructed free theory whose field strength has Wightman two-point function with PSD matrix measure ρ
(tempered; ∫Tr dρ(s)·min(1, (ts)^{−1/2}) < ∞, the condition for the smeared time-zero magnetic field to exist),
  f_B(t) := ⟨Ω, 𝓑^♮(t)Ω⟩ = (1/(4π²))∫Tr(M dρ(m²))J_B(tm²),  J_B(σ) := ∫_0^∞v⁴e^{−2v²}(v² + σ)^{−1/2}dv,
J_B is decreasing (A6.6), J_B(0) = 1/8 (A6.2); so f_B is non-increasing and f_B(0+) = ρ_M([0,∞))/(32π²) ∈ [0, ∞]. Hence (AF-W)
fails for every such free theory, every mixture (Fatou) and every scale-invariant state — **with no subtraction limit and no
contact-term caveat**: a Euclidean representative with P_M ≢ 0 has infinite Euclidean sharp-time value (A6.5), whereas the
reconstructed value is the canonical one.
*Proof.* The magnetic components T^I_{ij,kl}(p) involve only p⃗ (A3.4), so time-zero smearing integrates the scalar factor
over p₀: ∫dp₀/(2π(p₀² + p⃗² + m²)) = 1/(2ω_m) (A6.1) — the equal-time Wightman formula
⟨Ω, B(g)B(g)Ω⟩ = ∫Tr(Mdρ)∫d³p|ĝ|²T^I(p⃗)/((2π)³2ω_m). Then Σ_{ij}T^I_{ij,ij}(p⃗) = 4|p⃗|² (A3.4), d³p/(2π)³ = u²du/(2π²),
u = v/√t (A6.3), massless value 1/(32π²) = J_B(0)/(4π²) (A6.4; with the 4D trace 6 one would get 3/(64π²), control A6-F);
monotone convergence for f_B(0+). ∎
*Cost on the Yang–Mills side (ARGUED; not resolved).* The 3D-flowed field at sharp time is not smoothed in time; its
continuum finiteness in Yang–Mills is plausible under asymptotic freedom (a field-strength spectral weight ≍ dm²/(m²log²m²)
has ∫dρ/m < ∞) but not established, and would be part of (TS-up)^B. Tree level: f_B = (N² − 1)g²/(32π²) + O(g⁴); its running
is not computed here.

### R1.10 What no one-point witness can do (T1(f)). PROVEN-HERE by the examples cited
(i) *Identification.* Without a fixed rule, every profile is realisable in a free theory: the identification
𝓔(t) ↦ φ(t)·1 realises any φ ≥ 0, and a local example is Codex's free massive scalar with M²(K_t∗φ)²:
t²⟨M²(K_t∗φ)²⟩ = (M²t/(16π²))∫_0^∞ve^{−2v}(v + M²t)^{−1}dv ∈ (0, M²t/(32π²)] → 0 (re-derived: A7), an (AF-W)-type profile in a
free theory. So H_int is non-freeness **relative to (ID♮)** and cannot be "non-free under every identification".
(ii) *Euclidean representatives.* The 4D-flowed one-point function is not an OS invariant (CT, Codex CONFIRMED). The 4D
statement is about Euclidean states; by Lemma REP it holds against every Euclidean representative of every free theory in
𝔊^col_∞. Only sharp-time (time-zero) observables make both sides reconstructed-theory numbers (R1.9).
(iii) *Bounded observables.* Evaluated literally in a free law, a bounded compact observable can show (AF-W) (Codex's
compound-Poisson contact example). Under (ID♮) the counterpart of a bounded O is the quadratic O^♮, to which SEP^col applies;
Codex's example then has E[O^♮] = λ·const·s^{−2} → ∞ and is not a counterexample.
(iv) *Finitely many scales.* CT (Codex CONFIRMED): no finite subfamily of (1.2) excludes contact representatives.
(v) *Nonabelian flow of a free field.* Not an observable of the free theory (R1.3).

## §R2. T2 — the Yang–Mills side: the bounds the RG must deliver, and H_int ⇐ (flow) + (named bounds) with every link
(appended from 2026-10-29T03:41Z)

### R2.1 The named bounds, exactly
*Setting.* F-tune's tuned sequence at fixed renormalised coupling g ∈ (0, g₁] (FLOW §8); bare spacing a = L^{−K} (unit
lattice = level K); torus side R ≥ R₀ (physical); f_{K,R}(t) := ω_{K,R}(𝓔(t, 0)) with 𝓔 as fixed in R1.1; grid
t^{(m)} = c_tL^{−2m}, i.e. lattice flow time τ = c_tL^{2k} with k = K − m (the flow time **matched to RG level k**).
- **(TS-up)** There are C₊ > 0, ϑ ∈ [0, 1), d₀ such that for all K, all R ≥ R₀ and every level k with d₀ ≤ k ≤ K − m₀:
  f_{K,R}(c_tL^{−2(K−k)}) ≤ C₊ g_k^{2(1−ϑ)}, g_k the chain's own coupling at level k (FLOW Def F-g).
- **(TS-low)** At one level k₀ = K − m₀ (fixed physical time t₀ = t^{(m₀)}): f_{K,R}(t₀) ≥ c₋ g_{k₀}², c₋ > 0, uniformly in
  K ≥ m₀ + d₀ and R ≥ R₀.
- **(MOM-E)** sup_{K,R} ω_{K,R}(𝓔(t₀, 0)^{1+δ}) < ∞ for some δ > 0 (uniform integrability at the coarse time only).
In words: at every short flow time the bare-field flowed energy density is bounded by a power of the running coupling at
the matched level (asymptotic freedom of the observable); at one fixed physical flow time it is at least a multiple of the
coupling there, and uniformly integrable. c₋ and C₊ are arbitrary (no smallness, no perturbative coefficient: Codex
confirmed H-RED needs none); ϑ < 1 is necessary (ϑ = 1 lets a constant f meet every bound). HINT55's (CONV-E) is **not** an
input any more (Lemma CONV below). If an RG delivered directly
  (UV-0) lim_{m→∞} sup_{K,R} f_{K,R}(t^{(m)}) = 0   and   (IR-pos) inf_{K,R} f_{K,R}(t₀) > 0,
no coupling flow would be needed at all (take c_W := ½ inf f(t₀)); the flow is what converts bounds stated in terms of g_k —
the natural RG output — into (UV-0) and (IR-pos).

### R2.2 Theorem H-RED♮. PROVEN implication; CONDITIONAL on (F-tune), (TS-up), (TS-low), (MOM-E)
**Lemma INT (inter-scale). PROVEN-HERE (arithmetic of the conclusion: h2_55_d D1).** For any translation-invariant law on the
lattice torus, e(τ) := ⟨E_pl(τ, 0)⟩ is non-increasing in τ; hence f(t) ≤ L⁴ f(t^{(m+1)}) for t ∈ [t^{(m+1)}, t^{(m)}].
*Proof.* Σ_xE_pl(τ, x) = S_fl(V(τ)) (R1.1), and along the gradient flow dS_fl(V(τ))/dτ = −Σ_{b,a}(∂^a_bS_fl)² ≤ 0 for every
configuration; the flow commutes with translations (EXISTENCE `X-FLOW`), so ⟨E_pl(τ, x)⟩ = ⟨S_fl(V(τ))⟩/|Λ| is
non-increasing. Then f(t) = t²e(t/a²) ≤ (t^{(m)})²e(t^{(m+1)}/a²) = L⁴f(t^{(m+1)}). ∎ (This is Codex's suggested inter-scale
step, with the normalisation fixed. A clover density lacks Σ_xE = S_fl, so the lemma is stated for E_pl only.)
**Lemma CONV. PROVEN-HERE.** Under (TS-up) and Lemma INT, sup_{K,R}f_{K,R}(t) < ∞ for every t ∈ (0, t₀] (bounded below by
the depth margin τ ≥ c_tL^{2d₀}); non-negative variables with bounded means are tight, and the joint laws of a countable
family of tight real variables have a weakly convergent subsequence (Prokhorov on R^D, D countable, product topology). So
along a further subsequence of any H_reg subsequence the joint laws of {𝓔(t, 0)}_{t∈D}, D := (0, t₀] ∩ (Q ∪ grid),
converge (jointly with H_reg's other observables, by the same diagonal argument). ∎
**Theorem H-RED♮.** Let x := U₊(m₀), U_±(m) := g^{−2} + β_±m log L ± R (F-tune's bounds), m₁ as in HINT55 (4.1) or m₁′ as
in H-RED′, and m₁^c := least m ≥ m₀ with U₋(m + 1)^{1−ϑ} ≥ 2L⁴C₊U₊(m₀)/c₋. Then, with c_W := c₋/(2U₊(m₀)) and constants
independent of K and of the torus:
(1) for m ≥ m₁: W_m(ω_{K,R}) = f_{K,R}(t₀) − f_{K,R}(t^{(m)}) ≥ c_W (HINT55 H-RED/H-RED′; Codex CONFIRMED);
(2) **continuous time (new):** for every t with c_tL^{−2(K−d₀)} ≤ t ≤ t^{(m₁^c)}: f_{K,R}(t₀) − f_{K,R}(t) ≥ c_W;
(3) every limit point ω (Lemma CONV) has f_ω(t₀) ≥ c₋/U₊(m₀), f_ω(t) ≤ L⁴C₊U₋(m + 1)^{ϑ−1} for t ∈ D ∩ [t^{(m+1)}, t^{(m)}]
(m ≥ m₀), hence **lim_{t↓0, t∈D} f_ω(t) = 0** (zero bare charge along all of D, not only along the grid — this closes
Codex's "NOT-VERIFIED from the displayed grid bounds alone"), and W_m(ω) ≥ c_W for m ≥ m₁ (upper semicontinuity, Codex's
correction: W_m is usc, not continuous, which suffices for this closed inequality);
(4) by SEP^col under (ID♮): the energy-density one-point profile of ω is not that of any member of conv(𝔊^col_∞ ∪ 𝔖),
for any colour metric.
*Proof.* (2): for t ∈ [t^{(m+1)}, t^{(m)}], m ≥ m₁^c: f(t) ≤ L⁴f(t^{(m+1)}) (INT) ≤ L⁴C₊u_{K−m−1}^{ϑ−1} (TS-up) ≤
L⁴C₊U₋(m + 1)^{ϑ−1} (F-tune) ≤ c₋/(2U₊(m₀)) ≤ f(t₀)/2 (TS-low with u_{K−m₀} ≤ U₊(m₀)); so f(t₀) − f(t) ≥ f(t₀)/2 ≥ c_W.
(3): portmanteau for the non-negative continuous 𝓔 gives ω(𝓔(t)) ≤ liminf_jω_j(𝓔(t)), so the upper bounds pass; at t₀,
(MOM-E) gives uniform integrability, so ω_j(𝓔(t₀)) → ω(𝓔(t₀)) and f_ω(t₀) ≥ c₋/U₊(m₀); U₋(m) → ∞ since β₋ > 0; the
W_m-bound is limsup_jW_m(ω_j) ≤ W_m(ω). (4): (3) gives (AF-W); apply SEP^col. ∎ Arithmetic of the threshold:
h2_55_d D2 (200 exact parameter sets: the bound holds on [m₁^c, m₁^c + 40]; m₁^c ≥ m₁′ − 1; ϑ ∈ {0, 1/3, 1/2, 2/3}).

### R2.3 Connection to the coupling flow — the full chain, every link with owner and status
| link | statement | status |
|---|---|---|
| L1 | H_int(𝓔) [(1.2) uniformly, (AF-W) in every limit, non-membership in conv(𝔊^col_∞ ∪ 𝔖) under (ID♮)] ⇐ (F-tune) + (TS-up) + (TS-low) + (MOM-E) | **PROVEN implication here** (H-RED♮: HINT55 H-RED/H-RED′, Codex CONFIRMED; INT, CONV, usc, SEP^col PROVEN-HERE) |
| L2 | (F-tune) is used ONLY through: β₋ > 0 (u_{K−m} ≥ U₋(m) → ∞, for UV-0); U₊(m₀) < ∞ (g_{k₀}² ≥ 1/U₊(m₀) > 0, for IR-pos); K- and torus-independence of γ, g₁, β_±, R | by inspection of R2.2 |
| L3 | (F-tune) ⇐ (UNIV-1L) + (SF-g)_k + (RLF-δ)_k + (SF-cont) + (SF-∞) | FLOW §8 Theorem F-tune, PROVEN-HERE there (CONFIRMED upstream per HINT55's reading; Codex checked the quoted statement) |
| L4 | **Remark B-BR.** In FLOW's Theorems F-flow, F-tune and Lemma F-ind, (UNIV-1L) may be replaced by the two-sided bracket **(B-BR)**: there are 0 < β′ ≤ β″, R′ < ∞ with β′(n − j)log L − R′ ≤ B_n − B_j ≤ β″(n − j)log L + R′ for 0 ≤ j ≤ n (B_n := Σ_{k<n}b_k); take γ with C_ργ² ≤ ½β′log L, β₋ := β′ − C_ργ²/log L ≥ β′/2 > 0, β₊ := β″ + C_ργ²/log L, R := R′, and in F-ind fix β₋ := β′/2, R := R′ first | **PROVEN-HERE** by inspection of FLOW §7-§9 (re-read this run: F-flow's proof uses (UNIV-1L) only for the two-sided bound on B_n − B_j; F-tune uses only F-flow; F-ind orders constants); arithmetic h2_55_d D3 |
| L5 | (UNIV-1L) ⇒ (B-BR) with β′ = β″ = β₀^std, R′ = 2R₀ | trivial |
| L6 | (UIR^♮) ⇒ (UNIV-1L) [in fact ⇔] | FLOW55 Corollary K̄-β; CODEX_REVIEW_FLOW55 item 4: CONFIRMED as a conditional reduction at the fixed-n coefficient level (with the φ-tower normalisation for N ≥ 3, item 2) |
| L7 | **(UIR^♮)** sup_n\|β[G^♮_⊥,n] + (21/22)β₀^std n log L\| < ∞ | **OPEN** (FLOW55 §5.5; UIR55 at work, its file has no result yet as of 02:46Z). **Named input of this file.** |
| L8 | Weaker sufficient form: by B_n = −β[G^♮_⊥,n] + (1/22)β₀^std n log L (FLOW55, Codex CONFIRMED conditional), (B-BR) ⇔ **(UIR^♮_br)**: (β′ − β₀^std/22)(n − j)log L − R′ ≤ β[G^♮_⊥,j] − β[G^♮_⊥,n] ≤ (β″ − β₀^std/22)(n − j)log L + R′ for some β′ > 0 | PROVEN-HERE (substitution). H_int needs only (UIR^♮_br): a two-sided linear bracket on the transverse group with *some* positive total slope, not the exact 21/22. Whether this is easier than (UIR^♮) is not decided here |
| L9 | (SF-g)_k (layer-1 polydisc; FLOW55 §7-§8: needs N5 at levels ≥ 1 at complex backgrounds, (NA-H_loc) OPEN, and BFT-0 in analytic form, OPEN); (RLF-δ)_k (requirement FI-1 on RLARGE, recorded in FLOW §9, not discharged); (SF-cont) (Balaban CMP 109 smoothness, IMPORTED as read by FLOW); (SF-∞) (stated hypothesis) | statuses as FLOW/FLOW55 give them; not re-verified here |
| L10 | (TS-up), (TS-low), (MOM-E) | **OPEN, not supplied by any layer-1 statement** (R2.4) |
| L11 | (ID♮) | definition (R1.2) |
**So: H_int(𝓔) ⇐ (UIR^♮_br) [⇐ (UIR^♮)] + (SF-g) + (RLF-δ) + (SF-cont) + (SF-∞) + (TS-up) + (TS-low) + (MOM-E), relative to
(ID♮).** Constants: c_W = c₋/(2U₊(m₀)), m₁, m₁^c depend only on (c₋, C₊, ϑ, β_±, R, g, L, c_t, m₀) — none on K or the torus.
*Is any input H_int restated?* (TS-low) is met by every non-trivial comparator; (TS-up) at finitely many levels is met by
free comparators with small couplings; what separates is (TS-up) at all levels together with β₋ > 0 — the ultraviolet
vanishing of the observable — and the theorem that no comparator has it is SEP^col, proved here. No input is a lower bound
on a separating quantity. (Codex's remark stands: these Yang–Mills inputs carry the substantive asymptotic-freedom work.)

### R2.4 What the named bounds require, and that no layer-1 statement supplies them
**(TS-up) for the bare 4D flowed density — two requirements, the second new.**
(i) *Transport.* 𝓔(t) is a function of the bare field U₀ at lattice flow time c_tL^{2k}; an RG controls laws of level-k
fields. Needed: **(SRC)** two-sided control of E[𝓔(t)(U₀) | level-k field] on level-k small fields (or **(FLOW-BLK)**, a
two-sided comparison with a level-k block observable). EXISTENCE lists the related H-src-flow as OPEN ("it needs fine-scale
control (the flow reaches the cutoff scale), i.e. H-Bal-3 at every scale"). Not stated by layer 1.
(ii) *Large fields — ARGUED.* The flowed density at τ = L^{2k} is sensitive to field concentrations at every finer level
j < k that survive the flow. On the lattice the Wilson flow removes a concentration of size L^j (lattice units) only on a
flow-time scale ≍ L^{4j} (the Wilson action's O(a²/ρ²) instanton-shrinking term; [m]), so those with j ≳ k/2 survive to
τ = L^{2k}, and a surviving concentration of size L^j near the origin contributes τ²E ≍ (τ/L^{2j})² = L^{4(k−j)}. With P_j
the per-block probability of such a concentration at level j, (TS-up) needs Σ_{k/2≲j<k}L^{4(k−j)}P_j = o(g_k^{2−2ϑ}).
The large-field factor of Balaban-type estimates — e^{−c p(g_j)²} per block with p(g) = (−log g)^p (PROOF.md `L5.
Large-field R-operation`, IMPORTED-NOT-YET-REVERIFIED; Dimock III's e^{−c₂p_j²}) — decays only like exp(−c(log 1/g_j)^{2p}),
polylogarithmically in log L^j, while L^{4(k−j)} grows exponentially in k − j: the sum diverges. A sufficient replacement is
**(LF-inst)**: P_j ≤ Ce^{−c_LF u_j} for flow-surviving concentrations with c_LFβ₋ > 4 (then
Σ_jL^{4(k−j)}e^{−c_LFu_j} ≤ Ce^{−c_LFu_k}Σ_{r≥0}L^{(4−c_LFβ₋)r}). For the true dilute-instanton weight e^{−8π²/g²} with the
one-loop slope this is the classical small-instanton convergence 11N/3 > 4, true for N ≥ 2 — but no estimate in the lane
delivers a large-field bound of that strength. **Hence (TS-up) for the bare 4D density is not "standard UV-stability
content" as HINT55 §4.5 said: it needs (SRC) plus a sharp large-field estimate.** (A correction of HINT55's reading of an
input, not of a banked item. The order-of-magnitude analysis uses flow-stability of instantons and the lattice shrinking
rate, which are [m]/IMPORTED-standard and not proven here; that the union bound fails is proven by the displayed growth
comparison, that the true (TS-up) needs (LF-inst) is not.)
**(TS-low)**: (SRC) at the coarse level plus anti-concentration of the level-k₀ fluctuation (its Gaussian part must
dominate) — an LAP-1-type statement; not supplied for 𝓔 by any layer-1 statement. **(MOM-E)** ⇐ EXISTENCE H-src-flow (OPEN).
**Contrast — a bounded, level-local block observable.** For the deterministic S4c block energy Ψ_m (Branch D), the law of
Ψ_m is the level-k marginal of the hard RG, so (TS-up) is level-local: small fields give O(g_k²), large fields at level k at
most Nπ²P_k ≤ Nπ²e^{−p(g_k)} ≪ g_k² (Ψ_m ≤ Nπ²). That is EXISTENCE X-NTAF's upper half (⇐ H-Bal-1 + H-sg), and its lower half
is (TS-low) (⇐ H-Bal-1 + H-loc-LF); (MOM)/(CONV) are automatic. Neither (SRC) nor (LF-inst) arises. The time-zero 𝓑 of
R1.9 is unbounded and flowed like 𝓔 and needs the same two items plus sharp-time finiteness.

## §R3. T3 — HINT55's soft-branch inputs (NOISE-ADD), (ANTI-♭), and the deterministic S4c branch

### R3.1 (NOISE-ADD): survives as an input, only where HINT55 used it
As stated (HINT55 §4.4: ω(Ψ_m) ≤ C_NA ω(‖log U_{K−m}(p)‖²_HS) + C′_NA g_{K−m}^{2−2ϑ}, deterministic A^{K−m}(U₀) against the soft
U_{K−m}) it is an **upper-bound transfer**, the right direction for (TS-up) of the deterministic block observable in the
soft scheme, and that is its only consumer. Status: NOT-VERIFIED in the nonlinear case (Codex), and genuinely nonlinear
because the kernel's centre is a non-unitary contour mean (KER-fwd fails exactly; Codex CONFIRMED, I agree). It is **not** an
input of the bare 4D witness (Lemma BARE, Codex CONFIRMED: its expectation is kernel-independent) nor of Branch D.

### R3.2 (ANTI-♭): survives as an OPEN input; its route (β) does not survive
I agree with Codex: (NOISE-ADD) transfers only upper bounds, so route (β) ("E[Ψ_det] = E[Ψ_soft] − 𝒩_m" plus a Gaussian
comparison) is not a reduction — the exact scalar data E Ψ_soft = 2g², E Ψ_det = 0 satisfy (NOISE-ADD) with zero error and
violate every positive (ANTI-♭). A route needs a **lower** comparison, e.g. **(NOISE-SUB)**: E Ψ_det ≥ E Ψ_soft − 𝒩_m − εg²
with 𝒩_m the noise budget of the actual kernel at its level-dependent couplings (Codex: EXISTENCE Lemma NT-G uses a constant
fine coupling, which is not the chain's) and ε below the signal margin, plus the exceptional-event error translated to the
signal scale. (ANTI-♭) is needed only by the soft scheme's block-observable route.

### R3.3 The deterministic S4c branch (Branch D) avoids both — and what it needs instead
*Avoids (NOISE-ADD), (ANTI-♭):* the witness observable Ψ_m = ‖log V^{(m)}_p‖²_HS is a function of the deterministic block
field V^{(m)} = A^{K−m}(U₀), whose law is what a hard (deterministic-averaging) RG controls; X-NTAF bounds it directly
((δ_*/2)/(1/g² + β′m log L) ≤ ω(1 − P_{p,m}) ≤ φ(G_m), EXISTENCE `X-NTAF`; with Lemma EV this is (TS′)), with no auxiliary
noise. By R2.4 its (TS-up) is level-local, so neither (SRC) nor (LF-inst) arises — the decisive advantage over the bare
flowed witness.
*Comparator side under (ID♮):* ‖log e^{cX + O(c²)}‖²_HS = c²‖X‖²_HS + O(c³), so Ψ^♮_m = Σ_a|φ^a_m|²_p with φ_m = DA^{K−m}(1)[·] the
linearised block flux (CONTR's definition; the S4c map is smooth at 1 by EXISTENCE `X-S4c`). If **(S4c-lin)** holds — the
linearisation read at resolution m converges, as the depth K − m → ∞, to a fixed self-similar smearing φ_s, s = L^{−m}, with
w ≢ 0 on some annulus (Codex's caveat: co-closed tests can give w ≡ 0, so this must be checked for the actual block flux) —
then HINT55's KLM and the UV-D_∞/SEP^col of R1.6 (self-similar version) apply in the discrete scale s = L^{−m} (no inter-scale
lemma needed). Codex's compound-Poisson refutation concerns the literal bounded Ψ_m in a free law; under (ID♮) the
counterpart is the quadratic Ψ^♮_m, so it does not apply (R1.10 (iii)). I agree with Codex that "linearisation alone ⇒
the comparator dichotomy for the bounded observable itself" is false; (ID♮) does not use that implication.
*OS clause:* Ψ_m is strictly local, hence in 𝔄₊ (EXISTENCE `X-RP`): its Yang–Mills one-point function is a
reconstructed-theory number ⟨Ω, [Ψ_m]⟩; the comparator side is the Euclidean-representative statement of Lemma REP.
*What Branch D needs (not supplied by the lane's soft RG):* H-Bal-1 **for the hard scheme's couplings** (FLOW/FLOW55's
F-tune is a statement about the soft chain's couplings; the hard scheme needs its own flow theorem — HINT55 recorded H-Bal-1 as
"IMPORTED-NOT-YET-REVERIFIED", Balaban's), H-loc-LF and H-sg for the S4c variables (EXISTENCE: HYPOTHESIS-NEW), and (S4c-lin)
(OPEN; a linear-algebra statement about the linearised S4c tower).

### R3.4 The bare 4D witness in the soft scheme
It needs neither (NOISE-ADD) nor (ANTI-♭) as stated, but it does not escape the noise either (ARGUED): to bound
ω(𝓔(U₀)) = E[E[𝓔(U₀) | U_k]] with a soft RG one must transport the bare observable through the soft chain's fluctuation
integrals — **(SRC^S)** — and E[𝓔(U₀) | U_k] carries the backward spread of the kernel noise (given the soft U_k, the
deterministic block of U₀ is undetermined by the injected noise), which must cancel against the noise in the law of U_k
because the total is kernel-independent (Lemma BARE). That is the same noise bookkeeping in conditional form. In addition it
needs (LF-inst) (R2.4 (ii)).

**T3 verdicts.** (NOISE-ADD): survives (input of the soft block route only; direction correct; nonlinear case NOT-VERIFIED).
(ANTI-♭): survives as an OPEN input of the soft block route; route (β) refuted as a reduction (Codex; agreed); replacement
needs (NOISE-SUB). Branch D: avoids both, needs hard-scheme hypotheses + (S4c-lin). Bare 4D witness: avoids both formally,
needs (SRC^S) — noise bookkeeping in conditional form — plus (LF-inst).

## §R4. Checks (criteria before scripts; exact arithmetic only; nice 10; all < 20 s, < 100 MB)
| id | files (UTC, from the run log) | result | could it fail? |
|---|---|---|---|
| h2_55_a | criteria 03:17-03:18Z (one garbled phrase in A6.4 deleted and header times corrected 03:18-03:19Z, before any h2_55 script); script + run 03:20Z; `h2_55_a_out.txt` | **27/27 gates PASS; 6/7 controls fire; registered VERDICT: FAIL** — control A3-F (sign-flipped T^I must fail Bianchi) did not fire because its premise was false: the Bianchi contraction annihilates every first-pair structure carried by p, so it cannot see signs inside T^I | yes: A1 (h′ sign; A1-F gives h′ ≥ 0), A2 (A2-F), A4.1 (wrong exponent fails), A5 (factorial), A6 (4D trace), A7 (measure) all fired |
| h2_55_a2 | criteria 03:21Z (after the a run, before the a2 script); run 03:21Z | **PASS**: G1 (Gram form), G2 (Bi[T^I] = 0, Bi[I] ≠ 0); controls C1 (Bi[T^I + I] ≠ 0), C2 (sign-flipped T′ fails the Gram identity), C3 (Bi[2I] ≠ 0) fire | yes |
| h2_55_b | criteria 03:18Z; control B1-F corrected at 03:21Z (first typed 03:22Z) before any b script — the first version (∂G only) could not fire, every commutator still carrying one c; run 03:23Z | **15/15 gates, 6/6 controls: PASS**. B5.1: 2 − tr P = 4 sin²a sin²b | yes (B1-F, B2-F, B3-F, B4-F, B5-F, B6-F fired) |
| h2_55_d | criteria 03:18Z; run 1 at 03:23Z killed ~03:33Z with no output (D2's linear threshold search did not terminate; kept as `h2_55_d_run1_abort_*`); run 2 at 03:34Z with only that search replaced by an exact binary search | **4/4 gates, 4/4 controls: PASS** (D1: 43 200 exact inequalities; D2: 200 sets) | yes (D1-F increasing e violates; D2-F, D3-F, D4-F fired) |
*What the checks do not test:* Fatou/monotone-convergence steps, Schwartz's point-support theorem, Weyl's theorem, ODE
uniqueness, the large-q bound and regulator bookkeeping of GC-ξ (b), the flow-stability and shrinking-rate inputs of R2.4
(ii), and every Yang–Mills estimate. They support exact algebra and arithmetic only.

## §R5. Corrections to this run's own text (appended, not edited in), and notes on HINT55
*Corrections (this run, found on re-reading after appending; the text above is left as written):*
- **E1 (times).** The §R1 heading says "appended from 2026-10-29T03:36Z"; the append began at 03:39Z (date -u). The §R2 heading
  says "03:41Z"; that append began at 03:40Z. No content depends on either.
- **E2 (GC-ξ powers).** In R1.3 read: ⟨t²E_1(t)[cA]⟩ = c²⟨t²E_c(t)[A]⟩ = c²f₀ + c⁴Q_t(ξ) + O(c⁶), f₀ := A_∞e² (regulated), with
  Q_t(ξ) = κ₂e⁴ξ² + κ₁(t)ξ + κ₀(t), κ₂ > 0 [PROVEN-HERE, formal level] and κ₁(t) = −(N/(16π²))e²f₀·log(t/s₀) + O(e²f₀) [ARGUED].
  The display "⟨t²E_c(t)[A]⟩ = c²·(tree) + c⁴e⁴·Q_t(ξ)" and "−(N/(16π²))·log(t/s₀)·(tree)/e²" had the powers of c and e wrong;
  the derivation (and the PRE-STATED preliminary value "−Nξe²/(16π²)·log(t/s₀) times the tree value") are unchanged.
- **E3 (ID♮).** "O^♮ depends on A only through dA": the argument shows invariance under A → A + dλ; on a torus a quadratic
  form with that invariance factors through dA only up to the harmonic (constant) part of A. For the two observables used
  (𝓔^♮ = ¼|e^{τΔ}dA|², Ψ^♮_m = Σ|φ_m|² with φ_m a block flux) the dependence on dA alone is explicit.
- **E4 (NOBS).** "⟨E_pl(τ, x)⟩ > 0 at every x (translation invariance)" needs the λ-covariance translation invariant as
  well as nondegenerate; without it the lemma gives ⟨S_fl(V(τ))⟩ > 0, which suffices for the decision.
- **E5 (R2.4 (ii) wording).** "decays only like exp(−c(log 1/g_j)^{2p}), polylogarithmically in log L^j" should read: decays
  like exp(−O((log j)^{2p})) in the level j (since 1/g_j² ≍ j log L), i.e. slower than any exponential in j; and the needed
  bound is O(g_k^{2−2ϑ}), not o(·).
- **E6 (R3.3).** Differentiability of A^{K−m} at the identity is part of (S4c-lin), not a quoted property: EXISTENCE `X-S4c`
  states continuity, locality and covariance (the map is built from principal logarithms, averages and exponentials, so
  smoothness near 1 is expected, not verified here).
*Errata to the stopped draft:* none — it contained no derivation, value or check.
*Notes on HINT55 (inputs and labels, not banked items; no edit of HINT55):* (1) §4.5 "(TS-up) … standard UV-stability
content" — for the bare 4D density it needs (SRC) and (LF-inst) (R2.4); (2) §2.3's formal scale invariance of covariant-gauge
Gaussian connections fails for ξ > 0 at order e⁴ (R1.3 (b), ARGUED); (3) §1.1's flow normalisation is replaced by R1.1's
(Codex's point); (4) §2.8 (N1) REFUTED by Codex, repaired by 𝔊^col (R1.5); (5) §2.6 "K ≥ 2 subtractions ARGUED" is now
PROVEN-HERE (UV-D_∞, R1.6); (6) §9.4 continuity → upper semicontinuity, and §8.2's grid limit → Lemma INT (R2.2), both on
Codex's corrections.

## §R6. Summary table (claims of this resumed run) and what changes for PROOF.md / HANDOFF
| # | claim (locating string) | label |
|---|---|---|
| 1 | Flow/energy normalisation fixed; Σ_xE_pl = S_fl (R1.1) | PROVEN-HERE (definitions + one expansion) |
| 2 | Lemma CONTR: E_c[A] = c^{−2}E_1[cA]; c = 0 gives the abelian composite; lattice second-order contraction (R1.2) | PROVEN-HERE (+ h2_55_b B1) |
| 3 | (ID♮) the contraction identification | DEFINITION (named) |
| 4 | Lemma NOBS: the nonabelian flow of a lattice abelian pure gauge has ⟨S_fl(V(τ))⟩ > 0 while F ≡ 0 | PROVEN-HERE (+ B5) |
| 5 | GC-ξ (a): ξ²-coefficient of the order-e⁴ term of the Gaussian-connection realisation is > 0, finite, t-independent | PROVEN-HERE at the formal-expansion level (+ B2, B6); powers per E2 |
| 6 | GC-ξ (b): ξ¹-coefficient carries −(N/16π²)e²f₀ log(t/s₀) | ARGUED (+ algebraic core B2-B4) |
| 7 | T1(e) decision: the nonabelian flowed density of a free field is not an observable of the free theory | PROVEN-HERE (from 4; 5 for the continuum) |
| 8 | Lemma PAIR: one-point function of the quadratic composite = paired two-point function, any law, any PSD colour metric | PROVEN-HERE |
| 9 | 𝔊^col, Lemma COL; (N1) corrected; Codex's counterexample excluded | PROVEN-HERE (+ A1, A2); agree with Codex's REFUTED |
| 10 | Theorem UV-D_∞ (every number of subtractions; also for self-similar smearings with w ≢ 0 on an annulus) | PROVEN-HERE (+ A4) |
| 11 | Theorem SEP^col (all colour metrics, all subtractions, all contact polynomials, any law, mixtures) | PROVEN-HERE |
| 12 | Exact free values table (Maxwell any colour matrix; Proca; GFF; contact; mixtures) | PROVEN-HERE (+ A5) |
| 13 | Lemma REP: every O(4)/Bianchi representative with the same separated-point two-point function is in 𝔊^col_∞ | PROVEN-HERE given two IMPORTED-standard facts (point support; Weyl FFT) (+ A3, a2) |
| 14 | Proposition T0 (time-zero magnetic witness: comparator value is a reconstructed-theory number; monotone; no subtraction or contact caveat) | PROVEN-HERE for generalised free fields (+ A6); CONDITIONAL on tensor KL (IMPORTED) for interacting abelian theories; YM-side finiteness ARGUED/OPEN |
| 15 | No one-point witness without a fixed identification; 4D flowed one-point functions are Euclidean-representative data; bounded observables need (ID♮) | PROVEN-HERE by examples (+ A7) |
| 16 | Named YM bounds (TS-up), (TS-low), (MOM-E); (CONV-E) no longer an input (Lemma CONV) | statement; Lemma CONV PROVEN-HERE |
| 17 | Lemma INT (e(τ) non-increasing; f(t) ≤ L⁴f(t^{(m+1)})) | PROVEN-HERE (+ D1) |
| 18 | Theorem H-RED♮ (uniform family, continuous-time family, zero bare charge on all of D, usc, SEP^col) | PROVEN implication; CONDITIONAL on (F-tune), (TS-up), (TS-low), (MOM-E) (+ D2) |
| 19 | Remark B-BR: (UNIV-1L) replaceable by the two-sided bracket (B-BR) in F-flow/F-tune/F-ind; (B-BR) ⇔ (UIR^♮_br) | PROVEN-HERE (inspection of FLOW §7-§9; substitution in FLOW55's identity) (+ D3) |
| 20 | Full chain H_int ⇐ (UIR^♮_br) [⇐ (UIR^♮)] + (SF-g) + (RLF-δ) + (SF-cont) + (SF-∞) + (TS-up) + (TS-low) + (MOM-E), rel. (ID♮) | PROVEN implication; inputs OPEN as listed (R2.3) |
| 21 | (TS-up) for the bare 4D density needs (SRC) and a sharp large-field bound (LF-inst); Balaban-type e^{−cp(g)²} factors do not suffice via the union bound | ARGUED (the growth comparison is exact; the flow-stability/shrinking inputs are [m]) |
| 22 | Block observable (Branch D): (TS-up) level-local, = X-NTAF's halves | ARGUED (reading of EXISTENCE X-NTAF, not re-verified) |
| 23 | T3: (NOISE-ADD) survives (soft block route only); (ANTI-♭) survives as OPEN input, route (β) does not; Branch D avoids both but needs hard-scheme H-Bal-1, H-loc-LF, H-sg, (S4c-lin); bare 4D witness avoids both formally, needs (SRC^S) + (LF-inst) | verdicts as argued in §R3 (agree with Codex on NOISE-ADD/ANTI-♭) |
| 24 | k₁ conversion (Codex): 4k_g/b₀ = 4γ_E + 208/33 − (36/11)log 3 | arithmetic re-checked (+ D4); k_α's value [m] |
*Checks:* h2_55_a registered FAIL (27/27 gates, 6/7 controls: one mis-designed control), superseded for its control by
h2_55_a2 PASS; h2_55_b PASS; h2_55_d PASS (run 2; run 1 aborted without output).

**What should change in PROOF.md / HANDOFF (recommendations to the lead; this worker edits neither).**
1. HANDOFF row H_int: "free comparator banked for a narrower class" can become, after Codex review, "comparator side PROVEN
   for the observable as realised under the contraction identification (ID♮): all colour normalisations (matrix class),
   all Källén–Lehmann subtractions, all contact representatives, any law, mixtures (SEP^col); the nonabelian flow of a free
   field is shown not to be a free-theory observable". The identification is a named definition; no one-point witness can
   do without one.
2. The Yang–Mills side is now exactly: (UIR^♮_br) [implied by (UIR^♮)] + layer-1 (SF-g), (RLF-δ), (SF-cont), (SF-∞) + (TS-up)
   + (TS-low) + (MOM-E). (CONV-E) and the continuous-time limit are no longer open (Lemmas CONV, INT).
3. **Critical-path consequence.** For the bare 4D flowed witness, (TS-up) is not level-local: it needs (SRC) and a large-field
   bound sharper than any Balaban-type factor in the lane ((LF-inst), the lattice form of the small-instanton convergence
   11N/3 > 4). The bounded, level-local deterministic block witness (Branch D) avoids this — its (TS-up)/(TS-low) are X-NTAF's
   two halves — but needs a hard-scheme flow (H-Bal-1 for the hard couplings), H-loc-LF, H-sg and (S4c-lin), none supplied by
   the soft RG. So the choice of H_int witness is coupled to the choice of RG scheme (decision 4): with the soft scheme the
   witness costs (SRC^S) + (LF-inst) (bare flowed) or (NOISE-ADD) + (ANTI-♭ via NOISE-SUB) (deterministic block); with a hard
   scheme it costs Branch D's hypotheses.
4. If "survives the physical OS quotient" is read as "a reconstructed-theory number on both sides", only a sharp-time
   witness (Proposition T0) meets it on the comparator side; its Yang–Mills side adds sharp-time finiteness to (TS-up)^B.

**End of HINT2_55 resumed findings (worker claude-opus-5-5).**

*Corrections, continued (appended after §R6 on a final re-read; text above left as written):*
- **E7 (R2.4 contrast paragraph).** "Nπ²P_k ≤ Nπ²e^{−p(g_k)} ≪ g_k²" uses e^{−p(g_k)} for the same large-field factor written
  e^{−c p(g)²} two paragraphs earlier; with p(g) = (−log g)^p, e^{−c(log 1/g)^{2p}} ≪ g² requires 2p > 1 (or c > 2 at 2p = 1).
  This is a property of the imported large-field factor (PROOF.md `L5`), not verified here.
- **E8 (R1.9 "no subtraction limit").** A reconstructed theory whose spectral measure needs a subtraction (∫dρ/(1 + s) = ∞)
  has ∫dρ/√s = ∞, hence f_B ≡ ∞: its smeared time-zero magnetic field does not exist. Such theories are excluded trivially
  (they cannot match a finite Yang–Mills value), not by the monotonicity; "no subtraction limit" means that no restriction on
  ρ has to be imposed by hand.

## §R7. Addendum: the pre-registered check h2_55_c, and the plan items of the PRE-STATED not carried out
**h2_55_c** (pre-registered in the PRE-STATED; criteria and script written in one command at 03:45:13Z by file mtime, the
criteria file first — its header says "03:46Z", typed before reading the clock; run 03:45Z): **PASS** (4/4 gates, 2/2
controls). [Same kind of header slip for h2_55_a2: header "03:21Z", file mtime 03:20:57Z.]
**Proposition WN (wrapped-normal monotonicity). PROVEN-HERE** (Poisson summation for the wrapped normal IMPORTED-standard;
exact core h2_55_c C1-C4). For a centred Gaussian X of variance v: E[2(1 − cos X)] = 2(1 − e^{−v/2}) and
E[2 dist(X, 2πZ)²] = 2π²/3 + 8Σ_{n≥1}(−1)^n e^{−n²v/2}/n² are strictly increasing in v (derivatives e^{−v/2} and
4Σ_{n≥1}(−1)^{n+1}e^{−n²v/2} ≥ 4(e^{−v/2} − e^{−2v}) > 0) and bounded by their v → ∞ limits 2 and 2π²/3.
*Consequence for Codex's bounded-observable obstruction.* For Codex's one-colour literal observables B_s = 2(1 − cos X_s),
Ψ_s = 2 dist(X_s, 2πZ)², X_s a self-similar linear smearing with w ≢ 0 on an annulus, every **Gaussian** member of 𝔊^col_∞
and every mixture of such fails (AF-W): in case (a) of UV-D_∞, v(s) = Var X_s is non-increasing in s (KLM), so E B_s, E Ψ_s are
non-increasing in s; in case (b), v(s) → ∞ as s ↓ 0 and the expectations increase to their suprema; mixtures by Fatou
(bounded). So the obstruction genuinely needs **non-Gaussian** contact noise (Codex's compound-Poisson law is non-Gaussian),
and (ID♮) removes it for every law. (For SU(N) block energies the literal reading would need a map from the abelian field to
SU(N); (ID♮) does not need one.)
**PRE-STATED plan items not carried out (stated, not hidden).** (1) h2_55_a's "Proca/GFF monotonicity at rational points":
not done — the monotonicity is pointwise (the integrand v²e^{−2v}/(v + σ) of J decreases in σ), and a rational-point
evaluation would need rigorous E₁ enclosures while adding nothing; R1.7's monotonicity rests on the pointwise argument.
(2) h2_55_b's "α₀-independence test" of the order-e⁴ logarithm: not done, because the derivation used never involves α₀
(R1.3); GC-ξ (b) therefore stays ARGUED, exactly as the PRE-STATED pre-registered for this case. (3) T1(e)'s "compute the
order-e⁴ logarithm": computed only for its ξ-dependent parts; the ξ-independent (transverse flow-only) e⁴ term is not
computed. No pre-registered check id was removed (a, b, c, d all exist; a2 was added).
Summary-table additions: **25** Proposition WN — PROVEN-HERE (+ h2_55_c). §R4 addition: h2_55_c PASS.
- **E9 (Lemma INT notation).** With R1.1's definition 𝓔 = τ²E_pl(τ) (lattice units), f(t) = τ²e(τ), τ = t/a²; the proof's
  "f(t) = t²e(t/a²) ≤ (t^{(m)})²e(t^{(m+1)}/a²)" should read f(t) = τ²e(τ) ≤ τ_m²e(τ_{m+1}) = (τ_m/τ_{m+1})²f(t^{(m+1)}) =
  L⁴f(t^{(m+1)}). The written form differs by the common factor a⁻⁴ on both sides; the inequality and L⁴ are unchanged.

**End of HINT2_55 (resumed run, claude-opus-5-5; last append 2026-10-29T03:4xZ — see `date -u` stamps in the run log).**
