Reviewer model: claude-opus-5-5

# COFUN_CC — (CO-fun) on the composite-co-closed class (cc), conditional on Finding X1

Role: Opus 5.5 WORKER (not a reviewer); the shared rules of REVIEW_BRIEF_55.md apply. Append-only file.
Writes: this file and `checks/cc55_*` only. No git.

## PRE-STATED (written before any derivation; UTC 2026-10-28 23:00)

Targets.
- **T1 (Hölder half).** On source class (cc), prove (or show unprovable from the cited statements) the
  [f_0]^∞_α half of (CO-fun) as stated with quantifiers in COFUN.md §2.0, by the X1 decomposition
  (root-charge current b → top datum Q_{k-1}^T b, plus root-charge-free remainder), using LINEAR_PACKAGE
  Theorem 4.2 / 4.2′ for the datum part and Theorem COF (BFT_B §35.5) for the remainder. Verify the
  exponent window (claimed 0 < α < θ_c) against the actual statements.
- **T2 (assembly).** State BFT-5 clause (b)'s curvature half on (cc), conditional exactly on X1's steps
  plus anything added here; list what is PROVEN-given-X1, what still needs (G♯_0-field) / the nontrivial
  background, and how the level-count factor ≈25(k−1) (COF-crit, non-co-closed part V_l of the BCH₂
  rows) enters — interface only.
- **T3 (two nearby defects).** (a) Lemma SPLIT's "D(S^s) = 0" for a non-co-closed top residual slot;
  (b) the two operators both called h_l (4!-averaged, LINEAR_PACKAGE §1.2, vs fixed-order, BFT_B
  §27.1/§29.2 and COFUN). Every step used here is to be stated for the correct h_l.
- **T4 (X1 itself).** Re-check every X1 step I build on. If a step fails, stop building on it and say so.

What would count as a refutation (decided in advance).
- X1 fails if any of: (i) the root charges of a (cc) source are NOT the divergence of a coarse current b
  with ‖b‖_∞ ≤ Σ_l π_l (or the bound needs a quantity not controlled on (cc)); (ii) Q_{k-1}^T b is NOT an
  admissible top datum for LP 4.2(ii) (wrong normalisation κ_{k-1}, wrong lattice/scale, LP 4.2(ii)
  needs a hypothesis b lacks, or LP 4.2(ii) is stated for the other h_l); (iii) the remainder still
  carries root charges, or lies outside the hypotheses of Theorem COF.
- T1 fails (Hölder half NOT obtained by this route) if LP 4.2/4.2′ give only sup control of the datum
  response, or Theorem COF gives only sup control, or the exponents they give do not cover the window
  that (CO-fun) needs; in that case I name the missing estimate precisely instead of claiming it.
- An "uniform in k and T" claim fails if any constant in the chain carries a k- or T-dependence
  (e.g. a level count, a Σ_l without decay, a 1/κ_{k-1} not compensated).

### PRE-STATED addendum (appended after READING, before any criteria file, script or written derivation)

New input received while reading (coordinator message): a second Opus 5.5 review, REVIEW55_BFTB.md Finding 5
(l.153-188) with check `checks/r55b_dip_*`, reaches X1's conclusion by a "dipole identity" route and claims the
WHOLE of (CO-fun) as stated in BFT_B §31.2 (sup and Hölder halves) on class (cc). Instruction: treat X1 and Finding 5
as two independent derivations of the sup half, rest T1/T2 on whichever is cleaner, CONDITIONAL until Codex reports,
say exactly where they disagree, and state T2 relative to Finding 5's scope list (background Z(V_k), full 𝔐-pair
bound, weighted locality, level count).

Reading done before this addendum (no derivation written): REVIEW_BRIEF_55.md; REVIEW55_TENT.md l.1-150, 457-842
(incl. X1, X-T6, X-T7, §8-§10); REVIEW55_BFTB.md l.1-235, 268-278, 600-669; checks/r55b_dip_criteria.md,
r55b_dip_out.txt; COFUN.md l.1-205; BFT_B.md l.3573-3640, 3775-3863, 3946-4131; BFT_A.md l.436-560, 920-935,
1069-1110, 2195-2275, 2401-2500, 2546-2557, 3478-3500; LINEAR_PACKAGE.md l.1-290; REVIEW_BFT_A_S2.md l.145-200;
REVIEW_BFT_B_S9_S10.md l.466-620; REVIEW55_TUNIF.md l.396-450; REVIEW_S22.md l.380-440; KFACTOR_O55.md (header only).
CODEX_REVIEW_X1.md NOT read (to be read last, as instructed).

While reading I formed four suspicions. The targets below that bear on them carry NO pre-registration weight beyond
the label and are marked (c).
- **T5 (c) Simpler flux.** The coarse current b of X1 can be written down explicitly and locally (the level-k
  block-face flux of the source), with the same bound Σ_l π_l(j_l) + ||s_{k−1}||_∞, so that Gale-Hoffman is not
  needed. Refuted if d*b ≠ the root charges for some (cc) source, or the bound fails.
- **T6 (c) Hölder half of the datum part from BL-4, not from LP 4.2.** LP Theorem 4.2 (ii) is a kernel bound
  uniform in the fine offset u and gives no modulus of continuity in u; the Campanato control of the datum response
  is BFT_A Proposition BL-4 (LES + J-str + N2-lin). Refuted if BL-4's Hölder clause does not cover the datum b/κ_{k−1}
  at every α in the window, or if (CO-fun)'s seminorm is not reachable from BL-4's by BL-C.
- **T7 (c) Top residual.** (CO-fun) as stated carries κ_+||r^c_{k−1}||_∞ of the response on its right side, and the
  lane's (Res-Hölder) is also relative to it (REVIEW55_BFTB Finding 1). I suspect the X1 decomposition plus Theorem
  COF's step-(c) argument run with the top response Y^{(b)} (as Theorem W0 step 3 does) bounds the top residual of
  every (cc) source by the class norms. Refuted if any input of that argument is unavailable for non-level-wise
  co-closed (CC-0) plain currents, or if the bound needs a quantity not in the class norms.
- **T8 (c) h-collision is harmless for the datum part.** The gauge-invariant outputs of the DATA problem do not
  depend on which root-covariant h_l is used (both reviewers' collision X-T6 bites only on source responses).
  Refuted by an exact instance where the fixed-order and order-averaged chains give different f_0 or r for the same
  datum.
- Where X1 and Finding 5 differ (to be stated, not assumed): Finding 5 subtracts the straight path current P(b) and
  needs its dipole identity (P(b) ≡ residual source b + divergence-form G_{k−1}); X1 subtracts Q^T b directly. If either
  step fails exactly in the lane's model, that route is withdrawn.

Numeric checks: only `checks/cc55_*`, criteria file first, exact Fractions/ints, single thread, designed-FAIL
controls; algebra only (no k-uniformity can be measured at small k).

---

## 0. Check record cc55 (criteria → script → output), and what each clause can decide

Files: `checks/cc55_criteria.md` (written 23:20:31Z, before any script), `checks/cc55_checks.py` (23:23Z),
`checks/cc55_out.txt`, `checks/cc55_err.txt` (only /usr/bin/time's report). ONE run, 23:24:51-23:25:01Z, 9.2 s,
21.5 MB peak, `python3 -I`, nice 10, thread variables = 1, Fractions/ints only. No criterion edited after the run;
nothing post-hoc. Independent construction (no code from r55t/r55b/bb9/bb10/bb11/cf1). Model: d = 2, L = 3, roots =
block centres, the lane's ORDER-AVERAGED root map Q^avg (2 orders in d = 2) and, for the collision tests, the two
fixed-order maps Q^01, Q^10; κ_l = l + 1.

| clause | result | what it can decide (and whether it could fail) |
|---|---|---|
| A1 (k=2,3) | PASS | Q d = d ev and Q = Q_str − d∘h for 01/10/avg: implementation sanity (can fail on any indexing error) |
| A2 (k=2,3) | PASS | **Lemma FLUX (i)-(ii)**: d*_k Φ_l j = blocksum_l(d*_l j) exactly; ‖Φ_l j‖ ≤ 3^{k−l}‖j‖ |
| A3 (k=2,3) | PASS | the random sources are (cc) with q ≠ 0 (non-vacuity of A4-A6) |
| A4 (k=2,3) | PASS | **Lemma FLUX (iii)**: d*b(S) = q(S) exactly, ‖b‖ ≤ c(S); e.g. (max|q|, max|b|, c) = (11, 10, 75), (3, 12, 249) |
| A5 (k=2,3) | PASS | **Lemma DEC (i)**: L_S(x) = L_{S'}(x) + ⟨b, r_{k−1}(x)⟩ on 64 (S, x) pairs (implementation-level identity; C2 shows it is operator-sensitive) |
| A6 (k=2,3) | PASS | **Lemma DEC (ii)**: D(S') = D(S'^G) = D(S'^s) = D(S'^j) = 0 pointwise (S' is (CC-0), Lemma SPLIT valid for it) |
| A7 (k=2,3) | PASS | **X-T7 reproduced**: top residual slot alone has D = ev^{(0→k)T}d*s_{k−1} ≠ 0, root-supported, total 0 |
| A8 (k=2,3) | PASS | **Lemma TS in functional form**: E_src(x; top source b) − E(x; B_k = b/κ_{k−1}) = −‖b‖²/(2κ_{k−1}) for all x |
| A9 (k=2,3) | PASS | **Lemma SF**: D(Hx) = κ_{k−1}ev^{(0→k)T}d*r_{k−1}(x) for every chain (16 random chains) |
| C1-C5 (k=2,3) | all FIRE | Φ_0 omitted ⇒ d*b ≠ q; Q^{01T} in S' vs chain Q^avg ⇒ A5 fails; wrong κ ⇒ A8, A9 fail; bound without ‖s_{k−1}‖ fails on s_{k−1} = δ_b |
| B1 (k=1, solve) | PASS | the gauge-fixed solves are true critical points (Hx = S on all 162 links) |
| B2 | PASS | **Lemma SF at critical points**: κ_0 d*r_0(x) = q exactly, max|q| = 8, 7, 12 |
| B3 | PASS | additivity f_0(S) = f_0(S') + f_0(y), r_0(S) = r_0(S') + r_0(y) + b/κ_0 (linear-algebra consequence of A5/A8; tests the solver) |
| B4 | PASS | **Lemma H-FREE**: the data map's dx_0 and r_0 are identical for Q^avg, Q^01, Q^10 (3 data, incl. b/κ_0) |
| C6 | FIRES | non-vacuity of B4: the three energies differ as functions and the gauge-fixed minimisers x_0 differ |
| B5 (informational) | differ = True | a root-charged plain-current RESPONSE is operator-dependent (Q^avg vs Q^01): the collision X-T6 bites on source responses, not on data |

What cc55 cannot decide (stated in the criteria before running): nothing analytic. k- and T-uniformity of Theorem COF,
BL-4, Proposition W, Corollary FP are quoted inputs; d = 2, k ≤ 3, abelian, 2 orders (not 24); Part B is k = 1 only.

---

## 1. Symbols pinned (systemic defect 1), and the conventions used below

- **Setting LIN^cc**: BFT_B §27.1 l.3586 (Setting LIN of BFT_A §7.1 with the plain currents' co-closedness dropped and
  replaced by Ξ^TS = 0). **E_src**: BFT_A l.449, E_src(x; B_k) = ½‖dx_0‖² + Σ_{l<k}(κ_l/2)‖r_l(x)‖² −
  Σ_{l<k}[⟨G_l, dx_l⟩ + ⟨j_l, x_l⟩ + ⟨s_l, r_l(x)⟩], r_l(x) = Q_lx_l − x_{l+1}, x_k = B_k. (CO-fun) has B_k = 0.
- **Q_l = the chain's root map** = "the linearised S4′ root map" (BFT_A l.446), which LINEAR_PACKAGE §1.2 (l.66-72)
  defines ORDER-AVERAGED; **h_l is defined by Q_l = Q_{str,l} − d∘h_l** (BFT_A l.447) and is therefore the
  order-averaged slice functional. The "fixed coordinate order" description at BFT_B §27.1 l.3589 / §29.2 is of a
  different operator (REVIEW55_TENT X-T6). Every statement below uses h_l only through (a) the chain identity
  Q_l = Q_{str,l} − d∘h_l, (b) root covariance Q_l∘d = d∘ev (true for both operators; cc55 A1), (c) Lemma FT (i)'s
  block-interior support and |c| ≤ 1 (true for both: every axial path from c_X to y ∈ B(X), in any order, stays in
  B(X)). The one numerical constant that sees h is w := max|kernel of h_l| = 10/81 for the lane's operator at d = 4,
  L = 3 (r55t A4; not recomputed here); I write every bound with w and note that FT (i)'s w ≤ 1 is also valid.
- **Chain coefficients** S_l := d*G_l + j_l + Q_l^Ts_l − s_{l−1} (s_{−1} := 0); with x_k = 0 the source's linear term is
  L_S(x) := Σ_l⟨S_l, x_l⟩. **D(S) := Σ_{0≤l≤k−1}ev^{(0→l)T}d*S_l**, a level-0 function (BFT_B l.3587), always read
  POINTWISE here. **(cc)**: D(S) supported on the level-k roots with total 0 (⟺ Ξ^TS = 0 on Λ_0). **(CC-0)**: D(S) = 0
  pointwise (BFT_B l.3962). **q(S)** := the level-k function with ev^{(0→k)T}q(S) = D(S) (the root charges).
- **Norms** (BFT_A §7.2 l.457-470, BFT_B l.3591): π_l(j) := L^{3(k−l)}sup_own|j| (= ‖j^c_l‖_∞); ‖j‖_Pc :=
  max_{1≤l≤k−1}L^{θ(k−l)}π_l(j_l); ‖s‖_R := max_lL^{θ(k−l)}L^{k−1−l}‖s^c_l‖_∞, so ‖s_{k−1}‖_∞ ≤ L^{−θ}‖s‖_R (s^c_{k−1} =
  s_{k−1}: a level-k 1-form is in coarse units already); ‖G‖_Y := max_lω_l(‖G^c_l‖_∞ + [G^c_l]_α). [·]_α = Campanato,
  [·]^∞_α = pointwise (separations ≤ 1 coarse unit), BFT_A l.458-461. f_0 := n²dx_0. θ is the class exponent COFUN
  calls θ_c (never θ_w). **N(S)** := ‖G^c_0‖_∞ + [G^c_0]_α + ‖j^c_0‖_∞ + ‖j‖_Pc + ‖G‖_Y + ‖s‖_R (= (CO-fun)'s right side
  without the top-residual term). **|j|_Σ := Σ_{0≤l<k}π_l(j_l)** (level-summed plain norm); |j|_Σ ≤ ‖j^c_0‖_∞ +
  ‖j‖_Pc/(L^θ − 1).
- **Collisions avoided below**: C_C is BOTH COF-size's (1 + 2d(1−L^{−3})^{−1})(1 + (1−L^{−θ})^{−1}) (BFT_B l.4063) and
  BL-C's 2^α(8·2^α/(2^α−1) + 32·4^α) (BFT_A l.508): written **C_size** and **C_BLC**. G_D is BOTH BL-4's m = 0 data
  constant (BFT_A l.510) and Proposition W's weighted G_D(m) (l.928, = e^{20m}G_D♭): written **G_D** and **G_D(m′)**.
  A := 4κ̂G_D(m′)S(m′)/κ_− is COF's (BFT_B l.4093). C_fun is Theorem COF's constant (BFT_B l.4076).

---

## 2. T4 — X1 re-checked step by step (REVIEW55_TENT l.606-642), and a local form of its flux

I re-derived every step X1 uses. **No step fails.** Two of X1's steps can be replaced by simpler or already-banked
ones (2.2, 2.4), which matters for the weighted clause and for review.

### 2.1 X1 step (1), the cut bound — **CONFIRMED** (re-derived; also a corollary of Lemma FLUX below)
For a set A of level-k sites let Ã_l be the level-l sites whose level-k ancestor is in A. Placement ev^{(0→l)T} puts
the value at a level-l site Z at a level-0 site inside the level-0 block of Z's level-k ancestor, so for every
level-l function f: Σ_{z∈Ã_0}(ev^{(0→l)T}f)(z) = Σ_{Z∈Ã_l}f(Z). Since D(S) vanishes off the level-k roots,
Σ_{X∈A}q_X = Σ_lΣ_{Z∈Ã_l}(d*S_l)(Z). The G-slots give 0 pointwise (d*d* = 0); a residual slot s_l (l ≤ k−2) gives
Σ_{Y∈Ã_{l+1}}(d*s_l)(Y) through Q_l^Ts_l (d*Q^T = ev^Td*, BFT_A l.607) and the opposite amount through −s_l in S_{l+1}:
they cancel; the top slot leaves Σ_{X∈A}(d*s_{k−1})(X). Each sum Σ_{Z∈Ã_l}(d*j_l)(Z) is the net flux of j_l through
∂Ã_l, and each level-k boundary face of A is crossed by exactly L^{3(k−l)} level-l links, so
|Σ_{X∈A}q_X| ≤ |∂A|·c(S), **c(S) := Σ_{l<k}π_l(j_l) + ‖s_{k−1}‖_∞**, as X1 states.

### 2.2 X1 step (2), Gale-Hoffman — **CONFIRMED, and unnecessary.** Lemma FLUX gives the current explicitly.
*Classical fact (correct as X1 uses it):* on a finite undirected (multi)graph with uniform capacity c and a neutral
demand q, a flow b with d*b = q, |b| ≤ c exists iff |Σ_Aq| ≤ c|∂A| for every vertex set A (Gale 1957; or max-flow
min-cut with a super-source/sink: the cut {s} ∪ A has capacity Σ_{X∉A,q_X>0}q_X + Σ_{X∈A,q_X<0}|q_X| + c|∂A|, which is
≥ Σ_{q>0}q iff q(A) ≤ c|∂A|). But nothing non-constructive is needed:

> **Lemma FLUX (explicit, local root-charge current). PROVEN-HERE (elementary; cc55 A2, A4; controls C1, C5 fire).**
> For 0 ≤ l < k define Φ_l (level-l 1-forms → level-k 1-forms) by **Φ_lj(X, μ) := Σ j(Z, μ) over the level-l μ-links
> (Z, μ) with Z ∈ B_l(X) := L^{k−l}X + {0,…,L^{k−l}−1}⁴ and Z + e_μ ∉ B_l(X)** (the links leaving the level-k block of X
> through its upper μ-face). Then
> (i) d*_kΦ_lj = blocksum_l(d*_lj), i.e. (d*Φ_lj)(X) = Σ_{Z∈B_l(X)}(d*j)(Z);
> (ii) |Φ_lj(X, μ)| ≤ L^{3(k−l)}sup_own|j| = π_l(j), and Φ_lj(X, μ) reads j only on the links crossing the one face
> between B_l(X) and B_l(X + e_μ);
> (iii) for every Setting LIN^cc source S with B_k = 0, **b(S) := Σ_{l<k}Φ_l(j_l) + s_{k−1}** satisfies
> **d*b(S) = q(S)** and **‖b(S)‖_∞ ≤ c(S) ≤ |j|_Σ + L^{−θ}‖s‖_R ≤ ‖j^c_0‖_∞ + ‖j‖_Pc/(L^θ − 1) + ‖s‖_R.**
>
> *Proof.* (i) With (d*j)(Z) = Σ_μ[j(Z − e_μ, μ) − j(Z, μ)] (the adjoint of d), summing over Z ∈ B_l(X) cancels every
> link with both ends in the block; what remains is the inflow through the lower μ-faces — exactly the upper-face links
> of B_l(X − e_μ) — minus the outflow through the upper μ-faces: Σ_μ[Φ_lj(X − e_μ, μ) − Φ_lj(X, μ)] = (d*_kΦ_lj)(X).
> (ii) The upper μ-face of B_l(X) has L^{3(k−l)} level-l sites (d = 4). (iii) Because D(S) is supported on the level-k
> roots, its block sum over the level-0 block of X equals its root value q(S)(X); by the placement remark of 2.1 and
> the slot-by-slot cancellation of 2.1 that block sum is Σ_lΣ_{Z∈B_l(X)}(d*j_l)(Z) + (d*s_{k−1})(X), which is
> (d*b(S))(X) by (i). The bound is (ii) and the triangle inequality; the last two inequalities are the definitions of
> ‖j‖_Pc (π_l(j_l) ≤ L^{−θ(k−l)}‖j‖_Pc, l ≥ 1, summed geometrically) and of ‖s‖_R. ∎
>
> *What it adds over X1 (2).* b(S) is linear in S, explicit, and **local** (one face), so its weighted version costs
> only e^{O(m)}: the root-charge step creates no obstruction for BFT-3's weighted clause (§6). The cut bound of 2.1 is
> the corollary |Σ_Aq| = |Σ_Ad*b| ≤ |∂A|·‖b‖_∞.

### 2.3 X1 step (3), the subtraction — **CONFIRMED, with X-T7's reclassification made part of the construction**
X1's S′ := S − Q_{k−1}^Tb has D(S′) = 0 by d*Q^T = ev^Td* (CONFIRMED, cc55 A6), but if S has a non-co-closed top
residual slot, S′^j is not (CC-0) and Theorem COF's written proof does not apply (X-T7; cc55 A7). X1 says to reclassify
first; the clean way to do both at once is Lemma DEC (§3), which removes the top slot and the root charges in one
step. X1's norm cost π_{k−1}(Q^Tb) ≤ L³(L^{−3} + 2dw)‖b‖_∞ = (1 + 2dL³w)‖b‖_∞ is **CONFIRMED** (Q^T = Q_str^T − h^Td*,
BFT_A l.608; ‖Q_str^T‖_{∞→∞} = L^{−3}, l.609-610; |d*b| ≤ 2d‖b‖; ‖h^T‖_{∞→∞} = w by block-interior support): with the
lane's w = 10/81 it is 83/3; with FT (i)'s w ≤ 1 it is ≤ 217.

### 2.4 X1 step (4), "the subtracted current IS data" — **CONFIRMED; it is BFT_A Lemma TS, already banked**
At x_k = 0, ⟨s_{k−1}, r_{k−1}(x)⟩ = ⟨Q^Ts_{k−1}, x_{k−1}⟩, so the plain level-(k−1) current Q^Tb, the pure top residual
source s_{k−1} = b, and the datum B_k = b/κ_{k−1} give the same energy up to the constant −‖b‖²/(2κ_{k−1}) (cc55 A8,
exact; control C3 fires). This is **Lemma TS** (BFT_A l.925-927, proof §13.8 from BL-1 (i); CONFIRMED, REVIEW_BFT_A_S3
l.297): same minimiser set in every gauge, outputs equal except r_{k−1}(x) = r_{k−1}(y) + b/κ_{k−1}. X1's sup bound for
the datum, LINEAR_PACKAGE Theorem 4.2 (ii) (l.211-217: |K(X)| ≤ Me^{−m′|X|_1}, uniformly in k, T and the fine offset u),
is **CONFIRMED as a sup bound**; the same follows from BL-4's ‖f_0‖ ≤ 4C_f‖B_k‖_D. **It gives no Hölder control** (see
T1, §4.1).

### 2.5 X1 step (5), linearity — **CONFIRMED** (Lemma FG (iii), BFT_A l.2554-2556: for (cc) sources the gauge-invariant
outputs are those of the Setting-LIN minimiser, so they add over (cc) pieces; cc55 B3).

### 2.6 A second, even shorter current: the response's own top residual. **Lemma SF. PROVEN-HERE (cc55 A9, B2).**
For every chain x with x_k = 0, **D(Hx) = κ_{k−1}ev^{(0→k)T}d*r_{k−1}(x)**, where H is the Hessian of E_src's
quadratic part. *Proof.* For any level-0 λ, ⟨Hx, Ξλ⟩ = Ê(x, Ξλ) and ⟨Hx, Ξλ⟩ = ⟨D(Hx), λ⟩; in Ê(x, Ξλ) the terms
r_i(Ξλ) = Q_id ev^{(i)}λ − d ev^{(i+1)}λ vanish for i ≤ k − 2 (root covariance) and r_{k−1}(Ξλ) = d ev^{(k)}λ (x_k = 0),
so Ê(x, Ξλ) = κ_{k−1}⟨d*r_{k−1}(x), ev^{(k)}λ⟩ for every λ. ∎ Hence at the response of a (cc) source,
**q(S) = κ_{k−1}d*r_{k−1}(x(S))**: the root charges are the divergence of κ_{k−1} times the response's own top residual
(this is Lemma RT-cc (a) at l = k − 1, BFT_B l.3599, read at the top). So b_self := κ_{k−1}r_{k−1}(x(S)) is a second
admissible current, with ‖b_self‖_∞ ≤ κ_+‖r^c_{k−1}‖_∞ — **a term (CO-fun) as stated already carries on its right
side**. With it, (CO-fun) as stated follows from §3-§4 without Lemma FLUX; FLUX is what removes the top residual.

### 2.7 X1's displayed bound and consequences (a)-(e)
- Displayed bound ‖f_0(S)‖_∞ ≤ C_fun N(S′) + (C_D/κ_{k−1})c(S), N(S′) ≤ N(S) + L^θ(1 + 2dL³w)c(S): **CONFIRMED** (with
  the precision that Theorem COF's sup half carries no top-residual term, §4.2).
- (a) sup half of (CO-fun)[cc] holds; S10-11 / BFT_B §35.7 / COFUN §2.1, §7, §9 "FALSE" refuted: **CONFIRMED**
  (conditional on Theorem COF and Lemma TS + BL-4 or LP 4.2 (ii)).
- (b) COF-res's premise "every other term bounded as in Theorem COF" fails whenever the residue is large:
  **CONFIRMED as logic** (f_0 is bounded, so a large residue is compensated inside the complement; agrees with S10-10's
  NOT-VERIFIED and REVIEW55_BFTB Finding 5).
- (c) (TENT-Q), (TENT-osc), face (b), the G_e sign, FB-NBHD, (YH-pin), (ROOT-sup) are not obstructions to the curvature
  half on (cc): **CONFIRMED at m = 0 and the trivial background** (not beyond; §6).
- (d) the level count reappears: **CONFIRMED**, located precisely in §6.4.
- (e) root-level questions harmless: **CONFIRMED for the curvature half**, and with Lemma TOP-cc (§5) also for the top
  residual.
- X1's own scope statement "the Hölder half needs a Hölder bound for the data-to-f_0 map, not checked": **CONFIRMED as
  a statement about X1**; closed in §4.

**Verdict T4: X1 holds at every step.** It rests on Theorem COF (session 10; CONFIRMED as an implication by
REVIEW_BFT_B_S9_S10 S10-6 l.505 and REVIEW55_BFTB Finding 4, with the SPLIT repair) and on banked lane-A data results.

---

## 3. The decomposition used everywhere below

> **Lemma DEC (every (cc) source = a (CC-0) source without top slot + a datum). PROVEN-HERE (cc55 A5, A6, A8, B3).**
> Let S = (G_l, j_l, s_l; B_k = 0) be a Setting LIN^cc source, b := b(S) of Lemma FLUX, b_j := Σ_{l<k}Φ_l(j_l)
> (so b = b_j + s_{k−1}). Define **S′** := (G_l; j′_l; s′_l) with j′_l := j_l (l < k − 1), **j′_{k−1} := j_{k−1} −
> Q_{k−1}^Tb_j**, s′_l := s_l (l ≤ k − 2), **s′_{k−1} := 0**; and let **T_b** be the pure top residual source s_{k−1} = b.
> (For k = 1 the subtraction is in the (P0) slot: j′_0 := j_0 − Q_0^Tb_j.)
> (i) S = S′ + T_b as functionals on chains with x_k = 0: L_S(x) = L_{S′}(x) + ⟨b, r_{k−1}(x)⟩.
> (ii) **S′ satisfies (CC-0) pointwise and has no top residual slot**; hence Lemma SPLIT's pointwise conclusions hold
>   for S′ as written: D(S′^G) = D(S′^s) = D(S′^j) = D(S′) = 0.
> (iii) G and s_{≤k−2} are unchanged, ‖s′‖_R ≤ ‖s‖_R, and ‖j′‖_Pc ≤ ‖j‖_Pc + L^θ(1 + 2dL³w)|j|_Σ,
>   |j′|_Σ ≤ (2 + 2dL³w)|j|_Σ; hence **N(S′) ≤ (1 + L^θ(1 + 2dL³w)K_θ)N(S)**, K_θ := max(1, (L^θ − 1)^{−1}).
> (iv) The response to T_b is the source-free minimiser y with datum b/κ_{k−1} (Lemma TS), with
>   r_{k−1}(x(T_b)) = r_{k−1}(y) + b/κ_{k−1} and all other outputs those of y.
> (v) Every gauge-invariant output adds: f_0(S) = f_0(S′) + f_0(y), r_{k−1}(S) = r_{k−1}(S′) + r_{k−1}(y) + b/κ_{k−1},
>   and likewise for every f_j, r_i (Lemma FG (iii) for the two (cc) pieces).
>
> *Proof.* (i) With x_k = 0, ⟨s_{k−1}, r_{k−1}(x)⟩ + ⟨Q^Tb_j, x_{k−1}⟩ = ⟨s_{k−1} + b_j, Q x_{k−1}⟩ = ⟨b, r_{k−1}(x)⟩.
> (ii) D(S′) = D(S) − ev^{(0→k)T}d*s_{k−1} − ev^{(0→k−1)T}d*Q^Tb_j = D(S) − ev^{(0→k)T}d*b = D(S) − ev^{(0→k)T}q(S) = 0,
> by d*Q^T = ev^Td* and Lemma FLUX (iii). The G-slots and the residual slots of levels ≤ k − 2 have D = 0 pointwise
> (§2.1's cancellation), so D(S′^j) = D(S′) = 0. (iii) Only j_{k−1} changes; §2.3 gives π_{k−1}(Q^Tb_j) ≤ (1 + 2dL³w)
> ‖b_j‖_∞ ≤ (1 + 2dL³w)|j|_Σ (Lemma FLUX (ii)), weighted by L^θ in ‖·‖_Pc; |j|_Σ ≤ K_θ(‖j^c_0‖_∞ + ‖j‖_Pc).
> (iv) Lemma TS (BFT_A l.925-927). (v) linearity. ∎
>
> *Reading.* This is X1 with X-T7's repair built in: the top residual slot and all root charges are moved into ONE
> datum b/κ_{k−1}, of size ≤ c(S); what is left is (CC-0), without the defect that broke Lemma SPLIT.

> **Lemma H-FREE (the data map does not see which h_l is used). PROVEN-HERE (cc55 B4; non-vacuity C6 fires).**
> Let Q_l, Q′_l be root-covariant with Q_l − Q′_l = d∘g_l and g_l(dλ) constant (for the lane's two operators
> g = h′ − h and h(dλ) = mean − root value for both, r55t A7). Then for every datum B_k the source-free problems with
> Q and with Q′ have the same minimum and the same gauge-invariant outputs (all dx_j, all r_j), and the same 𝒩(x).
>
> *Proof.* For a chain x choose a level-0 λ_0 with ev^{(0→k)}λ_0 = Σ_{i<k}ev^{(i+1→k)}g_i(x_i) (prescribed at the level-k
> roots only), put λ_{i+1} := ev λ_i − g_i(x_i) and Ψ(x) := (x_i + dλ_i)_{i<k}. Then Q′_iΨ(x)_i − Ψ(x)_{i+1} =
> Q_ix_i − x_{i+1} for i ≤ k − 2, and for i = k − 1, Q′_{k−1}Ψ(x)_{k−1} − x_k = Q_{k−1}x_{k−1} − x_k because
> d(ev λ_{k−1} − g_{k−1}(x_{k−1})) = 0 by the choice of λ_0. So E_{Q′}∘Ψ = E_Q, dΨ(x)_i = dx_i, and Q′-residuals of Ψ(x)
> are the Q-residuals of x; Ψ is invertible (g_i(dλ) is constant, so the λ's computed from Ψ(x) equal those computed
> from x up to constants, and Ψ^{−1}(x′) = x′ − (dλ_i(x′))). Ψ moves x_0 by a level-0 gradient, so 𝒩 is unchanged. ∎
>
> *Consequence for the collision X-T6.* Everything about the datum part T_b (its f_0, its Hölder seminorm, its
> residuals, 𝒩(Y^{(b)})) is the same for the order-averaged and the fixed-order operator. **Source** responses are not:
> E_{Q′}∘Ψ = E_Q fails once a source pairs with dΛ(x), and cc55 B5 shows the response to a root-charged plain current
> differs between Q^avg and Q^01. So the collision bites exactly on statements about source responses with root
> charges (the witness funnels, Φ_k, COF-res residue values) — as X-T6 says — and on nothing in §4-§6.

*Precision to Lemma H-FREE's proof (appended immediately; the statement is unchanged).* The invertibility sentence
is exact for the lane's two operators (there g(dλ) = 0, so Λ(Ψ(x)) = Λ(x)), but it is not needed in general: the same
construction from Q′ to Q gives Ψ′ with E_Q∘Ψ′ = E_{Q′}, so the two minima are equal and Ψ maps minimisers to minimisers;
since the gauge-invariant outputs are the same at every minimiser of each problem (BFT_A §7.1 l.452-453; LINEAR_PACKAGE
Lemma 2.5), they coincide.

---

## 4. T1 — the Hölder half of (CO-fun) on (cc)

### 4.1 What the cited statements actually give (read, not assumed)
- **LINEAR_PACKAGE Theorem 4.2 / 4.2′ (l.211-221): sup only.** They bound, for each fine offset u separately and
  uniformly in u, the coarse kernel B_k ↦ f_0(n· + u) by Me^{−m′|X|_1}. Nothing is said about K_u − K_{u′}; the bound
  uniform in u gives |f_0(z) − f_0(z′)| ≤ 2C_D‖B_k‖ and no factor |z − z′|^α. Lemma 4.4 (l.261-281) is also per-u.
  **So LP 4.2 does not give the Hölder half of the datum part.**
- **The datum part's Hölder half is LINEAR_PACKAGE §3, packaged as BFT_A Proposition BL-4 (l.510-515):** for every B_k,
  uniformly in k ≥ 1, T ≥ 1, **every α ∈ (0, 1)**: ‖x(B_k)‖_inv ≤ G_D‖B_k‖_D, with ‖f_0‖ ≤ 4C_f‖B_k‖_D and the
  Campanato bound [f_0]_α ≤ C_L(α)(‖f_0‖ + ‖J^c_0‖), ‖J^c_0‖ ≤ κ_{k−1}‖r_{k−1}‖ (inputs: LES = LP Lemma 3.2, J-str = LP
  Lemma 3.1 (c), N2-lin = LP Theorem 3.8). Status: **CONFIRMED given the package, one constant to fix** (REVIEW_BFT_A_S2
  Part 7, l.162-184; fix B7, l.401: the LES box convention changes a factor 4 to ≤ 25 — a constant, not the uniformity).
  ‖·‖_inv contains ‖f_0‖_∞ + [f_0]_α and L^0‖r^c_{k−1}‖_∞ (BFT_A l.462). **Lemma BL-C** (l.507-508; CONFIRMED,
  REVIEW_BFT_A_S2 Part 6 l.149): [H]^∞_α ≤ C_BLC[H]_α + 2·8^α‖H‖_∞ converts to (CO-fun)'s pointwise seminorm.
- **Theorem COF (BFT_B l.4074-4104) DOES give the Hölder half for the root-charge-free remainder**: its statement bounds
  ‖f_0‖_∞ + [f_0]^∞_α for (CC-0) sources, the Hölder half by step (d) (W0 step 4: LES-div + Lemma LE + BL-C, which ask
  only for sup|J_0| — Lemma W0-use step 4, l.4021-4024 — not for co-closedness). Two precisions, both re-derived:
  (1) step (d) uses the identity J_0[S^j] = C(j) − (Q_str^{(0→k)})^Tρ_{k−1}, which needs d*ρ_{k−1} = R_k(D(S^j)) = 0, i.e.
  (CC-0) of S^j, and Lemma SPLIT's "S^j is (CC-0) with S" fails for a non-co-closed top slot (X-T7) — Lemma DEC's S′ has
  no top slot, so this is satisfied; (2) step (d)'s top residual is that of the j-only problem; it differs from S′'s by
  the top residuals of the G- and s-slot responses, which W0, GU and BL-5 (a) bound by source norms (their ‖x‖_inv
  bounds contain L^0‖r^c_{k−1}‖), so COF holds as stated with S′'s own top residual up to the constant.
- **COF's sup half carries no top-residual term** (its steps (a)-(c): W0/GU sups, LIN0/BL-5 (a), and step (c)'s bound
  [C_YN·C_size + A(1−L^{−2})^{−2}C_size](‖j^c_0‖_∞ + ‖j‖_Pc), l.4096-4097). Agree with REVIEW55_BFTB Finding 3/5.

### 4.2 The theorem

> **Theorem CC-FUN ((CO-fun) on the composite-co-closed class). PROVEN-HERE as an implication; unreviewed.**
> At m = 0, the trivial background, and every (α, θ) in Theorem COF's window **0 < α < θ < 1**, there are constants
> C_sup, C_H < ∞ depending only on (C_fun and COF's sup constant, G_D, C_BLC, d, L, α, θ, κ_±, w) — not on k ≥ 1,
> T ≥ 1, the basepoint, the level, or the source — such that for every Setting LIN^cc source S with B_k = 0 in the
> (P0) + (Pl-c) + (G) + (R) classes:
> (a) **‖f_0(S)‖_∞ ≤ C_sup·N(S)** — no top-residual term;
> (b) **‖f_0(S)‖_∞ + [f_0(S)]^∞_α ≤ C_H·(N(S) + κ_+‖r^c_{k−1}(S)‖_∞)** — (CO-fun) exactly as BFT_B §31.2 / COFUN §2.0
>     state it, on the whole class (cc);
> (c) with Lemma TOP-cc (§5): **‖f_0(S)‖_∞ + [f_0(S)]^∞_α + κ_+‖r^c_{k−1}(S)‖_∞ ≤ C_H′·N(S)** — no response quantity on
>     the right.
> Everything holds verbatim with N(S) replaced by the weaker-norm N_Σ(S) := ‖G^c_0‖_∞ + [G^c_0]_α + |j|_Σ + ‖G‖_Y + ‖s‖_R
> (§6.4).
>
> *Proof.* Lemma DEC: f_0(S) = f_0(S′) + f_0(y), y the source-free minimiser with datum b/κ_{k−1}, ‖b‖_∞ ≤ c(S) ≤
> K_θN(S) (Lemma FLUX (iii)).
> (a) COF's sup half for S′ (a (CC-0) source without top slot, so its written proof applies): ‖f_0(S′)‖_∞ ≤
> C_COF,sup·N(S′) ≤ C_COF,sup(1 + L^θ(1 + 2dL³w)K_θ)N(S) (Lemma DEC (iii)). BL-4: ‖f_0(y)‖_∞ ≤ G_D‖b‖_∞/κ_{k−1} ≤
> G_DK_θN(S)/κ_−. Add.
> (b) Seminorms are subadditive. COF for S′: ‖f_0(S′)‖_∞ + [f_0(S′)]^∞_α ≤ C_fun(N(S′) + κ_+‖r^c_{k−1}(S′)‖_∞), and by
> Lemma DEC (v) and BL-4, ‖r^c_{k−1}(S′)‖_∞ ≤ ‖r^c_{k−1}(S)‖_∞ + ‖r_{k−1}(y)‖_∞ + ‖b‖_∞/κ_{k−1} ≤ ‖r^c_{k−1}(S)‖_∞ +
> (G_D + 1)K_θN(S)/κ_−. Datum part: BL-4 gives ‖f_0(y)‖_∞ + [f_0(y)]_α ≤ G_D‖b‖_∞/κ_{k−1}, and BL-C gives
> ‖f_0(y)‖_∞ + [f_0(y)]^∞_α ≤ (1 + 2·8^α + C_BLC)G_DK_θN(S)/κ_−. Add.
> (c) Substitute Lemma TOP-cc into (b). ∎
>
> **Exponent window (the brief's question, verified against the statements).** BL-4: every α ∈ (0, 1). BL-C: every
> α ∈ (0, 1) (C_BLC ~ 1/(α ln 2) as α ↓ 0). Lemma FLUX/DEC: θ > 0 only (through K_θ). Theorem COF: its stated window
> **0 < α < θ < 1** (BFT_B l.4076; α < θ is GU's level sum and LIN0/BL-5 (a)'s α ≤ θ; whether θ < 1 is used by COF's
> steps is COFUN §2.2's question — not load-bearing here). **So the root-charge part adds no constraint: (CO-fun)[cc]
> holds on exactly COF's window, 0 < α < θ_c < 1.** (Intersected with lane A's pair window α ≤ θ ≤ 1 − α this is
> α ∈ (0, ½), θ_c ∈ (α, 1 − α], as COFUN §2.2 and REVIEW55_TENT CF3 state.)

**Verdict T1: the Hölder half of (CO-fun) on (cc) is PROVEN as an implication** of Theorem COF (both halves, on
(CC-0) sources without top slot), Lemma TS, Proposition BL-4 and Lemma BL-C, through Lemmas FLUX and DEC. LP Theorem
4.2/4.2′ are NOT the right input for it (sup only); BL-4 is.

---

## 5. T7 — the top residual of a (cc) response is bounded by the class norms

Why it matters: (CO-fun) as stated, Theorem COF's Hölder half, §31.2 (a)'s residual bounds and Theorem RHT-cc are all
**relative to the response's own top residual** (REVIEW55_BFTB Finding 1: "Its right side contains κ_+‖r^c_{k−1}‖_∞ of
the same response"), and Corollary RHT-V's absolute η² form is NOT-VERIFIED there for exactly this reason ("Missing: a
bound on the top residual of the response to V"). Theorem W0 step 3 bounds the top residual for level-wise co-closed
level-0 sources by Lemma TOPD (BFT_A l.2474-2478); COF's own scope note says the term "could be removed by running (d)
through Lemma TOPD as W0 step 3 does — not done here" (BFT_B l.4104). Here it is done, on the whole class (cc).

> **Lemma TOP-cc. PROVEN-HERE as an implication; unreviewed.** At m = 0, the trivial background, 0 < α < θ < 1: for
> every Setting LIN^cc source S with B_k = 0 in the classes, **‖r^c_{k−1}(S)‖_∞ ≤ C_top^cc·N(S)** (and ≤ C·N_Σ(S)),
> uniformly in k ≥ 1, T ≥ 1 and in the gauge fixing.
>
> *Inputs, status quoted (not re-judged):* Lemma TOPD (BFT_A l.2223-2225, §28.2; CONFIRMED, REVIEW_BFT_A_S6 l.108);
> W0 step 3's 𝒩(Y^{(b)}) ≤ 4n³e^{20m′}(1083G_D(m′) + 40)S(m′)/κ_− via Corollary FP (T ≥ 3; lift for T ≤ 2) (BFT_A
> l.2474-2478; W0 CONFIRMED REVIEW_BFT_A_S6 l.23, this bound ✓ at l.156; Corollary FP CONFIRMED REVIEW_BFT_A_S3 l.327);
> Proposition W (CONFIRMED given the package, REVIEW_BFT_A_S3 l.299); Lemma TS; W0, GU, BL-5 (a); Lemma DF-cc (i), (iii)
> and Proposition COF-size (CONFIRMED: REVIEW_BFT_B_S9_S10 S10-3, S10-5; REVIEW55_BFTB Finding 4).
>
> *Proof.* By Lemma DEC (v), r_{k−1}(S) = r_{k−1}(S′) + r_{k−1}(y) + b/κ_{k−1}, and the last two have sup ≤ (G_D + 1)
> ‖b‖_∞/κ_− ≤ (G_D + 1)K_θN(S)/κ_− (BL-4, Lemma FLUX). Split S′ = S′^G + S′^s + S′^j (legitimate: Lemma DEC (ii)).
> (1) S′^G: Theorem W0 (level 0) and Theorem GU (levels ≥ 1, summed against ω_l = L^{θ(k−l)} with α < θ) bound ‖x‖_inv,
> which contains ‖r^c_{k−1}‖_∞: ≤ C_W0(‖G^c_0‖_∞ + [G^c_0]_α) + C_GU′‖G‖_Y.
> (2) S′^s (residual slots of levels ≤ k − 2 only): BL-5 (a) gives ‖x‖_inv ≤ G_R‖s′‖_R ≤ G_R‖s‖_R (α ≤ θ).
> (3) S′^j (plain currents j′, D(S′^j) = 0 by Lemma DEC (ii), not level-wise co-closed). Lemma TOPD holds for any source
> with a critical point (its proof uses only criticality, BFT_A l.2410-2412; equivalently Lemma FG (ii)), so for every
> level-k link b, r_{k−1}(x(S′^j))(b) = Σ_l⟨j′_l, Y^{(b)}_l⟩, with Y^{(b)} the response to the top source δ_b, i.e.
> (Lemma TS) the source-free minimiser y^{(b)} with datum δ_b/κ_{k−1}. BL-1 (ii) summed over l (the telescoping of
> COF (c), l.4087-4088) gives, for this fixed chain,
>   Σ_l⟨j′_l, Y_l⟩ = ⟨C(j′), Y_0⟩ − Σ_{0≤m≤k−2}⟨Σ_{l>m}(Q^{(m+1→l)})^Tj′_l, r_m(Y)⟩.
> *First term:* d*C(j′) = D(S′^j) = 0 (DF-cc (i)), so ⟨C(j′), Y_0⟩ = ⟨C(j′), Y_0 + dλ⟩ for every level-0 λ and
> |⟨C(j′), Y_0⟩| ≤ sup|C(j′)|·𝒩(Y^{(b)}) ≤ n^{−3}π_0(C(j′))·4n³e^{20m′}(1083G_D(m′) + 40)S(m′)/κ_− =: C_𝒩·π_0(C(j′)),
> and π_0(C(j′)) ≤ C_size(‖j′^c_0‖_∞ + ‖j′‖_Pc) (COF-size, (CC-0) of S′^j).
> *Residual terms:* by DF-cc (iii) the operators are Q_str^T acting on ĵ′; for m ≤ k − 2, r_m(Y^{(b)}) = r_m(y^{(b)})
> (Lemma TS), the data residuals are co-closed with κ_mr_m = κ_{k−1}(Q_str^{(m+1→k)})^Tr_{k−1} (W0 step 3), and
> ‖Q_str^Tu‖_1 ≤ L‖u‖_1 per step (BFT_A l.3492-3493), so ‖r_m(y^{(b)})‖_1 ≤ κ̂L^{k−1−m}‖r_{k−1}(y^{(b)})‖_1; Proposition W
> at weight m′ centred at b (as W0 step 3 and PW-cc use it) gives |r_{k−1}(y^{(b)})(b′)| ≤ G_D(m′)κ_−^{−1}e^{−m′d(b′,b)},
> hence ‖r_{k−1}(y^{(b)})‖_1 ≤ 4G_D(m′)S(m′)/κ_− and ‖r_m(y^{(b)})‖_1 ≤ A·L^{k−1−m} with COF's A. The sum is COF (c)'s sum
> without its n²: with m = l − 1 − a, L^{−3a}L^{−3(k−l)}L^{k−l+a} = L^{−2a}L^{−2(k−l)}, so the residual terms are
> ≤ A(1 − L^{−2})^{−2}max_lπ_l(ĵ′_l) ≤ A(1 − L^{−2})^{−2}C_size(‖j′^c_0‖_∞ + ‖j′‖_Pc).
> Hence ‖r_{k−1}(S′^j)‖_∞ ≤ C_size[C_𝒩 + A(1 − L^{−2})^{−2}](‖j′^c_0‖_∞ + ‖j′‖_Pc), and Lemma DEC (iii) converts to N(S).
> Γ-uniformity: the top residual is a gauge-invariant output (Lemma FG (iii)). ∎
>
> *The same with N_Σ:* COF-size's step 3 (π_0(C(j)) ≤ Σ_lπ_l(ĵ_l)) and FT (ii) give π_0(C(j′)), max_lπ_l(ĵ′_l) ≤
> (1 + 2d(1 − L^{−3})^{−1})|j′|_Σ = (121/13)|j′|_Σ at d = 4, L = 3, so every bound above holds with |j|_Σ in place of
> ‖j^c_0‖_∞ + ‖j‖_Pc.

**Consequences.** (i) Theorem CC-FUN (c) holds: (CO-fun) on (cc) with no response quantity on the right. (ii) BFT_B
§31.2 (a)'s residual bounds and Theorem RHT-cc's N_res bound, which carry κ_+‖r^c_{k−1}‖_∞, become absolute in N(S)
on (cc). (iii) For the BCH₂ rows V (Corollary RHT-V), Lemma TOP-cc gives ‖r^c_{k−1}(x(V))‖_∞ ≤ C·N_Σ(V) = O((k−1)η²)
— so RHT-V's absolute form is now PROVEN as an implication **with a factor (k − 1)**, not with η²; its k-uniform form
still needs the level-decay input of §6.4.

---

## 6. T2 — assembly: BFT-5 clause (b)'s curvature half on (cc)

### 6.1 The assembled statement
> **Theorem CC-INV ((NC-Γ)_cc at the trivial background, both halves, in the class norms). PROVEN-HERE as an
> implication; unreviewed.** At m = 0, the trivial background, 0 < α < θ < 1: for every Setting LIN^cc source S with
> B_k = 0 in the (P0) + (Pl-c) + (G) + (R) classes, the response x = 𝓛_Γ^{−1}S obeys
>   **‖x‖_inv = max_j[‖f_j‖_∞ + [f_j]_α + L^{k−1−j}‖r^c_j‖_∞] ≤ C_inv·N(S)  (and ≤ C·N_Σ(S)),**
> together with the pointwise ‖f_0‖_∞ + [f_0]^∞_α ≤ C_H′N(S), uniformly in k ≥ 1, T ≥ 1 and the gauge fixing Γ.
>
> *Components.* f_0 pair: Theorem CC-FUN (c). Top residual: Lemma TOP-cc. Lower residuals: BFT_B §31.2 (a) (l.3794-3797;
> from Lemma RT-cc (c) + Lemma TC; RT-cc CONFIRMED by REVIEW55_BFTB Finding 1), whose right side is
> κ_−^{−1}[L^{−θ(m+1)}‖s‖_R + L^{−m}(κ_+‖r^c_{k−1}‖_∞ + ‖s^c_{k−1}‖_∞ + C|j|_Σ) + C L^{−θm}‖G‖_Y] (m = k − 1 − i; I re-did the
> G-term: L^{−m}Σ_{l>i}6L^{k−l}‖G^c_l‖ ≤ 6L^{−θm}‖G‖_Y/(1 − L^{−(1−θ)}), using θ < 1) — absolute by TOP-cc. Tower
> f_j (j ≥ 1): §31.2 (b) / Proposition INV-cc (l.3798-3800; session 9, "PROVEN as a reduction"; not adjudicated by name
> in REVIEW_BFT_B_S9_S10 or REVIEW55_BFTB), which is Theorem W0 step 5's argument (CONFIRMED with W0): f_j =
> 𝒜^{(0→j)}f_0 − R_j, ‖(dr_i)^c‖ ≤ 4L^{k−1−i}‖r^c_i‖, [R_j]_α ≤ Σ_{i<j}4L^{α(k−j)}L^{k−1−i}‖r^c_i‖_∞. Summability
> (re-checked): k − 1 − i ≥ k − j for i < j, so with the per-level decays above Σ_{i<j}L^{α(k−j)}L^{−θ(k−1−i)} ≤
> L^{(α−θ)(k−j)}(1 − L^{−θ})^{−1} ≤ (1 − L^{−θ})^{−1} for α ≤ θ. ∎

### 6.2 What this is, and is not, of BFT-5 clause (b) (BFT_B l.3831; REVIEW_S22 l.430-432)
Clause (b) asks, at the background Z(V_k), in SF/RTARGET §33's 𝔐-pair (field components, Hölder curvature),
‖x‖_𝔐 ≤ C_5‖S‖_{𝔐*} for every composite-co-closed S, plus BFT-3's weighted locality at rate ≥ m_Y. **Theorem CC-INV is
its gauge-invariant half at Z = 1 and m = 0.** In Proposition BFT5-red (l.3837-3851) the composite-co-closed clause
"additionally inherits (NC-Γ)_cc's status, i.e. it is CONDITIONAL on (CO-fun) for the curvature half" (l.3851): **that
condition is now discharged, as an implication.** Relative to REVIEW55_BFTB's scope list (Finding 7 (iii)) what remains
for clause (b) is, item by item:
- **(R1) the full 𝔐-pair bound (gauge-variant components).** Needs (G♯_0-field) (BFT5-red input (1), OPEN; BFT_A BL-7
  (e)). CC-INV gives nothing here: ‖x‖_inv ≤ 2‖x‖_{𝔐^∇} is the wrong direction.
- **(R2) the background Z(V_k).** Needs (R♯_ω) (OPEN), Lemma Rω-frame (ARGUED), SF's Lemma G-pert (PROVEN-HERE
  implication, one-gauge X_c-small scope) and (G♯-patch^Ω) (OPEN; REVIEW55_BFTB Finding 9: NOT-VERIFIED as
  bookkeeping) — quoted, not re-judged. **New for the (cc) mechanism:** every identity behind Lemmas FLUX/DEC/SF/TOP-cc
  must be re-established with Z-covariant operators — the flat d* in FLUX's Gauss law, root covariance d*Q^T = ev^Td* in
  DEC (ii) (REVIEW55_BFTB REFUTED-item 11: lane A's Q_l^Z is root-covariant only up to a defect ≲ Cρ²_{l+1}f_k on
  straight-row towers), Lemma SPLIT (item 13: S^G is not composite-co-closed at curved Z), and Ker H_Z = Ran Ξ_Z ((N1-nd),
  item 2). Named here **(CC-dec_Z)**: "at Z(V_k) every composite-co-closed source is a (CC-0)_Z source plus a datum with a
  bounded flux, up to priced defects" — **OPEN**. (Lemma TS itself is algebraic in r_{k−1} and survives wherever
  r_{k−1} is affine in x_k.)
- **(R3) weighted locality, m > 0.** Lemma FLUX is one-face local (weights cost e^{O(m)}); the datum part has
  Proposition W / Theorem W (CONFIRMED, REVIEW_BFT_A_S3 l.299); FT (iv) prices the funnel at e^{2m}. **The binding item
  is Theorem COF at m > 0** (its level-0 pairing needs YH_m: 𝒬_{H,m} ARGUED; DX_m, DB_m OPEN — BFT_A §28.13 heading),
  and TOP-cc_m needs W0 step 3's weighted form (BFT_A l.2614, stated for level-0 co-closed sources). The (cc) step adds
  no new obstruction at m > 0.
- **(R4) the rows' level count** — §6.4. This is not a defect of clause (b) as a linear estimate (CC-INV is k-uniform in
  the source norm); it is the size of the rows in that norm.

### 6.3 Exactly what is PROVEN given X1 (no more)
Inputs (all quoted with status): Theorem COF (BFT_B §35.5; CONFIRMED as an implication by S10-6 and REVIEW55_BFTB
Finding 4, with the SPLIT repair) and through it YH, W0 (steps 3-5), GU, LIN0/BL-5 (a), PW-cc, RT-cc, FT, DF-cc,
COF-size; Lemma TS; Proposition BL-4 (CONFIRMED-WITH-FIX) and Lemma BL-C; Lemma TOPD, Corollary FP, Proposition W;
BFT_B §31.2 (a)-(b) (quoted; summability re-checked). Proven here as implications: Lemma FLUX (elementary, no input),
Lemma SF, Lemma DEC, Lemma H-FREE, Theorem CC-FUN (a)-(c), Lemma TOP-cc, Theorem CC-INV. Scope: m = 0, Z = 1,
gauge-invariant outputs, 0 < α < θ < 1, every k ≥ 1, T ≥ 1, Γ.

### 6.4 The level count ≈ 25(k−1): interface only (KFACTOR_O55 is on it; not solved here)
For the rows of BFT_A Corollary NC (W_l in (G), V_l plain, level-0 pieces in (P0)), π_l(V_l) ≤ 2C_NCC_bchκ_+L²η²
**uniform in l** (BFT_B l.3735; BFT_A [RBA2-fix] B3 l.819-824), so |V|_Σ ≲ (k − 1)·2C_NCC_bchκ_+L²η² + π_0(V_0) and
‖V‖_Pc ≍ L^{θ(k−1)}η² (S10-6). Every constant in §2-§6.1 is k-uniform; **k enters only through the rows' source norm**,
at exactly these places:
- **(I1) COF-size step 3**, π_0(C(V)) ≤ Σ_lπ_l(V̂_l) ≤ (121/13)|V|_Σ — consumed by COF (c), COF (d) and the first term of
  TOP-cc. This is S10-6's place: ≈ 9.31(k − 1)×(row size) in the Σ-form, ≈ 25(k − 1)×(row size) in the class-norm form
  at the optimal θ = 1/((k−1)ln L).
- **(I2) the residual terms** of COF (c) and TOP-cc: max_lπ_l(V̂_l) — a max, not a sum: **no k**.
- **(I3) Lemma FLUX**, ‖b(V)‖_∞ ≤ Σ_l‖Φ_l(V_l)‖_∞ + ‖s_{k−1}‖_∞ ≤ |V|_Σ + ‖s_{k−1}‖_∞ — consumed by DEC (iii) and by the
  datum part (BL-4). Same order as (I1); it reads only the net level-k face fluxes Φ_l(V_l), which can be smaller than
  π_l(V_l), but no gain is established.
**So X1/FLUX neither removes nor worsens the level count**: by this route the curvature half on the rows is
O((k − 1)η²) — an upper bound; whether f_0 of the rows actually grows is not decided here. **Interface condition:** a
k-uniform bound on Σ_lπ_l(V̂_l) (equivalently a carrier-class input COF-size can consume, cf. lane A's CO-B via SPD,
REVIEW55_TUNIF W9 (e)) closes the curvature half on the rows with no change to anything in §2-§6.1, since it also bounds
(I3). The norm is not slack: BL-6 (b)'s family (BFT_A l.535-540; constant coarse currents (Q^{(l→k)})^Tce_μ at every level,
level-wise co-closed, hence (cc)) has r_{k−1} = (k − 1)c/κ_{k−1} exactly while |j|_Σ = (k − 1)|c| — Lemma TOP-cc's
Σ-form is sharp up to its constant, so no level-max norm can carry a k-uniform top-residual bound on (cc).

**Verdict T2.** (NC-Γ)_cc, both halves, at Z = 1 and m = 0, in the class norms: **PROVEN as an implication** (it was:
residual half relative to the top residual, curvature half CONDITIONAL on (CO-fun)). (BFT-5_E) clause (b): **still
OPEN**, with (R1) (G♯_0-field), (R2) the background transfer incl. the new (CC-dec_Z), (R3) weighted COF; its (NC-Γ)_cc
input is discharged at Z = 1, m = 0. Applied to the contraction's rows: O((k − 1)η²); k-uniform only with (I1)'s input.

---

## 7. T3 — the two defects the X1 reviewer found nearby

### 7.1 Lemma SPLIT's "D(S^s) = 0" (BFT_B §35.2 l.4031-4037) — **defect CONFIRMED; repair CONFIRMED; moot under DEC**
- *The defect.* For a top residual slot, D(S^s) = ev^{(0→k)T}d*s_{k−1} pointwise: nonzero, root-supported, total 0
  (cc55 A7, my code, exact at k = 2, 3; agrees with r55t E2 and r55b D5). The proof's "r_i(x + Ξλ) = r_i(x) for every λ"
  holds for i ≤ k − 2 and for λ ∈ Λ_0; at i = k − 1 with x_k fixed, r_{k−1}(x + Ξλ) = r_{k−1}(x) + d ev^{(k)}λ (§2.6).
  Lower slots give 0 pointwise (§2.1). Consequence: "S (CC-0) ⇒ S^j (CC-0)" fails when s_{k−1} is not co-closed
  (r55b D7), and COF's steps (c) (co-closedness of C(j)) and (d) (the identity J_0[S^j] = C(j) − (Q_str^{(0→k)})^Tρ_{k−1})
  are then unsupported. Step (b) is NOT affected (BL-5 (a) covers every residual source, the top one included).
- *The repair (X-T7):* at x_k = 0, ⟨s_{k−1}, r_{k−1}(x)⟩ = ⟨Q^Ts_{k−1}, x_{k−1}⟩ exactly, so moving Q^Ts_{k−1} into
  j_{k−1} changes no response and no output, makes D(S^s) = 0 pointwise, and costs π_{k−1}(Q^Ts_{k−1}) ≤
  (1 + 2dL³w)‖s_{k−1}‖_∞ ≤ (1 + 2dL³w)L^{−θ}‖s‖_R in ‖j‖_Pc. **CONFIRMED.** REVIEW55_BFTB Finding 4's alternative
  (j_{k−1} += P(s_{k−1}), G_{k−1} −= Σ_bs_{k−1}(b)G_b) is also valid.
- *Theorem COF's statement survives* (for (CC-0) sources with a top slot, apply the repair first). **Under Lemma DEC
  the question does not arise**: S′ has no top slot at all — the top slot is moved, with the root charges, into the
  datum T_b. Lemma DF-cc (i) "d*C(j) = D(S)" must likewise be read with D(S^j) (agree REVIEW55_BFTB Finding 4).

### 7.2 The two operators called h_l — **collision CONFIRMED (X-T6); no step of §2-§6 depends on it**
- I did not recompute the d = 4 constants (10/81 vs 1/3, r55t A4); my model has d = 2 with two orders.
- Every step above is stated for the lane's operator (§1): FLUX uses no h; DEC (i)-(ii) and SF use only the chain's own
  Q_l and root covariance (true for both operators, cc55 A1); DEC (iii) uses w (lane's 10/81; FT (i)'s ≤ 1 also valid);
  the datum part is h-free (Lemma H-FREE, cc55 B4 exact, C6 fires); Theorem COF and TOP-cc use FT (i)-(ii) (block-interior
  support, |c| ≤ 1 — true for the order-averaged operator because every axial path of every order from c_X to y ∈ B(X)
  stays in B(X); FT (ii) is operator-free) and the algebraic identities RF, DF-cc, which hold for whatever h defines the
  chain's Q. **So BFT_B §27.1 l.3589's fixed-order parenthetical is a description error, not a proof error, for COF.**
- Where the collision does bite (cc55 B5): the response to a root-charged plain current differs between Q^avg and Q^01.
  Exact values of source-response objects — witness funnels, Φ_k(Y^p), COF-res residues, 65/26244, 243/260 — are
  operator-specific, as X-T6 says. CC-FUN never uses such a value.
- One more control from cc55 C2: Lemma DEC (i) FAILS if the subtracted current is built with a different h than the
  chain (Q^{01T}b_j against chain Q^avg). The identity "the subtracted current IS data" holds only with the chain's own
  Q — X1 states it that way; any re-use must keep it so.

---

## 8. X1 (REVIEW55_TENT) vs REVIEW55_BFTB Finding 5 — where the two derivations differ

They agree on every conclusion they share. Differences, all of route:
1. **What is subtracted.** X1 subtracts Q_{k−1}^Tb (≡ top source b ≡ datum b/κ_{k−1}, Lemma TS) and leaves the rest
   for Theorem COF. Finding 5 subtracts the straight path current P(b) = Σ_bb(b)·path_b and needs its **dipole identity**
   P(b) ≡ (s_{k−1} = b) + (G_{k−1} = Σ_bb(b)G_b) (r55b D2, checked in d = 2 with one order; it uses only that every S4′
   contour of b stays in B(X) ∪ B(X + e_μ), true for every order). The two remainders differ by the divergence-form
   source d*G(b) at level k − 1, which Finding 5 sends to Theorem GU and X1 leaves inside S′. Both valid; X1's route needs
   no box-local 2-form G_b and no Bogovskii-type solve. I did not re-derive the dipole identity (not used here).
2. **The current b.** Both use the cut bound + max-flow (Gale). Lemma FLUX replaces both by an explicit one-face-local
   current with the same bound — needed for the weighted clause, cosmetic otherwise.
3. **The top residual slot.** X1 puts ‖s_{k−1}‖_∞ into c(S) and reclassifies (X-T7); Finding 5 handles plain currents
   in its general case and the top slot by its Finding-4 repair. Equivalent; DEC does both at once.
4. **The Hölder half.** X1: "not covered" (true of X1). Finding 5: holds, "with COF's κ_+‖r^c_{k−1}‖ term (of S^{j′}'s
   response, which differs from S's by LIN0-bounded pieces)" — **CONFIRMED, but its justification is one line**: the
   datum piece's Hölder bound is BL-4 (inside LIN0's package via BL-7 (a)) converted by BL-C, and COF's step (d) needs
   S′ without a non-co-closed top slot. §4 supplies both.
5. **"The sup half needs no top-residual term"** (Finding 5, Finding 3): **CONFIRMED** (§4.1).
6. **"Conditional only on the lane-A inputs Theorem COF already quotes"** (Finding 5): CONFIRMED with two precisions:
   Theorem COF itself is a session-10 (lane B) input, and the datum piece uses Lemma TS + BL-4 + BL-C (lane A, banked).
7. **Scope of what still blocks clause (b)** (Finding 7 (iii): background Z(V_k), full 𝔐-pair bound, weighted locality,
   level count): **agree**; §6.2 states the result relative to exactly these, adds the (cc)-specific background item
   (CC-dec_Z), and moves the top-residual gap (Finding 1's NOT-VERIFIED for RHT-V) to "PROVEN with a factor k − 1".
8. Finding 7's reading of BFT_B l.3810 (functional on Λ_0 vs pointwise; correct formula at l.4202): **spot-checked only**
   (BFT_A l.2951's sentence "As a level-0 function, D(S^E_0(S)) = I_χ^TD(S)" quoted by Finding 7 not re-read); not used.

**No disagreement found.** If one of the two routes is withdrawn by Codex, §2-§6 stand on the other except for item 1
(the subtracted object), and on Lemma FLUX for item 2 in either case.

*§8 item 8, completed (appended 23:39Z, after re-reading):* BFT_A l.2951 reads "Ξ^TS^E_0(S) = 0 on Λ_0. As a level-0
function, D(S^E_0(S)) = …" and BFT_B l.4202 gives D(S^E_0(S)) = I_χ^TD(S) pointwise, while l.3810's "D(S^E_0(S)) = 0" is
the Λ_0 statement. Finding 7's reading: **CONFIRMED by reading.** One consequence for this file: l.4203's "Theorem COF
applies to S^E_0(S) **except** for Proposition COF-res's residue" is superseded by Theorem CC-FUN, which applies to the
(cc) source S^E_0(S) entirely; off the critical set what remains is the class-norm size of the correction Γ_E^TD(S)
(its (P0)-slot size, l.4203-4204) — REVIEW55_TENT §9's second item, not touched here.

---

## 9. CODEX_REVIEW_X1.md (read last, as instructed), and whether it changes anything

Read at 23:38Z: 30554 B, 745 lines, mtime 23:16Z (it was 1876 B when the brief was written). It ends with a complete
"Final verdict" paragraph; **its display (18) is visibly truncated on disk** ("\left[C_0(1+L^\theta A_L C_c)+ \quad}" —
the remainder of the bracket and the N_src factor are missing), so (16)-(17) are the bankable form there.

| Codex X1 item | its verdict | mine | note |
|---|---|---|---|
| §1 top residual contributes root divergence; SPLIT's "D = 0 for every residual slot" | CONFIRMED / REFUTED | **AGREE** | cc55 A7 (my code) |
| §2 cut control; explicit face-flux current F_lj_l, b = a + s_* | CONFIRMED | **AGREE — independent coincidence** | it is my Lemma FLUX, found separately (cc55 A2, A4); same convention, same bound c(S) |
| §3 datum identification; LP 4.2 hypotheses; C_D = row-sum constant 4M((1+e^{−m′})/(1−e^{−m′}))⁴ | CONFIRMED | **AGREE** | = Lemma TS; BL-4 gives the same with 4C_f |
| §4 remainder in COF's class with N_src; S′: j′_{k−1} = j_{k−1} − Q^Ta, s′_{k−1} = 0 | CONFIRMED | **AGREE — independent coincidence** | it is my Lemma DEC (cc55 A5, A6) |
| §4 X1's literal N(S′) comparison if N includes the response residual | NOT-VERIFIED | **AGREE**, and closed | §4.2 (b): ‖r^c_{k−1}(S′)‖ ≤ ‖r^c_{k−1}(S)‖ + (G_D + 1)c(S)/κ_− (Codex's (13) with C_{D,r} ↔ G_D) |
| §4 w = 10/81, A_L = 83/3 for the order-averaged map at d = 4, L = 3 | (exact enumeration, 24 orders) | **AGREE** (not re-run; matches r55t A4) | the only h-sensitive constant in my chain |
| §5 superposition | CONFIRMED | **AGREE** | cc55 B3 |
| §6 S10-11 as a proof of failure | REFUTED | **AGREE** | its identity (15) is the representation-dependence in one line |
| §6/§8 the full sup + Hölder statement | NOT-VERIFIED | **AGREE as a verdict on X1; now supplied** | §4: BL-4 + BL-C for the datum, COF (d) on S′ |
| §8 bankable sup theorem (16)-(17) | CONFIRMED | **AGREE** | = Theorem CC-FUN (a) |
| §8 S10-6 level count survives | (stated) | **AGREE** | §6.4 (I1), (I3) |
| §8 weights, backgrounds, nonlinear problem not covered | (stated) | **AGREE** | §6.2 (R2), (R3) |

**Does it change anything here? No conclusion changes.** It independently produces Lemma FLUX and Lemma DEC, which
strengthens §2-§3. It does not review the Hölder half (§4), Lemma TOP-cc (§5), Lemma H-FREE or Theorem CC-INV (§6):
**those four are new in this file and have had no cross-family check.**

---

## 10. Line corrections to this file (verified by grep after writing; content unchanged)

- §2.1 "d*Q^T = ev^Td*, BFT_A l.607" → l.608-609. §2.3 "‖Q_str^T‖_{∞→∞} = L^{−3}, l.609-610" → l.610.
- §2.5 "Lemma FG (iii), BFT_A l.2554-2556" → statement l.2249-2250, proof l.2553-2554.
- §4.1 COF step (c)'s bound "l.4096-4097" → l.4095 (A defined at l.4092); "Lemma W0-use step 4, l.4021-4024" → l.4023.
- §4.2 "C_BLC ~ 1/(α ln 2)" → C_BLC ~ 8/(α ln 2) as α ↓ 0.
- §6.4 "BL-6 (b) (BFT_A l.535-540" → l.538-541; "no level-max norm can carry …" → "no UNWEIGHTED level-max norm
  (max_lπ_l(j_l)) can carry a k-uniform top-residual bound on (cc)" (the θ-weighted ‖·‖_Pc can, at the price L^{θ(k−1)}).

---

## 11. Update after the coordinator's second message (banked sup half; CODEX_REVIEW_C2; Lemma TR) — appended 23:42Z

Read on disk now: CODEX_REVIEW_C2.md (36236 B, mtime 23:21Z; complete, ends with "Exactly what may be banked");
CODEX_REVIEW_X1.md §8 (as in §9); KFACTOR_O55.md §4 (Lemma TR, l.117-220); CODEX_REVIEW_TR.md (2518 B, 23:40Z: PRE-STATED
only, "Review in progress" — so Lemma TR has NO Codex verdict yet).

**11.1 The banked sup half [S26-BANKED] and Theorem CC-FUN (a).** Codex X1 (16)-(17) and C2's first (C2-COF) line are
CC-FUN (a). N_src (Codex X1 (9)) = my N(S): source-class norms, top residual excluded. The coordinator's quoted (16)
"C_0(N_src + γ_kA_Lc_j) + (C_D/κ_{k−1})(c_j + ‖s_{k−1}‖_∞)" is my proof of (a) term by term (γ_kA_L ↔ L^θ(1 + 2dL³w);
C_D/κ ↔ G_D/κ_− with BL-4, or LP's row-sum constant). On disk, Codex X1's display (18) is truncated (§9).

**11.2 The Hölder half — what the Codex files actually say (correcting the coordinator's summary, per the brief's rule
to read the files, not summaries).** The message says "Hölder half: NOT-VERIFIED by either Codex review". That is true
of CODEX_REVIEW_X1 (§6, §8). It is **not** what CODEX_REVIEW_C2.md says: its verdict table (l.34) reads "Whole-class
CO-fun reversal | **CONFIRMED** | … retain the top-response term in the Hölder estimate", its §4 (l.180-192) proves
  ‖f_0(S)‖_∞ + [f_0(S)]^∞_α ≤ C[N + κ_+‖r^c_{k−1}(x(S))‖_∞]   (C2-COF, second line)
by COF (d) on the strict plain-only remainder plus LIN0/GU + BL-C on the dipole pieces, and calls it "the original
§31.2 CO-fun estimate on the **whole** composite-co-closed class". What C2 does **not** confirm is a **source-only**
Hölder bound ("nor does it give a source-only bound for the full invariant norm", l.192; "The Hölder conclusion still
carries the full response's top residual unless independently bounded", l.290). So:
- **Theorem CC-FUN (b) = (C2-COF)'s second line, reached by an independent route** (Lemma DEC + Lemma TS + BL-4 + BL-C
  for the datum, COF (d) on S′; C2 uses the dipole identity + LIN0/GU + BL-C). Two derivations, one Codex confirmation:
  **this form may be banked as CONDITIONAL on COF's inputs** — it is what "keep the top-response term" refers to.
- **Theorem CC-FUN (c) and Lemma TOP-cc are exactly the "unless independently bounded" step.** They are new here and
  have NO Codex check. **Do not bank the source-only Hölder form until TOP-cc is reviewed.** I agree with the banking
  instruction as a statement about what is reviewed; I do not read it as a claim that the top residual is unbounded
  (neither file asserts that, and BL-6 (b)'s family in §6.4 shows the Σ-form of TOP-cc is sharp, not false).

**11.3 The terminal-slot and ĵ_0 corrections (C2 item 1: "preserve … when reusing the proof").** Terminal slot: Lemma
DEC removes it (S′ has s′_{k−1} = 0), so no step uses SPLIT's pointwise claim for the top slot. ĵ_0: wherever COF's
regrouping is used on S′ — COF (c), (d) and TOP-cc's first term C(j′) = Σ_l(Q_str^{(0→l)})^Tĵ′_l — read **ĵ′_0 :=
j′_0 + h_0^Tψ′_0** (the definition the regrouping needs; BFT_B l.3590's "ĵ_0 := j_0" is the collision of Codex COFUN F14,
REVIEW55_TENT CF13, REVIEW55_BFTB Finding 4, Codex C2 §4). The bound π_0(C(j′)), max_lπ_l(ĵ′_l) ≤ (121/13)|j′|_Σ used in
§5 already contains the l = 0 funnel term (FT (ii) at l = 0: π_0(h_0^Tψ_0) ≤ 2dπ_0(j′_0)). No statement changes.

**11.4 C2 item 4 ((CC-0) at every critical point REFUTED).** Consistent with everything here: §2-§6 use only (cc).
At critical points the rows are composite-co-closed (Lemma CD on root-pinned directions, as C2 banks it), which is
exactly the class Theorems CC-FUN / CC-INV cover. COF-crit's (CC-0) step is not needed and not used.

**11.5 Lemma TR (KFACTOR_O55 §4; CONDITIONAL — CODEX_REVIEW_TR.md has no verdict yet) and what it does to §6.4.**
(TR-4): at a critical point x* of 𝔉_k∘exp with ‖x*‖_𝔐 ≤ η ≤ η_0, Σ_{1≤l≤k−1}π_l(V_l) ≤ K_Ση², K_Σ independent of k, T
and Γ. That is precisely the interface condition of §6.4: it makes (I1) and (I3) k-uniform at once (|V|_Σ = O(η²)).
Check of the remaining slots of N_Σ for the critical-point rows S*: level-0 Wilson G-row, ‖q^c‖_∞ ≤ 9η² and
[q^c]^∞_α ≤ 8C_qη² (Corollary WR (a), BFT_A l.2234-2236); level-0 plain rows ≤ A_Wη² (KFACTOR_O55's A_W); completions
W_l (l ≥ 1): ω_l‖W^c_l‖_∞ ≤ CL^{−(1−θ)(k−l)}η² (Corollary NC) — **only their sup enters**, because Theorem GU, COF (a),
TOP-cc (1) and §31.2 (a) use no Hölder norm of G_l for l ≥ 1 (so in §4-§6 ‖G‖_Y may be replaced by
max_{l≥1}ω_l‖G^c_l‖_∞ plus the level-0 Hölder pair; this sidesteps the W_l-Campanato question KFACTOR_O55 marks ARGUED);
residual-type rows: ‖s‖_R ≲ κ_+C_6L^{θ−1}η² from own ≤ κC_6L^{−3(k−l)}η² (BFT_A l.155-157). Hence N_Σ(S*) ≤ C_*η²,
k-uniformly, and:

> **Corollary CC-CRIT (CONDITIONAL on Lemma TR and on Lemma TOP-cc; both unreviewed by Codex).** At every critical point
> of 𝔉_k∘exp with ‖x*‖_𝔐 ≤ η ≤ η_0, at the trivial background and m = 0, 0 < α < θ < 1, the linear response x to the
> rows S* obeys **‖x‖_inv ≤ C_inv C_*η²** — sup and Hölder halves of the whole curvature tower AND the top residual —
> uniformly in k, T and Γ. Without TOP-cc: the same with κ_+‖r^c_{k−1}(x)‖_∞ kept on the right of the Hölder half
> (CONDITIONAL on Lemma TR only, via (C2-COF) or CC-FUN (b)).
>
> *Proof.* Theorem CC-INV in its N_Σ form (§6.1; its j-dependence is only through |j|_Σ, §4.2 last line, §5 last
> paragraph) with N_Σ(S*) ≤ C_*η² from (TR-4) and the slot list above. ∎

What this changes in §6: (i) **the level count no longer stands between (NC-Γ)_cc and k-uniformity at critical
points**, for either half or the top residual — given Lemma TR; (ii) it closes, conditionally, the two items left open
for the rows: REVIEW55_BFTB Finding 1's "Missing: a bound on the top residual of the response to V" (Corollary RHT-V's
absolute η² form) and KFACTOR_O55's own "What is NOT discharged: the top-residual input of Corollary RHT-V" (l.188-191) —
both are TOP-cc + (TR-4); (iii) off the critical set nothing changes (the available bound is O(kη²); KFACTOR_O55 §5 is
ARGUED and not used here). BFT-5 clause (b) itself is unchanged: it is a linear estimate, k-uniform in N_Σ already
(§6.2); Lemma TR is about the size of the rows fed to it.

*Line/number corrections to §11 (verified after writing; conclusions unchanged):* KFACTOR_O55's "What is NOT
discharged" is at l.194, not l.188-191. The residual-type rows' class norm is sharper than written:
‖s‖_R ≲ κ_+(C_6L^{θ−3} + L^θ)η² (BA-6's κρ^{(2)}_l, own ≤ κC_6L^{−3(k−l)}η², BFT_A l.156-157, maximal at k − l = 1; CR-1's
s^C_l, own ≤ κ_lL^{−3(k−1−l)}η²) — k-uniform either way.

---

## 12. Summary table (every claim in my batch), counts, and what changes for the lead

### 12.1 Claims reviewed (verdicts CONFIRMED / NOT-VERIFIED / REFUTED)

| # | claim (file, locating string) | verdict | where |
|---|---|---|---|
| 1 | X1 displayed bound, N = source-class norms ("‖f_0(S)‖_inf <= C_fun·N(S')", REVIEW55_TENT l.614-616) | CONFIRMED (with the top residual inside N it needs +(G_D+1)c(S)/κ_−; agree Codex X1 §4) | §2.7, §4.2 |
| 2 | X1 (1) cut bound | CONFIRMED | §2.1 |
| 3 | X1 (2) Gale-Hoffman feasibility | CONFIRMED (unnecessary: Lemma FLUX) | §2.2 |
| 4 | X1 (3) S − Q^Tb is (CC-0), after X-T7's reclassification | CONFIRMED | §2.3, §3 |
| 5 | X1 (3) π_{k−1}(Q^Tb) ≤ (1 + 2dL³w)‖b‖ (w = 10/81 → 83/3) | CONFIRMED | §2.3 |
| 6 | X1 (4) "the subtracted current IS data" | CONFIRMED (= Lemma TS; same Q required, cc55 C2) | §2.4 |
| 7 | X1 (4) LP 4.2 (ii) ⇒ ‖f_0‖ ≤ C_D‖b‖/κ_{k−1} | CONFIRMED (C_D = row-sum constant; agree Codex X1 (6)) | §2.4 |
| 8 | X1 (5) linearity | CONFIRMED | §2.5 |
| 9 | X1 consequence (a): sup half holds, "FALSE" refuted | CONFIRMED | §2.7 |
| 10 | X1 (b): COF-res premise fails when the residue is large | CONFIRMED (logic) | §2.7 |
| 11 | X1 (c): TENT-Q … ROOT-sup not obstructions to the curvature half | CONFIRMED at m = 0, Z = 1 only | §2.7 |
| 12 | X1 (d): level count reappears | CONFIRMED (located: (I1), (I3); removed at critical points by Lemma TR, CONDITIONAL) | §6.4, §11.5 |
| 13 | X1 (e): root-level questions harmless | CONFIRMED | §2.7 |
| 14 | X1: "Hölder half … not checked" | CONFIRMED (of X1); closed in §4 | §4 |
| 15 | X-T7: Lemma SPLIT "D(S^s) = 0" false for a non-co-closed top slot | CONFIRMED (cc55 A7) | §7.1 |
| 16 | X-T7: repair by reclassifying Q^Ts_{k−1} | CONFIRMED | §7.1 |
| 17 | X-T6: two operators called h_l | CONFIRMED (no step here depends on it; data map h-free) | §7.2 |
| 18 | BFT_B §35.7 / S10-11 "(CO-fun) as stated in §31.2 is FALSE" | **REFUTED** (both halves; conditional on COF + TS + BL-4 + BL-C) | §4 |
| 19 | [S10-fix 1]: (CO-fun) must be restricted to (CC-0) | **REFUTED** (unnecessary) | §4 |
| 20 | COFUN §2.1/§7/§9: "(CO-fun)[cc] FALSE / refuted as stated" | **REFUTED** | §4 |
| 21 | Window 0 < α < θ_c (< 1) for (CO-fun) (COFUN §2.2; COF l.4076) | CONFIRMED; the root-charge route adds only θ > 0 | §4.2 |
| 22 | Finding 5: flux b with sup ≤ ‖j^c_0‖ + ‖j‖_Pc/(L^θ − 1) | CONFIRMED | §8 |
| 23 | Finding 5: (CO-fun) as stated holds on the whole class, Hölder half included | CONFIRMED (its Hölder step was one line; supplied in §4; Codex C2 agrees) | §4, §8 |
| 24 | Findings 3/5: the sup half needs no top-residual term | CONFIRMED | §4.1 |
| 25 | Finding 5: dipole identity P(b) ≡ (s_{k−1} = b) + (G_{k−1} = Σ b G_b) | NOT-VERIFIED by me (not re-derived, not used; Codex C2 CONFIRMED it with 24 orders) | §8 |
| 26 | Finding 7: l.3810 is a Λ_0 statement, l.4202 the pointwise one | CONFIRMED (by reading BFT_A l.2951) | §8 |
| 27 | Finding 1: RHT-V's absolute form lacks a top-residual bound | CONFIRMED as of the reviewed text; supplied here CONDITIONALLY (TOP-cc + Lemma TR) | §5, §11.5 |
| 28 | Theorem COF's statement holds for (CC-0) sources with a top slot | CONFIRMED (after the repair) | §7.1 |
| 29 | COF step (d) applies to S′ (J_0[S′^j] = C(j′) − (Q_str^{(0→k)})^Tρ_{k−1}; sup bound) | CONFIRMED (identity re-derived; LES-div/LE/BL-C quoted) | §4.1 |
| 30 | BFT_B l.4203: "Theorem COF applies to S^E_0(S) **except** for COF-res's residue" | **REFUTED** as an exception clause: CC-FUN applies to the (cc) source S^E_0(S) entirely; what remains off the critical set is π_0(Γ_E^TD(S)) | §8 |

**Counts (reviewed claims): CONFIRMED 25 · NOT-VERIFIED 1 · REFUTED 4.**

### 12.2 Results of this file (status words; none has a Codex verdict unless stated)

| result | status | cross-check |
|---|---|---|
| Lemma FLUX (explicit one-face-local root-charge current) | PROVEN-HERE (elementary; cc55 A2, A4) | found independently by Codex X1 §2 and Codex C2 §3 (CONFIRMED there) |
| Lemma SF (q(S) = κ_{k−1}d*r_{k−1}(x(S)); D(Hx) identity) | PROVEN-HERE (cc55 A9, B2) | = RT-cc (a) at the top |
| Lemma DEC (S = (CC-0) source without top slot + datum b/κ_{k−1}) | PROVEN-HERE (cc55 A5, A6, A8, B3) | = Codex X1 §4's representation (CONFIRMED there) |
| Lemma H-FREE (data map independent of h_l) | PROVEN-HERE (cc55 B4; C6 fires) | none |
| Theorem CC-FUN (a), sup, source-only | PROVEN as an implication | **= banked [S26-BANKED]** (Codex X1 (16)-(17), C2) |
| Theorem CC-FUN (b), sup + Hölder with κ_+‖r^c_{k−1}‖ | PROVEN as an implication | **= (C2-COF), CONFIRMED by Codex C2** by another route |
| Lemma TOP-cc (top residual ≤ C·N(S) on (cc)) | PROVEN-HERE as an implication | **none — review needed** |
| Theorem CC-FUN (c), sup + Hölder, source-only | PROVEN as an implication (needs TOP-cc) | **none — do not bank yet** |
| Theorem CC-INV ((NC-Γ)_cc both halves, Z = 1, m = 0, class norms) | PROVEN as an implication (TOP-cc; §31.2 (a)-(b) quoted, summability re-checked) | none |
| Corollary CC-CRIT (critical-point rows: ‖x‖_inv ≤ Cη², k-uniform) | CONDITIONAL on Lemma TR and TOP-cc | none (CODEX_REVIEW_TR in progress) |
| (CC-dec_Z) — the (cc) mechanism at the background Z(V_k) | named, OPEN | — |

### 12.3 What should change in PROOF.md's tally / HANDOFF's critical path (no file edited by me)
1. **(CO-fun) on (cc), Hölder half:** bank CC-FUN (b) = (C2-COF) in the form WITH κ_+‖r^c_{k−1}‖_∞ (Codex C2 CONFIRMED;
   independent second derivation here). Do not record the Hölder half as NOT-VERIFIED: that is true only of Codex X1.
   The source-only form (CC-FUN (c)) waits for a Codex review of Lemma TOP-cc (§5).
2. **Remove "(CO-fun)[cc] FALSE"** from every status line (BFT_B §35.7, S10-11, COFUN §2.1/§7/§9) and withdraw
   [S10-fix 1]; BFT_B l.4203's "except for COF-res's residue" is superseded.
3. **(NC-Γ)_cc at Z = 1, m = 0:** curvature half no longer "CONDITIONAL on (CO-fun)" (BFT_B l.3851): PROVEN as an
   implication relative to the top residual (now), absolute in the class norms once TOP-cc is confirmed (CC-INV).
4. **BFT-5_E clause (b): stays OPEN**, with exactly (R1) (G♯_0-field), (R2) the background transfer [(R♯_ω), (G♯-patch^Ω),
   G-pert's scope, and the newly named (CC-dec_Z)], (R3) weighted COF (YH_m). Its (NC-Γ)_cc input is discharged at
   Z = 1, m = 0.
5. **Level count:** X1/FLUX add no new k-dependence; the only k is in the rows' |V|_Σ (I1)/(I3). With Lemma TR (pending
   CODEX_REVIEW_TR) it is removed at critical points for the WHOLE gauge-invariant curvature half and the top residual
   (Corollary CC-CRIT, also needing TOP-cc); off the critical set unchanged.
6. **Critical path in this neighbourhood:** (TENT-Q), (TENT-osc), face (b), G_e sign, FB-NBHD, (YH-pin), (ROOT-sup) are not
   on it (agree REVIEW55_TENT §10 item 2). Next reviews, in order of leverage: Lemma TOP-cc; Lemma TR (already queued);
   Lemma H-FREE; CC-INV's §6.1 summability.
7. **X-T6 erratum** (BFT_B §27.1 l.3589, §29.2): descriptive only for COF; exact source-response numbers (65/26244,
   243/260, Φ_k witnesses) remain operator-specific.

UTC at end of writing: see the stat of this file. Files written: this file; checks/cc55_criteria.md, cc55_checks.py,
cc55_out.txt, cc55_err.txt; one empty scratch directory. No git command was run; no other lane file was edited.

*Final line correction (verified):* X1's displayed bound is REVIEW55_TENT l.614 (12.1 row 1 says l.614-616; the display
is one line). §2.7's pointer "§4.2" for "COF's sup half carries no top-residual term" should read §4.1. Content unchanged.
