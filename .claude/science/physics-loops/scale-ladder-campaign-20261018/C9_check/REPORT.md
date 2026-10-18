# C9 check: structure functions, the arc lemma and enlarged generator sets

Provenance: a fresh-context checker of the same model family as the C9 worker and the lane-note author, so not independent in model lineage. All code is new and imports nothing from C9 or the lane runner. The checker's REPORT.md write was blocked; the supervisor saved this report from the hand-back.

**Verdict: confirmed, with scope corrections.** Every C9 mathematical claim tested holds. One sign slip in L3 changes no conclusion. Several framing sentences reach wider than what was shown. C9 contradicts none of the lane note's theorems, but the note's Answer bullet and its Reading need the qualifier "with field-independent structure constants" (and "with one generator per momentum").

**Counts: PASS = 66, FAIL = 0.** All checks are exact (sympy, QQ, Q(ω)).

| Script | Route | Result |
|---|---|---|
| `chk_ruler.py` | P6 in two ways: position space with C solved from the frame equation, and Fourier form with a symbolic λ_k | 38/0 |
| `chk_gap.py` | gap form of the arc lemma by exact lex-Gröbner projection | 14/0 |
| `chk_L3L5L8.py` | L3 sign; L5 frame with exact rational C (L = 4, 5); sl2 ⋉ V_{L−1} as affine matrices; necessity by Gröbner; a literal-(S) counterexample | 12/0 |
| `chk_d2.py` | the ruler model's e₁ sector in d = 2 | 2/0 |

The L = 6 L5 run was too slow and was killed; it is not counted.

## (a) L1–L4

- **L1: confirmed.** T-averaging is legitimate. In P6 the C are unique.
- **L2: confirmed, including the + sign.** Non-zero V_e(Φ̄) of distinct momenta are independent (distinct T_* eigenvalues). Missing hypothesis: C differentiable at Φ̄.
- **L3: confirmed, with a sign correction.** For linear vector fields D[V_A, V_B] = −[A, B], so [A_a, A_b] = −c̄(a,b) A_{a+b}. This is harmless, since c → −c preserves (S) and all ratios.
- **Gap form: confirmed.** No step of the note's proof uses that all momenta are present. One implicit step: the class of D is V_2, because ad_E E = 0 makes weight 2 the top weight. Exact projection certificates were computed for Z6∖{3}, Z7∖{3}, Z7∖{4}, Z8∖{4}, Z8∖{3,6} and Z9∖{4,5}, with full Z7 as a control.
- **L4: confirmed.** Closure must hold on a neighbourhood of 0 or on an open cone at 0. B14's G_m is linear in π and φ, so B19 stands under continuous structure functions.

## (b) P6, the ruler model

- **Closure: confirmed.** Exact closure with the stated C (L = 3–7). The Fourier form gives Λ_n = −λ_n and the stated first-order term for any symbol (L = 3–6).
- **Central difference.** Λ_2/Λ_1 = 2cos(2π/L) for all L (exact, L = 3–12). This is positive iff L ≥ 5, and 0 at L = 4. Jac(c̄) = 0 at L = 3 and ≠ 0 for L = 4–9.
- **SLAC.** Λ_n = n̄Λ_1, and Jac(c̄) ≠ 0 at L = 5, 7, 9 and 11.
- **Forward difference.** Λ_1 + Λ_{−1} ≠ 0.
- **Hypotheses.**
  - (P1) holds formally (linear, injective, covariant, T-fixed background).
  - (S) holds only at zeroth order.
  - On Z_L the ruler is not periodic, so P6 is an affine field-space model taken as a definition, not a relabelling of a periodic field. It uses a site central difference, not B14's bond G_m.
  - Uncertified remark: on the ruler, G_m has V_n(0) ∝ ½(1 + ω^{−n}), which is a mixed background at even L.
- **Interpretation.** Λ_n here is minus the symbol of Δ, so "Λ_n ∝ n" reduces to "Δ is SLAC".
- **Asymptotics remark.** The first-order terms are O(k⁴) per unit u_c, or O(k³) per unit Δu, not "O(k³)" as written.

## (c) L5: confirmed

Exact at L = 4 and 5. It is an abstract frame, not a lattice relabelling, and the findings do not claim otherwise.

## (d) L8: confirmed, plus one addition

- **Sufficiency.** sl2 ⋉ V_{L−1} (L = 5, 7, 9) is graded with dim g_{0,±1} = 2 and satisfies (S′). It has Λ_n = n̄Λ_1, and span G is not a subalgebra.
- **Necessity.** The proof is confirmed, and Gröbner at L = 5 agrees, with controls.
- **Addition.** Under literal (S), even 2Λ_n/Λ_1 ∈ Z fails: g = span{D, Z, X_n} with Z central and [X_1, X_{−1}] = Z satisfies Jacobi for any Λ with Λ_{−1} = −Λ_1. Certified at Λ_2 = Λ_1/3, L = 5.

## (e) Framing

- **"Closes within its span is nearly vacuous".** This is correct only when the generators span the configuration tangent space on an open set, and for their cotangent lifts. It is not vacuous in three cases:
  - a proper distribution (Frobenius): in d = 2 on a 3×3 torus, the ruler model's e₁ sector fails to close even with structure functions (rank 3 → 6);
  - phase-space generators not linear in π (C, H_m);
  - restricted C.
- **C9's suggested sharpenings.**
  1. Accurate, with qualifiers: the evasion uses a moved background (where closure is automatic and Λ_n is a free input); the enlargement needs at least two generators at each of 0 and ±1; both are abstract or affine models.
  2. "Help only at moved backgrounds or by discontinuity" is **overstated**. The loopholes from (S) degenerating at linear order and 2 ∉ S remain, and mixed backgrounds are open.
  3. Needs the word "continuous": H1 shows that degree-0 C on {Δφ_x ≠ 0} close.
  4. Theorems A–C are not contradicted: correct.
- **Lane-note sentences (scope, not error).**
  - The Answer bullet needs "with field-independent structure constants (P2)".
  - The Reading needs "with one generator per momentum".

## Proposed lane-note scope paragraph

The supervisor used the checker's proposed wording, with light edits, in the lane note's new §"Scope: structure functions and enlarged generator sets".

## Corrections to C9 FINDINGS (applied by the supervisor)

1. L3 sign. 2. L2 differentiability. 3. L4 neighbourhood/cone. 4. Scope "vacuous" with the d = 2 e₁ counter-case. 5. Sharpening bullet 2 loopholes. 6. Sharpening bullet 3 "continuous". 7. L8 literal-(S) corollary (i) failure. 8. P6 asymptotics and G_m mixed background. 9. P6 is an affine field-space definition on Z_L.

## Not checked

C9's P7 and H1 beyond the remarks above; `F_R7`, which was replaced by an elementary sign argument; the lane note's other theorems.
