# A34 review round 3: A36 (record-timed ticks), A37 (swap or flow), and their text in the draft and summary

**Provenance.**
- Same agent as REVIEW.md and REVIEW2.md, so this is not independent of those rounds.
- Primary files read:
  - A36 and A37 reports, and their prompts;
  - A36's outputs `out_c1`, `c2`, `c3` (and `c3_readability.py`), `c4`, `c5`;
  - A37's outputs `out_t1`, `t2_exact_attract`, `t3`, `t4`;
  - `toys/verify_A37_flux.py`;
  - the LOG entries from 04:27 to 05:08.
- Draft and summary versions reviewed:
  - `MORNING_DRAFT.md` (05:10, 411 lines);
  - `MORNING_SUMMARY_DRAFT.md` (05:10, 63 lines).
- No git and no repo edits. I wrote only into `c8/A34/`.

**What I ran.** All runs at 1-minute load 2.2–3.7, `nice -n 10`, four thread caps at 1, each run ≤ 13 s and ≤ 34 MB.
- **`c8_record_timed_speed.py` (A36 D7(e)).** Gated 2D growth, one shared tick against a phase that rises with the neighbour count, at higher statistics than A36.
  - Excess speed (ratio − 1) of 0.131 ± 0.002, 0.068 ± 0.003, 0.041 ± 0.005 and 0.017 ± 0.007 at F = 0.4, 0.2, 0.1 and 0.05 (1500, 1000, 600 and 300 runs).
  - Excess/F = 0.33, 0.34, 0.41 and 0.34. The O(F) claim is confirmed.
  - A36's F = 0.1 point (1.081 ± 0.021) was a roughly 2σ fluctuation.
- **`c9_flow_around_turning.py` (A37's untested "turning" case).** A 2D classical decohered gas at density 0.3, with odds favouring excitations (α = 1, β = 0.1), 150 runs × 400 ticks per rule.
  - Swap: p(back) 0.458; mean squared displacement (MSD) 149.
  - Line push PL1: p(same) 0.460; MSD 833.
  - Flow-around, random side: p(left) 0.319, p(right) 0.320, p(same) 0.183, p(back) 0.178; MSD 383, close to a random walk.
  - Flow-around, always left (2D handed): p(left) 0.456; the record circles at +0.27 quarter-turns per tick.
- **`c10_pf_flux.py` (A37 Step 1).** Choi information flux on A37's window: swap 1.000000, fill-behind (PF) 0.000000.

---

## 1. Verdicts

| Item | Verdict | One-line reason |
|---|---|---|
| **A36** | **Holds** (minor narrowing) | D1–D8 are right as stated. The steering argument in D2 is applied correctly; it needs no-signalling (Campaign 7 sentence 4, unadopted). D4 is EXACT given Q2 read as "no clock in the law unless supplied". The D5 percolation equivalence is EXACT and its threshold is a COMPARATOR. D6 is right that there is no *spatial* pattern, but the numbered cycle is a pattern in time. D9 says "odds" where it means "rates". The supplied list in D13 omits the rule's range RT1. |
| **A37** | **Holds** (minor narrowing) | Step 1 is right; I re-derived the flux as ½·log₂[(dim K₁·dim H₂)/(dim K₂·dim H₁)] = 1. Step 2 is complete for steps that permute content; general quantum steps rest on the index argument (open edge 3). Step 4's 3D impossibility holds for steps that do not let the record's content pick the side. Step 6 is right. The "turning" case for flow-around was ARGUED and is now CHECKED by me in 2D. |
| **Draft A36 text** | **2 MAJOR** | Gravity-paced set ticks contradict A36 D2 on the field route (C100). The A36 block omits that "one site per tick" survives only per instant of the shared clock, and omits the supplied items (C101). |
| **Draft A37 text** | **2 MAJOR** | "Whatever the rule … must flow back" drops "if nothing is made or destroyed", which the owner's own push picture relaxes (C109). "Push makes them keep going" is true of line pushes in a line toy; the tidy full-grid flow makes records turn (C110). |
| **Summary** | **Needs the same fixes** | Items 2 and 3 carry C100, C102, C103, C109 and C110. The round count needs updating (C115). |

---

## 2. Findings

### A36 and its draft text

**C100. MAJOR (cross-lane; draft + summary). Set ticks cannot follow a gravity carried by the shared possibilities; only the chances can.**
- **Claims.**
  - Draft:28: "The tick can also be influenced by gravity's slowing."
  - Draft:166–169: "**Influenced by gravity (exact).** The record-tick rate may vary from place to place. … Ticks that themselves run slower in gravity need each place to keep its own phase."
  - Draft:393 (decision 18): "which time-stretch paces a record's step between places of different gravity?"
  - Summary:29: "The tick can also be influenced by gravity."
- **What is wrong.**
  - A36 D2 (EXACT given no-signalling) shows set times cannot depend on the possibilities. A36 D11(b) adds: "long-range influence on formation enters through the odds, never through set ticks".
  - On the field route the time-stretch (lapse) *is* a field of the shared possibilities (A32 D13). It is never recorded (F1), and it must be dynamical (A31 K4(b)).
  - A tick paced by it, with phase ∫N dt, is a nonlinear function of the possibilities. A distant choice can steer the local lapse's branch and so shift when local records form.
  - A32 D13's lapse-paced ticks are therefore consistent only for a lapse that is a fixed, given background, which the field route does not supply.
  - The memory-free option is unaffected: "one global tick, with each place's record chances slowed by gravity's time-stretch" is linear (the weight N̂⊗F).
- **Corrected wording (EXACT, given no-signalling and the field route).** "How often records form can follow gravity's slowing, through the chance per tick. If the slowing is carried by the shared possibilities, the ticks themselves cannot follow it, because that would let faraway choices steer records (A36 D2). Lapse-paced ticks need a fixed, given slowing, plus per-place phases."
- **Draft.**
  - **Line 28:** "- **Constant or influenced?** Ticks chosen by records are influenced only by the records right next to a spot, not by a heavy body farther away, so on their own they are not gravity's slowing (A36). How often records form can also follow gravity's slowing, through the chance per tick. But if that slowing is carried by the shared possibilities, as on the gravity-field route, the ticks themselves cannot follow it without letting faraway choices steer records (A36). If clocks that count records are to agree with other clocks near heavy bodies (your choice), the chance of forming a record per unit of local time must be the same everywhere."
  - **Line 166:** "- **Influenced by gravity.** How often records form may vary from place to place."
  - **Line 169:** "- Ticks that themselves run slower in gravity would need each place to keep its own phase (at Earth's surface, neighbouring grid points would drift a full cycle apart about once a year). They also need gravity's slowing to be a fixed, given background. If the slowing is carried by the shared possibilities, as on the gravity-field route, such ticks would let faraway choices steer records (A36), and only the chances can follow it."
  - **Decision 18:** "which time-stretch paces a record's step between places of different gravity (through the chances, if the time-stretch is part of the shared possibilities)?"
  - **Summary:29:** "- **Influenced.** Ticks chosen by records feel only the records in contact, not gravity (A36). How often records form can follow gravity's slowing through the chance per tick, but not through the ticks themselves if gravity is carried by the shared possibilities (that would let faraway choices steer records). If clocks that count records are to agree with other clocks near heavy bodies (your choice), how often records form must follow gravity's slowing exactly."

**C101. MAJOR (draft). The A36 block lists only gains. "One site per tick" now holds per instant of the shared clock, and the construction supplies a numbered cycle and a table.**
- **Claim.** Draft:181–187 lists "set and differs by neighbourhood; influenced by records; needs no per-place memory; treats every place and turn alike".
- **What is missing.**
  - **(i) Your I2 holds per clock instant only (A36 D7(a), D7(f), EXACT).** A record steps at most one site per instant of the shared clock. Per spot's own cycle, a spot can act twice, a record can be claimed twice, and a chain can advance as many sites as the cycle has instants in use. At full chance the 3D cone becomes a cube, with body diagonals 3× faster (A36 C2a). At small chance the speed-up is O(F): A36's data, and my c8 at 0.34F.
  - **(ii) Supplied items (A36 D13).** The numbering of the shared ticks into a repeating cycle; the class table; a claim convention across instants; an order for same-class neighbours. The range-1 rule (RT1) is a choice too.
  - **(iii) A pattern in time.** The law treats every place and turn alike, but not every instant: it distinguishes the positions of the cycle.
- **Draft, replace lines 181–187:**
  - "- **With one shared clock underneath** (the shared ticks numbered in a repeating cycle), each spot can use the instants that its pattern of recorded neighbours selects (exact construction). The result:
    - it is set and differs by neighbourhood;
    - it is influenced by records;
    - it needs no per-place memory;
    - it treats every place and turn alike, though not every instant (the numbered cycle is a pattern in time).
  - The costs:
    - your 'one site per tick' then holds per instant of the shared clock. Per spot's own cycle a chain of new records can advance as many sites as the cycle has instants in use (at full chances, three times faster along diagonals; at small chances only slightly faster). Keeping one site per spot's own cycle needs memory;
    - supplied: the cycle's numbering, the table of which patterns use which instants, a rule for claims across instants, and an order for same-pattern neighbours.

    'Records form only next to records' is the simplest case: records switch the shared tick on or off. There are 10 neighbour patterns up to the grid's turns (57 if the law tells the two possible contents apart, 33 if it does not), and exactly one mirror-image pair, so a rule could even time a pattern and its mirror image differently (my check)."

**C102. MINOR (draft + summary). Without a shared clock, set place-dependent ticks also exist as zero-delay triggers; "need a per-place memory" is too strong.**
- **Claims.**
  - Draft:27: "Without a shared clock, set ticks that differ by place need a per-place memory".
  - Draft:162 and decision 18 (draft:397): "Without it, set ticks are either the same everywhere or need memory."
  - Summary:28.
- **What is wrong.** A36 D4(a) and D5: without memory, the moments new records form are set, place-dependent instants. Triggering neighbours at those moments needs no memory, but it breaks the one-site-per-tick limit (cascades, F^d; percolation above about 0.31 in 3D) and needs rate-timed seeds. The draft's own line 188 says so, so line 27 contradicts it.
- **Draft.**
  - **Line 27, last sentence:** "Without a shared clock, the only memory-free set moments are those at which new records form; letting them trigger neighbours breaks the one-site-per-tick limit (section 5). Any other set ticks that differ by place need a per-place memory (your small-memory question); random local times need none but are just a thinned-out shared tick."
  - **Decision 18 item, last sentence:** "Without it, set ticks are the same everywhere, need memory, or fire only when a neighbouring record forms (which can record a whole region at once)."
  - **Summary:28, last sentence:** "Without a shared clock, set ticks that differ by place need a per-place memory, or fire only when a neighbouring record forms, which can record a whole region at once."

**C103. MINOR (draft + summary). Visibility needs the chance to scale with each spot's own interval, not just to be small.**
- **Claims.**
  - Draft:29: "If the chance of a record on a single tick is tiny, … whichever choice is made shows in the records only in proportion to that chance".
  - Summary:30: "With the small chances per tick that freezing and heating already require, the choice is far too faint to see."
- **What is wrong.** A36 D9(c): if records set *how often* a spot's tick comes, and every firing keeps the same chance (P1′), the difference shows at full strength. TV stays near 0.053 as τ shrinks, appearing as formation rates that depend on the surrounding records. That holds even with small chances. Small chances help only together with P1 (the chance per firing scales with the spot's own interval).
- **Draft.**
  - **Line 29, first sentence:** "If the chance of a record on a single tick is tiny, as freezing and heating already require, and it also scales with the length of each spot's own interval, whichever choice is made shows in the records only in proportion to that chance …"
  - Add after it: "If records set how often a spot's tick comes and each tick keeps the same chance, the difference shows at full strength, as rates of forming that depend on the surrounding records (A36)."
  - **Summary:30:** "- **Visible?** With small chances per tick that also scale with each spot's own interval, the choice is far too faint to see. If records set how often a spot's tick comes and each tick keeps the same chance, it shows at full strength, as record-dependent rates of forming."

**C104. MINOR (draft). "One shared clock underneath" is the shape's existing shared tick, numbered.**
- **Claim.** Draft:27 and 181, "if one shared clock runs underneath".
- **What is wrong.**
  - In the record-tick shape records already form on one shared tick (A32 D8(a), D17). A36 adds a numbering of those ticks into a cycle of L positions, and a table (A36 RT2–RT3).
  - "A shared clock runs underneath" reads as an extra global device on top of the shape. It is the same tick, numbered, and the law then becomes periodic in time.
  - Owner rule (a) is respected: the draft frames it as conditional.
- **Draft.** Line 27, middle sentence: "Ticks can still differ by place without any memory if the shared ticks are numbered in a repeating cycle: the records around each spot then choose which numbers that spot uses (A36, exact construction)."

**C105. MINOR (draft + lane). "57 counting the records' contents" assumes the law tells r from −r.**
- **Claim.**
  - Draft:187: "There are 10 neighbour patterns up to the grid's turns (57 counting the records' contents)".
  - A36 D6(f).
- **What is wrong.**
  - Telling the content r from −r needs a law-level sign for the content axis, which privileges a possibility (decision 16).
  - With an inherited axis, only the 33 relational classes are available (r ↔ −r as a symmetry).
  - The mirror pair survives in both counts (A36 `out_c4`: 33/32).
  - Covariance here is under spatial turns with contents as labels. That is acceptable because Q3 leaves formation unglued.
- **Draft.** Already folded into C101's replacement text.

**C106. MINOR (draft). "Not gravity" and "far from all records" need their conditions.**
- **Claims.**
  - Draft:189: "**Not gravity.** The influence comes only from records in contact, not from a heavy body farther away."
  - Draft:190: "against 'all clocks slow together'".
  - Draft:192: "Far from all records nothing sets a tick and nothing forms".
  - Draft:180: "Records … never change".
- **What is wrong.**
  - A36 D11(f) (ARGUED): through a gas of wandering records captured by a lump, record-timed ticks or the gate alone inherit A6's 1/r profile. So they can reproduce section 6's record-carried slowing, with its shortcomings (coefficient set by capture, β = ½).
  - P5 is your choice, not a law.
  - "Nothing forms" holds under "records form only next to records".
  - Records do move (steps), so "never change" should be "do not change between record events".
- **Draft.**
  - **Line 189:** "- **Not gravity's slowing.** The influence comes only from records in contact, not from a heavy body farther away. Through a gas of wandering records it could at most reproduce the record-carried slowing of section 6, with its shortcomings (argued)."
  - **Line 190:** "… against your choice, if you make it, that all clocks slow together."
  - **Line 192:** "- **Far from all records,** if records form only next to records, nothing sets a tick and nothing forms; the smooth change is the only time empty space has."
  - **Line 180:** "Records carry no time of their own and do not change between record events, so by themselves they cannot mark a later moment."

**C107. MINOR (lane, A36).**
- **D2:** add "given no-signalling (Campaign 7 sentence 4, unadopted)".
- **D9(c) and Answer:82** say "formation odds set by records". It should be "formation *rates* set by records": by reading note 2, Admissibility's odds concern which possibility a forming record locks, not the rate.
- **D9(c)'s P1′** is "the same chance per firing for every class, whatever its period". In C3 that chance still scales with the base instant (c = γτ).
- **D7(e):** confirmed at O(F) by my c8 (excess/F ≈ 0.34). A36's table was noisier than "within errors, the excess shrinks" suggests.
- **D12(c):** inside a full jam there are no empty spots, so "every spot has … a class and a tick" is empty. "Both kinds of clock stop" holds for record clocks and matter-possibility clocks; gravity's clocks inside are open (C66).
- **D13:** add RT1 (the rule's range) to the supplied list.
- **Plain language, "so this is not gravity's slowing":** see C106.

**C108. MINOR (draft). Decision 18 should carry A36's other owner choices.** Add two items:
- "Does 'one site per tick' (I2) refer to the shared clock's instants, or to each spot's own cycle (which needs memory)?"
- "May new records trigger their neighbours at the same moment (which can record a whole region at once)?"

### A37 and its draft text

**C109. MAJOR (draft + summary; fair representation of your push picture). "Whatever the rule … must flow back" holds only if nothing is made or destroyed.**
- **Claims.**
  - Draft:17: "Whatever the rule, when a record steps, exactly one spot's worth of possibilities must flow back to where it came from (exact)."
  - Draft:330: "net exactly one spot's worth must end up back on the side it came from, whatever the rule."
  - Summary:24, the same.
- **What holds (EXACT; re-derived).**
  - For any *unitary* (nothing made or destroyed) step V: H_{W∖x} → H_{W∖y}, the Choi state is pure with maximally mixed marginals.
  - So ½[I(K₁:R₂) − I(K₂:R₁)] = ½·log₂[(dim K₁·dim H₂)/(dim K₂·dim H₁)] = 1 qubit (the coordinator's check gives 1.000000 in 5 of 5 random unitaries).
- **What is wrong.**
  - "Whatever the rule" includes A37's own non-conservative rules.
    - Fill-behind (PF) erases y's content and refills x: the Choi computation gives an information flux of 0 (my c10: 0.000000, against 1.000000 for swap).
    - The conveyor (P∞) makes a fresh spot at x and sends everything ahead to infinity.
    - Push-and-absorb (PA) destroys content.
  - In the bare counting sense, the identity only restates which site is unrecorded.
  - As written, the sentence reads as ruling out your push for every rule. A37 itself shows that push survives by relaxing exactly this premise, at a cost.
- **Corrected wording (EXACT).** "If no possibility content is made or destroyed, a record's step sends net exactly one site's worth (one qubit's worth) from the side it enters to the side it left, whatever the rule; pushing versus swapping only decides which content lands where."
- **Draft.**
  - **Line 17:** "- **Swap or flow (A37, checked).** If no possibility content is made or destroyed, then whatever the rule, when a record steps, exactly one spot's worth of possibilities ends up back on the side it came from (exact). On a single line the only tidy way to do that is the swap. Your 'everything pushes right' exists as an endless conveyor that changes things arbitrarily far away at once, or by letting each step wipe out one spot's worth. On the full grid the possibilities can genuinely flow around the record, but with no special side the rule must pick one at random. Section 11 has the details."
  - **Line 330:** "- **The one fixed fact (exact).** Each spot always holds exactly one spot's worth of possibilities. So if no possibility content is made or destroyed, when a record steps from one spot to the next, net exactly one spot's worth must end up back on the side it came from, whatever the rule. Pushing versus swapping only decides which content lands where. My check confirmed this for random rules of that kind: always exactly one qubit's worth. Rules that wipe out or freshly make a spot's worth escape this, at the costs below."
  - **Summary:24, first sentence:** "If nothing is made or destroyed, then whatever the rule, when a record steps, exactly one spot's worth of possibilities must flow back to where it came from (exact)."

**C110. MAJOR (draft + summary + decision 27). "Push makes them keep going" is the line push in a line toy; the tidy full-grid flow makes records turn.**
- **Claims.**
  - Draft:340: "Under push it shoves it ahead, so it tends to keep going".
  - Draft:409 (decision 27): "push makes them keep going, swap makes them bounce."
  - Summary:24: "push makes them keep going, swap makes them bounce back."
- **What is wrong.**
  - A37's persistence numbers come from line pushes in 1D toys: p_same 0.69–0.71 for PL1, PL2, P∞ and PA; speed 0.154 for PA in the classical gas. On a line, those are exactly the non-tidy rules: a long return jump, unbounded reach, or content destroyed.
  - For flow-around, the only tidy push on the full grid, A37 left the turning case ARGUED (Step 10). The pushed content lands at the side, so a record that favours excitations turns.
  - My c9 (2D, classical decohered, odds favouring excitations):
    - swap bounces (p(back) 0.458);
    - line push keeps going (p(same) 0.460);
    - random-side flow-around turns (p(left) 0.319 and p(right) 0.320 against p(same) 0.183), with a mean squared displacement (MSD) near a random walk's (383 against 400);
    - the 2D handed "always left" rule makes records circle (+0.27 quarter-turns per tick).
- **Draft.**
  - **Line 340:** "- If the odds look at the neighbours, it matters. A record that steps onto something leaves it behind under swap, so it tends to bounce back. A push along the line shoves it ahead, so the record tends to keep going (or, with the opposite preference, gets hemmed in), but on a line such pushes need a long jump back, an endless conveyor or wiping something out. The tidy flow around the record on the full grid puts it to the side, so the record tends to turn instead (my check; with an 'always turn left' rule in 2D it circles)."
  - **Decision 27, last sentence:** "That is the only case where the rules differ for how records move: swap makes them bounce back, a line push makes them keep going, and flowing around makes them turn."
  - **Summary:24, the persistence sentence:** "It changes how records move only if their stepping odds look at their neighbours: swap makes them bounce back, a line push makes them keep going, flowing around makes them turn. That is a memory in what was pushed, not momentum."

**C111. MINOR (draft; fair representation). The 1D premises: the whole-line shift is your standing conveyor, and the quantum version of the classification is open.**
- **Claims.**
  - Draft:331: "If nothing is made or destroyed and nothing jumps more than one site, the only rule is the swap."
  - Draft:332: "Your 'everything pushes right' exists only as an endless conveyor".
- **What is wrong.**
  - **The whole-line shift is missing.** Shifting the whole line, records and all, by one site also satisfies both premises (A37 Step 2). It is a relabelling that changes nothing, and it is impossible if another record is on the line.
  - **That shift is your picture.** Your brief's I4 ("net flow across any cut … is the same at every cut … a standing conveyor through the whole line") is exactly this relabelling. The half-line conveyor (P∞) is its version with a source behind the record.
  - **Grading.** The classification is EXACT for steps that permute site contents. For general quantum steps it rests on the index argument (A37 open edge 3; COMPARATOR: Gross–Nesme–Vogts–Werner).
- **Draft.**
  - **Line 331:** "- **On a single line (exact for steps that move whole contents).** If nothing is made or destroyed and nothing jumps more than one site, the only rule is the swap, apart from shifting the whole line, records and all, which changes nothing and is impossible once a second record is on the line."
  - **Line 332:** "- Your 'everything pushes right' as a push across every cut is that whole-line shift. As a push ahead of the record only, it is an endless conveyor: everything ahead shifts and a fresh spot appears behind. That changes things arbitrarily far away at the same moment, breaking every speed limit, and it needs an endless empty line."

**C112. MINOR (draft). The flow-around details.**
- **Claim.** Draft:335–336: "It obeys all the rules and reaches at most two sites. In 3D no side is special, so the rule must pick one at random, which slightly blurs linked possibilities nearby."
- **What is wrong.**
  - **"Slightly" understates the cost.** Purity given the step is 0.50 in 2D (A37 t4), and about 0.25 in 3D (by hand). Linked information at the destination is 0.587 bits against 2 for swap.
  - **"Must pick at random" holds only for steps that ignore the record's content**, which is the unglued case (A37 Step 4). A step that lets the record's content, turned along with the grid, choose the side could be deterministic, except when the content lies along the step axis (ARGUED, mine). Such a step ties records to the grid.
  - **"Obeys all the rules" overstates.** It passes the same checks as the swap, with the same admissibility gap (C40). It is no better on energy near excitations (A37 Step 8).
- **Draft.**
  - **Line 335:** "- It passes the same checks as the swap (one site per tick for the record, no faraway leaks, nothing made or destroyed), reaches at most two sites, and shares the swap's open questions (whether the moved content suits its new spot; energy near excitations)."
  - **Line 336:** "- In 3D no side is special, so unless the record's own content picks the side (which would tie records to the grid's directions), the rule must pick one at random. That noticeably blurs linked possibilities nearby: where a linked piece went is spread over the sides (A37). In 2D an 'always turn left' rule is allowed."

**C113. MINOR (draft). Clash tangles.**
- **Claim.** Draft:343: "… only if the law settles each tangle of overlapping pushes at once."
- **What is missing.**
  - A37 Step 12 (ARGUED): tangles can chain across many records, so the settling rule can reach far and needs small chances.
  - An endless conveyor makes every pair of records on a line clash.
- **Draft.** Append: "Tangles can chain across many records, so that settling rule can reach far and needs small chances (argued); with an endless conveyor every pair of records on a line clashes."

**C114. MINOR (lane, A37).**
- **Grading.**
  - Answer:31 and Step 2 say "1D (EXACT)". That is EXACT for content-permuting steps; for general quantum steps it is via the index (open edge 3).
  - Step 4's 3D impossibility covers steps that do not use the record's content (unglued).
  - Step 10's flow-around turning is now CHECKED by my c9 (classical, 2D).
  - The self-propelled gas result is a SUPPLIED classical analog.
- **Cross-lane: A30's sealed jams.** A30 assumed "capture by swap … the excitation is caged … a sealed jam is a pure accretor" (A30 2.7).
  - Under the β = 0 seal, every rule is a re-formation (A37 Step 6). Under a line push the captured content is shoved outward instead of caged; under flow-around it goes sideways.
  - So "pure accretor" needs redoing for push rules (open).
  - Under β = 0 with the 2D handed flow-around, a lone record beside its own left-behind copy would circle in place (ARGUED from the one-step rule).
- **Comparators.** These are flagged correctly: Darwin drift, the Zener ring, Hilbert hotel/GNVW, PushASEP and others.
  - "Consistent with observation: no wake in calm vacuum" is fine.
  - Nothing is presented as more than a comparison.

**C115. MINOR (provenance).**
- After this round, the count is seven rounds by four agents: A16 once, A21 twice, A29 once, A34 three times.
- Summary:10 and draft:50 should read "Seven rounds of hostile review by four separate agents (the second reviewed twice and the fourth three times; each later round had read the earlier ones)".
- Draft:57 should read "all review rounds".

---

## 3. Fine as they are

- **Draft, A36 text.**
  - Lines 160–161, 163–165, 167–168 and 170–178.
  - The A36 heading on line 179.
  - The steering sentence on line 180, apart from "never change".
  - Line 188, cascade, with "(without memory)" optionally added.
  - Lines 190–191, with C106's P5 wording.
- **Draft, A37 text.**
  - The section 11 heading.
  - Lines 333–334, 337–339, 341–342.
  - The core of the clash statement on line 343.
- **Summary.** Lines 26, 31 and 32.
- **Owner rules.**
  - The tick and the push are framed as your instincts and options throughout.
  - No beat is adopted: the shared clock is conditional ("if one shared clock runs underneath").
  - No "read" possibility, and no adopted import.
  - Q7 is untouched.
  - Your flow picture is represented fairly once C109 and C111 are applied.

---

## 4. New open questions for the owner

1. **Which clock does "one site per tick" refer to?** If records may choose among numbered instants of the shared tick, does "one site per tick" mean per instant of the shared clock, or per spot's own cycle (which needs memory) (C101)?
2. **Gravity through the ticks or through the chances?** If gravity's slowing is carried by the shared possibilities, only the chance of forming records can follow it, not the ticks. Is that acceptable for your "influenced tick" (C100)?
3. **Which flow do you mean?** A push along the line makes a record that is drawn to busy spots keep going, but on a line it needs a long jump back, an endless conveyor or a loss each step. The tidy flow around it makes the record turn instead. Which of these, if any, matches your "neighbourhoods can shift" (C110)?

---

## 5. Lane and LOG wording fixes

| Location | Old | New |
|---|---|---|
| A36 D2 | "EXACT, using the standard steering theorem" | add "given no-signalling (Campaign 7 sentence 4, unadopted)" |
| A36 Answer:82; D9(c) | "record-dependent formation odds" | "record-dependent formation rates" |
| A36 D11 | (missing) | "set ticks cannot follow a lapse carried by the possibilities (D2); A32 D13's lapse-paced ticks need a given, classical lapse" |
| A36 D12(c) | "every spot has six recorded neighbours, so it has a class and a tick … Both kinds of clock stop" | "a full jam has no empty spots; record clocks and matter-possibility clocks stop; gravity's clocks inside are open (C66)" |
| A36 D13 | supplied list | add "RT1, the rule's range" |
| A37 Answer:31 | "1D (EXACT)" | "1D (EXACT for content-permuting steps; quantum steps via the index, open edge 3)" |
| A37 Step 10 | "The flow-around 'turning' case is ARGUED only (not simulated)" | "CHECKED in a 2D classical toy (A34 c9): random side turns (0.32/0.32 vs 0.18 same); handed side circles" |
| LOG A37 entry | "push makes them keep going" (in the summary of results) | "a line push makes them keep going; flow-around makes them turn" |

**Scripts.** In `c8/A34/`:
- `c8_record_timed_speed.py`, with `out_c8_record_timed_speed.txt` and `time_c8_record_timed_speed.txt`;
- `c9_flow_around_turning.py`, with `out_c9_flow_around_turning.txt` and `time_c9_flow_around_turning.txt`;
- `c10_pf_flux.py`, with `out_c10_pf_flux.txt`.
