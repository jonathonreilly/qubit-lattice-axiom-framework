# Campaign C4, lane RW, probe W2: Dirac analysis of linearized VS/N-type gravity with the C3 anomaly

**Who and when.** Claude Opus 5.5 (same family as the supervisor), 2026-10-11, 16:53Z to about 17:30Z. Not refereed. No repository file was edited.

**Where things are.** Scratch folder `scratchpad/C4/W2/`. Scripts are in `scripts/`, each with a matching `.out`:

| Script | What it does |
|---|---|
| `w2_stueckelberg_scalar.py` | Wess–Zumino (WZ) term, scalar spectrum and Krein signs (sympy, exact) |
| `w2_stueckelberg_with_khronon_term.py` | adds the BPS acceleration term α(∇(Φ + π̇))² |
| `w2_gradient_branch.py` | WZ-consistency test of the alternative ultralocal representative |
| `w2_cnumbers_and_rank.py` | vacuum and thermal anomaly sizes; rank of the bracket matrix on backgrounds |
| `w2_extra_checks.py` | the vacuum identity, the mode's null vector, and the vacuum-branch scale |

**Labels.**
- **proved:** short algebra, complete in its stated class.
- **checked:** computed here.
- **suggested:** an argument, not computed.
- **reading:** an interpretation.
- **comparator (M):** literature from memory, not re-fetched.

**Inputs used.**
- C3's refereed anomaly: {K_b, P_c} = −δ_bc E_c with E_c − H_m = −¼Σ[(d_cπ)² + d_cφ d_c(ω²φ)]. Its symbol is (cos q_c − 1)ε_q per quantum, and every gravity-dependent completion vanishes in the Killing sector. The rotation bracket uses Q_ca.
- RN L1's setup: the stencils, the linear first-class property, and the uniform-strain seagull.
- The 09-14 note: H_N, G and S.
- F1, unrefereed.

---

## 0. Bottom line in plain words

1. **Which constraints become second class.** On any matter background with excitations, C3's anomaly pairs the Hamiltonian constraint with the momentum constraint.
   - The pairing strength is the background density of excitations' anomaly: a_exc = Σ(cos q_c − 1)ω n_q / V < 0.
   - It is **irreducible**. C3's Killing-blindness covers every finitely excited state, so no completion removes it.
   - **Checked** (6³ torus, C3's representative): rank **416/864**, i.e. about 2 second-class constraints per site, for homogeneous or inhomogeneous excited matter; up to **800/864** when the matter carries a current (the rotation anomaly).
   - No secondary constraints arise. Instead, preservation fixes the multipliers: **the lapse becomes projectable** (∂_c n = 0 wherever 𝒜_c ≠ 0), and the longitudinal shift is fixed.
   - **Mode count:** 2 TT + about 1 scalar per site, rising to about 1.85 with currents.
   - In the bare vacuum, the excitation part is zero. The vacuum's own c-number is a separate counterterm question (item 3).
2. **The extra scalar is a ghost.** Restore the broken directions with Stückelberg fields: π for time (khronon-like) and ζ for longitudinal space. The anomaly fixes their WZ term **uniquely** (checked):

   L_WZ = a[∇B·∇π − ∇ζ·∇Φ + ∇ζ̇·∇π − ½(∇π)²].

   - The transverse (vector) Stückelbergs drop out identically (proved).
   - With linearized GR there is exactly one extra mode: **ω² = a k²/(3a − 2M_P² k²)**.
   - **a < 0** (the physical sign of the excitation anomaly): a **ghost at every k**. It is gapless for k² < 3|μ|² (ω² ≈ k²/3), and above that its band flattens to ω² → |μ|² = 4πG|a|.
   - **a > 0:** a ghost below √3μ and a **tachyon** above.
   - The mechanism is Boulware–Deser's. The second-class Hamiltonian constraint no longer fixes the conformal mode: on the extra mode, Ψ = −(a/2M_P²)ζ (checked).
   - The BPS acceleration term does not cure it. Φ + π̇ ≡ 0 on the mode, and the spectrum is independent of α (checked, at λ = 1).
3. **Sizes, with the anomaly in units of energy density.**
   - **Tree level / IR:** each quantum carries (cos q_c − 1)ω ≈ −(q_c a)²ω/2. Thermal: a_T/ρ_T ≈ −3.2(Ta)² for massless matter (checked).
   - **Loops:** the zone average of (cos q_c − 1) is exactly −1 (checked).
   - **Vacuum (checked, exact):**
     - ⟨E_c⟩_vac = −⟨T_cc⟩_vac, a total q-derivative.
     - So the vacuum c-number ⟨E_c − H⟩/V = −(ρ + p)_vac = −1.30 per site at m = 0, and the lattice vacuum has w = +0.09, not −1.
     - Whether the counterterms that make flat space static (energy ρ, and pressure p as a separate counterterm since w ≠ −1) also absorb this c-number is **not settled**. The identity suggests the natural stress completion does (suggested).
     - If it is not absorbed, the extra scalar is a gapless ghost at the Planck scale: |μ| ≈ 4.0/ℓ, and √3|μ| ≈ 7/ℓ exceeds the zone edge π/ℓ.
4. **Observational status.**
   - **Robust branch** (excited matter, with the vacuum c-number absorbed):
     - μ² = 4πG|a_exc| ~ H²(Ta)². For example |μ| ≲ 1e-32 H₀ in the CMB (≈ 3e-34 H₀ from μ²/H₀² ≈ 4.8(Ta)²Ω_γ).
     - The ghost has negative energy, but it is light and its phase space is tiny.
     - Its kinetic normalization ∝ a_exc → 0 near the vacuum, and the mode count jumps from 2 (vacuum) to 3 (any excitation). So it is strongly coupled; perturbation theory fails above roughly the local temperature (suggested).
   - **Vacuum branch** (c-number not absorbed): a gapless Planck-normalized ghost coupled through the lapse. Vacuum decay is then unsuppressed, and this is excluded (suggested; Cline–Jeon–Moore-type bounds, M).
   - **In neither branch does the mode decouple.** It is light where it is tuned and gapless where it is Planckian.

**W2 reading against the FIXED line: FAIL (bounded; must go to the codex referee).** An extra scalar ghost (a ghost plus a tachyon for the other sign) appears at the order computed, in every background with matter excitations. The supervisor's escape clause, "Planckian mass and decoupling ⇒ INCONCLUSIVE", is not realized.

---

## 1. Dirac analysis: second class, secondary constraints, mode count

### 1a. The irreducible anomaly (proved: C3's certificate plus the completion ideal)

**Constraints.**
- C_s = S(q)/κ_s + T00 + λT00⁽¹⁾[h, E; φ, π]
- C_j = −(J/κ_s)G_j(E) + P_j + λP_j⁽¹⁾

**Completions.**
- An h-dependent completion enters {C_c[ξ], C_s[N]} only through Gᵀξ, the symmetric gradient of ξ.
- An E-dependent completion enters only through SᵀN, the second differences of N.
- Both vanish for constant ξ and linear N.

**What survives.** The irreducible content is C3's exact Killing coefficient: **Δ[ξ, N] = −Σ_c∫ξ_c(∂_cN)𝒜_c**, where 𝒜_c is the local density of E_c − H_m.

**Rotation sector.**
- The antisymmetric gradient is not in the completion ideal.
- So Δ_rot[ξ, η] = ∫(ξ_c ω_ca[η] − η_c ω_ca[ξ])ℛ^A_ca. Here ω[η] is the antisymmetric gradient, and ℛ^A has symbol ∝ (cos q_c − 1)sin q_a, antisymmetrized.

**{C_s, C_s}:** closes exactly (L1, refereed).

**Which part is irreducible.**
- For the **excitation (normal-ordered) part**, C3's Killing-blindness applies as proved: the fields of a finitely excited state are compactly supported, so no completion contributes there.
- For the **vacuum c-number part**, boundary terms of the linear smearings do not vanish (vacuum fluctuations fill space). So a c-number h-completion can contribute there, and the argument does not fix it (§1c).

**The alternative ultralocal representative is rejected (checked, `w2_gradient_branch.out`).**
- Rewriting modulo the ideal as ∫ξ_c N ∂_c𝒜_c is tempting, but with a background gradient it is **not Wess–Zumino consistent**: the term ε₂∂ε₁ − ε₁∂ε₂ is not a total derivative.
- No local WZ term in a 12-term ansatz exists.
- So it cannot stand as a cocycle on its own, and C3's form is used throughout.

### 1b. Bracket matrix on backgrounds, and its rank (checked: `w2_cnumbers_and_rank.out` (B2))

Evaluate on a background with densities 𝒜_c(x) and ℛ^A(x) (mean field). Then:
- M_cs(x, y) = −𝒜_c(x)·(D_c)_xy;
- M_ab is the rotation form;
- M_ss = 0.

On a 6³ torus there are 4N = 864 constraints. The count uses dof per site = 2 + rank/(2N).

| Background | rank | dof per site |
|---|---|---|
| vacuum after the vacuum counterterms (𝒜 = 0) | 0 | 2 (GR) |
| homogeneous excited matter (𝒜 const ≠ 0) | 416 | 2.96 |
| modulated or generic inhomogeneous excited matter | 416 | 2.96 |
| homogeneous beam (current), 𝒜 const | 624 | 3.44 |
| beam + inhomogeneous 𝒜 | 800 | 3.85 |

- The rank deficit for 𝒜 ≠ 0 comes only from the momenta where every sin p_c = 0, i.e. the global charges plus the zone corners.
- **The pair.** Without a current, the pair is C_s(p) and p̂·C(p), where p̂_c ∝ 𝒜_c sin p_c. The two components of the momentum constraint perpendicular to it stay first class. A current also pairs the transverse components.

**Secondary constraints (proved, elementary).** None arise where the pairing is invertible. Preservation fixes the multipliers instead:
- Ċ_c ⊃ −𝒜_c ∂_c n forces **∂_c n = 0**: the lapse becomes projectable, n = n(t).
- Ċ_s ⊃ 𝒜_c ∂_c N_c fixes the longitudinal shift.

This is the Gambini–Pullin / Bahr–Dittrich outcome that C3 flagged as suggested; it is now explicit. The variant in which the lapse is forced to zero (Henneaux–Kleinschmidt–Lucena Gómez, M) belongs to the rejected ultralocal form.

**Reading.**
- The count is 2 at the vacuum and about 3 in any excited state. A count that jumps between nearby backgrounds is the standard signature of a strongly coupled mode around the background where it disappears.
- Examples: Hořava's projectable khronon (Charmousis–Niz–Padilla–Saffin, M) and the Boulware–Deser mode.

### 1c. The vacuum c-number (checked: `w2_cnumbers_and_rank.out` (A1), `w2_extra_checks.out` (1))

**Exact identity (proved and checked, residual 6.6e-17).**
- e_c + p_c = ½⟨∂_{q_c}(sin q_c ω)⟩_zone = 0, where e_c = ⟨E_c⟩/V and p_c = ⟨T_cc⟩ (L1 stress).
- Hence ⟨E_c − H_m⟩_vac/V = −(ρ + p)_vac.

| m | ρ_vac | p_vac | w | −(ρ + p) |
|---|---|---|---|---|
| 0 | 1.1938 | +0.1100 | +0.092 | −1.3038 |
| 0.5 | 1.2216 | +0.1068 | +0.087 | −1.3284 |
| 1 | 1.3000 | +0.0991 | +0.076 | −1.3991 |
| 2 | 1.5687 | +0.0807 | +0.051 | −1.6493 |

**Reading.**
- A static flat vacuum needs the energy (ρ) and the pressure (p) tadpoles cancelled. Since w ≠ −1, these are two separate counterterms, not one GR cosmological constant; the pressure one is preferred-frame.
- The identity says the vacuum's Killing c-number equals minus the vacuum pressure. So the same pressure-type h-completion that cancels the tadpole can absorb it.
- This is consistent with the continuum: there e = ρ = −p, and GR's √h does both jobs.
- **The sign bookkeeping that would make this a proof was not completed.** That bookkeeping decides between:
  - the robust branch: vacuum absorbed, rank 0 at the vacuum;
  - the vacuum branch: rank about 2 even in the vacuum, with a ≈ −1.3/ℓ⁴.

---

## 2. Effective theory: Stückelberg fields and the extra mode

### 2a. Wess–Zumino term (checked: `w2_stueckelberg_scalar.out` (a)–(c))

**Setting.**
- The scalar sector of linearized GR on flat space, with continuum IR symbols (the lattice q̂ is not included).
- L_GR = M_P²[−3Ψ̇² + (∇Ψ)² − 2∇Φ·∇Ψ − 2Ψ̇∇²(B − Ė)]. Gauge invariance is checked.
- Gauge transformations: δΦ = ε̇, δB = −ε + χ̇, δE = χ.

**The anomaly as a variation.** C3's form with background density a gives δS_anom = a∫[∇B·∇ε − ∇χ·∇Φ]. It is WZ consistent: [δ₁, δ₂] gives a total time derivative (checked).

**The WZ term.** With δπ = −ε and δζ = −χ, solving δS_WZ = −δS_anom over a 9-term ansatz gives a **unique** answer:

**L_WZ = a[∇B·∇π − ∇ζ·∇Φ + ∇ζ̇·∇π − ½(∇π)²].**

- Time reparametrization gives the khronon-like π. The longitudinal spatial diffeomorphism gives ζ.
- The transverse ζ_i and the transverse shift drop out, because every term contracts them with a gradient (proved).
- So the boost anomaly adds **no vector** at quadratic order. A current (the rotation anomaly) would; that was not computed.

### 2b. Spectrum, signs, masses (checked: `w2_stueckelberg_scalar.out` (d)–(e), `w2_stueckelberg_with_khronon_term.out`, `w2_extra_checks.out` (2))

**Gauge and fields.** Gauge B = E = 0, leaving Φ, Ψ, π and ζ. The determinant is

det = M_P² a² k⁶ (2M_P² k² ω² + a k² − 3a ω²)/128.

There is **exactly one** extra mode:

**ω² = a k²/(3a − 2M_P² k²)**, with μ² ≡ a/(2M_P²) = 4πG a.

| a | k² < 3\|μ\|² | k² > 3\|μ\|² | Krein energy sign |
|---|---|---|---|
| < 0 (excitations: always; vacuum branch: −1.3/ℓ⁴) | ω² ≈ k²/3 (gapless) | ω² → \|μ\|² (flat band) | **ghost**, every k |
| > 0 | ω² ≈ k²/3 | ω² → −μ²: **tachyon**, rate μ | **ghost** where ω is real |

- **Mechanism.** On the mode Φ + π̇ = 0, and Ψ = −(a/2M_P²)ζ. The conformal mode is dynamical and passes its wrong sign (−3Ψ̇²) to the extra scalar. This is Boulware–Deser's mechanism: the lapse constraint loses its first-class role.
- **The BPS cure fails.** Adding α M_P²(∇(Φ + π̇))², the BPS healthy-extension term, leaves the determinant, the roots and the Krein signs unchanged for α = 0, 1e-3, 0.1 and 1, because Φ + π̇ ≡ 0 on the mode.
- **Not tested:** GR-breaking kinetic terms (λ ≠ 1, β ≠ 0), i.e. F1's khronometric window, where the khronon's own kinetic term could compete.

**Masses and couplings in terms of the anomaly.**
- **Tree / IR:** a_exc ≈ −Σ(q_c a)²ω n_q/(2V). Thermal massless: a_T ≈ −3.2(Ta)²ρ_T, giving μ² ≈ 4πG·3.2(Ta)²ρ_T ~ H²(Ta)².
- **Loops:** the zone average of the per-quantum anomaly is exactly −1 × ω. Its vacuum c-number is −(ρ + p)_vac ≈ −1.3/ℓ⁴. If that is not absorbed: |μ| ≈ √(4π·1.3)/ℓ ≈ 4.0/ℓ (ℓ = ℓ_P), and the gapless window √3|μ| ≈ 7/ℓ covers the whole Brillouin zone.
- **Coupling (suggested estimate).**
  - The kinetic normalization is ∝ a. The couplings to matter run through δ𝒜, an a²-suppressed dimension-6 operator in the IR.
  - This gives a strength g(E) ~ E⁶a²/|a|. With a ~ T⁶a² (thermal), strong coupling sets in at E ~ T. It is infinite at the bare vacuum.

### 2c. Comparison

| Theory | Extra modes / health | Relation to W2 |
|---|---|---|
| Fierz–Pauli → Boulware–Deser (M) | nonlinear: 6th mode, the conformal ghost | **same mechanism**: the lapse constraint stops removing the conformal mode |
| Rubakov–Tinyakov / Dubovsky LV massive gravity (M; Dubovsky abstract verified in F1) | the healthy phase keeps the lapse constraint first-class-like (m₀ = 0); other phases have ghosts or instabilities | W2 has no TT or vector mass (the L1 seagull keeps the TT mass zero at p → 0) but loses the lapse constraint. It is in the unhealthy class |
| Projectable Hořava (RN L3 refereed; F1) | 1 scalar: ghost (λ < 1), tachyon (λ > 1), strongly coupled (λ = 1) | Here the lapse is also projectable, but the WZ term gives the scalar a gradient: a ghost with ω² ≈ k²/3 even at λ = 1 |
| Non-projectable Hořava, Li–Pang / Henneaux et al. (M) | second-class H; inconsistent | the same algebraic fate for the Hamiltonian constraint |
| BPS khronon (F1) | healthy for 0 < α < 2, λ > 1 | its α term does not touch the W2 mode at λ = 1 |

---

## 3. Observational status of the extra mode

**Robust branch: excitations only, vacuum c-number absorbed.**
- **Mass scale:** μ² = 4πG|a_exc| ~ H²(Ta)² or H²(ka)². Examples: ≲ 1e-32 H₀ in the CMB, and roughly 1e-25/t_ff in the solar interior. Not resolvable as a Yukawa range or a fifth force (suggested; static exchange not computed).
- **PPN:** γ and 1/r are L1's O(√κ) results, unchanged. Corrections are O(μ²r²) (suggested).
- **GW polarizations:** a breathing mode could exist, but its normalization ∝ a → 0 in vacuum, so there is no perturbative emission (suggested).
- **Ghost:** its energy is negative (checked sign), but it is light. Vacuum-decay phase space is set by |μ| and is negligible (suggested).
- **Strong coupling:** the main problem. The mode count jumps at the vacuum, and perturbation theory fails above roughly the local temperature (suggested). The fixed bar does not ask about this, but it means the theory is uncontrolled exactly where gravity is tested.

**Vacuum branch: c-number not absorbed.**
- A gapless (c_s² ≈ 1/3), Planck-normalized ghost coupled to matter through the lapse.
- Vacuum decay into ghost + matter or gravitons is then unsuppressed. Cline–Jeon–Moore-type bounds put any Lorentz-violating phase-space cutoff at ≲ MeV (comparator M), against ~M_P here: **excluded** (suggested).
- It does not decouple: the Planck scale is its band top, not a gap.

---

## 4. Reading against the FIXED W2 line

| Fixed criterion | Result |
|---|---|
| PASS: exactly 2 TT, no ghost or tachyon to the order computed | **not met.** About 3 dof in any excited background; the extra scalar is a ghost (a < 0) or ghost plus tachyon (a > 0) |
| FAIL: an extra ghost or tachyon, or an extra mode with anomaly-set mass that violates bounds | **met** at quadratic order in the Stückelberg EFT. This holds for both signs of a and in both vacuum branches, wherever excitations are present |

**W2 = FAIL (bounded).** Refereeing is required before it is recorded.

**Against the supervisor expectation.**
- "Boulware–Deser-type ghost or the khronon": **confirmed as BD-type.** The extra scalar is khronon-like in its fields, π and ζ, but it is the released conformal ghost, and the BPS cure does not reach it.
- "INCONCLUSIVE if Planckian and decoupled": **not realized.**
  - In the robust branch the mass is tiny and the mode strongly coupled.
  - In the vacuum branch the band top is Planckian, but the mode is gapless.
- **Not foreseen:**
  - The exact identity ⟨E_c⟩_vac = −⟨T_cc⟩_vac. It ties the anomaly's loop value to the lattice vacuum's w ≈ +0.09, so a static flat vacuum needs energy and pressure counterterms separately (two CC-level tunings rather than GR's one; reading).
  - The ultralocal rewriting of the anomaly is not WZ consistent.

**Price, if a route must survive.** Any of:
- give up GR's lapse structure (lane RF, F1's cases);
- use matter outside C3's class (lanes RI and RD);
- accept a strongly coupled ghost in every excited background, plus a preferred-frame vacuum-pressure tuning.

None is supplied by the axioms.

---

## 5. Assumptions, scope, strong words, negative-claim record

**Class.** C3's: the fixed 09-14 generators; L1's real single-band free scalar; regular local completions; the O(κ) matter-bilinear brackets. Interacting, multi-band and non-local matter are outside it.

**Representative.** C3's Killing form, the WZ-consistent one, is used for the rank and the spectrum. The alternative ultralocal form fails WZ consistency (checked) and is not used.

**Mean field.**
- The background enters through Gaussian expectations of the bilinears, with the excitation anomaly a treated as constant over a wavelength.
- Not included: matter fluctuations in the Stückelberg sector, loops of the extra mode, and the rotation-anomaly (current) spectrum.

**Gravity.**
- Continuum IR symbols at the GR point (λ = 1, c_g = 1).
- Not included: the lattice q̂ corrections, the khronometric couplings, nonlinear orders.

**Sign map.** The sign relation between C3's bracket and the a in δS_anom was not fixed. Both signs give a ghost, and C3's symbol makes the excitation anomaly negative in every state.

**Open item (main gap).** The vacuum c-number bookkeeping (§1c) decides the vacuum branch. It does not affect the FAIL, which rests on excited backgrounds.

**Strong words.**
- **"proved":**
  - the completion-ideal reduction;
  - the vanishing of the transverse Stückelbergs;
  - the identity e_c + p_c = 0;
  - the multiplier fixing.
- **"checked":**
  - WZ uniqueness and consistency;
  - the WZ inconsistency of the ultralocal form;
  - the spectrum, Krein signs and α-independence;
  - the rank tables;
  - the c-number tables.
- **"suggested":**
  - the strong-coupling scale;
  - the vacuum-decay exclusion;
  - the fifth-force, PPN and GW-polarization statements;
  - absorption of the vacuum c-number by the pressure completion.
- **Comparators from memory:** BD, RT/Dubovsky, Henneaux et al., Li–Pang, Charmousis et al., Cline–Jeon–Moore.

**N1–N8.**
- **N1, routes:**
  1. GR kinetic structure plus the WZ term: ghost or tachyon.
  2. Plus the BPS α term: unchanged.
  3. The ultralocal representative: not a consistent cocycle.
  4. Absorbing the vacuum c-number: open, and irrelevant to excitations.
  5. Projectable-lapse reading: the same scalar.
- **N2:** these routes are branches of one Dirac structure, not independent walls.
- **N3, hidden conditions:** λ = 1, single-band free scalar, mean field. All stated.
- **N4:** the comparators are analogies; the W2 statements rest on the checked computations.
- **N5:** scope is C3's class and quadratic order.
- **N6:** the escapes change the dynamics or the matter class, not the axioms.
- **N7, strongest counterargument:** non-GR kinetic terms (λ > 1, α in F1's window) might give the Stückelberg scalar a positive kinetic term large enough to dominate the conformal-mode admixture of size a/M_P². Not tested. It would put W2 inside lane RF's khronometric question, with F1's tuning costs.
- **N8:** RN L3 and F1's projectable scalar is the closest prior wall. W2's mode differs from it: it is gapless with a WZ-supplied gradient, and it is a ghost even at λ = 1.
