# OBS-1 report: X2 observational sheet

**Readings:**
- **R1:** FLAV-NEAR.
- **R2:** Z4-EXACT, under two conditions.
- **R3:** PDK-SAFE-AT-PLANCK.

**Provenance and hygiene.**
- **Author:** Claude Opus 5.5, window 21:11–21:45Z. Same model family as everyone else in the exercise; not refereed.
- **This file:** the harness blocked the worker from writing it, so the supervisor saved it from the worker's final message, condensed. Every number and file reference is the worker's.
- **Pre-registration:** `PREREG.md` was written before any run and not edited afterwards. `PREREG_FOLLOWUP_2026-10-14.md` records, with dates, what was added after the first runs.
- **Resources:** peak memory 237 MB. One process at a time.

## R1. Flavour–strain coefficient (X2-L8): FLAV-NEAR

### Model

- X2's walker carrier, with a Dirac mass built from one 16 and the conjugate of another.
- A vector-like U(1) stand-in for the gauge field: nearest-neighbour photon, Feynman gauge, Ward vertices plus a tadpole.
- The SF strain law, in closed form for both the walker and the photon.
- A bilinear mirror-gap proxy Δ·f_NN, with Δ ∈ {0, 0.5}.

### Controls

- Ward identity holds to ≤ 3e-16.
- The continuum mass log is reproduced to +6% at N = 64.
- The D4 symmetry is exact.
- N = 48 and N = 64 agree within 1.5%.
- The result does not depend on m0.

### Coefficients (per e², per unit diagonal strain)

| Quantity | Value | Source |
|---|---|---|
| On-site corner mass, traceless response | 0 exactly at Δ = 0; 1.52e-3 at Δ = 0.5 | `r1_loop.out` |
| Leak of a heavy corner-selective mass into a light corner, static | 0.082 | `r1_leak.out` |
| Same leak, traceless strain response | 7.21e-3 (7.9e-3 at Δ = 0) | `r1_leak.out` |
| Own-corner response | 9.99e-3 | `r1_own.out` |
| Off-diagonal (π,π,0) condensate | 4.9e-4 | `r1_offdiag.out` |
| Untuned static velocity anisotropy | 0 at Δ = 0; 6.2e-3 at Δ = 0.5 | `r1_vel.out` |

### Two lemmas (proved)

- **Staggered-reflection lemma.** The map x_a → −x_a, with sign (−1)^{x_a}, sends k_a to π − k_a. With on-site terms only, every light corner's one-loop mass and velocity are isotropic (checked to 1e-14). So the registered on-site quantity is blind to flavour. Flavour operators were therefore added after the first runs, as recorded in the follow-up file.
- **Circulant sectors.** A circulant (residual symmetry T) sector has exactly zero first-order strain response. Only the CKM-forced departure from T contributes.

### Clock mapping

Rates are m_p/m_e drift under the nHz gravitational-wave background, against the clock bound of 3.6e-17/yr. Only E_g strain is included, so these are lower bounds. Estimator: TW-2's, unchanged.

| Branch | Rate / clock bound | Rate if couplings are halved or doubled |
|---|---|---|
| A (generations aligned to corners), trace | 80–300 | 40–600 |
| A, selective | 94–360 | — |
| **B (up quarks and charged leptons circulant; CKM in the down sector; PMNS in the neutrinos), trace** | **0.12–0.45** | — |
| **B, selective** | **0.65–2.5** | — |
| B′ (PMNS in the charged leptons), trace | 2.2–8.3 | — |
| B′, selective | 25–93 | — |

- **Reading: FLAV-NEAR.** Branch B falls inside the pre-registered [0.1, 10] window. Branches A and B′-selective are more than 10× over the bound. This is not KILL, because not every branch is over.
- **Branch A's static tuning:** about 3% on the electron's bare mass (the τ leaks about 15 MeV into it) and about 4e-4 on the up quark's.

### Assumptions

- One loop.
- U(1) stand-in for the gauge group; couplings e² = 0.1 and C_F g² = 0.4 (a factor of 2–3 matters).
- Bilinear mirror proxy.
- SF strain transplanted to the walker. Under H-cov, the shifts are already tree-level and O(1); not computed.
- T₂g not computed.
- Flavour completions are choices.
- |strain| = |h_GW|.
- NANOGrav taken at 3.5–4σ.

### Lorentz-violation side (not R1's quantity)

- The untuned static velocity anisotropy is about 5e-4 for electrons and about 2e-3 for quarks. It is generation-blind, so set C's existing cubic counterterm per field removes it.
- **Flavour-pattern residual (suggested, not computed):** Higgs/Yukawa loops with corner-selective Yukawas give about y²·K_v: 6.5e-7 (τ), 3.6e-6 (b), 6e-3 (t). That is at least 10¹⁴ above the SME bounds unless per-flavour-pattern counterterms are added, which would be a new price. **This is the biggest open hazard for route 2.**
- **Conditional static-strain position-invariance row:** ×6e3 (branch B) to ×4e6 (branch A). It depends on the open static registration and is **not used for the reading**.

### PREREG self-correction

The formula "y²/16π²·K_v" double-counts the loop factor. The report uses y²·K_v instead; both values are printed in `sizes.out`.

## R2. Z₄^F on the light sector: Z4-EXACT (conditions c1, c2), in fact exact U(1)_{B−L}

### Argument (proved)

- Z₄^F = exp(iπX/2), where X = 5(B−L) − 4Y ≡ 1 mod 4 on the 16.
- Every term of X2 as written is U(1)_X-invariant:
  - the walker and filter do not act on the Spin(10) index;
  - the quartic is a Spin(10) singlet;
  - the Standard Model gauge links commute with U(1)_X;
  - the leakage channels are built from these.
- U(1)_X is anomaly-free on each 16, so no breaking term can be generated.
- Electroweak breaking preserves X + 4Y = 5(B−L). Checked: 0 exceptions in 1003 monomials.

### Breaking operators

These carry B−L ≡ 2 mod 4: ν^cν^c (dimension 3), LLHH (5), d^cd^cd^cLH† (7), (u^cd^cd^c)² (9). None is in X2, and none can be generated.

### Conditions

- **c1:** no Majorana ν^cν^c term and no 126-type vev is added. If one is added, the reading becomes Z4-BROKEN, with ν^cν^c as the named operator.
- **c2:** L_X2's symmetric vacuum holds (open; GPR).

### Prediction and status

- **Prediction:** Dirac neutrinos; 0νββ exactly zero; no neutron–antineutron oscillation; no ΔL = 2 or 4 processes; nucleon decays only with ΔB = ΔL.
- **Consistent with:** KamLAND-Zen (T½ > 3.8e26 yr) and GERDA + Majorana Demonstrator + LEGEND-200 (T½ > 1.9e26 yr).
- **Static price:** Dirac Yukawas of about 1e-13–1e-12.

## R3. Proton decay: PDK-SAFE-AT-PLANCK

### Leading operators

- The leading operators are dimension 6 and conserve B−L.
- Dimension 7 is forbidden by R2.
- p → e⁺π⁰ is unsuppressed.

### Rate

Γ = (m_p/32π)(1 − m_π²/m_p²)²|C·W₀·A_R|², with W₀ = 0.10–0.15 GeV² and A_R = 1–2.5. The Super-K bound τ > 2.4e34 yr then gives a unit-coefficient scale above 3.2–6.2e15 GeV.

| Channel | Floor on 1/a | Margin at a = ℓ_P |
|---|---|---|
| (i) link-pair conversion | 6e13 to 2.5e15 GeV | ≥ 5e14 |
| (ii) filter offset | 3e11 to 3e13 GeV | ≥ 3e22 |
| (iii) worst case | 3e15 to 2.0e16 GeV | ≥ 1.5e11 |

- **Floor across all branches:** 1/a ≳ 2e16 GeV, i.e. a ≲ 600 ℓ_P.
- **Skeptic correction:** Γ = m_p⁵/Λ⁴ omits phase space and the matrix element and overstates the rate by about 4800×. At Λ = 1e16 GeV the margin is ×57, not ×0.012.

## Reading for route 2

The corner package survives only in a narrow flavour corner:
- circulant up quarks and charged leptons, CKM in the down sector;
- Dirac neutrinos carrying the PMNS mixing;
- a chosen Koide-like charged-lepton matrix.

That corner predicts:
- m_p/m_e drift at 0.1–2.5 times today's clock bound;
- zero 0νββ.

Corner-aligned generations are excluded at ×80–360, unless P-R19-34a′ or the counting rule applies. The largest open hazard is the flavour-pattern Lorentz-violation anisotropy, which needs a lattice Yukawa loop.

## Files

`PREREG.md`, `PREREG_FOLLOWUP_2026-10-14.md`, and `scripts/`:
- `r1_loop`, `r1_leak`, `r1_offdiag`, `sizes` (`.py` and `.out`);
- `r1_own.out`, `r1_vel.out`;
- `.err` memory records.
