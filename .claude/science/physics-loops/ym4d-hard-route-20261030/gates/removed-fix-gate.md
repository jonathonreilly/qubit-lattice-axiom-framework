lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T22:44Z

# Gate: `library/removed-fix.md` (row 136)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), max effort, Mac mini worker, gating a text by OpenAI Codex (row 131), repository at `566b3155c`. Sussman–Alpoge `31a47c543775` `YM4_sketch_500.tex` was fetched once into a scratch folder outside the repository. Its SHA-256 `d7f77d4d…2537d4b6f` matches the hash in `gates/h-walk-fix-gate.md`, so SA line numbers agree with the note's. Balaban was read from `~/ym4d-papers/` (OCR). This is one cross-provider read by hand. It is not an audit and grants no status, and no computation enters any step.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for R9, the erosion assignments, the box backgrounds, WF3–WF7, WF13a and OA7. Tadeusz Balaban for the cut-down/walk comparison of two domain sequences (CMP 99 (389–434), Theorem 3.14) and the same-index box replacement (CMP 109, p. 290). Codex wrote the note and the gates of rows 129 and 132 whose repairs it implements; Claude wrote `o1-decoupled.md`, `h-walk.md` and `wf-room-2.md`.

## Verdicts

**First failing step: none.** I redid every proof the row lists, and each holds as an implication from its named inputs. The note's own scope statement is accurate ("Result", "Where rank 4 stops"): the abstract removed comparison is repaired, and it does not reach WF7's factor e^{-cM/σ_j}.

| Statement | Verdict | What was checked |
|---|---|---|
| 1.1, one-sided agreement | admissible; CORRECT-NO-ADVANCE | row-129 gate Defect 1 example, rebuilt |
| 1.2, mixed ball count | admissible; CORRECT-NO-ADVANCE | row-129 gate Defect 2 obstruction, rebuilt |
| 1.3, old-level box vs step sequence | admissible; ADVANCE | against SA 5615–5618, 9769, 15753–15779, 16165–16167, 9783 (§1) |
| 2, Balaban citations | CORRECT-NO-ADVANCE | CMP 109 p. 290 and CMP 99 pp. 426–427 compare same-index, same-depth operators, as stated |
| (H-seq-sym), (3.3) | correct hypothesis; (3.3) proved | §2 |
| Lemma C1-sym | ADVANCE | §2 |
| Theorem C, (4.4)–(4.7) | ADVANCE (implication) | §3 |
| Theorem D, (5.17)–(5.18) | ADVANCE (implication) | §4 |
| §6, two endpoint radii | CORRECT-NO-ADVANCE | restates row-129 gate Defect 4 repair; arithmetic redone (§5) |
| 7.1, SA table | correct, one wording point (N2) | every row read against SA |
| Lemma G | ADVANCE | §6 |
| Corollary G-D, (7.4), (7.5) | ADVANCE (implication) | §6 |
| 7.3 | CORRECT-NO-ADVANCE | remark; chain rule correct |
| j⁰ point (`gates/h-walk-fix-gate.md` §5 item 3) | not read by the note; first failing step none | §7 |

No defect breaks a statement. Three notes that break nothing are in §8.

## 1. The Section 1 counterexamples

**1.1.** The two sequences are constant layers: Ω_0 = … = Ω_n = 𝕋 in one, and Ω_0 = 𝕋, Ω_1 = ∅ in the other. Both are separated vacuously, and the flat pair (1,0) is regular. Take G a cube whose side lies between the fine and coarse fourth-enlargement sides, 9M_1L^{-n} and 9M_1. Then the one-sided union is empty, the old (H-seq) is vacuous, and the inner families differ. Admissible.

**1.2.** System 1 is constant at top depth. System 0 descends from top depth near c to bare scale in Q through separated layers of total physical width below ρL/(L−1), in top units. So sup_{y∈Q} d_1(y,c) ≤ D_0 independently of depth, while #(𝓑_0 ∩ Q) ≥ c_Q η^{-4}. The min-distance sum therefore diverges as η → 0, while both native ball counts stay fixed. Admissible.

**1.3, redone.**
- *Step sequence.* Ω_q = 𝕋 for q ≤ k and Ω_{k+1} = ∅ is the all-small-field sequence, separated vacuously. The flat pair with zero current is regular at every ceiling.
- *The box map is old-level.* WF13a (SA 16165–16167) "first forms its actual nonlinear averaged datum and then takes the old-level constrained critical box pair of that datum". WF3–WF4 (SA 15753–15779) build that datum with 𝓜^j. The inner background is the background of the tower of □_0, "(first rule) … cut off at depth j" (SA 9769). (1.1) is Definition A's first rule (`assign-adopt.md` §1) with p = k.
- *(1.2) by induction.* Suppose {d_∞(·,R^c) > e_q} ⊂ T_q, so T_q^c ⊂ {d_∞(·,R^c) ≤ e_q}. If d_∞(x,R^c) > e_q + ρξ_q + 𝔐ξ_{q+1}, every point of the aligned 𝔐ξ_{q+1}-cube containing x has d_∞(·,R^c) > e_q + ρξ_q. Since d_∞(·,R^c) is 1-Lipschitz, that cube lies at sup-distance > ρξ_q from T_q^c, so it is in T_{q+1}. Summing the geometric series gives e_j ≤ (ρ+L𝔐)ξ_j/(L−1) ≤ ρξ_j, using L ≥ 3 and ρ = R_1𝔐 ≥ L𝔐 (`assign-adopt.md` (1.0)). Hence z ∈ T_j.
- *Mismatch.* Ω_{j+1} = 𝕋 contains z, and S^{old box}_{j+1} = ∅, so no G ∋ z satisfies (H-seq-sym). By SA 5615–5618, Γ_j excludes bonds with an endpoint in Ω_{j+1}, so the step sequence has no level-j rows at all, while the box has level-j rows throughout T_j. These are two different determining problems at the centre of a flat window. Correct.
- *Scope.* This refutes reading the WF box map as 6(c)'s single-part localisation U_{k,□}. That localisation ("one part on one lattice, with μ = M_1′", SA 9783) is a depth-k problem, and `o1-decoupled.md` §3.4 (its line 275) made exactly that identification. It does not refute WF7, and the note says both.

## 2. (H-seq-sym), (3.3) and C1-sym

**(3.3).** On G the regions agree, so the densities agree. Truncating at the first exit then gives d_0(·,G^c) = d_1(·,G^c) on G, and both vanish off G. So D is one function, the distance to a fixed set, and it is 1-Lipschitz in each native metric. Interface points are assigned to layers consistently, as in `gates/h-walk-fix-gate.md` N(d); this changes nothing.

**C1-sym.** Let κ be a cube of either family with κ^(4) ⊂ G. Then E_G contains κ^♯, of half-side 4L²M_1ξ_κ.
- Membership of κ reads the regions on κ only, so κ is a cube of the other family.
- Every candidate in θ_κ's denominator, present or absent, lies in κ^♭ ⊂ κ^♯. This is N(a)–(b) of the h-walk-fix gate, with N1 applied separately in each sequence to the now-common κ and R_1 ≥ 8L³.
- Cut-downs read Ω_i ∩ κ^(4) (`h-walk.md` Lemma C), and commutators read within κ^(5/2).

So C1 holds in both directions and the two injections are mutually inverse. The sharp hull is a physical set fixed by the cube list, so Definition D gives the same monomial in both systems. This is the row-129 gate's visible repair, carried out. ADVANCE.

## 3. Theorem C

- **(4.8).** W(b) gives rate τ_L/2 in d_𝐁(ω;y,c), the length of a path from y to c meeting X_{κ_1}, …, X_{κ_n}. Lemma P gives #𝖯 ≤ 16 + 64ℓ/ℓ_𝖯, so with ℓ_𝖯 ≥ 256κ̄/τ_L the monomial costs at most e^{16κ̄}e^{τ_Lℓ/4}, leaving β = τ_L/4. The row factor ξ_c cancels against 𝗆^{-1}, and there are N_Lν_1^n walks with ν_1C_W/M_1 ≤ 1/2. Correct.
- **Inner walks.** At j = 0, W(c) says the field reads lie on ∪κ_i^(4) ⊂ G, so ε_ω ≤ ε_P e^{-θ_Pδ_ω}. Cauchy's inequality on the t-disc of radius R_ω = c·a_min/ε_ω ≥ 4 costs Cε_ω/a_min. Identifying system 1's term with T_ω(P(1)) needs single-term covariance under g. W(d) supplies it for every gauge transformation once K is covariant ((I2)), by an algebraic identity that also holds for complex g of bounded condition number where both local inverses exist. The block-constant restriction in `h-walk.md` §2.1 concerns A's G^(2)_V, not K.
- **(4.9).** Pick p ∈ [[ω]] with D(p) = δ_ω. The path meets the cell of p's cube within r_*, or starts in the root cell, and the 1-Lipschitz property gives ℓ_0 ≥ S − 2δ_ω − 2r_*.
  - For δ_ω ≤ S/2: (β/2)ℓ_0 + θ_Pδ_ω ≥ (β/2)(S − 2δ_ω) + θ_Pδ_ω − βr_*. This is linear in δ_ω, so it is at least min(β,θ_P)S/2 − βr_*.
  - For δ_ω ≥ S/2, the pair factor alone gives θ_PS/2.
  - With a ≤ β/2 and θ ≤ min(β,θ_P)/2 this gives (4.4).
- **Outer walks.** The path passes within r_* of G^c, so ℓ_i ≥ S − 2r_*. This gives (4.5) in the native norm and metric. At exterior native pillars only outer walks contribute.
- **(4.6)–(4.7).** The decomposition is exact: H_0^Tf_0 − H_1^Tf_1 = Σ_𝓘[(H_0−H_1)^Tf_0 + H_1^T(f_0−f_1)] + Σ_{𝓑_0∖𝓘}H_0^Tf_0 − Σ_{𝓑_1∖𝓘}H_1^Tf_1.
  - Common-pillar sums use 𝓘 ⊂ 𝓑_0 with K_{0,a}, and 𝓘 ⊂ 𝓑_1 with K_{1,a}; the two are never crossed.
  - The term H_1^T(f_0−f_1) is (O1) in system 1 with w = e^{θD}, which is admissible because D is 1-Lipschitz in d_1 and θ ≤ τ_L/8.
  - On the remainders D_y ≤ 2r_0 + C_L and D_c ≤ D_y + d_i(y,c), which gives (4.12); the native ball count then runs at rate β − θ ≥ a.
  - The curl version goes through D_{U(t)}T_ω(P(t)), which contains the base change.

So row-129 Defect 2 is answered: no sum over 𝓑_0 uses K_{1,a}, and no exterior quantity is measured in the other system's norm. ADVANCE.

## 4. Theorem D

- **(5.3).** This is `wf-room-2.md` (6.1) verbatim, with Z_i = K_{i,A_i} − K_{i,0}. H_i keeps its J-dependence, as the wf-room-2 gate's S1 repair requires.
- **(5.4)–(5.5).** λ_{0i} = (D_iH_i)^T𝓕_i. The anchor identity has two terms, with no double count (row-129 Defect 3.1).
- **(5.7)–(5.10).** (I+T_i^T)μ_i = H_i^T(F′(A_i) − F′(0)) − T_i^Tλ_{0i}, with F′(A) − F′(0) = D^TDA + 𝒩(A). The Neumann series converges since ‖T_i^T‖ ≤ 1/4. (5.10) is the exact identity RK_A^Tλ − K_0^Tλ_0 = RK_A^Tμ + RZ^Tλ_0 + (R−I)K_0^Tλ_0.
- **(5.1).** Write Z(P_0,A_0) − Z(P_1,A_1) = [Z(P_0,A_0) − Z(P_0,A_1)] + [Z(P_0,A_1) − Z(P_1,A_1)]. The second bracket is ∫∂_P∂_AK_{tA_1}[A_1], which is where r_bx_b comes from. F1 is in response form as the row-129 gate wrote it.
- **(5.12)–(5.13).** Since ṽ_1 − v_1 = E_1(P_0v_0 − P_1v_1), the remainder is 𝓡 = P_0T_0^Tv_0 − P_1T_1^Tṽ_1. That is (4.6) with f_0 = Z_0^Tv_0 and f_1 = Z_1^Tṽ_1. On stencils that read only common rows, δf = (Z_0^T − Z_1^T)v_0; the other stencils lie in D ≤ 2r_0 and go to the native tails.
- **(5.15)–(5.16).** Apply P_i to (5.7), subtract, and use (5.12) twice; this is exact. Then ‖A_{1,G}‖_{w→w} ≤ C_LC_Hh_1 ≤ 1/4.
- **(5.17)–(5.18).** Every right-hand term carries h_i or ε_H. B_anc is not small, but it only appears multiplied by h_1. (5.17) follows. (5.18) follows from j_1 = Ad(g)j_{1,g} and the full (5.9), which keeps C_H(1+C_Hα_0) (row-129 Defect 3.2).
- **Zero response.** There T_i = 0, R_i = I and 𝒩_i(0) = 0, so μ_i = 0 and j_i = 0.

ADVANCE.

## 5. Section 6

The two radii a_s and a_t are kept distinct, which is the row-129 Defect 4 repair. The checks:
- On the half ball, |g(ς) − ςg(1)| ≤ sup|g″|/8 ≤ C_f‖B‖²/(4r_B), so the note's constant 4 is generous.
- (9/8)(5/12 + 1/8) = 39/64.
- √m·L^{-2m} ≤ L^{-2}, which is stronger than the printed √2·L^{-2}; also √m·L^{-m} ≤ L^{-1}.
- α_{0,k}/α_{0,j} ≤ √m, under the floor x ≥ max(C_x, e^{2q}, e²) and SA 9767's flow bound.

CORRECT-NO-ADVANCE.

## 6. Section 7

**7.1.** Every row of the table was read against SA, and each is accurate up to N2 below.

**Lemma G.** The induction of §1 works for both rules:
- first rule c_q = ρξ_q + 𝔐ξ_{q+1}; second rule c_q = 2M_1′ξ_{q+1}, since d_∞(Q, T_q^c) ≥ M_1′ξ_{q+1} (`assign-adopt.md`);
- E = {d_∞(·,R^c) > e_n} lies in every T_q;
- κ^(4) ⊂ G puts the centre of κ at depth > e_n + b_*ξ_n, and κ^♯ has half-side ≤ b_*ξ_n, so κ^♯ ⊂ E;
- every native density is ≥ 1/ξ_n and d_∞(·,R^c) is 1-Lipschitz, which gives (7.3).

The joined-meet remark holds because T^a_{min(q,j_a)} ⊃ {d_∞(·,R_a^c) > e^a_{j_a}}. The hypothesis that the meet is separated is needed for the second rule, whose gap M_1′ξ_{q+1} may be below ρξ_q, and the note correctly assumes it. ADVANCE.

**(7.4)–(7.5).** These follow from (7.3) with ξ_n = ξ_j = σ_jξ_k, or with ξ_n = ξ_k. The age-enhanced exponent needs a pair of depth-j systems. A depth-k comparison gives only (7.5). Balaban's CMP 109 p. 290 replacement is of the depth-j kind.

## 7. The j⁰ point

**The note does not read the stage-2 coefficient.**
- Theorem C's H_i is R9's lift 𝖧(s)𝗆^{-1}, the Stage-1 (j = 0) block (`h-walk.md` §7 Stage 1; `o1-decoupled.md` (I-b), gated in row 129). By W(c) at j = 0, each term reads the pair only on ∪κ_i^(4). So the inner class "every κ^(4) ⊂ G" reads the pair only where (H-pair) holds.
- Theorem D uses only H_i, its curl and local row maps.
- In the note, "H_1" denotes system 1's Stage-1 lift, not R9's 𝖧_1.

The coefficient j^(0) enters 𝖧_1(s) and the trees, hence R9's field, and so only through (H-field). Any proof of (H-field) must use the h-walk-fix gate's full-carrier repair: call a tree inner only if F_ω ⊂ G, and use R_h = 16L³M_1 + C_L. That gate's one-layer example (λ centred at 4s, G of half-width just over 4.5s) applies to such a proof verbatim.

## 8. Notes that break nothing

**N1.** (H-field) is stated as "ε_H < ∞". That holds for any two finite-volume fields, so the content is the bound (5.17) in terms of ε_H. Theorem D serves a consumer only once something like ε_H ≤ C_F(h_0 + h_1) is proved, which needs the comparison of R9's 𝖧_1(s), 𝔊(s), C_k and 𝖶_s in §7. Suggested wording, unproved: assume ε_H ≤ C_F(h_0 + h_1) with C_F fixed.

**N2.** Section 1.3 and the 7.1 row for SA 15821–15834 call the box-map estimates hypotheses or assumptions of the window package. The outline does not. SA 15821 asserts them ("obey"), and OA7 (SA 16849–16852) says "We must also prove a compatible boundary comparison and the weighted Hölder response estimates for the actual box backgrounds". They are open obligations. The note's conclusion, that 1.3 does not refute WF7, is unchanged.

**N3.** In (4.9), the sentence about taking "the nonnegative path length" is unnecessary. ℓ_0 ≥ S − 2δ_ω − 2r_* holds whatever its sign, and the βr_* loss follows directly (§3).

## Result

Row 131 is gated, first failing step none:
- C1-sym, Theorem C, Theorem D, Lemma G and Corollary G-D ADVANCE as implications.
- The three counterexamples are admissible.
- The j⁰ comparison is not read.

This does not move WF7's removed factor e^{-cM/σ_j}. The note obtains it only for a pair of depth-j systems ((7.4)), while the WF4 box is depth j and the step response is depth k. Rows 137 and 141 have since shown that no proof goes through WF4's actual pair.

Still open, as the note lists:
- (H-field), which needs the R9 comparison with full tree carriers;
- complex 6(c) for the actual box pair, (H-pair);
- the Landau (H-node) comparison;
- for the age-enhanced exponent, an old-depth composition.
