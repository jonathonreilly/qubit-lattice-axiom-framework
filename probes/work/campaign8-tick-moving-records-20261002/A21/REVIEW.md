# A21 second hostile review: late lanes and MORNING_DRAFT v4+

**Scope.** I read BRIEF, A16/REVIEW.md, the LOG (correction entries C1–C10 onward), the A12, A14, A15, A17, A18 and A19 reports and MORNING_DRAFT. **A20 has no REPORT.md yet (checked 00:35), so it is not reviewed.**

**What I ran.** Two tiny checks, each nice 10, single-threaded, under 2 s and 80 MB, in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A21/`:
- `r1_capacity_and_scales.py`:
  - exact Z³ Green function (G(0) = 0.252731, G(e1) = G(0) − 1/6 exactly), giving Cap(site) = 3.9568 and Cap(star) = 11.6192;
  - freezing times at weak formation strength;
  - D23 wake geometry and a persistence loophole.
- `r2_fixed_coupling_ns.py`: A15's 4-qubit no-signalling toy, plus a fixed controlled-angle coupling.
  - A15's nonlinear "angle set by possibilities" dial: TV 6.9e-2.
  - Fixed coupling in which a1's possibility sets the (a2, a3) angle coherently: TV 2.7e-16.

I also redid by hand: 2κ = 1.7627 and 2.2244; the Chebyshev index and √T factor; γ = b/a − 1; β = (1 + FF''/F'²)/2; β = 1 − 1/(2m); the D23 solution (substitute φ = e^{−vz/2D}ψ, which gives a screened Poisson equation for ψ); Theorem B's 2p bound; and the AND metric.

---

## 1. A12

**(a) Lattice Reeh–Schlieder: STANDS (EXACT), scoped.**
- L1 is a one-line positivity bound, and A9 n4's full rank holds.
  - |k|·f analytic forces f ≡ 0, because x²+y²+z² is prime in the ring of analytic germs.
  - Massive seas are also full rank.
- The name is apt: the sea is separating for local algebras.
- Exemptions to state:
  - record-gated weights (F = 0 in voids);
  - infinite-reach weights (A9's untruncated P₊e₀ is quasi-local with rate exactly 0);
  - rank-deficient vacua (A13's aligned emptiness).
- The "finite window" case needs a strict-cone change (L4). It does not cover e^{−iH}.
- Hidden assumption: treating formation weights as fermion bilinears takes the repo's graded (fermionic) cross-site product for granted. The four axioms do not fix that product (the composition gap).
- Narrowed wording: *"In the half-filled sea, every nonzero formation weight that ignores records and acts on a finite region (finite reach, or a finite window under a strict-cone change) has a positive vacuum rate."*

**(b) Chebyshev/Bernstein–Walsh ceiling e^{−2κT}: STANDS-NARROWED.**
- The maths is right:
  - T_{T−1}(cos(ν′/2)/sin(α/2)) times e^{i(T−1)ν′/2} is a genuine T-tap polynomial;
  - the peak width ∝ T^{−1/2} gives the √T factor;
  - Bernstein–Walsh plus an O(T) Nikolskii factor on an arc gives the e^{−2κ(T−1)}/(CT²) lower bound.
- "The fastest decay **any** T-tick window can have" is overbroad. It holds for a fixed, finitely supported seed whose spectral weight on the occupied arc is bounded below.
  - Spreading the seed over r sites adds spatial filtering (A12's own L3′: e^{−4.6R}).
  - In massless 1D, space and time filters are interchangeable (θ = ±k), so the ceiling is per unit of T + r, not per tick of every instrument.

**(c) Multi-tick windows need a per-site memory, an import: STANDS-NARROWED.**
- Correct given Q2's snapshot rule. Without memory a T-tick window is a reach-T weight. That breaks nearest-neighbour admissibility, and its record is influenced from outside its past cone (CHECKED, ΔP ≤ 1.07e-3).
- But "memory at each site" assumes formation may happen everywhere. A memory made of matter (bound patterns of possibilities, or record structures) is not excluded; it exists only where matter is.
- The same import class recurs in two other lanes:
  - A15 S0: the per-site beat register;
  - A17: the accumulator and rotor pointer.
- The owner should get these as **one** decision.

**(d) "Distant coherent light favours formation gated by recorded neighbours": STANDS-NARROWED (ARGUED).**
- VLBI and the CMB constrain the **response to light-like excitations** in empty space (≲1e-60 per photon per tick). That is a different quantity from the vacuum false-record rate.
- Two rules satisfy the light constraint:
  - **record gating**, which also makes the void exactly quiet;
  - **a light-blind (mass-selective) rule** (comparator: GRW/CSL), which fixes light but not the sea's vacuum rate.
- Record gating's costs, unstated in the draft:
  - an empty grid never starts;
  - records near matter must still not record light passing through transparent matter;
  - record-set menus are safe only from records cut to agree with their site (A16 C2/C4).
- (b) Semantics: A12's plain summary says a one-tick rule "can never fully tell emptiness from a faint ripple". Do not reuse that phrase; it edges toward a possibility being read.

## 2. A14

**Records as walls fail: STANDS-NARROWED** to A6/A8's capturing clump in the dilute mean field.
- The pinning lemma is EXACT; I re-derived it, including ⟨a|SWAP|a⟩ = |a⟩⟨a|.
- "Wrong sign" is exact for the velocity part (wanderers are depleted as u = u∞N).
- The mass (plasma) part bends rays *toward* the clump, with early arrival. So the sign is wrong for the delay and mixed for the bending.
- 3D Dirac walls were not run (`w3d_single_NOT_RUN.py`).
- The most consequential output is the cross-constraint u∞ ≲ 1e-47 to 1e-92 if wanderers pin light. In A14's toys pinning appears whenever the change moves possibilities. **The draft omits it** (see claim 5).

**AND gating gives n = 1/N² and γ = 1: STANDS-NARROWED.**
- The averaged-generator algebra is right: ω² = N²μ² + N⁴c²q² gives −N²dt² + N⁻²dx².
- Hidden costs:
  1. **Jitter.** The success holds only in the dose → 0 averaged limit. With real discrete events, AND gating is per-site event pacing and inherits A14's own caveat (d2) and A17's floor. The quiet version is A18's deterministic product angle, which needs a smooth field.
  2. **Light needs activity.** Light speed ∝ 25·a∞²·θ in grid units. A void with no wanderers stops light. With Cassini's a∞ ≲ 1e-5, light runs at ≲1e-9·θ of the grid limit.
  3. "Global" should read "shared". In-step local ticks suffice (A5, A15).
  4. One-site rest energies are required; A10's masses are two-site.
- Narrowed wording: *"If two-site steps need record activity at both ends within one shared tick, then in the averaged small-dose limit light bends and is delayed by the full first-order amount; with real events this inherits the jitter floor, and light cannot cross regions without activity."*

**β stays 1/2: STANDS (EXACT, dilute mean field).** N is harmonic, so g00 = −(1−U)², giving β = ½, a 7/6 perihelion factor and 50.1″.

(b) Semantics: N is an event rate. That matches the owner's "time = accumulation of records" only because A6/A8 clocks count capture events. Say so.

## 3. A15

**Theorem A (mismatched bonds never act; mirror walls): STANDS (EXACT).**
- Scope: rigid per-site clocks at one rate, the handshake rule, and words in which each bond appears once per period.
- A18 uses A10's time-symmetric (palindromic) word, which is exactly the exception A15 left uncomputed.

**Theorem B (lag lock): STANDS (EXACT).**
- I re-derived it: n_xy is within 1 of both c(x)/p and c(y)/p, so |c(x) − c(y)| ≤ 2p.
- Semantics: "rate" is relative to an unreadable scheduler. The readable content is that neighbouring event counts cannot drift apart.

**Theorem C (waiting loops freeze everything): STANDS (EXACT).** A directed naming cycle of length ≥ 3 freezes the whole connected component. Each site's future is bounded by p·(distance) + p.

**The angle lapse transmits: STANDS-NARROWED.**
- CHECKED in 1D only.
- It transmits only packets whose quasi-energy fits inside both sides' bands. Halving θ near the crossing gives total reflection near the band top.
- **A17 D1 supersedes A16 C8's "angle lapse avoids random pacing".** A deterministic per-site record-set angle keeps the drive-term jitter. Only a smooth, wide average escapes it.

**"Neighbourhood time fits in change per beat, not beat rate": STANDS-NARROWED.**
- EXACT within fixed-word pair schedules (S13); ARGUED beyond. The comparator (sustained redshift with no reflection) supports it.
- Missing bridge to the owner's reading: under "time = record accumulation", formation odds per tick must carry the same factor N (A15 S14, A18). The draft never says this.

## 4. A17

**Capacity floor S_N(0) ≥ 2(1−u)/(uκ·Cap(K)): STANDS (EXACT for linear drives** in an equilibrium SSEP or independent-walker gas).
- Cauchy–Schwarz in the G_KK inner product is verified.
- Numbers re-checked: 6.07 ticks (site) and 2.066 ticks (star) at u = ½.
- Near a clump the gas is not at equilibrium. Nonlinear drives are ARGUED.

**Time windows don't help: STANDS (EXACT)** for long-time dephasing, since the zero-frequency gain is 1.
- It does not address the grid-scale part that drives scrambling. Time smoothing would help there, but it needs a per-site memory: the same import as A12's windows.

**Per-site beats scramble matter: STANDS-NARROWED.**
- EXACT at second order in the 1D toy (0.05975 vs 0.05989).
- "An electron every ~3 s" is ARGUED. It assumes:
  - Planck ticks;
  - u = ½ (the most favourable case);
  - noise white up to the tick rate;
  - P2: every process, including the rest-mass phase, takes the same dose.

**"The smooth beat must be a field of the possibilities": STANDS-NARROWED to A17's own words, "not excluded here; not constructed".**
- Conditional on P1–P4, nearest-neighbour admissibility, the Q2 snapshot rule, no extra memory, and diffusing-record carriers. L3's class membership is ARGUED; a near-packed relay gas (u′ → 1) evades the floor but jams.
- **It must enter through fixed (linear) dynamics.** My r2 check shows a fixed coupling in which a possibility sets the pace does not signal (2.7e-16), while A15's dial does (6.9e-2).
- "Set by records" alone would mean unrecorded matter does not source the field. That should be stated as an open choice.

## 5. A18

**P1–P4 give exactly the exponential metric, γ = β = 1: STANDS-NARROWED.**
- It holds at ray level in the small-dose limit, plus six supplied items: θ0 ≲ 6e-3, cone at the vacuum quasi-energy, time-symmetric word, unpaced wanderers, formation odds ∝ N, and a smooth lapse.
- **Semantic catch:** "light" here is a two-site Dirac ripple. Light from four-site loop terms (gauge-type, as the photon lane's likely is) gets n = N⁻³ under the site-count rule (D7): γ = 2, so it bends 1.5× too much. The light-bending match does not transfer without a dimension-based weight rule.

**Dialled-in choices: STANDS (EXACT).** What is dialled is a "degree-2" composition (any symmetric degree-2 combination works) and an exponential F.

**Nearest-neighbour β = 1 − 1/(2m): STANDS (EXACT)** for an exponential per-record response on m = 6 non-self neighbours. With the site itself included (m = 7), the bond product no longer factorizes exactly.
- The draft's "a nearest-neighbour rule … gives Mercury 44.2″" is overbroad. A tuned degree-m rule hits β = 1 at today's density (D12), and m → ∞ with r → 1 recovers β → 1.
- The decisive nearest-neighbour failure is jitter (D13, A17), not β.

**D23, moving sources make only wakes: STANDS (EXACT mean-field solution).** Its application is right **in scope**.
- With Planck-scale hops, D/v = 1.35e-32 m at 30 km/s.
- The wake at the Moon's distance is about 5e-12 m wide, and the upstream screening exponent is about 3e40. "A moving Earth holds no Moon" is correct for diffusing carriers.
- It is robust to carrier persistence. Within its persistence length a carrier is ballistic, and a ballistic shadow falls as 1/r², which the inverse-square law tests rule out above about 50 μm.
  - Persistence ≲ 50 μm gives D/v ≈ 0.17 m.
  - Holding the Moon at 30 km/s would need about 100 km of persistence.
- "Moving" means relative to the wanderer gas. Records carry no momentum, so matter cannot drag the gas along.
- Not covered:
  - ballistic record carriers, which make no wake but fail on the 1/r² shadow;
  - fields carried by possibilities.

**Omitted by the draft:**
- unpaced carriers form an absolute clock (D14, D24);
- light runs at under 1% of the grid limit (D4);
- with A14's u∞ ≲ 1e-47, D13 needs averaging over R ≳ 1e56 sites (~50 kpc), so the Sun's field cannot be resolved.

## 6. A19

**Sharp registration gives no inertia: STANDS (EXACT in the toy).**
- In 1D the direction bit survives with probability about 1 − sin(m)/2 per record; in 3D it is erased. "Forgets its direction every time" is wrong for 1D.
- R1 needs a star-local F that annihilates a **quiet** emptiness. In the sea vacuum its premise fails.
- **A13's own c·P_singlet is of this kind, so A13's model as written gives massive movers no inertia. The draft's A13 section omits this.**

**Coarse registration gives the first law: STANDS-NARROWED.**
- The mean is EXACT for sliding, symmetric cuts; the track speed is CHECKED in 1D; 3D is only a small box. Fixed partitions freeze.
- The readable law is spatial (straight, evenly spaced records); speed needs a clock.

**Mediated records give coarse cuts: STANDS-NARROWED.** The structure is EXACT and fully consistent with Q1: the probe's record is sharp, and the shared possibilities "change at once to agree". It needs a medium. That there are no tracks in empty space is consistent.

**Time-umklapp falsifier: STANDS-NARROWED as a *potential* falsifier.**
- About 0.5 of the reflected weight goes to the doubled channel for single-site contact phases.
- The reflected weight falls about as m². At physical masses per Planck tick that is minuscule per collision. Visibility is open.
- R2's go-between demonstration used the same contact bumps.

(b) Semantics: "readable content is their place" conflates content with location. It is acceptable because presence is readable (a site with no record cannot be read), but it should be stated that way.

## 7. The coordinator's synthesis

**Verdict: the conclusion STANDS-NARROWED as an open candidate. The argument as written in the draft FAILS in two places.**

1. **"The pace cannot be set by the shared possibilities, or faraway choices leak (A9, A15)" FAILS as worded.**
   - Counterexample (r2): a fixed coupling in which a1's possibility sets the (a2, a3) angle gives TV 2.7e-16.
   - A15 S11 tested only nonlinear dials (θ·p1, thresholds). As worded, the premise also contradicts the synthesis's own conclusion that gravity rides on the possibilities.
2. **"In every record-based version … thin wake" FAILS** for ballistic record carriers: they make no wake, and fail instead through the 1/r² shadow. The correct scope is diffusing carriers.
3. **Better support for "records can at best match the static picture":**
   - readable records carry no momentum, so a record gas's only conserved density diffuses and it cannot ripple at gravitational-wave frequencies;
   - ballistic carriers give 1/r²;
   - persistence is capped by lab 1/r² tests;
   - add establishment (~50 μm) and jitter.
   - "At best" is apt: even the static match needs a source at rest in the gas frame, after cosmological build-up times.
4. **"Would have to be" is must-language.**
   - Under Q2 the snapshot holds only records and possibilities, so with no imports and momentum-less records the possibilities are the remaining carrier.
   - That is a dichotomy (ARGUED); per-site memory is an import route it does not cover.
   - Phrase it as "the candidate left open".
5. **"The direction the repo's gravity lane already takes" is unverified.**
   - The stale worktree has a W-native **induced-gravity** program, e.g. `docs/UNIVERSAL_GR_GRAVITON_DISPERSION_LORENTZ_ISOTROPY_BOUNDED_THEOREM_NOTE_2026-06-08.md`: TT stiffness induced by the staggered sea's stress response.
   - That lane rests on the half-filled sea that the draft's section 6 puts in doubt.
   - Verify against origin/main and cite it, or drop the sentence.

## 8. MORNING_DRAFT as a whole

**A16 corrections not carried over**
- Fix 3/8's safety clause, "records re-formed at each step are safe for this" / "cut to agree", is dropped. The proposed Q7 text, which the owner is asked to approve, now lacks its condition.
- Fix 13's A9 linear-chance line is dropped.
- Fix 15 (verify the ai/probes path) is still open.
- Line 36 reflects C8's view, which A17 superseded.

**New overclaims**
- Line 36: "set by nearby records" contradicts line 97 and A17.
- Line 37: "A shared global beat … lets light bend by the full amount" is averaged-toy only, and "point 5" is a dangling reference.
- Line 47: "needs" (see A18 D17).
- Lines 52–57: package costs are missing.
- Lines 58–62: see claim 7.
- Lines 66–68: the vacuum section.
  - The "5 per million" figure is per unit formation strength.
  - The conclusion survives as a ratio: a rule that records a particle within a second freezes empty space in about 2 days, or about 80 s for the energy rule.
  - A rule weak enough to keep space clear for the age of the universe would take about 70,000 years to record anything.
  - "At least 5 times per million ticks" is false as a rate (A13 itself needs c ≲ 1e-43).
- Line 97: "has to be" overstates A17's "not excluded".
- Lines 101–105: the A19 bullets overstate in places.
- Line 28: "cannot move a spinning particle over long distances" mistranslates A1 D18, which concerns the long-wavelength (light-like) linear term.

**Readability**
- The draft uses "beat" and "tick" interchangeably, along with round, Planck tick and experienced tick. Use "tick" throughout.
- Jargon: "first-order", "frame dragging", "exponential", "time-doubled partner state".
- Section 5 is overloaded. Split the A18 package and the synthesis into their own point.
- Add a five-line bottom line at the top.

**Language rule.** No violation found. Two improvements:
- line 57: "sees only nearest neighbours" → "uses only nearest neighbours' records";
- add the unifying sentence in fix 16.

---

## Exact wording fixes for MORNING_DRAFT.md

1. Old: "A hostile reviewer attacked every main claim before this draft. Its corrections are included, and overstatements from earlier drafts are fixed."
   New: "Two hostile reviews attacked the main claims: one for the early lanes, one for the late lanes (A12, A14, A15, A17–A19) and the gravity synthesis. Their corrections are included."

2. Old: "- Read every \"must\" below as \"if those hold\"."
   New: "- Read every \"must\" below as \"if those hold\". Most numbers also assume one tick lasts the Planck time (about 5×10⁻⁴⁴ s). Some lanes call the tick a \"beat\"; here it is always \"tick\"."
   Also replace "beat" with "tick" in the section 4 bullets, the A18 bullet, line 62 and line 92.

3. Old: "A strictly local rule that treats all 24 turns alike cannot move a spinning particle over long distances (A1)."
   New: "A strictly local rule that treats all 24 turns alike cannot let a lone spinning particle move like light at long wavelengths (A1)."

4. Old: "### 4. The beat: effectively shared, but how much happens per beat can vary (A5, A15, A14)"
   New: "### 4. The tick: effectively shared, but how much happens per tick can vary (A5, A14, A15, A17)"

5. Old: "- **Out-of-step beats:** they leave a mark. Where neighbouring beats disagree, the pair between them never acts, so the seam acts like a mirror wall."
   New: "- **Out-of-step ticks:** if each site keeps its own fixed tick without waiting for its partner, then wherever neighbours are out of step the pair between them never acts, so the seam is a mirror wall that records can reveal."

6. Old: "- **Where variation can live:** time running differently in different places, as gravity needs, fits in how much change happens per beat, set by nearby records. It does not fit in how often the beat comes."
   New: "- **Where variation can live:** in these toys, time running differently in different places cannot sit in how often each place's tick comes. It can sit in how much change, and how much record-forming, each shared tick brings. That amount must vary smoothly: set by the records right next to each spot, it jitters far too much (see the jitter problem under idea 1)."

7. Old: "- **A shared global beat has a positive role:** it lets light bend by the full amount (A14, point 5)."
   New: "- **A shared tick helps light bend fully, in one toy (A14):** if passing between two neighbours needs activity at both ends within the same tick, light bends by the full amount. That toy averages the activity. With real record events it inherits the jitter problem, and light could not cross a region with no wandering records."

8. Old: "### 5. Gravity-like clock slowing appears, but only under conditions (A6, A8, A14)"
   New: "### 5. Gravity-like clock slowing appears, but only under conditions (A6, A8, A14, A18)"

9. Old: "Full bending needs moves to require activity at both ends on one shared beat (A14). Even then, Mercury is still off."
   New: "Full bending appears when passing between neighbours is slowed twice over, for example by needing activity at both ends within one shared tick (A14). Even then, Mercury is still off."

10. Old: "- **A package that matches Einstein to first order (A18).** Combine:" … through "…it gives Mercury 44.2″ against the measured 42.98″."
    New:
    "- **A toy package that matches Einstein's main corrections for light and planets (A18).** Combine:
      - a shared tick;
      - records, averaged over a very large surrounding region, setting how much changes per tick, with passing between neighbours slowed twice over;
      - one particular exponential shape for the slowing.

      For light made of two-site ripples this gives exactly the right main light bending, radar delay and Mercury orbit, and things whose mass sits at single sites fall alike. Its costs:
      - both key numbers are dialled in, not derived;
      - light built from four-site loop terms would bend 1.5 times too much unless a further rule ties each term's slowing to its size;
      - light runs at under 1% of the grid's one-site-per-tick limit;
      - the wandering records that carry the slowing must not slow down themselves;
      - using only nearest neighbours' records jitters far too much, and the natural version gives Mercury 44.2″ against the measured 42.98″;
      - if wandering records also hold light back, as records do in A14, the averaging region must be about the size of our galaxy, so the Sun's own field could not be resolved."

11. Old: "- **The deeper problem (A18, plus my synthesis, argued).** In every record-based version, …" through "…That is the direction the repo's gravity lane already takes."
    New:
    "- **The deeper problem (A18, plus my synthesis, argued).** When the slowing is carried by diffusing wandering records (A6, A8, A18), a moving body's field survives only in a wake behind it, thinner than an atom at the Moon's distance, so a moving Earth could not hold the Moon. This holds even if the wanderers keep their heading for a while, as long as gravity's inverse-square law holds down to the sub-millimetre scales where it is tested. There are also no gravitational waves and no frame dragging (a spinning body twisting nearby paths). Records struggle here because they carry no momentum (A7, A13): a crowd of them can only spread out, not ripple, and wanderers that fly straight give the wrong fall-off (A17).
      - **The candidate left open:** gravity carried by a collective ripple of the shared possibilities, changing by a fixed rule on a shared tick, the way the photon lane's light works. The fixed rule matters. A pace computed from the current unrecorded possibilities lets faraway choices leak (A9, A15); a fixed rule that lets the ripple's possibilities set the pace does not (second review's check).
      - This is close to the repo's induced-gravity notes, which build gravity from the half-filled sea's response; point 6 puts that sea in doubt. (Check against current main before sending.)"

12. Old: "- **The repo's current vacuum, the half-filled sea:** any single-tick straight-average rule makes records in it at least 5 times per million ticks, and that is the best case. At Planck ticks, everything freezes at once."
    New: "- **The repo's current vacuum, the half-filled sea:** a rule whose odds depend only on nearest neighbours within one tick, as a straight average, forms false records there at least 5 per million times as often as it records a real passing thing (best case; about 1 in 80 for an energy-based rule). At Planck ticks, a rule strong enough to record a particle within a second fills empty space within a few days (about a minute and a half for the energy-based rule). A rule weak enough to keep space clear for the age of the universe would need some 70,000 years to record anything."

13. Old: "…can make this exponentially rare, though never zero. About 5 to 40 swings of the gentlest rhythm to be recorded is enough. They need a small memory at each site, which the axioms do not provide."
    New: "…can make this exponentially rare, though never zero for a rule that ignores records. About 5 to 40 swings of the gentlest rhythm to be recorded is enough, and anything gentler is never recorded. In empty space this needs a small memory at every site, which the axioms do not provide; a memory made of matter is not ruled out, but exists only where matter is."

14. Old: "…arrives without forming records on the way. That suggests records form mainly next to records that already exist."
    New: "…arrives without forming records on the way, so light crossing empty space must essentially never be recorded. Letting records form only next to existing records would explain this and keep empty space exactly quiet at once; a rule that simply ignores light would explain the first but not the second (A12, argued). The cost: an empty grid would stay empty forever."

15. Old: "- **What has to come from records:** which possibilities a record can lock (the menu's directions) must be set by the law and the records around it."
    New: "…set by the law and the records around it. This is safe for records that lock their own site's possibility, as the Record axiom says (records re-formed at each step do). A record whose place is not cut to agree must not set a neighbour's menu, or the leak in point 2 returns."

16. After "My check found complete leakage." append: "In short: a rule that uses unrecorded possibilities as if they could be read lets faraway choices leak; a fixed straight average does not."

17. Old: "\"The menu is set by the conditions. Recorded neighbours may set which possibilities are on offer; …\""
    New: "\"The menu is set by the conditions. Recorded neighbours, whose records lock their own possibilities, may set which possibilities are on offer; …\""

18. Three edits in the jitter section:
    - Old: "an electron within seconds." New: "at Planck ticks, an electron within seconds."
    - Old: "  - The jitter shrinks only with the width of the region averaged over, and averaging over time doesn't help (exact)."
      New: "  - For a tick that counts wandering records, the jitter shrinks only with the width of the region averaged over, and averaging over time doesn't help (exact). The region needed is a billion or more sites across: tiny in metres, but far beyond nearest neighbours."
    - Old: "  - A quiet, local, influenced beat therefore has to be a smooth field … cannot build it without breaking the speed limit."
      New: "  - A rule using only neighbouring records cannot build that average. Using far records at once breaks the speed limit, a running average needs a memory the grid does not have, and passing the average along by records brings the jitter back. The option left open is a smooth field carried by the shared possibilities, changing by a fixed rule and fed by records (A17, argued; not built)."

19. Five edits in the inertia bullets:
    - Old: "it forgets its speed and direction every time. The trail becomes a jittery zigzag, …"
      New: "it forgets its speed every time, and in 3D its direction too. A slow thing becomes a near-light-speed zigzag, …"
    - Old: "are always the sharp kind."
      New: "are always the sharp kind when empty space is quiet. That includes the assembled model's formation rule (below), so as written it gives massive things no inertia."
    - Old: "That is how real particle tracks form in a detector."
      New: "This matches the textbook account of cloud-chamber tracks (comparison, not adopted)."
    - Old: "Newton's first law comes out of the toy, and a thrown ball easily qualifies."
      New: "Newton's first law comes out of the one-dimensional toy, with a small 3D check: records line up straight and evenly spaced. A thrown ball easily qualifies."
    - Old: "- **Catch:** sharp contact bumps put about half the bounce into a \"time-doubled\" partner state, which must be suppressed."
      New: "- **Catch:** in the toy, a bump made at a single site sends about half of whatever bounces back into a \"time-doubled\" twin that flickers at the tick rate. Nothing like it is seen, so such bumps must be avoided or the twin shown invisible. The bounce shrinks with mass squared; the real-world size is not computed."

20. Old: "- every record locks the same content."
    New: "- every record locks the same content;
    - massive things it records directly lose all inertia; straight tracks need records formed on a go-between (A19)."

21. Add these decisions:
    - "9. **Memory:** may a site carry a small memory besides its possibilities? Build-up-over-time formation, local ticks and smoother pacing all need one (A12, A15, A17). If not, any memory must be made of matter or records."
    - "10. **Pacing:** when two neighbours' change per tick differs, does passing between them go at the product (full light bending), the average, or the slower of the two (half bending)? Are the wandering records that carry the slowing themselves slowed (A14, A18)?"
    - "11. **Direct records:** may a lone moving thing form records straight from its own neighbourhood? If so, it loses all inertia (A19)."

22. Before sending: verify the `probes/work/campaign8-tick-moving-records-20261002/` path (A16 fix 15 is still open).

---

## Top 3 risks

1. **The A18 package reads as a near-success, and it isn't one.**
   - The match holds only for two-site light, at the ray level, with γ and β dialled in.
   - It needs an unslowed gravity carrier (an absolute clock), and light runs at under 1% of the grid limit.
   - Four-site-loop light gets γ = 2.
   - A14's photon-mass cross-constraint (u∞ ≲ 1e-47) pushes A18's own smoothing radius to about 50 kpc.
   - The draft lists only "dialled in".

2. **The gravity and tick story contradicts itself.**
   - "Pace can't be set by possibilities" against "gravity rides on possibilities": only nonlinear dials signal (6.9e-2 vs 2.7e-16).
   - Line 36's "set by nearby records" against A17, which also overturns A16 C8.
   - "Every record-based version", "would have to be", and an unverified repo-lane claim. That lane rests on the sea the draft disputes.
   - The owner could adopt "nearby records set the pace" as the answer to I1 when the campaign's own results exclude it.

3. **The vacuum and menu text could steer decisions 4 and 6 from misstated premises.**
   - "5 per million ticks … freezes at once" is a per-unit-strength figure. The conclusion survives only as a ratio: a few days, or about 80 s.
   - "Memory at each site" and "records next to records" are overbroad. Per-site memory recurs across A12, A15 and A17 as one import, and should be one decision.
   - The proposed Q7 text lost A16's "only from records cut to agree" condition.