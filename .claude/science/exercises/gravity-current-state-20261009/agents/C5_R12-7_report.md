# C5 round 12, probe R12-7: route E2, classical metric records with frame friction on GWs (worker report)

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 19:47Z to about 20:10Z. No repository file was edited.

**Scratch:** `scratchpad/C5/R12-7/`.
- `scripts/r127_checks.py` and `scripts/r127_checks.out` (sections [1]–[11]) hold every number below. Runtime about 2 s, OMP_NUM_THREADS=2. SHA-256: script `6e74250d…95c3`, output `28c85282…a4d`.
- `dl_untrusted/lu1803.11397.pdf` (downloaded, data only; never executed), text extracted by `scripts/pdf2txt.py` (run with `python3 -I`) into `text/lu1803.txt`.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `vR11-5` = `P/agents/C5_R11-5_referee_verdict.md` (and so on); `ref12-4/` = `scratchpad/C5/ref_R12-4/`; `out:N` = line N of `scripts/r127_checks.out`.

**What I read.** In full: `AX`; `TESTS:2302-2320` (C5 method); the R12-7 item `TESTS:4527-4542`; `P/agents/C5_R12-4_report.md` and `scripts/C5/R12-4/r124_checks.{py,out}`; `C5_R11-5_report.md`, `vR11-5`; `vR6-4`; `vR10-3`; `ref12-4/REFEREE_VERDICT.md` and `ref12-4/C5_R12-4_referee_verdict.md` (appeared during the run). In part: R6-4/R8-3/R9-4/R10-3/R11-5/R12-4 registrations and results (`TESTS:3143-3180, 3405-3418, 3468-3481, 3555-3573, 3707-3738, 3905-3916, 3984-3998, 4218-4243, 4285-4296, 4436-4470`); `C5_R6-4_report.md:1-140`; `C5_R10-3_report.md:140-240`; `r115_checks.py:1-120`; `ref12-4/C5_R12-4_referee.md` (grep for E2; lines 73-106 read).

**Labels.** **proved** (derived here under stated hypotheses); **checked** (a number in `r127_checks.out`); **suggested** (argued, not proved); **reading** (interpretation); **comparator** (literature: web-checked this run, via an earlier referee, or RECALLED).

---

## Reading against the FIXED rule (`TESTS:4539-4542`)

**Worker reading: OPEN.** No stated bound is violated for every γ, so not EXCLUDED. VIABLE is not reached, for three reasons listed after the table.

| Stated test (`TESTS:4532-4537`) | Result | Label |
|---|---|---|
| (a) stationary non-demolition dilation with friction | Per frame mode: an explicit causal bank of saturated QND elements with a positive synthesis measure; H-T excess X ∈ [1, 2.47]; both near-cone integrals finite and ∝ L (§2). The friction lives in the classical retarded filter G_γ, so CP follows as in R11-5 §2.1. Not assembled: the spin-2 tensor channel, and the bank combined with R11-5's n ≥ 3 UV chain in one computation. | checked [6],[7]; proved (CP, given the elements) |
| (a) energy sink | Explicit: a classical zero-temperature Ohmic bath (Lamb string) with an outgoing-only boundary condition gives exact friction and no fluctuation noise (§3). A hydrodynamic (Hawking) sink is impossible for ρ ≤ ρ_crit. A noisy quantum sink breaks the energy budget. At second order the sink must gravitate (Bianchi). | checked [8],[9],[11]; proved (Bianchi step, conditional on the Isaacson premise) |
| (b) causality | E2-h (friction on every component of h̄ in harmonic gauge, equivalently on the linearized curvature) is local and hyperbolic. Its kernel lies in the forward cone, the static limit is exact, and no mode grows in any boosted frame up to v = 0.999. **E2-TT (TT-only friction, as R12-4 wrote it) is acausal at O(γ)**, because the TT projector is instantaneous and non-local. | proved + checked [1],[10] |
| (b) positivity | CP by causal record feedback; H-T ≥ 1 for the bank (X ≥ 1). | proved; checked [6] |
| (c) GW170817 c_T | (v−c)/c = ±γ²/8ω² = 1.5e-42 at 100 Hz, front speed c. c_T alone allows γ up to 4.4e13 H₀. | checked [2]; comparator (web-checked) |
| (c) binary pulsars (power at the source) | P(γ)/P(0) − 1 ≤ γ/Ω. At γ = H₀ that is 4.9e-15 (B1913+16) and 1.5e-15 (J0737), against 1.6e-3 and 1.3e-4. | checked [3] |
| (c) standard sirens | d_L^GW/d_L^EM = exp(γ t_lb/2). Lu et al.: γ ≤ 2.98 H₀ (method-dependent); GW170817 + EM: γ ≤ 62 H₀. At γ = H₀ the ratio is 1.20 (z = 0.5), 1.32 (z = 1), 1.60 (z ≫ 1), inside the GWTC-3 Ξ₀ = 1.2 ± 0.7. At 3H₀ it is 1.7–4.1, a tension. | checked [4]; comparator |
| (d) Newtonian static limit, R6-4 lab window | G_γ(0, k) = 1/k² exactly. Lab kernels change by ≤ 4e-85. R6-4's window carries over unchanged. | proved; checked [10] |
| (e) PPN α₁, α₂ | Linear order: the new frame terms are not of PPN form and are ≤ 7e-19 of Newton at 1 AU (E2-h), 2e-24 U (E2-TT). R11-5's F_u terms carry over. Noise-fed second order: suggested only. | checked [5]; suggested |
| (f) prices | §6. | reading |

**Region where every stated observational test (b)–(e) passes:** 0 < γ ≤ H₀ (conservative), and ℓ_s ∈ [4e-10, 5e-6] m (R6-4's conservative demonstrated subwindow, `vR6-4:7`, unchanged by friction). Extensions: up to 2.98 H₀ by Lu et al. at face value, and up to 62 H₀ by GW170817 alone.

**Why not VIABLE:**
1. **The energy budget closes the same way as R11-5's.** (a) asks where the damped energy goes. The answer forces the sink to gravitate. In an expanding background it then holds a steady state of (γ/3H)·ρ_GW. Keeping ρ_GW + ρ_sink < ρ_Λ needs near-cone record suppression ε < 4.9e-17, 8.1e-12, 5.2e-9 and 3.3e-6 at ℓ = 1e-8, 2e-7, 1e-6 and 5e-6 m (out:72-75). By Corollary U_L that inflates matter's near-cone noise by 1/ε. These rest on R11-5's assumed coefficients (A′, f_cone, O(1) tensor weights, the Isaacson premise), which kept R11-5 OPEN (`vR11-5:22`). E2 removes the start time. It does not remove the budget.
2. **The dilation is explicit per mode and per scalar channel, at the linear-response level.** The elements are idealized saturated single-mode QND meters (comparator) with two-tone modulation. The spin-2 channel and the UV-chain-plus-bank assembly are not built.
3. **The sink must be classical, at zero temperature, and outgoing-only.** If the sink carried zero-point FDT noise into h, each near-cone mode would hold about ħω/2 independent of γ. That gives ρ ≈ ħc/(16π²ℓ⁴), which is 6e2 to 4e13 times ρ_Λ across the window (out:91-94), if near-cone record content gravitates (suggested).

**Against the expectation.** None was registered. Two results were not anticipated by R12-4:
- TT-only friction is acausal. The causal completion damps all components.
- The energy sink reinstates R11-5's ε budget, so E2's only gain over E1 is stationarity.

---

## 0. In plain words

- **The friction is physically clean.** A wave equation with a drag term still sends nothing faster than light. The drag removes 0.45% of a GW's amplitude over 40 Mpc at the Hubble rate. The arrival-time shift is about 1e-27 s, and binary pulsars feel nothing measurable.
- **But the friction must act on the whole metric, not only on the wave part.** Damping only the "pure wave" (TT) part breaks causality slightly. Picking out the TT part requires knowing the source everywhere at once.
- **Where the energy goes matters.** The damped wave energy must go somewhere that itself gravitates, or Einstein's equations become inconsistent at the next order. A dark fluid with viscosity cannot do it: any fluid light enough would have a mean free path of about 2 Gpc. What works is a hidden, noiseless, frame-anchored absorber, like an endless string attached at every point of space that carries the energy away and never sends any back.
- **The bill is the same one R11-5 paid.** The record's own stochastic gravitational waves are now stationary instead of growing. But they, and the energy the absorber collects, still have to stay below the dark-energy density. That again forces the record to be very quiet near the light cone. By the R12-4 trade-off, matter is then very noisy there. The friction buys a law with no start time. It does not buy a cheaper energy budget.

---

## 1. Prior art (each counted once)

1. **R12-4** (`P/agents/C5_R12-4_report.md:154,163,181`): E2 proposed as the escape from Theorem U's U2, with G = g/(s + iγω) and saturated split P̄ ∝ √(s² + γ²ω²). **Referee** (`ref12-4/REFEREE_VERDICT.md:13`; `ref12-4/C5_R12-4_referee.md:73-100`): E2 is a causal stationary spectral ansatz, not a CQ model. The sink, its fluctuation noise, a Bianchi-compatible completion and a non-demolition realization are absent. Lu et al.'s β = γ/c, not γ/2c. This report addresses exactly those four gaps.
2. **R11-5** (`vR11-5:5-22`): Lemma C; the four-stage QND chain confirmed (quantum-limited, CP under causal feedback, self-commuting, zero reverse gain, ω⁻⁸); the full 𝒦_ε lacked a positive synthesis measure, a causal spectral factor and an exact bank-to-spectrum map. ρ_GW ≈ εLħc/(π³ℓ⁴) and the near-cone heating come from `C5_R11-5_report.md:189,228-233` (suggested there). The α₁ and α₂ sources are corrected in `vR11-5:12`.
3. **R6-4** (`vR6-4:7,25`): the least-decoherence floor and the conservative window 4e-10 to 5e-6 m.
4. **R10-3** (`vR10-3:5`, Lemma Q): ground-state meters write no record with gain. The bank here is driven, as in R11-5.
5. **Repository grep** (R12-4 §1.6, counted once): no repository construction of GW friction, a viscous GW sink or a CQ friction dilation. My own grep of `P/agents/` this run: "Lamb string", "Lamb model" and "Ohmic" have no hits. "Harmonic gauge" hits only `C3_G-B_report.md:108` ("the harmonic gauge holds only in mean"), a different question. `docs/` was not grepped.

## Hypotheses (class 𝓔₂, stated before any title)

- **E-H1.** Linearized CQ gravity on Minkowski space, with a fixed frame u (the CMB frame), translation- and time-stationary in u, at second order in the matter coupling.
- **E-H2 (E2-h).** The record-fed metric obeys (□ − γ u·∂) h̄_μν = −16πG J_μν in harmonic gauge, where J is the classical record and E[J] = F_u⟨T⟩. **E2-TT** is the variant with friction on h^TT only.
- **E-H3.** The meter is a stationary linear non-demolition dilation (self-commuting record, zero reverse gain), with causal classical post-filtering and feedback h = G_γ * J.
- **E-H4.** The sink is a classical Ohmic bath anchored in u, at zero temperature, with outgoing-only boundary conditions.
- **E-H5 (premise, as R11-5).** The Isaacson stress of the classical near-cone record content gravitates.

**Excluded realizations:** quantum sinks with FDT noise (§3, shown costly); dynamical frames; nonlinear gravity beyond the Bianchi step; jump or mediator CQ.

---

## 2. (a) The meter dilation with friction

**Construction (per frame mode k and channel).** The bank has elements i with linewidths Γ_i log-spaced from 2b (b ≈ γω/2c|k|) up to the band edge δ:
- Each element is a single-mode QND meter (Lorentzian gain, saturated: P_i·D_i = |F_i|²/4; comparator: textbook QND, Clerk et al. via `vR10-3:7`). Two-tone modulation centres it on ω = c|k|. Coupling strength is λ_i ∝ Γ_i^{1/2}, the positive synthesis weight from 1/√x = (1/π)∫t^{-1/2}/(x+t)dt (checked to 1e-6, out:49-52).
- Each record is passed through its own causal Lorentzian filter (weight c_i = λ_i). The records are summed and fed back through the retarded G_γ.
- Broadband and UV structure: R11-5's four-stage chain (`vR11-5:8`). It is not assembled with the bank here.

**Results (checked [6],[7]).**
- H-T excess X = P·D/(|F|²/4) ∈ [1.000, 2.467] across the band (out:53). The construction is near-saturated, and the bound is never violated.
- Inside the band, P_eff ∝ |u|^1.000 and D ∝ |u|^-1.000 (out:54). This is the saturated-split shape.
- At the cone both are finite (out:55). With G_γ, ∫M and ∫D are both finite and grow as L = 2 ln(1/b) (out:56-58): Corollary U_L's trade, met at 0.55–0.60 of L².
- The two-tone element is stationary: the correlation at two absolute times 1.55 rad of carrier phase apart agrees with the stationary prediction to 1σ (out:61-62). Proved algebraically, as in R11-5 §2.3.
- **CP (proved, given the elements).** Each element is a Gaussian instrument. Feedback uses only past records, since the per-element filters and G_γ are retarded ([1]). So the averaged map is Kraus-form, as in R11-5 §2.1 (`vR11-5:8`, confirmed for the chain).
- **Zero BMV entanglement (proved within the model).** The backaction commutes, and the feedback is LOCC (as R11-5).

**Price surfaced (proved by the construction's scale).** The bank needs element linewidths down to ~γ, so meter coherence times reach ~1/γ ~ t_H. A Hubble-scale meter memory replaces R11-5's T_* ≥ t_H.

**Not done:** the spin-2 polarization structure of the bank; one assembled kernel with both the bank and the UV chain; a quantum simulation of the elements (spectra taken as ideal).

## 3. (a) The energy sink

- **Hydrodynamic sink fails (checked [9]).** Hawking damping γ = 16πGη/c² needs η = 5.9e7 Pa·s at γ = H₀. Any kinetic fluid with ρ ≤ ρ_crit then has mean free path ≥ 2.2 Gpc, far above λ_GW (3e6 m) and ℓ. So it is collisionless, not viscous, at the relevant frequencies (out:69-70; suggested at O(1)).
- **Explicit noiseless sink (checked [8]).** A field mode attached to a semi-infinite string of impedance Z decays at exactly γ = Z/m:
  - 0.0500 vs 0.0500, and 0.1002 vs 0.1000;
  - the work delivered into the string equals the mode's energy loss to 2e-4 and 9e-4 (out:65-66).
  - With nothing incoming from the far end, the friction is deterministic and adds no noise.
  - One string per frame point is a frame-anchored hidden continuum.
- **Noisy quantum sink fails the budget (checked [11]; suggested normalization).** FDT noise 2γħω fed into h gives a γ-independent ≈ ħω/2 per near-cone mode (out:90). That is ρ ≈ ħc/(16π²ℓ⁴) = 6.1e2 ρ_Λ at 5e-6 m and 3.8e13 ρ_Λ at 1e-8 m (out:91-94), if near-cone record content gravitates (E-H5).
- **The sink must gravitate (proved, given E-H5).**
  - At second order, G⁽²⁾ = 8πG(T + t^GW + X), and the linearized Bianchi identity forces ∂^μ(T + t^GW + X) = 0.
  - Friction gives ∂^μ t^GW_μν ≠ 0, so X ≠ 0 and must source gravity.
  - The bath also absorbs GW momentum: the frame takes recoil (price).
- **Steady state in FRW (suggested).** A pressureless anchored bath gives ρ̇_s + 3Hρ_s = γρ_GW, so ρ_s = (γ/3H)ρ_GW (out:71). In exact Minkowski stationarity ρ_s grows without bound, so stationarity holds for the matter, meter and metric sectors, not for the sink's energy.

## 4. (b) Causality and positivity

- **Poles (checked [1]).** Every pole of 1/(k² − ω² − iγω) has Im ω ≤ 0 for all real k (max −1e-13, out:2), so the response is retarded.
- **Kernel (proved; checked).** G_γ(t, r) = e^{−γt/2}[δ(t−r)/4πr + θ(t−r)(γ/2)I₁(γτ/2)/(4πτ)], with τ = √(t²−r²). It follows from h = e^{−γt/2}u, where u obeys Klein–Gordon with m² = −γ²/4.
  - The numerical inverse transform matches it: zero outside the cone, 0.00282 and 0.00119 inside (out:6-8).
  - ∫G dt = 1/4πr reproduces to quadrature truncation (out:3-5).
- **Boosted frames (checked).** No growing mode for v up to 0.999 over 16000 random k′ (out:9). This is consistent with the theorem that a causal, rest-frame-stable dissipative law is stable in all frames (comparator, RECALLED: Gavassino 2021).
- **E2-h preserves the harmonic gauge (proved).** (□ − γu·∂) commutes with ∂^μ and ∂·J = 0, so ∂·h̄ = 0 is propagated. Curvature, a constant-coefficient derivative of h̄, obeys the same local damped equation. So the gauge-invariant content is local and causal.
  - The price is broken gauge invariance of the h-equation: non-TT curvature appears at relative O(γ/ω), which is 1.5e-20 at 100 Hz (suggested).
- **E2-TT is acausal (checked [10]; the argument is standard, suggested at theorem level).**
  - The TT projector applied to a compactly supported field is non-zero outside the support: 1.2e-2, 3.7e-3 and 8.3e-4 at r = 2, 3 and 5 (out:84-86).
  - In GR, the scalar and vector sectors cancel this non-locality in the Riemann tensor. With friction only on TT, Λ^TT[(G_γ − G_R) * T] is uncancelled. The curvature then changes outside the source's light cone at O(γ).

## 5. (c)–(e) Observational tests

- **c_T (checked [2]).** Δv/c = ∓γ²/8ω² = 1.5e-42 at 100 Hz (`ref12-4/REFEREE_VERDICT.md:13` agrees). The GW170817 lag is 6.3e-27 s. Bound: −3e-15 < Δv/c < +7e-16 (comparator, web-checked abstract of arXiv:1710.05834).
- **Binary pulsars (checked [3]).**
  - The radiated power with the damped G is P ∝ ∫k²dk A(k) Im G. For constant A it is exactly (π/2)Re√(Ω² + iγΩ), that is 1 + γ²/8Ω² (out:26-27). For compact sources it changes by ≤ γ/Ω (out:18-25).
  - Hulse–Taylor: 4.9e-15 vs 0.16% precision (comparator: 0.16% via a 2025 review snippet; Weisberg–Huang 2016 RECALLED).
  - Double pulsar: 1.5e-15 vs 1.3e-4 (95%) (comparator, web-checked abstract of arXiv:2112.06795).
- **Standard sirens (checked [4]).**
  - In cosmic time the friction gives h ∝ e^{−γ t_prop/2}/d_L, so d_L^GW/d_L^EM = exp(γ t_lb/2). This is Ξ-type friction with α_M = γ/H on the TT sector only (reading).
  - **Lu et al. (web-checked full text):** β = 16πGη, with amplitude ∝ e^{−βD/2} (`text/lu1803.txt:157,162`); joint 95% bound β < 6.75e-4 Mpc⁻¹ (`:361`); GW170817 alone β ≲ 1.408e-2 (`:393`). Here β = γ/c, so γ ≤ 2.98 H₀ and ≤ 62 H₀ (out:32-33).
  - **Correction (concurs with the R12-4 referee):** R12-4's γ/2c comparison (`C5_R12-4_report.md:163`) overstated the margin ×2. The real margin is ×3.0.
  - **Scope of Lu's joint bound:** it holds each true distance at its β = 0 best fit when raising χ² (`text/lu1803.txt:287-289`; "fixing the D_min,i"). With true distances free, BBH events alone do not bound β. Only GW170817 + EM distance does. So 2.98 H₀ is method-dependent (reading).
  - **Dark sirens:** at γ = H₀ the ratio is 1.20 (z = 0.5), 1.32 (z = 1) and 1.60 (z ≫ 1) (out:34). GWTC-3 gives Ξ₀ = 1.2 ± 0.7 at 68% with a flat prior (comparator, web search snippet of Mancarella et al. 2203.09238). The Ξ-to-exponential mapping is approximate (suggested). At 3H₀ the ratio is 1.7–4.1 (out:35), a tension.
- **Static limit and lab window.**
  - G_γ(0, k) = 1/k² exactly (proved).
  - Lab kernels: |G_γ|²/|G_R|² − 1 = −(γω/s)² ≤ 3.7e-85 at 1 kHz and ℓ = 5e-6 m (out:82-83). So R6-4's window (`vR6-4:7`) and R11-5's lab table carry over unchanged.
  - **Caveat:** if ε < 1 is imposed for the budget (§3), R11-5's near-cone heating applies (`C5_R11-5_report.md:228-233`; suggested there). With ε = 1 it does not bind.
- **PPN α₁, α₂ (checked [5]).**
  - **E2-h** puts friction on h̄₀₀ too. A source moving at w then gets an r-independent "frame dipole" Φ₁ = (GMγ/2c²)(w·x̂) (proved by Fourier inversion). Its force relative to Newton is γwr/2c² = 6.8e-19 at 1 AU and 4.5e-21 at a pulsar orbit (out:40-41). These are not 1/r PPN terms and are far below any α-sensitivity (α̂₁ ~ 4e-5, α̂₂ < 1.6e-9; comparator via `vR11-5:12`).
  - **E2-TT:** about 2e-24 U at 1 AU (out:44).
  - R11-5's F_u terms carry over (lag ≤ 5e-14 s; dipole ≤ 1.2e-19; `C5_R11-5_report.md:220`).
  - Noise-fed second order: a homogeneous fluid at rest in the frame (record waves plus sink). Suggested only, as `vR11-5:22` requires.
- **Untested prediction (E2-h; proved formula, unconstrained).** A moving body is dragged toward the frame at rate 2γ|U|/(3Mc²): Sun 1.9e-24 s⁻¹ and neutron star 2.2e-19 s⁻¹, i.e. Δv/v ≈ 0.1 over t_H (out:45-46). For binary pulsars the effect is common-mode and a/c ~ 3e-22 s⁻¹ (suggested). E2-TT suppresses it by (w/c)⁴.

## 6. (f) Prices against the axiom texts (named, not adopted)

- **P-r1, a preferred frame.** Frame-tied friction, bank and sink. The Lattice axiom supplies no frame for set A's continuum (`AX:37-41`).
- **P-r12a′ (refines R12-4's P-r12a), dissipative metric.** Friction on every component of the harmonic-gauge h̄ (E2-h): the h-equation is not gauge invariant, curvature is local and causal. Choosing E2-TT instead costs causality at O(γ). AX names no time metric or dynamics (`AX:114-123,185-186`).
- **P-r12b (new), a noiseless frame-anchored classical sink.** It must be at zero temperature, outgoing-only (an arrow at the sink's far boundary: `AX:185`, arrow open), gravitating, and it must absorb GW momentum (the frame recoils). Record permanence (`AX:79-80`) is untouched: records stay; the metric is a leaky functional of them.
- **P-r12c (new), Hubble-scale meter memory.** Bank linewidths down to ~γ. This replaces R11-5's T_* ≥ t_H. Record-production dynamics with an energy input stays open in `AX:185-186` (as P-r11b).
- **Carried over:** P-r2′ (n ≥ 3 temporal smearing, chain N ≥ 4); P-r3 (R6-4's P-i1–P-i5); P-r4 (vacuum photons); P-r9b′ (near-cone suppression ε(ℓ), now with ε < 4.9e-17 … 3.3e-6 from out:72-75 including the sink); P-r11b (driven meters); R6-4 (iii)'s Qubit, Admissibility and Record prices (`vR6-4:19`).
- **Removed relative to E1:** P-r11a (start time). Per `ref12-4/C5_R12-4_referee.md:106`, a start time is a temporal boundary, not a breach of "no site is privileged" (`AX:40`). So E2's gain is stationarity, not an axiom-text saving (reading).

## 7. Strong words checked

- **"Exact"** (static limit, harmonic-gauge preservation) holds at linear order.
- **"Acausal"** (E2-TT): the curvature has support outside the source's light cone at O(γ). The projector non-locality is checked; the full Riemann statement is the standard SVT argument (suggested at theorem level).
- **"Explicit"** (the dilation): per frame mode, scalar channel, linear response, with idealized elements. It is not a full tensor CQ model.
- **"Must gravitate":** conditional on E-H5 (the Isaacson premise).
- **"Noiseless sink":** classical, T = 0, outgoing-only. Quantum sinks are not shown impossible, only budget-breaking if their noise reaches h at FDT level.
- **"Pass"** for sirens at γ ≤ H₀ is against Lu's method-dependent joint bound and an approximate Ξ₀ mapping. The robust (EM-counterpart) bound is 62 H₀.
- **"OPEN"** is a worker reading. No no-go is claimed, so no referee is mandatory. A referee is recommended for §4's E2-TT acausality and §3's Bianchi step.

## 8. What would decide it

1. Build the spin-2 bank and the chain-plus-bank kernel as one positive measure with a causal factor, then recompute X and L.
2. Settle E-H5 (whether classical near-cone TT content and the sink gravitate). If not, E2 passes every stated test on the region above, and the reading would move to VIABLE. If yes, the R11-5 coefficient work (A′, f_cone) decides the ℓ window.
3. Fit standard-siren data with profiled true distances (bright plus dark sirens), not Lu's fixed-distance method. Γ ≤ H₀ versus 3H₀ is decidable with current catalogues.
4. Referee E2-TT's acausality and the second-order Bianchi argument.

**Sources.**
- Web-checked this run:
  - [arXiv:1803.11397](https://arxiv.org/abs/1803.11397) (abstract + full text, Eqs. 5–7, Table I, joint fit);
  - [arXiv:1710.05834](https://arxiv.org/abs/1710.05834) (c_T interval);
  - [arXiv:2112.06795](https://arxiv.org/abs/2112.06795) (double pulsar, 1.3e-4 at 95%);
  - search snippets: [arXiv:2203.09238](https://arxiv.org/pdf/2203.09238) (Ξ₀ = 1.2 ± 0.7), [arXiv:2512.16161](https://arxiv.org/pdf/2512.16161) (Hulse–Taylor 0.16%).
- Via earlier referees: α₁, α₂ (`vR11-5:12`); Clerk et al. QND (`vR10-3:7`); Planck dipole.
- RECALLED: Hawking 1966 viscous damping; Gavassino 2021 (causal + stable implies stable in all frames); Lamb 1900 string model; ρ_crit and ρ_Λ; Weisberg–Huang 2016.
