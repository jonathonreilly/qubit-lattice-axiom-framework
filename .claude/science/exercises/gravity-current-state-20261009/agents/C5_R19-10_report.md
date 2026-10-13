# C5 R19-10 report: is "the law's lowest state" well defined when the lattice creates sites?

- **Worker:** Claude Opus 5.5 (Claude Code agent), started 04:44Z, report 05:12Z, 2026-10-13. Same family as the supervisor; unrefereed.
- **Item:** `TESTS.md:7581-7610` (readings FIXED there).
- **Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C5/R19-10/` (scripts `r1910_*.py`, outputs `r1910_*.out`, archived-runner rechecks in `recheck/`).
- **Abbreviations:** `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS` = `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`; `rX`/`vX` = `agents/C5_X_report.md` / `agents/C5_X_referee_verdict.md` in that exercise folder; `S26` = `agents/C5_S26_synthesis.md`. Output files are cited as `file.out:line`.
- **Units:** lattice units a = c = ħ = 1. For the cosmology comparison a = ℓ_P, G = 1, H₀ = 1.1775e-61 t_P⁻¹, Ω_Λ = 0.685 (RECALLED), so ρ_Λ = 1.134e-123 (`r1910_e0_convergence.out:51`).

---

## 0. Reading against the FIXED readings

**Worker reading: INJECTS, bounded to a stated class 𝒞_Γ (below), in the "energy above e₀ that a growing lattice carries" sense. Referee required. If "injects" is read as only the net excitation left behind after each insertion has finished, the reading is OPEN.**

- **WELL-DEFINED: not met.**
  - Clause 1 holds for the *static* perfect law [checked]. e₀ is intensive and time-independent. Its corrections on tori are L⁻⁴ (gapless) or e^{−mL} (gapped). These are ≲ 3e-121 ρ_Λ at the Hubble size.
  - Clause 1 fails for the *growing* lattice. Insertions in progress, or the dislocation cores that local insertion into Z³ needs, shift the vacuum's energy density by a term proportional to H(t). Its size: 6.7e60 ρ_Λ (scalar ramps) to 1.2e62 ρ_Λ (Wilson-Dirac static, 3.1e62 × 0.374 per unit T) in the computed models [checked]; |3.4e61/v| ρ_Λ for dislocation climb [checked]; ≥ 5.5e59/Γ ρ_Λ in 𝒞_Γ [proved].
  - Clause 2 is not checked for any rule. A slow ("adiabatic") ramp's *net* leftover excitation extrapolates below ρ_Λ only for ramp times T ≳ 5e56 t_P [suggested; power-law extrapolation over 54 decades]. At that T, its standing in-progress energy is ~3e117 ρ_Λ [checked slope × extrapolated T].
- **INJECTS: candidate, bounded.**
  - **Product insertion, as registered:** checked. It injects 1.1e122–1.6e122 ρ_Λ per Hubble time for scalars and 1.8e123–2.6e123 for Wilson-Dirac (`r1910_insert_product.out:25-30`).
  - **Class 𝒞_Γ:**
    - a new site is born uncorrelated with the rest (a product state);
    - it is then evolved by the law plus a local insertion generator K(t), whose energy-extraction power is at most Γ;
    - energy is counted with the completed law.

    For every rule in this class the steady-state energy density above e₀ is at least (3H/a³)·ΔE_bp²/(2Γ) (Lemma S-ins, proved below). That is ≥ 5.5e59/Γ ρ_Λ for the 3D scalar and ≥ 1.5e62/Γ ρ_Λ for Wilson-Dirac, with Γ in Planck units (`r1910_numbers.out:43-54`).
  - **What the referee must rule:** whether a standing excess density counts as "injects energy above ρ_Λ per Hubble time". Under N_red it is what gravitates: it is part of V − e₀ (`S26:185`).
- **Expectation check** (`TESTS:7610`).
  - "INJECTS for product-state insertion" is confirmed. The expectation guessed "about the local zero-point gap, ~1/a" per site. The computed best-product cost is 0.04–0.06 ħc/a for scalars (about 20× below that guess) and 0.7–1.0 ħc/a for Wilson-Dirac.
  - "Adiabatic insertion is plausibly WELL-DEFINED" is **not** borne out. Slowness trades excitation for an in-progress energy that grows with T. In the untuned ramp family, the sum of the two is ≥ 6.7e60 ρ_Λ for every T.

---

## 1. Plain words

- **Fixed lattice.** The lowest-energy state of a fixed, perfect lattice law has a well-defined energy per site. It does not drift as the lattice gets bigger: the size corrections fall like 1/L⁴ and are negligible.
- **Growing lattice.** A lattice that grows by adding sites is never in that state.
  - A new site cannot arrive already entangled with its neighbours. Born unentangled, it carries extra energy, about 0.04–1 Planck energies per site. Three new sites per old site per e-fold makes that about 1e122 times the observed dark energy.
  - Adding the site slowly removes the leftover excitation. But while a site is half added, the lattice is a slightly different lattice whose lowest energy is higher. Sites are always being added somewhere, at a rate set by H, so a growing lattice always carries a population of half-added sites. Their energy is a new vacuum term proportional to H, about 1e61 times too big.
  - Adding sites the most local way (dislocation loops whose rims climb, R12-2) gives the same thing in another form: the dislocation lines carry energy, and their density is proportional to H.
  - Every escape found costs one of these:
    - a tuning to about 62 digits, one per species, which loop corrections undo;
    - insertion machinery working about 1e60 times faster than the lattice's light-crossing time;
    - instantaneous entangling action over large regions;
    - insertions as slow as the expansion itself.

---

## 2. Probe (a): e₀(L) for scalar, Wilson-Dirac and photon

**Setting.** Free fields on L³ tori.
- S(m): real NN scalar, ε² = m² + Σ4sin²(k_i/2).
- D(m): 4-component Wilson-Dirac, r = 1, filled sea, periodic (P) and antiperiodic (AP) boundary conditions.
- A: noncompact lattice Maxwell.

All runs use `r1910_e0_convergence.py`.

- **The photon equals two massless scalars [checked].** The explicit curl-curl operator on L = 3 and 4 tori gives E₀ equal to 2 × S(0) to within 1e-14, with 2(L³ − 1) nonzero modes (`r1910_e0_convergence.out:2-3`). The k = 0 holonomies contribute nothing.
- **Intensive limit and corrections [checked].** e₀(128):
  - S(0) = 1.193801, S(1) = 1.300034;
  - A = 2.387602;
  - D(0) = −6.556992, D(1) = −8.396562.

  L⁴[e₀(L) − e₀(∞)] tends to constants for gapless fields:
  - S(0): −0.84;
  - A: −1.68;
  - D(0), P: +3.35, so the sign follows the boundary condition;
  - D(0), AP: −0.79.

  Gapped fields fall faster than any power, e.g. S(1) < 1e-14 by L = 24 (`r1910_e0_convergence.out:4-36`).
- **Growing torus L → L+1 [checked].** The energy added by one inserted plane, minus e₀L², is ~L⁻⁴ per inserted site for gapless fields and ~1e-14 for gapped ones (`r1910_e0_convergence.out:37-46`). So a perfect lattice that gains whole planes gains exactly e₀ per site, up to the Casimir term.
- **Size at the Hubble scale [checked arithmetic].** At L = 1/H₀ = 8.5e60 sites the Casimir term is 1.3–2.8e-121 ρ_Λ. Its drift per Hubble time is ~5e-121 ρ_Λ (`r1910_e0_convergence.out:52-55`).
- **Boundaries [checked control].** A Dirichlet (open) box has a surface term L·d → 0.040 (m = 0) or 0.026 (m = 1) (`r1910_e0_convergence.out:48-49`), i.e. Λ̃ would drift as 1/L. C-box-E has no boundary, so this term is absent there (reading).
- **Count once.** This confirms with numbers `rR17-7:256` ("for a gapped H fixed by finite patches to exponential accuracy; for a gapless H, Casimir-type corrections ~ℓ⁻⁴"), which was suggested there. It also matches the definition e₀ = lim min spec(H_V)/V (`rR18-6:68`; `vR17-7:58`).
- **(i) answered.** For the static perfect law family, e₀ is the same for every volume. There are no 1/V terms, and the boundary term exists only for open boxes.

---

## 3. Probe (b): energy above the new ground state after insertion

### 3.1 Product insertion (`r1910_insert_product.py`)

**Geometry.**
- 1D: ring N → N+1, one site inserted.
- 3D: plane insertion on an L_x × L_p × L_p torus. The transverse momentum is conserved, so the problem splits into L_p² rings. This is R12-2's "global plane insertion": it keeps exact Z³ but is non-local per event (`rR12-2:235`).

**Lemma BP (best product) [proved, elementary, quadratic laws].** Take the old sites in the old ground state with zero means, and a product state on the new site. Then ⟨H_new⟩ depends on the new site only through its own on-site block, because the cross terms ⟨φ_new⟩⟨φ_j⟩ vanish. So the best product state is the new site's local ground state:
- scalar: ω_loc² = m² + z, with z = 2 (1D) or 6 (3D);
- Dirac: fill the negative eigenvectors of β(m + 3r).

A fixed product state costs (ω_ref − ω_loc)²/(4ω_ref) more [checked to 1e-6 against `r1910_insert_product.out:11` and lines 2-4].

ΔE_bp > 0 whenever the new ground state is entangled across the new site [proved: otherwise the product would be a ground state].

**Results per inserted site [checked; stable in N and L_p].**

| Field (3D plane insertion) | ΔE, P-loc (best product) | ΔE, P-fix (law-independent state) | Per Hubble time, P-loc |
|---|---|---|---|
| Scalar, m = 0 | 0.0594 | 0.585 | **1.57e122 ρ_Λ** |
| Scalar, m = 1 | 0.0405 | 0.718 | 1.07e122 ρ_Λ |
| Wilson-Dirac, m = 0 | 0.976 | 6.98 | **2.58e123 ρ_Λ** |
| Wilson-Dirac, m = 1 | 0.677 | 8.68 | 1.79e123 ρ_Λ |
| Photon (transverse content as 2 massless scalars) | ~0.119 | — | ~3.2e122 ρ_Λ [suggested: Gauss-law bookkeeping not built] |

Sources: `r1910_insert_product.out:14,18,20-22,25-31`. 1D point insertion (m = 0.05): 0.560 (`:4`).

**(iii) answered [checked].** Local ground state versus fixed product state:
- The local ground state is the *optimum* among product insertions.
- A law-independent fixed state costs 10–18× more (scalar) or 7–13× more (Dirac).
- Neither choice changes the conclusion: both are ≥ 1e122 ρ_Λ per Hubble time.
- An in-plane-entangled insertion (P-plane: the new plane enters in its own 2D ground state) lowers the scalar figure only to 0.041, and it is less local.

### 3.2 Ramped ("adiabatic") insertion (`r1910_adiabatic.py`, 3D scalar plane insertion)

**The ramp.**
- K(g) = (1 − g)K_A + gK_B.
- K_A is the old lattice plus the decoupled new site in its local ground state. So the ramp starts from exactly the P-loc state.
- K_B is the final perfect lattice. The old bond fades as the new site's bonds turn on.
- g(t) is a C^∞ smoothstep over time T.
- The transverse integral is done with the square-lattice density of states (RECALLED formula, checked: normalisation 0.998, second moment 1.0000, fourth moment 2.2500; `r1910_adiabatic.out:1`).
- Propagation is exact for piecewise-constant K.
- **Checks:**
  - the sudden limit reproduces P-loc to the quadrature normalisation;
  - doubling N changes ε_∞ by 0.8% (T = 16) and 1.3% (T = 32);
  - halving dt changes it by 1e-4 relative (`r1910_adiabatic_checks.out`).

**Results per inserted site [checked, T = 1–64 for m = 0; T = 1–32 for m = 0.3 and 1].**
- **Net leftover excitation.** For m = 0: ε_∞ = 6.6e-4, 1.4e-4, 3.3e-5, 7.5e-6 at T = 8, 16, 32, 64, a fit of 0.058·T^{−2.15} (`r1910_adiabatic.out:10-13`; `r1910_numbers.out:12`). For gapped fields it falls faster: m = 1 gives 3.2e-11 at T = 32 (`:27`).
- **The static in-progress excess.** δ(g) = E₀(K(g)) − E₀(K_B) is **positive along the whole path**:
  - m = 0: +0.031, +0.034, +0.031, +0.020, 0 at g = 0, ¼, ½, ¾, 1 (`r1910_adiabatic.out:2`);
  - m = 1: about 0.7× those values (`:4`);
  - Wilson-Dirac: +0.56, +0.60, +0.53, +0.33, 0 (m = 0), with path mean δ̄ = +0.374 (`r1910_dirac_static.out:1-2`).
- **The standing integrals.** A_law and A_fix (§4) both grow linearly in T. For m = 0 the slope dA_law/dT = 0.0214 equals the path mean of δ (`r1910_numbers.out:12`).

**Probe (b)'s measure, energy density per e-fold.**
- Product insertion: 3ΔE per e-fold, as in the table above.
- Ramp: the net is 3ε_∞(T). It reaches ρ_Λ only at T ≳ 5e56 t_P for m = 0 [suggested: extrapolated power law].

---

## 4. Probe (c): the in-progress energy, a new Λ ∝ H term

**Standing density [proved, elementary].** Take statistically homogeneous creation at mean rate 3H per site (L-CR, `TESTS:4511`; `vR12-2:5`), events of duration T ≪ 1/H, and A = ∫ excess dt per event. The steady-state energy density above e₀ is then ρ_ins = (3H/a³)·A. Relative to the dark energy:

  ρ_ins/ρ_Λ = 8πA/(Ω_Λ H₀) = **3.1e62 · A** (A in units of ħ; `r1910_numbers.out:1`).

**Two accountings, both computed.**
- **A_fix: energy counted with the completed law H_B from the instant the site exists.** The excess ε(t) is ≥ 0 by the variational principle.
- **A_law: energy of the time-dependent law H(g(t)) above E₀(H_B).** This splits as A_law = ∫δ dt + ∫ε_inst dt, where ε_inst = ⟨H(g)⟩ − E₀(H(g)) ≥ 0, while δ has no sign constraint.

**Lemma S-ins [proved, elementary; class 𝒞_Γ].**
- **Setting.** A site is born in a product state with the rest. Reading: a site that did not exist carries no correlations. The axioms supply no creation map (`AX:37`; R12-2's prices S1–S3, `rR12-2:280-282`). It then evolves under H_B + K(t), with |⟨i[K(t), H_B]⟩| ≤ Γ, and the excess is counted with H_B.
- **Claim.** ε(t) ≥ ε(0) − Γt with ε(0) ≥ ΔE_bp, so A_fix ≥ ΔE_bp²/(2Γ).
- **Proof.** d⟨H_B⟩/dt = i⟨[H_B + K, H_B]⟩ = i⟨[K, H_B]⟩. ∎
- **Boundedness.** On the qubit lattice local terms are bounded (`AX:47`), so a Planck-scale K has Γ = O(1) in Planck units.
- **Consequence.** The standing density is ≥ 5.5e59/Γ ρ_Λ for the scalar, ≥ 2.6e59/Γ for scalar m = 1, and ≥ 1.5e62/Γ for Wilson-Dirac (`r1910_numbers.out:43-54`).
- **Necessary condition to evade.** Γ ≳ 5.5e59 E_P/t_P (scalar) or 1.5e62 (Dirac). That is insertion machinery acting at least ~1e60 times faster than one lattice light-crossing.
- **Checked on the ramp family.** Measured extraction power per site: Γ̂ = 0.014–0.077. In every run ε(t) ≥ ε(0) − Γ̂t holds, and A_fix exceeds ε(0)²/(2Γ̂) by 1.8–3.1× (m = 0 and 1, T = 1–8; `r1910_lemma_check.out:2-9`).

**The untuned ramp family [checked].**
- A_law ≥ ∫δ dt = 0.0214·T. The path mean of δ is static and positive (`r1910_tuning.out:2`, Δ = 0).
- For T < 1, the net excitation tends to P-loc (≥ 0.04).
- So for every T, standing + net ≥ 6.7e60 ρ_Λ (m = 0). On the computed grid the minimum is 2.0e118 ρ_Λ, at T = 64 (`r1910_numbers.out:10`).
- A_fix ≥ A_law in every computed row (`r1910_adiabatic.out`).

**Local Z³-preserving insertion = dislocation climb (R12-2) [checked, 2D proxy and exact 3D straight lines].**
- **Law on a defected graph.** The same bond rule everywhere; core sites have 3 bonds.
- **Core energy (2D dislocation dipole).** δ_core ≈ −0.118 (m = 1), −0.136 (m = 0.3), −0.139 (m = 0.1) per core. It is stable in L and in segment length (`r1910_dislocation.out:11,22,33`).
- **3D straight edge lines.** A straight edge line is exactly the 2D dipole graph × Z (separation in k_z). Its energy is δ_line = −0.099, −0.108, −0.110 per lattice step for m = 1, 0.3, 0 (`r1910_dislocation.out:36-38`).
- **Standing density.** R12-2's line density 3H/(a v_climb) (`rR12-2:234`; rerun identical) gives ρ_def = 3Hδ_line/v ≈ **−3.4e61/v ρ_Λ** (`r1910_numbers.out:56-61`).
- **Sign.** The sign is negative under the bond-rule law. It is law-dependent (reading: a law that fixes the on-site term instead of the bond count would shift it). The size is generic.
- **Reading.** This is the same structure as A, with A = δ_line·(a/v): the core is where insertion is "in progress".

**What the term is [suggested].**
- ρ_ins ∝ H(t) is a running-vacuum ("Λ ∝ H") component, not a constant.
- Treated as a separate fluid, w_ins = (1 + w_tot)/2 − 1: −1/3 in the radiation era, −1/2 in the matter era, −1 in de Sitter (`r1910_numbers.out:63-66`).
- Comparator, RECALLED: Λ ∝ H models (Schützhold 2002; Borges–Carneiro 2005). There the coefficient is ~m_π³; here it is A·M_P³ with A = O(1e-2–1).

**Where it enters the bridge [reading, from refereed equations].**
- **Under (S) + N_red (`S26:185`).** The source is T_m − (V − e₀)g, and V includes ρ_ins. So Λ̃(t) = κρ_ins(t) ≠ 0 even if P93 holds for the static law. The vacuum of a lattice that grows by local insertion is never the lowest state of the static law.
- **If "the lowest state" means that of the instantaneous law H(t)** (which contains the insertions in progress), then e₀[H(t)] − e₀[H_perfect] = 3H·Tδ̄ moves with H.
  - With conserved T, Bianchi forces ∂C = 0 (`vR17-7:44-50`).
  - In class 𝒟 the only carrier is λ̇ = −g_E θ_n (`vR17-11:11-14`), so g_E = κė₀/θ_n ≠ 0. That reopens the Lemma-S channel (`TESTS:4998`; refereed as a FAIL of the CMC model, `TESTS:5176`).
  - |g_E|/H² ~ 8πTδ̄/H ≫ 6 (the ghost threshold, `TESTS:4999`) [suggested, not computed in 𝒟].
- **"Is the lowest state defined?" (main question) [reading].** For the static law, yes (§2). For the growing lattice, the two natural definitions give either:
  - (D1) a fixed e₀ that the vacuum never reaches, by ρ_ins ∝ H; or
  - (D2) a drifting e₀[H(t)] ∝ H that breaks g_E = 0.

  Neither yields a time-independent intensive constant **that the vacuum actually sits at**.

---

## 5. Escapes tried, and what each costs

| Escape | Result | Label |
|---|---|---|
| **E1. Fast extraction** (Γ unbounded) | Needs Γ ≳ 5.5e59 (scalar) to 1.5e62 (Dirac) Planck units: super-Planckian, lattice-scale superluminal insertion machinery | proved (Lemma S-ins) + checked numbers |
| **E2. Tuned path** (law-energy accounting): choose the dark site's stiffness d_A so that the path mean of δ vanishes | **Exists**: d_A* = 5.5888 (m = 0), 5.6913 (m = 0.3), 6.6790 (m = 1) (`r1910_tuning.out:3,6,9`). That is one number per species and mass, to precision ~1e-62/T. dΔ*/dm² = +0.16, +0.13, +0.06 (`:4,7,10`), so loop shifts of m² move it. It is radiatively unstable (reading: analogous to Lemma PT's counterterm) | checked |
| **E2′. After E2, the sign-definite part** | ∫ε_inst dt = c/T with c = 0.0259–0.0260 (m = 0, T = 16–32) and c = 0.0035–0.0034 (m = 1, T = 16–32; still drifting down slowly). Halving dt changes c by ≤ 1% (checked at T ≤ 16) (`r1910_einst_check.out:2-9`). Below ρ_Λ needs T ≳ 3.1e62·c: **≈ 8e60 t_P ≈ 1/H₀ (m = 0)**, ≈ 1.1e60 t_P ≈ 0.12/H₀ (m = 1). Insertion events would last about a Hubble time: no longer local events. Reading: the limit is a continuous deformation of the whole lattice at the expansion rate, i.e. R11-3's V1 ("spacing grows", SOURCED) rather than site creation [suggested] | checked (c, T ≤ 32); suggested (extrapolation, reading) |
| **E3. Entangled birth** (an instantaneous quasi-local isometry of radius R) | A = 0, but the action is instantaneous over radius R. For gapless fields R grows as a power of 1/ε_target. This is acausal at scale R and beyond nearest-neighbour Admissibility (`AX:57`) | not computed; suggested |
| **E4. A new principle (S_ins)**, "an insertion in progress weighs nothing" / "volume is counted by energy" | Number-free in form, like (S). But it must also declare the sign-definite in-progress *excitation* weightless, which conflicts with N_red's "energy above the lowest state weighs" (`S26:185`). It is also not shift-covariant without a further convention | reading; unbuilt |
| **E5. Global plane insertion** | Not an escape: every 3D number above *is* plane insertion | checked |
| **E6. No site creation** (V1, or set A) | Leaves the C-box-E arena. V1 is SOURCED with two tadpoles (`vR11-3`; `TESTS:4417-4423`) | count once |

---

## 6. Prices (named; none adopted)

- **P-r1910a (insertion energy).** Site creation (P52) carries a standing energy density ρ_ins = 3H·A/a³ above e₀, with A ≥ ΔE_bp²/(2Γ) in 𝒞_Γ. Paying it needs one of:
  - super-Planckian insertion (Γ ≳ 1e60);
  - one per-species tuning of the in-progress mean to ~1e-62, plus insertions lasting about a Hubble time;
  - an unbuilt principle (S_ins).

  Axiom text touched: `AX:37,40` (P52); `AX:43-53` (birth state: the possibility domain is named, but no state for a new site; reading); `AX:186-187` (source).
- **P-r1910b (dislocation-core energy).** Local Z³-preserving insertion gives |ρ_def| ≈ 3.4e61/v ρ_Λ unless the core energy is tuned to zero per species. Axiom text touched: `AX:37` ("points of Z³"), `AX:40-41`.
- **Status change proposed for the referee.**
  - P93 ("our vacuum is the law's lowest state") cannot hold exactly on a lattice that grows by local insertion within 𝒞_Γ: the excess is ≥ (3H/a³)·ΔE_bp²/(2Γ).
  - So (S) + (d-i) + N_red in C-box-E inherits P-r1910a. The C-box-E package's "three clauses, zero numbers" (`S26:185`) holds only for a static or plane-perfect site set with no energy cost of creation.

---

## 7. Archived runners rechecked (before relying on them)

These were rerun in `recheck/`. After removing lines that match a timing filter, all are **identical** to their stored outputs (empty diffs; `recheck/recheck_summary.out`):
- R11-3 `r113_tadpoles`;
- R17-7 `r177_gridvac_sector_cov`, `r177_records`, `r177_enthalpy_orders`;
- R12-2 `r122_numbers`;
- R17-3 `r173_symmetry_radiative`;
- R17-11 `r1711_lemmaV_general`.

Independent cross-check: my S(m) torus e₀ reproduces R11-3's NN zero-point densities ρ = 1.300034 (m = 1) and 1.193801 (m = 0) (`r1910_e0_convergence.out:13,5`; `scripts/C5/R11-3/r113_tadpoles.out` NN rows).

---

## 8. Scope and what is not shown

- **Fields.**
  - Free fields only.
  - Photon insertion uses its transverse content only; the Gauss-law bookkeeping for new links is not built.
  - Ramps were computed for the scalar only (Dirac: static δ only).
- **Geometry.**
  - 3D insertion is plane insertion (exact Z³). Point insertion in 3D needs the defect geometry, covered only through straight edge lines.
  - The 3D dislocation result is exact for straight edge lines under the bond-rule law; the climb dynamics are not simulated.
- **Lemma S-ins** uses energy counted with the completed law (A_fix). Under the law-energy accounting it does not apply as stated: E2 shows the static part can be tuned away, and only the sign-definite ε_inst part remains.
- **Extrapolations.** All extrapolations to ρ_Λ-level precision are **suggested**. The checked statements are the computed T-ranges, the linear growth of A (exact, static δ̄ > 0), and Lemma S-ins.
- **Not covered:**
  - interacting matter;
  - E3 (entangled birth) quantitatively;
  - an inhomogeneous creation rate (bound regions, R13-3);
  - the redshift/encoder issue (`rR12-2:226-229`), counted once and not re-examined.
- **Strong words checked.**
  - "forced": used only for L-CR's mean rate.
  - "every": scoped to 𝒞_Γ or to the computed family.
  - "exact": used only for:
    - plane insertion keeping Z³;
    - straight dislocation lines by separation;
    - Lemma BP within quadratic laws;
    - propagation for piecewise-constant K;
    - the ramp starting from the P-loc state.

## 9. Files (scratch folder)

- **Scripts:**
  - `r1910_e0_convergence.py`;
  - `r1910_insert_product.py`;
  - `r1910_adiabatic.py`, `r1910_adiabatic_checks.py`, `r1910_einst_check.py`, `r1910_lemma_check.py`;
  - `r1910_dislocation.py`;
  - `r1910_dirac_static.py`;
  - `r1910_tuning.py`;
  - `r1910_numbers.py`.
- **Outputs:** the matching `.out` files.
- **Rechecks:** `recheck/` (copies of the archived runners, `.rerun`, `.diff`, `recheck_summary.out`).
