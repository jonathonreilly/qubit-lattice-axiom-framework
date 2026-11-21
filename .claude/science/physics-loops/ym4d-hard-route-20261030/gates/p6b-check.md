lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T17:46Z

First failing step: none. Under the port's own convention, every result a quoted proof invokes is a named hypothesis, and every step I redid holds given those hypotheses. One such step is open but is labelled as a citation: the stability bound (7) of the torus bound, port lines 3595-3604 (F1).

# p6b-check: library/port/p6-correlation.md, second half (5.1:thm-correlation-theorem, 5.14:thm-one-loop-law)

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, 2026-11-06. Repository commit d9d592ba8. Sources: CA-I, CA-II and CA-III fetched by raw URL at upstream 31a47c543775. CA-II has sha256 6a1f74b05f74...4b2b8f and 145,624 lines, the same file as p6a-check. Balaban CMP 119 was read from the text copy in ~/ym4d-papers, for (2.49)-(2.50) only. One reading, not an audit, not human review. No numerics were run.

Credit: the theorems and proofs checked here are by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Balaban's papers are cited inputs of their proofs. The port is Codex's.

Kind of result: a check of their proofs as ported, and of the port's fills, corrections and input tables. Nothing here is a new proof.

Scope: port lines 460-642 and 681-728 (the two statements), 2645-4020 (the B3 proof passages, fills C-F1 to C-F7, corrections C-C1 to C-C4), 4021-4330 (B4b: inputs, majorants, proof, fills O-F1 to O-F3), and the input tables at 2647-2668 and 4331-4596 where this half reads them.

## Findings (ranked by what each breaks)

None is fatal. F1 matters most for the chain, because it is an open step and not a citation.

- **F1 (B3 (iv); port 3595-3604, CA-II 59804-59813). The stability bound (7), |Z̃(z)| <= e^{E_+^♯ N_side^4} on D, is not derived. The port carries it only as a citation of CMP 119 (2.50).**
  - Step: "Balaban proves the upper member of (2.50) by bounding the moduli of the terms. We follow that proof, with the moduli integrated over the variables V_{K'} by the device for integrating bounds on moduli over these variables. ... Combining this with (4), (a) and the history bound above gives (7)."
  - What is wrong: CMP 119 (2.50) is Balaban's Corollary 3 (ultraviolet stability). It covers the real, unsourced density ρ_k, with E_± depending on g_k. Balaban's own proof is three sentences after (2.49) that refer to Sect. 3 of his [6]. Step (7) is a different statement: a bound on a complex-sourced integral, uniform on D, after the counterterm E is removed. No proof of it is written.
  - "The device for integrating bounds on moduli" occurs nowhere else in CA-I, CA-II or CA-III. The account's later restatement (CA-II 61781-61812) lists five ingredients for this bound. The fifth is "Balaban's proof of the upper bound in (2.50) ... here integrated over V_{K'}". The port's register entry B040 ("B-CMP119: (2.50) | 59804") does not state (7), and neither do the nine C-last hypotheses.
  - Why it matters: (7) is the only source of Q, and later statements read it (CA-II 60734, 61781, 62561, 64174; CA-III 21073, 34455).
  - Repairable: add a named open input, for example C-stability: "(7) on D at fixed (g, m, N_T), with E_+^♯ as built at CA-II 59736-59796", with the source's sketch as its route. Relabel B040 so that it is not read as a published result that a rebuild of CMP 119 would close.
  - Everything after (7) in the torus bound I redid. It holds given (7) and the floor (8).

- **F2 (B3 (i) and the definition of K; port 2731 and 3145, used at 3090). The flow part of the step is restricted to k<K, but K needs the step at k = K.**
  - K is "the largest k such that x_j > X for all j <= k" (CA-II 2041-2042), so x_{K+1} = x_K - b_{K+1}(0) must exist.
  - Two places use |b_{K+1}(0) - β^0_{K+1}| <= λ: the deduction "x_{K+1} <= X gives x_K <= X + b_+" (port 3090), and clause (i)'s second line at k = K. The pure step and the coupling increment derive that bound only "Throughout, k<K".
  - Not fatal. The stated reason, "so that g_j < g for every j <= k", holds for every k <= K. 5.2:def-auxiliary-torus (b) runs the frozen run at every level k <= K+1 (CA-II 24944-24947). Every displayed argument holds verbatim at k = K.
  - Repair (wording): run the pure step, the frozen integral and the coupling increment for every k with x_j > X for all j <= k, that is, for k <= K. Keep k < K for the averaging and large-field steps. The port's C-F3 already uses the step at k = K without saying so.

- **F3 (B3 (ii) and the clause on N_K; port 2689, 3100, 3118). "Real for real ζ" is asserted at each level, but no step derives it for level k+1.**
  - (J_k)(b) asserts it, and the final deduction uses it (h_k'(0) is real, so N_K is real). No passage of the inductive step proves it for (J_{k+1}).
  - Without it the proof gives N_K in the closed disc of radius 1/3 about 1, not in the real interval [2/3, 4/3].
  - Repairable. Take ζ real. The ζ_j with j <= k are real by (J_k), so s_j = 1 - ζ_j g_j^2 is real, and the Gaussian measures and vertices are real. If the input families are real at real fields, then E^{(k+1)}_ζ is real and b_{k+1}(ζ) = β[E^{(k+1)}_ζ] is real. For this, either (J_k) must carry "E^{(j)}_ζ and R^{(j)}_ζ are real at real ζ and real fields", or C-slots and C-frozen must state it.
  - b_{k+1}(0) is real in any case, since it comes from the unsourced real construction, so x_{k+1} is real. Only the dependence on ζ is affected.

- **F4 (B4b hypothesis (a); 5.14:not-flow-notation (d), CA-II 26845-26859; the port's O-flow, line 4023). 5.14 reads clause (i) of 5.1 for every x_0 > g^{-2}, but 5.1 asserts it only when an admissible m exists.**
  - All of 5.1's conclusions (i)-(iv) sit under "every integer m with m_T(g) <= m <= K" (CA-II 2869-2872). For K < m_T(g) that range is empty, so (i) is not asserted.
  - N_T(g,m) >= C_T (log g^{-2})^{r_pr}, so m_T(g) grows without bound as g -> 0. At every fixed s, this touches 5.14's uniformity in g <= γ_J.
  - Not fatal. Clauses (i)-(ii) concern the frozen run, which is performed on T_aux and does not depend on the torus (5.2:def-auxiliary-torus (b), (d)). The proof of (i)-(ii) never uses m.
  - Repair: state (i)-(ii) of 5.1 for every g <= γ_J and x_0 > g^{-2}, outside the quantifiers on m and N_T.

- **F5 (C-F4; port 3429). Wrong supplier for the integral identity.**
  - C-F4 says ∫ρ^w_k dV_k = ∫ρ^w_0 dU is "retained from C-admitted and P1". P1 (p1-base.md) has no averaging-integral identity.
  - The identity is Balaban's kernel normalisation, CMP 119 (3.1), recorded at CA-II 103194-103201 ("Preservation of integrals"). R^♭ is an exact rewriting.
  - Repair: cite CMP 119 (3.1) under C-admitted and drop P1. Cosmetic.

- **F6 (pointers and standings; no effect on any proof).**
  - (a) C-preparation's locus "II:2386 onward" misses both statements. The window-data statement (proof outstanding) is named at CA-II 2376-2378, and the z-free resummation geometry at 2122.
  - (b) Port line 3 and the last line of the Result ("not yet checked by another model") are stale after p6a-check and this check.
  - (c) 5.14's Step 7 gives "e(g') -> 0 ... (hypothesis (a))". This is a property of the formula for e, not of hypothesis (a). O-F1 already supplies it.

## Verdicts

| Statement | Port lines | Verdict |
|---|---|---|
| 5.1:thm-correlation-theorem (B3) | 460-642, 2645-4020 | **ADVANCE as an implication (faithful)**, at fixed (g, m, N_T) as C-C3 states. F1 must be added as a named open input, with the repairs F2, F3 and F5. Clauses (i)-(ii) follow from (J_K) by the arithmetic I redid. Clause (iii) is (J_{K'})(d) with the local-averaging bound and the integral identity. Clause (iv) follows from C-last plus F1's input, C-compact and C-positive. The joint induction itself is C-sites: assumed, not proved. |
| 5.14:thm-one-loop-law (B4b) | 681-728, 4021-4330 | **ADVANCE (faithful).** A closed elementary implication from O-flow, O-Gaussian, O-identification and O-passage. O-Gaussian is cited: CMP 109 (1.22) and Theorem 3, and CMP 116 (2.41); "used here as stated", CA-I 3928-3929. I redid every step. F4 repairs the scope of its supplier, not its proof. |

Confirmed as correct:

- C-C1: the driven-flow lemma needs the bound on the driver over the whole disc. The bound at ζ = 0 is not enough.
- C-C2: s_j lies in D(1, σ_rad), so σ_rad <= σ_0 must be part of the slot admission, as the port says.
- C-C3: E_+^♯ and C_low read (g, m) (CA-II 59772-59779, 59820-59821), so the uniformity holds only at fixed (g, m, N_T).
- C-C4: the compactness proof needs (16), not (a).
- Fills C-F1, C-F2, C-F3, C-F5, C-F6, C-F7, O-F1, O-F2 and O-F3; C-F4 except its supplier (F5).
- The input standings match the source. C-Mfree: "incomplete at (∗)", CA-II 59588. C-sixth: "not written out", 59618-59619. C-rank: "Proof outstanding", 60191. C-one-loop: cited.
- The port is right to add C-Mfree and C-sixth. The chapter uses both (CA-II 59566-59568 and 34693), although the account's own list of inputs (CA-II 60268-60272) names only 5.6:prop-polydisc-holomorphy. That omission is bookkeeping in their text, so under FINISH rule 6 it is not a candidate for an upstream issue.

## Quotation check

Every fenced `latex` block of the port's second half was compared with CA-II by plain text comparison. A script in my scratch folder did the comparison. All 11 blocks are exact copies. The same run covered port line 460 onward, so it also matched the 13 first-half blocks in that range, which agrees with p6a-check.

| Port lines | CA-II lines | Content |
|---|---|---|
| 465-639 | 2791-2966 | 5.1:thm-correlation-theorem statement |
| 686-725 | 27042-27082 | 5.14:thm-one-loop-law statement |
| 2677-2911 | 25243-25478 | joint hypothesis, pure step, frozen integral, frozen averaging, large-field step |
| 2920-3124 | 25480-25685 | 5.2:prf-induction-order and the deduction of clauses (i)-(ii) |
| 3141-3289 | 26531-26680 | 5.3:prf-flow-reference |
| 3331-3425 | 26682-26777 | 5.3:prf-local-averaging |
| 3436-3714 | 59645-59924 | 5.12:prf-torus-bound-proof |
| 3748-3908 | 59926-60087 | 5.12:prop-subsequential-limits and its proof |
| 3927-4015 | 60089-60178 | 5.12:lem-limit-positivity and its proof |
| 4040-4112 | 26967-27040 | 5.14:def-defect-majorants and its proof |
| 4124-4308 | 27120-27305 | proof of 5.14:thm-one-loop-law |

A text comparison checks quotation only. I redid the mathematics by hand, as follows.

## What was redone by hand

**B3, the flow (clauses (i)-(ii)).**

- Pure step: |ζ_k| <= (4/3)|ζ| <= (8/3) r on D(0,2r).
- Frozen averaging: δ <= (1 - 4/L)/10 gives r(δ) = (1 - 10δ)L/2 >= 2, and β_s = 1/4. The bound δ_0 M >= 2κ comes from CMP 116 §2 through δ_0 M > 48κ_1 (CA-II 12340-12346).
- Coupling increment: c_0 = 2λ puts the sum of (k+1-i)c_0 and the k+1-i defects in [λ, 3λ](k+1-i), and |s_i - s_{k+1}| <= 2c_2 widens that interval by 2c_2 on each side. Each consecutive-level ratio x_k/x_{k+1} is 1 + O(g^2) at active levels, so the radius comparison (5.3:eq-flow-reference-5) holds once g is small.
- The final deduction:
  - Cauchy on radii r' -> r about points of the closed disc D(0,r) gives |h_k'| <= 2 d_k(2r), so the total Lipschitz bound is 2/3.
  - Schwarz gives |h_k'(0)| <= d_k(2r).
  - N_K - 1 = Σ_{k<K} h_k'(0).
- The derivative bound (4/3) C_β e_k of clause (ii) on the closed half polydisc is 5.2:lem-polydisc-gradient. With a Möbius map at |a_j| <= 1/2, Σ_j (1 - |a_j|^2)|∂_j g| <= 1. p6a-check checked this lemma.
- D_k(ρ) = φ'_k + φ''_k/ρ (CA-II 2054-2060) decreases in ρ. So clause (b) of (J_k), recorded only at ρ = 2r, gives the bound at every ρ in [r, 2r] on D(0, ρ).
- C-F2: on a prefix with x_k > X, y_j > X - 4c_2 + λ(k-j) >= X/2 + λ(k-j), since X >= γ°^{-2} = 8c_2 + 4.
  - With e = 2E*τ + ϑ (CA-II 1946-1957), ψ(y^{-1/2}) = y^{-1} e(y^{-1/2}) <= C y^{-3/2}(log y)^{p_0}. Here p_0 >= 5r >= 10 is an integer (CA-I 1862-1864), so the exponential term is negligible.
  - h(t) = t^{-3/2}(log t)^{p_0} decreases for log t > 2p_0/3. Integral comparison with t = A e^v gives Σ_u h(A + λu) <= C λ^{-1} A^{-1/2}(log A)^{p_0}.
  - For a = (κ_0 - 4)/2 >= 3/2, Σ_u (A + λu)^{-a} <= C λ^{-1} A^{1-a} = C' λ^{-1} g^{κ_0-6}. This is the theorem's bound on Σ_{k<K} D_k(ρ).
  - The port's extra ceiling X/2 >= e^{2p_0} is needed and right. The source's step ω_k = C_β e_k <= C_β e(y_k^{-1/2}) (CA-II 26552-26553) uses that e is monotone at y_k^{-1/2} >= g_k, and y_k^{-1/2} can exceed γ_J by a factor of up to √2.

**B3, clause (iii).** I redid (5.3:eq-local-averaging-2): |ζ_{k+1}(p)| <= sup|w| (1 + Σ_{j<=k+1} d_{j-1}(2r)) <= (4/3) sup|w|. This uses 0 <= φ_j <= 1, h_y >= 0 and Σ_y h_y = 1, and |w| < r_{k+1} < 2r on W_{k+1}. Also |b_j| <= b_+ + 2r/3, because λ - 2c_2 <= b_j(0) <= b_+.

**B3, the torus bound (clause (iv)).**

- x_{K'} <= X + b_+ + 3λm + 2c_2 follows from (i).
- D = {z : Σ_i |z_i| ||f_i||_♯ < r} on the unit torus (CA-II 679-760), so the source ball is balanced.
- (α): for z in D, s -> h(sz) - 1 is holomorphic on |s| < 1, is 0 at 0, and is bounded by Q + 1. Schwarz gives |h - 1| <= 1/2 on (2Q+2)^{-1} D, so |Log h| <= log 2. Cauchy on the polyradii (1-υ) r/((2Q+2) n ||f_i||_♯) then gives the term log 2 (2Q+2)^n (n/r)^n Π_i ||f_i||_♯. On that ball, log Z = E + log Z̃(0) + Log h, with the branch that is real at 0.
- (β): the source's step "4M t_j (d_j(X) + 3) >= d" is a geometric claim that it does not prove. I read X^{[j]} as X plus one layer of level-j M-cubes and d_j(X) as Balaban's tree length in M-units. Under that reading a crude estimate gives diam X^{[j]} <= M t_j (d_j(X) + 6) <= 4M t_j (d_j(X) + 3), so the claim holds with room. Another reading would change only constants in C_UV. For j <= K' the level-j side N_T L^{K-j} is at least L^{11} M, so (M t_j)^{-4} counts the level-j cubes exactly.
- C-F5: for a_j = M t_j <= d/24, [d/(4a_j) - 3]_+ >= d/(8a_j), and e^{-κd/(32a_j)} <= 5!(32/κ)^5 (a_j/d)^5. The geometric sums give C(1 + d^{-4}).
  - The other scales number at most 1 + log_L^+(24M/(d N_side)), and each contributes at most C(1 + (24/d)^4).
  - With d <= 1 on the unit torus, the total is C d^{-4}(1 + log^+ d^{-1}).
- Subsequential limits:
  - Every point of B_j lies within 3d/4 of supp f_j, so the B_j are at distance >= 3d/2.
  - C^1_{B_j} is a subset of a separable metric space, so it is separable.
  - Diagonal extraction, then C-F6's three-term split. The extension to a distribution remains the assumed second part of C-compact.
  - Symmetry: mixed partials of the holomorphic function log Z near 0 commute.
  - Covariance: O(f)(ι_*U) = O(f∘ι)(U), and Haar measure and the action are invariant under ι_*.
- Positivity: θ(O(f)) = O(θf), conj O(f) = O(conj f), and the expectation is θ-invariant. The moment-cumulant formula over partitions into blocks of size at least 2 applies, and every block has pairwise disjoint compact supports. The limit is taken in a finite sum of finite products.

**B4b.** I redid Steps 0-8 and the majorant definition.

- Step 4: x_i > g^{-2} + λu - 2c_2 >= 6c_2 + 4 + λu for i <= K - u, so g_{K-u} < h̄_u.
- Step 5: the base 4c_2 + 4 + λu >= 4 + λu gives v_{K-u} <= 𝔳_u, as O-F2 says.
- ∫_0^∞ (4 + λt)^{-3/2} dt = 1/λ.
- Step 7: the Cesàro means of 𝔢_u tend to 0.
- Step 8: the closed interval for g_{∞,s}^{-2}; the upper end keeps g_{K_i-s} away from 0.
- e(g') in (5.14:eq-flow-notation-c) equals 2E*τ + ϑ of 5.1:not-coupling-functions.
- c_0 = 11N^2 log L/(12π^2) agrees with g^{-2} = 2N/g_std^2 and β_0 = 11N/3.

Side note on O-passage, not a defect. If x_K <= X, then K - 1 = K_J. Clause (i) of 5.1 at k = K_J, the case F2 repairs, gives x_K >= x_{K-1} - b_+ > X + B^♯ - b_+. So x_K > X whenever B^♯ >= b_+, and O-passage could be derived from 5.1 under that condition. The port keeps O-passage as an input, which is correct.

## Side observation from p6a-check, settled

p6a-check asked whether the third bullet of the 5.2 copy of 5.5:lem-weight (c) is covered: "m for the completed preparation of a live region (Y,m)" (CA-II 13806-13809). The bullet is vacuous.

- After a completed operation R_m, the partition B_m on Z is {Z^{(m)}}, by CMP 122b (1.33), which CA-II cites at 34115-34121. So no stratum of cells other than Z^{(m)} remains on Z, and a completed preparation has no thin strata for the doubled block to cross.
- The bullet also requires t_c = m >= n_0. Every cell of Z then has level m >= n_0, while the case assumes the doubled block holds a point of level <= n_0 - 2 inside X_c.
- So a consumer reading the 5.2 copy reads nothing beyond what the 5.5 proof shows. This rests on the cited CMP 122b (1.33).

Checked line by line by Claude (Mini worker).
