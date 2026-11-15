lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CN1 referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 under PR #10138's method. (The lane brief's generic head says "pass 1"; this lane is the pass-3 referee.) Claude drafted pass 1 (`CN1_OUTLINE.md`). Codex gpt-6.1-terra distilled pass 2 (`CN1.md`). This session wrote neither. This is one check: one line-by-line read of `CN1.md`. It reviews no other review.

**What this file is.** A referee report. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `CN1.md` is not edited. "Referee closure" means a short complete argument for a step the text leaves missing. "[check]" marks a tiny scratch computation in `/tmp/toe-CN1ref/`; it guides and never proves.

**Text read.** `CN1.md` at branch `claude/toe-assembly`, commit `033b892d8` (the last commit that touches it). SHA-256 `218e449ef5ddc16328247695adedfa8eb6d2827b16f53784440b624d32aa5686`. Line numbers below refer to that file.

**Pass-1 source checked.** `CN1_OUTLINE.md` at the same commit, SHA-256 `db536699debc9effeaae029e9e5e3d351a06f5639116b61d56b2afb56cab09da`.

**Other sources read, with commits.** Listed in section 0.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms and working-set entries are read plainly.

**Working-set entries used.** None as premises; see section 0.

---

## 0. Sources read and working set

**This folder, branch `claude/toe-assembly`, commit `033b892d8`.** `CN1.md` lines 1-180 (all). `CN1_OUTLINE.md` lines 1-417 (all). `prior/CN1.md` lines 1-79 (all). `LZ1I.md` lines 5, 11, 15-30, 80-92, 117-119, 154-165, 180-194, 205. `LZ1.md` lines 24, 62-66. `ZM1.md` lines 374-380. `CH1_5UQ.md` lines 1-9, 38-42. `TOE_ASSEMBLY.md` lines 225, 229, 233-235, 248-252, 356, 363, 718-720. `GA15PHI.md` line 5. For format only: `LW1_REFEREE.md` lines 1-80 and `Y2W_DRAFT.md` lines 1-30.

**`origin/main` at `f5af11cd0`**, read with `git show` after `git fetch -q origin main`. The Peierls note, `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md`, lines 5-9, 38-50, 158-180, 427-437, 478-503 and 505-517. The exchange-matrix note, `docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`, lines 15-24 and 66-78. No other branch was read. The audit ledger was not read.

**Working-set entries used.** None as premises of a referee closure. The closures use only the definitions of CN1.md and of `LZ1I.md` line 23, averaging over a compact gauge group, the spectral theorem for commuting unitaries, Grönwall's inequality and elementary real analysis. The owner decisions LZ1-SC (`TOE_ASSEMBLY.md` line 229) and ZM1-INV (line 252) are quoted where CN1.md uses them. Nothing is adopted.

## 1. Verdict table

**Method.** Every proof was re-derived by hand. No `[check]` was run; none was needed. Verdicts: CORRECT; ERROR (a false line, with the fix); INCOMPLETE (a named missing step, with the repair where one exists). "Referee closure" means a short complete argument for a missing step. Item numbers are used in sections 2-6.

**Counts.** 68 items: 62 CORRECT, 2 ERROR, 4 INCOMPLETE. No ERROR or INCOMPLETE item changes the content of a proved result.

| # | Item (CN1 line) | Verdict | Note |
|---|---|---|---|
| 1 | Status line (5) | CORRECT | |
| 2 | Proved list (7) | CORRECT | |
| 3 | GAP summary (9) | CORRECT | Each listed defect is real (items 15-17, 41, 47, 50, 53). |
| 4 | Open by name (11) | CORRECT | H2's content is carried by R2-a and H-TICK. |
| 5 | Provenance (13) | CORRECT | |
| 6 | Definition 1, star flow (17) | CORRECT | |
| 7 | Definition 2, `α = 2q²/W` (18) | CORRECT | `P(c,c) = 1/(3π²c)`, `S(c) = 1/(6π²c)`. |
| 8 | Definition 3, zoom (19) | CORRECT | Matches `TOE_ASSEMBLY.md` line 252. |
| 9 | Definition 4, photon band (20) | CORRECT | |
| 10 | Definition 5, CN1-OBS (21) | CORRECT | Monotone in `κ`; static or quadratic modes give `inf S = 0`. |
| 11 | Definition 6 (22) | CORRECT | |
| 12 | Definition 7 (23) | CORRECT | |
| 13 | CN1-T (27-30) | INCOMPLETE | Domain, static modes, node location. Repair CN1-T′; nonemptiness proved. |
| 14 | CN1-T(r) (31) | INCOMPLETE | Needs `κ`-uniform constants; a linear `κ` term needs `C^{1,1}`. |
| 15 | GAP 2.1 (33) | CORRECT | Real; partly closed (item 13). |
| 16 | GAP 2.2 (35) | CORRECT | Real; the rate is `min(γ,1)`, not `2q²/W`. |
| 17 | GAP 2.3 (37) | CORRECT | Real. |
| 18 | R0 and its GAP (41) | CORRECT | GAP real; closed at level 0; coarse levels under a stated proviso. |
| 19 | R1 paragraph (43) | INCOMPLETE | R1-MOD must state (Sm) and exponential forcing; R1-OBS `κ`-uniform (E3). |
| 20 | R2 (45) | CORRECT | |
| 21 | R3 and R-P (47) | CORRECT | |
| 22 | Hard steps (49) | CORRECT | |
| 23 | Overlap (51) | CORRECT | Add `CH1_5UQ.md` Theorem 2.2 and `LZ1.md` Corollary 2.3. |
| 24 | (OL) and its source (55-63) | CORRECT | Port faithful at `f5af11cd0`; source conditional-support. |
| 25 | Lemma 7 statement (65) | CORRECT | Conditional on the textbook coefficient. |
| 26 | Lemma 7 proof (67) | CORRECT | |
| 27 | Theorem 1 statement (69-78) | CORRECT | |
| 28 | Theorem 1: monotonicity, coupling, existence (80) | CORRECT | |
| 29 | Theorem 1: window contraction, limit (82) | CORRECT | |
| 30 | Explicit bounds for (OL) (84) | CORRECT | |
| 31 | Theorem 2 statement (86-90) | CORRECT | `P ∈ C¹` would suffice. |
| 32 | Theorem 2 proof (92) | CORRECT | Two terse steps filled in. |
| 33 | Power-of-`k` remark (94) | CORRECT | |
| 34 | Consistency checks C1-C4 (96) | ERROR | C1 needs all `q_a² = 1` (E4). |
| 35 | Class `𝓡` (100-107) | CORRECT | |
| 36 | Exchange-symmetry sentence (108) | CORRECT | |
| 37 | Theorem 3 statement (110-114) | CORRECT | Optional E6. |
| 38 | Theorem 3 proof, box (116) | CORRECT | |
| 39 | Theorem 3 proof, windows and rate (118) | CORRECT | Constants supplied. |
| 40 | Theorem 3 proof, pair (120) | CORRECT | |
| 41 | GAP 5.1 (122) | CORRECT | Real in part; convergence for integrable `f` closed. |
| 42 | Proposition 4 statement (124) | CORRECT | |
| 43 | Proposition 4 proof (126) | CORRECT | |
| 44 | Scope sentence (128) | CORRECT | Closures R1-D-a and R1-D-b. |
| 45 | Proposition 5 statement (132-136) | CORRECT | |
| 46 | Proposition 5 proof (138) | CORRECT | Given item 47. |
| 47 | GAP 6.1 (140) | CORRECT | Real; `C₁ > 0` closed for the free continuum. |
| 48 | Lemma 6 statement (142) | CORRECT | State the sign convention; prior forms in `ZM1.md` and `CH1_5UQ.md`. |
| 49 | Lemma 6 proof (144) | CORRECT | |
| 50 | GAP 6.2, H1 (146) | CORRECT | Real; the outline's "H1 fails" is invalid. Optional E12. |
| 51 | Section 7 preamble (150) | CORRECT | |
| 52 | H1 row (154) | CORRECT | |
| 53 | H2 row (155) | CORRECT | Outline's "holds for `L = 2`" corrected. |
| 54 | H3 row (156) | CORRECT | |
| 55 | H4 row (157) | CORRECT | |
| 56 | H5 row (158) | ERROR | Stronger than `LZ1I.md` proves (E8). |
| 57 | H6 row (159) | CORRECT | |
| 58 | H7 row (160) | CORRECT | |
| 59 | R1-MOD attacks (162) | CORRECT | Three distinct attacks with named failing steps. |
| 60 | Four-test preamble (166) | CORRECT | |
| 61 | CN1-OBS row (170) | CORRECT | |
| 62 | R-PH row (171) | INCOMPLETE | Test 1 is C; the Clifford clause may exclude a one-signed photon (E5). |
| 63 | R-SCALE row (172) | CORRECT | |
| 64 | R-THR row (173) | CORRECT | |
| 65 | T2 row (174) | CORRECT | |
| 66 | Readings commentary (176) | CORRECT | |
| 67 | Downstream scope (178) | CORRECT | |
| 68 | Literature and provenance (180) | CORRECT | |

**The distiller's GAPs, ruled.**

| GAP (CN1 line) | Real? | Repair given here |
|---|---|---|
| 2.1 (33) | Yes | CN1-T′; nonemptiness under T1 proved (item 13). |
| 2.2 (35) | Yes | `κ`-uniform CN1-T(r) (item 14); attainable rate `min(γ,1)` (item 16). |
| 2.3 (37) | Yes | None; H-THR stays open. |
| R0 (41) | Yes, as stated | Closed at level 0; coarse levels under a stated proviso (item 18). |
| 5.1 (122) | In part | Comparison constants (item 39); convergence for integrable `f` (item 41); the rate stays open. |
| 6.1 (140) | Yes | `C₁ > 0` closed for the free continuum (item 47); coupling and tick stay open. |
| 6.2 (146) and the H1 row (154) | Yes | CN1.md's wording is right; Lemma 6 is not specific to the framework (item 50). |

## 2. Notes by item

Item numbers refer to the verdict table in section 1. Each note quotes the line it judges.

### 2.1 Status and definitions (CN1 lines 3-23)

**Items 1-5 (lines 5-13).** CORRECT. The status, proved list, GAP summary and provenance lines are accurate summaries of the body. Line 11 lists the open statements; H2 is not in that list, but line 9 says "Continuous time is not established by the zoom", and the content of H2 is carried by R2-a and H-TICK (line 45, 49). No edit is needed beyond the ones in section 4.

**Item 6 (line 17, definition 1).** CORRECT. The general star flow needs `P,R` positive and locally Lipschitz on `(0,∞)^2` and `S` on `(0,∞)`; the line says "positive locally Lipschitz functions", which is that.

**Item 7 (line 18, definition 2).** CORRECT. Check of the stated exponent. From (OL), `P(c,c) = (4+3+1)c^2/(6π^2·c·4c^2) = 1/(3π^2 c)` and `S(c) = 1/(6π^2 c)`. So `P∞/S∞ = 2` and `α = q^2P∞/(WS∞) = 2q^2/W`.

**Item 8 (line 19, definition 3).** CORRECT. `TOE_ASSEMBLY.md` line 252 (ZM1-INV) reads: "Replace the full-algebra map by a unital injective *-homomorphism ... Retain cell covariance. Require exponential locality ... Impose no map on charged fields or Gauss generators. Retain class (a) and \(p=2\) ...". Definition 3 matches it. The clause "one coarse tick per `L` fine ticks" is not in line 252; it is the ZM1 graining convention that R-SCALE (item 63) names.

**Items 9, 11, 12 (lines 20, 22, 23).** CORRECT.

**Item 10 (line 21, definition 5, CN1-OBS).** CORRECT as a proposed definition, with the domain defects that GAP 2.1 names. Two facts sharpen it. (a) Monotonicity: if `κ < κ'` then `W(κ) ⊂ W(κ')`, every observable light at `κ` is light at `κ'`, and `E_A(κ) ⊂ E_A(κ')`. Hence `S_k(κ) ⊂ S_k(κ')` and, where both are defined, `Δ_k(κ) ≤ Δ_k(κ')`. So the limit in κ in CN1-T exists in `[0,∞]` whenever `Δ_k` is defined for small κ. (b) A spectral component on `{λ = 0, K ≠ 0}` (a stationary or flat invariant mode) puts `0` in `E_A(κ)`. Then `inf S_k(κ) = 0` and `Δ_k(κ)` is undefined. A gapless mode with `|λ| ≤ b|K|^2` does the same in the limit `K → 0`. Section 2.2 gives a repaired statement that handles both.

### 2.2 Target and its domain (CN1 lines 25-37)

**Item 13 (lines 27-30, CN1-T).** INCOMPLETE. The statement formalizes W3 faithfully. `TOE_ASSEMBLY.md` line 720: "species that interact through a common gauge field have speed differences that flow to zero". T1 and T2 restrict it, and the restriction is stated. Three things are missing. (a) The domain of `Δ_k` (GAP 2.1). (b) Stationary or sub-linear light modes make `inf S_k(κ) = 0` (item 10(b)). (c) The window `W(κ)` is centred at `K = 0`, but T1 does not put the photon node there. (The bands of R0 do have nodes at zero: `LZ1I.md` line 85, "Each has a node at zero and Clifford speed `v_j=sin θ_j/√3`".)

**Repaired statement CN1-T′ (referee proposal, not adopted).** Keep the law, update, vacuum, zoom, T1 and T2; in T1 the photon band has its node at `K = 0`. For local `A ∈ 𝔄_k^G`, let `ξ_A^s` be the projection of `ξ_A` onto `ker(Ũ_k − 1)^⊥`, and `μ_A^s` its joint spectral measure. Define `E_A(κ)` and `S_k(κ)` as in definition 5 with `μ_A^s` in place of `μ_A`. *Conclusion:* for every `ε > 0` there are `κ₀ > 0` and `k₀` such that for all `κ ∈ (0, κ₀]` and `k ≥ k₀` there is `s > 0` with `∅ ≠ S_k(κ) ⊂ [s, (1+ε)s]`.
- Where `Δ_k(κ)` is defined, `S_k(κ) ⊂ [s,(1+ε)s]` for some `s > 0` exactly when `Δ_k(κ) ≤ ε`. So CN1-T′ is CN1-T on its domain. Outside the domain it is false instead of undefined, which is the right answer for a light stationary or quadratic mode.
- Four tests. (1) P: it restates CN1's own target and fixes no other part's target. (2) P: closed. (3) P: the projection drops only tick-fixed weight, which the owner's LZ1-SC already records as "a separate static class, which LZ1 does not constrain" (`TOE_ASSEMBLY.md` line 229). (4) P: each change has its own reason (domain, static weight, node in the window); no constant is added.

**Referee closure: nonemptiness from T1.** Under T1 (photon band in `H_phys`, node at `K = 0`, `c_k > 0`), `S_k(κ) ≠ ∅` for every `κ ∈ (0,1]`. *Proof.* (i) Local invariants are norm dense in `𝔄^G`: if local `A_n → A ∈ 𝔄^G`, average `A_n` over the compact gauge group of the finitely many sites it touches; the average is local, invariant and within `‖A − A_n‖` of `A`. So `{π(A)Ω : A local invariant}` is dense in `H_phys = closure π(𝔄^G)Ω`. (ii) The band eigenphases are `±c_k|K| + o(|K|)`, so for some `δ > 0` the band image `X` over `0 < |K| ≤ δ` has joint spectrum inside `W(κ)`. `X` is a nonzero closed subspace of `H_phys`, invariant under the tick and translations, and orthogonal to `Ω`: `V(K)` has no eigenvalue `1` for `0 < |K| ≤ δ`, so `X ⊂ ker(Ũ−1)^⊥`, while `Ω` is tick-fixed. By density some local invariant `A` has `P_Xξ_A ≠ 0`. (iii) The band part of `μ_A^s` lives on the graph of the eigenphases, a Lebesgue-null set; every point of its support therefore lies in `ss(μ_A^s)`. So `E_A(κ) ≠ ∅`. □ The same argument gives **local spectral access** for any band in `H_phys ∩ ker(Ũ−1)^⊥` with a node at `0`; it is used for R0 in item 18.

*Remark (not an error).* If `Φ_k` intertwined `α_{k+1}` with `α_k^L` exactly and `ω_{k+1} = ω_k∘Φ_k`, the level-`(k+1)` measure of `A` would be the push-forward of the level-`k` measure of `Φ_k(A)` under `(λ,K) ↦ (Lλ, LK)` mod `2π`. The coarse window would then read the fine window of size `κ/L` plus aliased points. The hard content of CN1-T then sits in alias control (R2-b), as the outline's H-TRANSFER says.

**Item 14 (line 31, CN1-T(r)).** INCOMPLETE; GAP 2.2 is right. By monotonicity (item 10(a)) a bound at one `κ₀` gives `limsup_k Δ_k(κ) ≤ Cκ₀` for `κ ≤ κ₀`, and no more. **Repaired form:** there are `C, γ, κ₀ > 0` with `Δ_k(κ) ≤ C(1+k)^{−γ} + Cκ` for all `κ ∈ (0, κ₀]` and all `k`, with `C, γ` independent of `κ`. Then `limsup_k Δ_k(κ) ≤ Cκ → 0`, so the repaired CN1-T(r) implies CN1-T on its domain. A bound linear in `κ` needs more than `C¹` at the nodes: with `V ∈ C^{1,1}` near a Clifford node the eigenphases are `±v|K| + O(|K|^2)`, which gives `O(κ)`; with `C¹` only one gets `o(1)`.

**Item 15 (line 33, GAP 2.1).** Real. After this report: nonemptiness under T1 is closed (above); positive infimum and boundedness are not implied by T1-T2, and CN1-T′ moves them into the conclusion; the clipping of a cone with `v > 1` is harmless, since points with `|K| ≤ κ/v` remain; several spectral components are harmless, since `S_k` is a union; the `C¹` versus `O(|K|^2)` point is real for the rate form only; aliased branches are real under a zoom and are part of R2-b.

**Item 16 (line 35, GAP 2.2).** Real, and verified. Suppose R1-OBS holds with a constant `C` independent of `κ`. Then `Δ_k(κ) ≤ [D(ℓ_k) + 2C(κ + G_k)]/[m(ℓ_k) − C(κ + G_k)]`, which is at most `C'((1+k)^{−min(γ,1)} + κ)` for small `κ` and large `k`, because `G_k ≤ C/k`. Here `γ` is the exponent of the full spread `D` (photon included) from Theorem 1 or 3, not `2q^2/W`. So the outline's "R1-B gives CN1-T(r) for the truncated flow with `γ = 2q²/W`" (outline lines 135 and 258) is an ERROR of pass 1, which CN1.md has already corrected. The remark that `G_k = O(1/k)` can dominate an exponent above one is right: two unit-charge Weyl species have `W = 1` in Dirac units and `α = 2`.

**Item 17 (line 37, GAP 2.3).** Real, and correctly limited. The step from free thresholds to interacting ones is open (H-THR). The claim that every neutral bound state couples irrelevantly is not proved anywhere in CN1.md, and T2 is only a hypothesis.

### 2.3 Ladder and prior results (CN1 lines 39-51)

**Item 18 (line 41, R0 and its GAP).** CORRECT as a citation; the GAP is real and closable. `LZ1I.md` line 85: "They define orthogonal bands `(8,F_j,V_j)` ... Both band images lie in `ker(Ũ−1)^⊥`. Each has a node at zero and Clifford speed `v_j=sin θ_j/√3`." `LZ1I.md` line 11 lists RC-Z and Theorem 10′ as "Imported referee closures, unrefereed", as CN1.md says. **Referee closure at level 0.** The band vectors are `u_x^j = π(E^x_{j0})Ω` with `E^x_{j0}` local and gauge invariant (`LZ1I.md` line 80). They are orthogonal to the tick-fixed `Ω`, so `ω(E^x_{j0}) = 0` and `ξ_A = u_x^j` for `A = E^x_{j0}`. Each fibre of `u_x^j` has norm one, so `μ_A` puts positive mass on the band graph over every ball `0 < |K| ≤ δ`; by item 13(iii) those points lie in the singular support. Hence `E_{A_j}(κ)` is nonempty and lies within `ε(κ) → 0` of `v_j`. So `S_0(κ)` meets small neighbourhoods of both `v₁` and `v₂`. If `v₁ < v₂`, `ε < (v₂−v₁)/v₁` and `κ` is small, no `s` gives `S_0(κ) ⊂ [s,(1+ε)s]`. At every level that carries both bands in the same way, CN1-T′'s inclusion fails. **At levels `k ≥ 1`.** Theorem 10′ gives coarse zero branches near `±Mw_j(θ/L′)`, with `Mw_j(θ/L′) = (Mv_j/L′)|θ| + O(|θ|^3)`, only "along every ray of" a closed cone `Γ` of directions (`LZ1I.md` line 156). One direction is enough. Access at a coarse level follows if the coarse list vectors of Theorem 10′ lie in the coarse `H_phys`; they do when they are made from coarse invariant operators, the only ones ZM1-INV maps. Proof: `H_phys` is invariant under the spectral projections of `(Ũ, T)`, so the spectral projection `E` onto the part of a coarse branch graph inside `W(κ)` is nonzero on `H_phys`; density gives a local invariant `A` with `Eξ_A ≠ 0`; the graph is Lebesgue-null, so the points it charges lie in `ss(μ_A)`. With only `C^1` the error term is `ε(κ)`, not `Cκ`. R0 is neutral, so it is a counterexample to the universal claim without T2, not to CN1-T; CN1.md says so.

**Item 19 (line 43, R1).** INCOMPLETE (minor). CN1.md's R1-MOD says "(OL+ρ) with the §5 bounds uniformly at all scales". Theorem 3 also needs (Sm) at the starting scale and forcing that is zero or exponential. The outline's Lemma R1-MOD states the forcing bound (outline line 291: "`f(ℓ) + f₁₂(ℓ) ≤ Ke^{−βℓ}`") but not (Sm). **Fix (E3):** state both in R1-MOD. CN1.md's R1-OBS should also say that the constant in `O(κ + G_k)` is independent of `κ` (item 16).

**Item 20 (line 45, R2).** CORRECT. R2-c asks for forcing that decays like `L^{−βk}`; at `ℓ = k log L` this is `e^{−βℓ}`, which is exactly Theorem 3's exponential case.

**Item 21 (line 47, R3 and R-P).** CORRECT.

**Item 22 (line 49, hard steps).** CORRECT. Theorem 3 and the closure of item 41 show that the flow consequences follow once (OL+ρ) holds with `ρ ∈ 𝓡` and (Sm). The remaining content of rung 1 is therefore R1-MOD and R1-OBS, as line 49 says.

**Item 23 (line 51, overlap).** CORRECT against `prior/CN1.md`. One prior result is missing from both the digest and CN1.md. `LZ1.md` line 66 (Corollary 2.3): "For local odd operators with disjoint translated supports, the same pattern decomposition gives vanishing unequal-support two-point functions at all tick times, as in `CH1_5UQ.md` Theorem 2.2". This reaches Lemma 6's conclusion for odd operators by a parity argument. It is listed under Prior work used. The other overlap claims check: the exchange-matrix note says "This proves the exchange-matrix algebra for any positive mutual-drag coefficients. It does not derive the physical one-loop coefficients from framework interactions" (its line 21); the Peierls note's linearized flow (its lines 427-434) is C2 with `κ = e²/(6π²)`; its forcing paragraph (lines 505-517) already says "a permanent marginal source or a new mass threshold is a different problem", which is the distinction Proposition 4 makes precise.

### 2.4 The one-loop input and Theorems 1 and 2 (CN1 lines 53-97)

**Item 24 (lines 55-63, (OL) and its source).** CORRECT. I checked the port against the Peierls note at `origin/main` `f5af11cd0`. The note's gauge action is "S_g = 1/2 integral [sum_i E_i^2 + c^2 sum_{i<j} F_ij^2]" (Euclidean), so its electric weight is `1` and its photon speed is `c`. Its fermion line is "dv/dell = v(A_s-A_t) = e^2(c-v)(4v^2+3vc+c^2)/[6 pi^2 c(v+c)^2]". I re-derived that equality from the note's displayed `A_t = e²(3v²−c²)I₃/(8π²)`, `A_s = e²(c²+v²)c²I₅/(8π²)`, `I₃ = 2/[c(c+v)²]` and `I₅ = 2(2c+v)/[3c³v(c+v)²]`. Then `v(A_s − A_t) = e²[(c²+v²)(2c+v) − 3v(3v²−c²)]/(12π²c(c+v)²)`, and the bracket equals `2(c−v)(4v²+3vc+c²)`. I did not re-derive `I₃`, `I₅` or the Clifford contraction. For `½(εE² − μ^{−1}B²)`, the substitution `A → A/√ε` gives unit electric weight, speed `c` and vertex charge `q_ae/√ε`, so `e² → q_a²G`, as the outline says (its line 196). Status: the note says "Author proposal; actual source status is conditional-support. Independent scientific review is pending." It says its speeds "are not exact charged-particle pole speeds, microscopic signal-front speeds or a proved interacting spectral threshold." CN1.md line 63 reports both facts. The note's shared-speed lines 478-481 ("dr/dell = -g(r-1) H_N(r)/(12 pi^2)", "dg/dell = -N g^2(r+1/r)/(12 pi^2)", "d log c/dell = N g(r^2-1)/(12 pi^2 r)", "H_N(r)=2(4r^2+3r+1)/(r+1)^2+N(r+1), N=N_D") match C1 term by term. Since `v` and `c` are independent there, these lines fix `R(v,c)` and `S(v)` at every positive `(v,c)`. So the note and Lemma 7 give the same photon and coupling lines.

**Item 25 (line 65, Lemma 7).** CORRECT, conditional on the imported Lorentz-invariant coefficient `(q²e²/6π²)·(E²−B²)/2`. That coefficient is the textbook one-loop vacuum polarisation. Neither pass rebuilds it, and CN1.md says so.

**Item 26 (line 67, proof).** CORRECT. Re-derived: under `y = x/v`, `Ã_j = vA_j`, one has `Ẽ = vE`, `B̃ = v²B`, `d³y = v^{−3}d³x`, so `½(Ẽ² − B̃²)d³y = ½(E²/v − vB²)d³x`. Hence `ε' = Σ_b n_bq_b²e²/(6π²v_b)` and `(μ^{−1})' = Σ_b n_bq_b²e²v_b/(6π²)`. Then `(log c)' = ½(μ(μ^{−1})' − ε'/ε) = (G/12π²)Σ_b n_bq_b²(v_b/c² − 1/v_b)`, the `R` line. With `e` fixed, `G' = −G²ε'/e²`, the `S` line. A momentum cutoff `Λ` in `x` becomes `vΛ` in `y`; this shifts `ℓ` by `log v` and leaves `d/dℓ` unchanged.

**Ruling on the ported coefficient and its status.** Theorem 1 uses only positivity and local Lipschitz continuity of `P, R, S`. The form `α = q²P∞/(WS∞)` in Theorem 2 uses no coefficient values. The value `α = 2q²/W` uses `P∞/S∞ = 2`. That ratio rests on the Peierls note (conditional-support, unaudited) and on the textbook coefficient; the two agree on `R` and `S`. C3 adds agreement with outside displays that were not re-checked. So the exponent is conditional exactly as CN1.md line 7 says.

**Theorems 1 and 2.** Every step below was re-derived by hand.

**Item 27 (lines 69-78, Theorem 1).** CORRECT. The constants are finite and positive: `p₋ > 0` because every `q_a ≠ 0`; `R₊ < ∞` and `S₋ > 0` because `B^2` is a compact subset of the open positive quadrant.

**Item 28 (line 80).** CORRECT. (i) Dini rule: for `C^1` functions `f_i` and `F = max_i f_i`, `D^+F(ℓ) ≤ max_{i∈I(ℓ)} f_i'(ℓ)`, where `I(ℓ)` are the maximizing indices; the other indices stay strictly below `F` near `ℓ`. (ii) At a maximizing matter speed `v_a' = Gq_a^2P(c−M) ≤ 0`; at a maximizing photon speed each term of `c'` has `v_b − M ≤ 0`. (iii) A continuous function with `D^+M ≤ 0` everywhere is nonincreasing (the tilt argument of `CN1_OUTLINE.md` line 231, checked). `G` stays positive: `G ≡ 0` with frozen speeds solves the system, so by uniqueness no solution with `G₀ > 0` reaches `G = 0`. Then `(1/G)' = Σ_b n_bq_b^2 S(v_b) ∈ [S₋, S₊]`. On `[0, ℓ*)` the solution stays in `B^{n+1} × [G₀/(1+G₀S₊ℓ*), G₀]`, a compact subset of the open domain. So `ℓ* = ∞`.

**Item 29 (line 82).** CORRECT. Let `M̄, m̄, D̄` be the values at the window start `τ₀`. If `c(τ₀) ≤ M̄ − D̄/2`, then `|dc/dτ| ≤ R₊D̄` keeps `c ≤ K := M̄ − D̄/4` on `[τ₀, τ₀+s₀]`. A matter speed above `K` obeys `d(v_a−K)/dτ ≤ −p₋(v_a−K)`. A matter speed at or below `K` stays there, because `dv_a/dτ < 0` whenever `v_a > K ≥ c`. So `v_a(τ₀+s₀) ≤ K + (D̄/4)e^{−p₋s₀} = M̄ − ηD̄`. Since `η ≤ 1/4`, the photon also ends at most `M̄ − ηD̄`. With `m` nondecreasing, `D(τ₀+s₀) ≤ (1−η)D̄`. The other case is symmetric. Iteration gives `D(τ) ≤ (1−η)^{⌊τ/s₀⌋}D(0) ≤ (1−η)^{−1}D(0)e^{−|log(1−η)|τ/s₀}`. The lower bound on `G` gives `τ(ℓ) ≥ S₊^{−1}log(1+G₀S₊ℓ)`, hence the stated power. `M` decreases, `m` increases and `M − m → 0`, so all speeds have one limit `c∞ ∈ B`.

**Item 30 (line 84).** CORRECT. `4v^2+3vc+c^2 − (v+c)^2 = 3v^2 + vc ≥ 0`, so `P ≥ 1/(6π^2c) ≥ 1/(6π^2M(0))`. `R = (1/v + 1/c)/(12π^2) ≤ 1/(6π^2m(0))`. The `S` bounds are immediate.

**Item 31 (lines 86-90, Theorem 2).** CORRECT. The hypotheses are more than the proof uses: `P ∈ C^1` near `(c∞, c∞)` and `S` Lipschitz near `c∞` suffice. No edit is required.

**Item 32 (line 92).** CORRECT. Two steps are terse; here they are. (a) For every `ℓ`, `c∞ ∈ [m(ℓ), M(ℓ)]`, so every speed is within `D(ℓ)` of `c∞`. This gives `Λ − P∞ = O(D)` and `Σ_b n_bq_b^2S(v_b) − WS∞ = O(D)`. (b) Hence `1/G − WS∞(1+ℓ) = O(1 + ∫₀^ℓ D)`, which is `O((1+ℓ)^{max(1−γ,0)}log(2+ℓ))`. Since `G = O((1+ℓ)^{−1})`, `G − [WS∞(1+ℓ)]^{−1} = O((1+ℓ)^{−1−min(γ,1)}log(2+ℓ))`, which is integrable. Then `Δ(ℓ) = Δ(0)exp(−q^2∫₀^ℓGΛ)` gives the claim with `C = |Δ(0)|e^{−q^2 c₁} > 0` for a finite constant `c₁`.

**Item 33 (line 94).** CORRECT. `(1 + k log L)^{−α}` is not `O(L^{−βk})` for any `β > 0`.

**Item 34 (line 96, C1-C4).** ERROR (minor) in C1; C2-C4 CORRECT. I re-derived C1, C2 and C4 from (OL). Example, C4: `2c'/c + v'/v = G(v−c)[(v+c)^3 − c(4v^2+3vc+c^2)]/(6π^2c^2v(v+c)^2)`, and the bracket is `v^2(v−c)`. C1 is false as written when charges differ: equal speeds do not stay equal, and the factor `2` in `H_W` is `2q^2` with `q^2 = 1`. **Fix:** add "with all `q_a^2 = 1`, so `W = Σ n_a`". For C3, the contraction algebra of the quoted displays checks: with `k̃_{κμ} = η^{λν}(k_F)_{κλμν}` the four `c`-terms give `−η tr c − (c + c^T)`; then `r = 2c − k̃` obeys `μ dr/dμ = (q^2/2π^2) r`, and with `μ dq^2/dμ = q^4/(6π^2)` this gives `r ∝ q^6`, exponent `3`. Whether the quoted displays match the paper is not checked here; C3 is not load-bearing.

**What Theorems 1 and 2 decide.** Global convergence of the `n`-species flow holds for all positive data, with an explicit but not sharp exponent `γ`. The exponent `2q^2/W` is proved sharp only for the difference of two species of equal `q^2` (Theorem 2). For the full spread with unequal charges no sharp exponent is claimed (line 94), and none should be read into "rate `ℓ^{−2q^2/W}`". [Referee remark, not needed by CN1.md: in the linearized star flow (C2), the nonzero decay rates per unit `∫κ` are `2q_a^2` for each charge class with at least two members and one root of `Σ_b n_bq_b^2/(2q_b^2 − μ) = −1` in each gap between consecutive distinct values `2q_b^2` and above the largest; all are at least `2 q_min^2`.]

### 2.5 Remainders, Theorem 3 and Proposition 4 (CN1 lines 100-128)

**Item 35 (lines 100-107, class `𝓡`).** CORRECT as a definition. It matches `CN1_OUTLINE.md` lines 264-267.

**Item 36 (line 108).** CORRECT. Line 108 says: "Exchange symmetry together with a uniform `O(G²)` Lipschitz bound in the two exchanged speed coordinates gives the homogeneous difference form; symmetry alone does not give the bound." Proof. If `ρ₂(v₁,v₂,·) = ρ₁(v₂,v₁,·)` and `ρ₁` has Lipschitz constant at most `KG^2/2` in `(v₁,v₂)` for the `ℓ^1` norm, then `|ρ₁ − ρ₂| = |ρ₁(v₁,v₂,·) − ρ₁(v₂,v₁,·)| ≤ KG^2|Δ|`. The diagonal `{v₁ = v₂}` is invariant under the symmetric flow, so `Δ(0) ≠ 0` gives `Δ ≠ 0` for all `ℓ`, and `ϑ := −(ρ₁−ρ₂)/(G^2Δ)` obeys `|ϑ| ≤ K`. One scope note: with `n₁ ≠ n₂` the exchange is not a symmetry of M1; the hypothesis is then that `ρ_a` is one function of `v_a` and of the shared variables. That is an assumption, as line 108 already implies.

**Item 37 (lines 110-114, Theorem 3).** CORRECT. The pair clauses use the power bound on `D` from the first clause, so they hold under the same hypothesis on `f` (zero or exponential). The sentence order of line 114 says this; an explicit "under the same hypothesis on `f`" would help (edit E6).

**Item 38 (line 116).** CORRECT. Re-derived: `(1/G)' = Σ_b n_bq_b^2S(v_b) − ρ_G/G^2 ≥ S' − KG ≥ S'/2`, `G` decreases, `∫G^2 ≤ 2G₀/S'`, `D' ≤ 2KG^2D + 2f` in the Dini sense, `D ≤ e^a(D(0)+2F)`, and the excursion bound follows from (Sm). The bootstrap needs only the upper end of `B'` (`S` decreases in `v`) and positivity; the estimate gives `M ≤ M(0) + m(0)/2 < 2M(0)` strictly. So the "equality case" sentence is harmless and not needed.

**Item 39 (line 118).** CORRECT. The comparison step, with constants. In `τ` time the perturbed field differs from the homogeneous star field by at most `KGD + f/G`. Let `L_B` be the Lipschitz constant of the homogeneous field on `B'` and `s₀'` the window length built from the constants `p₋', R₊'` of `B'`. Grönwall gives a displacement at most `e^{L_Bs₀'}∫_window(KG^2D + f)dℓ`. The homogeneous barrier step contracts the spread by `1 − η'`. With `max_window D ≤ D_j + 2∫_window(KG^2D+f)dℓ` and `G_j → 0`, this gives `D_{j+1} ≤ (1−η'/2)D_j + C∫_window f dℓ` for late `j`. The rest is as written.

**Item 40 (line 120).** CORRECT. With `|ρ_G/G^2| ≤ KG = O((1+ℓ)^{−1})`, `1/G − WS∞(1+ℓ) = O((1+ℓ)^{max(1−γ',0)}log(2+ℓ))`, so `G − [WS∞(1+ℓ)]^{−1}` stays integrable. Variation of constants: `Δ = Ψ[Δ(0) + ∫₀^ℓ Ψ^{−1}g₁₂]` with `|Ψ^{−1}g₁₂| ≤ C(1+s)^αf₁₂(s)` integrable.

**Item 41 (line 122, GAP 5.1).** Real in part; closed in part. (a) The comparison estimate is supplied by line 118 with the constants of item 39; that part of the gap is closed. (b) The exponent replacement for general `P, R, S` is correct and needed: the outline's (R-iii) weight `2q^2/W` (outline line 267) is the (OL) value of `α`. (c) **Referee closure: convergence for every integrable `f`.** Under (Sm) and any continuous `f ≥ 0` with `∫f < ∞`, the solution is global, stays in `B'`, and all speeds converge to one limit; no rate is claimed. Proof: items 38-39 give `D_{j+1} ≤ (1−η'/2)D_j + ε_j` for `j ≥ j₁`, with `ε_j = C∫_window f` and `Σε_j < ∞`. Then `D_j ≤ (1−η'/2)^{j−j₁}D_{j₁} + Σ_{i=j₁}^{j}(1−η'/2)^{j−i}ε_i → 0`, because `ε_i → 0`. Inside a window `D ≤ D_j + 2∫_window(KG^2D+f)`, so `D(ℓ) → 0`. `M − ∫₀^ℓ(KG^2D+f)` is nonincreasing and bounded below, so `M` converges; likewise `m`. Their limits agree. So GAP 5.1's last sentence is right only for the rate.

**What Theorem 3 decides.** Robustness is proved for remainders that vanish at consensus at order `G^2D`, coupling remainders of order `G^3`, the smallness (Sm), and forcing that is zero or exponentially small in `ℓ`. Lattice terms that decay like `L^{−βk}` are exponentially small in `ℓ = k log L`, so they are covered. Exchange-symmetric `O(G^2)` remainders are covered when the Lipschitz bound of item 36 holds. Robustness is not proved for large `KG₀` or for remainders without the vanishing structure. The outline's summary "the rate survives every exchange-symmetric `O(G²)` remainder and integrable forcing" (outline line 40) overstates both; CN1.md does not repeat it.

**Items 42-43 (lines 124-126, Proposition 4).** CORRECT. In `τ` time, for `τ ≥ τ₁`: `|y(τ)| ≤ |y(τ₁)|e^{−q^2P∞(τ−τ₁)/2} + (2|σ|/(q^2P∞)) sup_{s≥τ₁}|1 − Λ(s)/P∞|`.

**Item 44 (line 128).** CORRECT. Proposition 4 takes `Λ → P∞` as given; a full flow with a persistent source need not reach consensus, so that hypothesis is not automatic. Two referee closures make R1-D a refutation for full flows. **(R1-D-a) Robust form.** If `σ ≠ 0`, `∫₀^∞G = ∞` and `|Λ| ≤ Λ̄` along the solution, then `liminf|Δ| ≥ |σ|/(q^2Λ̄)`. Proof: take `σ > 0` and `b = σ/(q^2Λ̄)`. In `τ` time, wherever `|Δ| < b − δ`, `dΔ/dτ ≥ σ − q^2Λ̄|Δ| > q^2Λ̄δ`. So `Δ` crosses the band `|Δ| < b − δ` upward in finite `τ` and never re-enters it from above. Hence eventually `|Δ| ≥ b − δ`; let `δ → 0`. **(R1-D-b) Explicit full flow.** Fix `(v₁*, v₂*, c*)` positive with `q₁^2 = q₂^2` and `v₁* ≠ v₂*`. Put `ρ_a = Gσ_a`, `ρ₀ = Gσ₀`, `ρ_G = 0`, with `σ_a = −q_a^2P(v_a*,c*)(c*−v_a*)` and `σ₀ = −Σ_b n_bq_b^2R(v_b*,c*)(v_b*−c*)`. Then the speeds stay at `(v*, c*)` for all `ℓ`, `G` solves `G' = −G^2Σ_b n_bq_b^2S(v_b*)`, and `Δ ≡ v₁* − v₂* ≠ 0`. The source is `O(G)` and violates (R-i). So the vanishing-at-consensus structure of `𝓡` cannot be replaced by an `O(G)` bound. As line 128 says, neither closure shows that a tick produces such a source.

### 2.6 The free threshold and local gauge invariance (CN1 lines 130-146)

**Item 45 (lines 132-136, Proposition 5).** CORRECT. The statement is limited to the continuum, the unsmeared current and the positive-energy vacuum, and it says that smearing can remove threshold weight.

**Item 46 (line 138).** CORRECT once GAP 6.1 is closed (item 47). The rest checks. With `ρ^{μν} = (q^μq^ν − q²g^{μν})ρ₁(q²)` and `ρ₁ = C₁θ(q⁰)θ(q²)`, the `00` entry is `λ² − (λ² − |K|²) = |K|²`, so `ρ^{00} = C₁|K|²θ(λ − |K|)`. The density is smooth on each side of the cone and jumps by `C_v|K|² ≠ 0` across it for `K ≠ 0`. Points of the cone with `0 < |K| ≤ min(κ, κ/v)` lie in `W(κ)` and have ratio `v`. So the threshold set is `{v}`.

**Item 47 (line 140, GAP 6.1).** Real, and closable for the free continuum. **Referee closure for `C₁ > 0` (sketch; standard free-field facts, used by nothing else here).** `ρ^{00}` is the spectral density of a vector, so it is a positive measure. It is the two-particle phase-space integral of `|⟨p,s;p',s'|j⁰(0)|Ω⟩|²`. For a massless Dirac field the right-handed part of this amplitude is the overlap of the `σ·p̂ = +1` and `σ·p̂' = −1` spinors; its square is `(1 − p̂·p̂')/2`, which is positive for non-parallel momenta. A positive continuous integrand on an open set gives `C₁ > 0`. The other parts of GAP 6.1 stay open as stated: nonzero coupling, the tick (H-TRANSFER) and smeared local observables.

**Item 48 (line 142, Lemma 6).** CORRECT. It needs one sign convention: "charge `−1` at `x`" means `U_x(θ)ψ_xU_x(θ)^* = e^{−iθ}ψ_x`. The attribution is right: `ZM1.md` Lemma R-GI (line 374) ends "The same holds for a coarse state invariant under every coarse gauge transformation", which is Lemma 6 at one level. `CH1_5UQ.md` Theorem 2.2 (line 38) also contains it.

**Item 49 (line 144).** CORRECT. `α` commutes with `Ad U_x(θ)`, and `ψ_y` has zero charge at `x`, so `Ad U_x(θ)(α^n(ψ_y)) = α^n(ψ_y)`; invariance of `ω` gives `ω(·) = e^{iθ}ω(·)` for all `θ`.

**Item 50 (line 146, GAP 6.2, H1).** CORRECT; the gap is real, and CN1.md's wording is the right one. The decisive point: Lemma 6 holds word for word for Hamiltonian lattice QED with Gauss's law imposed, since its Hamiltonian commutes with every local gauge rotation. That is the setting in which the gauge-fixed speed flow is the standard computation. So Lemma 6 cannot single out the framework tick, and it cannot refute H1 read as a statement about gauge-fixed or dressed variables. What Lemma 6 shows is narrower. The undressed correlator `ω(ψ_x^*α^n(ψ_y))` vanishes for `x ≠ y` at every `n`, so its spatial Fourier transform does not depend on `K` and has no dispersion. The reason is that `α` fixes every `G_x`, so the Gauss defect that `ψ_y` creates stays at `y`. The framework-specific facts concern the interface, not the dynamics: ZM1-INV imposes "no map on charged fields or Gauss generators" (`TOE_ASSEMBLY.md` line 252), and odd bands are flat in the R-loc reading (`LZ1.md` Theorem 2.2). **Ruling on the outline's claim** "On a framework tick the hypothesis that fails is H1" (outline lines 40, 330, 408): ERROR as stated. The correct claim is that H1's flow variable is not supplied as a zoom observable on the framework; a bridge (R1-OBS) or a dressed prescription (R-CS^str) must supply it. CN1.md line 146 states exactly this; it must be kept at freeze.

### 2.7 Mechanism hypotheses and the R1-MOD attacks (CN1 lines 148-162)

**Item 51 (line 150).** CORRECT. The outline says of [CN]: "The paper's text is NOT VERIFIED (not fetched)" (outline line 47). H1-H7 are working hypotheses, as line 150 says.

**Item 52 (line 154, H1).** CORRECT. See item 50: H1's variable is not supplied as a zoom observable; Lemma 6 does not refute it.

**Item 53 (line 155, H2).** CORRECT. The outline's "Holds after translation for `L = 2`" (outline line 323) overstates: the no-folding clause it quotes from `LZ1I.md` Theorem 10′(e) is about the branches of the specified band list, not about the light sector in general. CN1.md's wording is the right one.

**Items 54-55 (lines 156-157, H3, H4).** CORRECT. `LZ1I.md` line 180, Theorem 11: "The difference tends to zero exactly when it starts at zero or the integral diverges." In (OL) the integral `∫G dℓ` diverges (Theorem 1 gives `G ≥ G₀/(1+G₀S₊ℓ)`), so the criterion holds inside the ODE; on the framework it is open, as line 157 says.

**Item 56 (line 158, H5).** ERROR (wording). CN1.md states H5 as "All relevant species couple to the common field" and calls it "False for the specified decoupled neutral bands". `LZ1I.md` proves less. Its line 80 shows the band vectors `u_x^j = π(E^x_{j0})Ω` are in `H_phys ∩ H_even` ("Gauge invariance of the operators puts the vectors in `H_phys`, and link-only support makes them even"), so they carry no Gauss charge. Its line 194 says "The constructed one-excitation bands are exactly decoupled in the tick; no interspecies alignment follows": the two bands do not mix with each other. Nothing there shows that the bands do not couple to a gauge field. They are made of link-register operators, and the frozen sector has no photon band. **Fix (E8):** use the outline's form, "H5: every light species carries the common gauge charge", which fails for these neutral bands; or keep CN1.md's form and replace "False" by "not established: the specified bands are neutral and mutually decoupled (`LZ1I.md` lines 80, 194)". Either way the claim concerns these bands, not neutral species in general.

**Items 57-58 (lines 159-160, H6, H7).** CORRECT. For H7, Proposition 4 and the closures R1-D-a and R1-D-b (item 44) give the consequence of a persistent source in the flow; whether a tick produces one is open.

**Item 59 (line 162, the R1-MOD attacks).** CORRECT as a record. **Ruling on the three attacks.** The three attacks are distinct in method and fail at different named steps. Attack 1 sums an all-orders renormalized expansion; it fails at bounds summable in the order. Attack 2 integrates the Gaussian photon exactly and runs a convergent fermionic tree expansion; it fails at decay of the massless current-current kernel across a scale gap. Attack 3 uses Ward identities and exchange symmetry; it fails at the size estimate. So R1-MOD meets the stopping rule "a lemma on which three distinct attacks failed". Three qualifications. (i) Each attack is a plan with its first failing step named; none is carried to a written partial result. CN1.md's phrase "failed attacks as recorded, not impossibility theorems" is the right strength. (ii) Attack 3 could at most give the vanishing structure of (R-iii), never the size bound; it is distinct but addresses half of R1-MOD. (iii) Attack 3's physics is right: without Lorentz symmetry the Ward identity ties the temporal vertex to `∂Σ/∂p₀` and each spatial vertex to `∂Σ/∂p_j`, which fixes the charge and leaves the speed ratio free. This agrees with the #9913 entry quoted in `TOE_ASSEMBLY.md` line 363: "no symmetry fixes the ratio of two species' dressed speeds". Attack 4 (large `N`) is recorded, not needed for the rule.

### 2.8 Readings, downstream scope and provenance (CN1 lines 164-180)

**Item 60 (line 166).** CORRECT. The four tests are paraphrased faithfully; "(2) is closed rather than open-ended" is test (2) stated positively.

**Item 61 (line 170, CN1-OBS: P P P C).** CORRECT as a record of pass 1's check, which line 166 says it is. My check gives the same result. Test 1: it defines the measured quantity and not the outcome. Test 2: closed (one window, one notion of singular support, one family). Test 3: it decides no downstream question; T2 still needs R-CS. Test 4: conditional; the repair of item 13 adds one projection, which its own reason needs (section 2.2).

**Item 62 (line 171, R-PH: P P P P).** INCOMPLETE. Two points. (a) Test 1 is conditional, not a pass. As hypothesis T1 of CN1-T, R-PH fixes nothing. Read as the meaning of "photon" for GA1, it would fix GA1's target; line 49 assigns H-PHOTON to the framework's photon work. (b) The Clifford-cone clause may exclude the photon that CN1-OBS is built to see. `LZ1I.md` line 23 (quoted in `CN1_OUTLINE.md` line 83) defines a node by "`V(K₀)=1` and `V` is `C¹` nearby" and a Clifford cone by `{N_i,N_j}=2v²δ_ij` with `N_i=∂_i h(K₀)`. Suppose the photon's one-excitation eigenphases near `K = 0` all have one sign, `λ(K) = c|K| + o(|K|)` on both polarizations, as in a Fock-type vacuum. Then `V(K) = e^{−iλ(K)}·1` is not differentiable at `K = 0`, because `|K|` is not. So the photon is not a node and T1 fails, while CN1-OBS still reads a clean cone of speed `c`. Whether the VC1 vacuum has one-signed photon eigenphases is open; this is a conditional defect. **Repair (proposed, not adopted).** In T1 replace "Clifford cone of speed `c_k`" by "a flux-carrying band in `H_phys` whose eigenphases obey `|λ(K)| = c_k|K| + o(|K|)` near `K = 0`". Four tests: (1) P, it is a hypothesis of CN1-T only; (2) P, closed; (3) P, it settles nothing downstream; (4) P, it removes a condition that CN1-OBS does not use and adds none.

**Item 63 (line 172, R-SCALE).** CORRECT. Line 176 already calls it "a comparison convention, not a proof of a continuous RG".

**Item 64 (line 173, R-THR).** CORRECT.

**Item 65 (line 174, T2 as a reading of LZ1).** CORRECT. The two failures match the reasons pass 1 gives (outline line 351).

**Items 66-67 (lines 176-178).** CORRECT. Line 178 says "CN1-T alone supplies none of these bridges"; that is accurate.

**Item 68 (line 180).** CORRECT. CN1.md keeps the literature in the outline and says that no outside paper was fetched in pass 2. No citation in CN1.md is load-bearing.

## 3. The outline against CN1.md (pass-1 source check)

This section answers whether the outline states its target, rungs, imports, proof assignments and hardest step correctly, and whether CN1.md carries them faithfully.

**Target theorem.** The outline's CN1-T (outline lines 99-107) and CN1.md's (lines 27-31) agree, and both formalize W3 faithfully. Both share the domain defects of item 13, which CN1-T′ repairs. The rate form needs constants uniform in `κ` (item 14).

**Rungs.** R0 is correct as a frozen import; its lower bound holds at level 0 (item 18). R1 separates correctly the proved flow statements (R1-A, R1-B, R1-C), the counterexample (R1-D) and the open model statements (R1-MOD, R1-OBS). R2, R3 and R-P name the right open inputs. R-P is right that the infrared-free U(1) gives no power rate: Theorem 2 gives a power of `ℓ = k log L`, and `LZ1I.md` line 188 (Theorem 12) says "a nonzero difference is not `O((a_lat|k|)^p)` for any `p>0`".

**Imports.** Correct, with two remarks. The textbook vacuum-polarisation coefficient is imported and not rebuilt; both passes say so. `CH1_5UQ.md` Theorem 2.2 and `LZ1.md` Corollary 2.3 already contain Lemma 6's conclusion and are not cited (item 23). The citations I checked hold at `033b892d8`, except that `ZM1.md` Lemma R-GI is now at line 374, not 372.

**Proof assignments.** R1-A, R1-B and R1-C are new relative to the prior notes. The Peierls note proves convergence for one shared fermion speed (its line 487: "to a positive common value. This is a theorem of the displayed truncated ODE"); the exchange-matrix note treats constant drag. Lemma 6.1 is not new: the last clause of `ZM1.md` Lemma R-GI ("The same holds for a coarse state invariant under every coarse gauge transformation", line 374) and `CH1_5UQ.md` Theorem 2.2 contain it. The outline credits R-GI, as CN1.md does.

**Hardest step.** H-CONV, the content of R1-MOD, is the right hardest step for rung 1 (item 22).

**Pass-1 errors that CN1.md already corrects.**
- (P1) "R1-B gives CN1-T(r) for the truncated flow with `γ = 2q²/W`" (outline lines 135, 258). The full spread and the `O(G_k)` threshold error cap the rate (item 16).
- (P2) "On a framework tick the hypothesis that fails is H1" (outline lines 40, 330, 408). Lemma 6 holds equally for Hamiltonian lattice QED with Gauss's law (item 50).
- (P3) "H2 holds after translation for `L = 2`" (outline lines 323, 330, 408) (item 53).
- (P4) "R1-A and R1-B survive every remainder in the class `𝓡` (exchange-symmetric `O(G²)` terms, integrable forcing); integrable forcing changes only the constant" (outline line 392; also line 40). The outline's own Theorem R1-C(a) assumes (Sm) and zero or exponential forcing (outline line 275). With merely integrable forcing only convergence holds (item 41).
- (P5) "`C₁ > 0`, because `ρ₁` is dimensionless and the only scale is `q²`" (outline line 306) (item 47).
- (P6) Fact (i), "spectral measure on the graph `λ = ±v|K| + O(|K|²)`" (outline line 95), from a `C¹` node; this needs `C^{1,1}` (item 14).
- (P7) T2's justification, "its photon couplings are multipoles, which are irrelevant" (outline line 101) (item 17).

**Defects that remain in CN1.md.** C1 lacks "unit charges" (item 34). H5 is worded more strongly than `LZ1I.md` proves (item 56). R1-MOD omits (Sm) (item 19). R-PH's test 1 is conditional, and its Clifford clause may exclude a one-signed photon (item 62). The target's domain defects are flagged but not repaired (items 13-14).

## 4. Edits

Each edit names the CN1.md line and the change. "Required" means needed before freeze. "Optional" means the text is correct without it.

**Required.**
- **E1 (after line 33, GAP 2.1; and line 27).** Add a paragraph "**Referee repair CN1-T′ (proposed, not adopted).**" with the statement of item 13, its four-test line and the nonemptiness closure. In T1 (line 27) add "with its node at `K = 0`". The outline's CN1-T stays as the proposed target; only the owner adopts a target.
- **E2 (line 31).** Replace CN1-T(r) by: "There are `C, γ, κ₀ > 0` with `Δ_k(κ) ≤ C(1+k)^{−γ} + Cκ` for all `κ ∈ (0, κ₀]` and all `k`, where `C` and `γ` do not depend on `κ`." Add: "A term linear in `κ` needs `C^{1,1}` regularity at the nodes; `C¹` gives only `o(1)`."
- **E3 (line 43).** In R1-MOD add "with (Sm) at the starting scale and `f + f₁₂ ≤ Ke^{−βℓ}`". In R1-OBS add "with a constant independent of `κ`".
- **E4 (line 96).** In C1, after "With all `v_a=v`", add "and all `q_a²=1` (so `W=Σ n_a`)".
- **E5 (lines 171, 176).** In the R-PH row change test 1 from P to C, with the reason of item 62(a). After line 176 add: "If the photon's eigenphases near `K=0` all have one sign, `V` is not `C¹` at the node, so the photon has no Clifford cone in the sense of `LZ1I.md` line 23. CN1-OBS needs only `|λ|=c|K|+o(|K|)`; a T1 stated that way is the referee's proposed repair."
- **E8 (line 158).** Replace the H5 row by: "| H5 | Every light species carries the common gauge charge | Fails for the specified neutral bands of `LZ1I.md` Theorems 7–9 (in `H_phys`, line 80; mutually decoupled in the tick, line 194); T2 excludes them. Whether those bands couple to a gauge field is not established. |"

**Optional.**
- **E6 (line 114).** "Under (R-iii)" becomes "Under the same hypothesis on `f` and (R-iii)".
- **E7 (line 41).** Replace "It is not a consequence of abstract band transfer alone." by the level-0 closure and the `k ≥ 1` proviso of item 18.
- **E9 (line 122).** Add the convergence closure for every integrable `f` (item 41).
- **E10 (line 128).** Add R1-D-a and R1-D-b (item 44).
- **E11 (line 140).** Add the `C₁ > 0` closure (item 47).
- **E12 (lines 51, 142, 146).** Cite `CH1_5UQ.md` Theorem 2.2 and `LZ1.md` Corollary 2.3 as prior forms of Lemma 6. Quote `LZ1.md` line 24 exactly: "flatness in it does not settle charged sectors or infraparticles".
- **E13 (line 94).** Add the linear star-spectrum remark of section 2.4 ("What Theorems 1 and 2 decide"), labelled as a linear statement.

## 5. Open statements to carry by name

These are CN1.md's open statements (line 11), confirmed by this report. None is closed here. Partial closures are noted.

- **CN1-T** and **CN1-T(r)**: open. Proposed repairs: CN1-T′ (item 13) and the `κ`-uniform rate form (item 14). Under T1, nonemptiness of `S_k(κ)` is now proved (item 13).
- **R1-MOD**: open. Three distinct attacks failed, by name: (1) the all-orders renormalized expansion fails at bounds summable in the order; (2) exact Gaussian photon integration with a convergent fermionic expansion fails at decay of the massless current kernel across a scale gap; (3) Ward identities with exchange symmetry fail at the size estimate (item 59). Sub-lemma **R1″-MOD** and test model **R1′** stay open.
- **R1-OBS** beyond the free continuum: open. At zero coupling in the continuum it is Proposition 5, with `C₁ > 0` now closed (item 47).
- **R2** with **R2-a** (H-TICK), **R2-b** (H-TRANSFER, including alias control), **R2-c**: open.
- **R3** (H-NA), **R-P** (H-RATE), **H-FIN**, **H-PHOTON**, **H-THR**, **H-CONV** (the content of R1-MOD): open.
- Framework inputs: **GA1-P-5** (plaquette class), **GA1-5-Φ** as a cone (T1; see item 62), **VC1**, **ZM1-I1[INV]**, **R-CS**, **MT1-S[R-CS]**, **Y2-W**, **GA2**, **BK1**, **CH1**, and the **graviton bridge** (GR2). H3, H4, H6 and H7 are open framework inputs.
- **Rate for unequal charges**: no sharp nonlinear exponent for the full spread is claimed (line 94); this is a remark, not a carried statement.

## 6. Freeze recommendation

**FREEZE after E1-E5 and E8.** Every proved result in CN1.md is correct within its stated hypotheses: Lemma 7 (conditional on the imported coefficient), Theorems 1-3, Propositions 4-5 (5 with the closure of item 47) and Lemma 6. Each was re-derived by hand. No ERROR or INCOMPLETE item changes the content of a proved result. The two ERROR items are a missing hypothesis in a consistency check (C1) and the wording of one hypothesis row (H5). The four INCOMPLETE items concern the proposed target (CN1-T, CN1-T(r)), the statement of R1-MOD and the reading R-PH; each has a stated repair. CN1.md already corrects the seven pass-1 overstatements of section 3, and the frozen text must keep those corrections, in particular line 146 on H1.

**The decisions the lane brief asks for.**
1. *Global convergence.* Proved for the `n`-species one-loop flow and all positive data (Theorem 1), with an explicit exponent that is not sharp. The exponent `2q²/W` is proved sharp only for the difference of two species of equal `q²` (Theorem 2). Its value depends on the ported coefficients.
2. *Robustness.* Proved under (Sm) for remainders of order `G²D` that vanish at consensus, coupling remainders of order `G³`, and forcing that is zero or exponentially small in `ℓ`. This covers exchange-symmetric `O(G²)` remainders with the Lipschitz bound of item 36, and lattice terms that decay like `L^{−βk}`. For any integrable forcing, convergence holds without a rate (item 41).
3. *R1-D.* Correct. It refutes widening the remainder class to `O(G)` sources, and it extends to full flows (item 44). It does not say whether a tick has such a source.
4. *Lemma 6.1, H1 and H5.* Lemma 6.1 is correct; `ZM1.md` Lemma R-GI (last clause) and `CH1_5UQ.md` Theorem 2.2 already contain it. "H1 fails on a framework tick" is not proved: Lemma 6.1 holds equally for Hamiltonian lattice QED with Gauss's law. The correct statement is CN1.md line 146: H1's variable is not supplied as a zoom observable. "H5 fails for neutral species" is correct for the specified bands in the form "every light species carries the gauge charge"; CN1.md's wording needs E8.
5. *The R1-MOD attacks.* Three distinct attacks, each failing at a named step; R1-MOD is a valid stopping point (item 59).
6. *The ported coefficient.* Faithful to the Peierls note at `origin/main` `f5af11cd0`; status conditional-support, unaudited. The note's own shared-speed lines fix `R` and `S` and agree with Lemma 7 (item 24).
7. *The outline.* Target, rungs, imports, proof assignments and hardest step are stated correctly, apart from the target's domain (items 13-14) and the seven pass-1 overstatements that CN1.md already corrects (section 3).

## 7. Prior work used

Commits: this folder at `033b892d8`; `origin/main` at `f5af11cd0` (read with `git show` after `git fetch -q origin main`). "Peierls note" is `origin/main:docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md`.

| Prior result | Path and lines | Status there | Use here |
|---|---|---|---|
| CN1 digest | `prior/CN1.md` lines 1-79 | digest | Overlap check (item 23) |
| Status and observable caveat | Peierls note lines 7-8, 40-43 | conditional-support, unaudited | Item 24 |
| Gauge action `½∫[ΣE_i² + c²Σ_{i<j}F_ij²]` | Peierls note lines 47-49 | same | Normalization of `G` (item 24) |
| Fermion speed log, with `A_t, A_s, I₃, I₅` | Peierls note lines 158-176 | same | Port check of `P` (item 24) |
| Shared-speed truncated flow and its convergence | Peierls note lines 478-487 | same | C1; fixes `R, S` (items 24, 34) |
| "Higher-loop control remains open" | Peierls note line 503 | same | Scope of R1-MOD |
| Linearized multi-cone flow, multiplicities in Dirac units | Peierls note lines 427-434 | same | C2; Weyl `n_a = 1/2` (items 16, 34) |
| Decaying lattice forcing; "a permanent marginal source ... is a different problem" | Peierls note lines 505-517 | same | Items 23, 44 |
| Exchange-matrix attraction for constant positive drag | `origin/main:docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md` lines 15-24, 66-78 | bounded theorem, unaudited (per the digest) | Item 23 |
| Band, node and Clifford cone | `LZ1I.md` line 23 | frozen 2026-11-06 | Items 10, 62 |
| Theorems 7-9 (neutral bands, node at zero) | `LZ1I.md` lines 80-119 | frozen | Items 13, 18, 56 |
| Theorem 10′ (zoom transfer on a cone of directions) | `LZ1I.md` lines 154-176 | frozen; referee closure, unrefereed (line 11) | Item 18 |
| Theorems 11-12 | `LZ1I.md` lines 180-190 | frozen | Items 33, 55; section 3 |
| A3 ("exactly decoupled in the tick") and S-CONN row | `LZ1I.md` lines 194, 205 | frozen | Items 56, 65 |
| (G1), Theorem 2.2, Corollary 2.3 | `LZ1.md` lines 24, 62, 66 | frozen | Items 23, 50 |
| Lemma R-GI | `ZM1.md` line 374 | frozen | Item 48 |
| Theorem 2.2 (charge decomposition of two-point functions in a gauge-invariant state) | `CH1_5UQ.md` line 38 | frozen 2026-11-06 | Item 23; prior form of Lemma 6 |
| R-CS^str, LZ1-SC, NN-a, ZM1-INV, LZ1(a), #9913 entry, W3 | `TOE_ASSEMBLY.md` lines 225, 229, 235, 252, 356, 363, 720 | owner decisions and assembly text | Items 8, 13, 50, 59 |
| GA1-5-Φ: "not an identified photon or a Clifford cone" | `GA15PHI.md` line 5 | frozen 2026-11-07 | Item 54 |

**Prior work the digest missed, added here.** `CH1_5UQ.md` Theorem 2.2 (line 38): "For a gauge-invariant state, local `A,B` and any integer `n`, `ω(B^*α^n(A))=Σ_q ω(B_q^*α^n(A_q))`. If `S(A)` and `S(B)` are disjoint and all components of `A` have nonzero total charge, this expectation is zero." This contains Lemma 6. `LZ1.md` Corollary 2.3 (line 66) states the same vanishing for local odd operators. The Peierls note's lines 478-481 fix the photon and coupling lines at every `(v, c)`; the digest records that flow but not this use. The outline had already added `ZM1.md` Lemma R-GI, `GA15PHI.md` and `LZ1I.md` Theorem 10′(e).

**Not opened here.** The attractor, seagull, naturalness, Hall, B4, matched-cone and gravity notes on `origin/main`, and the #9913 consolidation note. CN1.md cites them only through the digest or the outline, and no verdict above depends on them.

## FINISH

**Proved here (referee closures; checked by no one else yet).**
- Under T1, `S_k(κ)` is nonempty for every `κ ∈ (0,1]`; more generally, any band in `H_phys ∩ ker(Ũ−1)^⊥` with a node at `K = 0` is seen by some local invariant observable (item 13).
- The R0 lower bound holds at level 0 for the bands of `LZ1I.md` Theorems 7-8, and at coarse levels when the coarse list of Theorem 10′ lies in the coarse `H_phys` (item 18).
- Under (Sm), every speed converges to one limit for every integrable forcing, without a rate (item 41).
- R1-D-a: with a persistent source `σG`, `∫G = ∞` and `|Λ| ≤ Λ̄`, `liminf|Δ| ≥ |σ|/(q²Λ̄)` (item 44).
- `C₁ > 0` for the free massless Dirac current (sketch; item 47).
- Lemma 7, Theorems 1-3, Propositions 4-5 and Lemma 6 re-derived by hand and found correct within their hypotheses; the algebra of C1-C4 and of the ported fermion line re-derived from the Peierls note's displayed integrals.

**Counterexamples.**
- R1-D-b: an explicit full flow, (OL) plus a source `Gσ`, keeps the permanent offset `Δ ≡ v₁* − v₂* ≠ 0` (item 44).
- C1 as written fails when charges differ (item 34).
- A photon whose eigenphases near `K = 0` all have one sign is not a node in the sense of `LZ1I.md` line 23. It fails T1 as written while CN1-OBS reads a clean cone (item 62; whether VC1 is of this kind is open).
- Lemma 6 holds word for word for Hamiltonian lattice QED with Gauss's law. So the outline's inference "Lemma 6.1, hence H1 fails on a framework tick" is invalid (item 50).

**Open by name.** CN1-T (repair CN1-T′ proposed), CN1-T(r) (`κ`-uniform form proposed), R1-MOD (three named failed attacks, item 59), R1″-MOD, R1′, R1-OBS beyond the free continuum, R2 (R2-a, R2-b, R2-c), R3, R-P, H-CONV, H-THR, H-PHOTON, H-TRANSFER, H-TICK, H-NA, H-FIN, H-RATE. Framework inputs: GA1-P-5, GA1-5-Φ as a cone, VC1, ZM1-I1[INV], R-CS, MT1-S[R-CS], Y2-W, GA2, BK1, CH1, the graviton bridge; H3, H4, H6, H7.

**What changes downstream.**
- *CN1.* Freeze after E1-E5 and E8.
- *LZ1.* As CN1.md says: the U(1) mechanism gives a power of the zoom level, so `p ≥ 2` needs R-P.
- *GA1.* If E5's repair is taken, CN1 needs a flux-carrying band with `|λ| = c|K| + o(|K|)`, not a Clifford node. Proposed, not adopted.
- *MT1-S and R-CS.* Lemma 6 removes only undressed charged correlators. Charged speeds must come from a dressed prescription (R-CS^str) or from R1-OBS.
- *ZM1.* R2-b needs control of aliased points in coarse windows. Spectral access itself follows from density whenever the coarse data lie in the coarse `H_phys`.
- *Owner.* Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
