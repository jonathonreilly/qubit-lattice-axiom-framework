# Lane RG, probe G2: gapless networks, constructions and readout Q

Worker: Claude Opus 5.5, the same model family as the supervisor. Not refereed. Run 00:54Z–01:15Z on 2026-10-11. No repository files were edited.

Scratch: `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/laneRG/G2/`

| Script | What it does |
|---|---|
| `g2_lib.py` | On-shell sampler with the exact collision measure (details below). |
| `g2_filters.py` → `g2_filters.out` | Filter sup norms, LP minimax filters, Bernstein–Walsh exponents. |
| `g2_shells.py` → `g2_shells_{KG_d2_m1,KG_d2_m0.3,KG_d3_m1,TB_d2}_coul.out`, `g2_shells_KG_d2_m1_lind.out` | Shell and energy-integrated ratios. |
| `g2_cheb.py` → `g2_cheb.out` | The Chebyshev stopband filter. |
| `g2_fit.py` → `g2_fit.out` | Decay-law fits and readout Q. |
| `g2_nullspace.py` → `g2_nullspace.out` | Weighted collision-invariant null space. |

**Sampler.** For fixed (k1, k2), k2 and k3 are placed on closed axis lines with a uniform transverse offset. All roots on each line are kept, each weighted by 1/|∂_t ΔE|. This avoids the single-ray missed-branch pitfall. The umklapp label is the exact integer winding round((k1+k2−k3−k4)/2π), so there is no roundoff floor. All amplitudes are handled in the log domain, so there is no underflow. Null-space zero tests use an absolute floor of 1e-12, not only a relative one.

## Reading against the FIXED lines

G2 is a construction probe. Its job is the number Q, and on its own it decides no lane verdict.

Every construction examined gives an umklapp amplitude that is **strictly nonzero at every finite depth and falls exponentially with depth**. None gives exact umklapp-free scattering. So nothing here supports PASS. The results are consistent with G1's identity-theorem FAIL for the classes built here. Each FAIL needs the codex sol referee.

## 1. Setup and one structural fact

**Matter.**
- Nearest-neighbour lattice KG, ω² = m² + Σ 4 sin²(k_j/2), in d = 2 (m = 1 and 0.3) and d = 3 (m = 1).
- Tight binding −2Σ cos k_j in d = 2.
- The staggered band is KG at (2k, 2m); see §6.

**Mediators.**
- **(a) and (c):** a static gapless lattice exchange V = 1/Ω²(q), Ω² = Σ 4 sin²(q/2), in the t + u channels. Forward cut |q| > 0.3, because Coulomb-type forward scattering diverges.
- **(b):** a static lattice Lindhard kernel χ₀(q) of a TB Fermi sea (μ = −1, T = 0.02), computed by direct sum on a 48² grid.

**Network vertex.** Each matter leg couples through a depth-n chain of nearest-neighbour nodes, i.e. a filter F(k) = Π_j f(k_j) with f a cos-polynomial of degree n. The kernel's range is n.

**PROVED (factorization).** For product vertices, the tree 2↔2 amplitude through any mediator is

T_n = F(k1) F(k2) F(k3) F(k4) · T_0

in both the t and u channels. So all umklapp/normal discrimination comes from the leg factors. The mediator enters only as an O(1) weight.

## 2. Construction (a): binomial filter f_r(k) = ((1 + cos k)/2)^r, degree r

**PROVED.** sup over all on-shell umklapp configurations of Π_legs F_r = 16^(−r) exactly.
- Reduce to one wrapping component. The incoming pair has unwrapped sum s ∈ [π, 2π], and the outgoing pair has |sum| = 2π − s.
- Log-concavity of ln(1 + cos) gives the bound [cos(s/4) sin(s/4)]^(4r) = [sin(s/2)/2]^(4r) ≤ 2^(−4r).
- The bound is approached at the threshold configuration, with legs at (±π/2, y), as K reaches the zone face.
- This holds in any d ≥ 2 for KG and TB, and is independent of the mass.
- Checked: `g2_filters.out`, 16^(−r) reproduced to 6 digits for r = 1–32.

**Fit (CHECKED).** The vacuum-weighted rate defect ε_D (rms sawtooth winding per collision, |T|²-weighted, k1 and k2 uniform), r = 8–80, fitted to exponential × power (`g2_fit.out`):

| Case | Rate c per unit r | Fit residual |
|---|---|---|
| KG d=2, m=1 | 2.73 | 0.007 decades |
| KG d=2, m=0.3 | 2.82 | 0.005 decades |
| KG d=2, Lindhard | 2.74 | |
| TB d=2 | 2.77 | |
| KG d=3, m=1 | 3.16 | |

- A pure power law fails, with residual about 8.5 decades. **The law is exponential, with c ≈ 4 ln 2 = 2.773.**
- **Caveat.** At large r the Monte Carlo rms is dominated by the sample nearest the sup point. Two TB runs with different streams differ by about 6 decades at r = 80, and the d = 3 rate of 3.16 is pre-asymptotic. Only the sup value is exact.

**Energy dependence (CHECKED, KG d=2 m=1).**
- **Below E_U = 2√(m² + 2), umklapp is kinematically absent.** On every low shell, ε = 0 identically for any network.
- **Absolute per-shell rates** (−ln max Φ_U per unit r) rise with energy: 3.07 at E = 3.61, 7.0 at E = 4.73, 18.0 at E = 5.6. The minimum over all energies, 4 ln 2, sits at threshold.
- **The same-shell ratio is much weaker.** ε_same = rms_U / rms_N on the same shell falls at:
  - 0.37 per r just above threshold;
  - about 0.1 per r at mid band;
  - 2.6 per r near the band top.
- **TB at the nested shell (E ≈ 0.37):** ε_same is flat at about 10^(−1.1) to 10^(−1.9) for r = 1–80, with max Φ_U ≈ max Φ_N.
- **Plain reading:** the network does not separate umklapp from normal scattering at the same energy. It switches off all lattice-scale-momentum scattering, and umklapp needs lattice-scale momenta.

## 3. Construction (b): Fermi-sea (Lindhard) mediator. It does not help.

- **PROVED.** The static lattice χ₀(q) = Σ_k (f_k − f_{k+q})/(ε_{k+q} − ε_k) is a sum of nonnegative terms. It depends only on the transfer q mod 2π, which cannot tell umklapp from normal. The 2k_F (Kohn) non-analyticity is a codimension-1 cusp, not an open zero set.
- **CHECKED.** Unfiltered, |T_0| ranges over [0.31, 0.43] on umklapp and [0.27, 0.44] on normal configurations (low shell). The same-shell ratio is about 1.1 at all three shells, against 0.39–0.68 for the Coulomb mediator.
- With the filter, the decay rate is identical to the Coulomb case (2.735 against 2.732).
- **Not computed:** the dynamic χ(q, ν). That it gives no open zero set is argued only, from analyticity off the continuum edges.

## 4. Construction (c): best depth-n filters

**Fixed passband κ (PROVED, classical).** Stopband [π/2, π] is the minimal interval stopband that kills every umklapp. Passband [0, κ]. The optimal one-leg error of a degree-n filter is δ_n = exp(−n g₁(κ) + o(n)), where g₁ = g_E(x*) is the Green function of E = [−1, 0] ∪ [cos κ, 1] at its gap critical point (Bernstein–Walsh).

Computed g₁ (`g2_filters.out`):

| κ | 0.1 | π/8 | π/6 | π/4 | π/3 | 0.4π | 0.45π |
|---|---|---|---|---|---|---|---|
| g₁(κ) | 0.913 | 0.643 | 0.557 | 0.405 | 0.265 | 0.158 | 0.079 |

- Near π/2, g₁ ≈ (π/2 − κ)/2.
- As κ → 0, g₁ → arccosh 3 = 1.763, but only logarithmically slowly.
- **CHECKED:** LP minimax filters give 0.554, 0.427 and 0.289 for κ = π/6, π/4, π/3. The LP floor is about 1e-8.

**2↔2 umklapp sup with the minimax product filter (CHECKED).** −ln(ε_sup)/n approaches roughly g₁ itself, not 2g₁:
- 0.32 at κ = π/3 (n = 40), where ε_sup ≈ δ_n;
- 0.48 at κ = π/4.

Reason: the configuration k1 = κ, k2 = π, k3 = k4 = −(π − κ)/2 has only one stopband leg.

**Vanishing passband (Gaussian passband of width about 1/√n; this is enough for matter at k ≪ 1).**
- Binomial: c = 2.773 (proved).
- Chebyshev f = T_n(2cos k + 1)/T_n(3):
  - c = 4 arccosh 3 − max_x[φ(x) + 2φ((π − x)/2)] = **3.100**, with φ = arccosh(2cos + 1). The maximum is at x = π/3: three legs at π/3, one at π. This was obtained analytically.
  - **CHECKED:** local rate 3.08 at n = 32 (`g2_cheb.out`).
  - The naive guess 2 arccosh 3 = 3.53 is wrong.
- **Open:** the true optimum over all depth-n vertices, including non-product g(k, k') and rational vertices from gapped chains. The binomial and Chebyshev values are achieved rates, not limits.

## 5. Null-space consistency with G1 (CHECKED, `g2_nullspace.out`, KG d=2 m=1, binomial filter)

Rows are on-shell configurations weighted by √w |T_r|. The basis is 40 odd sin(n·k) with |n|_∞ ≤ 4, plus the two sawtooth columns. The log-domain sawtooth defect is:

| r | 1 | 4 | 8 | 12 | 16 |
|---|---|---|---|---|---|
| log₁₀ defect | −1.51 | −4.91 | −9.53 | −14.18 | −18.84 |
| −r·log₁₀ 16 | −1.20 | −4.82 | −9.63 | −14.45 | −19.27 |

- It tracks 16^(−r) times a weak power.
- The best sawtooth-plus-periodic combination equals the sawtooth alone for r ≥ 4, so periodic corrections cannot help.
- **Periodic-only smallest singular value** falls only as a power: 1.6e-6, 3.6e-8, 4.0e-10 at r = 4, 8, 16. That is about r^(−6.5), as L2-A implies.
- **Floor caveat.** σ_min with the sawtooth is 1.9e-11 at r = 8. From r = 10 on it falls below the absolute floor, so it is flagged "ZERO". That is the numerical floor. The exact log-domain defect is 10^(−11.8) at r = 10.
- **PROVED.** The defect is never exactly zero at finite r. Φ_r > 0 off the measure-zero set k_j = π, and T_0 ≠ 0 on an open part of the umklapp set. This agrees with G1.

## 6. Scope additions (ARGUED)

- **Compton (matter–mediator).** If the mediator legs carry the same filter, the matter–mediator 2↔2 amplitude has the same four-leg structure, so its sup is also 16^(−r).
- **All orders.** Every amplitude with external matter legs carries Π_ext F, and umklapp is fixed by external momenta. So the suppression persists beyond tree level, away from thresholds.
- **Staggered matter.**
  - The filter must act on 2k: cos^(2r) k_j, with period π. That makes it equal to 1 at every taste corner, so it is taste-blind.
  - **It costs twice the range.** The rate is 2 ln 2 per lattice step, so n* doubles.

## 7. Readout Q

ℓ_P = 1.6e-35 m. Here r is the vertex smoothing range per leg. The mediator itself is gapless, so its range is unlimited.

| Construction | Rate per step | n for 1e-10 | n for 1e-50 | n for 1e-100 | Range at 1e-100 |
|---|---|---|---|---|---|
| Binomial, sup (proved) | 2.773 | 8.3 | 41.5 | 83.0 | 1.3e-33 m |
| Binomial, vacuum rms fit (checked) | 2.7–3.2 | 7–9 | 36–43 | 72–85 | |
| Chebyshev, sup (checked) | 3.100 | 7.4 | 37 | 74 | 1.2e-33 m |
| Fixed passband κ = π/4 (sup, checked) | about 0.48 | about 48 | about 240 | about 480 (570 at g₁) | about 8e-33 m |
| Fixed passband κ = π/3 | 0.265 | 87 | 435 | 869 | 1.4e-32 m |
| Staggered matter | half of the above | | | ×2 (about 150–170 for binomial or Chebyshev) | |

**Thermal weighting.**
- At lattice-scale T = 1, 0.5 and 0.25, it lowers log₁₀ ε_D by only 0.3–3 decades and leaves the rate unchanged.
- At physical T ≪ 1, umklapp is already suppressed kinematically by about e^(−(E_U − 2m)/T), with no network at all.
- What counts for the constraint algebra is the operator-level (sup or vacuum) measure, which is what the table reports.

## 8. Against the supervisor's expectation

- **"ε_U(n) falls exponentially, at best e^(−cn)": confirmed.**
  - Exponential, not a power law.
  - c ≈ 2.8–3.1 per step for a vanishing passband.
  - c ≈ 0.27–0.56 for a fixed passband κ = π/3 down to π/6.
- **n* at the 1e-100 level:**
  - about 70–85 steps for scalar matter with a vanishing passband;
  - about 150–170 for staggered matter;
  - 400–900 for a fixed lattice-scale passband.
- So the price is roughly a hundred to a thousand grid steps.

**What differs from the expectation.** The "relative" umklapp suppression is only large *relative to the natural low-energy interaction*. At the same energy, the networks barely separate umklapp from normal scattering (ε_same is flat at the TB nested shell). The mechanism is "turn off lattice-momentum scattering", not "select out umklapp".

## Labels and strong words

| Label | Items |
|---|---|
| **Proved** (same family, unrefereed) | factorization; sup = 16^(−r); Lindhard positivity and q-only dependence; Bernstein–Walsh rates; strict nonvanishing at finite r |
| **Checked** | LP rates; Chebyshev 3.100; Monte Carlo shell and vacuum ratios; fits; null space; d = 3; m = 0.3; TB |
| **Argued** | Compton; all-orders statement; staggered range doubling; dynamic Lindhard |
| **Open** | the true optimum over all depth-n networks |
| **Reading** | Planck-length conversions; whether approximate conservation is acceptable (not decided here) |
| **Comparator** | Bernstein–Walsh and Chebyshev extremal theory (recalled, not re-read) |

**Strong words.**
- "Exact" is used only for 16^(−r) and the factorization.
- "Never zero" is proved only for the product constructions here.
- "Optimal" is used only for the one-leg fixed-passband problem.
