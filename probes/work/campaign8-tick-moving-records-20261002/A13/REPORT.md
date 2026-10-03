I have everything needed: five checks ran within budget, apart from one recorded breach on the first run. Here is the report.

# A13 report: assembling I1–I6 into one toy model

Scratch directory: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A13/`. It holds the scripts `toy1d_assembled.py`, `walks.py`, `timecount.py`, `pacing_noise.py` and `bands_weight.py`, their outputs `out_*.txt`, and `run.sh`.

**Grades.**
- **EXACT**: proved, or exact arithmetic.
- **CHECKED**: a numeric check with a stated tolerance.
- **ARGUED**: reasoning without proof.
- **COMPARATOR**: literature, cited and not adopted.

**Status.**
- Everything below is a supplied toy. I1–I6 are instincts, not positions, and every new rule is a named conditional.
- A11 had scripts but no report when I read it; A12 did not exist. Neither is used.

---

## 1. Question

Suppose I1–I6 are taken together with:
- the axioms;
- the approved readings Q1–Q4, and Q7 read as "menus are set by records" (the A9 caveat);
- every result from lanes A1–A10.

Then:
1. What is the most coherent single toy model?
2. Does it satisfy (C) record odds consistent with possibilities, (L) locality, (NS) no-signalling over multi-tick histories, a quiet vacuum, one record per site, and permanence read as "never destroyed; relocates by re-forming"?
3. Under it, what does "time = accumulation of records" amount to, and what is a tick?
4. How do readable records and unrecorded possibilities divide the world?
5. What does it predict, where does it fail, and what must the owner decide?

## 2. Answer

**Conditional yes.** Consistency is EXACT by construction and CHECKED in a 1D instance; the physics claims are ARGUED.

**The model.** If I1–I6 are combined with the readings and with what the campaign forced, one coherent toy results:
- **Change.** It comes in strictly one-site pair steps, G(θ) = cos θ − i sin θ·SWAP. The partner sets cycle through a round: x-even, x-odd, y-even, y-odd, z-even, z-odd.
- **Empty space.** It is the *aligned emptiness*. The pair steps leave it exactly unchanged.
- **Formation.** Records form on record-free pairs with chance c·⟨P_singlet⟩, which is zero in empty space.
- **Records.** A record is never destroyed. Each tick it may re-form at its empty partner (option A), so its place is readable every tick.
- **Interference.** Everything that interferes stays unrecorded.

**Consistency.** The model meets C, L, NS over multi-tick histories, an exactly quiet vacuum, one record per site, and permanence as relocation.
- A distant choice moves B's 4-tick record history by TV ≤ 3.2e-16.
- Two nonlinear variants move it by 2e-3 to 3e-2.

**Time.** Under option A:
- Formation events, relocations included, grow without bound wherever moving records keep passing. The rate is s·u(1−u) per site per tick (CHECKED, 0.07837 vs 0.07836).
- Distinct records stay bounded at ≤ 1−ρ₀ per site (EXACT).
- Readable accumulated time in a fixed region is bounded by the region's size (EXACT).

**The tick.** The round's tick is global only up to relabelling, and its rate is unreadable. Experienced time is local and event-paced.

**Failures:**
- Readable records carry no momentum: zero drift, E[x²] → s·t/(1−s) (EXACT in the toy).
- Net chirality is doubled away (EXACT).
- The gravity-like slowing has β = 1/2 and γ = 0, no waves, and an unnatural weakness (from A6/A8).
- **Pacing fork (ARGUED):**
  - If the change steps on every tick, only record clocks slow, so slowing is not universal.
  - If the change waits for local events, heavy superpositions dephase within t_coh ≈ ħ²/(M²c⁴τ_e). At Planck-scale steps that is about 1 ns for atoms.
- The formation scale must be tiny (c ≲ 1e-43 at Planck ticks for one second of interference) (ARGUED).

It needs eight owner decisions (§6).

## 3. Derivation

### 3.1 The assembled model (task 1)

**Tags.**
- **[AX]**: axiom text.
- **[Qn]**: approved owner reading.
- **[N-…]**: new named conditional.
- "Forced" means a campaign result requires the rule once I2 and (C) are kept.

**M1 [AX].** Physical sites are the points of Z³, with nearest-neighbour adjacency, translations and proper cubic rotations. The grid has no edge; I6 is already axiom text.

**M2 [AX + Q1].** Each site's possibilities have presentation M₂(C). Sites with no record share their possibilities, and one site's possibilities can be linked with many others. When a record forms, the shared possibilities change at once to agree with it.

**M3 [AX].** Records form. A record locks exactly one admissible possibility. A site never carries more than one record. Only records are readable, by content alone.

**M4 [N-perm; needs the owner's wording].** A record is never destroyed. It may re-form at a neighbouring site that has no record; the site it leaves then has no record. This is the A3/A7 reading of "records are permanent".

**M5 [N-step; forced by A3 given I2 + C].**
- The change between records comes in ticks.
- In one tick it acts on disjoint pairs of neighbouring sites, with the same step on every pair: G(θ) = cos θ·1 − i sin θ·SWAP.
- Nothing reaches past a site's partner in one tick.
- G is the number-conserving pair step that commutes with every on-site rotation (A10 S1, coordinator-verified). So it is glued to rotations, as Q3 asks.

**M6 [N-cycle; A10's schedule-covariant reading].**
- The partner sets repeat in a fixed round: x-even, x-odd, y-even, y-odd, z-even, z-odd.
- "One fixed rule, covariant" is read as: each lattice symmetry maps the round to itself, up to which tick is called first. Once records interact, odd rotations must also reverse the round.
- Supplied choices:
  - N1: a shared round phase;
  - N2: the word;
  - N3: one angle;
  - N4 (optional): a sign pattern, for isotropic light-like motion;
  - N5: a sublattice labelling.

**M7 [N-form; the form is forced by A9 Theorems 1–2; the weight is a conditional].** On each tick, every pair with no record carries one local instrument:
- a record forms with chance tr(Fρ), where F = c·P_singlet(pair) and 0 < c ≤ 1;
- the lock odds are the ones after the formation update (½ and ½ in the singlet, which is where Q4's equal odds appear);
- a tick with no record reshapes the possibilities by √(1−F);
- the menu's axis is set by records (Q7 as corrected by A9), never by unrecorded possibilities.

**M8 [N-reloc; option A, forced by A7 given readable places].**
- On each tick, a pair with exactly one record carries the relocation instrument. After the pair step, the record re-forms at its own site or at its partner, with the odds the step gives, and the possibilities change at once to agree (M2).
- A pair with two records does nothing.
- A record never enters a recorded site.
- So a record's place is readable at every tick.

**M9 [N-quiet; forced by A4, A6, A9 for a grid that neither freezes nor screens].**
- Empty space is the aligned emptiness: every unrecorded site holds |n⟩. The law does not fix n.
- M5 leaves it unchanged and F annihilates it, so empty space never forms records. This answers the open question: no.

**M10 [Q2, re-read].**
- The film never ends.
- "Evolves continuously" is read as "without end", not "smoothly": A3 shows smooth change cannot keep one-site moves consistent.
- The rule acts locally on the snapshot (records plus shared possibilities) and on the round phase.

**M11 [N-time; decision D5].** Time at a place is the number of formation events there, relocations included. The alternative, counting distinct records, is treated in §3.3.

**M12 [N-pace; decision D6].** The change either advances on every round tick, or only when a record event happens in the pair's neighbourhood.

**M13 [N-hold; optional, decision D8; A8].** A record that touches a held record of agreeing content becomes held: its menu is {stay} from then on. Held status is visible in the conditions.

**Not used:**
- triggered formation;
- net conveyors (A1 D12 excludes them);
- continuous change (A3);
- guided (R3) records (A7);
- own-state menus (A9; they signal maximally).

**Why these choices fit together (EXACT).**
- **The round fixes only aligned states.** For generic θ, a state that every pair step leaves unchanged up to phase must be an eigenstate of each nearest-neighbour SWAP. Eigenvalue −1 on two overlapping bonds would make three qubits fully antisymmetric, which is impossible. So the state is symmetric under every swap: the aligned family. On infinite Z³ these are mixtures of |n⟩^⊗ (de Finetti, COMPARATOR).
- **A9 n3 points to the same family.** For pair-local, rotation-invariant weights, the quiet emptiness must be aligned.
- **Quiet and Q4 together.** The rotation-averaged aligned emptiness has single-site odds ½, matching Q4; quietness then requires sharing.

**How each instinct lives in the model.**

| Instinct | In the model | Status |
|---|---|---|
| I1: set ticks, same-tick formations | Formation only at round ticks, on disjoint pairs, so any number per tick | Kept. Global vs local is unreadable (A5); experienced tick is local (§3.3) |
| I2: ≤ 1 site per tick, site reuse | Relocation only to the current partner; one formation per site per tick; a vacated site is cut to the emptiness, so it is reusable and does not breed | Kept; forces strict pair steps (A3) |
| I3: move odds like formation, collisions | Relocation = re-formation with the step's odds. Collisions never arise, since each site has one partner per tick | Kept in spirit. Literal independent proposals are replaced (A3: TV up to 0.50) |
| I4: flow, not swap | Content moves along counter-passing sublattice lanes; net flow zero | Standing conveyor excluded (A1 D12, EXACT) |
| I5: full region as black hole | Full region: no change, formation or relocation, so time stops | EXACT. Persistence needs M13 |
| I6: infinite grid | Gauss law and 1/r (A6); dilution of finite record sets (§3.3) | Kept |
| Open question | Empty space never forms records | Answered no, conditional on M9 |

**Minimal instance used for the checks (supplied toy).**
- 1D open chain: N = 8 for the main run, N = 6 for the cone control.
- The round in 1D is a brickwork: even bonds, then odd bonds.
- Emptiness |0…0⟩. The axis z stands in for a recorded frame; record content is |1⟩.
- Parameters θ = 0.6 (s = sin²θ = 0.3188), c = 0.5.
- **Relocation (record at i):** K_stay = |1⟩⟨1|_i, K_move = |0⟩⟨0|_i.
- **Formation:** K_i = √c·|10⟩⟨10|P_s, K_j = √c·|01⟩⟨01|P_s, K_null = √(1−cP_s).
- 3D: the six-layer round, for single records and for a classical gas of option-A records.

### 3.2 Consistency (task 2)

**S1 (C), EXACT.**
- Every record event is an outcome of a local instrument, with odds tr(E_k ρ) on the snapshot it acts on.
- The relocation odds are the formation odds after the step, ‖Π_y G ψ‖². This is A3's R1 rule: unique, and automatically consistent.
- CHECKED:
  - A lone record's position law after 6 ticks equals the classical chain with kernel |G|² to 4.4e-16.
  - Records agree with possibilities in every branch (worst disagreement 0).

**S2 (L), EXACT.**
- G and every instrument act on one pair.
- Which instrument applies depends only on that pair's record labels.
- Reach is one site per tick, giving the strict cone (A5 T1.1).

**S3 (NS over multi-tick histories), EXACT.**
- The history is a network of pair instruments with local classical feed-forward; record labels move ≤ 1 site per tick.
- Summing A's unread outcomes gives a channel on A's pairs. That channel commutes with everything in B's backward cone, and nothing there depends on A's labels.
- So B's joint record history inside the cone ignores A's choice, for any number of ticks (A5 T1.2; COMPARATOR: causal-operation lemma, Beckman–Gottesman–Nielsen–Preskill 2001).
- A9's conditions are what make each step linear: a linear chance, post-update lock odds, the no-record reshaping, and menus set by records.
- A7's obstruction does not arise. It needs a readable place whose possibilities stay uncut and linked. Under M2 and M8 a recorded site is always cut to its content, and unrecorded possibilities are never readable (A7 Step 8a).
- CHECKED (A and B Bell-linked; A registers at tick 1 or follows M7):
  - B's history: TV ≤ 3.2e-16 for 1–4 ticks.
  - Variant without the no-record reshaping: 2.6e-3, 1.2e-2, 3.3e-2, 3.3e-2.
  - "Product" variant (chance times raw lock odds): 2.0e-3, 1.1e-2, 1.3e-2, 1.45e-2.
  - Cone control: ≤ 2.9e-16 for t ≤ 3; 3.0e-3 once A's cone reaches B at tick 4.

**S4 (quiet vacuum), EXACT.**
- SWAP|nn⟩ = |nn⟩, so G|nn⟩ = e^{−iθ}|nn⟩.
- P_s|nn⟩ = 0, so F annihilates the emptiness and √(1−F) fixes it.
- The vacuum rate is exactly 0 for every n, with no tuning.
- A lone record never seeds others: the vacated site is cut to the emptiness, so no record-free pair gains a singlet part. CHECKED: 0. This avoids A6's breeding failure.
- Contrast: the half-filled sea is not quiet (A9: ≥ 5.0e-6 per tick for a rank-1 weight, 0.012 energy-based). It freezes in about 1/ε ticks (A4).

**S5 (one record per site), EXACT.** M7 forms at most one record per record-free pair per tick, and M8 never enters a recorded site.

**S6 (permanence as relocation), EXACT.** No instrument removes a record, and M8 keeps both count and content. CHECKED: in every branch, number of records = initial + formations.

**S7 (schedule independence), EXACT.**
- Instruments within a tick sit on disjoint pairs and commute, so A5 T3.1 applies.
- A9's open problem of overlapping, non-commuting stars does not arise.

**S8 (what is given up), EXACT consequences rather than inconsistencies.**
- Campaign-7 sentence 2: "continuous" and "keeps locked possibilities" (A3 Step 13; A8 B0).
- Per-tick covariance (A3 Step 10).
- Q2's "snapshot alone": the round phase is an extra input.

### 3.3 Time counting, and what a tick is (task 3)

**Counts.** Per site x and window [0,t):
- F_x: new records formed at x;
- A_x: relocation arrivals at x;
- E_x = F_x + A_x: formation events, since under option A every arrival is a formation.

**T1 (distinct records are bounded), EXACT.**
- Let H_R be the number of record-free sites in region R. Then F_R = H_R(0) − H_R(t) + Out_R − In_R ≤ |R| + Out_R − In_R.
- Under invariance by 2-translations, every unit cell has the same expected net inflow, and these sum to zero. So E[F per site over all time] ≤ 1−ρ₀ (A4 3.1b, A6 3.2).
- CHECKED: 0.8047 = 1−ρ₀ at saturation.

**T2 (formation events are unbounded), EXACT for the mean.**
- The product measure at density u is invariant: each pair maps 10 ↔ 01 with odds s and fixes 00 and 11.
- So E[A_x per tick] = s·u(1−u), and E[E_x(0,t)] = s·u(1−u)·t → ∞.
- CHECKED (3D, L = 16, 3000 ticks):
  - rate 0.07837 vs 0.07836;
  - the smallest per-site count grew 23 → 52 → 116 → 191;
  - every site had arrivals in the last 1000 ticks.
- That every site's count diverges is ARGUED (ergodicity).

**T3 (dilution caveat), EXACT; COMPARATOR Pólya.** "Unbounded locally" needs a positive density of moving records. A finite set of records on infinite Z³ dilutes: each walk is transient, so each site sees finitely many events almost surely.

**T4 (readability), EXACT.**
- E_x is not stored. The snapshot holds current records only, and contents never change.
- So readable accumulated time in a fixed region is ≤ |R| in every reading.
- It can grow without bound only in a growing structure: a front, or a swallowing clump fed from the infinite grid (A6 3.10).
- "Stays" must not count. Otherwise every record adds one unit per tick, and time collapses to the round count.

**T5 (the tick), EXACT given A5.**
- The *round tick* is an opportunity: records form and relocate only on it (I1).
  - Whether it is global or local, and what its rate is, has no readable content (A5 T3.1, T3.3).
  - It needs a shared phase (N1); mismatches are seams.
- The *experienced tick* is one formation event at a place. It is local and influenced, with rate s·u(1−u) per round tick.
- So I1's open question resolves this way: "global" and "constant" hold by convention only; time is the event count, local and influenced.
- What remains open is M12: does the change itself wait for events?

**T6 (I5 and the void), EXACT.**
- Event time stops in full regions (no gaps) and in empty regions (no records).
- It runs fastest at half filling.
- A full region also has no change at all (A8 B1, A10 S14).

**T7 (link to the move clock), EXACT.** Under option A, A6's move-event clock *is* the owner's accumulation of records, read as formation events.

### 3.4 The two kinds of things (task 4)

| | Readable records (option A) | Unrecorded possibilities (option B) |
|---|---|---|
| Readable | Place and content, every tick | Never; only through records formed from them |
| Motion | Persistent random walk: E[x_T²] = Ts + 2Σ_{k=1}^{T−1}(T−k)s²(2s−1)^{k−1} → sT/(1−s) | Ballistic; ⟨x²⟩/t² constant (0.0447 to 0.6377 for θ = 0.3 to 1.2) |
| Interference | None across ticks | Yes |
| Momentum | None: offset → s/(2(1−s)), no drift | Group velocity; low-speed Lorentz kinematics (A5 T2) |
| Clock | Move events (M11) | The change's own phase |

**Persistent walk (EXACT).**
- A move lands on the opposite parity, whose next partner on that axis lies in the same direction. A stay leaves the partner on the opposite side.
- So moves continue a direction and stays reverse it.
- Formula and 3D factorization CHECKED to ≤ 4e-12 and 3.6e-13.

**Mapping (ARGUED):**
- Interfering particles must be unrecorded between registrations (A7, EXACT).
- Tracks and detector clicks are *fresh, stationary* records formed from an unrecorded mover: accumulated records. This refines A7's "tracks behave like (A)": an option-A record would wander off the track.
- Option-A wanderers cannot form coasting bodies. They fit A6/A8's clock carriers and the held records of clumps.
- Ordinary bodies must therefore be unrecorded content kept effectively definite by records formed in their surroundings, at the surroundings' resolution (COMPARATOR: environmental decoherence).

**Registration smallness.**
- On the round over the aligned emptiness, the soft branch has quasi-energy 0 at K = 0 and rises as (tan θ/4)K². Its registration chance is ∝ K² (CHECKED: coefficient 0.1710).
- The linear crossing sits at quasi-energy 2θ, K = π, with chance c/2 per tick (CHECKED).
- So light-like content is registered fastest (EXACT for this weight).
- At Planck ticks, one second of interference needs c ≲ 1e-43. Matter that stays unrecorded for the age of the universe needs c ≲ 1e-61 (ARGUED).

### 3.5 Predictions and failures (task 5)

| Item | Toy prediction | Grade | Verdict |
|---|---|---|---|
| Clocks | Steady move clock at s·u(1−u); formation-only clocks bounded; readable clocks are accumulators | EXACT/CHECKED | Matches in kind |
| Gravity-like slowing | Around a net sink (M13), in the quiet void, with u∞ < 1/2: Φ ≤ 0, Gauss law, exact 1/r. The mean-density equation E[n_i′] = (1−s)E[n_i] + sE[n_j] is linear and closed, so A6 carries over. Additivity needs sparse matter (A8) | EXACT (mean field); CHECKED in A6/A8 | Partial |
| Universality | Change paced by the round: only record clocks slow. Change paced by events: universal, but the void has no change, the trigger needs one tick of memory (A8 3.10), and V = \|1−p+pe^{iω}\|^{2t}, giving t_coh = ħ²/(τ_e M²c⁴): 31 s (electron), 9 μs (neutron), 0.9 ns (100 amu), 15 fs (25 kDa) at τ_e = t_P | Algebra EXACT; identification ARGUED | Both sides fail a known test |
| Black-hole-like regions | Full region frozen (EXACT). Without M13, jams leak; A4 predicts lifetime ∝ N^{2/3}, the 3D check gave N^1.06 (unsettled); opposite trend to Hawking. With M13 and t = qN/4πR ≳ 1: charge ∝ radius, surface clock → 0, runaway growth. Unrecorded content is turned back at the wall, not absorbed | EXACT/ARGUED | Analog only |
| Relativity at low speed | 1D: the round with θ_e = π/2, θ_o = π/2 − m is A5's Dirac step; departures are quadratic and mass-suppressed. 3D plain round: eight diagonal sheets. Isotropy needs N4 signs (two Dirac cones). C3-symmetric words split at linear order (GRB-disfavoured). Mass breaks unit translations. Records: none | EXACT/CHECKED | Partial |
| Strict cone | One site per tick, exactly | EXACT | Unobservable at Planck scale |
| Chirality | Strictly range-1 steps give W3 = 0, so doubling persists: 2L+2R, and every available mass gaps both copies | EXACT | Fails, unless many-body structure, recorded-region edges (A11), or faint reach help |
| β = 1/2 | N = 1 − U gives β = 1/2; γ = 0 | EXACT (mean field) | Fails (perihelion, Cassini) |
| No waves | The clock field diffuses; 1/r is established only to ~5e-5 m at Planck steps | ARGUED | Fails (GW170817) |
| Weakness | q ≈ 1e-18 against O(1) odds; plus the small c | ARGUED | Not natural |
| Soft ripples | The aligned emptiness's ripples are quadratic (z = 2) | EXACT | Light must be the crossing content |

## 4. Checks

All runs used `nice -n 10`, the four thread caps set to 1, and a 60 s alarm, via `run.sh`.

| Script | What it checks | Result | Time, memory |
|---|---|---|---|
| `toy1d_assembled.py` | C, NS with a 4-tick history, two controls, cone control, quiet vacuum, permanence, lone record | As in S1–S6: TV ≤ 3.2e-16; controls 2e-3 to 3.3e-2; cone 3.0e-3; vacuum formation probability 0; branch law equals \|G\|² chain to 4.4e-16 | 1.5 s, 90 MB |
| `walks.py` | Record walk vs unrecorded spread, 1D and 3D | Formula ≤ 4.1e-12; E[x²]/T at T = 400: 0.4678 vs s/(1−s) = 0.4680 (θ = 0.6); 3D factorization 3.6e-13 | 0.35 s, 74 MB |
| `timecount.py` | Event time vs distinct records | 0.07837 vs 0.07836. Noisy illustration: C1 = 0.8047 = 1−ρ₀; 0 events per site in ticks 2001–3000 | 0.4 s, 35 MB |
| `pacing_noise.py` | Two-clock visibility, physical scale | Exact vs Monte Carlo 0.18610 vs 0.18598 (s.e. 0.0022); t_coh table as in §3.5 | 0.14 s, 44 MB |
| `bands_weight.py` | Branches and registration weight | Soft-branch coefficient 0.1710 = tan θ/4; crossing phase 1.2 = 2θ; weight 0.5 | 0.06 s, 27 MB |

**Budget breach.** The first `toy1d_assembled.py` run included a 6-tick extension. It peaked at 497 MB for about 5 s, over the 300 MB cap, and was replaced by the smaller cone control.

**Should be run (bigger, not run):**
1. An event-paced 1D Dirac round with random local gate firing, to measure dephasing against the formula.
2. The 3D gas with M13 capture on the round's kernel.
3. A 2D version of the consistency toy in a one-excitation-per-region sector.

## 5. Real-physics match

Every physical number assumes ticks near the Planck time, and that toy excitations stand for particles. The axioms fix neither.

**Matches:**
- no-signalling;
- a quiet vacuum without tuning;
- a strict cone;
- low-speed relativity for unrecorded content;
- the sign and 1/r of gravity-like slowing.

**Falsifiers and conflicts:**
- **Chirality:** weak interactions are net-chiral.
- **Post-Newtonian:** β and γ from perihelion, lunar laser ranging and Cassini.
- **Waves:** GW170817.
- **Redshift universality**, if the round paces the change.
- **Interference times**, if events pace the change (comparators from memory, unverified): neutron interferometers run tens of μs, half-metre atom interferometers about 2 s, and 25 kDa molecules for milliseconds.
- **Bounded registration:** collapse-model-style limits on how often matter is registered.

**COMPARATORS (not adopted):**
- Kogut–Susskind; Nielsen–Ninomiya.
- GRW/CSL. Formation as a linear-rate "flash" has this structure, but the localization here is lattice-scale.
- Milburn 1991. There, global random steps dephase only energy differences; local pacing is stronger.
- Pólya; Beckman–Gottesman–Nielsen–Preskill; Joos–Zeh and Zurek.

## 6. Owner decisions, open edges, next steps

**Decisions.**

**D1. May a record move ("never destroyed; may re-form at an empty neighbouring spot")?**
- **Yes:** there is a steady local clock, and mixed regions never finish.
- **No:** nothing moves, each spot has at most one event ever, and every region ends.

**D2. Is a moving record's place readable at every step?**
- **Yes:** records are classical dust, with no interference and no momentum.
- **Only when a new formation registers it:** interference survives, but Record and Qualification wording must allow a record without a readable place.
- Readable and uncut is not an option: it signals (A7).

**D3. Do you accept strict steps on a fixed round of partner directions, read as covariant over a full round?**
- **Yes:** lone records can move, and the speed limit is exact. The cost is a supplied phase and choices of word and angle. A sub-choice: a sign pattern buys equal speeds in all directions, at the price of re-phasing the shared possibilities.
- **No:** a lone record never moves (A3 Step 10). Smooth change also breaks consistency.

**D4. Does empty space ever form records on its own?**
- **Never:** the emptiness must be aligned, and the half-filled-sea vacuum ruling must change.
- **At some rate:** everything freezes in about 1/rate ticks. Keeping the sea needs a rate ≲ 1e-61 per tick.

**D5. Does time count every formation, or only new records?**
- **Every formation:** time is unbounded wherever records move, slows near swallowing clumps, and stops in full or empty regions.
- **Only new records:** about one per spot per region, ever.

**D6. Does the change wait for local record events?**
- **No:** universality is lost.
- **Yes:** clocks slow universally, but the void has no change and heavy interference washes out (~1 ns for atoms at Planck steps).

**D7. Strictly one site per step, or faint longer reach?**
- **Strict:** handedness stays balanced.
- **Faint reach:** handedness can tip, but I2 holds only approximately and consistency is lost.

**D8. Can a record tell a held neighbour from a wandering one?**
- **Yes:** swallowing clumps, 1/r slowing, and black-hole-like interiors.
- **No:** clumps melt and leave no field.

**Confirmations (forced, not choices):**
- menus are set by records;
- the formation chance is linear;
- lock odds are taken after the update;
- a tick with no record still reshapes the possibilities;
- no standing conveyor;
- Q2's "continuously" means "without end".

**Open edges:**
- **E1. Records with general content.** When a record's content is not orthogonal to its partner's possibilities, relocation needs a rule. Candidate: a content-carrying exchange with odds s, which equals M8 whenever the two are orthogonal.
- **E2. Menus with no recorded neighbour.** The toy fixes the axis.
- **E3. A weight that is quiet but small on crossing content.** This bears on the small c, and A12 may bear on it.
- **E4. Locked, sub-Poissonian pacing.** It would need roughly 1e9 noise suppression.
- **E5. Chirality from recorded-region edges** (A11).
- **E6. Held status from the snapshot** (A8).

## 7. Plain-language summary

Your ideas, put together with the campaign's results, give one consistent toy:
- Things change in small steps on a fixed round of neighbour pairs.
- Empty space is a stretch of agreeing possibilities that never forms records.
- Records form where neighbours disagree.
- A record never disappears, but at each step it may re-form next door, so its place can always be read.

In this toy nothing far away can be learned early, nothing travels faster than one spot per step, and records are never doubled or lost. Readable records behave like dust: they jiggle and carry no momentum. Everything that interferes stays unrecorded between formations. If every formation counts, moves included, time runs forever where records move through gaps and slows near clumps that swallow them, but it stops in full and in empty regions. The toy still fails on handedness, and on the size, spread and weakness of its gravity-like slowing. Making all clocks slow alike would also wash out the interference of atoms, unless steps are far shorter than the Planck time.

**One-page owner summary.**

- **The grid and the steps.** The grid has no edge. Spots without a record share their possibilities. Change happens in small steps. Each step pairs every spot with one neighbour, and the pairings take turns: east–west, north–south, up–down. Within a pair the possibilities partly trade places, and nothing reaches further.

- **Empty space.** All possibilities agree with their neighbours. The steps leave it exactly as it is, so no record ever forms there.

- **Records.** A record forms where partners disagree, with a chance that is a straight average over the possibilities. When it forms, the shared possibilities change at once to agree with it, and even a step with no record nudges them a little. A record is never destroyed. At each step it may re-form at an empty partner spot; each move is a new formation, so its place can be read every step.

- **Two kinds of things.** Records are dust: they spread slowly, never interfere, and keep no direction of travel. Electrons, atoms and light are possibilities moving between formations. When one is registered, the result is a fresh record that stays put; a detector track is a line of such records.

- **Time.**
  - Counting every formation, moves included: time runs without end wherever records move through gaps, slows where they thin out, and stops in full or empty regions.
  - Counting only new records: each region ages by about one record per spot.
  - The round of pairings is not time. No record can tell one universal beat from many local ones.

- **What works:**
  - an exact speed limit;
  - no faraway influence;
  - quiet empty space;
  - records never doubled or lost;
  - slow-speed relativity for unrecorded things (equal in all directions only with a sign pattern);
  - clocks that slow as one over distance near swallowing clumps.

- **What fails:**
  - left- and right-handed things always come in equal amounts;
  - the slowing's next-order size is half of Einstein's, it spreads rather than travelling as waves, and its weakness must be put in by hand;
  - moving records carry no momentum;
  - universal clock slowing would wash out atom interference within about a billionth of a second;
  - records must form extremely rarely for interference to last.

- **Decisions for you:** (1) may records move; (2) are they readable every step; (3) steps on a round of pairings; (4) which emptiness; (5) what time counts; (6) does change wait for record events; (7) strict one-spot reach; (8) can records tell held neighbours from wanderers.