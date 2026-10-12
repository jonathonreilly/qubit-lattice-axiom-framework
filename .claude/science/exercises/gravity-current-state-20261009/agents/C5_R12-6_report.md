# C5 R12-6 report: the twisted N=4 Kähler–Dirac gauge multiplet on Z³ × ℝ with charged box matter

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 19:37Z to about 20:20Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R12-6/`. Scripts and outputs are in `S/scripts/`. Each runs in under 4 min with `OMP_NUM_THREADS=2` (most under 60 s).
- `r126_free_cartan.{py,out}`: the free (quadratic) content of the equivariant law; Kähler–Dirac photino; boson/fermion count; doubler scan; λ-family.
- `r126_pauli_photon.{py,out}`: the selectron Pauli term forced by the Q-exact matter coupling; the one-loop photon speed; the B-coupling repair.
- `r126_electron_loops.{py,out}`: one-loop electron speed from the full partner sector (η + all photino link components + σ); R12-3 control.
- `r126_repaired_loops.{py,out}`, `r126_mscan.{py,out}`: the same for the B-repaired law; mass scan.
- `r126_mscan2.{py,out}`: a memory-sliced rerun of the matched-curve 𝒦₀ total down to m = 0.025 (N ≤ 256).
- `r126_algebra_check.{py,out}`: symbolic operator check of Q² = iσL and of every listed term of {Q, Q†}, on a minimal gauged toy, with negative controls.
- `r101_pairing.py`, `r85_box_qed_copy.py`, `r123_bf_multiplet.py`: unmodified copies of the R10-1, R8-5 and R12-3 helpers.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: the C5 method (`:2302-2320`), the R10/R11 referee results (`:4268-4331`), R12-3 (`:4373-4390`), R12-6 (`:4490-4507`).
- `agents/C5_R12-3_report.md` (all), and its referee verdict, which appeared during this run: `scratchpad/C5/ref_R12-3/REFEREE_VERDICT.md` (CONFIRMED WITH CORRECTIONS, INCONCLUSIVE) and `R12-3_referee_verdict.md`.
- `agents/C5_R10-5_report.md`, `C5_R10-5_referee.md`, `C5_R10-5_referee_verdict.md`; `agents/C5_R10-1_referee_verdict.md`; the R8-5 and R10-1 helpers.
- `scripts/C5/R12-3/r123_partner_loop.py` (reused as a control).

**Labels.** proved / checked / suggested / reading / comparator (V = verified this session or by a C5 referee; R = recalled).

---

## 0. In plain words

1. **The local law exists.** R12-3's charged BF law was non-local because its photinos were forced to be "horizontal". Building the gauge multiplet the equivariant way removes that. Add a complex site scalar σ and a site fermion η, and use the supercharge
   Q = Σ ψ†(p − i∂W) + i Σ_s σ_s (v_s·ψ) + c Σ_s η_s π_σ̄,s.
   - Then Q² = i Σ_s σ_s L_s, where L_s is the Gauss generator. So Q² = 0 on gauge-invariant states.
   - H = ½{Q, Q†} is a sum of local (box symbols: quasi-local) terms, and it is ≥ 0.
   - Proved by hand algebra, and checked symbolically on a minimal gauged toy (§3.1).
   - Its free photino is exactly the Kähler–Dirac operator. That operator is doubler-free and untwistable to spin ½.
   - The free spectrum is 8 bosons and 8 fermions per momentum, all at ω² = Δ (checked).
   - So (a) and (b) are **yes** for the free gauge multiplet.
2. **The supercharge does not fix the electron–photon split, and N=4 does not change that (Theorem L′, proved).**
   - Scale the gauge part of W by λ and set c = 2λ. Every member of that family keeps the same exact Q, the same Q², the Ward identity, locality and the Kähler–Dirac photino.
   - At tree level, c_γ = λ and c_e = 1.
   - Any supercharge that commutes with gauge charge maps the photon sector and the electron sector to themselves.
3. **The Q-exact matter coupling has a built-in, in-box Lorentz violation (proved; checked).**
   - The electron's operator must be the Hessian M_A. The selectron's energy is then ½|M_Aφ|². That contains a magnetic-moment (Pauli) coupling of the selectron to the magnetic field, with no electric partner.
   - Result: the photon's one-loop speed shift is δc_γ = −e²⟨|c′_x|²|c′_y|²/E³⟩. This → −(e²/2π²) ln(1/m) inside the box.
   - Checked: slope −8.0 per unit ln(1/m), in units of e²/16π², for the Wilson curve and for two box curves.
   - So R12-3's "δc_γ = 0 (matter loops cancel)" is wrong for the Q-exact law. Theorem P covered minimally coupled scalars only.
4. **The "dressing terms" R12-3 left out are now computed (checked).** They are η, the longitudinal photino and the σ loop.
   - For matched curves they cancel to zero among themselves. So they cannot remove the electron's infrared log.
   - The full one-loop partner contribution to the electron still grows like about −2 ln(1/m).
   - The split therefore carries an in-box term of about +6 ln(1/m) e²/16π². Taken at face value at a = ℓ_P, that is about +0.2 (reading).
5. **A repair, and where it stops.**
   - Coupling the selectrons to the BF partner B, with N_B = −e Σ B_jk A_jA_k J, cancels the photon's Pauli log exactly inside the box. That cancellation is proved; the leftover is an m-independent edge term (checked).
   - But it gives the electron a spin coupling to B, and the electron's infrared log returns, larger: about −1.9 to −2.2 per halving of m (checked).
   - A covariant completion would plausibly also need τ, the φ₀ partner. That is not built.
6. **The six scalars (d).**
   - In this law only σ (2 real) couples to the electron at O(e), with Yukawa √2 e. B couples only to selectron currents, or to the electron's spin after the repair. τ decouples.
   - A massless σ at that strength is excluded (comparator R).
   - σ is a flat direction of {Q, Q†}, so giving it a mass breaks Q.
7. **Against the FIXED readings.**
   - **PASS: not met.**
   - **Worker reading: FAIL (bounded) on the split, in the minimal-coupling Kähler–Dirac class 𝒦₀.** Theorem L′ shows the split is not protected. The Pauli theorem plus the computed electron log show it does not vanish (in-box Lorentz violation).
   - For the B-coupled completions (𝒦_B, and τ-coupled ones) the reading is **INCONCLUSIVE**.
   - Locality and spin give no no-go: both are met at the free level.
   - Referee required.

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat.** Z³ × ℝ, continuous time. Translations and the proper cubic group (`AX:37-41`).
  - Symbols are C¹ and periodic: the cochain D_j = e^{iq_j} − 1, or R8-5's box symbol D_j = i d(q_j)e^{iq_j/2}, plateau (1, 2).
  - Matter is R10-5's Clifford-flat multiplet, complexified (Lemma J, onsite charge): 16 real CCR plus 16 CAR per site. M(k) = Σ_j[S(k_j)A_j + W(k_j)B_j] + mB₀ (`C5_R10-5_report.md:128-145,158-161`).
  - Curves: the Wilson circle (sin k, 1 − cos k), and the unit-speed box curves b₁ = 0.8 and 0.5 from R10-1.
  - Masses matched; one loop.
- **Class 𝒦 (equivariant gauged SUSY-QM).**
  - Real coordinates x = (A on links, B on plaquettes, τ on cubes, φ on sites), one complex fermion per coordinate, plus per site a complex σ (with momenta) and a complex fermion η.
  - An abelian gauge group acts by affine isometries v_s, with W real and invariant: v_s·∂W = 0.
  - Q as in §0.1. Physical states satisfy L_s|ψ⟩ = 0.
- **𝒦₀ ⊂ 𝒦 (minimal coupling).** W = λ(⟨B, dA⟩ + ⟨τ, dB⟩) + ½⟨φ, M_Aφ⟩. M_A is the Peierls-dressed M. No B- or τ-dependent matter term.
- **𝒦_B ⊂ 𝒦.** As 𝒦₀ plus ½⟨φ, N_Bφ⟩, with N_B linear in B (§3.4).
- **Untwisting (H-tw)** as in R12-3 (`C5_R12-3_report.md:84`).
- **Excluded, not addressed:**
  - Euclidean or A₄*/hypercubic Q-exact lattices (set B);
  - non-abelian gauge groups and compact links;
  - two loops;
  - light-cone supercharges;
  - laws whose electron one-particle operator is not the Hessian of W;
  - τ-coupled completions.

## 2. Prior art (each counted once)

- **R12-3** (referee CONFIRMED WITH CORRECTIONS, INCONCLUSIVE; `ref_R12-3/REFEREE_VERDICT.md`):
  - the BF multiplet, c₁ = 0, the Ward identity;
  - "local equivariant completion unbuilt";
  - Theorem L is valid only for the single Nicolai Q;
  - PD₁ and PD₂ are narrowed;
  - Catterall hep-lat/0503036 is hypercubic (V via referee);
  - KKU shows that spatial-lattice SUSY plus lattice symmetry can constrain tuning (V via referee).
- **R10-5** (CWC, FAIL bounded to 𝒮):
  - Theorem Q (`C5_R10-5_report.md:128-145`);
  - Lemma J, onsite (`:158-161`);
  - "Q relates partners only, not c_e and c_γ" (`:185-188`).
- **R10-1** (CWC): Theorem P, the photon cancellation for *minimally coupled* scalars; the paired electron residual −17.96 (Wilson) and −10.66 (box) at N = 224 (`C5_R10-1_referee_verdict.md:9,17`).
- **R8-5** (CWC): the box photon; Peierls vertices.
- **Lemma R** (`TESTS.md:1172`); its narrowing at `TESTS.md:140`.
- **Comparators.**
  - Groot Nibbelink–Pospelov hep-ph/0404271 (V via the R10-5 and R12-3 referees: it assumes the standard supercharge–translation algebra).
  - The 3D N=1 → 1D reduction / Cartan model of equivariant cohomology (R).
  - Seiberg–Witten–Floer: the Weitzenböck/Pauli cancellation in CSD (R).
  - Light-scalar contribution to the electron g−2, Δa_e ≈ (3/2)g²/8π² for m_σ ≪ m_e (R).

## 3. Results

### 3.1 The local equivariant law (answers (a)). Proved (hand algebra); checked symbolically on a toy; lattice quadratic part checked

**Definitions.** Coordinates x^a with momenta p_a, and fermions ψ_a. The gauge vector fields v_s(x) = T_s x + c_s are affine, with T_s antisymmetric (on φ: T_s = eJ at site s; on A: c_s = d₀δ_s). The abelian conditions are [v_s, v_t] = 0 and v_s·∂W = 0. Take σ_s complex with [σ_s, π_σ,s] = i, and fermions η_s.

**Supercharge.**

Q = Σ_a ψ_a†(p_a − i∂_aW) + i Σ_s σ_s (v_s^aψ_a) + c Σ_s η_s π_σ̄,s.

**Step 1: Q² = i Σ_s σ_s L_s, with L_s = v_s·p − iψ†T_s^Tψ.**
- {ψ_a†G_a, v_bψ_b} = ψ_a†ψ_b[G_a, v_b] + v_aG_a = v·p − iψ_a†(∂_av_b)ψ_b, using v·∂W = 0 and tr T = 0.
- Every other anticommutator in Q² vanishes:
  - ψψ and ηη terms square to zero;
  - [π_σ̄, σ] = 0;
  - G_a is independent of σ.
- On physical states, Q² = 0.

**Step 2: [Q, L_s] = 0.** Each term is gauge covariant, and the vector fields commute.

**Step 3: H = ½{Q, Q†}.** It contains:
- ½(p² + |∂W|²) + ψ†Hess W ψ (standard);
- ½|σ|²|v|². This is |d₀σ|² on the links, and e²|σ_s|²|φ_s|² on matter.
- (|c|²/2)|π_σ|²;
- ½[c (v_s·ψ†)η_s + h.c.]. This is the hopping ψ_A†(d₀η) plus the η–selectron–electron Yukawa e(Jφ_s)·ψ_s†η_s.
- −½σ̄_s(∂_av_b)ψ_a†ψ_b† + h.c. This is the σ–electron Yukawa ½eσ̄ψ†Jψ†.

**Properties.**
- H ≥ 0 on the whole Fock space, since ⟨{Q, Q†}⟩ = ‖Q†ψ‖² + ‖Qψ‖².
- Every term is a product of local densities, so the law is local: nearest-neighbour for cochain symbols, quasi-local for box symbols and box curves.
- The Ward identity holds. Checked: Σ_j D_jΓ_j = −ie[M(p) − M(k)] to 5.0e-16 (`r126_electron_loops.out:1`).
- This corrects R12-3's locality caveat (`C5_R12-3_report.md:159-162`). The non-locality came from the horizontal restriction, and the η–σ completion removes it.

**Checked symbolically (`r126_algebra_check.out`).**
- Toy: two links, one charged site, complex σ, η, with a cubic gauge-invariant W.
- Acting on generic test states (undefined functions of all coordinates), Q² − iσL ≡ 0, and {Q, Q†} equals the listed terms exactly.
- Negative controls fail as they should: a wrong η-hopping coefficient fails, and dropping the iσv·ψ term gives Q² = 0 ≠ iσL.
- The identity uses only [x, p] = i, the CAR, linearity of v and invariance of W, so the lattice law is an instance.

**Checked, lattice quadratic part (`r126_free_cartan.out`).** With c = 2λ:
- The assembled photino operator on (η, ψ_A, ψ_B, ψ_τ) equals R12-3's C_kd exactly. K² = λ²Δ·1₈ to 3.6e-15.
- 6 physical gauge bosons (A_T, B, τ) plus 2 real σ give 8 oscillators. 8 fermion levels. All at λ²Δ (to 2.7e-14).
- Doubler scan, box symbol, N = 24: the smallest level 0.2267 sits at the grid point nearest 0. For |q| > 1 the minimum is 1.0055.
- Inside the plateau, every level equals |q| to 12 digits.

### 3.2 (b) Photino spin and doublers. Checked (free); interactions not shown untwistable

- K = d + d†, so K² = Δ: zeros only at q = 0, doubler-free.
- The twisted helicities per band are {+1, 0, 0, −1}, which untwist as 2 × (½ ⊗ ½_R). This is from R12-3, confirmed by its referee (`C5_R12-3_report.md:192-200`).
- This is a free-level statement. §§3.3–3.5 show that the matter couplings of 𝒦₀ and of the tested 𝒦_B are **not** Lorentz invariant inside the box. So the interacting law does not untwist to a Lorentz-invariant theory.

### 3.3 The selectron Pauli term and the photon (part of (c)). Proved for 𝒦₀; checked

**Claim.** In 𝒦₀ the selectron potential is ½φM_A²φ, with M_A² = E_A² + Pauli:
- E_A² is R10-1's minimally coupled scalar;
- the Pauli part has continuum form (e/2)Σ_{j<k}F_jkA_jA_kJ.

For a static A_y = a cos(qx):
- K₁ = K₁^scalar − (e/2)Δ_xG, with Δ_x = [S(k_x+q) − S(k_x)]A_x + [W(…) − W(…)]B_x and G = S′(k_y)A_y + W′(k_y)B_y;
- K₂ on the diagonal equals K₂^scalar;
- the cross term is traceless.

The second-order vacuum energy then gives the exact one-loop result

  **δc_γ^Pauli = −e²⟨|c′(k_x)|²|c′(k_y)|²/E³⟩ = −e²⟨1/E³⟩ for unit-speed curves → −(e²/2π²)[ln(2Λ/m) − 1].**

**Why this is in-box Lorentz violation.**
- The Pauli vertex couples only to curl A, so Π₀₀^Pauli = 0 while Π_T^Pauli = −q²χ ≠ 0.
- A Lorentz-invariant Π^{μν} = (q²g − qq)π cannot have that pattern.
- The minimal scalar and Dirac loops are separately Lorentz invariant inside the box. So nothing in 𝒦₀ cancels this term at one loop.
- No B–photon mixing arises at one loop: the traces of products of distinct generators vanish.

**Checked (`r126_pauli_photon.out`).**
- The decomposition holds: K₁ to 1e-16, K₂ to 2e-8.
- The second-order formula agrees with finite differences to 1.6e-5 relative.
- The finite-q values −34.39, −34.24, −33.67 approach the q → 0 formula, −34.44 (box, m = 0.3).
- Mass scan, ×16π²/e², q → 0:

| curve | m = 0.4 | 0.2 | 0.1 | 0.05 | 0.025 | slope d/d ln(1/m) at the smallest m |
|---|---|---|---|---|---|---|
| Wilson | −20.84 | −26.75 | −32.41 | −38.00 | −43.55 | −8.02 |
| box b₁ = 0.8 | −31.51 | −38.16 | −44.00 | −49.62 | −55.19 | −8.03 |
| box b₁ = 0.5 | −25.00 | −31.14 | −36.85 | −42.44 | −48.00 | −8.01 |

- The continuum prediction is −8. Values are N-stable to 1e-3.
- Size (reading): −(α/4π)·8 ln(1/(m_e a)) ≈ −0.24 at a = ℓ_P (m_eℓ_P ≈ 4e-23). This needs no edge at all.

**Correction to R12-3.** Its §3.6 "δc_γ = 0 (R10-1 Theorem P)" (`C5_R12-3_report.md:220-224`) does not hold for the Q-exact law. Theorem P assumed minimally coupled scalars, and the Q-exact selectron is not one.

### 3.4 The B-coupling repair (𝒦_B). In-box cancellation proved; residual checked

- With W ⊃ ½⟨φ, N_Bφ⟩ and N_B = κΣ_{j<k}B_jkA_jA_kJ, the cross term of ½|∂_BW|² = ½|λdA + ½φ(∂_BN)φ|² is λκ/2·F_jk φA_jA_kJφ.
- κ = −e/λ cancels the Pauli term exactly in the continuum. N_B is real symmetric because A_jA_kJ is.
- With a site-local N_B (form factor 1) the leftover is −2e²⟨(1 − S′_xS′_y)/E³⟩. It is m-independent and edge-only:
  - −31.39 (Wilson);
  - −55.12 (box 0.8);
  - −38.65 (box 0.5).
- **Suggested:** a divided-difference (Ward-form) N_B kernel would cancel it at one loop as well.
- With the repair, the one-loop photon is Lorentz invariant inside the box (Theorem P plus the cancellation; checked as the m-flat residual).

### 3.5 The electron's one-loop partner sector, including R12-3's omitted dressing (part of (c)). Checked

**Vertices.** Derived from W and the Cartan term in my Fourier convention:
- Γ_j^a = −ie[h_j(p) − h_j(k)]/D_j (Peierls divided difference);
- Γ^η = ie·1;
- σ: √2 ie s̄ψ₊†χ with χ = ψ₋† (particle–hole), whose one-particle operator is −M.

The photino propagator uses the full Kähler–Dirac projectors ½(1 ± K/w). The method is R10-5's normal term plus Z term (referee-confirmed). The control (transverse only) reproduces R12-3's table exactly: −8.875, −9.008, −9.876, −10.125 (Wilson) and −9.562, −9.694, −10.563, −10.812 (box).

| law (×16π²/e²) | Wilson e / cochain photino, m = 0.4 / 0.2 / 0.1 | box 0.8 / box photino, m = 0.1 / 0.05 (N = 64 / 80) |
|---|---|---|
| 𝒦₀ total (η + all a + σ) | −6.30 / −7.71 / −9.09 (N = 64 / 96 / 128); m = 0.05: −10.44 (N = 160); m = 0.025: −11.76 (N = 256) | −8.81 / −9.92 |
| of which σ | 0.000 / 0.000 / −0.001 | −2.83 / −2.94 |
| 𝒦_B total (η + a + b + σ + B) | −23.97 / −26.15 / −28.01 | −25.95 / −27.12 |

**Findings.**
- **For matched curves (Wilson e and cochain photino), the dressing sector sums to zero.** (η, longitudinal photino, σ) together contribute nothing: KD + σ = T to ≤ 1e-3 in all four rows, and σ alone → 0 with N.
  - The reason: the longitudinal photino couples with −ie[M(p) − M(k)]/w (Ward), η with ie, and (η, ψ_L) forms a w-paired doublet. The combination then depends only on w and E.
  - For mismatched curves (box) it does not vanish: σ ≈ −2.9.
- **The infrared log survives.** In 𝒦₀ the matched-curve total (N-converged to about 0.04) grows by −1.41, −1.38, −1.35 and −1.32 per halving of m, from m = 0.4 to 0.025. That is −1.9 to −2.0 per unit ln(1/m) (`r126_mscan.out`, `r126_mscan2.out`). It is in-box Lorentz violation in the photino–selectron–electron Yukawa, not a missing piece.
- In 𝒦_B the photino part flattens (−9.83, −10.70, −11.44), but the B loop grows (−14.14, −15.45, −16.57). The total grows by −2.2 and −1.9 per halving.
- **Scope.** The B-loop has slow N-convergence (about 0.1–0.3 per N step). The m = 0.05 box and 𝒦_B rows (N = 80) are under-resolved. The log coefficients are fits (checked as trends, not proved).

**The split, at one loop.**
- In 𝒦₀: c_e − c_γ = (−17.96 or −10.66, photon loop, R10-1, refereed) + (partner, about −6 to −9 at these m) − δc_γ^Pauli.
- The in-box parts are about −2 ln(1/m) for the electron and −8 ln(1/m) for the photon, so the split contains about +6 ln(1/m) e²/16π².
- Reading: about +0.2 at a = ℓ_P, if a one-loop log fit is extrapolated over 50 e-folds. Either way it is nonzero and IR-enhanced, not edge-suppressed.

### 3.6 (e) Theorem L′: the extended (N=4 / equivariant) structure does not relate c_e and c_γ. Proved in 𝒦

**(i) The family.** For every λ > 0 and c = 2λ:
- W_λ = λW_BF + W_matter (plus N_B with κ = −e/λ in 𝒦_B) is in the same class;
- Q² = iσL is independent of (λ, c), by §3.1, Step 1;
- gauge invariance, the Ward identity, locality and the Kähler–Dirac photino (K → λK) all hold;
- c_γ = λ and c_e = 1 at tree level.

Exact Q and the cubic symmetry therefore leave the relative speed as a free marginal parameter. This answers the R12-3 referee's KKU point: the lattice symmetry fixes one speed per multiplet, not the ratio between the vector multiplet and the charged multiplet.

**(ii) Charge sectors.** Any further exact supercharge must commute with the Gauss generators to act on physical states. It therefore preserves electric charge, and it relates only same-charge states:
- E_e = E_ẽ;
- E_γ = E_γ̃.

The N=4 supercharges that relate the photon to the adjoint scalars stay inside the neutral sector.

**(iii) Momentum in the algebra (suggested).** A GNP-type cross-sector constraint needs a sector-universal momentum in {Q, Q′†}. On Z³ × ℝ the spatial generators are discrete. An additive C¹ substitute is excluded by Lemma R in the class where Lemma R holds (`TESTS.md:140,1172`).

**Answer to (e): no.**

### 3.7 (d) Neutral scalars and their masses

**Which scalars couple at O(e).**
- In 𝒦₀ only σ (complex: 2 real) couples to the electron, through the σ Yukawa √2 e, and to the selectron through e²|σ|²|φ|².
- B couples to the selectron current via ⟨d†B, j⟩ from ½|∂_AW|², not to the electron at tree level.
- τ decouples.
- So R12-3's "6 massless scalars with O(e) Yukawas" (`C5_R12-3_report.md:54,254`) is corrected to 2 for 𝒦₀. In 𝒦_B there are 5: B gains a spin Yukawa.

**Exclusion (comparator R).** A massless scalar with g² = 2e² gives Δa_e ≈ (3/2)(α/π) ≈ 3.5e-3, against agreement at about 1e-12. It also gives a long-range force between electrons of Coulomb strength.

**The price of a mass.** About m_σ ≳ 10² GeV is needed (reading, from the decoupling (m_e/m_σ)² ln).
- σ is a flat direction of H = ½{Q, Q†}: its potential is ½|σ|²|v|², which vanishes at φ = 0 for uniform σ (the Coulomb-branch modulus).
- So a σ mass is not of {Q, Q†} form in 𝒦 (suggested), and it breaks Q softly.
- That brings back O3's vacuum residual and R10-1's and R10-5's mass-split residuals.

### 3.8 Prices (named, not adopted)

- **P-site.** Against the Qubit fibre M₂(ℂ) (`AX:43-53`), per site:
  - gauge multiplet: 9 real CCR, 8 physical (A 3, B 3, τ 1, σ 2), plus 8 CAR (η, ψ_A, ψ_B, ψ_τ);
  - matter: 16 real CCR plus 16 CAR.
- **P-dyn.** H = ½{Q, Q†} with Q² = iσL (`AX:116-130`).
- **P-match.** A selectron degenerate with the electron.
- **P-neutral.** A massless σ with Yukawa √2 e (§3.7).
- **P-twist (new).**
  - 𝒦₀ is Lorentz-violating inside the box at O(e² ln(1/ma)): the photon through the selectron Pauli term, the electron through the photino Yukawa.
  - 𝒦_B moves the violation to the electron.
- **P-noP.** No sector-universal momentum (Theorem L′), so the split is tuned (R8-5's price).

## 4. Against the FIXED readings (`TESTS.md:4505-4507`)

**PASS: not met.** Item by item:
- Explicit local Hamiltonian, exact supercharge, Ward identity: **met** (§3.1).
- Doubler-free spin-½ photino: **met at the free level** (§3.2).
- One-loop c_e − c_γ vanishing or protected: **not met.**
  - It is not protected (Theorem L′).
  - It does not vanish: it carries in-box ln(1/m) terms of unequal size in the photon (−8) and the electron (about −2) in 𝒦₀ (§§3.3, 3.5).

**Worker reading: FAIL (bounded), the split, in 𝒦₀.** Offered to the referee. The bounded no-go is:

> In the equivariant Kähler–Dirac class 𝒦₀ (exact Q with Q² = iσL, local H ≥ 0, doubler-free photino, matter Hessian = Peierls-dressed Clifford-flat M_A, no B/τ matter terms), (i) no supercharge fixes c_γ/c_e (Theorem L′, λ-family), and (ii) the one-loop photon speed carries the in-box Lorentz-violating term −e²⟨|c′_x|²|c′_y|²/E³⟩ ∝ −ln(1/m) (Pauli theorem, proved; checked), which no other one-loop photon diagram in 𝒦₀ cancels.

- Point (ii) suffices on its own for "the split does not vanish for every m". The electron log (checked, not proved) makes the split's in-box coefficient about +6 rather than +8.

**INCONCLUSIVE for the wider N=4 Kähler–Dirac class.**
- 𝒦_B cancels the photon log and was tested in one site-local form only. Its electron log is checked, not proved.
- τ-coupled completions are not built.
- **No no-go on locality or spin.** Both are met for the free gauge multiplet, and the equivariant law is local.

**The record, if confirmed.**

> "The local equivariant (σ, η) completion of R12-3's BF law exists: Q² = iσL, H = ½{Q,Q†} ≥ 0, local, Kähler–Dirac photino (doubler-free, untwistable). But no supercharge in the class fixes c_γ/c_e (λ-family), and the Q-exact matter coupling makes the theory Lorentz-violating inside the box: the selectron Pauli term shifts c_γ by −(e²/2π²) ln(1/m), and the photino Yukawa shifts c_e by about −2 ln(1/m)·e²/16π². R12-3's omitted dressing terms (η, longitudinal photino, σ) cancel among themselves for matched curves. Coupling selectrons to the BF partner B repairs the photon but not the electron. The split remains unremoved and unprotected."

## 5. Strong-word check

- **"Exact":**
  - Q² = iσL and [Q, L] = 0 (hand algebra, §3.1);
  - K = C_kd (checked, difference 0) and K² = λ²Δ (3.6e-15);
  - the Ward identity (5e-16);
  - the Pauli decomposition (1e-16);
  - the in-box Pauli cancellation by N_B (continuum algebra).
- **"Proved":**
  - §3.1, the construction (hand algebra; machine-checked on the toy, `r126_algebra_check.out`);
  - Theorem L′ (i)–(ii);
  - the Pauli formula for δc_γ, and its Lorentz-violation argument via Π₀₀ = 0.
- **"Checked":** every table number, with N and m stated. The electron logs are numerical trends: m ≥ 0.025 with N ≤ 256 for 𝒦₀ (matched curves), and m ≥ 0.1 with N ≤ 96 for 𝒦_B. The coefficients (≈ −1.9 to −2.0, and ≈ −2.1 to −3) are fits.
- **"Suggested":**
  - Theorem L′ (iii);
  - the divided-difference N_B;
  - that a σ mass cannot be Q-exact in 𝒦;
  - that τ couplings might restore covariance.
- **"Reading":**
  - the physical sizes at a = ℓ_P (one-loop logs extrapolated);
  - the g−2 bound.
- **Not claimed:**
  - any statement about τ-coupled or non-Hessian-electron completions;
  - Euclidean twisted lattices;
  - non-abelian gauge groups;
  - two loops;
  - a class-wide FAIL for all N=4 Kähler–Dirac laws.

## 6. For the referee

1. **§3.1 algebra.** Check:
   - Q², in particular that {ψ†G, iσvψ} = iσ(v·p − iψ†∂vψ) with no constant;
   - the cross terms in {Q, Q†} that produce the η hopping (c(v·ψ†)η) and the σ pairing;
   - that H ≥ 0 and is local.
2. **§3.3.** Check:
   - M_A² = E_A² + Pauli for the Peierls-dressed Clifford M;
   - that the only one-loop photon pieces in 𝒦₀ are the minimal scalar, the Dirac loop (Theorem P) and the Pauli piece;
   - the Π₀₀ = 0 Lorentz argument.

   Rerun `r126_pauli_photon.py`.
3. **§3.5.** Check:
   - the vertex conventions (Γ^a, Γ^η, Γ^b, σ via particle–hole);
   - the Kähler–Dirac projector contraction S± = Σ_{μν}(P±)_{μν}R_μ†R_ν;
   - the matched-curve cancellation of the dressing;
   - whether the electron's ln(1/m) is genuine in-box Lorentz violation or resolution.

   The control reproduces R12-3.
4. **Theorem L′ (ii).** Do the Gauss-law and charge-sector arguments exclude every cross-sector supercharge?
5. **Scope of FAIL.** Is 𝒦₀ a fair stated class, given that 𝒦_B escapes the photon half?

**Downloads:** none. No web lookups this session. Comparator verifications are cited from the R10-5 and R12-3 referees.
