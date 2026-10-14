# Panel D: foundations skeptic / axiom economy (2026-10-14)

**Who wrote this.** Claude Opus 5.5. This is the same model family as the supervisor and all 18 exercise agents, so it is not independent. No repository was edited. One tiny script is in `scripts/` (`skeptic_arith.py` → `.out`): block-size arithmetic and one proton-decay estimate.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (AX).
- The axiom-update criterion memory.
- The exercise packet `SUMMARY.md`, `ROUTES.md`, `WALL.md`, `ASSUMPTIONS.md` and `OUTSIDE_VIEW.md` in full; F2, K3 and X3 in full; X1, X2, F4, F6 and K2c in the cited parts; the K2c referee verdict.
- On origin/main: DEFERRED_DECISIONS #4.
- In the gravity packet: SUMMARY §26–27; the TESTS rows R19-28, R19-33 and the C5 follow-up; panel F's SYNTHESIS; PRICE_NOTE P10, P12, P14 and P183; R2-4 §5; the kinetic-isotropy primitive.

**State of the running tests.** At 20:54Z, NT-1 and NT-2 had no report, and NT-3 had only its pre-registration.

**Labels:** proved / checked / suggested / reading / comparator.

**Path keys.**
- `CH:` = `origin/claude/chirality-grid-exercise-20261014:.claude/science/exercises/chirality-grid-20261014/`.
- `GR/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `DD` = `origin/main:docs/repo/DEFERRED_DECISIONS.md`.

---

## Plain words

**The common fact.** The four axioms supply three things to every chirality route:
- the cubic grid (Z³) with its rotations;
- one qubit's worth of possibilities per point;
- a neighbour rule for the odds.

Everything else the routes use is put in by hand and named as a price: fermions, force fields on links, a Hamiltonian or transfer matrix, and the number of matter slots per point. The four decisions ask whether to write some of those hand-supplied pieces into the axioms.

**My rule** comes from Jon's own criterion. Do not change an axiom to rescue a route that has not passed its decisive test. Change one only when there is a plain sentence about how reality works that a layman could follow.

**My answers.**
- **D1, matter per site.** No axiom change now.
  - Option (a), "keep the qubit, call a block of qubits a site", is not the free option it looks like. Blocking breaks the axioms' "every point is alike" clauses (translations, and rotations about each point). The gravity campaign already priced this (P183).
  - Matter per site is not a chirality-only question. Gravity's root (~90 modes per site), the supplied graviton and the force-field links already exceed one qubit per point.
  - Decide it once, for all lanes, after a route passes its decisive test. Record "chirality is not realized under the axioms as written" as **today's status**, not as policy.
- **D2, range.** No.
  - Keep "one fixed nearest-neighbour rule".
  - Jon's own reading, that influence spreads through networks of nodes, is exactly the class that Lemma R proves cannot give exact chirality.
  - Exactness itself is not observed. A finite approximation that is good enough needs extra modes per site, which turns D2 back into D1.
- **D3, time.** Keep set C (continuous time) as the working default.
  - Set B has the best layman sentence on the table: "time is a fourth grid direction, so everything shares one speed limit."
  - But its bridge back to real-time probabilities has now failed on four separate objects. The repair on offer, Π-W, rewrites the Admissibility axiom's own noun from "probability distribution" to "weight". I do not see that Π-W even fixes the chirality failure, which K2c found in a real, positive weight.
  - So set B as it stands costs up to three axiom-text changes, and only one of them has a layman sentence.
- **D4, compute.** Buy information, not axiom text.
  - Let NT-3 (T-G1, hours) finish first.
  - If it reads symmetric, make one narrow collaborator ask for the corner package, which is the route with the smallest per-site cost.
  - Do not fund weeks of QMC before that. Defer 4D HMC.

---

## D1. Matter per site

**Recommendation.** None of (a), (b) or (c) as a policy today.
- Keep AX:47 as written.
- Record (c) as the current status.
- Wake #4, re-scope it from "M₄(C) for γ5" to "site content for all lanes", and re-park it behind one gated wake condition (see "One concrete next action").

**Reasons.**

1. **(a) moves the price; it does not avoid it.** [reading; prior art counted once]
   - The repo already priced "block site algebra … or blocking ~6 log₂(2S+1) sites" as `AX:47`, *or* `AX:37 + AX:57` (`GR/PRICE_NOTE.md:601`, P183).
   - A law with a b³ block period is not covariant under unit translations (AX:57-58), or under proper rotations "about each site" (AX:37-38). It is covariant only under block translations and rotations about block centres.
   - Couplings inside a block span about b sites, so "nearest-neighbour" fails too unless the block's internal couplings are laid out as chains.
   - From `scripts/skeptic_arith.out` [suggested arithmetic]:
     - the 32 modes per site of the corner package need b = 4–5 (64–125 qubits, allowing about 3 qubits per mode for a local fermion encoding; the overhead is an assumption);
     - the minimal onsite SMG needs b = 3–4;
     - the F4 slab needs b = 10–15.
   - The only way (a) costs no axiom text is a block structure that is **spontaneous**: the law stays site-uniform and the state picks the blocks. That is an unbuilt dynamical claim. The literature's emergent-fermion qubit models so far give only paired or Dirac spectra (`CH:OUTSIDE_VIEW.md:259-263`).

2. **(b) fails the axiom-update criterion today.**
   - "Each point holds 16 (or 32, or 10³) fermion slots" is a fit to a route's needs. It is not an explanation.
   - A candidate layman sentence exists, but only conditionally (see "One concrete next action"). Its physics is SMG, which is open across the whole field (`CH:SUMMARY.md:26-28`).

3. **(c) as a policy would concede the goal.**
   - Handedness is observed.
   - "Chirality is not realized on this lattice" means the framework fails an observed outcome, the very standard Jon set.
   - As a *status* it is accurate and costs nothing: no route has passed its decisive test (`CH:SUMMARY.md:50`).

4. **The question is not chirality's alone.** [reading]
   - The C5 root already needs a site of at least 90 qubits (`GR/agents/panel_F/SYNTHESIS.md:51-52`).
   - The graviton is supplied, which "conflicts with one M₂(C) per site" (`GR/SUMMARY.md:777`).
   - A graviton from qubits is estimated at about 30–2000 qubits per cell [worker] (`GR/PRICE_NOTE.md:602`).
   - C4's P10 continuum tower is an infinite fibre per cell (`GR/PRICE_NOTE.md:364`).
   - Force-field links are supplied structure outside AX:47 altogether (`CH:WALL.md:55`).
   - Deciding D1 for chirality alone would leave the others silently priced.

**Technical corrections to the dossier's D1 numbers.**
- **The corner package is 32 complex modes per site, not 16.** X2's prices give "16 Spin(10) components per walker component, i.e. 32 complex fermion modes (2^32 per site)" (`CH:combos/X2/COMBO_REPORT.md:212`). The dossier's "16" counts one walker component.
- **"Fermion number only mod 4" has an observable face** [suggested; `scripts/skeptic_arith.out`].
  - Z4^F allows ΔF = 4 processes such as p → e⁺π⁰, with quarks and leptons counted alike.
  - If light fermions see that violation only through the dimension-6 Eichten–Preskill leakage at the Planck scale (`CH:combos/X2/COMBO_REPORT.md:44`), τ ~ 6e44 yr, about 1e10 above the bound. At a 1e16 GeV scale it would already fail.
  - This should be a registered row, not an aside.
- **K3's governance finding stands.** #4's wake condition 1 literally fires (`DD:139-142`; `CH:kills/K3/KILL_REPORT.md:148-158`), and per `DD:13-15` that has to be reported to the owner. Lemma R removes the γ5 motivation (`CH:ROUTES.md:11`). What remains is site content.

---

## D2. Range

**Recommendation.** Do not accept a non-finitely-generated kernel as law content. Keep AX:57 as written.

**Reasons.**

1. **Jon's own range reading is the class Lemma R closes.** [proved, refereed + reading]
   - Jon: "we don't have an only-nearest-neighbour rule, right? You can influence through networks of nodes." The record agreed: Admissibility fixes the local odds rule, not the dynamics (`GR/TESTS.md:976-981`; AX:116-125).
   - A network of nodes with finitely many hidden helpers per site, eliminated through a gap, is exactly Lemma 0's rational class (`CH:routes/F2/ROUTE_REPORT.md:48-54`).
   - Lemma R (codex-confirmed, `CH:ROUTES.md:146-150`) says that class has zero net chirality.
   - So D2 is not "is quasi-local OK?" (Jon already said influence can reach far). It is "does the law contain an *infinitely* deep network per site, or a vacuum projector?" Those are F2-R's options (b) and (c) (`CH:routes/F2/ROUTE_REPORT.md:153-155`). Option (c) costs AX:94 ("a law privileges no states").
   - The referee notes the three-way list is not exhaustive (`CH:ROUTES.md:154`). The point stands for every listed option.

2. **The layman test fails.**
   - "Each point listens only to its neighbours" is a plain insight about reality.
   - "Each point's rule depends on a pattern that no finite arrangement of neighbours can build" is a mathematical admission, not an insight.

3. **What exactness buys is small and Euclidean-only.**
   - Exact GW gives an exact chiral projector. But the non-abelian measure's locality (L2α) is still open, the field's own problem (`CH:combos/X3/COMBO_REPORT.md:222`).
   - The real-time version then needs an infinite fibre per site (X3-C; the referee says the two prices co-occur and are not an equivalence: `CH:ROUTES.md:164`).
   - And gauged RP fails in the 2D proxy (K2c, codex-confirmed: `CH:ROUTES.md:190-204`).

4. **Under Jon's standard, exactness is not required.** [suggested]
   - "Only observed outcomes need to be matched." Exact lattice chirality is not an observed outcome; light handed fermions and gauge symmetry to observed precision are.
   - F2's finite-n approximation keeps a finite rule (AX:57-compatible in form). Its price is about 30 poles, roughly 60 auxiliary Dirac fields per physical field per site, for δ ≈ 1e-35 (`CH:routes/F2/ROUTE_REPORT.md:157-160`; Shamir's form needs 118).
   - Its gauge breaking is O(δ). The observational requirement is an order-of-magnitude estimate only: the ρ parameter needs δ ≲ 1e-35, and the photon mass needs δ ≲ 1e-88 unless U(1)_em is kept exact.
   - So D2-exact can be replaced by D1 (about 10² modes per site) plus one integer law parameter (n or L_s). This is not checked beyond that estimate. Gauge non-invariance is a known swamp: longitudinal modes, restoration by disorder.

5. **Set C mostly makes D2 moot.**
   - In continuous time, a non-local Hamiltonian is not against Admissibility as worded (P14, `GR/PRICE_NOTE.md:368`).
   - For free carriers with a compact charge, the GW family collapses to SMG anyway (Lemma H, `CH:routes/F2/ROUTE_REPORT.md` §4). The referee keeps other non-local escapes open (`CH:ROUTES.md:156`).
   - D2 binds directly only in set B, where the Euclidean weight *is* the site distribution (B3, `CH:combos/X3/COMBO_REPORT.md:244`).

---

## D3. Time

**Recommendation.**
- Set C stays the working default.
- Do not reopen set B as a law candidate until NT-1 and NT-2 come back positive.
- If they do, reconsider set B with its one layman sentence. If they do not, record set B's chirality branch as price-only.

**The honest bill on each side** (counted once).

| | Set C (Z³ × continuous time) | Set B (Euclidean Z⁴, a_t = a_s, OS) |
|---|---|---|
| Axiom text changed | none | **Lattice** Z³→Z⁴ (B1, AX:37); **Admissibility**: "probability distribution" → RP "weight" if Π-W is paid (`GR/agents/C5_R2-4_report.md:293`, AX:60-61), or "nearest-neighbour" → power-law non-local if Π-NL is paid (`:294`, AX:57); the chirality route adds AX:57 again via the overlap kernel (D2) |
| Approved primitive | `kinetic_isotropy_primitive` is stated on the Z³ × Z_τ regulator block (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md:19-27`) and needs re-reading under set C (`GR/PRICE_NOTE.md:182`, reading). **This cost of set C is missing from the dossier.** | consistent with the primitive; set B is its whole-law completion |
| Matter light cones | 4 tuned numbers per class, reset each order, or a counting clause (`GR/SUMMARY.md:778`) | zeroed by the 90° time–space rotation (refereed T1/F2/O1; `GR/SUMMARY.md:774`) |
| Gravity bill | C-box: 33 + 4 per class per order by codimension | 12 by codimension; lower only on the formal ledger, "not overall" (`GR/TESTS.md:8688-8689, :8768-8776`) |
| Real-time probabilities | native (Hamiltonian) | need RP. It has failed for box symbols (R10-2, refereed), the conserved GR bridge (R19-33 B-RP-FAILS, `GR/TESTS.md:8909-8913`), the gauged overlap under both measures, torus included (K2, K2c, codex-confirmed for the finite 2D U(1) proxy) and the hard plaquette bound for pure gauge at odd Lx (K2c referee: proved at Lx = 3; 3D/4D suggested) |
| Chirality routes | reduce to SMG for free compact charges (F2-T; the referee keeps other escapes open) | overlap: exact free spectrum (X3-A, referee-confirmed), but gauged RP fails (2D proxy) |
| Layman sentence | "time flows; the grid is space" (the current axioms) | "time is a fourth grid direction, so everything shares one speed limit": **a real insight**, the best one on the table |

**Reasons.**

1. **Set B's case is genuine.**
   - It is the only route that explains one light cone by symmetry rather than by tuning or a counting clause. The approved primitive already points there.
   - On explanatory economy, set B beats set C. That is the strongest case against my recommendation (see "The strongest argument from my tradition, and the steelman against it").

2. **Set B's entry ticket keeps bouncing.** The bridge from Euclidean weights to real probabilities, which Record needs because records are real outcomes, has failed on four distinct objects. Each failure is at its stated scope. Two of them (K2c) are finite 2D proxies, so they are not yet 4D results.

3. **Π-W is an axiom change in disguise, and is not shown to help chirality.** [reading]
   - R2-4 defines Π-W as a rewrite of AX:60-61's text, "probability distribution" → "weight (real or complex), reflection-positive under Θ = θ∘conj" (`GR/agents/C5_R2-4_report.md:293`). It literally "drops W1 (positivity)" (`:124`).
   - K2c's failing object is the massive vector-like Dirac overlap at m = 0.05. Its determinant is real and positive, and it is the *reflection form* that goes negative (`CH:kills/K2c/REFEREE_VERDICT.md`, "Strongest correct statement").
   - Π-W relaxes positivity of the weight but keeps RP under Θ. For a real weight, Θ = θ∘conj acts like the ordinary antilinear reflection. So I do not see how Π-W removes K2c's negative eigenvalue.
   - X3 itself calls Π-W for matter "a form not yet constructed" (`CH:combos/X3/COMBO_REPORT.md:252`).
   - This needs a referee. Until then, "Π-W for matter" should not appear as an available exit.

4. **The other exit, "5D fermions without PV", is shown only for RP of a vector-like determinant.**
   - The bare 5D determinant is PSD (Osterwalder–Seiler; `CH:ROUTES.md:184`; K2c §0 item 4).
   - X3 says its gauge invariance is only approximate, falling back to F2-R's finite-n price (`CH:combos/X3/COMBO_REPORT.md:311`). That is D1 plus D2's approximate branch.
   - A chiral light spectrum with that gauging is not shown in the packet [reading]. The exit exists for RP. It is not shown for chirality.

5. **Count.**
   - Set B for chirality, as of now, costs Lattice (one layman sentence), plus Admissibility's noun (Π-W, no layman sentence and not shown to work) or the 5D/finite-n branch (D1 at about 10², approximate gauge invariance), plus gravity's Π-W or Π-NL.
   - Set C costs no axiom text, one primitive re-reading, tuned cone numbers or a counting clause, and the D1 question that every route shares.
   - On axiom economy set C wins today. On explanatory economy set B wins if, and only if, its RP failures turn out to be proxy artifacts.

---

## D4. Compute and collaborators

**Recommendation.**
- (b) first, after the cheap in-house step: NT-3 is already running.
- No weeks-scale QMC funding before T-G1 reads.
- Defer 4D HMC (option (c) for that part).
- Record the prices either way.

**Reasons.**

1. **Tests are where axiom decisions should come from.**
   - A passing X2-MB or F4 DQMC tells you the per-site count D1 would need, and whether a layman sentence is earned.
   - A failing one closes a route without spending axiom text.
   - D4 is the only decision of the four that buys information without spending axiom budget.

2. **Order by per-site cost.** If anything is funded, the corner package (32 modes per site, Z³-native corners) comes before the F4 slab (~10³ qubits per site, an internal ladder read as part of a site; `CH:routes/F4/ROUTE_REPORT.md:153-164`). A positive result there costs the axioms least.

3. **Be honest in the ask.**
   - X2 is "the Eichten–Preskill design", with the Golterman–Petcher–Rivas symmetry-breaking phase as its open kill (`CH:ROUTES.md:43`).
   - K1's mean field already shows f_NN keeping the condensation channel at 1.14×, with no independent-site limit for either filter (`CH:ROUTES.md:102-103`).
   - What is new to offer collaborators is the exact decoupling of the light corners, [H, ψ(hw1)] = 0, and the cubic-invariant filter.
   - Natural first contacts: groups with existing 4D staggered SMG and 2+1D SMG QMC (Butt–Catterall–Hartshaw–Hasenfratz; Slagle–You–Xu lineage; `CH:OUTSIDE_VIEW.md:94-97`).
   - Collaborators also give the program its first independence beyond one codex referee. Every exercise agent is the same family (`CH:SUMMARY.md:7`).

4. **(c) is legitimate for 4D.** This is the field's 40-year problem (`CH:SUMMARY.md:20`). The framework does not need to beat the field to be honest. It does need its prices recorded.

---

## How the decisions interact

- **D3 = B forces D2.**
  - In set B the Euclidean weight is the site distribution (B3), so the overlap kernel sits in AX:57's object.
  - Answering D2 "no" in set B leaves only the finite-n / 5D branch, which lands on D1 at about 10² modes per site.
- **D3 = C makes D2 mostly moot.**
  - A non-local Hamiltonian is not against Admissibility as worded (P14; `GR/TESTS.md:976-981`).
  - The free GW family collapses to SMG (Lemma H). The referee's caveat on other escapes stands.
- **D1 = (a) does not make D2 moot for exact chirality.**
  - Finite blocks are finite fibres, and Lemma R holds for any finite fibre (`CH:routes/F2/ROUTE_REPORT.md:77-80`). Only an infinite block escapes, which is P-X3b.
  - D1 at about 10² modes *does* make exact D2 observationally unnecessary, if the O(δ) gauge breaking is harmless (suggested, unchecked).
- **Every surviving route lands on D1.**
  - SMG routes need 16–32 or about 10³ modes per site; the overlap needs ∞; finite-n needs about 10².
  - So D1 = (c) as policy kills every route. D1 at a finite count kills only the exact overlap.
- **D1 is shared with gravity.** The supplied graviton (P-N1), P183, P10 and the C5 root all already exceed AX:47. One cross-lane D1 decision, not a chirality-only one.
- **D3 and gravity are one choice.** Set B is the same Z⁴ choice as C5's question 6 (`GR/SUMMARY.md:796`), with the same Π-W/Π-NL price. If Π-W were ever paid, count it once across gravity, CP and matter (`GR/agents/C5_R2-4_report.md:293`). But see D3 reason 3: it may not cover matter at all.
- **D4 should come first in time.** Its outcomes set the count D1 needs and whether set B's RP failures matter (NT-1/NT-2).

---

## The strongest argument from my tradition, and the steelman against it

**My tradition (axiom economy; Occam and Quine).**
- An axiom set is worth what it forbids.
- Today the four axioms forbid almost nothing in the chirality work. Every route runs on hand-supplied fermions, links, dynamics and matter content.
- If the owner writes those supplies into the axioms one route at a time, the axioms become a list of whatever the last route needed, and stop being a theory.
- So pay in tests first and axioms last. Change an axiom only for a sentence that says why reality is that way.
- One such sentence is close: three generations from three grid directions, plus sixteen slots because sixteen is the smallest bundle whose mirror can be hidden. It is earned only if the dynamics works.

**The steelman against me.**
1. **Deferral is itself a decision, and it hides cost.**
   - #4 has been parked since 2026-09-05. Since then every lane has quietly exceeded one qubit per site.
   - The "fixed axiom" is fiction. Better to write (b) honestly than to keep a Qubit axiom that no physics lane obeys.
   - *My answer:* I accept that the status quo is dishonest *if left unstated*. Hence the action below: re-scope #4 as cross-lane site content and write the current over-budget down. Writing a number into the axioms before any route works would trade one dishonesty for a guess.
2. **On explanatory economy set B wins.**
   - One axiom change explains one light cone for every particle. Set C instead carries 4 tuned numbers per class per order to 1e-16, or a counting clause that is a stipulation in disguise.
   - By any Occam measure that counts parameters rather than axiom lines, set C is worse.
   - *My answer:* agreed on the cones. But set B's bill is not one line. It is the Lattice change, plus an Admissibility rewrite (Π-W or Π-NL) that gravity already forces, plus the open RP failures on four objects. If NT-1 and NT-2 clear the RP failures as proxy artifacts, I would move to set B.
3. **"Only observed outcomes" cuts against my D2 position too.**
   - If exactness is unobservable, then so is the difference between a sign-function kernel with a Planckian decay length and a nearest-neighbour rule.
   - Insisting on finite generation is a mathematician's distinction.
   - *My answer:* I agree it is unobservable. That is why I recommend the finite-n branch (AX:57 intact, cost moved to D1) over amending AX:57. Both match observation equally, so the cheaper axiom text wins.
4. **(c) is the honest answer.**
   - Forty years and 18 agents have not cracked it. The prudent owner records the wall as the framework's limit, and stops spending.
   - *My answer:* as a status, yes. As a policy it gives up the matter sector of a TOE on a question open across the whole field, when one cheap test (NT-3) is already running.

---

## What would change my mind (including NT-1, NT-2 and NT-3)

**NT-1 (chiral-measure RP, 2D anomaly-free chiral U(1)).**
- **Positive** (RP holds for the chiral measure on the torus where K2c's vector-like proxy failed): the K2c failure would look like a vector-like or proxy artifact. I would move D3 toward reopening set B, priced as Lattice (B1–B4) plus D2-exact, or the finite-n branch. I would still require NT-2 and an RP statement for the gravity bridge.
- **Negative:** set B's real-time chirality is dead without an unconstructed Π-W that, on my reading, does not address the failure. I would recommend recording set B's chirality branch as price-only, and closing route 1 of `CH:SUMMARY.md:56` for the owner bar.

**NT-2 (3D plaquette-bound RP).**
- **RP holds in 3D:** the odd-Lx 2D failure is a low-dimension artifact, and Admissibility read as hard support is not in tension with OS positivity (K2c item 4).
- **Fails:** the overlap's locality condition (the hard bound) and OS positivity are incompatible even without fermions. That is a second, independent block on set B's chirality route, and possibly on any set-B gauge theory that uses AX's support reading. Set B would then need a soft gauge measure, which K2 showed also fails for the overlap. I would close set B for gauge matter.

**NT-3 (T-G1; toy rings plus the 2×2×2 cube; readings fixed in `next/NT3/PREREG.md`).**
- **TG1-SYMMETRIC** for at least one filter, with the cube consistent: it justifies the collaborator ask for X2. I would draft, not adopt, the conditional layman sentence for D1.
- **TG1-BROKEN** for both filters: X2 is wounded further (GPR-type order or degeneracy). Compute should then go to F4's DQMC or nowhere, and D1's lowest live count rises to about 10³ qubits per site. That is a much harder sell under the criterion.
- **OPEN:** no change.
- Either way it is a 1D/toy instrument, not 3+1D evidence (`CH:SUMMARY.md:65`).

**Other evidence that would move me.**
- **On D1:** a decisive test passing at a stated count. Or a demonstration that the block structure can be spontaneous in a site-uniform qubit law, which would make (a) genuinely free.
- **On D2:**
  - a checked computation that finite-n gauge breaking at δ ≈ 1e-35 produces no observable beyond the ρ estimate would remove the last reason anyone needs D2-exact;
  - a proof that it produces an unremovable observable effect would make D2 live and put it squarely on AX:57.

---

## One concrete next action

**An owner decision, which costs nothing and gates all spending.**

1. Wake #4 as K3 reports it must (`DD:13-15, :139-142`).
2. Re-scope #4 from "M₄(C) for γ5" (made irrelevant by Lemma R) to **"site content for all lanes"**. That means fermion modes, link registers and graviton slots against AX:47's "full one-site possibility domain M₂(C)". Write down today's over-budget per lane: C5 root ≥ 90, graviton P-N1, chirality 32 / ~10³ / ∞.
3. Re-park it with **one** wake condition, pre-registered now: a chirality or graviton route passes its decisive test (X2-MB, F4 DQMC or the R19-25 class) at a stated per-site count, **and** a one-sentence layman reason is written and survives a blind check. The candidate sentence, for the record and not adopted: *"Three generations because space has three directions; sixteen slots per point because sixteen is the smallest bundle whose mirror image can be hidden."*
   - Its known consequence: CKM mixing then forces a preferred strain direction in the flavour sector (X2-L8, `CH:ROUTES.md:43`). That is a channel the strain/equivalence-principle bounds can check.
4. Spend only D4 money in the meantime: NT-3, then the X2 collaborator ask.

This keeps all four axiom texts unchanged, makes the existing over-budget visible instead of silent, and ties any future change to a passed test plus a plain sentence. That is Jon's criterion, applied before rather than after the fact.

---

## Errata for the dossier and packet (found while reading)

1. **X2's per-site count is 32 complex modes, not 16** (`CH:combos/X2/COMBO_REPORT.md:212`).
2. **Option D1(a) is not cost-free.** It is P183's alternative pricing, `AX:37 + AX:57` (`GR/PRICE_NOTE.md:601`).
3. **Set C needs the `kinetic_isotropy_primitive` re-read** (`GR/PRICE_NOTE.md:182`). The dossier lists no set-C price.
4. **"Π-W for matter" is not shown to address K2c,** whose failing weight is real and positive. Π-W keeps RP under Θ (`GR/agents/C5_R2-4_report.md:293`). This is a reading; a referee is owed.
5. **"5D without PV" is shown RP only for the vector-like bare determinant.** Its chiral gauging is approximate (`CH:combos/X3/COMBO_REPORT.md:311`).
6. **Jon's own range reading** (`GR/TESTS.md:976-981`) means D2 binds AX:57 only in set B (B3). In set C a non-local Hamiltonian is a supplied-dynamics choice (P14).
7. **Z4^F should carry a registered ΔF = 4 observational row** (p → e⁺π⁰). It is safe at Planck-scale dimension 6 by about 1e10, and fails at about 1e16 GeV (suggested, `scripts/skeptic_arith.out`).
