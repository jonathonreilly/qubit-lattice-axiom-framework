# C5 R19-14 report: if site creation injects energy, does any other way of growing space keep (S) number-free?

- **Worker:** Claude Opus 5.5 (Claude Code agent; same family as the supervisor). Started 05:20Z, report ~05:55Z, 2026-10-13. Unrefereed.
- **Item:** `TESTS.md:7773-7810` (FIXED readings at `:7801-7804`).
- **Scratch:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/R19-14/` (`S/`).
- **Abbreviations:** `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS` = `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`; `rX` / `vX` = `agents/C5_X_report.md` / `agents/C5_X_referee_verdict.md` in that folder; `vR19-10` = `scratchpad/C5/ref_R19-10/REFEREE_VERDICT.md` (it appeared during this run).
- **Units:** lattice units with comoving spacing ℓ₀ = 1, c = ħ = 1. Cosmology in Planck units, G = 1. H₀ = 1.1775e-61, Ω_Λ = 0.685 (RECALLED), so ρ_Λ = 1.134e-123 (`r1914_v1_lag.out:31`).
- **Labels:** proved / checked (numerics here) / suggested / reading / comparator (RECALLED = from memory, not verified this run).

---

## 0. Reading against the FIXED readings: **OPEN** (worker)

**ALT-GROWTH-OK is not met.**
- Literal (S) (C = e₀ as a fixed law constant) fails in V1 [checked]:
  - Λ̃ drifts with the vacuum, which behaves like Planck radiation;
  - N_red then breaks Bianchi.
- A modified V1 bridge is number-free and non-signalling in the homogeneous sector [checked there]. It has two parts:
  - (S_V): the full stress of the instantaneous lowest state weighs nothing;
  - (S_ad): the lowest state is taken as the adiabatic vacuum.

  It fails ALT-GROWTH-OK for three reasons:
  - it is a new completion, not (S) as written (literal-first rule, `TESTS:7124`);
  - the inhomogeneous, non-signalling sector is not built;
  - it requires that the lattice set no physical scale, so ℓ/ℓ_P ∝ a(t) and the scale-reference gate `AX:189-190` holds at one epoch only.

**NO-NUMBER-FREE-GROWTH is not met, and the worker does not claim it.**
- Site creation is **refereed OPEN**. The R19-10 referee returned NOT CONFIRMED on INJECTS (`vR19-10:1-3,32,40`).
- V1's cost, under the modified bridge, is a new clause plus the loss of the scale reference. It is not a number or a signalling channel. The one *number* found is the frame parameter s (§2.2–2.3), and a number-free principle (S_ad) removes it.
- V0 does not survive as a separate mode. By Lemma G0 (proved) it either gives z ≡ 0 or is V1 in another frame.

**Against the expectation (`TESTS:7805-7810`).**
- **Confirmed:**
  - V1 makes e₀ time-dependent: e₀ ∝ a⁻⁴ at zeroth order;
  - a fixed grid cannot expand, sharpened to z ≡ 0 by Lemma G0.
- **Not borne out:**
  - "V1 brings back the Bianchi carrier and signalling." The carrier V1 needs is the vacuum's own enthalpy. No new field is involved, and there is no CMC constraint, so no Lemma-S channel arises in the homogeneous sector.
  - "(S) is number-free only on a static universe." This is not established. V1 + (S_ad) is a number-free homogeneous candidate. Its price is structural: the lattice sets no physical scale.

---

## 1. Plain words

- **No new site, no redshift.** On a fixed set of sites, a law that is the same at every site conserves a light wave's wavenumber on the grid. So light arriving from far away is redder than local atoms only if the atoms have shrunk relative to the grid since the light left. "Space expands" on a fixed grid therefore means exactly this: the grid spacing, measured with atoms, grows like the scale factor. A grid that stays fixed in atomic units gives no redshift at all, and records or metrics cannot change that. That rules out "V0" as a separate option.
- **Stretching the grid (V1) works only if the grid sets no scale.** If particle masses were fixed in grid units, nothing would redshift. If gravity's strength were fixed in grid units, G would grow as the square of the universe's size (Ġ/G = 2H); lunar ranging excludes that by a factor of about a thousand. So in V1 the grid spacing drifts against the Planck length by the whole expansion since inflation, more than 1e50.
- **The vacuum follows the stretching smoothly.** There is no Planck-sized injection, unlike site insertion. But its energy falls like radiation (a⁻⁴), so "subtract one fixed lowest-state energy" fails at once. "Subtract the lowest state's whole stress, at the current stretch" works, and keeps the gravity equations consistent with no extra field.
- **A small lag remains, and its size depends on a convention.** The vacuum trails the instantaneous lowest state slightly. Today that lag is about the size of the observed dark energy per field (if the spacing is near the Planck length). But how big it is depends on which variables you call "the law's" variables. One choice, the "adiabatic vacuum", makes it vanish. Any other choice must be fixed to 1 part in 1e21–1e38, or inflation is impossible.

---

## 2. Results

### 2.1 Lemma G0: redshift on a fixed site set is spacing growth in atomic units (proved)

**Setting.**
- Fixed sites Z³.
- A law covariant under lattice translations (`AX:57-58`), possibly time-dependent.
- A statistically translation-invariant state.

**Claim.** A signal mode keeps its lattice quasi-momentum k from emission to reception, because translation invariance is exact. Write λ_A(t) for an atomic wavelength measured in lattice steps. At emission λ = λ_A(t_e) in lattice steps; at reception the same k is compared with λ_A(t_o). So

  **1 + z = λ_A(t_e)/λ_A(t_o) = ℓ_A(t_o)/ℓ_A(t_e),**

where ℓ_A = 1/λ_A is the spacing in atomic units. ∎

**Consequences.**
- **(G0-a) A fixed-grid V0 gives z ≡ 0.** That is a grid fixed in atomic units, with no creation and a static or dimensionless-static law. If the law is also time-independent, the received pulse period equals the emitted period, by time-translation invariance. So there is no supernova light-curve dilation either.
- **This excludes the option.** CMB T(z) ∝ 1 + z and supernova light-curve dilation ∝ 1 + z (comparators, RECALLED) exclude it. This is a reading on the data and proved on z.
- **(G0-b) V1 and "records/metric carry the expansion" are the same physics.** Expansion without creation is ℓ_A(t) ∝ a(t), whether it is read as a growing metric spacing (Einstein frame, V1) or as growing dimensionless masses on a static grid (Jordan frame, V0-b).
- **(G0-c) In V1 no physical scale may be lattice-native.**
  - Lattice-native masses give z ≡ 0.
  - A lattice-native G with physical masses gives G ∝ ℓ² ∝ a², so Ġ/G = 2H₀ = 1.4e-10/yr against |Ġ/G| ≲ 1.5e-13/yr (lunar laser ranging, RECALLED). That is excluded by about ×1000.
  - So ℓ/ℓ_P ∝ a, which is about e⁶⁰·T_rh/T₀ ≥ 1e50 since the start of inflation.
  - Count once: this sharpens R11-3's P-V1b/P-V1c (`rR11-3:216,242-243`). The new part is the mass side, and the statement that both sides are forced.
- **Scope.**
  - G0 does not cover translation-breaking states. Those include galaxies moving through a fixed grid (Milne-like) and redshift by scattering ("tired light"). Both are disfavoured by Ω_m ≈ 0.3 and by time dilation and image sharpness (reading, RECALLED; R12-2's foam result for random insertion is counted once, `vR12-2:11`).
  - Breaking the law's translation covariance is excluded by `AX:57`.

### 2.2 Probe (a): e₀ and excitations under V1

**Model.**
- A minimally coupled NN lattice scalar on comoving Z³ in cosmic time: H_k = p²/(2a³) + a³ω_k²x²/2, with ω_k² = m² + Ω_k²/a² and Ω_k² = Σ4sin²(k_i/2).
- The physical mass m is fixed, as G0-c requires.

**Zeroth order (proved; checked).** The vacuum is the instantaneous ground state.
- e₀(t) = ε₀(μ)/(a ℓ₀)⁴ with μ = m ℓ₀ a.
- Its drift is d ln(e₀a⁴)/d ln a = 2c_ρμ²/ε₀(0). That is 1.9e-35 for μ = 1e-17 (`r1914_v1_lag.out:55-57`).
- So e₀ is **not** constant (answering (i)). It falls like radiation, with w = 1/3 for massless content (R11-3's M/U result, counted once).
- The vacuum fluid with p = −d(ρV)/dV is exactly conserved: ρ̇ + 3H(ρ + p) = 0 (sympy, `r1914_checks.out:29`).

**Second order: the lag (proved; checked).**
- Let H′_s = H + sH_ub(vp + pv)/2 be the instantaneous Hamiltonian in the canonical frame v = a^s x. Its ground energy is ½√(ω² − s²H²).
- For the state that evolved smoothly from the static ground state, the excess above that lowest state is

  **δE_s = H²(2 + m²/ω² − 2s)²/(16ω) per mode, ≥ 0.**

- *Proof.* The Gaussian Riccati equation Ȧ = −i(A²/M − Mω²) gives A = Mω + i(Mω)˙/(2ω) + O(2). Then E − ω/2 = |Im A|²/(4M²ω), and the frame shift adds sH⟨(xp+px)/2⟩ = −sH(Mω)˙/(4Mω²). ∎
- **Checked.** For sub-horizon modes, numerics match the formula to 4–5 digits for s = 0, 0.5 and 1, and m = 0 and 0.3. Halving H divides the excess by 4.0000. At s = 1 the massless residual falls by 16 (4th order) (`r1914_checks.out:3-26`). Horizon-crossing runs also agree at s = 0 (`r1914_v1_lag.out:1-19`).
- **The sign is variational.** Each species separately has ⟨H′(t)⟩ ≥ E₀(H′(t)). So the lag cannot be cancelled by boson–fermion pairing [proved].
- **Conformal content gives exactly 0.** Its law is static in conformal lattice units, so its eigenvectors are time-independent [proved].

**Zone total.**
- ρ_X = (1 − s)²⟨1/Ω⟩H²/(4ℓ²), with ⟨1/Ω⟩ = 0.45533 (N = 64 and 96 agree to 4e-5) (`r1914_v1_lag.out:22-28`).
- Per minimally coupled massless real dof: **ρ_X/ρ_crit = 0.954 (1 − s)²(ℓ_P/ℓ)²** (`:32`; s-family `r1914_checks.out:37-40`).
- At ℓ = ℓ_P today and s = 0, this is **1.39 ρ_Λ per dof** (`:33`).
- The dof that must be counted, conditional on J2 (gravity's zero-point in H, `vR18-6:7`), are the two graviton polarizations, which behave as minimal massless scalars. The Higgs doublet adds four more if ξ ≈ 0 (reading).

**Answer to (ii).**
- There is no standing Planck-sized injection. This contrasts with R19-10's insertion stock (`rR19-10:151-158`), now refereed only as a conditional statement (`vR19-10:24-32`).
- What remains is an O(H²/ℓ²) lag. Its size is fixed only once "the law's instantaneous Hamiltonian" is fixed.
- This makes quantitative the R19-10 referee's remark that, for a growing law, the axioms do not select the instantaneous Hamiltonian or the energy comparator (`vR19-10:40`; `AX:116-123`).
- **What s is (reading).** If a supplied qubit law fixes H(t) in site operators, then s is a property of that law, not a convention. The result then reads: the law's instantaneous ground state must coincide with the adiabatic vacuum, or the lag gravitates. If no H(t) is supplied, s is a free frame choice.

### 2.3 Probe (b): (S) with a time-dependent e₀ under V1 (Bianchi, carrier, signalling)

| Bridge on V1 | Homogeneous Bianchi | Λ̃ / leftover | Label |
|---|---|---|---|
| **Literal (S)** (C fixed) + N_red, source T_m − (V − e₀)g | Defect = V̇ = ė₀ ≠ 0. Needs a carrier Q₀ = ė₀ = −3HW (`r1914_checks.out:32`) | Even with a carrier, Λ̃ = κ(e₀(t) − C) ∝ a⁻⁴ drift: 4.3e121 ρ_Λ per scalar at Δz = 0.01 (`r1914_v1_lag.out:50-53`; count once, `rR11-3:209-211`) | checked |
| **(S-inst)**: C(t) = e₀(t) in Cg only | Defect = 3HW = −ė₀ (`r1914_checks.out:33`) | W h_μν (energy 0, pressure W ≈ (4/3)e₀) gravitates | checked |
| **(S) + (d-i) as registered** | (d-i) needs a free spatial trace with √h fixed per site and site creation (`vR17-11:23`). V1 imposes the trace, so (d-i) cannot be posed | — | reading |
| **(S_V)**: subtract the full instantaneous lowest-state stress, i.e. the per-site counterterm function −E₀(V) that R11-3 named "allowed" (`rR11-3:211`) | **Closes.** The receiver of W is e₀'s own drift, Q = ∂e₀, because T_vac = −e₀g + Wh is separately conserved (`r1914_checks.out:29,34`) | Leaves only the second-order lag ρ_X(s) of §2.2 | checked (homogeneous) |
| **(S_ad)**: (S_V) with the lowest state taken as the adiabatic vacuum (s_k = 1 + m²/2ω_k² per mode) | Closes order by order | O(H⁴): ρ/ρ_Λ ~ H²ℓ_P² ~ 1e-122 | checked to 4th order (scaling) |

**Signalling.**
- R15-1's Lemma-S channel needs the E-sector's g ≠ 0 constraint (`TESTS:4998`; `TESTS:5166-5176`). V1 has no CMC λ or g_E, so no such channel arises in the homogeneous sector (reading).
- The R19-10 referee confirms that tracking e₀(t) reopens g_E only inside class 𝒟 (`vR19-10:34`). V1 is outside 𝒟.
- At zeroth adiabatic order, (S_V)'s counterterm is a site-fluid action. The vacuum plus counterterm stress vanishes identically for every local site density. So it has no gravitational effect, local or remote (suggested).
- Not built:
  - the inhomogeneous (S_ad) subtraction;
  - a law for the lattice frame. The frame's net inertia is zero, so its motion is undetermined.

**What the lag costs without (S_ad)** (checked numbers; bounds RECALLED).
- Friedmann becomes 3H²(1 − x)/(8π) = ρ_rest, with x = 0.954 N(1 − s)²(ℓ_P/ℓ)², and ℓ ∝ a.
- For gravitons only (N = 2, s = 0) (`r1914_v1_lag.out:34-39`; N = 6 at `:40-45`):
  - BBN (|ΔG/G| < 10%) needs ℓ_today > 1.8e9 ℓ_P;
  - lunar ranging needs ℓ_today > 43 ℓ_P;
  - **60 e-folds of inflation needs x < 1 at its start, so ℓ_today > 6.7e36 ℓ_P ≈ 100 m (T_rh = 10 MeV), up to 1e19 m (T_rh = 1e15 GeV).** Colliders probe about 1e-19 m (RECALLED), so this is **excluded**.
- **Escape by tuning s.** With ℓ_today ≤ 6e15 ℓ_P, inflation needs |1 − s| ≲ ℓ_start/ℓ_P ≈ 1e-21 (T_rh = 10 MeV) down to ≈ 1e-38 (T_rh = 1e15 GeV) [checked arithmetic from the same lines]. That is a number.
- **Escape by principle.** (S_ad) sets s to the adiabatic value exactly, with no number. It is a new clause.

**Answer to (iii).**
- (S) + (d-i) + N_red + W1, read literally, cannot be posed on V1:
  - literal (S) drifts;
  - (d-i) has no free trace.
- The modified V1 bridge is (S_ad) [replacing (S) and (d-i)] + N_red + W1. That is 3 clauses and 0 fitted numbers, with homogeneous Bianchi closed and no Lemma-S channel.
- No conflict with W1 was found: (S_ad) subtracts a weight-1 density √−g⟨T⟩₀ (suggested).
- Its standing prices are in §2.6.

### 2.4 Probe (c): does R12-2's fixed-site no-go still bind with (S) in place?

**Yes (proved).**
- L-CR is pure number balance: fixed proper site density, timelike sites, flat FRW slicing and homogeneity give c̄ = 3H (`rR12-2:123-130`; `vR12-2:5`).
- No source term enters it, so changing the gravitating source to (S) + N_red leaves it unchanged.
- G0 adds the converse. Without creation, the atomic-unit spacing must grow, which is V1. With neither creation nor growth, z ≡ 0.
- So the class {site creation, V1, fixed grid} is exhaustive for translation-covariant laws on homogeneous states, and its third member is empty.

### 2.5 Probe (d): V0 options

| V0 option | Result | Label |
|---|---|---|
| V0-a: grid fixed in atomic units, records or metric "carry" expansion, static law | z ≡ 0 and no time dilation (G0-a). Excluded by T_CMB(z) and supernova dilation | proved (z); reading (data, RECALLED) |
| V0-b: static grid, dimensionless couplings drift (e.g. driven by record accumulation) | V1 in the Jordan frame: same observables (G0-b), same lag. The graviton lag is frame-independent: in lattice units M_P,lat² ∝ a² gives the same H²/(4Ω) per mode. A record drive meets the one-record-per-site budget (`rR11-3:236`) and needs R12-2's tuned F(n_rec) (`rR12-2:162-166`, suggested; count once) | proved (equivalence); suggested (record drive) |
| V0-c: galaxies moving through a fixed grid (Milne-like), or tired light | Outside G0 (translation-breaking state). Disfavoured: Ω_m ≈ 0.3 against empty Milne; no time dilation or blurring for scattering | reading, RECALLED |
| Set A (continuum, no physical Z³) | Not a lattice growth mode. It is the separate (S) + N_c package (`S26:185`; `vR18-6:9`), counted once | reading |

### 2.6 Probe (e): prices (named, none adopted)

- **P-r1914a, (S_V)/(S_ad).** "The stress of the law's adiabatic lowest state, at the current metric, weighs nothing."
  - On V1 this replaces (S)'s constant C and (d-i)'s receiver.
  - It is a new completion under literal-first (`TESTS:7124`). It goes beyond R17-7's (S−T), which the R17-7 referee calls a new bridge if dynamical (`vR17-7:32`).
  - Text touched: `AX:186-187` (source/action); `AX:116-123` (no Hamiltonian, so no canonical frame for a time-dependent law).
- **P-r1914b, the frame number.** The alternative to (S_ad): fix s (the canonical frame of "the law's variables") to the adiabatic value within 1e-21–1e-38. This is the one number found.
- **P-r1914c, no lattice-native scale.**
  - G and all masses are supplied in metric units.
  - ℓ/ℓ_P ∝ a, ≥ 1e50 since inflation.
  - The scale-reference gate (`AX:189-190`) is false except at one epoch.
  - ℓ_today/ℓ_P is a free datum, bounded above by lattice-violation and collider limits.
  - A lattice-produced graviton whose coupling is fixed in lattice units is excluded by lunar ranging (×1000).
  - This sharpens and counts once R11-3's P-V1b/c (`rR11-3:242-243`).
- **P-r1914d, the lattice-frame law.** Under (S_V) the vacuum plus counterterm carries no inertia, so the lattice frame's motion needs its own rule. Lattice-scale Lorentz-violation effects refer to that frame.
- **Inherited, counted once:**
  - P93 (our vacuum is the global minimum; `vR17-7`);
  - dynamical dark energy (Λ̃ = 0 exactly; `vR17-7` corrections);
  - J2 for the graviton lag (`vR18-6:7`).

---

### 2.7 Strongest statement (worker)

**Fixed site sets.** On a fixed site set with a translation-covariant law (`AX:57`), cosmological redshift is exactly the growth of the lattice spacing in atomic units (Lemma G0, proved). So a grid fixed in physical units cannot produce z. Growth without site creation is V1 in some frame, and it is consistent with lunar ranging only if neither G nor any mass is lattice-native, so ℓ/ℓ_P ∝ a.

**V1 and the bridge.**
- Literal (S), a fixed C, leaves a Planck-radiation-like drift Λ̃ ∝ a⁻⁴, and literal N_red then breaks Bianchi.
- Subtracting the full instantaneous lowest-state stress, (S_V), closes homogeneous Bianchi with no carrier field and no Lemma-S channel. The receiver of the enthalpy is e₀'s own drift.
- The vacuum's sign-definite, un-pairable second-order lag ρ_X = 0.954(1 − s)²(ℓ_P/ℓ)²ρ_crit per minimally coupled dof then gravitates under N_red. For s ≠ 1 this rules out 60 e-folds of inflation unless |1 − s| ≲ 1e-21–1e-38, which is a number.

**The number-free completion.** V1 + (S_ad) + N_red + W1 has 3 clauses and 0 numbers, and is checked in the homogeneous sector. It is a new completion, not (S) as registered. It gives up the scale reference, and its inhomogeneous, non-signalling form is unbuilt.

**Overall.** Site creation is refereed OPEN. Therefore the fixed reading is **OPEN**: neither ALT-GROWTH-OK nor NO-NUMBER-FREE-GROWTH is met.

---

## 3. Prior art (each counted once)

- **R11-3 and its verdict** (`vR11-3:43-57,79-81`):
  - V1 is SOURCED, with two tadpoles;
  - the fixed-site V2/V3 are excluded on expansion;
  - the per-site function f(V) is allowed (`rR11-3:211`);
  - G ∝ a² if gravity is induced (`rR11-3:216`).
- **R12-2 and its verdict** (`vR12-2:5,17`): L-CR, and "records-only".
- **R17-7 and its verdict** (`vR17-7:44-50`): Bianchi gives ∂C = 0 without a carrier; a local exchange sector is allowed.
- **R17-11 and its verdict** (`vR17-11:5-23`): (d-i) in class 𝒟; the free trace is a postulate.
- **R18-6 and its verdict** (`vR18-6:3-13`): N_red, J2.
- **R19-6 and its verdict:** W1.
- **R19-10** (`rR19-10:151-203`) and its referee (`vR19-10`, NOT CONFIRMED, OPEN; read 05:37Z).
- **SUMMARY §25** (`SUMMARY.md:662-664`).
- **Comparators (RECALLED):**
  - the adiabatic regularization of Parker and Fulling;
  - the cutoff vacuum term H²Λ_c²/(16π²) (Maggiore 2011). Our ρ_X at s = 0 is its lattice version: the continuum cutoff gives ⟨1/(4ω)⟩ → Λ_c²/(16π²);
  - Wetterich's "universe without expansion" (field-dependent masses, frame equivalence);
  - the LLR Ġ/G bound;
  - BBN ΔG/G;
  - CMB T(z) and supernova time dilation.

---

## 4. Archived runners rechecked (before relying on them)

All 27 runners were copied to `S/recheck/` and rerun there; nothing was run in the repository:
- R11-3: 5 runners;
- R12-2: 3;
- R17-7: 5;
- R17-11: 4;
- R19-10: 10.

**All are IDENTICAL to their stored outputs** after the `[Ns]` timing brackets are stripped (`S/recheck/recheck_summary.out`). The R11-3 runners write their `.out` beside the script, so the copies were used and the stored originals were preserved in `stored/`.

---

## 5. Scope and strong words

- **"proved":**
  - G0, for translation-covariant laws on statistically homogeneous states;
  - the 2nd-order lag formula, for quadratic (free) modes;
  - the variational sign, for any H′(t).
- **"exactly":**
  - wavenumber conservation;
  - conformal content static.
- **"excluded":**
  - V0-a, by observed z (data RECALLED);
  - V1 with s = 0 plus inflation, against collider limits (RECALLED, reading level).
- **Not covered:**
  - interacting fields;
  - the inhomogeneous (S_ad) subtraction and the lattice-frame dynamics;
  - quantum graviton dispersion (taken as NN-scalar-like, reading);
  - Dirac or Wilson lags (bounded below by 0, not computed);
  - qubit (bounded) versions of the oscillators;
  - non-adiabatic eras (reheating), where real particle production gravitates as in GR.
- **Not claimed:** any refereed no-go. No FAIL or no-go reading is asserted, so a referee is optional. The V1 inflation exclusion with s = 0 and Lemma G0 are the referee items if one is run.

## 6. Files (`S/`)

- `r1914_v1_lag.py/.out`: Riccati lag checks; zone averages; cosmology bounds; literal-(S) drift; e₀a⁴ drift.
- `r1914_checks.py/.out`: sub-horizon checks and H² scaling; sympy homogeneous Bianchi for the (S) variants; the s-family of zone totals.
- `recheck/`: copies of the archived runners, their `.rerun` outputs, `stored/` originals, `run_all.sh`, and `recheck_summary.out`.
