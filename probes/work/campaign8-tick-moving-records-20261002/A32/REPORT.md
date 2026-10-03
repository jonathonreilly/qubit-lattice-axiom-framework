*(Saved by the coordinator from the agent's final message; the agent's sandbox blocked it from writing REPORT.md.)*

# A32 report: the owner's tick instinct, redone inside Option R

**Scratch directory:** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A32/`
- Scripts `c1`–`c8`, outputs `out_*.txt`, timings `time_*.txt`.
- Wrapper `run.sh`: `nice -n 10`, the four thread caps at 1, a 55 s alarm inside each script, and a load gate that skips the run if the 1-minute load is 6 or more. One run was skipped at load 6.53 and repeated at 2.46.
- No git operations, no repo edits, no subagents, no review or audit lanes.

**Status.**
- Every model below is a supplied toy, and every rule is a named conditional, not framework content.
- The owner's tick ideas (I1, I2) are instincts, not positions.
- Option R itself is a candidate (A27, narrowed by A29). It takes Theorem N's quasi-locality exit for the possibilities and its irreversibility exit for records (C27).

**Grades.**
- **EXACT**: proof, or exact arithmetic.
- **CHECKED**: numerics in a stated toy, with a tolerance.
- **ARGUED**: reasoning without proof.
- **SUPPLIED**: a premise put in by hand.
- **COMPARATOR**: literature or experiment, quoted from memory unless marked, and never adopted.

## 1. Question

Inside Option R, records form and step only at ticks: the swap step SW, the claim rule CL, linear local instruments, and A28's gated formation where stated. Between ticks the possibilities change smoothly under a covariant, homogeneous, star-local generator compressed onto the records. In that setting:

1. **Global or neighbourhood record ticks.** Do A15's mirror walls survive? What can be read from records: seams, claim-rule clashes, start-of-tick gating across neighbourhoods, formation statistics? Does a neighbourhood tick need a per-site phase, that is, memory?
2. **Constant or influenced.** Can the record-tick rate vary from place to place? Is the lapse N(x) the influence? If the possibilities' change is lapse-paced and the record ticks are not (or the reverse), do two clocks disagree? Does consistency force one lapse? What follows for time dilation and redshift of record-made clocks?
3. **Match to real physics.** What is the leading effect of a global tick's frame on record statistics, and how small is it at Planck ticks? How does it compare with Lorentz-violation bounds? Does the record cone plus the faint possibility tail give frame effects for moving clocks? What survives of A5's relativity at low speed?
4. **Records forming on the same tick (I1, I2).** Is it consistent? Is a shared formation moment needed? What is the exact difference between commuting and non-commuting instruments?
5. **Minimum distance and minimum tick.** How are τ, a, a/τ, the possibilities' top speed and light's speed related? Must records keep up with light? Is "minimum distance implies minimum tick" derivable, or only consistent?

## 2. Answer

**The organizing fact [EXACT].**
- Under Option R the possibilities' change never depends on when records tick. The tick schedule enters only through the instants at which record instruments act.
- **Re-timing lemma (D2).** Moving one formation instrument by δ changes the law of the whole later record history by at most δ·c·‖H_∂‖·(4 + 1/√(1−c)) in total variation, to first order in δ.
  - c is the chance per tick.
  - ‖H_∂‖ is the strength of the change on bonds touching the instrument's spot.
- So everything about the schedule is readable only at order (chance per tick) and (tick length × the rate at which the odds vary). That covers global or local, constant or varying, set times or random times.
- If the chance per tick is the tick length times a rate (c = γτ), all schedules share one continuous-time limit [EXACT; CHECKED ∝ τ, C1].

**1. Global or neighbourhood.**
- **A15's mirror walls do not survive for the possibilities** [EXACT; CHECKED, C8].
  - A packet crosses an out-of-step seam in Option R. The amount that crosses (0.816–0.818, depending on τ) is the same for in-step and offset ticks to 2e-12.
  - A15's handshake rule passes nothing beyond the initial tail.
- Walls survive for records only if a record step needs both ends to tick at the same instant.
- Waiting deadlocks and rate locking have no counterpart, because nothing waits.
- **What records can show** [EXACT bounds; CHECKED, C1, C2]: only order-c and order-τ traces.
  - Exact same-tick coincidences exist only inside a phase region.
  - The claim rule needs a convention at seams. With claims at the claimant's tick, step rates are phase-blind at order c.
  - Gating at each site's own tick lets chains of new records run along rising phases. The strict one-site-per-tick record cone then becomes a probabilistic one:
    - 10 sites per period up a ramp of 0.1 period per site, at F = 1;
    - a front-speed change of order F: in 1D exactly v = 1/(E[w] + 1/F − 1), and about 1.2F in 2D.
- **What a neighbourhood tick needs.**
  - A tick written into the law must be the same everywhere, by covariance [EXACT].
  - Set ticks that differ from place to place need a stored per-site phase: the memory decision, or more room per site. For a changing lapse this is EXACT: the phase depends on the lapse's history, not on the snapshot.
  - Random per-site times need no memory, but they are a diluted global schedule with no set ticks [EXACT].
  - Tick times set by a possibility are just a formation weight [EXACT].
- A global time offset is unreadable [EXACT; CHECKED 2.2e-15]. Relative offsets are readable at order τ [CHECKED].

**2. Constant or influenced.**
- **The rate can vary.** The record-tick rate may differ from place to place with none of A15's walls, rate locks or opaque gradients [EXACT; CHECKED: a lapse ramp from 1 to 0.5 over 100 sites reflects 3.8e-5].
- **The natural influence is the lapse.**
- **Two clocks.** Suppose the possibilities' change is lapse-paced but the chances of record formation are not. Then record-counting clocks and clocks carried by the possibilities disagree by ΔΦ/c² [EXACT; CHECKED: order (1−N), independent of τ]. The reverse case gives the same disagreement the other way [EXACT].
- **What consistency forces.**
  - Exact local position invariance forces the formation chance per unit proper time to be the same everywhere. The chances must carry the same lapse as the change [EXACT].
  - The tick rate itself must follow that lapse only at order τ × frequency [EXACT; CHECKED: exact invariance with lapse-paced ticks, to 2.6e-13; with a global tick and lapse-weighted chances the residual is 0.037·τ₀(1−N)].
  - Exception: if the chance per tick is a fixed number, the ticks themselves must be lapse-paced.
- **Memory-free option.** One global coordinate tick, with lapse-weighted chances.
- **Lapse-paced ticks** need per-site phases. Neighbouring Planck sites at Earth's surface would drift through a full cycle every c/g ≈ 1 year [EXACT arithmetic].
- **Record-made clocks** then slow and redshift universally [EXACT in the eikonal].
- **A record's own step needs a pacing convention across a gradient.** Claimant, record or bond lapse put record dust in proportion to N, to 1/N, or uniform [EXACT; CHECKED].

**3. Match to real physics.**
- **No new frame, and no effect on propagation.**
  - The tick's frame is the lattice's [EXACT].
  - Under gated formation the tick has no effect, at any order, on how light or matter propagate through empty space [EXACT].
  - So gamma-ray-burst timing and birefringence bounds constrain the change H, not the tick (COMPARATOR).
- **Discreteness effect.** It is of order c + Eτ/ħ per record event, times v/c for moving systems. That is ≲ 1e-22 for GeV content at Planck ticks [ARGUED from the EXACT bound].
  - At a matched Planck tick (change per tick of order 1) this needs records whose odds vary slowly compared with the tick: gentle records (A24).
- **A separate frame that does not shrink with τ.**
  - The schedule sets formation chances per lattice tick. So formation-limited record counting runs on lattice time unless the formation weight scales like m/E.
  - In a two-band toy, no nonzero positive local weight achieves that, and at most half of the count rate slows with motion [EXACT toy; ARGUED in general].
  - Gravitational slowing of formation can be made exact; slowing by motion only partly.
  - The effect is unobservable at the formation rates already bounded by heating (A24, A28), but it is structural.
- **Moving clocks carried by the possibilities** slow as R = √(1 − v²/cos²k) in the continuous-time lattice toy [EXACT; CHECKED 6e-10].
  - A5's relativity at low speed survives as a property of the change, with (pa/ħ)² corrections: about 1e-38 for a muon storage ring.
  - A5's exact cone, its exact 1D identities and its exact schedule independence do not survive.

**4. Same tick.**
- Simultaneous formations are consistent and never signal [EXACT; CHECKED 3e-16].
- **One-site weights.** If each tick's instruments act on their own site only, they commute. "Together" then equals every order, and no shared moment is needed [EXACT; CHECKED 7e-17].
- **Relational (star) weights** need an ordering rule. Different orders differ at order c² [EXACT bound; CHECKED 0.044c²].
- **Reading choice.** Whether same-tick neighbours see each other's new records is a reading choice. The start-of-tick reading keeps the strict cone. The two readings differ at order c² [CHECKED 0.059c²].
- **Frequency.** With realistic chances, same-tick neighbouring formations are a fraction of about c/2 of pairs.

**5. Minimum distance and minimum tick.**
- **Change per tick = speed ratio.** The change per tick equals the possibilities' top speed divided by the records' speed limit a/τ [EXACT].
- **Maximum tick.** For the one-site-per-tick limit to bound all influence, with only an exponentially faint leak, τ < a/v_max ≤ a/c [EXACT, given that light is a ripple of the possibilities].
  - At τ = a/v_max the leak is a power law, 0.169·n^(−1/3) in 1D [EXACT asymptotics; CHECKED].
  - In 3D, records keep up with isotropic light in every direction only if τ ≤ a/(√3c) [EXACT].
- **The change's own minimum time.** Finite bandwidth gives the change a minimum time of about (a/v_max)/z [EXACT bound]. "Minimum distance implies minimum time" is therefore derivable for the change of possibilities, but not for the record schedule.
- **A pinned tick, conditionally.** If every tick carried an order-1 chance, two effects would pin τ near a/v_max, within a factor of about 2 [EXACT toy optimum Jτ* = 1.1656; ARGUED in general]:
  - Zeno freezing below about c/(2J);
  - outrunning above a/v_max.
- Such chances are excluded near transparent matter and for sharp records (A28, A24) [ARGUED].
- With small chances the tick is only bounded above, and it is consistent all the way down to the continuous limit.
- **Verdict on the instinct.** It is derivable as an upper bound, and as a pinned value only conditionally. Otherwise it is only consistent.

**Scope notes on binding corrections.**
- **C38 is redone here.**
  - Cone: D7, D22.
  - 1D identities: D21.
  - Mirror walls: D5.
  - Deadlocks: D1.
  - Schedule independence: D2, D3, D24.
- **C39's scope.** "Nearly undetectable at Planck ticks" holds for a small change per tick, τ ≪ a/c. At the owner's matched tick (change per tick of about 1), the EXACT bound is of order 1 per record event. Near-undetectability then needs gentle records [ARGUED, D4].

## 3. Derivation

### 3.0 Setup [SUPPLIED] and named conditionals

**The snapshot.**
- Records: a site plus a pure content.
- Shared possibilities ρ (Q2).

**Between record events.**
- ρ ↦ e^{−iH_R s} ρ e^{iH_R s}, with H_R = Q_R H Q_R.
- H = Σ_b N_b h_b is covariant and star-local.
- N ≡ 1 unless the lapse is on (A26).

**At record events: linear local instruments (A9 Theorems 1–2).**
- Formation has weight 0 ≤ F ≤ c on a star S, with Kraus operators:
  - P_k √F: record k forms and the site is cut to agree;
  - √(1−F): no record.
- SW steps and CL claims, as in A27.
- A28 gating, where stated.

**The schedule** is the set of instrument times t_{x,n} at each site.
- **Global:** t = φ + nτ.
- **Neighbourhood:** φ(x) varies from site to site.
- **Lapse-paced:** proper interval τ₀, which is coordinate interval τ₀/N(x).

**Named conditionals introduced here [SUPPLIED].**
- **P1 (chance scaling).** c = γ × (proper length of the tick). The alternative P1′ is a fixed chance per tick.
- **P2 (gating instant).** Gating and menus use the records present at the instrument's own instant. A28's start-of-tick rule is the global-tick case.
- **P3 (step pacing).** A step is scheduled at the claimant's tick, at the record's tick, or by a symmetric bond lapse.
- **P4 (same-tick reading).** For same-tick neighbours, the conditions are those at the start of the tick, or those within the tick.
- **P5 (proper-time pacing of formation).** The formation chance per unit proper time is universal.

### 3.1 Global or neighbourhood (Q1)

**D1. The change does not depend on the schedule [EXACT].** H_R depends only on the record configuration (A27 Step 1), and a schedule fixes only when instruments act. Hence:
- (a) Every bond term acts at all times, whatever its ends' phases. Nothing corresponds to A15's "naming" of a pair.
- (b) Under gating, sites at distance ≥ 3 from all records are touched by no instrument (A28 Step 2). There the possibilities evolve by e^{−iHt} under every schedule.
- (c) Nothing in the change waits. A15 Theorem B (rate lock) and Theorem C (waiting deadlock) therefore have no counterpart for the possibilities.

**D2. Re-timing lemma [EXACT].**
- **Setup.** An instrument with Kraus operators {K_k} on support S acts at time t (process A) or at t + δ (process B), with everything else equal.
- **The difference.** Let U^{(k)} be the flow after outcome k, compressed on any new record, and U the flow before. The outcome-resolved outputs differ by D_k = U^{(k)}(δ)K_k − K_k U(δ).
- **Bound on D_k.** ‖D_k‖ ≤ δ‖H^{(k)}K_k − K_kH‖ ≤ 2δ‖H_∂S‖‖K_k‖. Only terms touching S fail to cancel, and compression does not raise norms.
- **Bound on the history.** XρX† − YρY† = DρY† + YρD† + DρD†. So the trace distance of the joint (outcome, state) outputs is ≤ Σ_k (‖D_k‖‖K_k‖ + ‖D_k‖²/2). Every later step is a CPTP map, so this bounds the total variation of the whole later record history.
- **For a formation instrument:**
  - each forming outcome gives ≤ 2δc‖H_∂S‖;
  - the no-record outcome gives ≤ δ‖[H, √(1−F)]‖ ≤ δc‖H_∂S‖/√(1−c), by the power series Σ n|f_n|c^{n−1} = 1/(2√(1−c)) applied to ‖[H,F]‖ ≤ 2c‖H_∂S‖.
  - Total: **ΔTV ≤ δ·c·‖H_∂S‖·(4 + 1/√(1−c)) + O(δ²).**
- **Reordering.** Exchanging two instruments with overlapping supports costs ≤ 25c² (crude constant; D25). Disjoint supports commute.

**D3. Consequences [EXACT; CHECKED].**
- **(a) Two schedules with the same instruments** can be joined by re-timings, each of at most τ, and by exchanges of overlapping instruments.
  - Over time T with n_S active sites: TV ≤ n_S (T/τ)[5c‖H_∂‖τ + 25zc²].
  - Under P1 this is ≤ n_S Tγτ[5‖H_∂‖ + 25zγ], which goes to 0 linearly in τ.
- **(b) The continuous-time limit.** Each ticked process with c = γτ converges, at rate O(τ), to the continuous-time (Poisson-timed) record process with generator −i[H_R,·] + γΣ_x 𝒟_x. This is a first-order product formula with a local commutator. The scaling is EXACT; the constant is not optimized.
- **(c) A global offset is unreadable** for stationary preparations, because it is a time translation.
  - CHECKED C1d: 2.2e-15 on a ring prepared in an eigenstate.
- **(d) Relative offsets and rates are readable only at order τ.** CHECKED, C1:

  | C1 case | TV (coefficient of τ) |
  |---|---|
  | Neighbourhood vs global phase, adjacent detectors | 0.0070·τ |
  | Neighbourhood vs global phase, far detectors | 0.0083·τ |
  | Exact bound for the same comparison | 5.3·τ |
  | Phase ramp over six detectors | 0.0082·τ |
  | Random phases over six detectors | 0.0098·τ |
  | Ticked vs continuous limit | 0.037·τ |
  | Stationary preparation, relative shift, adjacent detectors | 0.0057·τ |
  | Stationary preparation, relative shift, far detectors | 0.0015·τ |

**D4. Size per record event [ARGUED; bound EXACT].**
- **The exact bound.** Dividing D3 by the expected number of record events (about n_S Tγ) gives ≲ 5‖H_∂‖τ + 25zγτ per record event.
- **Slowly varying odds.** When the odds vary at a frequency ω ≪ ‖H_∂‖, the effect is of order ωτ.
  - CHECKED (C8): a smooth packet crosses out-of-step detectors. Total transmission is unchanged to 2e-12. The share recorded by the B detectors shifts by 2.9e-5, 1.4e-5 and 7.0e-6 at τ = 0.2, 0.1 and 0.05.
  - A localized (broadband) start gives 7e-3·τ instead (C1a).
- **At a change per tick of order 1, with sharp records.** Sharp records inject grid-scale energy (A24), and the bound then allows order 1 per record event. In C1b's coarse readout the effect stays at most 0.0153 even at change per tick 1 and chance 1.
- So at matched Planck ticks, "nearly undetectable" (C39) relies on gentle records.

**D5. Mirror walls [EXACT; CHECKED].**
- **Why they existed.** A15 Theorem A needs a pair process that acts only when both ends' clocks pick it.
- **Option R's change has none** (D1a), so possibilities cross any phase seam.
- **Record steps.** These are the only pair processes. With claimant- or record-scheduled steps, no seam blocks them. A15's argument applies verbatim only if a step requires both ends to tick at the same instant (a handshake). Then the seam is a mirror for records, never for possibilities.
- **CHECKED (C8, 400-site chain).**
  - A15 handshake seam (θ = π/4): the weight beyond the seam equals the initial Gaussian tail, 1.714e-11. With no seam it is 0.147.
  - Option R: 0.816–0.818 crosses, identical for in-step and τ/2-offset detector ticks to 2e-12.

**D6. The claim rule across seams [EXACT].** Here CL uses claims at the claimant's tick.
- **Rates.** Each empty neighbour y applies its claim instrument once per own period, with effect (c/z)W_y. Each record therefore gets one claim chance per neighbour per period, as under a global tick. Step rates agree at order c.
- **I3 is phase-blind.** At a contested site it is decided inside y's own instrument: P(i | y taken) = w_i/Σw.
- **What changes at order c².**
  - A record beside a seam can be claimed in two rounds per period, so two steps per period become possible.
  - Across the seam, "a record claimed by several sites picks one uniformly" becomes "the first claim in the period wins".
- **Exclusion** holds round by round.
- **A C40 admissibility filter** ("step only if r is on y's menu given y's recorded neighbours at that instant") is a classical function of records. It is therefore linear and works with any schedule [ARGUED].

**D7. The record cone under neighbourhood phases [EXACT; CHECKED].** Assume P2.
- **Chain criterion.** A chain of gated formations, or of claimant-scheduled steps, x₀ → … → x_n completes within one period if and only if the phases rise strictly along the path.
- **Cases.**
  - (a) Global tick: exactly one site per period (A28).
  - (b) A ramp of g periods per site: 1/g sites per period up the ramp, 1/(1−g) down it.
  - (c) Independent random phases: chains along rising paths.
- **1D front speed (renewal).** With per-tick success F at gate-open sites, the speed is exactly **v = 1/(E[w] + 1/F − 1)** sites per period. Here w is the wait from a site's tick to its neighbour's next tick, and w = 1 for equal phases. So v/v_global = 1/(1 − (1 − E[w])F) = 1 + O(F).
- **Coupling.** Using the same success draws, no phase field is ever slower than the global tick, since every wait is ≤ 1.
- **CHECKED (C2).**
  - 1D Monte Carlo matches the formula within error; the largest deviation is 0.8%, at F = 0.5 up the ramp: 0.916 against 0.909.
  - 2D at F = 1 after 12 periods:

    | Phase field | Reach along +x | Reach along −x | Sites recorded |
    |---|---|---|---|
    | Global (the L1 ball) | 12 | 12 | 313 |
    | Ramp, g = 0.2 | 60 | 15 | 916 |
    | Independent random | 27.5 | 28.0 | 2401 |

  - 2D linear speed-up with independent random phases: about 1.2F, for F from 0.2 down to 0.0125.
- **Reading.** Under P1, F = γτ. The cone's reach grows, but its probability-weighted speed changes only at order γτ. The strict cone softens into the record-side analogue of the possibilities' faint leak.
- **Restoring the strict cone.** A per-site memory of the record pattern at the site's previous tick restores at most one site per period [EXACT].

**D8. What a neighbourhood tick needs [EXACT, construction by construction; this is not a closure claim].**
- **(a) A law-level schedule.** Translation covariance requires φ(x+e) ≡ φ(x) (mod τ) for every lattice vector e. So a law-level phase is uniform: a tick written into the law is global. A non-uniform law-level pattern is supplied structure that tells sites apart: A16 C7's cost, and Theorem N's supplied-pattern exit.
- **(b) Random per-site times, with the randomness unrecorded.** At each instant dt the site applies (1 − dt/τ)·id + (dt/τ)·I. That is one linear instrument with weight (dt/τ)F: a diluted global schedule. It needs no memory, but it has no set ticks.
- **(c) Times set by a possibility** (a clock projector Π). The controlled instrument has Kraus operators P_k√F ⊗ Π and K_∅ ⊗ Π + 1 ⊗ (1−Π). That is exactly the instrument with weight F ⊗ Π: a weight, not a set time. On one qubit per site, the clock would share the qubit with everything else, which means more room per site (C54) [ARGUED].
- **(d) Set, non-uniform phases held in the state** need an extra per-site register: memory, decision 9. For lapse-paced ticks with a changing lapse, φ(x,t) = ∫₀ᵗ N(x,t′)dt′/τ₀ depends on the lapse's history. Two histories with the same present lapse give different phases, so memory is required.
- **(e) Ticks triggered by neighbouring record events.** Without memory they fire at the triggering instant, which allows unbounded same-instant chains (A28 Step 1). A delay needs memory.
- **Summary.** In each construction examined, set neighbourhood ticks either reduce to a global tick, lose their set times, or need per-site memory or more room.

**D9. The coincidence signature of a seam [EXACT, given P4 and a menu frame set by records].**
- **Inside a phase region.** Linked neighbours with chance p per tick form on the same tick in a fraction p/(2−p) of pairs (A5 T5.1). Under the start-of-tick reading they do not see each other's new records.
- **Across a seam.** The two never form at the same instant, so the later one always sees the earlier one.
- So the seam shows in pair statistics at order p = c.

### 3.2 Constant or influenced (Q2)

**D10. Rate differences need no handshakes [EXACT; CHECKED].**
- By D1, varying tick rates leave the change untouched. Nothing locks rates and nothing deadlocks.
- A lapse gradient enters the change as H_N (A26), and a packet crosses it smoothly.
- CHECKED (C3b): H_N with N falling from 1 to 0.5 over 100 sites reflects 3.8e-5 and transmits 0.99996. A sharp step reflects 0.076.
- Compare A15 S10: rigid lapse-paced beats under ticked change transmit only 0.021–0.157 through a gradient.

**D11. Local position invariance [EXACT; CHECKED].**
- Take a region of constant lapse N, with proper tick τ₀ (coordinate τ₀/N) and chance γ₀τ₀ per tick.
- After rescaling t′ = Nt, the record process is identical to the N = 1 process.
- CHECKED (C3a): TV ≤ 2.6e-13 for N = 0.8, 0.625 and 0.5, and τ₀ from 0.1 to 0.0125.

**D12. Two clocks [EXACT; CHECKED].**
- **Phase clocks** are oscillations carried by the possibilities and locked by a forming record. Under H_N they run at N per coordinate time.
- **Counting clocks** count record events. They run at (chance per tick)/(coordinate tick).
- **Cases.**
  - **(i) Global coordinate ticks with fixed chances (P1′).** Counting clocks run at c/τ and do not slow, so the two clocks disagree by 1 − N = ΔΦ/c² however small τ is.
    - CHECKED: TV 0.045, 0.090 and 0.124 at N = 0.8, 0.625 and 0.5, the same for every τ₀.
  - **(ii) Global coordinate ticks with lapse-weighted chances, c = γ₀Nτ.** Counting clocks run at γ₀N and slow correctly. The process at lapse N equals the N = 1 process with proper tick Nτ, so only a tick-length residual remains.
    - CHECKED: TV = 0.037·τ₀(1−N) (0.0383 at τ₀ = 0.1 falling to 0.0371 at 0.0125). This matches C1's tick-length coefficient, 0.0371τ, as expected.
  - **(iii) Lapse-paced ticks:** exact, as in D11.
  - **(iv) The reverse case** (change not lapse-paced, ticks lapse-paced, fixed chances): counting clocks slow while phase clocks and light do not. This gives the same order-ΔΦ/c² disagreement.

**D13. Consistency conditions [EXACT].** Exact local position invariance requires two things:
- **(A)** a universal formation chance per unit proper time. The chances must carry the same lapse as the change. This is needed at order ΔΦ/c².
- **(B)** a universal proper length of the tick. This is needed only at order τ × frequency (D3, D12(ii)).

Consequences:
- With fixed chances per tick (P1′), condition (A) forces the ticks themselves to be lapse-paced.
- **The pacing must use the very lapse that paces the change.** On the field route that lapse is a field of the possibilities. It then enters formation linearly through the weight N̂ ⊗ F (A23 tension (a)), which is positive and linear because the field and matter factors act on different parts.
- A record-computed estimate of the lapse would differ from the change's lapse and reopen the mismatch.
- **The memory-free option** is one global coordinate tick with chances γ₀N̂τ.
- **Lapse-paced ticks** meet (A) and (B), but they are neighbourhood ticks with drifting phases (D8d).
  - Neighbouring sites drift through a full cycle every τ₀/(a|∇N|) = (cτ₀/a)(c/g).
  - At Earth's surface with a/τ₀ = c, that is c/g ≈ 3.1e7 s, about 1 year [EXACT arithmetic].

**D14. Redshift and time dilation of record-made clocks [EXACT in the eikonal, given D13(A)].**
- With a static H_N, the change conserves coordinate frequency.
- Phase clocks run at N(x), and counting clocks run at γ₀N(x).
- So every clock comparison made with light gives the ratio N_emit/N_recv (A26 D2), the same for every clock type.
- A global coordinate tick is not itself slowed. With small chances, though, it cannot be counted, since each tick leaves a record with probability about c. It is an absolute clock that is readable only at order c and order τ × frequency [ARGUED].

**D15. Record steps across a lapse gradient [EXACT; CHECKED].**
- A step x → y is a two-site event. Its rate per coordinate time depends on the convention:
  - claimant-scheduled: k·N_y;
  - record-scheduled: k·N_x;
  - bond-symmetric: k·(N_x + N_y)/2.
- Detailed balance gives stationary record-dust densities proportional to N, to 1/N, and uniform respectively.
- CHECKED (C7, 101 sites, N from 1 to 0.7): exact to 5e-15.
- So the convention is readable at order ΔΦ/c² in dust densities. It is the step-level form of decision 10's pacing composition.

**D16. Other influences [ARGUED].**
- **Record-set tick rates** are classical control and do not signal (A15 S11). Their shot noise only randomizes when records form, which is readable only at order c.
- A17's dephasing problem concerns pacing of the change, not of the record tick.
- **A tick rate set nonlinearly by possibilities** signals (A15 S11; A21 C11). Set linearly, it is a weight (D8c).

### 3.3 Match to real physics (Q3)

**D17. The tick's frame is the lattice's [EXACT].**
- A global schedule t ∈ φ + τZ is invariant under the lattice's translations and proper rotations.
- A tilted schedule φ + τZ + u·x is invariant only for u ≡ 0 modulo the period lattice. This is A5 T6.1 in Option R form.
- What the tick adds, for record events only: simultaneity slices and time discreteness. It adds nothing to the change.

**D18. Propagation never sees the tick [EXACT under gating].**
- Between record events the change is e^{−iH_R t}.
- At distance ≥ 3 from records no instrument acts (A28).
- So in empty space the dispersion, speed and polarization of every ripple are those of H, at every order. The tick adds no energy-dependent speed and no birefringence.
- Near matter, weights acting on light add order-γ decoherence. Its tick-dependent part is of order γτ × frequency.

**D19. Discreteness effects on record statistics [ARGUED, from D2–D4].**
- Per record event the effect is of order c + ωτ.
- For a system moving at v, the lattice's tick slices are tilted by Γv/c² in its rest frame, and its proper tick spacing is τ/Γ.
  - Direction-dependent statistics then differ from rest by order (c + ωτ)·v/c.
  - Scalar statistics differ by order (c + ωτ)·v²/c².
- **Numbers at τ = t_P = 5.4e-44 s.**
  - ωτ = E/E_P: 8.2e-20 at 1 GeV, 8.2e-29 at 1 eV.
  - c = γt_P ≲ 5e-35 for a nanosecond detector response; ≲ 3e-86 per tick for sharp edge records (A28).
  - v/c ≈ 1.2e-3: Earth against the cosmic-background rest frame (COMPARATOR).
- **Result:** ≲ 1e-22 per record event for GeV content.
- For N independent events the distinguishability grows only like √N times the per-event effect.

**D20. The schedule's own frame, independent of τ [EXACT in a toy; ARGUED in general].** Formation chances are set per lattice tick. A moving system's record count per lattice time is therefore (c/τ)Σ_x tr(F_x ρ_v).
- **(a) A number-type weight, F = c·n.** Σ_x tr(F_x ρ) = c × (number of excitations), whatever v is. Per proper time the count runs Γ times its rest rate: it is a lattice-time clock.
- **(b) A two-band toy, H(k) = sin k·σ_x + m·σ_z.**
  - A translation-invariant weight has block F(k) = a + bσ_z + dσ_x + eσ_y. Its upper-band expectation is a + (bm + d·sin k)/ω.
  - Proper-time counting needs this to be proportional to m/ω = R. By Feynman–Hellmann, ⟨∂H/∂m⟩ = ∂ω/∂m. CHECKED: ⟨σ_z⟩ = m/ω to 1e-10.
  - Multiplying by ω, a(k)ω(k) would have to be a trigonometric polynomial. For m ≠ 0, ω is not a rational function of e^{ik}, because the quartic under the square root has four distinct roots. So a ≡ 0.
  - Positivity, a ≥ √(b²+d²+e²), then forces F = 0.
  - **So no nonzero positive finite-range weight makes the count follow proper time [EXACT, toy].**
  - With momentum-independent blocks, the count ratio is (a + bR)/(a + b) with a ≥ |b|. **At most half of the count rate slows with motion** [EXACT; CHECKED f = 0.500000 over 20,000 random positive weights].
- **(c) Gravity versus motion.**
  - The lapse part can be exact, through the weight N̂ ⊗ F (D13).
  - Formation can therefore follow gravitational slowing exactly but slowing by motion only partly. Formation-limited counting keeps a lattice-frame part of size between v²/4c² and v²/2c² [ARGUED beyond the toy].
  - No schedule can repair this: a schedule set by a possibility is a weight (D8c), and records do not carry a body's speed [ARGUED].
  - COMPARATOR: collapse models face the same preferred-frame issue. GRW and CSL are non-relativistic; relativistic versions are due to Tumulka, Bedingham and Pearle. From memory, not adopted.

**D21. Moving clocks carried by the possibilities [EXACT; CHECKED].**
- **Model.** The clock is two internal states with masses m ∓ δ/2 (A5 T2.5). Its rate relative to rest is R = ∂ω/∂m = m/ω.
- **1D result.** For H(k) = sin k·σ_x + m·σ_z, v = sin k·cos k/ω, and **R² = 1 − v²/cos²k** exactly.
  - Proof: 1 − v² = (sin⁴k + m²)/ω², so R² = 1 − v² − v²tan²k.
- **3D naive Dirac:** R² − (1 − v²) = −Σ_i sin⁴k_i/ω².
- **CHECKED (C6):** 6.4e-10 and 8.8e-11, limited by finite differences.
- **Comparison with A5.** A5's stepped walk gave R² = 1 − v²/cos²m. The species-dependent limiting speed cos m becomes the momentum-dependent cos k.
- **Size at Planck spacing** [EXACT arithmetic]: v²tan²(pa/ħ) is
  - 6.4e-38 for 3.09 GeV muons;
  - 4.3e-39 for Li⁺ ions at 0.34c;
  - 6.7e-27 for 1 PeV protons.

**D22. What survives of A5; the record cone and the tail [ARGUED].**
- **What survives, as properties of the change.**
  - Low-speed Lorentz kinematics and the slowing of possibility clocks (D21).
  - Real-valued, conserved energy: no quasi-energy folding and no time doubler for the change.
  - The order of record events outside each other's light cone stays unreadable, up to Lieb–Robinson tails.
- **What is lost (C38).**
  - The exact cone.
  - A5's exact 1D identities, which were specific to the stepped walk.
  - Exact schedule independence, now order τ (D3).
  - "1D massless content has no dispersion": the continuous-time lattice gives v = cos k.
- **The record cone** is an L1 polytope in the lattice frame. Its speed is a/τ along axes and a/(√3τ) along body diagonals.
  - It never limits a possibility clock. It matters only for recorded fronts that must follow a body moving near a/τ.
- **The faint tail** is a property of H beyond its light cone and does not change clock rates.
- So the record cone plus the tail adds no frame effect for moving clocks at v ≪ a/τ.

**D23. Stroboscopic blindness [EXACT, toy].**
- With set ticks, an oscillation of the possibilities whose period divides the tick is never recorded.
- In the two-level toy (H = Jσ_x, weight c|r⟩⟨r|) at Jτ = π, the state at every tick is exactly the unrecordable one, for every c. C5d shows the rate collapsing near Jτ = 3.
- This is a readable signature of set ticks, absent for Poisson-timed formation. It is irrelevant when ωτ ≪ 1.

### 3.4 Records forming on the same tick (Q4)

**D24. One-site supports commute [EXACT; CHECKED].**
- Suppose each instrument on a tick has Kraus operators on its own site only, given the start-of-tick record pattern. That means one-site weights F^(R) and one-site claim weights; resolved SWAPs act on disjoint pairs by exclusion.
- Then all instruments on that tick commute. "Together" equals every order, and a shared formation moment has no readable content.
- **An example** compatible with a quiet emptiness and with no law-level axis: F^(R) = c(1 − |r⟩⟨r|) on the forming site, with r taken from a recorded neighbour.
- CHECKED (C4, W1): TV between the two orders ≤ 7e-17, for c from 0.4 to 0.025.

**D25. Overlapping (relational) weights [EXACT bound; CHECKED].**
- A28's weight B and the activity weight act on shared sites, so instruments at distance 1 or 2 do not commute.
- Each outcome-resolved map is id + O(c) or O(c), so order effects are order c² per overlapping pair per tick. The crude constant is ≤ 25.
- CHECKED (C4, W2): TV = 0.0437c², with P(both form) = 0.109c².
- **A rule is then needed** (A27 open edge 2). The options:
  - a fixed order, which picks a direction unless it is made symmetric;
  - random order, which is covariant and linear;
  - a joint instrument.
- In the continuous limit the choice does not matter: it contributes order γ²τ per unit time.

**D26. No signalling for any order [EXACT; CHECKED].**
- Every such rule is a composition or mixture of linear local instruments, so none signals (A9 Theorem 2; A13 S3).
- CHECKED: TV across a distant qubit's three choices ≤ 3.1e-16 for both orders and for random order. Completeness 9e-15.

**D27. Admissibility of same-tick neighbours [EXACT as a dichotomy; CHECKED].**
- **Start-of-tick reading (P4).** Each same-tick formation's menu is set by the records present at the start of the tick. Each record is admissible relative to the conditions when it locked, and the strict record cone holds. Same-tick neighbours ignore each other's new records.
- **Within-tick reading.** A later same-tick formation sees an earlier one. Then one of three things is needed:
  - an order (D25);
  - accepting in-tick chains, which break the strict cone (A28 Step 1);
  - a joint instrument with a joint admissible menu over each cluster of simultaneously forming sites, whose reach is the cluster's size.
- The two readings differ at order c² [CHECKED, W3: 0.0593c²].
- This mirrors C40's admissibility question for moved records. It is an owner decision.

**D28. Frequency, and I2 [EXACT].**
- With chance p per tick at both linked neighbours, a fraction p/(2−p) of pairs form on the same tick (A5 T5.1).
- With p = c ≪ 1 that is about c/2, and it is zero in the continuous limit.
- "One formation per site per tick" (I2) holds automatically: one joint instrument per site per tick, with outcomes form, claim or nothing (A28 Step 0).

### 3.5 Minimum distance and minimum tick (Q5)

**D29. The change per tick is a speed ratio [EXACT].**
- For hopping strength J, the change's top speed per axis is 2Ja, from the group velocity 2Ja·sin k.
- The change per tick, x = 2Jτ, equals (2Ja)/(a/τ): the possibilities' top speed divided by the records' speed limit.
- In 3D the L1 top speed is 6Ja (A27's 6Jτ < 1).

**D30. Containment [EXACT asymptotics; CHECKED].** The weight beyond the record cone after n ticks, for a single excitation in 1D, is Σ_{|d|>n} |J_d(nx)|².

| Change per tick | Behaviour of the leak | CHECKED |
|---|---|---|
| x < 1 | Exponential, ∝ e^{−2nη(x)}, with η(x) = ln((1+√(1−x²))/x) − √(1−x²) | Slope 0.909 against 2η(0.5) = 0.902 |
| x = 1 | Power law, 2·2^{1/3}·Ai′(0)²·n^{−1/3} = 0.1688·n^{−1/3} (Airy) | Ratio rises 0.52 → 0.92 from n = 10 to 3000, converging |
| x > 1 | Tends to 1 − (2/π)·arcsin(1/x) | 0.2732 against 0.2736 at x = 1.1 |

The 3D L1 cone:

| Per-axis change per tick | Behaviour of the leak |
|---|---|
| 0.2 and 0.3 | Exponential |
| 1/3 (matched) | About n^{−0.9}: 1.5e-3 at n = 100, 5.4e-4 at n = 300 |
| 0.4 | About 0.14: the change outruns the records |

**D31. τ against a/c [EXACT, given the premises].**
- Suppose light is a ripple of the possibilities, with speed c ≤ v_LR, and the one-site-per-tick limit is to bound all readable influence with only an exponentially faint leak.
- Then **τ < a/v_LR ≤ a/c**.
- At τ = a/v_max the leak is only power-law small (D30).
- With the L1 record cone in 3D and isotropic light, records keep up in every direction only if τ ≤ a/(√3c).
- Option R does not need records to keep up in order to be consistent. It holds at any change per tick, with a growing leak (C52).

**D32. The change's own minimum time [bound EXACT; identification ARGUED].**
- For any weight, |d tr(Fρ)/dt| = |tr(i[H,F]ρ)| ≤ 2‖H_∂‖‖F‖ ≤ 2zJ‖F‖. So record odds cannot change by order 1 in less than about 1/(2zJ).
- The fastest content crosses one site in a/v_max = 1/(2J).
- Both follow from one bounded coupling on a finite site domain (Qubit plus star-locality). The minimum readable time is about (a/v_max)/z.
- This derives "minimum distance implies minimum time" for the change of possibilities. It says nothing about when records may form.

**D33. The Zeno window for order-1 chances [EXACT toy; ARGUED in general].**
- **Toy.** H = Jσ_x between an unrecordable state u and a recordable state r, with weight c|r⟩⟨r| at each tick.
- **Record rate at c = 1.** Exactly sin²(Jτ)/τ.
  - About J²τ for Jτ ≪ 1: Zeno freezing.
  - Largest, 0.7246J, at Jτ* = 1.1656 (where 2Jτ = tan Jτ).
  - Zero at Jτ = π (D23).
- **Smaller chances.** For c = 0.5 and 0.1 the optimum sits at Jτ ≈ 0.248 and 0.050, that is τ* ≈ c/(2J). CHECKED with exact Stein-equation sums.
- **The window.** With an order-1 chance per tick, ticks much shorter than about c/J freeze the possibilities next to records. Ticks longer than a/v_max = 1/(2J) let the possibilities outrun records (D30–D31).
  - For c = 1, the rate is within a factor 2.5 of its maximum only for Jτ ≳ 0.3, while the cone needs Jτ ≤ 0.5.
  - So τ lies between about 0.6 and 1 times a/v_max: pinned to the time light takes to cross one site, within a factor of about 2.
- So "minimum tick ≈ a/c" follows, conditional on order-1 chances.
- With c = γτ ≪ 1 the window opens: Zeno freezing needs only γ ≲ J, and any τ ≤ a/v_max works.

**D34. Order-1 chances are excluded where the window would matter [ARGUED; rests on A28's and A24's COMPARATOR-based bounds].**
- Near transparent matter, weights that act on light need κ ≲ 4e-6 per contact tick for nucleon-sized records in silica fibre (A28 Step 8).
- Sharp records at Planck coupling need ≲ 3e-86 per tick (A28 Step 7c).
- Weights on settled content commute with the local change (A24). There Zeno freezing does not bite, and nothing pins τ either.

**D35. Aliasing at matched ticks [EXACT arithmetic].** A27 Step 7: there is no time doubler if and only if bandwidth × τ < 2π.

| Toy and tick | Bandwidth × τ | Against 2π = 6.283 |
|---|---|---|
| 1D hopping, τ = a/v_max | 2 | No doubler |
| 3D hopping, L1-matched τ = 1/(6J) | 2 | No doubler |
| 3D hopping, axis-matched τ = 1/(2J) | 6 | No doubler, little margin |
| 3D hopping, τ = 1/J | 12 | Aliasing |

**D36. Verdict on "minimum distance implies minimum tick" [graded by parts].**
- **Derivable:**
  - (i) an upper bound τ < a/c, if one site per tick is to be the universal limit [EXACT, given the premises];
  - (ii) a minimum time of the change, about (a/v_max)/z [EXACT bound];
  - (iii) a pinned tick of about a/c, if every tick carries an order-1 chance [EXACT toy; ARGUED in general]. That regime is excluded near matter [ARGUED].
- **Otherwise only consistent.** With small chances any τ ≤ a/c works, down to the continuous limit. The owner's τ = a/c is the marginal case of D30.

## 4. Checks

Every run: `run.sh` (nice 10, four thread caps = 1, 55 s alarm, load gate < 6). Loads at the runs were 1.8–5.3. Every run took ≤ 1.41 s and peaked at ≤ 75 MB.

| Script | Toy | What it checks | Key numbers | Tolerance |
|---|---|---|---|---|
| `c1_phase_readability.py` (0.20 s, 33 MB) | One excitation on rings L = 12 and 16; detectors with one-site weights; c = γτ, γ = 0.5, T = 10; exact single-particle evolution plus exact non-Hermitian continuum integral | D2–D4: phase readability scales ∝ τ; the lemma bound; global offset; regime with change per tick 1 | TV/τ: 0.0070 and 0.0083 (phase shift), 0.037 (ticked vs continuum), 0.0082 (ramp), 0.0098 (random); bound 5.3τ holds; stationary start: global shift ≤ 2.2e-15, relative 0.0057τ and 0.0015τ; change per tick 1 and chance 1: ≤ 0.0153 | Probability sums to 1 within 1.2e-14 |
| `c2_front_ramps.py` (0.82 s, 36 MB) | Classical gated growth; 1D renewal; 2D first-passage (Dijkstra), 241² sites | D7: chains along rising phases; exact 1D formula; O(F) speed changes | Formula vs MC within 0.8%; 2D F = 1: reach (+x, −x) 12, 12 (global), 60, 15 (ramp), 27.5, 28.0 (random); sites 313 / 916 / 2401; 2D small-F speed-up ≈ 1.2F | Monte Carlo error (8–20 repetitions) |
| `c3_lapse_pacing.py` (0.27 s, 66 MB) | C1's ring at uniform lapse N, run for proper time 10; 900-site chain with a lapse ramp | D10–D12: local position invariance; two clocks; transparency | Lapse-paced ≤ 2.6e-13; global tick with lapse-weighted chance: TV = 0.037·τ₀(1−N); fixed chance: 0.045 / 0.090 / 0.124; ramp reflection 3.8e-5 (step 0.076) | Norm 1 to 1e-12 |
| `c4_same_tick.py` (0.12 s, 33 MB) | 5 qubits, random entangled start; formation at neighbours 1 and 2 | D24–D27: commutation, order effects, readings, no signalling | One-site weights ≤ 7e-17; star weights 0.0437c²; readings 0.0593c²; no-signalling ≤ 3.1e-16; completeness 9e-15 | Machine precision (an eigenvalue clip at 1e-12 avoids spurious square roots) |
| `c5_tick_vs_grid.py` (0.80 s, 75 MB) | Bessel sums in 1D and 3D (L1); two-level Zeno toy (Stein equation) | D30, D33, D35 | See D30, D33 and D35 | Norms 1 to 1e-12 |
| `c6_moving_clocks.py` (0.38 s, 32 MB) | Continuous-time lattice Dirac (1D 2×2, 3D 4×4); random positive weights | D20, D21 | R = √(1−v²/cos²k) to 6.4e-10; 3D formula to 8.8e-11; ⟨σ_z⟩ = m/ω; best dilating fraction 0.500000 | Finite-difference step 1e-6 |
| `c7_dust_drift.py` (0.09 s, 27 MB) | Classical master equation, 101 sites | D15 | Stationary density ∝ N, 1/N or uniform to ≤ 5.2e-15 | Machine precision |
| `c8_mirror_contrast.py` (1.41 s, 34 MB) | 400-site chain: A15 handshake brickwork vs Option R with out-of-step detectors | D5, D4 | Handshake: beyond seam = initial tail 1.714e-11 (no-seam control 0.147); Option R: 0.816–0.818, offset-independent to 2e-12; B-detector share shifts 2.9e-5 → 7.0e-6 ∝ τ | Norm to 1e-12 |

**First-run problems, fixed.**
- `c4` first used a clipped eigen-decomposition square root that left spurious null-space components. The order differences for one-site weights then showed 1e-11 to 1e-13 instead of 0. A 1e-12 eigenvalue threshold fixed it.
- `c3` first used N = 0.9 with a non-integer number of ticks. The boundary tick made TV non-monotone in τ₀. Values of N giving whole tick counts were used instead.
- `c5`'s first Zeno routine iterated tick by tick and was replaced by the exact Stein-equation sum before any timed run.

**Not run (would help).**
- Many-body interacting tests of D2's tightness and of D4's order-ωτ suppression with gentle records.
- A 3D first-passage version of D7.
- A many-site Zeno window with gated formation under A28's transparency bounds.

## 5. Real-physics match

**Comparators.** These are not adopted. All are from memory except the two that A5 checked online.

| Comparator | Value | Source |
|---|---|---|
| Gamma-ray-burst time of flight | E_QG,1 > 10 E_P, E_QG,2 > 6e-8 E_P | LHAASO, GRB 221009A (A5, online) |
| Gamma-ray-burst time of flight | E_QG,1 ≳ 1.2 E_P | Fermi, GRB 090510 |
| Vacuum birefringence | ξ ≲ 3.4e-16 | GRB 061122 (A5, online) |
| Moving-clock dilation | \|α̂\| ≲ 2e-8 | Ives–Stilwell with Li⁺ at 0.34c (Botermann et al. 2014) |
| Moving-clock dilation | Muon storage-ring lifetimes dilate by γ to about 1e-3 | Muon storage rings |
| Gravitational redshift | To 1.4e-4 | Gravity Probe A |
| Gravitational redshift | To about 2.5e-5 | Galileo 5 and 6 (2018) |
| Gravitational redshift | 33 cm height differences resolved | Optical clocks (Chou et al. 2010) |
| Universality of redshift across clock types | About 1e-6 | Null redshift tests |
| Earth's speed against the cosmic-background frame | About 370 km/s | — |
| Preferred frame of collapse models | GRW and CSL; relativistic versions by Tumulka, Bedingham, Pearle | — |
| Quantum Zeno effect | — | Misra–Sudarshan; Itano et al. 1990 |
| Airy edge of Bessel functions | — | DLMF 10.19 |

**What the tick in Option R gives against them.**
- **Propagation bounds.**
  - The tick contributes nothing at any order (D18), so there is no conflict.
  - These bounds constrain H's own lattice dispersion instead. Per A5 T6.4, quadratic cubic-anisotropic dispersion is allowed up to a ≲ 1e7 l_P, and linear terms are excluded by symmetry for two-band blocks.
  - This contrasts with ticked change, where a linear split from step ordering would be excluded unless τ ≪ t_P (A5).
- **Moving-clock dilation.** Possibility clocks slow as in D21, with corrections of about 1e-38 to 1e-39 at laboratory momenta. This passes Ives–Stilwell and muon-ring data by more than 25 orders of magnitude.
- **Redshift.** Universal under D13(A). If chances are not lapse-weighted, formation-limited clocks are off by ΔΦ/c² (about 7e-10 at Earth's surface). No clock tested so far is formation-limited [ARGUED].
- **Frame effects on record statistics.** ≲ 1e-22 per record event at Planck ticks (D19). No conflict, and no prediction within reach.
- **The schedule's own frame (D20).** Present structurally, at v²/4c² to v²/2c² of formation-limited counting. It is unobservable at formation rates already bounded by heating (A24, A28: ≲ 4e-48 per nucleon per second for sharp records).

**Falsifiers.**
1. An energy-dependent light speed or vacuum birefringence traced to time discreteness. This would contradict D18. It would point to ticked change (A5) or to H's own dispersion, not to Option R's record tick.
2. A clock-type dependence of gravitational redshift involving any clock whose rate is set by record formation. This would contradict D13(A), the requirement that formation chances follow the lapse.
3. A sidereal or annual modulation, at order (v/c)² against the cosmic-background frame, of how fast records form in a moving apparatus, beyond D20's predicted lattice-frame share. Equally, its absence at a level where formation-limited counting is identified would require weights that are non-local or not positive.
4. Reflection or opacity of light at smooth gravitational gradients. This would contradict D10.
5. Order-1 fractions of exactly coincident neighbouring records, or blindness of records to particular frequencies. These would point to order-1 chances per tick (D23, D28, D33), which near matter conflict with A28's transparency bounds.

## 6. Open edges

1. **Joint per-site instrument across phase seams.** Build formation, claims, start-of-tick gating and a C40 admissibility filter evaluated at each instrument's instant, under neighbourhood phases. Test exclusion and the probabilistic cone (D6, D7).
2. **Tightness and size.** Test D2's lemma with interactions and many records, and D4's order-ωτ suppression for gentle (settled, A24) records when the change per tick is of order 1.
3. **Where a phase is kept.** Can one qubit per site carry a clock phase without disturbing its content (C54), or is per-site memory (decision 9) the cheaper choice (D8)?
4. **Proper-time formation for moving systems (D20).** Go beyond the two-band toy: many-body, momentum-dependent blocks, non-bilinear weights. Is a lattice-frame share of formation unavoidable for positive local weights? Which observables, if any, are formation-limited?
5. **Step pacing across gradients (D15).** Settle the claimant, record or bond convention, and work out its consequences for record dust near masses and for A30's jam surfaces.
6. **Allowed region of tick and chance.** Run a many-site Zeno-window toy with gated formation under A28's transparency bounds to map the allowed (τ, c) region (D33, D34).
7. **The 3D record cone against isotropic light** (D31). Would claims across face diagonals change the matched tick?
8. **Near N → 0 (A30).** With lapse-weighted chances, formation stops in coordinate time; with lapse-paced ticks, the ticks stop. Both fit "time stops"; check them against A30's surface records.

**Owner decisions surfaced.** Each is framed as yours to make; none is adopted.
- P1 or P1′: does the chance per tick scale with the tick's length?
- One global tick (no memory) or neighbourhood ticks (needing memory, decision 9).
- P2: gating at each site's own instant (the cone softens), or a memory of the previous tick's pattern.
- P3: which lapse paces a record's step.
- P4: start-of-tick or within-tick reading for same-tick neighbours.
- P5: does formation follow proper time? At least the gravity part can be exact.

## 7. Plain-language summary

**The option.** Records form and step only on ticks, while the shared possibilities change smoothly all the time. In this option the possibilities never notice the ticks. The trouble that out-of-step ticks caused in the earlier ticked toys simply goes away: no walls bounce things back, and no places get stuck waiting for each other.

**Global or neighbourhood?**
- A tick written into the rule itself has to be the same everywhere, because the rule treats every place alike.
- Ticks that differ from place to place are allowed, but each place would then have to remember where it is in its own cycle. That is your small-memory question again.
- Neighbourhood ticks would also let a chain of new records run a little faster than one place per tick, along places whose ticks come one after another.
- Whichever choice is made shows up in the records only in proportion to how likely a record is on any single tick. On the finest grid that is far too small ever to see.

**Constant or influenced?**
- The tick can be influenced, most naturally by the same slowing near heavy bodies that already slows the change of possibilities.
- What must follow that slowing exactly is how often records actually form. Otherwise a clock that counts records and a clock made from the possibilities would disagree about how much time passed near a heavy body.
- Whether the ticks themselves follow the slowing matters only at that unseeable level.

**The match to real physics.**
- The ticks never touch how light and matter travel through empty space. So the very precise tests of Einstein's relativity, using light from distant explosions, say nothing against them.
- Moving clocks and clocks held low near a heavy body slow by the usual amounts.
- The one leftover trace is that record forming keeps a slight preference for the grid's own resting frame. Nothing measured so far could detect it.

**Same tick.** Two records can form on the same tick with no problem at all. With realistic odds, though, it almost never happens.

**Minimum distance and minimum tick.** This comes out of the rules in one case only.
- Suppose every tick carried a real chance of a record, not a tiny one. Then ticks much shorter than the time light needs to cross one grid step would freeze things next to records, and much longer ticks would let things outrun the records. That would pin the tick to about that crossing time.
- But odds that large would make ordinary glass and water cloudy.
- So as things stand, the tick is only limited from above by that crossing time.

---

## ERRATA from the fourth hostile review (A34/REVIEW.md), added by the coordinator

- Line ~55: add 'or, up to an unreadable global shift, a two-sub-grid checkerboard (A16 C7's cost)' (C77).
- Line ~339: prefix 'For left–right-symmetric weights (d = 0),' (C82).
- Line ~456: the optima are 0.244 and 0.037; for small c, τ* ≈ c/(2√2 J). 0.050 was a grid-edge artifact (C79).
- D36: no minimum tick follows; a longest allowed tick follows given the premises. A 'pinned' tick needs order-1 chances plus an aim of near-fastest recording (C79).
- D21 assumes Dirac-like (two-band) matter, which over the calm background needs the painted sign pattern (C80).
- D2 scope: the constant 4 assumes a two-outcome menu; first order in δ; H_∂S covers the whole support's boundary; one limit per finite window; global offset unreadable for stationary preparations (C81).
- D24's example weight breeds next to −n records (C83).
