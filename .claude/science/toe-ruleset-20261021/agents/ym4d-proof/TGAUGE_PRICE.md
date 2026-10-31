# TGAUGE_PRICE: constructing μ and pricing Proposition TGAUGE's representative shift exactly — session 25 (2026-10-28 UTC)

Scope of the whole file, stated once and binding on every claim in it: **m = 0, trivial background, d = 4,
L = 3, the elliptic slice S_E (lead decision D1), abelian / linearised, su(N) componentwise in an
orthonormal basis.** Every status is one of PROVEN-HERE / PROVEN as an implication / COMPUTED (exact) /
ARGUED / CONDITIONAL (input named) / OPEN. Nothing here is offered at m > 0, at θ > 0, at a nontrivial
background, or about N.

## 1. PRE-STATED — statements only; the FIRST edit of this file, written 2026-10-28 15:23 UTC

This section is the **first edit** of TGAUGE_PRICE.md. It contains **statements only**. It cites **no
constant produced in this drive session** — in particular no numeric constant of YSUP.md or TENTQ.md
appears anywhere in §1 or in any criteria file of this lane; where those files are needed they enter as
**named hypotheses**, quoted and not re-judged, and only structurally (powers of L and of n, and the
absolute combinatorial constants 2d, 2^d of the cited lemmas).

Exploratory *reading* preceded this edit (DRIVE_BRIEF; HANDOFF; YSUP.md in full; TENTQ.md in full;
REVIEW_BFT_A_S8 §S8-7's spike rationals; BFT_B §35.3 Lemma DF-cc, §35.4 Proposition COF-size, §35.5
Theorem COF, §35.7 Proposition COF-res, §36.0-§36.2) with exploratory reasoning that is not recorded. The
only claim §1 makes is file order.

### 1.0 The objects, as cited (named inputs, quoted, not re-judged)

- **Proposition TGAUGE** (TENTQ §2.7, PROVEN-HERE there; tq1 A6): for every level-0 function μ and every
  level-k site X, **Φ_k(x_0 + dμ)(X) − Φ_k(x_0)(X) = A^{(0→k)}μ(X) − μ(c_X)**, with
  A^{(0→k)}μ(X) = L^{−dk}Σ_{s∈[0,L^k)^d}μ(L^kX + s). For μ ∈ Λ_* (μ = 0 at the level-k roots, so that
  Ξμ ∈ 𝒢_0) the change is exactly A^{(0→k)}μ(X), which can be prescribed arbitrarily.
- **Proposition YS-K** (YSUP §2.1, PROVEN-HERE there): Φ_k(v)(c_X) = Σ_{i<k}⟨K_i, v⟩ with
  K_i := (Q_str^{(0→i)})^T h_i^T δ_{Y_{i+1}}; **supp K_i is exactly the level-(i+1) block of c_X**, both ends
  attained; sup|K_i| ≤ n_i^{1−d}; ‖K_i‖_1 ≤ (8/3)n_i.
- **Theorem TQ-INT** (TENTQ §2.5, PROVEN-HERE there): with Ψ := I_χΦ = Σ_XΦ(c_X)χ^5_X,
  **𝒯_p(S) = n²Σ_{l=0}^{k−1}⟨d(ev^{(0→l)}Ψ), S_l⟩**, and the box charges are eliminated.
- **Lemma TENT-TV** (TENTQ §2.5, PROVEN-HERE there): ‖d(ev^{(0→l)}Ψ)‖_1 ≤ 2d(n/L^l)^{d−1}Σ_X|Φ(c_X) − c|
  for every constant c; and Corollary TQ-osc: |𝒯_p(S)| ≤ 2^d·2d·n²·osc_𝔅(Φ)·Σ_lπ_l(S_l) per coarse cell.
- **Proposition QN** (TENTQ §2.1, PROVEN-HERE there): Σ_X Q_X(S) = 0 for every chain source.
- **Proposition COF-res** (BFT_B §35.7, PROVEN-HERE there): for a Setting LIN^cc source with D(S) ≠ 0 the
  single extra term in f_0 not covered by Theorem COF is exactly
  **n²⟨D^root(S), h^{(0→k)}Y^p_{*,0}⟩ = n²Σ_X D(S)(c_X)·Φ_k(Y^p_{*,0})(c_X)**.
- **Lemma DF-cc (i)-(ii)** (BFT_B §35.3, PROVEN-HERE there): **d*C(j) = D(S)** with
  C(j) = Σ_{l<k}(Q^{(0→l)})^T j_l; and (†) C(j) = Σ_l(Q_str^{(0→l)})^Tĵ_l − Σ_i(Q_str^{(0→i)})^Th_i^TR_{i+1}(D(S)).
- **Theorem COF step (c)** (BFT_B §35.5): f_0[S^j](p) = n²[⟨C(j), Y^p_0⟩ − Σ_m⟨Σ_{l>m}(Q^{(m+1→l)})^Tj_l, r_m(Y^p)⟩],
  the first term bounded under (CC-0) by n²·sup_own|C(j)|·𝒩(Y^p) ≤ C_YN·π_0(C(j)) using co-closedness of
  C(j) and Theorem YH's 𝒩(Y^p) ≤ C_YN·n.
- **The profile input** (BFT_A §38.7 / Theorem YH, via YSUP §2.8 (1)): Y^p_{*,0}'s core is in the class
  |v(b)| ≤ C_0(1 + |b − p|_∞)^{−3}, co-closed. Every statement here about Y^p_{*,0} specifically is
  **CONDITIONAL** on that; statements about an arbitrary level-k function Φ are not.
- **Accepted and not claimed against:** the upstream level count (REVIEW_BFT_B_S9_S10 Part J, binding fix
  RS10-1, refuting Corollary COF-crit §35.6). **No k-uniformity for (NC-Γ) is claimed anywhere in this
  file.** (NEUT-box) is FALSE and struck (TENTQ Proposition QFALSE); it is not used.
- **(Φ-conv)** is PROVEN for this profile class (YSUP §2.5), so nothing here is conditional on it.

### 1.1 Targets of this session (written before any derivation)

- **G1 (construct μ).** Write down explicitly at least two level-0 functions μ ∈ Λ_* with
  A^{(0→k)}μ(X) = −Φ(c_X) on p's coarse cell: (a) a **flat** one, constant on each level-k block with a
  one-site correction at the root; (b) a **single-site** one, supported at one fine link-neighbour of the
  root. For each state its support, its own sup, ‖dμ‖_1, and the level-l object ‖d(A^{(0→l)}μ)‖_1 in closed
  form, as a power of L^{k−l}. State which object the main pairing actually sees: A^{(0→l)}μ (the level-l
  **block average**) or ev^{(0→l)}μ (the level-l **root value**), and say which identity fixes it.
- **G2 (price it exactly).** Compute, in exact rationals, both sides of the ledger for the SAME source:
  (i) the residue 𝒯 := n²Σ_X Q_X(S)Φ(c_X) that the gauge removes; (ii) the change ΔM in Theorem COF step
  (c)'s main pairing caused by Y^p_{*,0} ↦ Y^p_{*,0} + dμ. Decide whether |ΔM| = |𝒯|, |ΔM| < |𝒯| by a power
  of n, or |ΔM| > |𝒯|. Do it without any estimate: exact rationals only.
- **G3 (decide, and say what is forced).** Report **equal / strictly less / worse** against the table of
  §1.2, and state whether the verdict depends on the choice of μ. If it does not, prove the
  μ-independence; if it does, exhibit the optimal μ and prove the optimum.
- **G4 (the lower bound's leverage).** Decide, for the exact terminating witness of YSUP §2.3 (ii)
  (u = ⅛d*δ_p, series terminating), whether (a) μ may be taken **finitely supported**, and if so in how many
  fine sites and how many level-k blocks; (b) whether finite support makes the gauge cheap; (c) whether the
  **termination** is what forces the cost, or is a separate fact. Distinguish the three.
- **G5 (what (TENT-Q) becomes).** State what survives: whether face (b) is an obstruction, at what scope,
  and which single statement replaces it. State plainly if nothing is gained.

### 1.2 PRE-REGISTERED VERDICT TABLE (written before any script and before any derivation)

Let 𝒯 be the residue of Proposition COF-res for a given source S and a given representative, and let ΔM be
the change in Theorem COF step (c)'s main pairing under the admissible shift Y^p_{*,0} ↦ Y^p_{*,0} + dμ,
for a μ ∈ Λ_* that sets Φ_k ≡ 0 at the level-k roots of p's coarse cell. Define the price ratio
**ρ := |ΔM| / |𝒯|** (exact rational, for a specific S and μ), and the estimator ratio
**ρ_est(l) := ‖d(A^{(0→l)}μ)‖_1 / [(n/L^l)^{d−1}·osc_1(Φ)]**, osc_1(Φ) the maximum one-step difference of
Φ over adjacent level-k roots.

| outcome | what I will count as that outcome | consequence I will then report |
|---|---|---|
| **EQUAL** | ρ = 1 exactly for every tested S, μ, k; **or** ρ bounded above and below by absolute constants with no power of L, together with ρ_est(l) ≍ 1 (i.e. no μ beats Lemma TENT-TV's total variation by more than a fixed factor) | TENTQ §2.7's ARGUED pricing is **CONFIRMED**; face (b) **stands** as an obstruction; the n² is real; route (β) of YSUP §2.7 is **CLOSED** |
| **STRICTLY LESS** | ρ ≤ c·L^{−βk} for some β > 0 and an absolute c, for every tested S and the constructed μ, with β stable as k increases | face (b) is **not** an obstruction at the level of the gauge; I report β, the resulting form of (TENT-Q), and the scope (which quantifiers survive) |
| **WORSE** | ρ ≥ c·L^{+βk}, β > 0 | the gauge is a loss; route (β) is closed from the other side |
| **INDETERMINATE** | ρ depends on the choice of μ with no optimum, or the ledger is not closed by an identity and only estimates are available | I report that the question is not decidable by a finite computation and say what is missing |

**Pre-registered check verdicts** (each PASS/FAIL stated before the script exists; L, d, k, n = L^k and
2d, 2^d are the only constants used):

- **TG-A (TGAUGE rebuild).** For pseudo-random μ and pseudo-random x_0, at every level-k site X,
  Φ_k(x_0 + dμ)(X) − Φ_k(x_0)(X) = A^{(0→k)}μ(X) − μ(c_X), **exactly**. PASS iff equality holds at every X
  in both models. *Tested against:* an outside formula (TENTQ §2.7) proven in a file this lane did not
  write, through two disjoint code paths (forward funnel vs plain block average).
- **TG-B (the construction).** For each constructed μ: (i) μ(c_X) = 0 at every level-k root; (ii)
  A^{(0→k)}μ(X) = −Φ(c_X) exactly at every X of the target set; (iii) Φ_k(x_0 + dμ)(c_X) = 0 exactly there.
  PASS iff all three hold exactly for both μ's. *Tested against:* TG-A's identity, independently computed.
- **TG-C (THE PRICE — the decisive clause).** For a pseudo-random source S and a pseudo-random x_0:
  **n²⟨Ĉ, dμ⟩ = −𝒯** exactly, where Ĉ := C(j) + Σ_i(Q_str^{(0→i)})^Th_i^TR_{i+1}(D(S)) is (†)'s regrouped
  form and 𝒯 := n²Σ_X D(S)(c_X)Φ_k(x_0)(c_X). PASS iff exact equality, for **both** constructed μ's.
  *Tested against:* two disjoint code paths — the left side runs Q_str^T, h_i^T, R_{i+1}, d and the block
  average chain; the right side runs the forward funnel and the box-charge sum. Neither calls the other.
  A FAIL here reverses the verdict.
- **TG-D (the invariance that forces it).** n²⟨C(j), dμ⟩ = 0 exactly for every μ ∈ Λ_* and every chain
  source S; and n²⟨C(j), dμ⟩ = n²⟨D(S), μ⟩ exactly. PASS iff both hold exactly. *Tested against:* Lemma
  DF-cc (i) (d*C(j) = D(S)), a closed statement from another file.
- **TG-E (the estimator ratio and the isoperimetric bound).** ρ_est(l) is computed exactly for both μ's at
  every l < k. PASS iff (i) ρ_est(l) ≥ 1 for every l and every μ (no μ beats the stated lower bound), and
  (ii) the flat μ has ρ_est(l) ≤ 2d for every l (it attains the bound up to the cited absolute constant),
  while the single-site μ has ρ_est(l) ≥ L^{k−l} (it is worse by a power). FAIL if either clause is
  violated at any l.
- **TG-F (DESIGNED-FAIL CONTROL 1: a μ outside Λ_*).** Re-run TG-C and TG-D with the root-supported
  μ_root := Σ_X a_Xδ_{c_X}, which satisfies TGAUGE but violates μ(c_X) = 0. **The control FIRES (i.e. the
  control is a PASS of the control) iff TG-D's identity n²⟨C(j), dμ⟩ = 0 FAILS for μ_root**, demonstrating
  that TG-D is capable of failing. If TG-D still returns 0 for μ_root, TG-D has no power and I will say so.
- **TG-G (DESIGNED-FAIL CONTROL 2: a corrupted block average).** Re-run TG-A with A^{(0→k)} computed at a
  deliberately wrong root offset (off(k) := 0). The control FIRES iff TG-A then FAILS. If TG-A still
  passes, the whole pipeline has no power over the block convention and I will say so.

### 1.3 Pre-registered failure modes, with expectations

- **TP-F1.** ρ = 1 exactly, by an identity rather than by an estimate, so that the verdict is **EQUAL** and
  **μ-independent**. Expected: **OCCURS.** Reason stated in advance: f_0 is invariant under the composite
  gauge shift, D(S) is root-supported and μ ∈ Λ_* vanishes at the roots, so the main pairing's change and
  the residue's change must be the same number. If this occurs, TENTQ's "equal" is upgraded from ARGUED to
  PROVEN and its smoothness choice for μ is shown to be **unnecessary**, not merely natural.
- **TP-F2.** ρ depends on μ, with the flat μ strictly cheaper than the single-site μ. Expected: **DOES NOT
  OCCUR for ρ** (the exact ledger), and **DOES OCCUR for ρ_est** (the ℓ¹ × sup estimator): the single-site
  μ needs amplitude L^{dk} and so inflates the estimator by a power of n while leaving the exact value
  unchanged. If so, the lesson is that the estimator, not the gauge, is where the choice of μ matters.
- **TP-F3.** The gauge is **strictly less** because the main pairing carries no n² while the residue does.
  Expected: **DOES NOT OCCUR** — Theorem COF step (c) carries the same explicit n² on the main pairing as
  Proposition COF-res carries on the residue. This is the single arithmetic point on which a "strictly
  less" verdict would have to rest, and it is to be checked against BFT_B §35.5's display, not assumed.
- **TP-F4.** μ cannot be taken finitely supported, because A^{(0→k)}μ must be prescribed at every level-k
  root of the torus. Expected: **DOES NOT OCCUR** — the prescription is needed only where Φ ≠ 0, and for a
  compactly supported level-0 field Φ_k vanishes at every level-k root whose block misses the support
  (Proposition TQ-NOGAIN's mechanism), so μ may be taken supported in a single level-k block. Expected
  consequence: finite support is **real and does not help**, because by TP-F1 the cost is an identity.
- **TP-F5.** The residual terms of Theorem COF step (c) (the ⟨·, r_m(Y^p)⟩ sum) also change under the
  shift, so that the level-0 ledger is not the whole cost. Expected: **OCCURS as a scope limitation.** The
  composite shift is (Ξμ)_l = d(ev^{(0→l)}μ) at every level, so r_m(Y^p) is not inert. Any such change is
  **additional** cost and can only move the verdict from EQUAL towards WORSE, never towards STRICTLY LESS;
  this is to be stated as a one-sided scope limitation and not computed here.
- **TP-F6.** TENTQ §2.7's displayed chain ⟨Σ_l(Q_str^{(0→l)})^Tĵ_l, dμ⟩ = Σ_l⟨ĵ_l, d(ev^{(0→l)}μ)⟩ is
  **wrong as an identity**, because Q_str^{(0→l)}d = d∘A^{(0→l)} (the block average) and not d∘ev^{(0→l)}
  (the root value), the latter being BL-2 (c) for the **full** Q^{(0→l)} and not for Q_str. Expected:
  **OCCURS**, with the two sides differing pointwise but carrying the same powers of L in every norm used,
  so that TENTQ's size conclusion is unaffected. To be reported as SOURCE-DISAGREES with the exact
  statement if it occurs, and as my error if it does not.

### 1.4 Pre-registered process commitments

- Any numeric check gets `checks/tg1_criteria.md` written **before** its script, containing no constant
  derived in this drive session. All arithmetic exact (`fractions.Fraction` / Python ints), plain
  `python3 -I`, `nice -n 10`, single thread, all thread variables = 1, no numpy, no BLAS, **no numeric
  lock** (DRIVE_BRIEF rule 6 exempts exact rational arithmetic).
- At least one check must be **capable of failing against an independently produced object**, and at least
  one must be a **designed-FAIL control** demonstrating that the pipeline detects a deliberate error. Each
  check is graded for discriminating power and a gate that cannot fail is labelled as such.
- A FAIL is reported as a FAIL, script and output kept unaltered; a re-run uses a **new id** with the
  criteria **untouched**; anything run after seeing a result is labelled **post-hoc**.
- Load-bearing cited mathematics is **rebuilt** here, not cited: h_i, Q_str, the root offsets, A^{(0→l)},
  χ^5, Q_X, C(j), R_{i+1} and the spike rationals of REVIEW_BFT_A_S8 S8-7 are recomputed in this lane's own
  script before being used in any statement.
- This file is **append-only**. I write **only** TGAUGE_PRICE.md and `checks/tg1_*`. **No other lane file is
  edited** — in particular not YSUP.md, TENTQ.md, BFT_A.md, BFT_B.md or any REVIEW_* file; requests go in a
  final "## FOR OTHER FILES (not edited)".

## 2. Construction, price and decision (appended after §1 (15:23 UTC), after `checks/tg1_criteria.md` (15:31 UTC), after `checks/tg1_price.py` (ran 15:33:16, 2.06 s, 79 MB, **3 FAILs**), after `checks/tg1b_criteria.md` (≈15:35 UTC) and after `checks/tg1b_ledger.py` (ran 15:36:14, 4.07 s, 205 MB, ALL PASS))

Notation. n = L^k, d = 4, L = 3, off(l) = (L^l − 1)/2, c_X = the level-0 avatar of the level-k site X,
B_X = its level-k block [L^kX, L^kX + L^k)^d (n^d fine sites), s := (1 − n^{−d})^{−1} = (1 − L^{−dk})^{−1}.
Λ_0 = the composite gauge functions = level-0 functions **constant on the level-k roots** (BFT_A §26.0);
Λ_* ⊂ Λ_0 those vanishing there. Φ denotes **any** level-k function; where it is Φ_k(Y^p_{*,0}) that is said.

### 2.0 Scope note: why a scalar model is COMPLETE here, and where that stops

Every operator in §2 — Q_str, h_i, ev, A^{(0→l)}, d, d*, χ^5 — acts **componentwise on su(N) in an
orthonormal basis** at the trivial background (BFT_B §24.0, §16.1 (f)). Every statement of §2 is linear with
scalar coefficients in the fibre, so an exact scalar model is a **complete** test of it, not a vacuous one.
**Where this stops:** at a nontrivial background the axial transports do not commute with the fibre and a
scalar model would be vacuous; §2 makes **no** background claim, and Proposition QN — which §2.2 uses — is
itself a trivial-background statement (TENTQ §2.9 (c) shows it fails at a background by a holonomy defect).

### 2.1 Proposition TG-MU (the explicit μ): PROVEN-HERE + COMPUTED

*Statement.* Let 𝒳 be any set of level-k sites and Φ any level-k function. By Proposition TGAUGE, a shift
Y^p_{*,0} ↦ Y^p_{*,0} + dμ with μ ∈ Λ_* sets Φ_k ≡ 0 on 𝒳 **iff**

  **(G)  A^{(0→k)}μ(X) = −Φ(c_X) for X ∈ 𝒳,  and  μ(c_X) = 0 at every level-k root.**

Two explicit solutions, both in Λ_* and both **finitely supported** when 𝒳 is finite:

  **μ_flat := Σ_{X∈𝒳} (−s·Φ(c_X))·(1_{B_X} − δ_{c_X})**  — constant on each block except a one-site hole
  at its centre. supp = |𝒳|(n^d − 1) fine sites; own sup = s·max_𝒳|Φ|;
  **μ_pt := Σ_{X∈𝒳} (−n^d·Φ(c_X))·δ_{c_X+e_0}**  — ONE fine site per box; own sup = n^d·max_𝒳|Φ|.

A third, **not** admissible and recorded because §2.5 needs it:
  **μ_root := Σ_{X∈𝒳}(−s·Φ(c_X))·δ_{c_X}** satisfies TGAUGE's displayed identity (its change is
  (L^{−dk} − 1)a = −Φ, which is exactly YSUP §2.1's ys1 A5 formula Φ_k(dδ_{c_X})(c_X) = L^{−dk} − 1) but
  **μ_root ∉ Λ_0**, so Ξμ_root ∉ 𝒢_0 and the shift is **not a gauge transformation**.

*Proof.* A^{(0→k)}(1_{B_X} − δ_{c_X})(X) = L^{−dk}(n^d − 1) = 1 − n^{−d} = s^{−1} and the blocks are disjoint,
so A^{(0→k)}μ_flat(X) = −Φ(c_X); (1_{B_X} − δ_{c_X})(c_X) = 0. A^{(0→k)}δ_{c_X+e_0}(X) = L^{−dk} = n^{−d}
(the site lies in B_X because off(k) + 1 < L^k for every k ≥ 1 at L = 3), so A^{(0→k)}μ_pt(X) = −Φ(c_X), and
μ_pt(c_Y) = 0 for every Y. With μ ∈ Λ_*, TGAUGE's change is A^{(0→k)}μ(X) exactly. ∎
*Checked, exactly, in every model (d = 2 at k = 2, 3; d = 4 at k = 1, 2):* **tg1 B** PASS for both μ, all
three clauses — μ(c_X) = 0 at every root, A^{(0→k)}μ = −Φ at every X, and **Φ_k(x_0 + dμ)(c_X) = 0 exactly**,
the last computed through the forward funnel and not through the block average. **tg1 A** PASS: TGAUGE
itself rebuilt at every level-k site of the torus in all four models.

**Which object the main pairing sees — and TENTQ §2.7's displayed chain is wrong here. SOURCE-DISAGREES.**
TENTQ §2.7 writes the change in Theorem COF step (c)'s main pairing as
⟨Σ_l(Q_str^{(0→l)})^Tĵ_l, dμ⟩ = **Σ_l⟨ĵ_l, d(ev^{(0→l)}μ)⟩**, citing "d*(Q_str^{(0→l)})^T = ev^{(0→l)T}d*,
BL-2 (c) transposed". BL-2 (c) is the identity for the **full** Q^{(0→l)}, not for Q_str: TGAUGE's own proof
establishes **Q_str^{(0→l)}∘d = d∘A^{(0→l)}**, the **block average**, so the correct form is

  **Σ_l⟨ĵ_l, d(A^{(0→l)}μ)⟩,   not   Σ_l⟨ĵ_l, d(ev^{(0→l)}μ)⟩.**

*Checked:* **tg1b B4** PASS in all three models — Q_str^{(0→l)}(dμ) = d(A^{(0→l)}μ) exactly at every
level-l link for every 1 ≤ l ≤ k, and **≠ d(ev^{(0→l)}μ) at every l ≥ 1**. The two differ maximally exactly
where it matters: for μ ∈ Λ_* one has ev^{(0→k)}μ ≡ 0 while A^{(0→k)}μ = −Φ ≠ 0. **TENTQ's size conclusion
is unaffected** (both objects have own sup ≤ sup|μ| and comparable level-l total variations, so the L-powers
it quotes are right), which is why this is an erratum and not a refutation; but the identity as displayed is
false and the pricing below is done with A.

### 2.2 Theorem TG-PRICE (the exact price: it is EQUAL, for every admissible μ): PROVEN-HERE

*Statement.* Let S be a Setting LIN^cc source with D(S) = D^root(S) supported on the level-k roots (total 0
by Proposition QN), j its plain currents, C(j) = Σ_{l<k}(Q^{(0→l)})^Tj_l,
Ĉ := Σ_l(Q_str^{(0→l)})^Tĵ_l = C(j) + Ĉ_def with Ĉ_def := Σ_{i<k}(Q_str^{(0→i)})^Th_i^TR_{i+1}(D(S))
(Lemma DF-cc (ii) (†)). Put

  **P := n²⟨C(j), Y^p_{*,0}⟩**  (Theorem COF step (c)'s first term — the quantity actually to be bounded),
  **M := n²⟨Ĉ, Y^p_{*,0}⟩**  (the regrouped main term Theorem COF estimates by C_YN·π_0),
  **𝒯 := n²Σ_X D(S)(c_X)·Φ_k(Y^p_{*,0})(c_X)**  (Proposition COF-res's residue), so that **M = P + 𝒯**.

Then for **every** μ ∈ Λ_0 — with no hypothesis on Φ, on the profile class, on the source class, on k or on
T:

  **(i) ΔP = n²⟨C(j), dμ⟩ = n²⟨D(S), μ⟩ = 0.**  P is invariant: f_0's first term does not move.
  **(ii) ΔM = Δ𝒯 = n²Σ_X D(S)(c_X)·A^{(0→k)}μ(X).**
  **(iii) If μ obeys (G) on a set 𝒳 ⊇ supp D(S), then Δ𝒯 = −𝒯, so 𝒯_new = 0 and M_new = M − 𝒯 = P.**

  **Hence ρ := |ΔM| / |𝒯| = 1 EXACTLY, for every admissible μ.** The gauge removes the residue and adds
  **precisely the same number** to the main pairing. **The price is EQUAL — exactly, with no constant, no
  estimate, and no smoothness choice for μ.**

*Proof.* (i) ⟨C(j), dμ⟩ = ⟨d*C(j), μ⟩ by the adjointness convention of BFT_A §23.1, and d*C(j) = D(S) by
Lemma DF-cc (i). D(S) is carried by the level-k roots and μ ∈ Λ_0 is constant = κ there, so
⟨D(S), μ⟩ = κΣ_XD(S)(c_X) = 0 by Proposition QN; for μ ∈ Λ_* the vanishing is termwise (κ = 0). (ii) From
M = P + 𝒯 and (i), ΔM = ΔP + Δ𝒯 = Δ𝒯, and Δ𝒯 is Proposition TGAUGE summed against the root charges, with
the μ(c_X) term killed by μ ∈ Λ_*. (iii) is (G) substituted into (ii). ∎

*Checked, exactly, with the whole ledger closed on ONE source:* **tg1b B1 ALL PASS** — 3 models (d = 2 at
k = 2 and k = 3; d = 4 at k = 2) × 2 fields (support in one block; support in several) × 2 admissible μ:
d*C(j) = D(S) at every site (B1 (i)); D(S) root-supported and neutral (B1 (ii)); **M = P + 𝒯 exactly**
(B1 (iii), which is Proposition COF-res's identity re-derived here from (†) by a code path disjoint from the
forward funnel); **ΔP = 0 exactly** (B1 (iv)); and **ΔM = −𝒯 exactly, ρ = 1, 𝒯_new = 0, M_new = P** (B1 (v))
for μ_flat **and** μ_pt. In tg1 the same equality holds in all four models (tg1 C1/C2 on the non-vacuous
field), with C1 additionally matched against the **outside** statement of BFT_B §35.7.

> **Corollary TG-NULL (what "equal" means here, and it is stronger than "equal cost"). PROVEN-HERE.**
> After the gauge the only surviving term is M_new, and M_new = P is the **same number** as before. So the
> gauge is a **null operation on the quantity to be bounded**: every bound available after it was available
> before, and conversely. It is a relabelling of one invariant into one slot instead of two, and it carries
> no information. **Route (β) of YSUP §2.7 is CLOSED.**

*What Proposition TGAUGE does and does not say, restated precisely.* Φ_k **is** a representative artefact —
that part of TENTQ §2.7 is right and is re-verified here (tg1 A, tg1 B). What is **not** a representative
artefact is the number P that the estimate must bound. The split of P into "main term + tent residue" moves
with the representative; P does not. TENTQ's one-line reason for the equal price ("f_0 is gauge-invariant,
so no representative choice changes the true size") is **not** sufficient as an argument — an estimate of an
invariant may be lossy, and TENTQ itself shows exactly that elsewhere (Proposition PINC: "Hölder is being
applied at the wrong place"). The reason the price is equal is the **termwise** identity (i)-(iii), and that
is what is proven here.

### 2.3 Lemma TG-TV and Proposition TG-OPT (no μ beats the tent's own total variation): PROVEN-HERE + COMPUTED

This settles TENTQ §2.7's remaining soft spot — the cost estimate "uses a smoothness choice for μ that is
natural but not forced" — **independently of §2.2**, on the ℓ¹ × sup estimator's own terms.

*Lemma TG-TV (a total-variation lower bound). PROVEN-HERE.* Let G be a function on the level-l lattice and
X, X′ two μ-adjacent level-k boxes, each holding N^d level-l sites, N := n/L^l. Then
  **Σ_z|dG(z, μ)| ≥ N^{d−1}·|mean_X G − mean_{X′}G|.**
*Proof.* Partition the level-l sites of X ∪ X′ into the N^{d−1} lines in direction μ, each meeting both
boxes. Along one line the total variation is at least the modulus of the difference of its averages over
X ∩ line and X′ ∩ line. Summing over lines and using mean_X G = N^{−(d−1)}Σ_lines avg_{X∩line}G together
with the triangle inequality gives the claim. ∎
*Consequence.* For **every** μ obeying (G), with osc_1(Φ) the maximum one-step difference of Φ over adjacent
level-k roots,
  **‖d(A^{(0→l)}μ)‖_1 ≥ (n/L^l)^{d−1}·osc_1(Φ) — exactly Lemma TENT-TV's upper bound divided by 2d.**
*Checked:* tg1 clause E (i) PASS for both μ in all four models (ρ_est(l) ≥ 1 everywhere).

*Proposition TG-OPT (μ_flat is optimal, with the exact constant). COMPUTED (exact) + PROVEN.* For Φ carried
by a single level-k box, writing ρ_est(l) := ‖d(A^{(0→l)}μ)‖_1 / [(n/L^l)^{d−1}·osc_1(Φ)]:

  **ρ_est(l) = 2d·s·(1 + L^{−l}n^{1−d})  for μ_flat,   ρ_est(l) = 2d·L^{k−l}  for μ_pt,**

both exact. Equivalently, against Lemma TENT-TV's **own** total variation (like for like):

  **ρ_tv(l) := ‖d(A^{(0→l)}μ_flat)‖_1 / ‖d(ev^{(0→l)}I_χΦ)‖_1 = s·(1 + L^{−l}n^{1−d}) → 1 as k → ∞.**

*Proof.* A^{(0→l)}μ_flat = s·(−Φ) at every level-l site of the block except the one containing c_X, where it
is s(−Φ)(1 − L^{−dl}); its level-l total variation is therefore 2d(n/L^l)^{d−1}s|Φ| across the 2d block
faces plus 2d·L^{−dl}s|Φ| across the root hole, and osc_1(Φ) = |Φ|. For μ_pt, A^{(0→l)}μ_pt = L^{d(k−l)}(−Φ)
at one level-l site and 0 elsewhere, giving 2d·L^{d(k−l)}|Φ|. The tent attains Lemma TENT-TV exactly, which
converts ρ_est into ρ_tv by dividing by 2d. ∎
*COMPUTED, exact, tg1b B3 ALL PASS at every (model, l):* ρ_est(l) for μ_flat = 9/2, 21/5 (d = 2, k = 2);
54/13, 369/91, 366/91 (d = 2, k = 3); **657/82, 1641/205 (d = 4, k = 2)** — against 2d = 8 in d = 4; and for
μ_pt exactly 2d·L^{k−l} = 72, 24 (d = 4, k = 2). The like-for-like ratios are
**ρ_tv = 9/8, 21/20 (d = 2, k = 2); 27/26, 369/364, 183/182 (d = 2, k = 3); 657/656, 1641/1640 (d = 4,
k = 2)** — i.e. in d = 4 at k = 2 the gauge's total variation exceeds the tent's own by **0.15 %**, and it
decreases in k at fixed l (tg1b B3 (iii), checked k = 2 → 3 at l = 0 and l = 1).

> **So TENTQ's smoothness choice is not merely natural — it is OPTIMAL, by Lemma TG-TV, and the optimum IS
> the tent's own total variation, to a factor that tends to 1.** The clause of §2.7 that was ARGUED because
> the choice was "not forced" is now **PROVEN on its own terms**, and §2.2 makes the estimator question moot
> in any case. The single-site μ_pt, by contrast, is worse by **exactly L^{k−l}** — the cheapest-support μ
> is the most expensive ESTIMATE, while its exact price is identical (§2.2).

### 2.4 >>> THE DECISION: **EQUAL**. Face (b) stands as an obstruction and the n² is real

Against the pre-registered table of §1.2, the outcome is **EQUAL**, and by the strictest of the two entries
there: not "bounded above and below by absolute constants" but **ρ = 1 exactly** in every model, both
fields, both admissible μ (tg1b B1 (v)), together with ρ_est(l) ≍ 2d and ρ_tv(l) → 1 (tg1b B3).

**TENTQ §2.7's ARGUED pricing is CONFIRMED, and upgraded from ARGUED to PROVEN.** Four respects in which the
statement proven here is stronger than the one it confirms:
1. **Exact, not asymptotic:** ρ = 1, not ρ ≍ 1.
2. **μ-independent:** the equality holds for every admissible μ, so there is no optimum to search for and no
   construction left to try. TENTQ's hole — "no μ is constructed explicitly here" — is closed by exhibiting
   two and by proving the price does not depend on which.
3. **Unconditional on the profile input:** §2.2 holds for every level-k function Φ. In particular it is
   **not** CONDITIONAL on Y^p_{*,0}'s core being in the |z|^{−3} class, unlike YSUP's n²-failure verdict,
   and it does not use (Φ-conv), the level count, Theorem YH or any source-class norm.
4. **It is a null operation, not merely an equal trade** (Corollary TG-NULL).

**Pre-registered failure modes.** **TP-F1 OCCURS** exactly as expected (ρ = 1 by an identity, μ-independent).
**TP-F2 OCCURS as pre-stated in both halves:** the exact price does **not** depend on μ, and the estimator
does — by exactly L^{k−l} between μ_pt and μ_flat. **TP-F3 DOES NOT OCCUR**, and this was the single
arithmetic point on which a "strictly less" verdict had to rest: Theorem COF step (c)'s main pairing
n²⟨C(j), Y^p_0⟩ carries **the same explicit n²** as Proposition COF-res's residue (BFT_B §35.5 (c) and
§35.7, read directly and quoted in §1.0). There is no n² to win. **TP-F4 DOES NOT OCCUR** (§2.6).
**TP-F5 OCCURS as a one-sided scope limitation** (§2.7, item 4). **TP-F6 OCCURS** (§2.1, SOURCE-DISAGREES).

### 2.5 Proposition TG-EXCL (what WOULD be cheap is exactly what is not a gauge): PROVEN-HERE + COMPUTED

This is the constructive by-product of designed-FAIL control 1, and it says what shape the obstruction has.

*Statement, with its proof.* For the inadmissible μ_root of §2.1 — the root-delta, the one choice that puts
the gauge function's whole weight **at** the level-k roots — one has μ_root(c_X) = s·Φ(c_X), hence
  **ΔP = n²⟨D(S), μ_root⟩ = s·n²Σ_XD(S)(c_X)Φ(c_X) = s·𝒯 ≠ 0,**  and  Δ𝒯 = −𝒯 (it does set Φ_k ≡ 0, since
s(1 − n^{−d}) = 1), so **ΔM = ΔP + Δ𝒯 = (s − 1)·𝒯** and
  **|ΔM| / |𝒯| = s − 1 = n^{−d}/(1 − n^{−d}) = 1/(n^d − 1) = 1/(L^{dk} − 1)  exactly.**
So it would be cheaper than the residue by **n^d = L^{4k} in d = 4** — far more than the n² needed. But
ΔP ≠ 0, i.e. the shift changes **f_0 itself**: Ξμ_root ∉ 𝒢_0 and it is **not a gauge transformation at
all**. The "saving" and the change in f_0 are the same number up to the factor s/(s − 1) = n^d.
*COMPUTED, exact (tg1b B2, the control FIRED in all three models and both fields):* ρ_root = **1/80**
(d = 2, k = 2, n^d = 81), **1/728** (d = 2, k = 3, n^d = 729), **1/6560** (d = 4, k = 2, n^d = 6561) — i.e.
1/(L^{dk} − 1) in each case; and ΔP ≠ 0 in each case, with M_new ≠ P.

> **Reading, and it is the structural content of the verdict.** The cheap "gauge" is cheap by exactly the
> amount by which it moves f_0. The functions that would remove face (b) for free are precisely those
> excluded by **Λ_0's own definition** — the composite gauge functions are **constant on the level-k roots**
> (BFT_A §26.0) — and that constraint is not an estimate, a currency or an incidentally-fixed parameter: it
> is what makes Ξμ a composite gauge transformation. *Observation, offered and not claimed as an
> identification:* the same root locus carries S_E's pin λ^E_X(c_X) = 0, which TENTQ §2.4 (i) proves
> **FORCED** and constitutive of the slice. Whether the two are one fact is not decided here.

### 2.6 The lower bound's leverage (G4): finite support is real, and worthless — three separate facts

**(a) μ IS finitely supported. PROVEN-HERE for the mechanism, COMPUTED for the witness.** For the exact
witness u = ⅛d*δ_p of YSUP §2.3 (ii), Φ_k(u) vanishes at **all 2d one-coarse-step neighbours** of its box —
rebuilt exactly here (tg1 clause H prints 0 at all eight, confirming tq1 A8 independently) — and generally
at every level-k root whose block misses supp u (Proposition TQ-NOGAIN's mechanism). So (G) has to be
imposed on **one box**, and μ may be taken carried by **one level-k block** (μ_flat: n^d − 1 = 6560 fine
sites at d = 4, k = 2) or by **one single fine site** (μ_pt). **The cause is the compact support of the
witness, not the termination of the series.**

**(b) Finite support does not make the gauge cheap.** ρ = 1 for both μ, exactly (tg1b B1 (v)). The price
depends on μ **only through A^{(0→k)}μ**, which (G) fixes completely; it does not depend on supp μ, on
sup|μ| or on μ's smoothness. The brief's hypothesis that finite support would make the gauge cheap is
therefore **false, and provably so**. Worse than neutral: the cheapest-support choice μ_pt is the one that
makes the standard ℓ¹ × sup **estimate** worst, by exactly L^{k−l} (Proposition TG-OPT), at an identical
exact price.

**(c) What the termination DOES do — and it is the other half of the brief's question.** φ_3 = φ_4 = φ_5 = 0
exactly and Φ_k(u) = −65/26244 for **every** k ≥ 2 (YSUP §2.3 (ii); the k = 2 rationals −1/432, −17/104976,
17/243, −65/26244 rebuilt exactly here, **tg1 H PASS**, against an outside prior computation this lane did
not produce). So the amount to be gauged away is **k-independent**: it neither grows nor decays with the
level count. The termination therefore does **not** force the equality — §2.2 holds for every Φ, including
one decaying like n^{−2}, for which the same identity would make the price harmless — but it **pins the
magnitude**: the equal price is a k-independent constant times n², which is why the n² survives at every
level and cannot be outgrown. **The termination is a statement about the size of the obstruction, not about
the cost of removing it.** Both halves of the brief's question 4 answer negatively for the gauge.

### 2.7 What (TENT-Q) becomes (G5), and the invariant form of face (b)

1. **(TENT-osc) stays exactly where YSUP leaves it.** FALSE at p's own coarse cell by exactly n² = L^{2k}
   (YSUP §2.3, §2.4 (a)), **CONDITIONAL** on the profile input (BFT_A §38.7 / Theorem YH); and k-, T-uniform
   with an R_c^{−3} decay outside that cell (YSUP §2.4 (c), ARGUED there). **Nothing in this file changes
   either half**, and nothing in this file is evidence for or against the profile input.
2. **Route (β) is CLOSED, and that is this file's deliverable.** YSUP §4.3 named Proposition TGAUGE's price
   as "the single biggest remaining obstruction in this scope" and "the cheapest high-value item left",
   because "if the price is strictly smaller the tent face is free". It is **not** strictly smaller: it is
   exactly equal, by an identity, for every admissible μ (§2.2), and the estimator cannot be beaten either
   (§2.3). **Face (b) is an obstruction.** The item should be struck from the open set, not retried.
3. **The invariant, representative-free form that should be carried instead. PROVEN as an implication.**
   Since P = n²⟨C(j), Y^p_{*,0}⟩ is invariant under every μ ∈ Λ_0 (§2.2 (i)), Hölder may be applied to the
   **best** composite-gauge representative:
     **|P| ≤ n²·sup_own|C(j)|·𝒩_*(Y^p),  𝒩_*(Y^p) := inf{‖Y^p_0 + dμ‖_1 : μ ∈ Λ_0},**
   for **every** source, with **no (CC-0)**, **no split into main term plus residue**, and no tent
   coefficient anywhere. So face (b) may be carried as one statement about the response alone:
   > **(Y-N*), named and stated.** 𝒩_*(Y^p) ≤ C·n, uniformly in k, T and p — Theorem YH's bound with the
   > infimum **restricted to the composite gauge functions Λ_0** (constant on the level-k roots) instead of
   > over all level-0 functions. **OPEN.**
   *Honest limits of this reformulation, stated plainly.* (a) It is a **sufficient** condition, PROVEN as an
   implication; its **sharpness is not assessed here**, and the ℓ¹ × sup step it uses is the same step
   Proposition PINC shows to be lossy elsewhere, so (Y-N*) may well be strictly stronger than face (b)
   needs — that is OPEN. (b) Theorem YH supplies the **unrestricted** 𝒩(Y^p) ≤ C_YN·n; what the restriction
   to Λ_0 costs is exactly the question, and by YSUP's n²-failure it is **expected to cost n²** for the
   |z|^{−3} profile class, so (Y-N*) is expected FALSE by n² (ARGUED, inheriting YSUP's conditional verdict,
   not proven here). Its merit is not optimism: it is that the whole of face (b) becomes **one norm
   inequality on Y^p in the same currency as Theorem YH**, with the source, the charges, the tent and the
   representative all eliminated.
4. **One-sided scope limitation (TP-F5), stated because it matters.** The composite shift acts at every
   level, (Ξμ)_l = d(ev^{(0→l)}μ) (the transpose of Ξ^TS = Σ_lev^{(0→l)T}d*S_l), so Theorem COF step (c)'s
   **residual terms** Σ_m⟨Σ_{l>m}(Q^{(m+1→l)})^Tj_l, r_m(Y^p)⟩ are **not inert** under it. They are **not
   computed here.** Any change in them is **additional** cost, so the limitation is one-sided: it can move
   the verdict from EQUAL towards WORSE and never towards STRICTLY LESS. The verdict is therefore safe, and
   the ledger of §2.2 is the **level-0** ledger — which is where both the residue and the tent live.
5. **What is left to attack on face (b), ranked, statements only and none claimed here.**
   (α) YSUP §2.4 (c)'s restriction to its true domain — PROVEN-grade, shrinks the item by T^d, unchanged.
   (γ) Pair D^root against the funnel exactly rather than through Hölder (YSUP §2.7 (γ)) — untouched here.
   (ε) **New, and the one this file points at: control the root charges themselves.** The residue obeys
   𝒯 ≤ n²·max_X|Φ_k(Y^p_{*,0})(c_X)|·Σ_X|Q_X| with **max|Φ_k| ≤ 3.89·C_0 k- and T-uniformly** (YSUP
   §2.3 (i), PROVEN there), so face (b) holds as soon as the **source** class controls Σ_X|Q_X| ≲ n^{−2}.
   That is a statement about D^root(S) — i.e. about BFT_A Lemma CD and Corollary NC's rows — and **not**
   about Y^p at all. It is the one place where the n² could be met from the other side, and nothing read
   here prices it. *Not claimed; offered to lane A in §5.*
   (δ) A restatement of (TENT-Q) without the n²: still not available from anything read here.

### 2.8 What is NOT reached, plainly

1. **No response field is computed anywhere.** x_0 is a pseudo-random sparse stand-in and u is the explicit
   witness; neither is Y^p_{*,0}. §2.2's price identity needs **no** input about Y^p and is unconditional;
   every statement that mentions Y^p_{*,0}'s **size** (and only §2.7's items 1, 3 (b) and 5 (ε) do) inherits
   the profile input as a named hypothesis. **YSUP §5's flagged attack point — whether Z″₀'s funnel could
   cancel g₀'s — does not bear on this file's verdict:** if it did cancel, Φ_k would be small and there
   would be nothing to gauge, and §2.2's identity would hold trivially. The "equal" verdict is robust to
   that question in both directions, and that is worth recording.
2. **Nothing nonabelian, nothing at a background, nothing at m > 0 or θ > 0, nothing about N.** §2.0.
3. **The upstream level count is untouched.** REVIEW_BFT_B_S9_S10 Part J (RS10-1) refutes Corollary COF-crit
   and leaves k (or ≈ 25(k − 1) through ‖·‖_Pc) upstream of (TENT-Q), (Y-sup^loc) and everything above.
   **This file accepts that and claims no k-uniformity for (NC-Γ).** Every statement of §2 is k-uniform **in
   its own right** — no constant in §2.2 or §2.3 contains k — which is a different and weaker thing.
   k ≤ 3 throughout, so no level count is measured here.
4. **(NEUT-box) is FALSE and struck** (TENTQ Proposition QFALSE) and is not used anywhere above.
5. **The r_m residual terms are not computed** (§2.7 item 4), and **no claim is made about the sharpness of
   (Y-N*)** (§2.7 item 3 (a)).
6. **k ≤ 3, T ≤ 3, and three of the four tg1 models are d = 2 for the full-torus identities**; d = 4 is
   covered at k = 1 (tg1 P3) and k = 2 (tg1 P4, tg1b Q3) with the complete ledger at k = 2.

## 3. Check record, with a per-check statement of discriminating power (written after §2)

Files, all in `checks/`: `tg1_criteria.md` (15:31 UTC, **before** the script), `tg1_price.py` (ran 15:33:16,
**2.06 s real, 79 MB peak**, **3 FAILs**), `tg1_out.txt`, `tg1_err.txt`; `tg1b_criteria.md` (≈15:35 UTC,
written before its script, declaring the three repairs **before** any new number was produced, with a
disclosed timestamp correction in its own header), `tg1b_ledger.py` (ran 15:36:14, **4.07 s, 205 MB**,
**ALL PASS**), `tg1b_out.txt`, `tg1b_err.txt`. Exact `fractions.Fraction` / Python ints, plain `python3 -I`,
`nice -n 10`, `OMP/OPENBLAS/MKL_NUM_THREADS=1`, no numpy, no BLAS, single thread, **no numeric lock taken**
(DRIVE_BRIEF rule 6 exempts exact rational arithmetic). Load at start 2.74 and 2.45.

**Three FAILs are reported, all disclosed and none repaired in place.** `tg1_criteria.md` was **not
touched**; `tg1_price.py`, `tg1_out.txt` and `tg1_err.txt` are kept unaltered with their FAILs; the repairs
were pre-registered in a **new** criteria file under a **new id** before the re-run. *Development
disclosure:* `tg1_price.py` was edited three times **before** its recorded run — batching the Q_str chain
over the level-k sites, sparsifying the pseudo-random μ, and clamping the one-block field's support — all for
affordability and all **before** any verdict was printed; the criteria were not touched, the script is
deterministic, and the recorded run is of the file as it now stands.

| id | verdict | what it is tested **against** | could it have failed? |
|---|---|---|---|
| **tg1 A** TGAUGE rebuilt at every level-k site | **PASS** (exact, 4 models, every box) | **an outside formula** (Proposition TGAUGE, TENTQ §2.7) proven in a file this lane did not write, through two disjoint code paths: forward h_i∘Q_str funnel against a plain block average | **HIGH.** It pins the whole normalisation: a wrong root offset, a wrong block convention, a wrong level count or a telescoping error each break it. **tg1 G proves it can fail** |
| **tg1 G** DESIGNED-FAIL CONTROL 2 (off(k) := 0 in the block average) | **PASS of the control — it FIRED in all four models** (clause A then fails at 6/9, 4/4, 6/16 and 8/16 boxes) | itself | **this is the power measurement for clause A.** It establishes that A is sensitive to the root/block convention, which is the one thing the whole construction rests on |
| **tg1 B** the construction (μ(c_X) = 0, A^{(0→k)}μ = −Φ, Φ_k(x_0+dμ)(c_X) = 0) | **PASS** (exact, both μ, 4 models) | clause (iii) is computed through the **forward funnel**, independently of the block average that (ii) uses | **MEDIUM-HIGH.** An error in either chain breaks (iii) while leaving (ii) intact |
| **tg1 C1** n²⟨Ĉ_def, x_0⟩ = 𝒯 | **PASS** (exact) on the non-vacuous field in all 4 models | **an outside formula**: Proposition COF-res (BFT_B §35.7), rebuilt here from Lemma DF-cc (ii)'s (†) by a path (R_{i+1}, h_i^T, Q_str^T) disjoint from the forward funnel and the root sum | **HIGHEST against a statement this lane did not produce.** Any error in R_{i+1}, h^T, Q_str^T, the avatars or the normalisation fails it |
| **tg1 C2** n²⟨Ĉ_def, dμ⟩ = −𝒯 | **PASS** (exact, both μ) on the non-vacuous field in all 4 models | the same two disjoint paths | **HIGH, and the session's verdict turns on it.** Pre-registered to be able to reverse the verdict: a value smaller by a power of L would have meant **strictly less** |
| **tg1 D1/D2/D3** d*C(j) = D(S); root-supported and neutral; ⟨C(j), dμ⟩ = 0 | **PASS** (exact, k ≥ 2 models) | **a closed statement from another file** (Lemma DF-cc (i)) against the full (Q^{(0→l)})^T chain built here from Proposition RF transposed | **HIGH for D1** — a wrong h^{(0→l)T}, a wrong placement ev^{(i+1→l)T} or a wrong adjoint fails it. **MEDIUM for D3** given D1/D2, and **tg1 F / tg1b B2 measure its power** |
| **tg1 Z** non-vacuity (𝒯 ≠ 0) | **FAIL in 3 of 4 models** (P1, P3, P4, generic field) | itself, as pre-registered | it **did** fail. The script placed the root charges without checking Φ_k ≠ 0 there — i.e. it did not implement its own criterion. **Consequence, as the criteria pre-registered: the generic-field clauses of P1, P3, P4 are VACUOUS, not PASSes.** The non-vacuous tg1 results are P2's generic field and all four models' one-block field. Repaired under tg1b |
| **tg1 F** DESIGNED-FAIL CONTROL 1 (μ_root ∉ Λ_*) | **FAIL in P1 and P4; PASS of the control in P2** | itself | consequential on Z: where 𝒯 = 0 the root charges sit where Φ = 0, so μ_root's value there is 0 and D3 cannot distinguish. Where the field is non-vacuous the control **fires**. Repaired and strengthened under tg1b B2 |
| **tg1 E (i)** ρ_est(l) ≥ 1 (Lemma TG-TV) | **PASS** (exact, both μ, all 4 models, every l) | Lemma TG-TV, proven in §2.3 **before** the numbers were read | **MEDIUM-HIGH.** A violation would refute the lower-bound lemma outright |
| **tg1 E (ii)** ρ_est(l) ≤ 2d for μ_flat | **FAIL in all four models** (9/2, 21/5; 54/13, 369/91, 366/91; 42/5; 657/82, 1641/205) | the closed form of Lemma TENT-TV | it **did** fail, and the criterion was **wrong**: it omitted the one-site root hole that μ ∈ Λ_* forces and the normalisation s. The derivable statement is ρ_est(l) = 2d·s(1 + L^{−l}n^{1−d}), which **exceeds** 2d by a factor → 1. Derived analytically in `tg1b_criteria.md` before the re-run and confirmed exactly (tg1b B3) |
| **tg1 E (iii)** ρ_est(l) ≥ L^{k−l} for μ_pt | **PASS** (exact, all models, every l) | the same closed form | **MEDIUM-HIGH.** It is the clause that separates the two μ in the estimator |
| **tg1 H** rebuild of REVIEW_BFT_A_S8 S8-7's four rationals | **PASS** (exact, all four: −1/432, −17/104976, 17/243, −65/26244) | **an independent prior computation in another file and another session**, rebuilt here from the axial 24-order construction, Q_str and the plaquette convention | **HIGHEST against an outside number.** Any error in the axial weights, the root offsets, Q_str, the plaquette convention or the normalisation fails it. It also reproduces Φ_k(u) = 0 at all eight one-coarse-step neighbours (tq1 A8, independently) |
| **tg1b B0** non-vacuity, repaired | **PASS** (3 models × 2 fields) | itself | it is the gate tg1 failed; it now holds in every cell of the grid |
| **tg1b B1 (i)-(iii)** d*C(j) = D(S); root-supported, neutral; **M = P + 𝒯** | **PASS** (exact, 3 models × 2 fields) | **three closed statements from another file** — Lemma DF-cc (i), Lemma DF-cc (ii)'s (†) and Proposition COF-res — now all on **one** source, so the ledger is closed rather than assembled from two unrelated objects | **HIGH.** (iii) is the COF-res split itself; a wrong ĵ-regrouping, a wrong R_{i+1} or a wrong Q^T chain fails it |
| **tg1b B1 (iv)-(v)** ΔP = 0 and **ΔM = −𝒯, ρ = 1** | **PASS, exact, 3 models × 2 fields × 2 admissible μ** | the forward funnel + root sum (for 𝒯) against R_{i+1}, h^T, Q_str^T, d (for ΔM); neither path calls the other | **HIGHEST in this file — the verdict is this clause.** Pre-registered in §1.2 to be able to return **strictly less** (ρ ≤ cL^{−βk}) or **worse**; it returned **exactly 1** in all twelve cells, and also returned M(gauged) = P and 𝒯(gauged) = 0, which are two further independently computable consequences. **tg1b B2 proves it can return something other than 1** |
| **tg1b B2** DESIGNED-FAIL CONTROL 1, strengthened (μ_root ∉ Λ_*) | **PASS of the control — it FIRED in all 3 models and both fields** | itself | **this is the power measurement for B1 (v), and it is CONSTRUCTIVE.** It returns ΔP ≠ 0 **and** ρ_root = **1/80, 1/728, 1/6560** = 1/(L^{dk} − 1) exactly — so the pipeline demonstrably reads prices other than 1, and the one it reads is the content of Proposition TG-EXCL |
| **tg1b B3 (i)-(ii)** the repaired estimator closed forms | **PASS** (exact, every (model, l), both μ) | closed forms **derived analytically in the criteria file before the script**, from the face count and the root hole | **HIGH.** An exact rational match at 7 (model, l) pairs for μ_flat and 7 for μ_pt; a wrong face count, a wrong hole weight or a wrong s fails it |
| **tg1b B3 (iii)** ρ_tv ∈ [1, 2] and decreasing in k | **PASS** | ‖d(ev^{(0→l)}I_χΦ)‖_1, **an independent operator** (the quintic tent itself) on the same data | **HIGH.** It is the like-for-like comparator and it is what makes "equal" quantitative: 9/8, 21/20; 27/26, 369/364, 183/182; **657/656, 1641/1640** |
| **tg1b B4 (i)** Q_str^{(0→l)}(dμ) = d(A^{(0→l)}μ) | **PASS** (exact, every l ≤ k, 3 models) | TGAUGE's own proof step, against a block average computed independently | **HIGH; tg1b B5 measures it** |
| **tg1b B4 (ii)** ≠ d(ev^{(0→l)}μ) | **PASS** (it differs, at every l ≥ 1, in all 3 models) | **a live displayed identity in another file** (TENTQ §2.7) | **HIGH, and it reversed a cited identity.** Pre-registered to be able to show **my** TP-F6 wrong: had the two agreed, TENTQ's chain would have been right and this file would have said so |
| **tg1b B5** DESIGNED-FAIL CONTROL 2 (flat longitudinal multiplicity) | **PASS of the control — it FIRED in all 3 models**: the mass assertion Σ_t mult(t) = L² rejected the corrupted table (5 against 9) **and** B4 (i) then failed | itself | **this is the power measurement for the straight average.** It confirms the pipeline is sensitive to the one feature the argument turns on — that the axial line integral **sums** along its direction with multiplicity L − \|t − (L−1)\| and not flatly |

**What these checks do NOT test, stated plainly.**
1. **Nothing nonabelian.** §2.0 argues from BFT_B §24.0 and §16.1 (f) that a scalar model is *complete* for
   every identity in §2; it would be **vacuous** for a background statement, and §2 makes none. Proposition
   QN, which §2.2 (i) uses, is itself trivial-background only (TENTQ §2.9 (c)).
2. **No response field.** x_0 and u are stand-ins; §2.2's identity needs no input about Y^p, and the places
   that do need one say so (§2.7 items 1, 3 (b), 5 (ε)).
3. **No level count.** k ≤ 3; a factor k cannot be measured there and none is claimed.
4. **The r_m residual terms of Theorem COF step (c) are never computed** (§2.7 item 4) — a one-sided
   limitation.
5. **(Y-N*)'s sharpness is not tested**, nor is 𝒩_* computed anywhere. §2.7 item 3 (a).
6. **d = 2 carries the full-torus identities at k = 3**; d = 4 is at k = 1 and k = 2 only.

## 4. Outcome (written after §3)

### 4.1 Outcome table

| object | status | content |
|---|---|---|
| **Proposition TG-MU** (the explicit μ) | **PROVEN-HERE** + **COMPUTED** | two admissible μ ∈ Λ_* with A^{(0→k)}μ = −Φ_k on any prescribed set: **μ_flat** = −sΦ(c_X) on the block minus its centre, and **μ_pt** = −n^dΦ(c_X) at the single site c_X + e_0. Both **finitely supported**; both verified exactly to set Φ_k ≡ 0 through the forward funnel (tg1 A, tg1 B, 4 models) |
| **the object the main pairing sees** | **PROVEN-HERE**; **SOURCE-DISAGREES with TENTQ §2.7** | Q_str^{(0→l)}∘d = d∘**A^{(0→l)}** (the block average), so the change is Σ_l⟨ĵ_l, d(A^{(0→l)}μ)⟩ and **not** Σ_l⟨ĵ_l, d(ev^{(0→l)}μ)⟩ as §2.7 displays — BL-2 (c) is the identity for the **full** Q^{(0→l)}, not for Q_str. Exact at every l; the ev form **fails** at every l ≥ 1 (tg1b B4). **TENTQ's size conclusion is unaffected**; the identity as displayed is not |
| **>>> THE DECISION: what does the gauge cost?** | **EQUAL. DECIDED, and PROVEN.** | **ρ = \|ΔM\|/\|𝒯\| = 1 EXACTLY**, for **every** μ ∈ Λ_0 and every level-k function Φ, by the termwise identity ΔP = n²⟨D(S), μ⟩ = 0 ⟹ ΔM = Δ𝒯 = −𝒯. Measured exactly in 12 cells (3 models × 2 fields × 2 μ) plus 4 more in tg1. **No estimate, no constant, no smoothness choice, no profile input** |
| **Theorem TG-PRICE** | **PROVEN-HERE** | M = P + 𝒯 and ΔP = 0, so the gauge sends (M, 𝒯) ↦ (P, 0): the residue is **relabelled, not removed** |
| **Corollary TG-NULL** | **PROVEN-HERE** | the gauge is a **null operation on the quantity to be bounded**. M_new = P is the same number as before; every bound available after it was available before. **Route (β) of YSUP §2.7 is CLOSED** |
| **Lemma TG-TV** (total-variation lower bound) | **PROVEN-HERE** | ‖d(A^{(0→l)}μ)‖_1 ≥ (n/L^l)^{d−1}·osc_1(Φ) for every admissible μ — Lemma TENT-TV's upper bound divided by 2d. So the ℓ¹ × sup estimator cannot be beaten either, independently of the identity |
| **Proposition TG-OPT** | **COMPUTED (exact)** + **PROVEN** | ρ_est(l) = 2d·s(1 + L^{−l}n^{1−d}) for μ_flat and 2d·L^{k−l} for μ_pt; equivalently **ρ_tv(l) = s(1 + L^{−l}n^{1−d}) → 1**, measured 657/656 and 1641/1640 at d = 4, k = 2. **TENTQ's "natural but not forced" smoothness choice is OPTIMAL**, and the optimum **is** the tent's own total variation |
| **Proposition TG-EXCL** | **PROVEN-HERE** + **COMPUTED** | the root-delta μ_root would be cheaper by **exactly n^d = L^{dk}** (ρ_root = 1/(L^{dk} − 1); measured 1/80, 1/728, 1/6560) **but it is not a gauge**: ΔP = s𝒯 ≠ 0, so it moves f_0. **What would remove face (b) for free is exactly what Λ_0's definition excludes** |
| **finite support (the brief's Q4)** | **PROVEN-HERE** (a) + **PROVEN-HERE** (b) + **COMPUTED** (c) | (a) μ **is** finitely supported — one level-k block, or **one fine site** — because Φ_k of a compactly supported field vanishes at every root whose block misses the support (Φ_k(u) = 0 at all eight neighbours, rebuilt here). (b) It **does not help**: the price depends on μ only through A^{(0→k)}μ, which (G) fixes; and the one-site choice makes the **estimate** worst by L^{k−l} at an identical exact price. (c) The **termination** does not force the equality (that holds for every Φ) — it **pins the magnitude**, making the amount to be gauged away k-independent, which is why the n² survives every level |
| **(TENT-osc)** | **unchanged from YSUP** | FALSE at p's coarse cell by exactly n² (CONDITIONAL on the profile input), k-, T-uniform outside it with R_c^{−3} (ARGUED). Nothing here changes either half, and nothing here is evidence about the profile input |
| **face (b) of Theorem NCE (ii)** | **IS AN OBSTRUCTION. The n² is real** | the representative freedom is priced and spent: it buys nothing, for any μ. The item should be **struck from the open set, not retried** |
| **(Y-N*)** (new, the invariant form) | **PROVEN as an implication** (the reduction); **OPEN** (the statement); sharpness **OPEN** | \|P\| ≤ n²·sup_own\|C(j)\|·𝒩_*(Y^p) with 𝒩_*(Y^p) := inf{‖Y^p_0 + dμ‖₁ : μ ∈ Λ_0} — Theorem YH's norm with the infimum **restricted to the composite gauge functions**. One statement, **no (CC-0)**, no split, no charges, no tent. Expected FALSE by n² for the \|z\|^{−3} class (ARGUED, inheriting YSUP) |
| **the upstream level count** | **accepted, not claimed against** | RS10-1 stands; no k-uniformity for (NC-Γ) is claimed anywhere |

### 4.2 The brief's questions, answered

1. **The explicit μ.** §2.1: μ_flat = Σ_X(−sΦ_k(c_X))(1_{B_X} − δ_{c_X}) and μ_pt = Σ_X(−n^dΦ_k(c_X))δ_{c_X+e_0},
   s = (1 − n^{−d})^{−1}, both in Λ_*, both verified exactly to gauge Φ_k to zero. The condition is exactly
   **A^{(0→k)}μ = −Φ_k with μ = 0 at the level-k roots**, and the main pairing sees the **block average**
   A^{(0→l)}μ, not the root value ev^{(0→l)}μ (erratum to TENTQ §2.7's display).
2. **Its exact price in the main pairing.** **ΔM = −𝒯 exactly**, for every admissible μ: Theorem COF step
   (c)'s main pairing absorbs precisely the residue that Proposition COF-res removes, because
   P = n²⟨C(j), Y^p_{*,0}⟩ is invariant under Λ_0 (d*C(j) = D^root(S) is carried by the roots, where every
   composite gauge function is constant). Exact rationals, 16 cells, no estimate anywhere.
3. **Equal, strictly less, or worse? → EQUAL**, and by the strictest reading of the pre-registered table:
   ρ = 1 exactly, μ-independently, unconditionally on the profile class. TENTQ's ARGUED pricing is
   **CONFIRMED and upgraded to PROVEN**, and its one soft spot (a smoothness choice "not forced") is closed
   twice over — by Lemma TG-TV, which makes the choice optimal, and by Theorem TG-PRICE, which makes it
   irrelevant. **Face (b) stands as an obstruction and the n² = L^{2k} is real.**
4. **Does the termination make μ finitely supported?** μ **is** finitely supported — one level-k block, even
   one fine site — but that is the **compact support** of the witness, not the termination; and it **does
   not make the gauge cheap**, because the price is an identity in A^{(0→k)}μ alone. What the **termination**
   does is pin the magnitude: Φ_k(u) = −65/26244 for every k ≥ 2, so the amount to be gauged away is
   k-independent and the equal price is a k-independent constant times n². It is not what forces the
   equality — the invariance of P is — but it is what makes the obstruction survive every level.
5. **What (TENT-Q) becomes, and is face (b) an obstruction?** **Yes.** (TENT-osc) stays as YSUP left it,
   route (β) is closed, and the useful restatement is the invariant one: **(Y-N*)**, Theorem YH's norm with
   the infimum restricted to Λ_0, which covers main term and residue in one inequality with no (CC-0) and no
   representative in it. Its sharpness is OPEN and it is expected false by n² for the |z|^{−3} class. The
   one genuinely new place to meet the n² from the other side is **(ε)**: bound Σ_X|Q_X| ≲ n^{−2} on the
   **source**, which is a Lemma CD / Corollary NC question and not a question about Y^p at all.

### 4.3 The single biggest remaining obstruction in this scope

Not the pricing — that is now decided exactly, by an identity, with two designed-FAIL controls that both
fired and one of them constructive. It is that **face (b) has no representative-theoretic escape at all**,
so the n² must be met in one of the two currencies that remain: on the **response** side, (Y-N*) — how much
the Λ_0 restriction costs in Theorem YH's norm, expected n² and therefore expected fatal — or on the
**source** side, Σ_X|Q_X| ≲ n^{−2} for the charges that actually occur, which **nothing read in this lane
prices** and which is the only one of the two that is not already expected to fail. Everything else in this
scope sits behind the upstream level count (RS10-1), which is untouched here and still binding on all of it.

## 5. FOR OTHER FILES (not edited)

*No file other than TGAUGE_PRICE.md and `checks/tg1_*`, `checks/tg1b_*` was written by this lane. In
particular YSUP.md, TENTQ.md, BFT_A.md, BFT_B.md and every REVIEW_* file are untouched.*

**To TENTQ.md's owner — one erratum and one status upgrade, both to live statements.**
1. **ERRATUM to §2.7's displayed chain (SOURCE-DISAGREES).** §2.7 writes
   ⟨Σ_l(Q_str^{(0→l)})^Tĵ_l, dμ⟩ = Σ_l⟨ĵ_l, d(**ev**^{(0→l)}μ)⟩, citing "d*(Q_str^{(0→l)})^T = ev^{(0→l)T}d*,
   BL-2 (c) transposed". BL-2 (c) is the identity for the **full** Q^{(0→l)}. For Q_str the identity is
   §2.7's **own** proof step Q_str∘d = d∘A, so the correct form is Σ_l⟨ĵ_l, d(**A**^{(0→l)}μ)⟩ with
   A^{(0→l)} the level-l **block average**. Checked exactly at every level in d = 2 (k = 2, 3) and d = 4
   (k = 2): the A form holds, the ev form **fails at every l ≥ 1** (tg1b B4). The two differ maximally where
   it matters — for μ ∈ Λ_* one has ev^{(0→k)}μ ≡ 0 while A^{(0→k)}μ = −Φ_k. **§2.7's size conclusion is
   unaffected** (both objects have own sup ≤ sup|μ| and comparable level-l total variations), so this is an
   erratum to one display, not a refutation of the paragraph.
2. **§2.7's price is CONFIRMED and should be upgraded ARGUED → PROVEN, by a different argument than the one
   given.** Suggested replacement for the *"What this does and does not buy. ARGUED for the second half"*
   paragraph: *"The price is **exactly** equal, for every admissible μ and with no smoothness choice.
   Writing P := n²⟨C(j), Y^p_0⟩ for Theorem COF step (c)'s first term, M := n²⟨Σ_l(Q_str^{(0→l)})^Tĵ_l, Y^p_0⟩
   and 𝒯 for Proposition COF-res's residue, one has M = P + 𝒯, and ΔP = n²⟨C(j), dμ⟩ = n²⟨D(S), μ⟩ = 0 for
   every μ ∈ Λ_0, because d*C(j) = D(S) is carried by the level-k roots (Lemma DF-cc (i)) and every
   composite gauge function is constant there (BFT_A §26.0). Hence ΔM = Δ𝒯 = −𝒯: the gauge sends
   (M, 𝒯) ↦ (P, 0) and the residue is relabelled, not removed. (TGAUGE_PRICE §2.2, PROVEN; tg1b B1.)"*
   Two notes on the existing wording. (a) The sentence *"This is as it must be: f_0 is gauge-invariant, so
   no representative choice changes the true size"* is **not sufficient as an argument** — an estimate of an
   invariant can be lossy, as §2.4's own Proposition PINC demonstrates ("Hölder is being applied at the
   wrong place"). The termwise identity is what carries it. (b) The hole *"no μ is constructed explicitly
   here"* is closed: two are constructed (TGAUGE_PRICE §2.1) and the price is shown **not to depend on
   which**, so there is no μ left to try. Additionally, §2.7's "may be taken smooth on the coarse scale" is
   **optimal**, not merely natural: no admissible μ has level-l total variation below
   (n/L^l)^{d−1}osc_1(Φ_k), which is Lemma TENT-TV's own bound over 2d (TGAUGE_PRICE §2.3).
3. **§2.8 (iv)'s named item and §4.5's "single biggest obstruction" may drop the representative hedge.**
   (TENT-osc) is not open **because** of a bookkeeping choice; the choice has now been priced and spent.
   One line worth carrying: *the root-delta μ would be cheaper by exactly L^{dk}, and it is cheaper by
   exactly the amount by which it changes f_0* (TGAUGE_PRICE §2.5).

**To YSUP.md's owner — §4.3 and §5's request 4 are answered, negatively.**
1. **Request 4 ("price Proposition TGAUGE's μ exactly") is DONE: the price is EQUAL, exactly.** μ is
   constructed (two of them, both finitely supported — one of them on a **single fine site**), and
   ΔM = −𝒯 exactly for every admissible μ, by the identity of TGAUGE_PRICE §2.2. **So §4.3's hope — "the
   whole of (TENT-osc) would evaporate if the cost of that gauge were strictly smaller than the tent it
   removes" — does not happen, and cannot happen for any μ.** §2.7's option **(β) is closed**; options (α)
   and (γ) are untouched by this file.
2. **Your negative verdict is not weakened, and this file's verdict does not depend on yours.** Theorem
   TG-PRICE holds for **every** level-k function Φ, so it is unconditional on the |z|^{−3} profile input and
   on (Φ-conv). **Your flagged attack point — whether Z″₀'s funnel could cancel g₀'s — does not bear on it
   in either direction:** if the cancellation happened, Φ_k would be small, there would be nothing to gauge,
   and the identity would hold trivially. That is worth one line in §2.8 (1) if you append again.
3. **Two of your exact facts are rebuilt here against your own numbers, independently of ys1/ys1b:**
   the four S8-7 rationals (tg1 H, exact) and Φ_k(u) = 0 at all 2d one-coarse-step neighbours (tg1 H). Your
   §2.1 normalisation formula Φ_k(dδ_{c_X})(c_X) = L^{−dk} − 1 is also what makes μ_root's price
   1/(L^{dk} − 1) exactly (TGAUGE_PRICE §2.5), so ys1 A5 is load-bearing twice.

**To BFT_B.md's owner (lane B) — one reading of §35.7, one proposed replacement item, one erratum inherited.**
1. **Proposition COF-res's residue is not removable by a representative choice. PROVEN.** The identity
   M = P + 𝒯 with P invariant under Λ_0 (TGAUGE_PRICE §2.2) says the residue is one bookkeeping of an
   invariant, and that gauging the tent coefficient to zero moves exactly that number into §35.5 step (c)'s
   first term. Suggested one-line addition after §35.7's *Reading*: *"The residue is not an artefact of the
   representative: n²⟨C(j), Y^p_0⟩ is invariant under the composite gauge group, and a shift that kills
   Φ_k adds the residue to the main pairing exactly (TGAUGE_PRICE §2.2)."*
2. **Proposal: carry face (b) as a norm statement on Y^p instead of a tent statement.** Because
   ⟨C(j), dμ⟩ = ⟨D^root(S), μ⟩ = 0 for every μ ∈ Λ_0, Hölder may be applied to the best composite-gauge
   representative, giving — **for every source, with no (CC-0) and no split** —
   **|n²⟨C(j), Y^p_0⟩| ≤ n²·sup_own|C(j)|·𝒩_*(Y^p),  𝒩_*(Y^p) := inf{‖Y^p_0 + dμ‖_1 : μ ∈ Λ_0}.**
   Named **(Y-N*)**: 𝒩_*(Y^p) ≤ C·n, k-, T-uniformly — i.e. **Theorem YH with the infimum restricted to the
   level-k-root-constant gauge functions.** This eliminates the charges, the tent and the representative in
   one step, and puts face (b) in the **same currency as Theorem YH**. *Two caveats, both mine and both
   stated: it is only a **sufficient** condition and its sharpness is OPEN (the ℓ¹ × sup step is the one
   Proposition PINC shows lossy elsewhere); and by YSUP §2.3-§2.4 it is **expected FALSE by n²** for the
   |z|^{−3} profile class.* Offered, not claimed.
3. **Inherited erratum.** If §35.5/§35.7 or any consumer repeats TENTQ §2.7's "d*(Q_str^{(0→l)})^T =
   ev^{(0→l)T}d*", note that this holds for the **full** Q^{(0→l)} (BL-2 (c)) and **not** for Q_str, whose
   correct form is d*(Q_str^{(0→l)})^T = (A^{(0→l)})^Td* (checked exactly, tg1b B4). Lemma DF-cc (i)'s own
   proof uses the full Q and is unaffected — tg1b B1 (i) re-verifies d*C(j) = D(S) exactly at d = 2 (k = 2,
   3) and d = 4 (k = 2) from the Proposition RF transpose built here.

**To BFT_A.md's owner (lane A) — one request, and it is the only unexpected-to-fail route left on face (b).**
**Request: price Σ_X|Q_X| for the root charges that actually occur.** Face (b)'s residue obeys
𝒯 ≤ n²·max_X|Φ_k(Y^p_{*,0})(c_X)|·Σ_X|Q_X| with **max|Φ_k| ≤ 3.89·C_0, k- and T-uniformly** (YSUP §2.3 (i),
PROVEN there; its lower bound 2.4768e−3·C_0 is attained, so this factor cannot be improved by more than
≈ 1.6e3 and cannot be made to decay in k). Therefore **face (b) holds as soon as the source class controls
Σ_X|Q_X| = Σ_X|D(S)(c_X)| ≲ n^{−2}.** That is a statement about D^root(S) — Lemma CD (i) off the critical
set, and Corollary NC's rows — and **not** about Y^p at all. BFT_B §35.7's *Reading* currently says only
that "the class permits q of own size L^{−3}π_{k−1}(j_{k−1})", which is a permission, not a measurement of
the charges the contraction actually produces; and BFT_B §41.3 records, at a background, charges of own size
≤ c_NC_NL^{−4(k−l)}f_k‖G^c_l‖_∞, i.e. **with** level decay. **If the charges that occur carry L^{−4(k−l)}-type
decay at the trivial background too, face (b) may be met from the source side**, and this file has shown
that it cannot be met from the representative side at all. Not claimed, not priced here; offered as the
ranked-first remaining route.

**To PROOF.md's owner.** If the tent face is entered in the ledger, the representative question should be
entered **CLOSED, not open**: *"Proposition TGAUGE's representative shift is priced EXACTLY: the cost in
Theorem COF step (c)'s main pairing equals the residue removed, for every admissible μ (TGAUGE_PRICE §2.2,
PROVEN, m = 0, trivial background, d = 4, abelian/linearised). The tent coefficient is a representative
artefact; the number to be bounded is not. Face (b) of Theorem NCE (ii) is an obstruction and the L^{2k} is
real."* **(TENT-osc)** should be entered as YSUP asks (FALSE at the core by L^{2k} for the |z|^{−3} profile
class, CONDITIONAL on that input; k-, T-uniform outside p's coarse cell), with **no** representative hedge.
**(Y-N*)** may be carried as a new named item, OPEN, with its sharpness also OPEN. Nothing above is counted
in PROOF's tally by this lane, and **no k-uniformity for (NC-Γ) is claimed** — RS10-1 stands and is upstream
of all of it.
