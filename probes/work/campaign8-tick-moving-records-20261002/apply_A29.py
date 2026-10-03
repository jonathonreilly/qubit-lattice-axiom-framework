p = "MORNING_DRAFT.md"
s = open(p).read()
n_ok = 0
def rep(old, new):
    global s, n_ok
    assert s.count(old) == 1, ("NOT UNIQUE/MISSING", old[:90], s.count(old))
    s = s.replace(old, new); n_ok += 1

# C42 provenance / title
rep("(v7, after two hostile reviews)", "(v8, after three hostile reviews)")
rep("(A20, checked by both reviewers)", "(A20, checked step by step by the second reviewer)")
rep("Two hostile reviews by separate agents attacked the main claims (the second had read the first), and their corrections are included.",
    "Three hostile reviews by separate agents attacked the main claims (each later one had read the earlier ones), and their corrections are included.")
rep("the log, both reviews, and my own checks.", "the log, all three reviews, and my own checks.")

# C27 line 11
rep("So one thing has to give. The options are a longer reach per tick, a supplied pattern of partners, more room per site, sameness only on average, or, for records only, steps that cannot be undone.",
    "So one thing has to give. The options are: a longer reach per tick, including a change that reaches everywhere but only with an exponentially faint tail beyond the neighbours; a supplied pattern of partners; more room per site; sameness only on average; or, for records only, steps that cannot be undone.")
# owner-rule safety line 13
rep("   - Records form and step only on ticks. A record steps at most one site per tick,",
    "   - In this option, records form and step only on ticks. A record steps at most one site per tick,")
# C53 + C30 line 15
rep("Campaign 7's change sentence comes back as written, and your \"evolves continuously\" holds literally.",
    "Campaign 7's change sentence comes back as written, and your \"evolves continuously\" holds literally between record events (at ticks, records still cut and trade places). This holds for the simple toy change; the light-like pieces built tonight (matter in A26, the shape field in A25) still use fixed patterns.")
# C27 + C41 line 16
rep("   - This gets around point 1's limit, needs no supplied pattern to move things, and has no time-doubled twin. (The gravity field still needs one: point 4.)",
    "   - This does not escape point 1's limit; it uses two of its ways out at once. The smooth change reaches past the neighbours in every tick (only faintly, if the change per tick is small), and records move by steps that cannot be undone. What is new is that the two fit together: records still move at most one site per tick. In the simple toy it needs no supplied pattern to move things, and it has no time-doubled twin while the change per tick stays below a simple bound. (The gravity field still needs a pattern: point 4.)")
# C52 line 18 + C30 compact additions after line 20
rep("     - unrecorded influence has no exact speed limit, only an exponentially faint leak, and only if the change per tick is small;",
    "     - no exact speed limit for unrecorded influence: a leak beyond one site per tick always remains, and it stays exponentially faint only if the change per tick is small;")
rep("     - anything that interferes stays unrecorded between formations.\n3. **The tick.**",
    "     - anything that interferes stays unrecorded between formations;\n     - as built so far, its change moves only ripples that behave like slow massive particles over its calm empty background; light-like ripples are not built yet in this shape;\n     - the empty background stays calm only if every record's content lies along one direction, which the law would have to fix or earlier records pass on.\n3. **The tick.**")
# C38 line 21
rep("3. **The tick.** One shared tick works, and neighbourhood ticks work if they keep in step. In these toys, time running differently in different places must come from how much changes per tick, varying smoothly. It cannot come from how often ticks come.",
    "3. **The tick.** In the ticked toys, one shared tick works, and neighbourhood ticks work if they keep in step. Time running differently in different places must come from how much changes per tick, varying smoothly, not from how often ticks come. Under point 2's shape the change no longer comes in ticks, so these tick results need redoing there.")
# C47 line 23
rep("   - **Record-carried gravity** gets the static picture partly right, but cannot make waves or hold a moving Moon.",
    "   - **Record-carried gravity** gets the static picture partly right, but with wandering records it cannot make waves or hold a moving Moon (argued).")
# C33 line 24
rep("   - **The road left open** is a field carried by the shared possibilities. The grid's own symmetry pins its \"shape\" version to Einstein's linear gravity.",
    "   - **The road left open** is a field carried by the shared possibilities. If its bookkeeping is kept exact (a choice you would make), the grid's turns fix the form of its \"shape\" version to Einstein's linear gravity at long wavelengths. Its speed compared with light, and its strength, are not fixed by this.")
# C29 line 25
rep("   - **Conditions:** its ripples need a change that moves things, which the smooth change of point 2 provides; the places need a fixed 2×2×2 pattern of jobs, or the field comes out as 8 copies (A25); forming a record must not change energy; and how one qubit per site hosts the field is open.",
    "   - **Conditions:** its ripples need a change that moves things. As built, the field gets that from more room per place than one qubit and a fixed 2×2×2 pattern of jobs (A25), whether its change is ticked or smooth. With the usual bookkeeping, leaving out the pattern makes the field come out as 8 copies (exact); an unusual bookkeeping is open. Forming a record must leave energy unchanged on average. Fitting the field into one qubit per place is open.")
# C32 line 26
rep("   - **Matter on that field (A26).** Tied to the field in the simplest fixed way, matter bends light by the full amount and falls alike, with no extra choices. The supplied pieces are how link weight is classed and a small in-block shuffle for one ripple type.",
    "   - **Matter on that field (A26).** In a ticked toy, matter tied to the field in the simplest fixed way follows the field's geometry at the level of rays and to first order. Light is delayed and bent by the full amount, provided the field's space-stretch is twice its time-slowing; that is A23's static solution, which needs the time-stretch to pace the field's own change, a supplied choice. Everything whose weight sits at single places falls alike. Supplied: the tie itself; the rule that a uniform stretch must go unnoticed (a new condition); how link weight is classed; a three-move shuffle inside 2×2 blocks for the diagonal ripple (checked in 2D only); and the matter step's own fixed pattern of partner pairs and signs. See point 6 for why this matter has not yet been built in point 2's smooth shape.")
# C48 line 28
rep("6. **Handedness.** Ticks by themselves do not give a preferred handedness. This is exact for single free particles.",
    "6. **Handedness.** Neither ticks nor smooth change give single free particles on a uniform grid a preferred handedness (exact for steps of strictly limited reach and for any smooth change). Interactions and record edges are untested.")
# C43 line 34
rep("  - Campaign 7's bookkeeping for shared possibilities: joint possibilities across sites, odds from the site's own part, and possibilities changing at once to agree when a record forms.",
    "  - Campaign 7's bookkeeping for shared possibilities: possibilities joined across sites in one combined description, odds from the site's own part, and the exact way they change to agree when a record forms. (That they change at once to agree is your Q1.)")
# C38 line 35
rep("  - No faraway influence faster than one site per tick.\n",
    "  - No faraway influence faster than one site per tick. (Point 0's shape gives this up for unrecorded influence, so the results that lean on it, in points 1 and 4 and the tick results in point 5, would need redoing there.)\n")
# C27 lines 45-49
rep("""moves nothing. The alternatives each carry a cost:
- cycling partner pairs (sub-grid privilege);
- a longer reach (scrambling);
- more room per site;
- sameness only on average.""",
"""moves nothing. The ways out each carry a cost:
- cycling partner pairs (sub-grid privilege);
- a longer but still strict reach (scrambling, in the simplest class);
- more room per site;
- sameness only on average;
- a change with no strict reach at all, only a faint tail (point 0 takes this one; its costs are below).""")
# owner-rule line 54 + C40 line 55
rep("- They are classical facts, and they step on ticks by their own rule.",
    "- In this option, they are classical facts that step on ticks by their own rule.")
rep("with odds that are a straight average over what that neighbour holds, or with fixed odds.",
    "with odds that are a straight average over what that neighbour holds, or with fixed odds (which ignore the neighbours, against Admissibility's \"varies with\").")
# C40 after line 61
rep("The literal \"both try, then pick by odds\" rule leaks faraway choices; the claim rule does not.\n",
    "The literal \"both try, then pick by odds\" rule leaks faraway choices; the claim rule does not.\n- **Not yet checked:** a record that trades places keeps its content, but its new spot's own conditions might not allow that content (for example, a recorded neighbour there may set a different menu). With fixed odds the step ignores this entirely. The claim rule and one of the step weights also look two sites away, one step beyond the nearest neighbours. Point 0 also takes menus from records, which is the proposed menu text below, not your Q7 as decided.\n")
# C27 line 65
rep("- This change is not limited to one site per tick, so the exact limit does not bind it, and it moves things without any supplied pattern.",
    "- This change reaches beyond one site in every tick, though only faintly when the change per tick is small. So it takes the \"longer reach\" way out of the exact limit, in its gentlest form. In the simple toy it moves things without any supplied pattern.")
# C52 line 69, C39 line 70
rep("- **No exact speed limit for unrecorded influence.** A faint, exponentially small leak remains, and only if the change per tick is small.",
    "- **No exact speed limit for unrecorded influence.** A leak beyond one site per tick always remains, and it stays exponentially faint only if the change per tick is small.")
rep("- **The change per tick becomes readable.** So \"one universal tick or local ticks\" now has real content.",
    "- **The change per tick becomes readable** (argued). So \"one universal tick or local ticks\" now has real content, though at Planck ticks the effects are tiny and the tick becomes nearly undetectable in practice.")
# C30 after line 71
rep("- **Steps that look at their neighbours nudge them slightly.** Steps that ignore the neighbours do not.\n",
    """- **Steps that look at their neighbours nudge them slightly.** Steps that ignore the neighbours do not.
- **Only slow-particle ripples so far.** The only change built so far for this shape moves ripples that behave like slow massive particles over its calm empty background, not like light. A light-like version over a calm background is not built yet.
- **A direction for the calm background.** The empty background stays calm only if every record's content lies along the background's own direction. The rule cannot take that direction from the unrecorded possibilities without leaking faraway choices. So it must either be fixed by the law, which privileges a possibility, or passed on from earlier records, and who sets the first one is open.
""")
# C30 line 78
rep("- Campaign 7's change sentence, as written.\n",
    "- Campaign 7's change sentence, as written. This holds for the simple toy change; the light-like pieces built tonight (matter in A26, the shape field in A25) still use fixed patterns.\n")
# C45, C46
rep("leaks past that, by about 28% in the toy.",
    "leaks past that: about 28% with a full unit of change per tick, falling steeply (about the fourth power) as the change per tick shrinks.")
rep("So what is ruled out is Campaign 7's change sentence as written.",
    "So, if records follow the possibilities, what is ruled out is Campaign 7's change sentence as written. Point 0 drops that \"if\", and the sentence comes back.")
# C44
rep("### 2. A record whose place can be read every tick must re-form at each step (A7, A19)",
    "### 2. A record whose place can be read every tick must not ride the shared possibilities (A7, A19, A27)")
rep("- **What re-forming means.** The record forms afresh at each step, and the shared possibilities change at once to agree with it. That is what the Record axiom's \"locks\" already says.",
    "- **One way: re-forming.** The record forms afresh at each step, and the shared possibilities change at once to agree with it. That is what the Record axiom's \"locks\" already says. Point 0's step is the other way: the record keeps its own content and trades places, never riding the possibilities.")
rep("- **Why it must.** Otherwise,", "- **Why.** Otherwise,")
# C37 lines 96-100
rep("""- **Catch, now resolved: the "time-doubled" twin (A22).**
  - A twin that flickers at the tick rate exists exactly when each tick fully swaps a set of partners, which is also what lets light run at the grid's top speed.
  - In that case nothing local can remove it, and slow collisions push half or more of their outcome into the twin.
  - With small changes per tick (which A18's gravity package needs anyway), the twin cannot be produced by a few-particle collision, and many-particle production falls off extremely fast.
  - The price: light runs well below the grid's top speed.""",
"""- **Catch, avoidable: the "time-doubled" twin (A22).**
  - In the ticked toys, a twin that flickers at the tick rate exists exactly when each tick fully swaps a set of partners, which is also what lets light run at the grid's top speed.
  - In that case no interaction that respects the turning of possibilities can remove it. Slow collisions push up to about half (different particles) or nearly all (identical particles) of what they scatter into the twin.
  - With small changes per tick, starting from empty space, no collision of fewer than about 90–200 particles can make a twin (exact). Many-particle production falls off extremely fast (argued from a standard result and a small toy).
  - The price: light runs well below the grid's top speed. A18's package needs small changes anyway in one way of writing its coupling, but not in the other (point 6). Point 0's smooth change has no such twin at all below a simple bound.""")
# C38 point 4 and 5
rep("### 4. An exact speed limit, and relativity at low speed (A5)",
    "### 4. An exact speed limit, and relativity at low speed, for ticked change (A5)")
rep("- In a one-dimensional toy, moving clocks slow by the Einstein amount, and each kind of matter gets its own top speed.\n",
    "- In a one-dimensional toy, moving clocks slow by the Einstein amount, and each kind of matter gets its own top speed.\n- Point 0's smooth change gives up this exact limit for unrecorded influence, and these exact one-dimensional identities with it.\n")
rep("The seam is a mirror wall that records can reveal.", "The seam is a mirror wall that records can reveal (ticked change only).")
# C34
rep("- **A one-number (scalar) field fails.** Light bends the wrong way unless the grid's rest frame is singled out.",
    "- **A one-number (scalar) field fails** (argued, against measurements). Tied to matter in the usual ways, it bends light either not at all or only half as much as seen. The full amount needs the grid's rest frame singled out, which tests for a preferred frame rule out. It also gives no frame dragging and the wrong kind of waves.")
# C33 lines 172-173
rep("  - The grid's own turns, plus exact bookkeeping, fix every number exactly as in Einstein's linear gravity (checked, and confirmed by hand).",
    "  - If the field's bookkeeping is kept exact, the grid's own turns fix its form exactly as in Einstein's linear gravity at long wavelengths (checked, and confirmed by hand twice). Not fixed: the ripples' speed compared with light, and gravity's strength. At grid scale, direction-dependent corrections are free but tiny.")
rep("  - A stepping rule gives two wave polarisations at light speed, with no time-doubled twin, full light bending, and all matter falling alike.",
    "  - A stepping rule gives two wave polarisations at one common speed, equal to light's only if the two are set together, with no time-doubled twin. With matter tied in (A26), it gives full light bending, and everything whose weight sits at single places falls alike.")
# C49 line 176
rep("    - The field can be stepped with next-door moves only, treating every turn of the grid alike and keeping its bookkeeping exact at every step. Its ripples then come out exactly right: two kinds, at light speed, with nothing extra.",
    "    - The field can be stepped with next-door moves only. Its rule treats every turn of the grid alike once the jobs are relabelled along with the turn, and it keeps its bookkeeping exact at every step. At linear order its ripples come out right: two kinds, all at one speed, with nothing extra.")
# C35 lines 180-184
rep("""  - Forming a record must not change energy, or a phantom weight remains where the record formed. A24 found this is possible, but only one way: catch first, record later.
    - A small thing is caught at one spot, and its spare energy flies off.
    - The record then forms at the catching spot. It costs nothing once the spare energy has left.
    - Recording anything still freely spreading jolts it by about half its whole energy range, which is enormous on the finest grid.
    - So records must form only on caught, settled things, and slowly. This matches how real detectors work (absorb, then amplify).""",
"""  - Forming a record must leave energy unchanged on average, or a phantom weight remains where the record formed (A23). A24 found exactly when that holds: when the rival possibilities no longer overlap through any of the spot's links, because the change has already carried the difference away ("settled"). Something still freely spreading is never settled. A24 built one working example in a supplied toy, "catch first, record later":
    - A small thing is caught at one spot, and its spare energy flies off.
    - The record then forms at the catching spot. Once the spare energy has left it costs almost nothing; forming sooner costs more.
    - Recording a freely spreading thing at one exact spot jolts it by about half its whole energy range, which is enormous on the finest grid. Recording it loosely costs less, but never nothing.
    - So, under the gravity field, almost all records would have to form on caught, settled things, and slowly. Earth's heat flow allows other records only extremely rarely. This matches how real detectors work (absorb, then amplify; a comparison, not adopted).
    - The toy needs a trap and a separate channel for the spare energy. Whether the framework's own change can catch and release like that is open.""")
# C29 line 186
rep("  - How one qubit per site hosts the field is open.\n",
    "  - Whether the field can be fitted into one qubit per place, for example as a collective ripple of many places, is open.\n")
# C32 lines 190, 193, 196; C31 line 194
rep("  - Then light and matter both follow the field's own geometry.",
    "  - Then, at the level of rays, to first order in the field and for a small change per tick, light and matter both follow the field's own geometry.")
rep("The field's own bookkeeping requires that classing anyway, but at grid level it is supplied.",
    "The field's own bookkeeping requires that classing anyway (argued, at long wavelengths), but at grid level it is supplied.")
rep("  - **The diagonal ripple.** One of the two ripple types is felt only if each step's sense of direction is turned by a fixed three-move shuffle inside each 2×2 block. No simpler local tweak does it; one tweak makes the two copies of each particle feel opposite ripples. The shuffle is supplied.",
    "  - **The diagonal ripple.** One of the two ripple types is felt only if each step's sense of direction is turned by a fixed three-move shuffle inside each 2×2 block. None of the simple next-door tweaks tested does it, and one of them makes the two copies of each particle feel opposite ripples. The shuffle is supplied, checked in 2D only, and whether it treats all 24 turns alike in 3D is unchecked. It is built from ticked moves, and it reaches diagonally across the block. A smooth change made only of next-door terms (point 0) cannot produce it, so matter on the field has not yet been built in point 0's shape.")
rep("  - **My check.** I rebuilt the 2D toy independently: all four bands follow the field's geometry exactly.",
    "  - **My check.** I rebuilt the 2D toy's band structure independently: the slopes of all four bands follow the field's geometry exactly, and massive bands agree to about 0.1%.")
# Decisions
rep("The price is an exact speed limit for unrecorded influence. Several decisions below then simplify: decisions 1, 2, 8 and 12 mostly resolve in its favour.",
    "The price is giving up an exact speed limit for unrecorded influence: it leaks past one site per tick, and the leak stays exponentially faint only if the change per tick is small. It brings its own choices: how much the change does per tick, how often records step and with which weighting, the claim rule (which looks two sites away), and an order for overlapping formation spots. Decisions 1, 2 and 8 then mostly resolve in its favour. Decision 12 does not yet, because light-like ripples have not been built in this shape (decision 17).")
rep("   - a faint longer reach.\n", "   - a faint longer reach (point 0's shape takes this one: the change reaches everywhere, faintly).\n")
rep("and the emptiness next to matter is tidy, not half-filled.",
    "and the emptiness next to matter is tidy, not half-filled. Under that rule your Q4 (an uninfluenced site has equal odds) never applies to an actual formation, because a site with no recorded neighbour never forms a record (A28).")
rep("Does \"permanent\" mean \"never destroyed, may re-form next door\"?",
    "Does \"permanent\" mean \"never destroyed, may move next door (by re-forming, or by trading places as in point 0)\"?")
rep("and still needs a rule for two records wanting one site. Or by a supplied sub-grid pattern (A10)?",
    "and still needs a rule for two records wanting one site. Or by a supplied sub-grid pattern (A10)? Or by trading places with an empty neighbour and keeping its content (point 0, A27)? That one is not tied to the grid; the open item is whether its content suits its new spot (decision 15).")
rep("is the in-block shuffle allowed?",
    "is the in-block shuffle allowed? As built, the field needs more settings per place than one qubit holds. May a place hold more (a change to the Qubit axiom), or must the field be built from one qubit per place, for example as a collective ripple (open)?")
rep("This is needed for energy bookkeeping under the gravity field, and for straight tracks (A19).",
    "Under the gravity field this is needed for almost all records (others only extremely rarely), and it also gives straight tracks (A19).")
# New decisions 15-18 (A29 open questions)
rep("and it also gives straight tracks (A19).\n",
    """and it also gives straight tracks (A19).
15. **A moved record's new spot.** Under point 0's swap step, a record carries its content to a new spot whose own conditions might give that content zero odds. Should a step be allowed only where the content is on the new spot's menu (A29)?
16. **The calm background's direction.** Under point 0, empty space stays calm only if every record's content lies along its direction. Is that direction fixed by the law (which privileges a possibility), or passed on from a first record (A29)?
17. **Light and matter under point 0.** No smooth, everywhere-alike change on one qubit per site has yet produced light-like ripples over a calm background; the matter and the field built tonight both use fixed patterns. Is a fixed pattern acceptable for light and matter, given that point 0 was chosen to avoid one for records? If a pattern is used, should matter's sub-grids, its 2×2 cells and the field's 8 layouts be one shared choice (A31 is checking whether they can be)?
18. **What a tick means.** If record chances per tick are scaled down to avoid freezing, ticks become almost undetectable at Planck spacing (argued). Would "records form at set ticks" then be a physical statement or a bookkeeping one? This is exploration of your instinct, not a position.
""")
rep("*Still running: a third hostile review (A29) of A22–A27 and this draft; A30 (your black-hole idea under the point-0 shape). Next: A31, assembling the point-0 shape into one model.*",
    "*Still running: A30 (your black-hole idea under the point-0 shape) and A31 (assembling the point-0 shape into one model, including whether one shared pattern could serve matter and the field).*")
open(p, "w").write(s)
print("applied", n_ok, "replacements; length", len(s))
