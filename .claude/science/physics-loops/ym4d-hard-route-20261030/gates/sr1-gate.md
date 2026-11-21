First failing step: none.

# sr1-gate: pass-3 referee check of `library/sr1.md`

Referee: Claude Opus 5.5 (`claude-opus-5-5`), fresh session, 2026-11-05. One reading by one other model of a Codex distillation. This is not an audit and grants no status. Every step was redone by hand. No computation was used as a proof step.

Credit: the arguments rebuild Ethan Sussman and Levent Alpoge's outline (with Claude and Codex as the authors of their text), at `31a47c543775`.

## What was read

- `library/sr1.md`, whole, line by line, once.
- Its sources: `library/d2-d4.md` and `library/growth-qf3.md`, whole. Their gates: `gates/bridge-check.md` §1 (and §2 for the box-size clarification) and `gates/cluster-check.md` Part B.
- The SR1 entry of `library/ym4-assembly.md` §§4–5, and the UV1, IN1 and LG1 entries there.
- Imports: `library/lg1.md` (definitions, Theorem 10, Lemma 11, Theorem 13) and `library/in1.md` (constant order, Theorem 12, Amendment 1).
- SA outline `scratchpad/sa/ym4.tex` (sha1 prefix `107abaef`, the same file bridge-check read): L4086–4196 (D1, D2, D3, D4), L4541–4605 (G4, H1), L23621–23660 (ST1), L23770–23905 (ST5–ST10), L24060–24140 (GS1–GS3 and the cell-source setup), L24651–24720 (CC8–CC10), L24917–24990 (QF1–QF3), and spot reads of L2834–2942 (AM5–AM7 chessboard) and L25073–25110 (QF8 period cubes).
- YM3_I `scratchpad/sa/YM3_I.tex`: L74807–75168 searched for the Fourier order and slot weight (IV-25-55, IV-26-24/37).

The CA-II row of the source concordance (line 537) was not re-read. It is outside the requested texts, and sr1 says it imports nothing from it.

## Check by statement

**Definitions and imports (L7–86).** (1) and (2) match the assembly conventions and SA L23632. The UV1 form (4)–(6) matches SA (ST5)–(ST6) L23770–23812 and D1 L4088–4135: raw upper bound with V, floor, point terms, domain terms with locality, representation independence, normal convergence, and the rooted cube/tree indexing. The source radius 2r_src for the list norm is SA's. The separated-limit definition (7), the spaces (8) and the RP form (9) are consistent with SA H1 (L4572–4590) and QF2.

**Order of constants (L88–105).** The ten rows abbreviate IN1's table (in1.md L221–236) with Amendment 1. L ≥ 27 is IN1's standing choice (in1.md L9). The added SR1 order (p, then k, C_B, b_0, C_E, before n, R, d, positions, states) has no cycle.

**Theorem 1 (L107–129)** matches the assembly SR1 entry clause by clause. The proof map to Lemmas 2–10 is complete.

**Lemma 2.** Checked: nonnegativity of the disseminated integral by torus RP at a link-plane pair (LG1 Theorem 13.3); the complex one-direction chessboard (T² ≤ T₊T₋, both reflected fillings maximize, run doubling, constant fillings ≤ 1, ε ↓ 0); the four directions; triangle inequality, homogeneity, P(F̄) = P(F). (14): C(ℓ/a)³ boundary plaquettes, 2β each, numerator and denominator, divided by N = (ℓ/l)⁴, gives Cβl⁴a⁻³ℓ⁻¹ (LG1 (24) has the constant 384). The log(1+tG) step with ℓ first, then t ↓ 0, is correct. The coarse-cell step is correct, since the coarse reflections are fine-board reflections with the same parity.

**Lemma 3.** Checked: list norm of W^ch ≤ 2Σ|z_i|t_{f_i}, so (4) applies on Σ|z_i|t_{f_i} < r_src; the odd-cell conjugation keeps the real part and holomorphy; a discarded nonzero domain has diam X⁺ ≥ b, so m ≥ b/(C_dep a_s) − 1; (16) per cell, with stability cost (C₊+C₋)ℓ⁴/N = (C₊+C₋)l⁴, and the scale sum Σ L^{4s}e^{−c′bL^s} < ∞. This is SA (ST8)–(ST9). The fixed-K local bound, Montel selection and the state-independent subsequence are correct. Offset count: l/a > n(2(R+b)/a + 2) once l > 2n(R+b+1).

**Lemma 4.** Cauchy on |z| < r_src/t_f gives |h′(0)| ≤ Q t_f/r_src. The partition of unity uses an everywhere-nonnegative bump (gate correction kept). Product rule gives t_{fφ_k} ≤ (1 + c_M C)t_f. The plaquette clause uses f ≥ 0 everywhere and f ≥ 1 on a unit cube; the case a ≥ a₀ is correct.

**Lemma 5.** (19): 16 roots, 8^{2m} walks, at most 16(m+1) candidate cubes. This is SA (GS1) L24078–24093 verbatim in content. (17) follows by root counting. The table (20): global count divided by (ℓ/η)⁴ for a_s ≥ η; bounded cost on log_L(η/δ)+1 scales; forced size for a_s < δ. The bound 3^j ≥ 2j(j−1) is correct. Stability cost ≤ C₊+C₋ since η ≤ 1.

**Lemma 6.** (21)–(22) correct. Offset count: with a ≤ δ/16 = η/(1024n), n(4δ/a+2) ≤ (33/8)nδ/a = (33/512)η/a. Distinct tests sit in distinct cells, since 2η ≤ d̄/8 < d. Q_i ≤ Q₀(64n)^p. (23) is a product polydisc. (24): the mixed derivative at 0 is ρ(ΠX_i) because E_i(0) = 0. The 2ⁿ expansion and the piece sum give (25), with δ⁻⁴ (count) times δ⁻¹ (norm), and δ⁻¹ < 1024Ln/d̄. The coarse case a > δ/16 is correct. n^{(p+5)n} ≤ e^{kn}(n!)^k. (26)–(27): Σ_{|π|=m} Π|D|! = n!·C(n−1,m−1)/m!, times (m−1)!, gives the bound 2^{n−1}(n!)^k. Centering at ρ for n ≥ 2 is legitimate, since higher cumulants are shift-invariant.

**Lemma 7.** (28) from (10) at R = 1 with ‖f‖_♯ ≤ max(1,c_M)‖f‖₁ and the 2ⁿ real/imaginary split. (29): Re(1/z) ≥ 2/(9t) on |z−t| = t/2; the bound is 9^q(q!)². (30): the factor C(q,r)⁻¹ is correct, and the induction closes with sum 1/2. (31): ψ-sum ≥ 1 with at most three terms; ζ = 0 on |u|_∞ ≤ 1, 1 on |u|_∞ ≥ 2. (32): multinomials sum to N^q, Π|α_k|! ≤ q!. Tensor consistency: d/2 + d/4 < d forces a zero factor; otherwise point-evaluation bases give injectivity of the algebraic tensor product.

**Lemma 8 (4D Fourier counts).** Inner side 2ε, expanded side 4ε, period 8ε; the expanded cube meets no other period copy of the inner cube. (1 − π⁻²Δ_y)⁴ per slot is 8 derivatives per slot, 8n in total, and gives Π(1+|v_i|²)⁻⁴. Cut-off modes have C¹ norm ≤ Cε⁻¹(1+|v|). Shell |v|_∞ = r in Z⁴ has Cr³ points with summand Cr⁻⁷, so the slot sum converges. Losses: (h/2)⁻⁵ⁿ from (28) and (64/h)ⁿ from the norms give h⁻⁶ⁿ. The Fejér identification and the overlap gluing are correct.

**Lemma 9 (4D Taylor and position counts).** (36) layer support is correct. Retained boxes: expanded-cube distance ≥ h_j − 6ε_j = (58/64)h_j > h_j/2. (37): (Cn²)^{8n}((8n)!)² ≤ Cⁿ(n!)³². (38): |x − y| ≤ 8h_j, ℓ¹ displacement ≤ 16h_j over four coordinates, Taylor order m = 10n+2, total derivative order 18n+2 ≤ 20n, weight ratio ≤ 3. (40): h_j⁻⁴ⁿ positions, with radial tail ∫r^{3−20}dr. (41): h_j^{10n+2−6n−4n} = h_j². The sum over j converges.

**Lemma 10.** (43), (44) and the positive-time cutoff (45) are correct. Cross-diagonal flatness in the three time cases and (46) are correct. The lattice-to-limit RP paragraph is correct: a lattice coordinate mirror within a^{(j)} of time zero, centering covariance from ν_j's reflection invariance (LG1 Theorem 13.5), a translation of size ≤ 2a^{(j)}, and telescoping with (10). This matches SA CC8–CC10 L24651–24717.

**Imports used only as stated.** UV1 is used only through (4)–(6) and the rooted geometry. LG1 is used for torus link-plane RP (Theorem 13.3) and for invariance and RP of every periodic state (Theorem 10 / 13.5). IN1 supplies only the order and the meaning of a datum.

**Source readings.** The concordance rows for YM4 L4086–4194, 4541–4599, 2834–2942, 23621–23883, 23884–24335, 24917–25391 and 24651–24717 read correctly where I read them: D1 is an obligation; D2, D4, G4, H1 are conditional deductions; the nonnegative bump is SA L4189–4190; the separation exponent is 5n; (ST5) is a raw bound and floor, not a zero-free logarithm. The YM3_I reading is correct: IV-25-55 uses order 4n+1 (L74818, L74851) and IV-26-24/37 use the slot weight (1+|x_l|²)⁻² (L75028 and following).

## Findings

1. **L36 and L553 (LG1 import labels).** The text imports "S1d" and "S1g". These are labels of the old skeleton. `library/lg1.md` states them as Theorem 13, clause 3 (torus link-plane RP) and Theorem 10 / Theorem 13, clause 5 (all-state invariance and RP). The mathematics is right. **Repairable, wording only.** Repair: name the LG1 theorem and clause next to each label.

2. **L105, L124 (symbol C_E).** The H1 growth constant C_E has the same name as IN1's row-7 constant C_E (in1.md L233), which the order table (L100) says it retains. The two are different objects. No step confuses them. **Repairable, wording only.** Repair: rename the growth constant, for example C_{H1}.

No other defect was found.

## Verdict

ADVANCE. `library/sr1.md` proves, as stated, the conditional implication full rooted UV1 + LG1 ⇒ SA-D4, G4 and D2, with B(R) = C(R+1)⁴, k = ⌈p⌉+5 and loss max(1, d⁻⁵ⁿ). For every existing separated limit (7) it proves H1 with k_E = 20 and exponent k+32, constrained tensor density, uniqueness, and RP transfer, including compact RP from LG1. Each lemma matches its source note and keeps the gate corrections (nonnegative bump, S1g dependence, S1d link-plane input, explicit box sizes). The main theorem matches the SR1 entry of the assembly. UV1 stays an open import, as the text says.

Checked line by line by Claude (fresh session).
