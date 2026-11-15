lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GB1E referee report (pass 3)

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (model id `claude-opus-5-5`, max effort), as pass 3 under PR #10138's method. Claude drafted the part (`GB1E_DRAFT.md`, pass 1). Codex gpt-6.1-terra distilled it (`GB1E.md`, pass 2). This session wrote neither. This is one check: one whole-part, line-by-line read of `GB1E.md`. No review of this review was commissioned, and this report reviews no other review.

**What this file is.** A referee report. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. It does not edit `GB1E.md`.

**Text read.** `GB1E.md` at commit `b7aca11a2` (the commit that writes it; branch head when read). SHA-256 of the file read: `36cc1b9ea2c35aa72db7405e6eb946241f1352b7e889012f8cf39ddcefaf0b5c`. All 204 lines were read in order. Line numbers below refer to that file.

**Sources read, with commits.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (this checkout) | `b7aca11a2` |
| `origin/claude/ym4d-hard-route` (read with `git show` only, after `git fetch -q origin claude/ym4d-hard-route`) | head `4cc8895bd`; file last changed `e7a21cd98` |

This folder: `GB1E_DRAFT.md`, all 477 lines (SHA-256 `aa1d0f93…0c4663`, equal to the hash `GB1E.md` line 15 records); `prior/GB1E.md`, all 85 lines (SHA-256 `f8bb1c96…b745`, equal to the hash `GB1E.md` records); `GB1QL.md` lines 9, 35-75 (§1.1-1.4), 183-190, 209, 211, 219-221 (Lemma 4.7 and its plaquette step), 227-229, 259 (Theorem 4.8 and its scope), 299, 303 (Proposition 4.11), 326-345 (Lemma H, hand-off table); `GB1.md` lines 31, 45, 59-67 (Theorems 2.1 and 2.3), 209, 212 (rows H2, H5); `GA2_Y2.md` lines 176, 178; `GA2_Y2_DRAFT.md` lines 205-215 (T0-start[G], T0-rate); `SMG1.md` line 29 (Lemma G0); `TOE_ASSEMBLY.md` lines 259-265 (§3.10, bounded R-GEN); `LW1_5_DRAFT.md` line 328 (the four tests); `LW1_REFEREE.md` lines 1-80 and `Y2W_DRAFT.md` lines 1-30 (format only). YM branch: `.claude/science/physics-loops/ym4d-hard-route-20261030/library/port/p8-positivity.md` lines 26-48 (B5, (P8.1)), 81, 131, 144, found by grep for "P8.1", "torus isometry", "Reducible". The `docs/` notes on `origin/main` that `GB1E.md` credits (lines 54, 80, 186) were not read; they carry no proof step in `GB1E.md`, and this report uses none of them.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The test law, R-SUM, R-IA and bounded R-GEN are read plainly. No hostile meaning is read into any axiom or owner text.

**Working-set entries used.** None as a premise. PS-6r enters only through `GB1QL.md`'s rung test law `L5[SU(2), s]` (not a working-set law). The owner decision SMG1-GAP = R-GEN, bounded (`TOE_ASSEMBLY.md` line 261, scope SMG1 only) is read to judge `GB1E.md`'s GAP 1; its scope is not widened here.

**Method.** Every proof was re-derived by hand, including the trace-norm Trotter bound, the crossing-kernel reflection argument, the sign field, the Duhamel analyticity and `Δ'(0)`, and the tree-level dictionary. A `[check]` is a scratch computation in `/tmp/toe-GB1Eref/` (under a minute, a few MB). It guides and never proves. Verdicts: CORRECT; ERROR (a false or misattributed line, quoted, with a fix); INCOMPLETE (a named missing step). A **referee closure** is a short complete argument for a missing step, written to be formalizable in Lean. Theorem numbers below are those of `GB1E.md`; the draft's numbers are given where the lane brief uses them (draft Theorem 7.5 = `GB1E.md` Theorem 7.2, last clause; draft Theorem 8.2 = 8.1; draft Lemma 8.3 = 8.2; draft Theorem 8.4 = 8.3).

**Counts.** 69 items: 63 CORRECT, 1 ERROR, 5 INCOMPLETE. No ERROR or INCOMPLETE item changes a proved finite-box theorem. Items 32, 33 and 66 (one finding, the repair of GAP 1) change what the generator readings give. Item 65 (GAP 2) sharpens the hand-off order.

---

## 1. Verdict table

| # | Item (`GB1E.md` line) | Verdict | Note |
|---|---|---|---|
| 1 | §0 status and scope (5) | CORRECT | |
| 2 | §0 "Proved" summary (7) | CORRECT | Each clause is proved below. |
| 3 | GAP 1 statement (9) | CORRECT | The gap is real. Its repair is incomplete: items 32, 33, 66 and §2.1. |
| 4 | GAP 2 statement (11) | CORRECT | The gap is real for Y1 and for `Z⁴`. Sharpened in §2.2: T0-start[G]'s own text quantifies over torus sides. |
| 5 | §0 "Open by name" (13) | CORRECT | Every listed item appears in §3 below. |
| 6 | §0 provenance (15) | CORRECT | Both recorded SHA-256 values match the files `[check: shasum]`. |
| 7 | Box, link space, `H_k`, `E²`, `Θ` (19) | CORRECT | `dim H_k=(k+1)²` and `E²=k(k+2)/4` match `GB1QL.md` §1.1. The `N_t=2` remark is right: the two mirror planes cross distinct oriented bonds. |
| 8 | Gauge action and `P_0` (23) | CORRECT | `R(h)R(h')=R(hh')` with the stated `h·U`. |
| 9 | `CF`, `B_p`, `H_B`, `V_θ`, `H` (25) | CORRECT | Parity description re-derived. The unnormalized trace matches `GB1QL.md` line 209 (`‖tr X^s_p‖ ≤ 2`, `‖B_C‖ ≤ 24`). Each `CF` plaquette lies in one tiling cube, so `Σ_C B_C = H_B`. |
| 10 | Transfer-kernel lift (27) | CORRECT | |
| 11 | `Π_k`, `z_k`, `k_t`, class `𝒫` (29) | CORRECT | |
| 12 | Local-lift density and `W_{xy,r}` (31-35) | CORRECT | Under `U ↦ h_yUh_x^{-1}`, `V_{x,r} ↦ h_{x,r+1}V_{x,r}h_{x,r}^{-1}`, `W` is conjugated by `h_{x,r}`. |
| 13 | Exact lift, `𝒜_HK`, `𝒜_FK` (36) | CORRECT | "equivalently" holds by Theorem 3.2. |
| 14 | Link reflection and RP (38) | INCOMPLETE | The action on bond variables is not stated. Add: `(ϑ·U)_b = U_{ϑb}`, inverted when `ϑ` reverses `b`, as in (P8.1) (`p8-positivity.md` line 37). |
| 15 | Theorem 2.1 (42-48) | CORRECT | Re-derived, including `dim P_0𝓗 = ∞` (powers of `Tr X_p`; its law under Haar has a density on `[−2,2]`). |
| 16 | Theorem 2.2 (50-52) | CORRECT | First-minimum argument and approximation by `p_n²` re-derived from draft Lemma 4.2. |
| 17 | Credit paragraph (54) | CORRECT | Credit only; the note was not read here and carries no step. |
| 18 | Theorem 3.1 (58-68) | CORRECT | `M² = e^{βΣ_{CF}Tr X_p}`; the gauge-averaged kernel is that of `TP_0`; `Z>0` from injectivity. |
| 19 | Theorem 3.2, rate (70-76) | CORRECT | Re-derived step by step from draft Lemmas 4.6-4.8 and Theorem 4.9: the two Duhamel identities, the graph-norm `O(s²)` one-step bound, the kernel domination, the three ranges of `j`. "Sufficiently large `n`" means `n ≥ 8` and `a_0/n ≤ 1`. |
| 20 | Theorem 3.2, existence, gauge invariance, `Z` (74, 78) | CORRECT | The `L²` limit keeps `0 ≤ K ≤ e^{a_0‖V_θ‖}∏k_{a_0τ_E}`. |
| 21 | Theorem 3.2, coarse-graining and TV limit (74, 78) | CORRECT | The substitution `Ũ_j=(V_{j−1}⋯V_{j_0})·U_j` and `∫|K_n−K| ≤ ‖K_n−K‖_{L²}` re-derived. Oddness of `n` is not used here; it is used in Theorem 6.1. |
| 22 | Credit paragraph (80) | CORRECT | Credit only. |
| 23 | Theorem 4.1 (84-86) | CORRECT | The identity is exact. See §2.3 for what "one free step" means. |
| 24 | Paragraph after 4.1 (88) | CORRECT | `GB1.md` lines 45 and 59-63 match. |
| 25 | Four-test legend (90) | CORRECT | Matches `LW1_5_DRAFT.md` line 328. |
| 26 | R-SUM row (94) | CORRECT | Grades defensible; §2.4 gives the referee's reading of each test. |
| 27 | R-IA row (95) | CORRECT | §2.4. |
| 28 | Bounded R-GEN row (96) | CORRECT | "C P C C" matches `TOE_ASSEMBLY.md` line 261. Those grades are for SMG1's scope. The row should add what the reading gives on GB1 (§2.1, closure R2). |
| 29 | R-ISO row (97) | CORRECT | |
| 30 | Theorem 5.1 (101-103) | CORRECT | Tonelli, symmetry of the kernel of `X^{N_t/2}`, and `Tr X^{N_t} ≥ e^{−N_ta_0‖H'‖}·rank P_0 = ∞` re-derived. |
| 31 | Theorem 5.2, finite registers (105, 107) | CORRECT | No finite-register phase is `π` mod `2π` when `τ_E/π` is irrational. `w(x)=x` on `[0,π)`; the eigenphases increase in `k`. |
| 32 | Theorem 5.2, infinite register (105, 107) | INCOMPLETE | "Weyl equidistribution" is cited, not rebuilt. Referee closure R1 (§2.1) rebuilds what is used. The rest of the step is right: `‖X‖<π` puts `spec e^{−iX}` on a closed arc that misses `−1`. |
| 33 | Paragraph after 5.2 (109) | INCOMPLETE | It omits the `τ_E` at which strict R-GEN is defined. Closure R2 (§2.1): wherever strict R-GEN defines a GB1 Hamiltonian, Theorem 5.1 excludes a lift. |
| 34 | Theorem 6.1, `CF` and reflections (113-115) | CORRECT | `2m−x_i ≡ x_i`, `2m−x_i−1 ≢ x_i` (mod 2); `N` even. |
| 35 | Crossing-kernel argument (117) | CORRECT | Re-derived from draft Lemma 6.2: the split `σ=σ'σ''^{-1}` puts the `Γ_−` indices on `σ'` and the `Γ_+` indices on `σ''`, giving `Σ_α c_α G_α(U_+)\overline{G_α(ϑ·U_−)}`, `c_α ≥ 0`. Absolute convergence needs `Σ_q a_qd_q^6 < ∞` (four plaquette indices, two splitting indices); `𝒫` gives every moment. |
| 36 | Temporal, spatial `β ≥ 0`, sign field (119) | CORRECT | Products of `σ` around `(1,2)`, `(1,3)`, `(2,3)` plaquettes are each `−1`; `σ` is independent of `x_1`; temporal plaquettes carry `σ_ℓ² = 1`. |
| 37 | Exact lift RP; site mirrors (121) | CORRECT | Fine mirror at `nt_0+n/2 ∈ ℤ+½` for odd `n`; coarse `Γ_+` temporal links are products of fine `Γ_+` links. The log of a positive injective operator is unique, so commuting transfers force `[ϑ, H_B]=0`. |
| 38 | Scope remark (123) | CORRECT | |
| 39 | Theorem 7.1 (127-134) | CORRECT | `c_0=I_1(2b)/b` and the recurrence `I_k−I_{k+2}=2(k+1)I_{k+1}/x` checked; `[check]` agrees with the draft's `10^{-11}` report. |
| 40 | Theorem 7.2, `μ_loc` exchange (136-138) | CORRECT | Bond counts: a direction-1 bond meets 2 `CF`, 2 non-`CF`, 2 temporal plaquettes; a temporal bond meets 6 temporal plaquettes. At `β=0` the relation forces `k_t` constant near `e`, the `b=0` case of 7.1. |
| 41 | Theorem 7.2, unit translation (136, 138) | CORRECT | |
| 42 | Theorem 7.2, `μ_ex` at `θ=0` (140) | CORRECT | |
| 43 | `Δ=0` from exchange and time translation (140) | CORRECT | `ς` sends a `(1,2)`-plaquette at `x_1` to a `(t,2)`-plaquette at time `x_1`. |
| 44 | Duhamel series entire in `θ` (140) | CORRECT | `‖I_m‖_1 ≤ ‖H_B‖^m(β^m/m!)Θ(βτ_E/(m+1))^{|𝓛|}`, polynomial in `m` against `1/m!`. |
| 45 | `Δ(0)=0` and `Δ'(0)<0` (140-143) | CORRECT | Only `r=p` survives; the denominator's derivative vanishes; `u ↔ β−u` symmetrizes the integrand into the displayed Hilbert-Schmidt norm. |
| 46 | Discrete subset of `ℝ∖{0}` (144) | CORRECT | This is the draft's Theorem 7.5. |
| 47 | Theorem 7.3, `c_t` (146-150, 158) | CORRECT | `sin((k+1)ψ)/((k+1)sinψ) = 1 − k(k+2)ψ²/6 + O(k⁴ψ⁴)`; `dc_t/dt = −(2/3)Var_t(E²)`; `⟨E²⟩_t ~ 3/(2t)`. |
| 48 | Theorem 7.3, dictionary (150-156, 158) | CORRECT | Re-derived: matching `(β/2)(a/a_0) = c_t(a_0/a) = 2/g²` gives both formulas and the ray limits. It is a definition by classical matching, as line 160 says. |
| 49 | Relation to T0 (160) | CORRECT | T0's weight `e^{(x_0/2)Tr}` follows from `p8-positivity.md` lines 46-48 (`tr 1 = 1`). `GB1.md` row H5 (line 212) matches. |
| 50 | §8 notation (164) | CORRECT | |
| 51 | Theorem 8.1, `m_s>0` (166, 168) | CORRECT | Draft Theorem 8.2. |
| 52 | Theorem 8.1, kernel bound, real part (166, 168) | CORRECT | `|κ_X−κ_1| ≤ ‖X−1‖d_s^{|𝓛|}` holds for every `X`; the real part is the right statement for complex kernels. |
| 53 | Theorem 8.1, thresholds (166, 168) | CORRECT | The `θ=0` bound is valid since `log(1+x)<x`; the proof gives the larger `4m_s/(d_ss(s+2))`. `[check]` reproduces the draft's `D_s` and `s=1` minima. |
| 54 | Scope after 8.1 (170) | CORRECT | The draft's counterexample wording ("the framework at fixed `s` supplies a probability measure") overreached; this line states the true scope. |
| 55 | Theorem 8.2 (172-174) | CORRECT | Draft Lemma 8.3. Nonnegative orthonormal columns have disjoint supports. |
| 56 | Scope after 8.2 (176) | CORRECT | The draft's "an exactly gauge-invariant Euclidean measure ... needs the infinite register" is unproved; it is rightly not carried. |
| 57 | Theorem 8.3, statement (178-182) | CORRECT | Draft Theorem 8.4. |
| 58 | Theorem 8.3, proof (184) | CORRECT | `GB1QL.md` line 209 gives `B̃_C = ιB^s_Cι^*`; line 219 gives `‖(B̃_C−B_C)v‖ ≤ 96δ_s(M'')‖v‖`; Lemma 4.3 gives `δ_s(M') = 2M'(M'+3)/(s(s+3)) → 0`. Eigenvalue limits, domination by `τ_Eα_i − w'`, and the trace-norm upgrade re-derived. |
| 59 | Paragraph after 8.3 (186) | ERROR | "The fixed-volume SU(2) real-time regulator comparison was already proved in `GB1QL.md` Theorems 4.8–4.10". `GB1QL.md` line 303 says those rates hold "uniformly in the volume and in `n ≤ T`", and 4.9, 4.10 are corollaries. Fix: "The volume-uniform, finite-time SU(2) real-time regulator comparison was already proved in `GB1QL.md` Theorem 4.8 and Corollaries 4.9-4.10." |
| 60 | Hand-off row (H-G) (192) | CORRECT | `GB1QL.md` line 299. |
| 61 | Row (H-4D), (H-GI), (H-Haar) (193) | CORRECT | |
| 62 | Row (H-RP) (194) | CORRECT | |
| 63 | Row (H-class) (195) | CORRECT | |
| 64 | Row T0-rate, Y3, E-2, VC1 (196) | CORRECT | |
| 65 | Line 198, first two sentences | INCOMPLETE | T0-start[G] quantifies "for every `a`, every torus side, every `k_0`" (`GA2_Y2_DRAFT.md` line 211). The finite-torus lifts with `N_t=N` even are measures of the kind it takes. §2.2. |
| 66 | Line 198, R-GEN sentences | INCOMPLETE | As item 33; closure R2. |
| 67 | Line 200 | CORRECT | |
| 68 | Draft checks (202) | CORRECT | Reported as draft output. The referee's own `[check]` agrees on every value it recomputed (§2.5). |
| 69 | Literature scope (204) | CORRECT | |

The INCOMPLETE items are 14, 32, 33, 65 and 66; items 33 and 66 are one finding. The ERROR is item 59. Sections 2.3 and 2.4 add wording notes to items 23, 26 and 28; they do not change those verdicts.

---

## 2. The distiller's GAPs and the lane's decisions

### 2.1 GAP 1 (principal generator): real; repaired below

`GB1E.md` line 9: "For irrational `τ_E/π`, the electric phases are dense on the circle. Thus −1 is in the spectrum and the owner's strict `‖X_g‖<π` generator does not exist for the infinite-register electric gate." This is true. The draft's Proposition 3.2(a) applied `SMG1.md` Lemma G0, whose text begins "Let `g` be a unitary on a finite-dimensional space" (`SMG1.md` line 29), to the infinite-dimensional gate `e^{−iτ_EE²}`. There "no eigenvalue −1" does not give "−1 ∉ spec". Two steps were missing: a rebuilt density lemma, and what strict R-GEN gives at the `τ_E` where it is defined.

**Referee closure R1 (density of quadratic phases).** *Let `α ∉ ℚ` and `c ∈ ℝ`. For every `ε > 0` there is `m ≥ 1` with `dist(αm² − c, ℤ) < ε`.*

*Proof.* Write `e(x) = e^{2πix}`. *Step 1 (van der Corput).* Let `|u_m| ≤ 1` for `1 ≤ m ≤ M`, `u_m = 0` otherwise, and `1 ≤ H ≤ M`. Each `u_m` occurs `H` times in `Σ_n Σ_{r<H} u_{n+r}`, where `n` runs over `M+H−1` integers. Cauchy–Schwarz over `n`, then grouping the pairs `(r, r')` by `h = r − r'`, gives
`|Σ_m u_m|² ≤ ((M+H)/H) Σ_{|h|<H} (1 − |h|/H) |S_h|`, with `S_h = Σ_n u_{n+h}\overline{u_n}`.
*Step 2.* Fix an integer `j ≠ 0` and put `u_m = e(jαm²)`. Then `u_{n+h}\overline{u_n} = e(jα(2hn + h²))`. For `h ≠ 0`, `2jhα ∉ ℤ`, so the geometric sum gives `|S_h| ≤ 1/|sin(2πjhα)|`. Also `|S_0| ≤ M`. Divide by `M²` and let `M → ∞`: `limsup |M^{-1}Σ_{m≤M} e(jαm²)|² ≤ 1/H`. As `H` is arbitrary, `M^{-1}Σ_{m≤M} e(jαm²) → 0`.
*Step 3.* For `0 < ε < ½` let `f(x) = max(0, 1 − dist(x − c, ℤ)/ε)`. It is continuous, 1-periodic and nonnegative. It is positive only within `ε` of `c + ℤ`, and `∫_0^1 f = ε`. Its Fourier coefficients are `f̂(j) = ε e(−jc)(sin(πjε)/(πjε))²`, which are absolutely summable. So `M^{-1}Σ_{m≤M} f(αm²) = Σ_j f̂(j) M^{-1}Σ_{m≤M} e(jαm²) → f̂(0) = ε > 0`, by Step 2 and dominated convergence over `j`. Hence `f(αm²) > 0` for some `m`. □

*Use.* The link eigenphases are `φ_k = τ_Ek(k+2)/4 = 2πα((k+1)² − 1)` with `α = τ_E/(8π)`. `α` is irrational exactly when `τ_E/π` is. R1 with `c = α + ½` and `m = k+1` gives `dist(φ_k − π, 2πℤ) < 2πε` for some `k`. The spectrum of the diagonal unitary `e^{−iτ_EE²}` is the closure of its eigenvalues, so it contains `−1`. `[check]` at `τ_E = 1`: the least distance from `φ_k` to `π` (mod `2π`) over `k ≤ K` is `4.2·10^{-2}, 2.1·10^{-3}, 1.3·10^{-3}, 1.8·10^{-4}, 6.3·10^{-6}` for `K = 10, …, 10^5`.

**Referee closure R2 (what strict R-GEN gives on GB1, for every `τ_E`).** Read R-GEN's text (`TOE_ASSEMBLY.md` line 261) with GB1's gates: the cube gates `e^{−iθB_C}` and the link gates `e^{−iτ_EE²_ℓ}` (`GB1QL.md` §1.3), on a finite box.

*(a) Existence and uniqueness, any dimension.* For a unitary `g`, a Hermitian `X` with `e^{−iX} = g` and `‖X‖ < π` exists if and only if `−1 ∉ spec g`, and it is then unique. *Proof.* If `‖X‖ < π`, then `spec g = e^{−i spec X}` lies on a closed arc that misses `−1`. Conversely, if `−1 ∉ spec g`, the compact set `spec g` lies on an arc `{e^{−ix} : |x| ≤ π − δ}`. Let `f` invert `x ↦ e^{−ix}` there; it is continuous. Then `X = f(g)` has `‖X‖ ≤ π − δ`. If `X'` is another such operator, `f ∘ e^{−i·}` is the identity on `spec X' ⊂ (−π, π)`, so `X' = f(e^{−iX'}) = f(g)`. □ This extends Lemma G0 to infinite dimension.

*(b) Where strict R-GEN is defined, there is no lift.* Suppose every GB1 gate has `−1 ∉ spec g`. Each `X_g = f(g)` commutes with every gauge operator `R(h)`, because `g` does. Their sum `H_U` has `‖H_U‖ < π·(number of gates)`. So `H_U` is bounded, self-adjoint and gauge invariant, and Theorem 5.1 excludes a transfer-kernel lift of `e^{−a_0H_U}` for every `a_0 > 0` and even `N_t`.

*(c) Elsewhere it defines no Hamiltonian.* If some gate has `−1 ∈ spec g`, strict R-GEN gives no `H_U`. This happens for every irrational `τ_E/π` (by R1). It also happens for rational `τ_E/π` with some `τ_Ek(k+2)/4 ∈ π(2ℤ+1)` (for example `τ_E = π/2`, `k = 2`).

*(d) Both cases occur.* Take `τ_E = π/3` and `24|θ| < π`. The cube gates satisfy `‖θB_C‖ < π`. The link phase `πk(k+2)/12` equals `π` mod `2π` only if `(k+1)² ≡ 13 (mod 24)`, hence `(k+1)² ≡ 5 (mod 8)`, which no square satisfies (squares mod 8 lie in `{0, 1, 4}`). The phases take finitely many values (`k(k+2) mod 24` is periodic in `k`). So `−1 ∉ spec`, strict R-GEN is defined, and (b) applies. `[check]`: squares mod 24 are `{0, 1, 4, 9, 12, 16}`.

**What this does to "under bounded R-GEN no lift exists".** The conclusion survives, in a split form. Under strict R-GEN widened to GB1, for no `τ_E` and no `θ` is there a GB1 Hamiltonian whose semigroup has a transfer-kernel lift. Where the reading is defined, the first failing step is the partition function (Theorem 5.1). Where it is not defined, which includes every irrational `τ_E/π`, the first failing step is the existence of the generator itself, that is, E-1 under that reading, before (H-4D). The draft's route to the conclusion (irrational `τ_E/π`, then the bounded `H_wr`) fails at its first step, as GAP 1 says. `GB1E.md` line 198 ("Strict R-GEN is undefined on the infinite electric gate under Theorem 5.2, so it cannot be used to claim that obstruction without changing the reading") is true at irrational `τ_E/π`. It is incomplete, because at `τ_E = π/3` strict R-GEN gives the obstruction unchanged.

**A fact for the owner's question, not a proposal (R3).** If `−1` is not an eigenvalue of a unitary `g`, there is exactly one Hermitian `X` with `‖X‖ ≤ π` and `e^{−iX} = g`. *Proof.* Existence: `X = f(g)`, with `f` the bounded Borel inverse of `x ↦ e^{−ix}` on `(−π, π]`. Uniqueness: for any such `X'`, the spectral projection of `X'` on `{−π, π}` equals the spectral projection of `g` at `{−1}`, which is zero. So `X'` lives on `(−π, π)`, where `x ↦ e^{−ix}` is injective, and `X' = f(g)`. □ So a non-strict variant of R-GEN ("`‖X_g‖ ≤ π`, with `X_g` required unique") would be defined at every irrational `τ_E/π`. Its link generator is then `w(τ_EE²)`, and its sum is the draft's `H_wr`. Theorem 5.1 then excludes a lift. Four tests, author-side: (1) P, it fixes no target; (2) P, the text is closed; (3) C, like R-GEN it fixes E-1 by premise, and on GB1 that fixes the (H-4D) answer; (4) P, it changes one bound and adds nothing. It is recorded, not proposed. Whether R-GEN's scope or bound changes is the owner's decision.

### 2.2 GAP 2 (scope of the hand-off): real; sharpened

`GB1E.md` line 11: "The constructed measures are finite-torus measures. A consistent infinite-volume measure, the full T0 reflection interface and membership in its unpinned class are not established." Each clause is true. Three facts sharpen what follows from it.

1. **T0-start[G] takes torus measures.** `GA2_Y2_DRAFT.md` line 211: "There is `g_* > 0` such that for every `a`, every torus side, every `k_0`, and every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4` …". The quantifier "every torus side" only makes sense for measures on tori. B5 is stated on "the torus `𝕋=ℝ⁴/Nℤ⁴`" (`p8-positivity.md` line 31), and `GB1.md` row H2 (line 209) names "The Wilson measure on `ℝ⁴/Nℤ⁴`". So on a hypercubic torus `N_t = N` with `N ≥ 4` even, both lifts are measures of the kind T0-start[G] takes. (H-4D), (H-GI) and (H-Haar) hold for them. (H-RP) holds for the reflections B5 states in (P8.1): coordinate reflections through planes that contain no site, in all four directions (Theorem 6.1). The cube-face tiling needs `N` even, so the family gives no start on odd sides. That does not block a hand-off, since T0-start[G] is a statement about every start in its class.
2. **The infinite-volume clause is real for Y1 and for Lemma H's wording.** Y1 asks for a representation "on `Z^3 x Z`" (`TOE_ASSEMBLY.md` line 613, quoted in `GB1E_DRAFT.md` line 39). `GB1QL.md` line 335 writes (H-4D) on "`a_{k_0}Z⁴`". No measure on the infinite lattice is constructed. The draft's sentence "`μ_loc` is a Euclidean representation on `Z³ × Z`" (`GB1E_DRAFT.md` line 474) exceeds its proof.
3. **The reflection interface decides which input fails first.** If the consumer's RP is (P8.1), the lifts pass (H-RP). If it is LG1 Theorem 13's set, "all coordinate site, coordinate bond and diagonal lattice mirrors" (quoted through `prior/GB1E.md` line 38; not read here), (H-RP) fails first. RP at a mirror includes invariance under it. `μ_loc` with `β ≠ 0` is not invariant under spatial site mirrors (Theorem 6.1). The diagonal mirror `x_1 ↔ t` is the exchange `ς` itself, and Theorem 7.2 excludes invariance under it, for `μ_loc` at every parameter and for `μ_ex` outside a discrete set of `θ`.

**Decision on "the first failing T0-start step under R-SUM is (H-class), at time–space exchange invariance".** CORRECT under three stated conditions: (i) T0-start[G] in its own torus form, with `N_t = N` even; (ii) (H-RP) read as (P8.1); (iii) `𝒜_{k_0}(g)` consisting of densities invariant under exchanging time with a space axis, as every image of the isotropic Wilson start under a hypercubic-covariant block map is. Under (i)-(iii), (H-class) fails at exchange invariance: for `μ_loc` at every `(β, t)`, and for `μ_ex` at every `θ` outside a discrete subset of `ℝ∖{0}`. Unit spatial translations also fail for `μ_loc` with `β ≠ 0`; exchange is the failure that holds at every parameter. Without (iii) the row is undecided, because the class is not pinned (`GA2_Y2.md` line 178). With LG1's mirror set in place of (ii), the first failure is (H-RP). On `Z⁴` in place of (i), (H-4D) is not delivered. `GB1E.md` §9 states the conditional form correctly. Its line 198 should name (i) and (ii) (required edit E4).

### 2.3 The lane's decisions on the lift and the tick

**(a) Existence under R-SUM, `τ_E > 0`.** Decided: yes, on every finite periodic box `(ℤ/Nℤ)³ × ℤ/N_tℤ` with `N ≥ 4` and `N_t ≥ 2` even, for every `θ ∈ ℝ` and `a_0 > 0`. The measure `μ_ex` is a gauge-invariant probability measure on `SU(2)`-valued links. It has a bounded density with respect to product Haar measure. Its transfer matrix is exactly `e^{−a_0H}` in the sense of line 27. It is link-reflection positive in all four coordinate directions. Proofs: Theorems 2.1, 3.2 and 6.1, all re-derived (items 15-21, 34-37). Not decided: a measure on `ℤ³ × ℤ` (GAP 2).

**(b) "The tick continued to imaginary angles is an exact local heat-kernel-in-time and cube-face-Wilson-in-space lift with one free step `λ`".** The identity `Φ(λθ, λτ_E) = T_loc` at `(β, t) = (−2λθ, λτ_E)` is exact (Theorem 4.1), and `T_loc` is the transfer matrix of `μ_loc` (Theorem 3.1). So the claim is CORRECT once three data are supplied: the written split into `W_B` and `W_E`, the sign `τ_E > 0`, and the representative of `τ_E`. The unitary `U_KS` alone does not supply them. The layer `W_B = e^{−iθH_B}` fixes `θ`, because the range of `H_B` is an interval of positive length. The layer `W_E = e^{−iτ_EA}` fixes `τ_E` only modulo `8π`: `4E²` has spectrum `{k(k+2)}`, and `gcd(3, 8) = 1`. Each representative `τ_E + 8πn > 0` gives a different ray. So, given the written layers, the free data are the step `λ > 0` and the integer `n`. "One free step" is exact for each representative. The draft's Theorem 5.1(c) ("and only from these … The tick fixes the ray") overstated this. `GB1E.md` drops it and says "The constants and angles are supplied data, not derived from the unitary alone" (line 88). That is correct. One sentence naming the representative should follow Theorem 4.1 (required edit E6). "Continued" means the substitution of angles in the analytic family `Φ`, which is built from the written layers. It is not an analytic continuation of the unitary `U_KS` itself.

**(c) Draft Theorem 8.2 = `GB1E.md` Theorem 8.1.** CORRECT in the real-part form. The counterexample is valid against "the embedded group-variable transfer kernel `ι_𝓛e^{−a_0H_s}ι_𝓛^*` is nonnegative" below the threshold, for every Hermitian `H_s`. It is not a counterexample to "the framework at fixed `s` supplies some probability measure". Line 170 states this scope correctly. **Draft Lemma 8.3 = Theorem 8.2.** CORRECT. **Draft Theorem 8.4 = Theorem 8.3.** CORRECT, per box: fixed box, `a_0` and `N_t`, then `s → ∞`. Its input `δ_s(M') = 2M'(M'+3)/(s(s+3))` (`GB1QL.md` Lemma 4.3) tends to zero, which the strong-convergence step needs.

**(d) Relation to T0's isotropic Wilson action.** Theorems 7.1-7.3 and line 160 are CORRECT. Same group (`SU(2)`) and same Haar links. T0 puts `e^{(x_0/2)Tr}` on every plaquette. The lifts put the heat kernel on temporal plaquettes and `e^{β Tr}` on half of the spatial ones. The heat kernel is never a Wilson weight (Theorem 7.1). The tree-level dictionary is a classical matching, not a quantum statement.

**(e) Draft Theorem 7.5 = `GB1E.md` Theorem 7.2, last clause.** CORRECT. One fact can be added; it changes no verdict. *`Δ` is odd in `θ`.* The central sign field `Ψ` of Theorem 6.1, acting on slice functions, is unitary. It satisfies `ΨAΨ^{-1} = A` and `ΨH_BΨ^{-1} = −H_B`, and it commutes with `P_0`. So `E_{−θ}[Tr X_q] = −E_θ[Tr X_q]` for every spatial plaquette `q`, and `Δ(−θ) = −Δ(θ)`. The possible exceptional set is therefore symmetric under `θ ↦ −θ`.

### 2.4 Are R-SUM, R-IA and bounded R-GEN four-tested correctly?

The tests are those of `LW1_5_DRAFT.md` line 328: "(1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need." A reading fails a test when the condition holds. The table gives `GB1E.md`'s grade, the referee's grade, and the reason where they differ or where the reason needs a word.

| Reading | Test | `GB1E.md` | Referee | Reason |
|---|---|---|---|---|
| R-SUM | 1 | P | P | The lane brief asks for "a stated generator reading"; the reading is an input. Existence, RP and the class row are proved from it, not assumed. |
| R-SUM | 2 | P | P | For GB1QL's family it reads only the operators the law names. A part cannot add to it without changing the law. |
| R-SUM | 3 | C | C | It fixes E-1, hence every imaginary-time correlator (`GB1.md` Theorem 2.1), by the law's notation. It leaves E-2 and Y3 open. The choice of the representative of `τ_E` mod `8π` belongs here too, since it selects the Euclidean theory. |
| R-SUM | 4 | C | P (C defensible) | Read literally, R-SUM adds no structure or constant beyond the written data. The draft's reason (the tick leaves the representative and the sign free) is a test-3 matter. C is a cautious grade, not an error. |
| R-IA | 1 | P | P | |
| R-IA | 2 | C | C | `λ` is left free, and a part can choose it. R-ISO is such a choice, and it fails tests 1 and 3. |
| R-IA | 3 | C | C | It defines the Euclidean side (E-1 and E-3 at once) instead of deriving it. |
| R-IA | 4 | C | C | Its reasons need a step, not a particular one; no law datum fixes `λ` or the representative. |
| Bounded R-GEN | 1-4 | C P C C, "recorded for SMG1 only" | not graded for GB1 | The record matches `TOE_ASSEMBLY.md` line 261, whose scope is "SMG1's rungs only". Those grades were made for finite-dimensional gates. On GB1's infinite link register the text is undefined at every irrational `τ_E/π` (R1, R2(c)). The four tests presuppose a defined reading, so they cannot see this. |

**Verdict.** R-SUM and R-IA are four-tested correctly. One grade, R-SUM test 4, is more cautious than the literal test; it is not wrong. Bounded R-GEN is recorded, correctly labelled, and not four-tested for GB1. If the owner considers widening it to GB1, two checks are needed first: the definedness check, which strict R-GEN fails at every irrational `τ_E/π`, and a fresh four-test on GB1's scope. Under that widening, test 3 would be C on the same ground as R-SUM's: the choice of generator fixes E-1, and E-1 fixes the (H-4D) answer (R2(b)).

**The owner question, as it stands after this check.** Which generator reading GB1 uses. The consequences, all on finite boxes:

| Reading | What GB1E then gives |
|---|---|
| R-SUM, `τ_E > 0` | `μ_ex` exists with transfer `e^{−a_0H}`; (H-4D), (H-GI), (H-Haar), (H-RP) in (P8.1) form hold; first failure (H-class) under §2.2's conditions. |
| R-IA, `τ_E > 0` | `μ_loc` exists for every `λ`; same rows; (H-class) fails at every `λ`, including the tree-level isotropic step. |
| Strict bounded R-GEN, widened | No `τ_E` gives a GB1 Hamiltonian with a lift: undefined at every irrational `τ_E/π` and wherever some gate has `−1` in its spectrum; elsewhere bounded, with infinite partition function (R2). |
| Non-strict variant (R3), recorded only | Defined at every irrational `τ_E/π`; equals `H_wr`; infinite partition function (Theorem 5.1). |
| Any reading, `τ_E ≤ 0` | No transfer-kernel lift: bounded generator at `τ_E = 0` (Theorem 5.1); unbounded `e^{−a_0H}` at `τ_E < 0` (Theorem 2.1). |

### 2.5 Scratch check

`/tmp/toe-GB1Eref/check.py`, run with `python3 -I`; 0.13 s; one-dimensional sums only; started at 58 percent free memory. Results: minima of `D_s` for `s = 1, …, 5` on 20001 angles: `−3.0, −2.3333, −10.0, −6.0343, −21.0`. One-link band-limited heat kernel at `s = 1`: minima `−2.9701, −2.7110, −1.7492, 0.1075` at `t = 0.01, 0.1, 0.5, 2`, equal to the closed form `1 − 4e^{−3t/4}`. Heat kernel at the antipode, `t = 1`: `8.82·10^{-3}`. Phase distances in R1 and squares mod 24 in R2(d): as quoted there. The hand values `D_2 = 12c² + 4c − 2` (minimum `−7/3` at `c = −1/6`) and `D_3 = 32c³ + 12c² − 12c − 2` (minimum `−10` at `c = −1`), with `c = cos ψ`, agree. These guide only.

---

## 3. Required edits, open statements, freeze recommendation

### 3.1 Required edits to `GB1E.md`

- **E1** (item 14, line 38). After "Its positive algebra consists of bounded functions of bonds wholly in one open half", add: "A reflection acts on bond variables by `(ϑ·U)_b = U_{ϑb}`, inverted when `ϑ` reverses the orientation of `b`, as in (P8.1)."
- **E2** (item 32, line 107). Replace "Weyl equidistribution for the quadratic sequence `τ_Ek(k+2)/(8π)` gives dense electric phases" by the rebuilt lemma: R1 of `GB1E_REFEREE.md` §2.1 (van der Corput, then a tent function with summable Fourier coefficients), applied with `α = τ_E/(8π)`, `c = α + ½`, `m = k+1`. Credit R1 to this report.
- **E3** (items 28, 33, 66; lines 96, 109, 198). Add closure R2: strict R-GEN widened to GB1 is defined exactly when every gate has `−1 ∉ spec g`. Its generator is then bounded and gauge invariant, and Theorem 5.1 excludes a lift; `τ_E = π/3`, `24|θ| < π` is an instance. Otherwise, including every irrational `τ_E/π`, it defines no Hamiltonian. Replace line 198's last R-GEN sentence by: "Under strict R-GEN widened to GB1, no `τ_E` gives a Hamiltonian with a transfer-kernel lift; the first failing step is the existence of the generator at every irrational `τ_E/π`, and the partition function wherever the generator exists." Add to the R-GEN row of line 96: "Its SMG1 grades were made for finite-dimensional gates; on GB1 it fails the definedness check at irrational `τ_E/π`." R3 may be recorded as a fact, with its four tests, not proposed.
- **E4** (item 65; lines 11 and 198). Add: "T0-start[G] quantifies over every torus side (`GA2_Y2_DRAFT.md` line 211). On a hypercubic torus of even side `N = N_t ≥ 4`, both lifts are measures of the kind it takes. The infinite-volume clause concerns Y1 on `Z³ × Z` and the `Z⁴` wording of `GB1QL.md` line 335." In line 198, state "(H-class) first" with conditions (i)-(iii) of §2.2. Note that with LG1 Theorem 13's mirror set, (H-RP) fails first.
- **E5** (item 59, line 186). Replace "The fixed-volume SU(2) real-time regulator comparison was already proved in `GB1QL.md` Theorems 4.8–4.10" by "The volume-uniform, finite-time SU(2) real-time regulator comparison was already proved in `GB1QL.md` Theorem 4.8 and Corollaries 4.9-4.10".
- **E6** (item 23, after line 88). Add: "`W_E` fixes `τ_E` only modulo `8π`, since `4E²` has spectrum `{k(k+2)}`. Each representative `τ_E + 8πn > 0` gives its own ray; the step `λ` is the one free constant on each ray."

One optional addition changes no verdict: the oddness `Δ(−θ) = −Δ(θ)` of §2.3(e), after line 144.

### 3.2 Open statements, carried by name

- **GB1E-ς.** Is `μ_ex` invariant under exchanging time with a space axis at some nonzero zero of `Δ`? The zero set is discrete and, by §2.3(e), symmetric. Three distinct attacks were tried in this check, and all failed. *(A) More observables.* Exchange invariance forces `Δ_j(θ) = E[χ_j(X_p)] − E[χ_j(X_{p'})] = 0` for every character `χ_j`. Each `Δ_j` is real-analytic, but no argument here shows that their common zero set misses `ℝ∖{0}`. *(B) Convexity.* `θ ↦ log Tr(P_0e^{−N_ta_0H})` is strictly convex, so the mean of `Tr X_p` over `CF` decreases strictly in `θ`. That does not separate the `CF` mean from the non-`CF` mean. No lattice symmetry exchanges the two sets: a translation by `a` flips plane `(i,j)` exactly when `a_i + a_j` is odd, and the three sums cannot all be odd (their total is even); coordinate reflections obey the same parity count. *(C) Spatial Markov property.* Exchange invariance would give `μ_ex` a Markov property across hyperplanes `x_1 = c`, as time slices have. No argument here shows that the kernel of `e^{−a_0H}` breaks it; the Feynman–Kac form of that kernel has local plaquette coupling, so the failure is not evident. Carried, not new.
- **(H-class)** as a decision: `𝒜_{k_0}(g)` and its topology must be pinned (`GA2_Y2.md` line 178). Carried.
- **The reflection interface of the consumer**: (P8.1) or LG1 Theorem 13's mirror set. It decides whether (H-RP) or (H-class) fails first (§2.2). Carried from GAP 2.
- **Y1 on `Z³ × Z`**: no infinite-volume measure is constructed. Carried from GAP 2.
- **T0-start for anisotropic, cube-face starts; Y3 and isotropy restoration; E-2; VC1; T0-rate**. Carried.
- **A volume-uniform form of Theorem 8.3.** Carried.
- **Owner question: which generator reading GB1 uses** (§2.4). If bounded R-GEN is widened to GB1, its definedness at irrational `τ_E/π` must be settled first (R1, R2, R3).

### 3.3 Freeze recommendation

**Freeze `GB1E.md` after edits E1-E6.** Every finite-box theorem in it is correct as stated: Theorems 2.1-3.2, 4.1, 5.1, 6.1, 7.1-7.3 and 8.1-8.3, with the finite-register half of 5.2. The one ERROR (item 59) is a misdescription of `GB1QL.md`. The INCOMPLETE items are filled by closures R1 and R2 and by short insertions. Edits E2 and E3 change what bounded R-GEN is said to give on GB1. They make the R-GEN statement stronger where the reading is defined and replace "obstruction" by "undefined" elsewhere. No edit changes a proved theorem, so a second referee pass is not needed for them.

---

## 4. Prior work used

Paths are relative to this folder unless marked.

- **`GB1E_DRAFT.md`** (pass 1). Lemma 4.2, Lemmas 4.6-4.8, Theorems 4.9-4.10, Lemma 6.2, Theorem 6.3, Lemma 7.1, Theorem 7.3, Theorem 7.5, Theorem 8.2, Theorem 8.4: the full proofs behind `GB1E.md`'s condensed ones. Each was re-derived for items 15-58.
- **`GB1QL.md`** (frozen). §1.1-1.4 (link space, `R_s`, ticks, `ι`); line 209 (`B̃_C = ιB^s_Cι^*`, `‖B̃_C‖, ‖B_C‖ ≤ 24`); Lemma 4.3 (`δ_s(M') = 2M'(M'+3)/(s(s+3))`); the plaquette step of Lemma 4.7 (line 219); Theorem 4.8's scope (lines 259, 303); Proposition 4.11(a) (line 299); Lemma H and the hand-off table (lines 326-343). Used for items 9, 58, 59, 60 and §2.2.
- **`GB1.md`** (frozen). Theorem 2.1 (line 45), Theorem 2.3 (lines 59-63), rows H2 and H5 (lines 209, 212). Used for items 24, 49 and §2.2.
- **`SMG1.md`** Lemma G0 (line 29). Extended from finite to arbitrary dimension in R2(a).
- **`TOE_ASSEMBLY.md`** line 261 (bounded R-GEN, its scope and recorded tests). Used for items 28, 33 and §2.4.
- **`GA2_Y2_DRAFT.md`** line 211 (T0-start[G]) and **`GA2_Y2.md`** line 178 (class unpinned). Used for §2.2.
- **`LW1_5_DRAFT.md`** line 328 (the four tests). Used for §2.4.
- **YM branch**, `library/port/p8-positivity.md` lines 26-48 at `e7a21cd98`: B5's torus, its reflection geometry (P8.1), and T0's weight. Used for items 14, 49 and §2.2.
- **`prior/GB1E.md`** line 38: the quoted mirror set of the YM branch's `library/lg1.md` Theorem 13, used only to state the alternative in §2.2(3). `lg1.md` was not read.

**Prior work the digest missed.** (1) `GB1QL.md` Lemma 4.3: its explicit `δ_s` is what makes Theorem 8.3's strong-convergence step go to zero. (2) `GB1.md` row H2, "The Wilson measure on `ℝ⁴/Nℤ⁴`": with T0-start[G]'s "every torus side", it shows that the hand-off is posed on tori (§2.2). (3) The finite-dimensional scope of `SMG1.md` Lemma G0 ("Let `g` be a unitary on a finite-dimensional space"): the draft applied it to an infinite-dimensional gate, which is the origin of GAP 1.

**Standard mathematics, rebuilt here, credited.** The van der Corput difference inequality and the Weyl equidistribution theorem for polynomial sequences (H. Weyl, 1916; J. G. van der Corput, 1931), rebuilt for squares in R1 in the part needed. Fourier series of the tent function (Fejér's kernel), in R1, Step 3. The spectral theorem and Borel functional calculus for bounded self-adjoint operators, in R2 and R3. Credited from memory, not load-bearing: Osterwalder–Seiler for link-reflection positivity of lattice gauge measures; Lüscher for positive transfer matrices.

---

## FINISH

**Proved** (by this check; not yet used by any frozen file).
- Every finite-box theorem of `GB1E.md` was re-derived and is correct: Theorems 2.1, 2.2, 3.1, 3.2, 4.1, 5.1, the finite-register half of 5.2, 6.1, 7.1, 7.2 (including draft Theorem 7.5), 7.3, 8.1, 8.2, 8.3. In particular: under R-SUM with `τ_E > 0`, on every finite periodic 4D box (`N ≥ 4`, `N_t ≥ 2`, both even), there is a gauge-invariant `SU(2)` link probability measure with bounded Haar density, transfer matrix exactly `e^{−a_0H}`, and link-reflection positivity in all four coordinate directions.
- R1: for irrational `α` and any `c`, `αm² − c` comes within any `ε` of `ℤ`; hence `−1 ∈ spec e^{−iτ_EE²}` for every irrational `τ_E/π`.
- R2: Lemma G0 holds in any dimension. Under strict bounded R-GEN widened to GB1, no `τ_E` gives a Hamiltonian with a transfer-kernel lift: the reading is undefined wherever some gate has `−1` in its spectrum (every irrational `τ_E/π` among them), and elsewhere its generator is bounded and gauge invariant, so Theorem 5.1 applies (instance `τ_E = π/3`, `24|θ| < π`).
- R3: if `−1` is not an eigenvalue of `g`, exactly one Hermitian `X` with `‖X‖ ≤ π` has `e^{−iX} = g`.
- `Δ(−θ) = −Δ(θ)`.

**Counterexamples.**
- To the draft's Proposition 3.2(a), "Every gate of `U_KS` … has a principal generator" at irrational `τ_E/π`: `τ_E = 1` (R1; `[check]` distances to `π` reach `6.3·10^{-6}` at `k ≤ 10^5`).
- To the reading of `GB1E.md` line 198 that strict R-GEN cannot give the partition obstruction: `τ_E = π/3`, `24|θ| < π` (R2(d)).
- To `GB1E.md` line 186's "fixed-volume": `GB1QL.md` line 303, "uniformly in the volume and in `n ≤ T`".
- To the draft's "the framework at fixed `s` supplies a probability measure through its own registers" as a general claim: not a counterexample. Theorem 8.1 excludes only the embedded group-variable kernel; `GB1E.md` line 170 says so.

**Open by name.** GB1E-ς (three attacks failed: more observables, convexity, spatial Markov property); (H-class) with its class and topology; the consumer's reflection interface; Y1 on `Z³ × Z`; T0-start for anisotropic cube-face starts; Y3; E-2; VC1; T0-rate; a volume-uniform Theorem 8.3; the owner question on GB1's generator reading.

**What changes downstream.**
- `GB1E.md`: freeze after edits E1-E6 (§3.1).
- GB1-H and the hand-off order: in T0-start[G]'s own torus form, with (P8.1) reflections and a hypercubic class, the first failing input under R-SUM is (H-class), at time–space exchange invariance. With LG1's mirror set it is (H-RP). On `Z⁴`, and for Y1 on `Z³ × Z`, it stays (H-4D).
- The owner's bounded R-GEN, if widened to GB1, gives no Euclidean lift for any `τ_E`. At irrational `τ_E/π` the reason is that it defines no Hamiltonian, not that a partition function diverges. Widening it would need a definedness decision (strict or non-strict bound) and a fresh four-test.
- SMG1: Lemma G0 holds in any dimension (R2(a)). This changes no SMG1 result.
