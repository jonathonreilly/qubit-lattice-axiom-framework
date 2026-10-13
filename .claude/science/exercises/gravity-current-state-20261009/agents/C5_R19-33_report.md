# C5 R19-33 report: box-free set B — is matter + TT graviton reflection-positive with the Newtonian part as a non-local constraint bridge?

**Author and provenance.** Claude Opus 5.5 probe, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13, 07:20Z to about 08:00Z. I edited no repository file and downloaded nothing.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `S/` = `.../scratchpad/C5/R19-33/` (this folder); scripts and outputs in `S/scripts/`.
- `rX` = `P/agents/C5_X_report.md` (or `C4_X_report.md`); `vX` = the referee file of item X.

**Labels.** proved (complete argument under stated hypotheses; mine, unrefereed) / checked (numerics run here) / suggested (argued, not proved) / reading (interpretation) / comparator (outside reference; RECALLED = from memory). Sources: **[ref]** = referee record, **[worker]** = unrefereed.

**Read.** AX in full (233 lines); the R19-33 item (`TESTS:8693-8712`); `rR19-28` in full (worker; referee running); `rK2` (`C4_K2_report.md`) and `C4_K2_referee.md`; `rR2-4` and `C5_R2-4_referee.md`; `rR10-2` and `C5_R10-2_referee_verdict.md`; `rR19-20` and `C5_R19-20_referee_verdict.md`; `P/scripts/C4/K2/k2_transfer_rp.py`, `k2_scalar_stress_exact.py` (K2's stress and gauge map are re-implemented locally in `r1933_cd_static_cov.py`); `P/scripts/C5/R10-2/r102_rp_hankel.py` (Hankel test pattern reused).

---

## 0. Against the FIXED readings (`TESTS:8708-8711`)

**Worker reading: B-RP-OK, scoped** — site reflection positivity (RP) only, and only for one of the two lattice discretizations of the bridge I tested. The other discretization meets the B-RP-FAILS wording. That is a registration collision; I flag it for the referee (§7).

- **Coupled matter + TT graviton (no bridge): RP, exactly.**
  - Use the **spatial** TT projector. It acts inside each time slice, so it is local in time.
  - With it, the coupling h^TT_ij T_ij to K2's exact stress is slice-local: the time-link part of T_ii is δ_ij × scalar and drops against a traceless h.
  - So the coupled action has only slice-local and nearest-neighbour time-link terms. It is site- **and** link-RP to all orders in κ (proved, §2.1). At O(κ) the RP matrix gets no contribution on the null space (proved).
  - The **4D-covariant** TT projector is non-local in time. The 4D-TT Gaussian's h-correlators fail RP outright (checked, §3).
- **The bridge: the constraint part of linearized GR, derived as an instantaneous remainder.**
  - Derivation (checked exactly, §4.1): on conserved sources, W_GR = W_TT + W_inst, with W_inst = (½ρ² − ρA + 2|P_⊥|² + ½P_L²)/q². Here ρ is the energy density, A the transverse trace of the spatial stress, and P the momentum density.
  - The registered "Newtonian part" alone (ρKρ) gives an attractive 1/r but **γ = 0**, which is excluded by Cassini through R2-4. γ = 1 needs the ρ–pressure term −ρA, the conformal sector.
- **Site RP of the bridge at O(κ²) depends on how the time-link part of ρ is put on the lattice:**
  - **K2's exactly conserved T_44** contains ½Δ₄φ(z)Δ₄φ(z−e₄), which straddles the reflection slice.
    - The Newton-only bridge is site-RP. This needs the Newtonian kernel K entrywise ≥ 0, which holds for 1/(4πr) and for a screened kernel.
    - The GR bridge **fails**: the O(κ²) RP matrix on the null space is negative definite (checked). The failure persists for L = 3–6, m = 0.25–1, screened or zero-mode-removed K, and also non-perturbatively at λ = 0.01–1 (§2.3). This is the B-RP-FAILS disjunct for this realization.
  - **D2: symmetric link squares, ρ ∋ −¼[(Δ₄φ)² + (Δ₄φ(z−e₄))²].** This differs from K2 by ¼(Δ₄²φ)², a dimension-6 term.
    - The whole exponent's cross-reflection part is ⅝λ Σ K_xy a_x² b_y², a positive-type kernel.
    - Matter + TT + **full GR bridge** is therefore site-RP to all orders in κ (proved). With a slice-local field cutoff it is site-RP non-perturbatively. Checked at O(κ²) and non-perturbatively.
- **(c) static pull.** The bridge gives V(r) = −2λM₁M₂/(4πr). 4πr·G(r) → 1.00 ± 0.01 on axes and diagonals at L = 96 (checked). Light/dust = 2, so γ = 1, exactly on the lattice (proved).
  - **The sign is forced by RP.** A repulsive bridge violates site RP in both discretizations (checked).
- **(d) covariance cost (named).**
  - The bridge breaks W(B4) to W(B3) × Z₂ᵀ, index 4 (checked: W_inst changes by O(1) under the 1↔4 swap; W_GR is invariant to 4e-14).
  - On exactly conserved sources, TT + bridge equals the covariant lattice Fierz–Pauli (FP) response to 1.8e-12 (checked). So the tree-level exchange does not see the foliation. But the RP realization (D2) is not exactly conserved (checked), so that statement holds only to O(a²) (suggested).
  - At loop level the foliation is suggested to be visible at O(κ²). It may cost the W(B4) protection of the matter speed rows that R19-28 counted as set B's main saving (§5).
- **Not established:**
  - link RP of the bridged theory (the O(κ²) null-space test is empty for link reflection; §2.4);
  - normalizability without a field cutoff (the bridge exponent grows as +quartic: Newtonian collapse);
  - the Wilson-fermion comparator (not run);
  - whether any exactly conserved stress makes the GR bridge site-RP.

**Against the expectation (`TESTS:8712`).**
- **"The TT projector is non-local in time":** true for the 4D TT projector (checked). The spatial TT projector is local in time, and it is the one the foliated bridge needs.
- **"The bridge breaks W(B4) to a foliation":** confirmed.
- **"OPEN":** exceeded on the site-RP question. A constructed realization exists, and a refuted one exists too.

---

## 1. In plain words

- **The plan, from R19-28 and R2-4's Π-NL.** Keep only the two "wave" polarizations of the graviton as fluctuating fields. Put the rest of gravity (the Newtonian pull and its partners) in as an instantaneous action-at-a-distance term between energy densities. Then ask whether the Euclidean 4D grid weight is still reflection-positive, which is what turns it into a quantum theory with a Hamiltonian.
- **The wave part is fine.** If "wave polarizations" is defined slice by slice (transverse to the spatial momentum), the graviton and its coupling to matter live inside time slices, and reflection positivity holds exactly. The 4D-covariant definition reaches across time and breaks positivity.
- **The action-at-a-distance part is subtle.**
  - With only the Newtonian energy–energy term, positivity holds, and the pull is attractive with the right 1/r.
  - But that term alone bends light by half the observed amount (γ = 0).
  - The full constraint term that gives Einstein's light bending also couples energy to pressure. Whether that keeps positivity depends on a lattice detail: how the kinetic energy sitting on the time links is written.
    - With the grid's exactly conserved stress (K2's), it fails.
    - With a symmetric variant, differing only at order (spacing)², it holds exactly.
- **Positivity also fixes the sign.** An instantaneous energy–energy term is reflection-positive only if it is attractive.
- **The price.**
  - A preferred time direction in the law: the 4D grid's 90° time–space turns are lost.
  - A 1/r non-locality in space.
  - Exact conservation of the stress is lost at order (spacing)² in the positive version.
  - A weight that cannot be normalized for unbounded fields (gravitational collapse) unless site values are bounded.
  - Whether graviton loops then spoil the matter light cone that the 4D grid protected is not computed.

---

## 2. (a) RP of the coupled form at O(κ) and O(κ²)

**Hypotheses (stated before titles).**
- **Lattice:** Euclidean Z⁴, ξ = 1. The spatial torus is L³, time is Z.
- **Matter:** S_m = ½Σ[(Δ_μφ)² + m²φ²].
- **Graviton:** h^TT in K7a/K2's placement. The diagonals of h_ij sit on sites and the off-diagonals on spatial plaquette centres, all at integer time. The spatial-TT kinetic form is (ŝ₄² + q̂²)/4 per polarization (`C4_K2_report.md:188-190`; [ref] `C4_K2_referee.md:13`).
- **Coupling:** −κΣ h^TT_ij T_ij, with K2's exact stress (`C4_K2_report.md:61-65`).
- **Bridge:** the weight factor e^{+B}, with B = Σ_t B_t and B_t built from same-time sources (§4.1):
  - **GR bridge:** B_t = λ[ρKρ + 2ρKA + 4P_⊥KP_⊥ + P_LKP_L];
  - **Newton bridge:** B_t = λρKρ;
  - λ = κ²/4 and K = (−Δ₃)^{-1}.
  - ρ = −T₄₄ (Minkowski energy density), A = θ_ij T_ij, P = T₄ᵢ (on half-integer time links).
- **Reflections:** site reflection through slice 0, and link reflection between slices 0 and 1.
- **Measure:** "RP at O(κ²)" is meant in the formal sense below (Schur criterion), or exactly when a slice-local field cutoff makes the weight normalizable (§2.5).

### 2.1 Matter + spatial TT: site and link RP to all orders (proved)

1. **The spatial TT projector P3(q) does not depend on k₄,** so it acts slice by slice (checked: time kernel δ_{t0}, `r1933_b_tt_projector.out:3`).
2. **The time-link part of K2's T_ii drops.** K2's T_ii contains −¼[(Δ₄φ(z))² + (Δ₄φ(z−e₄))²]. That is i-independent, i.e. δ_ij × scalar. A pointwise-traceless h^TT kills it. The remainder is ¼(φ(z+e_i) − φ(z−e_i))² for diagonals and the purely spatial ¼(Δ_iφ + Δ_iφ′)(Δ_jφ + Δ_jφ′) for off-diagonals. **So h^TT·T is slice-local.**
3. **The action is therefore a sum of slice-local terms plus nearest-neighbour time links** (φ, h^TT), and each time link has the positive cross term +φ_tφ_{t+1} (or the h analogue).
   - **Site RP** follows from the Markov factorization: ∫dφ₀dh₀ e^{−S₀}(∫e^{−S₊}F)² ≥ 0.
   - **Link RP** follows because the only cross term is e^{φ₁·Θφ₁} (and the h analogue), which is of positive type.
   - **Hence κ-exact.** This fills the "joint RP not shown" gap in K2 (`C4_K2_report.md:196-201`; [ref] `C4_K2_referee.md:13,15`) for the TT-reduced, temporally gauge-fixed form.
4. **O(κ).** On the null space of the O(1) RP matrix (E[F | slice 0] = 0), the O(κ) block vanishes, and so does its mixing with h-independent range vectors. The coupling is slice-local and odd in h. So no O(κ) violation can occur (proved).

### 2.2 Where the bridge can break site RP (proved)

**Notation.** Fix the slice-0 data. Let a = φ₁ − φ₀ (positive side) and b = Θa = φ₋₁ − φ₀.

**Which terms straddle slice 0.**
- Every bridge term except B₀ is one-sided. The P terms sit at t = ±½.
- In B₀:
  - **ρ (K2):** ρ = ½a⊙b + u, with u = ¼Σᵢ[(Δᵢφ₀)² + (Δᵢφ₀′)²] + ½m²φ₀² ≥ 0. The product a⊙b straddles.
  - **ρ (D2):** ρ = −¼(a² + b²) + u.
  - **A (both):** A = −½(a² + b²) + A_s, from θ_ii = 2 acting on K2's link squares.

**The kernel criterion.** With the Markov factor written as g(ψ′)g(ψ), site RP is equivalent to: the cross kernel X(b, a) = exp(B_cross) is PSD for almost every slice-0 configuration. At O(κ²), with test functions on the null space, it is equivalent to B_cross being PSD there.

**The cross parts.**

| Bridge | B_cross / λ | Positive type? |
|---|---|---|
| K2-Newton | ¼Σ K_xy(a_xa_y)(b_xb_y) + Σ(Ku)_x a_xb_x | yes, if K_xy ≥ 0 entrywise (u ≥ 0) |
| K2-GR | ¼Σ K_xy(a_xa_y)(b_xb_y) + Σ_x (K(u + A_s))_x a_xb_x − ½Σ K_xy(a_xa_y²b_x + a_xb_xb_y²) | **no**: the last term is f⊗e + e⊗f with no f⊗f partner, so it is indefinite; also u + A_s < 0 at constant φ₀ |
| D2-Newton | ⅛Σ K_xy a_x² b_y² | yes, if K is PSD |
| D2-GR | ⅝Σ K_xy a_x² b_y² | yes, if K is PSD |

**Attraction is the RP sign (proved).** Flipping the bridge sign turns each positive-type kernel into a negative-type one.

**The TT exchange cannot rescue K2-GR on its failing directions (proved).** The ½(S₁)² cross terms are of positive type (they come from E[h₊h₋ | h₀]). But on the odd test functions used in §2.3 they vanish: at φ₀ = 0, or at constant φ₀, T^TT is even in the fluctuation z and the conditional mean has no spatial gradient.

### 2.3 Numbers (checked)

**Perturbative test** (`r1933_a_site_rp.py` → `.out`, 5 s).
- O(κ²) RP matrix per λ, on the centred linear test functions F_i = z_i of slice 1 (on the null space).
- Exact Gaussian moments, with the conditional law from an 8-slice free half-chain.

| Case | K2-Newton | K2-GR | D2-Newton | D2-GR |
|---|---|---|---|---|
| φ₀ = 0, L = 3, m = 1, μ_K = 0.3 (`.out:5`) | 0 / 0 | **−0.259 / −0.011** | 0 / 0 | 0 / 0 |
| φ₀ = 0, L = 6, m = 0.25, μ_K = 0.1 (`.out:28`) | 0 / 0 | **−9.49 / −0.075** | 0 / 0 | 0 / 0 |
| φ₀ = const, L = 6, m = 0.25, μ_K = 0.1 (`.out:54`) | +0.028 / +4.75 | **−17.1 / −0.10** | +1e-5 / +1.41 | +5e-5 / +7.05 |
| φ₀ random, L = 6, m = 0.25, μ_K = 0.1 (`.out:80`) | +1.96 / +237 | **−174 / −1.4** | ≥ 0 | ≥ 0 |

- **K2-GR is negative definite on the whole linear sector at all 72 settings:** L = 3–6, m = 1, 0.5, 0.25, μ_K = 0.3, 0.1, and three φ₀ types.
  - Along L the minimum converges: −0.259, −0.229, −0.220, −0.216 at φ₀ = 0, m = 1, μ_K = 0.3.
  - It grows as m and μ_K decrease.
- **IR control** (`r1933_a_site_rp_zeromode.out`; K = pinv(−Δ₃), zero mode removed, so not entrywise ≥ 0):
  - K2-GR stays negative definite (−7e-3 to −0.43 relative scale; every row).
  - D2 stays PSD.
  - **K2-Newton now fails at random φ₀** (min −0.06 to −0.30). Its positivity needs K ≥ 0 entrywise, which the infinite-volume 1/(4πr) and screened kernels have, and the torus-neutralized kernel does not.
  - Repulsive Newton: negative in both discretizations (min −0.16 to −26).

**Non-perturbative test** (`r1933_a_nonpert_kernel.py` → `.out`, 7 s).
- X(b, a) = exp(λB_cross) on 1500 random points of the grid a ∈ {−1, 0, 1}^8 (2³ torus, m = 0.5, μ_K = 0.3).
- A negative Gram eigenvalue on any finite set proves non-PSD, by bump test functions.

| Case | λ = 0.01 | λ = 0.1 | λ = 1 |
|---|---|---|---|
| attractive K2-Newton, D2-Newton, D2-GR (φ₀ = 0 and random) | min/max ≥ −1e-15 (roundoff) | same | same |
| one exception: K2-Newton, random φ₀ | +2.7e-8 | +8.1e-8 | −1e-15 |
| K2-GR, φ₀ = 0 | **−0.060** | **−1.00** | **−1.00** |
| K2-GR, random φ₀ | **−0.20** | **−1.00** | **−1.00** |
| repulsive Newton, both discretizations | −3e-3 | … | … to −1.0 |

### 2.4 Link RP (proved: the test is empty; full status not established)

- For link reflection, the O(1) RP form is strictly positive on functions of the boundary slice φ₁. The kernel e^{φ₀·φ₁} has Mehler eigenvalues rⁿ > 0.
- Its null space is {E[F | φ₁] = 0}. On that null space the O(κ²) bridge block is nonzero only for terms coupling slices ≤ −1 to slices ≥ 2. No same-time bridge built within one link of a slice does that, in either discretization.
- **So link RP cannot fail at O(κ²) in the formal sense, for K2 or D2, and the formal pass is vacuous.**
- Non-perturbative link RP is **not computed**. A risk (suggested): P = T₄ᵢ on the straddling link is Θ-odd, so P_⊥KP_⊥ contains −2XKΘX-type negative boundary cross terms.
- **Consequence for OS reconstruction.**
  - Site RP alone gives a self-adjoint contraction T with T² ≥ 0 (comparator, RECALLED; R10-2's H-E accepts one reflection, `C5_R10-2_report.md:49-53`).
  - So H = −(1/2a)log T² exists perturbatively. That restores the "lowest state" which (Σ) needs (`rR19-28:28`).
  - T ≥ 0 itself is not shown.

### 2.5 Normalizability (proved; reading)

- The bridge exponent contains +λρKρ ~ +λ(½m²φ²)K(½m²φ²), which is +quartic. The TT exchange adds +κ²T^TT G T^TT, also +quartic.
- So for unbounded φ the weight is not normalizable. This is the Newtonian gravitational-collapse instability.
- RP holds as a formal power series in κ, order by order. It holds exactly once the weight is made normalizable by a slice-local bound |φ_x| ≤ Φ: the kernel proofs in §2.2 are pointwise and survive the cutoff.
- **Reading.** Bounded site values fit the Qubit axiom's M₂(C) (`AX:43-50`), but the non-perturbative vacuum with a cutoff is unexamined.
- **Correction to R2-4's Π-NL comparator (suggested).** "Bounded below by the positive-energy theorem" (`C5_R2-4_report.md:127`) is a nonlinear-GR statement. It does not hold for this linearized bridge.

---

## 3. (b) The TT projector: locality in time, and RP of the projection (checked)

`r1933_b_tt_projector.py` → `.out`, 8 s. Lattice symbols in ŝ_μ = 2 sin(k_μ/2), at three spatial momenta.

- **Spatial TT projector P3.**
  - Time kernel: exactly δ_{t0} (`.out:3`). It is local in time, and non-local in space (1/r³ from q_iq_j/q², proved).
  - The spatial-TT field (K2's reduced graviton) passes site H0/H2 and link Hankel tests to roundoff, ≤ 6e-16 relative, at N = 1–6 (`.out:6-10, 27-31`).
- **4D TT projector P4.**
  - Time kernel: non-zero at every t, e.g. P4_{11,11}(t) = 0.536, −0.084, −0.054, −0.034, −0.021 at q = (0.3, 0.2, 0.1) (`.out:4`).
  - It decays like a polynomial × e^{−E_q|t|}. So it is non-local in time, with a range that diverges as q → 0.
- **The 4D-TT Gaussian on its h components ("model A" of R2-4).**
  - It fails site and link RP: Hankel min/max −0.03 to −0.40, growing then stable in N (`.out:11-15, 32-36`).
  - There are direct violations. The diagonal correlators at even times are negative, e.g. G_{11,11}(4) = −0.020 (`.out:16`), G_{11,11}(2) = −0.021 and G_{12,12}(2) = −0.037 at q = (0.9, 0, 0) (`.out:37,41`). Site RP needs G_aa(2t) = ‖Tᵗh_a‖² ≥ 0.
  - Model A was RP on curvature correlators only ([ref] `C5_R2-4_referee.md:40`), and it has γ = ½ (`C5_R2-4_report.md:134`). So the 4D-TT route fails on both counts.
- **Reading.** The foliated (spatial-TT) projection is the RP-compatible one. The expectation's concern applies to the covariant projector.

---

## 4. (c) The constraint bridge and its static response

### 4.1 The bridge, derived (checked exactly; `r1933_c_decomp.py` → `.out`, 11 s)

- **Setting.** Euclidean conserved J (p·J = 0), GR response W_GR = (J:J − ½(trJ)²)/p² (K7a symbol; `C5_R2-4_report.md:86-87`), and spatial-TT exchange W_TT = |J^TT|²/p².
- **The remainder** W_inst = W_GR − W_TT:
  - has no pole at p² = 0 (`.out:2`);
  - equals, identically on conserved J and exact in sympy (`.out:3-6`):

  W_inst = (½ρ² − ρA + 2|P_⊥|² + ½P_L²)/q²,

  with ρ = J₄₄, A = θ_ijJ_ij and P = J₄ᵢ split into ⊥ and L parts. This is instantaneous: there is no p₄, so it is local in time and non-local in space.
- **The (ρ, A) block** has eigenvalues (1 ± √5)/4, one of them negative (`.out:15`). That is the conformal direction: R2-4's negative mode, moved into the bridge. The TT part is a covariance.
- **The lattice version** is the same algebra with p → ŝ, because K7a's symbol is O(4)-covariant in ŝ (checked: §5).
- **In the weight** (J = κT, T₄₄ = −ρ_M): ½W_inst → λ[ρKρ + 2ρKA + 4P_⊥KP_⊥ + P_LKP_L], with λ = κ²/4 and K = 1/q̂².

### 4.2 1/r and its sign (checked; `r1933_c_static_fit.out:1-7`, `r1933_cd_static_cov.out:1-11`)

- **Two static dust masses.** The cross term is 2λM₁M₂K(r) per slice, so V(r) = −2λM₁M₂K(r).
- **Lattice Green's function on L³** (zero mode removed, background r²/6L³ subtracted). 4πr·G(r) at L = 96:
  - axis: 1.08, 1.08, 1.02, 0.999, 0.999 at r = 1, 2, 4, 8, 12;
  - face: 0.98–1.007;
  - body: 0.95–1.02 (the drift at the largest r is a torus effect, smaller at L = 96 than at L = 48).
  - G > 0 and decreasing, so the pull is **attractive**, with G_N = λ/(2π) (convention-dependent constant).
- **Light bending.**
  - A light probe uniform along x has q₁ = 0, so θ₁₁ = 1 exactly and A_l = ρ_l. The probe–mass cross term is then 2λ(ρ_l + A_l)Kρ_m, so light/dust = 2, i.e. 1 + γ = 2 (proved on the lattice; continuum check `r1933_c_decomp.out:18-20`).
  - **The Newton-only bridge gives ratio 1, so γ = 0.** That is excluded via Cassini (R2-4's Lemma W input, [ref] `C5_R2-4_referee.md:20-24`).
- **Reading.** The attractive sign is an input of the bridge (P-N1, graviton supplied; `rR19-20:215`). §2.2 shows it is also the only site-RP-compatible sign.

---

## 5. (d) W(B4) covariance and its cost (checked / suggested)

1. **Symmetry of the bridge (checked).**
   - Under the W(B4) element swapping axes 1 and 4, W_inst changes by O(1): max relative change 1.00 over 200 lattice momenta. W_GR changes by 3.9e-14 (`r1933_cd_static_cov.out:17`).
   - The bridge keeps W(B3) × Z₂ᵀ: spatial hyperoctahedral group, time translations and time reflection. That is index 384/96 = 4 in W(B4), i.e. the choice of time axis.
   - The spatial TT projector carries the same foliation. Since W_TT = W_GR − W_inst on conserved sources, it is non-covariant too (proved from the identity).
2. **Tree level on exactly conserved sources (checked).**
   - On lattice-conserved J (ŝ·J = 0), W_TT + W_inst = W_GR to 1.8e-12 at 200 random lattice momenta (`r1933_cd_static_cov.out:14`).
   - So for K2's exactly conserved stress (on shell), the matter–matter exchange is W(B4)- and indeed ŝ-O(4)-covariant: the foliation is invisible at tree level.
   - **But K2-GR is not site-RP (§2.3).**
3. **The RP realization breaks conservation (checked; size suggested).**
   - D2's T₄₄ = K2's + ¼(Δ₄²φ)² (with the sign of T₄₄ = −ρ). On an exact Euclidean lattice solution (EOM residual 7.8e-14), K2's Ward sum Σ(∇ξ + ∇ξ)T vanishes (0.0 for four time-gauge ξ), while D2's gives −166, 287, 696, 721 (`r1933_cd_static_cov.out:20-22`).
   - The extra term is dimension 6, so the tree-level foliation leak is O(p²a²) (suggested, power counting).
4. **Loop level (suggested, not computed).**
   - The reduced (foliated) theory equals a W(B4)-covariant one only where lattice gauge invariance holds. K2 proved the O(κ²) Killing closure fails for these realizations ([ref] `C4_K2_referee.md:9,17`).
   - So graviton loops (TT exchange plus bridge) can generate time–space anisotropy in matter's dimension-4 speed rows at O(κ²/a²) × loop factor, which is not small at a = ℓ_P.
   - That would remove, for the gravitational contributions, the "charge block = 0 by W(B4) at all orders" saving that R19-28 credits to set B (`rR19-28:187`; [ref] T1/F2/O1). Size not computed.
5. **Axiom-text reading.**
   - The foliated law is covariant under Z³ cubic rotations and time translations, which is what `AX:57-58` literally asks.
   - It violates set B's added B2 (whole-law B4⁺) and the "nearest-neighbor" clause (`AX:57,61`) through the 1/r kernel. That is R2-4's Π-NL price (`C5_R2-4_report.md:294`), here **constructed** at site-RP level, under the caveats of §2.4–2.5.

**Named covariance cost (for B-RP-OK).**
- W(B4) → W(B3) × Z₂ᵀ in the law (a preferred time axis);
- exact lattice conservation lost at O(a²) in the RP realization;
- a suggested O(κ²) loop-level leak into the matter light cone;
- power-law spatial non-locality (Π-NL).

---

## 6. Prior art (each counted once) and what changes

- **K2** [ref]: TT transfer positive; coupled RP unproved. **Now:** κ-exact site and link RP for spatial-TT + matter (§2.1).
- **R2-4** [ref]: Lemma W; Π-NL suggested, "not constructed on Z⁴". **Now:**
  - Π-NL is constructed at site-RP level, with the GR-complete constraint sector (D2), and γ = 1 is checked.
  - The Newton-only version is RP but γ = 0.
  - Correction suggested to its "bounded below" comparator (§2.5).
- **R10-2** [ref]: box symbols fail RP. **Here:** no box symbols are used (box-free set B), and every symbol is analytic. R10-2 does not apply.
- **R19-28** [worker]: box-free set B OPEN on K2 and R2-4; payment "TT in the transfer matrix + non-local constraint" suggested (`rR19-28:166-170`). **Now:** that payment is site-RP in one realization and fails in the exactly conserved one. Its W(B4) charge-block saving is put at risk at loop level (§5.4, suggested).
- **R19-20** [ref]: (Σ) needs a lowest state, hence a Hamiltonian. **Now:** site RP supplies T² ≥ 0 and H perturbatively.
- **Comparator, RECALLED:**
  - Coulomb-gauge QED / ADM reduction: transverse field + instantaneous constraint term equals the covariant exchange on conserved sources (the continuum counterpart of §5.2).
  - Lattice-gauge OS positivity (Osterwalder–Seiler; Lüscher): link RP via positive-type cross terms, the criterion used in §2.

## 7. For the referee

1. **Registration collision.** D2-GR meets B-RP-OK (site RP, checked, 1/r attractive, cost named). K2-GR meets the B-RP-FAILS wording (negative O(κ²) eigenvalue, persistent under L, m, μ_K and the IR treatment). Since the two differ by a dimension-6 term, I read "the coupled form" as admitting an RP realization, i.e. B-RP-OK. If exact lattice conservation (K2's Ward identity) is required, the reading is B-RP-FAILS for this pair of discretizations.
2. Is site RP alone acceptable for B-RP-OK? (R10-2's H-E says one reflection suffices.) Link RP is formally unviolated at O(κ²) but not established.
3. Check the W_inst decomposition (§4.1) and the kernel classification (§2.2), especially the claim that the TT exchange vanishes on the failing odd directions.
4. Is the loop-level foliation leak (§5.4) the right cost to carry forward to R19-28's bill?

## 8. Strong-word check and scope

- **"Exactly / κ-exact":**
  - site and link RP of matter + spatial TT, as a formal power series or with a field cutoff;
  - site RP of D2-GR and of the Newton bridges under the stated K conditions.
  - All are proved by positive-type kernels; none is refereed.
- **"Fails":** K2-GR site RP at O(κ²), checked numerically. It is a property of that discretization, not of the continuum bridge.
- **"Attractive 1/r":** checked to about 1% at r ≥ 4 on axes and diagonals at L = 96.
- **Not claimed:**
  - link RP of the bridged theory;
  - non-perturbative normalizability without a cutoff;
  - the Wilson-fermion comparator (not run);
  - loop-level sizes;
  - that no exactly conserved stress works;
  - nonlinear (O(κ³)) structure.
- **Scalar only.** The fermion case is open.

## 9. Files (`S/scripts/`, all under 15 s with `OMP_NUM_THREADS=2`)

- `r1933_c_decomp.py` / `.out`: W_GR = W_TT + W_inst; the instantaneous form; signature; static and light ratios.
- `r1933_a_site_rp.py` / `.out`: O(κ²) site-RP matrices, linear sector; K2/D2 × Newton/GR; L = 3–6.
- `r1933_a_site_rp_zeromode.py` / `.out`: IR control (pinv K) and repulsive sign.
- `r1933_a_nonpert_kernel.py` / `.out`: the non-perturbative cross-kernel PSD test on a 2³ grid subset.
- `r1933_b_tt_projector.py` / `.out`: projector time kernels; Hankel tests, spatial TT vs 4D TT.
- `r1933_cd_static_cov.py` / `.out`: static pull, conserved-source identity, 1↔4 covariance, K2 vs D2 Ward residual.
- `r1933_c_static_fit.py` / `.out`: corrected 4πrG(r) at L = 48, 96.
- `R19-33_report.md`: this report.
