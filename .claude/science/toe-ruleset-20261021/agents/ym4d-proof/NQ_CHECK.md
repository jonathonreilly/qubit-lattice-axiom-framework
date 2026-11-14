# NQ_CHECK.md — the (N-Q) decision: is ‖Q^j‖_{∞→∞} ≤ 𝔮_0 L^j with 𝔮_0 bounded in j?

Owner: the (N-Q) worker, session 24. This file is append-only. It may be read by anyone; nobody else writes it.
Scope: ONE question — the named input (N-Q) of NORMS.md §N4, on which Theorem N1-15 (and with it the C_♭ clause of
(H-C) at the trivial background) is CONDITIONAL. Requests for other files are collected in the final section
"FOR OTHER FILES (not edited)". I do not edit NORMS.md, PROOF.md, LINEAR_PACKAGE.md, SQ.md or any other lane file.

---

## §Q0 PRE-STATED (first edit of this file, 2026-10-28 13:06:09 UTC; statements only; cites nothing produced in this session)

This section was written before any derivation, any script and any computation in this session. Nothing below §Q0
existed when §Q0 was written.

**The question.** (N-Q), verbatim from NORMS.md §N4: *‖Q^{j}‖_{∞→∞} ≤ 𝔮_0 L^{j} for a constant 𝔮_0 = 𝔮_0(L, d),
uniformly in j.* Here Q is Setting SC's averaging operator (level-j 1-forms → level-(j+1) 1-forms) and
‖·‖_{∞→∞} = max_c Σ_b |·(c, b)| (the row ℓ¹ sum / N_0 norm).

**Targets.**
- **TQ1 (definition).** Settle what Setting SC's Q is, from the files, and resolve the recorded conflict between
  LINEAR_PACKAGE's Lemma J-str ("Q^T = Q_str^T − h^T d^*", i.e. Q ≠ Q_str) and SQ's Lemma SHIFT ("Q^m is the straight
  average over L^m-blocks"). Quote both with file:line. If the conflict cannot be resolved from the files, say so and
  carry BOTH readings through TQ2. Do not average the two readings, and do not guess.
- **TQ2 (exact computation).** At L = 3, d = 4 compute **max_c Σ_b |Q^j(c, b)| for j = 1, 2, 3**, exactly, in
  `fractions.Fraction` / integer arithmetic, plain python, one process, no numpy and no BLAS (so no numeric lock is
  needed; brief rule 6). Compare against L^j = 3, 9, 27 and against p_L^j = 11, 121, 1331.
- **TQ3 (which of the three cases).** Report which case of NORMS.md's [N1-corr 1] holds: 𝔮_0 bounded (Theorem N1-15 as
  stated), 𝔮_0 polynomial in j (C_♭^{(k)} ≲ k², not uniform), or only the crude 𝔮_0 ≤ (p_L/L)^j (depth-dependent).
- **TQ4 (all j, if available).** A computation at j = 1, 2, 3 is evidence about boundedness in j, never a proof of it.
  If a proof for all j is available it is to be written out in full and labelled PROVEN; if not, the result stays
  COMPUTED (exact) and the status of Theorem N1-15 stays CONDITIONAL.
- **TQ5 (consequence).** State the consequence for Theorem N1-15 in NORMS.md's own terms, including what is NOT
  established (Theorem N1-15's other named inputs (N-loc) and (N-bg) are out of scope here and are not touched).

**Pre-registered verdict table for TQ2/TQ3.** Put **R_j := (max_c Σ_b |Q^j(c, b)|) / L^j** (an exact rational). The
constants used in these thresholds are NOT derived in this session: L = 3, d = 4, p_L = 11 and the ratio
p_L/L = 11/3 are quoted from PROOF.md (p_L = the S4′ contour length bound) and from NORMS.md §N4 / [N1-corr 1],
which records (p_L/L)² = (11/3)² ≈ 13.4 as the crude per-level cost. The a priori upper bound is
R_j ≤ (p_L/L)^j = 11/3, 121/9, 1331/27 ≈ 3.67, 13.4, 49.3.

| reading of the data | pre-registered criterion (j = 1, 2, 3) | verdict |
|---|---|---|
| **BOUNDED** | R_j ≤ p_L/L = 11/3 for every j ∈ {1, 2, 3}, **and** the increments are non-increasing: R_3 − R_2 ≤ R_2 − R_1 | 𝔮_0 bounded at the computed j, with 𝔮_0 ≥ max_j R_j; COMPUTED evidence for (N-Q), upgraded to PROVEN only if TQ4 delivers an all-j proof |
| **POLYNOMIAL** | some R_j > 11/3, **and** the increments are roughly constant: (R_3 − R_2)/(R_2 − R_1) ∈ [1/2, 2] | 𝔮_0 polynomial in j: Theorem N1-15 weakens to C_♭^{(k)} ≲ k² ([N1-corr 1], case 2) |
| **CRUDE** | R_3 ≥ (1/2)·(p_L/L)³ = 1331/54 ≈ 24.6 (geometric growth at rate ≈ p_L/L) | only the crude bound: 13.4 per level, depth-dependent ([N1-corr 1], case 3) |
| **OTHER** | none of the three patterns matches | no verdict; report the numbers and say the three-case reading does not resolve at j ≤ 3 |

**Pre-registered correctness gates (all must PASS; a FAIL voids the verdict and is reported as a FAIL, with the
failing script and output kept unaltered as the record, and the re-run done under a new id with these criteria
untouched).**
- **(G1) slice identity.** The constructed one-level Q row satisfies Q = Q_str − d∘h entrywise, against independently
  constructed rows of Q_str and h (LINEAR_PACKAGE §1.2 / PROOF.md L3g(a)-slice; checked there numerically as c8(f)).
- **(G2) constant reproduction.** For the constant 1-form with A_ν ≡ δ_{νν_0}: Q^j A = L^j δ_{ν_0 μ} on a level-j link
  of direction μ, for j = 1, 2, 3 and every (ν_0, μ) — i.e. Q(const) = L·const, h(const) = 0 by centring (PROOF.md
  Lemma LED-dual's proof).
- **(G3) pure-gauge covariance.** Q^j(d_0 λ) = (d_j ev^j λ) for a non-trivial λ: the composite row applied to an exact
  level-0 1-form returns λ(root of the far end) − λ(root of the near end) (root covariance Q∘d = d∘ev, PROOF.md
  J-str's proof).
- **(G4) straight-average control.** The same code path with Q := Q_str returns exactly L^j for j = 1, 2, 3 (the
  statement NORMS.md §N4 records as immediate), and all its entries are non-negative.

**Admissible outcomes, pre-registered.**
- (QO1) BOUNDED with an all-j proof: (N-Q) PROVEN; Theorem N1-15 stands uniformly in k, CONDITIONAL on (N-loc) alone.
- (QO2) BOUNDED without an all-j proof: (N-Q) ARGUED + COMPUTED at j ≤ 3; Theorem N1-15 stays CONDITIONAL on (N-Q)
  and (N-loc), with the conditional input now supported by exact values.
- (QO3) POLYNOMIAL: Theorem N1-15 does not hold as stated; the honest form is C_♭^{(k)} ≲ k² and (H-C) is NOT
  discharged. To be reported as a weakening, not dressed as progress.
- (QO4) CRUDE: the composite gain survives (≈ 95× per level better than 1267) but is depth-dependent; (H-C)'s C_♭
  clause is not discharged.
- (QO5) The files do not determine Q: both readings reported separately, with the verdict for each.

**Not success.** A verdict from j = 1 alone; a verdict from a script that fails a gate; calling a COMPUTED value a
PROOF; silently replacing Setting SC's Q by Q_str because that is the convenient reading; any claim about (N-loc),
(N-bg), or any clause of (H-C) other than C_♭'s k-uniformity at the trivial background.

---

## §Q1 What Setting SC's Q is, and the resolution of the J-str / SHIFT conflict (TQ1): SETTLED FROM THE FILES

**Answer: Setting SC's Q is Q_root, the full S4′ order-averaged root map. It is NOT the straight average.** Two files
say so in the definition itself, and a third names it when it imports the package:

- **PROOF.md l.2060** (Setting SC, the definition): "*Q is the linearised S4' map from level i to level i + 1
  (**Q_root** of L3g(a)-slice, with the S4' order average).*"
- **RTARGET.md l.414** (the setting of the section that supplies Setting SC's norms): "*Setting SC of PROOF L5 [S10]
  (d = 4, L ≥ 3 odd, levels 0..k, κ_- ≤ κ_i ≤ κ_+, **Q = Q_root of S4'**, …)*"
- **SQ.md l.15** (its own reading list): "*LINEAR_PACKAGE.md §1-§3 (S4', **Q_root = Q_str - d∘h**, Setting SC, …)*"

The three objects, verbatim from **LINEAR_PACKAGE.md l.70-73**:
- "*the averaged link is **Q_rootA(X, μ) := avg_{σ,y}∫_{T^σ_y}A** (the "root map")*";
- "*The **straight average** is (Q_strA)(X, μ) := L^{-4}Σ_{y∈B(X)}Σ_{j<L}A_μ(y + je_μ)*";
- "*With the **slice functional** h(A)(X) := avg_σavg_{y∈B(X)}∫_{P^σ(c_X→y)}A, the exact identity
  **Q_root = Q_str - d∘h** holds (l.982-990; check c8(f), error ≤ 2e-16). Root covariance: **Q∘d = d∘ev**, ev the
  restriction to roots.*"

**The two statements NORMS.md §N4 records as conflicting do not conflict. They are about different operators, and
each is correct where it stands.**

- **J-str is a statement about Setting SC's Q = Q_root.** LINEAR_PACKAGE.md l.166-171 (Lemma 3.1) and PROOF.md
  l.2093-2094: "*L3g(a)-slice: **Q = Q_str - d∘h exactly**, so Q^T = Q_str^T - h^Td^*. On co-closed r the funnel term
  h^Td^*r vanishes*". So in Setting SC, Q ≠ Q_str as an operator; what is true is that **Q^T = Q_str^T on CO-CLOSED
  forms**, which is all J-str (b) needs.
- **SHIFT's "Q^m is the straight average" is SQ's own declared convention, not a claim about Q_root.** SQ.md l.655
  (§11.0 Setting, the section that contains Lemma SHIFT): "***Q := Q_str*** *(§0.4; the argument there is unchanged by
  the sources below, since B ↦ B + dλ leaves them untouched)*". SQ justifies that substitution with a proof of its
  own: **SQ.md §0.4 l.352-357**, "*Q_str may replace Q_root in linear computations: PROVEN-HERE*" — put λ_0 := 0,
  λ_{i+1} := avg(λ_i) + h(B_i), B'_i := B_i + dλ_i; then "*Q_root = Q_str - d∘h and Q_str∘d = d∘avg give
  Q_strB'_i - B'_{i+1} = Q_rootB_i - B_{i+1}, so residuals and curvatures are equal and B'_0 = B_0*". The SHIFT
  parenthesis at **SQ.md l.710-711** ("*Q^m is the straight average over L^m-blocks, d(Q^ms)(p) =
  L^{-4m}Σ_y∮_{∂sq_y}s*") is therefore a true statement about SQ's Q, and the quantity it bounds, **d(Q^m s)**, is
  insensitive to the distinction in any case: Q_root^{(m)} − Q_str^{(L^m)} is exact (PROOF.md l.2545: "*a composite of
  root maps equals Q_str^{(L^m)} plus a coarse exact form*"), so **d∘Q_root^{(m)} = d∘Q_str^{(L^m)} exactly** and
  d∘d = 0 removes the difference. SQ states this too, at l.411: "*B_{j+1} = QB_j - r_j (Q = Q_root) … (dQ = dQ_str)*".

**So one object is in play and there is no ambiguity to carry forward: (N-Q) is a question about Q_root.** §Q2 and §Q3
answer it for Q_root. Q_str is carried only as the control (gate G4), where it returns exactly L^j, as NORMS.md §N4
says it must.

**One consequence worth stating at once, because it is the reason (N-Q) is a real question and not already answered
by SQ §0.4.** SQ's substitution is a **gauge shift**: it replaces B_i by B_i + dλ_i with λ_{i+1} = avg λ_i + h(B_i).
It therefore leaves the residuals and curvatures alone (which is all SQ measures) but moves the **potentials** — and
Lemma N1-11 of NORMS.md is a bound on |ζ^c_{sm,j}Y|_∞, i.e. on a potential in a stated gauge. The accumulated λ_i is
exactly the funnel gauge function; **𝔮_0 > 1 is a measure of it, and it is what §Q3 bounds.**

---

## §Q2 The exact computation (TQ2): COMPUTED (exact)

**Record of check nq1.** Criteria written first: `checks/nq1_criteria.md`, 13:08 UTC, before the script existed.
Script: `checks/nq1_qnorm.py` (exact integer arithmetic over the common denominator (d!·L^d)^j = 1944^j, reported as
`Fraction`s; plain python, one process, `python3 -I`, no numpy, no BLAS, **no numeric lock taken**, permitted by the
brief's rule 6 for exact rational arithmetic; `nice -n 10`, load average 2.0 at launch). Output: `checks/nq1_out.txt`
(full run) and `checks/nq1_stage2_out.txt` (a staged run with j ≤ 2, to size the problem; same code, same criteria,
`jmax` argument only). Resources: `checks/nq1_time.txt` — **25.7 s wall, 856 MB peak RSS**, single thread.

Q^j is built one level at a time by translating the precomputed one-level row pattern (459 fine links per row at
L = 3, d = 4), so nothing of size L^{dj} is formed; the level-0 support of the j = 3 row is 4 113 747 links.
The computation is on Z⁴ (no wrapping), which **dominates every torus**: periodisation merges columns, and
|v_b + v_{b′}| ≤ |v_b| + |v_{b′}|, so a torus row ℓ¹ sum is ≤ the Z⁴ one. max_c is the value at one c because Q^j is
covariant under level-j translations, and all four link directions were computed and agree (gate G5).

| j | 𝔫_j := max_c Σ_b \|Q^j(c, b)\| (exact) | decimal | L^j | p_L^j | R_j = 𝔫_j/L^j | decimal |
|---|---|---|---|---|---|---|
| 1 | **205/27** | 7.592593 | 3 | 11 | **205/81** | 2.530864 |
| 2 | **2021/81** | 24.950617 | 9 | 121 | **2021/729** | 2.772291 |
| 3 | **6115/81** | 75.493827 | 27 | 1331 | **6115/2187** | 2.796068 |

Increments: R_2 − R_1 = 176/729 = 0.241427, R_3 − R_2 = 52/2187 = 0.023777 (a factor ≈ 10.2 smaller).

**Gates (all pre-registered, all PASS).**
- **G1 PASS.** The one-level row built from the S4′ contours equals (Q_str row) − (d∘h row) **entrywise and exactly**,
  for all four directions: 0 residual entries. This re-verifies L3g(a)-slice's identity on our own construction, as
  exact rationals rather than at 2e-16 (check c8(f)).
- **G2 PASS.** Q^j(const) = L^j·const exactly, for j = 1, 2, 3 and all 16 direction pairs (so h(const) = 0 by
  centring holds through the composite).
- **G3 PASS.** Q^j(d_0λ) = λ(far root) − λ(near root) exactly for a non-linear test λ, j = 1, 2, 3 — root covariance
  survives the composition.
- **G4 PASS.** The same code path with Q := Q_str returns exactly L^j = 3, 9, 27 with every entry ≥ 0.
- **G5 PASS.** 𝔫_j is the same for all four directions μ at every j.

**Pre-registered verdict: nq1-1 BOUNDED FIRES** (R_j ≤ p_L/L = 11/3 for j = 1, 2, 3, and R_3 − R_2 ≤ R_2 − R_1);
nq1-2 POLYNOMIAL does not fire; nq1-3 CRUDE does not fire; nq1-4 OTHER does not fire. No gate failed, so no verdict
is void. **No check was run after seeing a result and then re-labelled; no post-hoc probe was added; the staged j ≤ 2
run used the identical script and criteria and is kept.**

**What this establishes and what it does not.** It establishes, exactly and with no measured input, that
‖Q^j‖_{∞→∞}/L^j is 2.53, 2.77, 2.80 at j = 1, 2, 3 — far from the crude p_L^j/L^j = 3.67, 13.4, 49.3, and bounded by
p_L/L at every computed j. It is **evidence about boundedness in j, not a proof of it**: three values cannot exclude
slow growth. The extrapolation "increments falling by ≈ 10 per level, so R_j → ≈ 2.799" is an extrapolation and is
not a result. The proof is §Q3, and it is what the verdict rests on.

---

## §Q3 Theorem NQ-1 — (N-Q) for all j: PROVEN-HERE

*Statement.* Let d ≥ 2, L ≥ 3 odd, and let Q = Q_root be Setting SC's averaging operator (the linearised S4′ root
map), on Z^d or on any level-j torus. Then for every j ≥ 1,

  **‖Q^j‖_{∞→∞} ≤ L^j + (d(L² − 1)/(2L))·(L^j − 1)/(L − 1) ≤ 𝔮_0·L^j,  𝔮_0 := 1 + d(L + 1)/(2L),**

with 𝔮_0 a function of (L, d) only — **uniformly in j**. At d = 4, L = 3: **𝔮_0 = 11/3 = 3.6667**.

*Inputs.* Only two, both PROVEN imports, and both re-verified here:
- **(i)** the one-level slice identity **Q = Q_str − d∘h** (L3g(a)-slice, PROOF.md l.1127-1131, LINEAR_PACKAGE l.72;
  verified entrywise as gate G1);
- **(ii)** root covariance **Q∘d_i = d_{i+1}∘ev_i**, ev_i λ(X) := λ(c_X) (PROOF.md l.2090; one line: for a 0-form λ,
  ∫_{T^σ_y}dλ = λ(c_Y) − λ(c_X) for every σ and y, because every S4′ contour runs from c_X to c_Y, so the average is
  λ(c_Y) − λ(c_X); verified through the composite as gate G3).

*Proof.* Write Q_i for the level-i step, S_i := Q_str, H_i := h, D_i := d_i, E_i := ev_i, and
Q^{(j)} := Q_{j-1}∘⋯∘Q_0.

**Step 1 (telescoping, exact).** By (i), Q_0 = S_0 − D_1H_0, so
Q^{(j)} = (Q_{j-1}⋯Q_1)S_0 − (Q_{j-1}⋯Q_1 D_1)H_0. By (ii) applied j − 1 times,
Q_{j-1}⋯Q_1 D_1 = D_j E_{j-1}⋯E_1. Substituting (i) for Q_1 inside the remaining product and inducting,

  **Q^{(j)} = S_{j-1}⋯S_0 − D_j·Σ_{i=0}^{j-1} (E_{j-1}⋯E_{i+1})·H_i·(S_{i-1}⋯S_0),**

with empty products read as the identity. This is an exact operator identity. (It is the quantitative form of
PROOF.md's Lemma IT-str consequence, l.2545, "a composite of root maps equals Q_str^{(L^m)} plus a coarse exact
form"; the same object written with the block mean M instead of ev, h^{(m+1)} = Mh^{(m)} + hQ^{(m)} (PROOF.md
l.2787, l.2980), agrees with it exactly, because h∘d = M − ev on 0-forms — PROOF.md l.1134's
"h(A + dλ) = h(A) + Q_0λ − λ(c)". **The ev form is the one to use: it is not self-referential, so it needs no bound
on "h applied to a pure gauge" — which is precisely the hole NORMS.md §N4 left open.**)

**Step 2 (the four norm inputs).** All norms are ‖·‖_{∞→∞} = max row ℓ¹ sum, which is submultiplicative.
- **‖S_{i-1}⋯S_0‖ = L^i exactly.** One straight average has non-negative entries and every row sum exactly
  L^{-d}·L^d·L = L (L^d choices of y, L links each, weight L^{-d}); a product of non-negative matrices with constant
  row sums has constant row sum equal to the product. (Gate G4 confirms the value and the sign at j = 1, 2, 3.)
- **‖E_{j-1}⋯E_{i+1}‖ = 1.** A composite of restrictions is a restriction: one entry 1 per row.
- **‖H_i‖ = ‖h‖ ≤ d(L² − 1)/(4L).** P^σ(c_X → y) is a monotone axial path with exactly |y − c_X|_1 links, each
  traversed once with coefficient ±1, so the row ℓ¹ mass is at most
  avg_{σ,y}|y − c_X|_1 = L^{-d}Σ_{y∈B(X)}|y − c_X|_1 = d·L^{-1}·2·Σ_{t=1}^{(L-1)/2}t = d(L² − 1)/(4L)
  (= 8/3 at d = 4, L = 3). (Equality in fact holds — all contributions to a given link have the same sign, since
  every axial step runs away from the block centre — but only "≤" is used.)
- **‖D_j∘G‖ ≤ 2‖G‖** for any G into level-j 0-forms: (D_jG)(X, μ; ·) = G(X + e_μ; ·) − G(X; ·).

**Step 3 (assembly).** By Steps 1–2 and the triangle inequality,
  ‖Q^{(j)}‖ ≤ L^j + 2·Σ_{i=0}^{j-1} 1·(d(L² − 1)/(4L))·L^i = L^j + (d(L² − 1)/(2L))·(L^j − 1)/(L − 1)
            ≤ L^j·[1 + d(L + 1)/(2L)] = 𝔮_0 L^j,
using (L² − 1)/(L − 1) = L + 1 and (L^j − 1) ≤ L^j. ∎

*Torus.* Every step is an identity or an inequality between row ℓ¹ sums of the same operators on the torus;
periodisation merges columns and can only decrease a row ℓ¹ sum, so the bound holds on every level-j torus with the
same 𝔮_0.

*Consistency with §Q2 (an independent cross-check of both).* The theorem's bound at L = 3, d = 4 is
L^j + (8/3)(L^j − 1) = 25/3, 91/3, 289/3 = 8.3333, 30.3333, 96.3333 at j = 1, 2, 3, against the exactly computed
205/27, 2021/81, 6115/81 = 7.5926, 24.9506, 75.4938. The bound dominates each computed value, by 10%, 22%, 28%; and
𝔮_0 = 11/3 = 3.6667 dominates max_j R_j = 2.7961. The analytic bound and the exact computation agree where they must
and the slack is where the triangle inequality was used (the funnel legs partly overlap the straight part with the
opposite sign).

*Scope, stated plainly.* **Abelian / linearised only** — which is exactly the scope of Setting SC, of (N-Q) and of
Lemma N1-11, but no further. Input (i) has no nonabelian analogue, and L3g(a)-slice says so in terms
(PROOF.md l.1123-1125, [R3-fix]: "*the identity is linearised and abelian only: the nonabelian straight average is not
even covariant, so there is no nonlinear SU(N) analogue*"). **Theorem NQ-1 therefore does nothing for (N-bg)**, where
a background version of Lemma N1-11 would need a background version of (i). Nothing here touches (N-loc).

---

## §Q4 Which of the three cases holds (TQ3), and the consequence for Theorem N1-15 (TQ5)

**Case 1 of NORMS.md [N1-corr 1] holds: 𝔮_0 is BOUNDED in j.** Not merely bounded at j ≤ 3 — PROVEN bounded for all
j, with the explicit value **𝔮_0 = 1 + d(L + 1)/(2L) = 11/3** at d = 4, L = 3, and with the exact values
‖Q^j‖/L^j = 2.53, 2.77, 2.80 at j = 1, 2, 3 showing the true constant is near 2.8, not 3.67.
The other two cases are excluded: the polynomial reading (𝔮_0 ≤ 1 + cj, which NORMS.md §N4's own pure-gauge
bookkeeping produced and which [N1-corr 1] priced at C_♭^{(k)} ≲ k²) is superseded — the j-dependence came from
organising the expansion so that h had to be applied to a pure gauge at every level, and Step 1's ev form removes it;
and the crude reading (p_L/L per level, 13.4 per level in the soft vertices) is off by the factor (11/3)^{j-1} it
claimed per level beyond the first.

**In NORMS.md's own terms:** (N-Q) was the named input of **Lemma N1-11** (composite potential bound, θ_A = 1) and,
through it, of **Theorem N1-15** and of the discharge of **(H-C)'s C_♭ clause** at the trivial background
(NORMS.md tally items 12, 13, 14, 15). With Theorem NQ-1:

- **(N-Q): PROVEN** (𝔮_0 = 1 + d(L+1)/(2L), uniformly in j). NORMS.md tally item 15 moves ARGUED → PROVEN, and its
  named hole ("h applied to a pure gauge") is not a hole but an artefact of one choice of expansion.
- **Lemma N1-11: CONDITIONAL on nothing further** — it was conditional on (N-Q) alone (tally item 12), so it becomes
  PROVEN-HERE within NORMS.md's own proof, with 𝔠_P = 2[c_AX R_eff C_f·𝔮_0 + 𝔮_0·4κ̂C_R L²/(L² − 1)] + 2 at
  **𝔮_0 = 11/3** (an explicit number where a named unknown stood).
- **Theorem N1-15: CONDITIONAL on (N-loc) ALONE** (was: on (N-Q) and (N-loc)). Its conclusion is unchanged —
  N3(D³E_k^br(1)) ≤ 𝔚 + 13.5·𝔖 uniformly in k, soft level-ratio A_soft = 1/L = 1/3 < 1 — and it now **stands
  uniformly in k** as stated, with no k- or depth-dependence entering through the transport.
- **(H-C)'s C_♭ clause** at the trivial background: CONDITIONAL on **(N-loc)** for the trivial-background statement and
  on **(N-bg)** for the Lipschitz-on-the-class statement that BR1 and δ_Sch actually consume (NORMS.md Remark N6-5).
  Those two were always separate from (N-Q) and are untouched here.

**What is NOT established.** (a) (N-loc) — the exponential locality of the gauge-variant representative; NORMS.md
rates it ARGUED and tradeable for a near/far split, and nothing here bears on it. (b) (N-bg) — the small-field class
statement; §Q3's scope paragraph says why Theorem NQ-1 does not transfer. (c) Any other clause of (H-C)
(𝔠_∞^{(i)}, A_in, A_out, c_K, 1/m_1, Z-tails). (d) The per-level no-go of NORMS.md §N5 is unaffected: Theorem NQ-1 is
about the composite transport and says nothing about A_per. (e) No value of ε_1, g_K² or any smallness condition
changes — NORMS.md §N9 already records that making C_♭ level-uniform does not move those numbers, and that remains
the case.

---

## §Q5 Tally for this file

**PROVEN-HERE**
1. **Theorem NQ-1**: ‖Q^j‖_{∞→∞} ≤ L^j + (d(L²−1)/(2L))(L^j−1)/(L−1) ≤ (1 + d(L+1)/(2L))L^j, uniformly in j, on Z^d
   and on every torus, for Setting SC's Q = Q_root (abelian/linearised). At d = 4, L = 3: 𝔮_0 = 11/3. **This is
   (N-Q).**
2. The exact telescoping identity Q^{(j)} = Q_str^{(j)} − d_j Σ_{i<j} ev^{(j-1-i)} h Q_str^{(i)}, and the observation
   that the ev form is non-self-referential (which is what closes NORMS.md §N4's named hole).

**COMPUTED (exact)**
3. max_c Σ_b |Q^j(c,b)| = 205/27, 2021/81, 6115/81 at j = 1, 2, 3 (L = 3, d = 4), i.e. R_j = 2.530864, 2.772291,
   2.796068 against L^j and against p_L^j. Check nq1, gates G1–G5 all PASS.

**SETTLED FROM THE FILES (a reading, not a theorem)**
4. Setting SC's Q is Q_root (PROOF.md l.2060, RTARGET.md l.414). The J-str / SHIFT "conflict" is not one: SHIFT's Q is
   Q_str by SQ's declared convention (SQ.md l.655, §0.4), and the quantity it bounds (d∘Q^m) does not see the
   difference (PROOF.md l.2545, SQ.md l.411).

**Counted here: nothing.** This file is not a ledger. No item above is to be added to PROOF.md's tally by this worker.

---

## FOR OTHER FILES (not edited)

Nothing below has been written into any other file.

**1. NORMS.md owner — (N-Q) is PROVEN; three statuses move, and one of your own remarks should be withdrawn.**
Theorem NQ-1 above proves (N-Q) with 𝔮_0 = 1 + d(L+1)/(2L) = 11/3 at d = 4, L = 3, uniformly in j, from your own two
imported identities (L3g(a)-slice and root covariance) and nothing else. Consequently, in your tally: item 15
((N-Q)) ARGUED → **PROVEN**; item 12 (Lemma N1-11) CONDITIONAL → **PROVEN-HERE** with 𝔮_0 = 11/3 substituted into 𝔠_P;
item 13 (**Theorem N1-15**) CONDITIONAL on (N-Q) + (N-loc) → **CONDITIONAL on (N-loc) alone**; item 14 (the C_♭ clause
of (H-C)) likewise. Two text items to withdraw or amend: (a) the §N4 bullet "*The files are ambiguous about what Q
actually is*" — they are not; see §Q1 (the ambiguity was SQ's local convention, declared at SQ.md l.655/§0.4). (b) the
§N4 estimate "*𝔮_0 ≤ 1 + 2d‖h‖·j/L — only POLYNOMIAL in j*" and the hole "*h applied to a pure gauge*": the
j-dependence is an artefact of expanding Q^j with the block mean M (self-referential, h^{(m+1)} = Mh^{(m)} + hQ^{(m)});
expanding with the root restriction ev instead gives a j-independent constant and never applies h to a pure gauge.
[N1-corr 1]'s **case 1** is the case that holds, so its cases 2 and 3 are now moot for this route.

**2. NORMS.md FOR-OTHER-FILES item 8 — the suggested measurement is DONE, with these numbers.** You asked for
"‖Q^j‖_{∞→∞} = max_c Σ_b |Q^j(c, b)| for j = 1, 2, 3 at L = 3, d = 4 for Setting SC's actual Q, compared with
L^j = 3, 9, 27 and p_L^j = 11, 121, 1331". Answer: **205/27 = 7.5926, 2021/81 = 24.9506, 6115/81 = 75.4938**, i.e.
2.53·L^j, 2.77·L^j, 2.80·L^j — and PROVEN ≤ (11/3)L^j for every j. Your own conditional reading of that item ("*If
the answer is ≈ L^j, Theorem N1-15 is PROVEN modulo (N-loc) and (H-C)'s C_♭ clause is closed at the trivial
background*") is met in the form that matters: 𝔮_0 is a bounded constant, which is what Theorem N1-15 consumes; it is
**not** 1, and the honest statement is 𝔮_0 = 11/3 proven / ≈ 2.8 computed. The second cheap piece you suggested (the
measured column masses of 𝒦_Z and 𝒦_ρ) is untouched here.

**3. LINEAR_PACKAGE.md / Setting SC owner — a one-line lemma worth adding next to Lemma 2.4 (IT-str).** IT-str already
records "a composite of root maps equals Q_str^{(L^m)} plus a coarse exact form". The quantitative form is cheap and
is now needed by a consumer: **‖Q_root^{(j)}‖_{∞→∞} ≤ L^j + (d(L²−1)/(2L))(L^j−1)/(L−1) ≤ (1 + d(L+1)/(2L))L^j**, with
the exact values 205/27, 2021/81, 6115/81 at L = 3, d = 4, j = 1, 2, 3 (check nq1). It is the composite companion of
J-str (c)'s ‖Q_str^T‖_{∞→∞} = L^{−(d−1)} and it is what a potential bound (as opposed to a curvature or residual
bound) must go through. The proof is §Q3 and uses only L3g(a)-slice's identity and root covariance.

**4. SQ.md owner — no error found, but one clause would prevent a re-run of this confusion.** Lemma SHIFT's
parenthesis at l.710-711, "(Q^m is the straight average over L^m-blocks, …)", is correct under §11.0's declared
"Q := Q_str (§0.4)", and in any case d∘Q_root^{(m)} = d∘Q_str^{(L^m)} makes the step insensitive to the choice. Read
from outside SQ it looks like a statement about Setting SC's Q, and that is how it was recorded as a file conflict in
NORMS.md §N4 / FOR-OTHER-FILES item 1. Suggested clause: "*(Q = Q_str here by §0.4; Setting SC's Q is Q_root, and only
dQ_root = dQ_str is used)*". Second, more substantive: §0.4's substitution is a **gauge shift** (B_i ↦ B_i + dλ_i,
λ_{i+1} = avg λ_i + h(B_i)), so it is **not** available to a consumer that needs a potential bound in a stated gauge —
NORMS.md's Lemma N1-11 is such a consumer. Worth one sentence in §0.4 ("curvatures and residuals only; the potentials
move by the accumulated funnel gauge").

**5. PROOF.md — two small records, if the lead wants them.** (a) Root covariance Q∘d = d∘ev and the slice identity
Q = Q_str − d∘h together give the exact composite identity
Q^{(j)} = Q_str^{(j)} − d_j Σ_{i<j} ev^{(j-1-i)}∘h∘Q_str^{(i)}, which is the non-self-referential form of
h^{(m+1)} = Mh^{(m)} + hQ^{(m)} (l.2787, l.2980) and is what makes the composite funnel bookkeeping j-uniform. (b) The
L3g(a)-slice identity was re-verified here as **exact rationals**, entrywise, at L = 3, d = 4, in all four directions
(gate G1), which strengthens check c8(f)'s 2e-16 to an identity.

---

## §Q6 POST-HOC check of Theorem NQ-1's Step 1 (labelled post-hoc; no pre-registered verdict)

Run **after** check nq1's result was seen, and therefore labelled post-hoc under the brief's rule 3. It is a self-check
of the proof's algebra, not a new result, and nothing in §Q1–§Q5 depends on it.

Script `checks/nq1_telescope_posthoc.py`, output `checks/nq1_telescope_posthoc_out.txt`. It verifies **entrywise and
exactly, as integers over DEN1^j**, the Step 1 identity

  Q^{(j)} = Q_str^{(j)} − d_j ∘ Σ_{i=0}^{j-1} ev^{(j-1-i)} ∘ h ∘ Q_str^{(i)}

at L = 3, d = 4, for j = 1 and j = 2, in all four link directions, by building each side independently with the row
machinery of `nq1_qnorm.py` (unaltered). Result: **0 entries differ in all 8 cases** (459 nonzero entries per row at
j = 1, 47 385 at j = 2) — ALL MATCH. j = 1 is input (i) itself; j = 2 is the first instance of the induction step,
which is uniform in j. j = 3 was not run: two 4.1M-entry rows at once would exceed the brief's 1 GB budget, and the
induction step is already exercised at j = 2.
