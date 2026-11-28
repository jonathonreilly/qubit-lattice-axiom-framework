First failing step: none.

# cl1-gate: pass-3 referee check of `library/cl1.md`

Referee: Claude Opus 5.5 (`claude-opus-5-5`), fresh session, 2026-11-05. One reading by one other model of a Codex distillation. This is not an audit and grants no status. Every step was redone by hand. No computation was used as a proof step.

Credit: the arguments rebuild Ethan Sussman and Levent Alpoge's outline and YM3_I (with Claude and Codex as the authors of their text), at `31a47c543775`.

## What was read

- `library/cl1.md`, whole, line by line, once.
- Its sources: `library/s4-s6.md` and `library/cone-o6.md`, whole. Their gate: `gates/bridge-check.md` §§2–3, with its corrections (box sizes, overlap step, momentum sign).
- The CL1 entry of `library/ym4-assembly.md` §§4–5, and the LG1, IN1 and SR1 entries there.
- Imports: `library/sr1.md` (refereed in `gates/sr1-gate.md`), `library/lg1.md` (Theorem 10, Theorem 13), `library/in1.md` (constant order, Theorem 12, Amendment 1).
- SA outline `scratchpad/sa/ym4.tex` (sha1 prefix `107abaef`): L6895–6945 (centred functional, Theorem 0(a), (b)), L24651–24720 (CC8–CC10), L24917–24990 (QF1–QF3), and label searches in L24376–24470 (CC1–CC2), L25736–25962 (HB8–HB16).
- YM3_I `scratchpad/sa/YM3_I.tex`: L74440–74490 (IV-21-28/33), L75425–75580 (sh_b, IV-28-12/15, IV-28-17, IV-28-21), label positions of IV-10-25/28, IV-24-15, IV-27-22.

The CA-II row of the source table (L500) was not re-read. It is outside the requested texts, and cl1 says it supplies no premise.

## Check by statement

**Definitions (L7–55).** (1) matches the assembly and SA (0a): six orientations, no spacing prefactor. The DLR class, the torus-limit class, first-passage data and the two orders of limits match SA Theorem 0(a)(iii) (L6915). (3) is SA's centred functional σ_S (L6897). E_{+,n} equals sr1's S_{≠,+,n}: smoothness forces flatness on the zero-time boundary.

**Imports (L57–95).** I1 uses IN1 Theorem 12 only for nonempty W_K(g) at unbounded K and g⁻² < x_K ≤ g⁻² + B_♯. I2 is LG1 Theorem 13.5 (aZ⁴ ⋊ W₄, coordinate site, coordinate bond and diagonal mirrors, with diagonal heights in aZ). I3 is SR1 Theorem 1 clauses 1–4. Complexification costs 2ⁿ, so B → 2B. The order table abbreviates IN1's rows with Amendment 1.

**Lemma 1.** Compact metric product, separability of C(X), Riesz limit, DLR identity on large tori with a kernel denominator ≥ e^{−2β|P(W)|}, properness, and weak passage of aZ⁴ and W₄ invariance (the cubic torus is W₄-symmetric). Correct; this is SA CC1–CC2.

**Lemma 2.** (5): squarefree exponential of the cumulant polynomial; the r! cancels. Only singletons change under centering. The position-independent bound M_n(d,R) follows from I3. Separability of supported C¹ spaces through C(Q)⁵, the countable diagonal extraction, telescoping (6) in fixed containers, and the Cauchy argument through a fixed approximant are correct.

**Lemma 3.** (7) is SA (CC9). Rounded mirrors: b_j ∈ a_j(Z+½) for x_μ = b and b_j ∈ a_jZ for x_μ ± x_λ = b; the offsets 2(b_j−b)e_μ and (b_j−b)(e_μ±e_λ) follow from θ_c x = x − 2(n·x−c)n/|n|². This matches SA L24683–24692 and LG1 clause 5. (8) uses lattice RP, centering covariance from ν_j's reflection invariance, and moving tests. (9): δ_j is plaquette-independent because aZ⁴ ⋊ W₄ is transitive on plaquettes; m_{j,1} = c_jR_j holds exactly; the Riemann error is C(R+1)⁴a_j‖∇f‖_∞ (side-a cube diameter 2a). c_j → c and |c| ≤ C₁(R_*)‖f_*‖_♯. (10): log coefficient (r−1)!. (11) and its identification with (3) are correct. RP of σ_S uses the self-centered pair (ρ_j, ρ_j).

**Lemma 4 (4D Fourier counts).** Inner side 2ℓ, expanded side 4ℓ, period 8ℓ (the bridge-check §2 choice). Four applications of 1 − π⁻²Δ per four-dimensional slot: 8 derivatives per slot, 8n in total, and decay Π(1+|v_i|²)⁻⁴. Cut-off modes have C¹ norm ≤ Cℓ⁻¹(1+|v|). The Z⁴ shell has O(r³) points against O(r⁻⁷), so the sum converges. (14): (h/2)⁻⁵ⁿ times (64/h)ⁿ gives h⁻⁶ⁿ. Grid boxes: expanded distance ≥ h_r − 6ℓ_r > h_r/2. (15): Taylor segment ≤ 8h_r, Taylor order 10n+2 after at most 8n, so 18n+2 ≤ 20n. Positions: (1+Σ|x_i|²)⁻¹⁰ⁿ ≤ Π(1+|x_i|²)⁻¹⁰ and O(ℓ_r⁻⁴) per slot, so h_r⁻⁴ⁿ; radial tail ∫r⁻¹⁷dr. Net h_r^{10n+2−6n−4n} = h_r². Density, positive-time density and convergence of the lattice extensions on the flat space are correct.

**Lemma 5.** Positivity, Hermiticity and the quotient are correct. Symmetry of normal translation follows from θ_uτ_{tu} = τ_{−tu}θ_u. The cross-distance identity |y−x+ru|² = |y−x|² + 2r u·(y−x) + r² ≥ |y−x|² is correct, so (4) bounds a_F(t). (18) gives contraction. Strong continuity, ker T₁ = 0 by halving, H_u = −log T₁, dense domain, T_t = e^{−tH_u}, the joint spectral theorem, the convention U_x = e^{ix·P} in (17), the W₃ action and separability are correct. This matches s4-s6 §5 and YM3_I IV-27-22.

**Lemma 6.** Cross-diagonal flatness, (20), convergence of the finite forms by (12) and (20), positivity from Lemma 3, and the bridge by common mollification are correct. sh_b agrees with YM3_I (IV-28-13) under A ↔ A^c. sh_b sh_{b′} = sh_{b+b′} is correct. By (11), σ_S = σ ∘ sh_{−c}; with IV-28-15 this gives the vacuum-fixing unitary that intertwines translations.

**Lemma 7.** Fubini bound |e^{−sw−s′w̄}| = e^{−(s+s′)E/√2} ≤ 1. The identity ∫c̄(s′)e^{−is′y}ds′ = p^♯(y) is correct. The Gauss limit for Γ(α), its nonvanishing (H_N − log N decreasing and ≥ 0; |log(1+z) − z| ≤ |z|² for |z| ≤ ½), the two suprema η^{−ε} and η^{−ε}e^{|κ|π/2}, the two Fatou steps, and the sector argument are correct. This matches YM3_I IV-28-17 (L75480–75530) step for step.

**Lemma 8.** r(x_i, x_4) = (x_4, −x_i), so W_i and rW_i lie in {u·x > 0}. (27): su + s′v = ((s+s′)e₄ + (s−s′)e_i)/√2; with w = (E − ip_i)/√2 the exponent is −(s+s′)E/√2 + i(s−s′)p_i/√2, which matches U_x = e^{ix·P}. θ_u r = θ gives the second representation. Every concatenation is separated. The time shift into W_i, commutation and injectivity of T_R, and (28) are correct. This matches YM3_I IV-28-21 (L75532–75576), with three spatial generators.

**Theorem 9** matches the CL1 entry of the assembly. Clause 2 states RP for σ_S (and σ), which is SA (0b)(ii)'s form. The finite-torus realization (29) is correct: at most N_j^n index tuples, each within 1/(j·max(1,N_j)^j), so the error is ≤ Π‖f_i‖_∞/j for 2 ≤ n ≤ j. This is YM3_I IV-21-28/33 (L74451–74485) without the a_K⁻ⁿ prefactor, as the text says.

## Findings

1. **L208 (Lemma 4, last sentence; also L273).** "I3 improves A′_n to C_E^n(n!)^{k+32}, enlarging C_E for cumulants if necessary." I3 imports SR1's H1, which SR1 states for the moment limits (7). It covers σ and σ_S (σ_S is (7) with ν_j = ρ_j). It does not state the factorial bound for the cumulant limits S_n, n ≥ 2, or for the lattice extensions Σ_{j,n}. **Repairable; not fatal.** No clause of Theorem 9 uses this bound for S_n or Σ_{j,n}. Repair: say that SR1's Lemmas 7–9 use only an admissibly multilinear consistent form with bound (28). The cumulant limits satisfy (28) with b₀ replaced by a constant times 2B(1), by the third line of (4); the lattice forms satisfy it at each j. SA (QF1) (L24929–24946) states this hypothesis and needs no invariance or positivity.

2. **L74, L88, L93 (notation).** The symbol C_E names both SR1's H1 growth constant and IN1's row-7 constant C_E (in1.md L233), which the order table retains. The letter c names both IN1's reserve product c = C_v c_r (table row 7, L88) and the one-point constant of Lemma 3. No step confuses them. **Repairable, wording only.** Repair: rename the growth constant (for example C_{H1}) and the one-point constant (for example c_σ).

No other defect was found.

## Verdict

ADVANCE. `library/cl1.md` proves CL1 as an implication from SR1, LG1 and IN1(4) in the forms I1–I3: volume-first limits that exist and are limits of SA 0(a)(iii) type, all coordinate and diagonal affine mirrors, off-diagonal distributions of locally finite order, the identification of the compact and diagonal-flat Hilbert spaces (with recentering), and H ≥ |P_i| with the cube cone. The 4D counts are right: eight derivatives per slot, h⁻⁴ⁿ positions, Taylor order 10n+2, net h². Each lemma matches its source note and keeps the gate corrections. The main theorem matches the CL1 entry of the assembly. The upstream construction inputs stay Outstanding, as the text says.

Checked line by line by Claude (fresh session).
