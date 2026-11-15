# CONST_T: (CONST-T) — explicit bound on EPS-T's Moser constant C_T

Worker: the (CONST-T) agent of session 24. I own this file and `checks/ct1_*` only. I have written nothing else
anywhere. No git command has been run by me.

---

## 1. PRE-STATED (first edit of this file, 2026-10-28 12:53:33 UTC)

**This section is the very first edit to this file. It contains STATEMENTS ONLY and cites nothing produced in this
session.** Everything below it was written after this section existed on disk.

### 1.1 The task, as I received it

Theorem EPS-T (SQ.md §15.1, l.1458-1509) asserts: fix q > 4; there are ε_* = ε_*(N, q) > 0 and C_T = C_T(N, q) with

  sup_{B_{R/2}}|𝒫| ≤ C_T[ R⁻²||𝒫||_{ℓ²(B_R)} + R^{1-4/q}||𝒮||_{ℓ^q(B_R)} ]

for every SU(N) lattice configuration and embedded cube B_R with ||𝒫||_{ℓ²(B_R)} ≤ ε_* and R^{3-4/q}||𝒮||_{ℓ^q(B_R)} ≤ ε_*.
Its proof is a Moser iteration whose constants are not computed. REVIEW_SQ_S4 §S4-16 pins the downstream consequence:
C_D ≈ (0.5-0.9)·10³·C_T and RLARGE needs C_D ≤ 6.7·10¹⁵, i.e. **C_T ≲ 10¹³**. Nobody has computed C_T.

### 1.2 What I will do

T1. Extract, explicitly, the iteration EPS-T performs: the Caccioppoli/energy inequality (★) with its constant, the
    lattice Sobolev inequality with its constant, the exponent sequence (p_i), the radius sequence (r_i), the cut-off
    cost, and the step inequality. Reconstruct every constant the proof leaves implicit, and say at each point whether
    the value I supply is FORCED by the written proof or a CHOICE I am making.
T2. Evaluate the telescoping product and the radius-power product exactly (rationals / interval arithmetic in plain
    python; no BLAS; no numeric lock).
T3. Carry the two corrections REVIEW_SQ_S4 already found into the iteration: R_0 = 128 (not 64), and e^{100} → 1.6·10⁴.
T4. Carry REVIEW_SQ_S4's hole S4-3 (the added hypothesis sup_{p⊂B_R}||1 - U(p)|| ≤ ¼) explicitly, and record whether it
    changes a constant.
T5. Optimise over the iteration's FREE parameters (the exponent step χ, the radius ratio / the geometric schedule of
    r_i, the cut-off profile, the Young/absorption split δ, and the choice of q > 4), subject to everything else EPS-T's
    proof needs — in particular q > d = 4 and the scale-invariance of both sides.
T6. Report an interval for C_T: a rigorous upper bound if one is obtainable, and separately a best estimate with
    uncertainty; name the single step contributing the most slack.

### 1.3 PRE-REGISTERED verdicts

I register these now, before any derivation or script.

- **PASS (positive result).** A *rigorous* upper bound C_T ≤ X is written out in this file, from EPS-T's stated
  hypotheses plus S4-3's added hypothesis, with X < 10¹³, at some admissible choice of the free parameters (q > 4 and the
  iteration schedule), AND a proof that the iteration still closes at that choice (every absorption inequality used is
  verified at the chosen parameters). In that case the (CLS-min) → RLARGE interface carries a number.
- **FAIL (decisive negative).** A rigorous *lower* bound on the constant that THIS iteration produces, of the form
  C_T ≥ Y with Y > 10¹⁴, together with the identification of the step contributing the dominant factor and a statement
  of what would have to be replaced. In that case the interface does not carry a number as EPS-T is written.
- **PARTIAL (straddle).** The rigorous upper bound exceeds 10¹³ while the best estimate is below it, or the bound is
  below 10¹³ only at a parameter choice I cannot verify closes. I must then name the step with the most slack and the
  work needed to sharpen it. A straddle is reported as a straddle, not rounded to a PASS.
- **NO RESULT.** I cannot reconstruct the iteration well enough to produce any two-sided statement. Reported plainly.

### 1.4 Things I state in advance that I will NOT do

- I will not edit SQ.md, or any file other than this one and `checks/ct1_*`. Requests for SQ's owner go in the final
  "FOR OTHER FILES (not edited)" section.
- I will not change the definition of C_D, C_err, A_0, B_0, G, c_pr, t_pr or ε_1. I take the downstream chain
  (C_T' = 22.6·C_T, A_0 = c_N·C_T'·10.09, G = 2(1.011A_0 + B_0), C_D = max{G, C_r}, C_err = 1.655·10⁷·C_D²,
  C_D ≤ 6.7·10¹⁵) as GIVEN from REVIEW_SQ_S4 §S4-16 and REVIEW_RLARGE_V3 l.286/l.313, and only substitute into it.
- I will not claim PROVEN for a constant obtained by optimising free parameters unless the resulting iteration is also
  shown to close at those parameters.
- If a constant in EPS-T's proof is not determinable from what is written (e.g. WB's C_K, BIA's C_B, the "≤ 200 terms"),
  I will say so, give the value I supply, label it SUPPLIED, and carry its sensitivity through to the final interval
  rather than hiding it in an O(1).

### 1.5 Pre-registered structural expectations (so that agreement is evidence and disagreement is reportable)

Written before computing. These are expectations, not claims.

- E1. The dominant factor in C_T will be the Stage-2 Moser telescope Π_i (C·a^i·β_i^4)^{1/p_i} through its C^{Σ1/p_i} =
  C^{1/2} dependence on the per-step constant C — i.e. C_T will scale like √C with C the one-step energy-inequality
  constant, and the i-dependent and β-dependent parts will contribute a bounded factor of order 10³-10⁴.
- E2. The small-R branch will contribute a factor R_0² = 128² = 16384 that is additive-in-max, not multiplicative, with
  the iteration branch; so C_T ≥ 16384 but 16384 will not be the binding term.
- E3. The free parameter with the most leverage will be the radius schedule (how fast r_i decreases to R/2), because it
  controls both the cut-off cost r⁻² and the number of steps i_*, and hence R_0.
- E4. Raising q above 8 will cost, not save, because the ℓ^q → ℓ² interpolation constants worsen; q = 8 or a little
  lower (but > 4) will be near-optimal.

---

## 2. STEP 1: the iteration EPS-T actually performs, with every constant named

Status of this section: **PROVEN** as an extraction (every line is either quoted from SQ.md §15.1 or an elementary
inequality written out here), **except** that I take (★) itself as given with a symbol C_1. I did **not** re-derive
(★) from steps (2)-(4); the review (S4-4) says those steps are written as inequalities and not expanded, I agree,
and expanding them is a separate job. Everything downstream of (★) is expanded here.

### 2.1 The objects (SQ.md l.1467-1504)

u := 𝒫, ε := ||u||_{ℓ²(B_R)}, k := R^{1-4/q}||𝒮||_{ℓ^q(B_R)}, w := (|u|² + k²)^{1/2}, W := w^{(β+1)/2}.
V := C_V[M_3u + (M_3u)² + |𝒮|²_loc/k²] =: V_c + V_s (l.1480). ζ a cutoff. (★) is l.1487:

  **(★)  Σ|∇(ζW)|² ≤ C_1 β⁴ [ Σ_p V(p)·ζ̃(p)²·W̃(p)² + |∇ζ|²_sup·Σ_{supp⁺}W² ]** ,

ζ̃, W̃ the maxima over N_3(p) (l.1479), supp⁺ the support enlarged by 3 (l.1488).
Lattice Sobolev: SOB (a), **C_S = 3** (l.1453), so ||f||²_{ℓ⁴} ≤ 9Σ|∇f|².
Lattice sup: SOB (c), ||f||_∞ ≤ ||f||_{ℓ^r} for every r (l.1448).

### 2.2 The exponent sequence is FORCED, not a choice

l.1498 takes p_i := 2χ^i with χ = 2. **χ = 2 is forced.** Under x ↦ λx the step
||w||_{ℓ^{p_{i+1}}(B_{r_{i+1}})} ≤ (Cβ^m d_i^{-2})^{1/p_i}||w||_{ℓ^{p_i}(B_{r_i})} scales as
λ^{4/p_{i+1}} on the left and λ^{-2/p_i}·λ^{4/p_i} = λ^{2/p_i} on the right, so 4/p_{i+1} = 2/p_i, i.e.
p_{i+1} = 2p_i. (The same statement in one line: on a d = 4 lattice the Sobolev gain is ℓ² → ℓ^{2*} with
2* = 2d/(d - 2) = 4, which doubles the exponent and nothing else.) **[PROVEN]**

Consequences, all exact (**COMPUTED**, checks/ct1_out.txt Block A, verdict A1 **PASS**):
Σ_{i≥0}1/p_i = 1, Σ_{i≥0}i/p_i = 1, Σ_{i≥0}(i+1)2^{-(i+1)} = 2. In particular the per-step constant enters the
telescope to the power Σ_{i<i_*}1/p_i < 1 — **this is the whole point of Moser and it is why a large one-step
constant is survivable while a large *exponent on it* is not.**

### 2.3 The cut-off and the neighbour-maximum transfer, expanded

The written proof asserts the transfer ("w(p)^α w(p')^γ ≤ w(p)^{α+γ} + w(p')^{α+γ} and ζ(p)² ≤ 2ζ(p')² + 2(6/r)²",
l.1483-1484). Expanded, with a cut-off profile that makes it land inside the right ball:

**Choice (mine; CHOICE, conservative).** For step i put d_i := r_i - r_{i+1} and take ζ_i := the ℓ^∞-linear cut-off
equal to 1 on B_{r_{i+1}}, 0 outside B_{r_i - 6}; then |∇ζ_i| ≤ 2/(d_i - 6) ≤ 4/d_i whenever **d_i ≥ 12**.
(The written proof needs only d_i ≥ 4 (l.1499); d_i ≥ 12 is my choice, and §4.1 prices it.)

**Lemma T (transfer). [PROVEN here]** Define ζ^{++}(x) := max_{N_6(x)}ζ. Then ζ^{++} = 1 on B_{r_{i+1}},
supp ζ^{++} ⊂ B_{r_i}, |∇ζ^{++}| ≤ 4/d_i, and for every s ≥ 1 and every family of maxima over a neighbourhood N,
  **||ζ̃W̃||_{ℓ^s} ≤ |N|^{1/s}·||ζ^{++}W||_{ℓ^s}.**
*Proof.* Let p* ∈ N(p) attain max_{N(p)}W. The point attaining max_{N(p)}ζ lies within the radius of N of p, hence
within twice that radius of p*, so ζ̃(p) ≤ ζ^{++}(p*) and ζ̃(p)W̃(p) ≤ max_{p'∈N(p)}[ζ^{++}(p')W(p')]. Then
Σ_p (max_{N(p)}G)^s ≤ Σ_pΣ_{p'∈N(p)}G(p')^s = |N|·Σ_{p'}G(p')^s. ∎
From here on ζ denotes ζ^{++} and the inequality |∇ζ| ≤ 4/d_i is retained.

**The two multiplicities, counted. [PROVEN]** §15.0 l.1397 defines M_r by the ℓ^∞ distance r of the base point.
- WB's coefficient is M_3η and its support is N_2(p) (l.1432), so V_c's maxima run over
  **|N_3^plaq| = 7⁴·6 = 14406**.
- V_s = C_V|𝒮|²_loc/k² with |𝒮|_loc(p) := max of |𝒮| on the links of N_1(p) (l.1480), and the w-maximum that
  accompanies it in step (3) is w_max over the plaquettes of the link (l.1481), so V_s's maxima run over
  **|N_1^plaq| = 3⁴·6 = 486** and **|N_1^links| = 3⁴·4 = 324**.
This split matters: V_c carries the big multiplicity 14406 but a *small* norm (γ_c ≲ ε_*), while V_s carries the
small multiplicity 486 and an *O(1)* norm. Lumping them at N_3 (which is what l.1479-1480 literally says) costs
(14406/486)^{3/4} ≈ 12.7 in A, i.e. ≈ 160 in C_T at a = 2.

### 2.4 The one step, written out

Fix i; write X := ||ζW||²_{ℓ⁴}, Y := ||ζW||²_{ℓ²}, Σ := Σ_{B_{r_i}}W² = ||w||^{p_i}_{ℓ^{p_i}(B_{r_i})}.
Let σ be the potential's exponent and γ its **scale-invariant** norm, γ := R^{2-4/σ}||V||_{ℓ^σ(B_R)}.

(a) Hölder + Lemma T: Σ_pVζ̃²W̃² ≤ ||V||_σ·||ζ̃W̃||²_{ℓ^{2σ'}} ≤ |N|^{1/σ'}||V||_σ·||ζW||²_{ℓ^{2σ'}},
    σ' = σ/(σ-1), 2σ' = 2σ/(σ-1) < 4 ⟺ σ > 2. **[σ = q/2 > 2 ⟺ q > 4: this is exactly where q > d = 4 is used,
    and it is the same place REVIEW_SQ_S4 S4-5 identifies.]**
(b) Interpolation: 1/(2σ') = (1-ϑ)/2 + ϑ/4 gives **ϑ = 2/σ**, and ||ζW||²_{2σ'} ≤ Y^{1-ϑ}X^{ϑ}.
(c) The extra cut-off terms of l.1483-1484: ζ̃² ≤ 2ζ² + 2(3·4/d_i)² = 2ζ² + 288/d_i², and
    Σ_p V·max_{N}W² ≤ ||V||_∞|N|·Σ. So they multiply the cut-off coefficient 16/d_i² by
    **Q := 1 + 18·||V||_∞·|N|**, and they put a factor 2 on the absorbed term.
(d) With SOB (a) and |∇ζ|² ≤ 16/d_i²:
      **X ≤ P·Y^{1-ϑ}X^{ϑ} + Z,  P := A β⁴ ||V||_σ,  A := 36·C_1·|N|^{1/σ'},  Z := 144 C_1 Q β⁴ d_i^{-2} Σ.**
(e) Young, λ := 1/(2ϑ): P Y^{1-ϑ}X^ϑ ≤ ϑλX + (1-ϑ)λ^{-ϑ/(1-ϑ)}P^{1/(1-ϑ)}Y = ½X + c_ϑ P^{a}Y with
      **a := 1/(1-ϑ) = σ/(σ-2) = q/(q-4)**  and  c_ϑ := (1-ϑ)(2ϑ)^{ϑ/(1-ϑ)} ≤ 1 for ϑ ≤ ½.
    Hence **X ≤ 2P^aY + 2Z**.
(f) *Scale-invariance check (exact).* ||V||_σ = γR^{-2+4/σ} and (-2 + 4/σ)·σ/(σ-2) = -2 identically, so
    **P^a = (Aβ⁴γ)^a·R^{-2}** for every σ > 2. The step is therefore exactly scale-invariant, which is the
    property REVIEW_SQ_S4 S4-5 verified at q = 8; it holds for every q > 4. **[PROVEN]**
(g) d_i ≤ R/2 gives R^{-2} ≤ ¼d_i^{-2}, and β ≥ 1, a ≥ 1 give β⁴ ≤ β^{4a}. With Y ≤ Σ:
      **X ≤ Ĉ·β_i^{4a}·d_i^{-2}·Σ,   Ĉ := ½(Aγ)^a + 288·C_1·Q.**
(h) X ≥ ||w||^{p_i}_{ℓ^{2p_i}(B_{r_{i+1}})}, so taking p_i-th roots:
      **||w||_{ℓ^{p_{i+1}}(B_{r_{i+1}})} ≤ (Ĉ β_i^{4a} d_i^{-2})^{1/p_i}·||w||_{ℓ^{p_i}(B_{r_i})}.**

This is the written step of l.1500 with its constants resolved: the proof's "(C·16^i·β_i⁴)^{1/p_i}(R2^{-i})^{-2/p_i}"
is my (Ĉβ_i^{4a}d_i^{-2})^{1/p_i} with d_i = R2^{-i-4}; the 16^i of l.1500 over-states the schedule's own 4^i
(|∇ζ|² ∝ d_i^{-2} ∝ 4^i), and the proof's β⁴ under-states the Young cost β^{4a} = β^8 at q = 8.

### 2.5 The telescope

With B(m) := Π_{i≥0}β_i^{m/p_i} (β_i = p_i - 1) and the **schedule factor** F := R²·Π_{i<i_*}d_i^{-2/p_i}:

  sup_{B_{R/2}}w ≤ ||w||_{ℓ^{p_{i_*}}(B_{r_{i_*}})}   [SOB (c), B_{R/2} ⊂ B_{r_{i_*}}]
                ≤ Ĉ^{Σ1/p_i}·B(4a)·F·R^{-2}·||w||_{ℓ²(B_{r_0})}  ≤  Ĉ·B(4a)·F·R^{-2}·||w||_{ℓ²(B_R)} ,

using Σ_{i<i_*}1/p_i < 1 and Ĉ ≥ 1. Step (7) of l.1506 (||w||_{ℓ²} ≤ ε + √6kR²) then gives

  **C_T = √6 · F · B(4a) · Ĉ ,  Ĉ = ½(A_sγ_s)^{a} + ½(A_cγ_c)² + 288·C_1·Q ,  a = q/(q-4),**

together with the separate lower bound **C_T ≥ (R_0 - 1)²** from the small-R branch (l.1466). The V_c term keeps
a_c = 2 for every q, because Stage 1 delivers V_c in ℓ⁴ (σ_c = 4 ⟹ ϑ_c = ½ ⟹ a_c = 2) whatever q is.
**[PROVEN, given (★) and the values of C_1, C_V, ε_*.]**

**An exact cancellation worth recording. [PROVEN]** γ_s = C_V·|N_1|^{1/σ}·(1) and A_s = 36C_1|N_1|^{1/σ'} with
1/σ + 1/σ' = 1, so
  **A_sγ_s = 36·C_1·C_V·|N_1^plaq| = 36·C_1·C_V·486 = 1.75·10⁴·C_1·C_V,  independent of q.**
(γ_s: ||V_s||_σ ≤ C_V·|| |𝒮|_loc ||²_{ℓ^{2σ}}/k² ≤ C_V|N_1|^{1/σ}||𝒮||²_{ℓ^q}/k² = C_V|N_1|^{1/σ}R^{-2+8/q}, and
2σ = q, 4/σ = 8/q.) **So q changes C_T only through the exponent a and through B(4a) — nothing else in the
iteration depends on q.** That is the single most useful structural fact I found.

### 2.6 What Stage 1 does and does not contribute

Stage 1 (β = 1, l.1489-1494) is used *only* to make V_c supercritical in Stage 2 (R||V_c||_{ℓ⁴} ≤ C'ε_*,
l.1496). Its own constant therefore lands in **ε_*** — the hypothesis threshold — **and not in C_T**, except
through γ_c ≲ c_c·ε_*. REVIEW_SQ_S4 S4-16's remark that "the θ_ε half is safe by ~30 orders" is about that
threshold and is unaffected by anything here. **[ARGUED; it follows from reading l.1489-1497, which I did.]**

---

## 3. STEP 2: the products, evaluated

All of §3 is **COMPUTED** in checks/ct1_moser.py (pre-registered) and checks/ct1b_moser.py (**post-hoc**, see §6).

### 3.1 The β-telescope B(m) = Π_{i≥0}(p_i - 1)^{m/p_i}

| m | B(m) | the crude bound 2^{2m} used in the review | gain |
|---|---|---|---|
| 4 | **43.95** | 256 | 5.8× |
| 4.17 (q = 100) | **51.45** | 294 | — |
| 8 (q = 8) | **1931.5** | 65536 | 34× |

Verdict A2 **PASS**: the products are increasing in i_* and stay strictly below 2^{2m} for every i_* ≤ 60.
REVIEW_SQ_S4 S4-16's estimate of this factor, "C·e^{ln16·Σ(2i+1)2^{-i-1}} ≈ C·4·10³", is the same object; the
exact value at the proof's own β⁴ is 43.95, and at the Young-corrected β^8 it is 1931.5.

### 3.2 The schedule factor F = R²·Π_{i<i_*}d_i^{-2/p_i}

**Lemma S (the written schedule is the optimal *allocation*). [PROVEN]** For fixed i_* and fixed budget
Σ_{i<i_*}d_i = S, the product Π d_i^{-2/p_i} is minimised at d_i ∝ 2^{-i} (Lagrange on Σλ_i log d_i with
λ_i = 2/p_i = 2^{-i}). SQ.md's d_i = R2^{-i-4} is exactly proportional to λ_i, so **the written geometric
allocation cannot be improved; the lever is the budget and the number of steps, not the shape.**
Numerically confirmed (verdict B4 **PASS**: 2000 random admissible allocations at each i_* ∈ {2,3,4,5}, none beats
the proportional one).

**Lemma S' (the closed form). [PROVEN]** With d_i = D2^{-i}, i < i_*, Λ := Σ_{i<i_*}2^{-i} = 2 - 2^{1-i_*}:
F = R²D^{-Λ}2^{Σ_{i<i_*}i2^{-i}}, and if the budget is exhausted (ΣD2^{-i} = S) and the smallest gap equals the
minimum admissible d_min, then F = (S/d_min-dependent) · 2^{6 - 2^{1-i_*}} ≤ 64 in the case
(S, d_min) = (R/2 - 4, 4·2^{0}) — the deficit 2^{1-i_*} = 4/p_{i_*} is the "R^{4/p_{i_*}}" of l.1504.

| schedule | budget | d_min | max F over admissible R | attained at | R_0 | trivial floor (R_0-1)² |
|---|---|---|---|---|---|---|
| **as written** (l.1498) | R/8 | 4 | **4080** | R = 255 | 128 | 16129 |
| **optimised** (mine) | R/2 - 4 | 12 | **175.8** | R = 79 | 32 | 961 |
| optimised, d_min = 8 | R/2 - 4 | 8 | 128.7 | R = 55 | 24 | 529 |
| optimised, d_min = 4 | R/2 - 4 | 4 | 83.6 | R = 31 | 16 | 225 |

The optimised schedule's asymptote is F → 64.01 as R → ∞, matching Lemma S'. The gain over the written schedule
is **23×** (4080 → 175.8), and up to 49× if the transfer of §2.3 can be run at d_min = 4.

**Three corrections to my own pre-registered criteria, reported as FAILs (§6).** B1, B2 and B3 all failed because
I mis-stated the targets, not because the mathematics differed:
- **B2 FAIL.** I predicted i_* = 1 on R ∈ [64, 128). The truth is **i_* = 0** there, which is *exactly* what
  REVIEW_SQ_S4 S4-6 says ("the iteration performs no step"). My criterion mis-transcribed the review; the review
  is right and is independently reproduced.
- **B1 FAIL.** I predicted the written schedule's max F to be 2048 at R = 128. In fact F grows across each dyadic
  block and peaks at its right edge: max F = **4080 at R = 255** (and, if the scan is allowed below the review's
  fixed R_0 = 128, the trivial branch at R = 127 gives 127² = 16129, which is the 1.6·10⁴ the review quotes).
- **B3 FAIL.** I predicted the optimised schedule's max F < 128. It is **175.8 at R = 79**, for the same
  right-edge reason. The *asymptotic* value is 64.01, below my target, but the maximum is what enters C_T.

### 3.3 The small-R branch is not the binding term

REVIEW_SQ_S4 S4-6 records "C_T ≥ 128² = 16384 from this branch alone". That is correct but **far from binding**:
the iteration branch contributes √6·F·B(4a)·Ĉ with Ĉ ≥ 10⁷ at any plausible parameter point, so the trivial
branch is swamped by ≥ 6 orders. Lowering R_0 from 128 to 32 (possible with the §3.2 schedule) is therefore worth
nothing by itself. **[PROVEN] The 1.6·10⁴ of S4-6 should not be read as the leading contribution to C_T.**

---

## 4. STEP 3: the free parameters — what is forced, what is a choice, and which choice matters

| parameter | status | value | why |
|---|---|---|---|
| exponent step χ | **FORCED** | 2 | scale-invariance of the step; d = 4 Sobolev gain ℓ² → ℓ⁴ (§2.2) |
| gap allocation shape | **FORCED to be optimal already** | d_i ∝ 2^{-i} | Lemma S; SQ.md already uses it |
| radius budget, d_min | **CHOICE** | R/2 - 4, d_min = 12 | §2.3, §3.2; worth 23× over the written R/8 |
| Young parameter λ | **FORCED** once half-absorption is asked | λ = 1/(2ϑ) | §2.4(e) |
| the absorption exponent a | **FORCED given q** | a = q/(q-4) | §2.4(e); ϑ = 2/σ, σ = q/2 |
| **q** | **CHOICE** (SQ.md fixes q := 8 at l.1621) | free, q > 4 | §4.2 — **this is the lever** |
| C_S | FORCED | 3 | SOB (a), l.1453 |
| \|N_1^plaq\|, \|N_3^plaq\| | FORCED | 486, 14406 | §2.3 |
| C_1 (the (★) constant) | **SUPPLIED** | 20 (range 5-100) | not stated in SQ.md |
| C_V (the constant in V) | **SUPPLIED** | 100 (range 20-500) | not stated in SQ.md |
| c_c, ε_* (V_c's norm) | **SUPPLIED** | 50, 10⁻⁴ | ε_* is Stage 1's absorption threshold |

### 4.1 d_min = 12 is a choice I price

The written proof requires only d_i ≥ 4 (l.1499, so that the cut-offs stay inside B_{R-4} and the radius-3 local
operators fit). I took d_i ≥ 12 so that Lemma T's 6-enlargement lands inside B_{r_i} with |∇ζ| ≤ 4/d_i — the
convention (★) itself uses (l.1473). Price: max F rises 83.6 → 175.8, i.e. a factor 2.1 in C_T, and R_0 rises
16 → 32. A sharper transfer lemma recovers that factor 2.1. **[reported as a CHOICE, not forced.]**

### 4.2 q is the lever, and it is a legitimate one

From §2.5: **C_T(q) = √6·F·B(4a)·[½(36C_1C_V·486)^{a} + ½(A_cγ_c)² + 288C_1Q] with a = q/(q-4)**, and
A_sγ_s = 1.75·10⁴C_1C_V is **independent of q**. So raising q does exactly one thing to the iteration: it drives
the exponent a from 2 (at q = 8) down towards 1, and shrinks B(4a) from 1931.5 to ≈ 44.

At the reference point C_1 = 20, C_V = 100, c_c = 50, ε_* = 10⁻⁴, F = 175.8 (checks/ct1b_out.txt):

| q | a = q/(q-4) | B(4a) | C_T | vs 10¹³ |
|---|---|---|---|---|
| 5 | 5.000 | — | 1.9·10⁴⁸ | OVER |
| 6 | 3.000 | — | 7.8·10²⁹ | OVER |
| **8 (SQ.md's choice)** | **2.000** | 1931 | **5.1·10²⁰** | **OVER by 7.7 decades** |
| 12 | 1.500 | 291 | 1.3·10¹⁶ | OVER |
| 16 | 1.333 | 150 | 3.8·10¹⁴ | OVER |
| 24 | 1.200 | 85 | 2.4·10¹³ | OVER (marginally) |
| **32** | **1.143** | 70 | **7.5·10¹²** | **UNDER** |
| 50 | 1.087 | 59 | 2.6·10¹² | UNDER |
| 100 | 1.042 | 51 | 1.2·10¹² | UNDER |
| 400 | 1.010 | 45 | 7.3·10¹¹ | UNDER |

**Is raising q compatible with everything else EPS-T and its consumers need?** I checked each requirement:
- **q > d = 4** ✓ (and σ = q/2 > 2, 2σ' < 4, ϑ = 2/σ ≤ ½, so c_ϑ ≤ 1) — all hold for every q > 4, more
  comfortably as q grows. **[PROVEN]**
- **Scale-invariance of both sides** ✓ exactly, for every σ > 2 (§2.4(f)). REVIEW_SQ_S4 S4-5 verified it at q = 8;
  the identity (-2 + 4/σ)·σ/(σ-2) = -2 shows it is q-free. **[PROVEN]**
- **EPS-0b-avg (l.1608-1613)** holds for every q > 4; its threshold is θ_G = the largest θ with qβ ≤ ½, i.e.
  **θ_G ∝ 1/q**. At q = 8 REVIEW_SQ_S4 S4-14 computes θ_G ≤ 1.46·10⁻¹³; at q = 100 it is ≈ 1.17·10⁻¹⁴ and at
  q = 400 ≈ 2.9·10⁻¹⁵. Since t_pr ≈ θ_0^{SQ4} and the thing it must exceed is ε_1 ≈ 6.7·10⁻⁴⁰, there are
  **≈ 25-26 decades of headroom on that side**: q can be raised by 10²⁵ before θ_G binds. **[ARGUED, from
  S4-14's numbers, which I did not recompute.]**
- **Downstream constants improve with q.** C_T' = 2^{2+4/q}·4C_T falls 22.63C_T → 16C_T; 32^{1/q}C_0 falls
  5.15 → 3.34, so A_0 = c_NC_T'(2.47N√κ_+ + 32^{1/q}C_0) falls from c_N·22.63·10.09·C_T = 228c_N·C_T to
  c_N·16·8.28·C_T = 132c_N·C_T. So raising q buys a further ≈ 1.7× on C_D at fixed C_T. **[COMPUTED from
  l.1513, l.1622-1624.]**
- **ε_* and Stage 1** are unaffected except that Stage 1's own V_s treatment also only needs q > 4 (l.1492-1493).

So **q is a free parameter of EPS-T that the lane happened to fix at 8, it is the parameter C_T is most sensitive
to, and raising it is nearly free.** This is the positive finding the brief asked me to look for.

---

## 5. The two corrections the review already found, and the hole S4-3, carried through

### 5.1 R_0 = 64 → 128 (S4-6): CONFIRMED independently, and non-binding

With i_* = ⌊log₂R⌋ - 6 the iteration performs **zero** steps on R ∈ [64, 128) (checks/ct1_out.txt: i_* = 0 on
[64,127], i_* = 1 from 128). REVIEW_SQ_S4 S4-6 is exactly right and my own pre-registered criterion B2 was wrong
(§3.2). With the §3.2 schedule R_0 can be lowered to 32 (16 if Lemma T is sharpened), but §3.3 shows this branch
never binds. **[PROVEN / COMPUTED]**

### 5.2 e^{100} → 1.6·10⁴ (M4-2): the review's replacement is itself 64× crude; the exact value is 255

l.1504 writes R^{4/p_{i_*}} ≤ R^{256/R} ≤ e^{100}, using the crude p_{i_*} ≥ R/64. The review replaces e^{100} by
sup_{R≥128}R^{256/R} = 128² = 1.6·10⁴. But the **exact** exponent is p_{i_*} = 2^{i_*+1} = 2^{⌊log₂R⌋-5}, so
  sup_{R ≥ 128} R^{4/p_{i_*}} = **255**, attained at R = 255 (where i_* = 1, p_{i_*} = 4),
decaying to 1 for large R. So:
- the right replacement for l.1504's e^{100} is **255**, not 1.6·10⁴ — the review's number double-counts the
  crudeness of p_{i_*} ≥ R/64 at the one R where it is worst;
- the quantity that actually enters C_T is the whole schedule factor F = R²Πd_i^{-2/p_i}, which also carries the
  allocation product Πs_i^{-2/p_i} ( = 16 at i_* = 1): **F ≤ 4080 as written, ≤ 175.8 optimised** (§3.2).
**[PROVEN / COMPUTED]**

### 5.3 S4-3's added hypothesis does not move the dominant constant

Carrying REVIEW_SQ_S4 S4-3's fix — add **sup_{p ⊂ B_R}||1 - U(p)|| ≤ ¼** to EPS-T and derive η ≤ c_N|u| from it
rather than from ||𝒫||_{ℓ²} ≤ ε_* — I checked where it lands in §2:
- BIA's C_B, WB's C_K and §15.0's R_1 bound feed only **V_c** (the M_3u and (M_3u)² terms) and the pointwise
  bound ||V||_∞ in Q. Both are **subdominant**: V_c's contribution is ½(A_cγ_c)² with γ_c ≲ c_cε_* and
  A_cγ_c ≈ 2.4·10²·C_1 at ε_* = 10⁻⁴, and Q's contribution is 288C_1Q ≈ 6.5·10⁶ at q = 100.
- The **dominant** term ½(A_sγ_s)^a is built from 𝒮, k and the N_1 multiplicities only. It never uses η.
So **the hypothesis S4-3 adds is necessary for EPS-T to be proven but changes no factor of C_T that matters.**
It does change ε_* and c_N, which are the places the review already flagged as safe by ~30 decades.
**[ARGUED]** One caveat I will not hide: if the added hypothesis is instead discharged by *shrinking* ε_*
(so that c_Nε_* ≤ ¼ is what gives η ≤ ¼), then ε_* falls and the V_c term falls with it — the verdict only
improves. I found no mechanism by which S4-3 makes C_T worse.

---

## 6. The verdict

### 6.1 The formula (PROVEN, given (★) and the supplied constants)

  **C_T = √6 · F · B(4a) · [ ½(36·C_1·C_V·486)^{a} + ½(A_cγ_c)² + 288·C_1·Q ],  a = q/(q-4),**
  F ≤ 175.8 (optimised schedule) or ≤ 4080 (as written), B(4a) as in §3.1, and separately C_T ≥ (R_0 - 1)².

Everything in it except **C_1**, **C_V**, **c_c** and **ε_*** is forced by the written proof or counted here.
C_1 and C_V are not stated anywhere in SQ.md, and they enter only through their **product C_1·C_V**, raised to
the power a. **Both are ≥ 1 in any expansion of (★) and of step (3)** — C_1 multiplies a bracket that already
contains Σ|∇ζ|²W², C_V multiplies a sum of nonnegative local terms — so C_1C_V ≥ 1 is forced.

### 6.2 At q = 8, the value SQ.md fixes (l.1621): **the threshold is unreachable on this route**

| C_1·C_V | C_T, optimised schedule | C_T, written schedule |
|---|---|---|
| **1 (the forced floor)** | **1.27·10¹⁴** | 2.96·10¹⁵ |
| 10 | 1.27·10¹⁶ | 2.96·10¹⁷ |
| 100 | 1.27·10¹⁸ | 2.95·10¹⁹ |
| 2000 (my reference point, C_1 = 20, C_V = 100) | **5.09·10²⁰** | 1.18·10²² |
| 5·10⁴ | 3.18·10²³ | 7.39·10²⁴ |

q = 8 would need **C_1·C_V ≤ 0.2799** to clear 10¹³, and C_1C_V ≥ 1 is forced. So:

> **At q = 8 this iteration yields C_T ≥ 1.27·10¹⁴ > 10¹³ whatever the local constants turn out to be, i.e. the
> (CLS-min) → RLARGE interface does NOT carry a number as EPS-T is written.** **[PROVEN, conditional only on
> (★) holding with some C_1 ≥ 1 and on C_V ≥ 1; it is a statement about this route's output, not a lower bound on
> the optimal constant in EPS-T's conclusion.]**

My **best estimate** at q = 8 is **C_T ≈ 5·10²⁰**, with the honest interval **[1.3·10¹⁴, 3.2·10²³]** over
C_1 ∈ [1,100], C_V ∈ [1,500]. Seven decades above the threshold at the reference point, one decade above it at
the unattainable floor.

### 6.3 With q raised — a legitimate parameter choice — the threshold is cleared

q_min := the smallest q at which this route clears 10¹³ (optimised schedule, c_c = 50, ε_* = 10⁻⁴):

| C_1·C_V | 1 | 10 | 100 | 1000 | 2000 | 10⁴ | 5·10⁴ |
|---|---|---|---|---|---|---|---|
| **q_min** | 9 | 12 | 16 | 25 | 31 | 132 | none |
| C_T at q_min | 8.5·10¹² | 4.7·10¹² | 7.3·10¹² | 9.5·10¹² | 9.9·10¹² | 1.0·10¹³ | — |

At the reference point (C_1 = 20, C_V = 100) and q = 100: **C_T ≈ 1.2·10¹², interval [6·10¹⁰, 3.3·10¹³]** over
C_1 ∈ [5,100], C_V ∈ [20,500]; the only corner of that range that fails is C_1 = 100 with C_V = 500 (3.3·10¹³).
And at q = 100 the downstream conversion also improves: C_T' falls 22.63C_T → 16C_T and A_0 falls ≈ 1.7×, so the
effective ceiling on C_T rises from ≈ 10¹³ to ≈ 1.7·10¹³.

**Compatibility of the q-raise with everything else EPS-T needs: checked in §4.2 and clean.** The only price is
θ_G ∝ 1/q in EPS-0b-avg, which has ≈ 25 decades of headroom above ε_1.

### 6.4 Status, honestly

- **PROVEN:** the extraction of the iteration (§2, given (★)); χ = 2 forced; the exact scale-invariance for every
  q > 4; Lemma T; Lemma S and S' (the written allocation is optimal, the closed form for F); the telescope
  identities and the exact values of B(m) and max F; the exact cancellation A_sγ_s = 36C_1C_V|N_1|; the exact
  sup R^{4/p_{i_*}} = 255; the conditional negative of §6.2.
- **ARGUED:** the identification of the dominant V_s/V_c split and the multiplicities 486 / 14406; the
  q-compatibility argument of §4.2 (it rests on S4-14's θ_G arithmetic, which I did not recompute).
- **CONDITIONAL:** every *number* for C_T, on the values of C_1 and C_V, which SQ.md does not state. The
  conditional negative at q = 8 is the one statement that survives every value of them.
- **OPEN:** (★) itself with an explicit C_1 — i.e. steps (2)-(4) of l.1471-1487 expanded. That is now the only
  thing standing between this file and an explicit C_T. Likewise C_V from step (3) (l.1476-1484).
- **NOT DONE:** I did not expand (★). I did not recompute θ_G, τ_R, t_pr or C_err. I did not touch SQ.md.

### 6.5 The single step contributing the most slack

**The Young absorption of the supercritical potential, §2.4(e).** It raises the *entire* one-step constant
A_sγ_s = 36·C_1·C_V·486 to the power a = q/(q-4), which at q = 8 is a **squaring**: at the reference point that
one exponent costs a factor 3.5·10⁷. Everything else is small by comparison:

| source of slack | factor available |
|---|---|
| **the exponent a = q/(q-4), q: 8 → ≳30** | **10⁴ - 10⁸** (depends on C_1C_V) |
| B(4a): 1931 → 44 (comes free with the q-raise, or from a β² Caccioppoli in (★)) | 44 |
| the radius schedule, R/8 → R/2 - 4 (§3.2) | 23 |
| pairing V_c with N_3 and V_s with N_1 instead of lumping both at N_3 (§2.3) | 160 at a = 2 |
| Lemma T at d_min = 4 instead of 12 (§4.1) | 2.1 |
| using B(m) instead of the crude 2^{2m} | 34 at m = 8 |

If q must stay at 8, the one remaining lever large enough to matter is sharpening (★) from β⁴ to β² (the standard
d = 4 Moser Caccioppoli carries one β², not two): that replaces B(8) = 1931 by B(4) = 44 and clears the threshold
**only at the floor** (1.27·10¹⁴ → 2.9·10¹²), not at the reference point (5.1·10²⁰ → 1.2·10¹⁹). **Raising q is
the only lever that clears the threshold across the plausible range of C_1C_V.**

---

## 7. Checks: what was run, and the three pre-registered FAILs

Criteria: `checks/ct1_criteria.md`, written before any script. Scripts: `checks/ct1_moser.py` (pre-registered),
`checks/ct1b_moser.py` and `checks/ct1c_floor.py` (**both post-hoc**, written after reading ct1_out.txt and
ct1b_out.txt respectively, and labelled as such in their headers). All three are plain python, single thread, no
BLAS, no numeric lock taken (total runtime 0.6 s); outputs in `ct1_out.txt`, `ct1b_out.txt`, `ct1c_out.txt`.

| verdict | result | what it means |
|---|---|---|
| A1 (series identities) | **PASS** | Σ1/p_i = 1, Σ(i+1)2^{-(i+1)} = 2 |
| A2 (β-products below 2^{2m}) | **PASS** | B(m) < 2^{2m} for all i_* ≤ 60, m ∈ {2,4,8} |
| B1 (written-schedule max F = 2048 at R = 128) | **FAIL** | the max is **4080 at R = 255**; F peaks at the right edge of each dyadic block, which my criterion got wrong. The mathematics is unaffected; the number used in §3.2 and §6 is the corrected 4080 |
| B2 (written i_* = 1 on [64,128)) | **FAIL** | i_* = **0** there. My criterion mis-transcribed REVIEW_SQ_S4 S4-6; **the review is right** and is independently reproduced |
| B3 (optimised max F < 128) | **FAIL** | the max is **175.8 at R = 79** (the asymptote is 64.01, below my target, but the max is what enters C_T). Same right-edge error |
| B4 (proportional allocation optimal) | **PASS** | 2000 random admissible allocations at each i_* ∈ {2,3,4,5}; none beats it |
| C1 (assembly) | REPORTED, no verdict | as pre-registered; its inputs are SUPPLIED constants |

The three FAILs are all errors in **my own criteria**, not disagreements with SQ.md or with the review. Reporting
them as FAILs: the corrected numbers (4080, i_* = 0, 175.8) are the ones used throughout §3-§6, and the
ct1_moser.py Block C table is superseded by ct1b/ct1c because it used F = 16129 (the trivial branch) where an
iteration factor belonged. **No conclusion in §6 rests on ct1_moser.py Block C.**

---

## 8. FOR OTHER FILES (not edited)

I edited only this file and `checks/ct1_*`. The following are requests, not edits.

### 8.1 For SQ.md's owner (§15.1, §15.2, §15.3)

1. **(the one that matters) Stop fixing q := 8.** l.1621 fixes q := 8 for Theorem EPS-0. §4.2 here shows the
   Moser constant obeys C_T ∝ (one-step constant)^{q/(q-4)}, so q = 8 is the **worst admissible choice** and the
   exponent is 2 there. Carrying q as a parameter and taking q ≈ 30-100 moves C_T by 4-8 decades at no cost
   except θ_G ∝ 1/q, which has ≈ 25 decades of headroom. Restate EPS-T, Corollary EPS-0a, EPS-0b-avg and
   Theorem EPS-0 with q free, and record θ_G = θ_G(q) explicitly in §15.2 (it is currently only implicit in
   "qβ ≤ ½", l.1609).
2. **l.1504: replace e^{100} by 255, not by 1.6·10⁴.** The exact sup over R ≥ 128 of R^{4/p_{i_*}} with
   p_{i_*} = 2^{⌊log₂R⌋-5} is 255, at R = 255. REVIEW_SQ_S4 M4-2's 1.6·10⁴ applies the crude p_{i_*} ≥ R/64 at
   the single worst R and over-states this factor by 64× (§5.2). The quantity that belongs in the write-up is
   the full schedule factor F = R²Πd_i^{-2/p_i} ≤ 4080 as written.
3. **l.1498-1499: change the radius schedule.** r_i := R/2 + R2^{-i-3} spends only R/8 of the available
   R/2 - 4, which costs a factor 23 and forces R_0 = 128. Taking the gaps d_i ∝ 2^{-i} with Σd_i = R/2 - 4
   (the same geometric *shape*, which Lemma S here proves is already the optimal allocation) gives F ≤ 175.8 and
   R_0 = 32. Also worth stating: l.1500's "16^i" over-states the schedule's own 4^i.
4. **l.1479-1480: split the potential's neighbourhood.** V's maxima are written uniformly over N_3(p). The
   source part V_s only ever needs N_1 (|𝒮|_loc is defined on N_1 at l.1480, and the accompanying w-maximum at
   l.1481 is over the link's plaquettes). Since V_s is the term with the O(1) scale-invariant norm and V_c is the
   small one, lumping both at N_3 costs (14406/486)^{3/4} ≈ 12.7 in the one-step constant, i.e. ≈ 160 in C_T at
   q = 8 (§2.3).
5. **The only thing now blocking an explicit C_T is (★).** Steps (2)-(4) (l.1471-1487) are the place where
   C_1 is defined, and step (3) (l.1476-1484) is where C_V is. Everything after (★) is expanded in §2 here with
   explicit constants. If (★) is expanded to a numerical C_1 and C_V, C_T follows by substitution into §6.1's
   formula — no further derivation needed. Two specific asks: (a) carry one β², not β⁴, in (★) if the standard
   d = 4 Caccioppoli allows it (worth a factor 44); (b) state ||V||_∞ so Q = 1 + 18||V||_∞|N_1| is a number.
6. **S4-3's added hypothesis** (sup_{p⊂B_R}||1 - U(p)|| ≤ ¼) is needed, and it changes no factor of C_T that
   matters (§5.3). Adding it does not reopen anything here.

### 8.2 For the lead

- **(CONST-T) answer: at q = 8 the interface does not carry a number, and that is now PROVEN for this route, not
  estimated.** C_T ≥ 1.27·10¹⁴ > 10¹³ for every C_1C_V ≥ 1. Best estimate 5·10²⁰.
- **It carries a number at q ≳ 30**, conditional on C_1·C_V ≲ 10⁴ and on ε_* ≤ 10⁻⁴. q is a free parameter of
  EPS-T, not a new assumption. This is the cheapest available repair in the lane: it is a restatement, not new
  mathematics.
- **The next bounded task is expanding (★)** (steps (2)-(4) of SQ.md §15.1) to numerical C_1 and C_V. That single
  task converts §6.1 from CONDITIONAL to PROVEN and decides the interface. It is one session's work and it is
  independent of every other lane.
- This is lead decision D3 ("the constants are the enemy") in its sharpest form so far: the enemy is one
  *exponent*, a = q/(q-4), not the size of any individual constant.

### 8.3 For RLARGE.md / REVIEW_RLARGE (not edited)

- The recorded ceiling should be stated as a function of q, because C_T' = 2^{2+4/q}·4C_T and 32^{1/q}C_0 both
  improve with q: at q = 8 the ceiling is C_T ≲ 10¹³ (REVIEW_SQ_S4 S4-16), at large q it is **C_T ≲ 1.7·10¹³**
  (A_0 falls from ≈ 228c_N·C_T to ≈ 132c_N·C_T, §4.2).
- REVIEW_SQ_S4 S4-16's "the finite-iteration/trivial branch contributes ≥ 128² ≈ 1.6·10⁴" is true but **not the
  leading contribution**: it is swamped by ≥ 6 decades by the iteration constant (§3.3). The 1.6·10⁴ should not be
  quoted as "the factor inside C_T".
- REVIEW_SQ_S4 S4-16's own estimate of the Moser product, "≈ C·4·10³", is the object B(4a)·F here; its value is
  1931·4080 = 7.9·10⁶ as written and 51·176 = 9.0·10³ at q = 100 with the optimised schedule.

### 8.4 One thing I could not settle

Whether the exponent a = q/(q-4) is **sharp** for this step. The sub-ball route (cover B_R by balls of radius ρ
with ρ^{2-4/σ}||V||_σ ≤ δ_0 small, iterate on each, chain) gives the same exponent at (d, σ) = (4, 4), so I could
not beat a = 2 at q = 8 by that device either. The literature exponent I half-remember for Serrin/Trudinger local
boundedness, σ/(2σ-d), would be 1 at (4,4); I could not reproduce it and I am not asserting it. **OPEN**, and it
matters only if q cannot be raised.

---

## 9. My own pre-stated expectations: three of four were wrong

§1.5 registered four structural expectations before any derivation, precisely so that disagreement would be
reportable. Reporting it:

| | pre-stated expectation (§1.5) | outcome |
|---|---|---|
| **E1** | the one-step constant enters as √C, the i- and β-parts contribute 10³-10⁴ | **REFUTED.** The one-step constant enters to the power Σ1/p_i = **1**, not ½ (§2.2); and the *potential norm* enters to the power a = q/(q-4), which is 2 at q = 8. The β- and schedule parts contribute B(4a)·F = 7.9·10⁶ as written — the right order, by accident |
| **E2** | R_0² = 16384 is a floor but not binding | **CONFIRMED** (§3.3), and by ≥ 6 decades |
| **E3** | the radius schedule has the most leverage | **REFUTED.** It is worth 23× (§3.2). q is worth 10⁴-10⁸ |
| **E4** | q = 8 or a little lower is near-optimal; raising q costs | **DECISIVELY REFUTED.** q = 8 is the *worst* admissible choice: a = q/(q-4) is monotone decreasing in q, so the whole result turns on raising q, and the cost (θ_G ∝ 1/q) has 25 decades of headroom (§4.2) |

The one expectation that held is the one that did not matter. The finding that decides the task — the exponent
a = q/(q-4) and the freedom in q — is the thing I expected to go the other way.
