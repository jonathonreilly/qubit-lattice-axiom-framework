# Campaign C4, lane RF, probe F1: the gravity sector with the grid's preferred slicing

**Who and when.** Claude Opus 5.5 (same family as the supervisor), 2026-10-11, 16:23Z to about 16:50Z. Not refereed. No repository file was edited.

**Where things are.** Scratch folder `scratchpad/C4/F1/`:
- scripts in `scripts/`, each with a matching `.out`:
  - `f1_khronometric_window.py`
  - `f1_lattice_foliation_symbol.py`
  - `f1_fdiff_closure_symbol.py`
  - `f1_lattice_only_masses.py`
  - `f1_symbol_lib.py`
- downloaded papers in `downloads/`. These are untrusted data: their text was extracted, they were never executed, and they were read only.

**Labels.**
- **proved:** a derivation complete within its stated class.
- **checked:** computed here.
- **suggested:** an argument, not computed.
- **reading:** an interpretation.
- **comparator:** literature.
  - **V** means verified in fetched text (the full text for GSS 1711.08845, Oost et al. 1802.04303 and Audren et al. 1410.6514; the abstract for the others).
  - **M** means from memory, unverified.

**Own prior art, read first.**
- `OUTSIDE_VIEW.md:47` already states that Hořava's protecting symmetry is spatial diffeomorphisms, "exactly what fixed Z³ breaks".
- `agents/B1_report.md:298` has row V: foliated theories pay with GW170817 and with Collins.
- RN L3 §4b–4c (refereed) covers the projectable scalar and notes that Hořava still needs an exact momentum.
- The 09-14 SOFT_SPIN2 note reconstructs an Einstein-aether quadratic example.

F1 makes these statements quantitative and lattice-explicit. It does not overturn them.

---

## 0. Bottom line in plain words

1. **The literature window exists and is narrow** (comparator, V). For the khronometric theory, the infrared limit of the healthy Hořava extension, the surviving region is:
   - |β| ≲ 1e-15 (GW170817);
   - 0 < α ≲ 8e-7 with weak-field PPN bounds, or ≲ 3e-9 if the pulsar α̂₂ bound is applied (a reading, since sensitivities are not included);
   - 0 < γ_G = λ − 1 ≲ 0.095 (BBN);
   - c_S unconstrained beyond the condition c_S ≥ 1.

   The α = β = 0 corner is observationally GR-like: pulsar sensitivities vanish, so there is no dipole radiation. But its khronon is strongly coupled at low energy. Einstein-aether has the analogous window: |c13| ≤ 1e-15, 0 < c14 ≤ 2.5e-5, c14 ≲ c2 ≲ 0.095.

2. **In the gravity sector alone, the lattice reproduces the healthy theory exactly** (checked). Take the 09-14 lattice tensor theory, keep the vector constraint exact, and demote the lapse from a gauge multiplier to a field with a gradient term α|∇n|². Its quadratic spectrum on the lattice symbols is then BPS/khronometric:
   - TT: ω² = Jg q̂²;
   - khronon: c_S² equals the GSS formula to machine precision at every k, including k at the zone scale;
   - G_N ∝ 1/(1 − α/2);
   - PPN γ = g_n/(2g).

   With a projectable lapse, the scalar is RN L3's ghost or tachyon again (checked).

3. **The slicing removes only half of C3's obstruction.** The grid supplies a preferred slicing and also a preferred spatial grid. Hořava and khronometric gravity tolerate the first but need the second to be absent: they keep spatial diffeomorphisms (FDiff = Diff(Σ) × time reparametrization).
   - C3's boost relation is no longer required as a Lorentz statement.
   - **C3's rotation sector lies entirely inside the spatial-diffeo algebra {H_i, H_j}, so it survives.** This is proved in C3 and refereed. The residual is re-checked here: nonzero at every stencil range tested.
   - In the healthy, non-projectable version, C3's linear-lapse bracket comes back as "the momentum constraint must transport the lapse field" (suggested). Its weight W = Hess u(q) has zone average 0 instead of 1 (checked).
   - Interacting single-band matter has no exact momentum at all (RN L2, refereed, d ≥ 2).

   So regular local finite-band lattice matter closes only with the grid's discrete symmetries plus time, not with FDiff.

4. **With only the lattice's symmetries, the preferred-foliation theory is Lorentz-violating massive gravity, i.e. P0 made explicit.**
   - Cubic symmetry allows 6 O(k⁰) mass numbers on (h_ij, n, n_i) (checked by group average): μ_A1, μ_E, μ_T2, μ_n, m4 and μ_1.
   - In the static sector, each of μ_A1, μ_E, μ_n and m4 separately destroys either the Newtonian 1/r pull or γ = 1 beyond the length 1/√μ (checked). Respectively they give: repulsion with γ → −1/3, γ → 1.09, Yukawa screening, and a collapsed pull.
   - That is at least 5 mass tunings at P0's level (about 1e-96 to 1e-120), against P0's stated 2.
   - The longitudinal (helicity ±1 and 0) parts of h become physical modes (R2 §4c checked).

5. **What lands in the window, and the cost.** Only the FDiff-exact realization (case A) lands there. It needs:
   - two tunings at 1e-15: speed match to light, and cubic TT isotropy kE = kT2;
   - one at about 1e-6 to 1e-9 (α);
   - one mild (γ_G ≲ 0.1);
   - **no** mass tuning, provided exact spatial diffeos *and* time reparametrization are supplied. These are two prices the axioms do not supply.

   Without time reparametrization: add g_n = 2g to 2.3e-5 (Cassini), and μ_n, m4 at P0 level. On severity, case A is far cheaper than P0. But it is **not realizable with regular local finite-band lattice matter**, which is item 3. Its realizability is exactly lane RI's or RD's question.

**F1 reading (gravity sector, against the FIXED lane-RF readings).** **FAIL (bounded)** for realizations with regular local finite-band lattice matter:
- the projectable lapse violates the "no unstable or strongly coupled scalar" bar;
- the lattice-symmetry-only realization needs more tunings than P0 (at least 5 against 2, under P0's own natural-size counting);
- the FDiff realization does not close with that matter class.

The one conditional survivor, case A, has a better tuning count than P0. Its realizability is conditional on matter outside that class (lanes RI and RD), so the bounded FAIL does not extend to it. That part is INCONCLUSIVE.

---

## 1. Literature: the surviving region (comparator, verified where marked V)

### 1a. Theories and parametrization

**Hořava IR, and its khronometric covariant form** (GSS 1711.08845, V, eqs. 1–4):

S = (M_P²/2)∫N√h (K_ijK^ij − λK² + ξ R + η a_i a^i).

The khronometric parameters (α, β, γ) map as:
- λ = (1+γ)/(1−β);
- η = α/(1−β);
- ξ = 1/(1−β).

The speeds are:
- c_T² = 1/(1−β);
- c_S² = (2−α)(γ+β)/[α(1−β)(2+3γ+β)].

**Healthy extension.** The a_i a^i term (BPS PRL 104, 181302, 0909.3525, V abstract) "endows the scalar graviton mode with a regular quadratic action". BPS JHEP 1104:018 (1007.3503, V abstract) find that only the non-projectable model avoids both instabilities and strong coupling, and that its PN parameters are compatible with observation. The projectable theory has infrared viability issues (GSS, V). PPN γ = β_PPN = 1 for all couplings (M; consistent with Oost et al.'s statement for aether, V).

### 1b. Bounds (V unless marked)

**GW170817.** −3e-15 ≤ c_T − 1 ≤ 7e-16 ⇒ |β| ≲ 1e-15 (GSS eqs. 13–14).

**Preferred-frame PPN.**
- α1 = −4(α − 2β)/(1 − β).
- α2 = [(α − 2β)/(2 − α)]·[1 − (α − 2β)(1 + β + 2γ)/((1 − β)(β + γ))] (GSS eq. 12).
- Weak-field bounds: |α1| < 1e-4 and |α2| < 4e-7 (GSS eq. 11).
- Strong-field bounds:
  - |α̂1| ≤ 1e-5 (Shao–Wex 2012, V via search abstract);
  - |α̂2| < 1.6e-9 (Shao et al. CQG 30 165019, 1307.2552, V).

  Hatted bounds include neutron-star sensitivities.

**BBN.** |(α + 3γ + β)/(2 + 3γ + β)| < 1/8, from G_C = 1/[4πM²(2+3γ+β)] and G_N = 1/[8πM²(1−α/2)] (GSS eqs. 7–10).

**CMB and LSS.** For khronometric gravity with Lorentz-invariant DM: α < 1.8e-3 and c_χ² < 91 (95%), with G_N/G_cos − 1 = (3/2)αc_χ² (Audren et al. JCAP 1503:016, Table I and eq. 32, V). This was derived on the pre-GW170817 α = 2β plane.

**Binary pulsars (dipole radiation).**
- Yagi–Blas–Yunes–Barausse (1307.6219, V abstract) give the most stringent bounds via dipolar emission, but on the α = 2β plane. GSS (V) note that this plane shrinks to a line segment of width < 1e-15 after GW170817.
- Barausse PRD 100, 084053 (1907.05958, V abstract): at α = β = 0 with generic λ, neutron-star sensitivities vanish. There is no strong-equivalence-principle violation at leading PN order, in either the conservative dynamics or the GW fluxes. λ is only weakly bounded (0 ≤ λ ≲ 0.01–0.1).

**Strong coupling.** M_SC ≈ √α M c_S^{-1/2} for c_S² > 1 (GSS eq. 15, V). Franchini–Herrero-Valea–Barausse PRD 103, 084012 (2103.00929, V abstract):
- the α = β = 0 class is *not* equivalent to GR, even in vacuum, but is observationally GR-like;
- "the extra scalar degree of freedom stays strongly coupled at low energies".

**Cherenkov.** This bound is one-sided: it excludes subluminal c_T and c_S (GSS, V).

### 1c. Surviving region (checked from the GSS formulas, `f1_khronometric_window.out`)

| Section | Allowed (β = 0) |
|---|---|
| weak-field PPN + BBN + c_S ≥ 1 | 0 < α ≲ 8e-7 for 1e-4 ≲ γ ≲ 0.095; at γ = 0.1 BBN fails |
| strong-field α̂ bounds, sensitivities neglected (a reading) | 0 < α ≲ 3.2e-9 |
| cancellation branch | α ≈ γ/(1+2γ) makes α2 = 0 but α1 = −4α forces γ ≈ α ≲ 2.5e-6, with c_S² ≈ 1 (borderline Cherenkov) |

- In a uniform O(1) box for (α, γ), 0 of 2·10⁶ samples land in the window. The analytic fraction is about 3e-8, and β adds a further 1e-15.
- At α = 1e-9 and γ = 0.01: c_S ≈ 3.1e3 and M_SC ≈ 5.6e-7 M, about 1e12 GeV. At α = 1e-15: M_SC ≈ 4e7 GeV. M_SC → 0 as α → 0.

**Einstein-aether, for comparison** (Oost–Mukohyama–Wang PRD 97, 124023, eqs. 3.13–3.23, V):
- |c13| ≤ 1e-15;
- 0 < c14 ≤ 2.5e-5 and c14 ≲ c1;
- 0 < c14 ≲ c2 ≲ 0.095;
- two sub-regions:
  - (i) c14 ≤ 2e-7 with c14 ≲ c2 ≲ 0.095;
  - (ii) 2e-6 ≲ c14 ≤ 2.5e-5 with 0 ≲ c2 − c14 ≲ 2e-7.

Gupta et al. CQG 38 195003 (2104.04596, V abstract) tighten this "by about an order of magnitude" with binary pulsars; the numbers were not extracted.

**Reading.** A lattice slicing gives a hypersurface-orthogonal frame, so the relevant class is khronometric, not general aether. Aether's spin-1 modes need a frame that does not come from a slicing.

---

## 2. Lattice realization

### 2a. The VS/N-type theory with the lapse as a field (checked: `f1_lattice_foliation_symbol.out`)

**Setting (supplied; nothing derived from the axioms).**
- The 09-14 canonical (h_ij, E_ij), with midpoint symbols (k → q̂ = 2 sin(k/2)).
- The vector constraint q̂_iE_ij = 0 is kept exact, and its gauge h → q̂_(iξ_j) is quotiented.
- The scalar constraint is dropped as a gauge generator. The lapse n becomes an auxiliary field:

  H = ½E·K·E + (g/2)h:R(h) + g_n n S(h) + ½(−2α q̂² + μ_n)n² + nρ,

  with K = kA1 P_A1 + kE P_E + kT2 P_T2.

Results (each is checked):

| Check | Result |
|---|---|
| Gauge invariance of R and S | exact (≤ 1e-15) |
| TT | ω²/q̂² = Jg at every k, including zone-scale k = (0.9, 0.4, 1.3) |
| Khronon | ω_s² = J(1−2c)(g_n²/α − g)q̂². With GR normalisation (g = ½, g_n = 1, J = 2), c = λ/(3λ−1) and λ = 1+γ, this equals the GSS c_S² exactly at all k, e.g. 0.441860 at (α, γ) = (0.1, 0.05) and 9852.21 at (1e-6, 0.01). The healthy region needs 0 < α < 2 and γ > 0, the same as BPS |
| Projectable limit (no n(x)) | scalar ω²/q̂² = −(1−2c)Jg: −0.0233 at λ = 1.05 (tachyon), +0.0588 at λ = 0.9 (but a ghost, per RN L3, refereed). This re-checks RN L3 |
| Static source | n k² → −1/[2(g_n²/g − α)], i.e. G_N ∝ 1/(1 − α/2), matching GSS eq. 8; PPN γ = g_n/(2g) exactly (1.020 at g_n = 1.02); a lapse mass μ_n = 1e-4 gives n k² → 0 (Yukawa) |
| Cubic kinetic anisotropy kT2 = kE(1+10⁻³) | TT speeds² split by direction: 1.001 on [001], 1.000252/1.001 on [110], 1.000667 on [111] |

### 2b. Coefficients to tune to land in the window

The khronometric continuum has 3 numbers (α, β, λ) beyond G. At leading derivative order, the lattice version of case A (exact linear spatial-diffeo gauge, cubic symmetry, lapse a field) has kA1, kE, kT2, g, g_n, α, μ_n and m4 (= n·tr h).
- μ_A1, μ_E, μ_T2 and the shift mass are forbidden by the exact vector gauge: R2's W(0) = 0, refereed. The h-block at O(k²) is unique (g h:R).
- μ_n and m4 are forbidden **only** by time reparametrization, t → f(t) with N → N/ḟ, which is a uniform shift of n with ∫H_⊥ ≈ 0 (proved, elementary).
- The same symmetry ties g_n = 2g, so it gives γ = 1. A term ∫√γ N^p R gives γ = p.

| Lattice coefficient | Khronometric role | Tuning to the window | Natural size | Supplied by |
|---|---|---|---|---|
| Jg/c_light² − 1 | β, i.e. c_T | ≲ 1e-15 | O(1) | nothing (P0 also "generically expects" it) |
| kT2/kE − 1 | none: cubic TT birefringence and anisotropy | ≲ 1e-15 (GW170817 direction plus one-sided Cherenkov in all directions; suggested) | O(1) | nothing |
| α (lapse gradient) | α | 0 < α ≲ 8e-7 (weak) or 3e-9 (strong-field reading) | O(1) | nothing |
| kA1/kE ↔ c ↔ λ | γ_G = λ − 1 | 0 < γ_G ≲ 0.095 (mild) | O(1) | nothing |
| g_n/(2g) − 1 | γ_PPN − 1 | ≲ 2.3e-5 (Cassini) | O(1) | time reparametrization (then automatic) |
| μ_n, m4 | lapse masses | P0 level, (ℓ/L)² ~ 1e-96 to 1e-120 | O(1) | time reparametrization (then forbidden) |
| μ_A1, μ_E, μ_T2, μ_1 | graviton masses | P0 level | O(1) | exact spatial-diffeo gauge (then forbidden) |

**Against P0.** P0 is two TT counterterms at ≤ 5.7e-99, plus speed tunings left open.
- **Case A with both symmetries supplied:** 2 tunings at 1e-15, 1 at about 1e-7, 1 mild, and 0 at P0 level. That is far milder than P0 by severity, and comparable by count if P0's speed tunings are counted.
- **Case A without time reparametrization:** add the γ tuning at 2e-5 and 2 at P0 level, i.e. P0-equivalent at best.
- (suggested) Without T supplied, a term linear in E is allowed. That is a cosmological-constant-type tadpole, the same problem every gravity theory has, and it is not counted against RF.

**Strong-coupling caveat (reading).** In the window M_SC ≈ α^{3/4}γ^{-1/4}M, which is about 1e12 GeV at α = 1e-9. That is far above observed scales, so the fixed bar ("no strongly coupled scalar at observed scales") is met. But the grid's own scale is about M. Between M_SC and M the khronon is strongly coupled, so the lattice cannot be matched to the window perturbatively. Hořava's cure (M_* < M_SC) is unavailable when M_* is the grid scale, which Crab synchrotron puts at ≳ 2e16 GeV for matter on the same grid (GSS §III, V). Whether any lattice flows into the window is therefore uncontrolled.

### 2c. Does C3's obstruction disappear? (C3 sectors under FDiff)

| C3 sector | In GR | Under FDiff (Hořava / khronometric) | Status |
|---|---|---|---|
| Constant shift ({P,P} = 0, {P,H} = 0) | needed | needed: H_i[const] = total momentum | free matter OK; **interacting single-band matter has no exact momentum** (RN L2, refereed, d ≥ 2) |
| Rotation ({L_ab, P_c} ∝ P) | needed | **needed**: it is inside {H_i[ξ], H_j[η]} with ξ constant and η a rotation, since FDiff keeps local spatial diffeos | **fails**: C3 rotation theorem (proved, refereed); completions vanish there since Gᵀη = 0 |
| Linear lapse ({P_c, K_b} = δ_bc H) | needed (boost) | projectable: absent. Non-projectable (healthy): needed in a new form. N(x) is a field transported by H_i, and preserving H_i[const] under ∫N H_⊥ with linear N needs the Leibniz first moment Σ[(D_cN)T00 + N D_c^{fw}T00] = 0, i.e. weight W = Hess u(q) = 1 | **fails** (suggested reduction to C3's exact bracket {K_b, P_c} = −δ_bc E_c) |
| Time reparametrization (global H) | — | needed: ∫H_⊥ ≈ 0 | fine: H is exactly conserved (proved, trivial) |

**Checked** (`f1_fdiff_closure_symbol.out`):
- W − 1 at k = 0.1 is −5.0e-3, −1.7e-5 and −5.0e-8 for stencil ranges 1, 2 and 3.
- At k = π it is −2.0, −2.7 and −3.2.
- **The zone average of W is 0 (≤ 1e-16) at every range, where 1 is needed.**
- The rotation residual min_μ‖Hess u − M − μ∇u∇uᵀ‖/‖Hess u‖ is nonzero at every sampled q and range: 7.4e-3 / 9.7e-5 / 1.2e-6 near the IR, and about 1.1–1.3 at zone scale.

**Reading.** For real matter the lapse-sector defect is (ka)²/2, about 3e-39 for a 1 GeV particle on a Planck grid. That is not an observable weak-equivalence-principle violation. It is O(1) for lattice-scale loop modes, so the failure is one of constraint-algebra consistency, i.e. of mode count, not a direct observational miss.

**Answer to the brief.** C3's obstruction does **not** disappear. Only the boost half goes, and only in the projectable version, whose scalar is pathological. Lattice matter closes only with Z³ translations × cubic rotations × time translation (or time reparametrization), not with FDiff. (Proved for the rotation sector in C3's class. Suggested for the lapse sector.)

### 2d. Lattice symmetries only: the extra modes (case B; checked: `f1_lattice_only_masses.out`)

- **Extra modes.** With spatial diffeos not a gauge redundancy, the 3 longitudinal components of h (helicity ±1 and 0) are physical. R2 §4c checked a Stückelberg-like linear mode at v = 2.91. Lapse and shift are physical once kinetic terms are induced.
- **Allowed masses.** Cubic symmetry allows exactly **6** O(k⁰) quadratic invariants on (h_ij, n, n_i): μ_A1, μ_E, μ_T2, μ_n, m4 and μ_1 (group average, checked). There is no shift–h or shift–n mixing.
- **Comparator.** This is Dubovsky's Lorentz-violating massive gravity, split for cubic symmetry (JHEP 0410:076, V abstract): generically 6 propagating degrees of freedom, with ghosts or rapid instabilities; consistent phases need Fierz–Pauli-like tunings among the masses.

Static response (GR target: n k² → −0.2632, γ → 1):

| Mass (1e-3, all others 0) | At k = 1e-4 | Effect |
|---|---|---|
| none | n k² = −0.2632, γ = 1.0000 | GR-like |
| μ_E (TT mass) | n k² = −0.2396, γ = 1.0936 | pull weakened, γ off |
| μ_A1 | n k² = +0.6522, γ = −0.333 | repulsive |
| μ_n | n k² → 0 | Yukawa: no 1/r |
| m4 | n k² → 0, γ → −1e5 | no 1/r |
| μ_A1 = m4 = μ_n | n k² → 0, γ → 0.667 | no 1/r |

Each mass shifts the long-range response once k² ≲ μ. So each must sit at P0 level for 1/r and γ = 1 to hold out to solar-system or cosmological lengths.

**Count:** at least 5 P0-level numbers (μ_E, μ_T2, μ_A1, μ_n, m4), plus μ_1 for the gravitomagnetic sector (suggested), plus the 1e-15 speed tunings, the α tuning and the γ tuning. P0 states 2.

**Reading.** Case B *is* the fixed grid with its Newtonian sector made explicit. So this is also a statement that P0's stated count of two omits at least three P0-level scalar-sector numbers.

---

## 3. Verdict against the FIXED lane-RF readings (gravity sector)

| Realization | Bars | Tunings vs P0 | Reading |
|---|---|---|---|
| C: projectable lapse + FDiff | khronon ghost (λ < 1), tachyon (λ > 1) or strongly coupled (λ = 1): RN L3 refereed, re-checked here; rotation sector still fails | — | violates the stability bar: **FAIL** |
| B: lattice discrete symmetries + slicing | 1/r and γ = 1 survive only if 5 masses are tuned | ≥ 5 P0-level + 2 at 1e-15 + α + γ_G, against 2 (+ open) | **FAIL** (more tunings than P0) |
| A: exact lattice FDiff + time reparametrization (khronometric) | in the window: c_T, α1, α2, BBN, no dipole (α, β → 0); khronon strongly coupled only above about 1e12 GeV | 2 at 1e-15, 1 at 1e-7, 1 mild, 0 at P0 level: better than P0 | **not realizable** with regular local finite-band lattice matter (§2c). Realizable only with matter outside that class (lanes RI and RD): **INCONCLUSIVE, conditional** |

**F1 reading: FAIL (bounded)** for every realization whose matter is regular, local and finite-band (single-band in C3's and RN L2's proofs). Case A with that matter is not first class, so it is case B. That reduction rests on:
- C3's rotation theorem (proved, refereed);
- P0's natural-size counting convention for the masses that are then allowed (a reading). The size of the induced masses was not computed here; RN L2's referee left a forced natural-size mass unproved.

Case A is the only route with a better count than P0, and it costs two prices the axioms do not supply:
- an exact lattice spatial-diffeo redundancy (R1 referee: the axioms supply no tensor redundancy);
- global time reparametrization: a global Hamiltonian constraint, with the lapse multiplying the whole energy density. The axioms supply no time metric or rate.

Case A also needs FDiff-closing matter, which is the RI/RD question. So the lane-level FAIL depends on RI and RD as well.

**Against the supervisor expectation.**
- "GW170817 plus PPN leave a narrow khronometric window": **confirmed**, and quantified in §1c.
- What the expectation did not register: the preferred slicing does not remove C3's obstruction. Its rotation sector and the lapse-transport sector live in the spatial-diffeo algebra that Hořava keeps.
- The lattice-only route is P0 plus at least 3 further P0-level scalar-sector tunings.
- The matter-sector Collins count is F2's job and was not done here.

**Plain words.** A preferred slicing is what the grid offers, and Hořava gravity can live with one. But Hořava also needs space to be smooth, so that sliding things around within a slice changes nothing. The grid breaks that too. Lattice matter's momentum does not generate those slides, not even for free matter at the rotation level. So either the slides are kept as an exact symmetry, which the grid's matter cannot obey, or they are dropped. Dropping them lets five mass-like numbers appear, and each must be tuned to about 1e-100: more than P0's two.

## 4. Strong-word check

- **"proved"** is used only for:
  - the time-reparametrization statements (μ_n and m4 forbidden; g_n = 2g ⇒ γ = 1; elementary);
  - re-cited refereed results: C3's rotation theorem, RN L2 and RN L3.
- **"checked"**: the lattice symbol spectra (machine precision), the static responses, the group-average count, the W and rotation residuals, and the evaluation of the GSS window formulas.
- **"suggested"**:
  - the lapse-transport sector reduction;
  - Case A → Case B under broken FDiff;
  - the μ_1 / gravitomagnetic count;
  - the isotropy bar at 1e-15 (it relies on one-sided Cherenkov plus the single GW170817 direction).
- **Strong-field α̂ bounds** are applied without sensitivities. That is a reading, made on Barausse's ground that sensitivities vanish at α = β = 0.
- **Not done:**
  - nonlinear order;
  - the shift and gravitomagnetic sector of case B;
  - a computed size for induced masses;
  - the matter-sector Lorentz violation (F2);
  - the numerical Gupta et al. aether bounds;
  - the Yagi et al. numbers, which are superseded on the α = 2β plane anyway.

Sources: [GSS 1711.08845](https://arxiv.org/abs/1711.08845), [Oost–Mukohyama–Wang 1802.04303](https://arxiv.org/abs/1802.04303), [Barausse 1907.05958](https://arxiv.org/abs/1907.05958), [Franchini–Herrero-Valea–Barausse 2103.00929](https://arxiv.org/abs/2103.00929), [Gupta et al. 2104.04596](https://arxiv.org/abs/2104.04596), [Shao et al. 1307.2552](https://arxiv.org/abs/1307.2552), [Shao–Wex 1209.4503](https://arxiv.org/abs/1209.4503), [Yagi–Blas–Yunes–Barausse 1307.6219](https://arxiv.org/abs/1307.6219), [Audren et al. 1410.6514](https://arxiv.org/abs/1410.6514), [BPS 0909.3525](https://arxiv.org/abs/0909.3525), [BPS 1007.3503](https://arxiv.org/abs/1007.3503), [Dubovsky hep-th/0409124](https://arxiv.org/abs/hep-th/0409124).
