I have everything needed. Writing the report.

# A4 report: filling, jams and event-rate profiles (lane M)

Scratch directory (all scripts and outputs): `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A4/`

**Grades.** EXACT = proof, exact arithmetic or exact enumeration. CHECKED = numeric check with a stated tolerance. ARGUED = reasoning without proof. COMPARATOR = literature result, cited and not adopted.

All models below are supplied toys. All formation and move rules are named conditionals, not framework content.

## 1. Question

Take the infinite grid with records that form only at empty sites, at most one per site per tick. If I2/I3 hold, records also move at most one site per tick, with odds set by the neighbourhood.

1. Which formation rules avoid local freezing, so that no final state is reached?
2. Suppose move odds are tilted toward crowded places, ∝ e^{g·(records around the destination)}.
   - Do jammed regions form?
   - Are they sealed, or do they leak and evaporate?
   - How does the leak scale with size?
3. Does the local event rate (formations plus moves, per site per tick) fall off toward a frozen region in a way that resembles gravitational time dilation?

## 2. Answer

**Conditional overall.**

**(i) Freezing vs no final state.**
- Without moves, every site has at most one event ever, so every region reaches a final state [EXACT].
- With moves and permanent records, a homogeneous grid gains at most 1−ρ₀ records per site over all time [EXACT].
- Every event needs an empty site, so events per site per tick are at most twice the empty fraction h [EXACT].
- One number then decides the outcome: p₀, the formation odds of a lone empty site surrounded by records.
- **If p₀ > 0:** h falls exponentially and every site has a last event (freezing).
  - This covers spontaneous formation, where h = h₀(1−p)^t exactly for any grid size, any move rule and any dimension [EXACT].
  - It also covers "needs a recorded neighbour", soft crowding suppression, and stirring that counts the site's own vacating move. These are EXACT where the odds have a floor, otherwise mean-field ARGUED, and CHECKED.
- **If p₀ = 0 and records move:** the rule needs a second empty neighbour, or hard crowding suppression, or stirring by other records' moves. Then h thins algebraically: t·h stays between 5.1 and 5.4 for t = 100–1500 in 3D. Events never stop at any site but grow ever sparser (thinning) [ARGUED, CHECKED].
- An eternal state with a steady nonzero rate would need formation to switch off for a reason the record pattern does not show [ARGUED].

**(ii) Jams under the crowd tilt.**
- Yes, jams form above an onset. The mean-field onset is derived below. In the tick toy, two phases appear at g ≈ 1.0–1.25 in 2D and 0.70–0.75 in 3D [CHECKED].
- No jam is sealed:
  - Every edge record has odds of about (number of exits)·e^{−g·(recorded neighbours)} > 0 to step out each tick [EXACT].
  - The interior keeps a small fraction of empty sites that move almost every tick [EXACT + CHECKED].
  - In empty surroundings jams evaporate.
- About 99% of escaping records come straight back, so the net loss is set by spreading through the surroundings, not by the edge [CHECKED in 2D].
- The net loss is roughly size-independent in 2D and ∝ radius in 3D. Evaporation time therefore grows like N (2D, times a log) or N^{2/3} (3D) [ARGUED; 2D CHECKED].

**(iii) Time-dilation analog: mostly no.**
- At balance, the event rate is flat from about 4 sites outside the jam outward [CHECKED, ±6%].
- A long-range fall-off exists only while records flow into the jam. It then has the Newtonian (harmonic) shape: linear for a flat jam face, ln r around a 2D disk, 1/r around a 3D ball [EXACT for the continuum equation; CHECKED for the flat-face case].
- Its strength is set by the inflow, not by the jam's content, and outflow reverses its sign [CHECKED].

## 3. Derivation

### 3.0 Supplied toy T1 and named conditionals

**Grid and tick.** Sites are empty or carry one record. One tick is a move phase followed by a formation phase (global ticks, I1 conditional).

**Move phase (I2/I3 conditional).**
- Each record at x draws one option: stay, or move to one empty neighbour y.
- Odds: w(y) = e^{g S_y}, where S_y = records around y other than the mover. w(stay) = e^{g S_x}, where S_x = records around x.
- If several records draw the same y, one wins with probability ∝ its drawing probability; the others stay.
- No chains: a destination must be empty at the start of the tick.
- g = 0 is unbiased.

**Formation phase.** Each empty site (after moves) forms with odds set by one of these rules:

| Rule | Odds at an empty site |
|---|---|
| F-spont | p |
| F-contact | p if at least 1 neighbour is recorded |
| F-kempty(k) | p if at least k neighbours are empty |
| F-soft(β) | p·e^{−β·n_rec} |
| F-hard(m) | p·(n_empty/z)^m |
| F-stirA | 1−(1−p)^a, a = arrivals at its neighbours this tick, including the record that just left this site |
| F-stirB | same, excluding that record |
| F-trig(m) | p if at least m neighbours are recorded |

Notation: z = 2d. h, F, M, E = empty fraction, and formations, moves, events per site per tick.

**Named conditional C-perm.**
- If "records are permanent" means a record never leaves its site, moves are excluded and only 3.1(a) applies.
- If it means a record is never destroyed, I2 moves are allowed.

**Comparator model K** (continuous time, not the brief's tick rule): each move x→y happens at rate e^{g S_y}.

### 3.1 Bookkeeping (task 2)

**(a) No moves ⇒ at most one event per site, ever** [EXACT]. One permanent record per site, and nothing else can happen at that site.

**(b) Homogeneous bound** [EXACT].
- Assume a translation-invariant start and a covariant rule. Then expected arrivals equal expected departures at each site.
- So ρ(t+1) − ρ(t) = F(t) ≥ 0, and Σ_t F(t) ≤ 1−ρ₀.
- Corollary: if time is the accumulation of records, each region's average total record-time is bounded by its size.

**(c) Events need empty sites** [EXACT, no-chain rule].
- M(t) ≤ h(t), because each arrival lands on a site empty at the start of the tick.
- F(t) ≤ h(t), because moves conserve the number of empty sites.
- So E(t) ≤ 2h(t).

**(d) Summable emptiness ⇒ local final state** [EXACT, Borel–Cantelli]. The expected number of events at a site is at most 2Σ_t h(t). If that sum is finite, each site has a last event almost surely.

**(e) A positive odds floor ⇒ freezing** [EXACT].
- If every empty site forms with odds ≥ p_min, then E[H(t+1) | past] ≤ (1−p_min)H(t).
- F-spont: H(t) ~ Binomial(H₀, (1−p)^t) exactly, because moves relabel empty sites but never create or remove them.
- F-soft: the floor p·e^{−zβ} gives an exponential rate ≥ p·e^{−zβ}.

**(f) Lone empty site inside a jam** [EXACT].
- Suppose the site's neighbours, and their other neighbours, are all recorded.
- Each of the z neighbours chooses it with probability exactly 1/2 for every g, because the stay and move weights are both e^{g(z−1)}.
- So the empty site steps to a uniformly chosen neighbour with probability 1−2^{−z} per tick (15/16 in 2D, 63/64 in 3D).

### 3.2 Formation rules (task 1)

Mean field with mixing moves (product closure): dh/dt = −p·h·Φ(h). The equations are EXACT as algebra; their use is ARGUED; the asymptotics are CHECKED in section 4.

| Rule | Φ(h) | Steady states | Late behaviour | Events forever at each site (with moves)? | Without moves |
|---|---|---|---|---|---|
| F-spont | 1 | h=0 | e^{−pt} [EXACT] | No (freezing) | final state |
| F-contact | 1−h^z | h=0 stable; all-empty grid absorbing [EXACT] | e^{−pt} | No locally; yes globally from a seed | final state; growth front |
| F-kempty(k) | Σ_{j≥k} C(z,j) h^j (1−h)^{z−j} ≈ C(z,k) h^k | h=0 | h ≈ [k·p·C(z,k)·t]^{−1/k} | Yes (thinning) | final state with isolated empty sites |
| F-soft(β) | (h+(1−h)e^{−β})^z → e^{−zβ} | h=0 | exponential, rate ≥ p·e^{−zβ} | No (slow freezing) | same |
| F-hard(m) | ≈ h^m | h=0 | h ≈ (m·p·t)^{−1/m} | Yes | final state |
| F-stirA | Φ(0) > 0 (a vacated site always has the arrival next to it) | h=0 | exponential | No | no formation |
| F-stirB | ≈ z·h | h=0 | ≈ 1/(p·z·t) | Yes | — |
| F-trig(m≥2) | Σ_{j≥m} C(z,j)(1−h)^j h^{z−j} | h=0; dilute regions grow only ∝ ρ^m | e^{−pt} near full | No | final state |

**Lone-hole criterion** [MF ARGUED; the freezing direction is EXACT by 3.1e].
- At high density almost every empty site is a lone hole surrounded by records, so the odds p₀ of that single environment decide.
- p₀ > 0 ⇒ exponential freezing.
- p₀ = 0 ⇒ h ~ t^{−1/m}, where m = extra empty sites (or other records' moves) the rule needs nearby. Σh diverges iff m ≥ 1.
- Beyond mean field for m = 1, the empty sites wander and merge: c/t in 3D, ln t/t in 2D, t^{−1/2} in 1D [COMPARATOR: coalescing random walks, Bramson–Griffeath]. Events per site then grow like ln t in 3D.

### 3.3 The infinite grid and what "no final state" requires (task 2)

**Global vs local.**
- Under F-contact without moves, a finite seed always has empty boundary sites, each forming with odds p. So formations never stop on Z^d, even though each site has at most one event [EXACT].
- With moves, the front is Fisher–KPP-like with speed ≈ 2√(D·p·z) [ARGUED; COMPARATOR].

**The brief's open question (does an empty site far from any record form on its own?).**
- If yes, with odds ≥ p_min > 0: every region freezes exponentially, everywhere at once [EXACT].
- If no: the empty grid stays empty forever, and activity spreads as a front from existing records [EXACT].

**Requirements for no final state at each site.**
- **N1.** Records must move [EXACT].
- **N2.** Σh must diverge [EXACT].
- **N3.** p₀ must be 0. A positive floor freezes [EXACT]; that the lone-hole environment alone decides is mean-field.
- **N4.** With N1–N3, the result is thinning: events never stop, but their rate goes to 0 [MF, CHECKED].
- **N5.** A steady nonzero rate with h(∞) > 0 needs formation to stop while moves continue.
  - On a finite torus the move chain is irreducible and aperiodic, so every pattern recurs [EXACT].
  - So formation odds would have to depend on something beyond the record pattern, for example the Q1 shared possibilities [ARGUED].
- **Finite-torus aside.** Under F-kempty(1) with one-at-a-time formation, the last empty site can never fill and wanders forever. With simultaneous formation, two adjacent empty sites can both fill, so the torus may end full [EXACT].

### 3.4 Crowd-tilted moves: mean-field stability (task 3)

**Reversibility.**
- K is reversible with the Gibbs law π ∝ e^{g·(recorded neighbour pairs)} [EXACT]: the ratio of rate(x→y) to rate(y→x) equals the change in pair count.
- T1 is not reversible [EXACT, by enumeration on a 4×4 torus].
  - Detailed balance fails by 1e−5 to 3e−4, against round-off near 1e−14.
  - At g = 0, T1 mildly repels pairs: P(two records adjacent) = 0.225 vs 0.267 uniform.

**General long-wave formula** [EXACT under product closure].
- D_eff = −Σ_w (2w·e − 1) ∂Φ_{x→y}/∂ρ_w, with Φ_{x→y} = E[n_x(1−n_y)·q] and q = probability the record at x ends at y.
- Proof:
  - Φ is multilinear in the site densities, so a linear density profile gives a current of first order in the gradient.
  - The reflection that swaps x and y leaves the rule unchanged and maps w·e to 1−w·e. That turns the current into Σ (2w·e−1)·∂Φ_{x→y}.
- Uniform density is unstable at long wavelength iff D_eff < 0.

**K closed form.**
- D_eff = A[1 − γ(z+1)ρ(1−ρ)], with A = (1−ρ+ρe^g)^{z−1} and γ = (e^g−1)/(1−ρ+ρe^g).
- Onset: e^g = [c(z+1)+1−ρ]/[c(z+1)−ρ], c = ρ(1−ρ). At ρ = ½ this gives g_c^MF = 0.847 (2D) and 0.588 (3D). There is no instability for ρ ≥ z/(z+1).
- Growth rate: σ(k) = −A(z−λ_k)[1 − γc(1+λ_k)], λ_k = 2Σcos k_i.
  - The onset is at k → 0.
  - The fastest mode is λ* = (z−1)/2 + 1/(2γc).
- For small g this reduces to g(z+1)ρ(1−ρ) = 1. The static Bragg–Williams estimate has z in place of z+1; the extra +1 comes from excluding the mover itself.
- Algebra EXACT; CHECKED against Monte Carlo within 1.3σ.

**T1 mean-field onset** [CHECKED, Monte Carlo of the exact product closure].

| ρ | 2D g_c | 3D g_c |
|---|---|---|
| 0.05 | 2.9 | — |
| 0.1 | 1.45 | 0.96 |
| 0.2 | 0.93 | 0.64 |
| 0.3 | 0.80 | 0.56 |
| 0.5 | 0.81 | 0.57 |
| 0.7 | 1.12 | — |

**Observed two-phase onset in T1** [CHECKED, slab runs]. 2D: between 1.0 and 1.25. 3D: between 0.625 and 0.75. Mean field undershoots by about 1.3–1.5×, as it does for K (comparator exact K values: 1.763 in 2D, ≈0.887 in 3D).

### 3.5 Jams (task 3)

**Conditions for jams** [ARGUED; COMPARATOR: nucleation, Gibbs–Thomson].
- g is above the onset.
- The density lies between the coexisting values ρ_v and 1−h_l. Inside the spinodal (D_eff < 0) clumping is spontaneous; between the spinodal and coexistence it needs nucleation.
- A jam survives only if its surroundings hold at least ρ_v(R), which rises for small R. On Z^d with empty surroundings, a jam evaporates.

**Coexistence in T1** [CHECKED; flat slab, approached from both sides].

2D:

| g | 1.25 | 1.5 | 1.75 | 2.0 | 2.5 |
|---|---|---|---|---|---|
| ρ_v (vapour density) | ≈0.05 | 0.013 | 0.0035 | 0.0015 | ~0.0004 |
| h_l (empty fraction inside jam) | 0.098 | 0.044 | 0.021 | 0.0094 | 0.0037 |

3D:

| g | 0.75 | 0.875 | 1.0 | 1.25 | 1.5 |
|---|---|---|---|---|---|
| ρ_v | 0.048 | 0.022 | 0.012 | 0.0035 | 0.0013 |
| h_l | 0.155 | 0.088 | 0.051 | 0.019 | 0.0076 |

- For K, the Boltzmann answer is ρ_v = h_l ≈ e^{−zg/2}.
- T1 breaks this symmetry: h_l is about 2–6 times ρ_v.

**"Fully recorded" jams.**
- At finite g the jam interior keeps empty sites at fraction h_l, each moving with probability 1−2^{−z} per tick.
- So the interior rate is h_l(1−2^{−z}) > 0: time slows but does not stop [EXACT + CHECKED].
- At g = 1.5 in 2D, the interior (≈0.03 events per site per tick) is busier than the coexisting vapour (≈0.009).

**Gross edge leak per edge record per tick** [EXACT single-tick odds, empty exterior].

| Edge record | Escape odds |
|---|---|
| Flat face (any d) | 1/(e^{(z−1)g}+1) |
| 2D corner | 2/(e^{2g}+2) |
| 3D cube edge | 2/(e^{4g}+2) |
| 3D cube corner | 3/(e^{3g}+3) |

These odds are never zero, so no jam is sealed. On a finite torus every jam dissolves and re-forms infinitely often [EXACT].

**Net leak** [ARGUED; 2D CHECKED].
- The net loss is limited by spreading in the vapour, not by the edge:
  - 3D: Q ≈ 4π·D·R·ρ_v(R), so ∝ R.
  - 2D: Q ≈ 2π·D·ρ_v/ln(R_out/R), roughly size-independent.
  - D is the free-record spreading rate: 1/5 per tick in 2D, 1/7 in 3D.
- Per edge record, the net leak falls like 1/R.
- Evaporation time: ≈ R²/(2D·ρ_v) ∝ N^{2/3} in 3D; ∝ N·ln N in 2D.
- An edge-limited leak would instead give Q ∝ R^{d−1}. The 2D data exclude that.

### 3.6 Event rate near a jam (task 4)

**Event rate tracks vapour density.** In the dilute vapour, the event rate equals density × moves per record, and moves per record are nearly constant (0.65–0.79 in 2D) [CHECKED].

**Why the profile is harmonic.**
- For symmetric exclusion in continuous time, d/dt E[n_x] = Σ_{y∼x} (E[n_y] − E[n_x]); the pair terms cancel [EXACT].
- So the steady density profile is discrete-harmonic. For the dilute tilted vapour this holds to leading order [ARGUED].

**Consequences.**
- **(P1) Balance:** the rate is flat beyond the near-surface layer [ARGUED, CHECKED].
- **(P2) Inflow Q:** a harmonic profile [EXACT continuum, CHECKED planar]:
  - linear in front of a flat face;
  - ρ_v + (ρ_∞−ρ_v)·ln(r/R)/ln(R_out/R) around a 2D disk;
  - in 3D, e(r)/e_∞ = 1 − Q/(4π·D·ρ_∞·r) = 1 − (1−ρ_s/ρ_∞)·R/r.
- **(P3) Outflow:** the same shape with the opposite sign, so events are more frequent near the jam [CHECKED].

**Coordinate caution.** A perfect sink gives e/e_∞ = 1 − R/r. That matches Schwarzschild's −g_tt only in areal coordinates, and the GR clock rate is √(−g_tt). So the match carries no evidential weight [ARGUED].

### 3.7 Formation and tilt together

All runs: 2D, g = 1.5 [CHECKED].
- **F-spont:** the whole grid freezes. Time stops everywhere, not just inside jams.
- **F-kempty(1):** jams merge into one dense medium that keeps thinning. There is no distinct frozen region.
- **F-trig(3):** jam interiors become event-free, but the jam grows as a front by forming records at its surface.
- **F-trig(4)** (only fully enclosed empty sites form):
  - Interior empty fraction drops to 0.5–4%, not zero.
  - The jam grows slowly by refilling vacancies that its own leaks inject.
  - The vapour stays alive.
- **Conclusion:** in these rules, an I5-like region where nothing happens inside never appears as a static sealed object in a living medium. It appears only as a growing front or a slowly growing, leaking jam [ARGUED from toys].

## 4. Checks

Every run used `nice -n 10` and OMP/OPENBLAS/VECLIB/MKL = 1. Each invocation finished in ≤ 32 s with ≤ 80 MB.

**Code self-tests** (`selftest.py`, `selftest_corner.py`).
- Record count is conserved and moves are one-to-one: pass.
- Isolated record stays with probability 1/(1+2d): 0.1973±0.002 (expected 0.2), 0.1421±0.0017 (expected 0.1429).
- 2D flat-face leak:

  | g | measured | exact | σ |
  |---|---|---|---|
  | 0.5 | 0.1835 | 0.1824 | 0.0011 |
  | 1.0 | 0.0480 | 0.0474 | 0.0006 |
  | 1.5 | 0.01139 | 0.01099 | 0.00029 |

- 2D corner leak:

  | g | measured | exact | σ |
  |---|---|---|---|
  | 0.5 | 0.4229 | 0.4239 | 0.0039 |
  | 1.0 | 0.2121 | 0.2130 | 0.0032 |
  | 1.5 | 0.0869 | 0.0906 | 0.0023 |

- 3D edge-record leak odds for 5, 4 and 3 recorded neighbours: all within 2σ.
- A bool-addition counting bug in the first corner test was fixed; the library itself was unaffected.

**F-spont exactness** (`toy1_exact40.py`, 40 seeds, 128²). Ratio of summed H(t) to H₀(1−p)^t:

| Setting | t = 20 | t = 50 | t = 100 |
|---|---|---|---|
| No moves | 1.0007±0.0018 | 0.9983±0.0048 | 1.0107±0.0179 |
| Moves, g = 2 | 0.9999±0.0018 | 0.9994±0.0048 | 1.0271±0.0179 |

All points are within 1.6σ of exact binomial errors.

**Formation rules** (`toy1_formation.py`, 2D 128², ρ₀ = 0.2, p = 0.05, 2000 ticks; moves at g = 0 where marked).

| Rule (moves?) | h(100) | h(500) | h(2000) | Late slope (500–2000) | Events per site | Sites with an event in last 500 ticks |
|---|---|---|---|---|---|---|
| spont (no) | 0.0045 | 0 | 0 | — | 0.799 | 0 |
| spont (yes) | 0.0049 | 0 | 0 | — | 10.2 | 0 |
| contact (yes) | 0.0046 | 0 | 0 | — | 10.6 | 0 |
| kempty(1) (no) | 0.1915 | 0.1914 | 0.1914 | 0 | 0.608 | 0 |
| kempty(1) (yes) | 0.078 | 0.0169 | 0.0048 | −0.91 | 39.3 | 0.68 |
| soft, β=1 (no) | 0.393 | 0.219 | 0.051 | exp. rate 0.00096 (floor 0.000916) | 0.75 | 0.03 |
| soft, β=1 (yes) | 0.336 | 0.134 | 0.022 | exp. rate 0.00118 | 170 | 0.996 |
| hard, m=1 (no) | 0.266 | 0.247 | 0.247 | 0 | 0.55 | 0 |
| hard, m=1 (yes) | 0.185 | 0.057 | 0.0158 | −0.90 | 94.6 | 0.98 |
| stirA (yes) | 0.0050 | 0 | 0 | — | 9.5 | 0 |
| stirB (yes) | 0.113 | 0.028 | 0.0081 | −0.92 | 56.8 | 0.85 |

- Soft suppression with moves still looks alive at t = 2000. The floor proves it freezes later; the bound h ≤ 0.128 at t = 2000 holds.
- Mean field at t = 2000: kempty 0.0026, hard 0.0099. The 2D toy decays more slowly, as expected from fluctuations.

**3D thinning** (`toy1_3d.py`, 40³, 1500 ticks).
- kempty(1): t·h = 5.32 / 5.21 / 5.36 / 5.09 at t = 100 / 400 / 1000 / 1500; slope −1.00.
- stirB: slope −0.93, with t·h rising slowly toward a constant.
- Events per empty site: 0.98–0.99.

**Mean field** (`tmf.py`).
- K closed form matches Monte Carlo within 1.3σ at 4 points in 2D, and within 1σ at 4 points in 3D.
- T1 onset values are as tabulated in 3.4; the bracketing points are separated by ≥ 20σ.

**Clumping** (`toy2_clump.py`, `toy2_blocks.py`, 128², 1000–2000 ticks).
- Neighbour excess B at ρ = 0.5 rises from 0.91 (g = 0) through 1.30 (g = 1.0) to 1.70 (g = 2).
- Dense 4×4 blocks (≥15 of 16 recorded) at ρ = 0.5: 0.4% at g = 0.75, 3.6% at g = 1.0, 13% at g = 1.25, 23% at g = 2.

**Coexistence** (`toy3_slab2.py`). Values as tabulated in 3.5. Vapour approached from below (empty start) and from above (seeded start) converge from g = 1.25 up in 2D and from g = 0.75 up in 3D. At g ≤ 1.0 (2D) and ≤ 0.625 (3D) the slab dissolves.

**Exact enumeration** (`exact_small.py`, 4×4 torus, 2–3 records).
- K: stationary law equals Gibbs to 1e−14.
- T1: max |π/π_Gibbs − 1| ranges 0.15–14.6. At g = 2 with 2 records, P(adjacent) is 0.466 vs 0.729 for Gibbs.

**2D evaporation** (`toy3_evap.py`, g = 1.5, 128² empty box, 2000 ticks, 4 seeds per size).

| Side s | 6 | 8 | 12 | 16 | 24 |
|---|---|---|---|---|---|
| Edge records | 15.5 | 29.1 | 55.2 | 87.7 | 168 |
| Gross detachments per tick | 0.89 | 1.16 | 1.66 | 2.19 | 3.26 |
| Fraction that return | 0.986 | 0.993 | 0.995 | 0.995 | 0.996 |
| Net loss per tick | 0.0123±0.0031 | 0.0087±0.0014 | 0.0081±0.0012 | 0.0116±0.0025 | 0.0139±0.0009 |

- Diffusion-limited estimate of net loss: 0.008–0.02 per tick.
- Half-lives: 111 (s = 4), 697 (s = 6), 1222 (s = 8).

**Event-rate profiles** (`toy4_planar2.py`; flat jam face, 96×128, 4 seeds × 2000 ticks).
- **Closed box (balance):** e(d) goes 0.0084 → 0.0093 → 0.0082 from d = 6 to d = 41, a small non-monotone hump. A flat fit gives χ²_r = 0.71, so the profile is flat to about ±6%.
- **Absorbing bath (outflow):** e falls from 0.0073 to 0.0009. Linear fit χ²_r = 1.6; flat fit χ²_r = 66. The ratio of flux to gradient gives D = 0.25±0.03, against the free-record value 0.2.
- **Bath at 0.02 (inflow):** slope +1.41e−4±0.15e−4 per site. Linear fit χ²_r = 1.5; flat fit χ²_r = 7.2.
- **Radial 2D runs** (`toy4_profile2.py`) give the same three signs. However, their i.i.d.-redrawn bath acts like a slightly over-full source, because redrawing breaks up the vapour's natural clusters. This artifact is flagged; the shape claims rest on the planar v2 runs.

**Formation plus tilt** (`toy5_form_tilt.py`, `toy6_crowdtrig.py`, `toy6b_crowdtrig.py`; 2D, 2000 ticks).
- F-spont: h = 0 by t ≈ 1000.
- F-kempty: h = 0.027 at t = 1000 and 0.014 at t = 2000; events per empty site 0.87–0.90.
- F-trig(3): empty fraction inside the jam reaches 0; records grow 494 → 1803.
- F-trig(4): records grow 494 → 852.

**Runs outside the literal envelope (2D, ≤ 128², ≤ 2000 ticks).** Each still ran in under 32 s and under 80 MB.
- `toy1_3d.py`: 64,000 sites.
- `toy3_slab2.py` 2D: 64² sites × 10,000 ticks.
- `toy3_slab2.py` 3D: 12,800 sites × 4000 ticks.

**Not run (bigger).** `big3d_evap_profile.py` was smoke-tested at tiny size only. It checks the 3D predictions that Q ∝ R and that the profile goes as 1/r. The usage lines are in its docstring; each run takes about 1–3 minutes and ~200 MB.

## 5. Real-physics match

**Thinning and clocks.**
- If time is the tick count, thinning means local physics slows down like 1/t. No observation shows that.
- If clocks are made of events, a uniform slowdown is just a relabelling of ticks and cannot be detected from inside [ARGUED].

**Bounded record-time** [EXACT consequence of 3.1b].
- Under "time = accumulation of records" plus permanence, each region can only age by a bounded amount, about one record per site. Real proper time is unbounded at every place.
- Possible ways out: count moves as time, or keep an ever-growing frontier into empty grid.

**Jams vs black holes.**
- Jams behave like droplets in a condensing vapour, a short-range effect [COMPARATOR: lattice-gas condensation]. They are not gravitational collapse. The nearest-neighbour rule excludes inverse-square pull [ARGUED].
- Jams always leak; classical black holes do not [EXACT].
- Jams lose more per tick the bigger they are (loss ∝ R in 3D, lifetime ∝ N^{2/3}). Hawking evaporation runs the other way: loss ∝ 1/M², lifetime ∝ M³ [COMPARATOR]. This opposite trend falsifies a literal analogy.

**Time dilation.**
- In GR, a static mass slows nearby clocks with a 1/r profile set by its mass alone, and the sign never flips.
- In this toy there is no long-range effect at balance [CHECKED].
- Under inflow, the strength is set by the inflow (in 3D ∝ jam radius × far-field excess density), and outflow reverses the sign.
- The match is in shape only, because both solve Laplace's equation outside a source.
- **Falsifier:** a static, non-accreting jam shows a flat profile [CHECKED].

## 6. Open edges and next steps

1. **Run the 3D script** (`big3d_evap_profile.py`) to test Q ∝ R and the 1/r profile.
2. **Owner decision on C-perm:** does permanence allow records to move? Every "no final state" result with permanent records hinges on it.
3. **Framework-native lone-hole odds.**
   - Under Q3/Q7, an empty site whose neighbours are all recorded might still have a menu of two or more possibilities with nonzero formation odds. Then the rule is freezing-type.
   - If full enclosure leaves nothing for formation to settle (odds 0), the rule is thinning-type.
   - This single question decides (i).
4. **Tick-rule choice under I3.**
   - T1 is not reversible.
   - A Metropolis-type rule, odds e^{g(S_y − S_x)}, would give Boltzmann jams with ρ_v = h_l ≈ e^{−zg/2}.
   - Allowing moves into sites vacated in the same tick would relax the M ≤ h bound.
5. **Shared depletion fields between accreting jams** (∝ 1/r in 3D). These drive ripening and competition [COMPARATOR: Lifshitz–Slyozov]. They are the only long-range coupling in this toy and are worth a dedicated toy.
6. **Coupling to I4 flow.** Can a standing conveyor maintain a permanent inflow, giving a steady 1/r profile with fixed strength?
7. **Local vs global ticks (I1).** The classification depends only on odds per tick, so asynchronous ticks should give the same mean-field equations [ARGUED, unchecked].

## 7. Plain-language summary

If records never move, each spot can gain at most one record and then nothing more happens there, so every part of the grid eventually stops. Even with moving records, the grid as a whole can gain only about one record per spot in total, so if time is counted by records alone, every region can only age by a limited amount. With moving records, the grid can stay alive forever only if an empty spot completely surrounded by records cannot form a record by itself; then empty spots grow rarer and events slow down without ever stopping. When moves lean toward crowded places, records gather into packed clumps, but no clump is sealed: records at its edge keep stepping out, a few empty spots keep wandering inside, and in empty surroundings a clump slowly comes apart, with bigger clumps taking longer. Near a clump, events happen at the same pace as far away unless records are streaming in, when they thin out near it and recover with distance the way a heavy body's pull fades, or streaming out, when they speed up near it; so the likeness to time slowing near a heavy body holds only in the shape of the fall-off, and only while records are on the move.