# C5 R17-7 report: if "the law's lowest state weighs nothing" (C = E₀[H]) is added as a principle, what does it predict, and does it survive?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Unrefereed. Run 2026-10-13, 00:46Z to 01:10Z. No repository file was edited.

**Scratch folder.** `S/` = `.../scratchpad/C5/R17-7/`. Each script runs in under 20 s at `OMP_NUM_THREADS=2`.
- `S/scripts/r177_late_universe.py/.out`: (a) thawing scalars against the DESI-like CPL curve (BAO-distance proxy).
- `S/scripts/r177_growth.py/.out`: (a)/(d) linear growth.
- `S/scripts/r177_gridvac_sector_cov.py/.out`: (b) Lemma V re-derived with (S) (sympy) and the residual enthalpy; (c) SM sizes and three sector rules; (d) Bianchi for a varying C, and the Lemma S coefficient at g = 0.
- `S/scripts/r177_records.py/.out`: the record test (KS sea; recorded-vacuum excess; one-record cost; a permanent-record component).
- `S/scripts/r177_enthalpy_orders.py/.out`: (b) the m² and m⁴ coefficients of the grid vacuum's enthalpy (R11-3 profiles).
- `S/recheck/`: the R16-6, R17-3 and R11-3 runners, copied and rerun. **All 12 checked runners reproduce their stored `.out` byte for byte** (5 for R16-6, 6 for R17-3, plus `r113_tadpoles`).

**Read.**
- In full:
  - `docs/MINIMAL_AXIOMS_2026-06-29.md` (`AX`);
  - the C5 method (`TESTS:2302-2320`) and the item (`TESTS:6018-6047`);
  - `C5_R17-3_report.md` (`R173`), `C5_R17-3_referee_verdict.md` (`vR17-3`), `C5_R17-3_referee.md`;
  - `C5_R16-6_report.md` (`R166`), `C5_R16-6_referee_verdict.md` (`vR16-6`);
  - `C5_R11-3_report.md` (`R113`), `C5_R11-3_referee_verdict.md` (`vR11-3`);
  - `C5_R15-1_referee_verdict.md` (`vR15-1`).
- In part:
  - `C5_S20_synthesis.md` §1.6 (`S20:207-230`) and §4 (`S20:413-534`), plus P70 and P92–P94 (`S20:355-357,387-389`);
  - the Λ-lane entries R11-3, R13-3, R14-5, R15-1, R15-4, R15-6, R16-6 and R17-3 in `TESTS` (`4157-4188, 4417-4424, 4621-4641, 4721-4729, 4876-4914, 4924-5036, 5160-5222, 5223-5245, 5295-5324, 5477-5491, 5576-5581, 5786-5812, 5907-5920, 5998-6016`);
  - `C5_R15-1_report.md:120-140,220-246` (Lemmas S and V);
  - `PRICE_NOTE.md:166` (P4) and `B_referee.md:100-104,184-190` (record heating).

**Labels.** proved / checked (sympy or numerics this run) / suggested / reading / comparator. Numbers from memory are marked RECALLED. Nothing was downloaded. DESI DR2 enters only as RECALLED values.

**Units and subtraction rule (named before the runs).**
- Homogeneous; κ = 1; u = ln a; 3H² = R; h = (ρ+p)_tot (as R16-6/R17-3).
- **(S): C := E₀[H]**, the bottom of the law's spectrum. In intensive form, **e₀ = lim E₀(V)/V**; the gravitating source is R = ρ_tot − e₀. Λ̃_late := κ(ρ_v,late − e₀).
- Every residual below is measured from the (S) zero e₀ and nothing else. The trace zero is printed only for comparison. The DESI comparison subtracts nothing: every model is compared directly with the CPL curve.

---

## 0. Verdict against the FIXED readings (`TESTS:6041-6043`)

**Worker reading: OPEN.** The conditions are sharper than the registered expectation (`TESTS:6044-6047`).

**Why not VIABLE-PRINCIPLE.** (a)–(d) are consistent with observation only under named conditions:
- **(a)** The dark energy must be dynamical content above e₀. Under (S) with P93 a pure Λ is forbidden. The minimal (canonical, thawing) content reproduces the DESI-like history only partly (proxy). If DESI's phantom crossing is real, it must be NEC-violating or coupled dark energy in GR. That is allowed, not forced.
- **(b)** e₀ includes the grid zero-point by definition, so the vacuum *energy* residual is exactly zero. The vacuum *enthalpy* (ρ₀ + p₀ > 0, R11-3) is outside the reach of a scalar e₀.
  - It is invisible only under R15-1's bridge (d-i).
  - Under (d-ii) it needs P70, which this probe sharpens: (ρ+p)_v must vanish at every mass the history passes through, i.e. pairing or one tuning per order in (ma)² per species.
- **(c)** With the SM potential alone, (S) gives Λ̃_late ≈ +1e112 to +3e120 ρ_Λ (RECALLED inputs, cutoff-dependent). So (S) needs P93: stabilizing physics, or lattice-scale terms that make our vacuum the global minimum.
  - A variant **(S′-start)** ("the bottom of the basin the universe starts in") avoids P93 causally. Its prices are a basin structure, a failure of Lemma U positivity, and P94′ (no basin change since the start).
  - The variant that tracks the *current* basin, **(S′-current)**, is active compensation (R15-1 FAIL) or breaks Bianchi.
- **Records.** (S) survives the record structure if records do not act on the physical state as lattice-scale local projections (P4's reconciliations).
  - If they do, and they are dense, the recorded vacuum weighs 1.19 M_P⁴ per staggered field (~1e123 ρ_Λ).
  - If they do and are sparse, each record costs ~2.4 ħc/a. That is P4's heating problem, which does not depend on (S).

**Why not EXCLUDED-PRINCIPLE.**
- No observation is contradicted once the conditions above hold.
- A local, covariant, non-signalling form exists: GR with Λ_* = −κe₀[H], a law constant.
- Only the variant (S′-current) is excluded in every local form. That is a narrower no-go, sent to the referee.

**Against the expectation (`TESTS:6044-6047`).**
- **(b) The wrong condition was registered.** The expectation said "(b) needs E₀ to include the grid zero-point exactly". It does, by definition. The live condition is the zero-point's *pressure*, which a scalar cannot cancel (R11-3's second tadpole). The fix is a source-bridge choice ((d-i)), not a property of e₀.
- **(c) Confirmed for (S).** A causal escape exists, (S′-start). It does not escape branching in general: it replaces P93 by P94′, which our known history satisfies (SM crossovers, slow roll; comparator RECALLED).
- **(d) Confirmed.** The "global quantity" is a law constant: an intensive spectral functional, quasi-local in practice. A constant carries no signal.

**Changed hypothesis relative to the governing prior result (vR17-3).** R17-3 asked whether the axioms force (S). Here (S) is *added*, and the probe tests its consequences against observation and the walls. Nothing here bears on whether (S) is forced; vR17-3's "not forced" stands.

---

## 1. In plain words

- **The rule.** Gravity ignores exactly the energy of the law's lowest state. Everything above that weighs.
- **Today's acceleration.** If our vacuum *is* the lowest state, the cosmological constant is exactly zero. The universe accelerates today only because something has not yet settled to its lowest energy, for example a very light field still rolling.
  - Prediction 1: the acceleration is temporary.
  - Prediction 2: the dark energy is not exactly constant.
  - Prediction 3: the leftover constant can never be negative.
  - DESI's data lean towards "not constant". A simple rolling field captures about half to two-thirds of DESI's departure from a constant (in a rough proxy). DESI's apparent "phantom" phase at redshift above 0.4 cannot come from such a field. It would need exotic or interacting dark energy, or be a statistical fluke.
- **The grid's own zero-point.** The rule automatically cancels the grid vacuum's energy. But on a grid with its own time, the vacuum also has a *pressure* that is not minus its energy. One number cannot cancel two.
  - The rule survives if the grid vacuum is allowed to trade energy and momentum with the sector that runs the expansion. Then the pressure is invisible.
  - If not, it needs boson–fermion pairing (or a tuning at every mass the universe passes through).
- **Our vacuum may not be the lowest state.** With the Standard Model alone, the Higgs potential turns over at very high field values, so a much deeper state exists. Then the rule makes our vacuum weigh a Planck-scale amount, which is catastrophic. So the rule predicts new physics that makes our vacuum the true bottom.
  - A milder version, "the bottom of the valley we started in weighs nothing", avoids this without looking into the future. It costs a little: states below our valley would weigh negative, and the universe must not have changed valleys since it started (true for the known history).
  - A version that follows the valley we are in *now* has to change its constant suddenly when the universe changes valley. That is the faster-than-light compensation already ruled out (R15-1).
- **Records.** If forming a record means pinning a lattice site to one definite value, then a recorded vacuum is not the lowest state. In the only worked model it weighs a Planck-scale amount, and each record costs about 2.4 Planck energies.
  - That is fatal, but it is the known "records heat the world" problem (P4), not a problem of this rule.
  - If records do not disturb the energy, the rule is untouched.
- **Covariance.** As a law of gravity the rule is just general relativity with a cosmological term fixed by the law's lowest energy. It is local, the same in every frame, and it sends no faster-than-light signals.

---

## 2. Hypotheses, variants and excluded alternatives (stated before titles)

- **H-Z, H-T, H-g0** as in R16-6/R17-3 (`R166:87-89`; `R173:81-82`).
- **(S), the principle under test** (`vR17-3:17`): C = E₀[H], intensive e₀ = lim min spec(H_V)/V. Under H-g0 the theory is GR with Λ_* = −κe₀ (Theorem Z, counted once).
- **Variants considered (each named, none adopted):**
  - **(S-T):** the lowest state's full stress tensor T₀ = ⟨0|T_μν|0⟩ is not a source. On a preferred-frame grid this is two numbers (ρ₀, p₀), both number-free.
  - **(S′-start):** C = the minimum of the basin in which the first reading finds the state. This is R17-3's "endpoint" variant (`R173:164`), counted once.
  - **(S′-current):** C = the minimum of the current basin.
  - **(S_rec):** C = the lowest *record configuration's* energy.
- **Source bridges for the grid vacuum** (`vR15-1:13`):
  - (d-i): the site-frame vacuum has no conservation law of its own and exchanges with the E/creation sector;
  - (d-ii): the vacuum conserves its own momentum.
- **Record readings (none is axiom content):**
  - **R-label:** a record locks a label (occurrence, a conserved or gauge-invariant variable, branch-relative decoherence) and does not change the physical state's energy (`B_referee.md:184-190`);
  - **R-proj:** a record at site x acts on the physical state as the projection/dephasing of x in the locked possibility's basis.
- **Excluded by the item** (`TESTS:6032`): active compensation (R15-1 FAIL); readers in 𝓡⁺ (R15-4).
- **Forks (rule `TESTS:5704`).**
  - The four variants above are not exhaustive.
  - Not covered: relaxation (R17-3's type (iv)); supercharge positivity (vR17-3:15, an alternative that would *enforce* e₀ = 0); frustration-free positivity (vR17-3:15).
  - These are omitted because they concern forcing (S), not testing it.

---

## 3. Prior art (each counted once)

1. **vR17-3:**
   - (S) is consistent, number-free, radiatively tracking and unforced (`vR17-3:17`);
   - Lemma U holds for attained ground states only, under its two conditions (`vR17-3:7`);
   - Lemma M holds in the fixed-weight count subclass (`vR17-3:9`);
   - the record-map numbers are confirmed (`vR17-3:11`).
2. **R17-3:**
   - the tilted double-well flip (`R173:294`; `r173_symmetry_radiative.out` D2);
   - the grid remark "(S) needs ρ₀ + p₀ = 0, pairing or one enthalpy tuning" (`R173:299`), sharpened in §4(b) here;
   - the "endpoint" variant and its positivity failure (`R173:164`);
   - "a primordial record of C" (`R173:315`).
3. **R16-6 and vR16-6:**
   - Theorem Z (`vR16-6:5-16`);
   - G0's metastability row (`R166:166`);
   - P-r166b = P93 and P-r166c = P94 (`R166:244-245`; `S20:388-389`);
   - S6: late acceleration is true dark energy, and DESI's phantom crossing must be real or a fluctuation (`R166:220-227`).
4. **R11-3 and vR11-3:**
   - Identity W, ρ + p_U = −⟨ε trA⟩/6 (`R113:117-123`);
   - w ≥ 0 (`R113:125-129`, corrected in `vR11-3:41`);
   - two tadpoles (`vR11-3:45-47`);
   - Lemma BR and the V2/V3 absorption (`R113:180-185`; `vR11-3:51`);
   - the V1 residual (`R113:209-211`);
   - small-m step coefficients and the infinitesimal edge root t* (`R113:152-157`; `vR11-3:63`).
5. **R15-1:**
   - Lemma S, signalling ⇔ g ≠ 0, and the GR control Δδ̇ = F at g = 0 (`C5_R15-1_report.md:122-138`; `vR15-1:5-7`);
   - Lemma V (d-i)/(d-ii) (`C5_R15-1_report.md:224-245`; `vR15-1:13`).
6. **R15-4:** DESI DR2 CPL histories are phantom at early times; no 𝓡⁺ reader tracks them (`TESTS:5301-5308`).
7. **R13-3/R14-5:** smooth-continuum V3 caustics; V2 needs a compensator (Lemma T) (`TESTS:4721-4729`). Under g ≡ 0 the lumpy form is GR's local constraint with source ρ − C (`R166:229-235`).
8. **P4 (record heating)** (`PRICE_NOTE.md:166`; `B_referee.md:103,184-190`). The R-proj cost in §4(e) is a concrete instance of it.
9. **P70, P92–P94** (`S20:355-357,387-389`).
10. **The owner's records-are-mass thought** (memory; a hypothesis only).
11. **Comparators, all RECALLED:**
    - DESI DR2 BAO effective redshifts and approximate errors; CPL (w₀, w_a) ≈ (−0.75, −0.86); a combined preference of about 2.8–4.2σ;
    - SM vacuum metastability (Degrassi et al. 2012; Buttazzo et al. 2013): λ < 0 above ~1e10–1e11 GeV; λ(M_P) ≈ −0.013; stability needs m_t ≲ 171 GeV;
    - thawing and PNGB quintessence (Frieman–Hill–Stebbins–Waga 1995: technically natural ultralight mass);
    - the Casimir effect (vacuum correlations exist).
12. **Repository grep** (the packet and `docs/`, for record heating/cost, lowest state and E₀[H]). New hits beyond 1–11 are only P4/B1/O2's heating lines (item 8). No prior test of (S)'s predictions was found.

---

## 4. Results

### 4(a) The late universe

**(a1) What (S) predicts (proved, elementary, given Theorem Z and H-g0).**
- **Λ̃_late = κ(V_late − e₀) ≥ 0 for every history, because e₀ is the spectral minimum.** A negative late cosmological constant is impossible under (S).
- With P93 (V_late = e₀), Λ̃_late = 0 exactly. Today's acceleration must then come from content above e₀ with ρ + 3p < 0. There are three ways:
  1. **A field not at its minimum (thawing or freezing quintessence).** The acceleration is transient, H → 0 asymptotically, and the future is Minkowski, not de Sitter.
  2. **A false vacuum above e₀.** Then w = −1 until it decays, but this violates P93. For the SM's own false vacuum the size is Planckian (§4(c)), so the false vacuum would have to sit in a hidden sector with a splitting of about (2.3 meV)⁴. That is the coincidence problem S6, counted once.
  3. **NEC-violating or interacting dark energy.** (S) does not forbid it; Lemma U bounds only the total energy.
- **Distinguishing predictions versus ΛCDM:**
  - (P-a1) no fundamental Λ: w(z) ≠ −1 at some epoch, unless option 2;
  - (P-a2) Λ̃_late ≥ 0;
  - (P-a3) eventual deceleration;
  - (P-a4) through P93, the EW vacuum is absolutely stable (§4(c)).
- None of these is decisive with current data. A frozen field mimics w = −1 arbitrarily well. So detecting w ≠ −1 would support (P-a1), but not detecting it cannot falsify (P-a1).

**(a2) The minimal (S) content against the DESI-like history (checked, PROXY; `r177_late_universe.out:1-10`).**
- **The proxy.** The "data" are the CPL curve's own BAO distances at the DR2 effective redshifts, with RECALLED approximate DR2 errors: diagonal, BAO only, one free amplitude.
- **ΛCDM:** χ²_proxy = 0.529 (Ω_m = 0.2823).
- **Canonical thawing scalars** (frozen at a = 1e-3, so w ≥ −1 throughout, checked):
  - exponential, λ = 0.639: χ² = 0.241, with CPL-equivalent (w₀, w_a) = (−0.934, −0.098);
  - PNGB, f = 0.357 (reduced Planck units): χ² = 0.200, with (−0.889, −0.230).
  - They recover **54% and 62%** of the ΛCDM-to-CPL gap.
- **Maximum |ln H| deviation from CPL over 0.1 < z < 2.33:** 4.4% (ΛCDM), 3.0% (exponential), 2.2% (PNGB).
- **Reading.** Both best fits sit in the thawing quadrant (w₀ > −1, w_a < 0), the same quadrant as the DESI fit. The phantom side at z > 0.41 cannot be reproduced. This is a proxy and states no significance: DESI's preference comes mainly from BAO + CMB + SN, which is not modelled here.
- **Growth (checked; `r177_growth.out:1-5`).** Linear growth under (S) is GR's: fD differs from ΛCDM by at most 1.7% for the thawing fits at z ≤ 1. Normalization is at a = 1e-3, with no CMB matching.
- **Naturalness (comparator, RECALLED).** A PNGB with f ~ M_P and Λ_a ~ meV has a technically natural mass m ~ H₀ (shift symmetry). So (S) converts an unprotected constant into a symmetry-protected small scale. The scale itself is not explained (S6).

### 4(b) The grid zero-point (P70, R11-3)

**(b1) e₀ includes the grid zero-point (proved, definitional).** E₀[H] is the bottom of the full law's spectrum: every band's zero-point, every sea, every condensate. The *energy* residual of the vacuum is exactly zero.

**(b2) The enthalpy is outside a scalar's reach (proved; checked).**
- On the grid with a preferred time, the vacuum stress has two invariants (ρ₀, p₀) (O1 count, counted once: `vR11-3:45`). For every positive band under U, and for every band with a nonnegative kinetic part under M, ρ₀ + p₀ = −⟨ε trA⟩/6 > 0 (`vR11-3:41`).
- (S), as a Λ√−g counterterm, removes (ρ, p) ∝ (1, −1). **It leaves (ρ_res, p_res) = (0, ρ₀ + p₀)** (`r177_gridvac_sector_cov.out:9`).
- Per real scalar at m = 1 (rerun of R11-3, `recheck/R11-3/r113_tadpoles.rerun`): **p_res = 2.068 (L), 1.849 (G), 1.399 (NN) /a⁴, i.e. 1.2–1.8e123 ρ_Λ at a = ℓ_P** (`r177_gridvac_sector_cov.out:11-14`).

**(b3) What happens to the residual depends on the option and the bridge:**
- **V2/V3 + site creation (the R16-6 setting), bridge (d-i): residual exactly zero for any w (proved; sympy).**
  - Lemma V re-derived (`r177_gridvac_sector_cov.out:1-6`):
    - λ′ = −3Hg′;
    - −2Ḣ = g′ + ρ_m + p_m, in which p_v does not appear;
    - 3H² = ρ_m + (λ + ρ_v).
  - (S) sets λ = −e₀ = −(ρ_v + ρ_rest), so Λ̃_late = 0 with g′ ≡ 0, whatever p_v is.
  - Through a transition with latent-heat transfer Q = −ρ̇_v, Λ̃̇ = −3Hg′ − κQ. So g′ = 0 holds, λ stays constant, the false vacuum gravitates, and nothing is absorbed actively (derived by hand from Lemma V's conservation; consistent with R16-6).
- **Bridge (d-ii): (S) is not enough. P70 is sharpened (checked at orders m² and m⁴, suggested beyond; the inputs are R11-3's refereed profiles and numbers, counted once).**
  - Conservation of a constant site-frame vacuum needs (ρ+p)_v = 0 (`r177_gridvac_sector_cov.out:8,10`).
  - The vacuum's enthalpy depends on the masses. The finite step m: 1 → 0.3 changes ρ + p_U by −0.018 (L), −0.064 (G) and −0.086 (NN) (`r113_tadpoles.rerun`). The small-m slopes d(ρ+p_U)/dm² are −0.0014 (L), +0.072 (G) and +0.099 (NN) (`R113:152-156`).
  - So a single enthalpy tuning at the late vacuum leaves a Planckian, non-conserved enthalpy, Δ(ρ+p)_v ~ 0.07 Δm²M_P², in every earlier phase with different masses. For the G edge and Δm² = (100 GeV)², that is about 1e41 GeV⁴ ≈ 4e87 ρ_Λ (arithmetic, RECALLED inputs).
  - **Under (d-ii), (S) therefore needs (ρ+p)_v(m) = 0 along the whole history.** That means structural pairing, or one tuning per order in (ma)² per species.
  - **Checked at the first two orders** (`r177_enthalpy_orders.out:1-10`):
    - By Identity W, E(m²) = ρ + p_U = −⟨ε trA⟩/6 is supported on the edge, where ε is bounded away from 0. So E is analytic in m², with no log term.
    - R11-3's edge root t* = 0.001170 is reproduced; there c₂ = 0.
    - But c₄ = ⟨trA/(48ε³)⟩ = **+0.0388** at t*, against +0.0427 (L), −0.0016 (G) and −0.0047 (NN). The finite-m check agrees: E(0.05) − E₀ = 2.41e-7 against c₄m⁴ = 2.43e-7.
    - So after the edge tuning and the late enthalpy tuning, a hot phase with Δm ~ 100 GeV keeps (ρ+p)_v ≈ 1.5e53 ρ_Λ per real scalar. That is non-zero, and it is inconsistent with the Euler equation in any well.
    - c₄ changes sign between t = 0.1 and G, so a second edge parameter could zero it. That is the "one tuning per order" pattern (suggested beyond m⁴).
- **V1 (spacing grows, fixed sites; not the R16-6 setting).**
  - The vacuum is a conserved barotropic fluid ρ₀(a). (S) with one constant leaves a Planckian matter/radiation-like residual away from one epoch: ρ(e) − ρ(0) ≈ −0.45 per scalar at e = 0.1 (`R113:209-211`, counted once). **Excluded for V1** (reading, same as R11-3's P-V1a).
  - (S-T) with the background-dependent T₀(a) would remove it, number-free. It is a reading only, because it would also remove any induced Einstein term.
- **(S-T) does not replace (d-i) (proved, elementary).** (S-T) subtracts the *late* ground state's (ρ₀, p₀). An earlier phase's vacuum difference (ΔT_v) is gravitating content with Δ(ρ+p) ≠ 0. At fixed site density it is created with the sites, so it is non-conserved, and that fails Bianchi unless (d-i) holds.

**Answer to (b).** E₀ includes the zero-point. The residual is exactly zero in energy. In pressure it is either invisible ((d-i)) or a Planckian w = "∞" pure pressure (ρ = 0, p > 0) that requires pairing ((d-ii)). It is not matter-like, except in V1.

### 4(c) Metastability

**(c1) (S) with the SM alone (comparator arithmetic, RECALLED inputs; `r177_gridvac_sector_cov.out:15-18`).**
- With V ≈ λ_eff h⁴/4 cut off at h ~ 1e17 GeV to M_P (the field range on the grid is a reading): **Λ̃_late = κ(V_EW − E₀) ≈ +1.5e112 to +2.9e120 ρ_Λ.**
- Without a cutoff, E₀ is undefined in the SM alone.
- On a qubit lattice with bounded nearest-neighbour terms, e₀ ≥ −(number of bonds per site)·‖h‖ always exists (proved, elementary). Whether the EW vacuum is the lattice law's bottom is not decided: the law is not supplied (`AX:116-130`).
- **Reading.** No *observation* is contradicted, because the law's potential above ~1e10 GeV is unmeasured. (S) **predicts** stabilization (P93): new physics below the instability scale, or a lattice-scale lifting of the deep region, or m_t below the stability bound.

**(c2) Three sector rules on a decay history (checked, sympy; `r177_gridvac_sector_cov.out:19-22`):**

| Rule | Λ̃ before decay | Λ̃ after decay | g | Status |
|---|---|---|---|---|
| (S) C = E₀ | κ(V₊ − V₋) > 0 | 0 | 0 | needs P93 |
| **(S′-start)** C = V(starting basin) | **0** | κ(V₋ − V₊) < 0 (AdS crunch inside the bubble; ordinary GR) | **0** | causal; no P93 |
| (S′-current) C = V(current basin) | 0 | 0 | κ(V₋ − V₊)δ(t − t_d)/3 ≠ 0 | active compensation: R15-1 FAIL |

**(c3) The local form of (S′-current) fails Bianchi (proved, elementary; `r177_gridvac_sector_cov.out:23-26`).**
- G = κ(T − C(x)g) with conserved T forces ∂C = 0.
- A C(x) that jumps across bubble walls is inconsistent unless an exchange sector carries ∂C. That is g ≠ 0, which is R15-1 signalling.
- **So (S′-current) is excluded in every local covariant form.** This is a no-go for the variant only, for the referee.

**(c4) (S′-start): what it buys and costs (reading/suggested).**
- **What it buys:**
  - C is a law functional of a discrete basin label, read once. It is number-free.
  - It tracks loops by definition.
  - g ≡ 0, so it is causal.
- **What it costs:**
  - Lemma U positivity: states below our basin weigh negative (reading; it is observationally harmless, since true-vacuum bubbles crunch in GR anyway).
  - A semiclassical basin structure: a field space and gradient-flow basins. This is not in the axioms (`AX:116-130`), and a metastable vacuum is a resonance, not an eigenstate. The ambiguity is of order the decay rate, exponentially below ρ_Λ (suggested).
  - A first reading (P-r166d's class, but exact by definition).
  - **P94′: no basin change between the first reading and now.** Our history satisfies it if the EW and QCD transitions are crossovers and inflation is slow roll on our basin's slope (comparator, RECALLED). It fails for any first-order transition between minima after the start, and for open (tunnelling-started) inflation.
- So (S′-start) avoids P93 without acausality, but it does not avoid branching in general. It moves the requirement to "no branch since the start".
- **The records link (reading).** Permanence makes a record the natural carrier of the basin label (`R173:315`). A global constant needs every site to record the same basin, otherwise C(x) breaks Bianchi as in (c3).

### 4(d) Inhomogeneous and covariant form

- **The statement (proved, elementary):**

  **G_μν + Λ_* g_μν = κ T_μν, with Λ_* := −κ e₀[H] and e₀[H] := lim_{V→∞} min spec(H_V)/V.**

  - It is local and generally covariant.
  - The only non-local ingredient is e₀, which is a property of the law, not of the state or the history. For a gapped H it is fixed by finite patches to exponential accuracy. For a gapless H, Casimir-type corrections ~ℓ⁻⁴ are below ρ_Λ for any patch larger than about 0.1 mm (suggested).
- **"Global quantity": yes, as a law constant. Signalling: none.** C is constant, so g ≡ 0 (Theorem Z). The R15-1 Lemma S remote coefficient (3g/2)/(k²/a² + Q̄) vanishes, and the response is ultralocal, Δδ̇ = F (`r177_gridvac_sector_cov.out:27`; GR control counted once).
- **Lumps.** The form is GR's local Hamiltonian constraint with source ρ − e₀ at every k (`R166:229-235`). Bound regions do not expand, and collapse is GR's. The R13-3 caustic applied to fixed-lapse V3, not to g ≡ 0 GR.
- **What remains carried:**
  - the site-creation law must realize GR's local volume change (P52/P53);
  - on the grid, the enthalpy condition of §4(b) applies locally: (d-i), or (ρ+p)_v = 0 by the Euler equation in every well (`vR15-1:13`).
- **(S-T) on the grid** subtracts a frame-tied T₀[u] = ρ₀uu + p₀h, a uniform c-number. It exerts no self-force on a moving compact body (round-17 rule).

### 4(e) The record and permanence structure (AX:79-83)

**(e1) Lemma X (proved, elementary; checked).**
- Write H = H_diag + H_off in the record basis. Pinching keeps ⟨H_diag⟩. For the ground state:

  **⟨H⟩_pinched − E₀ = −⟨H_off⟩₀ ≥ 0**, with equality iff every record configuration in the pinched support is itself a ground state. For a unique ground state, that means iff the ground state is diagonal (a record configuration).
- **The KS sea** (`r177_records.out:1-10`; ED at L = 8, Bloch at L = 257). Excess per site: **1.1938 (m → 0), 1.0992 (m = 1), 0.9201 (m = 2)**, in units of ħc/a. ED and the Bloch form agree to finite size.
- **One record** (one site dephased): **ΔE₁ = 2.38 (m = 0) to 1.84 (m = 2)** ħc/a. That is twice the per-site kinetic share, from 6 bonds against 3 (`r177_records.out:2-5`).

**(e2) Consequences for (S) by reading:**
- **R-label:** (S) is untouched. PASS (reading).
- **R-proj with dense records** (every site recorded, "until frozen", or the stadium's fixed seats):
  - (S)'s weightless state is never physically realized;
  - the recorded vacuum weighs **1.19 M_P⁴ ≈ 1.05e123 ρ_Λ per staggered field** at a = ℓ_P (`r177_records.out:12`);
  - **contradiction with observation** (checked, conditional on R-proj, the KS law and a = ℓ_P; for the referee).
  - The variant (S_rec) zeroes the recorded state instead. It then makes unrecorded regions weigh −1.19 M_P⁴, so new sites must be recorded instantly, and it keeps P4's heating (reading).
- **R-proj with sparse records:**
  - each record injects ~2.4 ħc/a = 2.9e19 GeV, which is P4's heating, independent of (S) (`r177_records.out:13`);
  - **if such records were the dark energy**, the observed ρ_Λ would allow at most 1.1e-19 records per m³ over the whole history (`r177_records.out:14`).
- A ground state that *is* a record configuration is a product state with no vacuum correlations. The measured Casimir effect excludes that (suggested; comparator RECALLED).

**(e3) The owner's records-are-mass thought, as a hypothesis (checked in a toy; reading).**
- Under (S) + R-proj, records *are* mass: each permanent record carries positive weight above e₀. So Jon's thought becomes a consequence there, not an extra rule.
- Unlike R17-3's literal record sourcing, records are then only *part* of the source. Excitations above e₀ also weigh, so Lemma M's "no radiation era" does not apply (`vR17-3:9`).
- The record component itself has a³ρ non-decreasing, so w ≤ 0.
- With a constant formation rate per physical volume and decreasing H, it is **phantom-like at every time, w = −1.49 (z = 3) to −1.24 (z = 0), never crossing −1** (`r177_records.out:16-21`). The proof that it never crosses is elementary: ρ < Q/(3H) always. That matches the sign of DESI's early-time phantom side, not its w₀ > −1.
- A growing record component under (d-i) has Λ̃ = λ + κρ_rec(t) changing, so g′ ≠ 0 (R15-1). Under a conserved bridge it is coupled dark energy (reading).

### 4(f) Prices (named, none adopted)

| # | Price | Axiom text touched | Status |
|---|---|---|---|
| **P92 = P-r173a (carried)** | (S): the source bridge is T − e₀[H]g | `AX:187`; `AX:116-130` (no H supplied) | consistent, number-free, unforced (`vR17-3:17`) |
| **P93 (carried, sharpened)** | Our vacuum is the global minimum. With SM-only running, Λ̃ ≈ 1e112–1e120 ρ_Λ otherwise, so the law must stabilize the Higgs potential | `AX:187`; downstream | prediction, not contradicted; RECALLED inputs |
| **P-r177a** | (S′-start) in place of P93: C = the minimum of the starting basin. Needs a basin structure (not in the axioms), a first reading, positivity given up, and **P94′** (no basin change since the start) | `AX:116-130`; `AX:94` reading (a state-dependent answer, one per state); `AX:185-186` | causal (g ≡ 0); P94′ holds on the known history (comparator) |
| **P70 (sharpened)** | Grid enthalpy. Under (d-i): no cost. Under (d-ii): **(ρ+p)_v(m) = 0 along the history**, i.e. pairing, or one tuning per order in (ma)² per species. One enthalpy tuning is not enough once masses change: after the edge root t*, c₄ = +0.0388 remains | `AX:187`; `AX:47` (pairing) | checked at orders m² and m⁴ (`r177_enthalpy_orders.out`); suggested beyond |
| **P-r177b** | Records must not cost energy at the lattice scale (R-label), or the ground state must be a record configuration (excluded by vacuum correlations) | `AX:79-83` reading; = P4 (`PRICE_NOTE.md:166`), counted once | the (S)-specific part is (e2)'s dense-record contradiction |
| P94, P51, S6, P52/P53 | carried | — | carried |

**Counting convention (rule `TESTS:5700`).**
- (S) and (S′-start): 0 numbers.
- (d-ii) without pairing: n_species × (orders kept) tunings.
- (d-i): 0.

---

## 5. Round-17 rules

- **Whole-zone v_max:**
  - KS symbol: v_max/c = 1 (counted once, `R173:225`);
  - L/G/NN scalar bands: as R11-3, not recomputed. No gauge-field symbol is used.
- **Self-force:** (S) has none, being constant. (S-T)'s T₀[u] is a uniform c-number with no body-dependent kernel.
- **Ward:** standard (diffeomorphism/Bianchi).
- **Enforced or stipulated:**
  - (S), (S′-start) and (S-T) are stipulated rules, with no number;
  - P70 under (d-ii) is stipulated numbers or a structure (pairing);
  - radiative tracking holds by definition for (S) and (S′-start), but not across a flip in the ordering of minima for (S) (counted once).
- **Physical controls:**
  - the thawing integrator returns w ≥ −1 exactly at freeze-out (`r177_late_universe.out:3-4`);
  - the ED and Bloch excesses agree;
  - R11-3, R16-6 and R17-3 runners reproduce byte for byte.
  - The DESI comparison is a proxy, not a control.
- **Readout bridges:** the record energies use R-proj or W1 pinching (`RM:25-27`); no stiffness claim is made.
- **Forks:** §2.
- **Generic GR comparison:**
  - §4(a) and §4(d) are generic GR plus quintessence;
  - §4(b) is grid-specific;
  - (c2) is generic GR;
  - §4(e)'s R-proj cost is generic to collapse-type records (P4), and the dense-record weight is (S)-specific.
- **Changed hypothesis:** §0.

---

## 6. Notes for the referee (no-go items)

1. **(S′-current) excluded in every local covariant form (§4(c3)).** Bianchi forces ∂C = 0, and the only alternative carrier is g ≠ 0 (R15-1). Check whether an exchange sector other than R14-5's E could carry ∂C without Lemma S.
2. **(S) + R-proj + dense records contradicts observation (§4(e2)).**
   - Is "every site recorded" a fair reading of "records form … permanent" together with the until-frozen thought? It is a thought, not a rule.
   - Is the KS sea a fair stand-in for the law's ground state?
   - Lemma X itself is elementary.
3. **The P70 sharpening under (d-ii) (§4(b3)).** Is "one tuning per order in (ma)² per species" right? R11-3's t* zeroes only c₂ (`vR11-3:63`); c₄ = +0.0388 remains there (`r177_enthalpy_orders.out:3`).
4. **(S-T) ≠ (d-i) (§4(b3), last bullet).**
5. **The DESI proxy (§4(a2)).** It is not a likelihood. Only the 54–62% "gap recovered" and the thawing-quadrant location should be used.
6. **Strong-word check:**
   - "exactly zero": energy, by definition; enthalpy only under (d-i) in Lemma V's setting.
   - "every local form": (S′-current) with conserved T.
   - "never negative": Λ̃_late under (S), by e₀ = min spec.
   - "never crosses": the constant-rate record toy with H decreasing.

**What would change the reading:**
- **To VIABLE-PRINCIPLE:**
  - a derivation that the source bridge is (d-i), or pairing;
  - P93 established (or (S′-start) accepted, with P94′);
  - R-label confirmed as the record reading.
- **To EXCLUDED:**
  - SM metastability confirmed with no new physics, together with (S) over (S′-start);
  - or R-proj with dense records established;
  - or a refereed demonstration that DESI's phantom phase is real and that no allowed content above e₀ can produce it. (S) does not forbid it, so this is unlikely.

## 7. Files

- Report: `S/R17-7_report.md`.
- Scripts and outputs: `S/scripts/r177_late_universe`, `r177_growth`, `r177_gridvac_sector_cov`, `r177_records`, `r177_enthalpy_orders` (each `.py` with its `.out`).
- Reruns: `S/recheck/{R16-6,R17-3,R11-3}/*.rerun`, byte-identical to the stored `.out`.
