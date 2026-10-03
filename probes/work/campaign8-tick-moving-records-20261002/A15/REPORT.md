# A15 report: local beats, seams, and whether moving records need a shared beat

Scratch directory: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A15/`. Everything here is a supplied toy: the A10 partial-swap cycles in 1D, 2D and 3D, and the A11 full-transfer cycle in 2D. Nothing is adopted. I did no git work, made no repo edits and spawned no subagents.

## 1. Question

Can records still move when each neighbourhood keeps its own beat, with local schedule phases that may run at different rates, instead of everyone sharing one global schedule phase (A10's N1)? At a seam where two regions disagree in phase or rate:
- does the seam block motion, scatter it, carry one-way channels (A11 open edge 2), or create or destroy anything?
- is a universal beat needed for records to move?

## 2. Answer

**Conditional.**

**Rigid local clocks: every disagreement is a wall.** Here each site keeps its own fixed clock. Under the natural rule, a pair acts only if both sites' clocks pick it. Wherever two neighbours' clocks disagree, the pair between them never acts, for any gate angle and any nonzero offset.
- The wall is a perfect mirror. Each side evolves exactly as if the other side were recorded (EXACT; CHECKED in 1D, 2D and 3D).
- In the handed 2D A11 cycle, the wall carries two one-way channels running in opposite directions, one on each side, so the net flow is zero (EXACT, CHECKED).
- Getting something through needs one of two things. One is a second gate on the seam site within one sub-step, which breaks the one-site-per-tick cone there (transmission 0.64–1.00, CHECKED). The other is an unrecorded random choice, which destroys coherence (transmission 2/9 at full swap, EXACT).

**Waiting local clocks: seams heal, but rates lock.** Here a site waits for its partner before taking its turn. A mismatch is then just a relabelling that leaves at the cone speed, and records move exactly as under one global beat (EXACT, CHECKED). Two costs follow:
- No neighbourhood can keep a different long-run rate. Neighbouring step counts never differ by more than two cycles, and a slow region throttles everything connected to it (EXACT).
- A closed loop of sites, each waiting on the next, stops every site in the world (EXACT). Random starting phases did this in 40/40 runs in 2D and 3D.

**Rate differences under rigid clocks.** They work only as commensurate steps; a 2:1 step refracts packets and totally reflects half of the fast side's band (CHECKED). Smooth rate gradients fill up with walls and become opaque (CHECKED).

**Bottom line.** A global master clock is not needed. Motion does need a beat that is shared in every readable respect: equal rate everywhere and no waiting loops. Neighbourhood-dependent slowing fits with motion when it sits in how much change happens per shared beat. A record-set gate angle passes a smooth lapse with transmission 1.0000 (CHECKED). It does not fit when it sits in how often the beat comes (ARGUED as a package).

## 3. Derivation

**Setup.**
- Gate on a pair: G(θ) = exp(−iθ·SWAP). Its one-excitation block, relative to the empty pair, is u = e^{iθ}(cos θ − i sin θ σ_x).
- A schedule word is a cyclic list of layers. Each layer is a perfect matching of the lattice:
  - A10 1D: (even, odd);
  - A10 2D: (xe, xo, ye, yo);
  - A10 3D: the six-layer word;
  - A11: four sub-steps with the sublattice-dependent directions +x, +y, −x, −y.
- In every one of these words, each bond appears in exactly one layer per period p.
- A site "names" its partner in the current layer.
- Two clock models:
  - **Rigid:** site x uses layer t + φ(x) (mod p) at the common sub-step count t.
  - **Waiting (self-timed):** site x keeps its own counter c(x), uses layer c(x) + φ(x), and advances only when its pair fires.
- Seam rules:
  - **H (handshake):** a pair acts iff both sites name it.
  - **K (conflict-skip):** candidates are the pairs named by at least one site; any candidate that shares a site with another is skipped.
  - **P:** a one-sided request wins over the agreed pair it conflicts with.
  - **Smu / Sum (sequential):** agreed pairs first, then requests (Smu), or the reverse order (Sum).
  - **R:** H or P, each with odds ½.

**S0. A per-site beat is extra state (ARGUED).** Local beats need each site to carry a register saying which pairing comes next. The axioms supply only the site's possibilities and at most one record. So this register is a named conditional, just as A10's N1 global phase is.

### Rigid local clocks

**S1. Theorem A: mismatched bonds never act under H (EXACT).**
- Bond (x,y) sits in one layer j_xy. Site x names it only when t + φ(x) ≡ j_xy, and y only when t + φ(y) ≡ j_xy. If φ(x) ≢ φ(y) (mod p), the two never coincide, for any θ and any geometry.
- Stronger form at straight walls: take any rule that (i) applies every agreed pair and (ii) keeps each sub-step a set of disjoint pairs, which is the strict one-site cone. Whenever x names the cross pair, y is in an agreed pair inside its own region, and vice versa. So no such rule ever acts across a straight wall.
- At island corners a non-H rule could leak; H cannot.
- Exception: in words where a bond appears in more than one layer (palindromes, time-symmetric blocks), some offsets let a cross bond act at one of its slots. Not computed.

**S2. Phantom lock (EXACT; CHECKED).** Under H, each region evolves exactly as if every site outside it carried a record under A11's lock rule (pairs touching a record are skipped). CHECKED as an exact permutation equality on both sides of A11 strips with k = 1, 2, 3.

**S3. 1D rule table (offset 1; the only nontrivial offset in 1D).**

| Rule | Result | Grade |
|---|---|---|
| H | Perfect mirror, T = 0 | EXACT, CHECKED |
| K | Perfect mirror; the two seam sites never act again (a two-site frozen pocket) | EXACT |
| P | Perfect mirror; the seam pair becomes an isolated pocket that swaps every sub-step | EXACT |
| Smu = Sum | Partial transmission, T → 1 at full swap; reach 2 sites in one sub-step at the seam, so the cone is broken there | CHECKED |
| R | Partial transmission, T = 2/9 at full swap; coherence lost (purity drops) | EXACT at full swap; CHECKED otherwise |

- Smu and Sum give identical numbers because their gate networks coincide apart from one initial seam gate acting before the packet arrives (EXACT).
- The R value 2/9 comes from an absorbing-chain solution (f = 2/3, b = 1/3, c = 4/9, T = c/2).
- R needs a random choice that no record holds, which is outside the ontology unless something registers it. Treat R as a comparator rule.

**S4. 2D and 3D (EXACT by S1; CHECKED).**
- 3D A10 word, H, slabs normal to each axis, offsets 1–5: zero weight ever crosses.
- **A11 open edge 2 (task 4):** under H, a straight phase wall (k = 1, 2, 3) carries +1 qubit per cycle on one side and −1 on the other. The net is zero, the two channels are exactly decoupled, and nothing crosses.
  - Islands of mismatched phase have an outer clockwise ring of 2s+1 items and an inner counter-clockwise ring of 2s−1 items. Their net circulation is zero for s ≥ 4.
  - This is S2 plus A11 D2 and D5: each side sees the other as recorded, and both have the same handedness.
- Under K the net is still zero, but the channels move one column inward (k = 2) or spread over two columns (k = 1, 3).
- Aside: a handedness wall (mirror word in one region) carries a net +2 per cycle. Both channels co-propagate (CHECKED).

### Waiting (self-timed) clocks

**S5. Firing order is irrelevant (EXACT).** Disjoint ready pairs commute. The event network is fixed by the words and the initial phases (the k-th x–y event of x is the k-th x–y event of y). By A5 T3.1, records cannot reveal the timing.

**S6. 1D healing (EXACT; CHECKED).** An offset-1 seam is the uniform network started on a stepped surface.
- A wait front leaves at one site per round. Every site on the lagging side waits exactly once (58 waits for 58 sites), and a uniform beat remains behind.
- Packets cross the old seam with T = 1 − 2×10⁻¹⁰ for θ = π/2, π/4 and 0.3.

**S7. Theorem B: lag lock (EXACT).** Each bond appears once per period in both endpoints' words. So n_xy (the number of x–y events) lies within one of c(x)/p and within one of c(y)/p. Hence |c(x) − c(y)| ≤ 2p.
- Consequences:
  - equal long-run rates across any connected network;
  - a slow region throttles all of it.
- CHECKED: with B available every second round, every site ends at rate 0.500, the throttled zone in A grows exactly one site per round, and the maximum neighbour difference is 1.

**S8. Theorem C: a waiting loop freezes everything (EXACT).**
- If sites x₁ → x₂ → … → x_n → x₁ (n ≥ 3) each name the next and none is named back, none of them ever fires again. A frozen site never changes its choice.
- Any neighbour freezes when it next names a frozen site, which happens within p of its own events.
- By induction, every site's total future is bounded by p·(its distance to the loop) + p.
- Flat phase fields (the uniform network on a valid stepped surface) never form such loops (EXACT).
- CHECKED cases:
  - **A11:** deadlock and a fully frozen torus for every island tested (s = 1, 2, 4; k = 1–3), for x-normal strips at k = 1, 2, for y-normal strips at k = 2, 3, and for a single plaquette vortex (frozen region 16 → 126 → 632 → 1024 sites at rounds 10/20/40/80).
  - **A11 healed exactly in the two cases my hand calculation predicts are flat:** x-normal k = 3 and y-normal k = 1.
  - **A10 words:** single-site offsets and slabs do not deadlock. A single site emits an expanding lag domain about 0.5–0.6 sites per round, with a uniform beat inside.
  - **But A10 words do deadlock:** a 0/2/0/2 plaquette freezes the whole torus by round 15.
  - **Random offsets:** deadlock in 40/40 runs for A10 2D, A10 3D and A11 2D.
  - **2% sparse offsets:** deadlock in 6/40 runs (A10 2D) and 25/40 runs (A10 3D).

### Rate mismatch (task 2)

**S9. Commensurate 2:1 step, rigid clocks, H-rate rule.**
- A slow region (one sub-step per tick) meets a fast one (one cycle per tick). The seam repeats every 2 ticks, so ω_A(K_A) ≡ 2ω_B(K_B) (mod 2π) using full one-cycle phases (EXACT).
- The gate's built-in singlet phase e^{2iθ} acts as a potential proportional to θ × (gate rate) (EXACT for this gate family).
- Predictions confirmed (CHECKED):
  - transmitted momenta match the prediction to ≤ 0.007;
  - no sidebands: at least 0.9988 of the transmitted weight sits within ±0.5 of the main peak;
  - fast → slow is 0.5000 at full swap, matching slot counting and A5 T3.4;
  - exactly 0 for the half of the fast band that has no partner on the slow side.

**S10. Smooth gradient, rigid clocks.**
- Neighbouring counts drift apart without bound, and a bond agrees only 1/p of the time (EXACT counting).
- CHECKED (100 sites, rate 1 → ½): 10, then 50, then 50 of 100 bonds mismatched at T = 20, 100, 300. Transmission falls to 0.021 (θ = π/2) and 0.157 (π/4).
- The same step taken sharply and commensurately gives 0.5000 (π/2) or 0 (π/4, in the no-partner window). With no rate change, transmission is 1.0000.

### Event-paced beats (task 3)

**S11. Consistency (C), no-signalling (NS) and the cone.**
- If records set the pacing, every step is a classically controlled local instrument. Then:
  - (C) holds: an adaptive sequence of instruments gives a valid joint record distribution (EXACT);
  - (NS) holds, by A5 T1.2 and A9 Theorems 1–2 (EXACT);
  - the strict cone holds in event counts: at most one site per causal event (EXACT).
- CHECKED on 200 random 4-qubit snapshots: maximum total-variation distance 2.7×10⁻¹⁶ when records set the pace. Pacing by the uncut possibilities signals: 0.257 (threshold rule) and 0.096 (angle set by possibilities).
- A7 caveat (ARGUED): if the beat is triggered by the moving content's own registered position, A7 Step 6 forces a full cut at each move (R1), and motion becomes classical.

**S12. Motion under event pacing (CHECKED; growth exponent of ⟨x²⟩).**
- E1 (wait): ballistic, exponent 1.96–1.99 for event odds q = 1, 0.5, 0.2. Only the pace changes.
- E2 (slip, H): diffusive, exponent 0.70–1.20. Mismatches do not freeze motion; they scramble it.
- E3 (one shared beat, each gate randomly skipped): diffusive at long times. For θ = 0.2 the crossover is slow (1.75, then 1.47).

### Synthesis

**S13. Dichotomy.**
- With fixed words, a local beat either waits, which locks rates (S7) and risks a global freeze (S8), or slips, which turns every disagreement into a wall (S1) and every gradient into an opaque stack of walls (S10). (EXACT)
- Neither lets neighbourhoods keep different sustained time while records move freely. Hence A8's event-paced change cannot be a pair-schedule beat rate. (EXACT within these toys; ARGUED beyond them.)

**S14. Angle lapse (CHECKED; package ARGUED).**
- Setup: one shared beat, with the gate angle set by records and varying in space.
- Results:
  - steps 0.3 → 0.25 and 0.6 → 0.5, either sign: a sharp step transmits 0.984–0.992, a 60-site ramp transmits 1.0000, and transmitted momenta match conserved quasi-energy to 0.002;
  - halving θ near the crossing leaves no partner states, and the packet reflects totally.
- For small θ the whole one-excitation spectrum scales with θ, including the e^{iθ} offset per gate. So θ_xy = θ₀N_xy realizes A8's ΣN(x)h_x.
- Universality also needs formation odds per beat proportional to N(x). A9 allows this, since F may depend on records.
- The angle must be set by records, not possibilities (S11). The sign of θ (A10's N3) decides whether the offset attracts or repels.

**S15. Global or local tick (ARGUED from S1–S14).** For pair-moving records, the beat is effectively global: flat and rate-locked. A5 already showed no global simultaneity is readable. What can vary by neighbourhood is the change per beat and the formation odds per beat.

N1 can be restated in two parts:
- **local:** handshake plus waiting;
- **global, a named conditional:** "the beat contains no waiting loop".

## 4. Checks

Every run used `run.sh`: `nice -n 10`, all four thread caps set to 1, and a 55 s alarm. All runs finished in at most 26 s with peak RSS at most 56 MB. Load average was about 3. Results are as reported in §3; key numbers:

| Script | Checks | Key results |
|---|---|---|
| `seam1d.py`, `seam1d_parity.py` | 1D rules H/K/P/Smu/Sum/R, θ ∈ {π/2, π/4, 0.3}, both sides, both seam parities | H/K/P: T = 0.000000, stuck weight < 2e-10. Smu = Sum: A→B 0.641/0.765 (θ = 0.3), 0.873/0.922 (π/4); B→A 0.875–0.967; 1.0 at π/2; reach 2. R: 0.222222 at π/2 (= 2/9); 0.18–0.36 otherwise; purity 0.06–0.36 |
| `selftimed1d.py` | Wait fronts, transmission, rate lock | Fronts at 1 site/round; T = 1 − 2e-10; late rates all 0.500; throttled depth = r |
| `a11walls.py`, `handwall.py` | A11 rigid walls and islands, H/K | Currents ±1 per side, net 0; islands (2s+1 out, 2s−1 in); handedness wall ±2 |
| `selftimed2d.py`, `selftimed_words.py`, `selftimed_probe.py` | Waiting deadlocks; 3D H cut | As in S8; 3D leak 0.0 for 15 slab/offset cases |
| `rate1d.py`, `rate1d_side.py` | 2:1 seam: matching, total-reflection windows, sidebands | As in S9 |
| `gradient1d.py` | Smooth rate gradient | As in S10 |
| `eventpaced1d.py`, `eventgated_shared.py` | E1/E2/E3 motion | As in S12 |
| `ns_eventpaced.py` | NS, exact 4-qubit linear algebra | 2.7e-16 / 0.257 / 0.096 |
| `anglelapse_and_phantom.py`, `anglelapse2.py` | Angle lapse; phantom-lock equality | As in S14 and S2 |

**Not run (suggested):**
- transmissive rules (Smu, R) in 2D and 3D with multi-sub-step offsets;
- words in which bonds appear more than once per period.

Both are small; extend `seam1d.py` with a y-direction of width 2–4.

## 5. Real-physics match

- **Observed redshift contradicts a beat-rate lapse.** Clocks at different heights keep sustained, different rates. Comparator, from memory, not re-verified: Pound–Rebka 1960; optical clocks about 33 cm apart (Chou et al. 2010). Light also crosses gravitational gradients without reflection. In these toys a beat-rate lapse is either impossible (waiting, S7) or opaque (rigid, S10). The rigid-clock reading is therefore falsified for any lapse carried by beat rates (ARGUED). A lapse carried by change per beat survives (S14).
- **Universality.** All clock types agree on redshift. In the angle-lapse package that requires every change and every formation odds per beat to scale with the same record-set N(x). Any record formed at a fixed chance per beat would be an absolute clock (A5 T2.6).
- **Comparators (not adopted; from memory).**
  - Marked graphs (Commoner–Holt–Even–Pnueli 1971): live iff every directed circuit carries a token, and token counts on a circuit are invariant. That is S8.
  - Equal long-run firing rates set by the slowest circuit (Ramamoorthy–Ho 1980). That is S7.
  - Asynchronous cellular automata reproducing synchronous ones (Nakamura 1974). That is S5–S6.
  - The 2D wall channels are analogs of counter-propagating, helical-like pairs; the handedness wall is an analog of a chiral domain wall (Rudner et al. 2013). These are 2D only; A11 D10 excludes such transfers in 3D under the 24 rotations.
- **What would falsify these results:**
  - an agreed-pairs, disjoint-sub-step rule that transmits across a straight mismatch;
  - a waiting loop that does not freeze;
  - a sustained rate difference between neighbours under fixed waiting words;
  - any observed reflection of light at gravitational gradients, which would favour rigid local beats.

## 6. Open edges and next steps

1. Transmissive seam rules in 2D and 3D, and multi-layer words (see §4).
2. Waiting with a timeout (skip a partner after m of your own events). This interpolates between lock and walls, but needs memory beyond Q2's snapshot or a Q1-type mark (A8 3.10).
3. A covariant rule with the gate angle and formation odds set by recorded neighbours, testing A8 universality and the attract-or-repel sign (N3).
4. Classifying which phase fields stay alive in 3D (every circuit carries a token), as a precise form of the N1 remnant.
5. A full toy with waiting beats, moving records and A9 instruments together.
6. Whether a "no waiting loop" condition can be derived or must remain a named conditional.

## 7. Plain-language summary

If every site keeps its own beat and two neighbours disagree about whose turn it is, the pair between them never acts. A moving record then bounces off that spot as if it hit a wall of records, and on a flat grid the wall even carries two little one-way streams going opposite ways. If instead each site waits for its partner before taking its turn, records move exactly as if one clock ran everything. But then no neighbourhood can stay faster or slower than another for long, and a ring of sites all waiting on each other stops the whole grid for good. Different speeds in different places work only in neat steps like 2 to 1, and smooth changes of speed turn into many walls that block motion. So moving records do not need one master clock, but they do need a beat that every neighbourhood shares in practice. If time is to pass differently in different places, as gravity seems to need, that difference fits better in how much changes on each shared beat, set by the records nearby, than in how often the beat comes.