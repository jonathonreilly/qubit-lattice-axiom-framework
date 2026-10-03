## A12 report: can formation stay quiet in a light-like (z = 1) sea if it builds up over many ticks?

Scripts and outputs are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A12/`. Every run went through `run.sh` (nice 10, four BLAS thread caps at 1, hard 60 s alarm).

**Grades.** EXACT = proof or exact arithmetic. CHECKED = numeric check with a stated tolerance. ARGUED = reasoning without proof. COMPARATOR = literature, cited and not adopted.

**Status.** All models are supplied toys. All rules are named conditionals, never framework content. Ideas I1–I6 are not adopted, and every statement is "if … then …".

---

### 1. Question

Suppose records form on ticks (I1). The rule may act through a window of T ticks inside the strict cone, like a detector coupled for T ticks.

- Is there then a formation rule that is linear (no-signalling, A9 T1), local and covariant, and whose vacuum rate is exponentially small (or zero) in a sea carrying linearly dispersing (z = 1) excitations?
- Can it still record excitations with order-1 probability?
- How does its vacuum rate fall with the window T and the reach R?
- Is that small enough against ε ≲ 1e-61 per Planck tick, and what does it imply for the owner's open question, the vacuum ruling, and A4/A6?

### 2. Answer

**Conditional yes.**

- **Zero is impossible (EXACT).** The sea's marginal on any finite region is full rank, so every nonzero weight of finite reach or finite window has a positive vacuum rate. This is a lattice analog of Reeh–Schlieder.
- **Exponentially small is possible.** Suppose the formation chance may build up over T ticks through a time-ordered, energy-absorbing instrument: one site coupled to a one-slot memory, the comparator being Unruh–DeWitt/Glauber.
  - The instrument is linear, local and covariant, and keeps the strict cone.
  - Its vacuum rate per window falls as e^{−2κT}, with κ = arccosh(1/sin(α/2)), where α is the half-length of the sea's occupied arc of quasi-energy.
  - For the massless 1D Dirac step, 2κ = 1.763 per tick. This is also the fastest decay any T-tick window can have (EXACT; CHECKED to 0.06%).
- **Soft excitations.** For excitations at quasi-energy E ≪ 1, the best rate at order-1 efficiency is ≈ e^{−c·E·T} with c ≈ 1–2. This is the time–energy uncertainty relation (CHECKED). The matched excitation is recorded with probability 1 − ε (EXACT), or 0.99 with a designed memory schedule (CHECKED).
- **Power laws come from only two places (CHECKED):**
  - abrupt window edges: ε ∝ T⁻¹ for a rectangular window and T⁻⁵ for Hann;
  - asking to record arbitrarily soft excitations: A9's R⁻³ equals the spectral weight of states softer than 0.85/R.
- **Three conditions carry the result:**
  - The strict cone needs the per-site memory, which the axioms do not supply. The memoryless alternative (one reach-T weight at the window's end) is influenced from outside the past cone (EXACT; CHECKED).
  - Any fixed window is blind below E_min ≈ ln(1/ε)/(cT).
  - On Planck ticks, the window must span about 5–40 cycles of the softest excitation it records (ARGUED arithmetic).

So super-polynomially small is enough. A9's "cosmological-constant-like fine-tuning" becomes a requirement that grows only logarithmically, conditional on the memory.

---

### 3. Derivation

#### 3.0 Setup

**The change (supplied toys).**
- The 1D Dirac step of A5: U(k) = C(m)·diag(e^{−ik}, e^{ik}). It has a strict cone.
- A 3D two-band conveyor step, e^{−ik_xσ_x}e^{−ik_yσ_y}e^{−ik_zσ_z} (A5 T6.4, one ordering). It also has a strict cone.
- A9's staggered Hamiltonian sampled once per tick, U = e^{−iH}. This one has no strict cone (Lieb–Robinson tails) and is used for rate scaling only.

**Quasi-energy and the sea.** θ is defined by the eigenvalue e^{−iθ}. The sea fills θ ∈ (−π, 0). By particle–hole symmetry, hole detectors are mirror images of particle detectors.

**The window rule.** A switching w(t) over t = 0…T−1, a carrier Ω, and a seed v₀ at site x define a single-mode formation weight:
- F = n_ŵ (a projector), with ŵ ∝ Σ_t w(t)e^{−iΩt}U^{−t}v₀.
- This is a fermion bilinear, local in any local fermion encoding; A9 takes the same stance.
- The multi-mode version projects onto several quiet modes.
- With windows tiled, the per-tick rate is p = ε_w/T, where ε_w is the rate per window.

#### 3.1 Task 1: the one-tick obstruction

- **L1 (EXACT).** For F ≥ 0 supported on a finite region A, tr(Fρ) ≥ λ_min(ρ_A)·tr F.
  - The sea's marginals are full rank: every restricted correlation eigenvalue lies in (0,1) (A9 n4).
  - So every nonzero strictly local weight has a positive vacuum rate.
  - By L4 below, the same holds per window for any finite window.
- **L2 (EXACT).** Take a single-mode weight n_w with w supported in A.
  - Its vacuum rate is ⟨w|C|w⟩ ≥ ν_min(C_A).
  - Its response to one added particle ψ is |⟨w|ψ⟩|² ≤ 1 − ⟨w|C|w⟩.
  - So vacuum/response ≥ ν_min/(1−ν_min). On the star, ν_min = 0.0126, reproduced as 1.263e-2.
- **L3 (CHECKED): A9's R⁻³ is infrared, not a locality bound.**
  - A9's cut mode P₊e₀ has vacuum rate equal to the site's spectral weight below |E| = E_c, with E_c·R = 0.841, 0.869, 0.856, 0.853 at R = 6, 8, 12, 16.
  - That weight is (4/(3π²))E_c³ (8 Dirac cones), checked to 1%.
  - So R⁻³ is the 3D density of soft states (∝ E²). (ARGUED: it would be R^{−d} in d dimensions.)
- **L3′ (CHECKED): the best reach-R single-tick single-mode weight falls exponentially.** Its vacuum rate is λ_min of the sea projector restricted to a ball of radius R (L = 32):

| R | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| ε_opt(R) | 1.26e-2 | 3.73e-4 | 7.72e-6 | 6.29e-8 | 7.44e-10 | 7.33e-12 | 6.73e-14 |
| A9's cut P₊e₀ | 1.28e-2 | 1.28e-2 | 2.42e-3 | 1.37e-3 | 6.79e-4 | 3.71e-4 | 2.38e-4 |

  - The log-decrement settles near −4.6 per unit radius.
  - The optimal mode simply avoids soft states.

#### 3.2 Task 2: multi-tick, energy-absorbing weights

**Step 1, spectral formula (EXACT).**
- ε_w = ∫ρ₋|W(θ−Ω)|² / ∫(ρ₊+ρ₋)|W(θ−Ω)|².
- Here W(ν) = Σ_t w(t)e^{iνt} is a trigonometric polynomial of degree T−1, and ρ± is the seed's spectral measure on the quasi-energy circle.
- This follows from ⟨u_b(k)|ŵ⟩ = W(θ_b(k)−Ω)⟨u_b(k)|v₀⟩.
- For the massless 1D step with the R seed, ρ is flat, so ε_w is exactly the window's spectral leakage onto the half circle (−π, 0).
- An independent real-space correlation-matrix computation agrees to four digits (CHECKED).

**Step 2, finite smoothness gives power laws (EXACT asymptotics; CHECKED).**
- If the n-th derivative of the window jumps at its ends, then ε_w ∝ T^{−(2n+1)}.
- Measured slopes:

| Window | Predicted | 1D, m=0 | 1D, m=0.3 | 3D staggered | 3D conveyor |
|---|---|---|---|---|---|
| Rectangular (n=0) | −1 | −1.000 | −1.006 | −0.98 | −0.99 |
| Hann (n=2) | −5 | −4.996 | −5.04 | −4.95 | −4.94 |

**Step 3, smooth compact bump gives a stretched exponential (CHECKED; ARGUED for general Gevrey windows).**
- ε_w ≈ e^{−a√T}, with a = 1.84 (1D, m=0), 1.82 (m=0.3), 1.59 (staggered) and 2.0 (conveyor).
- It is faster than any power but not exponential.

**Step 4, optimal windows decay exponentially, and that is the ceiling (EXACT).** Let the occupied arc S have half-length α.
- *Achievability.* The Chebyshev polynomial of the arc, W ∝ T_{T−1}(cos(ν′/2)/sin(α/2)) with ν′ measured from the antipode of S's centre, is at most 1 on S. Its peak is cosh((T−1)κ), with κ = arccosh(1/sin(α/2)). So ε_w ≲ √T·e^{−2κT}.
- *Optimality.* For a seed density bounded below on S, no T-tap window does better than e^{−2κ(T−1)}/(C·T²). The proof uses the Bernstein–Walsh lemma (max of the arc's Green function = κ) and a Nikolskii-type L²–sup inequality on an arc. Grade: EXACT given these standard polynomial inequalities; constants not computed.
- *Consequence.* Gaussian-in-T decay is impossible for a strict window.
- *Massless 1D.* α = π/2 gives 2κ = 2·arccosh√2 = 1.7627 per tick.
  - Measured slope: −1.7617.
  - The true optimum is the discrete prolate (Slepian) sequence. Its rates at T = 8, 16, 24, 32 are 1.6e-5, 1.8e-11, 1.7e-17, 1.5e-23, below Chebyshev at every T.
- *Massive m = 0.3.* α = π/2 − m gives 2.2244; measured −2.2233.
- *3D.* Conveyor: −1.7606 measured vs −1.7627. Staggered main-lobe Chebyshev: −0.8920 vs −0.8944.
- *Staggered, using the empty arc.* The sampled staggered sea has bandwidth √3 < π, so an arc of the circle holds no states. Ignoring it gives about −2.94 per tick against roughly −2.96 predicted.
- **Mid-band example.** About 80 ticks of an optimal window give ε_w ≈ 1e-61, but only for excitations near the middle of the band, i.e. Planck-scale ones.

**Step 5, soft excitations follow time–energy uncertainty (CHECKED; achievability EXACT).**
- The target band is [E/2, 3E/2].
- The Pareto optimum at efficiency ≥ 1/2 collapses onto E·T for E = 0.1, 0.2, 0.4:

| E·T | ln ε* at E = 0.1 | E = 0.2 | E = 0.4 |
|---|---|---|---|
| 10 | −15.84 | −15.77 | −15.54 |
| 15 | −26.04 | −25.91 | −25.79 |

- The slope is c ≈ 1.96 per unit E·T at efficiency 0.5, about 1.9 at 0.9, and 2.2 at 0.1.
- No √E·T law appears. The Bernstein–Walsh √E growth near the arc edge needs the window's weight to sit far from E, which costs efficiency.
- *Closed form.* A Chebyshev window centred at E, with main lobe [0, 2E], gives e^{−2arccosh(sec(E/2))T} ≈ e^{−ET}. Its efficiency is 0.98–1.0 for E·T ≥ 20, in 1D and in both 3D models (CHECKED: −0.198/tick vs −0.200 at E = 0.2).
- **Rule of thumb:** T ≈ ln(1/ε)/(cE), with c ≈ 1–2.

**Step 6, quasi-energy is only defined modulo 2π (EXACT).**
- "Positive frequency" means the arc of the circle complementary to the sea.
- The Dirac step's occupied arc has two edges that both touch the upper band: 0 (soft) and π (the time doubler, A5 T4.2c). The passband must stay clear of both.
- If one tick's bandwidth exceeds π, the bands overlap after folding. No temporal window can then separate the overlapping states, because they share a quasi-energy; momentum filtering is needed.
- Bounded quasi-energy is what makes exponential decay possible. In the continuum, with unbounded spectrum, compact switching gives only sub-exponential suppression (COMPARATOR: Paley–Wiener).

#### 3.3 Task 3: locality, causality, and no-record updates

- **L4, cone support (EXACT; CHECKED).** A T-tick window's effect, pulled back to the window's start, is supported in B(x, T−1+r) (A5 T1.1). The window mode's support was ±63 at T = 64.
- **Linearity (EXACT).** The structure of A9 Theorem 1 and Theorem 2 holds with reach T:
  - P(form) = tr(Eρ₀), 0 ≤ E ≤ 1;
  - P(form, lock k) = tr(E_kρ₀) with Σ_k E_k = E, so lock odds come after the formation update;
  - the no-record branch is a completely positive map.
- **The two implementations differ in causal structure (EXACT; CHECKED).**
  - *Time-ordered (register).* The record is affected only by its past cone. A distant Kraus operator at (y, s) with d > T−s commutes with every later coupling, so Σ_b‖K_b(…)‖² = ‖…‖².
  - *Memoryless.* One reach-T weight applied at the window's end responds to events out to d ≤ 2T−1−s.
  - *Check.* A distant record forms at (y, s) and its outcome is averaged; T = 24, s = 16, so the past cone is d ≤ 8.
    - Register: ΔP is exactly 0 for all d ≥ 9.
    - End-time weight: ΔP = 4.5e-5, 1.07e-3, 2.8e-5 at d = 9, 10, 12.
    - Without the distant record, the two agree to O(g²).
- **The memory is not supplied (EXACT).**
  - Each site carries one qubit, and that qubit is the field.
  - Q2 lets the rule act only on the current snapshot.
  - So a strict-cone window needs either a named per-site memory slot (a new structure, i.e. an import), or formation influence travelling T sites per tick, which gives up the strict cone for formation.
  - Without memory, sequential star-local instruments add incoherently: vacuum/response ≥ ν_min(star) per tick, at leading order in the coupling (EXACT at that order). There is no filtering gain.
- **A concrete register (CHECKED).** A fermionic slot side-coupled to the field by number-conserving swaps keeps everything quasi-free.
  - At weak coupling, the ratio of vacuum response to excitation response equals the single-mode ε: 1.026e-5 = 1.026e-5.
  - At strong coupling with a naive schedule, the window is dressed to w_eff(t) = sinθ_t·Π_{s>t}cosθ_s. Chebyshev-level suppression degrades to roughly e^{−0.25T}: ratios 6.2e-6, 6.1e-8, 1.6e-9 at T = 16, 32, 48 (g = 0.4).
  - For the one-way massless step, any target with Σw_eff² = Q ≤ 1 is realized exactly by inverting backwards (EXACT).
  - Designed-schedule check at T = 16: P(form|vac) = Q·ε_target = 1.395e-11, and P(form|matched particle) = 0.9900 at Q = 0.99.
- **Intermediate no-record updates (EXACT for the construction).**
  - Nothing locks during the window.
  - At its end, the no-click Kraus operator applies a fixed linear contraction, which satisfies A9 T2c. The register then resets.
  - Deciding on every tick (sliding windows) would need T slots per site.

#### 3.4 Task 4: efficiency

- **Single mode (EXACT).** The matched excitation P₊ŵ is recorded with probability 1 − ε. The designed register reaches Q(1−ε) = 0.99 (CHECKED).
- **Multi-mode, massless 1D, T = 64 (CHECKED).** With a quietness threshold of 1e-10, there are 21 quiet modes and a vacuum chance of 8.4e-12 per window.

| Packet quasi-energy k₀ | Efficiency, T = 64 | Efficiency, T = 128 |
|---|---|---|
| 0.6 to 3π/4 | 1.0000 | 1.0000 |
| 0.3 | 0.71 | 1.0000 |
| 0.1 | 0.055 | 0.35 |

  - Soft packets need E·T of about 20–40.
- **3D single-site windows (ARGUED).** They capture only the part of an excitation that converges on x: about (wavelength/width)² per site, like a resonant absorber's cross-section (COMPARATOR). Recording along a path then relies on many sites.

#### 3.5 Task 5: is super-polynomially small enough?

The requirement is p = ε_w/T. Solve c·E·T = ln(1/(p_max·T)), with E = E_phys/E_Planck in radians per tick (ARGUED arithmetic).

| Requirement | p_max per tick | E·T needed (c = 2 … 1) | 1 eV | 1 GeV |
|---|---|---|---|---|
| No freezing over the universe's age (A4) | 1.2e-61 | 36–92 rad (6–15 cycles) | 0.4–0.9e30 ticks, 24–47 fs, reach 7–14 μm | 0.6–1.1e21 ticks, 9–18 fm |
| 1/r out to 1 AU (A6) | 9.7e-94 | 66–165 rad (10–26 cycles) | 14–29 μm | 16–33 fm |
| 1/r out to the Hubble length (A6) | 1.2e-123 | 100–234 rad (16–37 cycles) | 21–42 μm | 23–46 fm |

Each column gives the window's reach, which equals T sites by the strict cone. Radio at 1 μeV needs about 6–40 m.

- **Strict cone.** Consistent, since reach = T by construction, but only with the register.
- **"Where things happen."** Holds at the window's resolution: the window length along the direction of travel, and about a wavelength across (ARGUED).
- **Infrared blindness.** A rule with fixed T never records anything below E_min ≈ ln(1/ε)/(cT). A family of windows at about 200 doubling scales would keep the total vacuum rate within about 200 × target (ARGUED).

#### 3.6 Task 6: consequences (ARGUED)

**The owner's open question (does empty space form records on its own?).**
- If the vacuum is the half-filled sea and the rule is linear with a finite window, then empty sites do form records on their own, and the rate is never zero (EXACT).
- That rate is a law-level choice that falls exponentially with the window.
- Exactly zero would need a rank-deficient (frustration-free) vacuum (A9).
- Separately, distant light arrives coherent: VLBI fringes and the CMB show it was not localized en route over about 1e60 ticks. So free excitations far from matter must essentially never be recorded. That favours formation that needs existing recorded neighbours, i.e. formation "only when neighbourhood conditions call for it".

**The vacuum ruling.**
- The sea and a quiet rule are compatible at the exponential level, but only with memory or long reach. A9's single-tick result stands: strictly local single-tick weights are never quiet.
- "Tick = formation rate" cannot mean the vacuum's own formation rate. At ε ≲ 1e-61, empty space would tick about once per site per age of the universe. The tick would then be a law-level step (A5) or set by matter (A8).
- A9's speculative identity "vacuum rate = frustration energy (T₀₀ = ε_v)" fails for windowed rules: the rate is set by the window's leakage, not by the vacuum energy.

**A9's z ≥ 2 obstruction.** A windowed weight is built from the change itself (its energy-absorbing part over a window) without being frustration-free. So z = 1 survives. The price is a nonzero but exponentially small rate, plus the memory.

**A4 and A6.**
- Freezing e-fold time: 1/p = T·e^{cE_min·T} ticks.
- Screening length: √(κT)·e^{cE_min·T/2} sites.
- Both are exponential in the window.
- If formation is gated by recorded neighbours, then f₀ = 0 exactly in voids, so A6's 1/r and A4's absence of freezing in voids hold exactly. Enclosed holes in matter would freeze only after about T·e^{cET}/g² ticks.

---

### 4. Checks

All runs were niced, single-threaded, and under a 60 s alarm. Machine load stayed about 2.2–2.7.

| Script | What it checks | Key numbers and tolerance | Time, peak memory |
|---|---|---|---|
| `c1_windows_1d.py` | 1D Dirac step, m = 0 and 0.3, T = 8–1024; rect, Hann, bump, prolate, Chebyshev | Slopes in 3.2 Steps 2–4; Chebyshev within 0.06%; prolate floor ~1e-30 at T = 48 | 5.5 s, 237 MB |
| `c1b_realspace.py` | Real-space correlation matrix, ring N = 400 | 6.1492e-9 vs 6.149e-9 (4 digits); support ±63 | 1.3 s, 137 MB |
| `c2_soft_tradeoff.py`, `c2lib.py`, `c2b_eta_dependence.py`, `c2c_eta09.py` | Pareto optimum for soft excitations | Collapse on E·T within 0.3 in ln ε; c ≈ 1.9–2.2; floor ~1e-15 | ≤ 1.5 s, 63 MB |
| `c3a_windows_3d.py`, `c3a_small.py` | 3D staggered (infinite-volume measure) and 3D conveyor | Slopes in 3.2; smaller-grid rerun identical for staggered, within a few % for conveyor at T > L/2 | 1.1 s at **312 MB (over the cap)**; rerun 0.7 s, 183 MB |
| `c3b_ball_optimum.py` → `c3b_L24.out`, `c3b_L32.out` | Best reach-R mode vs A9's mode | Table in 3.1; L = 24 vs 32 within 20% at R = 5; eigenvalue floor ~1e-15 | 1.8 s, 216 MB |
| `c3c_ir_weight.py` | A9's R⁻³ vs soft-state weight | E_c·R = 0.85 ± 0.02; small-E law within 1% | 0.1 s |
| `c4_cone.py` | Causal check | Register ΔP exactly 0 outside the cone; end-time weight up to 1.07e-3 | 0.1 s |
| `c5_efficiency.py` | Multi-mode efficiency | Table in 3.4 | 0.3 s |
| `c6_budget.py` | Planck-tick budget | Table in 3.5 | 0.1 s |
| `c7_register.py`, `c7b_designed.py`, `c7c_designed_eff.py` | Register instrument | Numbers in 3.3 | ≤ 1.6 s |

The one budget breach was the first `c3a` run: 312 MB (297.5 MiB) for 1.1 s. I reran it at 183 MB with the same exponents.

Not done: mpmath high-precision checks. Below about 1e-15 (eigensolvers) or 1e-30 (direct leakage sums), only the closed-form Chebyshev values, computed in log space, are trusted.

### 5. Real-physics match

**Comparators (not adopted).**
- Glauber photodetection (⟨E⁻E⁺⟩ = 0 in the vacuum) and Unruh–DeWitt detectors: vacuum quietness comes from energy absorption over a switching window.
- Sudden switching gives large spurious rates (Svaiter–Svaiter 1992; Sriramkumar–Padmanabhan 1996; Louko–Satz 2006). This matches the T⁻¹ class here.
- Slepian prolate sequences, the Dolph (1946) window, the Bernstein–Walsh lemma, Paley–Wiener, Reeh–Schlieder.
- Cavity-QED "photon catching" (Cirac–Zoller–Kimble–Mabuchi 1997), which matches the designed register schedule.
- All cited from memory; verify before citing.

**What it implies.** Windows of about 5–40 cycles are modest: about 10–100 fs for optical light, comparable to atomic absorption coherence. The lattice and tick allow exponential suppression where the continuum allows only sub-exponential, but the difference sits at the 1e-61 level and is unobservable.

**Falsifiers.**
- Spontaneous localization, heating or decoherence beyond collapse-model bounds would bound the coupling and window.
- Coherence of light over cosmological paths (VLBI, diffraction-limited imaging, CMB anisotropy) falsifies any rule that records free excitations efficiently in empty space. It requires per-photon recording ≲ 1e-60 per tick.

### 6. Open edges and next steps

1. **Owner choice: where the memory lives.** Options are a per-site slot (an import), formation influence at T sites per tick, or memory built from record structures. A record cage would need irreversibility to work.
2. **Analytic soft-regime constant.** Derive c for the one-sided prolate problem.
3. **3D reach-R optimum in high precision.** Also compute the version with an energy threshold, as a function of E_min.
4. **Floquet heating.** In interacting steps, quasi-energy non-conservation may set an irreducible vacuum-rate floor.
5. **3D window efficiency.** Design a covariant multi-site register and compute its cross-section for passing packets.
6. **Gated windows in A4/A6 toys.** Test p₀ ≈ g²e^{−cET}/T in matter, together with f₀ = 0 in voids.

### 7. Plain-language summary

If the chance that a record forms at a spot depended only on that spot and its neighbours at a single beat, the half-filled emptiness now in the repo would keep forming records on its own, because one beat can never fully tell emptiness from a faint ripple. If instead the chance may build up over many beats from what passes through the spot, and respond only to things with a steady rhythm, then false records from emptiness fall off extremely fast: each extra beat divides them by a fixed factor, so they never reach zero but can be made as rare as wished. Keeping emptiness from forming even one record per spot over the whole age of the universe takes a build-up of roughly five to forty swings of the gentlest rhythm one wants recorded, and anything gentler than that is never recorded at all. Building up over many beats without letting far-off happenings leak in faster than one spot per beat needs a small memory at each spot, which the axioms do not provide; without it, the build-up must reach across many spots at once, and influence can then outrun the grid's speed limit. Separately, light from distant galaxies arrives without having formed records on the way, which suggests records should form mainly next to records that already exist, not out in open emptiness.