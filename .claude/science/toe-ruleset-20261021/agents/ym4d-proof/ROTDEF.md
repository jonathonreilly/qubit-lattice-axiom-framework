Reviewer model: claude-opus-5-5

# ROTDEF — T56-R4: the rotation-defect identity for one renormalized local observable, and where it needs the coarse-field law

## PRE-STATED — 2026-10-28T23:08:07Z (written before any derivation in this file)

**Role.** Opus 5.5 worker (model ID above, verbatim from the system prompt), effort max. Brief: scratchpad `queue/r4.md`;
rules: scratchpad `REVIEW_BRIEF_55.md`. No git. I write only this file and `checks/rd55_*`. Inputs read before this
pre-statement: `PANEL_P1.md` (all), `PANEL_P3.md` (all), `RTARGET.md` §55 + §55 CORRECTION, `REVIEW_S22.md`
`Statement (BFT)` block. No derivation for this file has been written yet.

**Target (from P3 §6 "smallest discriminating next artifact", RTARGET §55 T56-R4).** For one specified renormalized,
scalar, gauge-invariant local observable O and two fixed, separated, smooth test functions f, g:
1. write the lattice infinitesimal-rotation identity for the two-point function <O(f) O(g)> after UV integration down
   to a fixed reference scale;
2. identify every term: source counterterms, the rotation-breaking insertion and its operator dimension, the
   boundary/annular contribution;
3. either prove that the normalized defect tends to zero uniformly in the containing torus from explicitly listed
   inputs (CONDITIONAL on exactly those), or
4. isolate the FIRST term whose bound depends on the unknown coarse-field law (R4-F1), and say whether the information
   it needs is weaker than infinite-volume uniqueness; flag R4-F2 if RP or gauge invariance is lost anywhere.

**What would count as success / failure, stated before deriving.**
- *Success (CONDITIONAL theorem):* a bound |defect| <= eta(a) + b(R) with eta -> 0 as a -> 0 uniformly in the torus
  side R, b -> 0, every input named (BFT clause numbers, large-field bound, coupling-flow statement), no hidden use of
  decay of coarse-field correlations.
- *Honest reduction (R4-F1):* the first term whose bound needs information on the coarse law, written as an explicit
  expectation in the selected finite-volume state, plus a proof that it is (or is not) implied by infinite-volume
  uniqueness, and an example or argument showing whether it is strictly weaker.
- *Refutation of my own route:* if the identity I write has a term I cannot bound and cannot express as a coarse-law
  statement, or if the normalization makes the defect trivially small (a check that cannot fail), I will say so.
- *Inconclusive (to be labelled as such):* any step that only holds at zero background, on one fixed torus, or as a
  formal series.

**Labels used.** PROVEN (complete argument here), CONDITIONAL (named inputs), ARGUED (stated gap), OPEN, [m]
(literature from memory, unverified). Inherited PROVEN labels from the lane are treated as unverified claims.

**Numeric checks.** Only if a number decides something; criteria file `checks/rd55_<id>_criteria.md` first, exact
rational arithmetic in plain python.

---

## 1. Result in one page (details and proofs in §2-§10; every label is argued where the claim is made)

**Verdict on the target.** I could NOT prove that the normalized rotation defect tends to zero uniformly in the torus.
I give instead the exact lattice identity, every term in it, a CONDITIONAL proof that every term except one tends to
zero uniformly in the torus, and the exact form of the one remaining term. That term is the first (and only) one whose
bound needs information on the unknown coarse-field law. It is **not** a uniqueness statement (R4-F1 in its literal form
does not occur). It is an infrared statement, and given the UV inputs it is *equivalent* to OS1 for the tested pair. So
this route reformulates the IR content exactly; it does not shrink it further. R4-F2 does not occur.

- **Observable (§2).** The clover plaquette energy density e_a(x), smeared: O_a(f) = Σ_x a⁴ f(x) e_a(x); the two-point
  function ω(O_a(f)O_a(g)) with f, g ∈ C_c^∞(R⁴), separated supports. The normalized defect is
  D(s) := [ω(F_s) − ω(F)]/Z_e(a)², with F_s := O_a(f∘Q_s⁻¹)O_a(g∘Q_s⁻¹), Q_s = e^{sJ}, and Z_e(a) the multiplicative
  renormalization of e_a fixed by the UV RG (input SRC-E), not by the state.
- **Exact identity (§3, PROVEN).** For the Wilson measure on a finite torus and any smooth configuration-space vector
  field Ξ: ω(ΞF) = Cov_ω(F, 𝔚), where 𝔚 := ΞS − div Ξ. With Ξ the gauge-covariant lattice Lie derivative along
  v_r = ψ_r·Jx (ψ_r a radial cutoff, = 1 on |x| ≤ r, = 0 on |x| ≥ 2r), Cov_ω(F, 𝔚(v_r)) is **exactly independent of r**
  (for r beyond the observable supports), because 𝔚(v) is uncorrelated with F whenever v vanishes near F.
- **Terms (§4).** (i) *Source terms* on the observable side. The multiplicative and additive renormalizations of e_a
  cancel in D. H(4) allows exactly two O(1) structures: a factor (1+ϑ₁) on the geometric derivative, and a finite mixing
  ϑ_Δ with a total-derivative stress structure. Both are generated at the cutoff scale, so ϑ = O(g_bare²) → 0 by
  asymptotic freedom (logarithmically). (ii) *The rotation-breaking insertion* has operator dimension exactly 6.
  Dimension 4 is excluded by a selection rule I checked exactly: no dimension-4 gauge-invariant operator carries the
  representation of a rotation generator under H(4), m(A in S²A) = 0 (`checks/rd55_rep_out.txt` C5). Dimension 5 is
  excluded by total inversion. Dimension 6 does occur (C7). The coefficient is a² up to logarithms. The same rule removes
  every O(1) or power-divergent contact counterterm between that insertion and the observables. (iii) *Boundary term*:
  the angular-momentum flux of the identity's own (symmetric, by the same selection rule) stress current through the
  shell r ≤ |x| ≤ 2r.
- **After UV integration to the reference level K (§5).** Every covariance splits exactly into ν_K[Cov(·,·|U_K)] plus
  Cov_{ν_K}(E_K[·], E_K[·]), where U_K is the soft chain's reference-scale field, ν_K its (unknown) law, and E_K = E[·|U_K].
  There is also an exact kernel identity: E_K[𝔚] = E_K[Ξ log K_0]. The coarse image of the Ward functional is the
  conditional mean of the RG kernel's response to the field redefinition.
- **CONDITIONAL theorem (§7).** Assume BFT-0..5, RLF v3 (incl. RLF-3′), the flow (F_R)/(RLF-δ), conditional decay CD, and
  source-inserted RG SRC (§6 lists each precisely; CD and SRC are NOT in the lane). Then for every r with
  r_F ≤ r ≤ R/4, uniformly in the torus side R,
  |(1+ϑ₁)D(s) + ∫₀ˢ TQ_ν(s′; r) ds′/Z_e²| ≤ s·C_F·[g_bare² + (a/ℓ_ref)² 𝔏(a)(r/ℓ_ref)⁵ + (r/ℓ_ref)⁴e^{−m_c r/ℓ_ref}],
  where 𝔏(a) is a fixed power of log(ℓ_ref/a).
- **The IR term (§8).** It is **TQ_ν(s; r) := Cov_{ν_K}(E_K[F_s], 𝒥_r)**, the coarse-law covariance between the
  observable's conditional expectation and the conditional angular-momentum flux 𝒥_r through the shell (an explicit sum
  of local coarse functionals). PROVEN (given the inputs): TQ_ν is r-independent up to the UV terms, and OS1 for the pair
  ⟺ TQ_ν → 0. It is "no rotation charge at infinity", i.e. absence of spontaneous rotation breaking in the selected limit.
- **R4-F1 comparison (§8.3).** TQ_ν → 0 follows from an o(|x|⁻⁴) decay, in logarithmic-Cesàro mean, of the coarse
  stress-channel covariance uniformly along the sequence. That is weaker than P2's |x|^{−4−η} and far weaker than a gap:
  gapless |x|⁻⁸ decay suffices. It is closed under mixtures of translation- and H(4)-invariant states, so it does not
  imply uniqueness. Uniqueness does not supply it: uniqueness carries no rate, and under the equivalence above such an
  implication would be uniqueness ⇒ OS1, which the panel showed needs action information. **So it is logically
  independent of bare uniqueness, and strictly weaker than "uniqueness + clustering with rate" and than a gap.**
- **Scale separation (§8.4, ARGUED; tensor facts CHECKED).** H(4)-invariant symmetric tensors of rank ≤ 3 are O(4)-invariant.
  The first cubic invariant is at rank 4 (`checks/rd55_tens_out.txt`). Consequently (CONDITIONAL on a UV input SRC-iso),
  the coarse law can affect the defect of observables at scale s_F ≪ ℓ_ref only at relative order (s_F/ℓ_ref)⁴.
  **The IR obstruction is confined to observation scales comparable to or beyond the reference scale.**

---

## 2. Setting, symbols, and the choice of observable

### 2.1 Symbols (collision check, REVIEW_BRIEF_55 defect 1)
| Symbol here | Meaning here | Collides with (file: locating string) | Resolution |
|---|---|---|---|
| a | fine lattice spacing (brief, P1, P3) | RLARGE §0 "The defect exponent": a := min{θa_bad, a_A} | RLARGE's exponent is written a_LF below |
| levels | **RLARGE convention**: level 0 = bare/fine, level K = unit (reference) lattice (RLARGE §0 "Levels") | PROOF S1 uses the REVERSE ("resolution-0 spacing equal to 1 … UV cutoff is the resolution K") | I use RLARGE's levels only |
| g_bare, g_ref | coupling at level 0, at level K | RLARGE §1.2 writes both the level-0 coupling and the smallness threshold as "g_0" ("g_0, …, g_k ∈ (0, γ_0]" vs "g_K ≤ g_0") | threshold written g_thr |
| R | torus side (physical units; ℓ_ref = 1) | RLARGE (F_R) bracket constant R; P1 "R for the physical box size" | flow constant written R_F |
| Q_s = e^{sJ} | rotation, J ∈ so(4) | brief's α_R | — |
| ψ_r | radial cutoff, ψ_r(x) = h(|x|/r), h ∈ C^∞, h = 1 on [0,1], h = 0 on [2,∞) | RLARGE χ_Q (indicator) | ψ, not χ |
| 𝔚(v) | Ward functional ΞS − div Ξ | RLARGE chain weight W(U_0,…,U_K) | fraktur 𝔚 |
| U_K, ν_K, E_K | reference-level soft field, its law, E[·|U_K] | PROOF ν_m (block laws of S4'' iterates, a different object) | — |
| ϑ₁, ϑ_Δ | finite source-mixing constants (§4) | κ (soft coupling) | ϑ, not κ |
| m_c | conditional decay rate (input CD) | BFT-3 m_0 | distinct |

ℓ_ref := L^K a = 1 is the reference scale, the unit lattice of RLARGE level K. The torus is hypercubic, with side R
(even in lattice units, for RP). The fine lattice is aZ⁴/RZ⁴ and the gauge group is SU(N), N ≥ 2. The Wilson
action is S = u_0 Σ_p s(U_p), with s(U) = 1 − N⁻¹Re tr U and u_0 = 1/g_bare². ω = ω_{a,R} is the normalized Wilson state.

### 2.2 The observable and the test pair
- **e_a(x)** := (4a⁴)⁻¹ Σ_{μ≠ν} Σ_{p ∈ clover_{μν}(x)} s(U_p). Here clover_{μν}(x) is the set of 4 plaquettes in the
  (μ,ν) plane with a corner at x, and the double sum over ordered μ≠ν counts each unordered plane twice (harmless
  normalization). Properties: gauge invariant; supported on links within distance a of x; invariant under H(4)_x (the
  signed permutations about the site x); smooth in U. Σ_x a⁴ e_a(x) = 2 Σ_p s(U_p), a fixed multiple of the Wilson
  action (each plaquette lies in exactly 4 clovers; factor 1/4; factor 2 from ordered pairs).
- **O_a(f)** := Σ_{x ∈ aZ⁴} a⁴ f(x) e_a(x), f ∈ C_c^∞(R⁴). Take f, g supported in the ball B_{ρ_F}, with
  dist(supp f, supp g) ≥ d > 0. Rotation about the origin preserves |x| and distances, so every rotated pair
  (f_s, g_s) := (f∘Q_s⁻¹, g∘Q_s⁻¹) has the same support radius and separation. Set r_F := 2ρ_F + 2.
- **F_s** := O_a(f_s)O_a(g_s), with d/ds O_a(f_s) = O_a(J f_s), where (Jf)(x) := −(Jx)·∇f(x).
- **Normalized defect** D(s) := [ω(F_s) − ω(F_0)]/Z_e(a)². Since ω(e_a(x)) is translation-invariant up to O(a^∞)
  smoothing errors and ∫f_s = ∫f, the disconnected part is rotation-invariant: D is the defect of the connected function.

**Why this observable (justification).**
1. It is strictly local: its links lie within distance a of supp f. A test function supported in {t > a} gives a
   positive-time lattice observable, so Wilson-lattice RP applies to it directly. No localization limit is needed (P1 §1:
   "heat-flow smoothing in Euclidean time reaches across a reflection plane").
2. It is an H(4)_x-scalar. By R1 (§4.2, checked exactly) the only H(4)-invariant, reflection-even, gauge-invariant
   dimension-4 operator is Σ tr F², so e_a mixes at dimension ≤ 4 only with itself and the identity. The identity
   cancels in the connected function. Z_e(a) is common to F_s and F_0. No rotation-sensitive counterterm can enter at
   dimension ≤ 4.
3. The gradient-flowed density E(t,x) at fixed t > 0 needs no renormalization, which is attractive. It fails 1: at fixed
   t it is not localized, and RP of the flowed algebra holds only in a t → 0 limit at fixed support distance (P1 §3,
   P3 §2). The lattice flow is also only H(4)-covariant, so it adds a second rotation-breaking source. Choosing it would
   flag R4-F2 for a reason unrelated to OS1. **Rejected.**

**Guard against a vacuous pass (REVIEW_BRIEF_55 defect 3).** Normalizing by Var(O_a(f)) would be wrong. That variance
diverges like a⁻⁴ (coincident-point singularity |x−y|⁻⁸ of the energy correlator), so any defect divided by it tends
to 0 whatever the state does. D is instead divided by the state-independent Z_e(a)². D can still pass vacuously if the
renormalized correlator itself tends to 0, for instance in a trivial limit. Excluding that needs a lower bound on
ω_c(O_a(θg)O_a(g))/Z_e² for one reflected pair (≥ 0 by RP; strict positivity uniform in (a,R) is **not** supplied
here). It belongs with P1's H_int/non-freeness input.

*Erratum to §2.2 (append-only correction).* "ω(e_a(x)) is translation-invariant up to O(a^∞) smoothing errors" should
read: ω(e_a(x)) = c_a is exactly lattice-translation invariant. The disconnected defect is c_a²·[Σ a⁴f_s Σ a⁴g_s −
Σ a⁴f Σ a⁴g]. The Riemann sums of C_c^∞ functions equal their integrals up to O(a^M) for every M (Poisson summation).
The integrals are rotation invariant. c_a is at most O(a⁻⁴). So the disconnected defect is O(a^{M−8}) for every M.

---

## 3. The exact lattice identity (all PROVEN; finite torus, every configuration, no small-field restriction)

**3.1 Integration by parts.** The configuration space is 𝒞 := SU(N)^𝔅, with 𝔅 the positively oriented fine bonds,
and dU is the product Haar measure. Fix an orthonormal basis {T_α} of su(N). Let ∂^α_b be the derivative along
U_b → e^{tT_α}U_b (left) and ∂̃^α_b the derivative along U_b → U_b e^{tT_α} (right). A smooth vector field is
Ξ = Σ_{b,α}(ξ^α_b ∂^α_b + ξ̃^α_b ∂̃^α_b), with div Ξ := Σ_{b,α}(∂^α_b ξ^α_b + ∂̃^α_b ξ̃^α_b).

- **Lemma 3.1.** ∫ Ξ(Φ) dU = −∫ (div Ξ) Φ dU for smooth Φ. *Proof.* Haar measure is left- and right-invariant, so
  d/dt ∫Φ(…e^{tT_α}U_b…)dU = 0, i.e. ∫∂^α_bΦ = 0, and likewise for ∂̃. Apply this to ξ^α_bΦ and ξ̃^α_bΦ, and use the
  Leibniz rule. ∎
- **Proposition 3.2 (Ward identity).** Let 𝔚 := ΞS − div Ξ. Then ω(𝔚) = 0 and ω(ΞF) = Cov_ω(F, 𝔚) for every smooth F.
  *Proof.* Lemma 3.1 with Φ = F e^{−S} gives ∫Ξ(F)e^{−S} = ∫F(ΞS − div Ξ)e^{−S}. Divide by Z. Taking F = 1 gives ω(𝔚) = 0. ∎

**3.2 The lattice Lie-derivative field Ξ_v.** v is a smooth vector field on R⁴ (on the torus: compactly supported in a
fundamental domain). For a bond b = (x, x+aμ̂), let P^{±ν}_b be the holonomies of the two plaquettes in the (μ,±ν) planes
that contain b, both based at x and starting with U_b (with U_{y,−ν} := U_{y−aν̂,ν}⁻¹). Let π be the projection onto
traceless anti-Hermitian matrices, π(M) = (M − M^†)/2 − tr(M − M^†)/(2N). Define
  𝔣^ν_b := (2a²)⁻¹[π(P^{+ν}_b) − π(P^{−ν}_b)] ∈ su(N),   ξ_b(v) := −a Σ_{ν≠μ} v^ν(m_b) 𝔣^ν_b,
where m_b is the midpoint of b. Ξ^left_v varies U_b → e^{tξ_b}U_b. Ξ^right_v is its mirror image: plaquettes based at
x+aμ̂, acting by right multiplication. Set Ξ_v := ½(Ξ^left_v + Ξ^right_v). Properties:
- (Lin) Ξ_v is linear in v and reads v only at midpoints: ξ_b depends on v(m_b) alone. *Immediate from the definition.*
- (G) Gauge covariance. Under U_b → g_xU_bg_{x+aμ̂}⁻¹, P_b → g_xP_bg_x⁻¹, so ξ_b → g_xξ_bg_x⁻¹ and e^{tξ_b}U_b → g_x e^{tξ_b}U_b g⁻¹_{x+aμ̂}.
  The right part is analogous. Hence Ξ_v commutes with gauge transformations: Ξ_vS and div Ξ_v are gauge invariant (Haar
  measure is gauge invariant), and so is 𝔚(v). Each coefficient of 𝔚 in its linear dependence on {v(m_b)} is
  gauge invariant (take v supported at one midpoint).
- (Loc) ξ_b depends only on the links of the two plaquettes through b.
- (H)/(T) Covariance under the hypercubic group H(4) and lattice translations: a lattice symmetry h maps Ξ_v to Ξ_{h_*v}.
  For a reflection of an axis ν ≠ μ, P^{+ν} ↔ P^{−ν} and v^ν → −v^ν leave ξ_b invariant. For the reflection of μ itself,
  the left/right symmetrization exchanges the two halves. Permutations relabel. (Checked by inspection; it is used only
  to justify the selection rules of §4.)
- (C) Classical consistency, standard and not re-derived in full here. For smooth fields, P_{μν} = exp(a²F_{μν} + O(a³)),
  so 𝔣^ν_b = F_{μν} + O(a), and the left/right average cancels the O(a) term by inversion. Then Ξ_v acts as
  δA_μ = v^νF_{νμ} + O(a²), the gauge-covariant Lie derivative (δA = L_vA − D(v·A)).

**3.3 Locality and cutoff independence.** Let dep(G) be the set of bonds on which G depends.
- **Lemma 3.3.** (i) If v(m_b) = 0 for every b ∈ dep(G), then Cov_ω(G, 𝔚(v)) = 0.
  (ii) If v = v′ at the midpoints of dep(G), then Cov_ω(G, 𝔚(v)) = Cov_ω(G, 𝔚(v′)).
  *Proof.* (i) By (Lin), Ξ_vG involves ξ_b only for b ∈ dep(G), and these vanish, so ω(Ξ_vG) = 0. Apply Prop. 3.2.
  (ii) Apply (i) to v − v′ and use linearity of 𝔚. ∎
- **Corollary 3.4 (the identity used below).** Let v_r := ψ_r·Jx, with r ≥ r_F (r_F := 2ρ_F + 2, ℓ_ref = 1, a ≤ 1).
  Then ψ_r = 1 at every midpoint of dep(F_s) for every s, since rotation keeps supp f_s ∪ supp g_s ⊂ B_{ρ_F}. Define the
  observable-side source term exactly by
    𝒞(s) := ω(Ξ_{v_r}F_s) − ω(O_a(Jf_s)O_a(g_s)) − ω(O_a(f_s)O_a(Jg_s)).
  By (ii) it does not depend on r. Then **d/ds ω(F_s) = Cov_ω(F_s, 𝔚(v_r)) − 𝒞(s)**, and **Cov_ω(F_s, 𝔚(v_r)) is the
  same number for every r ≥ r_F** (for r ≤ R/4, so that supp v_r fits in a fundamental domain).
  Integrating: ω(F_s) − ω(F_0) = ∫₀ˢ [Cov_ω(F_{s′}, 𝔚(v_r)) − 𝒞(s′)] ds′.

*Remark 3.5 (what 3.4 does and does not say).* The defect is equated with a covariance of F against a functional
spread over the whole ball B_{2r}. Nothing yet is small. Its r-independence is exact at every (a, R) and for every
configuration law. This is the lattice form of "the rotation charge measured on any surface surrounding F is the same"
(P3 §4: "a global rotation Ward identity … can leave an annular/boundary contribution").

---

## 4. Every term: source terms, the rotation-breaking insertion, the boundary torque

### 4.1 Selection rules (exact algebra; the decisive one is checked by exact computation)
Notation: V = R⁴ (vector rep of H(4)); A = Λ²V (rotation generators, 6-dim); the gauge-invariant dimension-4 operators
tr(F_{μν}F_{ρσ}) span S²A (the trace bilinear is symmetric), 21-dim. Check `checks/rd55_rep.py`. Criteria were written
first in `rd55_rep_criteria.md`; output is in `rd55_rep_out.txt`. Every criterion passed, including the control that must
fire, C6: m(A in Λ²A) = 1.
- **R1 (CHECKED, C4).** m(trivial in S²A) = 1, m(det in S²A) = 1. The only H(4)-invariant dimension-4 operator is Σ tr F²,
  and the only det-twisted one is tr FF̃. This agrees with the lane's GT (PROOF "Lemma GT"), P1 §3 and P2 §7.2; C2 also
  re-confirms GT's irreducibility claim for Λ²R⁴.
- **R2 (CHECKED, C5). m(A in S²A) = 0** (and m(A⊗det in S²A) = 0; also ⟨A, A⊗det⟩ = 1, so A ≅ A⊗det under H(4)). **No
  dimension-4 gauge-invariant operator carries the representation of a rotation generator, even though only H(4) acts.**
  The full H(4) content of S²A is 1 ⊕ det ⊕ 3 ⊕ 6′ ⊕ (three further irreps of total dimension 10). The off-diagonal
  symmetric 6′ is irreducible and ≇ A (C8).
- **P (inversion parity; PROVEN).** A gauge-invariant monomial of canonical dimension δ, built from F (two indices,
  dimension 2) and D (one index, dimension 1), carries exactly δ field indices. Total inversion −1 ∈ H(4) acts on it by
  (−1)^δ, and it fixes every contraction tensor (δ_{μν}, the cubic d_{μνρσ} = 1 iff all four indices are equal, and ε,
  since det(−1₄) = 1). So an equivariant map from dimension-δ operators to a rep ρ can be nonzero only if −1 acts on ρ by
  (−1)^δ. −1 acts on A trivially (χ_A(−1) = 6 = dim A) and on V by −1. Gauge-invariant local operators of dimension 1, 2, 3
  vanish (they are traces of single Lie-algebra-valued fields: tr F = 0, tr DF = ∂ tr F = 0). **Hence A-valued operators
  have dimension ≥ 6 (4 is excluded by R2, odd dimensions by P), and V-valued operators have odd dimension ≥ 5.**
- **Lemma 4.1 (dimension-5 vectors are total derivatives; PROVEN).** Every gauge-invariant true-vector (not V⊗det) operator of
  dimension 5 is a combination of ∂_ν tr(F_{λμ}F_{λμ}), ∂_μ tr(F_{μλ}F_{νλ}) and ∂_ν Σ_β tr(F_{νβ}F_{νβ}) (no sum on ν; the
  last is H(4)-only). Each is a divergence ∂_μX_{μν} of a **symmetric** dimension-4 tensor.
  *Proof.* A dimension-5 monomial is tr(F_{αβ}D_γF_{δε}): 5 field indices and 1 free index contracted by three δ's, or by
  one d plus one δ. ε-contractions give V⊗det; an axis reflection σ has χ_V(σ) = 2 and χ_{V⊗det}(σ) = −2, so these are
  not true vectors. *δδδ:* enumerating the free-index slot and the pairings, every nonzero contraction is ± one of
  (i) tr(F_{νλ}D_μF_{μλ}), (ii) tr(F_{λμ}D_νF_{λμ}) = ½∂_ν tr F², (iii) tr(F_{μλ}D_μF_{νλ}). The Bianchi identity gives
  D_μF_{νλ} = −D_νF_{λμ} − D_λF_{μν}. So (iii) = tr(F_{μλ}D_νF_{μλ}) − tr(F_{μλ}D_λF_{μν}) = ½∂_ν tr F² − (iii), after
  relabelling μ↔λ in the last term. Hence (iii) = ¼∂_ν tr F². Then ∂_μ tr(F_{μλ}F_{νλ}) = (i) + (iii) gives
  (i) = ∂_μ tr(F_{μλ}F_{νλ}) − ¼∂_ν tr F². *d + δ:* d needs four equal indices. If d takes four field indices, it takes
  both indices of one F, and F_{αα} = 0. Otherwise d takes the free index, γ, and one index of each F, leaving
  Σ_β tr(F_{νβ}D_νF_{νβ}) = ½∂_ν Σ_β tr(F_{νβ}F_{νβ}). ∎
- **Lemma 4.2 (PROVEN).** For any H(4)-covariant 2-tensor X_{μν} of gauge-invariant dimension-4 operators, the antisymmetric
  part vanishes. *Proof.* X ↦ X_{[μν]} is equivariant into A, so it is zero by R2. ∎
- **C7 (CHECKED).** A dimension-6 H(4)-invariant that is not O(4)-invariant exists. For Σ_{μ,ν} tr(D_μF_{μν}D_μF_{μν})
  (no sum convention inside: μ repeated four times), on abelian plane waves the normalized value is 1 at
  k = (1,0,0,0) and 1/2 at k = (1,1,0,0) (same polarization), while the O(4) control gives 2 and 2. So the dimension-6
  breaking is generically present: the selection rules make it the *first* allowed dimension, not an absent one. (That
  this operator is the unique such dimension-6 term in pure gauge theory is [m] Lüscher–Weisz 1985, unverified here
  and not used.)

### 4.2 Observable side: the source terms 𝒞(s)
Near F, v_r = Jx exactly, and Ξ_v e_a(x) is linear in the values v(m_b) at finitely many midpoints. So, **exactly**,
Ξ_{Jx}e_a(x) = (Jx)^ν τ_ν(x) + J^ν_μ τ_{μν}(x). Here τ_ν := Σ_b θ_{b,ν} (the covariant-translation variation of e_a) and
τ_{μν} := Σ_b (m_b − x)_μ θ_{b,ν}, where Ξ_v e_a(x) = Σ_b v^ν(m_b)θ_{b,ν}(x). Put t_ν := τ_ν − ∇̄_νe_a (∇̄ is the
symmetric difference) and A_J := J^ν_μτ_{μν}. Since (J(x ± aν̂))^ν = (Jx)^ν (J_{νν} = 0), exact summation by parts gives
Σ_x a⁴ f(x)(Jx)^ν∇̄_νe_a(x) = Σ_x a⁴ [(Jf)(x) + r_f(x)] e_a(x), with r_f = −(Jx)^ν(∇̄_ν − ∂_ν)f = O(a²) on supp f. Hence,
exactly,
  𝒞(s) = Σ_x a⁴ f_s(x) ω_c([(Jx)^νt_ν(x) + A_J(x)] O_a(g_s)) + Σ_x a⁴ r_{f_s}(x) ω_c(e_a(x)O_a(g_s)) + (f ↔ g).
Replacing ω by ω_c is legitimate. By lattice-translation invariance and H(4)_x covariance, ω(t_ν) is an invariant vector,
hence 0, and ω(τ_{μν}) = cδ_{μν}, so ω(A_J) = c·tr J = 0. The term Σ a⁴r_f·c_a² is O(a^M) (Poisson summation).
**Content.** A_J is A-valued: dimension ≥ 6, coefficient a². t_ν is V-valued: dimension 5 (total derivatives, Lemma 4.1)
plus dimension 7 (coefficient a²). By (C), t_ν = O(a²) classically, so its dimension-5 part has no tree-level
coefficient. It can arise only as a finite, power-divergent mixing (a² × a⁻² × loop factor) generated at the cutoff
scale: t_ν ⊃ ϑ₁∂_ν e + ϑ_{6′}∂_μS^{(6′)}_{μν} + ϑ₃∂_νS^{(3)}_{νν}. Inserted with weight f(Jx)^ν, a symmetric divergence gives
Σ f(Jx)^ν∂_μX_{μν} = −Σ(∂_μf)(Jx)^νX_{μν}, with no J·X_{[μν]} term (Lemma 4.2). So ϑ₁ rescales the geometric
derivative (X = δe gives Σ(Jf)e), and ϑ_{3}, ϑ_{6′} give smeared stress components.

**The complete list of source counterterms for this identity.** (a) Additive renormalization of e_a: cancels in the
connected function. (b) Multiplicative Z_e(a): common to F_s and F_0, divided out. (c) ϑ₁, ϑ₃, ϑ_{6′}: the only O(1)
structures H(4) allows. Input SRC-O (§6) asserts they are O(g_bare²), which vanishes as a → 0 by asymptotic freedom,
but only like 1/log(1/a). (d) Contact terms between the rotation-breaking insertion and the observables: the A-valued
part integrated against the H(4)_y-symmetric neighbourhood of an observable point y is an A-valued local operator at y.
That has dimension ≥ 6, so the contact integral a²·a^{d_k−6} is at most a²·log. The total-derivative part produces
only J·X_{[μν]} = 0 plus shell terms. **No O(1) or power-divergent contact counterterm is needed, by R2 and P.** This is
the main structural gain of choosing an H(4)-scalar observable.

### 4.3 Action side: the rotation-breaking insertion and the boundary torque
Let 𝒯 be any symmetric, H(4)-covariant, gauge-invariant local lattice tensor. With ∇_μ the forward difference,
∇_μ(ψ(Jx)^ν) = (∇_μψ)(x)(Jx)^ν + ψ(x+aμ̂)J^ν_μ exactly, and J antisymmetric with 𝒯 symmetric. Hence Σ_x a⁴∇_μv_r^ν𝒯_{μν} = 𝔗_r, with
  **𝔗_r := Σ_x a⁴ [(∇_μψ_r)(x)(Jx)^ν𝒯_{μν}(x) + Σ_{μ<ν} J_{νμ}(ψ_r(x+aμ̂) − ψ_r(x+aν̂))𝒯_{μν}(x)]**,
supported on the shell {r − a ≤ |x| ≤ 2r + a}. This is the **boundary (annular) term**: the lattice angular-momentum flux
of 𝒯 through the shell. For radial ψ_r the trace part of 𝒯 contributes only O(a/r) pointwise, since (Jx)·∂ψ_r = 0.
Define the bulk remainder exactly by **𝔅(v_r) := 𝔚(v_r) + 𝔗_r**, so **𝔚(v_r) = −𝔗_r + 𝔅(v_r)**.

**Content of 𝔅 (the rotation-breaking insertion).** Where ψ_r ≡ 1, its density is b_J(x) = (Jx)^νω_ν(x) + J^ν_μω_{μν}(x),
by the same exact midpoint expansion as in 4.2. Here ω_ν is V-valued: a divergence of symmetric dimension-4 tensors
(Lemma 4.1) plus dimension 7. J^ν_μω_{μν} is A-valued: dimension ≥ 6. Summation by parts over the region ψ_r ≡ 1 turns
(Jx)^ν∂_μX_{μν} into −J^ν_μX_{μν} = 0 (X symmetric) plus a shell term. So **with 𝒯 the identity's own current (the X
whose divergence is the dimension-5 part of ω_ν), 𝔅 has no content of dimension < 6. The rotation-breaking insertion
has operator dimension exactly 6 (C7), coefficient a² up to logarithms.** A different choice of 𝒯 moves a symmetric
divergence between 𝔅 and the shell; it changes which tensor appears in the torque, never the dimension count. Over
|x| ≤ 2r the dimension-7 part carries the weight |Jx| ≤ 2r‖J‖, hence the factor (r/ℓ_ref)⁵ below. This is an algebraic
classification; its non-perturbative counterpart is input SRC-W (§6).

---

## 5. UV integration down to the reference level K

**5.1 The chain (lane definitions, re-derived where used).** RLARGE §0 "The exact chain":
W_ch(U_0,…,U_K) = e^{−S(U_0)} Π_{i<K} K_i(U_{i+1}, U_i), with ∫K_i dU_{i+1} = 1. Each k_c is the normalized soft kernel of PROOF
"Decision 4: the RG kernel": k_c ∝ exp((κu_i/N) Re tr(V_c⁻¹M̄_c(U_i))), normalized over V_c ∈ SU(N). The V-independent
part of RLARGE's φ_M cancels in the normalization, so k_c is smooth and strictly positive in (V, U_i); M̄_c is a
polynomial in the links (PROOF "Lemma D4-norm" (1): 𝒩 > 0 and C^∞).
- **Lemma 5.1 (PROVEN).** The U_0-marginal of W_ch/∫W_ch is the Wilson state ω, and ∫W_ch = Z_Wilson.
  *Proof.* Integrate U_K, then U_{K−1}, …, U_1, using ∫K_i dU_{i+1} = 1 at each step. ∎
  Write ν_K for the law of U_K (the **unknown coarse-field law**) and E_K[·] := E[·|U_K]. For a fine observable G,
  ω(G) = ν_K(E_K[G]).
- **Lemma 5.2 (law of total covariance; PROVEN, elementary).**
  Cov_ω(G, H) = ν_K(Cov(G, H | U_K)) + Cov_{ν_K}(E_K[G], E_K[H]).
- **Lemma 5.3 (kernel identity; PROVEN).** For every smooth v and smooth G(U_0):
  (i) E_K[Ξ_vG] = Cov(G, 𝔚(v) − Ξ_v log K_0 | U_K);  (ii) E_K[𝔚(v)] = E_K[Ξ_v log K_0];
  (iii) Cov_{ν_K}(E_K[G], E_K[𝔚(v)]) = −ν_K(Cov(G, Ξ_v log K_0 | U_K)).
  *Proof.* Fix U_1,…,U_K and apply Lemma 3.1 in U_0 with Φ = G e^{−S}K_0(U_1,U_0). This gives
  ∫Ξ_v(G)e^{−S}K_0 dU_0 = ∫G(𝔚(v) − Ξ_v log K_0)e^{−S}K_0 dU_0. Multiply by Π_{i≥1}K_i, integrate over U_1..U_{K−1},
  and divide by the U_K-density: this is E_K[Ξ_vG] = E_K[G(𝔚 − Ξ_v log K_0)]. G = 1 gives (ii), and (i) follows.
  Average (i) over ν_K, and compare with Prop. 3.2 split by Lemma 5.2:
  ν_K(Cov(G,𝔚|U_K)) − ν_K(Cov(G, Ξ_v log K_0|U_K)) = ω(Ξ_vG) = ν_K(Cov(G,𝔚|U_K)) + Cov_{ν_K}(E_KG, E_K𝔚).
  Subtracting gives (iii). ∎
  *Reading.* The coarse image of the fine Ward functional is exactly the conditional mean of the RG kernel's response
  to the field redefinition. The soft kernel's block averages are not rotation covariant; that is where rotation
  breaking sits "after UV integration".

**5.2 The quantities that appear after UV integration.**
- E_K[F_s]: the coarse image of the observable, a local functional of U_K.
- 𝒯^K_{μν}(x) := E_K[𝒯_{μν}(x)], and the **coarse angular-momentum flux**
  𝒥_r := E_K[𝔗_r] = Σ_x a⁴[(∇_μψ_r)(x)(Jx)^ν𝒯^K_{μν}(x) + Σ_{μ<ν}J_{νμ}(ψ_r(x+aμ̂) − ψ_r(x+aν̂))𝒯^K_{μν}(x)].
  It is an explicit sum, over the shell r − a ≤ |x| ≤ 2r + a, of local coarse functionals.
- **The IR term: TQ_ν(s; r) := Cov_{ν_K}(E_K[F_s], 𝒥_r).**

**5.3 What the identity buys: it turns a symmetry question about ν_K into a decay question.** Lemma 5.1 alone gives
the trivial representation d/ds ω(F_s) = ν_K(∂_s E_K[F_s]). That is the ν_K-mean of a local functional which is O(1)
pointwise when s_F ≳ ℓ_ref: rotating f relative to a fixed coarse configuration changes E_K[F] at O(1). Its vanishing is
a *symmetry* property of the unknown law, and no decay hypothesis gives it. The Ward identity (Cor. 3.4 + §4.3 +
Lemma 5.2) rewrites the same number as −TQ_ν(s; r) plus UV terms. That is a *covariance at distance r*, which a
*decorrelation* hypothesis can kill without any symmetry information on ν_K (§8). Lemma 5.3(iii) shows how the two faces
are glued: TQ_ν = ν_K(Cov(F_s, Ξ_{v_r}log K_0|U_K)) + Cov_{ν_K}(E_KF_s, E_K𝔅(v_r)). The first term is local near F up to
conditionally decaying tails.

---

## 6. Inputs (every one named; the result of §7 is CONDITIONAL on exactly these)

| Id | Statement used | Where (locating string, current line) | Lane status |
|---|---|---|---|
| I1 | **BFT-0…BFT-5** at every level k ≤ K, uniform in k and in the torus | REVIEW_S22.md "Statement (BFT)" (l.387) | OPEN (the layer-1 target). Used only through I4 and I5 |
| I2 | **RLF v3**, in particular (RLF-3′) per-history bounds with HIST-sum. Used as a *local probability* bound: P_ω(𝔥) = Z(𝔥)/Z_K ≤ Z(𝔥)/Z(∅), since Z(∅) ≤ Z_K | RLARGE.md "(RLF-3′) Unreturned large fields, per history" (l.213) | OPEN / CONDITIONAL on RLARGE §4.2 rows 10–10f; SU(2) scope on the HW route, (KS-N) needed for N ≥ 3 |
| I3 | **Flow (F_R) + (RLF-δ)**: the chain's own sequence; tuning keeps g_ref := g_K ≤ min(g_thr, γ_0) fixed as K → ∞ (so ℓ_ref is a fixed physical scale), with g_bare → 0 | RLARGE.md "Flow hypothesis (F_R)" (l.98); "(RLF-δ)_k [v2-F" (l.198) | (F_R) hypothesis; F-mono CONFIRMED-WITH-FIX per RLARGE |
| I4 | **CD (conditional decay)**: for G ∈ {F_s} and dist(x, supp G) ≥ ℓ_ref, |Cov(G, 𝒯_{μν}(x) | U_K)| ≤ C_G(U_K) e^{−m_c dist/ℓ_ref}, with ν_K(C_G) ≤ C Z_e², uniformly in a, R, s | not in the lane as stated. Nearest: PROOF "W1-loc (4D) [S9]: reduced" ((DF) + Dimock I Thm 27 [m]), N5, N2-exp (linearised, trivial background) | **NEW, OPEN** |
| I5 | **SRC (source-inserted RG)** for the finite list {e_a, e_a⊗e_a, t_ν, A_J, the densities of 𝔚, 𝒯}: SRC-E, SRC-O, SRC-W below | not in the lane; P1 §4 and P3 §5 list source estimates as missing | **NEW, OPEN** |
| I6 | Hypercubic torus, side R even in lattice units; Wilson RP (Osterwalder–Seiler [m]) for the OS2 side only | PROOF "S3 Wilson action"; RLARGE §0 "Tori [v2-E7]" | standard / [m] |

**SRC-E (local moments).** There is a state-independent Z_e(a) > 0 with
sup_{a,R}[ν_K(|E_K G|²) + ν_K(Var(G|U_K))]/Z_e^{2·deg G} < ∞ for G ∈ {O_a(f), O_a(f)O_a(g)}, f, g in a fixed bounded subset
of C_c^∞(B_{ρ_F}). The same holds with Z = 1 for local densities of 𝒯. (In an RG proof this would come from small-field
size bounds plus I2 read as the local probability bound shown in the table.)
**SRC-O (observable side).** |𝒞(s)| ≤ C_F Z_e² [g_bare² + (a/ℓ_ref)²𝔏(a)]: the H(4)-allowed finite mixings ϑ₁, ϑ₃, ϑ_{6′}
of §4.2 are O(g_bare²) (they vanish at tree level by (C) and are generated at the cutoff scale), and the remaining
content of t_ν and A_J is dimension ≥ 6 (resp. 7) with coefficient a².
**SRC-W (bulk insertion).** There is a symmetric, H(4)-covariant, gauge-invariant local lattice tensor 𝒯 (the identity's
own current, §4.3) such that for r_F + ℓ_ref ≤ r ≤ R/4:
  |Cov_ω(F_s, 𝔅(v_r))| ≤ C_F Z_e² (a/ℓ_ref)² 𝔏(a) (r/ℓ_ref)⁵.
Its algebraic basis is §4.1 (R2, P, Lemmas 4.1–4.2). Its analytic content is the statement that the dimension-6
insertion acts with coefficient a² in renormalized correlations. That includes contact regions, where R2 is needed, and
the conditional measure, where H(4)_y holds only up to a positive power of (distance/ℓ_ref).

*Honest scope of the inputs.* I1–I3 are the lane's own layer-1 targets. I4 and I5 are additional UV statements, absent
from the lane, of the kind OS0 needs anyway (P1 §1, P3 §1). None of I1–I6 contains information about ν_K at distances
≫ ℓ_ref. BFT-3's e^{−m_0 tree} and CD's e^{−m_c dist} are statements about the background construction and the
*conditional* measure. By Lemma 5.2 (P1 §4: "Conditional locality is not full correlation decay") neither bounds a
Cov_{ν_K} term.

---

## 7. The conditional theorem: everything except one term vanishes uniformly in the torus

**Theorem 7.1 (CONDITIONAL on I1–I6).** There is C_F < ∞, depending on f, g, ‖J‖, N, L and the input constants but not
on a, R, r, s, such that for every lattice spacing a, every torus side R, every r with r_F + ℓ_ref ≤ r ≤ R/4 and every
s ∈ [0, 2π]:

  |d/ds ω(F_s) + TQ_ν(s; r)| ≤ Z_e(a)² ε_UV(a, r),
  ε_UV(a, r) := C_F[ g_bare² + (a/ℓ_ref)² 𝔏(a)(r/ℓ_ref)⁵ + (r/ℓ_ref)⁴ e^{−m_c(r−ρ_F−1)/ℓ_ref} ].

*Proof.*
1. Cor. 3.4: d/ds ω(F_s) = Cov_ω(F_s, 𝔚(v_r)) − 𝒞(s).
2. §4.3, exact: 𝔚(v_r) = −𝔗_r + 𝔅(v_r).
3. Lemma 5.2 with E_K[𝔗_r] = 𝒥_r: Cov_ω(F_s, 𝔗_r) = ν_K(Cov(F_s, 𝔗_r | U_K)) + TQ_ν(s; r).
4. Hence, exactly: d/ds ω(F_s) + TQ_ν(s;r) = −ν_K(Cov(F_s, 𝔗_r|U_K)) + Cov_ω(F_s, 𝔅(v_r)) − 𝒞(s).
5. Conditional shell term. 𝔗_r = Σ_{x∈Sh} a⁴ Σ_{μν} c_{μν}(x)𝒯_{μν}(x), with |c_{μν}(x)| ≤ |∇ψ_r||Jx| + 2a‖J‖ sup|∇ψ_r| ≤
   ‖h′‖_∞(2r + 3a)‖J‖/r ≤ 3‖h′‖_∞‖J‖, which does not grow with r. The shell has Σ_{x∈Sh} a⁴ ≤ C r⁴, and every
   x ∈ Sh has dist(x, supp F_s) ≥ r − a − ρ_F ≥ ℓ_ref. By I4: |ν_K(Cov(F_s,𝔗_r|U_K))| ≤ C Z_e² r⁴e^{−m_c(r−ρ_F−1)/ℓ_ref}.
6. Cov_ω(F_s, 𝔅(v_r)) is bounded by SRC-W, and 𝒞(s) by SRC-O. ∎

ϑ₁ (§4.2) multiplies d/ds ω(F_s) itself. Under SRC-E that derivative is O(Z_e²), so ϑ₁ = O(g_bare²) is absorbed into the
g_bare² term. This is equivalent to the factor (1+ϑ₁) written in §1.

**Corollary 7.2 (the IR term is r-independent; CONDITIONAL).** For r, r′ ∈ [r_F + ℓ_ref, R/4]:
|TQ_ν(s;r) − TQ_ν(s;r′)| ≤ Z_e²[ε′(a,r) + ε′(a,r′)], where ε′ is ε_UV without the g_bare² term.
*Proof.* Cov_ω(F_s,𝔚(v_r)) = Cov_ω(F_s,𝔚(v_{r′})) exactly (Cor. 3.4), and 𝒞(s) is the same number for both. Subtract
the two instances of step 4 and bound the remaining terms as in steps 5–6. ∎

**Corollary 7.3 (diagonal limit; CONDITIONAL).** Let a_j → 0 and R_j → ∞ along a sequence on which I1–I6 hold. Put
r_j := min{R_j/4, ℓ_ref(ℓ_ref/a_j)^{1/3}}. Then (a_j/ℓ)²𝔏(r_j/ℓ)⁵ ≤ (a_j/ℓ)^{1/3}𝔏 → 0, r_j → ∞ and g_bare → 0, so
ε_UV(a_j, r_j) → 0. **Uniformly in the torus**, therefore:
- (a) sup_{s≤2π} |D_j(s) + Z_e(a_j)⁻²∫₀ˢ TQ_{ν_j}(s′; r_j)ds′| ≤ 2π ε_UV(a_j, r_j) → 0.
- (b) For each fixed r ≥ r_F + ℓ_ref: limsup_j sup_s |TQ_{ν_j}(s;r) − TQ_{ν_j}(s;r_j)|/Z_e² ≤ 2C_F r⁴e^{−m_c(r−ρ_F−1)}.
- (c) **Equivalence.** Along any subsequence whose renormalized two-point functions converge to a continuous limit S
  (H_reg/OS0), the following are equivalent: the limit is invariant on the rotation orbit of (f, g), i.e.
  S(f_s, g_s) = S(f, g) for all s; and
  **lim_{r→∞} limsup_j sup_s |TQ_{ν_j}(s; r)|/Z_e(a_j)² = 0.**
  (⇐) by (a)–(b). (⇒) d/ds S(f_s,g_s) = 0 forces limsup_j sup_s |d/ds ω_j(F_s)|/Z_e² = 0, then Theorem 7.1 at r_j gives
  TQ(r_j) → 0, and (b) gives the bound C r⁴e^{−m_c r} at fixed r.

**What 7.1–7.3 establish, and what they do not.** They establish the brief's items 1–3 *for every term but one*: the
normalized lattice and observable artefacts, all contact terms and the conditional part of the boundary term tend to
zero uniformly in the containing torus, from the listed inputs only. This is not a zero-background, fixed-torus or
formal-series statement: the identity holds for every configuration and every R, the conditional terms are bounded
under ν_K (large fields included through I2), and the only R-dependence is r ≤ R/4. It does **not** prove that the
defect tends to zero. That requires TQ_ν → 0, and (c) shows nothing weaker will do on this route.

---

## 8. The IR term, named exactly (R4-F1), and its strength

### 8.1 The term
**TQ_ν(s; r) = Cov_{ν_K}( E_K[O_a(f_s)O_a(g_s)] , Σ_{x∈Sh_r} a⁴ c_{μν}(x) E_K[𝒯_{μν}(x)] )**, with c_{μν} the explicit
shell weights of §4.3, |c| ≤ 3‖h′‖_∞‖J‖. It is the covariance, under the law ν_K of the reference-scale soft field,
between the conditional energy-density pair at the origin and the conditional angular-momentum flux through the
shell r ≤ |x| ≤ 2r. It has a fine-level twin TQ^fine(s;r) := Cov_ω(F_s, 𝔗_r) (P2's TORQUE, now an exact lattice
object). Lemma 5.2 and I4 give |TQ_ν − TQ^fine| ≤ C Z_e² r⁴e^{−m_c(r−ρ_F−1)}, so for large r the two are interchangeable.
- **It is the first term whose bound needs the coarse law.** Every other term of §7 is bounded using only SRC-E's
  *local* moments of ν_K, I2's local large-field probabilities, and conditional (given U_K) properties. For TQ_ν, local
  moments plus Cauchy–Schwarz give only |TQ_ν| ≤ C Z_e²(r/ℓ_ref)⁴, which grows with r. Smallness needs decorrelation
  of ν_K at distance r.
- **It cannot be avoided on this route.** By Cor. 7.2–7.3 it is asymptotically r-independent and equals −D′ up to the
  UV terms. It is the lattice form of the *rotation charge at infinity*: zero iff the selected limit has no spontaneous
  rotation breaking for this pair.

### 8.2 A sufficient condition weaker than every one proposed so far
**Proposition 8.1 (PROVEN, given hypothesis DEC and I1–I6).** Hypothesis DEC: along the sequence, for |x| ≥ r₀ and
uniformly in j and s,
  Σ_{μν}|Cov_{ν_j}(E_K F_s, E_K 𝒯_{μν}(x))| ≤ Z_e(a_j)² ε(|x|)|x|⁻⁴,  with (1/log(ρ₂/ρ₁))∫_{ρ₁}^{ρ₂} ε(ρ)dρ/ρ → 0
as ρ₂/ρ₁ → ∞ (ρ₁ ≥ r₀). Then the limit is rotation invariant on the orbit of (f, g).
*Proof.* 𝔗 is linear in the cutoff. So for λ(dρ) := dρ/(ρ log(r₂/r₁)) on [r₁, r₂], ∫TQ_ν(s;ρ)λ(dρ) is the TQ of
ψ̄ := ∫ψ_ρ λ(dρ). Since h′(t) ≠ 0 only for t ∈ [1,2], |∂ψ̄(y)| ≤ (‖h′‖_∞/log(r₂/r₁))∫_{|y|/2}^{|y|}ρ⁻²dρ =
‖h′‖_∞/(|y| log(r₂/r₁)). The shell weights of ψ̄ are therefore ≤ C‖J‖/log(r₂/r₁) on r₁ − a ≤ |x| ≤ 2r₂ + a, and
|∫TQ_ν dλ| ≤ (C Z_e²/log(r₂/r₁)) ∫_{r₁−1}^{2r₂+1} ε(ρ)dρ/ρ. By Cor. 7.2, |TQ_ν(s;r₁) − ∫TQ_ν dλ| ≤
C Z_e²[(a/ℓ)²𝔏 r₂⁵ + r₁⁴e^{−m_c(r₁−ρ_F−1)}]. Take r₂ = r_j (Cor. 7.3), let j → ∞, then r₁ → ∞, and apply Cor. 7.3(c). ∎
- P2's sufficient bound |x|^{−4−η} is the case ε = ρ^{−η}. The borderline ε = 1/log ρ also works:
  ∫dρ/(ρ log ρ) = log log ρ, and that is o(log(ρ₂/ρ₁)). ε ≡ const (pure |x|⁻⁴) fails. A Goldstone-type |x|⁻³ (ε ∝ ρ)
  fails, as it must: that is what a rotation charge at infinity looks like.
- DEC is needed only for |x| ≤ R_j/2 (inside the torus) and only for the *coarse* covariance.

### 8.3 Comparison with uniqueness and with a gap (the R4-F1 question)
- **Proposition 8.2 (mixtures; PROVEN).** Let ω = Σ_i p_i ω_i (or an integral) with each ω_i invariant under fine
  lattice translations and H(4). Then **TQ^fine_ω(s;r) = Σ_i p_i TQ^fine_{ω_i}(s;r) exactly.**
  *Proof.* ω_i(𝒯_{μν}(x)) is a constant H(4)-invariant symmetric 2-tensor, hence τ_iδ_{μν} (one invariant in Sym²V:
  `rd55_tens_out.txt`, k = 2). Then ω_i(𝔗_r) = τ_iΣ_x a⁴Σ_μ(∇_μψ_r)(x)(Jx)^μ; the off-diagonal part of 𝔗 does not see
  δ_{μν}. Summation by parts gives −τ_iΣ_x a⁴ψ_r(x)Σ_μ∇^*_μ(Jx)^μ = −τ_iΣ_x a⁴ψ_r(x) tr J = 0. So the between-component
  term Σp_i(ω_i(F) − ω(F))(ω_i(𝔗_r) − ω(𝔗_r)) vanishes. ∎
  **Consequence.** TQ → 0 holds for a mixture of components that each satisfy it, whatever their number. **TQ does not
  imply uniqueness or extremality.** (P1 §2's two-phase example is of this kind.)
- **Proposition 8.3 (gap ⇒ TQ; PROVEN, trivial).** Uniform exponential clustering |Cov_{ω_j}(F_s, 𝒯_{μν}(x))| ≤
  C Z_e²e^{−m|x|} gives |TQ^fine| ≤ C Z_e² r⁴e^{−mr}, hence TQ_ν → 0 by I4.
- **Remark 8.4 (strictly weaker than a gap, as a hypothesis; ARGUED, standard).** DEC allows ε(ρ) = ρ⁻⁴, i.e. |x|⁻⁸
  decay. That is the decay in the free massless (abelian) comparator: |⟨F_{μν}(x)F_{ρσ}(0)⟩| = O(|x|⁻⁴), and by Wick's
  theorem the connected correlation of a quadratic functional near 0 with the quadratic stress at x uses two propagators
  across, giving O(|x|⁻⁸). DEC holds there without a gap. This compares hypothesis classes; it says nothing about YM.
- **Remark 8.5 (uniqueness does not supply TQ; ARGUED).**
  (a) Thermodynamic uniqueness (one infinite-volume state per lattice spacing and orientation) carries no rate. Tail
  triviality bounds covariances with *bounded* tail functionals, but the flux functional has size of order (r/ℓ_ref)⁴, and
  TQ is a rate statement.
  (b) Given I1–I6, Cor. 7.3(c) turns any implication "uniqueness ⇒ TQ → 0" into "uniqueness ⇒ OS1 for the pair". P1 §2
  and P3 §2 (the exp(−Σ|x_μ|) Gaussian) show that uniqueness, H(4) and RP do not give O(4) without action information.
  Here the action information enters only through the UV terms already used.
  (c) Analogy [m, unverified literature]: the d = 3 plane rotator in a field h > 0 has a unique Gibbs state [m:
  Lee–Yang-type results for rotators]. As h ↓ 0 at low temperature it converges to a magnetized state [m: infrared-bound
  SSB]. Its O(2) Noether flux through a large sphere has O(1) covariance with the order parameter (Goldstone,
  |x|^{−(d−1)}). That is exactly a failure of TQ with uniqueness at every regulator value. The analogy's breaking (h) is
  relevant, while YM's lattice breaking is irrelevant (dimension 6). So it shows uniqueness gives no a-priori control;
  it is not a YM counterexample.
- **Verdict.** TQ is **not** uniqueness. It is logically independent of bare uniqueness: it does not imply it (8.2),
  and uniqueness does not give it (8.5). As a hypothesis it is strictly weaker than "uniqueness + clustering with rate
  o(|x|⁻⁴)" and strictly weaker than a gap (8.1, 8.3, 8.4). It is exactly the statement that the selected limit carries
  no rotation charge at infinity: absence of spontaneous rotation breaking, not uniqueness of the phase.

### 8.4 Scale separation: the coarse law can matter only at scales ≳ ℓ_ref (ARGUED; tensor facts CHECKED)
- **Fact (CHECKED, `checks/rd55_tens_out.txt`).** The numbers of H(4)-invariants in Sym^kV are 0, 1, 0, 2 for k = 1, 2, 3, 4,
  against O(4)'s 0, 1, 0, 1. **Every H(4)-invariant symmetric tensor of rank ≤ 3 is O(4)-invariant. The first cubic
  invariant is Σ_i x_i⁴, at rank 4.**
- **Use.** In the trivial face D′(s) = ν_K(∂_sE_K[F_s]), average over the fine translations of the pair within one
  coarse cell. This is exact: ω is invariant under fine translations. The cell average makes every ν_K-moment tensor
  H(4)-invariant (H(4) about a coarse site maps the coarse lattice to itself). Suppose the conditional pair kernel
  E_K[e_a(x)e_a(y)] has, for small-field U_K and |x − y|, |x − x₀| ≤ s_F ≪ ℓ_ref, an expansion in
  (x − x₀)/ℓ_ref, (y − x₀)/ℓ_ref whose orientation dependence is carried by H(4)-covariant tensors of U_K. Its leading
  short-distance part is O(4)-invariant, and its remainder is O((s_F/ℓ_ref)⁴). Call this input **SRC-iso**; it is a UV
  statement, since everything in it lives at scales ≤ ℓ_ref. Then the anisotropic part of D′ starts at rank 4:
  |D(s)| ≲ (s_F/ℓ_ref)⁴ + ε_UV, uniformly in R.
- **Reading.** On this route the unknown coarse law can affect OS1 for observables much finer than the reference scale
  only at relative order (s_F/ℓ_ref)⁴. The obstruction lives at observation scales ≳ ℓ_ref, where the coupling leaves the
  RG-controlled window. Status: ARGUED. SRC-iso is not in the lane and is not proved here. It is plausible in the
  linearised theory, where the constrained propagator differs from the free one by a kernel smooth at scale ℓ_ref.

*Clarification of §8.1's phrase "smallness needs decorrelation" (append-only).* It refers to **vanishing in the
limit**. For s_F ≪ ℓ_ref, §8.4 (ARGUED, CONDITIONAL on SRC-iso) gives smallness of order (s_F/ℓ_ref)⁴ from symmetry
and UV inputs alone, but never zero. Exact OS1 at every observation scale still needs TQ → 0.

---

## 9. Verdicts on the named failure modes, and what changes for the lane

- **R4-F1** (RTARGET §55 T56-R4: "every candidate route reduces to uniqueness … say exactly which estimate and whether
  it is weaker than a gap"). **For this route: does not occur as stated.** The route reduces *exactly* to TQ (§8.1), an
  infrared decorrelation estimate in the coarse stress channel (sufficient form: DEC, §8.2). Given I1–I6 it is
  equivalent to OS1 for the pair. It is weaker than a gap (8.3, 8.4) and logically independent of bare uniqueness
  (8.2, 8.5). **Not established:** the "any route" form of T56-R4. This file tests one route.
- **R4-F2: does not occur.** *RP:* the route never changes the state. Prop. 3.2 is an identity for the Wilson state ω;
  Lemmas 5.1–5.3 rewrite ω-expectations; e_a is strictly local, so positive-time smearings are positive-time lattice
  observables, and the limit inherits RP by the finite-quadratic-form argument (P1 §1, P3 §1). *Gauge invariance:* e_a,
  𝔚(v) (§3.2 (G)), 𝒯 and the kernel are gauge invariant or covariant. The kernel's covariance is from PROOF "Decision 4:
  the RG kernel": "K(g|_roots·V, g·U) = K(V, U)". So E_K of a gauge-invariant functional is gauge invariant. The rejected
  flowed-density variant (§2.2) would lose exact RP locality at fixed flow time; that is why it was not used.
- **For PROOF.md / HANDOFF (for the lead; no inherited item is REFUTED here).**
  1. **L9b (OS1) can be restated precisely** (PROOF "L9b. Euclidean invariance (OS1): OPEN"; also §0 item 3 and route γ1's
     "probably uniqueness").
     - *UV part:* SRC-W + SRC-O + CD. These are new layer-1 items, shared with OS0's source estimates. R1, R2, P and
       Lemmas 4.1–4.2 already show that no O(1) or power-divergent rotation counterterm exists for an H(4)-scalar
       observable.
     - *IR part:* TQ, a named OPEN infrared input. It is neither "uniqueness" nor "a gap".
  2. SRC-W is (ARGUED) the infinitesimal, interior form of UNIV55's "rotated-lattice universality in bounded regions"
     (PLAN_S26 §10). The two targets should share one UV statement.
  3. **Rates.** The observable-side mixing is O(g_bare²) ∼ 1/log(ℓ_ref/a). On this route any quantitative OS1 rate is at
     best logarithmic in a, so P1 §3's sufficient form C a^η + b(R) is not available. P1 itself notes that a power rate is
     not logically required, and Cor. 7.3 does not need one.
  4. Wording: P2 §7.2's "TORQUE is narrower than full uniqueness" should read "does not require uniqueness and is not
     implied by it" (§8.5).

---

## 10. Agreement and disagreement with the panel (explicit, as required)

- **P1 §3 (H_Euc, assembly).** Agree. This file gives the decomposition only for the UV part, with a logarithmic rather
  than power rate (g_bare²). The b(R)-type piece is TQ, which UV inputs do not send to zero.
- **P1 §3 "Why irrelevant coefficients alone do not finish OS1".** Confirmed and sharpened. The volume integral of the
  breaking can be truncated at radius r(a), since a²r⁵ → 0 by choosing r(a). The price is the flux term, and that term
  is exactly as hard as the defect (Cor. 7.3(c)).
- **P1 §8 "least sure of"** (whether the soft RG can control the normalized remainder "without needing information about
  phase selection"): answered for this route. The remainder splits into a UV part (controlled under I1–I6) and TQ.
  TQ needs large-distance information, but not phase selection (8.2).
- **P2 §7.2 (W) + TORQUE.** Agree with the structure. Added here:
  - the lattice derivation that P2 marked "not yet a lattice derivation";
  - the conditional/coarse split, which places TORQUE's IR content in Cov_{ν_K};
  - exact r-independence, which makes TORQUE necessary as well as sufficient (given the UV inputs);
  - a weaker sufficient decay (log-Cesàro o(|x|⁻⁴) instead of |x|^{−4−η});
  - the H(4) selection rule R2, which removes every O(1) contact counterterm.
  Disagree with the wording "narrower than full uniqueness" (§9 item 4).
- **P3 §6** ("smallest discriminating next artifact") was done as specified. The outcome is the failure mode the
  brief names (first coarse-law term isolated), not a proof.
  - P3's "least certain" question was whether the boundary/coarse-field terms can be controlled by purely local UV
    estimates. Answer: they cannot; given the UV inputs the coarse boundary term is equivalent to the defect.
  - It does force a genuine large-distance input, weaker than a gap. Whether that input is "as difficult as a mass-gap
    analysis" is not decided here.
- **P1 §2 / P3 §2 counterexamples** (two-phase constant field; exp(−Σ|x_μ|) Gaussian) are used in 8.5(b) as stated in
  those files, labelled PROVEN there. I did not re-derive them in this file.

*Supplement to §4.3 and SRC-W (append-only): higher derivatives of the cutoff.* Expanding v(m_b) about each site
writes 𝔚(v) = Σ_k Σ_x a⁴(∂^kv)·ω^{(k)}(x). Here ∂^kv has rank k+1 and dimension k−1 (v has dimension −1), so ω^{(k)} has
canonical dimension 5−k. Its continuum content is operators of dimension δ ≥ 5−k with coefficient a^{δ−(5−k)}.
Inversion parity P forces δ ≡ k+1 (mod 2).
- k = 0 (rank 1): δ = 5, coefficient a⁰. These are total derivatives (Lemma 4.1) and are moved to the shell. δ = 7
  carries a².
- k = 1 (rank 2): δ = 4, coefficient a⁰. This is the current; in the bulk only its antisymmetric part is seen, and that
  is zero by R2. δ = 6 carries a².
- k = 2 (rank 3): δ = 3 does not exist, so δ = 5 with a².
- k = 3 (rank 4): δ = 4 with a².

On the shell ∂^kv = O(r^{1−k}), so every k ≥ 2 shell term is O(a²r^{4−k}·r) ≤ O(a²r³). With 𝒯 the identity's own
current, these terms are inside SRC-W's a²r⁵ bound. If 𝒯 differs from that current at dimension 4 (wrong H(4)-split
normalizations), 𝔅 acquires an O(1) shell torque of the difference, and SRC-W fails as stated. That is why SRC-W names
𝒯 as the identity's own current. No O(a) term survives anywhere, by parity.

---

## 11. Summary table of every claim in this file

| # | Claim | Where | Label |
|---|---|---|---|
| 1 | ω(ΞF) = Cov_ω(F, 𝔚), ω(𝔚) = 0 (finite torus, any smooth Ξ) | §3.1 | PROVEN |
| 2 | Ξ_v properties (Lin), (G), (Loc) | §3.2 | PROVEN |
| 2′ | (H)/(T) covariance | §3.2 | checked by inspection (used only for the selection rules) |
| 2″ | (C) classical consistency | §3.2 | standard, not re-derived |
| 3 | Locality; exact r-independence of Cov(F_s, 𝔚(v_r)) | Lemma 3.3, Cor. 3.4 | PROVEN |
| 4 | R1: one H(4)-invariant (and one det-twisted) dimension-4 operator | §4.1 | CHECKED (rd55_rep C4) |
| 5 | **R2: m(A in S²A) = 0**, no dimension-4 operator carries a rotation generator | §4.1 | CHECKED (C5; control C6 fired) |
| 6 | Inversion parity P: A-valued operators have even dimension, V-valued odd | §4.1 | PROVEN |
| 7 | Dimension-5 true vectors are divergences of symmetric tensors | Lemma 4.1 | PROVEN |
| 8 | Dimension-4 tensors have no antisymmetric part | Lemma 4.2 | PROVEN (from R2) |
| 9 | A non-O(4) dimension-6 H(4)-invariant exists | C7 | CHECKED |
| 10 | Exact form of the source terms 𝒞(s); the complete list (a)–(d) | §4.2 | PROVEN (algebra); sizes CONDITIONAL (SRC-O) |
| 11 | 𝔚 = −𝔗 + 𝔅 exactly; 𝔗 supported on the shell | §4.3 | PROVEN |
| 11′ | Breaking insertion has dimension 6, coefficient a²; no O(a) or O(1) bulk term | §4.3 + supplement | classification PROVEN/CHECKED; analytic size CONDITIONAL (SRC-W) |
| 12 | Fine marginal of the chain = Wilson | Lemma 5.1 | PROVEN |
| 13 | Law of total covariance | Lemma 5.2 | PROVEN |
| 14 | Kernel identity E_K[𝔚] = E_K[Ξ log K_0] and (iii) | Lemma 5.3 | PROVEN |
| 15 | UV part → 0 uniformly in R; TQ the only remainder | Thm 7.1 | CONDITIONAL (I1–I6) |
| 16 | TQ r-independent up to UV terms | Cor. 7.2 | CONDITIONAL |
| 17 | OS1 for the pair ⟺ TQ → 0 | Cor. 7.3 | CONDITIONAL |
| 18 | TQ is the first coarse-law term; local moments give only O(r⁴) | §8.1 | PROVEN (given SRC-E) |
| 19 | DEC (log-Cesàro o(\|x\|⁻⁴)) ⇒ OS1 for the pair | Prop. 8.1 | PROVEN given DEC + I1–I6 |
| 20 | TQ^fine exactly additive over translation/H(4)-invariant mixtures | Prop. 8.2 | PROVEN |
| 21 | Uniform exponential clustering ⇒ TQ → 0 | Prop. 8.3 | PROVEN (trivial) |
| 22 | TQ strictly weaker than a gap, as a hypothesis | Rem. 8.4 | ARGUED (standard comparator) |
| 23 | Uniqueness does not supply TQ | Rem. 8.5 | ARGUED ([m] analogy) |
| 24 | Rank ≤ 3 H(4)-invariants are O(4)-invariant; first cubic invariant at rank 4 | §8.4 | CHECKED (rd55_tens) |
| 24′ | Coarse-law effect on the defect is O((s_F/ℓ_ref)⁴) for s_F ≪ ℓ_ref | §8.4 | ARGUED (CONDITIONAL on SRC-iso) |
| 25 | Normalizing by Var(O_a(f)) would be vacuous (∼a⁻⁴ divergence) | §2.2 | ARGUED (short-distance power counting) |
| 26 | R4-F1 does not occur for this route; R4-F2 does not occur | §9 | as argued there |
| 27 | CD and SRC (E/O/W/iso) are new, OPEN UV inputs not in the lane | §6 | OPEN |
| 28 | SRC-W is the infinitesimal interior form of UNIV55's target | §9 | ARGUED |

Counts: PROVEN 18 (incl. 2, 3, 6–8, 10–14, 18–21 and the algebraic halves), CHECKED 4 (4, 5, 9, 24), CONDITIONAL 3
theorem-level (15–17), ARGUED 6 (2″, 22, 23, 24′, 25, 28), OPEN 1 (27). No inherited lane claim is REFUTED here.

## 12. For the Codex reviewer: the load-bearing steps, in the order to check them

1. Prop. 3.2 and Lemma 3.3. These need Haar bi-invariance, smoothness of Ξ_v, and (Lin): ξ_b reads v only at m_b.
2. §4.3's exact discrete Leibniz rule and the μ<ν rewriting, which put 𝔗_r on the shell. Then the supplement's
   parity bookkeeping for k ≥ 2.
3. `checks/rd55_rep.py`: the character formulas (Λ², S² of A), and that control C6 can fail. It returned
   m(A in Λ²A) = 1, so it fired as designed.
4. Lemma 4.1: the Bianchi computation (iii) = ¼∂_ν tr F² and the enumeration of δ- and d-contractions.
5. Lemma 5.3: integration by parts with the soft kernel K_0, which is smooth and positive in U_0. The V-independent part
   of φ_M cancels in k_c's normalization.
6. Theorem 7.1 step 5 (shell weights bounded independently of r; distance to the shell) and Cor. 7.3's choice of r_j.
7. Prop. 8.1: |∂ψ̄| ≤ ‖h′‖_∞/(|y| log(r₂/r₁)), from h′ supported in [1, 2].
8. Prop. 8.2: exact vanishing of ω_i(𝔗_r) by summation by parts with tr J = 0.

**Where I expect the strongest objections.**
- SRC-W asserts the a²r⁵ bound *including* the contact regions inside the conditional measure. There the H(4)_y
  symmetry needed by R2 holds only up to powers of (distance/ℓ_ref).
- CD is assumed uniformly in U_K, with large fields handled only through I2.
- The O(g_bare²) size of the ϑ's rests on tree-level vanishing via (C) plus power counting. It is not proved here.
- §8.4 is labelled ARGUED for these reasons.

---

## 13. Errata from my own re-read (append-only; each item overrides the earlier text it names)

- **E1 (§1 "Terms (i)" and §2.1 table row "ϑ₁, ϑ_Δ").** H(4) allows **three** O(1) observable-side coefficients, ϑ₁
  (rescaling of the geometric derivative) and ϑ₃, ϑ_{6′} (two total-derivative stress structures), as listed in §4.2.
  "two structures … ϑ_Δ" was loose wording.
- **E2 (§1 "CONDITIONAL theorem").** The admissible range is r_F + ℓ_ref ≤ r ≤ R/4 and the exponent is
  e^{−m_c(r−ρ_F−1)/ℓ_ref}, as in Theorem 7.1. §7 governs.
- **E3 (§2.2, justification item 2).** "R1 (§4.2 …)" should read "R1 (§4.1 …)".
- **E4 (centering; substantive).** Throughout §3–§8, read F_s as the **centered product**
  F̃_s := (O_a(f_s) − ω(O_a(f_s)))·(O_a(g_s) − ω(O_a(g_s))). TQ_ν is accordingly Cov_{ν_K}(E_K[F̃_s], 𝒥_r), and SRC-E's
  moments are for centered observables.
  - *Why it matters.* With the uncentered F_s = F̃_s + c_fO_a(g_s) + c_gO_a(f_s) − c_fc_g and c_f = c_a∫f = O(a⁻⁴), the
    identity holds, but its single-observable pieces enter multiplied by c_f. For one O_a(g) the exact identity gives
    Cov_ω(O_a(g_s), 𝔚(v_r)) = d/ds ω(O_a(g_s)) + 𝒞₁(s) = O(a^{M−4}): ω(t_ν) = ω(A_J) = 0 exactly, and Σa⁴r_g = O(a^M). So
    their *sum* is negligible. Their *pieces* (shell, bulk, conditional) need not each be O(a⁴).
  - *What the fix does.* With F̃_s the exact statements are unchanged: Ξ annihilates the constants, dep is unchanged,
    and ω(F̃_s) differs from ω(F_s) by c_{f_s}c_{g_s}. Since c_{f_s} = c_a∫f + O(a^M), D(s) changes by O(a^{M−8})
    (erratum to §2.2). The term-by-term bounds of §7 are then meaningful.
- **E5 (Cor. 3.4 wording).** 𝒞(s) is r-independent because, by (Lin), Ξ_{v_r}F_s is literally the same function for every
  r ≥ r_F: v_r = Jx at all midpoints of dep(F_s). It does not follow from Lemma 3.3(ii). Also r ≤ R/4 − a is needed
  for supp v_r (radius 2r + a) to sit inside one fundamental domain.
- **E6 (Cor. 7.3(c), direction ⇒).** The step "d/ds S(f_s,g_s) = 0 forces limsup_j sup_s|d/ds ω_j(F̃_s)|/Z_e² = 0"
  needs convergence of the renormalized two-point functions uniformly on the compact family
  {(f_s,g_s), (Jf_s,g_s), (f_s,Jg_s) : s ∈ [0,2π]}. The hypothesis of (c) is to be read that way.
- **E7 (§11 counts).** Correct tally of the 30 table rows:
  - PROVEN: 16 rows (1, 2, 3, 6, 7, 8, 10, 11, 11′ classification part, 12, 13, 14, 18, 19, 20, 21).
  - CHECKED: 4 rows (4, 5, 9, 24).
  - CONDITIONAL at theorem level: 3 rows (15, 16, 17), plus the size halves of 10 and 11′.
  - ARGUED: 6 rows (2″, 22, 23, 24′, 25, 28), plus 2′ checked by inspection.
  - OPEN: 1 row (27).
  - Row 26 is the verdict row.
  - REFUTED: none.

## 14. Closing statement (2026-10-28, after all derivations above)

**First coarse-law term.** For one renormalized local observable (the clover energy density, two separated smooth
tests), the lattice rotation identity after UV integration to the reference level has exactly one term whose bound
needs the unknown coarse-field law:
**TQ_ν = Cov_{ν_K}(E_K[F̃_s], 𝒥_r)**, the coarse covariance of the observable with the conditional angular-momentum
flux through a far shell.

**The other terms.** Under BFT-0..5, RLF v3, (F_R)/(RLF-δ), and the two new UV inputs CD and SRC, every other term
tends to zero uniformly in the torus. These are the source terms (O(g_bare²) + O(a²)), the dimension-6 breaking
insertion (O(a²r⁵)), all contact terms (by the exactly checked H(4) selection rule m(A in S²A) = 0), and the
conditional shell term (O(r⁴e^{−m_c r})).

**Equivalence.** Given those inputs, TQ_ν → 0 is necessary and sufficient for OS1 of the pair.

**What TQ_ν is.** It is the absence of a rotation charge at infinity. It is implied by an o(|x|⁻⁴) (log-Cesàro)
decay of the coarse stress-channel covariance, which is weaker than any gap. It is closed under mixtures, so it does
not imply uniqueness, and uniqueness does not supply it.

**Failure modes.** R4-F1 in its literal form does not occur; R4-F2 does not occur. The target "prove the normalized
defect tends to zero uniformly in the torus" is **not** achieved.

- **E8 (E7's row count).** The §11 table has **32** rows, not 30: 1–28 plus 2′, 2″, 11′, 24′. The tally in E7 sums to
  32: 16 + 4 + 3 + 6 + 1 (inspection) + 1 (OPEN) + 1 (verdict row 26).
- **E9 (provenance of external inputs).** No Codex review file was read or used for this deliverable. P1, P2 and P3 were
  read on disk as they stood at the time of writing (P2 only §7.2 and §§231–309 by grep). Their PROVEN labels are
  cited, not re-verified, except where this file re-derives a step.
- **E10 (wording of E9).** "§§231–309" means grep hits at lines 231–309 of PANEL_P2.md, not section numbers. I read P2 lines 180–207 (§7.2) in full.
