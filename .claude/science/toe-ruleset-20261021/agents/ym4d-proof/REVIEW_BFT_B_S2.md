# REVIEW_BFT_B_S2: hostile review of BFT lane B session 2 (BFT_B.md §0-§4 [RBB1-fix] edits, §5-§7; check bb2)

Reviewer: an independent agent. I wrote none of BFT_B.md, BFT_A.md, FLOW.md, SF.md or the ledger. This is the only file I
edited. No commits, PRs or pushes.

Inputs (read 2026-10-28 ≈06:00-06:10 UTC, after BFT_B.md's last write at 05:58:03 UTC):
- BFT_B.md: §0-§1 (l.1-143) in full; every [RBB1-fix] tag (44 occurrences, 41 of them in l.1-643) in context; §5-§7 and
  session-2 FOR OTHER FILES (l.644-963) in full. BFT_B_LOG.md in full.
- REVIEW_BFT_B_S1.md: bottom line, overclaims, tally, the 11 binding fixes, strategic verdict, re-run record.
- checks/bb2_criteria.md, checks/bb2_symbol.py (line by line), checks/bb2.out, checks/bb2.out.time; `TZ=UTC stat` of all of
  them and of BFT_B.md.
- BFT_A.md: BA-9, BA-10, Theorem BA (l.75-92); §6 [RBA1-fix] window and F3/F4 gaps (l.385-436); §10 outcome and FOR OTHER
  FILES (l.757-793); BFT_A_LOG tail. There is no REVIEW_BFT_A_S2.md.
- FLOW.md: §4 (SF-∞) (l.231-232), §5.2 Lemma F-tree statement and proof (l.251-267), (L-loc)/(L-loc2) (l.2326-2341).
- PROOF.md: L4a-Π (l.1181-1225), block-kernel conventions (l.5248-5253), Theorem RW and RW-triv (l.5346-5400), Theorem
  N5-sf0 (l.5401-5480), Lemma U0 (l.5608-5622), Lemma N5-an♭ and Lemma BR1 (l.5648-5705).
- REVIEW_S22.md Part 5 (BFT statement, l.395-437). SF.md (L-loc)_k (l.180-185, l.846-852). ym4d-existence/EXISTENCE.md
  (CE-loc) (l.4330-4350).

Re-run: bb2 under the numeric lock. The record is at the end of this file.

---

## Bottom line

- **RBB1 fixes: all 11 APPLIED and CORRECT.** The log says 41 tags; I count 41 in §0-§4 (plus 3 references in §6-§7). One
  cosmetic residual: the pre-stated §1.2 (l.77, l.79) still has the old "≥ Lμ_1/n − o(1)" / "Lμ_1/4 − O(1/L)·μ_1" phrasing
  without a pointer to the B1-2 replacement at l.224-226.
- **Provenance: CONSISTENT with the log, partly verifiable.**
  - The bb2 order (criteria 05:50:12 < script 05:50:30 < output 05:51:32-34) is verified by stat.
  - The order of §5 before §6 inside one file cannot be checked by stat: the Edit tool resets APFS birth time, and the file
    is now born = modified 05:58:03. The log's sizes agree within 4 bytes with the reconstructed sizes (§0-§4: 69328 logged
    vs 69337 now; up to the end of §5: 76562 logged vs 76566 now). The title-line change "session 1" → "sessions 1-2"
    (+3 bytes) is disclosed and accounts for almost all of the difference.
  - I checked the two post-proof corrections against the pre-stated text:
    - §5.1 still says m' < m (l.668), and §6.1 marks the correction to m' < m/(n − 1) (l.756-757).
    - §5.2's thresholds (l.701) are exactly the 𝔠_s := s̄𝔠_♮p_Π instances, and §6.5 marks the max(·, 𝔠_∞) change
      (l.862-863).
  - The 05:57 in-place edit of §6.4 is logged but not marked in the file (minor).
- **Lemma BB-W: CONFIRMED.** I re-derived every step:
  - K_1 = 0;
  - n = 2 via L4a-Π;
  - parity under total inversion about a link midpoint;
  - the order-by-order Ward identity (★) with its induction;
  - the algebraic lemma (A1);
  - Schwarz.

  The dimension count is right. Only tr F² survives at dimension 4 (B_4-invariant, gauge-invariant). The cubic and quartic
  dimension-4 parts are slaved to β by the Ward identity, and every odd dimension is removed by inversion.
- **Lemma BB-sm: CONFIRMED.** I re-derived the constants. The ℓ^{-2} comes from the vanishing moments (orders 2-5) and from
  ℓ⁴·ℓ^{-6} (orders ≥ 6).
- **Theorem BB-4♮: CONFIRMED as an implication, with two binding fixes:**
  - the domain ρ := ε_0 is not inside the BFT-2 ball;
  - the "right form of BFT-4" sentence overclaims.

  The F-tree extension to level-varying κ_j is **CORRECT**. I read the proof: κ_k enters only through κ_k^{-1}P_⊥, which
  is bounded and killed by |ŝ|² → 0.

  **It inherits lane A's (α, θ) window problem, but only through its hypotheses (I1) and (I2).** Its own steps are
  pair-agnostic (Part B.3).
- **BB-mix-wall: CONFIRMED as ARGUED, with one narrowing fix.** "Switching one cube's pinning is an O(1) change" (l.823) is
  wrong in absolute terms: the switch is O(r(ε)). The fix also bears on the strategic reading.
- **Theorem BB-mix′_1: CONFIRMED-WITH-FIX (k = 1).**
  - I checked every step:
    - the cube-weighted walk operator and the splitting (S1). The columns of every piece lie in one box □ ⊂ Q(□), and the
      rows lie within R + 1 blocks of □;
    - the weighted contraction;
    - A(1) = A*;
    - the class splitting of A(s) and ΔE(s);
    - the interpolation identity;
    - gauge invariance and support;
    - the Cauchy and lattice-animal counts.
  - Fixes:
    - a factor 4 in N_0(|P|) (constant only);
    - the complex domain;
    - the density-analyticity constant c_ρ, which is a routine but unwritten extension of N5-an♭ (verified: N5-an♭
      covers gradient and Hessian entries, not single densities).
  - **With these fixes this is BFT-4's polymer bound at k = 1: the first polymer-form instance of BFT-4.**
- **BB-mix-k: CONFIRMED as a named wall, but not precisely stated** (fix BMk-1). **(H-RW^∇)_k is not the same object as SF's
  (L-loc)_k, FLOW's (L-loc) or existence's (CE-loc).** It is the composite-route analogue of Theorem RW (iv), the
  s-weakened walk expansion, which all three use or presuppose in per-level form. Its output via BB-bond_k is BFT-4's
  polymer form, which is SF's (L-loc)_k for the branch part. Part E has the precise map.
- **bb2: PASS, re-run byte-identical.** The information it adds is modest: it is F-tree at k = 1, n = 2 in bb1's abelian
  fibre model.
- **One ledger-level flag (not lane B's fault): BR1 (v)'s complex radius α_*/8 is not supported by its proof.** That radius
  is used by BB-3_1, BB-loc and BB-mix′_1 (Part D.4).

---

# PART A: Step 1, the [RBB1-fix] edits (l.1-643)

| fix | where | verdict |
|---|---|---|
| B1-1 μ_1 = m_1/2 ≈ 2.4·10⁻¹¹, Lμ_1 ≈ 7.2·10⁻¹¹ | l.258-261; l.584 table; l.568-570; l.409-414 (M_c redone ≈ 10¹³) | CORRECT (9.66e-11/4 = 2.415e-11; ×3 = 7.25e-11). Old values remain at l.255, l.408 and l.567, each immediately followed by its fix. OK |
| B1-2 unit conversion | l.224-226 | CORRECT (each of the n tree edges loses ≤ 2dL level-0 units). **Residual R-1:** the pre-stated l.77/l.79 still carry "− o(1)" / "− O(1/L)μ_1" unmarked; add "[see l.224]" |
| B1-3 chart vs left-trivialised derivative | l.26-28, l.221 | CORRECT (dexp^{±1} factor (1 + O(ϱ))^n; "analytic continuation from the totally real set") |
| B1-4 closed domain | l.230 | CORRECT |
| BB-geo star = spanning tree | l.33-35 | CORRECT |
| scope (tori T ≥ T_0 only) | l.226-227 | CORRECT |
| B-NL-1 | l.66-68, l.190-191, l.583 | CORRECT |
| B3k-1 half radius | l.287-288 | CORRECT |
| B3k-2/3 (Gronwall for all sub-chains; gauge compatibility; per-level alternative) | l.309-320 | CORRECT |
| B4-1/B4-2 ((H-𝔊_w) = lane A's (H-lin^∇)_m + (H-rem^∇)_m; (LEG_w) = data-map row) | l.87-94, l.288-291, l.318-320 | CORRECT |
| B3F1-1 | l.326-329 | CORRECT |
| B3F2-1 (NOT ESTABLISHED; "⊂ BFT-4" withdrawn) | l.105-108, l.339-350, l.357-358, l.588-589, l.636-638 | CORRECT. Every "⊂ BFT-4" occurrence (l.357, l.633) is followed by its withdrawal |
| B-loc-1 (RW on Ω_□ ∩ Λ_Y) | l.368-371 | CORRECT. CT♯ applies to the compressions, and the multiplicity count is inherited |
| B-loc-2 (general-k clause withdrawn; E_∅ = L^{2k}S_W) | l.117-119, l.390-394 | CORRECT |
| B-mix-1/2/3 | l.122-127, l.409-414, l.415-418 | CORRECT. K ≈ Ce^{-μM_c/2^d} and the M_c estimate are redone; BB-mix-gap (2) is relabelled a route NO-GO (ARGUED) |
| B4i-1/2/3 | l.474-484 | CORRECT |
| B4c-1/2 | l.502-512 | CORRECT (81² factor; AX-Taylor for |X| ≲ r_ℂε_0/ε, plain Cauchy beyond) |
| B-bb1-1/2 | l.555-557, l.568-570 | CORRECT |
| FOR OTHER FILES corrections | l.611-618, l.636-639 | CORRECT |

Verdict: **all 11 binding fixes applied correctly.** The only residual is R-1, which is cosmetic.

# PART B: §5.1 / §6.1-§6.3 (marginal-extracted BFT-4)

## B.1 Lemma BB-W (pre-stated l.664-669; proof l.715-762): CONFIRMED

Checked step by step.

- **Analyticity (l.716-718).** If |Im p_i|_∞ ≤ η, then |Im(p_i·Δ_i)| ≤ η|Δ_i|_1. Since Σ_i|Δ_i| ≤ (n − 1)max_i|Δ_i|, Ṽ_n is
  bounded by M_n^{(m)} on |Im p|_∞ < m/(n − 1). The pre-stated range m' < m (l.668) was wrong for n ≥ 3. The correction to
  m' < m/(n − 1) is right and marked (l.756-757).
- **Step 0.** ∇F(0) is Ad-invariant, and su(N) has no non-zero Ad-invariant vector. Correct.
- **Step 1 (n = 2).**
  - L4a-Π's hypotheses (S), (H) and (G) hold.
  - The colour-scalar form holds because the adjoint of su(N) is absolutely irreducible, so the commutant is the scalars.
    This gives exactly the Ad-equivariance argument stated.
  - L4a-Π derives the evenness of Π̃ from the total reflection alone; reality is not needed for the vanishing of odd orders.
    So a complex-valued F is harmless.
  - The O(p⁴) claim is exactly L4a-Π. Its order-2 analysis also shows that β(δ|p|² − pp^T) is the only B_4-covariant
    transverse quadratic tensor; I re-did it (a δp² + b pp + c δ_{μν}p_μ²: transversality forces c = 0 and a = −b).
- **Step 2 (parity).**
  - x ↦ 2c − x with c a link midpoint is −1 ∈ B_4 composed with the integer translation 2c. It maps the positively oriented
    link with midpoint m to the one with midpoint 2c − m, and B ↦ −B exactly, since log V^{-1} = −log V.
  - K_n(b_1, …) = (−1)^nK_n(Ib_1, …) and Ib_1 = b_1, so μ_α = (−1)^{n+|α|}μ_α. Correct.
- **Step 3 (Ward identity).** The B^{n−1}λ coefficient of Σ_b∂F/∂B_b·δ_λB_b = 0 collects:
  - m = n with r = 0, where δ^{(0)} = −dλ;
  - 2 ≤ m ≤ n − 1 with r = n − m ≥ 1. m = 1 drops out because K_1 = 0.

  δ^{(r)}_b is local to the link b, so in Fourier variables the m-terms are Ṽ_m with one momentum replaced by a sum of
  momenta, times an analytic multiplier. Their Taylor degree is ≥ 6 − m ≥ 7 − n under the induction hypothesis, so for
  J ≤ 6 − n the degree-J part of (★) is the pure transversality relation. I checked the bookkeeping case by case:
  - n = 3: the m = 2 term is O(p⁴), and 4 ≥ 7 − 3. J = 1 kills Ṽ_3^{[0]} (dim 3); J = 2 with (A1) kills Ṽ_3^{[1]} (dim 4);
    parity kills Ṽ_3^{[2]} (dim 5).
  - n = 4: the m-terms are O(p³), and 3 ≥ 3. J = 1 kills Ṽ_4^{[0]} (dim 4). Ṽ_4^{[1]} (dim 5) is killed by (A1) and also by
    parity.
  - n = 5: Ṽ_5^{[0]} (dim 5) is killed by J = 1 and by parity.

  The general-β reading also holds: with β ≠ 0, the m = 2 term contributes at degree 2 for n = 3 and gives the cubic F²
  vertex. This is the expected "slaving".
- **(A1).** I re-proved it.
  - The coefficient of p_{i,α}p_{i,β} forces Y_i to be antisymmetric in (α, ν_1).
  - For i ≠ i', the coefficient of p_{i,α}p_{i',β} forces Y_i = Y_{i'}.
  - Then V = −p_{1,α}Y^{α…}. With p_2 = 0 (allowed for n ≥ 3, with p_3 = −p_1 − Σ_{i>3}p_i), V = 0 for every p_1, so Y = 0.
  - The colour indices are spectators. Correct.
- **Bound (l.755-757).** On the disc |ζ| < m/(n − 1) the function vanishes to order 6 − n, and Schwarz gives the stated bound
  for any m' ≤ m/(n − 1). Correct.
- **Reading (l.759-762).** "tr F² is the only dimension-4 invariant (θ-term P-odd)". Correct as a lattice statement under
  B_4 and gauge invariance.

**Non-binding remark BW-r1.** (SF-∞)_B is dispensable. The Ward identity and the inversion argument hold exactly on the
torus. With minimal-image moments, the conclusions become "the dimension-≤5 moments are ≤ C e^{-mT/2}", and BB-sm acquires
an additive O(ℓ⁴e^{-mT/2}). If the lane prefers the infinite-volume statement, (SF-∞)_B is plausibly a consequence of a
walk-type localisation such as (H-RW^∇)_k (Part E).

## B.2 Lemma BB-sm (l.671-673; proof l.764-780): CONFIRMED

- N_s ≤ 4(2ℓR_A + 2)⁴ ≤ 1024R_A⁴ℓ⁴ for ℓR_A ≥ 1, and ||f||_D ≤ a/ℓ ≤ ρ/2.
- The vanishing moments are needed per (direction, colour) component; they are, because Ṽ_n is a tensor.
- Multivariate Taylor with the remainder (Σ|Δ_i|_1)^{6−n}/(6 − n)!·max|∂^αg| is right, because each y_i sits in a single
  factor.
- x^je^{−mx} ≤ (j/(em))^j. Σ_{b_1}|f(b_1)| ≤ N_sa/ℓ. Total: ℓ^{4−1−5} = ℓ^{−2}, with c_n as stated.
- Orders ≥ 6: F(wf) has the line-integral bound G_∇ρN_s on |w| = W, Cauchy gives the coefficients, Σ_{n≥6} ≤ 2W^{−6}, and
  2·1024 = 2048.
- C_sm = R_A⁴·max{…}, with Σx_iy_i ≤ max x·Σy. Correct.

Note: ρ ≈ ε_0 is tiny, so "a ≤ ρℓ/2" means ℓ ≥ 2a/ε_0. That is fine asymptotically, but C_sm ∝ ρ^{−5} in its n ≥ 6 part.
(Not a defect.)

## B.3 Theorem BB-4♮ (l.674-685; proof l.782-820): CONFIRMED as an implication; fixes B4N-1, B4N-2 (binding)

- **(a) c_k = 1.**
  - The envelope/Schur step and the identification of Hess E_k^br(0) with FLOW's chain form H_k are **read, not
    re-derived** (l.787-789). This is honestly labelled. It is supported at k = 1 by bb2 and by FLOW f1/c17.
  - **The F-tree extension to level-varying κ_j: VERIFIED** from FLOW l.256-266. The recursion is
    Ĝ_{k+1} = κ_k^{-1}P_⊥ + 𝒬(Ĝ_k). Induction clause (a), boundedness away from p ≡ 0, uses only that κ_k^{-1}P_⊥ is
    bounded and that the K ≠ 0 alias terms are bounded by (a) at level k. Clause (b) is
    |ŝ(p)|²Ĝ_{k+1} → 0 + L^{-4}·L²·L²·P_⊥. Neither uses κ_k = κ_{k-1}, and 𝒬 and Q̃_K are κ-independent. So the claim
    holds for any κ_j > 0 varying with j; [κ_-, κ_+] is not even needed for β = 1, only for the bounds.
  - The independent bound |c_k| ≤ (2/(em'))²M_2^{(m')} holds (|z_1z_2| ≤ |z|_1², x²e^{−m'x} ≤ (2/(em'))²).
- **(b).** β[R_k] = 0 trivially.
  - The M_n bound from the pair form is correct: max_{i,j}d ≥ max_id(b_1, b_i), and the split into n − 1 factors gives
    (4coth⁴(m'/(4(n − 1))))^{n−1}.
  - (I2) asks for the E-part up to **n = 5**, while BB-3_k was stated for n ≤ 4. BB-C's pair version gives every n ≥ 2 from
    the Hessian pair decay on the polydisc, so this is harmless. Record it as "BB-3_k's E-part extended to n = 5 by BB-C"
    (non-binding B4N-r1).
  - G_∇ via BB-E1 at complex B: correct given BA-3's sizes on the complex ball (C_M not evaluated; labelled).
- **(c).** BB-W and BB-sm apply with m = m'/2: R_k(0) = 0, gauge, B_4 and translation invariance (the value function does
  not depend on the fixing), and holomorphy. Correct.

**B4N-1 (binding, domain).** l.677 sets ρ := ε_0 and uses 𝒫_ρ = {B complex, max_b|B_b| ≤ ρ}.
- BFT-2 / Theorem BA give holomorphy on {e^z e^{B^r} : |B^r| ≤ ε_0 real, |z| ≤ r_ℂε_0} with r_ℂ ≤ 1.
- 𝒫_{ε_0} contains points with |Im B| = ε_0, and log(e^Be^{−Re B}) = i Im B + O(ε_0²). So 𝒫_{ε_0} ⊄ BFT-2's domain unless
  r_ℂ ≥ 1 + O(ε_0).
- Fix: take **ρ := r_ℂε_0/2** (BCH margin), or state explicitly that (I1) includes BA-10's complex data ball 𝒫_{ε_0} itself.
  Only the constants C_sm and C_♮ change.

**B4N-2 (binding, overclaim).** l.957 says "the right form of BFT-4 is E_k^br = c_kS_W + R_k with β[R_k] = 0 and R_k bounded
in the irrelevance norm 𝒩". l.820 lists the reasons this is not so:
- 𝒩 is a Taylor norm at V = 1 (n ≤ 5) plus one global gradient sup.
- BFT-4's stated consequences (REVIEW_S22 l.416-417: C_♭^{(k)}, (H-G), C_θ level-uniform by Cauchy) need sups of local
  pieces on polydiscs about *non-trivial* backgrounds. 𝒩 does not give them (BB-4♮'s "what it is not" (3)).

Replace with: "a marginal-extracted *Taylor-norm* form of BFT-4 (necessary, weaker); the polymer form ||·||_𝒜 remains
BFT-4". Apply the same change to the §7 table row (l.941) wording "BFT-4 … in the right form" at l.813.

**Does BB-4♮ inherit lane A's (α, θ) window problem?** **Yes, through its hypotheses only.**
- Lane A's corrected pair has the window α ≤ θ ≤ 1 − α (BFT_A l.394-399). Lane A's own BL-6 (b) shows that the (Pl)
  plain-current slot "as written fails for θ ≤ 1 − α" (BFT_A l.770, l.780). So at present (H-lin^∇) has **no consistent
  target pair** for plain level-l currents; the repair is the rough/smooth split, (G♯-rough), which is OPEN.
- (I1) is Theorem BA on that pair. (I2) runs through (H-rem^∇)_m. The soft cubic rows (∂ρ^{(2)})^Tr_l are among the plain
  level-l currents of lane A's GAP 1 (BFT_A l.386-390). So the window problem reaches **both** (I1) and (I2).
- BB-4♮'s own steps never use α, θ, θ_w or any Hölder component. They consume:
  - depth-k existence and uniqueness, and BA-9's identification;
  - holomorphy (BA-10);
  - BA-3's sup sizes;
  - exponentially weighted (m' > 0) pair decay of Hess E_k^br on a fixed polydisc.
- So the theorem **transfers unchanged** to any repaired pair whose output norm dominates the sup of own-unit link logs and
  soft fluctuations, and which carries e^{±md} weights with m > 0 uniform in the centre.
- It **does not survive** a repair that only reaches m = 0. Lane A's m > 0 versions are ARGUED, not written (BFT_A
  l.786-790).
- Add this sentence to §6.3's "what it is not" (5) (non-binding B4N-r2).

# PART C: §5.2 / §6.4-§6.6 (polymer form)

## C.1 Proposition BB-mix-wall (l.690-694; l.822-833): CONFIRMED as ARGUED; fix BMW-1

- **Product form, Σ_id(x, Q_i) ≥ (n − 3^d)M_c.** Correct: all but 3^d cubes lie at distance ≥ M_c.
- **Steiner form, ≳ (n/2^d − 1)M_c.** Correct up to an O(1) factor in the inference. A piece of the tree with ℓ^∞ diameter
  < M_c meets ≤ 2^d cubes, and a tree of length ℓ splits into ≲ 2ℓ/M_c + 1 such pieces. The order of magnitude stands;
  [inference] is the right label.
- M_c ≈ 2^d(m_0 + log(Cc_an))/μ_1 ≈ 10^{13}: arithmetic correct.

**BMW-1 (binding wording).** l.823 says "Switching one cube's pinning is an O(1) change of the field inside that cube, so
no per-cube smallness can come from the switch itself."
- In absolute terms the switch changes the fluctuation by ≤ r(ε) = 12𝔠_∞ε. Small fields are exactly the source of
  smallness that §6.5 then exploits, through bond weights.
- Correct reading: "the switch is O(1) *relative to the fluctuation*, and the hard pinning constraint has no known analytic
  interpolation of radius ≫ 1 (the mass family has radius 1 + O(γ/S), BB-mix-gap (2)). So for BB-loc's polymers the only
  mechanism identified is distance."
- Without this fix, §6.4 and §6.5 contradict each other.

## C.2 Construction BB-bond and Theorem BB-mix′_1 (l.694-706; proof l.835-905): CONFIRMED-WITH-FIX

I followed every step against PROOF's Theorem RW, N5-sf0, U0, N5-an♭ and BR1.

- **Setting at box size R (l.836-840).** Correct.
  - N5-sf0's proof uses R only through the AX box (4R + 5)L and T ≥ 4R + 6. ε_*(R) and 𝔑_R are the right replacements.
  - Theorem RW holds for any box partition with sides in [R, 2R) (R20-fix RW2-1).
  - From RW remark RW-2, ε_R(R) ≤ ½e^{−aL(R−R_*)/2}. So R = R_* + ⌈(2/(aL))log(2s̄)⌉ gives ε_R ≤ 1/(4s̄).
- **Step 1, splitting (S1).** Verified from RW's definitions.
  - G_□1_□ and R_□ = −1_{Ω_□^c}KG_□1_□ both have **columns in □ ⊂ Q(□)**. Their rows lie within R, resp. R + 1, blocks
    of □, hence in Q(□) or a *-adjacent cube when M_c ≥ R + 2.
  - Each piece therefore carries exactly the weight s_{Q(row)Q(□)} of the crossing it makes. In a product PR^n the column
    cube of each factor is the row cube of the next.
  - A zero weight between classes kills every chain that crosses. Entrywise |R(s)| ≤ s̄Σ|R_□|, since each row lies in one
    cube.
- **C2-1 (binding, constant).** l.847 states N_0(|P|) ≤ (2/γ')coth⁴(m/2), citing BB-geo (c).
  - The sum is over **links** y. PROOF l.5252 gives Σ_{b'}e^{−cd} ≤ **4**coth⁴(c/2) (4 directions per position), and RW's
    own proof uses N(|P|) ≤ (2/γ')·4coth⁴.
  - BB-geo (c) (l.45) has dropped the 4. §6.3 (l.795) uses 4coth⁴ correctly, so the file is internally inconsistent.
  - Fix: N_0(|P|) ≤ (8/γ')coth⁴(m/2) and **𝔠_♮ := (32/3)coth⁴(m/2)/γ'**. Correct BB-geo (c) to 4coth⁴(a/2) when the sum
    is over links.
  - The thresholds keep their form. Nothing else changes.
- **Step 2 (weighted contraction).** Verified.
  - ||K^{-1}(s)Πg|| ≤ s̄𝔠_♮p_Π·6ε ≤ 6𝔠_sε.
  - ℛ(B) − ℛ(B') = ∫[Hess f(B_t) − Hess f(0)](B − B'), with N_0 ≤ C_♭·s̄r_s by rows (S_{Q(b)} varies by row, but N_0 is a row
    bound). Hence Lip ≤ 12𝔠_s²C_♭s̄²ε and the ball is invariant.
  - A(1) = A*: K^{-1}Π = C_0Π, C_0ΠO_0 = id on ker h, BR1's map equals Φ_1 on ker h, and uniqueness in the r_s ball
    (r(ε) ≤ r_s by 𝔠_s ≥ 𝔠_∞).
  - The post-proof correction 𝔠_s := max(s̄𝔠_♮p_Π, 𝔠_∞) is needed and correct.
- **Step 3.** Verified. K^{-1}(s) and Π are block-diagonal over classes. S_{Q(b)}A is supported in the class of Q(b), so
  ℛ^s(A)(b) reads only that class. The sup-norm ball is a product, so A(s) = ⊕A_i(s), and A_i depends only on the bonds
  internal to its class. ΔE(1) = E_1^br − E_∅.
- **Step 4.** Verified.
  - f(1) = Σ_Γ∫∂^Γf(s_Γ, 0) is correct.
  - At s_{𝔅∖Γ} = 0 the classes are the components of (cubes, Γ). ∂^Γ kills every component term that misses a bond of Γ,
    so only connected Γ survive (plus Γ = ∅).
  - *-connectivity, gauge invariance (R_Ĝ block-diagonal, commuting with 1_Q and S_Q; uniqueness) and the support X^+ are
    correct.
- **Step 5.** Verified.
  - sup_{|s|≤s̄}|ΔE_X| ≤ |X|N_Qc_ρs̄r_s, with ||S_QA|| ≤ s̄||A||.
  - Cauchy with radius s̄ − 1 about [0, 1]^Γ stays inside |s| ≤ s̄.
  - |Γ| ≥ |X| − 1, and there are ≤ 2^{40|X|} edge subsets. With |X| ≤ 2^{|X|−1}: C_RK^{|X|−1}, K = 2^{41}/(s̄ − 1).
  - Lattice animals (80e)^{n−1} and c_ane^{m_0}K ≤ ½ give ||R||_𝒜 ≤ 2e^{m_0}C_R.
  - R_1 = (L^{d−2} − 1)S_W + ΣR(X) is consistent with c_1 = 1:
    - U0 (ii) puts the full V_P on L^{d−2} corner plaquettes per block, so E_∅ = L²S_W;
    - the smooth minimiser spreads it, giving coefficient 1 (bb2).
- **C2-2 (binding, labelling of c_ρ).** l.886-889 take S_ρ, i.e. holomorphy and boundedness of each *single density*
  D(e^ÃU^(0), V) on the radius-r_♭ polydisc, from "the proof of N5-an♭".
  - Verified: N5-an♭ (PROOF l.5648-5660) is stated for the entries of the **gradient and Hessian of F** and of h_U, D_U and
    P_res. It is not stated for individual densities. A partial sum Σ_{D owned by X} is not an entry of ∇F, so the
    statement cannot be cited as is.
  - Its proof covers densities verbatim. The plaquette densities are entire, and the soft densities are finite compositions
    with NA-alg's analytic X_0, with finitely many types modulo translation.
  - Fix: add a one-line **Lemma N5-an♭-dens** with that proof, and make the theorem's status "PROVEN-HERE given N5-an♭-dens
    (routine)". The constant n_1 in c_ρ := 2S_ρn_1/r_♭ is unnecessary (one-variable Schwarz along w ↦ ρ_D(wÃ) gives
    2S_ρ/r_♭), but it is harmless.
- **C2-3 (binding, domain).** l.701-702 / l.898 claim the result on "BR1 (v)'s complex neighbourhood |z_c| ≤ α_*/8". Two
  problems:
  - (i) BR1 (v) requires ε_V ≤ ε_br/4, while ε_mix contains ε_br(R), not ε_br(R)/4.
  - (ii) The radius α_*/8 itself is not supported (Part D.4).

  Fix: state the result for |z_c| ≤ ϱ_br := ε_br(R)/16 (any fixed radius with complex curvature ≤ ε_mix), and require
  ε ≤ ε_mix/2. BFT-2's polydisc is r_ℂε with r_ℂ ≤ 1, so it lies inside, and BFT-4 at k = 1 is unaffected.
- **C2-4 (minor).**
  - "C_R explicit" (l.704) should read "explicit in terms of N_Q, s̄, r_s and the uncomputed c_ρ".
  - "every m_0 > 0" (l.898) is correct only because ε_mix depends on m_0 through s̄. Say "for each m_0 > 0, ε_0 ≤
    ε_mix(s̄(m_0))". BFT's constants may depend on m_0, which is a fixed choice, so this is admissible.

**Verdict.** With C2-1..C2-4, Theorem BB-mix′_1 is a correct proof of **BFT-4's polymer bound at k = 1**.
- The constants are ledger constants plus the routine c_ρ.
- The per-cube smallness K = 2^{41}/(s̄ − 1) ∝ ε^{1/4} comes from the analyticity radius in the bond weights
  (ε_mix ∝ s̄^{−4}). It does not come from M_c, which is only R + 2. This is the mechanism of a Glimm-Jaffe-Spencer /
  Brydges-type decoupling expansion, here run on the critical point of the classical problem.
- The polymers are not BB-loc's, which is correctly stated.

## C.3 Proposition BB-mix-k (l.707-711; l.907-915): CONFIRMED as a named wall; fix BMk-1

The two obstacles are real:
- (W1) the composite 𝓛^{-1} has no walk expansion yet;
- (W2) the sharp cube weights S_Q have ∇^c jumps L^{k−j}·(s̄ + 1)|x^c| at level j and uncontrolled Hölder seminorms in 𝔐^∇.

The per-level alternative is correctly placed outside the anti-circularity clause.

**BMk-1 (binding, precision).** "(H-RW^∇)_k: a walk/localised expansion of 𝓛^{-1} whose inter-cube pieces carry a factor
≪ 1/s̄, uniformly in k" is not a statement. To be usable by BB-bond_k it must specify the following.
- (a) The partition: level-k cubes of side M_c (level-k blocks), with all levels' variables of a cube assigned to it.
- (b) The decomposition 𝓛^{-1} = P(1 − R)^{-1}, with R = Σ_□R_□ over boxes □ of an R-partition refining the cubes. Each
  piece maps 𝒴^∇ data supported in □ to 𝔐^∇ outputs, so that column-in-□ holds. This is what (S1) needs.
- (c) The bounds ||P||_{𝒴^∇→𝔐^∇} ≤ G and ||Σ_□|R_□|||_{𝒴^∇→𝒴^∇} ≤ ε_W, with s̄ε_W ≤ ¼, uniformly in k, T and the data in
  𝒞_glob(ε). "Solid" absolute-value forms are needed for the s-weighting, so B3-F3's solid-norm caveat applies.
- (d) Holomorphy in the data on BFT-2's ball.
- (e) (W2) in the form: multiplication by the s-weighted cube projections is bounded 𝔐^∇ → 𝔐^∇ with norm ≤ Cs̄, or a
  smooth-weight variant with lane A's (COMM).
- (f) (H-rem^∇)_m for s-weighted arguments: the Lipschitz bound of the nonlinear remainder ℛ^s in 𝔐^∇ with ||S_QA|| ≤ s̄||A||.
  This is Step 2's analogue, and §6.6 omits it.

Item (c) is the heart. Lane A's (H-lin^∇)_m gives only e^{−mM_c} per cube crossing, so it needs M_c ≫ log s̄/m and an
organisation into walks. §6.6 says so (l.909-911).

# PART D: check bb2 and a ledger flag

## D.1 Pre-registration: CONFIRMED

The criteria were born 05:50:12, the script 05:50:30, and the output 05:51:32-34 (stat). The criteria text matches the
script: the directions, t values and thresholds; B2-1 ≤ 1e-8; B2-2 |β(0.025) − 1| ≤ 1e-3 with ratio in [2.5, 6]; B2-3 ρ ratios
in [0.8, 1.25]; verdict at κ = 1 only.

## D.2 Script audit: CONFIRMED

- `H1` is bb1's `hats` formula at off-grid momenta, in complex128. bb1's formula was audited in REVIEW_BFT_B_S1 Part C.
- H_W = d1c†d1c. Both H_1 and H_W annihilate d0c (d1d0 = 0), so ||H_1 − H_W|| measures transverse content only.
- `transverse` is a correct complex Gram-Schmidt. β is a Rayleigh-quotient ratio on transverse unit vectors.
- B2-3 fixes c_1 = 1 and does not fit it.
- Weakness (not a defect): B2-3 implies B2-2's O(t²) approach, so the two are not independent. Neither tests n ≥ 3 (BB-W's
  Ward-identity content), k ≥ 2, non-abelian structure or backgrounds. The file says so (l.932-934).

## D.3 Reading: CONFIRMED

§7's numbers match bb2.out: the worst-direction β − 1 values −1.243e-1, −3.432e-2, −8.809e-3, −2.217e-3, −5.552e-4; ρ =
0.774 … 0.888; ratios 3.993; the κ = 0.25 and κ = 4 rows.

## D.4 Ledger flag (not a lane-B defect; load-bearing for BB-3_1, BB-loc, BB-mix′_1)

BR1 (v) (PROOF l.5671-5672, proof l.5701-5703) claims that A*(e^zV) exists "with the same bounds" for |z_c| ≤ α_*/8.
- Its contraction uses ||Φ(0)||_∞ ≤ 6𝔠_∞ε_V, from Lemma U0 (iv), which is stated **for real V** (l.5619-5620).
- For V = e^zV^r the corner plaquettes of U^(0)(V) carry log V_P = O(ε_V + 8|z|).
- At |z| ≈ α_*/8 ≫ ε_br the gradient is O(α_*), not O(ε). The conditions 12𝔠_∞²C_♭·(size) ≤ ½ and size ≤ r_♭/(24𝔠_∞) are
  then not implied (α_* is not ≤ 1/(24𝔠_∞²C_♭)).
- The holomorphy argument goes through on the smaller fixed radius ϱ_br := ε_br/16: complex curvature ≤ ε_V + 8ϱ_br ≤ ε_br
  for ε_V ≤ ε_br/2. This radius is still ε-independent.
- Consequences:
  - BB-3_1's Cauchy constants (4/ϱ)^{n−1} change (ϱ := min(ϱ_br, r_♭/16)). They stay ε-independent.
  - BB-loc's and BB-mix′_1's complex domains become |z| ≤ ϱ_br.
  - Nothing in BFT-3/BFT-4 at k = 1 changes qualitatively.
- [Inference from reading U0 (iv) and BR1's proof. Recommend that the ledger owner restate BR1 (v)'s radius. REVIEW_S20's
  RW2-2 addressed 𝔠_∞ at complex backgrounds, not the size of g.]

# PART E: is (H-RW^∇)_k the same object as SF's (L-loc), FLOW's (L-loc), or existence's (CE-loc)?

**No to all three.** The precise relations follow.

| object | what it is | relation to (H-RW^∇)_k |
|---|---|---|
| **SF (L-loc)_k** (SF l.846-850) | **Output**: the main-term densities 𝓔_{k,x} = Σ_R𝓔_{x,R}, each piece strictly local, holomorphic and ≤ S_ke^{−κ_Ld(R)} on a uniform polydisc | (H-RW^∇)_k + (W2) + C.3 (f) ⇒ (via BB-bond_k) BFT-4's polymer form, which is (L-loc)_k for the **branch (classical) part** of 𝓔_k (per-cube smallness K^{|X|−1} ⇒ e^{−κ_Ld(R)} with κ_L ≈ log(1/K)/M_c). The fluctuation-integral parts of 𝓔_k are not covered. At k = 1, BB-mix′_1 supplies (L-loc)_1's branch part, so the §7 note (l.962-963) is right with this qualification |
| **FLOW (L-loc)/(L-loc2)** (FLOW l.2329-2341) | Pointwise exponential decay of the kernel of one **single-level** operator Ã(U) = H + M^T𝒞_n^{-1}M + D_UE'D_U^* and of its first and second background derivatives, ARGUED by Combes-Thomas | Different operator (one level n, per-level 𝒞_n) and weaker property: decay, not a walk structure with an analytic s-weakening. A walk expansion of Ã would imply (L-loc2); the converse fails. Not the same object |
| **existence (CE-loc)** (EXISTENCE l.4330-4350) | A probabilistic cluster expansion of the stage-j **conditional law** on a region Ω with frozen exterior, including the excision of large-field and deep-noise regions ((CE-Q^∞), RLARGE branch (iii)) | Needs a localised (walk) expansion of the stage-j **fluctuation covariance**, which is per level: Theorem RW (iv) / RW-triv / N5-sf_i. It also needs large-field machinery. (H-RW^∇)_k is classical, composite and small-field. It does not supply (CE-loc) |

**Common ancestor.** All four rest on Theorem RW (iv), the s-weakened walk expansion with decoupling.
- SF's CE-exp^k and existence's (CE-loc) use it for per-level covariances.
- BB-mix′_1 uses it at level 0.
- (H-RW^∇)_k is its composite-route, multi-level analogue for lane A's 𝓛^{-1}.

The cross-lane statement to record: **(H-RW^∇)_k is the single localisation input that the composite route needs.** It
would give BFT-4's polymer form for every k, hence SF's (L-loc)_k for the branch part. It would plausibly also give
(SF-∞)_B and FLOW's (SF-∞) [inference]: walk terms that wrap the torus are suppressed by ε_W^{T/(2M_c)}. It does not touch
the fluctuation-integral localisation ((CE-loc), CE-exp^k's activities), which stays per level.

---

# Overclaims
1. "the right form of BFT-4" (l.957, and the l.813 phrasing). Fix B4N-2.
2. "no per-cube smallness can come from the switch itself" (l.823). Fix BMW-1.
3. "on BR1 (v)'s complex neighbourhood |z_c| ≤ α_*/8" (l.701-702, l.898). Fix C2-3; ledger flag D.4.
4. "C_R explicit" (l.704). Fix C2-4.
5. BB-mix′_1 is "PROVEN-HERE (given the ledger theorems …, N5-an♭ …)", but N5-an♭ does not state density bounds. Fix C2-2.

# Tally (lane B session 2; nothing counted in PROOF)

| verdict | items |
|---|---|
| CONFIRMED | all 11 RBB1 fixes (residual R-1 cosmetic); **Lemma BB-W**; **Lemma BB-sm**; the F-tree κ_j-variation inference (verified from FLOW's proof); bb2 pre-registration, script and reading; re-run byte-identical |
| CONFIRMED as an implication, with fixes | **Theorem BB-4♮** (B4N-1 domain, B4N-2 overclaim; non-binding B4N-r1/r2) |
| CONFIRMED-WITH-FIX | **Theorem BB-mix′_1 / Construction BB-bond (BFT-4 polymer bound at k = 1)** (C2-1 constant, C2-2 N5-an♭-dens, C2-3 domain, C2-4 wording) |
| CONFIRMED as ARGUED, with a wording fix | BB-mix-wall (BMW-1) |
| CONFIRMED as a named wall, not precisely stated | BB-mix-k (BMk-1: statements (a)-(f)) |
| provenance | consistent with the log; bb2 order verified; §5-before-§6 not stat-verifiable (single file), sizes agree to 4 bytes; two post-proof corrections verified against the pre-stated text; the 05:57 §6.4 edit is unmarked in the file |
| ledger flag | BR1 (v) radius α_*/8 unsupported; ϱ_br := ε_br/16 works (D.4) |

# Required fixes (binding for the next lane-B session)
1. **B4N-1.** ρ := r_ℂε_0/2 in §5.0/§6.3, or name BA-10's complex data ball explicitly as part of (I1).
2. **B4N-2.** l.957 and l.813: "right form of BFT-4" → "a marginal-extracted Taylor-norm form (weaker than ||·||_𝒜)".
3. **BMW-1.** l.823: "O(1) change" → "O(1) relative to the fluctuation (absolute O(r(ε))); the hard pinning has no known
   large-radius analytic interpolation".
4. **C2-1.** l.847-849: N_0(|P|) ≤ (8/γ')coth⁴(m/2), 𝔠_♮ := (32/3)coth⁴(m/2)/γ'; BB-geo (c) l.45: 4coth⁴ for sums over
   links.
5. **C2-2.** Add Lemma N5-an♭-dens (single-density holomorphy and bound S_ρ on the r_♭-polydisc; the proof of N5-an♭
   verbatim). Restate BB-mix′_1's status as given N5-an♭-dens.
6. **C2-3.** BB-mix′_1's complex domain → |z_c| ≤ ε_br(R)/16 with ε ≤ ε_mix/2. Carry D.4's radius into BB-3_1 and BB-loc
   (constants only).
7. **C2-4.** "C_R explicit" → "explicit up to c_ρ"; "every m_0" → "for each m_0, with ε_0 ≤ ε_mix(s̄(m_0))".
8. **BMk-1.** Restate (H-RW^∇)_k as (a)-(f) of C.3, including the s-weighted (H-rem^∇) (f).
9. **R-1 (cosmetic).** Point l.77/l.79 to the B1-2 replacement; mark the 05:57 edit in §6.4.

# Strategic verdict

- **BFT-4 at k = 1 is now a theorem in polymer form** (BB-mix′_1 after C2-1..C2-4), on curvature-small backgrounds, for
  every m_0 with ε_0(m_0). Together with BB-3_1, level 1 of BFT-3 + BFT-4 is closed modulo the routine N5-an♭-dens and the
  BR1 (v) radius restatement. The mechanism (small fields ⇒ large bond-analyticity radius ⇒ per-cube smallness) is sound,
  and it answers session 1's "(BB-mix) OPEN even at k = 1".
- **For every k on 𝒞_glob:** BB-4♮ correctly separates the marginal coefficient (c_k = 1 exactly, F-tree with varying κ_j)
  from an irrelevant remainder (BB-W, BB-sm). It is a clean, architecture-consistent statement, but a Taylor-norm one.
  Its inputs are exactly lane A's open estimate at m > 0 plus (SF-∞)_B (dispensable, BW-r1). So it inherits lane A's
  window problem as a hypothesis and is pair-agnostic in its own steps.
- **The single remaining localisation wall of the composite route is (H-RW^∇)_k**, stated as in BMk-1. It is not SF's,
  FLOW's or existence's localisation object, but it implies the branch part of SF's (L-loc)_k. **Priority:** state
  (H-RW^∇)_k precisely, then test whether lane A's BL-type exact reductions admit a box-walk form at the trivial chain.
  That is the k ≥ 2 analogue of what Theorem RW did at level 0.

---

## Re-run record (bb2)
- Runner: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/revBB2/run.sh`.
  - It waits with `until mkdir …/scratchpad/locks/numeric 2>/dev/null; do sleep 20; done`, then waits for load1 < 8.
  - Environment: nice 10; OPENBLAS/OMP/MKL/vecLib threads = 1; PYTHONDONTWRITEBYTECODE=1; `/usr/bin/time -l`; python3
    without -I; no `timeout`; no trap.
  - It runs checks/bb2_symbol.py unchanged, with outputs in revBB2/.
  - It calls `rmdir` exactly once.
- Lock held 06:06:33-06:06:35 UTC. load1 2.26; memory free 42%; 1.83 s wall; peak RSS 566 MB; exit 0.
- After the run: the lock directory is gone, no bb2 process is left, and checks/ holds no __pycache__.
- **Result: with the timing/RSS suffixes stripped, revBB2/bb2.out is byte-identical to checks/bb2.out.** bb2 PASS: B2-1
  1.12e-16; B2-2 max|β(0.025) − 1| = 5.552e-4, ratios 3.993; B2-3 ρ ratios 1.0069, 1.0017.
