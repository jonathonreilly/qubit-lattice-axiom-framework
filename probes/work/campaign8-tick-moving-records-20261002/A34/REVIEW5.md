# A34 hostile review, round 9 (REVIEW5): A41, the doc's A41 note, and a final summary skim

**Scope and sources.** I read these primary files only:
- A41: REPORT.md and the d1–d9 outputs;
- MORNING_DRAFT.md (07:07): section 14, the A41 note, and lines 1, 22, 51, 318 and 445;
- MORNING_SUMMARY_DRAFT.md (06:42), in full.

I ran no new numerics. Every claim below is an exact argument, graded as such. I ran no git, made no repo edits, and edited no other agent's files.

**Counts.** 4 MAJOR (C145–C147, C150) and 7 MINOR (C148, C149, C151–C155).

## Verdict on A41: holds as graded, with three corrections

These parts are sound and correctly graded:
- the closed form (EXACT; it agrees with c13 and with the coordinator's B(k));
- the reductions H24 ≅ 2H6 ⊕ 2(−H6) (EXACT);
- the zero-flux θ = 0 triple points with slopes (2,1,1)t (EXACT);
- the θ = π/2 π-flux cones and lines (CHECKED);
- the symmetry reduction θ ∈ [0, π/2] (EXACT).

The mean-field caveat is stated properly in the report: in the header and in open edge 4, where U = σ⁺ is nilpotent with |⟨U⟩| ≤ ½.

The verdict (ARGUED) is fairly scoped, and it is stronger than A41 says. Zero flux and π flux are the only uniform link backgrounds the turns allow. Under a turn, a square's flux can come back reversed, so a uniform flux must equal its own reverse: Φ = −Φ mod 2π (EXACT).

Three corrections:
1. **Tr H = 0 ⇒ "the empty matter vacuum is never lowest in the one-particle sector" holds for the hop alone (EXACT), not in general.** The triplet is irreducible under the turns, so by Schur's lemma the only on-site term they allow is μ·1, a uniform energy per charge. That term is also gauge-invariant. It shifts Tr H(k) to 3μ. For μ at or above the band's half-width, every one-particle energy is ≥ 0 and the empty vacuum is lowest. The price is that every zero-energy crossing moves up to E = μ, with lower states beneath it (A39 (a′)). So the true statement is: "zero-cost crossings over the empty vacuum force negative energies; lifting them gives (a′)." This is what section 14's price list already says.
2. **One sign of charge (EXACT; missing from A41 and the doc).** With two qubits per corner, the only turn-invariant operators are combinations of the singlet and triplet projectors (A40 M2). So relative to the singlet empty state, charge takes a single nonzero value. There is no antimatter.
   - A filled sea, open edge 5's alternative, would carry net charge.
   - On a closed grid, Gauss's law forces the total charge to zero, so it allows no net charge at all without a background offset.
   - Both signs of charge need more room per corner or a further background-charge pattern (ARGUED).
3. **Scope.** The family is nearest-corner hops only. A38 showed that longer hops can evade nearest-neighbour twist constraints. The verdict should say "nearest-corner hops".

## Findings

### C145 — MAJOR: the doc's A41 note drops the toy's conditions and states a route-level verdict

- **Where.** MORNING_DRAFT.md, the paragraph that begins "**Follow-up on the twist from light (A41; checked by me, not hostile-reviewed).**"
- **Quote.** "**So** the twist-from-light route gives near-misses, not clean light."
- **What is wrong.**
  - Every result in the note comes from a single-particle toy with light's links replaced by fixed numbers. The note never says so.
  - The toy uses the least room (two qubits per corner) and nearest-corner hops only.
  - So the conclusion is about this toy, not about the route.
  - This finding's replacement also carries the fixes from C146–C148.
- **Replacement text** (the whole paragraph and list):
  > **Follow-up on the twist from light (A41; checked by me and by one hostile review round).** In a single-particle toy where light's links are replaced by fixed numbers (light's twisted or untwisted pattern, not its quantum state), the charged matter that can hop through light's links with the least room (two qubits per corner) has three internal states that turn as it hops, and its nearest-corner rule has one free angle.
  > - **With light's half-turn twist on every square:** perfectly round light-like cones appear at one setting of that angle (same speed in every direction, checked over 300 directions). But straight lines of zero-energy states come with them, and every other setting tried gives the cones a gap (checked).
  > - **Without the twist:** the hop itself already makes zero-energy crossings at two settings. At one, they are lopsided (twice as fast along one diagonal as across it) with a flat band through them (exact; my check reproduced both). At the other, sheets of zero-energy states pass through them (checked).
  > - **Negative energies:** with the hop alone, every setting has negative energies, so matter's empty state is not its lowest (exact). An energy cost for each charge can lift all states above zero, but then every zero-energy crossing moves up to that cost with lower states beneath, as in the price list above.
  > - **One sign of charge:** with two qubits per corner, charge comes in one sign only, so there is no antimatter (exact). Both signs need more room or a further pattern (argued).
  > - **So** in this toy the twist-from-light route gives near-misses, not clean light, and the free angle would be one more choice put in by hand. The quantum version, with light's links as qubits under Gauss's law, is open.

### C146 — MAJOR: "Always ... never its lowest (exact)" is exact only for the hop alone

- **Quote.** "**Always:** negative energies exist, so matter's empty state is never its lowest (exact)."
- **What is wrong.** The turns allow an on-site energy per charge, μ (Schur's lemma on the triplet). It can lift every one-particle energy above zero. The crossings then sit at a finite energy with lower states beneath (A39 (a′)).
- **Fix.** The "Negative energies" bullet in C145.

### C147 — MAJOR: one sign of charge (no antimatter) is a missing cost

- **Where.** The A41 note, and A40/A41 generally.
- **What is wrong.** At two qubits per corner, the turn-invariant charge has only two values, so there is one charged species and no antiparticle (EXACT). This is a real cost for "charged matter". It also rules out a filled sea, which would carry net charge that a closed grid's Gauss's law forbids.
- **Fix.** The "One sign of charge" bullet in C145.

### C148 — MINOR: "for one setting" and "any other setting" misstate A41

- **Quotes.**
  - "...the hop itself already makes crossings at zero energy for one setting..."
  - "...any other setting gives the cones a gap."
- **What is wrong.**
  - A41 also has zero-flux crossings at θ = π/2 (location EXACT, with zero-energy sheets through them).
  - The gapping off θ = π/2 is CHECKED at the sampled angles, not shown for every angle.
  - "The only charged matter" holds at the least room. With more room, other triplet-type reps can be charged as well.
- **Fix.** Already in C145's replacement.

### C149 — MINOR: A41 report wording (not doc text)

- **§2, "Negative energies".** After "The empty matter vacuum is never the lowest state of the one-particle sector", add: "for the hop alone; the turn-allowed on-site energy μ·1 (Schur) shifts Tr H to 3μ and can lift all energies above 0, moving every zero-energy crossing to E = μ (A39 (a′))".
- **Verdict.** Add: "nearest-corner hops only; zero and π flux are the only uniform backgrounds the turns allow (EXACT)".
- **Open edge 5.** Add: "with two qubits per corner charge has one sign, so a filled sea would carry net charge, which Gauss's law on a closed grid forbids (EXACT)".

### C150 — MAJOR: the summary still says light-like matter needs a painted pattern

- **Where.** Summary line 46. The same sentence appears in draft line 22, the bold lead of line 318, and decision 17 (line 445).
- **Quote.** "Light-like matter then needs a pattern of plus and minus signs painted onto the rule."
- **What is wrong.** This holds for matter with one internal state per place (A31). It is contradicted by the corrected section 14 and by A41:
  - matter with internal parts can get a twist from the rule itself, with no pattern (c13; neutral vector matter, with a flat partner);
  - A41's charged triplet has zero-energy crossings without any twist, and round cones with light's twist at one setting.
- **Replacement text.**
  - Summary line 46:
    > - Light-like matter with one internal state per place then needs a pattern of plus and minus signs painted onto the rule. Matter with internal parts that turn with the grid can get a twist from the rule itself, but so far only lopsided crossings, or round ones with heavy or zero-energy partners beside them (A41; fourth review).
  - Draft line 22: after "Over that background, light-like matter" insert "with one internal state per place".
  - Draft line 318, bold lead: "**Over that background, light-like matter with one internal state per place needs a painted-on sign pattern.**"
  - Decision 17: "Light-like matter with one internal state per place needs a painted-on sign pattern (A31)."

### C151 — MINOR: the summary's A40 sentence predates A41

- **Where.** Summary line 48, its last sentence.
- **Quote.** "...and open questions about how charged matter hops through light's links and about matter's empty space."
- **Replacement text** (replace the quoted tail, then append a sentence):
  > ...and charged matter that has three internal parts and one sign of charge. A follow-up (A41), with light's links held as fixed numbers, found such matter gets round light-like cones only at one setting of a free angle, with zero-energy lines beside them, and over its empty state it has negative energies unless each charge is given an energy cost, which lifts its crossings off zero.

### C152 — MINOR: summary item 4 lists two of A39's three ways out

- **Where.** Summary line 36.
- **Quote.** "next to matter the emptiness would have to be the tidy, lined-up kind, or recording there would have to build up slowly over many ticks;"
- **Replacement text:**
  > next to matter the emptiness would have to be the tidy, lined-up kind (which carries only slow ripples), recording there would have to build up slowly over many ticks, or records there would have to be blind to light (A39);

### C153 — MINOR: summary item 5 omits that A40's layout changes the black-hole picture

- **Where.** Summary line 38. Append to the item's first sentence:
  > (Under A40's candidate layout no region can ever be fully recorded, since light and gravity places never record.)

### C154 — MINOR: review counts and labels

- **Summary line 10.** Replace "Eight rounds" with "Nine rounds".
- **Draft line 1.** Replace "(v12, after eight review rounds)" with "(after nine review rounds)".
- **Draft line 51.** Replace with:
  > Nine rounds of hostile review by four separate agents attacked the main claims (the second reviewed twice and the fourth five times; each later round had read the earlier ones; the last two covered only the late sections 12 to 14, the A41 follow-up and the summary), and their corrections are included.
- **A41 note label.** Covered by C145.

### C155 — MINOR: summary decision (17) misses the internal-parts option

- **Where.** Summary line 62.
- **Replacement text:**
  > - **(17)** Is a painted-on sign pattern acceptable for light and matter, and which version, or should matter instead carry internal parts that turn with the grid (A40, A41)?

## Fine as written

- **Section 14 as corrected.** It is consistent with A41: the price list already covers lifting energies (A39 (a′)). Adding C145's note completes it.
- **Summary items 1–3 and the gravity and handedness items.** These are consistent with all earlier corrections.
- **Summary lines 47–48.** They match the corrected sections 12–13, apart from the A41 update (C151).
- **Owner rules.** No "read" possibilities, no adopted beat, Q7 untouched, and choices framed as yours. The same holds in every replacement above.
