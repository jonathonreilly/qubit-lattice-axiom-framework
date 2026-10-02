The report holds up as mathematics: Theorem 1 is correct, with two one-line gaps. It also fills a gap the landed notes left open. But it does not lower the Born price from the axiom text; that price moves into supplied structure. Separately, Theorem 2 has a real gap at its last step, and one ARGUED claim about compression is wrong.

No code was run; every check below is by hand. EXACT means a hand proof or exact hand arithmetic, and ARGUED means reasoning I have not fully checked. Line 1 of REPORT.md is a note from the harness asking the reader to save the file; it is not science and should be stripped.

## A. Verdict per claim

| Claim | Verdict | Reason |
|---|---|---|
| §1 / summary 1: every antipodal law is the Born law of some convex hull [EXACT] | HOLDS WITH NARROWED SCOPE | Needs Σ\|h_l\| < ∞. The step law (landed in the menu note) fails it: its Legendre coefficients are \|a_l\| = \|P_{l−1}(0)\| + \|P_{l+1}(0)\| ~ l^{−1/2}, so ‖Φ(q)‖² = Σ\|a_l\| diverges. Polynomial laws, including both witnesses, are fine. |
| O1 antipodal blindness | HOLDS (EXACT) | (2a−1)h(p·q) = \|r\| h(r̂·p), rechecked. |
| O2 cube orbits blind below l = 9 | HOLDS (EXACT) | Counts rechecked in §C. |
| O3 barycenter criterion | HOLDS WITH NARROWED SCOPE | The conclusion is almost-everywhere. It assumes the barycenters and weights are given in advance. |
| O4 records-only conditions cannot carry coherence | WRONG as stated | With record conditions on two sites, C4 is satisfied by every odd h (see §D3), not unsatisfiable. |
| O5 lock plus no-signalling passes every law | HOLDS | Matches the landed replacement-rule countermodel. |
| O6 soldered reading | HOLDS | A bump h = t + εg works, with g odd, vanishing at the finitely many probed points and at ±1, and \|g\| ≤ 1 − \|t\|. |
| Theorem 1, Steps 0–5 | HOLDS WITH NARROWED SCOPE | The math is correct. There are two missing lines (§B), and several premises it uses are not listed. |
| "Repeat certainty is an output" | HOLDS WITH NARROWED SCOPE | It comes from the null-option half of C4 (§D3). It is already landed inside the affine family as λ(λ−1) = 0. |
| "No affinity clause" | HOLDS WITH NARROWED SCOPE | There is no affinity clause with prescribed weights. C3 + C4 together are a barycentric-coherence clause with self-generated weights. |
| Witness arithmetic | HOLDS | Every value recomputed (§C). |
| Theorem 2 (trine) | HOLDS WITH NARROWED SCOPE + GAP | h = ct holds almost everywhere. The next step, "f(1) = 1 sets c = 1", fails under that hypothesis (§F). |
| R3: the trine row gives the same identity | HOLDS | (2/3)Σ f(t_k·q) = 1 is equivalent to Σ h(t_k·q) = 0. |
| ARGUED: "compression and Born force each other under marginal no-signalling" | WRONG | Born plus the replacement rule passes marginal no-signalling (the landed countermodel covers every binary law that reads the reduced state). The landed compression note also needs joint Born effects and full tomography of the partner. |
| Summary 6: "settles" the deferred nonlinear-law item | HOLDS WITH NARROWED SCOPE | Settles the covariant, binary, antipodal case under continuum abundance. |
| Summary 9: relation to Han–Choi "unverified" | GAP | Han–Choi is a close precedent and can now be checked (§D4). |
| Sentence-audit row "C3 is reading-level" | GAP | The landed randomizer note lists the same premise as supplied. The axiom text says "A state is a configuration of records." |

## B. Re-derivation of Steps 0–5

**Step 0** [EXACT]. This needs unsoldered SO(3) covariance applied to the law at mixed law-level states. That is a reading beyond pure states and should be listed as a premise.

**Step 1** [EXACT]. Recomputed:
- ⟨m|_Bψ⟩ = √a cos(θ/2)|0⟩ + √(1−a) e^{−iφ} sin(θ/2)|1⟩, with squared norm (1+rc)/2.
- The z-numerator is (r+c)/2, giving u_+ = (c+r)/(1+rc).
- The transverse length is 2\|αβ\|/norm = √(1−r²)√(1−c²)/(1+rc).
- ⟨σ_x⟩ ∝ cos φ and ⟨σ_y⟩ ∝ −sin φ, so the azimuth is −φ. For the outcome −m: (r−c)/(1−rc), and the azimuth is −φ+π.
- Both n_± are unit vectors, since (c+r)² + (1−r²)(1−c²) = (1+rc)².
- Quantum check: the Born-weighted average Σ p^Born_± n_± equals r e_z.

**Step 2** follows from C4. **Step 3, (A)**: correct, with y = cos φ ranging over [−1, 1]. Setting r = c = √ρ gives s_+ = (1−ρ)/(1+ρ) = 1/λ and s_− = 1.

**Step 3(i): gap (minor).** Spreading the zero needs w_−(λ₀) ≠ 0 for at least one λ₀ > 1. Iterating h(y) = κ h(y/λ₀) then pushes the zero set from (0, δ) to (0, 1], including h(1) at z = 1/λ₀. If instead H(√ρ, √ρ) = 1 for every ρ, then (A) gives h ≡ 0 on (0, 1) but leaves h(1) free.
- The law "h = 0 on (−1, 1), h(±1) = ±1" then survives (A).
- It is removed by (B) at α = β: H(r, r) = [h(1) + h(cos 2β)]/2 = h(1)/2 ≤ 1/2, which contradicts H(r, r) = 1.
- Also, "the law is the constant coin" needs (B) to give H ≡ 0. Both repairs are one line each.

**Step 3(ii): gap (minor).** The claim "h(1) ≠ 0" is missing a step. If κ(λ) = 0 for some λ, then w_+ = 0, and (A) with s_− = 1 gives h ≡ 0 on [−1, 1]. So κ > 0 throughout case (ii). Then h(1) = 0 would force h(1/λ) = 0 for every λ, contradicting case (ii).
- The Cauchy step is correct. Let g(x) = log κ(e^x); it is additive on (0, ∞) and g ≥ log\|h(1)\|. Since g(nx) = n g(x) stays bounded below, g ≥ 0, so g is monotone and therefore linear. No measurability assumption is used.

**Step 3(iii)** [EXACT]. w_+/w_− = ((1+rc)/(1−rc))^γ gives H = tanh(γ artanh(rc)).

**Step 4** [EXACT]. With c = 0, w_± = 1/2, n_± = (±sin β, 0, cos β), and n_±·p = cos(β ∓ α).

**Step 5** [EXACT].
- At α = π/2 − ε, the right side of (B) is [h(sin(β+ε)) − h(sin(β−ε))]/2. Its ε-derivative is γ h(1) cos β (sin β)^{γ−1}; the left side's derivative is γ cos β. For γ > 0 this forces γ = 1 and h(1) = 1.
- γ = 0 contradicts h(1) ≠ 0 from case (ii), so it is simply excluded. The wording "the constant law" belongs to case (i).
- c = ±1 is covered by (B) at α ∈ {0, π}: H(r, ±1) = ±r. So H(r, c) = rc for every c.

**Optional shortcut** [EXACT]. Take m = e_z and p = e_z in Step 2. This gives H(r,1)(h(1) − 1) = 0. In case (ii), (B) at α = 0 gives H(r,1) = h(r) ≠ 0, so h(1) = 1 at once. This is the nonlinear analogue of the landed λ(λ−1) = 0.

**Premises used but not listed:**
- **Continuum abundance:** every ρ ∈ (0, 1) with B's menu tied at c = r, every azimuth φ, A's probe e_x, an arc of the xz great circle, and the ε → 0 limit. With a countable dense set of λ, h is fixed on that set and free elsewhere. So "no regularity" is true, but abundance takes its place. The landed program tracks abundance as a separate unpaid price (MENU_INDEPENDENCE…NEEDS_MENU_ABUNDANCE_2026-09-03; THE_MATTER_LAWS_OWN_TICKS…ABUNDANCE_IS_UNPAID_2026-09-04).
- **Same H at both sites:** the function giving B's weights is the same as A's direct law. This is translation covariance applied at the level of law-level states.
- **Controlled preparation of every ψ_r.** In the landed note this is a supplied partial swap plus local rotations.

## C. Arithmetic (EXACT, by hand)

- **(A), cubic law at r = c = 3/5:** (1+rc)/(1−rc) = 17/8; cubed, 4913/512; so H = 4401/5425. Cross-check: (3x + x³)/(1 + 3x²) at x = 9/25 is 17604/21700 = 4401/5425. ✓
- **(B), same point:** cos 2β = −7/25, so H = (1 − 343/15625)/2 = 7641/15625. ✓ Born gives 9/25 in both.
- **Trine:**
  - cubic: 1/2 + (1/6)(3/4) = 5/8 ✓
  - monotone: h(−1/2) = −19/32, Σ = −3/16, value 15/32 ✓
- **Tetrahedron:**
  - cubic: 1/2 + (1/8)(8/9) = 11/18 ✓
  - monotone: h(−1/3) = −11/27, Σ = −2/9, value 17/36 ✓
- **l = 5 rogue:**
  - P_5(−1/2) = −23/256, Σ = 21/256, value 1/2 + 21/1536 = 263/512 ✓
  - P_5(1/3) = 1/3, so 1 + 3P_5(−1/3) = 0 ✓
  - It is monotone: min P_5′ = −5/2, so h′ ≥ 0.65.
- **T-invariant counts:**
  - l = 5: (11 − 8 − 3)/12 = 0 ✓
  - l = 3: 1; l = 7: 1; l = 9: 2; l = 11: 1. Among odd l ≥ 3, l = 5 is the one sector the tetrahedron misses, which supports the claim.
- **O-invariant counts:** l = 1, 3, 5, 7 give 0; l = 9 gives (19 + 8 + 6 − 9)/24 = 1 ✓.
- **Monotone ratio:** h(λz)/h(z) = λ(5 − λ²z²)/(5 − z²) ✓.

## D. Semantics

**D1. Does C3 presuppose linearity? No.** [EXACT] For unit ψ, ψ′ in C²⊗C², Tr_Bψψ† = Tr_Bψ′ψ′† holds exactly when ψ′ = (1⊗U)ψ for some unitary U, because purifications of equal dimension differ by a unitary on B. So, given C1 and a law that reads the joint vector, C3 is equivalent to this: A's law is unchanged by unitaries applied to B alone. That is a no-signalling premise about B's local reversible operations, not a probability premise. It leaves F an arbitrary function of (\|s\|, ŝ·p), so Theorem 1 really does treat a nonlinear class.

- [ARGUED] The Born weights are carried by C1 + C2 geometry instead. The ratio s_−/s_+ = (1+rc)/(1−rc) is the ratio of the compression norms ‖⟨±m|ψ⟩‖², and the transverse probe in (A) reads exactly that ratio. They are not assumed about F; they come in through the normalisation in compression.
- C3 is still not a reading of the axiom text. The Qualification says "A state is a configuration of records," and Admissibility conditions the distribution on nearest-neighbour conditions, not on a site's own law-level state. The landed randomizer note puts the identical premise under "Supplied setting."

**D2. "No affinity clause."** C3 + C4 together say Σ w_± F(n_±) = F(ρ_A) over every steering ensemble. With Born weights, that is exactly the landed preparation-affinity premise restricted to steering. So Theorem 1 trades "affinity with prescribed Born weights" for "barycentric coherence with self-generated weights." That is a real sharpening, since the weights and the calibration come out as results. But it is still an affinity-type clause.

**D3. What each half of C4 does.** Split C4 into two parts:
- **C4a, menu-to-menu no-signalling:** A's average over B's pick is the same for every menu m.
- **C4b, the null option:** that common value equals A's direct law at ρ_A.

C4a alone does not give repeat certainty [EXACT]:
- C4a reproduces (A), by comparing with m = e_z, where n_±·e_x = 0. So the power law follows, and B's weights are tanh(γ artanh(rc)).
- Comparing m = e_x with m = e_z on xz probes gives H(r,1) h(cos α) = [h(cos(β−α)) + h(cos(β+α))]/2. Its ε-expansion forces γ = 1 and H(r,1) = r, but h(1) cancels out.
- **Explicit survivor:** h(t) = ct for any c ∈ [−1, 1] with c ≠ 0, with mixed-state law H(r, c′) = rc′. Born weights give Σ w_± n_± = r e_z for every m, so the average is c·r·p_z for every m. This includes anti-Born on pure states. The law h ≡ 0 with any odd H also survives.
- **Consequence:** calibration (h(1) = 1) is bought by C4b + C3 + the same H at both sites. In record terms, C4b equates "A forms first" with "B forms first, then A" for A's marginal. That is a marginal formation-order-blindness clause, and it is the A-marginal of Han–Choi's ordering condition.

What the axiom text supports [ARGUED]:
- The report grounds C4 in reading note 1 plus nearest-neighbour determination ("B's menu is distance-2 data"). That supports C4a at most.
- C4b compares A's law before and after a change in one of A's own nearest-neighbour conditions (B's record). The variation clause expects that change to move A's distribution, so the reading does not supply C4b.

The O4 error. With record conditions, two sites and unsoldered covariance:
- A's law with B unrecorded, and B's law with A unrecorded, are both fair coins on antipodal menus.
- After B's pick, A's condition is ±m, so A's average is ½[f(p·m) + f(−p·m)] = ½ for every odd h. C4 is satisfied by every law, not unsatisfiable.
- The landed constancy theorems (HOLES_AS_UNRECORDED_SITES…, ORDER_BLIND_NEAREST_NEIGHBOUR…) are about joint order-blindness on finite alphabets under the unsoldered reading. The ORDER_BLIND note also exhibits varying order-blind rules on the Haar sphere under soldering.
- So all of C4's power to tell laws apart comes from C1–C3.

**D4. Literature and circularity.**
- **Gleason:** Theorem 1 is not a Gleason-type argument. It uses no frame functions, and Gleason fails for d = 2. [ARGUED]
- **Galley–Masanes, Quantum 2, 104 (2018):** per the abstract, alternatives to Born can be no-signalling but violate purification and local tomography. So no-signalling plus pure-state kinematics does not force Born. In Theorem 1 the extra premises are C2 and C4b; C3 follows automatically from no-signalling under B's local unitaries (D1). This is consistent, but where the Galley–Masanes alternatives fail C1–C4 is not identified; C2 is likely. [ARGUED]
- **Han & Choi, arXiv:1307.2026 (Sci. Rep. 2016):** this is from a fetched summary of the PMC full text; I did not check their derivation line by line.
  - Their setting: two binary devices, collapse to eigenstates, the same unknown rule H for both parties, H(0) = 0 and H(1) = 1 assumed, H a function of the squared amplitude. They require the Alice-first and Bob-first joint distributions to agree, and conclude H(x) = x.
  - This is the same mechanism as Theorem 1. If the summary is accurate, Theorem 1 is sharper in three ways: it does not assume H(1) = 1, it allows a general covariant mixed-state law, and it uses only the A-marginal of the ordering condition.
  - Verdict on circularity: not circular, but also not new in kind.
- **Svetlichny, Found. Phys. 28, 131 (1998):** checked from the abstract only. It is the dynamics-side cousin: collapse plus no superluminal signalling makes state transformations linear.

## E. Comparison with landed notes on origin/main

- **Recorded-randomizer note (2026-09-24):** same supplied setting.
  - It already has the self-weighted classification inside the affine family, λ(λ−1) = 0, giving Born or the constant law. So "repeat certainty as an output" is already landed there.
  - It explicitly defers the nonlinear self-weighted classification. Theorem 1 extends it to all bounded, covariant, binary antipodal laws.
  - No contradiction: the landed runner's tanh and cubic laws signal under compression and pass under the replacement rule, which matches Theorem 1 and O5.
- **Compression note:** argues "joint Born effects + sharp marginals + full tomography of the partner ⇒ the compressed partner state," and warns that recovering the same update by the steering route would be circular. The report's mutual-forcing sentence invites exactly that circle. C2 must be supplied independently.
- **Synthesis note, line 176:** lists "nonlinear-law classification" as open ✓.
- **Menu note, Theorems 3–4:** the witnesses match exactly; the monotone law (1+t)/2 + t(1−t²)/8 corresponds to h = t + t(1−t²)/4. Theorem 1 removes them only when they are re-read as laws on a site's own state, not as laws conditioned on a neighbour's record.
- **Born-price note (2026-09-05), Appendix A2:** gets linearity from all non-collinear balanced ternaries plus homogeneity, with no covariance. The single equilateral trine with Funk–Hecke, and the tetrahedral l = 5 rogue, do not appear in it or in the 2026-09-03 note (checked by grep). Theorem 2 is a modest extension.

## F. Theorem 2 gap

Funk–Hecke under an "almost every p" hypothesis gives h = ct almost everywhere, not at every point.

**Counterexample to "f(1) = 1 sets c = 1":** take h(t) = t/3 on (−1, 1) and h(±1) = ±1. It is odd, monotone, satisfies \|h\| ≤ 1 and f(1) = 1, and Σ_k h(t_k·p) = 0 except at the six points p = ±t_k.

**Repair** [EXACT]. Coin-versus-trine coherence actually holds for every p. Let g = h − ct; g vanishes off a null set N.
1. For \|s\| < 1, put t_1 = e_1 and take the circle p = (s, √(1−s²) cos φ, √(1−s²) sin φ).
2. On it, t_2·p = −s/2 + (√3/2)√(1−s²) cos φ, and t_3·p is similar. Both are non-constant with isolated critical points, so their preimages of N are null.
3. Choose p on the circle with both values outside N. Then g(s) = 0.
4. At p = t_1, g(1) = −2g(−1/2) = 0. So h = ct at every point, and f(1) = 1 then gives c = 1.

## G. Required corrections

1. Strip the harness note on line 1.
2. §1 / summary 1: add the condition Σ\|h_l\| < ∞ and cite the step-law counterexample.
3. Step 3(i): add the w_− ≡ 0 case, removed via (B), and note that H ≡ 0 comes from (B).
4. Step 3(ii): add the κ > 0 line.
5. Step 5: say γ = 0 is excluded within case (ii).
6. Premise list: add continuum abundance, covariance of the mixed-state law, the same H at both sites, and preparation of every ψ_r. Change "no regularity" to "no regularity; continuum abundance used instead."
7. Move C3 to the supplied column, and restate it as "the law reads the joint vector and is unchanged by the partner's local unitaries" (an EXACT equivalence).
8. Split C4 into C4a and C4b. State that calibration needs C4b, include the h = ct counter-model, and say the axiom reading supports C4a at most.
9. Change "no affinity clause" to "no prescribed-weight affinity clause."
10. O4: replace "unsatisfiable" with "vacuous on two sites," and state the scope of the landed theorems precisely.
11. Delete "compression and Born force each other under marginal no-signalling."
12. Theorem 2: use the every-p hypothesis and add the null-set step, or else drop "f(1) = 1 sets c = 1."
13. Credit the landed λ(λ−1) = 0 result; the new content is the extension to non-affine laws.
14. Add the Han–Choi comparison.
15. Narrow summary 6 to the covariant, binary, antipodal case under abundance. Soldered, non-antipodal and larger menus remain open.
16. The brief bans "only"; the report uses it, e.g. "the only regularity used" and "only if" in O2 and O3.

## H. Bottom line

Theorem 1 is correct as mathematics once two one-line repairs are made. It is non-circular in the narrow sense: it prescribes no affinity weights, assumes no repeat certainty and uses no regularity. It is new to the repo, because it settles the deferred nonlinear self-weighted classification of the landed randomizer note for covariant, binary, antipodal laws under continuum abundance. It is not new in kind: Han–Choi (2016) already obtain Born on two qubits from collapse, a shared rule and an ordering condition. Theorem 1 sharpens that by not assuming calibration, allowing a general mixed-state law, and using a marginal condition.

Semantically, it does not lower the Born price from the axiom text; it moves it. The part of C4 the axiom reading supports (menu-to-menu no-signalling) is vacuous when the conditions are records. Even with C1–C3 it leaves h = ct with c free. Everything that tells laws apart sits in supplied pieces: the tensor composite (C1), compression (C2), the reduced-state reading (C3, which is invariance under the partner's local unitaries), the null-option half of C4 (marginal formation-order blindness), and abundance. So "affinity + repeat certainty" is traded for that list, not removed. Theorem 2 holds almost everywhere and needs the every-p upgrade before f(1) = 1 can fix c.

Sources:
- [Han & Choi, arXiv:1307.2026](https://arxiv.org/abs/1307.2026)
- [Han & Choi, PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4789655/)
- [Galley & Masanes, Quantum 2, 104 (2018)](https://quantum-journal.org/papers/q-2018-11-06-104/)
- [Svetlichny, arXiv:quant-ph/9511002](https://arxiv.org/abs/quant-ph/9511002)