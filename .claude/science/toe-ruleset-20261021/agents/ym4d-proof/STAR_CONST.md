# STAR_CONST: expanding (★) — explicit values for C_1 and C_V

Worker: the (STAR-CONST) agent of session 24. I own this file and `checks/sc1_*` only. I have written nothing else
anywhere. No git command has been run by me.

---

## 1. PRE-STATED (first edit of this file, 2026-10-28 13:31:06 UTC)

**This section is the very first edit to this file. It contains STATEMENTS ONLY. It cites no derivation of my own and
no number computed by me; the only numbers it quotes are (a) constants already written in SQ.md §15.0-§15.1, (b)
numbers from REVIEW_SQ_S4, and (c) the thresholds handed to me in my brief, which were landed in CONST_T.md before
this file existed.** Everything below §1 was written after this section was on disk.

### 1.1 The task, as I received it

SQ.md §15.1's Theorem EPS-T proves its Moser iteration through an energy inequality

  **(★)  Σ|∇(ζW)|² ≤ C_1 β⁴ [ Σ_p V(p)·ζ̃(p)²·W̃(p)² + r⁻²·Σ_{supp⁺}W² ]**   (SQ.md l.1487)

with **V := C_V[M_3u + (M_3u)² + |𝒮|²_loc/k²]** (SQ.md l.1480). Neither C_1 nor C_V is given a value anywhere in
SQ.md. CONST_T.md §6.1 expanded everything *downstream* of (★) and reached the closed formula

  C_T = √6 · F · B(4a) · [ ½(36·C_1·C_V·486)^a + ½(A_cγ_c)² + 288·C_1·Q ],  a = q/(q-4),

so that C_1 and C_V are the last two symbols. **My job: expand steps (2), (3) and (4) of SQ.md l.1471-1487 and
supply explicit numbers, or rigorous upper bounds, for C_1 and C_V.**

### 1.2 What I will do

S1. Expand step (2) (l.1471-1475): the discrete convexity identity, the cut-off part of the pairing, the δ/C_δ Young
    split, and the resulting coefficient in front of Σ|∇ζ|²w^{β+1}. Record every δ as FORCED or CHOICE.
S2. Expand step (3) (l.1476-1484) term by term — the ≤ 6 covariant differences in D_1* and D_2, the discrete product
    rule, the source term, the R_1 and B (Bianchi) terms, the K (Weitzenböck) term — and read off the coefficient of
    each of the three pieces of V. This gives C_V, and it gives the β-power the proof actually needs.
S3. Expand step (4) (l.1485-1487): the discrete chain rule |∇W| ≤ ((β+1)/2)w_max^{(β-1)/2}|∇w|, the lower bound
    ψ̄ ≥ ½ζ_min²w_max^{β-1}, and the cut-off comparison ζ_max² ≤ 2ζ_min² + C/r². This gives C_1.
S4. Decide whether C_V should be **split** into a source coefficient C_V^s (the |𝒮|²_loc/k² term) and a curvature
    coefficient C_V^c (the M_3u and (M_3u)² terms), since CONST_T.md's dominant term uses only the source part.
S5. Check explicitly whether η = ||1 - U(p)|| enters C_1 or C_V. REVIEW_SQ_S4 S4-3 records that BIA, WB and the R_1
    bound all need η small, and S4-3's fix adds the hypothesis sup_{p⊂B_R}||1 - U(p)|| ≤ ¼. CONST_T.md §5.3 claims
    the added hypothesis changes no factor of C_T that matters. **If η enters C_1 or C_V I will say so plainly, and
    that contradicts CONST_T §5.3.**
S6. Substitute into CONST_T.md §6.1 and report C_1, C_V, C_1·C_V and the resulting q_min.

### 1.3 PRE-REGISTERED verdict table

Registered now, before any derivation or script. The thresholds are CONST_T.md's (landed before this file) and the
brief's; none is mine.

Brief's q_min table (given to me, not derived here): q_min = 9 at C_1C_V = 1, 16 at 100, 31 at 2000, 132 at 10⁴,
unreachable at 5·10⁴. The decision bar handed to me is **q_min ≤ 30**.

| verdict | condition |
|---|---|
| **PASS** | a rigorous upper bound C_1 ≤ X and C_V ≤ Y, derived from steps (2)-(4) as written plus S4-3's added hypothesis, with **X·Y ≤ 2·10³** (hence q_min ≤ 30 by the brief's table), AND each constant labelled FORCED or CHOICE with the choice priced. |
| **PARTIAL-HI** | rigorous bounds exist but **2·10³ < X·Y ≤ 10⁴** (q_min between 31 and 132): the interface carries a number only at a large q. Reported as a straddle, not rounded to PASS. |
| **FAIL** | rigorous bounds exist but **X·Y > 10⁴**, or a rigorous *lower* bound C_1C_V > 10⁴ on what steps (2)-(4) produce. The interface then carries no number at any admissible q. |
| **OPEN-STEP** | one of steps (2)-(4) cannot be pinned without an estimate SQ.md does not contain. I must then name the step, name the missing estimate, and give the best rigorous bound available. This is a real deliverable, not a failure to report. |
| **CONTRADICTS-CONST-T** | (orthogonal to the above) η enters C_1 or C_V in a way that makes either depend on ε_* or on the added hypothesis. Reported separately whatever the main verdict is. |

### 1.4 Things I state in advance that I will NOT do

- I will not edit SQ.md, CONST_T.md, NORMS.md, SQ_LOG.md, any REVIEW_* file, or any file other than this one and
  `checks/sc1_*`. Requests for other owners go in a final "FOR OTHER FILES (not edited)" section.
- I will not change CONST_T.md §6.1's formula, its F, its B(4a), its multiplicities 486 / 14406, its a = q/(q-4), or
  its downstream chain. I substitute into them.
- I will not re-derive BIA (C_B), WB (C_K), SOB (C_S = 3) or §15.0's R_1 bound; I take them as written in SQ.md and
  will say exactly which numerical content of each I need and whether SQ.md supplies it.
- I will not declare PROVEN any constant whose value needs a count SQ.md labels "crude" (the "≤ 200 terms" of WB at
  l.1439, the "ladders of ≤ 12 plaquettes" at l.1439) unless I count it myself and say so; otherwise it is SUPPLIED
  and its sensitivity is carried to the end.
- I will not optimise q. q is CONST_T.md's lever and the brief tells me q = 8 is already dead for every C_1C_V ≥ 1.
  I report q_min; I do not re-open the q discussion.

### 1.5 Pre-registered structural expectations (so that agreement is evidence and disagreement is reportable)

Written before any derivation. These are expectations, not claims.

- X1. C_1 will be dominated by the product of (i) the number of covariant differences the right side of step (2)
  carries (the "≤ 6" of l.1476, appearing squared after Cauchy-Schwarz) and (ii) the Young constant C_δ at the δ that
  step (2) and step (3) must share to leave a positive fraction of Σψ̄|∇u|² on the left. I expect C_1 in the range
  10²-10⁴, i.e. **above** CONST_T.md's SUPPLIED 20.
- X2. C_V's *source* coefficient will be much smaller than its curvature coefficient, because the source term
  (l.1481) is reached by a single Cauchy-Schwarz with no multiplicity, whereas the K term carries WB's ≤ 200 local
  terms. I expect C_V^s = O(10) and C_V^c = O(10²-10³).
- X3. Because CONST_T.md's dominant term is ½(36·C_1·C_V^s·486)^a, the product that decides the verdict will be
  C_1·C_V^s, not C_1·C_V^c. If X1 and X2 both hold, C_1·C_V^s ≈ 10³-10⁵ and the verdict will be PARTIAL-HI or FAIL,
  not PASS.
- X4. η will **not** enter C_1 (step (2) and step (4) are pure calculus on w and ζ) but **will** enter C_V^c through
  BIA and WB, as a factor already absorbed into the definition of V by writing M_3u in place of M_3η. So S4-3's
  hypothesis will turn out to be what licenses the *form* of V, with the conversion constant c_N riding in C_V^c, not
  in C_V^s. If so CONST_T.md §5.3 is right in its conclusion for the dominant term and imprecise in its reason.

---

## 2. Conventions, and the two lattice counts that the whole answer turns on

### 2.1 Notation (SQ.md §15.0, §15.1; nothing new)

u := 𝒫, ε := ||u||_{ℓ²(B_R)}, k := R^{1-4/q}||𝒮||_{ℓ^q(B_R)} > 0, w := (|u|² + k²)^{1/2}, W := w^{(β+1)/2}, β ≥ 1.
ψ := ζ²w^{β-1} (l.1473). For an edge (p, p + e_λ) write a := u(p), b := Ad_{U(p,λ)}u(p + e_λ), so |∇_λu(p)| = |b - a|,
ζ_a := ζ(p), ζ_b := ζ(p + e_λ), w_a, w_b likewise, and

  ζ_m := max(ζ_a, ζ_b),  ζ_min := min(ζ_a, ζ_b),  w_m := max(w_a, w_b),  ψ̄ := ½(ψ_a + ψ_b),
  **g := sup|∇ζ|**  (so CONST_T.md §2.1's "|∇ζ|²_sup"; CONST_T §2.3 fixes g ≤ 4/d_i, and I use g only as a symbol).

The good term of the energy identity is

  **𝒜 := Σ_{λ=1}^{4} Σ_p ψ̄(p, λ)·|∇_λu(p)|²**  (the "Σψ̄|∇u|²" of l.1475).

Two elementary facts used throughout, both **PROVEN** here:
- **(E1)** ψ(p + e_λ) ≤ 2ψ̄(p, λ) and ζ_min²w_m^{β-1} ≤ 2ψ̄(p, λ). *Proof.* ψ̄ is half a sum of two nonnegative
  terms, so 2ψ̄ ≥ each of them; and ζ_min²w_m^{β-1} is ≤ max(ζ_a²w_a^{β-1}, ζ_b²w_b^{β-1}) because t ↦ t^{β-1} is
  non-decreasing for β ≥ 1 (if w_m = w_a then ζ_min²w_a^{β-1} ≤ ζ_a²w_a^{β-1}, and symmetrically). ∎
  (This is l.1486's "ψ̄ ≥ ½ζ_min²w_max^{β-1}", with the proof the review called "stated, not executed" (S4-4).)
- **(E2)** ζ_m ≤ ζ_min + g, hence ζ_m² ≤ 2ζ_min² + 2g². (This is l.1483-1484's "ζ(p)² ≤ 2ζ(p')² + 2(6/r)²" at
  distance 1; at ℓ^∞ distance 3 the g becomes 3g and the constant 2(3g)² = 18g².)
- **(E3) (edge counting)** For any F ≥ 0 on plaquettes, Σ_{λ=1}^4Σ_p w_m^{...} -type sums obey
  Σ_λΣ_p F(w_m) ≤ Σ_λΣ_p[F(w_a) + F(w_b)] = 8Σ_pF(w(p)) when F is monotone, because each plaquette is the near
  end of 4 forward edges and the far end of 4 backward edges. If λ is restricted to a 2-element set Λ(p) the
  factor is 4.

### 2.2 Count A: D_1* and D_2 are each exactly **3** covariant differences, and the source pairs each plaquette with exactly **2** of them

**Lemma A1 (the divergence form of D_1*). [PROVEN]** With the straight covariant operators of l.1383-1384, for every
2-form v and every link (y, μ),

  **D_1*v(y, μ) = −Σ_{ν≠μ} Ad_{U(y-e_ν,ν)}^{-1}[ ∇_ν v_{μν}(y − e_ν) ]**  — exactly **3** terms in d = 4.

*Proof.* Expand ⟨D_1α, v⟩ = Σ_xΣ_{μ<ν}⟨α_μ(x) + Ad_{U(x,μ)}α_ν(x+e_μ) − Ad_{U(x,ν)}α_μ(x+e_ν) − α_ν(x), v_{μν}(x)⟩
and collect the coefficient of α_μ(y). The two un-transported terms give Σ_{ν≠μ}v_{μν}(y) (using v_{νμ} = −v_{μν}),
and the two transported terms give −Σ_{ν≠μ}Ad^{-1}_{U(y-e_ν,ν)}v_{μν}(y − e_ν). Their difference is
Ad^{-1}_{U(y-e_ν,ν)}[Ad_{U(y-e_ν,ν)}v_{μν}(y) − v_{μν}(y − e_ν)] = Ad^{-1}[∇_νv_{μν}(y − e_ν)] summed over ν ≠ μ. ∎

D_2 is **3** covariant differences by its definition (l.1385): (D_2v)_{λμν}(x) = ∇_λv_{μν} − ∇_μv_{λν} + ∇_νv_{λμ}.

So SQ.md l.1476's "sums of ≤ 6 covariant differences" is conservative by a factor 2 for both operators;
**the true number is 3.** [PROVEN]

**Lemma A2 (the source's incidence pattern). [PROVEN]** For a plaquette p with base x and plane {μ, ν} put
L(p) := {(x + e_ν, μ), (x + e_μ, ν)} — the two links of ∂p not incident to x. Then in
⟨𝒮, D_1*(ψu)⟩ = Σ_b⟨𝒮(b), D_1*(ψu)(b)⟩, re-indexed by Lemma A1 over plaquettes,
- each plaquette p carries exactly **|Λ(p)| = 2** terms, with directions λ ∈ {μ_p, ν_p} and source links L(p);
- each link b belongs to L(p) for exactly **|𝒩_rev| = 3** plaquettes p (one for each other in-plane direction).

*Proof.* By Lemma A1 the term indexed by (b, ν) carries the plaquette (y − e_ν; μ_bν) and the difference direction ν,
and b = ((y − e_ν) + e_ν, μ_b) is the far μ_b-link of that plaquette; so the difference direction is always one of
the plaquette's two in-plane directions, giving |Λ(p)| = 2. Conversely b = (y, μ) is the far μ-link of exactly one
plaquette per other in-plane direction β ≠ μ, namely the plaquette at y − e_β in the plane {μ, β}: 3 of them.
Consistency: 4V links × 3 = 6V plaquettes × 2. ∎

**Lemma A3 (the Bianchi term's incidence pattern). [PROVEN]** Each plaquette p = (x; μν) lies in exactly **2** 3-cells
(x; λμν), λ ∉ {μ, ν}, and each 3-cell carries exactly 3 plaquettes, all based at its own base point. So the B-group
has |Λ_B(p)| = 2 and reverse count 3 as well. ∎

**Why these two counts decide the task.** CONST_T.md §2.3 reads SQ.md l.1479-1480 literally and therefore pays a
plaquette-maximum multiplicity |N_1^plaq| = 3⁴·6 = 486 (or |N_3^plaq| = 14406) for the source term. Lemmas A1-A3 show
that the *only* maxima the source term needs are over **{p, p + e_{μ_p}, p + e_{ν_p}}** (3 plaquettes, same
orientation) and over **L(p)** (2 links, reverse count 3). Those are the numbers §6 substitutes.

---

## 3. STEP (2) EXPANDED (SQ.md l.1471-1475) — **PROVEN**

The identity at l.1472 is exact and was verified algebraically by the reviewer (REVIEW_SQ_S4 S4-4); I use it as
given: ⟨b − a, ψ_bb − ψ_aa⟩ = ψ̄|b − a|² + ½(ψ_b − ψ_a)(|b|² − |a|²).

Split ψ_b − ψ_a = ζ_b²(w_b^{β-1} − w_a^{β-1}) + (ζ_b² − ζ_a²)w_a^{β-1}. The first product with ½(|b|² − |a|²) is
**≥ 0** (both factors carry the sign of |b| − |a|, as l.1473-1474 says) and is discarded. For the second:

  |½(ζ_b² − ζ_a²)| ≤ ½|ζ_b − ζ_a|(ζ_a + ζ_b) ≤ g·ζ_m,
  w_a^{β-1}·||b|² − |a|²| = w_a^{β-1}(|a| + |b|)·||b| − |a|| ≤ w_m^{β-1}·2w_m·|b − a| = 2w_m^{β}|b − a|,

so the cut-off part is at most **2g·ζ_m·w_m^{β}|b − a|**. By (E2), ζ_m ≤ ζ_min + g, so this is at most

  2gζ_min·w_m^β|b − a|  +  2g²w_m^β|b − a|.

*First piece, by Young 2XY ≤ δX² + δ^{-1}Y² with X := ζ_min w_m^{(β-1)/2}|b − a|, Y := g w_m^{(β+1)/2}:*
  ≤ δ·ζ_min²w_m^{β-1}|b − a|² + δ^{-1}g²w_m^{β+1} ≤ **2δ·ψ̄|b − a|² + δ^{-1}g²w_m^{β+1}**  [(E1)].
*Second piece,* using |b − a| ≤ |a| + |b| ≤ 2w_m: ≤ **4g²w_m^{β+1}**.

Summing over the 4 directions and all plaquettes, and applying (E3) (factor 8):

> **(2′) [PROVEN]  Σ_λ⟨∇_λu, ∇_λ(ψu)⟩ ≥ (1 − δ_2)·𝒜 − 8(2/δ_2 + 4)·g²·Σ_{supp⁺}w^{β+1},  δ_2 := 2δ.**

This is l.1475 with **C_δ = 8(2/δ_2 + 4)** and the δ of l.1474 identified as δ_2/2.

**Status of the constants in (2′).** δ_2 is a **CHOICE** (§6.1 prices it). The 8 is **FORCED** (edge count, (E3)).
The 4 is **FORCED** given the route (it is 2·2 from |b − a| ≤ 2w_m). **No β and no η appear in (2′)** — step (2) is
pure calculus on ζ, w and the convexity identity. This already settles half of pre-stated expectation X4.

---

## 4. STEP (3) EXPANDED (SQ.md l.1476-1484) — the source group is **PROVEN**, the curvature groups are **CONDITIONAL on C_K′, C_B**

The right side of the pairing is ⟨𝒮 − R_1, D_1*(ψu)⟩ + ⟨B, D_2(ψu)⟩ + ⟨K(u), ψu⟩ (l.1471). I treat the four
groups separately, because — and this is the central structural finding of this file — **they do not deserve a
common constant.**

The exact discrete product rule (l.1476), **PROVEN**:
  ∇_λ(ψu)(p) = ψ(p + e_λ)·∇_λu(p) + (∇_λψ)(p)·u(p),
and (l.1477), **PROVEN** by the mean-value inequality for t ↦ t^{β-1} plus Kato (|∇w| ≤ |∇u|, l.1477-1478):
  **|∇_λψ(p)| ≤ 2gζ_m·w_m^{β-1} + (β − 1)ζ_m²w_m^{β-2}|∇_λu(p)|.**

### 4.1 The source group ⟨𝒮, D_1*(ψu)⟩ — **PROVEN**

By Lemmas A1-A2, with |𝒮|_L(p) := max_{b∈L(p)}|𝒮(b)| (**2 links**, not SQ's N_1 = 324):

  |⟨𝒮, D_1*(ψu)⟩| ≤ Σ_p Σ_{λ∈Λ(p)} |𝒮|_L(p)·[ψ(p+e_λ)|∇_λu(p)| + |∇_λψ(p)||u(p)|],  |Λ(p)| = 2.

Write **ζ̂(p), ŵ(p)** for the maxima of ζ, w over 𝒩_S(p) := {p, p + e_{μ_p}, p + e_{ν_p}} (**3 plaquettes**), and
**V_s := |𝒮|²_L/k²** (dimensionless, and ≤ 1; see §4.5). Throughout, k ≤ w gives k²ŵ^{β-1} ≤ ŵ^{β+1}, which is
l.1481's conversion.

**(S1)** Σ_pΣ_λ|𝒮|_Lψ(p+e_λ)|∇_λu| ≤ (t/2)Σ_pΣ_λψ(p+e_λ)|∇_λu|² + (1/2t)Σ_pΣ_λψ(p+e_λ)|𝒮|²_L
  ≤ **t·𝒜 + (1/t)·Σ_p ζ̂²ŵ^{β+1}V_s**  [(E1) gives ψ(p+e_λ) ≤ 2ψ̄ on the first; |Λ| = 2 on the second].

**(S2a)** the g-part of |∇_λψ| against |u(p)| ≤ w_m:
  Σ_pΣ_λ|𝒮|_L·2gζ_mw_m^{β-1}·w_m = 2Σ_pΣ_λ g·ζ_m·|𝒮|_L·w_m^β ≤ 2Σ_pΣ_λ g·[ζ_m(|𝒮|_L/k)]·w_m^{β+1}
  ≤ Σ_pΣ_λ[g² + ζ_m²V_s]w_m^{β+1}  ≤ **4g²Σ_{supp⁺}w^{β+1} + 2Σ_pζ̂²ŵ^{β+1}V_s**
  [2XY ≤ X² + Y² with X := g, Y := ζ_m(|𝒮|_L/k); then (E3) with |Λ| = 2 gives the factor 4, and ζ_m ≤ ζ̂, w_m ≤ ŵ].

**(S2b)** the (β−1)-part, with ζ_m² ≤ 2ζ_min² + 2g² ((E2)):
  Σ_pΣ_λ|𝒮|_L(β−1)ζ_m²w_m^{β-2}|∇_λu|·w_m = (β−1)Σ_pΣ_λ|𝒮|_Lζ_m²w_m^{β-1}|∇_λu|
  ≤ 2(β−1)Σ_pΣ_λ|𝒮|_Lζ_min²w_m^{β-1}|∇_λu| + 2(β−1)g²Σ_pΣ_λ|𝒮|_Lw_m^{β-1}|∇_λu|.
 *(S2b-1)* Young at s, then (E1): ≤ 2(β−1)s·𝒜 + (2(β−1)/s)Σ_pζ̂²ŵ^{β+1}V_s.
 *(S2b-2)* |∇_λu| ≤ 2w_m and |𝒮|_L/k ≤ ½(V_s + 1): ≤ 2(β−1)(1 + ||V_s||_∞)·4·g²Σ_{supp⁺}w^{β+1}.

**Choosing s := s_0/(2(β−1))** (for β > 1; at β = 1 the (S2b) terms vanish) makes the 𝒜-share β-free:

> **(3′s) [PROVEN]  |⟨𝒮, D_1*(ψu)⟩| ≤ (t + s_0)·𝒜 + C_A^s·β²·Σ_pζ̂²Ŵ²·V_s + C_B^s·β·g²·Σ_{supp⁺}w^{β+1}**
> **with  C_A^s := 1/t + 2 + 4/s_0   and   C_B^s := 4 + 8(1 + ||V_s||_∞) ≤ 20,**

using 1/t + 2 ≤ (1/t + 2)β² and 4(β−1)²/s_0 ≤ 4β²/s_0 for β ≥ 1, and 4 + 8(β−1)·2 ≤ 20β. (Ŵ² = ŵ^{β+1}.)

**Every constant in (3′s) is a Young parameter.** No c_N, no C_B, no C_K, no η, no ε_*. t and s_0 are **CHOICES**,
priced in §6.1; everything else (the 2, the 4, the 20, the multiplicities 2 and 3) is **FORCED** by Lemmas A1-A2 and
(E1)-(E3).

### 4.2 The R_1 group ⟨−R_1, D_1*(ψu)⟩ — same algebra, different potential

§15.0 l.1396 gives |R_1(b)| ≤ 4Σ_{p∋b}||1 − U(p)||·|𝒫(p)|. A link lies in **6** plaquettes in d = 4, and S4-3's
added hypothesis with §15.0 l.1389-1390 gives η(p) = ||1 − U(p)|| ≤ |log U(p)|_op ≤ c_N|𝒫(p)|; hence

  **|R_1(b)| ≤ 24·c_N·(M_1u(b))².**  [PROVEN given S4-3's hypothesis]

Repeating §4.1 verbatim with |R_1|_L in place of |𝒮|_L, and converting with ŵ^{β-1}|R_1|²_L ≤ 576c_N²(M_1u)²·ŵ^{β+1}
(using (M_1u)² ≤ (M_1w)² ≤ ŵ²), the group contributes

  (t_R + s_R)·𝒜 + [576·c_N²·(1/t_R + 2 + 4/s_R)]·β²·Σ_pζ̂²Ŵ²·(M_1u)² + O(c_Nε_*)·β·g²Σw^{β+1}.

The cut-off piece is O(c_Nε_*) because its S2a-analogue is 24c_N[g² + ζ_m²](M_1u)ŵ^{β+1} and M_1u ≤ ε ≤ ε_*
pointwise (SOB (c)). **This group's potential is (M_1u)², i.e. part of V_c.** [PROVEN given S4-3]

### 4.3 The Bianchi group ⟨B, D_2(ψu)⟩

BIA (l.1419-1420) with S4-3's hypothesis: |B(c)| = |(D_2𝒫)(c)| ≤ C_B·(max_{f⊂c}η)² ≤ C_B·c_N²(M_1u)². By Lemma A3
the incidence pattern is the same (2 per plaquette, reverse count 3), so this group contributes

  (t_B + s_B)·𝒜 + [C_B²·c_N⁴·(1/t_B + 2 + 4/s_B)]·β²·Σ_pζ̂²Ŵ²·(M_1u)² + O(C_Bc_N²ε_*)·β·g²Σw^{β+1}.

**C_B is not given a value in SQ.md.** q5 B1 measures |D_2𝒫|/η² = 3.1-3.6 at η = 0.01-0.04 on a side-3 torus, which
REVIEW_SQ_S4 S4-19 says does not test BIA's local geometry at all. So **C_B is SUPPLIED**; §6.3 shows it does not
matter.

### 4.4 The Weitzenböck group ⟨K(u), ψu⟩ — no absorption, no β

WB (l.1431-1433): |K(u)(p)| ≤ C_K′·M_3η(p)·M_2u(p) ≤ C_K′c_N·(M_3u)(p)·M_3w(p). Hence
  |⟨K(u), ψu⟩| ≤ Σ_pζ²w^{β-1}·w·C_K′c_N(M_3u)(M_3w) ≤ **C_K′c_N·Σ_pζ̃²·(M_3u)·(M_3w)^{β+1}**,
i.e. 𝒜-share **0**, β-power **0**, potential (M_3u), and the maxima here genuinely run over **N_3** (that is what WB's
coefficient M_3η and N_2 support force). [PROVEN given WB]

WB's own proof gives only crude counts: ≤ 200 local terms and ||Ad_γ − 1|| ≤ 2·4·12·M_3η = 96·M_3η (l.1439-1440), so
the written proof yields **C_K′ ≤ 200·96 = 1.92·10⁴**, against q5 W3's measured ||K||_op/η_P ≈ 3.5-3.9 (which S4-19
says is a global ratio, not an entrywise test). **C_K′ ∈ [4, 1.92·10⁴] is SUPPLIED**; §6.3 shows it does not matter.

### 4.5 ||V_s||_∞ — the number CONST_T asked for

CONST_T §8.1 ask (b) is "state ||V||_∞ so Q = 1 + 18||V||_∞|N| is a number". For the source part, **PROVEN**:

  ||V_s||_∞ = sup_p max_{b∈L(p)}|𝒮(b)|²/k² ≤ ||𝒮||²_{ℓ^∞}/k² ≤ ||𝒮||²_{ℓ^q}/k² = **R^{-2+8/q} ≤ R_0^{-2+8/q} < 1**

(SOB (c) gives ℓ^∞ ≤ ℓ^q; then k = R^{1-4/q}||𝒮||_{ℓ^q}). For the curvature part ||V_c||_∞ ≤ (ε + ε²) ≤ 2ε_*.
So l.1484's assertion "V ≤ C pointwise" is correct, and the constant is **≤ 1 + 2ε_*, not O(1) unknown** — in fact
V_s decays like R^{-2} in the radius, which is why Q is close to 1 and the cut-off term of (★) is not the problem.

---

## 5. STEP (4) EXPANDED (SQ.md l.1485-1487) — **PROVEN**

Per edge, |∇_λ(ζW)(p)| = |ζ_bW_b − ζ_aW_a| ≤ ζ_m|W_b − W_a| + |ζ_b − ζ_a|W_m ≤ ζ_m|∇_λW| + g·W_m, so

  |∇_λ(ζW)|² ≤ 2ζ_m²|∇_λW|² + 2g²W_m².

Discrete chain rule (l.1485) with Kato: |∇_λW| ≤ ((β+1)/2)w_m^{(β-1)/2}|∇_λu|. Hence, using (E2) then (E1) and
|∇_λu|² ≤ 4w_m²,

  2ζ_m²|∇_λW|² ≤ ((β+1)²/2)·(2ζ_min² + 2g²)·w_m^{β-1}|∇_λu|²
              ≤ 2(β+1)²·ψ̄|∇_λu|²  +  4(β+1)²·g²w_m^{β+1},

and 2g²W_m² = 2g²w_m^{β+1}. Summing over the **4** directions and all p, and using (E3) (factor 8) and
(β+1)² ≤ 4β² for β ≥ 1:

> **(4′) [PROVEN]  Σ|∇(ζW)|² ≤ 8β²·𝒜 + 272β²·g²·Σ_{supp⁺}w^{β+1}**
> (32β² + 2 ≤ 34β², times the edge factor 8).

**Status.** Everything in (4′) is **FORCED** except the use of (β+1)² ≤ 4β², which is tight at β = 1 and 4× lossy at
large β. (★) is stated for all β ≥ 1 with a single constant, so the β = 1 end sets it. **No η, no ε_*, no C_B, no
C_K.** With §3 this completes expectation X4: *η enters neither C_1 nor the source coefficient.*

---

## 6. ASSEMBLY: the explicit (★), and the two numbers

### 6.1 The split energy inequality (★*) — **PROVEN**

Add (2′) and the four groups of §4. With κ := 1 − δ_2 − (t + s_0) − (t_R + s_R) − (t_B + s_B) > 0,

  κ·𝒜 ≤ C_A^s β²Σ_pζ̂²Ŵ²V_s + C_A^{K}Σ_pζ̃²W̃²(M_3u) + C_A^{RB}β²Σ_pζ̂²Ŵ²(M_1u)² + C_B^{tot}β·g²Σ_{supp⁺}w^{β+1},

C_A^{K} := C_K′c_N, C_A^{RB} := 576c_N²(1/t_R + 2 + 4/s_R) + C_B²c_N⁴(1/t_B + 2 + 4/s_B), and
C_B^{tot} := 8(2/δ_2 + 4) + 20 + (the O(c_Nε_*) pieces of §4.2-4.3, ≤ 2 for c_Nε_* ≤ 10⁻²).
Substituting into (4′) and using β ≥ 1 to raise every β-power to β⁴:

> **(★*) [PROVEN]  Σ|∇(ζW)|² ≤ β⁴[ Σ_p(c_s·V_s)ζ̂²Ŵ² + Σ_p(c_K·M_3u + c_{RB}·(M_1u)²)ζ̃²W̃² + c_g·g²Σ_{supp⁺}W² ]**
>
> **c_s := 8·C_A^s/κ = 8(1/t + 2 + 4/s_0)/κ,  c_K := 8C_A^{K}/κ,  c_{RB} := 8C_A^{RB}/κ,  c_g := 8C_B^{tot}/κ + 272.**

**(★) as SQ.md writes it (one C_1, one C_V, all maxima at N_3) holds with the same numbers**, because enlarging a
maximum only increases the right side and because β⁴ ≥ β²: take
  **C_1·C_V^{source} = c_s,  C_1·C_V^{curv,lin} = c_K,  C_1·C_V^{curv,quad} = c_{RB},  C_1 = c_g**
in the three-coefficient reading, or, if a single C_V is insisted on, **C_1·C_V = max{c_s, c_K, c_{RB}, c_g}**.
This last is the reading that makes (★)-as-written expensive, and §6.3 prices it.

### 6.2 The budget: c_s = **412**, and this iteration cannot do better than ≈ 319

Only c_s is load-bearing (§6.3), so the budget is spent to minimise it. For fixed T := t + s_0 the inner optimum of
1/t + 4/s_0 is at t = T/3, s_0 = 2T/3, with value 9/T [elementary; Lagrange]. Hence

  **c_s(T) = 8(9/T + 2)/(1 − δ_2 − ρ − T),  ρ := (t_R + s_R) + (t_B + s_B).**

| allocation | δ_2 | ρ | T (optimal) | t | s_0 | κ | **c_s** | c_g |
|---|---|---|---|---|---|---|---|---|
| **chosen** | 1/16 | 1/16 | 0.4180 | 0.1393 | 0.2787 | 0.4570 | **412** | 5628 |
| δ_2, ρ → 0 (unattainable floor) | 0 | 0 | 0.4748 | 0.1583 | 0.3165 | 0.5252 | **319** | — |
| generous curvature budget | 1/8 | 1/4 | 0.3466 | 0.1155 | 0.2311 | 0.2784 | **821** | — |

So **c_s = 412 is a CHOICE, within 1.3× of the best this iteration admits (319)**; no allocation of the δ-budget
makes c_s smaller than 319. The chosen point leaves ρ = 1/16 for the two curvature groups (1/32 each ⟹
1/t_R + 2 + 4/s_R = 9/(1/32) + 2 = 290), and δ_2 = 1/16 for step (2) (⟹ 8(2/δ_2 + 4) = 288).

**c_s = 412 is the answer to the task's question**, in the form in which it is load-bearing:
**C_1 · C_V^{source} = 412 [COMPUTED, exact-rational optimum of the written route].**

### 6.3 C_1 and C_V separately, and why the curvature constants do not matter

| quantity | value | status |
|---|---|---|
| **C_1·C_V^{source} = c_s** | **412** (floor 319) | **COMPUTED** (exact), from steps (2)-(4) only |
| **C_1 (the (★) prefactor, = c_g)** | **5628** | COMPUTED given δ_2 = 1/16 |
| hence **C_V^{source}** | **412/5628 = 0.0732** | COMPUTED — note it is **< 1** |
| C_1·C_V^{curv,lin} = c_K | 17.5·C_K′·c_N ∈ [1.4·10², 6.7·10⁵] | CONDITIONAL on C_K′ (SUPPLIED) |
| C_1·C_V^{curv,quad} = c_{RB} | 17.5·(576c_N² + 290C_B²c_N⁴)·290/290 → ≈ 2.9·10⁶ + 5.1·10³C_B²c_N⁴ | CONDITIONAL on C_B (SUPPLIED) |
| ||V_s||_∞ | ≤ R^{-2+8/q} | **PROVEN** (§4.5) |

**The claim that C_1, C_V ≥ 1 is forced (brief, from CONST_T §6.1) is true of the product C_1·C_V only in the
single-coefficient reading.** In the split reading C_V^{source} = 0.073 < 1: the source's coefficient inside V is a
pure Young constant and nothing forces it to exceed 1. What is forced is the **product** c_s ≥ 319 > 1. I therefore
report the product and not the split, which is arbitrary. [This sharpens, and does not contradict, CONST_T §6.1.]

**Why c_K and c_{RB} do not matter.** They multiply V_c = M_3u and (M_1u)², whose scale-invariant norms are
γ_c = R||V_c||_{ℓ⁴} and whose size is *controlled by Stage 1* (l.1496: R||V_c||_{ℓ⁴} ≤ C′ε_*). The quantity that
enters C_T is the product A_cγ_c, and Stage 1's absorption condition is the statement that **this same product is
≤ O(1)**: raising c_K or c_{RB} forces ε_* down and leaves A_cγ_c unchanged. Since REVIEW_SQ_S4 S4-16 records ≈ 30
decades of headroom in ε_* ("the θ_ε half is safe by ~30 orders"), the lane may take ε_* small enough that
**A_cγ_c ≤ 1**, at no downstream cost. §7 reports C_T under that reading and under CONST_T's SUPPLIED
A_cγ_c = 236.9·C_1 as a sensitivity. **[ARGUED; the step I do not own is Stage 1 (l.1489-1494), which is step (5),
outside steps (2)-(4).]**

### 6.4 One β-power correction that is not mine to apply but changes the arithmetic

The V_c branch has σ_c = 4, hence ϑ_c = ½ and a_c = 2 (CONST_T §2.5 says so), and it enters the Moser step with a
β⁴ coefficient. Young at a_c = 2 therefore squares it to **β⁸**, for every q. Since the Moser step's bracket is a
*sum*, the telescope must be run at the **largest** β-power present, i.e. B(4·max{a, 2}) = **B(8) = 1931.5 for every
q ≥ 8** — not B(4a) with a = q/(q−4), which CONST_T §6.1 uses and which falls to ≈ 44-70 at large q. Dropping the
V_c branch (possible only if V_c is absorbed critically, which fails at large β because the absorption threshold
would have to beat β⁴) would restore B(4a). **I report both conventions in §7 and label them P-ct and P-max.**
**[ARGUED. It is a statement about CONST_T §2.5/§6.1, which I do not edit; it is in §9.]**

---

## 7. CORRECTIONS TO MY OWN §6 (appended, not rewritten)

Three numbers in §6.2-§6.3 were hand-computed before `checks/sc1_cs.py` ran. The exact values are:

| §6 said | exact (sc1_out.txt SC1-4) | effect |
|---|---|---|
| c_s = **412** (chosen allocation) | **411.9229708842423061** | none; 412 is the correct round-up and is the number I report |
| C_B^tot = 310 ⟹ c_g = 5628 | **C_B^tot = 310, c_g = 5699.632830341894211** | I mis-added 288 + 20 + 2 as 306; the correct c_g is 5699.6, 1.3 % larger. Used from here on |
| "generous curvature" allocation c_s = 821 | **787.648** | my hand T* was wrong; the exact optimum is T* = 0.30234. The row's role (a sensitivity) is unchanged |

The floor is confirmed exactly: **c_s ≥ 319.19798** over every admissible δ-budget (δ_2, ρ → 0). The chosen
allocation's c_s = 411.92 is 1.29× the floor.

---

## 8. THE VERDICT

### 8.1 The two numbers

> **C_1 = c_g = 5.70·10³**  (the prefactor of (★), fixed by the cut-off bookkeeping of steps (2) and (4))
> **C_V^{source} = c_s/c_g = 412/5699.6 = 7.23·10⁻²**  (the coefficient of |𝒮|²_loc/k² inside V)
> **C_1 · C_V^{source} = c_s = 411.92 ≤ 412**   — **COMPUTED (exact); floor over all δ-budgets 319.20**
>
> and, for the two curvature coefficients,
> **C_1·C_V^{curv,lin} = c_K = 17.51·C_K′·c_N ∈ [68, 3.4·10⁵]**  (SUPPLIED: C_K′ ∈ [3.9, 1.92·10⁴])
> **C_1·C_V^{curv,quad} = c_{RB} = 17.51·290·(576c_N² + C_B²c_N⁴) ≈ 3.0·10⁶ at (c_N, C_B) = (1, 3.6)**  (SUPPLIED: C_B)
>
> **||V_s||_∞ ≤ R^{-2+8/q} < 1**, so **Q = 1 + 18||V||_∞|𝒩| is a number** (CONST_T §8.1 ask (b) answered).

**η enters none of C_1, C_V^{source}.** It enters only c_K and c_{RB}, through c_N and the hypotheses of BIA and WB.
So **CONST_T §5.3's conclusion is CONFIRMED** — S4-3's added hypothesis changes no factor of C_T that matters — and
its reason is sharpened: the dominant term is built from steps (2) and (4), which are pure calculus, plus step (3)'s
source group, which never touches U. The §1.3 flag **CONTRADICTS-CONST-T is NOT raised.**

### 8.2 q_min, and the thing that actually decides it

Substituting into CONST_T §6.1 (checks/sc1_out.txt SC1-4; A_cγ_c = 1, see §6.3):

| (★)'s neighbourhoods | β-power | C_T(q = 8) | **q_min** | reading |
|---|---|---|---|---|
| **M-sharp** (Lemma A2: 3 plaquettes, 3 links) | P-ct (B(4a)) | 8.25·10¹⁴ | **10** | the sharpened (★*) |
| **M-sharp** | P-max (B(8)) | 8.25·10¹⁴ | **11** | (★*) with §6.4's β-power |
| M-ct (486, CONST_T §2.3) | P-ct | 2.16·10¹⁹ | 20 | CONST_T's own reading |
| M-ct (486) | P-max | 2.16·10¹⁹ | 74 | |
| M-lit (N_3 = 14406 / N_1 = 486, SQ.md l.1479-1480 literally) | P-ct | 3.49·10²¹ | 62 | |
| **M-lit** | **P-max** | 3.49·10²¹ | **none ≤ 400** | **(★) exactly as written fails at every q** |

**Verdict against the §1.3 pre-registered table: PASS**, because c_s = 412 ≤ 2·10³ and q_min = 10-11 ≤ 30 — **but the
PASS is conditional on two restatements, neither of which is new mathematics:**

1. **(★) must carry three coefficients, not one.** With a single C_V the product C_1·C_V is
   max{c_s, c_K, c_{RB}, c_g} ≈ **3.0·10⁶**, which by CONST_T §6.3's own table is beyond the reachable range at every
   q. The reason is structural and avoidable: the *quadratic curvature* coefficient c_{RB} — which is harmless,
   because the potential it multiplies has scale-invariant norm ∝ ε_*² — is promoted by the single-C_V form into a
   multiplier of the **source** term, which is the term that is raised to the power a. **The one-constant form of V
   at SQ.md l.1480 is, by itself, a blocker, independent of every multiplicity.** [PROVEN from §4-§6]
2. **(★)'s neighbourhood maxima must be stated per term** (Lemma A2). SQ.md l.1479 takes ζ̃, w̃ over N_3 for all of
   V; the source group needs them only over 𝒩_S(p) = {p, p + e_{μ_p}, p + e_{ν_p}} and |𝒮| only over L(p). The cost
   of not doing this is 486/3 = 162× in the base, i.e. 162^a ≈ 10⁴ at q = 8 and the difference between q_min = 11 and
   q_min = 74 (or none). [PROVEN from Lemmas A1-A3]

Both are *restatements of §15.1*, available at no cost: the proof already only uses the smaller sets, and the
three coefficients are what the expansion produces. They are requests to SQ.md's owner (§9).

### 8.3 Does the (CLS-min) → RLARGE interface now carry a number?

**Yes, at q ≈ 11-12, conditional on the two restatements of §8.2 and on A_cγ_c ≲ 3.4·10³.**

At the sharpened reading, **C_T ≤ 9.8·10¹² at q = 11 and 5.3·10¹² at q = 12** (P-max, the conservative β-power), and
C_T plateaus at **1.4·10¹²** for q ≳ 30 — a decade under REVIEW_SQ_S4 S4-16's ceiling C_T ≲ 10¹³, and therefore
**C_D ≈ (0.5-0.9)·10³·C_T ≈ (0.7-1.3)·10¹⁵ ≤ 6.7·10¹⁵**, so ε_1 < t_pr and RLARGE's a_bad = c_prε_1² branch holds.
q ≈ 12 is a free parameter choice of EPS-T (CONST_T §4.2), 25 decades inside θ_G ∝ 1/q's headroom.

The conditions, stated so a hostile reader can check them:
- the three-coefficient (★*) and the per-term neighbourhoods of §8.2 (both restatements);
- **A_cγ_c ≤ 3.35·10³** at q = 12 (4.4·10³ at q = 16, 4.5·10³ for q ≳ 30) under P-max; **1.2·10⁴** at q = 12 under
  P-ct (checks/sc1_out.txt, "largest A_c*gamma_c still clearing 1e13"). CONST_T's SUPPLIED reference value is
  A_cγ_c = 236.9·C_1 = 4.7·10³ at C_1 = 20, which **just fails** the P-max condition at every q — so the Stage-1
  threshold ε_* must be lowered by about a factor 2-10 below CONST_T's 10⁻⁴. REVIEW_SQ_S4 S4-16 records ≈ 30 decades
  of headroom there, so this is free, but it is a condition and I state it as one;
- q ≥ 12 (P-max) or q ≥ 10 (P-ct).

### 8.4 What in (★) cannot be pinned

1. **C_B (BIA) and C_K′ (WB) are not determined by SQ.md.** The written proofs give only C_K′ ≤ 200·96 = 1.92·10⁴
   (l.1439-1440, counts the file itself calls crude) and no bound at all for C_B. q5's measurements (3.1-3.6 and
   3.5-3.9) are on a side-3 torus where, as REVIEW_SQ_S4 S4-19 says, the locality claims are untestable. **This is
   the one genuinely missing estimate in steps (2)-(4): an entrywise bound on WB's kernel k(p, p′) and on BIA's
   BCH remainder.** It is harmless for C_T (§6.3), but it means c_K and c_{RB} are SUPPLIED, not computed, and so
   the single-C_V reading of (★) cannot be given a *number* at all — only a lower bound.
2. **A_cγ_c, i.e. ε_* and Stage 1's constant**, sit in step (5) (l.1489-1494), outside my scope. §8.3 states the
   condition on it rather than a value. Pinning ε_* is the natural next bounded task.
3. **The β-power of the V_c branch (§6.4).** Whether B(8) or B(4a) is the right telescope factor turns on whether the
   critical-type potential can be absorbed without a β⁴ coefficient. I could not do it (the critical absorption
   threshold would have to beat β⁴, and ε_* is β-free), so I report P-max as the conservative convention and P-ct as
   CONST_T's. The gap between them is the gap between q_min = 10 and q_min = 11 at M-sharp — immaterial there — but
   it is the gap between q_min = 62 and *no admissible q* at M-lit.
4. **Sharpness.** c_s = 412 is this route's optimum over its own δ-budget (floor 319.2), not a lower bound on the
   best constant in (★). The 4× from (β + 1)² ≤ 4β² in step (4) and the 2× in |∇(ζW)|² ≤ 2ζ²|∇W|² + 2g²W² are the
   two places a β-adapted treatment would gain; together they are worth ≈ 8 in c_s, i.e. ≈ 8^a ≈ 20 in C_T. Not
   decisive. **OPEN, and it does not matter at the sharpened reading.**

---

## 9. CHECKS: one pre-registered FAIL, honestly reported

Criteria: `checks/sc1_criteria.md`, written after STAR_CONST.md §1 and before `checks/sc1_cs.py`. Script:
`checks/sc1_cs.py` (one file, pre-registered, with its one post-hoc block labelled `[POST-HOC, SC1-2b]` in both the
source and the output). Outputs: `checks/sc1_out.txt` (40 digits), `checks/sc1_out_prec60.txt` (60 digits),
`checks/sc1_time.txt`. Plain python, `python3 -I`, single thread, OMP/OPENBLAS/MKL threads = 1, nice 10, no numpy,
no BLAS, **no numeric lock taken** (exact rational/Decimal arithmetic only; 22 s, ~20 MB).

| verdict | result | what it means |
|---|---|---|
| **SC1-1** (reproduce CONST_T §3.1's B(m)) | **PASS** | B(4) = 43.9486, B(8) = 1931.481, B(4.17) = 51.614 — all within 0.5 % of CONST_T's 43.95 / 1931.5 / 51.45 |
| **SC1-2** (reproduce CONST_T §6.3's q_min table) | **FAIL** | under my pre-registered reading "C_1 = 20 wherever C_1 appears alone" I get q_min = 10 / 16 / 30 / 56 / none against CONST_T's 9 / 16 / 31 / 132 / none. **The error is in my criterion, not in CONST_T**: §6.3's table splits the product as C_1 = C_V = √(C_1C_V), which my criterion mis-stated. The failing output is kept unaltered in sc1_out.txt |
| SC1-2b | **POST-HOC**, reproduces 4 of 5 | with C_1 = √(C_1C_V) I get 9 / 16 / 31 / **134** / none and C_T at q_min = 8.60·10¹² / 7.44·10¹² / 9.95·10¹² / 9.99·10¹², against CONST_T's 8.5 / 4.7 / 9.9 / 10·10¹². The single residual disagreement (134 vs 132) is 1.5 % in q at a point where dC_T/dq ≈ 0, and traces to CONST_T's §4.2 B(4a) column being ≈ 8 % below the exact B at mid-range (85 vs 93.5 at q = 24, 70 vs 75.4 at q = 32); **CONST_T's conclusions are unaffected** |
| **SC1-3** (monotonicity) | **PASS** | q_min non-decreasing in C_1C_V (9, 12, 16, 25, 134); C_T(q) strictly decreasing on q ∈ [8, 400] at every grid point — CONST_T §4.2's "raising q is the lever" independently confirmed |
| **SC1-4** (the result) | REPORTED, no verdict | §8.2's six-row table and the sensitivities; the verdict is read off §1.3 |
| **SC1-5** (40 vs 60 digits) | **PASS** | `diff sc1_out.txt sc1_out_prec60.txt` differs in exactly one line, the stated precision. Every q_min and every decade identical |

**The SC1-2 FAIL is an error in my own criterion**, like three of CONST_T's six. It is reported as a FAIL, the output
is unaltered, the post-hoc repair is labelled, and no conclusion in §8 rests on SC1-2: §8's numbers come from
SC1-4, whose harness is validated by SC1-1 (B) and SC1-3 (monotonicity), and whose formula is CONST_T §6.1 read
line by line.

---

## 10. My pre-stated expectations: two of four right

| | pre-stated (§1.5) | outcome |
|---|---|---|
| **X1** | C_1 dominated by the "≤ 6 differences" squared times the Young C_δ; C_1 ∈ [10², 10⁴], above CONST_T's 20 | **HALF-CONFIRMED.** C_1 = 5.70·10³ is in the predicted range and is far above CONST_T's SUPPLIED 20. But the "≤ 6" is really **3** (Lemma A1) and it never gets squared — C_1 is set by the *cut-off* bookkeeping (step (2)'s 8(2/δ_2 + 4) and step (4)'s 272), not by the differences |
| **X2** | C_V^s = O(10) ≪ C_V^c = O(10²-10³) | **CONFIRMED in the ratio, REFUTED in the value.** c_s = 412 against c_{RB} ≈ 3.0·10⁶ — the ratio is far larger than predicted — but C_V^{source} itself is **0.072 < 1**, not O(10) |
| **X3** | C_1·C_V^s ≈ 10³-10⁵ ⟹ the verdict would be PARTIAL-HI or FAIL | **REFUTED, and this is the result.** C_1·C_V^s = 412, and the two lattice counts of §2.2 (3, not 486) move q_min from 74 to 11. The verdict is PASS |
| **X4** | η in C_V^c only, never in C_1 or C_V^s; CONST_T §5.3 right in conclusion, imprecise in reason | **CONFIRMED exactly** (§3, §5, §8.1) |

The expectation that decided the task — X3 — is the one I got wrong, and the reason is the same kind of thing CONST-T
found: not the size of a constant, but a count (486 → 3) and a *form* (one C_V → three).

---

## 11. FOR OTHER FILES (not edited)

I edited only this file and `checks/sc1_*`. The following are requests, not edits.

### 11.1 For SQ.md's owner (§15.1, l.1476-1487) — two restatements, both free

1. **(the one that matters) l.1480: give V three coefficients.** Write
   **V := C_V^{(1)}M_3u + C_V^{(2)}(M_1u)² + C_V^{(3)}|𝒮|²_L/k²** instead of C[M_3u + (M_3u)² + |𝒮|²_loc/k²].
   With one constant, C_1C_V = max{…} ≈ 3.0·10⁶ (driven by the *quadratic curvature* term, whose own contribution to
   C_T is ∝ ε_*² and harmless) and CONST_T §6.3's table then has **no admissible q**. With three, the load-bearing
   product is C_1·C_V^{(3)} = **412** and q_min = 11. This is a one-line change and it is the difference between the
   interface carrying a number and not. (STAR_CONST §8.2 item 1.)
2. **l.1479-1480: state the neighbourhoods per term.** The source group's maxima are over
   𝒩_S(p) = {p, p + e_{μ_p}, p + e_{ν_p}} (**3** plaquettes) and L(p) = the two links of ∂p not incident to p's base
   (reverse count **3**), not over N_3 (14406) or N_1 (486). Proofs: Lemmas A1-A3 of §2.2 here. Worth 162× in the
   one-step base and the difference between q_min = 11 and q_min = 74. The curvature terms genuinely need N_3 (WB's
   M_3η) and should keep it.
3. **l.1476: "≤ 6 covariant differences" is 3, for both D_1* and D_2** (Lemma A1; D_2 by its definition at l.1385).
4. **l.1484's "V ≤ C pointwise" can be made a number:** ||V_s||_∞ ≤ R^{-2+8/q} < 1 and ||V_c||_∞ ≤ 2ε_* (§4.5).
5. **l.1473-1474 and l.1485-1486 can be written out as they stand** — §3 and §5 here do exactly that, with
   (E1) ψ̄ ≥ ½ζ_min²w_max^{β-1} and (E2) ζ_m² ≤ 2ζ_min² + 2g² proved, which is REVIEW_SQ_S4 S4-4's complaint
   discharged. The resulting constants are C_δ = 8(2/δ_2 + 4) in step (2) and 8β²/272β² in step (4).
6. **(★) needs one β², not β⁴, only in its V_c^{lin} term** (the K group carries no β at all, §4.4); the source and
   R_1/B groups genuinely carry β² before step (4)'s β², hence β⁴. CONST_T §8.1 ask (a) ("carry one β², not β⁴") is
   therefore **answerable only for the K term**; the source term's β⁴ is forced by the Young step at
   s ∝ 1/(β − 1).
7. **S4-3's added hypothesis** sup_{p⊂B_R}||1 − U(p)|| ≤ ¼ is needed exactly where REVIEW_SQ_S4 says and nowhere
   else: it licenses η ≤ c_N|u| in §4.2 (R_1) and §4.3-§4.4 (BIA, WB). It does **not** touch C_1 or C_V^{(3)}.

### 11.2 For CONST_T.md's owner (not edited)

- **§6.1's B(4a) should be B(4·max{a, 2}) = B(8) = 1931.5 for every q ≥ 8**, as long as the V_c branch is absorbed
  at a_c = 2 with a β⁴ coefficient (§6.4 here). §2.5 already notes a_c = 2 but §4.2's table and §6.3's q_min row use
  B(4a) with a = q/(q − 4). The effect is 1931.5/70 ≈ 28× at q = 32; it moves CONST_T's q_min at C_1C_V = 1 from 9 to
  about 12 and, at CONST_T's own multiplicity 486 with c_s = 412, from 20 to 74.
- **§2.3's |N_1^plaq| = 486 for V_s is 3** (Lemmas A1-A3 here). CONST_T §8.1 item 4 asks SQ for the N_3 → N_1 split;
  the correct split is N_3 → **3**, worth a further 162× in the base rather than 29×.
- **§4's SUPPLIED C_1 = 20 and C_V = 100 should be replaced by C_1 = 5.70·10³ and C_V^{source} = 7.2·10⁻²**, i.e. the
  product 412 — three decades below CONST_T's reference product 2000 in the dominant term, because of the
  neighbourhood count, not because the Young constants are small.
- **§6.3's table splits the product as C_1 = C_V = √(C_1C_V)** (reverse-engineered here, sc1_out.txt SC1-2b). Saying
  so in §6.3 would make the table reproducible; my pre-registered attempt to reproduce it FAILED for exactly this
  reason (§9).
- §4.2's B(4a) column is ≈ 8 % below the exact B at mid-range (85 vs 93.5 at q = 24; 70 vs 75.4 at q = 32). No
  conclusion of CONST_T changes.

### 11.3 For the lead

- **(STAR-CONST) answer: C_1 = 5.70·10³, C_V^{source} = 7.2·10⁻², product C_1·C_V = 412 (exact optimum of the
  written route; floor 319). q_min = 11** (conservative β-power) **or 10**. The (CLS-min) → RLARGE interface
  **carries a number at q ≈ 12**: C_T ≤ 5.3·10¹² there, against the 10¹³ ceiling, hence C_D ≈ 10¹⁵ ≤ 6.7·10¹⁵.
- **It carries that number only if two sentences of SQ.md §15.1 are restated** (§11.1 items 1-2): V with three
  coefficients, and the source term's neighbourhoods stated as the 3-plaquette / 3-link sets the proof actually
  uses. Neither is new mathematics; both are proved here. **With (★) left exactly as written, and the β-power
  correction of §6.4, there is no admissible q — so this is not a cosmetic request.**
- **The enemy was not a constant and not an exponent, but a *count and a form*:** 486 → 3 (what neighbourhood the
  source term really uses) and one C_V → three (what the curvature constants are allowed to multiply). Together they
  are worth ≈ 10 decades in C_T, against the ≈ 4-8 decades CONST-T bought by raising q. Lead decision D3 again, one
  level finer.
- **The next bounded task is ε_*:** Stage 1 (l.1489-1494, step (5)) fixes A_cγ_c, and §8.3's condition
  A_cγ_c ≤ 3.4·10³ is the only remaining inequality between §6.1's formula and a PROVEN number. It is one session's
  work, independent of everything here, and it is the last symbol in C_T.

---

## 12. One provenance inaccuracy, disclosed

`checks/sc1_criteria.md` carries the header "Written 2026-10-28 13:3x UTC". Its actual creation time is
**13:43:xx UTC** (09:43 local, EDT), as its mtime shows. The *order* it asserts is correct and is what matters —
STAR_CONST.md §1 (13:31:06 UTC) → sc1_criteria.md (13:43) → sc1_cs.py (13:50) → sc1_out.txt (13:50) → everything in
§2-§11 — but the minute in that header is wrong and I have not edited the criteria file to fix it, because editing a
criteria file after its script has run is the worse offence. Recording it here instead.
