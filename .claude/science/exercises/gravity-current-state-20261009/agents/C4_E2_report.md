# C4 lane RE, probe E2: how fast speed splits die under RG, and what that buys from M_Pl to TeV

**Worker:** Claude Opus 5.5 (same family as the supervisor). Not refereed. Run 2026-10-11, 16:54Z to 17:20Z.
**Labels:** proved, checked, suggested, reading, comparator. "Comparator" means a literature value. Values marked "(memory)" are from memory and were not re-verified. Values marked "(fetched)" were read from an arXiv HTML summary made by a small model, not from the full text.
**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/E2/`. No repository file was edited.
**Conventions:** a⁻¹ = M_Pl = 1.22e19 GeV (the framework's convention). From M_Pl down to 1 TeV is 16.09 decades (L = ln(Λ/μ) = 37.0). The starting split is F2's: c_e − c_γ = −8.55e-3 at the cutoff.

## Plain summary

**Weakly coupled gauge theories.** In QED-, QCD- and SM-like gauge theories, speed differences between species do shrink toward the infrared, but only logarithmically. From M_Pl to 1 TeV the shrink factor is:
- 0.83 for QED with one fermion;
- 0.19 for QCD;
- 0.91 for the slowest Standard Model mode.

Photon decay needs about 3e-17. These flows miss it by about 16 orders.

**Strongly coupled theories.** Power-law decay is real:
- in 2+1D, with exponents from 0.03 to 1;
- in holographic 4D models, with exponents up to about 2 in one class (comparator).

The bounds need an exponent of at least 1.3 for photon decay, 1.4 for neutrinos, and 2.5 for ultra-high-energy protons if the sign is unfavourable. These requirements are steeper than they look, because the highest-energy bounds sit only 8 to 13 decades below the cutoff.

**Two things no matter-sector flow can fix.**
1. **An elementary photon can be pulled onto the matter light cone only by the factor α_IR/α_UV**, i.e. by how much its own coupling runs. With α(TeV) = 1/128 and α(M_Pl) ≲ 1, that is about 1e-2. This is exact at one loop in e and holds to all orders in the matter's self-coupling.
2. **The graviton is frozen and its mass term is relevant.**
   - Its speed is pulled toward matter only at rate G·μ², which totals ≤ 0.5.
   - Its mass term is a relevant (dimension-2) coefficient, so (m_g/E)² grows by 1.5e32 from M_Pl to 1 TeV.
   - The TT stiffness comes from the cutoff zone; an infrared flow can remove at most a (μ/Λ)⁴⁺ᶻ share of it.

**E2 verdict: FAIL (bounded)** for the classes examined, against the FIXED readings. It is the supervisor's expected FAIL for the graviton. The hoped-for "partial win for matter speeds" does not survive for the photon or for weakly coupled Standard Model fields.

## (a) Weakly coupled 3+1D gauge theories: the one-loop speed flow

### Derivation
**Method.** The matter field (speed 1) exchanges a mediator whose quadratic form is covariant in the metric G = diag(c⁻²,c⁻²,c⁻²,1).
- I extract the ln Λ parts of the time and space self-energy coefficients exactly in c on S³ (sympy), then linearize.
- Gauge-parameter terms give only an isotropic p̸ (proved: k̸S(p−k)k̸ → −p̸ at the log level), so the speeds are gauge independent.

**Results (proved, in the sense of an analytic one-loop derivation).** Each line is dv/dL = κ·(coupling)·(c_mediator − v):

| Channel | κ | In α/π units |
|---|---|---|
| fermion ← gauge boson | 1/(3π²) · C₂(R) g² | (4/3) C₂ α/π |
| charged scalar ← gauge boson | 1/(4π²) · C₂ g² | C₂ α/π |
| fermion ← scalar (Yukawa y, real scalar) | 1/(24π²) · y² | |
| gauge boson ← its matter | g²/(8π²) × β₀ share: 4/3 T (Dirac), 2/3 T (Weyl), 1/3 T (complex scalar) | |
| scalar ← fermion loop | 2γ_φ = 4N_D y²/(16π²) | |

- **Why the last two rows hold.** A loop of a single species is covariant in that species' own metric. Self-interaction loops of the gauge field, including non-abelian ones, therefore never change the gauge field's speed.
- **QED with N_f flavours:**
  - singlet (fermions against photon): d(c_γ − c_f)/d ln μ = ((2N_f + 4)/3)(α/π)(c_γ − c_f);
  - nonsinglet (fermion against fermion): (4/3)(α/π).

  For N_f = 1 this gives b = 2 in F2's notation; F2 had guessed b = 1.

### Checks (checked)
**Independent brute-force check** (`e2_numcheck.py`): explicit 4×4 gammas, the exact (p−k)², a shell integral over S³ and finite differences.
- κ_F ratios: 1.0038 at c = 0.99 and 0.9963 at c = 1.01 (symmetric mean 1.000).
- κ_S ratios: 1.0017 and 0.9983.
- Gauge independence: ξ = 0, 1, 3 give the same anisotropy, +3.3648e-4, while the isotropic part moves from −2.5e-4 to 3.8e-2.

**Limits where the theory is Lorentz-invariant:**
- Z₂ = 1 − (α/2π) ln Λ (Feynman gauge);
- the scalar's γ_φ = (3 − ξ)e²/16π²;
- γ_ψ = y²/32π².

**Exact-in-c sign check:** the flow is attractive for c from 0.3 to 3.

**Comparator (fetched), Roy–Juričić–Herbut, JHEP 04 (2016) 018.**
- Their one-loop Yukawa velocity flows linearize to dv_F/dl = −(g²/3)(v_F − v_B) and dv_B/dl = −N_F g²(v_B − v_F).
- With g² ≡ y²/8π² and N_F = 2N_D (two-component counting; this identification is inferred), they equal my κ_Y = 1/(24π²) and 4N_D y²/16π².
- Their 3+1D photon flow −(4/3)α_F N_F(c − v_F) has the same form as mine.

### Integrated with running couplings, M_Pl → 1 TeV (checked, `e2_flow.py`)

| Content | Suppression of the relative speed |
|---|---|
| QED, N_f = 1 (α = 1/128 at TeV; 1/120 at M_Pl) | singlet **0.83**, nonsinglet 0.88 |
| QED, N_f = 8 (SM-like Σ Q²) | singlet 0.43, nonsinglet 0.85 |
| QCD, n_f = 6 (α_s 0.0885 at TeV → 0.0190 at M_Pl) | gluon–quark **0.19** = (α_Pl/α_TeV)^1.08; quark–quark 0.46 |
| SM-like: B, W, G, Q, u, d, L, e, H; 3 flavour-universal generations; 1-loop running; no Yukawas | slowest mode **0.911** (pattern e, B against G, Q); next 0.85; fastest 0.15. A kick to e alone: c_e − c_B → 0.71 of initial. A kick to Q: c_Q − c_G → 0.24 |

- **Asymptotic freedom helps, but only as a power of α_s:** S = (α_UV/α_IR)^{2·rate/β₀}.
- **What sets the slowest mode:** the fields that feel only hypercharge.
- **Yukawas omitted:** adding the top Yukawa only speeds up the Q₃/u₃/H relaxation, so it leaves the slowest mode alone (suggested).

## (b) Strongly coupled, large-N and ε-expansion flows: power laws

The velocity difference falls as δ ∝ (μ/Λ)^z.

| Model | z | Factor over 16.1 decades | Status |
|---|---|---|---|
| GNY chiral Ising, 4−ε at one loop: z = (4N_D + 2/3)·ε/(2(2N_D + 3)) | N_D = 1: 0.467; N_D = 2: **0.619** (ε = 1) | 3e-8; 1e-10 | derived (a one-loop exponent at ε = 1 is an extrapolation) |
| GNY or GN, N → ∞, singlet (fermion against the bare scalar term) | 4 − d = **1** in 2+1D | 8e-17 | proved (the bare (∂φ)² is irrelevant at large N) |
| QED3 large N, singlet (fermions against the bare Maxwell term) | 4 − d = **1** | 8e-17 | proved (same reason) |
| QED3 large N, nonsinglet (one flavour against the rest) | **64/(5π²N) = 1.297/N**; N = 4: 0.32 | 6e-6 | derived; brute-force 3D check ratio 1.000 (`e2_numcheck3d.py`) |
| GN large N, nonsinglet | **16/(15π²N) = 0.108/N**; N = 4: 0.027 | 0.37 | derived and checked as above |
| Any theory in d = 4 with a weak or marginal coupling | 0 (logs only; z_eff ≈ 2α/π ≈ 0.005) | 0.8 | proved: in 4D, F² and (∂φ)² are marginal, so the large-N "slaving" exponent 4 − d is 0 |
| BPS 2013, Randall–Sundrum class: elementary field mixed with a CFT through O of dimension d/2 + ν, 0 ≤ ν < 1 | **2(1 − ν)**, up to 2; ν = 1 gives logs ("too slow for realistic particle physics") | ≥ 1e-32 | comparator (fetched) |
| BPS 2013, Lifshitz-flow class | 2α, with α < 0.35 in d = 4, so 2α < 0.7 | ≥ 7e-12 | comparator (fetched) |
| A general 4D CFT: z = Δ − 4 of the lightest non-conserved spin-2 operator that is a cubic singlet | model-dependent; z > 0 by unitarity | — | reading |

**What strong dynamics needs from the matter.** The power law requires the fields whose splits the bounds constrain to be strongly coupled, or to mix with the strong sector through a strongly relevant operator (ν < 0.36 for z ≥ 1.28), over essentially the whole range from M_Pl down to the bound's energy. The electron, photon, neutrinos and quarks are weakly coupled wherever their couplings have been measured. Their own flows are then the logarithmic ones in (a) (reading).

## (c) F2's lattice split propagated down

The start is δ₀ = c_e − c_γ = −8.55e-3 at a⁻¹ = M_Pl. Bounds are COMPARATOR (memory), as in F2.

| Bound | Decades available (M_Pl → E) | QED log flow gives | Miss | Power-law z needed |
|---|---|---|---|---|
| γ → e⁺e⁻, LHAASO 1.4 PeV: < 2.7e-19 (lattice sign) | 12.94 | 7.3e-3 | ×2.8e16 | **≥ 1.28** |
| IceCube PeV neutrinos: ≲ 1e-20 | 13.09 | 7.3e-3 | ×7e17 | **≥ 1.37** |
| UHECR proton vacuum Cherenkov at 1e20 eV: < 4.4e-23 (if c_p > c_γ) | 8.09 | 7.8e-3 | ×1.8e20 | **≥ 2.51** |
| γ → p p̄ at 1.4 PeV: < 9e-13 (lattice-like sign) | 12.94 | 7.3e-3 | ×8e9 | ≥ 0.77 |
| GW170817, c_g − c_γ: ~1e-15 | — | not reachable by matter flows; see (d) | — | — |

**Where the bounds sit (checked).** The bounds are measured at 1e6 to 1e11 GeV, not at 1 TeV. The "15–16 decades" in the brief is therefore really 8 to 13 decades.

**The photon cannot be pulled onto the matter cone (checked: an exact identity at one loop in e, all orders in the matter's own coupling; `e2_photon_bound.py`).**
- Write L_γ = ½(aE² − bB²). A matter sector that is Lorentz-invariant with speed c_m adds X(1/c_m, c_m), where X = 1/e²(L) − 1/e₀² is the same log that runs the charge.
- To first order, c_γ − c_m = (c_γ0 − c_m)·α_IR/α_UV. The numerical check of the exact (a, b) expression agrees to O(δ²).
- Matter is pulled back toward the photon with an extra exponent p_m, so S = (α_IR/α_UV)^{1+p_m}. For N elementary species, p_m = 2/N (Dirac) or 6/N (complex scalar).
- **Scan with α(TeV) = 1/128 and no Landau pole below M_Pl:** the best is S_min = **1.05e-2** (16 Dirac fermions, α(M_Pl) = 0.45). For scalars it is 1.2e-2 with α_UV ≤ 1, or 1.2e-3 with α_UV ≤ 4π.
- **The target is 3.1e-17.** Reaching it would need 1 + p_m ≥ 7.8 at α_UV = 1, or ≥ 5.1 at α_UV = 4π.
- **For a strongly coupled charged CFT, p_m ~ O(1)/C_T** (suggested). The reason: the Ward identity ties the photon-exchange pull on the CFT's T to C_J, which also drives the running.
- **An emergent photon in 3+1D** still has a marginal F², so the same bound applies from its emergence scale (reading).

## (d) The graviton: TT stiffness, mass and speed

**The mass term is relevant (proved; dimensional analysis).**
- With h_c = M_Pl h/2, the stiffness term is μ_TT h² = (4μ_TT/M_Pl²)·h_c², so m_g² ~ μ_TT/M_Pl² is a dimension-2 coefficient.
- At any matter fixed point, h's anomalous dimension comes only through G: γ_h ~ c_T μ²/M_Pl² ≈ 7e-33·c_T at 1 TeV. The operator stays dimension 2 + O(Gμ²).
- (m_g/E)² therefore grows by **1.5e32** from M_Pl to 1 TeV, and by ~1e86 down to the LIGO band.
- Making it irrelevant would need γ_h > 1, i.e. gravity strongly coupled all the way down. That is excluded by G·E² ≈ 1e-32 at a TeV (reading).

**The stiffness comes from the cutoff zone (checked; model profile).**
- μ_TT is a c-number contact term, built up by shells as ∫k³·(LV kernel) dk. It is not multiplicatively renormalized.
- With an LV kernel profile (k/Λ)^z, modes below μ carry a share (μ/Λ)^{4+z} of it. For μ = Λ/10 that is 1e-4 at z = 0 and 1e-6 at z = 2.
- So a flow toward Lorentz invariance in the infrared removes at most that share. The tuning stays at P0's refereed 5.7e-99.
- The free-field T0 values, K₀⁴/(120π²) per boson, already sit at the cutoff (PRICE_NOTE §2).

**The graviton's speed is frozen (suggested estimate).**
- Matter loops pull c_g toward the matter speed only through the induced Einstein–Hilbert term. That is a Sakharov-type rate ~ N_dof μ²/(96π² M_Pl²), which integrates to 0.05 for 100 degrees of freedom and 0.5 for 1000.
- So c_g − c_matter keeps ≥ 0.6–0.95 of its cutoff value, about 1e-2 natural. GW170817 needs 4e-13 of it.
- An infrared-attractive matter fixed point fixes a weighted average speed for matter, not c_g. The graviton "match" tuning of F2 and R2 therefore survives every flow.
- **Comparator (memory):** Weinberg–Witten forbids a massless composite graviton from a Lorentz-invariant sector with a covariant conserved T_μν. The graviton has to be supplied, and its speed and mass are set in the UV.

**The C3-type anomaly with scale (reading, with an elementary check, `e2_c3defect.out`).**
- C3's obstruction is that Hess(ω²/2) is not constant. For a nearest-neighbour band its defect is 1 − cos k_i = (ka)²/2 + …, a dimension-6 operator that falls as (E/Λ)² by itself.
- Its zone average is 1.0, which is order one. That piece feeds the vacuum and loop quantities: the TT stiffness and the dimension-4 splits.
- The low-energy, visible part of the anomaly is therefore:
  - (E/Λ)², which is harmless;
  - plus the loop-induced dimension-4 speed splits, which are marginal and flow as in (a) and (b);
  - plus a UV-fixed vacuum part that no flow touches.

## Verdict against the FIXED readings (lane RE)

**PASS: not met.** No examined mechanism drives every dimension ≤ 4 LV coefficient and the TT stiffness below bounds without tuning.

**FAIL clause: met for the examined classes.**
1. **TT stiffness or graviton mass:** relevant (dimension 2), and its coefficient is fixed at the cutoff zone. No matter flow can make it irrelevant. **FAIL** (proved scaling; checked UV share).
2. **c_g − c_γ:** frozen. It needs the "match" tuning. **FAIL** (suggested estimate).
3. **c_e − c_γ, and any split involving the elementary photon:** the photon-side factor is ≥ α_IR/α_UV ≈ 1e-2, against 3e-17 needed. **FAIL** (checked).
4. **SM matter–matter splits under SM dynamics:** logarithmic, ≥ 0.19 (QCD) and 0.91 (slowest mode), against 1e-17 to 1e-21 needed. The running is too slow. **FAIL** (checked).
5. **Strong-coupling power laws:** they exist (z ≈ 0.03 to 1 in 2+1D; up to ~2 in one holographic 4D class), but would need z ≥ 1.3–2.5 for the fields the bounds actually constrain, which are weakly coupled. **Suggested / reading:** not a mechanism for the SM as observed.

**E2: FAIL (bounded)** to:
- one-loop flows (exact in the matter coupling for the photon-side identity);
- the listed content (QED, QCD, SM gauge content without Yukawas, GNY/GN/QED3 at large N or in ε);
- the holographic classes as reported by BPS (comparator).

An other-vendor referee is required before this is recorded as FAIL.

**Against the supervisor's expectation:**
- "Graviton mass relevant, can't be cured": **confirmed**.
- "Partial win for matter speeds": **narrower than expected**. A power law over 15 decades would suffice only with z ≳ 1.3–2.5 for the very fields that are observed to be weakly coupled. It never helps the elementary photon (α_IR/α_UV) or the graviton.
- **Lane reading suggested:** FAIL rather than INCONCLUSIVE, unless E1 finds a construction in which the photon and every SM field are composites of a strong sector that stays strongly coupled down to ~1e6 GeV.

**Not computed:**
- two-loop terms;
- Yukawa-coupled SM running;
- non-compact versus compact lattice gauge fields at the cutoff (F2's open item);
- BPS's full text (only a summary was fetched);
- the actual exponent of a lattice-realizable 4D strongly coupled sector.

## Files (scratch)
- `e2_coeffs.py/.out`: symbolic one-loop κ's in d = 4 and d = 3, the Lorentz-invariant checks, and the exact-in-c sign check.
- `e2_numcheck.py/.out`: the 4D brute-force check (gamma matrices, gauge independence).
- `e2_numcheck3d.py/.out`: the 2+1D large-N brute-force check (QED3 and GN).
- `e2_flow.py/.out`: QED, QCD and SM-like running; the power-law table; F2's split against the bounds; the graviton numbers.
- `e2_photon_bound.py/.out`: the photon-cone identity check and the scan over charged content.
- `e2_c3defect.out`: the elementary Hessian-defect scaling.

**Sources (comparator, fetched):**
- [Roy–Juričić–Herbut, arXiv:1510.07650](https://ar5iv.labs.arxiv.org/html/1510.07650) ([JHEP](https://link.springer.com/article/10.1007/JHEP04(2016)018))
- [Bednik–Pujolàs–Sibiryakov, arXiv:1305.0011](https://ar5iv.labs.arxiv.org/html/1305.0011) ([abstract](https://arxiv.org/abs/1305.0011))
