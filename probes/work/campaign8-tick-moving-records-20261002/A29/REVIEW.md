# A29 third hostile review: A22–A27 (A25 added by scope), the Theorem N interface, and MORNING_DRAFT v7

**Provenance.**
- I read these primary files:
  - BRIEF;
  - the LOG correction sections C1–C26;
  - A16/REVIEW.md, A21/REVIEW_FINAL.md and A20/REPORT.md;
  - the full reports of A22, A23, A24, A25, A26 and A27;
  - A28's Answer section, since the draft now quotes A28;
  - A3:229 (for the draft's "28%");
  - the coordinator's `toys/verify_A25_symbol.py`;
  - MORNING_DRAFT v7, the 02:11 file (269 lines; line numbers below refer to it).
- I had read both earlier reviews, so I am not independent of them.
- I wrote only into `c8/A29/`. I made no git operations and no repo edits.

**What I ran.** Machine load was 2.5–3.7. Each run used `nice -n 10` and all four thread caps at 1.

| Script → output | What it checks | Time, memory |
|---|---|---|
| `thmA_continuous.py` → `out_thmA_continuous.txt` | A25 Theorem A in continuous time (no tick) | 0.24 s, 34 MB |
| `wilson_continuous.py` → `out_wilson_continuous.txt` | A25 S17 patch stability in continuous time | 1.4 s, 28 MB |
| `wilson_small_r.py` → `out_wilson_small_r.txt` | The same patch as its strength r → 0 | 2.3 s, 28 MB |

**Grades.** As the lanes use them: EXACT, CHECKED, ARGUED, SUPPLIED.

---

## 0. Direct answers to the coordinator's questions

**Q-a. Does Option R "sidestep" Theorem N?** The derivation is right, but the framing is wrong (C27).
- Theorem N's hypotheses (A20:75, A21 C21) are:
  - (i) the tick is a reversible automorphism;
  - (ii) strict nearest-neighbour reach, α(A_x) ⊆ A_{N̄(x)};
  - (iii) exact soldered covariance on the tick;
  - (iv) one qubit per site with an ordinary (ungraded) product.
- Option R's change between ticks, e^{−iH_Rτ}, keeps (i), (iii) and (iv) and drops **only (ii)**. Its reach is unbounded, with tails of about 2τ⁴ outside the 3-site window (A27:196–198).
- That is exactly A20's listed **relaxation 3, "Quasi-locality. Exact covariance at every instant, but the tails break I2"** (A20:196), already flagged as D3 (A20:168). It is the unbounded-reach limit of relaxation 1, "longer reach per tick".
- The full per-tick map also drops (i) for records, through the irreversible step: relaxation 6.
- So Option R takes **two of Theorem N's listed exits at once**: quasi-locality for possibilities, irreversibility for records.
- What A27 genuinely adds: A20 priced relaxation 3 as "the tails break I2". A27 shows the tails break I2 only for *unrecorded influence*. Records still move at most one site per tick, because they do not ride the change (EXACT by construction).

**Q-b. Does the Lieb–Robinson tail violate an owner decision?**
- No decided reading (Q1–Q4, Q7) requires a strict cone.
- Q2 ("the rule acts locally on the full snapshot") is met at every instant, because the generator is a sum of nearest-neighbour terms.
- What the tail does contradict:
  - the draft's own stated premise that "most results lean on" (draft:35);
  - A5's exact one-dimensional identities;
  - the stepped-tick conclusions the draft still presents as general (C38).
- Campaign 7 sentence 4 survives only as "no nonlinear signalling". In a reading where light is the record cone, the tail is faint faster-than-cone influence (ARGUED; A27's own falsifier, A27:318).

**Q-c. "Unglued (Q3 OK)", "no doubler", "no sub-grid privilege".**
- **Unglued: TRUE** for the swap step (CHECKED by A27 and by the coordinator).
  - A note: A27's example change (Heisenberg) is invariant under turning possibilities alone. It satisfies Q3's "change glued" only in the weak (covariance) sense.
  - Light-like matter needs the strong, direction-tied gluing (A23 D18, A26 D2). This is not a contradiction, but nothing in A27 tests it.
- **No doubler: TRUE only for *time* doublers**, below the single-particle aliasing bound max|E|τ < π (A27:204).
  - Spatial doubling remains for matter (A27:206–208).
  - Spatial doubling remains for the shape field unless roles are supplied (A25 Theorem A, which I checked also holds in continuous time; C29).
- **No sub-grid privilege: TRUE for A27's toy** (Heisenberg change, swap step, claim rule).
  - FALSE for the physics package as built tonight: A26's light-like matter uses A10's partner round, a staggered mass, KS signs and 2×2 cells (C31), and A25's field uses a 1-of-8 role layout (C29).
  - "Random order" for overlapping formation (A27:218) is quasi-local, a further named choice.

**Q-d. Does A25's Theorem A (S12) apply to A27's continuous-time setting? YES (EXACT; CHECKED).**
- Theorem A constrains only the spatial gauge generator g(k) and the potential V(k) at K = (π,π,π) (A25:199–205). No time step enters its proof.
- In continuous time the frequencies are ω² = eig(M·V(k)). So V(K) = 0 forces gapless non-gauge modes at K whatever the time evolution.
- `thmA_continuous.py` (CHECKED), on three O_h-covariant collocated families (covariance residual ≤ 2.2e-16, gauge invariance |VD| ≤ 2.5e-19):
  - |g(K)| ≤ 3e-16 and max|V(K)| ≤ 2e-32;
  - at K + q, exactly two nonzero ω², with ω²/|q|² = 1.000, 1.960 and 0.490 as |q| → 0;
  - that is a full second massless graviton at the corner, with no tick anywhere.
- The staggered (role) control at K is gapped: ω² = 12.000.
- The coordinator's `verify_A25_symbol.py` part (5) shows the same thing for central differences (V = 0 at all 8 corners).
  - Its part (3) shows continuous time works *for the staggered layout*, i.e. with roles. It does **not** show that roles are unnecessary.
- A25 S17's patch instability is also not a stepping artifact (`wilson_continuous.py`, `wilson_small_r.py`, CHECKED):
  - The full Wilson patch grows ×1.414 per τ = 0.5 at r = 0.01, through the conformal (trace) mode at (π,π,π). That equals A25's stepped 1.41.
  - The traceless-only patch also grows, through complex ω²: 0.37–0.50 per unit time for r = 0.01–0.25.
  - As r → 0 the growth falls only as about 1.8–2.0·r^{1/4}, for example 0.11 at r = 1e-5.
  - So no weak patch is stable.
- **A27:255 "A smooth covariant field generator needs no staggered roles" FAILS.** A23 itself had already said this (A23:160, tension (c)).

---

## 1. Verdicts per lane

| Lane | Verdict | One-line reason |
|---|---|---|
| **A27** Option R | **Holds with narrowing** (one claim fails) | The construction (compression, swap step, claim rule) is sound and covariant. But it takes Theorem N's quasi-locality and irreversibility exits rather than "not applying". "No staggered roles" for the field FAILS (Theorem A). Its quiet vacuum carries only z = 2 ripples and needs every record's content on the vacuum axis. Admissibility of a moved record at its new site is unchecked. |
| **A23** field route | **Holds with narrowing** | EH at O(k²) and the DeWitt weights (−½,1,1) are correct; I re-derived both by hand. They hold at long wavelength, linear order, given tensor content (F1) and F4 (which includes gauge invariance), and fix ratios only, not speed relative to light or strength. "Scalar fails" is ARGUED/COMPARATOR under stated coupling assumptions. Spatial roles are needed (its own tension (c)). |
| **A26** matter on the field | **Holds with narrowing** | "Sees the metric" is EXACT only in the eikonal, first-order, small-dose limit. G1 is a continuum conditional (stated by A26, dropped by the draft). The Laue argument is graded correctly. Its matter is a stepped, patterned circuit, and by its own D9 its cross-shear coupling cannot be made by a smooth nearest-neighbour generator. |
| **A24** energy-gentle locks | **Holds with narrowing** | The bookkeeping is EXACT, and "settled ⇒ zero ghost" is EXACT as a *sufficient* condition. "Catch first, record later" is a constructed toy, not "the only way", and is not yet available in the framework's own change. "Half the energy range" applies to sharp records only. "Must only" should be "rate-bounded". All numbers verified except one κ range. |
| **A22** time doublers | **Holds with narrowing** | The "iff" is EXACT for 1D two-layer number-conserving swap rounds. The arc lemma counts excitations over *emptiness*. The heating exponent is a 4-point 1D fit extrapolated about 100× in 1/θ (ARGUED). The draft's "nothing local can remove it" and "half or more" overstate. |
| **A25** stepping the shape field | **Holds** | Theorem A is correct and applies in continuous time (CHECKED here). S17 instability carries over (CHECKED here). The only narrowing is wording: "covariant" means covariant with role relabelling, and "light speed" means speed 1 in grid units. |
| **MORNING_DRAFT v7** | **Needs changes** | 1 BLOCKER (decision 0 states the price backwards). The MAJORs are: the Theorem N framing; missing Option R costs; A26 and A23 scope; A24 "only one way"; cross-lane strict-cone conflicts; more room per site; destination admissibility. |

---

## 2. Findings (continuing the correction numbering)

### A27 / Option R

**C27. MAJOR. "Theorem N does not apply" / "gets around point 1's limit" is the quasi-locality exit, not an escape.**
- **Claims.**
  - A27:29: "Theorem N does not apply: the change is not nearest-neighbour per tick, yet it moves content."
  - LOG:1074: "**Theorem N does not apply.**"
  - Draft:16: "This gets around point 1's limit, needs no supplied pattern to move things…"
  - Draft:65: "This change is not limited to one site per tick, so the exact limit does not bind it…"
  - Draft:45–49 lists "a longer reach (scrambling)" as an *alternative* that Option R avoids.
  - Draft:11 omits quasi-locality from the list of ways out.
- **What is wrong.** A27's own Step 6 (A27:196) says the hypothesis α(A_x) ⊆ A_{N̄(x)} fails. That is A20 relaxation 3 (A20:196) and A20 D3 (A20:168). The draft presents Option R as avoiding the exits when it uses two of them. A reader concludes the limit was beaten for free.
- **Corrected wording (EXACT).** "Option R drops exactly one of Theorem N's hypotheses for the possibilities, the strict per-tick nearest-neighbour reach. This is A20's quasi-locality exit. Records use the irreversible-moves exit. New (EXACT by construction): the two fit together, so the tails do not break I2 for records."
- **Draft changes.**
  - Line 11, replace the last sentence with: "So one thing has to give. The options are: a longer reach per tick, including a change that reaches everywhere but only with an exponentially faint tail beyond the neighbours; a supplied pattern of partners; more room per site; sameness only on average; or, for records only, steps that cannot be undone."
  - Line 16, replace with: "This does not escape point 1's limit; it uses two of its ways out at once. The smooth change reaches past the neighbours in every tick (only faintly, if the change per tick is small), and records move by steps that cannot be undone. What is new is that the two fit together: records still move at most one site per tick. In the simple toy it needs no supplied pattern to move things, and it has no time-doubled twin while the change per tick stays below a simple bound. (The gravity field still needs a pattern: point 4.)"
  - Lines 45–49, replace the list intro with: "The ways out each carry a cost:". Change the second bullet to: "a longer but still strict reach (scrambling, in the simplest class);". Add a fifth bullet: "a change with no strict reach at all, only a faint tail (point 0 takes this one; its costs are below)."
  - Line 65, replace with: "This change reaches beyond one site in every tick, though only faintly when the change per tick is small. So it takes the 'longer reach' way out of the exact limit, in its gentlest form. In the simple toy it moves things without any supplied pattern."

**C28. BLOCKER (draft). Decision 0 states the price backwards.**
- **Claim.** Draft:250: "The price is an exact speed limit for unrecorded influence."
- **What is wrong.** The price is *losing* the exact speed limit (A27:39, A27:262).
- **Replacement.** "The price is giving up an exact speed limit for unrecorded influence: it leaks past one site per tick, and the leak stays exponentially faint only if the change per tick is small."

**C29. MAJOR (lane); the draft is already mostly fixed in v7. "A smooth covariant field generator needs no staggered roles" FAILS.**
- **Claims.**
  - A27:255: "viable without Theorem N trouble. A smooth covariant field generator needs no staggered roles."
  - LOG:1092: "with no staggered roles needed".
- **What is wrong.**
  - Continuous time removes only the *temporal* leapfrog layering.
  - Doubler-free exact gauge invariance needs *spatial* staggered placement. A23 tension (c) (A23:160) says so; A25 Theorem A (A25:199) proves it for the standard gauge symmetry; my continuous-time check confirms it (section 0, Q-d).
  - The S17 patches are unstable in continuous time too, with growth about 2·r^{1/4} (CHECKED).
  - A25's construction leaves Theorem N's premises through *more room per site plus roles* (A25:186), not through smoothness.
- **Corrected wording (EXACT + CHECKED).** "In continuous time the field has no time doubler and no leapfrog layers. It still needs A25's 1-of-8 role layout (F6) or an open, lattice-modified gauge symmetry, plus more than one qubit per site."
- **Draft.** Lines 79 and 178 are now correct. Residual edits:
  - Line 25, replace with: "**Conditions:** its ripples need a change that moves things. As built, the field gets that from more room per place than one qubit and a fixed 2×2×2 pattern of jobs (A25), whether its change is ticked or smooth. With the usual bookkeeping, leaving out the pattern makes the field come out as 8 copies (exact); an unusual bookkeeping is open. Forming a record must leave energy unchanged on average. Fitting the field into one qubit per place is open."
  - Line 186 (now redundant with line 179), replace with: "Whether the field can be fitted into one qubit per place, for example as a collective ripple of many places, is open."

**C30. MAJOR. Option R's empty background: only slow-particle ripples, and calm only if every record's content lies on the vacuum's axis. The draft omits both.**
- **Claims omitted from the draft's cost lists (draft:17–20, 68–74).**
  - A27:315: "z = 2 ripples over an aligned quiet vacuum (A9)".
  - A27:330: light-like content over a quiet vacuum is OPEN.
  - A27:166–167: "The aligned emptiness |n⟩ is left alone by the compressed field … only if n_r = ±n (EXACT)".
  - A27:327: off-axis records "risk breeding".
- **What is wrong.**
  - (i) The only change built in Option R moves z = 2 (non-relativistic) magnons over its calm vacuum. No light-like ripple has been built in Option R's smooth, homogeneous form.
  - (ii) Calm requires every record's content to be ±n. The formation rule cannot take n from unrecorded possibilities without signalling (C4). So n must be a law-level axis, which privileges a possibility: A13's cost, C7. Otherwise it must be inherited from earlier records, and A13 E2's "who sets the first frame" is open.
  - (iii) Hence draft:15 and draft:78, "Campaign 7's change sentence comes back as written", hold for the toy Heisenberg change only. The light-like pieces built tonight (A26 matter, A25 field) are not homogeneous nearest-neighbour generators in that sense.
- **Corrected wording (EXACT for the conditions; ARGUED for the consequence).** "Option R as built has a calm vacuum only with all record contents along its axis, and its ripples there are z = 2. Light-like content is open."
- **Draft.** Add to the cost list after line 20 and after line 71:
  - "- the only change built so far for this shape moves ripples that behave like slow massive particles over its calm empty background, not like light; a light-like version over a calm background is not built yet;
  - the empty background stays calm only if every record's content lies along the background's own direction. The rule cannot take that direction from the unrecorded possibilities without leaking faraway choices. So it must either be fixed by the law, which privileges a possibility, or passed on from earlier records, and who sets the first one is open."
  - Lines 15 and 78, append: "This holds for the simple toy change; the light-like pieces built tonight (matter in A26, the shape field in A25) still use fixed patterns."

**C40. MAJOR. Axiom fit not checked: is a moved record's content admissible at its new site?**
- **Claims.**
  - A27:25: "Then Option R holds together".
  - A27:121–122 defines the content weight "W = β + (α−β)|r⟩⟨r|_y" and the blind weight "W = 1".
  - A27:12 (R-c): "menus are set by records".
- **What is wrong.**
  - Record says a record "locks exactly one admissible local possibility" (BRIEF:15). Admissible means on that site's menu, the support given its nearest-neighbour conditions (BRIEF:14; Q7, BRIEF:28).
  - The swap step places content r at y with odds that ignore whether r is on y's menu: always for W = 1, and whenever β > 0 for the content weight. Nothing handles a record arriving next to another record whose content sets a different frame.
  - Further fit gaps:
    - The claim rule is "strictly range 2" (A27:181), and so is the activity weight (A27:123). Admissibility speaks of "one fixed nearest-neighbor admissibility rule".
    - The blind weight ignores the neighbours. A21's C23 complaint ("against Admissibility's 'varies with'", A21/REVIEW_FINAL:98) therefore survives for it. So LOG:1063, "This fixes all of A21 C23's complaints", is too strong.
    - A swap is not re-forming. So decision 7's "may re-form next door" does not cover it.
    - R-c's "menus are set by records" is the *proposed* menu text (draft:235), not Q7 as decided.
- **Corrected wording (ARGUED).** "Option R is consistent with Record and Admissibility only if a moved record's content is on its new site's menu. The swap step as built does not enforce this. Rules of range 2 and one neighbour-blind weight remain."
- **Draft.**
  - Add after line 61: "- Not yet checked: a record that trades places keeps its content, but its new spot's own conditions might not allow that content (for example, a recorded neighbour there may set a different menu). With fixed odds the step ignores this entirely. The claim rule and one of the step weights also look two sites away, one step beyond the nearest neighbours. Point 0 also takes menus from records, which is the proposed menu text below, not your Q7 as decided."
  - Line 55, "or with fixed odds", becomes: "or with fixed odds (which ignore the neighbours, against Admissibility's 'varies with')".

**C39. MINOR. "The dose per tick becomes readable" cites evidence from the rejected reading.**
- **Claim.** A27:215: "the dose per tick Jτ is readable: record statistics at a fixed amount of change depend on τ (Step 2 table)".
- **What is wrong.** The Step 2 table (A27:103–110) is the *clip* completion of the "carried" reading, which A27 rejects.
- **Corrected wording (ARGUED).** "For the compression reading it is ARGUED: there are O(Jτ) and O(γτ) corrections, for example the Zeno distance ∝ τ (A27:64). With c = γτ at Planck ticks these corrections are tiny, so the tick itself becomes nearly unreadable."
- **Draft line 70.** Append "(argued)".

**C41. MINOR. "No time-doubled twin" needs its bound in the bottom line.**
- Draft:16 lacks the bound; draft:66 has it.
- Fixed by C27's line-16 text.

**C52. MINOR (clarity). The speed-limit cost reads backwards.**
- **Claims.**
  - Draft:18: "no exact speed limit, only an exponentially faint leak, and only if the change per tick is small".
  - Draft:69: "A faint, exponentially small leak remains, and only if the change per tick is small."
- **What is wrong.** Both say the leak exists only when the change per tick is small.
- **Replacement for both.** "No exact speed limit for unrecorded influence: a leak beyond one site per tick always remains, and it stays exponentially faint only if the change per tick is small."

**C53. MINOR. "Holds literally".**
- **Claim.** Draft:15: "your 'evolves continuously' holds literally".
- **What is wrong.** At ticks, cuts and swaps move possibilities in one go; a swap moves a neighbour's possibilities one site at once (A27:117).
- **Replacement.** "…holds literally between record events (at ticks, records still cut and trade places)."

### A23 / field route

**C33. MAJOR. "Pins … to Einstein's linear gravity" hides the named conditional, the scope and the free normalization.**
- **Claims.**
  - Draft:24: "The grid's own symmetry pins its 'shape' version to Einstein's linear gravity."
  - Draft:172: "fix every number exactly as in Einstein's linear gravity".
  - Draft:173: "two wave polarisations at light speed".
- **What is right.** I re-derived both A23 steps by hand.
  - D10 (CHECKED by A23; ARGUED step by me): any O(k²) form gauge-invariant in both slots factors as ⟨h, S·G_lin(k)h⟩, with S constant on the linearized-curvature image. Cubic invariance gives S = aP_A1 + bP_E + cP_T2. Left-slot invariance needs S to keep every k-transverse tensor transverse. k = ẑ forces a = b, and k = (1,1,0)/√2 forces a = c. So the anisotropic O(k²) potentials are removed *exactly, at O(k²)*.
  - D11 (EXACT): on the momentum-constraint surface, k = ẑ gives −(2a+b)/3·tr π = 0, and k = (1,1,0)/√2 gives (b−c)π_xx = 0. So the weights are ∝ (−½, 1, 1).
- **What is wrong.**
  - (i) Gauge invariance and constraint preservation are F4 (A23:62), a named conditional. A23's own summary is "the tensor branch reduces to one named conditional, F4" (A23:250).
  - (ii) The result holds at long wavelength (O(k²)) and linear order. Cubic-anisotropic O(k⁴) terms remain free (A25:284).
  - (iii) Only *ratios* are fixed. The field's speed relative to light needs "a common normalization across sectors" (A23:123), and the strength G is not fixed.
  - (iv) The tensor content itself (F1) is supplied.
- **Corrected wording (EXACT/CHECKED).** "Given F1 and F4, cubic symmetry forces linearized GR's form at O(k²), up to overall normalization."
- **Draft.**
  - Line 24, replace with: "**The road left open** is a field carried by the shared possibilities. If its bookkeeping is kept exact (a choice you would make), the grid's turns fix the form of its 'shape' version to Einstein's linear gravity at long wavelengths. Its speed compared with light, and its strength, are not fixed by this."
  - Line 172, replace with: "If the field's bookkeeping is kept exact, the grid's own turns fix its form exactly as in Einstein's linear gravity at long wavelengths (checked, and confirmed by hand twice). Not fixed: the ripples' speed compared with light, and gravity's strength. At grid scale, direction-dependent corrections are free but tiny."
  - Line 173, replace with: "A stepping rule gives two wave polarisations at one common speed, equal to light's only if the two are set together, with no time-doubled twin. With matter tied in (A26), it gives full light bending, and everything whose weight sits at single places falls alike."

**C34. MINOR (factual error in the draft). "Light bends the wrong way."**
- **Claim.** Draft:170: "A one-number (scalar) field fails. Light bends the wrong way unless the grid's rest frame is singled out."
- **What is wrong.** A23 D7 (A23:90) says γ = −1 means "**no light bending**, since light ignores a conformal factor". A lapse-only coupling gives γ = 0, i.e. half bending (A23:93). γ = 1 needs the stratified preferred frame (A23:94).
- **Scope of "fails".** It is ARGUED/COMPARATOR. It assumes matter sees a metric built from φ and the flat background, or one of A18's lapse/frame compositions. It rests on preferred-frame bounds, frame-dragging data and GW polarization data (A23:236).
- **Replacement.** "**A one-number (scalar) field fails** (argued, against measurements). Tied to matter in the usual ways, it bends light either not at all or only half as much as seen. The full amount needs the grid's rest frame singled out, which tests for a preferred frame rule out. It also gives no frame dragging and the wrong kind of waves."

**C54. MAJOR. As built, the field route needs more than one qubit per place, a Qubit-axiom-level choice that is missing from the decisions.**
- **Claims.**
  - A25:186: the construction "lies outside Theorem N's premises, because the payload exceeds one qubit". It realizes C22's escape 3, "more than one qubit per site".
  - A25:296–298: "3, 1, 2 or 3 reals per role" plus an 8-valued role label; "Compiling this into one qubit per site is open".
  - A25:312: "Whether each place may hold more than one site's worth of settings."
  - The draft says this at line 179 but not in decision 13 (draft:266).
- **What is wrong.** This is C22's escape 3 / A20 relaxation 5, a change to the Qubit axiom's one-site domain M₂(C) unless a compilation is found. The owner must be asked it explicitly (rule d).
- **Draft, decision 13.** Append: "As built, the field needs more settings per place than one qubit holds. May a place hold more (a change to the Qubit axiom), or must the field be built from one qubit per place, for example as a collective ripple (open)?"

**C55. MINOR. What A23 supplies is longer than the draft says.**
- **Supplied:**
  - F1–F5 (A23:59–63);
  - D16's condition that the lapse also paces the field's own change (A23:111; A26:63 lists it as "Still supplied");
  - the common normalization across sectors (A23:123);
  - G;
  - spatial roles (A23:160 / A25 F6);
  - payload (A23:177).
- A23 D1's "keeps the strict cone" (A23:67) and D13's "The strict cone survives" (A23:108) are stepped-leapfrog statements. Under Option R only "no nonlinear signalling" survives.
- **Draft.** Covered by C32's text for D16. No further change is needed if C33 and C29 are applied.

### A26 / matter on the field

**C32. MAJOR. The draft drops A26's scope and its supplied list.**
- **Claims.**
  - Draft:26: "Tied to the field in the simplest fixed way, matter bends light by the full amount and falls alike, with no extra choices. The supplied pieces are how link weight is classed and a small in-block shuffle for one ripple type."
  - Draft:190: "Then light and matter both follow the field's own geometry."
- **What is wrong.**
  - A26 grades the metric result "[EXACT in the eikonal, small-dose limit, at first order]" (A26:35).
  - Full bending needs h = 2U: 1.000 / 1.505 / 2.019 for h = 0, U, 2U (A26:45). That comes from A23 D16, conditional on the lapse pacing the field (A26:63, :211).
  - The coupling form needs G1, a *new* named conditional (A26:74). It is fixed "only at leading order" on the lattice (A26:123).
  - A26's own "Still supplied" list (A26:62–67) is longer than the draft's: F1–F4 including D16, the dose or amplitude form, the vacuum-centred cone E_c = 0, the mass/kinetic split, and the sandwich. So "with no extra choices" contradicts the next sentence and A26 itself.
  - "Matter bends light" is a garble: light bends, matter falls.
  - LOG:1155 "F4 therefore selects ST" should read "G1 (the matter half of F4, a new conditional) selects ST at long wavelength". The Laue identity is a continuum statement. A26's own grade "[EXACT core; ARGUED application]" (A26:52, :150) is correct.
  - LOG:1147 should add "small dose".
- **Draft.**
  - Line 26, replace with: "**Matter on that field (A26).** In a ticked toy, matter tied to the field in the simplest fixed way follows the field's geometry at the level of rays and to first order. Light is delayed and bent by the full amount, provided the field's space-stretch is twice its time-slowing; that is A23's static solution, which needs the time-stretch to pace the field's own change, a supplied choice. Everything whose weight sits at single places falls alike. Supplied: the tie itself; the rule that a uniform stretch must go unnoticed (a new condition); how link weight is classed; a three-move shuffle inside 2×2 blocks for the diagonal ripple (checked in 2D only); and the matter step's own fixed pattern of partner pairs and signs. See point 6 for why this matter has not yet been built in point 2's smooth shape."
  - Line 190, replace with: "Then, at the level of rays, to first order in the field and for a small change per tick, light and matter both follow the field's own geometry."
  - Line 193, append "(argued, at long wavelengths)" after "requires that classing anyway".
  - Line 196, replace with: "**My check.** I rebuilt the 2D toy's band structure independently: the slopes of all four bands follow the field's geometry exactly, and massive bands agree to about 0.1%."

**C31. MAJOR (cross-lane). A26's matter is a stepped, patterned circuit, and its cross-shear coupling cannot be carried by Option R's smooth nearest-neighbour change.**
- **Claims.**
  - Draft:22–26 sets A26 under "the road left open" right after recommending point 2's smooth, pattern-free change.
  - A26's step: A10's time-symmetric word on even/odd bonds, the sublattice mass ε_j = (−1)^j, KS signs η_y = (−1)^x, 2×2 cells and a fixed x-then-y block order (A26:83–96, 194–199).
  - Its strict cone comes from the finite-depth circuit (A26:188–189).
- **What is wrong.**
  - (i) These are supplied patterns, the kind A16 C7 and C22 escape 2 price.
  - (ii) D9 is "[EXACT in the Trotter limit]" (A26:156). The small-dose limit *is* a smooth generator. So no smooth, nearest-neighbour, cell-periodic hop term reaches the taste-blind cross shear (residual 1.000, A26:171).
  - (iii) The working sandwich R = exp(iβX_xY_y) is "an in-cell diagonal operator" (A26:95, :166). It is made by a time-ordered depth-3 circuit. A time-independent "sum of nearest-neighbour terms" (Campaign 7 sentence 2, restored "as written" by Option R) cannot contain it.
  - (iv) The 3D sandwich and its covariance under the 24 turns are unchecked (A26:278).
  - (v) The eikonal metric result (D2) plausibly carries over to a smooth Dirac-type generator, and D5/D13 are stepping artifacts that would vanish (ARGUED).
- **Corrected wording (ARGUED; D9 core EXACT).** "A26's γ = 1 and universal-fall results are for a ticked, patterned matter step. In Option R's smooth nearest-neighbour change, its cross-shear coupling is unavailable (D9). It needs an in-cell diagonal term, a 2×2 cell pattern, or another mechanism (open)."
- **Draft.**
  - Line 194, replace with: "**The diagonal ripple.** One of the two ripple types is felt only if each step's sense of direction is turned by a fixed three-move shuffle inside each 2×2 block. None of the simple next-door tweaks tested does it, and one of them makes the two copies of each particle feel opposite ripples. The shuffle is supplied, checked in 2D only, and whether it treats all 24 turns alike in 3D is unchecked. It is built from ticked moves, and it reaches diagonally across the block. A smooth change made only of next-door terms (point 0) cannot produce it, so matter on the field has not yet been built in point 0's shape."

### A24 / energy-gentle locks

**C35. MAJOR. "Only one way: catch first, record later" is overbroad, and EXACT and constructed claims are blended.**
- **Claims.**
  - Draft:180: "A24 found this is possible, but only one way: catch first, record later."
  - Draft:183: "Recording anything still freely spreading jolts it by about half its whole energy range".
  - Draft:184: "So records must form only on caught, settled things, and slowly."
- **What is EXACT.**
  - ΔE = −Σ_{k≠l}Re⟨ψ_k|H|ψ_l⟩ (A24:35, 64–67).
  - "Settled" (no rival overlap through any local term at the site) is **sufficient** for a zero ghost on every term (A24:131–134).
  - A slow lone excitation with nearest-neighbour hopping is never settled (A24:137–140).
  - No linear weight can detect settledness (A24:146–148).
  - "Zero is possible … no universal floor" (A24:261).
- **What is constructed.** "Catch first, record later" is **one supplied toy** (A24:194–200). It has a trap, a separate emission chain and "a three-site term" capture (A24:198). It is CHECKED.
  - It is not shown to be the only route. Any process that copies the distinction beyond the site's terms settles it (A24:134). Emptiness-aligned records on empty sites cost nothing (A24:290).
  - It is not yet available in the framework's own change. A13's change conserves excitation number, so the spare energy needs another excitation or a field sector (A24:333).
- **Half the energy range.** That is the cost of a *sharp* one-site record of a slow excitation (A24:89). Coarse records cost at least ħ²/(8mσ²) per axis (A24:108), which is small for wide records. A24's own summary at A24:343 also overstates this.
- **"Must only".** The heating bounds make unsettled records rate-bounded, not forbidden: ≤ 4e-48 per nucleon per s for sharp records, ≤ 5e-17 per s at 1 Å (A24:274–275). These are ARGUED with COMPARATOR data.
- **Corrected wording.** "Settled ⇒ zero ghost (EXACT, sufficient). Freely spreading ⇒ never settled (EXACT). Catch-and-emit is a working construction in a supplied toy (CHECKED). Under the field route, almost all records must be settled; the rest are rate-bounded (ARGUED)."
- **Draft, lines 180–184.** Replace with:
  - "Forming a record must leave energy unchanged on average, or a phantom weight remains where the record formed (A23). A24 found exactly when that holds: when the rival possibilities no longer overlap through any of the spot's links, because the change has already carried the difference away ('settled'). Something still freely spreading is never settled. A24 built one working example in a supplied toy, 'catch first, record later':
    - A small thing is caught at one spot, and its spare energy flies off.
    - The record then forms at the catching spot. Once the spare energy has left it costs almost nothing; forming sooner costs more.
    - Recording a freely spreading thing at one exact spot jolts it by about half its whole energy range, which is enormous on the finest grid. Recording it loosely costs less, but never nothing.
    - So, under the gravity field, almost all records would have to form on caught, settled things, and slowly. Earth's heat flow allows other records only extremely rarely. This matches how real detectors work (absorb, then amplify; a comparison, not adopted).
    - The toy needs a trap and a separate channel for the spare energy. Whether the framework's own change can catch and release like that is open."
  - Keep line 185.

**C36. MINOR. A24 numbers.**
- **Verified by my own arithmetic:**
  - ħ/t_P = 1.96e9 J, so the sharp cost is (π/2)ħ/t_P = 3.07e9 J;
  - 47 TW / M⊕ = 7.9e-12 W/kg, i.e. 1.31e-38 W per nucleon;
  - the rate bound is 4.3e-48 /s, i.e. 2.3e-91 per Planck tick;
  - at 1 Å, ħ²/(8mσ²) × 3 = 2.5e-22 J = 1.6 meV for a nucleon, giving 5.2e-17 /s, about one per 6.1e8 yr;
  - for an electron it is 4.6e-19 J = 2.9 eV, giving 5.7e-20 /s;
  - GRW gives 3.0e-17 W/kg;
  - the ghost mass is 7.4e13 kg = 1.2e-11 M⊕;
  - ħ/(1 ns) = 6.6e-7 eV.
- **Inconsistency.** A24:48 (and LOG:1117) give ticked-toy κ "≈ 0.4–0.5". The data at A24:236 are 0.37–0.39 (m_C = 0.3) and 0.49–0.50 (m_C = 0.05). It should read "≈ 0.37–0.50".
- **Expectation level.** "Must not change energy" (draft:25, :180) holds at the expectation level. The per-outcome energies differ, and the operator-level statement is ARGUED (A24:256). Hence "on average" in C29 and C35.

### A22 / time doublers

**C37. MINOR. The draft overstates A22, and three scopes are missing.**
- **Claims.**
  - Draft:96: "Catch, now resolved".
  - Draft:98: "In that case nothing local can remove it, and slow collisions push half or more of their outcome into the twin."
  - Draft:99: "(which A18's gravity package needs anyway), the twin cannot be produced by a few-particle collision, and many-particle production falls off extremely fast."
- **What is wrong.**
  - **(a) "Nothing local".** A22 shows that non-covariant two-lane phases do suppress it. In 1D, D falls roughly as k² (A22:33–35). For massless content, "Both bond types: ≤ 1.1e-8" (A22:205). The EXACT claim covers spin-½-covariant and record-basis-diagonal interactions (A22:28–29).
  - **(b) "Half or more".** The figures are 41–50% for distinguishable pairs (A22:31), and as low as 5.3% at m = 0.15, k = 0.05 (A22:198); 92–99.9% for identical covariant pairs. A22's own plain summary (A22:273) also says "half or more".
  - **(c) "The iff".** It is EXACT for the 1D two-layer number-conserving swap round (A22:78–79). For A10's 3D cycle only the sufficient condition θ < π/12 is shown (A22:138).
  - **(d) "Few-particle".** The arc lemma counts excitations "relative to emptiness" (A22:135). It says nothing about excitations over a dense half-filled vacuum; there only the many-body bound applies.
  - **(e) "Falls off extremely fast".** The e^{−c/θ0} form is a COMPARATOR theorem. c ≈ 10–16 comes from a 1D half-filled ring, L = 14–18, θ ∈ [0.6, 0.75] (four points with up to a factor-4 finite-size spread; A22:222–228). The 1e724 figure is a ~100× extrapolation in 1/θ (ARGUED; A22:144).
  - **(f) "Which A18 needs anyway".** That holds only for the angle-form coupling. A26's amplitude form meets Cassini at any dose (A26:129, :261).
  - **(g) "Resolved".** A22's verdict is "a suppressible nuisance" (A22:47), avoidable at a price.
- **Draft, lines 96–100.** Replace with:
  - "**Catch, avoidable: the 'time-doubled' twin (A22).**
    - In the ticked toys, a twin that flickers at the tick rate exists exactly when each tick fully swaps a set of partners, which is also what lets light run at the grid's top speed.
    - In that case no interaction that respects the turning of possibilities can remove it. Slow collisions push up to about half (different particles) or nearly all (identical particles) of what they scatter into the twin.
    - With small changes per tick, starting from empty space, no collision of fewer than about 90–200 particles can make a twin (exact). Many-particle production falls off extremely fast (argued from a standard result and a small toy).
    - The price: light runs well below the grid's top speed. A18's package needs small changes anyway in one way of writing its coupling, but not in the other (point 6). Point 0's smooth change has no such twin at all below a simple bound."

### A25 / stepping the shape field

**C49. MINOR. Two wording narrowings in the draft's A25 block.**
- **Claim.** Draft:176: "treating every turn of the grid alike … Its ripples then come out exactly right: two kinds, at light speed, with nothing extra."
- **What is wrong.**
  - Covariance holds with the role pattern carried along (A25:48). A given world's layout is kept by all 48 transformations only about vertex- and cube-role sites, by 16 about face- and edge-role sites, and by even translations (A25:158–160).
  - The speed is 1 in grid units. Equality with light needs a common normalization (A23:123).
  - "Exactly right" holds at linear order, with O((ka)²) lattice artifacts (A25:284).
- **Replacement for line 176.** "The field can be stepped with next-door moves only. Its rule treats every turn of the grid alike once the jobs are relabelled along with the turn, and it keeps its bookkeeping exact at every step. At linear order its ripples come out right: two kinds, all at one speed, with nothing extra."

### Cross-lane consistency

**C38. MAJOR. The recommended shape (point 0) drops the strict cone, but the draft still presents strict-cone and stepped-tick results as general.**
- **Contradictions.**
  - (i) Draft:35 lists "No faraway influence faster than one site per tick" as a premise "most results lean on". Point 0 gives it up for unrecorded influence (A27:39).
  - (ii) Draft:117–119 present "an exact limit" and the one-dimensional Einstein clock slowing. A27 lists among Option R's losses "The strict cone" and "A5's exact 1D Lorentz identities for stepped content" (A27:308–309).
  - (iii) Bottom line 3 (draft:21) and point 5 (draft:123–126) state the tick results from stepped toys without qualification. A27:215–216 says that in Option R "A5 T3.1 schedule independence is no longer exact. Tick phases are readable in principle through the change".
    - The out-of-step "mirror wall" (draft:124) arises because a pair acts only at ticks. Under continuous change the pair acts regardless of ticks.
- **Draft.**
  - Line 35, replace with: "- No faraway influence faster than one site per tick. (Point 0's shape gives this up for unrecorded influence, so the results that lean on it, in points 1 and 4 and the tick results in point 5, would need redoing there.)"
  - Line 21, replace with: "**The tick.** In the ticked toys, one shared tick works, and neighbourhood ticks work if they keep in step. Time running differently in different places must come from how much changes per tick, varying smoothly, not from how often ticks come. Under point 2's shape the change no longer comes in ticks and the change per tick becomes readable, so these tick results need redoing."
  - Line 117, retitle: "### 4. An exact speed limit, and relativity at low speed, for ticked change (A5)". Append to line 118: "Point 0's smooth change gives up this exact limit for unrecorded influence, and these exact one-dimensional identities with it."
  - Line 124, append "(ticked change only)".

**C44. MINOR. Point 2's heading conflicts with point 0's step.**
- **Claim.** Draft:87: "A record whose place can be read every tick must re-form at each step".
- **What is wrong.** Option R's swap step does not re-form. Its site stays pure, "so A7's obstruction does not arise" (A27:128).
- **Replacement.**
  - Heading: "### 2. A record whose place can be read every tick must not ride the shared possibilities (A7, A19, A27)".
  - Line 88, append: "Point 0's step is the other way: the record keeps its own content and trades places, never riding the possibilities."

**C45. MINOR. "28%" is the unit-dose value.**
- **Claim.** Draft:83: "leaks past that, by about 28% in the toy".
- **What is wrong.** A3:229 gives 0.285 at τ = 1, falling as ≈ τ⁴/2 (0.027 at τ = 0.5; 5.0e-5 at τ = 0.1). Point 0 relies on exactly that small-dose regime.
- **Replacement.** "…leaks past that: about 28% with a full unit of change per tick, falling steeply (about the fourth power) as the change per tick shrinks."

**C46. MINOR. Point 1 and point 0 contradict each other on Campaign 7's sentence.**
- **Claims.** Draft:84: "So what is ruled out is Campaign 7's change sentence as written." Draft:15 and :78: "comes back as written".
- **Replacement for line 84.** "So, if records follow the possibilities, what is ruled out is Campaign 7's change sentence as written. Point 0 drops that 'if', and the sentence comes back."

**C47. MINOR. The bottom line drops C12's qualifiers.**
- **Claim.** Draft:23: "cannot make waves or hold a moving Moon".
- **Replacement.** "**Record-carried gravity** gets the static picture partly right, but with wandering records it cannot make waves or hold a moving Moon (argued)."

**C48. MINOR. Handedness scope.**
- **Claim.** Draft:28: "Ticks by themselves do not give a preferred handedness. This is exact for single free particles."
- **What is wrong.** Quasi-local W3 ≠ 0 walks exist (A1 D14, A2 E3). Exactness covers strictly limited reach (C3) and any smooth change (A2 D4; A27:210).
- **Replacement.** "**Handedness.** Neither ticks nor smooth change give single free particles on a uniform grid a preferred handedness (exact for steps of strictly limited reach and for any smooth change). Interactions and record edges are untested."

### Draft-only provenance and owner-rule items

**C42. MINOR. Reviewer provenance.**
- **Claim.** Draft:5: "(A20, checked by both reviewers)".
- **What is wrong.**
  - A16 landed at 23:45 and A20 at 00:40 (LOG:637, :813). A16/REVIEW.md contains no mention of A20 or Theorem N.
  - Only A21 checked Theorem N step by step (A21/REVIEW_FINAL:59–79).
  - Draft:32 also needs updating for this third review. I read both earlier reviews.
- **Replacements.**
  - Line 5: "(A20, checked step by step by the second reviewer)".
  - Line 32: "Three hostile reviews by separate agents attacked the main claims (each later one had read the earlier ones), and their corrections are included."
  - Line 1: "(v8, after three hostile reviews)".

**C43. MINOR (owner rule: decisions framed as yours). An approved reading is listed as unadopted.**
- **Claim.** Draft:34 lists "possibilities changing at once to agree when a record forms" as not adopted.
- **What is wrong.** Q1's approved wording says exactly that (BRIEF:24). What is unadopted is the *form*: a Lüders cut on a joint tensor-product possibility, plus odds from the site's own part (Campaign 7 sentences 1 and 3).
- **Replacement for line 34.** "- Campaign 7's bookkeeping for shared possibilities: possibilities joined across sites in one combined description, odds from the site's own part, and the exact way they change to agree when a record forms. (That they change at once to agree is your Q1.)"

**C51. MINOR (owner rule: Q-decisions). A28's Q4 consequence is missing.**
- **Claim.** A28:45: "Q4 must be read as conditional on formation, and under gating it never applies to an actual formation."
- **What is wrong.** Neither section 7 nor decision 4 says this.
- **Draft.** Append to decision 4 (line 257): "Under that rule your Q4 (an uninfluenced site has equal odds) never applies to an actual formation, because a site with no recorded neighbour never forms a record (A28)."

**C50. MINOR. The decision list is out of step with point 0.**
- **Decision 0 (line 250).** After the C28 fix, append: "It brings its own choices: how much the change does per tick, how often records step and with which weighting, the claim rule (which looks two sites away), and an order for overlapping formation spots."
- **Decision 2 (lines 252–255).** Append to the last bullet: "(point 0's shape takes this one: the change reaches everywhere, faintly)".
- **Decision 7 (line 260).** "Never destroyed, may re-form next door" becomes "never destroyed, may move next door (by re-forming, or by trading places as in point 0)".
- **Decision 8 (line 261).** Add: "Or by trading places with an empty neighbour and keeping its content (point 0, A27)? That one is not tied to the grid; the open item is whether its content suits its new spot."
- **Decision 14 (line 267).** "This is needed for energy bookkeeping under the gravity field" becomes "Under the gravity field this is needed for almost all records (others only extremely rarely)".

**Owner-rule scan (no change needed).**
- No sentence says a possibility is "read" or that a "question is asked". Line 234's "as if they could be read" is a negation and is fine.
- Q7 is kept as decided (lines 226–235), and the menu text is marked "not approved".
- No axiom or import is presented as adopted.
- Points 0 and 2 describe ticks only as part of an option, with decision 0 framed as the owner's.
  - For safety, change line 13's "Records form and step only on ticks." to "In this option, records form and step only on ticks."
  - Change line 54's "They are classical facts, and they step on ticks by their own rule." to "In this option, they are classical facts that step on ticks by their own rule."

---

## 3. Draft sentences that are fine as they are (do not touch)

- **Bottom line:** lines 6–10 (the four conditions of the limit); line 14; line 19; line 20; line 27 (the A28 summary matches A28:25–46).
- **Point 0:**
  - line 51;
  - line 57 ("It never moves more than one site per tick.");
  - lines 58–60;
  - line 61 (claim rule against literal I3; CHECKED in one toy, which the sentence does not overstate);
  - line 64;
  - line 66;
  - line 71;
  - line 74;
  - line 77;
  - line 79 (now correct after A25).
- **Point 1:** lines 82 and 85.
- **Point 2:** lines 88–95.
- **Point 3:** lines 103–115 (A21's corrected text).
- **Point 4:** line 120.
- **Point 5:** lines 125, 127–131.
- **Point 6:**
  - lines 136–169 (record-carried gravity and the A18 package, as corrected by C9–C18, C25);
  - line 171;
  - line 175;
  - lines 177–179 (A25's role-pattern cost, the 8-copies statement including "whether change comes in ticks or smoothly", which my check confirms, the patch statement, which my check confirms holds in continuous time with growth falling only as r^{1/4}, and the payload line);
  - line 185;
  - line 187;
  - line 189;
  - lines 191–192, with C32's prefix added on line 190 above them;
  - line 195;
  - line 197.
- **Point 7:** lines 200–219 (including the A28 block, checked against A28:25–46).
- **Point 8:** lines 222–224.
- **Menu decision:** lines 226–235.
- **Assembled model:** lines 237–246.
- **Decisions:** 1, 3, 5, 6, 9, 10, 11, 12.

---

## 4. New open questions for the owner

1. **Can a record that moves land where its content is not on offer?** Under point 0's swap step, a record carries its content to a new spot whose own conditions (for example, a different recorded neighbour) might give that content zero odds. Should a step be allowed only where the content is on the new spot's menu (C40)?
2. **Who sets the calm vacuum's direction under point 0?** The empty background stays calm only if every record's content lies along its direction. That direction cannot be taken from unrecorded possibilities without leaking. Is it fixed by the law, which privileges a possibility, or passed on from a first record (C30)?
3. **Light under point 0.** No smooth, everywhere-alike, next-door-terms change on one qubit per site has yet produced light-like ripples over a calm background. A26's matter and A25's field both use fixed patterns. Is a fixed pattern acceptable for light and matter, given that point 0 was chosen to avoid one for records (C30, C31)?
4. **More than one qubit per place.** The shape field as built needs several numbers plus a role label per place. Is that a Qubit-axiom change you would consider, or must the field come from collective ripples of one qubit per place (C54)?
5. **One pattern or three?** A10's matter sub-grids, A26's 2×2 cells and KS signs, and A25's 8 role layouts all use the same 2×2×2 block. If any pattern is supplied, should it be one shared choice (A25 open 2)?
6. **What a tick means at Planck scale under point 0.** With record chances per tick scaled as c = γτ to avoid freezing, the ticks become almost unreadable at Planck spacing (ARGUED, C39). Is "records form on ticks" then a physical statement or a bookkeeping one?

---

## 5. LOG wording fixes

| LOG line | Old | New |
|---|---|---|
| 1062 | "Q3 is satisfied" | Add: "for the step; the toy change (Heisenberg) does not use the gluing; light-like matter needs it" |
| 1063 | "This fixes all of A21 C23's complaints" | "all except, for the blind weight, odds that ignore the neighbours" |
| 1074 | "**Theorem N does not apply.**" | "Theorem N's strict per-tick reach is dropped: A20 relaxation 3 (quasi-locality) for possibilities; relaxation 6 for records" |
| 1092 | "with no staggered roles needed" | "FAILS: spatial roles (A25 F6) are still needed in continuous time (Theorem A; A29 check); only the temporal leapfrog layers go" |
| 1117 | "κ ≈ 0.4–0.5" | "κ ≈ 0.37–0.50" |
| 1147 | "(EXACT, eikonal, first order, given F2)" | Add "small dose" |
| 1155 | "F4 therefore selects ST" | "G1 (a new conditional, the matter half of F4) selects ST at long wavelength; EXACT core, ARGUED application" |

**Scripts:** `c8/A29/thmA_continuous.py`, `c8/A29/wilson_continuous.py` and `c8/A29/wilson_small_r.py`, with `out_*.txt` and `time_*.txt` beside them.
