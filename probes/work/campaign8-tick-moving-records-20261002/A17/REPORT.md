C5 is clean. With random relocation the integrated-count variance grows linearly (Var/T ≈ 3.1–3.5). With deterministic rotor relocation it stays flat at 31–33 from T = 300 to T = 3000, a different scaling. All checks are done and within budget (longest 38.5 s, peak 247 MB). Here is the report.

# A17 report: can the beat be local, influenced, universal and quiet?

**Scratch directory:** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A17/`
- Scripts: `z3_floor.py`, `torus_mc.py`, `dirac_pacing.py`, `predvar_check.py`, `phys_numbers.py`, `rotor_scaling.py`.
- Outputs: `out_*.txt`. Wrapper: `run.sh`.

**Grades.**
- **EXACT**: proved, or exact arithmetic.
- **CHECKED**: numeric check with a stated tolerance.
- **ARGUED**: reasoning without proof.
- **COMPARATOR**: literature or experiment, quoted from memory, unverified, not adopted.

**Status.** Everything is a supplied toy. I1–I6 and D6 are instincts and decisions, not positions. Every new rule is a named conditional.

## 1. Question

Is there a local pacing rule (nearest-neighbour or bounded-radius, Admissibility-like) for the change between records that is all three of the following?
- **(a) Universal.** Every clock, including the change's own phase, slows by the same N(x) near concentrations.
- **(b) Low-noise.** Heavy superpositions keep their coherence.
- **(c) Consistent.** It keeps the strict cone, no-signalling (A9's linear instruments), and "only records are readable".

If not, what is the best trade-off?

Sub-questions:
- the general dephasing law;
- averaging over a radius R or a time window W;
- deterministic pacing from the record configuration;
- whether the two branches share their pace;
- a corrected coherence time t_coh, and whether A13's 1 ns is an artifact.

## 2. Answer

**Conditional yes, but not with a nearest-neighbour rule acting on records, and not with each spot counting its own events.** Grades: the core formulas are EXACT, the toys are CHECKED, and the physical numbers and the general relay claim are ARGUED.

**What washes out interference.**
- It is not the redshift difference between the branches. That is a fixed, run-independent phase (COW-type) and costs no visibility (EXACT; CHECKED).
- It is the shot noise of whatever the beat counts.
- Both branches live in one shared record history. Their phase difference comes only from the beat fluctuating differently at the two places. A per-site or nearest-neighbour beat is effectively independent at two separated places, so A13's estimate stands. It is not an artifact; if anything it is optimistic by 11× or more.

**An exact floor on the noise.** Take any beat driven by a diffusing record gas, read over a region K. Its long-time noise obeys S_N(0) ≥ 2(1−u)/(uκ·Cap(K)) (EXACT for linear drives).
- The noise falls with the region's capacity, which grows like its radius. It does not fall with the number of events counted, which grows like its volume.
- Time windows do not lower it at all.

**What the experiments demand.** Matching interferometers (Rb-87 for 2 s; 25 kDa molecules for 10 ms; COMPARATOR) needs a smooth average over R ≈ 4e9–1.5e12 lattice sites at carrier density u = 1/2, and up to ~1.5e18 sites at A8's dilute u ≲ 1e-6. A nearest-neighbour record rule falls short by 3e9 to 1e18.

**A stronger falsifier than interference.** A per-site beat also scrambles every massive particle inside each branch: an electron about every 3 s at u = 1/2 (EXACT at second order in the toy; physical reading ARGUED).

**The condition.** (a), (b) and (c) hold together only if each place's beat is a smooth, retarded average of record activity over a region of enormous capacity, with a small grid-scale tail.
- With records alone under Q2's snapshot rule, no nearest-neighbour rule can form that average. Same-tick reading at radius R breaks the cone. Retarded reading needs history the snapshot does not hold. Relays made of records carry the same floor at the point of use.
- The way out not excluded here: the smooth beat is carried by the shared possibilities, as a field inside the change that records set. That refines D6 from "the change waits for events" to "the change advances by a smooth dose set by record activity".

## 3. Derivation

### 3.0 Setup and named conditionals

- **P1 (EXACT from Record + Q1).** There is one realized record history. Records are facts, so both branches of an unrecorded superposition share it.
- **P2 (A8's condition U).**
  - At site x on tick t, the change applies a dose d(x,t), normalized so the far-away mean is 1.
  - Every process at x uses the same dose: formation, relocation and every step of the change.
  - The mean dose is N̄(x) = 1 + Φ/c².
- **P3 (content-blind; new conditional).** The odds of the pacing events do not depend on the paced content's possibilities. Otherwise the pacing events register which path the content took (open edge E2).
- **P4 (carriers).** The carriers are A6/A8 wanderers: diffusive records at density u, hopping with odds κ per direction per tick (κ = 1/12 in A6), modelled as simple exclusion (SSEP) or independent walkers. A13's option-A records are persistent walks with the same long-time diffusive structure (ARGUED).
- **Identification (ARGUED; A5 T2.6, A13).** The toy mass phase is m = Mc²τ/ħ per tick, with the tick at the Planck time.

### 3.1 Dephasing law for general pacing statistics (Task 1)

**Phase per run (EXACT given P1–P3).** Branch i receives the integrated dose K_i = Σ_t d(x_i,t), taken along its path. Given the record history H, the inter-branch phase is θ_H = m(K₂ − K₁).

**Single run.** θ_H is a phase, so it causes no loss of overlap.

**Ensemble over runs (EXACT).** V = |E_H e^{iθ_H}| = |φ_ΔK(m)|, the characteristic function of ΔK at m.
- For Gaussian ΔK, or at second order: −ln V = (m²/2)·Var(ΔK).
- Var(ΔK) = Var K₁ + Var K₂ − 2 Cov(K₁, K₂).

**Long times (EXACT).** For stationary paces with integrable correlations, Var(ΔK) = 2T[S_N(0) − C_N(Δx)].
- S_N(0) = Σ_τ Cov(d(x,0), d(x,τ)) is the zero-frequency noise at one place.
- C_N(Δx) is the same quantity across the separation Δx.

**Physical units.**
- −ln V = (Mc²/ħ)² t [S_N(0) − C_N(Δx)].
- Separately, the mean gives the deterministic fringe shift (Mc²/ħ)·ΔN̄·t = MΔΦt/ħ (EXACT split into mean and fluctuation).

**Recovering A13 (EXACT).** Per-site Bernoulli events with d = e/p give S_N = (1−p)/p ticks and C_N = 0. That is A13's |1−p+pe^{iω}|^{2T} at second order.

### 3.2 Minimum noise for pacing driven by local random events (Task 1)

**Theorem 1 (split; EXACT).** Suppose firing at x on tick t is a Bernoulli trial with odds p_t set by the snapshot (the "drive"). By the law of total variance:

Var(K) = E[Σ_t p_t(1−p_t)] + Var(Σ_t p_t),

that is, a firing term plus a drive term.
- With memoryless odds the firing term has Fano factor 1 − p, so pacing is sub-Poissonian only by (1−p).
- A local accumulator (fire whenever the accumulated drive passes an integer) keeps |K − Σp_t| < 1, so the firing term stays bounded for all T (EXACT).
- The accumulator is a stored, changing number per site. That is not a record, because records never change.

**Theorem 2 (capacity floor on the drive term).**
- Setting: SSEP or independent walkers at equilibrium, density u, generator κΔ_lat.
- Drive: N(x,t) = Σ_y w(y−x)η_y(t), supported in K, with E N = 1, so Σw = 1/u.
- Result: S_N(0) = 2u(1−u)⟨w, G w⟩/κ ≥ 2(1−u)/(uκ·Cap(K)), where G = (−Δ_lat)⁻¹ and Cap(K) = 1ᵀG_KK⁻¹1.
- Proof:
  - SSEP self-duality gives Cov(η_y(0), η_z(τ)) = u(1−u)p_τ(y,z) (COMPARATOR: Liggett). For independent walkers, (1−u) → 1.
  - Integrating over τ gives the identity.
  - Cauchy–Schwarz in the G_KK inner product gives (1ᵀw)² ≤ Cap(K)·wᵀG_KK w.
  - Equality holds for the equilibrium charge on K's boundary.
- Grades: EXACT for linear drives. For nonlinear drives whose mean tracks density it is ARGUED, via the chaos decomposition.
- This is the same capacity as A6/A8's charge. Independent carrier visits reach K at rate uκ·Cap(K) per tick.

**Corollary 2a (EXACT).** Any time window or causal filter with unit total weight leaves S_N(0) unchanged, because its zero-frequency gain is 1. Averaging over a window W therefore buys nothing at long times (CHECKED, C2).

**Corollary 2b (EXACT arithmetic, C1).** For a uniform ball of radius R:
- 4πR_eff·e = 1.33, 1.25, 1.22, 1.21, 1.21, 1.205 for R = 1–6 (continuum 6/5); the floor tends to 1/(4πR).
- At R = 6 the suppression relative to one site is 0.063, against 1/|K| = 0.0011.
- Why: each wanderer that enters stays about R²/κ ticks and keeps being counted.

**Corollary 2c (EXACT arithmetic).**
- For the nearest-neighbour star, Cap = 11.62, so S_N(0) ≥ 2.07(1−u)/u ticks: at least 2.1 ticks at u = 1/2, and at least 2e6 at u = 1e-6.
- For a single site, 6.1(1−u)/u ticks.

**Events versus presence (EXACT for independent walkers in continuous time).**
- The hop count in K equals the total hop rate times the occupation time, minus independent holding-time noise.
- So an event clock's S(0) is the presence clock's minus a Poisson term of order 1/R³. Both obey the floor at leading order.
- A presence clock must count wanderers only; counting held records gives the wrong sign (A8 3.7).

**So, for Task 1.** The minimum variance is Var(K) ≳ T·2(1−u)/(uκ·Cap(K)). For nearest-neighbour drives that is O(1/u) per tick, so no large sub-Poissonian gain is available locally.

### 3.3 Averaging and locality (Task 2)

**Required radius (EXACT arithmetic given Theorem 2 and the identification; experiment values are COMPARATOR).** The target is S_max = 1/((Mc²/ħ)² t_obs), in ticks.

| Experiment | S_max (ticks) | R at u = 1/2 | R at u = 1e-6 |
|---|---|---|---|
| neutron, 50 μs | 0.18 | 13 | 1.3e7 |
| Rb-87, 2 s | 6.1e-10 | 3.7e9 (6e-26 m) | 3.7e15 (6e-20 m) |
| 25 kDa, 10 ms | 1.5e-12 | 1.5e12 (2.5e-23 m) | 1.5e18 (2.5e-17 m) |

A13's "~1e9" is the right order for atoms; molecules need about 1e12.

**Locality.**
- **L1 (EXACT).** A pace at x that depends on the records within radius r at the same tick fails the cone. A choice at distance r changes those records, and with them x's next step, within a tick or two. That is influence faster than one site per tick, which breaks the strict cone (A5 T1.1) for r > 2.
- **L2 (EXACT given A13 T4).** A retarded average needs event history the snapshot does not hold: records carry no formation time, and event counts are not stored. So under Q2 a radius-R pace has to be relayed by something in the snapshot.
- **L3 (EXACT within the class; class membership ARGUED).** A relay made of records is itself a carrier gas, and x can use only its star. Theorem 2 then gives at least 2.07(1−u′)/u′ ticks, however smooth the relay is at larger scales.
  - Records cannot be rewritten.
  - Formations are capped at about one per site over all time (A6 3.2).
  - Moving records are themselves the noise source.
- **L4 (ARGUED).** A relay carrying continuous values has to sit in the shared possibilities (Q1).
  - A unitary nearest-neighbour change can transport such a field. Its spreading is wave-like, not diffusive.
  - The beat would then be a field inside the change, set by records, not a gate that waits for events.
  - Not constructed here (E1).

**A6's density field (Task 2c; EXACT).** It is not a stored field. It is the coarse-grained configuration of the wanderers, whose local value is 0 or 1. That is the K = one-site drive, with S ≈ 6.1(1−u)/u ticks. It becomes smooth only over large-capacity regions, which L1–L3 exclude for nearest-neighbour record rules.

### 3.4 Deterministic pacing and the shared environment (Task 3)

**D1 (EXACT).** A deterministic function of the record configuration removes the firing term but not the drive term, so Theorem 2's floor stands.
- Because records are facts, each run's fringe offset is a readable function of the record history. In C3 it was predicted from the realized dose field to an rms of 1e-2 rad, against spreads of 0.25–0.63 rad.
- So this is dephasing, undoable in principle by reading the records. It is not which-path decoherence.

**D2 (EXACT).** The pace difference has zero-frequency spectrum 2[S − C(Δx)], with C(Δx) = [2(1−u)/(uκ)]·⟨ν_{x1}, Gν_{x2}⟩.
- **Δx ≪ R.** S − C ≈ (1−u)Δx²/(3uκ|K|). On the lattice at Δx = 1 this is exact: e_self − e_cross(1) = 1/(6|K|), 1.355e-3 both ways (C1).
- **Δx ≫ R.** C → [2(1−u)/(uκ)]·G(Δx), so C/S ~ R/Δx (C1: 0.005310 against G(15) = 0.005311).
  - Building this correlation needs a carrier to cross Δx, which takes Δx²/(6κ) ticks: 4e8 s at 1 nm.
  - On lab time scales, C ≈ 0.
- **Consequence.** Sharing the environment cancels the noise only when Δx ≲ R. CHECKED:
  - C2: at D = 1 the variance is 12% of the independent value; at D = 10 it is independent.
  - C3: at D = 100 < 401 the variance is 0.07, against 0.39 at D = 600.

**D3 (ARGUED).** Real arms are μm to m apart. Lab inverse-square tests need the potential unsmoothed above about 50 μm (COMPARATOR), so Δx ≫ R. Each arm then carries its own noise.

### 3.5 Corrected t_coh; is A13's estimate an artifact? (Task 4)

**Corrected formula.**
- **Noise part.** t_coh⁻¹ = (Mc²/ħ)²[S_N(0;R) − C_N(Δx)].
- **Redshift part.** It enters only as the deterministic shift MgΔh·t/ħ (EXACT). In C3 Part C, |O| ≥ 0.9994 and the phase is −1.789 rad against a predicted −1.800.

**Verdict on A13's 1 ns.**
1. **Not an artifact of separate histories.** With one shared history and per-site pacing, the correlation is only G(Δx)/G(0) ≈ 0.32/Δx, and only after Δx²/κ ticks (EXACT/CHECKED).
2. **Optimistic.** With the round tick at Planck time, A13's own rate p = s·u(1−u) ≤ 0.08 gives S_site ≥ 11.5 ticks. Then t_coh(100 amu) is 80 ps at u = 1/2, and 3e-16 s at u = 1e-6.
3. **Incomplete: within-branch scrambling.**
   - Toy result (EXACT at second order; CHECKED): E[1−F] = m²Σ_t E[⟨δd²⟩ − ⟨δd·s⟩²], where s is the local σ_x density.
   - For paces whose correlation length is below the packet size, this equals m²T·S_N: per-site pacing destroys each branch's own coherence at A13's rate. C3 Part A: 0.05975 measured against 0.05989 predicted.
   - The lost part spreads over all lattice momenta, which are grid-scale states.
   - Physical scale (ARGUED): at u = 1/2, an electron every ~2.7 s; a nucleon treated as elementary, about 1e6 per second. Matter would not persist.
4. **The gradient phase is not dephasing.** The redshift-gradient phase is real and measured (COW, atom gravimeters; COMPARATOR) and costs no visibility.

**Smoothed beats and matter stability (ARGUED).**
- Long-wavelength pace noise is slow. Its effect on particle dynamics is suppressed by (2κM/m_P)²: 5e-47 for the electron, 1.6e-40 for the nucleon.
- What matters is the kernel's grid-scale tail. A sharp ball keeps about 9/R⁴ of the per-site noise power at the grid scale. Lifetime-type bounds (COMPARATOR) then need R ≳ 1.6e9 sites (electron) to 1.4e12 (nucleon).
- Smooth kernels need much less.

**Diósi–Penrose comparison (COMPARATOR).**
- At r ≫ R, the long-time correlation is C_Φ(r) = A·ħG/r, with A = 2(1−u)/(4πuκ) (EXACT algebra, using c⁴t_P l_P = ħG).
- A = 1.91 at u = 1/2. This is the spatial form of the DP correlator.
- The time structure differs (4e8 s to build at 1 nm), so DP's white-noise bounds do not transfer directly.

### 3.6 Other scalings and trade-offs

- **Ballistic carriers.** S_N(0) = 9/(8πuvR²) (EXACT, continuum), so R ≈ 3e4–7e5 at u = 1/2. But ballistic carriers give a 1/r² shadow, not 1/r (A8 3.5): a quiet beat with the wrong field.
- **Deterministic (rotor-type) relocation.** COMPARATOR: Propp machine, Cooper–Spencer, Holroyd–Propp; not adopted.
  - CHECKED (C5): the variance stays at 31–33 from T = 300 to 3000, against linear growth for random relocation. No noise accumulates, which is a different scaling.
  - On infinite Z³ the start randomness still diffuses in, giving Var ∝ √T (ARGUED).
  - Costs: a mutable per-site pointer that is not a record, and relocation odds of 0 or 1.
  - The tick-scale jitter that drives scrambling is untouched, so spatial smoothing is still needed.
- **Skip pacing (ARGUED).** The change steps every tick except for skips with odds ε ≈ |Φ|/c².
  - The void then runs at full speed, which fixes A13's "the void has no change".
  - Firing noise is about ε per tick: about 1e-6 here (galactic potential, COMPARATOR), which is too noisy by 1e3–1e6.
  - An accumulator scales the drive term by ε², but per-site skips are still grid-rough.

**Best trade-off.**
- **Most promising, not excluded here:** carry a smooth beat field in the shared possibilities. It is NN-local and wave-like, which might also bear on A8/A13's "no waves". Not constructed.
- **Record-only fallback:** a retarded average over a bounded radius R ≳ 1e10–1e18. This gives up nearest-neighbour Admissibility, and Q2 unless it is relayed.
- **Round pacing:** quiet but not universal (A13).

### 3.7 Condition for the owner (Task 5)

Given P1–P4, a local, influenced, universal beat keeps heavy interference and matter intact only if each place's beat is a smooth, retarded average of record activity over capacity Cap ≳ 2(1−u)/(uκ·S_max), with a small grid-scale tail.
- The "only if" is EXACT for linear record-driven paces. The sufficiency is ARGUED.
- Under records alone and the snapshot rule, no nearest-neighbour rule provides this (L1–L3).

## 4. Checks

Every run used `nice -n 10` and thread caps of 1, and stayed under 60 s and 300 MB (maximum 38.5 s, 247 MB).

| Check | Script | What it shows | Result |
|---|---|---|---|
| C1 | `z3_floor.py` (0.4 s, 183 MB) | exact Z³ Green's function, ball noise against the floor, branch identity | G(0) vs Watson/6 to 1.0e-9; Laplacian residual ≤ 6e-9; table in 3.2; identity exact; far field to 2e-4 |
| C2 | `torus_mc.py` (6.2 s, 67–74 MB; 2 seeds) | walker Monte Carlo against the exact finite-T variance formula | MC/exact 0.905–1.094 (relative s.e. 0.063, all within 1.6σ); window ratio 0.90 against weight ratio 0.92 (1/W would be 0.01) |
| C3 | `dirac_pacing.py` (38.5 s, 247 MB) | Part A: within-branch scrambling | measured 0.05975 vs predicted 0.05989 (R = 0); 0.00841 vs 0.00842 (R = 3); 1.0e-4 vs 0.9e-4 (R = 200) |
| | | Part B: two branches, shared field, 600 runs | per-run phase to rms 1.0–1.2e-2 rad; Var 0.400 vs 0.386 (D = 600) and 0.061 vs 0.070 (D = 100, 2σ) |
| | | Part C: deterministic gradient | phase −0.573 vs −0.600 (m = 0.05) and −1.789 vs −1.800 (m = 0.15); fall −1.86 vs −2.00 and −2.01 vs −1.99 (deviations shrink as k/m falls) |
| C3b | `predvar_check.py` (9.3 s) | variance of the linear phase predictor, 20000 samples | 0.0693 ± 0.0007 vs 0.0698 exact; 0.388 vs 0.386 |
| C4 | `phys_numbers.py` | arithmetic | tables in 3.3 and 3.5 |
| C5 | `rotor_scaling.py` (0.7 s and 3.4 s) | random vs deterministic relocation | random: Var/T 3.1–3.5; rotor: Var 32.5 → 31.4 for T = 300 → 3000 |

C3b establishes that the D = 100 shortfall in Part B was a 2σ sampling fluctuation, not a formula error.

**Should be run (bigger, not run; variants of the scripts above):**
- `torus_mc.py` with exclusion (SSEP), to check the (1−u) factor.
- C3 on A13's 3D pair round, with smoothed versus per-site dose.
- `rotor_scaling.py` at L = 64, to see √T growth.

## 5. Real-physics match

**Matches (in kind).**
- A mean pace gradient gives the deterministic COW/redshift phase.
- It also gives a mass-independent fall toward slower clocks (toy, CHECKED).
- A shared smoothed beat makes all clocks slow alike (A8).

**Falsifiers.**
- Per-site or nearest-neighbour beats are falsified twice over:
  - interference times (Rb about 2 s; 25 kDa about 10 ms; COMPARATOR);
  - far more strongly, the stability of matter (electron scrambling).
- Smoothed beats predict mass-squared dephasing (Mc²/ħ)²·S_N. Any interferometer with M²t beyond 1/S_N for the (u, R) forced elsewhere would falsify them.
- Dilute carriers (u ≲ 1e-6, A8) make every requirement about 1e6× harder.
- The establishment and β problems of A6/A8 remain.

## 6. Open edges and next steps

- **E1.** Build a nearest-neighbour unitary on the aligned emptiness that carries a dose field sourced linearly by record events (A9). Compute its noise: quantum fluctuations plus filtered source shot noise. Then check waves, β and establishment.
- **E2.** Content-blindness: carriers that share pair steps with the content (A13 M8) register its path. This needs a bound, like A13's c.
- **E3.** The full S(q, ω) for smooth versus sharp kernels, against matter-stability and radiation (Donadi-type) bounds.
- **E4.** Composite rest energy: whether it acts as a spread density (self-averaging over the body) or as elementary excitations (no averaging) changes the mass scaling, A versus A².
- **E5.** Gating the motion itself (A14): O(1)-angle gates backscatter, so they would need smooth doses.
- **E6.** What a rotor pointer would cost in framework terms.

## 7. Plain-language summary

If each spot keeps its own beat by counting the record events right next to it, the beat jitters. The two halves of an atom spread over two places then pick up different jitter, so their interference fades within a billionth of a second. Worse, the jitter shakes every particle apart even when it is not spread out. The real slowing near a heavy body is not the problem: it is the same on every run, so it only shifts the pattern, exactly as experiments see. The jitter fades only if each spot takes its beat from a smooth average over a huge surrounding region, roughly a billion to a billion-billion spots across. Even then it fades only with the region's width, not its size, because the same wandering records keep coming back, and averaging over time does not help at all. A rule that looks only at neighbouring records cannot build that average without breaking the speed limit, so a quiet, local and influenced beat would have to be carried smoothly by the shared possibilities, set by the records, rather than each spot waiting for record events.