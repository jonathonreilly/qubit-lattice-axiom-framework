# Campaign C4, lane RF3, probe F3: Z⁴ matter with foliated gravity at a separate UV scale M_*

**Who and when.** Claude Opus 5.5 (same family as the supervisor), 2026-10-11, 17:10Z to about 17:40Z. Not refereed. No repository file was edited.

**Where things are.** Scratch folder `scratchpad/C4/F3/`:
- `scripts/f3_numbers.py` / `.out`: Pospelov–Shang bounds, healthy window, hierarchy sizes, dimensional-transmutation couplings.
- `scripts/f3_tadpole.py` / `.out`: the z=3 lattice graviton's self-feed into its own speed coefficient, Z⁴ tick against continuous time.
- `scripts/f3_species.py` / `.out`: the species count needed to bend the graviton at M_*.
- `downloads/hv2307/`: Herrero-Valea's review (2307.13039). Text extracted only; never executed.

**Labels.**
- **proved:** complete within its stated class.
- **checked:** computed here.
- **suggested:** an argument, not computed.
- **reading:** an interpretation.
- **comparator:** literature.
  - **V:** verified in fetched text. Full text for Pospelov–Shang 1010.5249, Liberati–Maccione–Sotiriou 1207.0670 and Herrero-Valea 2307.13039 §II, §IV D, via an extraction tool. Abstract only for 1109.4495, 1007.3503 and 1505.04130.
  - **M:** from memory.

**Read first.**
- MINIMAL_AXIOMS (full).
- `scale_reference_primitive`: a⁻¹ = M_Pl as a units conversion; a = l_P is not derived.
- `kinetic_isotropy_primitive`: the matter regulator block is hypercubic, so ξ = 1 for matter is an approved primitive.
- TESTS.md: lane RF3 and the C4 first-wave results.
- F1 and F2, with their referees.
- I3's referee.
- E1, with its referee: "graviton–matter speed matching is an independent unresolved cost"; "the TT stiffness is a relevant, UV-dominated c-number".

---

## 0. Bottom line in plain words

1. **The Pospelov–Shang mechanism is real, with tighter numbers on one grid.** Lorentz violation in the gravity sector reaches matter suppressed by (M_*/M_P)².
   - With PS's own one-loop formula and the grid as the UV cutoff, the 1.4 PeV photon-decay bound gives **M_* ≲ 1e10 GeV**. That is L = M_Pl/M_* ≳ 1.1e9 (non-reduced M_P) or ≳ 6e9 (reduced).
   - PS's stated 1e-20 level gives M_* ≲ 2e9 GeV.
   - The healthy-Hořava condition M_* < M_SC is then easy to meet: α ≳ 2e-12 suffices, inside the PPN window α ≲ 8e-7.
   - **Condition (V):** every graviton component must be softened above M_*. PS's uncured vector sector leaves a term Λ_UV²/(24π²M_P²). On one grid Λ_UV = 1/a = M_Pl, so that term is about 4e-3, which kills the mechanism.

2. **On one grid the separation is a hierarchy that has to be written into the law.** It costs one of three things:
   - a gravity-law coefficient ratio L⁴ ≈ 4e35–1e39;
   - a coarse gravity length L ≈ 1e9 sites;
   - about 1e20 light species.

   **Dimensional transmutation makes a 1e-9 scale naturally**: an SU(3) or SU(2) gauge sector with α_h ≈ 0.03–0.04 at the grid scale. **But it cannot hand that scale to the graviton.** The graviton couples with 1/M_P, so a sector at Λ_h bends the graviton only at relative size ~N Λ_h²/(16π² M_P²). And M_*/M_P = √G is the Lifshitz-marginal coupling's *value*, not a scale where some coupling runs strong.

   The one natural DT version makes the foliation spontaneous: a khronon condensate with α, β ~ (Λ_h/M_P)², which is in the window for free. That keeps full diffeomorphism gauge symmetry, so it is not an RF realization; it reduces to the P0 setting.

3. **The matter sector on Z⁴ (ξ = 1) does not escape the C3/K2 question; it relocates it.**
   - The separate scale protects matter *from* gravity (the PS direction).
   - It does nothing for the reverse direction. Grid-scale matter loops feed the graviton's masses (P0) and its non-gauge-invariant forms at the grid scale, unsuppressed, unless the interacting Z⁴ stress is exactly conserved. That is RK2's K2.
   - **The dominance reading:** if K2 passes, W(B4) plus gauge invariance protects c_T and kills the masses without any foliation, so RF3 is superseded by lane K. If K2 fails, RF3 inherits the failure plus the hierarchy.

4. **F3 reading against the fixed RF3 lines: FAIL (bounded).** Every examined one-grid RF realization needs a hierarchy beyond P0. Details in §4.

---

## 1. Literature: the constraints on a separate gravitational LV scale M_* (comparator, V unless marked)

### 1a. Pospelov–Shang (PRD 85, 105001; 1010.5249; V)

**Set-up.** A Lorentz-invariant SM (dimension ≤ 4) coupled to Hořava–Lifshitz gravity, which turns z = 3 above Λ_HL ≡ M_*. The abstract says the transmission of LV is "protected by the ratio Λ_HL²/M_P²". A wide separation then keeps SM LV within bounds without fine-tuning.

**One-loop result (eq. 55, as extracted).**

δc²_γ − δc²_φ = −[Λ_HL²/(12π²M_P²)]·ln(Λ_UV²/Λ_HL²) − [(3λ+1)/(3λ−1)]·[Λ'²/(24π²M_P²)]·ln(Λ_UV²/Λ'²) − **Λ_UV²/(24π²M_P²)**,

where Λ' = (αλ̃)^{−1/4} Λ_HL.

- The last term comes from the vector (shift) graviton: ⟨v v⟩ = −2/k² does not soften.
- PS cure it by adding (2/Λ²)(∇_iK^{ij})(∇^kK_{kj}), which makes every term logarithmic (eq. 59).
- **Their scale:** "Λ_HL ≲ 1e10 GeV", for dimension-4 LV "more stringent than 10⁻²⁰". Λ_HL can be as low as the meV scale (sub-mm gravity).
- **On naturalness:** the hierarchy Λ_HL ≪ M_P is *chosen*, not derived. Their naturalness statement is about the SM coefficients given that choice.

**Checked arithmetic (`f3_numbers.out` §1a–1b).**

| δc bound | F2 form, (M_*/M)²/16π²; non-reduced / reduced | PS eq. 55 with Λ_UV = grid = M_Pl; non-reduced / reduced |
|---|---|---|
| γ decay, 2.7e-19 (lattice sign) | 8.0e10 / 1.6e10 GeV | **1.07e10 / 2.1e9 GeV** (log factor 42–45) |
| PS's 1e-20 | 1.5e10 / 3.1e9 | 2.0e9 / 3.8e8 |
| GZK p/γ, 4e-23 (one sign) | 9.7e8 / 1.9e8 | 1.2e8 / 2.3e7 |

- **So L = M_Pl/M_* ≳ 1e9 to 6e9 for the photon-decay bound with PS's coefficient.** F2's 1.5e10 GeV used the smaller coefficient 1/16π² without the log; the log makes the bound about 7× stronger.
- **The uncured vector term with Λ_UV = M_P is 1/(24π²) = 4.2e-3** (checked). That exceeds every matter bound by 16–20 orders.

### 1b. The healthy-Hořava requirement M_* < M_SC (V: GSS via F1, and the review §II)

- **GSS eq. 15:** M_SC ≈ √α·c_S^{−1/2}·M.
- **The review (2307.13039, V):** "M_* ≪ Min{√η M_P, √|λ−1| M_P}", with M_* < 1e15 GeV from solar-system λ.
- **Checked (γ_G = 0.01).** M_* = 1.5e10 GeV needs α > 2.4e-12; M_* = 2e9 GeV needs α > 1.7e-13. So the healthy window for α is roughly [2e-12, 8e-7] (weak PPN). It is nonempty, so PS and BPS are compatible.

### 1c. Matter's own LV scale must be separate (Liberati–Maccione–Sotiriou, PRL 109, 151602; V)

- **Crab synchrotron:** M_LV ≳ 2e16 GeV for dimension-6 electron operators (CPT and P assumed). This is "incompatible with the possibility that M_LV ∼ M_*".
- **Their conclusion:** a percolation-suppression mechanism must exist, and it must work for higher-order operators too.
- **The review's window** 1e11 < M_* < 1e15 GeV takes the GRB dimension-6 lower bound by *assuming* M_* percolates into matter. With Z⁴ matter, matter's dimension-6 scale is the grid's (~√6·M_Pl), which passes Crab. So the 1e11 lower bound does not apply to RF3 (reading).
- **Correction to the review (reading).** Its eq. 118 claims that 1e-16 < M_*²/M_P² < 1e-8 is "small enough to bypass all experimental constraints". That conflicts with PS's own coefficient: photon decay needs M_*²/M_P² ≲ 8e-19 non-reduced (§1a).

### 1d. The other names in the brief

- **Pujolàs–Sibiryakov, "Supersymmetric Aether"** (JHEP 1201:062, 1109.4495; V abstract). This is the Groot Nibbelink–Pospelov route: an LV aether sector that keeps the SUSY generators, so dimension-4 LV in a SUSY visible sector is forbidden, and soft breaking reintroduces it suppressed. F2 (refereed) records that the standard super-Poincaré protection is not established on Z³; not pursued here.
- **Kharuk–Sibiryakov, "Emergent Lorentz invariance with chiral fermions"** (TMF 189 (2016) 1755, 1505.04130; V abstract). Holographic strong flows from an LV UV to an approximately Lorentz-invariant IR. This is lane RE's mechanism. RE's E1 is refereed FAIL (bounded) for the gravity side, and it does not bear on M_*.
- **The quoted PS bound "M_* < 1.5e10 GeV"** is correct only as F2's arithmetic. As a literature statement it is PS's "≲ 1e10 GeV", and on one grid the eq. 55 coefficient tightens it to about 1e10 (non-reduced) or 2e9 GeV (reduced) for the photon-decay bound (checked).

---

## 2. One grid: can matter at a and gravity at M_* ≈ 1e-9/a coexist?

**What is required (proved, elementary).** With a⁻¹ = M_Pl and G_N = a² (the primitive's target), the gravity sector must have:
- Planck stiffness;
- O(1) Lorentz violation in its own propagator at M_* = a⁻¹/L, with L ≈ 1e9;
- a propagator *softer* than Lorentz-invariant above M_*, for every component (§1a condition V).

The Lifshitz-dimensionless gravitational coupling at the crossover is then G(M_*) = (M_*/M_P)² = 1/L² ≈ 1.5e-18 (checked).

### R1. A fine-lattice gravity field with z = 3 terms (Hořava on the grid)

1. **Hierarchy (checked).** For c_T = c = 1 with matter, ω² = k² + k⁶/M_*⁴ needs the z = 3 coefficient to be **L⁴ ≈ 4.4e35** in lattice units (1.4e39 at M_* = 2e9). The PS vector term ∇K∇K needs the same. The alternative, a natural z = 3 coefficient with a z = 1 coefficient of L⁻⁴, makes c_T ≈ 1e-18. So the large number cannot be moved elsewhere.

2. **On the Z⁴ tick, with quasi-energy ≤ π/a (checked arithmetic, suggested physics).**
   - The real-time z = 3 regime fits only up to k_max = (πM_*²/a)^{1/3} ≈ 2e13 GeV ≈ 1.7e-6/a.
   - Above that, modes are frozen: the Euclidean propagator ≈ 1/(L⁴k⁶). It is still soft, so PS suppression of gravity → matter survives.
   - z = 3 needs range-3 spatial stencils, so nearest-neighbour only with auxiliary fields.

3. **The gravity sector's own loops do not keep its IR parameters natural (checked, `f3_tadpole.out`; one component, O(1) combinatorics dropped, so suggested as physics).** The seagull from the z = 3 vertex feeds the z = 1 (speed) coefficient by:

   | Regulator | Feed into the z = 1 coefficient |
   |---|---|
   | Z⁴ tick | **0.251**, independent of L for L ≥ 10³ (the frozen modes' 1/p̂² Brillouin-zone integral) |
   | continuous time (Z³ × ℝ) | 1.194·L², i.e. **7.9e17** at L = 8.1e8 |

   - In continuum Hořava with dimensional regularization, α, β and λ − 1 run only as G·ln, so small values are stable. On a grid where gravity's modes reach a, that stability is lost.
   - β = c_T² − 1 has natural size O(0.1–1) (Z⁴) or 1e18 (continuous time). It needs tuning to 1e-15: about 4e-15 or 1e-33 of natural size.
   - That is F1's β tuning, made no milder (Z⁴) or much worse (continuous time).

### R2. A coarse-cell graviton (I3's route: the anomaly moves from a to ℓ = La)

1. **What the cells buy (reading, from refereed I3).** Coarse cells *are* the wanted outcome for gravity: its lattice-scale LV moves to ℓ = 1/M_*. If the graviton has no modes above π/ℓ:
   - gravity's self-loops give δβ ~ M_*²/(16π²M_P²) ≈ 1e-20, so the IR parameters are natural;
   - gravity → matter is PS-suppressed.

   This is the most favourable RF3 realization.

2. **What sets L ≈ 1e9 (suggested).**
   - **(i) An explicit cell size in the law.** A dimensionless 1e9 in the gravity law, not nearest-neighbour except through about 1e9 layers of auxiliaries.
   - **(ii) A spontaneous superlattice of period L.** A translation-covariant nearest-neighbour rule generically orders at wavevector O(1/a). In Landau theory Q² = −c₂/(2c₄), so Q ≈ 1e-9/a needs c₂/c₄ ≈ 1e-18: a tuning to a Lifshitz point (comparator, M).
     - A modulated medium also *folds* the graviton band; it does not soften it. The LV part of the propagator then persists from M_* up to 1/a. That is PS's uncured-term situation, δc ~ V/(16π²) for modulation depth V (suggested).
     - The long-wavelength speed shifts at O(V²) (harmonic-mean stiffness), with no a/ℓ suppression (suggested).
   - **(iii) A correlation length from dimensional transmutation,** ξ_c = a·e^{2π/(b₀α)}. Natural, but see R3: the graviton cannot be tied to it.

3. **Matter → gravity is not suppressed by the cells (suggested).** ⟨T_cell T_cell⟩ contains fine matter momenta up to 1/a. So P0's TT masses (unless the interacting Z⁴ stress is exactly conserved, i.e. K2) and the graviton–matter speed match (E1, refereed: an independent cost; GW170817 at 1e-15) are inherited at the grid scale. Nothing ties the coarse law's c_T to matter's c.

### R3. Dimensional transmutation, investigated seriously

1. **A natural 1e-9 scale exists (checked, `f3_numbers.out` §2b).** Λ_h/M_Pl = 1e-9 needs α_h at the grid scale of:

   | Gauge sector | 1-loop α_h | 2-loop α_h |
   |---|---|---|
   | SU(2) | 0.041 | 0.038 |
   | SU(3) | 0.028 | 0.026 |
   | SU(3) + 6 flavours | 0.043 | 0.041 |
   | SU(5) | 0.017 | 0.015 |

   The sensitivity is d ln Λ/d ln α = 20.7, with no fine-tuning. (QCD itself does this at 1e-20.)

2. **Why it does not give M_* (suggested; three independent obstructions).**
   - **(a) The wrong kind of small number.** M_*/M_P = √G(M_*), and G is the *marginal* Lifshitz coupling. It runs logarithmically: 1/G changes by b·ln(…) ≲ 50 between a and M_*. So G ≈ 1.5e-18 at M_* means G ≈ 1.5e-18 at a. DT turns O(0.03) couplings into exponentially small *scales*; it does not make a coupling 1e-18. The other route to M_*, the z=1/z=3 coefficient ratio, is a relevant ratio with power-law (not logarithmic) flow (R1.3).
   - **(b) A light sector cannot bend the graviton.** The graviton couples with 1/M_P. A sector with N species, or central charge C_T, changes its quadratic action by ≲ N k² ln/(1920π² M_P²) relative, for conformal scalars. O(1) bending at k = M_* needs **N ≈ 1e19–1e22** (checked, `f3_species.out`; one-loop power counting, O(1) tensor factors dropped). Below its own scale a massive sector induces only local terms ∝ N/(16π²Λ_h²), negligible at k ≪ Λ_h and non-local above it.
   - **(c) A composite graviton of the DT sector.** Its stiffness is ~C_T Λ_h²/(16π²), which needs the same ~1e20. Weinberg–Witten forbids it outright if the hidden sector is Lorentz-invariant; an LV hidden sector evades WW but not the count.

3. **The one natural DT version: a spontaneous foliation (suggested).** A khronon formed as a condensate of an asymptotically-free sector, with f ~ Λ_h ≈ 1e10 GeV.
   - **What it gives:**
     - α, β ~ (Λ_h/M_Pl)² ≈ 1.5e-18, inside the F1 window with no tuning;
     - PS percolation ≈ 1e-20;
     - the khronon EFT's strong coupling at √α·M_P ~ Λ_h is resolved by the hidden sector itself, so no z = 3 is needed (checked arithmetic).
   - **But the foliation is a field, not a gauge choice.** The gauge algebra is full diffeomorphisms. So this is not RF: C3 applies as in GR. The graviton on the grid is P0's setting, with the P0 tunings and the E1 c_T match.
   - **Reading:** DT works here only by giving up the property RF was opened for. It reduces to P0 with a harmless extra sector.
   - **Not shown:** a qubit, nearest-neighbour, asymptotically-free 3+1 gauge sector (quantum links are not shown to have a 3+1 AF continuum limit with qubit links: comparator, M).

**R3 reading.** In the examined classes, dimensional transmutation supplies a natural Λ_h ≈ 1e-9 M_Pl, but no mechanism transfers it to an *explicit*-foliation graviton with Planck stiffness without about 1e20 species. Bounded to one-loop and spectral power counting. This is not a theorem.

### Price if the hierarchy is simply supplied (reading)

Either:
- **two grids:** gravity on a lattice about 1e9 times coarser. That is a Lattice-axiom change, and conflicts with "one fixed nearest-neighbour admissibility rule" on one Z³; or
- **a 1e35–1e39 coefficient** in the gravity law. The F2 referee: "a fair lattice-unit price … not an axiom contradiction or automatically a 1e-36-precision tuning".

Moving the grid scale away from M_Pl (a scale-reference change) does not help. RF3 needs M_* ≪ M_P whatever a is, and Crab needs matter's LV scale ≳ 2e16 GeV.

---

## 3. Matter on Z⁴ at ξ = 1: does it still face C3/K2? (dependence noted, not computed)

- **Dimension 4: protected (comparator, refereed F2).** W(B4) maps time coefficients onto space coefficients, giving Δ(ξ = 1) = 0 exactly. Gravity's W(B4) breaking reaches matter only via PS, at (M_*/M_P)².
- **The separate scale does not touch the reverse direction (suggested; consistent with refereed E1 §3).** Grid-scale matter loops feed the graviton at the grid scale:
  - the TT masses: P0, a "relevant, UV-dominated c-number" (E1 referee);
  - the non-gauge-invariant W(B4) forms: lane K's 5;
  - the c_T match.

  Whether these vanish depends on whether the interacting Z⁴ stress is exactly conserved and gauge-covariant. That is **RK2's K2**: the discrete-time analogue of C3, exact linearized lattice diffeomorphisms with matter, and reflection positivity at ξ = 1 (K7a: leapfrog unstable at the hypercubic tick).
- **FDiff closure (suggested).** F1's surviving C3 sector is the rotation bracket inside {H_i, H_j}. It is a spatial statement, and Z⁴'s slices are Z³, so RN L2's "no exact momentum for interacting single-band matter, d ≥ 2" (refereed) applies slice by slice. Discrete time does not remove it. This depends on K2 and RM (composites) for the classes those referees left open.
- **Dominance (reading).**
  - **If K2 PASSES:** exact gauge invariance plus W(B4) leaves 1 of 9 O(q²) forms, the Lorentz-invariant one (lane K's exact count). That protects c_T = c and kills the masses with no foliation and no hierarchy. RF3 is superseded by lane K.
  - **If K2 FAILS:** RF3 inherits that failure (P0 masses, anisotropic forms, speed match) and adds the hierarchy.

  In neither case does the separate foliated scale buy anything on the matter–gravity coupling. Its only gain is the PS protection of matter from *gravity's own* LV, which Z⁴ gravity would not need.

---

## 4. Verdict against the FIXED RF3 readings

| Realization | Bounds | Hierarchy / tunings | Reading |
|---|---|---|---|
| **R1** fine-grid Hořava field (z = 3 + vector term) | PS met if M_* ≲ 1e10 / 2e9 GeV and every component is softened; healthy window α ∈ [2e-12, 8e-7] | coefficient L⁴ ≈ 4e35–1e39; β natural O(0.25) on the Z⁴ tick (1e18 in continuous time), so a 1e-15 tuning (F1's) not made natural; P0 masses unless K2 | **needs a hierarchy beyond P0: FAIL** |
| **R2** coarse-cell graviton, L ≈ 1e9 | PS met; IR parameters natural from gravity's own loops | L as law content, or a superlattice tuned near a Lifshitz point (c₂/c₄ ≈ 1e-18, which also folds rather than softens the propagator); P0 masses and c_T match from fine matter unless K2 | **needs a hierarchy beyond P0: FAIL** |
| **R3** dimensional transmutation tied to an explicit-foliation graviton | — | ~1e19–1e22 species (or C_T) to bend the graviton at M_* | **a hierarchy in species count: FAIL** (suggested bound) |
| **R4** spontaneous khronon from a DT condensate | α, β, PS natural (≈ 1e-18 to 1e-20) | none beyond P0 + E1's c_T match | **not an RF realization** (diffeomorphism algebra kept, C3 as in GR); reduces to P0 (reading) |

**F3 reading: FAIL (bounded)**, under the clause "needs a hierarchy or tuning beyond P0":
- for every examined one-grid realization with an *explicit* (grid) foliation, R1–R3;
- with R4 outside the lane.

**Referee-sensitive points, stated up front:**
1. The verdict counts a large dimensionless number in the gravity law (L⁴ or L) as "a hierarchy". That is the registered expectation's wording; F2's referee distinguished it from a precision tuning.
2. The DT exclusion (R3) is one-loop and spectral power counting, labelled suggested, not a theorem.
3. The FAIL does not rest on K2. The hierarchy clause suffices. The P0-inheritance statements are conditional on K2.
4. The seagull feed (R1.3) is a single-component power count. The Z⁴ value 0.251 is a Brillouin-zone integral (checked); the tensor combinatorics are not computed.

**Against the supervisor expectation.** "A separate M_* needs the gravity sector to see a coarser effective lattice than matter, roughly 1e9 times coarser. On one grid that is a hierarchy, i.e. a tuning." **Confirmed and sharpened:**
- L ≈ 1.1e9 (non-reduced) to 6e9 (reduced), from PS's own coefficient with the grid as the UV cutoff;
- every graviton component must be softened, or PS's vector term (4e-3) kills it;
- DT gives the scale but cannot transfer it without about 1e20 species;
- the only natural DT version (spontaneous foliation) leaves RF.

**Not expected:**
- **The dominance:** RF3 is never better than lane K on the matter–gravity coupling.
- **R1's lost naturalness:** in R1, gravity's own grid-scale modes keep β at natural O(0.1–1) on the Z⁴ tick. So PS-style naturalness of the IR parameters holds only for coarse-cell gravity (R2).

## 5. Strong-word check

- **"proved":** only the elementary requirement statements in §2 (G(M_*) = (M_*/M_P)², and that c_T = 1 forces the large coefficient onto the z = 3 term). Everything else is checked arithmetic, suggested, reading or comparator.
- **"checked":**
  - the PS / healthy / DT / species arithmetic;
  - the tadpole Brillouin-zone integrals at n = 96³, where the 0.2513 limit equals mean(1/p̂²).
- **Comparator caveats:**
  - PS eq. 55 was transcribed by a summarizing fetch tool. The referee should check the coefficients (1/12π², 1/24π²) and PS's M_P convention.
  - The Liberati et al. numbers were extracted the same way.
- **Not done:**
  - an explicit lattice PS computation with Z⁴ matter;
  - the superlattice folding numerics;
  - an explicit hidden-sector induced z = 3 computation;
  - K2 (RK2's job).

Sources:
- [Pospelov–Shang 1010.5249](https://arxiv.org/abs/1010.5249)
- [Pujolàs–Sibiryakov 1109.4495](https://arxiv.org/abs/1109.4495)
- [Kharuk–Sibiryakov 1505.04130](https://arxiv.org/pdf/1505.04130)
- [Liberati–Maccione–Sotiriou 1207.0670](https://ar5iv.arxiv.org/html/1207.0670)
- [Herrero-Valea review 2307.13039](https://arxiv.org/pdf/2307.13039)
- [Blas–Pujolàs–Sibiryakov 1007.3503](https://arxiv.org/abs/1007.3503)
- GSS 1711.08845 (via F1)
