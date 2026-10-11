# Lane RP, probe P1: species sum rules for the E_g shear mass (report)

Worker: Claude Opus 5.5 (same family as the supervisor and as V3). Run 18:56Z to about 19:25Z, 2026-10-11. **Not refereed.** No repository files were edited.
Scratch: `.../scratchpad/C4/P1/`. Every number below is in a `.out` file there:
- `p1_mu_species.py` / `.out`: exact μ_E(m) per species, the expansion coefficients, and the checks against V3 and its referee;
- `p1_bruteforce_check.py` / `.out`: an independent check by direct flow plus finite differences (V3's method, with no elliptic reduction and no integration by parts);
- `p1_sum_rules.py` / `.out`: the sum rules, Standard Model content, the P0 comparison and the interaction estimates;
- `p1_coeffs.npz`.

## Verdict against the FIXED reading: **FAIL (bounded)**

The FIXED FAIL disjunct "the sum rules need mass relations (tunings)" is met. The FAIL is bounded to: flow-coupled KG scalars, staggered fermions, naive fermions, a noncompact U(1) photon in two coupling options, and massive vectors (argued). Exact at the free level; interactions are estimated, not computed.

- **R0 (leading rule):** a natural count, but not the boson-equals-fermion count. It needs 1 real KG component per 2 staggered fields, i.e. per 16 infrared fermionic degrees of freedom. A 1:1 count per infrared d.o.f. works only if the bosons carry the fermions' doublers. SM content misses R0 by +22 natural units.
- **R2, R4 and R6:** three further rules, at (ma)², (ma)⁴ and (ma)⁶ ln(ma). All three are needed to reach the P0 level at physical masses, and they are mass relations. Only exact boson–fermion pairing satisfies all of them without tuning.
- **Interactions:**
  - The O(λ) Hartree term is a pure mass shift (proved).
  - The first unprotected terms are O(g²/16π²) × natural, about 10⁹⁸ times the P0 bound (suggested).
  - Kato–Sakamoto–So excludes lattice SUSY with the full algebra.
  - A nilpotent Hamiltonian supercharge is not excluded and would protect μ = 0. But it does so only for an exactly degenerate spectrum (suggested), which observation excludes.

## 1. Exact μ_E(m) per species (one normalization)

**Normalization.** RN-L1 throughout:
- the E-channel flow velocity is v = ½ ĥ f(k), with ĥ = diag(1, −1, 0) and f the species' local momentum symbol, normalized to unit slope at the physical zero;
- μ_E = d²E_vac/dε² per lattice site (cell a³), in lattice units;
- V1 normalization is 4 × RN-L1.

**General formula. PROVED (periodic integration by parts of V3's refereed Jacobian formula).** Since J''(0) = ∇·(v ∇·v):

  μ_E = ⟨ε_vac J''⟩ = −⟨∇ε_vac · v (∇·v)⟩_BZ.

For a separable v, ∇·v = ½(f′(k_x) − f′(k_y)).

**The species.** Every μ below is PROVED as a formula and CHECKED as a number.

| Species (symbol) | μ_E(m) per site | m = 0 value |
|---|---|---|
| Real KG scalar, ω² = M² + Σ4sin²(k/2) (f = sin k) | **F(M) = ⅛⟨(cos k_x − cos k_y)²(cos k_x + cos k_y)/ω⟩** | +2.695798e-3 |
| Staggered field (2 Dirac tastes; f = ½ sin 2p) | −½F(2m) | −1.347899e-3 |
| Naive fermion, taste-singlet f = ½ sin 2p (= 4 staggered fields) | −2F(2m) | −5.391596e-3 |
| Naive fermion, nearest-neighbour f = sin p | G(m) = ½⟨(s_x²c_x − s_y²c_y)(c_x − c_y)/ω_n⟩ | **+1.100007e-1** (40.80 F(0)) |
| Naive-dispersion real boson (bosonic doublers; f = ½ sin 2p) | +½F(2m) | +1.347899e-3 |
| Photon, option A (canonical/Poynting orbital flow, f_j = sin q_j) | 2F(0) | +5.391596e-3 |
| Photon, option B (Maxwell in a unimodular diagonal metric a = (e^ε, e^{−ε}, 1)) | 2F_B(0), with F_B(M) = ½⟨(K_x²+K_y²)/(2ω) − (K_x²−K_y²)²/(4ω³)⟩ | **+7.117212e-1** (264.0 F(0)) |
| Massive vector, option A (lattice Proca, all 3 polarizations ω² = M² + K̂²) | 3F(M) | ARGUED, not run |

**Checks.**
- F(1) = 1.970388641879e-3, against the V3 referee's 1.970388641877e-3.
- The staggered field reproduces the referee's V1-normalized continuum value −3.940777283755e-3 at m = 0.5, and V3's table value −5.29e-4 at m = 1.
- The naive fermion with ½ sin 2p, computed directly on the naive dispersion, equals −2F(2m) to all 13 printed digits.
- Brute-force flow plus finite differences at L = 64 and 96 reproduces G(0.5), F(0.5), F_B(0.5) and 2F_B(0) to 8 digits.
- The elliptic kz-reduction agrees with direct quadrature to 4e-16.
- The lattice Maxwell eigenvalues in the diagonal metric are {0, Ω², Ω²}, with Ω² = ΣK_i²/a_i, to 7e-15.

**Derivation of F.** ∇(½ω)·v = (sin²k_x − sin²k_y)/(4ω), and ∇·v = ½(cos k_x − cos k_y). Then use sin²k_x − sin²k_y = −(cos k_x − cos k_y)(cos k_x + cos k_y). The staggered and naive maps follow from k = 2p and ω_s(p; m) = ½ω_KG(2p; 2m), as in V3.

**The photon.** The photon's E_g coupling is ambiguous. It is the same flow-versus-metric ambiguity that every boson has.

- **Option A** is the analogue of V3's matter coupling. It uses the canonical momentum −E_k∇_j^sym A_k, whose symbol is sin q_j on every component.
  - On Gauss-law states, the gauge-invariant Poynting form E × B (Yee averaging) equals it.
  - The first moments of the two forms differ by two pieces: a Gauss-law term, and a translation-invariant "spin" term ĥ_ij E_j A_i, which is a polarization squeeze. Neither has a first moment, so neither has a Jacobian. ARGUED, not run.
  - So μ_γ^A = 2F(0), equal to two massless KG components.
- **Option B** is the metric (K1-type) coupling. For E_g the metric is diagonal, so the placement is unambiguous for constant strain; the exponential unimodular parametrization removes the tadpole ambiguity.
  - It is 132 times option A per polarization. This is the "cutoff fixed by grid labels" response.
  - Option B also needs off-diagonal placement for T_2g. So, unlike option A, it does not inherit Liouville protection (suggested; not computed on Z³).
- **K1's Weyl zero** is a 4D tadpole statement. With the Hamiltonian strain coupling, the photon's μ_E is nonzero in both options.

## 2. Expansion in (ma)

**Universal function** (PROVED structure, CHECKED coefficients):

  F(M) = c₀ + c₂M² + c₄M⁴ + M⁶(c₆L ln M + c₆) + O(M⁸ ln M), with:
- c₀ = +2.695798e-3
- c₂ = −1.012898e-3
- c₄ = +4.792894e-4
- c₆L = 1/(384π²) = +2.638572e-4. Analytic; the fit gives 2.638567e-4.
- c₆ = −1.4541e-4 (fit, stable to 2e-5 relative across two fit bases).

The series to M⁶ matches F to 4e-15 at M = 0.05 and to 1e-12 at M = 0.1.

**Why the first log is at M⁶, not M⁴. PROVED.**
- In the continuum the E flow preserves volume.
- On the lattice, ∇·v = ½(cos k_x − cos k_y) ≈ (k_y² − k_x²)/4. That is an a²-suppressed anomaly operator.
- So the infrared integrand is (k_x² − k_y²)²/(16ω). The Taylor coefficients converge through M⁴, and the M⁶ term is logarithmic.
- Angular average 4/15 and the binomial coefficient −5/16 then give c₆L = 1/(384π²).
- **Physical form:** μ_E ⊃ a² m⁶ ln(ma)/(384π²), multiplied by (infrared d.o.f.) × (the symbol's cubic coefficient relative to sin k).

**Per species.** Use M → λm with weight w:

| Species | c₀ | c₂ | c₄ | m⁴ ln m | m⁶ ln m | m⁶ |
|---|---|---|---|---|---|---|
| KG component (w = 1, λ = 1) | +2.6958e-3 | −1.0129e-3 | +4.7929e-4 | 0 | +2.6386e-4 | −1.4541e-4 |
| Staggered field (w = −½, λ = 2) | −1.3479e-3 | +2.0258e-3 | −3.8343e-3 | 0 | −8.4434e-3 | −1.1994e-3 (incl. ln 2) |
| Per Dirac (proxy: ½ staggered field) | −6.7395e-4 | +1.0129e-3 | −1.9172e-3 | 0 | −4.2217e-3 | −5.997e-4 |
| Naive, ½ sin 2p (w = −2, λ = 2) | −5.3916e-3 | +8.1032e-3 | −1.5337e-2 | 0 | −3.3774e-2 | −4.7975e-3 |
| Naive, sin p: G | +1.10001e-1 | −5.7410e-2 | +1.5948e-2 | **−1/(2π²) = −5.0661e-2** (fit agrees to 7 digits) | not computed | |
| Metric-coupled scalar F_B | +3.55861e-1 | −2.2151e-2 | +1.7079e-3 | 0 (fit: 4e-10) | about −1.32e-4 (fit) | |
| Photon A / photon B | 2c₀ / 2b₀ | massless | | | | |

**The naive fermion with the nearest-neighbour symbol is an outlier.**
- Its doublers at (π,0,·) and (0,π,·) see a reversed velocity along one axis. For them the E strain is a compression, with ∇·v = ∓1 at leading order.
- That gives an m⁴ ln m term with coefficient −1/(2π²) (PROVED; CHECKED by fit) and a c₀ 40.8 times the scalar's.
- The taste-singlet symbol ½ sin 2p removes both effects.

**Orders needed** (`p1_sum_rules.out`):
- At physical masses, ma ≈ 1.4e-17 for the top quark (a⁻¹ = M_Pl) or 7.1e-17 (reduced-Planck cell).
- The (ma)⁶ ln(ma) term is still 3.6e2 times the P0 bound (framework) or 8.7e3 times it (refereed convention).
- (ma)⁸ is ≤ 5e-129, which is negligible.
- **So 4 rules are needed: R0, R2, R4 and R6.**

## 3. Sum rules, order by order

All taste-singlet, flow-coupled species are w·F(λm). So:
- **R0:** Σw = 0;
- **R2:** Σw λ²m² = 0;
- **R4:** Σw λ⁴m⁴ = 0;
- **R6:** Σw (λm)⁶[c₆L ln(λm) + c₆] = 0.

Weights relative to one real KG component:

| | n = 0 | 2 | 4 | 6 |
|---|---|---|---|---|
| Per real bosonic component | +1 | +1 | +1 | +1 |
| Per Dirac fermion | −¼ | −1 | −4 | −16 |
| Per fermionic d.o.f. | −1/16 | −¼ | **−1** | −4 |

**R0. PROVED.** R0 is an integer count:

  n_KG + 2n_γ + 3n_V + ½n_naiveB = ½n_stag + 2n_naive.

- It cancels with 1 real KG component per 2 staggered fields, which is 16 infrared fermionic d.o.f. per bosonic one.
- Alternatively, it cancels with 1 naive-dispersion boson per staggered field, which matches 8:8 in infrared d.o.f. That is I3's bosonic-doubler pairing.
- So R0 is satisfiable by a natural count, but **not** by matching Pauli's degrees of freedom with ordinary KG bosons.
- If a photon is option B, or a fermion is naive with sin p, R0 becomes a relation between unrelated lattice numbers (132.0057…, 40.8045…). That is a tuning, not a count.

**SM content, R0.** CHECKED. Unitary gauge, option A, fermions as half-staggered Dirac proxies:
- bosons give 28 (16 gluon + 2 photon + 6 W + 3 Z + 1 H);
- fermions give −6 (24 Dirac);
- **Σc₀ = +22 F(0) = +5.93e-2 per site, 22 times natural.** With Weyl neutrinos it is +22.375.
- Satisfying R0 would need 112 Dirac fermions for these bosons, or only 6 bosonic components for these fermions.
- Reading: if the axioms' single qubit per site carries a single staggered field, R0 needs ½ a bosonic component, and one photon already overshoots it four-fold.

**R2.**
- R2 is **not** Pauli's Str M², because fermions are weighted ¼ per d.o.f.
- SM: 79,396 − 89,526 = **−1.01e4 GeV²**, an 11% miss, dominated by 6M_W² + 3M_Z² + M_H² against 3m_t².
- Reading: this is a Veltman-like near-miss, but low-energy masses are not the cutoff-scale masses that enter c₂.
- Required precision: 1.8e-68 (framework) or 4.5e-67 (refereed convention) of the largest term.

**R4.**
- R4 is **exactly Pauli's quartic supertrace per d.o.f.** That is the map's 2⁴/16 = 1.
- SM: −9.97e9 GeV⁴, a 93% miss. Required precision: 4.7e-35.

**R6.**
- The coefficients carry (infrared d.o.f.) × (the symbol's cubic coefficient). That is not a pure d.o.f. count.
- SM: top-dominated, +3.9e-102 (framework), which is 360 times P0. Required precision: 2.8e-3 (framework) or 1.1e-4 (refereed).

**Count.** Beyond the R0 count there are **3 mass relations** (R2, R4, R6). The only all-orders solution is exact pairing, as follows; every pair is itself a mass relation unless a symmetry enforces it:
- a KG component of mass 2m against 2 staggered fields of mass m: F(2m) − F(2m) = 0;
- or a naive-dispersion boson against a staggered field at equal m.

## 4. Interactions

**O(λ) Hartree, φ⁴. PROVED.**
- E₁(ε) = (λ/8)G_ε², with G_ε = ⟨J/(2ω)⟩.
- The mass counterterm is fixed at ε = 0, so the Hessian is (λ/4)G′².
- G′ = ⟨∇·v/(2ω)⟩ = 0 in E, by x↔y antisymmetry.
- So O(λ) is only the mass shift already contained in F.

**First unprotected order.** It is O(g²) for Yukawa or gauge couplings, and O(λ²) for φ⁴. This is V3's transported self-energy anomaly, which V3 ARGUED is E-only.

**Size. SUGGESTED, not computed.**
- Estimate: δμ ≈ κ(g²/16π²)F(0), with κ = O(1).
- With g²/16π² ≈ 1e-3 to 2e-3 at M_Pl (gauge couplings and y_t), δμ ≈ 3–5e-6 per species, which is about 10⁹⁸ times the P0 bound.
- Holding the cancellation would need about 34–38 loop orders of exact boson–fermion cancellation.
- Comparator, reading only: K3a″'s O(e²) metric-type shear response, 1.2e-3 per cell at α = 1/137, is of order 2e²/16π² per cell.
- For QED, V3(b) adds that the O(e) dressing is not even exponentially local.

**Protection.**
- **Kato–Sakamoto–So** (0803.3121; comparator, from memory) is a no-go for a local Leibniz rule. It therefore excludes lattice SUSY with the algebra {Q, Q̄} ∼ P, and with it the continuum mechanism that would keep Bose–Fermi pairs cancelling under interactions.
- **Not excluded:** a nilpotent Hamiltonian supercharge with H = {Q, Q†}. Examples are Nicolai, Elitzur–Rabinovici–Schwimmer 1982 and Fendley–Schoutens–de Boer 2003 (comparators).
  - SUGGESTED: if Q is transported bulk-locally with H, then H(ε) = {Q(ε), Q(ε)†} ≥ 0 and E_vac(ε) ≡ 0 while SUSY is unbroken. That makes μ_E = μ_T2 = 0 at all orders.
  - But it needs the exact pairing degeneracy.
- **Broken SUSY.** A splitting of (1 TeV)² leaves an R2 residual of |c₂|Δ(m²a²) = 6.8e-36, which is **6e68 times P0**. R2 alone tolerates only |Σw Δm²| ≤ 1.6e-63 GeV².

## 5. Tunings against P0

**P0:** 2 counterterms (E_g and T_2g), each at ≤ 5.7e-99 (refereed) or 9.0e-102 (framework).

**Lane RP, flow coupling:**
- **T_2g:** 0 at the free level, by Liouville. This holds for every species with a separable symbol (V3, proved), including photon option A. Option B would reintroduce a T_2g number (suggested).
- **E_g, free level:** the R0 count plus 3 mass relations, at precisions 1.8e-68, 4.7e-35 and 2.8e-3. SM content fails all four.
- **E_g with interactions:** nothing protects it at O(g²/16π²). So the **E_g counterterm at the P0 level is still needed**: 1 tuning, as in P0. Once it is paid, the free sum rules are redundant.

**Net:** N_tune(RP) ≥ 1 (E_g) and no improvement on P0's E_g. The sum rules relabel the E_g tuning as a Pauli-type naturalness problem. It has the same structure as the cosmological-constant problem: R0 to R4 play the role of the Λ⁴, Λ² and log rules, and it is protected only by unbroken SUSY.

## Against the supervisor's expectation

- **Confirmed:** the leading rule is a count, and the SM fails it; the higher orders need mass relations; interactions break the cancellation at g²/16π²; the reading is FAIL (bounded).
- **Corrected or added:**
  1. The R0 count is 1 KG component per 16 fermionic d.o.f., not a match of bosonic and fermionic d.o.f. Only bosonic doublers restore 8:8.
  2. For taste-singlet symbols the first log is at (ma)⁶, not (ma)⁴. The (ma)⁶ ln rule is needed at physical masses, so there are 4 rules in all.
  3. R4 coincides exactly with Pauli's Str M⁴; R2 does not.
  4. The photon's μ_E is nonzero in both coupling options. Option B (metric) is 132 times option A per polarization.
  5. Lattice SUSY is not wholly absent: a nilpotent H = {Q, Q†} is allowed and would protect μ. It fails on the degenerate-spectrum requirement, not on Kato–Sakamoto–So.

## Labels

- **PROVED** (same family, unrefereed):
  - the IBP formula and F;
  - the species maps;
  - c₆L = 1/(384π²) and why there is no M⁴ ln M;
  - the naive sin p coefficient −1/(2π²);
  - the R0 count, the per-order weights and the pairing solutions;
  - the O(λ) Hartree result as a pure mass shift.
- **CHECKED:** every number in §§1–3, including the two independent methods and the V3 and referee values.
- **ARGUED:** photon option A = 2F(0), through the Poynting/canonical equivalence; massive vector = 3F(M).
- **SUGGESTED:**
  - the size of the O(g²) breaking (κ = O(1), not computed);
  - nilpotent-SUSY protection;
  - option B reintroducing T_2g.
- **READING:**
  - the normalization identification with P0's μ;
  - the use of low-energy masses in R2 and R4;
  - the Dirac-proxy split of staggered tastes;
  - the qubit-per-site remark.

**Not done:**
- an O(g²) computation of μ_E;
- a gauge-invariant numerical construction of the photon flow;
- Wilson fermions;
- the m⁶ coefficients of G and F_B beyond a fit.
