# Exercise Five — Reframing the three ABJ identification walls

**Skill:** `docs/ai_methodology/skills/exercise/SKILL.md` (Exercise Five slice)
**Slug:** abj-walls-break  •  **Date:** 2026-06-20
**Posture:** treat framework premises as challengeable; move boundaries to find a
frame where an identification becomes UNNECESSARY, a SELECTOR becomes an admissible
DIAL, an EXISTENCE target becomes an admitted REGISTERED premise, or an OBSTRUCTION
becomes a MISSING-INPUT. NOT a claim of closure. No new axioms/primitives; no audit
verdicts; READ-ONLY on `docs/audit/data/`.

**Framework Refresher Read (stated):**
`docs/MINIMAL_AXIOMS_2026-06-05.md`;
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
`docs/audit/data/axiom_premise_nodes.json` + `tier_a_admissions.json` (READ-ONLY);
`docs/ai_methodology/skills/review-loop/SKILL.md`;
`docs/repo/CONTROLLED_VOCABULARY.md`;
`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (boundary);
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (the dial-vs-selector precedent).
Plus wall sources: `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`,
`CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md`,
`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`,
`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md`,
the keystone `ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md`,
the block01 attempts note (2026-06-20), and the anomaly-baxis-wall GROUNDING_MAP.

---

## The single most important reframe (read this first)

**The keystone consumer (step B4 → B5) does not consume the staggered-ε → γ₅
IDENTIFICATION, and does not consume any single-taste selection. It consumes only
the EXISTENCE of one taste-singlet γ₅ on the spacetime Clifford carrier.**

Verbatim consumption points from the keystone bridge note (2026-05-26):

- **B4:** "a chirality operator `gamma_5` satisfying `gamma_5^2 = +I`,
  `{gamma_5, gamma_mu} = 0` **must exist on the spacetime representation** that
  carries the gauge-theory anomaly evaluation."
- **B5:** "By retained CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION, `gamma_5`
  **existence** forces total spacetime dimension `d = d_s + d_t` to be even."

The B5 supplier (`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE`)
is **carrier-agnostic**: its statement is "an element `gamma_5 ∈ Cl_C(p,q)` with
`gamma_5^2=+I` and `{gamma_5, gamma_mu}=0` exists **iff** `n=p+q` is even." It
quantifies over *any* algebra element. It never asks which taste, never asks for
ε, never asks for an irreducible Dirac factor.

The P-REC ARITHMETIC CORE (block01, runner PASS=43; also the spintaste-core
branch PASS=12) already proves, on the blocked free staggered 2⁴ carrier, that
**`Γ₅^spin = α₀α₁α₂α₃` is a genuine taste-singlet spacetime γ₅**: Hermitian
involution, `{Γ₅^spin, α_μ}=0` for all μ, commutes with the full taste commutant
(residual 1.2e-15), and `{Γ₅^spin, D_red(m=0,p)} = 0` exactly. That is precisely
a witness of "γ₅ exists on the spacetime rep, taste-singlet." **It is exactly the
object B4/B5 quantifies over.**

So the P-REC "wall" (the gauged/interacting single-taste SELECTOR, root authority
`NO_PER_SITE_CHIRALITY_THEOREM`) is a wall for a STRONGER claim — "identify the
staggered ε carrier with γ₅ on one irreducible Dirac factor" — that **the keystone
consumer never makes**. The block01 note itself frames P-REC's consumed claim as
"staggered ε → spacetime Clifford γ₅ on the irreducible Dirac factor" (line 55) —
but B4 as written only needs *existence of a taste-singlet γ₅*, not the ε-bridge
nor the irreducible-factor projection.

**Why this is genuinely new (not a pruned route).** Every prior P-REC attempt
(routes_already_tested: "ε-as-γ₅ shortcut PRUNED ×2", "factored B=0 lemma",
"Cl(3)→Cl(3,1) alone INSUFFICIENT", "R4 interacting reconstruction WALLED") works
on the SUPPLY side — trying to PROVE the ε→γ₅ identification. A grep of `docs/`
finds the consumer-side question — *does B4/B5 require the identification at all,
or just existence of a taste-singlet γ₅?* — appears **nowhere**. This is the
object-vs-readout boundary move, and it is the kind of win Exercise Zero ranks
highest: "a reframe that makes an identification unnecessary for the consumer."

This reframe is developed as Reframe 1 below; the other four reframes are the
remaining EXERCISE FIVE prompts.

---

## Reframe 1 — object vs readout: B4/B5 need γ₅ EXISTENCE, not the ε→γ₅ IDENTIFICATION

| Field | Content |
|---|---|
| **Reframe** | Move the P-REC boundary from "the staggered ε carrier IS spacetime γ₅ on one irreducible Dirac factor" (a readout/identification of one specific carrier element) to "a taste-singlet γ₅ EXISTS on the spacetime Clifford carrier" (the bare existence object the consumer quantifies over). |
| **What moves** | The load-bearing object the keystone's B4→B5 step consumes. The single-taste SELECTOR and the ε-bridge move from "load-bearing premise of the bridge" to "out of scope for the bridge" (they belong to a separate, stronger, optional theorem). |
| **What becomes simpler** | B4/B5 close from the *already-banked* P-REC arithmetic core: `Γ₅^spin = α₀α₁α₂α₃` is the existence witness, and `CLIFFORD_VOLUME` (retained_bounded, carrier-agnostic) does the even-d step. No interacting dynamics, no taste restoration, no OS/continuum reconstruction, no single-taste pick. The "highest-value soft wall" stops blocking the keystone. |
| **What becomes harder** | One must verify B4 *as actually used downstream* never silently re-imports the stronger ε-identification or a per-generation single-taste assignment. The even-d conclusion is a *kinematic existence* statement; if any later step needs ε itself to be the physical chirality projector with a definite single-taste reading, that stronger need must be located and named separately. Also: `Γ₅^spin` lives on the *free blocked 2⁴* carrier; one must check the carrier B4 evaluates the anomaly on is that same Clifford carrier (the keystone says "the spacetime representation that carries the gauge-theory anomaly evaluation" — confirm it is Cl(d_s,d_t), not the per-site M₂(C) the NO_PER_SITE no-go rules out). |
| **New route opened** | **R-EXIST.** Re-target P-REC from "derive the single-taste selector / ε-bridge" to a NARROW POSITIVE bounded theorem: *"The keystone's B4 chirality-existence premise is discharged by the existence of a taste-singlet γ₅ (`Γ₅^spin`) on the spacetime Clifford carrier; the staggered-ε identification and single-taste selection are NOT required by B4/B5 and are scoped out."* This is a **consumer-firewall + partial-closure** of the P-REC edge that does NOT need R4. It would partially unlock the 1105 cone exactly where the block01 note left it walled. |
| **First decisive test** | A runner/proof artifact that (a) states B4's premise as the existence predicate `∃ γ₅ ∈ Cl_C(d_s,d_t): γ₅²=+I ∧ ∀μ {γ₅,γ_μ}=0`; (b) exhibits `Γ₅^spin` as a satisfying witness on the blocked staggered carrier (reuse the PASS=43 / PASS=12 constructions, do NOT rebuild); (c) checks `CLIFFORD_VOLUME`'s statement is invoked only on the *existence* quantifier (it is — its claim_scope quantifies over "an element gamma_5", carrier-free); (d) greps the keystone + parent for any downstream step that consumes ε-as-γ₅ or a single-taste reading beyond bare existence, and reports PASS only if none is load-bearing for the d_t-odd conclusion. **Decisive failure** = a located downstream step that genuinely needs the single-taste selector → the reframe is refuted and P-REC stays as the block01 note has it. **Decisive success** = no such step → B4/B5 close on existence and the P-REC wall is reframed away from the keystone. |

**Honest caveat / what this does NOT do.** R-EXIST does not derive the ε→γ₅
identification (R4 stays open as a separate, harder, genuinely-open target). It
does not give per-generation single-taste physics. It is a *scope correction on the
consumer*, not a new derivation of the selector. It must survive the "is B4 the
only consumer of γ₅?" audit; if any sibling row needs the stronger reading, that
row — not the keystone — carries the P-REC wall.

---

## Reframe 2 — selector vs admissible dial: is the single-taste selector a within-sector readout choice?

| Field | Content |
|---|---|
| **Reframe** | Move the single-taste selection from "missing law-level SELECTOR the framework must derive" to "an admissible within-sector readout DIAL fixed by the realized state," in exact parallel to the registered Koide `r ∈ {0, 1/2, 1}` dial. The free taste reconstruction has a full `M₄(C)` taste commutant of EXACT symmetries of `D_red(m,p)`; two orthogonal rank-4 single-taste projectors are equally invariant. The block01 verdict reads this as "registered data, not a derivation" (selector-dependent). The dial reframe AGREES the laws do not pick it — and then asks whether that is the WALL or simply the correct registered-state classification. |
| **What moves** | The classification of "no single taste is preferred." Under the SELECTOR frame this is a *wall* (an undischarged derivation target). Under the DIAL frame, by the `realized_state_primitive` ("the laws do not pick the state; the world does, among the states the laws permit"; register item 4: "dial settings are sector data, never forced"), the same fact is the *correct registered-data answer*: the within-taste-sector readout is selected by the realized history, pointwise, and a quantity that would differ under another admissible taste is registered data — exactly the primitive's counterfactual clause. |
| **What becomes simpler** | If the consumer only needs a quantity that is INVARIANT across the taste dial, the dial setting never has to be derived — it drops out by the counterfactual test. Combined with Reframe 1, the even-d conclusion (B5) is manifestly taste-dial-invariant (`Γ₅^spin` is the *taste-singlet* element; it commutes with the entire taste commutant, so it is the *same object* regardless of which single-taste projector a state would pick). So B4/B5's output is dial-invariant and the dial need never be set. |
| **What becomes harder** | The dial reframe is only legitimate if the single-taste choice is genuinely a WITHIN-SECTOR readout (post-record, state-contingent) and not a LAW-level structural input. One must show the taste label is a central-sector / within-sector datum (cf. Record: "K/CPT orbit of the realized central sector"; the primitive supplies the slot not the content), not a gauge-group or particle-content choice (which `MINIMAL_AXIOMS` withholds at law level and the primitive explicitly does NOT supply). If single-taste selection secretly encodes a particle-content or species choice, the dial frame is illegitimate and it stays a SELECTOR wall. |
| **New route opened** | **R-DIAL.** Register the single-taste readout as a within-sector realized-state dial (NOT a derivation target), and prove the keystone-consumed output (even-d / d_t-odd) is dial-INVARIANT, so the keystone never depends on the dial setting. This converts "P-REC single-taste SELECTOR walled" into "P-REC single-taste readout = registered within-sector dial; consumed conclusion invariant," parallel to how Koide `r` is handled. Pairs naturally with Reframe 1 (existence) — the taste-singlet `Γ₅^spin` is the dial-invariant witness. |
| **First decisive test** | (1) A runner showing the keystone-relevant output is invariant over the full `M₄(C)` taste dial (the counterfactual test of `realized_state_primitive`): vary the single-taste projector across the commutant, recompute the consumed quantity (γ₅ existence / even-d), confirm it is constant — `Γ₅^spin` being taste-singlet makes this near-trivial, which is itself the point. (2) A typing check that the taste label is within-sector readout data, not a law-level gauge/content input — read against `CHIRALITY_RECORD_TYPING_INTERFACE` (record consumes a chiral label after a bridge supplies it) and `MINIMAL_AXIOMS` (no species/content at law level). **Decisive failure** = the consumed output depends on the dial OR the taste label is law-level content → stays a selector wall. **Decisive success** = output dial-invariant AND label is within-sector → reframe lands as registered-data, removing the "wall" framing. |

**Honest caveat.** R-DIAL does not give a single physical taste; it asserts the
consumer does not need one. If any DOWNSTREAM physics (beyond the keystone's
even-d step) needs a specific realized single-taste value, that value is then
*registered data conditional on the realized state* — admissible to quote, never
derived, and NOT a closure of the selector. The dial frame is a classification
correction, not a derivation.

---

## Reframe 3 — existence vs availability (P-COMP): RH completion as admitted accepted-premise the audit lane registers

| Field | Content |
|---|---|
| **Reframe** | Move the P-COMP boundary from "DERIVE the existence/minimality of the opposite-chirality SU(2)-singlet RH template `{u_R,d_R,e_R,n_R}` (incl. n=0) from framework-native structure" to "REGISTER the RH completion as an admitted accepted-premise (availability), like the existing Tier-A admissions, with the arithmetic consequence banked as a conditional bounded theorem." The block01 note already proved the existence side is NOT derivable (Route 1: `CHIRALITY_RECORD_TYPING_INTERFACE` — "Record is a CONSUMER of chirality, not a source"; Route 2: steelman defeated three ways; n=0 fails the counterfactual test). The reframe stops trying to DERIVE existence and instead asks the audit lane to REGISTER it cleanly. |
| **What moves** | The disposition of the template-existence claim. Under the EXISTENCE frame it is a derivation target → an open wall (and "circular-on-parent"). Under the AVAILABILITY frame it is an admitted accepted-premise (a supplied input), and the bridge becomes a CONDITIONAL bounded theorem over that named premise — exactly the keystone's own "accepted-premise bridge" pattern already used for (P1) ABJ. |
| **What becomes simpler** | The arithmetic core is ALREADY a clean conditional bounded theorem (P-COMP classification PASS=49 forces `{4a,−2a,−6a,0}`; the decoupling boundary PASS=47 with the B1/B2/B3 non-vacuity lemmas). Registering the template as a named premise makes the bridge honestly bankable WITHOUT pretending existence is derived, and removes the "circular-on-parent" defect (the premise no longer routes through an unaudited parent — it is admitted, like (P1)). |
| **What becomes harder** | The audit-lane CLASSIFICATION question is sharp and not for this exercise to decide: is the RH completion a genuine **Tier-A admitted derivation target** (`tier_a_admissions.json`, which chain-satisfies only at `retained_bounded`), or a **named accepted-premise** (P-COMP-min, like (P1), an external/admitted input), or a **registered-state datum**? Note the Tier-A registry currently lists exactly TWO admissions (AC_phi_lambda, theta) and says new admissions need owner approval — so adding P-COMP as Tier-A is a governance act, NOT a worker move. The honest output is to expose the choice, not to make it. Also: n=0 is load-bearing (counterexample `(0,2a,−2a,−4a)`), so "register the template" must register n=0 explicitly as part of the admitted content, not silently. |
| **New route opened** | **R-AVAIL.** Re-file P-COMP as availability: (i) bank the arithmetic as a conditional bounded theorem over a NAMED premise "P-COMP-min: opposite-chirality SU(2)-singlet RH completion with neutral n=0" (absorb the existing PASS=49/PASS=47 branches, do NOT rebuild); (ii) surface the governance/audit-lane DECISION of which accepted-premise class P-COMP-min belongs to (Tier-A admission vs named accepted-premise vs registered-state datum), citing the `tier_a_admissions.json` boundary and the keystone's own (P1) precedent. This converts "existence WALLED + circular-on-parent" into "availability ADMITTED + arithmetic banked + class decision exposed." |
| **First decisive test** | (1) Confirm (read-only) the arithmetic core is deps-all-retained when the template is a named premise rather than routed through the unaudited parent (the SM_ANOMALY_CLOSURE precedent, PASS=11, already proved the SM-anomaly arithmetic bankable by severing it from the unaudited parent — same move). (2) Draft (do NOT land) the named-premise registration and the three candidate class-assignments with the governing rule for each, so the owner/audit lane can pick. **Decisive** = audit-lane/owner ratification of one class (governance act, outside this exercise). **This exercise's deliverable** = the clean availability reframe + the exposed class decision, not a verdict. |

**Honest caveat.** R-AVAIL does NOT derive the template and does NOT add a Tier-A
admission (that needs owner approval + a reviewed registry update — explicitly
out of worker scope per `PRIMITIVE_REGISTRY_CHECK` step 6 and the review-loop
boundary). It REFRAMES the wall from "underived derivation target" to "admitted
input with banked arithmetic + an exposed governance choice." That is strictly
honest: the existence is genuinely not framework-native (block01 proved this), so
availability-by-admission is the correct disposition, not a dodge.

---

## Reframe 4 — obstruction vs missing-input (P-ABJ external premise): is "external" the right frame, or a registered Tier-A admission?

| Field | Content |
|---|---|
| **Reframe** | Move P-ABJ's (P1) from "categorically EXTERNAL standard-physics premise (Adler/Bell-Jackiw), permanently outside A_min" to the explicit question: is (P1) an OBSTRUCTION (irreducibly external, cannot enter the framework registries) or a MISSING-INPUT that should be REGISTERED in `tier_a_admissions.json` as an accepted derivation target, exactly as the strong-CP `theta` admission is ("Also unsolved in the Standard Model")? |
| **What moves** | The registry HOME of (P1). Under "external" it sits in the keystone's prose as an accepted-premise packet entry only. Under "registered Tier-A admission" it would be a named derivation target that chain-satisfies at `retained_bounded` until retired — giving the keystone a clean, auditable dependency edge instead of a bare prose admission, and a standing invitation for future loops to retire it. |
| **What becomes simpler** | Treating (P1) like `theta` makes the keystone's dependency status uniform and machine-visible: a `retained_bounded`-tier admitted input rather than a special-cased external premise. The keystone is already written in the accepted-premise bridge form for (P1) — registering it as Tier-A would formalize what the prose already does, and let `compute_effective_status` cascade dependents correctly. The precedent is exact: `theta` is "Also unsolved in the Standard Model" and is a registered Tier-A target, not treated as forever-external. |
| **What becomes harder** | The PRINCIPLED distinction. `theta` and AC_phi_lambda are framework-INTERNAL naturalness/flavor targets the framework could in principle derive (and partial decompositions exist). (P1) is a statement about the consistency of *continuum chiral gauge QFT* — its content (Ward identities, unitarity) may genuinely live OUTSIDE the `Cl(3)`-on-`Z³` substrate's expressive reach, especially since the internal lattice route is walled by `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO` (ε-index = 0 on equal-sublattice even tori) and the framework-internal Wess-Zumino/Fujikawa companion (PR 402) was closed without merge. So "register as Tier-A target" presupposes the framework COULD derive it; if it categorically cannot (no-new-axioms + substrate limits), "external" is the honest frame and Decision I (owner) should ratify it as the one irreducibly-external premise. The exercise's job is to FRAME the choice with the deciding criterion, not to pick. |
| **New route opened** | **R-TIERA-ABJ.** Pose the explicit governance question (Decision I in the GROUNDING_MAP) with a concrete deciding criterion: (P1) is a registrable Tier-A target IFF there exists *any* framework-internal route (continuum-limit bridge, taste-singlet Adams index, overlap/GW, imbalanced/curved complex with χ≠0, non-abelian cohomology — the five rays the no-go explicitly leaves open) that could in principle witness the anomaly-to-inconsistency content; otherwise it is the one irreducibly-external premise. This is NOT a new derivation; it is a CLASSIFICATION that determines (P1)'s registry home and tells future loops whether to keep attacking the internal route or to accept the external admission permanently. |
| **First decisive test** | A criterion-check note (read-only on registries): enumerate the five open escape rays the `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO` preserves; for each, state whether a framework-internal witness is *conceivable in principle* (not whether it is proven). If ≥1 ray is conceivable, (P1) is a candidate Tier-A target (register it, keep the internal route open as a retirement path). If ALL five are themselves blocked by retained no-gos / substrate limits, (P1) is irreducibly external and Decision I should ratify "permanent external premise." **Decisive** = owner/audit-lane ratification (governance). **This exercise's deliverable** = the criterion + the ray-by-ray conceivability table, exposing the choice. Note Reframe 5 attacks one of those rays directly. |

**Honest caveat.** R-TIERA-ABJ does NOT derive (P1) and does NOT register a new
admission (owner-only). It reframes "external by policy" into an explicit,
criterion-driven REGISTRY-HOME decision, and connects it to the live open escape
rays so the choice is informed rather than asserted.

---

## Reframe 5 — finite carrier vs limiting family (P-ABJ index on curved/continuum complex)

| Field | Content |
|---|---|
| **Reframe** | Move the P-ABJ internal-route obstruction from "the staggered ε-index vanishes on A_min's FINITE flat hypercubic carrier" to "the index is a property of a LIMITING FAMILY of carriers (curved / non-hypercubic / continuum-limit cell complexes), of which the finite flat torus is the measure-zero balanced special case where it must vanish." The block01 P-ABJ result sharpened the obstruction to an EXCLUSIVITY: on A_min's closed hypercubic Z⁴, χ≠0 (imbalanced sublattices) occurs IFF every edge length is odd, which is exactly when the ε grading is destroyed in every direction — so on the *finite flat* carrier, χ≠0 and intact chirality are mutually exclusive. The reframe asks whether that exclusivity is a FINITE-FLAT-CARRIER artifact that dissolves in the limiting family. |
| **What moves** | The carrier the index is evaluated on. Under the finite-flat frame, the index is forced to 0 (square bipartite block ⇒ `BB†` and `B†B` isospectral ⇒ `A_t=0`), and χ≠0 destroys chirality. Under the limiting-family frame, the relevant object is the index of the *continuum / curved* Dirac operator that the lattice family approximates, where Atiyah-Singer gives a nonzero index from curvature/topology (χ≠0 or Q≠0) WITHOUT the bipartite-balance obstruction, because the obstruction (`B` square ⇒ isospectral) is a feature of the *finite equal-sublattice* discretization, not of the continuum index. |
| **What becomes simpler** | The block01 control already PROVED the escape mechanism is real off the flat carrier: an open 3×3 complex is imbalanced (N₊=5, N₋=4), KEEPS `{ε,D}=0` (rectangular `B`), and yields nonzero index `A_∞ = N₊−N₋ = 1`. So a *non-square* `B` (rectangular, from an imbalanced/curved/open complex) breaks the isospectral obstruction and gives a nonzero signed index. The limiting-family frame says: the physical index is the limit object; the finite flat torus is the one carrier where it is forced to zero. This dovetails with `ABJ_RESIDUAL_GW_NOT_NECESSARY`'s (P1′) re-target ("exhibit a χ≠0 or Q≠0 background"). |
| **What becomes harder** | A_min (Lattice = `Z³` cubic adjacency + `kinetic_isotropy_primitive` time edge = hypercubic Z⁴, equal sublattices) supplies ONLY the finite flat carrier where the index vanishes. The curved/imbalanced/open complex that carries χ≠0 is structure A_min does NOT supply (the block01 control is explicitly OFF-substrate). The limiting family also needs a *taste-singlet* index (the naive ε-index is taste-confused; cf. P-REC R3a: ε ∉ {α}″, residual 4.0) and a continuum-reconstruction (OS/Reisz) bridge — neither is in A_min or the four primitives. So this reframe converts the obstruction into a MISSING-INPUT (the limiting carrier + the taste-singlet continuum index), which is a derivation target, not a free move. |
| **New route opened** | **R-LIMIT.** Re-target the P-ABJ internal route from "force a nonzero ε-index on A_min's finite flat torus" (PROVEN impossible, square-block no-go) to "construct the index on a LIMITING FAMILY where the finite flat torus is the degenerate balanced member": (i) a taste-singlet Adams/overlap index (the no-go explicitly leaves this open, and P-REC's `Γ₅^spin` is the taste-singlet grading to use — connects to Reframe 1); (ii) on an imbalanced/curved/open cell complex with χ≠0 (the block01 control's rectangular-`B` mechanism, generalized); (iii) as the continuum limit where Atiyah-Singer applies. The honest framing is OBSTRUCTION → MISSING-INPUT: name the missing carrier + index + continuum bridge as explicit derivation targets, NOT claim them supplied by A_min. |
| **First decisive test** | A runner that builds the **taste-singlet** index (using `Γ₅^spin` as the grading, NOT the naive site-parity ε) on a *family* of carriers interpolating from the balanced flat torus to an imbalanced/curved complex, and exhibits where the index becomes nonzero. The block01 control (open 3×3, index=1) is the existence proof that nonzero is reachable; the new content is (a) using the taste-singlet grading so it is the physically-correct chiral measure, and (b) making it a controlled FAMILY/limit rather than a one-off off-substrate complex. **Decisive failure** = the taste-singlet index also vanishes on every A_min-reachable carrier and the nonzero cases all require non-A_min structure → the obstruction is intrinsic and (P1) stays external (feeds Reframe 4's "irreducibly external" branch). **Decisive success** = a taste-singlet index nonzero on a carrier that is a legitimate limit of A_min-admissible complexes → the internal route reopens and (P1) becomes a Tier-A retirement candidate (Reframe 4's other branch). |

**Honest caveat.** R-LIMIT does NOT supply the curved/limiting carrier from A_min —
A_min gives the flat finite torus where the index provably vanishes. It reframes the
obstruction as a NAMED missing-input (limiting carrier + taste-singlet continuum
index + reconstruction bridge), turning a dead "ε-index = 0" wall into a structured
derivation target with the block01 control as the non-vacuity witness. It does not
claim closure; the square-block no-go on the FINITE FLAT carrier stands untouched.

---

## Cross-reframe synthesis (route portfolio for this slice)

| Rank | Route | Reframe boundary moved | Premise challenged | Status if successful | First artifact | Stop condition |
|---|---|---|---|---|---|---|
| 1 | **R-EXIST** | object vs readout | "B4 needs the ε→γ₅ identification / single-taste selector" | P-REC partially CLOSED for the keystone (consumer-firewall + existence witness); 1105 cone partially unlocked at B4/B5 | runner: existence-predicate statement of B4 + `Γ₅^spin` witness + grep proving no downstream step needs the stronger reading | a located downstream consumer that genuinely needs the single-taste selector |
| 2 | **R-DIAL** | selector vs admissible dial | "single-taste selection is an underived law-level SELECTOR" | P-REC selector reclassified as registered within-sector dial; consumed output dial-INVARIANT | runner: counterfactual taste-dial-invariance of the consumed output + typing check (within-sector, not law-level content) | output depends on the dial, or the taste label is law-level gauge/content |
| 3 | **R-LIMIT** | finite carrier vs limiting family | "the ε-index obstruction is intrinsic to the chirality grading" | P-ABJ internal route REOPENED as a structured missing-input (taste-singlet index on a limiting family) | runner: taste-singlet (`Γ₅^spin`-graded) index on a balanced→imbalanced/curved carrier family | taste-singlet index vanishes on all A_min-reachable carriers |
| 4 | **R-AVAIL** | existence vs availability | "P-COMP template existence must be DERIVED from native structure" | P-COMP reframed to admitted availability + banked arithmetic + exposed class decision (removes circular-on-parent) | named-premise draft + the three candidate accepted-premise class-assignments with governing rules | owner/audit-lane picks the class (governance) |
| 5 | **R-TIERA-ABJ** | obstruction vs missing-input | "(P1) is categorically external, never a registry target" | (P1) reframed to a criterion-driven REGISTRY-HOME decision (Tier-A target vs irreducibly-external) | criterion + ray-by-ray conceivability table for the five open escape rays | owner/audit-lane ratifies the registry home (governance) |

**The two highest-value, genuinely-new, WORKER-actionable routes are R-EXIST and
R-DIAL** (both attack the highest-value soft wall P-REC, both produce runner-checkable
artifacts, neither needs a governance act, neither re-proposes a pruned route). They
COMPOSE: `Γ₅^spin` is simultaneously the existence witness (R-EXIST) and the
dial-invariant taste-singlet object (R-DIAL), and it is also the correct grading for
R-LIMIT's taste-singlet index. **R-LIMIT** is the strongest genuinely-new attack on
P-ABJ's internal route (the prior work only enumerated the rays; R-LIMIT attacks the
"limiting family" framing with the block01 rectangular-`B` control as a non-vacuity
witness and `Γ₅^spin` as the correct grading). **R-AVAIL and R-TIERA-ABJ** are
honest CLASSIFICATION reframes that expose governance decisions — they remove the
"wall"/"circular-on-parent" framing without a derivation, and are correctly out of
worker-verdict scope.

## What NOT to do next (from this slice)

- Do NOT re-attempt the ε→γ₅ identification (R4) as the way to discharge B4 — it
  is genuinely walled AND, per Reframe 1, the keystone consumer does not need it.
  Attack the consumer-side existence framing first (R-EXIST); only pursue R4 as a
  separate, harder, optional theorem if a downstream consumer of the stronger
  reading is actually located.
- Do NOT add P-COMP or (P1) to `tier_a_admissions.json` or any registry — that is
  an owner/governance act (PRIMITIVE_REGISTRY_CHECK step 6; review-loop boundary).
  R-AVAIL / R-TIERA-ABJ EXPOSE the class decision; they do not make it.
- Do NOT claim R-LIMIT escapes the square-block no-go on the finite flat carrier —
  it does not; the no-go stands. R-LIMIT changes the CARRIER (limiting family),
  which the no-go itself lists as an un-pruned route, and names the missing inputs.
- Do NOT re-derive any arithmetic core (P-HY/P-COMP/P-REC spin-taste/full-gen
  cancellation) — all exist and are runner-verified; ABSORB per the GROUNDING_MAP
  duplication_warnings.
- Do NOT treat any of these reframes as a closure: the normal output is a better
  attack map. R-EXIST/R-DIAL/R-LIMIT each have an explicit decisive-FAILURE
  condition; run those tests before claiming anything moved.
