## Lane T (A5) report: a constant global tick and relativity

### 1. Question

Suppose records form, and the change steps, on one constant global tick. Which relativity features are kept, which are lost, and which emerge, beyond what the lattice already implies? The six tasks were:
- the strict light cone;
- emergent Lorentz behaviour of a Dirac-type step;
- global versus neighbourhood ticks;
- quasi-energy periodicity;
- visibility of the beat;
- the preferred frame, and whether grid dispersion starts at linear or quadratic order in E·τ.

### 2. Answer

**Conditional. The core statements are EXACT, the numerics CHECKED, and the scale and readability statements ARGUED.** The answer holds if records form and a nearest-neighbour change steps on one constant global tick, under two conditions:
- (a) the menus and odds at a tick are set only by records from earlier ticks;
- (b) formation odds, and the chance to form, are linear in the site's own possibilities.

Under those conditions:
- **Kept, and now exact:** a finite speed limit. Nothing spreads more than one site per tick for a single star-local step. Also kept is the analog of relativity of simultaneity: no record can reveal the order of events outside each other's cone, and every re-slicing of the step network gives identical records. [EXACT]
- **Emerging at low momentum** (1D Dirac-type step, toy). [EXACT, CHECKED]
  - cos ω = cos m cos k, and ω² = k² + m² − k²m²/3 − ….
  - v = p/E and γ hold exactly in deformed variables.
  - An internal clock dilates as R(v) = √(1 − v²/cos²m).
- **Lost:** [EXACT]
  - exact boosts;
  - real-valued energy: quasi-energy exists only modulo one turn per tick, is conserved only modulo 2πħ/τ, and has a time-doubled partner near quasi-energy π;
  - unbounded γ: γ ≤ 1/sin m, and each massive species has its own limiting speed cos m;
  - automatic universality of time dilation: a tick-locked internal rotation does not dilate.
- **Beyond the lattice:** the tick adds no new preferred frame, because rotation covariance pins it to the lattice's own [EXACT]. What it adds are discreteness observables:
  - the strict cone;
  - quasi-energy folding;
  - index-carrying conveyor steps, which no continuous change can produce;
  - exact coincidences of linked formations: a fraction p/(2−p) of linked pairs, which fades as p → 0 [EXACT; invisibility thresholds ARGUED].
- **Order of grid dispersion:**
  - In 1D, the Dirac step's group velocity departs from the low-momentum law only at quadratic order in Eτ, suppressed by mass, and not at all for massless content. [EXACT]
  - In 3D, proper cubic rotations exclude a linear-order term for rotation-invariant two-band content and for the band-summed dispersion. [EXACT]
  - They do not exclude it for branches that 90° rotations exchange. A strictly covariant six-ordering conveyor step splits its cone at linear order. [EXACT, CHECKED]
  - A linear split like that, if it reached photon-like content, is excluded by GRB timing and polarization bounds unless the tick is far below the Planck time. [COMPARATOR]

### 3. Derivation

**Conventions.**
- τ is the tick and a the site spacing. ω is in radians per tick and k in radians per site, so the grid speed a/τ = 1.
- A "star-local step" is one tick reaching only a site and its six neighbours. N₁ is the set of sites one tick can reach.
- Every model below is a supplied toy, not framework content.

**Summary against the lattice alone (lattice with continuous change):**

| Feature | Lattice, continuous change | Lattice plus constant global tick | Grade |
|---|---|---|---|
| Speed limit | Approximate; Lieb–Robinson tails | Exact cone t·conv(N₁) | EXACT |
| Order of out-of-cone events unreadable | Only approximately | Exactly | EXACT |
| Low-momentum Lorentz kinematics | Emergent | Emergent, with exact 1D identities; 1D massless content has no dispersion at all | EXACT/CHECKED |
| Preferred frame | Lattice rest frame | The same frame; nothing new | EXACT |
| Energy | Real-valued and conserved | Defined and conserved only mod 2π per tick; time doubler | EXACT |
| Index-carrying (conveyor) change | Impossible | Possible | EXACT (comparator theorem) |
| Exact coincidence of linked formations | Probability 0 | p/(2−p) | EXACT |
| Universal time dilation | Only if internal energy enters as mass | The same condition; tick-locked rotations would act as absolute clocks | EXACT |

#### T1. Strict light cone

**T1.1 [EXACT] One step per tick gives an exact cone.**
- If one tick has reach N₁, an operator on region X evolves within X + t·N₁. Every commutator with anything outside is identically zero. The proof is induction, one tick at a time.
- For a single star-local step this is the L1 ball: at most one site per tick.
- With L nearest-neighbour layers per tick, the reach is up to L sites per tick.
- The 1D Dirac step's support after t ticks is {|x − x₀| ≤ t, x ≡ x₀ + t (mod 2)}.

**T1.2 [EXACT] Record formation keeps the cone if (a) and (b) hold.** The process is then a network of local instruments, and the record statistics in region B at tick t ignore anything done in region A at tick 0 when dist(A,B) > t. The "at once" update of shared possibilities (Q1) carries correlation, not influence.

Counterexample to (b):
- Take a Bell-shared pair.
- If the distant record locks from menu {0,1}, the near site is left with pure {0,1} states. If it locks from {+,−}, the near site is left with pure {+,−} states.
- A formation chance f = ⟨0|ρ|0⟩² then averages 1/2 in the first case and 1/4 in the second.
- So the near site's formation statistics follow the distant menu at once, which is influence outside any cone.

If (a) fails, same-tick triggering chains cross arbitrarily far within one tick.

**T1.3 [EXACT] Continuous change with a time-independent local generator has no strict cone.**
- Take H(k) = sin k, whose speed is at most 1. Then ⟨d|e^{−iHt}|0⟩ = J_d(t), which is nonzero for every d at almost every t.
- The bound is |J_d(t)| ≤ (t/2)^d/d!: tails that are super-exponentially small but not zero.

**T1.4 [EXACT] The massive Dirac step is e^{−iH_eff} with H_eff = i·log U.**
- Its kernel decays as |h(r)| ~ r^{−1/2}·e^{−κr}, with κ = arccosh(1/cos m) ≈ m. The generator's range is about one Compton length.
- Running this generator for non-integer times gives tails; only whole ticks give the strict cone.
- For m = 0 (pure counter-moving conveyors) the kernel decays as 1/r. Each conveyor's band winds, so no continuous quasi-local time-independent generator exists. This is exact for the free single-particle case.
- More generally, a step with a net conveyor (nonzero GNVW index) cannot arise from any continuous local change, because the index stays constant along continuous paths. This is EXACT given the comparator theorems (Gross–Nesme–Vogts–Werner 2012; Ranard–Walter–Witteveen 2022). It turns Campaign 7's ARGUED flag into an exact statement, modulo those theorems.

**T1.5 [EXACT] The cone is a polytope, and emergent light can be slower than it.**
- Group velocities of all bands lie in conv(N₁). Proof: a packet's centroid stays inside the reachable set.
- An isotropic emergent light speed therefore obeys c ≤ 1/√3 site/tick for a single star-local layer (octahedral cone), and c ≤ 1 for three axis layers per tick (cubic cone).
- The strict cone and the emergent light cone are different objects that touch only along some directions.
- [CHECKED] In the fixed-order three-layer conveyor step, low-energy light moves at 1, but grid-scale modes reach √(3/2) along body diagonals. [ARGUED] This is generic: "low-energy light is the fastest signal" is not guaranteed.

#### T2. Dirac-type step (1D toy)

The step: R content moves one site right and L content one site left each tick, then mixes by angle m. In momentum space, U(k) = C(m)·diag(e^{−ik}, e^{ik}).

A single-track version gives the same spectrum [EXACT, CHECKED]: on a qubit chain in the single-excitation sector, apply full swaps on even bonds and partial swaps of angle π/2 − m on odd bonds.

**T2.1 [EXACT] Dispersion.** det U = 1 and Tr U = 2 cos m cos k, so **cos ω = cos m cos k**.

**T2.2 [EXACT] Exact Lorentz-form shell in deformed variables.** sin²ω = sin²m + cos²m sin²k. Writing ℰ = sin ω, μ = sin m and 𝒫 = cos m sin k gives ℰ² = μ² + 𝒫².

**T2.3 [EXACT; series CHECKED to 50 digits] Low-momentum law.**
- **ω² = k² + m² − (k²m²/3)·[1 + (k² + m²)/15] + O(8).** Every correction carries k²m².
- In units: E² = p²c² + M²c⁴ − (Mc²·pc·τ/ħ)²/3 + ….
- The nonrelativistic limit is ω ≈ m + k²/(2 tan m). So the inertial mass is tan m while the rest energy is m; "E = Mc²" fails at order (mτ)².

**T2.4 [EXACT] Velocity and γ.**
- v = cos m sin k / sin ω = 𝒫/ℰ, so 1 − v² = sin²m/sin²ω and γ = ℰ/μ.
- Massless: v ≡ ±1 at every k.
- Massive: |v| ≤ cos m, reached at k = π/2, and γ ≤ 1/sin m.

**T2.5 [EXACT, CHECKED] Time dilation.**
- Clock model: the walker carries two internal states with mixing angles m ∓ δ/2, i.e. internal energy entering as mass.
- The relative phase advances at δ·∂ω/∂m|ₖ. By the envelope theorem this equals the fixed-velocity rate to first order in δ.
- ∂ω/∂m = sin m cos k / sin ω = cos k·√(1 − v²), which gives **R(v) = ±√(1 − v²/cos²m)**, with the sign of cos k.
- So dilation is exactly Lorentzian, but with the species' own limiting speed cos m in place of the grid speed.
- Low speed: R ≈ 1 − v²/2 − (v tan m)²/2. γ⁻¹ is recovered, with relative deviation ½(Mc²τ/ħ)²(v/c)².
- Near the grid scale:
  - R → 0 as v → cos m.
  - At k = π/2 every mass shell passes through ω = π/2, so mass leaves no mark there and internal clocks stop.
  - For π/2 < |k| ≤ π the clock runs backward, with R ≈ −1 near k = π (the doubler).
- The chirality flip-flop is not a comoving clock. Its frequency is 2ω(k), and its two components separate.

**T2.6 [EXACT, CHECKED] Universality caveat.** An internal rotation applied once per tick that does not enter the mixing advances identically at every speed: it counts ticks. Uniform time dilation therefore requires internal energy to enter as mass-like mixing. The same caveat applies to continuous-time lattice models.

**T2.7 [ARGUED] No exact boosts.** Any flow that preserves every mass shell must fix their common crossing point (π/2, π/2). A nonlinear shell-preserving map also does not respect additive composition of the quasi-energy and momentum of independent packets.

#### T3. Global versus neighbourhood tick

**T3.1 [EXACT] Schedule independence.**
- Treat history as a network of events: gates on neighbourhoods, and formations whose menus depend on neighbouring records.
- Any two schedules that order every linked pair the same way give identical joint record statistics. Adjacent unlinked events act on disjoint parts, with no outcome dependence, so they commute as instruments; any two such schedules are connected by such swaps.
- Under (a), same-tick formations never depend on each other's records, so any order within a tick is equivalent.
- Hence a global tick and neighbourhood ticks with handshakes that rebuild the same network cannot be told apart by records. The tick's slicing (absolute simultaneity) has no readable content, and neither does the "at once" of Q1.

**T3.2 The analog of relativity of simultaneity.** [EXACT]
- The order of events outside each other's cone is unreadable; inside the cone it can be readable.
- Linked "together" formations are causally unrelated events in the network. Their coincidence is readable because it is a fact about the network, not about a slicing.
- [ARGUED] At low momentum, clocks and signals define tilted simultaneity surfaces that serve as well as the tick's. This is a neo-Lorentzian situation (comparator only).

**T3.3 [EXACT] A global tick's "rate" has no readable meaning.** Only step counts exist, so "constant" versus "variable" global tick is unreadable, unless the step itself depends on a duration.

**T3.4 Seams, where rates differ.**
- **Coincidence statistics change.** [EXACT toy, CHECKED] With rate ratio 2 and chance p per own tick, the coincidence fraction across the seam is p²(1−p)/(1−(1−p)³), about p/3, versus about p/2 in the bulk. Neighbourhood ticks with unlocked continuous phase offsets give zero coincidences across their boundary.
- **Flow balance.** [EXACT, given GNVW cut-independence] Content that carries an index must satisfy r_A·ind_A = r_B·ind_B. A one-qubit conveyor cannot run twice as fast on one side unless it is half as wide there. With qubits, rate ratios must be ratios of whole conveyor widths.
- **Conveyor slot counting.** [EXACT] On average, at most r_slow/r_fast of the fast side's slots can pass.
- [CHECKED] With a supplied seam rule:
  - From the fast side, transmission is 0.5000 at m = 0.
  - Packets refract by frequency matching: k goes from 0.30 to 0.150 (m = 0) or to 0.123 (m = 0.1, predicted 0.1224).
  - The naive rule also creates doubler content at k − π (weight 0.50).

**T3.5 [ARGUED] What different rates mean for causality** (overlaps A6/A4).
- Local-update networks stay acyclic, so there are no causal loops.
- The cone, counted in seam ticks, scales with the local rate: a lapse-like field. That gives twin-type step-count differences and bending toward slow regions.
- With fixed site spacing, a rate field acts like a pure g₀₀ field, whose light bending is half the observed value (comparator: PPN γ = 0 versus Cassini). So rate fields alone cannot be all of gravity.
- A zero-rate region freezes, and conveyor content arriving at it must turn around (flow balance).
- If records set the rates, the causal structure becomes record-dependent, and rate updates must themselves stay inside the cone.

#### T4. Quasi-energy periodicity

**T4.1 [EXACT] What it is.**
- The change is U per tick, and its eigenvalues lie on the unit circle. Energies become eigenphases ω, defined modulo 2π per tick.
- Records form only at ticks, so their statistics depend on U^n at whole n and are unchanged by ω → ω + 2π. Absolute quasi-energy beyond one turn is unreadable.

**T4.2 [EXACT] Consequences that records could register in principle.**
- (a) No oscillation of record odds is faster than one cycle per two ticks.
- (b) Any interacting step conserves summed quasi-energy only modulo 2π (time-umklapp).
- (c) Time doubler: a second cone sits at (k, ω) = (π, π), with the same dispersion times (−1)^{x+t} and an internal clock that runs backward. Interference between the 0-gap and π-gap content alternates record odds every tick.
- (d) A band can wind: ω(k + 2π) = ω(k) + 2πW, so ∮v dk/2π = W.
  - The featureless state then carries W sites per tick across every cut. No Hamiltonian band can do this.
  - A single conveyor has W = 1; the Dirac step has W = 0.
  - If records ride the conveyor (I2), they shift W sites per tick on average. [readability ARGUED]
  - In 3D, proper cubic rotations reverse the flow along any axis, so the net flow per axis is zero. [ARGUED]

**T4.3 [EXACT, CHECKED] The tick's imprint after averaging over geometric formation ticks.**
- A frequency θ survives with visibility p/|1 − (1−p)e^{iθ}|.
- That is p/(2−p) at θ = π, and 1 at θ = 2π (aliasing).
- Exponential waits instead give λ/√(λ² + θ²), which goes to 0.

**T4.4 [ARGUED; comparator] Heating risk.** A generic interacting step conserves no energy. Floquet literature finds heating unless the system is in a prethermal high-frequency regime. The Dirac step's bands fill the whole circle, so low-energy stability of an interacting stepping world is an open requirement.

#### T5. Visibility of a global beat

**T5.1 [EXACT, CHECKED] Coincidence of independent geometric waits.**
- P(T₁ = T₂) = Σₙ[p(1−p)^{n−1}]² = p/(2−p).
- P(|T₁ − T₂| = d) = 2p(1−p)^d/(2−p) for d ≥ 1.

**T5.2 Mapping onto misaligned pairs** (exact given Q7 and the prior probe result that sequence gives a shared frame and together gives none).
- A linked pair fails to share a frame exactly when both formed on the same tick. So **F_misaligned = p/(2−p)**, and the frame-sharing fraction is 2(1−p)/(2−p).
- Inverting gives a readable estimator: p = 2F/(1+F).
- If "misaligned" is instead meant as "landed on different ticks", that fraction is 1 − F.

**T5.3 [EXACT] The same number appears at the Nyquist frequency.** |E(−1)^T| = p/(2−p). Both quantities equal p/(1+q) by memorylessness.

**T5.4 What chance per tick makes the beat invisible.**
- **Pair channel, instant menus.** [EXACT] With instant menu-setting and continuous formation times, exact coincidence has probability 0. So F > 0 is a direct beat signature for every p > 0, fading as F ≈ p/2.
- **Statistical invisibility.** [ARGUED] With N linked pairs and per-pair distinguishability χ², detecting the beat needs N·F²·χ² ≳ 1. The beat is invisible for p ≲ 2/(χ√N), or for p ≲ 2/N if together-pairs can be recognised one by one.
- **Caveat.** [EXACT] If a record's effect on its neighbours' menus travels with the change (delay δ), continuous time gives a misaligned fraction 1 − e^{−λδ}. Any F can then be matched, so F alone stops singling out a beat; only tick-scale timing (T4.3) or faceting remains.
- **Triggered formation** (sites form only when a recorded neighbour calls). [reduction EXACT; thresholds COMPARATOR; bracket CHECKED]
  - Sites reached at exactly one site per tick form oriented bond percolation.
  - The recorded region grows flat facets moving at exactly the cone speed if and only if p exceeds about 0.6447 (square lattice) or about 0.3822 (cubic lattice).
  - Below that, the beat is macroscopically invisible, although microscopic coincidences remain.
- **Scale.** [ARGUED] With a tick near the Planck time, p = Γτ ≲ 10⁻²⁸ for realistic formation rates, so the beat is invisible in every channel. A world that looks continuous needs p ≪ 1.

#### T6. Preferred frame, and the order of dispersion

**T6.1 [EXACT] No new frame.** A drifting relabelling U' = T_n⁻¹U commutes with all proper cubic rotations only if Rn = n for every rotation R, which forces n = 0. The covariant step singles out the lattice's rest frame.

**T6.2 New observables from the tick are discreteness observables, not frame effects** (T1, T4, T5).
- [EXACT] Frame effects still enter only through grid dispersion, and the tick can remove them. 1D massless content has v ≡ 1 exactly, while the naive continuous lattice version has v = cos k.
- [EXACT for two-band steps] In d ≥ 2 an exactly dispersionless massless step is impossible. If cos ω = cos(c|k|) near 0, then by analyticity it holds everywhere, and periodicity would need both c and c√2 to be integers.

**T6.3 [EXACT] 1D order of departure.**
- v² = 1 − sin²m/sin²ω is even in E, so no odd orders of Eτ appear at all. Massless content: no departure at any order.
- Massive content, compared at the same E and rest energy: v²_lat − v²_cont = −(m²/3)·v²_cont − m²ω²/15 + O(m⁴).
- The leading effect is an energy-independent, species-dependent speed scale. Energy dependence first enters at (mτ)²(Eτ)². So the departure is **quadratic and suppressed by mass, never linear**.

**T6.4 3D under proper cubic rotations.**
- [EXACT] det U(k) is constant: finite range makes it a Laurent monomial, and invariance forces the exponent to zero.
- [EXACT, CHECKED] Tr U(k)^n is a rotation-invariant trigonometric polynomial. The lowest odd-degree invariant is xyz(x²−y²)(y²−z²)(z²−x²), of degree 9. At the (π,0,0)/(π,π,0) points the lowest is degree 5.
- [EXACT] So for any rotation-invariant two-band block with its cone at 0 or (π,π,π), and for every band-summed dispersion:
  - ω = c|k|·[1 + O(k²)], a quadratic departure, generically anisotropic (Σnᵢ⁴);
  - the leading speed is isotropic at those points, while anisotropic leading speeds are allowed at the (π,0,0)-type points.
- [EXACT] Why, in representation terms: a quadratic-in-k term times the content-set operators has a one-dimensional part only in the sign representation, which flips under quarter turns. It is forbidden in a two-band Weyl-type block, and allowed once an internal label also flips under quarter turns.
- [EXACT, CHECKED] Example: take the direct sum over the six orderings of three axis conveyors, U_s = e^{−ik_{s1}σ_{s1}}·e^{−ik_{s2}σ_{s2}}·e^{−ik_{s3}σ_{s3}}.
  - It is strictly covariant under all 24 rotations, with V_g independent of k.
  - Even orderings have cos ω = c_x c_y c_z − s_x s_y s_z; odd orderings have + s_x s_y s_z.
  - Its cone splits at linear order: ω = |k| ± |k|²·n_x n_y n_z. The two signs sit on branches that 90° rotations exchange.
  - The linear term comes from the order in which non-commuting axis conveyors act within a tick.
- [ARGUED, open] An isotropic, helicity-odd ±ξk² split between coupled blocks passes every spectral constraint found here. Decoupled rotation-invariant two-band blocks cannot carry it (constant determinant, EXACT).

**T6.5 [COMPARATOR] The experimental class.**
- Time-of-flight dispersion tests with gamma-ray bursts and flaring AGN, plus vacuum-birefringence (polarization) tests.
- LHAASO, GRB 221009A: E_QG,1 > 10·E_Pl and E_QG,2 > 6×10⁻⁸·E_Pl at 95% CL.
- Götz et al., GRB 061122: ξ ≲ 3.4×10⁻¹⁶.
- What that implies here:
  - A quadratic departure with an O(1) coefficient allows τ up to about 10⁷ t_P (about 10⁻³⁶ s).
  - A linear departure with an O(1) coefficient needs τ ≲ t_P/10 from timing alone.
  - If it splits polarization-like branches, a grid about 10¹⁵ times finer than the Planck length would be needed.

### 4. Checks

All scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A5/`. They ran with `nice -n 10`, all four thread caps set to 1, and a 60 s alarm. Every run took under 4 s.

One run broke the 300 MB budget: the first `check_fastmodes.py` grid at 121³ peaked at 362 MB for 0.26 s. A rerun at 81³ peaked at 121 MB and gave the identical result. All other runs peaked at or below 171 MB.

| Script | What it checks | Result |
|---|---|---|
| `check_dispersion.py` | Numerical eigenphases vs closed forms, 4000 k-points, m ∈ {0, .05, .3, .7, 1.2} | Dispersion error ≤ 1.5e-14. Shell identity ≤ 6e-16. v vs formula ≤ 5e-10. 1 − v² identity ≤ 1e-14. ∂ω/∂m ≤ 4e-10. R(v) identity ≤ 3e-13. Max \|v\| = cos m. Brickwork spectrum ≤ 3e-15 |
| mpmath, 50 digits | Series coefficients | The coefficient of k²m²(k²+m²) → −0.0222222 = −1/45 |
| `check_lightcone.py` | Strict cone vs continuous tails, step generator | Ring N = 1001, t = 200: amplitude outside the cone and on the wrong parity is exactly 0.0. Continuous hopping matches \|J_d(100)\|: d = 110 → 3.0e-3, 130 → 1.0e-8, 150 → 2.7e-16. Massive continuous Dirac: d = 110 → 4.2e-7. H_eff kernel: r\|h\| = √2 for m = 0; fitted decay 0.3225 vs predicted 0.3219 (m = 0.3) and 0.9195 vs 0.9195 (m = 0.8) |
| `check_clock_packet.py` | Moving-packet clock dilation | m = .3, δ = 1e-3, σ_k = .004, T = 400. Measured R matches √(1 − v²/cos²m) to ≤ 3e-4 relative for 10 momenta; at k = π/2 both vanish, absolute gap 1.2e-3 = O(σ_k). Continuum √(1−v²) is visibly off (k = 1.0: 0.186 vs 0.345). Decoupled rotation rate is 1.000000 at every speed |
| `check_beat.py` | Coincidence law, visibility, seam toy, facets | Exact series, and Monte Carlo with 2×10⁶ pairs: z = +0.18, −0.48, +0.06, +0.31. Seam formula matches series to 1e-12 and Monte Carlo (0.06567 ± 0.00018 vs 0.06557). 2D survival: 0.000 / 0.020 / 0.663 / 0.833 / 0.960 at p = .55 / .62 / .68 / .75 / .85. 3D: 0 / 0 / .417 / .783 at p = .30 / .35 / .42 / .50 |
| `check_seam.py` | Rate-2 seam, supplied rule | m = 0: slow→fast transmits 1.0000, split as k = 0.150 plus doubler −2.992 (0.50 each); fast→slow transmits 0.5000 at k = 0.300. m = 0.1: 0.972 at k = .123 (predicted .1224); 0.191 at k = .346 (predicted .3466) |
| `check_cubic.py` | Rotation invariants, conveyor product | Invariant dimensions for d = 1..9: [0,1,0,2,0,3,0,4,1], matching Molien. D4 has its first odd invariant at 5. Product dispersion ≤ 1.2e-15. (ω − \|k\|)/\|k\|² → n_x n_y n_z, with sign flip under 90° |
| `check_cubic2.py` | Six-ordering step | Strict covariance error 6.3e-16. Branches split ±0.1148 (three each) vs ±0.11454 |
| `check_fastmodes.py` | Fastest grid modes | Max group speed 1.2247 = √(3/2) at −(3π/4)(1,1,1); 41% of the zone is faster than low-energy light |

### 5. Real-physics match

**Implications if the tick is near Planck scale:**
- The strict cone cannot be told apart from Lieb–Robinson tails by any experiment.
- Low-energy kinematics matches special relativity up to (Mc²τ/ħ)² or (pa/ħ)². That is about 10⁻⁴⁵ for electrons, and about 10⁻³⁸ for time-dilation deviations of storage-ring muons.
- Species limiting speeds cos m differ by about ≤ 10⁻³⁴, even for the top quark.
- The beat (T5) and all quasi-energy effects (T4) sit at about ħ/τ, out of reach.

**Hard constraints on any concrete step (falsifiers):**
- Time dilation is observed to be universal. So internal dynamics must enter as mass-like mixing; tick-locked internal rotations are ruled out.
- No energy-linear photon speed change or vacuum birefringence is seen. So any linear-order branch split (T6.4) must vanish or be tiny for photon-like content. Fixed-order conveyor layers that carry such splits are effectively excluded.
- Quadratic, cubic-anisotropic dispersion is allowed up to τ ≈ 10⁷ t_P. Direction dependence tied to fixed sky axes would be the grid's signature.
- A pure tick-rate field gives half the observed light bending, so it cannot be the whole of gravity.
- An interacting step that heats quickly would contradict a cold, stable low-energy world.

**COMPARATOR literature, not adopted:**
- Lieb–Robinson (1972).
- Gross–Nesme–Vogts–Werner (2012); Ranard–Walter–Witteveen (2022).
- Meyer / Bialynicki-Birula / Strauch Dirac walks.
- D'Ariano–Perinotti (2014), who found no two-component Weyl walk on the simple cubic lattice under their isotropy assumptions.
- Bibeau-Delisle et al. (2015), relativity-like structure from walks.
- Durrett–Liggett (1981), flat edges in growth shapes; oriented-percolation thresholds.
- Gisin (1990), signalling from nonlinear rules; Hellwig–Kraus (1970).
- Floquet heating: D'Alessio–Rigol, Lazarides–Das–Moessner, Abanin et al.
- PPN/Cassini; Coleman–Glashow.

Only the two GRB results were checked online in this run ([LHAASO, PRL 133, 071501](https://link.aps.org/doi/10.1103/PhysRevLett.133.071501); [Götz et al., MNRAS 431, 3550](https://academic.oup.com/mnras/article/431/4/3550/1157600)). The rest are cited from memory; verify before citing.

### 6. Open edges and next steps

1. **3D step.** Find a star-local, proper-cubic-covariant 3D step with one low-energy cone. Measure its quadratic anisotropy and test it for a linear-order branch split. A design hint: applying the axis conveyors in a fixed order within a tick generates the linear term; acting on all axes at once (symmetrically) may avoid it.
2. **Isotropic helicity-odd linear term.** Decide whether coupled multi-band steps can realise it. This matters given the framework supplies only proper rotations.
3. **Formation timing must be linear.** Any I1 timing rule needs formation chances that are linear in the site's possibilities, or it signals outside the cone (T1.2). This is a consistency condition, not a new import.
4. **Interacting steps.** Establish heating rates or prethermal stability.
5. **Time doubler.** Does the staggered half-filled vacuum populate the π-gap partner?
6. **Seams.** Compare seam rules (Haar-type versus naive doubler creation), and hand the rate-as-lapse question to A6.
7. **Triggered growth.** Compute the misaligned fraction against distance from the facets, as a cheap 2D toy. It also bears on the open question of spontaneous versus called-for formation.
8. **Tension with Q2 and Campaign 7.** Q2 ("evolves continuously") and Campaign 7's sentence 2 (continuous change) both assume continuity. Under I1, sentence 2 becomes a stepping change: the strict cone and conveyors are gained, and the price is quasi-energy folding.

### 7. Plain-language summary

If every site in the grid changes in lockstep, one beat at a time, then nothing can spread faster than one site per beat, exactly rather than almost. Things moving through such a grid would, at slow speeds, behave just as Einstein's relativity says: moving clocks run slow by the familiar amount, with tiny differences that show up only at the scale of single grid steps. A shared beat leaves almost no trace in the records. The only traces are exact ties between neighbouring records forming on the same beat, and regions that beat at different rates, which show as seams that bend and bounce what crosses them. The beat adds no new "special direction of rest" beyond the one the grid already has. In one dimension light-like content is not sped up or slowed by its energy at all; in three dimensions the grid's rotations rule out the strongest such effect for simple content but not for every arrangement, and sky observations of distant bursts already rule out the strongest kind unless the beat is unimaginably short.

Sources:
- [Stringent Tests of Lorentz Invariance Violation from LHAASO Observations of GRB 221009A (PRL 133, 071501)](https://link.aps.org/doi/10.1103/PhysRevLett.133.071501)
- [The polarized gamma-ray burst GRB 061122 (MNRAS 431, 3550)](https://academic.oup.com/mnras/article/431/4/3550/1157600)