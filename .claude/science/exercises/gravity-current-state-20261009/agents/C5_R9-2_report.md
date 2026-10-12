# C5 R9-2 report: the interacting stress tensor on the box, the fall of bound bodies, and the free shear mass

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 16:38Z to about 17:30Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R9-2/`. Scripts and outputs in `S/scripts/` (all at `OMP_NUM_THREADS=2`, each under 6 min):
- `r92_fall_d1.py` → `r92_fall_d1_L{512,1024,2048}.out`: the d = 1 fall identities on lattice operators;
- `r92_fall_rt.py` → `r92_fall_rt_part1.out` (M_b = 0.85) and `r92_fall_rt_0.95.out`: real-time lapse evolution. `part1` ends in a traceback: a variable-name collision broke the second M_b. The script was fixed and M_b = 0.95 was rerun separately; the M_b = 0.85 lines were computed before the collision and are valid;
- `r92_weyl_density.py` → `r92_weyl_density_L512.out`, and `r92_weyl_density_b.py` (the same script, one test pair) → `r92_weyl_density_L1024.out`: the interaction's energy density and its moments;
- `r92_shear.py`, `r92_shear_conv.py`, `r92_shear_tune.py` → `.out`: part (a);
- `r81_common.py` is R8-1's module, copied unchanged.

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`). `TESTS.md` C5 method (`:2302-2440`), rounds 7–8 and all results through part 3 (`:3240-3573`), round 9 (`:3575-3791`; R9-2 at `:3643-3677`). `agents/C5_S8_synthesis.md` (§4–5). `SUMMARY.md` §§21–23 (`:534-606`). `agents/C5_R8-1_report.md` in full, and its referee verdict `scratchpad/C5/ref_R8-1/REFEREE_VERDICT.md` (CONFIRMED WITH CORRECTIONS, PASS WITH SCOPE; it appeared before I started). `agents/C5_R8-2_report.md` and `_referee_verdict.md`. `agents/C5_R7-4_report.md` and `_referee_verdict.md`. `agents/C5_R7-1_referee_verdict.md` (`:91-110,160-275`). `PRICE_NOTE.md:270-360`. `agents/C4_V3_referee.md` and the V3 scripts (`scratchpad/C4/V3/v3_tables.py`). `scripts/C5/R8-2/r82_edge.py`. R8-1's scratch scripts.
**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED.

---

## 0. In plain words

- **Binding energy can be made to weigh exactly like mass, in d = 1.** I build an energy density for R8-1's interacting two-body law. It is the free density of R8-2 plus a density for the interaction energy, placed at the pair's centre of energy. Its total is the full Hamiltonian, binding energy included. Its energy dipole is exactly R8-1's interacting boost K (proved; the dipole checked on the lattice to the finite-difference floor).
- **Energy is conserved locally everywhere. Momentum is conserved locally on the box sector only.** The momentum balance fails only in R8-1's *transition shell*, the band of lattice-scale total momenta Π₁ < |P| < Π₂ where the interaction is switched off. There the energy current is not a conserved momentum (checked: ‖[H, J′]ψ‖/‖Hψ‖ = 1–3e-2).
- **Bound bodies then fall universally.** In a uniform field, the centre of energy of every box-sector state accelerates at exactly −g(1 − 2V²) at linear order. That holds for a bound pair, an unbound pair, any binding fraction, at rest or moving within the rapidity budget. Proved from the box Poincaré algebra (Einstein's elevator). Checked: η between binding fractions 0.05, 0.15 and 0.30 is at most 3.0e-13 at rest and 5.6e-13 moving (L = 1024–2048). That is the double-precision floor; the underlying operator residuals are still converging (5e-11 – 5e-10 at L = 2048).
- **The interaction density is what does it.** Comparator: if only the free energy gravitates, the same bodies give η = 0.12–0.32.
- **Why R7-4's conditional exclusion does not bite.** Its chain needs the momentum Ward identity on all states. Here that identity has a source in the transition shell. The first moment K itself is globally self-adjoint, so the escape is not R7-1's "no global exponentiation" escape. The price is new: the linear graviton coupling is gauge-invariant only on the box sector.
- **Free shear (a).** R8-2's class has an empty vacuum, so its uniform-strain response is exactly zero. Give the same dispersion a zero-point energy or a filled sea, and V3's E_g shear mass returns. It is carried entirely by the edge (proved): μ_E = −0.206 (literal edge) or +7.98e-3 (gapped edge) at m = 1, against V3's +1.97e-3. μ_T2 = 0. An edge family between the two has a zero, at a mass-dependent point: a tuning, as in V3.
- **d = 2** is not built here. The fall identity would follow from R8-1's refereed d = 2 algebra once the same density exists (suggested).

**Against the FIXED readings.**
- (b)–(c), worker reading: **PASS WITH SCOPE (d = 1)**. η = 0 exactly at linear order (proved), checked to 1e-13.
  - If the referee requires d = 2, or a momentum Ward identity on all states rather than on the box sector, the reading is **INCONCLUSIVE**.
  - FAIL is not available. §3 is an explicit construction in the stated class.
- (a): **SHEAR-PRESENT, conditional on vacuum energy, edge-carried**: μ_E = −2.0565e-1 (L) and +7.9761e-3 (G), m = 1, d = 3. In R8-2's literal empty-vacuum class it is SHEAR-ABSENT (0 exactly, trivially).

---

## 1. Hypotheses and class (stated before any title)

- **H-law.** R8-1's repaired d = 1 two-body law (`C5_R8-1_report.md:95-116`; referee CWC, PASS WITH SCOPE, `ref_R8-1/REFEREE_VERDICT.md:1-3,12-13`).
  - One CAR mode per site, graded composition, continuous time, two-particle sector.
  - ε = √(m² + s(k)²) with s = k on |k| ≤ B = 2.6.
  - H = H₀ + W, with W(P) = c(P)[√(M² + P²) − √(M₀² + P²)] and M = M₀ + λ|g⟩⟨g|.
  - Plateau: c = 1 on |P| ≤ Π₁ = 0.6, c = 0 on |P| ≥ Π₂ = 1.2.
  - Parameters m = 0.5, κ = 0.4. Bound masses M_b = 0.95, 0.85, 0.70, i.e. binding fractions f_B = (2m − M_b)/2m = 0.05, 0.15, 0.30 (λ = −1.68, −3.17, −5.31).
- **H-free.** The free part of the stress is R8-2's Construction A (`C5_R8-2_report.md:73-90`; referee-confirmed, `C5_R8-2_referee_verdict.md:5-21`). It works for any C^∞ periodic ε, and its energy dipole is Σ_i ½{X_i, ε_i} = K₀ = ½{H₀, X_P} (`C5_R8-1_report.md:111`).
- **H-grav.** A static uniform field enters through a linear lapse, H_g = Σ_x (1 + g x) T⁰⁰(x) = H + g D₁, where D₁ is the first moment of T⁰⁰ (O2 Lemma F setting, `C5_R8-2_report.md:35`). Linear order means O(g). The gravitating momentum is J′ := ∫T⁰¹.
  - This is a spatially varying lapse acting on a composite's centre of energy with binding energy included, which is what the C4 V2 referee asked for (`C4_V2_referee_full.md:184-187`).
- **H-sector.** The box sector is R8-1's domain 𝒟₂: antisymmetric C_c^∞ two-particle wavefunctions with |P| < Π₁ and legs in the box (`C5_R8-1_report.md:64`).
- **Excluded, not addressed:**
  - N ≥ 3 (R9-3);
  - pair creation and loops (R8-4, R7-5);
  - gauge fields (R8-5);
  - the graviton's own dynamics;
  - the local-lapse algebra W4 (only a linear lapse is used);
  - d = 3;
  - ungraded ⊗M₂;
  - tidal (non-uniform) fields, which would test second moments of T⁰⁰.
- **Outside realizations not excluded.** The stress is not unique: improvement terms and other densities with the same zeroth and first moments exist. In a uniform field at linear order, H_g depends on T⁰⁰ only through ∫T⁰⁰ and its first moment (proved: H_g = H + gD₁). So every such choice gives the same fall.

## 2. Prior art (each counted once)

- **R8-2.** Free universal stress (Construction A), Lemma U, Theorem E, η = 0 only as a free-packet proxy, and no bound-body observable (`TESTS.md:3550-3557`; `C5_R8-2_referee_verdict.md:60-66`). R8-2 §3.6 already flags the d = 1 flow-covariant escape as not constructed (`C5_R8-2_report.md:167`).
- **R7-1 referee.** W2 (interacting stress) not established; W1 only on the χ = 1 subbox; inert edge violates universality (`C5_R7-1_referee_verdict.md:212-250`).
- **R7-4.** Lemma 1 (formal i[H,D] = J, [H,J] = 0) and the conditional box exclusion (`C5_R7-4_referee_verdict.md:35-55,75`).
- **R8-1.** The repaired law, the global self-adjoint K (`C5_R8-1_report.md:137-146`; referee item 4), Theorem L (`:230-243`; referee item 5).
- **R7-6.** P = Q and the instant form (`TESTS.md:3508-3509`): used here only in that P is kinematic and the boost carries the interaction.
- **V3 and the RN L1 seagull correction.** μ_E = +1.97038864e-3 per cell (`PRICE_NOTE.md:290-295,341-352`; `C4_V3_referee.md:3-7`).
- **O2 Lemma F** (`C5_O2_report.md:118-131`): band-bottom fall ẍ = −Hess(E²/2)∇Φ.
- **M1** (`SUMMARY.md:405`): globally isolated composite bands carry the averaged anomaly. Here the bound state is not globally isolated: it dissolves into the continuum for |P| ≳ Π₂ (`r81_d1_ring_L512.out`, (d)).
- **C4 V2** (`TESTS.md:1695`; `C4_V2_referee_full.md:180-187`): a scattering-sector Ward defect and composite universality; the referee's point that the Eötvös test needs a spatially varying lapse and the composite's centre of mass.
- **Wall T72** (`C5_R4-4_report.md:35`, citing `WALLS.md:91` on branch `claude/toe-walls-20260929`): "composites fall by O(binding)". Related, not the same setting.
- **Repo search.** A grep for Weyl-midpoint or centre-of-energy densities, "binding energy" and Rindler in the packet and in `docs/` found no prior construction of an interaction energy density for a box law. The one Weyl-symbol hit (`docs/ADMISSIBILITY_INCIDENCE_SCALAR_NONLINEAR_WARD_..._2026-08-14.md:5`) is a different object: a second-order Ward obstruction for Block95.
- **Literature (comparator, RECALLED, not verified this run).** Current operators in relativistic direct-interaction quantum mechanics (Lev; Klink; Polyzou) build conserved covariant currents for Bakamjian–Thomas models from form factors. I did not use them; the construction below is direct.

---

## 3. Construction: an interacting stress for R8-1's d = 1 law

### 3.1 The interaction's energy density (proved; checked)

- **Definition.** Let Q be the total-momentum transfer, P̄ = P + Q/2 the Weyl midpoint, and χ(Q) a C^∞ even bump (1 on |Q| ≤ 1, 0 on |Q| ≥ 2). In R8-1's chart (P, q), set

  ⟨P+Q, q′| T⁰⁰_W(Q) |P, q⟩ = χ(Q) · c(P̄) w(P̄; q′, q) √(J′J),

  where w is R8-1's exact smooth BT kernel and J the chart Jacobian. The real-space density is T⁰⁰_W(x) = ∫e^{iQx} T⁰⁰_W(Q) dQ/2π. It is translation covariant, because T⁰⁰_W(Q) changes lattice momentum by exactly Q.
- **Equivalently,** T⁰⁰_W(Q) = χ(Q) e^{iQX_P/2} W e^{iQX_P/2}. X_P = i∂_P|_q in the chart (`C5_R8-1_report.md:112`), so e^{isX_P} shifts P by s at fixed q.
- **Moments (proved).**
  - T⁰⁰_W(0) = W.
  - d/dQ T⁰⁰_W(Q)|₀ = (i/2){X_P, W}, using χ′(0) = 0. So the first moment is ½{X_P, W}.
- **Total density.** T⁰⁰ := T⁰⁰_A + T⁰⁰_W. Then
  - ∫T⁰⁰ = H₀ + W = H;
  - the first moment is K₀ + ½{X_P, W} = ½{H, X_P} = **K**, R8-1's global boost (`C5_R8-1_report.md:110-111`).
- **Hermitian.** T⁰⁰_W(Q)† = T⁰⁰_W(−Q), since W is Hermitian and χ is real and even.
- **Quasi-local (proved).** In centre coordinates the kernel factorizes as [W's kernel in the centre difference Y′ − Y] × χ̂((Y + Y′)/2 − x).
  - W's kernel is super-polynomial (R8-1).
  - χ̂ is Gevrey-2, decaying like exp(−c√r). Checked: χ̂(r) = 3.4e-3, 2.8e-6, 2.7e-11 and 6.1e-16 at r = 10, 50, 200 and 400 (`r92_weyl_density_L512.out`).
  - The relative coordinate is controlled by g's compact support.
- **Checks on the lattice ring** (`r92_weyl_density_L512.out`). Test packets: bound at P₀ = 0, centred at x = 7, against bound at P₀ = 0.03, centred at x = 4. M_b = 0.85, L = 512.
  - Zeroth moment: |⟨a|T⁰⁰_W(0)b⟩ − ⟨a|Wb⟩| = 2.8e-17, against |⟨a|Wb⟩| = 0.209.
  - First moment: d/dQ⟨a|T⁰⁰_W(Q)b⟩ = 0.486421 − 1.128716i, against i⟨a|(K − K₀)b⟩ = 0.486469 − 1.128786i. Relative difference 6.9e-5 at L = 512 and 4.3e-6 at L = 1024 (`r92_weyl_density_L1024.out`). The factor 16 is the O(h⁴) scaling of the Richardson difference with h = 2π/L, so this is the finite-difference error, not a defect.
  - Hermiticity: 4.2e-15.
  - Here K and K₀ are R8-1's independent lattice operators, so this checks the Weyl-ordering identity against the boost that R8-1's referee confirmed.

### 3.2 Energy current: exact Ward identity on all states (proved)

- **Definition.** T⁰¹(Q) := [H, T⁰⁰(Q)]/D(Q), with D R8-2's generalized forward difference (D = Q near 0; only zero at Q = 0; D(Q)* = −D(−Q); `C5_R8-2_report.md:92-94`, confirmed `C5_R8-2_referee_verdict.md:17-18`).
- **Why it is smooth.** [H, T⁰⁰(0)] = [H, H] = 0, so the quotient is C^∞ by Hadamard, as in R8-2's referee note. Hence super-polynomially quasi-local.
- **Hermitian.** T⁰¹(Q)† = [T⁰⁰(−Q), H]/D(Q)* = [H, T⁰⁰(−Q)]/D(−Q) = T⁰¹(−Q).
- **The Ward identity** [H, T⁰⁰(Q)] = D(Q) T⁰¹(Q) holds by construction on every two-particle state.
- **Its integral** is J′ := T⁰¹(0) = i[H, K] (sign fixed by D = Q near 0).
  - On 𝒟₂, J′ = P, by R8-1's [K, H] = iP.
  - Checked: ‖J′ψ − Pψ‖/‖Pψ‖ = 5.3e-10 and 3.1e-10 for bound states at rest, and 4.3e-10 and 2.5e-10 moving (L = 2048, `r92_fall_d1_L2048.out`). It converges with L: 5e-4 at L = 512 and 1e-6 at L = 1024.

### 3.3 Momentum current: exact on the box sector, with a source in the transition shell (proved; checked)

- **Symmetry.** In d = 1, T¹⁰ := T⁰¹, so symmetry is trivial and is not a test here.
- **Definition.** T¹¹(Q) := ([H, T⁰¹(Q)] − 𝒮(Q))/D(Q), where 𝒮(Q) is the Weyl-midpoint density (same χ) of the operator [H, J′].
  - The numerator vanishes at Q = 0, so T¹¹ is C^∞ and quasi-local.
  - Hermitian: [H, J′] is anti-Hermitian, so 𝒮(Q)† = −𝒮(−Q), and the same steps as §3.2 apply.
- **The resulting identity** is [H, T¹⁰(Q)] = D(Q) T¹¹(Q) + 𝒮(Q), i.e. ∂_μT^{μ1} = s.
- **Where the source lives (proved).** Fibrewise in P, using X_P = i∂_P|_q:
  - **Plateau** (|P| ≤ Π₁): H = √(M² + P²), so J′ = P and [H, J′] = 0.
  - **Free region** (|P| ≥ Π₂, where c and all its derivatives vanish): J′ = J_E = Σε_iε_i′ (R8-2's energy current), which commutes with H₀.
  - **Transition shell** (Π₁ < |P| < Π₂): [H, J′] is generically nonzero, because M and M₀ do not commute and c′ ≠ 0. It is supported on supp g in the relative momentum.
  - Hence for any two states with total momenta in the plateau, every matrix element of 𝒮(Q) vanishes: the Weyl midpoint of two plateau momenta lies in the plateau, by convexity. **So the momentum Ward identity is exact on the two-body box sector.**
- **Checked** (`r92_fall_d1_L1024.out`; shell numbers are converged between L = 512 and 1024):

| packet | ‖[H,J′]ψ‖/‖Hψ‖ | ‖J′ψ − Pψ‖/‖Pψ‖ |
|---|---|---|
| box sector, bound or scattering, at rest or moving (L = 2048) | 2.6e-11 – 1.6e-10 | 2.5e-10 – 5.3e-10 |
| transition shell, P₀ = 0.9, M_b = 0.95 / 0.85 / 0.70 | 1.0e-2 / 1.9e-2 / 3.2e-2 | 0.42 / 0.79 / 1.2 |
| free region, legs in box, P₀ = 1.6 | 1.6e-7 – 3.0e-7 (converging) | 1.2e-7 – 2.2e-7 |

**So (b) is met in d = 1, in this sense:**
- symmetric (trivially, d = 1);
- Hermitian;
- quasi-local, with super-polynomial C^∞ tails (Gevrey-2 from χ, plus W's tails);
- ν = 0 Ward identity exact on all two-particle states;
- ν = 1 Ward identity exact on the two-body box sector, with an explicit source supported in the transition shell;
- ∫T⁰⁰ = H;
- first energy moment = R8-1's interacting K.

**Can the shell source be removed? Suggested, not proved.**
- A momentum Ward identity on all states needs [H, i[H, D₁]] = 0 for D₁ = K + B, with B translation-invariant and quasi-local.
- The fibrewise solution is adiabatic transport in P. That makes J′ diagonal in each fibre's energy basis. But in the two-body continuum its gauge potential has principal-value kernels wherever the phase shift varies along the flow, which is exactly the transition shell. That suggests power-law, not quasi-local, tails.
- R7-4's chain gives the same conclusion conditionally: R7-4 Lemma 2 plus the d = 1 flow dk_i/ds = ε_i, which carries plateau pairs into the c = 0 region, where the phase shift is zero.
- **Escape, named but not built:** a "flow-covariant" interaction depending only on the lattice relative rapidity ϑ = θ₁ − θ₂, with θ = ∫dk/ε. It would have to act on edge pairs, so it is not box-supported. This is R8-2 §3.6's open d = 1 corner.

---

## 4. The fall of bound bodies (part (c))

### 4.1 Operator identity: Theorem E plus the interaction term (proved)

With H_g = H + gK and J′ = i[H, K]:

**dJ′/dt = i[H_g, J′] = 𝒩 − g(H + 𝒜), with 𝒩 := i[H, J′] and 𝒜 := −i[K, J′] − H.**

- **Box sector 𝒟₂.** 𝒜ψ = 𝒩ψ = 0 (proved from R8-1's algebra on the invariant domain: J′ψ = Pψ, [K, P] = iH).
- **Free region, legs in the box.** 𝒜 = 𝒩 = 0.
- **Free region, edge legs.** 𝒜 = dΓ(εA), A = Hess(ε²/2) − 1, and 𝒩 = 0. This is R8-2's Theorem E.
- **Transition shell.** 𝒜 and 𝒩 are nonzero.
- **Also exact, globally on legs-in-box states (proved).** [K, P] = ½{H, [X_P, P]} = iH, because [X_P, P] = Σ_i ε_i s_i′/H₀ = i there. So the lattice momentum obeys d⟨P⟩/dt = −g⟨H⟩ even in the shell (checked: |w_P − 1| ≤ 1.1e-13 for every packet at L ≥ 1024, shell included; 1e-11 at L = 512). In the shell what fails is the link between momentum and centre-of-energy velocity (J′ ≠ P), together with the non-conservation of J′.

### 4.2 Centre-of-energy acceleration (proved)

- **Definitions.** X_E := ⟨K⟩/⟨H⟩ and V := ⟨J′⟩/⟨H⟩. Exactly:
  - d⟨K⟩/dt = ⟨J′⟩;
  - d⟨H⟩/dt = −g⟨J′⟩;
  - d⟨J′⟩/dt = ⟨𝒩⟩ − g⟨H + 𝒜⟩.
- **Result.** At O(g):

  **Ẍ_E = −g(1 + ⟨𝒜⟩/⟨H⟩) + 2gV² + ⟨𝒩⟩/⟨H⟩ (plus terms of order g·⟨𝒩⟩).**
- **On the box sector:** Ẍ_E = −g(1 − 2V²), for every state. This is the relativistic form of fall in a static lapse (the R8-2 semiclassical [2(v·g)v − g], `C5_R8-2_report.md:123`). It depends only on the centre-of-energy velocity, not on composition or binding.
- **So η = 0 exactly** at linear order, between any two box-sector bodies with equal V, at rest or moving within the box.
- **To O(g²) at rest:** Ẍ_E = −g(1 + gX_E), the Rindler lapse factor, again universal.

### 4.3 Checks

**(i) Identities evaluated on lattice operators.** No algebra is assumed. ⟨[K, J′]⟩ is computed as ⟨Kψ|J′ψ⟩ − ⟨J′ψ|Kψ⟩, with J′ψ = i(HKψ − KHψ). Files: `r92_fall_d1_L{512,1024,2048}.out`. Gaussian P-profiles: σ = 0.06 at P₀ = 0, σ = 0.04 at P₀ = 0.25. The plateau tails are below e⁻¹⁹.

| L | body | f_B | (Ẍ_E/g) − (−1 + 2V²) | w_P − 1 (lattice momentum) | comparator: only free energy gravitates, ⟨H₀⟩/⟨H⟩ |
|---|---|---|---|---|---|
| 2048 | bound, rest | 0.15 | −2.0e-13 | 0.0 | 1.257196 |
| 2048 | bound, rest | 0.05 | −8.8e-14 | −5.2e-15 | 1.111111 |
| 2048 | bound, V = 0.282 | 0.15 | −2.3e-13 | 4.9e-14 | 1.239408 |
| 2048 | bound, V = 0.254 | 0.05 | −1.6e-13 | 7.8e-14 | 1.104539 |
| 1024 | bound, rest | 0.30 | −3.9e-13 | −5.7e-15 | 1.533784 |
| 1024 | scattering pair, rest | (unbound) | +3.0e-13 – +9.6e-13 | ≤ 1.4e-15 | 1.236 – 1.470 |
| 512 → 1024 → 2048 | bound, rest, f_B = 0.15 | | −2.4e-9 → −2.1e-13 → −2.0e-13 | | |

The last row shows convergence to the double-precision floor.

**η between binding fractions (linear order).** Interacting stress first, then the comparator in which binding energy does not gravitate:
- f_B 0.15 vs 0.05: η = 1.1e-13 at rest and 6.6e-14 moving (L = 2048). Comparator: 0.123 and 0.115.
- f_B 0.30 vs 0.05: η = 3.0e-13 at rest and 5.6e-13 moving (L = 1024). Comparator: 0.320 and 0.294.
- f_B 0.30 vs 0.15: η = 1.8e-13 at rest and 3.7e-13 moving (L = 1024). Comparator: 0.198 and 0.180.

**(ii) Real-time evolution.** No commutator identity is used. L = 512, RK4, g = 2e-3, T = 4. Files: `r92_fall_rt_part1.out`, `r92_fall_rt_0.95.out`.
- D₁ = K: d⟨P⟩/dt ÷ (−g⟨H⟩) = 0.999993746 (f_B 0.15) and 0.999993741 (f_B 0.05). Ẍ_E/g = −1.000034 for both.
  - The common 6e-6 offset is the O(g) fit systematic. The difference between the bodies is 5e-9 in the slope ratio, the L = 512 discretization level (the L = 512 identity check gives 1e-9).
- Comparator D₁ = K₀: slope ratio 1.2571886 against ⟨H₀⟩/⟨H⟩ = 1.2571960 (f_B 0.15), and 1.1111042 against 1.1111111 (f_B 0.05).

**(iii) The transition shell, where the box law is switched off.** Shell packets at P₀ = 0.9 give ⟨𝒜⟩/⟨H⟩ = +0.059, +0.234 and +0.628 for f_B = 0.05, 0.15 and 0.30. So bodies whose total momentum sits at lattice scale fall non-universally, at O(0.1–0.6). This is the composite analogue of Theorem E. At Π₁ ≈ 0.6/a it lies far outside lab kinematics if a ~ ℓ_P (reading).

### 4.4 R7-4's hypotheses (part (d))

- **Self-adjoint, exponentiating D: satisfied, not violated.** D₁ = K = ½{H, X_P} is globally self-adjoint (`C5_R8-1_report.md:137-146`; R8-1 referee item 4), so e^{isK} exists for all s.
- **Violated: the global premise of R7-4 Lemma 1**, that the constraint (momentum Ward identity) is preserved on all states (`C5_R7-4_referee_verdict.md:35-41`).
  - Here [H, J′] ≠ 0 in the transition shell, so e^{iHt}Ke^{−iHt} = K + tJ′ fails as an operator identity.
  - It holds on the box sector. H preserves P-support, and J′ = P there.
  - The Cook/Møller step (Lemma 2) and the "all-s" flow invariance (Lemma 3) are therefore never reached. Møller intertwining is not examined.
- **On the box sector,** the S-matrix commutes with the boost flow only for rapidities inside R8-1's Theorem L budget. That is consistent with box-supported scattering: R7-4's referee's "local rapidity domain" escape (`:75`), now with a stress tensor attached.
- **Rapidity range on which (b) is exact.** The ν = 1 identity is exact for matrix elements between states with P-support in |P| ≤ Π₁ (legs in the box).
  - Finite boosts keep a state there up to η* = asinh(Π₁/m_⊥) − asinh(|P|/m_⊥) per internal-mass component (`C5_R8-1_report.md:232-236`).
  - For the M_b = 0.85 bound state at rest, η* = 0.658 in these lattice units. Physical size, reading only: with a = ℓ_P and Π₁ = O(1)/a, lab bodies are deep inside.

---

## 5. Part (a): uniform-strain susceptibility of R8-2's box⊕edge stress

**Method (proved).**
- Uniform strain couples through the first moment of the momentum density. For R8-2's stress, the forward momentum density is p = ∇(ε²/2), the gravitating momentum (`C5_R8-2_report.md:89`).
- So the strain flow is dk/de = ½h·p(k), in RN-L1 normalization as for V3's scalar (`v3_tables.py:3-4`).
- V3's Liouville formula (`C4_V3_referee.md:13-17`) gives E(e) = ⟨J_e ε_vac⟩.
- Integrating by parts on the torus gives μ = d²E/de² = −⟨(div v)(v·∇ε_vac)⟩, with v = ½h·p.
- For E_g, div v = ½(A_xx − A_yy) with A = Hess(ε²/2) − I. That is zero on the box. **The integrand is supported on the edge: the edge carries all of μ_E.**
- For T_2g, div v = 0 identically, so μ_T2 = 0 (Liouville).

**Vacua.**
- **(F) R8-2's own class.** Number-conserving, normal-ordered T on the empty Fock vacuum. T(q)|0⟩ = 0, so every vacuum correlator of T vanishes: **μ_E = μ_T2 = 0 exactly** (proved, trivial). The S8 synthesis already notes that "C-box's tested vacuum is empty" (`C5_S8_synthesis.md:297`).
- **(Z)/(S) Conditional.** Give the same dispersion a zero-point energy +ε/2 (scalar reading) or a filled sea −ε (Dirac reading), as any pair-creating completion (R8-4) would.

**Calibration (checked, `r92_shear.out`).** V3's NN scalar at m = 1 gives +1.970388642e-3 (closed form) and +1.970388636e-3 (direct flow), against V3's +1.970389e-3. At m = 0.5: +2.467156e-3, matching V3.

**Results** (d = 3, zero-point vacuum, RN-L1 normalization; converged, closed form N = 640 against direct flow N = 128; `r92_shear_conv.out`):

| profile | m | μ_E | box part | direct flow, N = 128 | ratio to V3 (m = 1) |
|---|---|---|---|---|---|
| L (literal) | 1.0 | −2.0565108e-1 | ~1e-10 (quadrature) | −2.05576e-1 | −104 |
| L | 0.3 | −3.2604749e-1 | ~1e-10 | −3.25966e-1 | |
| G (gapped) | 1.0 | +7.9760558e-3 | ~1e-14 | +7.97597e-3 | +4.05 |
| G | 0.3 | +9.0482464e-3 | ~1e-14 | +9.04816e-3 | |

- A filled sea (−ε) gives −2× these values. d = 2 values are in `r92_shear.out`.
- **Tuning (checked, `r92_shear_tune.out`).** Along g_t = (1 − t)g_L + t g_G, with the box fixed at k², μ_E changes sign. Its root is t* = 0.287922 (m = 1) and 0.297708 (m = 0.3). So removing the shear means choosing the edge shape: one mass-dependent tuning per species, like V3's a* (`PRICE_NOTE.md` 2b).

**Reading for (a): SHEAR-PRESENT, conditional on vacuum energy, edge-carried.**
- μ_E = −2.06e-1 (L) or +7.98e-3 (G) at m = 1, against V3's +1.97e-3. μ_T2 = 0.
- In R8-2's literal empty-vacuum class it is SHEAR-ABSENT, at 0 exactly.
- S8's expectation (SHEAR-PRESENT; "the zone average still feeds the uniform-strain response") holds for vacua with energy. The mechanism is the edge's A ≠ 0, not the zone average itself: the gapped and literal edges give opposite signs, with the same zone mean of A.

---

## 6. Prices (named, not adopted)

- **P-W (new).** The linear graviton coupling's momentum Ward identity, i.e. linearized gauge invariance, is exact only on the box sector. A source s = ∂_μT^{μ1} sits at lattice-scale total momentum Π₁ < |P| < Π₂ (in units of 1/a).
  - Any process that reaches the transition shell sees a gravitating momentum that is not conserved. That includes loops (R7-5) and Planck-energy collisions.
  - Removing the source seems to need non-quasi-local densities (suggested) or a non-box-supported, flow-covariant interaction (not built).
- **Inherited.** R8-1's and R7-1's prices: non-quasi-analytic functions, a frame-fixed box, form-factor interactions, and graded fermions. Also R8-2's edge (Theorem E) and Lemma U.
- **P-S (conditional).** If the completion has a sea or a zero-point, the edge carries an E_g shear mass (numbers above). Removing it takes one mass-dependent edge tuning per species.
- **No axiom text changes.** Admissibility does not fix dynamics or a stress (`AX:116-123`). Source and gravity bridges are outside the axioms (`AX:173-190`).

## 7. Scope and strong-word check

- **"Exact"** is used only for:
  - the operator identities on 𝒟₂: J′ = P, 𝒜 = 𝒩 = 0, and Ẍ_E = −g(1 − 2V²) at O(g);
  - the ν = 0 Ward identity, true by construction on all two-particle states;
  - the vanishing of 𝒮's box-sector matrix elements;
  - the zeroth and first moments of T⁰⁰_W (Weyl ordering);
  - μ = 0 in the empty vacuum;
  - μ_T2 = 0.
- **"Checked"** numbers are finite-L and converging. The η figures (≤ 5.6e-13) sit at the double-precision floor, not at 1e-15. The proved value is 0. The claim "below 1e-15" therefore rests on the proof, with numerics agreeing to their floor.
- **d = 2 is not built.** Suggested: the same density with respect to X_E (for cW), plus improvement densities for the translation-invariant pieces εP½{S, cF} and X_NW − X_E. Hadamard's lemma then gives the ν = 0 vector current. A symmetric T^{ij} on the box sector needs a Belinfante-type step for the spin term, which is not checked. Given such a T⁰⁰, the fall identity Ẍ_E = −g + 2(V·g)V follows from R8-1's refereed d = 2 algebra ([K_a, P_b] = iδ_ab H; chart to 6e-13).
- **Two-body only.** N ≥ 3 needs R9-3's packed law. The density of a connected three-body term is the same Weyl-midpoint recipe (suggested).
- **Linear order in a uniform field.** Tidal fields test second moments, which are not fixed here.
- **The T¹¹ and T⁰¹ kernels** are not separately evaluated numerically away from Q = 0. Their properties are proved by elementary algebra (Hadamard quotient; Hermiticity via D(Q)* = −D(−Q)).
- **Labels.** Literature on relativistic current operators is RECALLED (comparator only). Physical sizes with a = ℓ_P are readings.

## 8. For the referee

1. The Weyl-midpoint density: T⁰⁰_W(Q) = χ(Q)e^{iQX_P/2}We^{iQX_P/2}, with first moment ½{X_P, W}. Check the sign and convention against R8-1's X = i∂_k, and the lattice check (6.9e-5 → 4.3e-6 from L = 512 to 1024, i.e. h⁴).
2. The support of [H, J′]: zero on the plateau and on the c = 0 region, nonzero only in the shell. Also the convexity argument that 𝒮's matrix elements between plateau states vanish.
3. Whether "exact linear Ward identity on the two-body box sector" is met by ν = 0 everywhere plus ν = 1 in box-sector matrix elements, with a shell source.
4. The fall identity (§4.2), and that the comparator (D₁ = K₀) is a fair "binding energy does not gravitate" control.
5. Part (a): the closed form μ = −⟨(div v)(v·∇ε_vac)⟩, the identification of R8-2's strain flow with p = ∇(ε²/2), and the empty-vacuum zero.
6. Whether d = 1 alone suffices for PASS (WITH SCOPE), given the setting lists d = 1 and d = 2.
