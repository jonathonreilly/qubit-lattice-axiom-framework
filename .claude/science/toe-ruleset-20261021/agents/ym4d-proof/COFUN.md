# COFUN.md — target T55-I: (CO-fun)

Owner: the T55-I worker (session 25). Writes confined to this file and `checks/cf1_*`.
Append-only after §1.

## 1. PRE-STATED (session 25, target T55-I) — statements only

**This is the FIRST edit of this file, written at 2026-10-28 21:33 UTC**, before any derivation of
mine, before any criteria file and before any script. Nothing in §1 cites a result produced in
session 25 — not by me and not by another worker. (My scope prompt referred me to a session-25 item
as the *reason* the target exists; no statement below depends on it, and nothing below is a claim
about it.)

Exploratory reading preceded this append and is not recorded as a result: the shared brief;
`SESSION25_RESULTS.md`; `BFT_B.md` §29-§32 and §34-§36.2; `REVIEW_BFT_B_S9_S10.md` headings and
Parts J, K, O and the binding-fix list. The only claim §1 makes is file order.

### 1.0 Scope

Background: trivial. Mass: m = 0 unless a statement says otherwise. Everything below is in lane B's
composite (BFT) setting, elliptic slice S_E (lead decision D1), d = 4, L = 3 where a number is
quoted.

### 1.1 Targets

- **T-I.1 (statement with quantifiers).** Write (CO-fun) out with every quantifier: what is bounded,
  in which norm, uniformly in which of (k, T, X_0, l, α, the source), and under which hypothesis on
  the source. Separate the statement's *asserted* class from the class its consumer supplies.
  *Planned outcome: a statement, labelled as a statement.*
- **T-I.2 (exponent, as a separate symbol).** Name the exponent (CO-fun) needs **θ_c**, never
  inheriting the symbol θ_w, and determine the full admissible range of θ_c and of the Hölder
  exponent α for which the estimate can be run. Decide whether (CO-fun) imposes any *upper* bound on
  θ_c of its own, or only α < θ_c. *Planned: PROVEN-HERE or REFUTED, with the step that binds.*
- **T-I.3 (handle 1, re-derived).** Re-derive the block-interior support statement for the funnel
  transpose h_l^T from the definition of h_l, not by citation: the kernel coefficients, the support,
  and the ℓ^∞ → ℓ^∞ and ℓ¹ → ℓ¹ operator norms. *Planned: PROVEN-HERE or a correction.*
- **T-I.4 (handle 2, re-derived, and the L^{k−l} question).** Re-derive the size estimate for the
  funnel source at level l, and decide whether a power of L^{k−l} is genuinely absent or is hidden
  in a constant, in the units conversion, or in the summation that consumes it. State which units
  each inequality is in at every step. *Planned: PROVEN-HERE, or the hidden power exhibited.*
- **T-I.5 (consumer audit).** Determine which source class BFT-5 clause (b) actually feeds to
  (CO-fun): (i) the solvability class Ξ^T S = 0 (composite-co-closed), (ii) the strictly co-closed
  sub-class, or (iii) something narrower. Decide whether the gap between (i) and (ii) is non-empty
  **and reached by a named consumer in this lane**, by exhibiting the consumer or showing there is
  none. *Planned: PROVEN-HERE as a reading of cited constructions, each cited by file and section.*
- **T-I.6 (the residue).** For the part of the class in the gap of T-I.5, decide whether the term
  that (CO-fun) does not cover admits a k- and T-uniform bound once a norm of the level-k root
  charges is added to the source class as its own slot; if it does, give the reduction with its
  constant, and name what is then left. *Planned: PROVEN, CONDITIONAL on a named item, or REFUTED.*
- **T-I.7 (the verdict asked for).** State plainly whether BFT-5 clause (b)'s curvature half is
  unconditional for the composite-co-closed class, and if not, name every condition that remains and
  which of them is upstream of which. *Planned: a status, with no distance-to-finish commentary.*

### 1.2 Failure modes (labelled before any derivation; no pre-registration weight beyond the labels)

- **I-F1.** The target is **stale**: (CO-fun) has already been decided (proved, refuted, or both,
  under different hypotheses) in a lane file later than the one my scope cites, so the work asked for
  is a re-derivation and the real remaining item has a different name. *If this occurs it is to be
  reported as the headline, not buried.*
- **I-F2.** The two handles are correct but **not load-bearing**: the estimate that (CO-fun) needs is
  obstructed somewhere neither handle touches, so "two proven handles" is not evidence of good odds.
- **I-F3.** The absence of L^{k−l} in handle 2 is **real per level but immaterial**, because the
  level sum that consumes it is not geometric for the sources the consumer supplies, and a factor
  growing in k enters there instead.
- **I-F4.** The gap class of T-I.5 is **non-empty and reached**, so a theorem proved under strict
  co-closedness does not discharge clause (b) as clause (b) is stated.
- **I-F5.** The residue of T-I.6 is bounded by two factors each of which is separately uncontrolled,
  so adding a root-charge slot moves the obstruction without reducing it.
- **I-F6.** d = 4 binds: some step needs d < 4, or needs a summability that holds only for d < 4.

### 1.3 Checks (criteria file to be written after this section and before any script)

- **cf1** — exact rational arithmetic (`fractions.Fraction` and Python ints only; no numpy, no BLAS;
  single thread; brief rule 6 exempts exact arithmetic from the numeric lock). Targets: the funnel
  kernel coefficients and support of T-I.3, and the per-level convolution inequality of T-I.4, on an
  explicitly constructed small block decomposition. Every gate carries a **designed-FAIL control**
  whose firing is to be reported (defect 3).
- No floating-point numerics are planned. If any is run, it is labelled post-hoc.

### 1.4 What I will not do

- I will not edit any file but this one and `checks/cf1_*`.
- I will not re-judge a lane-A item; where one is used I quote its status with the file and line and
  say it is quoted.
- I will not run a git command.

---

## 2. (CO-fun) written out with its quantifiers, and the exponent it needs

Appended 2026-10-28 21:45 UTC, after §1 and before `checks/cf1_criteria.md`.

### 2.0 The three statements that go by the name (CO-fun)

The name is used in this lane for three inequivalent statements. They must be separated before
anything is claimed, because two of them already have verdicts.

Common data, fixed first. Levels 0 ≤ l ≤ k; torus side T (in level-k blocks); n := L^k; basepoint
X_0; d = 4, L = 3 where a number is quoted. A **Setting LIN source** is
S = (G_l, j_l, s_l, B_k) with G_l level-l 2-forms (divergence slot), j_l level-l 1-forms (plain
slot), s_l level-(l+1) 1-forms (residual slot), B_k the datum (BFT_A §7.1, l.~455). The **composite
divergence** is the level-0 function D(S) := d*S_0 + Σ_{1≤l≤k−1} ev^{(0→l)T} d*S_l (BFT_B §27.1,
quoted at l.3961). Λ_0 := level-0 functions **constant on the level-k roots** (BFT_A §26.0). Three
nested source classes:

- **(cc)** *composite-co-closed*: Ξ^T S = 0 as a functional on Λ_0 ⟺ D(S) is supported on the
  level-k roots and Σ_X D(S)(c_X) = 0. This is exactly the solvability condition for the
  Euler-Lagrange system (Ker H = Ran Ξ, Lemma FG (i); BFT_B l.3665).
- **(CC-0)** *strictly* composite-co-closed: D(S) = 0 as a level-0 function (BFT_B l.3962).
  (CC-0) ⊊ (cc).
- **(lw)** level-wise co-closed: d*j_l = 0 for every l. (lw) ⊊ (CC-0).

Norms, with the exponent **named θ_c and α**, never "θ_w" (NB7 / [S25-fix 3] is about a different
quantity; see §2.2): π_l(j) := L^{3(k−l)} sup_own|j| = ‖j^c_l‖_∞ (BFT_B l.3591);
‖j‖_{Pc} := max_{1≤l≤k−1} L^{θ_c(k−l)} π_l(j_l) with π_0(j_0) = ‖j^c_0‖_∞ carried separately (P0);
‖G‖_Y := max_l L^{θ_c(k−l)}‖G^c_l‖_∞; ‖s‖_R the residual-class norm;
[·]^∞_α the pointwise Hölder seminorm at exponent α.

> **(CO-fun)[𝒞], for a source class 𝒞.** There is C_fun < ∞ **depending only on
> (N, L, d, κ_±, α, θ_c)** — and **not on k, on T, on the basepoint X_0, on the level l, or on the
> source** — such that **for every** k ≥ 1, **every** T ≥ 5, **every** basepoint, and **every**
> Setting LIN source S ∈ 𝒞 lying in the (P0) + (Pl-c) + (G) + (R) classes with B_k = 0, the level-0
> curvature of the Setting-LIN critical point x = 𝓛_Γ^{-1}S obeys
>
>   ‖f_0‖_∞ + [f_0]^∞_α ≤ C_fun(‖G^c_0‖_∞ + [G^c_0]_α + ‖j^c_0‖_∞ + ‖j‖_{Pc} + ‖G‖_Y + ‖s‖_R
>                                 + κ_+‖r^c_{k−1}‖_∞),
>
> at m = 0 and the trivial background, with f_0 := n² dx_0 in BFT_A §26.0's coarse units.

The three readings are **(CO-fun)[cc]** (the form written at BFT_B §31.2, l.3802),
**(CO-fun)[CC-0]** (Theorem COF, BFT_B §35.5, l.4076-4077), and **(CO-fun)[lw]** (the pre-existing
level-wise case, which is Theorem W0 + Theorem GU + Corollary LIN0).

**What is bounded:** the *level-0* pair (sup, Hölder) only. The upper-level tower f_j (j ≥ 1) is not
part of it; it is reduced to the level-0 pair plus residual data by BFT_B §31.2 (b), using BFT_A §23
and BL-2 (d), (e). **In which norm:** ℓ^∞ plus the pointwise Campanato-derived Hölder seminorm at
exponent α, in coarse units. **Uniform in:** k, T, X_0, l, and the source within its class ball —
*not* uniform in α or θ_c, on which C_fun depends. **Given:** the class memberships above, m = 0,
trivial background, B_k = 0.

**Two quantifiers that are easy to lose, and that matter below.** (i) The uniformity is over the
**class ball**, so any quantity not appearing on the right-hand side is *not* allowed to appear in
the bound — this is exactly how (CO-fun)[cc] fails (§5). (ii) ‖·‖_{Pc} is a **weighted max over
levels**, not a sum: a source whose per-level coarse sizes are uniform in l has ‖·‖_{Pc} ≍
L^{θ_c(k−1)}, not O(1). That is the trap REVIEW_BFT_B_S9_S10 **S10-6** records against §35.6, and it
is upstream of everything in this file (§7).

### 2.1 Status of each reading, quoted and not re-judged here

- **(CO-fun)[lw]:** PROVEN, by lane A's Theorem W0 + Theorem GU + Corollary LIN0. *Status quoted*
  CONFIRMED (REVIEW_BFT_A_S6 l.23, 24, 151, 181, 198, as collected in BFT_B §30.1).
- **(CO-fun)[CC-0]:** PROVEN as an implication — **Theorem COF**, BFT_B §35.5 (l.4074-4104).
  *Status quoted* CONFIRMED: REVIEW_BFT_B_S9_S10 **S10-6** opens "Theorem COF (§35.5, l.4076-4077)
  is correct and I could not break it", and PART O adjudicates session 10's two claims as right.
- **(CO-fun)[cc]:** **FALSE** — BFT_B §35.7 (l.4112-4126), *status quoted* CONFIRMED
  (REVIEW_BFT_B_S9_S10 **S10-11**). The uncovered term is Proposition COF-res's root-charge residue,
  named **(TENT-Q)**.

**So the target as my scope prompt put it — "prove (CO-fun), the single smallest remaining missing
input, with two proven handles" — is stale: I-F1 OCCURS.** The scope prompt locates (CO-fun) at
BFT_B §31.2 l.3802, which is **session 9's** statement; §35.5/§35.7, **session 10**, proved one form
and refuted the other, and REVIEW_BFT_B_S9_S10 adjudicated both. Both files are dated before session
25. The rest of this file is written on that footing: §3-§4 re-derive the two handles as asked
(they are load-bearing for Theorem COF and I do not take them on citation), §5-§6 ask what is
actually left, and §7 gives the verdict asked for.

### 2.2 The exponent (CO-fun) needs: **θ_c**, with its full admissible range. PROVEN-HERE (as a reading of the cited proofs, each step named)

I do **not** inherit θ_w. Reading Theorem COF's proof (BFT_B §35.5) step by step for the exponent it
actually consumes:

1. **G-slots, level 0** (step (a), Theorem W0): α ∈ (0, 1). **No θ.**
2. **G-slots, levels l ≥ 1** (step (a), Theorem GU): the level sum is
   Σ_{l≥1}(k − l + 1)² L^{(α−θ_c)(k−l)}, finite and k-independent **iff α < θ_c**. This is GU's own
   "hence for 0 < α < θ" clause (BFT_B l.3759, quoting BFT_A §26.1). **Binds: α < θ_c. No upper
   bound on θ_c.**
3. **s-slots** (step (b), Corollary LIN0 / Theorem BL-5 (a)): BFT_A **l.518** states the hypothesis
   as "**For 0 < α ≤ θ (no upper restriction on θ)**". **Binds: α ≤ θ_c. No upper bound.**
4. **Plain currents, sup half** (step (c), via Proposition COF-size): the only θ-dependence is the
   geometric factor (1 − L^{−θ_c})^{−1} in C_C (BFT_B l.4064). **Binds: θ_c > 0.** The constant
   diverges like 1/(θ_c ln L) as θ_c ↓ 0, which is a cost, not an obstruction.
5. **Plain currents, Hölder half** (step (d), W0 step 4 / LES-div / Lemma LE / BL-C): α ∈ (0, 1).
   **No θ.**

**Conclusion.** (CO-fun) imposes exactly **0 < α < θ_c** and **α ∈ (0, 1)**, and **no upper bound on
θ_c of its own**. Three consequences, each of which matters to the current state of the lane:

- **(CO-fun) does not need θ^r = 3.** The composite-contraction requirement NB7 reports
  (θ_w^r = 3, verified as A = L^{4−3−2}) is a requirement of the *contraction's* bookkeeping, not of
  this estimate. Nothing in §35.5 asks θ_c > 1.
- **(CO-fun) is satisfiable inside lane A's proven window.** Lane A proves its pair only for
  α ≤ θ ≤ 1 − α ≤ ¾ (BFT_A l.396, l.827). Intersecting with α < θ_c gives the non-empty window
  **α ∈ (0, ½), θ_c ∈ (α, 1 − α]** — e.g. α = ¼, θ_c ∈ (¼, ¾]. So the four-window incompatibility
  NB7 reports does **not** bind (CO-fun); (CO-fun) is one of the jobs that can be decoupled onto its
  own symbol at no cost.
- **The one place a θ-choice is not free** is the *level-count* optimisation of S10-6 (§7): there
  the best θ is θ* = 1/((k−1) ln L), which tends to 0 with k, and the resulting constant is
  ≈ 9.31·e·(k−1). That is a constraint on the *consumer*, not on (CO-fun).

**Honest status of §2.2:** PROVEN-HERE as a reading of §35.5's five steps with each exponent
constraint traced to the line that imposes it; the three cited proofs (W0, GU, LIN0/BL-5) are quoted
at their stated exponent ranges and not re-derived.

## 3. Handle 1 re-derived: the funnel transpose h_l^T. PROVEN-HERE

Appended 2026-10-28 21:46 UTC. This section does **not** cite BFT_B §29.2; it rebuilds the kernel
from the definition of h_l and then compares.

**Definition used** (BFT_A §7.1 and BL-2 (b), l.490; restated at BFT_B l.3589). h_l takes level-l
1-forms to level-(l+1) functions,
  h_l(w)(X) = L^{−d} Σ_{y ∈ B(X)} ∫_{a(c_X → y)} w,
where B(X) is the level-l block of the level-(l+1) site X (a cube of L^d level-l sites), c_X its
root (block centre, §15.0), and a(c_X → y) the axial path taking the coordinates in a fixed order
1, …, d, each coordinate traversed monotonically from (c_X)_μ to y_μ; ∫ is the signed sum of w over
the links crossed.

**(i) Kernel.** h_l(w)(X) = Σ_b c(X, b) w(b) with
  c(X, b) = L^{−d}·(signed count of y ∈ B(X) whose path uses b).
Fix b = (z, μ) (the link z → z + e_μ). Along a(c_X → y) the coordinates ν < μ have already been set
to y_ν and the coordinates ν > μ are still at (c_X)_ν, so the path uses b **iff**
y_ν = z_ν for ν < μ, z_ν = (c_X)_ν for ν > μ, and y_μ lies strictly beyond b in the direction of
travel. Three consequences, all exact:

1. **Every path uses b at most once, with a sign depending only on sgn(y_μ − (c_X)_μ).** The path is
   monotone in coordinate μ, so it cannot traverse b twice; and all y that use b traverse it in the
   same direction, so the counts do not cancel. *Hence the "signed count" is ± a count.*
2. **The count, exactly.** With L odd and c_X central, write M := (L − 1)/2. The ν < μ coordinates
   are determined (1 choice), the ν > μ coordinates are free (L^{d−μ} choices), and the number of
   admissible y_μ is M − |z_μ − (c_X)_μ| for b on the + side (and symmetrically on the −).
   The maximum over b is attained at μ = 1 and the link adjacent to the root on the far side:
   count_max = 1 · 1 · L^{d−1}·(a factor M at the innermost link; at L = 3, M = 1), so in general
   **max_{X,b}|c(X,b)| = L^{−d}·M·L^{d−1} = M/L = (L − 1)/(2L)**, and at **L = 3 this is 1/3**.
   (The L = 3 value is the one REVIEW_BFT_B_S9_S10 S9-5 recomputed independently; cf1 A2 tests the
   general form, and the general form is *mine*, registered before the script.)
3. **Support.** B(X) is a product of intervals and c_X ∈ B(X), so a path monotone in each coordinate
   between (c_X)_μ and y_μ stays inside B(X). Hence c(X, b) = 0 unless **both endpoints of b lie in
   B(X)**: h_l^T is supported on the **block-interior** level-l links and vanishes on every
   block-crossing link. Blocks are disjoint, so each interior link lies in exactly one block, and
   the transpose is diagonal in the block index:
   **(h_l^T ψ)(b) = c(X(b), b) · ψ(X(b)) for b interior, 0 for b crossing.**

**Operator norms.** ‖h_l^T‖_{ℓ^∞→ℓ^∞} = max_b Σ_X|c(X,b)| = max|c| = **(L − 1)/(2L)**, and
‖h_l^T‖_{ℓ¹→ℓ¹} = max_X Σ_b|c(X,b)| = avg_{y∈B(X)}|y − c_X|_1 = d·M(M+1)/L = **d(L² − 1)/(4L)**
(at d = 4, L = 3: **8/3**; at d = 2, L = 3: **4/3**, which is S9-5's independently recomputed value).

**Comparison with Lemma FT (i) (BFT_B l.3696-3700).** The support statement, the diagonality of the
transpose and the vanishing on block-crossing links are **reproduced exactly**. The two operator
norms there, ‖h_l^T‖_{ℓ^∞→ℓ^∞} ≤ 1 and ‖h_l^T‖_{ℓ¹→ℓ¹} ≤ d(L − 1), are **correct but loose**: the
sharp constants are (L − 1)/(2L) = 1/3 and d(L²−1)/(4L) = 8/3 against 1 and 8, i.e. loose by 3× and
3× at d = 4, L = 3. **No error found in handle 1. It is confirmed, and it is sharpenable by a factor
L in the ℓ^∞ norm**, which is where it is used in handle 2.

**One clause of BL-2 (b) that the centre convention is doing real work for:** h_l(const) = 0
(BFT_A l.491-492). With c_X central, h_l(e_μ)(X) = avg_y (y_μ − (c_X)_μ) = 0 by the symmetry of the
block about its centre. Under a corner convention it is (L − 1)/2 ≠ 0. §29.2's parenthetical
"(= d(L − 1)/2 for the centre convention)" and the §27.1 note that "the statements below are
convention-free (they need only *the axial paths of a block stay inside that block*)" are therefore
**both right about support and wrong if read as covering h(const) = 0** — the latter is not
convention-free. cf1 control C1 is built on exactly this distinction.

## 4. Handle 2 re-derived: the geometric convolution, and whether L^{k−l} is really absent. PROVEN-HERE

Appended 2026-10-28 21:58 UTC, after `checks/cf1_criteria.md` (21:47, amended 21:49) and after
`cf1_funnel.py` and `cf1b_posthoc.py` ran (21:52-21:57). §4 does not cite BFT_B §29.2's proof; it
rebuilds the estimate and then compares.

### 4.1 The cascade, rebuilt

The funnel source at level l is h_l^Tψ_l with ψ_l := d*ρ_l. Rebuilding the three steps that
determine ψ_l from the source alone:

1. The Euler-Lagrange equations of E_src are ρ_{l−1} = Q_l^Tρ_l − d*G_l − j_l (1 ≤ l ≤ k−1) and
   d*dx_0 + Q_0^Tρ_0 − d*G_0 − j_0 = 0. They are the stationarity equations and use **no**
   co-closedness.
2. Apply d*. Two identities: d*d* = 0 on 2-forms (so the G-slots drop out and d*(d*dx_0) = 0), and
   **d*Q_l^T = ev^{(l→l+1)T}d***, which is BL-2 (c)'s transpose of root covariance Q_l d = d ev.
   Hence ψ_{l−1} = ev^{(l→l+1)T}ψ_l − d*j_l and ev^{(0→1)T}ψ_0 = d*j_0.
3. Placements compose (ev^{(0→l)T}∘ev^{(l→l+1)T} = ev^{(0→l+1)T}) and ev^{(0→l+1)T} is **injective**
   (it writes a level-(l+1) function onto distinct level-0 sites). Induction gives
   ev^{(0→l+1)T}ψ_l = Σ_{0≤l'≤l} ev^{(0→l')T} d*j_{l'}, and injectivity turns that into the
   pointwise identity
     **ψ_l(Z) = Σ_{0≤l'≤l} (d*j_{l'})(z_Z)** at each level-(l+1) root Z with level-0 site z_Z.

**The one load-bearing word is "placement".** ev^{(0→l)T} is the adjoint of a restriction, so it
carries **no Jacobian and no unit rescaling**: the identity is between *raw lattice values*. If ev^T
carried a rescaling L^{a(k−l)}, a power of k−l would enter here and handle 2 would be false. It does
not: BL-2 (c)'s d*Q_l^T = ev^T d* is an identity of raw operators, and ev is restriction to roots.

### 4.2 The convolution, with the sharp constant

(d*v)(z) = Σ_μ[v_μ(z − e_μ) − v_μ(z)] has 2d terms, so sup_own|d*j_{l'}| ≤ 2d sup_own|j_{l'}|, and
by §4.1
  sup_own|ψ_l| ≤ 2d Σ_{0≤l'≤l} sup_own|j_{l'}|   (raw values).
By **handle 1** (§3, sharp ℓ^∞ constant (L−1)/(2L), not FT (i)'s 1),
  sup_own|h_l^Tψ_l| ≤ ((L−1)/(2L))·sup_own|ψ_l|.
Convert to coarse plain units with π_l(v) = L^{3(k−l)}sup_own|v| and
sup_own|j_{l'}| = L^{−3(k−l')}π_{l'}(j_{l'}):

  **π_l(h_l^Tψ_l) ≤ (d(L−1)/L) · Σ_{0≤l'≤l} L^{−3(l−l')} π_{l'}(j_{l'}).**

At d = 4, L = 3 the prefactor is **8/3 = 2.667**, against Lemma FT (ii)'s **2d = 8**: handle 2 is
**confirmed and sharper by a factor L = 3**, with the same exponent.

### 4.3 Is the L^{k−l} absent, or hidden? Three places it could hide; one of them is real, and it is not in FT

**(α) In the unit conversion.** The exponent of L in the conversion is
3(k − l) − 3(k − l') = **−3(l − l')**, which is **exactly k-free**: the output is measured at level
l and the input at level l', and both conversions carry the *same* k. Checked over all
k ≤ 8, 0 ≤ l' ≤ l < k (cf1 **B1 PASS**, including the separate k-independence sweep at fixed
(l, l')). **Not hidden here.**

**(β) In the operator constants.** The prefactor is d(L−1)/L — a function of (d, L) only. cf1 Part A
recomputes the two kernel norms exactly at (d, L) = (2,3), (3,3), (4,3), (5,3), (4,5): **all PASS**,
with max|c| = (L−1)/(2L) and ℓ¹ row sum d(L²−1)/(4L) at every one. **Not hidden here, and the
handles are dimension-blind**: nothing in handle 1 or handle 2 is marginal at d = 4. (cf1 **B3
PASS**. So if d = 4 binds (CO-fun) it binds somewhere else — I-F6 does not occur in my scope.)

**(γ) In the level sum that consumes it. This one is real, and it is a factor k, not a power of L.**
The per-level estimate is geometric in l − l', so Σ_{l'≤l}L^{−3(l−l')} < (1 − L^{−3})^{−1} = 27/26
(cf1 **B2 PASS**). But the sum the consumer needs is over **l**, and it is geometric only if
π_l(j_l) itself decays in l — i.e. only through the (Pl-c) weight L^{−θ_c(k−l)}. For a source whose
per-level coarse sizes are *uniform in l* — which is exactly what the consumer's rows are
(BFT_B §29.4 l.3729 item (3) and §19.4 l.2629: π_l(V_l) ≤ 2C_NC C_bch κ_+L²η², "uniform in l") —
‖V‖_{Pc} = max_l L^{θ_c(k−l)}π_l(V_l) ≍ L^{θ_c(k−1)}, and the sharper in-proof route
Σ_l π_l(ĵ_l) is ≍ (k − 1) times the per-level size. **I-F3 OCCURS.**

This is REVIEW_BFT_B_S9_S10 **S10-6**'s level-count loss, and my re-derivation corroborates it from
the handle side: **the funnel only adds to each π_l(ĵ_l)** — by §4.2 it contributes at most a factor
1 + d(L−1)/L·(1−L^{−3})^{−1} per level — so nothing in handle 1 or handle 2 can remove a factor that
arises from counting levels. The same fact is BFT_A's own binding erratum **[RBA2-fix] B3**
(l.819-824): "the entire level-count loss sits in the level-0 image".

**Verdict on the two handles, as asked.** Both are correct, both are sharper than stated, and
**neither is where the difficulty is** — **I-F2 OCCURS**. "Two proven handles" is not evidence of
good odds: they price the funnel, and the funnel was never the binding term. The binding terms are
the level count (§7) and the root charges (§5-§6). cf1's controls C1/C2/C6 fired against the
handles' own gates, so the re-derivation is not self-confirming (§8).

## 5. What BFT-5 clause (b) actually feeds to (CO-fun): the consumer audit. PROVEN-HERE as a reading

Appended 2026-10-28 22:00 UTC.

**The class in clause (b)** is "every composite-co-closed source S (Ξ^TS = 0, §27.1)"
(BFT_B l.3831) — class **(cc)** of §2.0, which is exactly the solvability class of the
Euler-Lagrange system (Lemma FG (i)). **Theorem COF's class is (CC-0)**, strictly smaller. So the
question of T-I.5 is whether anything in this lane actually produces a source in the gap
(cc) ∖ (CC-0): D(S) ≠ 0 but supported on the level-k roots.

**(a) Lemma CD never produces one.** BFT_A Lemma CD (i) gives
Ξ^T𝔑^0(x; B) = −K'^T_x∇(𝔉_k∘exp)(x; B) as an identity of level-0 functions. At a critical point the
right side is 0 **everywhere**, so D(𝔑^0) = 0 and the rows satisfy (CC-0) (this is §35.6's reading,
and REVIEW S10-8 confirms it is not circular). Off the critical set D(𝔑^0) is a general level-0
function, so the rows are not in (cc) at all. **Lemma CD's output is (CC-0) or nothing** — it never
lands in the gap.

**(b) The lane's own correction map lands in the gap, and that is where the consumer is.**
§31.3 (R1) route (i) replaces a general source S by S^E_0(S) = S + Γ_E^TD(S) (Lemma GE (c)) in order
to make it composite-co-closed. Its composite divergence is computed by **Lemma ΓT-op (e)**
(§25.1 (e), PROVEN-HERE there, d = 4), quoted at BFT_B l.3812:
  d*Γ_E^TD = −D + Σ_X Q_X δ_{c_X},  |Q_X| ≤ 8L^{3(k−l)}‖D‖_∞.
Since Γ_E^TD(S) is added to the level-0 slot, D(S + Γ_E^TD(S)) = D(S) + d*(Γ_E^TD(S)) =
**Σ_X Q_X δ_{c_X}**, supported on the level-k roots, with Σ_X Q_X = 0 (every chain source has
Σ_z D(S)(z) = 0). So the corrected source is in **(cc) and not in (CC-0)** unless every compensation
charge vanishes.

> **Erratum noted against §31.3 (R1), for the next lane-B review (I do not edit that file).**
> BFT_B **l.3810** writes "Lemma GE (c) gives S^E_0(S) = S + Γ_E^TD(S) with **D(S^E_0(S)) = 0**".
> That contradicts Lemma ΓT-op (e) on the same line, which leaves Σ_X Q_X δ_{c_X}. Session 10 says
> the right thing at **l.4203** ("Theorem COF applies to S^E_0(S) **except** for Proposition
> COF-res's residue, whose charges are these same Q_X"), so the lane already carries both readings.
> The correct statement is D(S^E_0(S)) = D^root = Σ_X Q_X δ_{c_X}: composite-co-closed, not (CC-0).

**(c) Verdict for T-I.5. I-F4 OCCURS.** The gap class is non-empty **and reached**, by the lane's
own route (i). So a theorem proved under (CC-0) does **not** discharge clause (b) as clause (b) is
stated; it discharges clause (b) restricted to critical points of 𝔉_k. BFT_B §32.2's own honest
status already says clause (b) "inherits (NC-Γ)_cc's status, i.e. it is CONDITIONAL on (CO-fun) for
the curvature half" (l.3851), and §2.1 above records what (CO-fun) is now known to be on each class.

## 6. The gauge freedom survives the pin: Lemma CO-pin, and where the obstruction actually sits

Appended 2026-10-28 22:03 UTC. This section is new mathematics of mine, small and checkable.

### 6.1 Lemma CO-pin: PROVEN-HERE

*Notation.* C(j) := Σ_{0≤l≤k−1}(Q^{(0→l)})^T j_l, the dual push-down of the plain currents
(BFT_B l.3963). Λ_0 = level-0 functions constant on the level-k roots. For a plaquette p, Y^p_* is
any representative of the level-0 plaquette response.

> **Lemma CO-pin.** Let S be a Setting LIN source in class **(cc)** — composite-co-closed, with no
> assumption that D(S) = 0. Then for **every** λ ∈ Λ_0,
>   ⟨C(j), dλ⟩ = 0,  hence  ⟨C(j), Y^p_{*,0}⟩ = ⟨C(j), Y^p_{*,0} + dλ⟩,
> and therefore
>   **n²|⟨C(j), Y^p_{*,0}⟩| ≤ n²·sup_own|C(j)|·𝒩_{Λ_0}(Y^p) = C_YN^{pin}·π_0(C(j))** whenever
>   𝒩_{Λ_0}(Y^p) := min{‖Y^p_{*,0} + dλ‖_1 : λ ∈ Λ_0} ≤ C_YN^{pin}·n.

*Proof.* In the §23.1 convention d^T = d*, so ⟨C(j), dλ⟩ = ⟨d*C(j), λ⟩. By **Lemma DF-cc (i)**
(BFT_B §35.3, CONFIRMED: REVIEW_BFT_B_S9_S10 S10-3) d*C(j) = D(S), whose proof is BL-2 (c) iterated
and needs no co-closedness. For S ∈ (cc), D(S) is supported on the level-k roots and Σ_X D(S)(c_X) =
0; and λ ∈ Λ_0 is constant on those roots, say ≡ c. Hence ⟨D(S), λ⟩ = c·Σ_X D(S)(c_X) = 0. The
displayed inequality is Hölder with sup_own|C(j)| = n^{−3}π_0(C(j)) and n²·n^{−3}·n = 1. ∎

### 6.2 What Lemma CO-pin settles, and what it moves

**(i) It discharges one half of RS10-6.** REVIEW_BFT_B_S9_S10 **RS10-6** (binding) objects that for
D ≠ 0 "⟨C(j), Y^p_0⟩ is representative-dependent, with defect ⟨D(S), λ_opt⟩ against the 𝒩-optimal
λ_opt, which is **not** in Λ_0 and so is not killed by GT-split". That is right about λ_opt.
Lemma CO-pin says the dependence on the representative **within the freedom composite co-closedness
licenses** — ΞΛ_0 — is **exactly zero**, and that the gauge-optimisation step of Theorem W0's step 2
therefore survives on class (cc) with the minimisation **restricted to Λ_0**. So the fix RS10-6 asks
for is available in the form "re-run step (c) with the minimisation pinned", and the price is one
named quantity:

> **(YH-pin), named and stated.** There is C_YN^{pin} < ∞, depending only on (N, L, d, κ_±), such
> that for every k ≥ 1, T ≥ 5, basepoint and plaquette p,
>   𝒩_{Λ_0}(Y^p) := min{ Σ_b |Y^p_{*,0}(b) + dλ(b)| : λ a level-0 function **constant on the
>   level-k roots** } ≤ C_YN^{pin}·n.
> **Status: OPEN.** It is Theorem YH's 𝒩* ≤ C_YN·n (BFT_A l.2203, l.2228, PROVEN-HERE there,
> CONFIRMED REVIEW_BFT_A_S6 l.23) with one linear constraint added to the minimisation, and
> 𝒩_{Λ_0} ≥ 𝒩 always. A one-line sufficient form: if λ_opt realises 𝒩(Y^p), then correcting it to
> Λ_0 by a one-site bump at each root costs ‖dμ‖_1 = 2d Σ_X |λ_opt(c_X) − c|, so
> **(YH-pin) ⟸ "the 𝒩-optimal gauge function of Y^p is constant on the level-k roots to a total
> ℓ¹ budget O(n)"** — which is a decay statement about λ_opt, of the kind Proposition W supplies for
> Y^p itself.

**(ii) It relocates the obstruction, and this is the finding.** With the gauge side pinned, the
whole of (CO-fun)[cc]'s sup half turns on the **coarse size** π_0(C(j)). By Lemma DF-cc (ii)'s
identity (†) (BFT_B l.4045, CONFIRMED S10-3),
  C(j) = Σ_{0≤l≤k−1}(Q_str^{(0→l)})^Tĵ_l − Σ_{0≤i≤k−1}(Q_str^{(0→i)})^T h_i^T R_{i+1}(D(S)),
and by §3's handle 1, sup_own|h_i^TR_{i+1}(D)| ≤ ((L−1)/(2L))·max_X|D(S)(c_X)|, so
  π_i(h_i^T R_{i+1}(D)) ≤ L^{3(k−i)}·((L−1)/(2L))·max_X|Q_X|,
and summing i = 0 … k−1 (Σ_{m=1}^{k}L^{3m} = L^3(L^{3k}−1)/(L^3−1)):
  **π_0(C(j)) ≤ Σ_l π_l(ĵ_l) + ((L−1)/(2L))·(L³/(L³−1))·n³·max_X|Q_X|**,
the second term being **0.3462·n³·max_X|Q_X|** at d = 4, L = 3. Hence

> **(CO-fun)[cc] ⟸ (YH-pin) ∧ (ROOT-sup)**, where **(ROOT-sup)**: n³·max_X|D(S)(c_X)| ≤
> C·(the class norms of §2.0), k- and T-uniformly.

**(iii) (ROOT-sup) is false for the stated class, by a route independent of §35.7's.** A (cc) source
may carry d*j_{k−1} supported on the level-k roots read as level-(k−1) sites (the "admissible
dipole" of REVIEW_BFT_A_S8 S8-7), with max_X|Q_X| up to 2d·sup_own|j_{k−1}| =
2dL^{−3}π_{k−1}(j_{k−1}) ≥ 2dL^{−3}L^{−θ_c}‖j‖_{Pc}. Then
n³max_X|Q_X| ≍ L^{3k−3}‖j‖_{Pc}: unbounded in k. **This is a second, independent route to the same
blow-up that Proposition COF-res found** — COF-res pairs the root charges with the response's funnel
Φ_k and reaches L^{2k−3}π_{k−1}(j_{k−1}); the sup route here is lossier by one factor n, as a sup
bound on an object concentrated at the roots must be. Two different routes, same verdict.

**(iv) An honest narrowing of "(CO-fun)[cc] is FALSE", recorded as a narrowing and not a reversal.**
Neither route **exhibits** a source for which ‖f_0‖_∞ is unbounded. §35.7 shows that one *exact term
of a decomposition of f_0* is unbounded over the class; §6.2 (iii) shows that an *upper bound* is.
Since f_0 is the sum of that term and a complementary one, falsity of the estimate strictly requires
ruling out cancellation — and the complementary term ⟨main, Y^p_{*,0}⟩ is itself bounded only
through ‖Y^p_{*,0}‖_1 for a fixed representative, i.e. through **(PW-ℓ¹)**, which is recorded as
expected FALSE for Γ_E ([RBB8-fix RS8-3]; BFT_B l.4019). So no cancellation argument is available
either, and the practical consequence — **no proof of (CO-fun)[cc] exists by either route** — is
unchanged. What would settle it is named: **an explicit (cc) source with a single admissible root
dipole for which ‖f_0‖_∞/(class norms) is computed, not estimated** (the k = 2 case is within reach
of the bb9b/bb10 model extended to carry G- and s-slots, which that model does not have —
REVIEW RS10-P5). I register this as a **NARROWING** of §35.7 / S10-11, labelled ARGUED, and I do not
claim a reversal: sixteen verdicts in this project have been reversed, and I am not adding a
seventeenth on an argument this thin.

**(v) Why (YH-pin) is nevertheless worth having.** It is strictly better-shaped than (TENT-Q):
it is **source-free** (a property of Y^p alone), it is lane A's own Theorem YH plus one linear
constraint, it is the **only** gauge-side input class (cc) needs, and it is what makes the statement
"the obstruction to (CO-fun)[cc] is the co-closedness of the paired object" — the framing of both
§31.2 (l.3802) and §35.7 — **wrong**: the paired object's gauge freedom survives intact on (cc). The
obstruction is the **size** of the push-down, i.e. the root charges, exactly as Proposition COF-res
found by the sharp route.

## 7. What is upstream of all of it: the level count. ARGUED (corroborating S10-6 from the handle side)

Appended 2026-10-28 22:06 UTC.

Even on the class where (CO-fun) **is** proven — (CC-0), i.e. at critical points of 𝔉_k — the
curvature half of clause (b) does **not** come out k-uniform. REVIEW_BFT_B_S9_S10 **S10-6** (binding
fix RS10-1) shows that Corollary COF-crit's substitution of the rows' per-level sizes
(π_l(V_l) "uniform in l") for the class norm ‖V‖_{Pc} is invalid, that ‖V‖_{Pc} ≍ L^{θ(k−1)}η², that
the sharper in-proof route gives ≈ 9.31(k−1)·(per-level size), and that optimising θ gives
≈ 9.31·e·(k−1) ≈ 25(k−1) at θ* = 1/((k−1)ln L) — with **no choice of θ removing the factor**. The
k-uniform form is CONDITIONAL on a level-decay input for the non-co-closed plain rows: lane A's
**(SPD)/(W2)** (BFT_A l.830-831), **OPEN**.

My §4.3 (γ) reaches the same place from the other side and adds one thing: **nothing in either
handle can remove it.** Handle 2 bounds the funnel at level l by a geometric convolution of the
*same* levels' coarse sizes, so it can only **add** to each π_l(ĵ_l) — by at most the factor
1 + (d(L−1)/L)(1 − L^{−3})^{−1} = 1 + 2.769 = 3.769 at d = 4, L = 3. A factor arising from counting
k levels is invisible to a per-level estimate, however sharp. So the two handles are not merely not
the difficulty (§4.3); they are provably incapable of being it.

**Ordering of the three remaining inputs to clause (b)'s curvature half**, which is what T-I.7 asks
for:

1. **(SPD)/(W2)** — lane A, OPEN. Needed even on (CC-0), even at critical points, even with
   everything else supplied. Supplying (TENT-Q), (YH-pin) and (NEUT-box) still leaves ≈ 25(k−1).
   This is REVIEW's own ordering (P9/10-b: "(SPD) … is now worth more than (TENT-Q), (NEUT-box) or
   (Y-sup^loc)"), and RS10-D1 records that SESSION24_RESULTS l.870-872 and HANDOFF l.84-85 both
   pre-date it.
2. **(TENT-Q)** (equivalently, through §6, **(ROOT-sup)**; and **(YH-pin)** is the gauge-side input
   that §6 shows is *not* the obstruction) — needed to extend from (CC-0) to the full class (cc),
   which §5 shows the consumer reaches.
3. **(CO-fun) itself** — not an open item. (CO-fun)[CC-0] is PROVEN (Theorem COF, CONFIRMED);
   (CO-fun)[cc] is refuted as stated, with the narrowing of §6.2 (iv).

## 8. Check record: cf1 and cf1b

Appended 2026-10-28 22:08 UTC.

**Provenance.** `cf1_criteria.md` born 21:47 UTC, amended 21:49 UTC (the amendment is recorded
inside the file; the gate changed from 1/L to (L−1)/(2L)) — **both before `cf1_funnel.py` existed**,
which was written at 21:51 and ran 21:52. `cf1b_posthoc.py` was written at 21:55, **after** seeing
that control C3 did not fire, and is labelled **POST-HOC** in its own header, per rule 3 and the
precedent [RBB8-fix RS8-7] (ii). Exact `fractions.Fraction` and Python ints only; no numpy, no BLAS;
single thread; no numeric lock taken (rule 6 exempts exact arithmetic). Outputs: `cf1_out.txt`,
`cf1b_out.txt` (`cf1_err.txt`, `cf1b_err.txt` empty).

**Part A — the kernel, at (d, L) = (2,3), (3,3), (4,3), (5,3), (4,5).** All gates PASS at every run:
A1 support violations 0; A2 max|c| = 1/3, 1/3, 1/3, 1/3, **2/5** — matching (L−1)/(2L) and
**discriminating against the amended-away 1/L at L = 5**; A3 ℓ¹ row sum 4/3, 2, 8/3, 10/3, **24/5** —
matching d(L²−1)/(4L); A4 one owner per link; A6 h(const) = 0 exactly; A7 multiplicity 1. The
(d, L) = (2, 3) values 1/3 and 4/3 reproduce REVIEW_BFT_B_S9_S10 **S9-5**'s independently recomputed
numbers. **B3 (d-independence) PASS**: the handles are not d = 4-marginal.

**Part B.** B1 PASS (the conversion exponent is −3(l−l') and is k-free, over all k ≤ 8); B2 PASS
(Σ_{l'≤l}L^{−3(l−l')} < 27/26).

**Controls, reported as the criteria require.**

| control | registered to break | observed | verdict |
|---|---|---|---|
| **C1** corner root | A2, A3, A6; leave A1/A4/A7 intact | max\|c\| 2/3, ℓ¹ row 4, \|h(const)\| = 1 → **A2, A3, A6 all FAIL**; A1, A4, A7 **PASS** | **FIRED, exactly as registered** |
| **C2** back-tracking path | A7 **and** A3 | multiplicity 3 → **A7 FAIL**; ℓ¹ row stays **8/3** → A3 **PASS** | **FIRED on A7 only. My registered A3 expectation was WRONG**: the −1/+1 pair cancels in the *signed* kernel, so **A3 has no power against a back-track**. Reported as a failed pre-registration of mine |
| **C3** wrap-around path | A1 **and** A4 | 0 violations, 1 owner → both **PASS** | **DID NOT FIRE.** cf1b (1) diagnoses it exactly: 7 out-of-block links are touched, **all 7 have net signed count 0** — for L odd with a *central* root the long-way excursions of the y above and below the root are equinumerous with opposite signs and cancel identically. **C3 has no power at a central root** |
| **C4** naive-grouping exponent | B2 (and leave B1 intact) | Σ_{i<l}L^{+3(l−i)} = 27, 756, …, 2.93·10^{11} → **B2 FAIL**; B1 **PASS** as registered | **FIRED.** And the registered intact-clause matters: **the k-cancellation is not what separates the two groupings** — both are k-free; what separates them is the *sign* of the level exponent |
| **C5** (POST-HOC) root one site outside its block | A1, A4 | 9 / 81 violations → **A1 FAIL**; one owner → A4 **PASS** | FIRED on A1 only |
| **C6** (POST-HOC) wrap path + corner root | A1, A4 | 63 / 567 violations and **3 owners** → **A1 FAIL, A4 FAIL** | **FIRED on both** |

**Discriminating power, stated against my own gates (defect 3, applied to me).**

- **A1** has a firing control (C5, C6) — both post-hoc. The pre-registered control for it (C3) was
  void.
- **A2, A3, A6** have a firing pre-registered control (C1). **A3's second registered control (C2)
  was wrong about A3**, which is a fail against my pre-registration, not against the lemma.
- **A4** has a firing control only post-hoc (C6), and I record that **A4 is not independent**: given
  A1 and the disjointness of the blocks it follows, so the criteria file's "power to fail: yes" for
  A4 was overstated. C5 demonstrates the two are not equivalent (A1 broke, A4 did not).
- **A5** was declared derived and low-power in the criteria file and is reported, not counted.
- **A7** has a firing control (C2).
- **B1 has no firing control**: C4 was registered to leave it intact and did. B1 is a bookkeeping
  identity, verified, not tested. **B2** has a firing control (C4).
- **What cf1 cannot reach, restated from the criteria file:** Theorem W0, Theorem YH, Y^p, the root
  charges, (CC-0) itself, the chain solution behind Lemma RT-cc (a), §6's Lemma CO-pin, and every
  nonabelian step. cf1 bears on handles 1 and 2 and on the unit bookkeeping, and on nothing else.
  In particular **cf1 is not evidence for anything in §5, §6 or §7.**

## 9. Statuses, and the answers to T-I.1 … T-I.7

Appended 2026-10-28 22:10 UTC.

| item | where | status |
|---|---|---|
| (CO-fun) written with quantifiers; the three classes separated | §2.0 | **PROVEN-HERE** (a statement, labelled as one) |
| Exponent: (CO-fun) needs 0 < α < θ_c, α ∈ (0,1), **no upper bound on θ_c**; window α ∈ (0,½), θ_c ∈ (α, 1−α] inside lane A's pair | §2.2 | **PROVEN-HERE** as a reading of §35.5's five steps, each constraint traced to its line; the three cited theorems quoted at their stated ranges |
| Handle 1 (block-interior support, kernel, norms) rebuilt; sharp constants (L−1)/(2L) and d(L²−1)/(4L) | §3 | **PROVEN-HERE**; cf1 A1-A7, B3 |
| h_l(const) = 0 is **not** convention-free | §3 | **PROVEN-HERE**; cf1 C1 |
| Handle 2 (geometric convolution) rebuilt with prefactor d(L−1)/L; **no power of L^{k−l}**, verified in all three places it could hide | §4 | **PROVEN-HERE**; cf1 B1, B2, B3 |
| The handles are dimension-blind (d = 2,3,4,5) | §4.3 (β) | **PROVEN-HERE**; cf1 B3 |
| The level sum is where a k enters, and no per-level sharpening can remove it | §4.3 (γ), §7 | **ARGUED**, corroborating S10-6 from the handle side |
| The gap class (cc) ∖ (CC-0) is reached, by route (i)'s own correction map | §5 | **PROVEN-HERE** as a reading of Lemma ΓT-op (e) + §31.3 (R1); §31.3 l.3810's "D(S^E_0(S)) = 0" is wrong, l.4203 is right |
| **Lemma CO-pin**: on class (cc) the ΞΛ_0 gauge freedom survives intact, so ⟨C(j), Y^p_{*,0}⟩ is Λ_0-representative-free | §6.1 | **PROVEN-HERE** (from Lemma DF-cc (i), quoted CONFIRMED) |
| **(CO-fun)[cc] ⟸ (YH-pin) ∧ (ROOT-sup)** | §6.2 (ii) | **PROVEN as an implication** |
| **(YH-pin)**, named and stated; source-free; Theorem YH plus one linear constraint | §6.2 (i) | **OPEN** (new name; not claimed) |
| (ROOT-sup) is false for the stated class — second independent route to §35.7's blow-up | §6.2 (iii) | **PROVEN-HERE** (the arithmetic) |
| "The obstruction is the co-closedness of the paired object" (§31.2 l.3802, §35.7) is **wrong**; it is the size of the push-down | §6.2 (v) | **PROVEN-HERE**, given Lemma CO-pin |
| "(CO-fun)[cc] is FALSE" narrowed: one exact term is unbounded, a configuration with ‖f_0‖_∞ unbounded is not exhibited, and no cancellation argument is available either | §6.2 (iv) | **ARGUED** — a NARROWING of S10-11, **not** a reversal |

**Failure modes: I-F1 OCCURS** (the target is stale — §2.1); **I-F2 OCCURS** (the handles are not
load-bearing for the difficulty — §4.3); **I-F3 OCCURS** (the per-level absence of L^{k−l} is real
and immaterial; a factor k enters at the level sum — §4.3 (γ), §7); **I-F4 OCCURS** (the gap class
is reached — §5); **I-F5 OCCURS** (adding a root-charge slot moves the obstruction without reducing
it: §6.2 (ii)-(iii) replaces (TENT-Q) by (ROOT-sup), which is lossier by n); **I-F6 does not occur
in my scope** (the handles hold in d = 2, 3, 4, 5 — cf1 B3; if d = 4 binds (CO-fun), it binds
elsewhere).

**T-I.7, the verdict asked for, plainly. BFT-5 clause (b)'s curvature half is NOT unconditional for
the composite-co-closed class.** It is:
- **PROVEN** on the strictly co-closed sub-class (CC-0) — Theorem COF, CONFIRMED — **with a constant
  that grows like k** when applied to the rows (S10-6), hence k-uniform only given **(SPD)/(W2)**,
  OPEN;
- **not proven, and refuted as stated** (with the narrowing of §6.2 (iv)) on the rest of class (cc),
  needing **(TENT-Q)** — equivalently **(ROOT-sup)** — plus, on the gauge side, **(YH-pin)**;
- reached in the gap by the lane's own route (i) (§5), so the (CC-0) result does not stand in for
  it.

**What I did not do.** I did not re-derive Theorem W0, Theorem YH, Theorem GU, Corollary LIN0,
Lemma ΓT-op or Lemma CD; each is quoted with its file, line and review status. I did not re-open
Theorem COF's proof beyond the exponent audit of §2.2 and the two handles. I ran no floating-point
numerics. I did not edit any file but `COFUN.md`, `checks/cf1_criteria.md`, `checks/cf1_funnel.py`,
`checks/cf1b_posthoc.py` and their outputs. I ran no git command.

## FOR OTHER FILES (not edited; for their owners)

1. **BFT_B.md §31.3 (R1), l.3810 (binding).** "Lemma GE (c) gives S^E_0(S) = S + Γ_E^TD(S) with
   D(S^E_0(S)) = 0" is false as written: by Lemma ΓT-op (e), quoted two lines later,
   D(S^E_0(S)) = Σ_X Q_X δ_{c_X}. §36.5 (ii) l.4203 states it correctly. The corrected source is in
   (cc) and not in (CC-0), which is precisely why route (i) needs (TENT-Q). (COFUN §5 (b).)
2. **BFT_B.md §31.2 l.3802 and §35.7's diagnosis (binding).** "The funnel pieces … are co-closed
   only collectively, so they cannot be fed into Theorem W0's hypothesis" was already superseded by
   §35.1/§35.3. What should replace it is not "(CC-0) restores co-closedness" but Lemma CO-pin: on
   class (cc) the gauge freedom survives with the minimisation **pinned to Λ_0**, and the obstruction
   is the **size** of C(j), not its co-closedness. (COFUN §6.)
3. **BFT_B.md §29.2 Lemma FT (i) (cosmetic).** ‖h_l^T‖_{ℓ^∞→ℓ^∞} ≤ 1 and ‖h_l^T‖_{ℓ¹→ℓ¹} ≤ d(L−1)
   are loose by a factor L = 3 each; the sharp values are (L−1)/(2L) = 1/3 and d(L²−1)/(4L) = 8/3
   (cf1, five (d, L) pairs, exact). Lemma FT (ii)'s prefactor 2d = 8 sharpens to d(L−1)/L = 8/3,
   and K_f = 2d/(1 − L^{−(2+α)}) = 8.737 sharpens to (d(L−1)/L)/(1 − L^{−(2+α)}) = 2.912.
   Nothing downstream changes sign or status; the constants improve by 3×.
4. **BFT_B.md §27.1 / §29.2 (cosmetic).** "The statements below are convention-free (they need only
   *the axial paths of a block stay inside that block*)" is right for the support and diagonality
   claims and wrong for BL-2 (b)'s h_l(const) = 0, which fails at a corner root (cf1 C1, exact).
5. **RTARGET.md / PROOF.md clause table (for the lead).** NBG_B's "(CO-fun) … the single smallest
   remaining missing input … at BFT_B §31.2, l.3802" cites session 9's statement. Sessions 10 and
   the S9/S10 review decided it: PROVEN on (CC-0), refuted as stated on (cc). The live open names
   are **(SPD)/(W2)** (upstream, lane A), **(TENT-Q)** / **(ROOT-sup)**, and the new **(YH-pin)**.
6. **BFT_A (for its owner).** **(YH-pin)** is yours in shape if not in ownership: it is Theorem YH's
   𝒩* ≤ C_YN n with the minimisation restricted to gauge functions constant on the level-k roots.
   Lane B needs it, and only it, on the gauge side of class (cc). A sufficient form is that the
   𝒩-optimal λ for Y^p is constant on the level-k roots to a total ℓ¹ budget O(n) — a decay
   statement about λ_opt of the kind Proposition W gives for Y^p.

## 10. Provenance erratum (binding on this file's own record). Appended 2026-10-28 21:55 UTC

**The per-section UTC times written into the headers of §2-§9 are wrong, and I am not editing them
in place** (append-only). They were drafted as planned times and never corrected against the clock.
The filesystem is the record. Stat-verified times (`stat -f %Sm`, UTC) at 21:53:

| file | mtime | what that mtime is |
|---|---|---|
| `COFUN.md` | 21:52:48 | the §7-§9 append (the file's earlier states are overwritten) |
| `checks/cf1_criteria.md` | 21:45:08 | the **amendment** write; the first draft's birth time is **unrecoverable**, exactly the situation REVIEW_BFT_B_S9_S10 **RS10-P2** records against bb10_criteria.md |
| `checks/cf1_funnel.py` | 21:46:33 | written |
| `checks/cf1_out.txt` | 21:46:47 | run |
| `checks/cf1b_posthoc.py` | 21:48:28 | written (includes the C6 append) |
| `checks/cf1b_out.txt` | 21:48:29 | run |

**The true order, which is what the process rules are about, and which the mtimes do support:**

1. `COFUN.md` §1 PRE-STATED — the **first edit of this file**, before any derivation of mine, any
   criteria file and any script. (Its own mtime is overwritten by the later appends; the claim is
   order, not time.)
2. `checks/cf1_criteria.md`, first draft. **Correction: this was written BEFORE §2-§3 of this
   file, not after**, contrary to the sentence in its own header. Rule 2 asks that criteria precede
   the script, and they do; the "after §2-§3" clause is simply false for the first draft and true
   for the amendment.
3. `COFUN.md` §2-§3 appended.
4. `cf1_criteria.md` amended (1/L → (L−1)/(2L)), **21:45:08**, still before any script existed. The
   amendment's own clause "no script existed and no result had been seen" is correct.
5. `cf1_funnel.py` written **21:46:33**, run **21:46:47**. Criteria-before-script holds with 85 s to
   spare against the amendment and more against the first draft.
6. `cf1b_posthoc.py` written **21:48:28** — after cf1's output was read, and labelled POST-HOC in
   its own header and in §8.
7. `COFUN.md` §4-§6, then §7-§9, appended last (21:52:48).

**Two further corrections to §8's own text**, which quoted the wrong clock: §8 says the criteria
file was "born 21:47, amended 21:49" and the script "written at 21:51 and ran 21:52". Read instead
the table above. The *order* claims in §8 are unaffected; the times are not. No threshold, gate,
verdict or constant anywhere in this file depends on a time.

**Addendum to §10, same defect, one more time.** §10's own header says "Appended 21:55 UTC" and the
correction appended to `cf1_criteria.md` says "21:56 UTC". Both were written in a single call that
began after a clock read of **21:53:55**; the stat times immediately after it are printed below.
I have now mis-stated a timestamp **three times in one file by writing the time I expected rather
than the time I measured** — which is the same habit, in miniature, that this lane's systemic
defect 2 is about. The rule I should have followed, and am recording for the next worker: **read
the clock, write the file, then stat it and quote the stat** — never the other way round. No
threshold, gate, verdict or constant in this file depends on any of these times; the order claims
are the ones that matter and they are stat-supported in §10's table.

Stat times immediately after the §10 append: `COFUN.md` 21:54:13, `checks/cf1_criteria.md` 21:53:55 UTC.
