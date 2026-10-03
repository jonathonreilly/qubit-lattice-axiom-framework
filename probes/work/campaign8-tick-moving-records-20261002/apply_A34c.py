p = "MORNING_DRAFT.md"
lines = open(p).read().split("\n")
n = 0
def line_rep(prefix, new):
    global n
    idx = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    assert len(idx) == 1, (prefix[:60], len(idx))
    lines[idx[0]] = new; n += 1
def sub_rep(old, new):
    global lines, n
    s = "\n".join(lines); assert s.count(old) == 1, (old[:60], s.count(old))
    lines = s.replace(old, new).split("\n"); n += 1
# C115 provenance
sub_rep("(v10, after six review rounds)", "(v11, after seven review rounds)")
sub_rep("Six rounds of hostile review by four separate agents attacked the main claims (two agents reviewed twice; each later round had read the earlier ones), and their corrections are included.",
        "Seven rounds of hostile review by four separate agents attacked the main claims (the second reviewed twice and the fourth three times; each later round had read the earlier ones), and their corrections are included.")
sub_rep("all six review rounds, and my own checks.", "all review rounds, and my own checks.")
# C109 line 17
line_rep("- **Swap or flow (A37, checked).** Whatever the rule,",
 "   - **Swap or flow (A37, checked).** If no possibility content is made or destroyed, then whatever the rule, when a record steps, exactly one spot's worth of possibilities ends up back on the side it came from (exact). On a single line the only tidy way to do that is the swap. Your \"everything pushes right\" exists as an endless conveyor that changes things arbitrarily far away at once, or by letting each step wipe out one spot's worth. On the full grid the possibilities can genuinely flow around the record, but with no special side the rule must pick one at random. Section 11 has the details.")
# C104/C102 line 27
line_rep("- **Global or neighbourhood?** A tick written into the rule itself is the same everywhere",
 "   - **Global or neighbourhood?** A tick written into the rule itself is the same everywhere if the rule treats every place exactly alike, or else a checkerboard of two sub-grids half a tick apart (which records can faintly tell apart). Ticks can still differ by place without any memory if the shared ticks are numbered in a repeating cycle: the records around each spot then choose which numbers that spot uses (A36, exact construction). Without that, the only memory-free set moments are those at which new records form; letting them trigger neighbours breaks the one-site-per-tick limit (section 5). Any other set ticks that differ by place need a per-place memory (your small-memory question); random local times need none but are just a thinned-out shared tick.")
# C100 line 28
line_rep("- **Constant or influenced?** Ticks chosen by records are influenced only",
 "   - **Constant or influenced?** Ticks chosen by records are influenced only by the records right next to a spot, not by a heavy body farther away, so on their own they are not gravity's slowing (A36). How often records form can also follow gravity's slowing, through the chance per tick. But if that slowing is carried by the shared possibilities, as on the gravity-field route, the ticks themselves cannot follow it without letting faraway choices steer records (A36). If clocks that count records are to agree with other clocks near heavy bodies (your choice), the chance of forming a record per unit of local time must be the same everywhere.")
# C103 line 29
line_rep("- **How visible is it?** If the chance of a record on a single tick is tiny,",
 "   - **How visible is it?** If the chance of a record on a single tick is tiny, as freezing and heating already require, and it also scales with the length of each spot's own interval, whichever choice is made shows in the records only in proportion to that chance, and to how fast the odds change within one tick. That is far too small to see on the finest grid. If records set how often a spot's tick comes and each tick keeps the same chance, the difference shows at full strength, as rates of forming that depend on the surrounding records (A36). With a real chance on every tick and sharp records, it could be visible.")
# C104 line 162
line_rep("- Ticks set differently by place need each place to remember its phase (decision 9), unless one shared clock runs underneath:",
 "  - Ticks set differently by place need each place to remember its phase (decision 9), unless the shared ticks are numbered in a repeating cycle: then the records around each spot can choose which numbers the spot uses, with no memory (A36, below).")
# C100 lines 166, 169
line_rep("- **Influenced by gravity (exact).** The record-tick rate may vary from place to place.",
 "- **Influenced by gravity.** How often records form may vary from place to place.")
line_rep("- Ticks that themselves run slower in gravity need each place to keep its own phase.",
 "  - Ticks that themselves run slower in gravity would need each place to keep its own phase (at Earth's surface, neighbouring grid points would drift a full cycle apart about once a year). They also need gravity's slowing to be a fixed, given background. If the slowing is carried by the shared possibilities, as on the gravity-field route, such ticks would let faraway choices steer records (A36), and only the chances can follow it.")
# C106 line 180
sub_rep("Records carry no time of their own and never change, so by themselves they cannot mark a later moment.",
        "Records carry no time of their own and do not change between record events, so by themselves they cannot mark a later moment.")
# C101 lines 181-187: replace block
i = next(k for k, l in enumerate(lines) if l.startswith("- **With one shared clock underneath** (a numbered cycle of instants)"))
j = next(k for k, l in enumerate(lines) if l.lstrip().startswith("\"Records form only next to records\" is the simplest case"))
lines[i:j+1] = [
 "- **With one shared clock underneath** (the shared ticks numbered in a repeating cycle), each spot can use the instants that its pattern of recorded neighbours selects (exact construction). The result:",
 "  - it is set and differs by neighbourhood;",
 "  - it is influenced by records;",
 "  - it needs no per-place memory;",
 "  - it treats every place and turn alike, though not every instant (the numbered cycle is a pattern in time).",
 "",
 "  The costs:",
 "  - your \"one site per tick\" then holds per instant of the shared clock. Per spot's own cycle, a chain of new records can advance as many sites as the cycle has instants in use (at full chances, three times faster along diagonals; at small chances only slightly faster). Keeping one site per spot's own cycle needs memory;",
 "  - supplied: the cycle's numbering, the table of which patterns use which instants, a rule for claims across instants, and an order for same-pattern neighbours.",
 "",
 "  \"Records form only next to records\" is the simplest case: records switch the shared tick on or off. There are 10 neighbour patterns up to the grid's turns (57 if the law tells the two possible contents apart, 33 if it does not), and exactly one mirror-image pair, so a rule could even time a pattern and its mirror image differently (my check)."]
n += 1
# C106 lines 189-192
line_rep("- **Not gravity.** The influence comes only from records in contact, not from a heavy body farther away.",
 "- **Not gravity's slowing.** The influence comes only from records in contact, not from a heavy body farther away. Through a gas of wandering records it could at most reproduce the record-carried slowing of section 6, with its shortcomings (argued).")
sub_rep("against \"all clocks slow together\".", "against your choice, if you make it, that all clocks slow together.")
line_rep("- **Far from all records** nothing sets a tick and nothing forms;",
 "- **Far from all records,** if records form only next to records, nothing sets a tick and nothing forms; the smooth change is the only time empty space has.")
# C108 + C100 + C102 decision 18
line_rep("- which time-stretch paces a record's step between places of different gravity?",
 "    - which time-stretch paces a record's step between places of different gravity (through the chances, if the time-stretch is part of the shared possibilities)?")
line_rep("- if ticks are to differ by neighbourhood without memory, is one shared clock underneath acceptable (A36)?",
 "    - if ticks are to differ by neighbourhood without memory, is numbering the shared ticks in a repeating cycle acceptable (A36)? The records around each spot would then choose which numbers that spot uses. Without it, set ticks are the same everywhere, need memory, or fire only when a neighbouring record forms (which can record a whole region at once).\n    - does \"one site per tick\" refer to the shared clock's instants, or to each spot's own cycle (which needs memory)?\n    - may new records trigger their neighbours at the same moment?")
# C109 line 330
line_rep("- **The one fixed fact (exact).**",
 "- **The one fixed fact (exact).** Each spot always holds exactly one spot's worth of possibilities. So if no possibility content is made or destroyed, when a record steps from one spot to the next, net exactly one spot's worth must end up back on the side it came from, whatever the rule. Pushing versus swapping only decides which content lands where. My check confirmed this for random rules of that kind: always exactly one qubit's worth. Rules that wipe out or freshly make a spot's worth escape this, at the costs below.")
# C111 lines 331, 332
line_rep("- **On a single line (exact).**",
 "- **On a single line (exact for steps that move whole contents).** If nothing is made or destroyed and nothing jumps more than one site, the only rule is the swap, apart from shifting the whole line, records and all, which changes nothing and is impossible once a second record is on the line.")
line_rep("- Your \"everything pushes right\" exists only as an endless conveyor:",
 "  - Your \"everything pushes right\" as a push across every cut is that whole-line shift. As a push ahead of the record only, it is an endless conveyor: everything ahead shifts and a fresh spot appears behind. That changes things arbitrarily far away at the same moment, breaking every speed limit, and it needs an endless empty line.")
# C112 lines 335, 336
line_rep("- It obeys all the rules and reaches at most two sites.",
 "  - It passes the same checks as the swap (one site per tick for the record, no faraway leaks, nothing made or destroyed), reaches at most two sites, and shares the swap's open questions (whether the moved content suits its new spot; energy near excitations).")
line_rep("- In 3D no side is special, so the rule must pick one at random,",
 "  - In 3D no side is special, so unless the record's own content picks the side (which would tie records to the grid's directions), the rule must pick one at random. That noticeably blurs linked possibilities nearby: where a linked piece went is spread over the sides (A37). In 2D an \"always turn left\" rule is allowed.")
# C110 line 340
line_rep("- If the odds look at the neighbours, it matters.",
 "  - If the odds look at the neighbours, it matters. A record that steps onto something leaves it behind under swap, so it tends to bounce back. A push along the line shoves it ahead, so the record tends to keep going (or, with the opposite preference, gets hemmed in), but on a line such pushes need a long jump back, an endless conveyor or wiping something out. The tidy flow around the record on the full grid puts it to the side, so the record tends to turn instead (the review's check; with an \"always turn left\" rule in 2D it circles).")
# C113 line 343
sub_rep("Combining separately computed odds lets faraway choices leak.",
        "Combining separately computed odds lets faraway choices leak. Tangles can chain across many records, so that settling rule can reach far and needs small chances (argued); with an endless conveyor every pair of records on a line clashes.")
# C110 decision 27
sub_rep("That is the only case where push and swap differ for how records move: push makes them keep going, swap makes them bounce.",
        "That is the only case where the rules differ for how records move: swap makes them bounce back, a line push makes them keep going, and flowing around makes them turn.")
open(p, "w").write("\n".join(lines))
print("draft applied", n)
# Summary
q = "MORNING_SUMMARY_DRAFT.md"
t = open(q).read()
def trep(old, new):
    global t
    assert t.count(old) == 1, ("summary", old[:60], t.count(old))
    t = t.replace(old, new)
trep("Six rounds of hostile review, by four separate agents, attacked the claims, and their corrections are folded in.",
     "Seven rounds of hostile review, by four separate agents, attacked the claims, and their corrections are folded in.")
trep("- **Swap or flow (A37, checked).** Whatever the rule, when a record steps, exactly one spot's worth of possibilities must flow back to where it came from (exact).",
     "- **Swap or flow (A37, checked).** If nothing is made or destroyed, then whatever the rule, when a record steps, exactly one spot's worth of possibilities must flow back to where it came from (exact).")
trep("your \"everything pushes right\" exists only as an endless conveyor that changes things arbitrarily far away at once.",
     "your \"everything pushes right\" exists as an endless conveyor that changes things arbitrarily far away at once, or by letting each step wipe out one spot's worth.")
trep("It changes how records move only if their stepping odds look at their neighbours: push makes them keep going, swap makes them bounce back. That is a memory in what was pushed, not momentum.",
     "It changes how records move only if their stepping odds look at their neighbours: swap makes them bounce back, a line push makes them keep going, flowing around makes them turn. That is a memory in what was pushed, not momentum.")
trep("Ticks can still differ by place without memory if one shared clock runs underneath: the records around each spot choose which of its instants that spot uses (A36). Without a shared clock, set ticks that differ by place need a per-place memory.",
     "Ticks can still differ by place without memory if the shared ticks are numbered in a repeating cycle: the records around each spot choose which numbers that spot uses (A36); then \"one site per tick\" holds per shared instant. Without that, the only memory-free set moments are those when new records form (letting them trigger neighbours breaks the one-site-per-tick limit); other place-dependent set ticks need a per-place memory.")
trep("- **Influenced.** Ticks chosen by records feel only the records in contact, not gravity (A36). The tick can also be influenced by gravity. If clocks that count records are to agree with other clocks near heavy bodies (your choice), how often records form must follow gravity's slowing exactly.",
     "- **Influenced.** Ticks chosen by records feel only the records in contact, not gravity (A36). How often records form can follow gravity's slowing through the chance per tick, but not through the ticks themselves if gravity is carried by the shared possibilities (that would let faraway choices steer records). If clocks that count records are to agree with other clocks near heavy bodies (your choice), how often records form must follow gravity's slowing exactly.")
trep("- **Visible?** With the small chances per tick that freezing and heating already require, the choice is far too faint to see.",
     "- **Visible?** With small chances per tick that also scale with each spot's own interval, the choice is far too faint to see. If records set how often a spot's tick comes and each tick keeps the same chance, it shows at full strength, as record-dependent rates of forming.")
open(q, "w").write(t)
print("summary applied")
