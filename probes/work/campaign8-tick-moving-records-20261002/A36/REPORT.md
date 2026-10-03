*(Saved by the coordinator from the agent's final message; the agent's sandbox blocked it from writing REPORT.md.)*

# A36 report: ticks timed by the records around each spot

**Scratch directory:** `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A36/`
- Scripts `c1`–`c6`, outputs `out_*.txt`, timings `time_*.txt`.
- Wrapper `run.sh`: `nice -n 10`, the four thread caps at 1, a 55 s alarm inside each script, and a load gate (1-minute load must be below 6).
- Loads at the runs were 2.1–3.2, and no run was skipped. Every final run took ≤ 9.1 s and peaked at ≤ 140 MB. One first run went over the 300 MB cap (section 4).
- No git operations, no repo edits, no subagents, no review or audit lanes.

**Status.**
- Every rule below is a supplied toy or a named conditional, not framework content.
- The owner's tick ideas (I1, I2, "influenced", "by neighbourhood") are instincts, not positions. Nothing here adopts records forming on a beat.
- The record-tick shape (Option R, A27; narrowed by A29 and A34) is itself a candidate.

**Grades.**
- **EXACT**: proof, or exact arithmetic or enumeration.
- **CHECKED**: numerics in a stated toy, with a tolerance.
- **ARGUED**: reasoning without proof.
- **SUPPLIED**: a premise put in by hand.
- **COMPARATOR**: literature or experiment, from memory, never adopted.

## 1. Question

Work in the record-tick shape:
- records form and step only when record instruments act;
- the possibilities change smoothly under the compressed change H_R;
- A28's gate applies where stated: no formation without a recorded neighbour.

The question is whether a spot's instrument times can be set by the permanent records around it, so that ticks are:
- set,
- different from neighbourhood to neighbourhood, and
- influenced by their surroundings,

with no per-site memory beyond the records.

More specifically:
- What can such a rule use?
- What follows for covariance, no-signalling, the record cone, readability, gating and the claim rule?
- Does "influenced" then mean "influenced by matter"? How does that compare with gravitational slowing and A32 D13?
- What happens in empty space?
- How well does this fit the owner's instinct?

## 2. Answer

**Conditional yes.** The construction is EXACT, and its need for a shared clock is EXACT given the named premises. The physics readings are ARGUED and the numbers CHECKED. One supplied item cannot be avoided: a shared clock.

**1. What a rule can use** [EXACT; enumeration CHECKED].
- It can use the records within its range: where they sit and what they hold.
  - In 3D there are 10 recorded-neighbour patterns up to the 24 turns; 9 of them have the gate open.
  - With contents on one axis (empty, r or −r) there are 57 patterns. If turning the possibilities alone is also allowed, there are 33.
- It can use a clock written into the law, if one is supplied.
- It cannot use formation times, because records carry no time.
- It cannot use the possibilities.
  - A set time that depends on them lets a distant choice steer local records: TV 0.090–0.443 in C1, against ≤ 2.9e-16 for record-set times.
  - Depending on them linearly only gives formation odds, which means random times.

**2. Set times need a shared clock** [EXACT, given Q2's snapshot rule, no-signalling and no memory].
- Records do not change between record events, so on their own they cannot mark a later moment.
- Without a shared clock and without memory, the only set instants are the record events themselves (zero-delay triggers). Every other formation time is random.
- Zero-delay triggers let one record set off a chain of new records at a single instant [EXACT; CHECKED].
  - In 1D the chain reaches d sites with probability F^d.
  - In 3D the chain becomes unbounded with positive probability once F is above about 0.31 (COMPARATOR threshold). 73% of runs reached the box edge at F = 0.35, and all of them did at 0.45.

**3. With a shared clock, record-timed ticks exist without memory** [EXACT by construction].
- Each spot acts at those instants of a shared, numbered cycle (a "dial") that the pattern of its recorded neighbours selects.
- This is covariant and set. It varies by neighbourhood, is influenced by records, needs no per-site memory, and puts no spatial pattern into the law.
- A28's gate is the one-instant case: the records only switch the shared tick on or off.
- This answers A34 C77(iii) and open question 5. A record-set tick is a neighbourhood choice among the instants of a global clock.

**4. Consequences.**
- **Cone** [EXACT; CHECKED].
  - At most one site per instant of the shared clock.
  - Per cycle, a chain can advance as many sites as the cycle has distinct instants in use.
  - The cone's shape follows the rule's table: at F = 1 the octahedron becomes a cube.
  - At small chances the speed changes only at O(F).
- **I2.** "One step per tick" holds per instant of the shared clock. Per spot cycle it would need memory [EXACT].
- **No signalling** [EXACT; CHECKED ≤ 2.9e-16].
- **Readability** [the bound is EXACT for fixed schedules (A32 D2); its extension here is ARGUED; CHECKED].
  - If the chance per firing scales with the interval (P1), the schedule shows only at order c and order ωτ. In C3 that was ≤ 0.025τ per record event.
  - If the chance per firing is fixed (P1′), record-set periods change formation rates at order 1: TV about 0.053, not falling with τ.
  - The process then equals, up to O(τ), one with **record-dependent formation odds and no set ticks**: TV 0.043τ.
  - At leading order, an influenced tick is an influenced chance.
- **Gating and claims** [EXACT].
  - The rule is needed exactly where the gate is open.
  - Spots of different classes never act together, so the class instants give a covariant, memoryless order for neighbouring instruments.
  - At contested claims the first instant wins, which shifts outcomes at order c².

**5. "Influenced" means by the records next door, not by gravity** [EXACT range statements; ARGUED synthesis].
- The tick feels only records within one site, which is recorded matter in contact.
- It does not depend on distant mass, so it cannot follow the potential.
- Its sign is a free choice.
- Its natural size is order 1 per pattern. A redshift-sized step would need a dial of at least about 1e9 positions, and a rule that knows the mass.
- With fixed chances per tick it conflicts with A32 D13(A), that is P5: clocks that count records would run at rates set by how crowded their spot is.
- With P1 and lapse-weighted chances there is no conflict, and no leading-order influence either.
- Long-range influence reaches formation only through the odds carried by the possibilities, never through set ticks.
- The possibilities next to records do ring at pitches the records set, and formation odds lock onto that ringing (C6: Ω = J√((k_x − k_z)² + 4)).
  - But the times stay random: the best spread found is 0.23 of a period.
  - In the calm aligned sector nothing rings.

**6. Empty space** [EXACT given gating].
- Far from records nothing sets a tick and nothing forms, so the rule needs no value there. That is consistent.
- A void's only time is the change's own parameter, which light takes to cross it.
- No record-time accumulates there. The crossing time is readable only through records at the void's edges.

**Fit with the instinct** [ARGUED from the EXACT steps]. "Records form at set ticks", "the tick varies by neighbourhood" and "influenced by its surroundings" can hold together. This needs neither memory nor a spatial pattern in the law. Three provisos:
- **The variation needs a shared clock.** The tick varies by neighbourhood only as the records' choice among the instants of a clock the law supplies.
- **The influence is local.** It comes only from records in contact.
- **The influence is nearly invisible.** It shows in records only at order c and ωτ, unless the chance per tick is fixed. In that case it acts like formation odds set by records.

The supplied list is in D13.

## 3. Derivation

### 3.0 Setup [SUPPLIED] and named conditionals

**The record-tick shape** (as in A32 §3.0):
- the snapshot is the records plus the shared possibilities ρ;
- between instrument actions, ρ evolves under e^{−iH_R s};
- formation is a linear local instrument with weight F, with Kraus operators P_k√F and √(1−F);
- steps use SW, claims use CL, and A28's gate applies.

A32's named conditionals carry over:
- **P1:** the chance per tick scales with the tick's length.
- **P2:** gating uses the records present at the instrument's own instant.
- **P3:** step pacing.
- **P4:** the same-tick reading.
- **P5:** formation follows proper time.

**New named conditionals.**
- **RT1 (inputs).** The timing rule at an empty spot x is a function of the record configuration within distance 1 of x: which neighbours hold records, and their contents. A28's gate uses the record pattern the same way.
- **RT2 (shared clock).** The law has instants t_j = jτ_f and a dial position j mod L. L = 1 is the plain global tick.
- **RT3 (table).** A covariant table S gives each pattern class C a set S(C) ⊆ Z_L of dial positions.
  - Spot x acts at instant j if j mod L ∈ S(C(R_x)).
  - R_x is taken at the start of instant j (P2, P4).

**Definitions.**
- **"Set"** means that, given the record history, the instants at which a spot's instrument acts are fixed. There is no randomness and no dependence on the possibilities. This is A32's sense (D8b counts random times as "no set ticks").
- **"Memory"** means any per-spot state beyond the records and the possibilities, including pending timers.

### 3.1 What a rule can use

**D1. Records carry no time** [EXACT, textual and by example].
- The Record axiom says a record "locks exactly one admissible local possibility", and that "a readout value is determined by record content alone".
- The content is an element of the site's possibility domain M_2(C). A formation time is not.
- Example: two neighbouring records formed in either order give the same configuration of sites and contents. So the order cannot be recovered from a snapshot.
- A stamp could enter content only if the law made menus depend on a shared clock [ARGUED].
  - That would be a supplied, time-dependent menu rule.
  - It would need a frame taken from records, to avoid privileging a possibility.
- In the quiet class, where contents are ±n, there is no room for a stamp at all [EXACT]. The sign is the formation outcome.

**D2. Set times cannot depend on the possibilities** [EXACT, using the standard steering theorem (COMPARATOR: Schrödinger; Hughston–Jozsa–Wootters 1993); CHECKED].
- **Setup.** Let δ(ρ) ∈ {0, 1} decide whether x's instrument acts at an instant, given the snapshot.
- **(a) Affine means constant.**
  - Suppose δ is affine in ρ, as A9 Theorem 1 requires for outcome laws.
  - A {0,1}-valued affine function on a convex set is constant: the midpoint of states with values 0 and 1 would have value ½.
- **(b) The direct argument.** Suppose δ(ρ₀) = 0 and δ(ρ₁) = 1 for two states compatible with the records.
  - When x's possibilities are suitably shared with a distant site (Q1), a distant record can leave x's snapshot in ρ₀ or in ρ₁. With no distant record, it stays at their average.
  - Whether x's instrument acts then depends on the distant choice.
  - The local record law changes with it whenever acting matters, that is whenever tr(Fρ) > 0.
- **Hence** set times can depend only on records and on a clock written into the law.
- A linear dependence on ρ is a formation weight (A32 D8c), and its times are random.
- **CHECKED (C1).**
  - A tick set by the possibilities ("act whenever ⟨n_x⟩ ≥ 0.5") moves the local record law by TV 0.090–0.443 across a distant choice (no record, a Z record, or an X record).
  - The record-set tick moves it by ≤ 2.9e-16.

**D3. Records are constant between record events** [EXACT]. Records are permanent and move only by steps, which are record events. So the record configuration near x is constant between record events there.

**D4. What remains without a shared clock** [EXACT, given Q2's snapshot rule, D2 and no memory].
- **The argument.**
  - Without a clock in the law, x's set decision at instant t is a function of the records near x (D2).
  - Those records are constant between record events (D3).
  - So isolated set instants can only be record-event instants: zero-delay triggers.
  - Otherwise the instrument acts at a rate. That is a formation weight, with random times.
  - Acting at every instant with a fixed chance is Zeno freezing; once the chance is rescaled, it becomes a rate.
- **(a) No set schedule.** Without a shared clock and without memory, every formation time is either random (set by a rate) or equal to an earlier record event's time.
- **(b) Delays.** A positive set delay after a record event needs a shared clock or memory (a pending timer). This refines A32 D8(e), "a delay needs memory".
- **(c) No timing by neighbours' actions.** A spot cannot time itself by what its neighbours' instruments do, because an action that forms no record leaves nothing readable. Rules in the style of distributed synchronizers therefore need memory, as A15's waiting clocks needed counters.
- **Premises that can move:**
  - memory (decision 9);
  - a clock written into the law (the record-tick shape already supplies instants);
  - a different reading of Q2.

**D5. Zero-delay triggers** [EXACT; CHECKED].
- **Rule.** When a record forms, each empty neighbour acts at that same instant, once per cascade, with chance F.
- **(a) 1D.** A chain of n formations occurs at one instant with probability F^n per direction.
  - Records then reach distance d with no time elapsed, while the change needs time of order d/v. So the record cone in the change's time is lost.
  - CHECKED: Monte Carlo (2e5 runs) agrees with F^d for d = 1, 3 and 6 at F = 0.3 and 0.6, for example 0.21732 against 0.21600.
- **(b) 3D.** The cascade is a site-percolation cluster around the seed (C5: 61³ box, distance 30 to the edge).

  | F | Mean cascade size (sites) | Runs reaching the box edge |
  |---|---|---|
  | 0.10 | 0.8 | none |
  | 0.20 | 5.0 | none |
  | 0.25 | 9.8 | none |
  | 0.30 | 478 | 10% |
  | 0.35 | 3.99e4 | 73% |
  | 0.45 | 9.67e4 | 100% |

  This is consistent with a threshold near the site-percolation value of about 0.3116 (COMPARATOR).
- **(c) No first event.** Pure triggering has no first event, so it needs rate-timed events as well (D4a).
- **At physical chances** cascades are negligible (A32 D19: c ≲ 5e-35 per Planck tick). The loss of the cone is still structural.

### 3.2 The construction and its consequences

**D6. Record-timed ticks on a shared clock** [EXACT by construction]. Under RT1–RT3:
- **(a) Covariant.** The rule is covariant under the 24 turns whenever S depends only on the class.
- **(b) Set, local, influenced.** It is set given the records, varies by neighbourhood, and is influenced by records.
- **(c) No memory.** The decision at each instant uses only the dial position and the current records.
- **(d) No spatial pattern.**
  - The schedule is a covariant function of the state, not of position.
  - So A32 D8(a) and A34 C77(ii) do not constrain it. (Those say a phase written into the law is uniform, or a two-sub-grid checkerboard.)
  - The clock itself is the same everywhere. What varies is which of its instants each spot uses.
  - A global offset of the clock is unreadable for stationary preparations (A32 D3c).
- **(e) What L allows.**
  - With L = 1, records can only switch the shared tick on or off at a spot. A28's gate is exactly this case.
  - Phase offsets need L ≥ 2.
  - Record-set periods p need p to divide L.
  - Phases that vary continuously with content would need absolute film time, and they lose a finest instant (D7c).
- **(f) What the table can distinguish** [CHECKED by orbit enumeration, C4].
  - Recorded or not, up to the 24 turns: 10 classes, 9 with the gate open.
    - By count k = 0…6 the numbers are 1, 1, 2, 2, 2, 1, 1.
    - In 2D: 6 classes, 5 with the gate open.
  - Empty, r or −r: 57 classes, or 33 if turning the possibilities alone (r ↔ −r) is also a symmetry (unglued, Q3).
  - Exactly one mirror-image pair exists in each count. One member is: −x holds r, −y holds −r, +z holds r, −z holds −r, and +x and +y are empty.
  - So a rule may time mirror-image record patterns differently without breaking the 24-turn covariance. The Lattice axiom names proper turns only.
  - With "recorded or not" alone, there are no mirror pairs.

**D7. The record cone** [EXACT; CHECKED].
- **(a) Strict per instant.** Under start-of-instant gating, a chain of formations or steps advances at most one site per instant of the shared clock. So the L1 reach is at most the number of instants elapsed. C2 asserts this at every instant.
- **(b) Per cycle.** A chain can advance up to the number of distinct instants in use, and the cone's shape follows the table. Results at F = 1 from one seed (C2a):

  | Lattice | Rule | Cycles | Sites | L1 reach | L∞ reach |
  |---|---|---|---|---|---|
  | 2D | one shared tick | 12 | 313 (L1 ball) | 12 | 12 |
  | 2D | phase rising with count k | 12 | 625 = 25² (L∞ ball) | 24 | 12 |
  | 3D | one shared tick | 8 | 833 (octahedron) | 8 | 8 |
  | 3D | phase rising with k | 8 | 4913 = 17³ (cube) | 24 | 8 |
  | 3D | phase falling with k | 8 | 3165 | 15 | 8 |

  With the rising rule, body diagonals in 3D advance three times faster than under one shared tick.
- **(c) No finest instant.** Phases that vary continuously with content have no finest instant. Chains then run along rising phases, as in A32 D7.
- **(d) 1D.** A count-based table times every 1D front site alike (k = 1). So the front moves exactly one site per cycle: A32's renewal formula with w = 1.
- **(e) Small chances.** C2b, 2D, cycles to reach L∞ distance 30. The table gives speed relative to one shared tick.

  | F | Phase rises with k | Phase falls with k | Periods, chance scaled (P1) | Periods, chance fixed (P1′) |
  |---|---|---|---|---|
  | 0.4 | 1.134 | 1.121 | 1.180 | 1.911 |
  | 0.2 | 1.050 | 1.044 | 1.063 | 1.900 |
  | 0.1 | 1.081 | 1.085 | 1.066 | 1.916 |
  | 0.05 | 1.03 ± 0.03 | 1.06 ± 0.03 | 1.05 ± 0.03 | 1.98 ± 0.06 |

  - Within errors, the excess shrinks with F, consistent with an O(F) change (A32 D7).
  - With fixed chances the speed changes by an order-1 factor at every F.
- **(f) I2 per cycle.**
  - A record can be claimed at one instant, and again later in the same cycle by a new neighbour with a later instant.
  - A spot can act twice in one cycle if its class moves to a later instant.
  - So "one step per tick" holds per instant of the shared clock.
  - Per spot cycle it needs a mark of "already stepped", which the snapshot does not hold (D1, D2). That is memory.

**D8. No signalling** [EXACT; CHECKED].
- For a fixed record history h, the instruments and their instants are fixed by h and the dial. So P(h) = tr(K_h ρ K_h†) is linear in ρ.
- Distant operations commute with the local instruments (A9 Theorem 2; A15 S11; A28 Step 4).
- CHECKED (C1):
  - TV ≤ 2.9e-16 across four random states and a Bell pair, at c = 0.3 and 0.8;
  - probabilities sum to 1 within 1.8e-15.

**D9. Readability.** The bound is EXACT for fixed schedules (A32 D2–D4, with C81's scope: first order, per finite window). Its extension to record-set schedules, by the same step-by-step comparison, is ARGUED. C3 checks it.
- **(a) Record-set phases** (one action per cycle per spot).
  - These move instruments by less than a cycle, so under P1 they are readable only at order c and order ωτ per record event.
  - CHECKED (C3): TV(global, record-set phases) = 0.0231τ for τ from 0.4 down to 0.025.
  - At τ = 0.1 and γ from 1 down to 0.0625, the TV per expected record event is ≤ 0.025τ, in units of 1/J.
- **(b) Record-set periods under P1.** The same holds. TV to the continuous limit is 0.0547τ, against 0.0483τ for one shared tick.
- **(c) Record-set periods under P1′** (a fixed chance per firing).
  - The rate per class is c|S(C)|/(Lτ_f), which is readable at order 1.
  - TV to the uniform continuous limit stays at about 0.053 and does not fall with τ: 0.0535 at τ = 0.025, with limit 0.0526.
  - The process does converge at O(τ) to the continuous process with **record-dependent rates** γ(C) = c/T(C): TV = 0.0427τ. This convergence is ARGUED by A32 D3(b)'s product-formula argument, and CHECKED.
  - So at leading order, a record-timed tick with fixed chances is the same as formation odds set by records, with no set ticks. (A9 allows formation odds to depend on records.)
  - The set ticks themselves show only at order c and ωτ.
- **(d) Order-1 chances** [CHECKED, coarse readout].
  - At τ = 0.5, TV(global, phases) = 0.011 at c = 0.5 and 0.005 at c = 1.
  - Nothing small suppresses these (A34 C78).
- **(e) Order-c signatures** [EXACT].
  - Neighbours of different classes never form at the same instant.
  - Take the start-of-instant reading with menus set by records. Then the later neighbour always has its menu set by the earlier one. This gives a class-dependent pattern of coincidences and menu alignment (A32 D9).
  - At order ωτ, a class is blind to oscillations whose period divides its own (A32 D23).

**D10. Gating and claims** [EXACT].
- **(a) Domain.**
  - The timing rule is needed only where the gate is open.
  - The gate's domain (R_x ≠ ∅) is the rule's domain, so no void value is needed.
  - Without gating, the void value would be a shared tick in voids.
- **(b) Shorter waits.** A spot whose gate opens partway through a cycle waits less than a cycle on average. This is the source of D7(e)'s O(F) speed-up.
- **(c) A covariant order.**
  - Only spots of the same class, or of classes sharing an instant, act together.
  - So class instants give a covariant, memoryless order between neighbours of different classes. That settles A32 D25's ordering rule for them.
  - Same-class neighbours still need random order or a joint instrument.
- **(d) Claims (CL).**
  - A record claimed at different instants goes to the first claimant. The uniform pick applies only among claimants at the same instant.
  - Take two claimants, each claiming with chance q.
    - At the same instant, each gets the record with probability q − q²/2.
    - At different instants, the earlier gets it with probability q and the later with q − q².
  - That is a priority bias of order q², which is O(c²).
  - I3 inside a claimant's own instrument is unaffected: P(i | y taken) = w_i/Σw (A32 D6).

### 3.3 What "influenced" can mean

**D11. Influence** [EXACT range statements; ARGUED synthesis].
- **(a) Set ticks** are influenced by records within the rule's range only (D2, D6).
- **(b) Odds** are influenced by the possibilities, linearly.
  - Through H_R these carry long-range influence. For example, a lapse field enters through the weight N̂ ⊗ F (A32 D13).
  - So long-range influence on formation enters through the odds, never through set ticks (EXACT, given D2).
  - Records also do not carry a body's speed (A32 D20), so set ticks cannot follow motion either.
- **(c) Matter in contact, not mass** [EXACT].
  - Records cluster where matter has been recorded. The tick then differs inside recorded matter and in its surface layer, and nowhere else.
  - A site at distance ≥ 2 from all records has no tick, whatever masses are nearby (gating).
  - Two spots with the same record pattern have the same tick, whatever the mass.
  - So the tick cannot follow the potential −GM/r: it has the wrong range and no dependence on M.
- **(d) Sign and size.**
  - The sign is set by the table [SUPPLIED]. For example, "fewer instants per cycle with more recorded neighbours" gives "slower in crowded spots".
  - Rates come in steps of 1/L per cycle. For comparison (COMPARATOR arithmetic), ΔΦ/c² is:
    - ≈ 7.0e-10 at Earth's surface;
    - ≈ 2.1e-6 at the Sun's;
    - ≈ 3.6e-17 for a 33 cm height difference.
  - Mimicking these would need L of about 1e9 to 3e16. It would also need a one-site record rule that knows the height, which it cannot.
- **(e) A32 D13 (P5).**
  - Under P1′, formation per unit proper time is c/(N(x)T(C)).
  - That is universal only if T(C) ∝ 1/N(x), which is impossible: spots of the same class can sit at different lapses.
  - So clocks that count records would disagree with clocks made of the possibilities, by order-1 factors set by how crowded their spot is [EXACT, given P5].
  - Under P1 with lapse-weighted chances (c = γ₀N̂ × interval), D13(A) holds for any table. Only D13(B) fails, at order ωτ [EXACT].
  - So a record-timed tick is compatible with P5 exactly when its influence is invisible at leading order.
- **(f) A6's route** [ARGUED mapping].
  - A record gas captured by a lump has a depletion profile with an exact 1/r tail (A6, CHECKED there).
  - Gate-open time and class counts near x follow the local gas density. So a record-timed tick, or the gate alone, would give formation-limited clocks A6's profile.
  - It inherits A6's results:
    - the right sign and the 1/r shape;
    - a coefficient set by the capture current rather than the mass;
    - β = ½;
    - universality that is not automatic.
  - It is also shot-noisy at one site (A17). In this shape that noise does not touch the change (A32 D1, D16).
- **(g) A pitch tuned by records** [EXACT; CHECKED, C6].
  - Records shape H_R, so the possibilities next to records ring at pitches the records set. Linear weights lock formation onto that ringing.
  - The Heisenberg toy: one excitation is shared between unrecorded neighbours x and z, which have k_x and k_z recorded neighbours with content r.
    - The excitation rings at Ω = J√((k_x − k_z)² + 4), matching the spectrum to 1e-6.
    - The peak spacing of the formation-time density matches 2π/Ω to within 4e-4, limited by the 1e-3 time grid.
  - This needs no memory and no shared clock, and it varies by neighbourhood. But the times are random:
    - the smallest spread found is 0.226 of a period, at γ = 2.67J;
    - at γ = 0.05J the spread is 11.6 periods.
  - In the calm aligned sector nothing rings, because aligned states are stationary under fields along r.

### 3.4 Empty space

**D12. Voids** [EXACT given gating; ARGUED reading].
- **(a) No rule needed.**
  - A spot with no recorded neighbour has no class, no tick and, under gating, no formation.
  - Sites at distance ≥ 3 see no instrument (A28 Step 2).
  - The rule needs no value there.
- **(b) What time a void has.**
  - The change continues in a void: e^{−iHt} on average. Per outcome, it changes at once to agree with distant records (Q1, C74).
  - So a void has the change's parameter (Q2's film) but accumulates no record-time.
  - Light takes film time to cross it. That time is readable only at the void's edges, through records formed there.
- **(c) A jam is the opposite (I5).**
  - Every spot has six recorded neighbours, so it has a class and a tick.
  - But nothing can form or step, and the compressed change has nothing left to move.
  - Both kinds of clock stop (A27 Step 10).
- **(d) The clock in voids.** A supplied shared clock exists everywhere in the law, but nothing uses it in voids. Without one, a void has no instants at all, only the smooth change.

### 3.5 Fit with the owner's instinct

**D13. Fit** [ARGUED synthesis of the EXACT steps].
- **"Records form at set ticks" (I1).** Without memory, this requires a shared clock (D4).
- **"The tick varies by neighbourhood".** It can: records choose which instants each spot uses (D6). The cone then belongs to the clock's instants, not to each spot's cycle (D7).
- **"Influenced by its surroundings".** Yes, by the records within one site (D6). Not by the possibilities (D2), and not by distant matter (D11c).
- **Without the shared clock.** Only zero-delay triggers (D5) or random times (D4, D11g) remain.

**What is supplied.**
1. The shared clock: instants, plus a dial of L positions for phases or periods.
2. The class table S.
3. P1 or P1′.
4. P2 and P4, the start-of-instant reading.
5. The claim convention across instants.
6. An order for overlapping instruments of the same class.
7. A28's gate and the starting set of records, as before.

**What is not supplied.** Per-site memory, and any spatial pattern in the law.

**Corrections to earlier wording.**
- A32 D8(e): "a delay needs memory" becomes "a delay needs memory or a shared clock".
- The draft says "ticks set by the surrounding records were not tried" (lines 26 and 161, decision 18). They are now tried.
- The draft also says "Set ticks that differ by place needed a per-place memory in every construction tried". That no longer holds as written: D6 is a memoryless construction, on a shared clock.

## 4. Checks

Every run used `run.sh`: `nice -n 10`, four thread caps at 1, a 55 s alarm and a load gate below 6. Loads at the runs were 2.1–3.2.

| Script | Toy | Checks | Key numbers | Tolerance | Time, memory |
|---|---|---|---|---|---|
| `c1_signalling.py` | 4 qubits (distant b; chain y–x–z); compressed Heisenberg change; two permanent \|0⟩ records; gated weight c\|1⟩⟨1\|. Instants 0 or τ/2 set by recorded-neighbour count, against x acting when ⟨n_x⟩ ≥ 0.5. b chooses none, Z or X | D2, D8 | Record-set: ≤ 2.9e-16 (4 random states and a Bell pair; c = 0.3, 0.8). Possibility-set: 0.090–0.443 | Probabilities sum to 1 within 1.8e-15 | 0.50 s, 33 MB |
| `c2_record_cone.py` | Classical gated growth in 2D and 3D from one seed. Rules: one shared tick; phase rising or falling with k; periods with chance scaled (P1) or fixed (P1′) | D7 | Tables in D7(b) and D7(e); strict bound asserted at every instant | Monte Carlo, 40/40/30/16 repetitions | 9.0 s, 37 MB |
| `c3_readability.py` | Ring L = 10, two hard-core excitations starting at sites 3 and 6; permanent \|0⟩ record at 0; compressed hopping; gated c\|1⟩⟨1\|; classes by neighbour content. Exact classical–quantum evolution; continuous limit by sparse exponential | D9 | TV/τ at τ = 0.025: 0.0231 (global vs phases), 0.0483 (global vs continuous), 0.0547 (P1 periods vs continuous), 0.0427 (P1′ periods vs record-dependent rates). P1′ vs uniform about 0.053, not falling. Per event ≤ 0.025τ. At c = 0.5 and 1: 0.011 and 0.005 | Probabilities sum to 1 within 9e-15 | 1.05 s, 140 MB |
| `c4_classes.py` | Orbits of neighbour patterns under the 24 (and 48) turns | D6(f) | 10 classes (9 gate-open); by k: 1,1,2,2,2,1,1; 57/56 and 33/32; one mirror pair; 2D: 6 (5) | Exact enumeration | 0.09 s, 27 MB |
| `c5_trigger_cascades.py` | Zero-delay triggered formation: 1D Monte Carlo against F^d; 3D 61³ clusters by labelling | D5 | 1D within Monte Carlo error; 3D share reaching the box edge 0, 0, 0, 0.10, 0.73, 1.00 for F = 0.10–0.45 | 2e5 runs (1D); 20–30 runs (3D) | 0.89 s, 106 MB |
| `c6_tuned_clock.py` | Heisenberg excitation on x–z beside k_x and k_z records with content r; continuous formation at x on \|−r⟩ | D11(g) | Ω formula to 1e-6; peak spacing within 4e-4 of 2π/Ω; smallest spread 0.226 periods at γ = 2.67J | Time grid 1e-3 | 0.44 s, 67 MB |

**First-run problems, fixed.**
- **The first `c3` run broke the memory cap.**
  - It peaked at 437 MB (over the 300 MB cap) because it used a dense exponential of a 1427×1427 generator. It finished in 3.4 s.
  - It was replaced by a sparse exponential-times-vector. Every printed number is identical, and the peak is now 140 MB.
- **`c2b` was too noisy at first.** The first run used 8/6/4 repetitions and its ratios were inconclusive. The rerun used 40/40/30/16.
- **`c6` had its two diagonal energies swapped** relative to its basis labels. The outputs are symmetric under the swap, and they were identical after the fix (diffed).

**Not run (would help).**
- 3D growth at small chance with class tables.
- A joint per-site instrument (form, claim or nothing) on a dial.
- An A6 record gas with a record-timed tick.
- Tables that depend continuously on content.

## 5. Real-physics match

**Comparators.** None is adopted; all are from memory.

| Comparator | Relevance |
|---|---|
| Lamport logical clocks (1978); vector clocks (Fidge; Mattern 1988) | Event-driven local clocks keep a counter per process, which is memory (D4b, D4c) |
| Synchronizers (Awerbuch 1985) | Per-node pulse counters (D4c) |
| Causal sets with classical sequential growth (Bombelli–Lee–Meyer–Sorkin 1987; Rideout–Sorkin 2000) | Time as the order of births with no global clock, though the growth has a labelled birth order (compare D5) |
| Site and bond percolation thresholds on the simple cubic lattice, about 0.3116 and 0.2488 | D5 |
| Steering; Hughston–Jozsa–Wootters (1993) | D2 |
| Waiting-time distributions with Rabi oscillations in resonance fluorescence (quantum jumps; Cohen-Tannoudji–Dalibard 1986; Carmichael) | The C6 analogue |
| Local position invariance and universality of redshift: Gravity Probe A; Galileo 5 and 6; optical clocks 33 cm apart (Chou et al. 2010); null redshift tests at about 1e-6 | D11 |
| Relational time (Page–Wootters 1983) | D12 |
| Detector dead time | Memory held by matter |

**What follows.**
- **With small chances per tick (P1),** a record-timed tick adds nothing measurable.
  - Its traces are of order c: ≲ 5e-35 per event at Planck ticks (A32 D19).
  - They are also of order ωτ: ≲ 1e-19 at GeV.
- **With fixed chances (P1′),** formation-limited counting would depend, at order 1, on how crowded a spot is with records.
  - No tested clock is formation-limited (A32), so this does not conflict with data.
  - It would break local position invariance for such clocks.
- **It is not gravity.** In this shape, the redshift measured in empty space above Earth (Gravity Probe A, Galileo) must come from the change's lapse and lapse-weighted odds (A32 D13), not from a record-timed tick (D11c).

**Falsifiers.**
1. **A formation-limited clock whose rate depends on its recorded surroundings at order 1.** Finding one would favour P1′ tables. Its absence, where such clocks are identified, would favour P1 or no table.
2. **Superluminal chains of correlated records forming at one instant across distance.** Zero-delay triggers predict these with probability about F^d (D5). Spacelike Bell tests show no such influence (COMPARATOR), which fits only if chances are tiny.
3. **A clock-type dependence of gravitational redshift traced to record crowding** (D11e under P1′).
4. **Pattern-dependent coincidences or frequency blindness.** These would be order-1 coincidences of neighbouring records, or frequency blindness, that depend on the record pattern (D9e). They point to order-1 chances, which A28 and A34 C79 already disfavour.

## 6. Open edges

1. **A joint per-site instrument on a dial.**
   - Build the instrument (form, claim or nothing) with record-set instants, start-of-instant gating and a C40-type admissibility filter.
   - Test exclusion, I2 per instant, and the same-class ordering rule (D7f, D10).
2. **Can the shared clock be avoided?** D2 rules out exactly set times from the possibilities. Two follow-ups remain:
   - What spread can a ringing tuned by records reach in many-body toys? One toy reached 0.23 of a period at best (C6).
   - Is that ringing absent in the calm sector in general, not only in the aligned product case (D11g)?
3. **Tables that depend continuously on content,** such as the angles between neighbours' contents. These need absolute film time and lose the finest instant. The probabilistic cone should be mapped (D7c).
4. **A handed table.** There is one mirror-image pair among the patterns with contents (D6f). Could a record-timed rule bias handedness? This connects to the chirality lanes and is untested.
5. **An A6 record gas with a record-timed tick, as a package.** Work out its profile, its noise for record-counting clocks, and its compatibility with P5 (D11f).
6. **Zero-delay triggers at physical chances.**
   - Compare the cascade's leak in film time with the change's Lieb–Robinson tail.
   - Any cap on cascades without memory runs into D4.
7. **3D growth at small chance under class tables.** Map how much the shape of the probabilistic cone depends on direction.

**Owner decisions surfaced.** Each is yours to make; none is adopted.
- **The backbone.** If set ticks are kept, is a shared clock acceptable underneath them? Without one there are no set ticks, or only zero-delay chains.
- **The table.** If a shared clock is kept, should it be L = 1, where records only switch it on or off as the gate already does? Or a numbered cycle with instants chosen by the records?
- **P1 or P1′.** A fixed chance per tick makes the record-set rate readable and, at leading order, equivalent to formation odds set by records. It conflicts with P5.
- **What "one step per tick" (I2) refers to.** The shared clock's instant, or a spot's own cycle? The latter needs memory.
- **Zero-delay triggers.** Are they allowed? They break the record cone in film time.

## 7. Plain-language summary

Can the tick vary by neighbourhood and be influenced without memory? Yes, but only on top of one shared clock. Records never change once made and carry no time of their own, so on their own they cannot mark a later moment. What they can do is choose which instants of a shared clock each spot uses: a spot with one recorded neighbour might use the first instant of each round, and a spot with two the second. That needs no memory, because the records stay where they are, and it treats every place and direction alike. Without a shared clock, the only set moments records give are the moments new records form. Then one record could set off a chain that records a whole region at a single moment, if the chance of each new record is high enough. The ticks can be influenced only by the records right next to a spot. They cannot be influenced by the unrecorded possibilities, because that would let a faraway choice send a message. Nor can they be influenced by a heavy body farther away, so this is not gravity's slowing. If each tick's chance of a record stays fixed, clocks that count records would run at different rates depending on how crowded their spot is, which clashes with all clocks slowing together. If instead the chance shrinks with the tick's length, the influence all but vanishes from what records show. Far from all records nothing sets a tick and nothing forms, which fits. The possibilities still change there, and that change is the only time empty space has.

---

## ERRATA from review round 7 (A34/REVIEW3.md), added by the coordinator

- D2: add 'given no-signalling (Campaign 7 sentence 4, unadopted)' (C107).
- D9(c) and Answer: 'odds' should be 'rates'. Admissibility's odds concern which possibility a forming record locks, not the rate of forming (reading note 2). The fixed-chance case means the same chance per firing for every class (C107).
- D7(e): the O(F) speed-up is confirmed by A34 c8 (excess about 0.34F); the F = 0.1 point was a fluctuation (C107).
- D12(c): a full jam has no empty spots, and gravity's clocks inside are open (C66) (C107).
- D13: add the rule's range (RT1) to the supplied list (C107).
- D6: the numbered cycle is a pattern in time; I2 holds per instant of the shared clock, not per spot's cycle (C101).
- Cross-lane: ticks cannot follow a lapse carried by the shared possibilities (D2 + A31 K4(b)); only the chances can (C100).
- The 57 classes assume the law tells r from −r (a privileged possibility); with an inherited axis, 33 (C105).
