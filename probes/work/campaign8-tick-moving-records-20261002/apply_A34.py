p = "MORNING_DRAFT.md"
lines = open(p).read().split("\n")
n_ok = 0
def line_rep(prefix, new):
    """replace the unique line whose content (after leading spaces) starts with prefix"""
    global n_ok
    idx = [i for i, l in enumerate(lines) if l.lstrip().startswith(prefix)]
    assert len(idx) == 1, ("line prefix not unique/missing", prefix[:70], len(idx))
    lines[idx[0]] = new; n_ok += 1
def sub_rep(old, new):
    global lines, n_ok
    s = "\n".join(lines)
    assert s.count(old) == 1, ("substring not unique/missing", old[:70], s.count(old))
    s = s.replace(old, new); lines = s.split("\n"); n_ok += 1

# C86 title / review count
sub_rep("(v8, after three hostile reviews)", "(v9, after four hostile reviews)")
sub_rep("Three hostile reviews by separate agents attacked the main claims (each later one had read the earlier ones), and their corrections are included.",
        "Four hostile reviews by separate agents attacked the main claims (each later one had read the earlier ones), and their corrections are included.")
sub_rep("all three reviews, and my own checks.", "all four reviews, and my own checks.")
# C57 line 21
line_rep("- over the calm empty background this shape needs,",
 "     - over the calm, all-pointing-one-way empty background, a change that treats every spot and turn alike moves single ripples only like slow, heavy particles, never like light (exact for single ripples; groups of ripples are untested). Over that background, light-like matter needs a sign pattern painted onto the rule, and in the version that keeps your gluing that pattern cannot keep the turns the gravity field's pattern keeps (proved). A background whose spots share their possibilities, instead of all pointing one way, can carry light-like ripples with the plain rule (a comparison from magnets, not adopted), but next to matter it gets recorded and heats (A28);")
# C77 line 26
line_rep("- **Global or neighbourhood?** A tick written into the rule itself must be",
 "   - **Global or neighbourhood?** A tick written into the rule itself is the same everywhere if the rule treats every place exactly alike. The only other way is a checkerboard of two sub-grids half a tick apart, and records can faintly tell those apart. Set ticks that differ by place needed a per-place memory in every construction tried (your small-memory question). Random local times need none but are just a thinned-out shared tick. Ticks set by the surrounding records were not tried.")
# C78 line 28
line_rep("- **How visible is it?**",
 "   - **How visible is it?** If the chance of a record on a single tick is tiny, as freezing and heating already require, whichever choice is made shows in the records only in proportion to that chance, and to how fast the odds change within one tick. That is far too small to see on the finest grid. With a real chance on every tick and sharp records, it could be visible.")
# C80 line 29
line_rep("- **Light.** The ticks never touch how light and matter travel",
 "   - **Light.** If records form only next to records, the ticks never touch how light and matter travel through empty space, so the precise relativity tests with light from distant explosions say nothing against them. Clocks made of light-like matter slow with motion by Einstein's amounts; in this shape that matter needs the sign pattern of section 10.")
# C84 line 31
line_rep("- **Same tick.** Two records can form on the same tick with no problem;",
 "   - **Same tick.** Two records can form on the same tick consistently. If the rule looks at neighbours, it needs an order or a joint rule, and a choice of whether same-tick neighbours see each other's new records. With small chances it almost never happens.")
# C79 line 32
line_rep("- **Minimum distance and minimum tick.** This comes out as an upper limit",
 "   - **Minimum distance and minimum tick.** No smallest tick follows. What follows is a longest one: if one site per tick is to be the limit for all influence, the tick must be shorter than the time light takes to cross one grid step (shorter by √3 in 3D). A tick near that crossing time is favoured only if every tick carries a real chance of a record and recording is to run near its fastest. Such chances would freeze anything slower than the grid's fastest motion next to records, and with nucleon-sized records they would cloud glass and water (argued).")
# C70 line 40, C65 line 41, C71 line 42, C66 line 46
line_rep("7. **Your black-hole idea (A30, checked).**",
 "7. **Your black-hole idea (A30, checked).** Inside the record-tick shape, a fully recorded region is a place where no record can ever form or move again, its possibilities never change, and no record or possibility from outside can reach in (gravity may still, depending on decisions 13 and 21). With one stepping choice it never wears away, but that choice also freezes every lone record in empty space. It is grey, not black:")
line_rep("- it catches fast things almost always and bounces slow ones;",
 "   - at the catching strength best for the fastest things, it catches those almost always and bounces slow ones;")
line_rep("- no setting catches everything at every speed;",
 "   - no fixed setting catches everything at every speed (proved in a one-line toy);")
line_rep("Whether gravity's clocks stop inside depends on a choice for you (point 9).",
 "   Whether gravity's clocks stop inside is open: it depends on choices for you and on strong gravity, which is not worked out (section 9).")
# C84 line 53
line_rep("- No faraway influence faster than one site per tick. (Point 0's shape gives this up",
 "  - No faraway influence faster than one site per tick. (The record-tick shape gives this up for unrecorded influence. A32 has redone section 5's tick results there; the results of sections 1 and 4 would need redoing.)")
# C56 line 92
line_rep("- **Only slow-particle ripples, provably (A31).**",
 "- **Only slow-particle ripples over the simplest calm background (A31).** Over a calm empty background where every spot points the same way, a change built from pairs of neighbours that treats every spot and turn alike must reduce to one simple form once any record holds the opposite content (exact). Rules with terms on three or more spots of a neighbourhood keep that background calm in more ways (the fourth review's check). Either way, single ripples behave like slow, heavy particles, never like light (exact for single ripples). Over that background, light-like ripples need a fixed pattern of plus and minus signs on the rule (section 10); a background whose spots share their possibilities is open (A33).")
# C84 line 156
line_rep("**The tick redone in the point-0 shape (A32, checked).**",
 "**The tick redone in the record-tick shape (A32, checked).** In this option, records form and step on ticks; the possibilities change all the time.")
# C78 line 157
sub_rep("changes everything recorded later only in proportion to the chance of a record on that tick.",
        "changes everything recorded later only in proportion to the chance of a record on that tick and to how much the change does during the shift.")
# C77 lines 160, 161
line_rep("- A tick written into the law must be the same everywhere, since the law treats every place alike.",
 "  - A tick written into the law is the same everywhere if the law treats every place exactly alike. A checkerboard of two sub-grids half a tick apart also qualifies, up to an unnoticeable overall shift, but records can faintly tell its sub-grids apart.")
line_rep("- Ticks set differently by place need each place to remember its phase (decision 9).",
 "  - Ticks set differently by place needed each place to remember its phase in every construction tried (decision 9); ticks set by the surrounding records were not tried.")
# C84 line 164
sub_rep("It does so only in proportion to the chance per tick, unless each place remembers the pattern from its last tick.",
        "If that chance is small, it does so only in proportion to the chance per tick, unless each place remembers the pattern from its last tick.")
# C84 line 166
line_rep("- What consistency requires is that the chance of forming a record per unit of local time",
 "  - If clocks that count records are to agree with all other clocks near heavy bodies (your choice), the chance of forming a record per unit of local time must be the same everywhere. Otherwise clocks that count records and clocks carried by the possibilities disagree near heavy bodies, by the full gravitational amount.")
# C80 line 169
line_rep("- **Light never sees the tick (exact).**",
 "- **Light never sees the tick (exact, when records form only next to records).** In empty space the ticks act on nothing, so they add no energy-dependent speed and no twisting of light's polarisation. Clocks made of light-like matter slow with motion as Einstein says, with corrections around 10⁻³⁸ at laboratory speeds; in this shape that matter needs section 10's sign pattern.")
# C79 lines 175, 176
line_rep("- A lower limit comes out only if every tick carries a real chance of a record.",
 "  - No smallest tick follows. A tick near light's crossing time is favoured only if every tick carries a real chance of a record and recording is to run near its fastest. Shorter ticks then slow recording beside records (they do not forbid it), and such chances already freeze slower motion beside records.")
line_rep("- With the small chances that glass and water allow, the tick is only limited from above.",
 "  - With small chances the tick is only limited from above.")
# C74 lines 257, 258; C84 259; C72 260; C76 264; C67 265
line_rep("- light crossing it is left completely alone;",
 "    - light crossing it is never recorded and no recording rule acts on it there; it changes only through its links to records formed elsewhere (your Q1), and on average not at all;")
line_rep("- no faraway influence leaks, because the rule looks only at the records next door,",
 "    - no faraway choice can steer it, because the rule looks only at the records next door, and those always agree with the spot they sit on;")
line_rep("- records spread at most one site per tick, provided the rule looks at the records present at the start of the tick.",
 "    - records spread at most one site per tick, provided the rule looks at the records present at the start of the tick and there is one shared tick.")
sub_rep("Next to any record, the half-filled sea always has some chance of being recorded (exact). So records creep into it, and each new one heats its surroundings far beyond what is seen.",
        "Next to any record, the half-filled sea always has some chance of being recorded (exact for the simplest half-filled sea; the fourth review's check confirms it for the repo's staggered kind). So records creep into it, and each new one heats its surroundings, far beyond what is seen if the rule's energy scale is the Planck scale (argued).")
line_rep("- in dense transparent matter such as glass or water, light escapes recording only if",
 "    - in dense transparent matter such as glass or water, light escapes recording only if records are point-like rather than nucleon-sized, recording is weak, or the rule ignores light.")
line_rep("- **One encouraging case.** With a tidy emptiness",
 "  - **One encouraging case, with a catch.** With a tidy emptiness and records whose content lies along its direction, recording stops once there is nothing left to record, while records keep moving forever: no freezing, no thinning. But this needs stepping odds that let records into calm space, so fully recorded regions then slowly dissolve (section 9). And if record contents are the opposite of the emptiness, every step that brings records together or apart changes the energy by a grid-scale amount.")
# C70 line 276; C67 279, 280; C65 282; C71 284, 285; C70 287, 289; C66 290-292
line_rep("- nothing from outside can ever reach in;",
 "  - nothing from outside can ever reach in (for records and possibilities; gravity's field may still cross, depending on decisions 13 and 21);")
line_rep("- The price: a lone record in empty space can never move either.",
 "  - The price: a lone record in empty space can never move either, and records stop moving through calm space altogether, so section 7's \"records keep moving forever\" does not hold under it. It is also the stepping rule that fits the stricter reading of \"admissible\" (decision 15).")
line_rep("- With any other stepping odds the region slowly dissolves,",
 "  - With fixed odds, or any chance of stepping into calm space, the region slowly dissolves, in a time that grows with its size far more slowly than a black hole's lifetime would. If its contents are the opposite of calm space, each record that leaves also changes the energy by a grid-scale amount. Two other stepping rules seal flat or box-shaped regions (A30).")
line_rep("- At the best catching strength, how much is caught depends only on the speed",
 "  - In a one-line toy, at the catching strength that is best for the fastest things, how much is caught depends only on the speed of what arrives: things near the grid's top speed are caught almost always, slow things mostly bounce. A strength tuned for slow, heavy things catches them much better (up to 99% in the fourth review's check) but other speeds less; no fixed strength catches the slowest things.")
line_rep("- No edge rule catches everything at every speed,",
 "  - No fixed catching rule catches everything at every speed (proved in a one-line toy), and the records' own pull on what arrives can cap catching at two-thirds.")
line_rep("- A rough, spongy edge helps somewhat, but never for the slowest things.",
 "  - A deeper, graded catching layer helps for all but the slowest things (one-line toy); in a flat 2D toy a spongy edge caught about 10% more of the slower waves tested, with a third fewer records.")
sub_rep("layered in the order it arrived. A black hole hides what fell in.",
        "layered in the order it arrived. A black hole in Einstein's gravity hides what fell in (a comparison, not adopted).")
sub_rep("If each recorded spot carries ordinary mass, any packed region",
        "If each recorded spot carries ordinary mass and that mass pulls (which needs more room per place, or gravity places that are never recorded), any packed region")
# C66 290-292: replace 3 lines
i = next(i for i, l in enumerate(lines) if l.startswith("- **Do clocks stop inside?** That depends on a choice for you."))
assert lines[i+1].lstrip().startswith("- If each spot holds only its one qubit's possibilities")
assert lines[i+2].lstrip().startswith("- If each spot can also hold a never-recorded part for gravity")
lines[i:i+3] = [
 "- **Do clocks stop inside?** That depends on choices for you and on strong gravity, which is not worked out.",
 "  - If each spot holds only its one qubit's possibilities (the axioms as written), there are two cases. If records may form at every place, a full region has nothing left to carry gravity, so everything stops; but then its contents do not pull as ordinary mass, gravity ripples bounce off it, and ordinary matter would wall off gravity ripples too, which detected ripples rule out if matter carries about one record per nucleon (A31). If gravity's places never hold records (decision 21), no region can be fully recorded, and gravity runs through it.",
 "  - If each spot can also hold a never-recorded part for gravity (decision 13's \"more room per place\"), gravity's clocks keep running inside, only slower, as long as gravity there is weak. For any region big enough to be black-hole-like, gravity is strong, and the field route cannot yet say whether clocks stop (open)."]
n_ok += 1
# C56/C57 297, 298; C59 300; C58 301; C61 302; C63 305, 307
line_rep("- **The sharp limit (exact, checked).**",
 "- **The sharp limit (exact, checked; single ripples).** Take empty space where every spot points the same way. Among rules built from pairs of neighbours that treat every spot and turn alike, only the plain \"line up with your neighbour\" rule keeps it calm once any record holds the opposite content. Rules with three-spot terms keep it calm too (the fourth review's check), but in every such rule single ripples behave like slow, heavy particles, never like light. Groups of ripples, and backgrounds that do not all point one way, are untested here.")
sub_rep("- **Light-like matter needs a painted-on sign pattern.** A fixed pattern",
        "- **Over that background, light-like matter needs a painted-on sign pattern.** A fixed pattern")
line_rep("- **Signs on the hopping only.** This can be hidden from records,",
 "  - **Signs on the hopping only.** This can be hidden from records only if a record's step carries the same signs, so the step itself must know the pattern. The rule then also favours one direction of the possibilities, and 16 of the 24 turns are no longer treated alike.")
line_rep("- **Two patterns, not one (proved).**",
 "- **The two patterns cannot be one pattern with all the field pattern's turns (proved).** The gravity field's 2×2×2 job pattern keeps certain half-turns of the grid; no sign pattern of the kind light needs can keep them. They can still be tied together as one supplied choice (1 of 16), but then the combined pattern keeps only 12 of the 24 turns. In the hop-only version they might share one label, which needs a piece not yet found.")
line_rep("- **New: gravity's places never hold records (exact).**",
 "- **New: gravity's places never hold records, if gravity lives in the one qubit per place (exact consequence).** If the field lives in each place's one qubit and records never lock it, the places carrying the field can never be recorded. As built, every place carries part of the field, so this would forbid every record. It needs a one-qubit version of the field that leaves some places free (not built), or more room per place (decision 13). Otherwise records wall the field off: with about one record per nucleon, gravity ripples in the Earth would die out within about 70 m (argued), yet ripples that crossed the Earth have been detected (a comparison, not adopted). Under this rule no region can be fully recorded, so section 9's \"everything stops\" picture cannot arise.")
line_rep("- the time-stretch that paces the field has to be a moving part of the field, so each place holds more;",
 "  - the time-stretch that paces the field would have to be a moving part of the field, so each place holds more (argued);")
line_rep("- **Ticks become bookkeeping if the chances per tick shrink with the tick,**",
 "- **Ticks become bookkeeping if the chances per tick shrink with the tick** (argued), which avoids freezing and keeps records from outrunning light. Four choices then matter less and less as the tick shrinks: the claim rule, start-of-tick gating, the formation order and the change per tick.")
# Decisions: C64 decision 0; C75 decision 4; C64 decision 17; C78/C84 decision 18; C67 19; C76 20; C61 21
sub_rep("Decision 12 does not yet, because light-like ripples have not been built in this shape (decision 17).",
        "Decision 12 does not yet: over the calm, all-pointing-one-way background, light-like ripples cannot be made without a painted-on pattern (A31; decision 17).")
sub_rep("Under that rule your Q4 (an uninfluenced site has equal odds) never applies to an actual formation, because a site with no recorded neighbour never forms a record (A28).",
        "Under that rule every forming site has a recorded neighbour. If \"uninfluenced\" in your Q4 means \"no recorded neighbour\", Q4 would never apply to an actual formation; if it means \"nothing tilts the odds\", it still applies next to records (argued, A28).")
line_rep("17. **Light and matter under point 0.**",
 "17. **Light and matter under the record-tick shape.** Over the calm, all-pointing-one-way background, no change that treats every spot and turn alike gives single ripples that move like light (exact). Light-like matter needs a painted-on sign pattern (A31). Either it goes on the whole rule: records can show it, it cannot keep the turns the field's pattern keeps, and tying the two together leaves 12 of 24 turns; and no simple way to give that matter a mass was found. Or it goes on the hopping only: one direction of the possibilities is favoured, against your Q3 for 16 of 24 turns, and records' steps must carry the signs. A background that supplies the pattern itself is being searched (A33). Is a fixed pattern acceptable, given that the record-tick shape was chosen to avoid one for records? Which version, if either?")
sub_rep("18. **What a tick means (A32).** In the point-0 shape, any tick schedule shows in the records only in proportion to the chance of a record per tick.",
        "18. **What a tick means (A32).** In the record-tick shape, if record chances per tick are small, any tick schedule shows in the records only in proportion to that chance.")
sub_rep("    - do same-tick neighbours see each other's new records?\n    - does recording follow each place's own time (needed for gravity; only partly possible for motion)?",
        "    - do same-tick neighbours see each other's new records?\n    - does a forming site look at the records present at its own tick (then chains of new records can outrun one site per tick), or at the previous tick's (a memory)?\n    - does recording follow each place's own time (needed for gravity if record-counting clocks are to agree; only partly possible for motion)?")
line_rep("19. **Sealing records in.**",
 "19. **Sealing records in.** May a record step only into a neighbouring spot that already holds something like its own content (A30)? That lets a fully recorded region last forever, and it fits the stricter reading of \"admissible\" (decision 15). But a lone record in calm empty space could then never move, and records would not keep moving forever (section 7). The alternative, fixed odds (A31's preference), lets records move but makes every fully recorded region slowly dissolve.")
sub_rep("but in glass or water that recording must be very weak (A28).", "but in glass or water that recording must be very weak if records are nucleon-sized (A28).")
line_rep("21. **Gravity's places.**",
 "21. **Gravity's places.** If gravity's field lives in one qubit per place and records never lock it, may the places carrying it be ones that never hold records (A31)? As built, every place carries part of the field, so this needs a one-qubit field that leaves some places free (not built), and it is a fixed pattern of record-free places. Under it, no region can ever be fully recorded. Otherwise records wall off gravity ripples, which detected ripples rule out if matter carries about one record per nucleon.")
open(p, "w").write("\n".join(lines))
print("applied", n_ok)
