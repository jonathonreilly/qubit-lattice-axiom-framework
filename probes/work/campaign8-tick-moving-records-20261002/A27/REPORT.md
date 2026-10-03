I have everything I need: nine checks ran, each under 3 s and 170 MB. The report follows.

# A27 report: Option R (ticks for records, smooth change for possibilities)

Scratch directory: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A27/`. It holds scripts `c1`–`c9`, outputs `out_*.txt`, timings `time_*.txt` and `run.sh`. There were no git operations and no repo edits. Every model below is a supplied toy, and every rule is a named conditional, not framework content.

## 1. Question

Is Option R a consistent single package? The candidate:
- **(R-a)** Records form and move only on ticks, at most one site per tick, by their own irreversible re-formation step (option A).
- **(R-b)** Between ticks the shared possibilities change smoothly under a covariant, homogeneous, star-local generator that keeps locked possibilities.
- **(R-c)** All odds come from linear local instruments, and menus are set by records.

Does it get around Theorem N, the time-doubler problem and A3's consistency limit, while keeping I2, no-signalling and Q3? What exactly does it cost?

## 2. Answer

**Conditional yes.** The construction is EXACT, the toys are CHECKED, and the physics readings are ARGUED.

**Where it holds.** Read R-a this way:
- the change holds each record's locked possibility fixed between ticks ("compression"; this is what "kept" amounts to for a smooth change, and it is also the limit of re-cutting at very frequent ticks);
- a record relocates by its own swap step: it trades places with one empty neighbour's possibilities, with odds linear in that neighbour's possibilities;
- clashes are settled by a claim rule.

Then Option R holds together:
- I2 is exact for records, and two records never share a site.
- The step is exactly covariant under all 24 turns and is not glued to the grid (Q3).
- There is no nonlinear (instant) signalling.
- Theorem N does not apply: the change is not nearest-neighbour per tick, yet it moves content.
- A3's limit does not apply, because records do not ride the possibilities.
- There is no time doubler while the change per tick stays below an aliasing bound.

**Where it fails.** Suppose instead R-a means that the record's own content is carried by the smooth change and re-cut each tick. Then:
- no complete instrument confined to the star keeps the record agreeing with its content (EXACT);
- keeping one site per tick requires pulling content back from beyond the star;
- frequent ticks freeze the record (Zeno).

**Costs.**
- The change has no exact speed limit. Influence outside the one-site-per-tick cone is exponentially small only if the change's own top speed is below one site per tick (6Jτ < 1 in the 3D hopping toy).
- Records are fixed weights and walls for the possibilities, and they wander as dust.
- A step whose odds depend on the neighbours slightly cuts them every tick.
- Records sit quietly in an aligned emptiness only if their content lies along its axis.
- The change per tick (the "dose") becomes a new readable parameter.
- Overlapping formation stars need an ordering rule.
- Handedness still comes doubled, and the stepped quasi-local walks that carry net handedness cannot arise.

## 3. Derivation

**Setup (supplied toy).**
- **Snapshot:** records (a site plus a pure content |r_x⟩) and shared possibilities ρ. Recorded sites hold |r_x⟩.
- **Between ticks:** ρ → e^{−iH_R s} ρ e^{iH_R s}, with H_R = Q_R H Q_R, where Q_R projects each recorded site onto its content.
- **H:** covariant and star-local. The example is Heisenberg, J Σ SWAP.
- **Ticks:** every τ. The dose per tick is x = 2Jτ.
- **At ticks:** local linear instruments act: formation as in A9 Theorems 1–2, moves, and no-record updates.

### Step 1. What "kept" must mean (EXACT; CHECKED)

**(a) Compression makes the record a one-site field.** By A8 B0, a fixed two-site change that keeps every locked content cannot interact, so "kept" means compression. The compressed term on a neighbour y is ⟨r|_x h_{xy} |r⟩_x = a + b·n_r·σ_y; covariance leaves only that form. For SWAP it is |r⟩⟨r|_y.
- CHECKED: ‖QHQ − Q(H_rest + J·field)Q‖ = 2.3e-15.
- The compressed generator never puts content into a recorded site, so records are walls (EXACT; see the c2 run).

**(b) Compression is the limit of re-cutting at fine ticks.**
- (Q e^{−iHτ} Q)^n → e^{−iQHQ t} as n = t/τ → ∞ (comparator: quantum Zeno dynamics, Facchi–Pascazio).
- CHECKED, N = 7, t = 1: distance 4.48e-2, 4.47e-3, 4.47e-4, 4.47e-5 for n = 10, 10², 10³, 10⁴.
- One-tick leak = τ²⟨H(1−Q)H⟩: 1.0836e-4 against 1.0832e-4 at τ = 0.01.

### Step 2. The "carried" reading of R-a fails star-locality

**Lemma C (EXACT).** Number-conserving toy:
- The record's content is one excitation over an emptiness, cut to site x at the start of the tick.
- w_out = ‖Π_{beyond star} U|x⟩‖² is the weight the change carries past the star.
- Take any complete instrument whose Kraus operators act only on star(x).

Then the post-tick states carry total weight exactly w_out with the content outside the star while the record sits inside it, so the record and its content disagree.

*Proof.* Write U|x⟩ = |a⟩_star|0⟩_out + |0⟩_star|χ⟩_out. Each Kraus operator acts as k⊗1 and maps the second part to (k|0⟩)⊗|χ⟩. That part is orthogonal to the image of the first (one more excitation outside), and Σ_k ‖k|0⟩‖² = 1. ∎

Combined with A3 Step 10: a carried record under a change that treats every site and turn alike either never moves (w_out = 0 forces the trivial tick) or leaves the star. EXACT within the number-conserving class.

**Size of the leak (EXACT, Bessel functions).**

| Jτ | 1D: 1 − J0² − 2J1² | 3D |
|---|---|---|
| 0.1 | 5.0e-5 | 1.3e-3 |
| 0.5 | 2.7e-2 | 0.40 |

For small doses the 3D leak is ≈ 13.5(Jτ)⁴.

**Repairs and their costs.**
- **Renormalized star odds**, tr(Π_y ρ)/tr(Π_star ρ), are not affine. With σ₁ = |x+1⟩ and σ₂ = (|x−1⟩+|x+2⟩)/√2:
  - steered average: (½, 0, ½);
  - unsteered mixture: (⅓, 0, ⅔);
  - TV = 1/6, EXACT.

  By A9 Theorem 1 this signals once the carried content can be linked to distant possibilities. (The free one-excitation toy cannot link it; an interacting change can.)
- **The linear completion is "clip".** The record steps one site toward its content, and the content is pulled back with Kraus operators |x±1⟩⟨z|.
  - It is complete and linear, but its reach is unbounded, weighted by the tails.
  - With several excitations, "the record's content" is not even identifiable (ARGUED).

**Zeno freezing (EXACT formula; CHECKED).**
- Under clip, the variance per tick is 1 − J0(2Jτ)². At fixed change-time T it is (T/τ)(1 − J0²) ≈ 2J²τT → 0 as τ → 0.
- Exact chain check over 10 ticks matches the formula to 5 decimals: 0.19851, 4.14473, 8.13309, 9.32373.
- At T = 4, uncut content spreads with variance 32; the clipped record reaches:

| τ | Record variance |
|---|---|
| 0.01 | 0.080 |
| 0.1 | 0.79 |
| 0.82 | 3.97 |
| 2.0 | 1.68 |

- Best mobility is D = 0.4957J at Jτ = 0.820. There, 15.5% of the content is pulled back from beyond the star each tick (1.3% from beyond 2 sites).
- The record is dust (variance grows linearly in ticks).

### Step 3. The compressed reading: a swap-relocation step "SW" (EXACT by construction)

**Definition.** For a record at x with content r and empty neighbours y:
- K_y = √(c/6) · SWAP_{xy} · √W_y
- K_stay = √(1 − (c/6)Σ_y W_y)

Three covariant choices of W:
- **content:** W = β + (α−β)|r⟩⟨r|_y;
- **blind:** W = 1;
- **activity:** W_y = the average singlet projector between y and its other neighbours. It vanishes on aligned states; range 2.

**Properties.**
- Linear (odds (c/6)·tr(W_y ρ)), complete, local, and at most one site per tick.
- Content is kept, and the record's site is pure at every tick, so A7's obstruction does not arise.
- Covariant under the 24 soldered turns.
- **Not glued:** it is also invariant under turning space alone and under turning the possibilities alone.
- **Q3:** the lockable possibility is the record's own content, not a grid direction. W-content is literally "the site's possibilities relative to the menu {r}".

**CHECKED on a 3D star (7 qubits).**

| Check | SW | D23 (A1 lock-and-move) |
|---|---|---|
| Completeness | 3.2e-15 | 2.2e-16 |
| 24-turn covariance | 3.4e-15 | 1.8e-15 |
| Turning space alone | 1.9e-15 | 0.58 (glued) |
| Turning possibilities alone | 4.7e-15 | 0.49 (glued) |
| Odds | (c/6)tr(W ρ_y), error 6e-17 | (1+n_r·v)/6 whatever the neighbours hold |

SW also addresses every A21 C23 complaint about D23:
- it has a stay outcome;
- it does not renew content;
- its odds can follow the neighbours;
- it makes no handedness claim.

### Step 4. Back-action and the quiet emptiness (EXACT; CHECKED)

**Coherence loss.** Take a neighbour's two components along W's eigenbasis and track the possibility wherever it ends. Its coherence is multiplied by:

f = (c/6)√(αβ) + (c/6)S + √((1 − (c/6)(S+α))(1 − (c/6)(S+β))) = 1 − (c/12)(√α − √β)² + O(c²)

The first-order loss is independent of the other neighbours, and it is zero exactly when W does not distinguish the neighbour's possibilities.

| α, β | c | Kept (neighbours empty) | Kept (neighbours random) | Formula / exact |
|---|---|---|---|---|
| 0.15, 0.85 | 0.06 | 0.998564 | 0.998564 | 0.998571 (first order) |
| 0.15, 0.85 | 0.6 | 0.98454 | 0.98477 | — |
| 0, 1 | 0.6 | 0.947214 | — | 0.5 + √0.2, exact |
| α = β | any | 1.000000 | 1.000000 | 1 |

So odds that depend on the neighbours cost back-action on them. This trade-off is EXACT.

**Quiet emptiness.**
- The aligned emptiness |n⟩ is left alone by the compressed field a + b·n_r·σ only if n_r = ±n (EXACT).
- SW-content also disturbs it unless n_r = ±n or α = β.
- SW-blind and SW-activity never disturb it.
- CHECKED, generic n: field 1.6e-2 at τ = 0.3; SW-content 1.9e-2; blind and activity ≤ 3e-16. For n = r or n = r⊥, all are ≤ 2e-15.

### Step 5. Several records: the claim rule "CL" (EXACT by construction; CHECKED)

**Stage 1.** Each empty site y next to records applies one instrument on itself, with outcomes:
- "claims record i", E_i = (c/z)·W^{(i)}_y;
- "claims nobody".

**Stage 2.** A record claimed by several sites picks one uniformly (classical post-processing). Then the SWAP is applied.

**Properties.**
- Linear, complete, strictly range 2, and covariant.
- Exclusion is exact: each site takes at most one record, and each record goes to at most one site. A site vacated this tick is reused only next tick.
- I3 holds exactly at a contested site: P(i | y taken) = w_i/Σw.

**Literal I3 signals.** Independent proposals with a relative-odds collision have joint odds containing products of linear functionals. These are quadratic, so the rule signals (EXACT via A9 Theorem 1).

**CHECKED (1D; the contested site is Bell-linked to distant b; b's choice is no record, menu Z or menu X):**

| Rule | Total probability | Double occupancy | TV across b's choices |
|---|---|---|---|
| CL | 1 − 1e-15 | 0 | 2.8e-17 to 2.0e-16 |
| Literal I3 (c = 0.9) | 1 | — | 3.5e-3 (none/Z), 7.1e-3 (Z/X) |

### Step 6. Theorem N (EXACT; CHECKED)

- Theorem N's hypothesis α(A_x) ⊆ A_{N̄(x)} fails for e^{−iHτ}.
- Corollary: for a non-trivial covariant H, the instants τ at which the change has nearest-neighbour reach are isolated, and the change is the identity there. This uses Theorem N plus analyticity of finite-range dynamics in τ (comparator: Bratteli–Robinson).
- CHECKED, 1D Heisenberg, N = 9: the weight of e^{iHτ}σ^z e^{−iHτ} outside the 3-site window is ≈ 2τ⁴ (ratio 1.9992 at τ = 0.02; 0.634 total at τ = 1).
- The change is exactly covariant at every instant, with no schedule, sublattice or partner pattern.
- It moves content: magnon speed 2J sin k (EXACT). CHECKED: under the compressed dynamics, content spreads through an unrecorded segment and none crosses into the far side of the record.

### Step 7. Time doublers (EXACT condition; CHECKED)

- Records sample the change only at ticks, so readable quasi-energy is Eτ mod 2π. U(τ) has a degeneracy away from H's own exactly when (E_i − E_j)τ ∈ 2πZ∖{0}. For a two-band traceless H that means max|E|τ ≥ π.
- **Below that bound:** no time doubler (and so no time-umklapp, which was a potential falsifier in A19).
- **But doubling moves into space:**
  - 1D stepped Dirac puts its partner at (k, ω) = (π, π); the sampled smooth naive Dirac puts it at (π, 0). Both have gap 0.6 at m = 0.3 (CHECKED).
  - 3D covariant H_W = Σ sin k_a σ_a at τ = 1: nearest eigenphase to π is 1.410 away; the 8 nodes have chiralities [+1 −1 −1 +1 −1 +1 +1 −1], net 0 (coordinator's FHS tool); W3 = 0.000.
  - At τ = 2 an aliasing surface appears at π.
- Per A2 D4, W3 = 0 for any continuously generated step. So under Option R the quasi-local walks with W3 ≠ 0 (A1 D14, A2 E3) cannot arise. This holds for single-particle walks; it is ARGUED beyond that.

### Step 8. What remains of the tick (ARGUED; toy evidence EXACT)

- The tick is an opportunity for record events: formation, steps and no-record updates.
- Unlike in stepped models (A5 T3.3), the dose per tick Jτ is readable: record statistics at a fixed amount of change depend on τ (Step 2 table).
- A5 T3.1 schedule independence is no longer exact. Tick phases are readable in principle through the change, so I1's "global or local" now has content.
- To avoid Zeno freezing of the possibilities by A9's √(1−F) update every tick, odds per tick must scale as c = γτ.
- Without A13's partner partition, overlapping formation stars do not commute. A covariant remedy exists: random order, which is quasi-local, or the small-c limit, where order effects are O(c²).

### Step 9. Cone and no-signalling (EXACT asymptotics and linearity; CHECKED)

**Exact part.**
- Linear local instruments plus a unitary change give no nonlinear signalling (A9; A13 S3).
- Influence outside the change's own cone is bounded by Lieb–Robinson tails, which are not zero (A5 T1.3).
- The record cone of one site per tick also bounds influence only if the change's top speed in grid steps is below one site per tick: 2Jτ < 1 in 1D, 6Jτ < 1 in 3D.
- Leak beyond the cone: |J_{n+1}(nx)|² ~ e^{−2nη(x)}, with η(x) = ln((1+√(1−x²))/x) − √(1−x²). η(0.5) = 0.451; η(0.9) = 0.031; η → 0 as x → 1.

**CHECKED, 1D: TV of B's record history.** Content can be placed by A's choice 7 sites from B; B forms with c = 0.5 each tick.

| Change | Before content could arrive at one site/tick | Later |
|---|---|---|
| Strict stepped tick | exactly 0 through n = 7 | 1.3e-2 at n = 8 |
| Smooth, x = 0.5 | ≤ 2.9e-6 for n ≤ 6 | 2.0e-5 at n = 7 |
| Smooth, x = 1.0 | 8.1e-3 at n = 6 | — |
| Smooth, x = 2.0 | 5.0e-2 by n = 4 (the change outruns I2) | — |

**CHECKED, 3D:** worst point at grid distance n+1:
- per-axis dose x = 0.2: 6e-13 at n = 24;
- x = 1/3: 4e-5;
- x = 0.5: 3e-4 (slow, power-law decay).

**Assembled toy** (8 qubits; Bell link across 4 bonds; compressed Heisenberg plus SW-content; A forms a record in Z or X):
- B's one-tick record law moves by TV ≈ 6.5e-3·τ⁴: 6.6e-11, 1.0e-9, 4.1e-8, 6.5e-7, 1.0e-5 at τ = 0.01–0.2.
- The renormalized-ratio step signals at once: 0.055–0.063, even at τ = 0.01.

### Step 10. Fit with the instincts and the clause (ARGUED; each item rests on the EXACT steps above)

- **I1:** kept. Records form and step only on ticks.
- **I2:** exact for records. Same-tick reuse is excluded.
- **I3:** kept via CL.
- **I4:** possibilities flow continuously. A standing conveyor is excluded twice: by covariance (A1 D12) and by continuity (index 0, A5 T1.4). A record's own step is a swap.
- **I5:** a full region has no change, no steps and no formation, so time stops there (EXACT).
- **Campaign 7 sentence 2:** restored clause by clause (continuous, reversible, homogeneous, soldered, star-local, keeps locked possibilities). Q2's "evolves continuously" now holds literally (A13 had to re-read it). The one change: record motion is separate from the change.
- **Sentence 4:** holds as "no nonlinear signalling"; it holds only approximately as a cone.
- **Field route (A23):** viable without Theorem N trouble. A smooth covariant field generator needs no staggered roles, and there is no doubler below the aliasing bound. Payload, energy-gentle locks and second order stay OPEN.
- **Compared with A13:** Option R removes the supplied round of pairs (A16 C7; A20/A21).

### Step 11. What Option R asks the owner to accept

1. **Two kinds of motion.** Possibilities change smoothly all the time. Records only step, on ticks, by their own rule.
2. **Records do not ride the change.** The change holds a locked possibility fixed, so a record acts on its neighbours as a fixed weight and a wall. It moves by trading places with a neighbour.
3. **No exact speed limit for unrecorded influence.** Leaks are exponentially small, and "one site per tick" also bounds influence only if the dose per tick is small.
4. **Named choices:**
   - step rate c, or a rate γ = c/τ;
   - the weight W (content, blind or activity);
   - the claim rule;
   - the dose per tick Jτ;
   - an ordering rule for overlapping stars.
5. **Neighbour-sensitive steps slightly disturb the neighbours.** Steps blind to the possibilities do not.
6. **Readable moving records are dust.** Whatever interferes stays unrecorded (A7, A13).
7. **Handedness stays doubled,** as in any continuous lattice change.

## 4. Checks

Every run used `nice -n 10`, the four thread caps set to 1 and a 55 s alarm (`run.sh`), with peak memory from `/usr/bin/time -l`.

| Script | What it checks | Result | Time, memory |
|---|---|---|---|
| `c1_carry_zeno.py` | Lemma C sizes; clip versus unclipped variance; Zeno at fixed change-time; renormalized TV | Step 2 numbers; chain matches formula to 5 decimals | 0.45 s, 79 MB |
| `c2_zeno_limit.py` | Compression identity; re-cut limit equals compression; leak | Step 1 numbers | 0.37 s, 65 MB |
| `c3_sw_instrument.py` | SW and D23 on a 3D star: completeness, covariance, unglued tests, odds, back-action | Steps 3–4 tables | 0.76 s, 46 MB |
| `c4_clash.py` | CL against literal I3 under a distant choice | Step 5 table | 0.09 s, 28 MB |
| `c5_cone.py` | Record-history TV, strict against smooth; Debye; 3D cone | Step 9 tables | 0.45 s, 62 MB |
| `c6_doublers.py` | Where the doubler sits; 3D aliasing; chiralities; W3 | Step 7 numbers | 1.69 s, 81 MB |
| `c7_reach.py` | Operator weight beyond nearest neighbours | ≈ 2τ⁴ | 0.46 s, 89 MB |
| `c8_package.py` | Assembled Option R toy; signalling scaling | τ⁴ law against instant 0.06 | 2.8 s, 166 MB |
| `c9_quiet.py` | Disturbance of the emptiness | Step 4 numbers | 0.35 s, 60 MB |

**Tolerances.** Machine identities are ≤ 5e-15. Signalling "zero" means ≤ 3e-16.

**Not run.**
- A 3D many-record CL plus formation run, with stationary density and jams. It is classical in its record part and cheap, but was not needed for the answer.

## 5. Real-physics match

**Structure.** Option R is a lattice classical–quantum hybrid: classical records jump with odds linear in the quantum possibilities, and they push back on them. Comparators, not adopted:
- Diósi;
- Blanchard–Jadczyk event-enhanced quantum mechanics;
- Oppenheim et al. 2023, whose decoherence–diffusion trade-off matches Step 4;
- GRW-type flashes.

**Gains.**
- No time doubler and no time-umklapp below the aliasing bound, which removes A19's potential falsifier.
- No supplied round.
- Continuous change everywhere.

**Losses.**
- The strict cone. This is unobservable (A5).
- A5's exact 1D Lorentz identities for stepped content.
- The stepped quasi-local walks with net handedness.

**Inherited problems.**
- Doubled chirality, as in lattice Hamiltonian field theory (Nielsen–Ninomiya comparator).
- If records act as walls for light, A14's bound applies (u∞ ≲ 1e-47 per Planck site).
- z = 2 ripples over an aligned quiet vacuum (A9).

**Falsifiers.**
- Any distant influence beyond the light cone larger than exponentially small.
- A time-doubler or time-umklapp signature, which would favour stepped change.
- Interference of anything whose path is readable at every tick.
- Measured decoherence of matter tied to record motion beyond the c(√α−√β)²/12 trade-off, if records were matter.

## 6. Open edges and next steps

1. **Joint per-site instrument.** One instrument per site with outcomes: form (lock k), claim record i, or nothing. Build it and check exclusion when formation and steps happen in the same tick.
2. **Ordering of overlapping formation stars.** Choose between random order and the c = γτ limit. Is the continuous-time limit acceptable under I1?
3. **Who sets the first menu frame (A13 E2).** Under compression, records whose content is off the emptiness's axis disturb it, which risks breeding.
4. **Owner decision on the dose per tick.** If ticks are local and influenced, does a varying dose act as A15's "change per beat" lapse, and what jitter does that bring (A17)?
5. **A rigorous Lieb–Robinson bound for the whole package.** Comparator: dissipative Lieb–Robinson bounds (Poulin 2010).
6. **Light-like content.** Covariant smooth generators with z = 1 content over a quiet vacuum (the A9/A12 tension).
7. **A23 payload.**
8. **Chirality in continuous time.** Edges of recorded regions and many-body routes are OPEN.

## 7. Plain-language summary

In this option the shared possibilities change smoothly and in the same way everywhere and in every direction, but they leave a spot that holds a record exactly as it is. On ticks a record may step to one empty neighbouring spot by trading places with what that spot holds, with odds set by what is there, and two records never end up on one spot. This hangs together: records never move more than one spot per tick, nothing far away can be learned at once, and things can move without a fixed pattern of partner pairs, which the earlier "nothing moves" result had blocked. The price is that unrecorded things have no exact speed limit, only an extremely faint leak beyond it, and that leak stays faint only if the change in one tick is small. Records wander like dust, a record that picks its step by looking at its neighbours nudges them a little each tick, and left- and right-handed things still come in equal amounts.