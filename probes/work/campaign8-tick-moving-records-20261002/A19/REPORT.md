I have everything needed. Here is the report.

# A19 report: do repeated registrations of an unrecorded massive mover give a straight track (inertia)?

All files are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A19/`. Each script `X.py` has its output in `out_X_<args>.txt` and its time and memory in `time_X_<args>.txt`. The wrapper is `run.sh`.

**Grades.** EXACT = proof or exact arithmetic. CHECKED = numeric check with a stated tolerance. ARGUED = reasoning without proof. COMPARATOR = literature, cited and not adopted. Everything is a supplied toy. The ticked change is I1 read as a named conditional, not an adopted position.

**Units.** A "cell" is A5's two-component site, which is two qubit sites of the single-track chain. Speeds are in cells per tick (light speed = 1). Momentum K is in radians per cell. The cut width σs is in qubit sites.

---

## 1. Question

In the assembled model, everyday motion must come from unrecorded movers that leave fresh, stationary records now and then. The setup is:
- the mover runs on the ticked 1D Dirac step;
- a linear formation instrument fires near it with chance g per tick;
- each record cuts the mover's possibilities to agree.

Does the trail of records come out straight, i.e. with inertia? Specifically:
- What are the track's velocity persistence, its spread from back-action, and the trade-off with registration rate (Zeno-type freezing)?
- Does the record track's mean velocity equal the group velocity v(k0)?
- Is momentum conserved across registrations?
- What registration coarseness is needed, and is a coarse cut compatible with "a record locks exactly one possibility" at one site?
- Does the 3D signed cycle (A10) behave the same way?

## 2. Answer

**Conditional yes. The negative half is EXACT in the toy; the positive half is EXACT for the mean and CHECKED otherwise; the real-world scales are ARGUED.**

**When registrations are sharp (one site), there is no inertia.** This is the case where a record forms directly from the mover's own site weight.
- Each record resets the mover completely. The track becomes a Markov walk that forgets k0 at its first record (EXACT).
- Only one bit survives each record: which sublattice the record landed on, i.e. the sign of the velocity. That bit is kept with probability 1 − sin(m)/2 per record at low rates (EXACT).
- Every record spreads the mover's momentum over the whole zone (EXACT). A slow massive mover is turned into a near-light-speed zigzag.
- Registering every tick gives a persistent walk with diffusion cot²m. It freezes only lattice-heavy movers (Zeno-type).
- In the toy, a record formed from a lone excitation's own neighbourhood can only cut it to within one star (EXACT). So direct registration is always this sharp kind. That includes A13's lone-excitation formation weight `c·P_singlet`.

**When registrations are coarse, Newton's first law emerges at the record level.**
- Coarse means the cut's width σ is much larger than the mover's reduced de Broglie length (σp/ħ ≫ 1).
- Symmetric unsharp registrations conserve the mean momentum exactly (EXACT).
- The track runs at v(k0) (CHECKED to ≤ 0.011 over K0 from −0.3 to 1.2).
- Each track's velocity random-walks by v′²/σs² per record. The direction persists for about 4(σp/ħ)² records.
- The best rate gives a velocity precision of the standard-quantum-limit form, δv ≈ √(2v′/T), independent of σ (CHECKED within about 25%).
- Coarse cuts are compatible with "a record locks exactly one possibility" when the record forms on a mediator. The mover is then cut only through the mediator's link: a broad partial cut plus the recoil. EXACT structure; CHECKED, with the velocity kept up to the physical recoil.
- In 3D (A10's signed cycle), coarse registrations keep the direction of motion and sharp ones erase it (CHECKED, small box).
- A thrown ball satisfies all of this with enormous margins (ARGUED).

## 3. Derivation

### 3.0 The toy

**D0 [EXACT; CHECKED 4e-16].** The mover is one excitation over the aligned emptiness on one axis. The change is A13's round with θe = π/2 and θo = π/2 − m, which is A5 T2's Dirac step:
- a′ⱼ = −cos m·aⱼ₋₁ − i sin m·bⱼ
- b′ⱼ = −i sin m·aⱼ − cos m·bⱼ₊₁

Here a is the even (right-moving) sublattice and b the odd (left-moving) one.
- Bloch form: cos W = cos m cos K.
- Band velocities: ±v(K), with v = cos m sin K / √(sin²m + cos²m sin²K).
- Checks: the fast step matches explicit pair gates to 4.4e-16. A band packet moves at v(K0) to within 2.5e-3, a finite-width effect.

**D1 [EXACT].** The registration instrument is linear (A9 Thm 1), with a Lüders cut and a no-record update √(1−F) (A9 Thm 2):
- Kraus operators: K_y = √(g·w(x−y)) when a record forms at y, and K_null = √(1−g) otherwise.
- The likelihood w is a delta (sharp site cut), a Gaussian of width σs (unsharp cut), or a block indicator (fixed partition).
- In the one-excitation sector, with Σ_y w = 1, the no-record update is exactly √(1−g)·1. Registration times are therefore Bernoulli(g), independent of the mover's state, and between records the mover evolves freely. (CHECKED: mean time to the first record 5.12 ± 0.29 and 5.34 ± 0.27, against 1/g = 5.)
- Records sit on medium sites next to the path and never move. Their readable content is their place. The tick is bookkeeping, because formation time is not record content (A13 T4).

### 3.1 Sharp site registration: the brief's toy

**S1 Reset [EXACT].** A site cut leaves the mover in |y⟩ whatever its past. The track is therefore a Markov additive process on (place, sublattice bit), and nothing about k0 survives the first record except through that bit.

**S2 [EXACT].** For a band state, (weight on the right-moving sublattice) − (weight on the left-moving sublattice) = v(K). So P(the first record lands on a right-moving site) = (1 + ⟨v⟩)/2.

**S3 [EXACT, Konno-type; CHECKED].** After a record on a right-moving site:
- the long-time mean velocity is ∫v² dK/2π = 1 − sin m;
- the velocity variance is sin m·(1 − sin m).

Check: at n = 1500, 0.85057, 0.43545 and 0.06811, against 0.85056, 0.43536 and 0.06796.

**S4 [EXACT; CHECKED].** The probability of staying on the same sublattice after n ticks is p_RR(n) = 1 − ∫ sin²(nW) sin²m / sin²W dK/2π (formula and simulation agree to 6 digits).
- The direction correlation per record is r(g, m) = 2·E_n[p_RR(n)] − 1.
- Limits: r → 1 − sin m as g → 0, and r = cos 2m at g = 1.
- The mean sublattice bit after k records is E[c_k] = ⟨v⟩·r^(k−1).

Checks:
- Record-parity correlation against the exact r, at m = 0.6 for g from 0.01 to 1: within 1.5σ (e.g. 0.3635 ± 0.0027 vs 0.3624).
- Gap-conditioned z-tests, which remove window censoring: pooled mean −0.0028 ± 0.0057 over 30,502 segments.
- E[c_k] against ⟨v⟩r^(k−1): within 2σ in three cases.

**S5 [EXACT].** Track diffusion is D_track = g·(M2 + κμ/q), where μ, M2, κ and q are per-record moments of the exact kernel (`exact_sharp.py`).
- At g = 1: the walk continues with probability cos²m per tick, q = sin²m and D = cot²m.
- At g = 0.3, the per-segment MC moments match exactly: μ = 1.673 ± 0.013 vs 1.672, and M2 = 8.61 ± 0.10 vs 8.64.

| m | r (g → 0) | speed during a run, gμ (g = 0.01) | D (g = 1) | Character |
|---|---|---|---|---|
| 0.15 | +0.85 | 0.85 | 43.8 | Light-speed zigzag |
| 0.6 | +0.43 | 0.44 | 2.14 | Diffusive |
| 1.4 | +0.01 | 0.017 | 0.030 | Frozen |

**S6 [EXACT; CHECKED].** The track has no memory of K0. The least-squares slope is about 0 for every K0 from −0.3 to 1.2 (all within 3σ of 0), and the late-half slope is consistent with 0 in every case.

**S7 [EXACT].** After a site cut, the momentum is uniform over the zone, with exactly half the weight in each band. For small m this means near-light speed, and an O(1) quasi-energy (O(ħ/τ)) is injected per record.

**Sharp-cut regimes:**
- **(i) Rare records.** The mover flies straight between records, at a velocity drawn afresh from the chirality-biased Konno law. Direction persists with probability 1 − sin(m)/2 per record.
- **(ii) Frequent records, light mover.** A light-speed persistent walk: heating, not freezing.
- **(ii) Frequent records, heavy mover.** Zeno-type freezing. CHECKED at m = 1.4, g = 1: the track spread stays at 20.4–20.7 cells (the initial packet width) for 600 ticks, while free motion would cover 74 cells; r = −0.9423 ± 0.0010 vs the exact −0.9422.
- **Massless (m = 0).** The track is exactly straight at light speed under every cut (EXACT; CHECKED with slope 1.000000 and zero deviation). This is a 1D chirality accident (see §3.4).

### 3.2 Coarse (unsharp) registration

**C1 [EXACT].** Averaged over outcomes, the instrument multiplies the possibilities' density matrix by (1 − g) + g·C(x − x′), with C(d) = Σ_z √(w(z)w(z−d)). This depends only on x − x′, so the averaged momentum distribution is convolved with a fixed symmetric kernel.
- The mean momentum is conserved.
- The variance grows by 1/σs² per record (K in rad/cell, σs in sites).
- CHECKED at σs = 64: final momentum spread 0.0722/0.1196/0.2024/0.3822 against predicted 0.0715/0.1245/0.2111/0.3835 (within 4%); mean K 0.298–0.310 against 0.300.

**C2 [EXACT for the mean, ARGUED for single tracks].** E[track velocity] = E[v(K)] = v(K0) while the momentum spread stays in the linear part of v.
- A single track's velocity random-walks by v′²/σs² per record.
- Persistence lasts about N_p = (σs·K0)² = 4(σp/ħ)² records. For the base mover (m = 0.6, K0 = 0.3) that is 1.4, 23 and 369 records for σs = 4, 16 and 64.

**C3 [ARGUED; CHECKED ≤ 4%].** The spread around the straight line is Var(Y(t) − v0·t) ≈ σr² + (g·v′²/σs²)·t³/3, where σr is the record scatter. At σs = 64, g = 0.3: 47.0 and 87.1 cells predicted, against 48.5 and 84.8 measured at t = 300 and 600.

**C4 Optimal rate [ARGUED; CHECKED].** Over a window T, the slope variance is about 12σr²/(gT³) + (13/35)(g·v′²/σs²)·T.
- The best rate is g* ≈ 11.4·σr·σc/(v′T²), where σc = σs/2 is the cut width in cells.
- At that rate the variance is about 2.1·(σr/σc)·v′/T, independent of σ. In physical units this is δv ≈ 1.45·√(ħ/(MT)).
- The track therefore looks classical when Mv0²T ≫ ħ.
- CHECKED: the best root-mean-square slope error is 0.079, 0.066 and 0.073 for σs = 32, 64 and 128, against an estimated 0.062. The predicted best rates are about 0.0075, 0.03 and 0.12; the observed best-rate ranges are about 0.01–0.02, 0.02–0.05 and 0.05–0.4.

**Base-mover map [CHECKED].** m = 0.6, v0 = 0.397, T = 600 ticks. Each cell gives the whole-window slope (mean ± sd), then in brackets the final momentum spread.

| Cut | g = 0.01 | g = 0.03 | g = 0.1 | g = 0.3 | g = 1 |
|---|---|---|---|---|---|
| Site | 0.12 ± 0.44 [≈2.7] | 0.00 ± 0.31 | 0.00 ± 0.18 | −0.01 ± 0.10 | 0.00 ± 0.07 |
| Gaussian σs = 4 | 0.29 ± 0.34 [0.64] | 0.24 ± 0.42 | 0.12 ± 0.48 | −0.01 ± 0.37 | 0.02 ± 0.20 [2.6] |
| Gaussian σs = 16 | 0.37 ± 0.15 [0.16] | 0.36 ± 0.19 | 0.28 ± 0.32 | 0.22 ± 0.43 | 0.14 ± 0.50 [1.6] |
| Gaussian σs = 64 | 0.39 ± 0.18 [0.05] | 0.39 ± 0.07 | 0.39 ± 0.08 | 0.37 ± 0.14 | 0.33 ± 0.25 [0.38] |

- At σs = 64, the first-half and second-half slopes have the same sign in 96–100% of tracks for g ≤ 0.3.
- Band mixing (backward-moving content) per record is about 2e-2, 5e-4 and 7e-5 for σs = 4, 16 and 64.

**Zeno with coarse cuts [CHECKED].**
- **Sliding (unsharp) cuts never freeze; they heat (C1).** At high rate the momentum spreads, as in the g = 1 column above.
- **Fixed partitions (pixels) do freeze slow movers at high rate.** With 32-site blocks at g = 1, the heavy mover's mean velocity is 0.001 against v0 = 0.123.
- **Sharp block edges also heat.** At g = 0.03, 128-site blocks give a momentum spread of 0.96, against 0.07 for 64-site Gaussians.
- **The tick caps the rate at one record per tick**, so the continuous-time Zeno limit does not exist. Freezing requires a fixed partition much coarser than the mover's motion per registration interval.

**One record per site [CHECKED; this refutes my own prior].** The formation weight is zero at already-recorded sites (menus set by records, Q7). The no-record update √(1−F) then suppresses the mover's possibilities on fresh sites (A9 Thm 2c), so the record cluster becomes a trap. At m = 1.4 and g = 1 there are only 13 records in 600 ticks, and the track spread stays at the initial 20.8 cells: the mover stays frozen. I had expected that using up the registering sites would release a frozen mover; it does not at high rate.

### 3.3 Where coarse cuts can come from (task 3)

**R1 Direct records are star-sharp [EXACT].** Suppose the formation weight F_y is star-local (A9 iii) and annihilates the emptiness (A9 iv). In the one-excitation sector, √F_y|x⟩ = 0 for every x outside star(y).
- So a record formed from the mover's own neighbourhood cuts it to within one star.
- A group of records forming on one tick does no better: the mover can be in at most one star.
- Partial weights inside the star still leave it on at most 7 sites, which is a lattice-scale momentum spread.
- So direct registration falls under S1–S7: no inertia for massive movers.

**R2 Mediated records are coarse [EXACT structure; CHECKED].** A sharp single-site record of a probe, after the probe has interacted with the mover, acts on the mover as M_y(x) = ⟨y|V_x|probe⟩.
- Σ_y |M_y(x)|² = 1 (checked to 1e-13).
- The modulus is broad: about 15 cells. The phase gradient is the recoil.
- Static check: the mover's momentum shifts by −0.156/−0.085/−0.187 against a recoil of 2q = −0.2/−0.1/−0.2. Its spread grows only from 0.05 to 0.06–0.08, and its band weight stays ≥ 0.998.
- For comparison, a direct site cut gives spread 1.81 (uniform) and band weight 0.5.

**R3 Dynamic check: time-umklapp [EXACT argument; CHECKED].** I ran the full two-excitation version, with the mover moving and recoiling. The contact |11⟩ phase is part of the A10 S1 gate family.
- Joint staggering of both partners (the time-doubler map Λ_A·Λ_B) commutes with the two-body step. The contact phase acts only on pairs that this staggering leaves unchanged.
- Hence every reflected pair amplitude splits 50/50 between the ordinary channel and a doubled channel (both partners K → K + π, band switched, two-body quasi-energy conserved only mod 2π). This is A5 T4.2(b, c) made concrete.
- CHECKED: the doubled channel's quasi-energy is 4.8566 against 2π − 1.4273 = 4.8558. Its share of the reflected weight is 0.499/0.498/0.490. Its total weight falls roughly as m² (0.145 down to 0.0002 for mover/probe masses from 1.2/0.1 down to 0.075/0.025).
- The doubled band at K + π has the same velocity, so the mover's velocity is kept in both channels. Heavy mover: v0 = 0.269 becomes 0.227 ± 0.017 after the probe reflects, against 0.02 ± 0.26 for a direct site cut. A lighter mover takes a larger, physical recoil (0.724 → 0.509).
- Caveat: the momentum spread I first quoted from the position-space conditional states (1.96) was misleading. Its distribution is bimodal across the two channels; the velocity distribution is narrow.

**Conclusion for task 3.** "A record locks exactly one possibility at one site" is compatible with a coarse cut on the mover when the record forms on a mediator that carried the mover's influence away (ARGUED). For the trail to trace the path, the mediator must also be absorbed near the path (ARGUED).

### 3.4 3D brief (task 4)

**ARGUED.** On A10's signed time-symmetric cycle (θ = 0.6), all eight bands at q0 = 0.8 move within cos ≥ 0.98 of ±n. A Gaussian cut diffuses the direction by about 1/(2σc²q²) rad² per record. Sharp cuts erase it.

**CHECKED.** L = 48 torus, 24 tracks, 30 cycles, rate 0.25 per cycle. The real-space step matches the Bloch form to 1.1e-15. The unregistered packet moves at 1.01 sites per cycle along n (cos 0.995).

| Cut | Speed along n | Mover direction (cos) | Record-cloud principal axis (cos) |
|---|---|---|---|
| Sharp site | 0.07 ± 0.06 and −0.005 ± 0.06 | ≈ 0 | −0.04 / −0.10 |
| Gaussian σ = 8 sites | 1.01 and 1.03 | 0.90–0.93 | 0.75–0.80 |
| Gaussian σ = 4, or rate 1 per cycle | 0.70–0.74 | 0.65–0.70 | — |

- The record cloud is fat because the record scatter is comparable to the 30-site track; a longer track is needed for a crisp readable line.
- Massless 3D movers are not protected. The exact 1D straightness is a chirality accident.

### 3.5 Readability [ARGUED]

Formation ticks are not record content. The readable form of the first law is therefore spatial: records lie on a straight line with uniform mean spacing v/g. Equivalently, equal distance per accumulated record, which is the owner's time count. Direction along the line and speed need correlation with other accumulating records, i.e. a clock.

## 4. Checks

All runs used `nice -n 10`, the four thread caps at 1 and a 60 s alarm. The longest took 31 s.

| Script | What | Key result |
|---|---|---|
| `check_core.py` | Step, Bloch form, dispersion, packet velocity, Konno mean, p_RR | 4e-16 / 2e-14 / 2e-16; 1 − sin m to 1.5e-4 at n = 1500 |
| `exact_sharp.py` | Exact Markov reduction | Closed forms at g = 1 and g → 0 reproduced; table in S5 |
| `check_markov.py`, `check_markov_big.py` | Censoring-free z-tests, massless control | Pooled z −0.0028 ± 0.0057; slope 1.000000 at m = 0 |
| `mc_grid.py` (site/cell/σ4/σ16/σ64/b32/b128/su, scans) | Quantum-trajectory tracks | §3.1–3.2 tables |
| `mc_k0.py` | Slope vs K0 | Coarse: within ≤ 0.011 of v(K0); sharp: about 0 |
| `check_chirality_memory.py` | E[c_k] = ⟨v⟩r^(k−1) | Within 2σ |
| `mediated.py` | Static mediator instrument | R2 numbers |
| `mediated_dynamic*.py`, `umklapp_check.py`, `mediated_velocity.py` | Dynamic two-body, time-umklapp | R3 numbers |
| `track3d.py` | 3D signed cycle | §3.4 |

**Peak memory.** At most 204 MB in the retained runs.

**Budget breach.** Six early `track3d.py` runs, with 24 tracks in one batch, peaked at 363–372 MB for about 4 s each. Their outputs were also wrong (an unwrapping error) and were discarded; I reran them in batches of 8 at ≤ 195 MB.

**Other discarded outputs:**
- the first massless control (NaN at the K = 0 point, now guarded in `core1d.py`);
- one set of 3D runs that received the wrong arguments.

**Should be run (bigger, not run):**
- a moving-window 3D box of 128 sites or more, to get crisp readable lines;
- a gas of mediators illuminating the mover symmetrically, to test mean-recoil cancellation and that momentum diffusion = rate × reflection probability × (2q)²;
- A13's full formation weight acting on a medium.

## 5. Real-physics match

**Matches (COMPARATOR, from memory, unverified):**
- Mott (1929): tracks are straight because each ionisation localises the particle only to atomic size, much larger than its wavelength.
- Continuous-measurement theory (Caves–Milburn; Diósi; GRW form): unsharp position registrations conserve the mean momentum, diffuse it by ħ²/(4σ²) per registration, and make the spread grow as t³.
- The standard quantum limit (Braginsky; Caves): δv ~ √(ħ/(MT)).
- Zeno (Misra–Sudarshan): freezing needs a fixed partition.
- Scattering decoherence (Joos–Zeh; Gallis–Fleming; Hornberger–Sipe): mediated registration with recoil.
- Quantum-walk weak-limit laws (Konno); two-particle interacting walks (Ahlbrecht et al. 2012, possibly relevant).

**Requirements and falsifiers (ARGUED):**
- **Site-sharp registration of matter.** At Planck ticks an electron has m ≈ 4e-23 in lattice units. Each such record would make it move at near light speed, with about 2 GJ (ħ/t_P) of kick. Slow tracks falsify this.
- **Heating bound.** Earth's heat flow (about 47 TW over 3.6e51 nucleons) limits direct sharp registration to below about 1e-90 per nucleon per Planck tick, far below A13's interference bound.
- **Coarseness needed.** Registrations need σ ≫ ħ/p: about 0.2 nm (≈ 1e25 lattice sites) for a 1 eV electron.
- **Everyday bodies pass easily.** For a 1 kg·m/s ball with atomic-scale registrations, 4(σp/ħ)² ≈ 4e48 records against about 1e27 per second; the limit precision is δv ≈ 1e-17 m/s.
- **Time doubler.** Contact collisions populate it with an O(1) share of the reflected weight (R3). Content staggered at Planck frequency is not observed, so this must be suppressed or shown to be invisible. This is a falsifier for sharp contact interactions, and it bears on A5 open edge 5.

## 6. Open edges and next steps

1. **Time-umklapp.** Does any star-local interaction avoid the joint-staggering symmetry? What do doubled pairs, whose internal clocks run backward (A5 T2.5), do to records?
2. **A mediating medium in A13's model.** Find one in which records form near the path while the cut on the mover stays coarse.
3. **Symmetric illumination.** Test drag, and that mean recoil cancels.
4. **Strength of the one-record-per-site trap.** Measure it against the number of registering sites per path site (4 in 3D).
5. **Composite bodies.** Centre-of-mass inertia when the constituents are what gets registered.
6. **Owner decisions:**
   - may a lone excitation form records directly, and at what rate (R1 says it then loses all inertia)?
   - is formation order readable at all (§3.5)?

## 7. Plain-language summary

A thing that has never been recorded can coast in a straight line, and the records it leaves now and then can line up into a straight trail, but only if each new record pins it down loosely, over a stretch much wider than its own ripples. If a record pins it to one exact spot, it forgets how fast and which way it was going: the trail turns into a jittery zigzag, or, for a very heavy thing recorded every step, it freezes in place. Records must also not come too often, because each loose pinning gives a tiny random nudge and the nudges add up, so there is a best pace that keeps the trail both visible and straight. A record only touches its own spot and its neighbours, so the loose pinning has to come from something small and soft that bumps the thing and is then recorded itself; the thing feels only the soft bump. A thrown ball easily meets all of this, so in this toy it keeps going straight, as Newton said.