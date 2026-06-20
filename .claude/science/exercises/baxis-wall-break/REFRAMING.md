# EXERCISE FIVE — Reframing (B-AXIS wall-break)

**Slug:** baxis-wall-break · **Date:** 2026-06-20 · **Slice:** Exercise Five (Reframing)
**Posture:** wall-BREAKING, not wall-defending. Framework premises are treated as
challengeable assumptions for this exercise. This file proposes NEW reframes and
NEW routes; it asserts no closure, applies no audit verdict, adds no axiom/primitive.
Independent audit lane is the sole status authority.

## Refresher surfaces read (stated per skill requirement)

- `docs/MINIMAL_AXIOMS_2026-06-05.md` (Lattice/Quantum/Record; the open gates list)
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (4 approved primitives)
- `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` (units-only, no dimensionless content)
- `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (c_t=c_s; "time-direction
  analogue of the LATTICE axiom's spatial cubic adjacency"; presupposes an emergent
  time direction) — **load-bearing for this slice**
- `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (pointwise eval at realized state;
  past hypothesis explicitly NOT housed here)
- `docs/audit/data/axiom_premise_nodes.json` + `docs/audit/data/tier_a_admissions.json` (READ-ONLY)
- `docs/ai_methodology/skills/review-loop/SKILL.md` (axiom/primitive/Tier-A distinction; Record guardrails)
- `docs/repo/CONTROLLED_VOCABULARY.md` (status taxonomy; central-sector vs within-sector)
- Wall surfaces: `.claude/science/exercises/baxis-wall-break/EXERCISE.md`;
  `docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`;
  `.claude/science/physics-loops/single-clock-baxis-wall/NO_GO_LEDGER.md`;
  `.../block02_section_frame_and_relocation.md`; `.../block02_section_N5.md`;
  keystone `docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`;
  `docs/SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`;
  `docs/SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`;
  `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`;
  `docs/RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`;
  runner `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` (header read).

---

## 0. The single load-bearing observation this slice adds

The campaign's whole N4/N5 wall is computed on the **bare** staggered-Dirac surface.
The N4 automorphism runner header is explicit: it enumerates the 384-element signed
hyperoctahedral group acting on the four Euclidean axes of the **Euclidean 4-torus**
`Z^3 × Z_τ` and finds the axis-permutation image is transitive S₄. **It uses none of
the approved primitives.** In particular it does not use `kinetic_isotropy_primitive`.

But `kinetic_isotropy_primitive` (approved, registered) is defined as setting
`c_t = c_s` — and that statement is *only meaningful if there is already a
distinguished "t" coordinate to compare against the "s" coordinates*. Its own note
calls it "the time-direction analogue of the LATTICE axiom's spatial cubic adjacency
`a_x = a_y = a_z`" and says it "fixes only the one graining ratio relating that
emergent time to space." The keystone theorem (S3′) even cites it and says it "makes
the surface **more** exchange-symmetric, not less."

That last sentence is, on inspection, the misframing. The kinetic-isotropy primitive
does **not** symmetrize the four axes into one orbit; it presupposes a **1+3 split**
(one time, three space) and then equalizes the two *blocks'* kinetic coefficients. A
1+3 split with equal coefficients is not the same object as a fully symmetric 4-set:
S₄ acts transitively on 4 points, but the stabilizer of a 1+3 partition is S₁×S₃ = S₃
— **exactly the "fixes one axis, permutes the other three" subgroup the N4 steelman
(E7) was hunting for**, and which the campaign concluded only a non-A_min boundary
datum could supply. The campaign treated the c_t/c_s structure as living *downstream*
of B-AXIS (the keystone consumes the primitive's "direction"); but the primitive is an
**approved premise node that chain-satisfies without bounding**, and it is logically
*upstream* of, and independent of, the staggered carrier. This is the central new
lever and it threads three of the reframes below.

This is NOT a claim that N4 is solved. It is the claim that the wall as computed has
been quietly testing the WRONG surface — the bare carrier rather than the
primitive-enriched carrier the framework actually grants — and that the gap between
"S₄-transitive" (bare) and "S₃-fixing-one" (kinetic-isotropy-enriched) is a concrete,
runnable, possibly decisive crack. First test is given in Reframe A1 below.

---

## 1. Reframe table

Columns: **Reframe | What moves | Simpler | Harder | New route opened | First decisive test**

### A. The "which-of-4-axes is time" frame (stress-test of misframing (a))

| Reframe | What moves | Simpler | Harder | New route opened | First decisive test |
|---|---|---|---|---|---|
| **A1. N4 is a representation-choice artifact of the Euclidean-4-torus presentation, not a missing physical input — because an approved primitive (kinetic_isotropy) already supplies the 1+3 split the wall says is absent.** | Boundary moved: *representation choice* (4-torus reconstruction) vs *physical observable* (the 1+3 graining the framework grants at premise grade). The c_t=c_s structure moves from "downstream of B-AXIS" (keystone's framing) to "upstream premise, independent of the staggered carrier." | The N4 "which axis" question reduces to "does the kinetic-isotropy partition predicate fix the time block?" — and the primitive *defines* a time block. The S₄-transitivity computation is then exposed as a property of a surface that **omits an approved premise**, i.e. a strawman surface. | Must show the 1+3 partition is the *unique* such structure compatible with the primitive (could there be a 2+2 graining?) and that admitting the primitive's partition does not itself smuggle B-AXIS. Need to recompute the automorphism group of the **primitive-enriched** carrier (staggered hop ⊕ a c_t/c_s-weighted kinetic quadratic form), not the bare hop. | **N4-via-kinetic-isotropy-partition:** the missing axis-selector is not "outside A_min" — it is the already-approved `kinetic_isotropy_primitive`'s 1+3 partition predicate. If the joint stabilizer of {staggered hop, c_t≠c_s kinetic quadratic form} is S₃-fixing-the-time-block, the axis *label-block* is fixed by an approved premise (no new axiom), even though the within-block orientation among the 3 spatial axes stays free (which is correct physics — space is isotropic). | Recompute the N4 automorphism runner on the **anisotropic** quadratic form `Q(p)=c_t p_τ² + c_s|p_s|²` with `c_t ≠ c_s` (the SPATIAL_CUBIC gate already proves O_h leaves exactly TWO coefficients, and the 4D-hypercubic/transitive-S₄ collapse needs `c_t=c_s`). The gate's own runner shows the anisotropic form "fails a time-space swap" — i.e. **W is already broken by the kinetic form whenever c_t≠c_s**. The decisive question: is c_t=c_s the *output* (emergent-Lorentz) or is the *partition* (which two coefficients exist) the *premise*? The SPATIAL_CUBIC gate says O_h alone gives the 2-coefficient invariant space — so the partition is O_h-structural, BELOW the c_t=c_s choice. Test: confirm the partition predicate "τ is the axis whose kinetic coefficient is independently variable under O_h" is W/S₄-**transportable or not**. (The s4-transportable branch tested BC data, never the kinetic-coefficient partition.) |
| **A2. Native one-parameter-group-on-Z³ frame makes N4 a non-question AND keeps the residual honest — but the campaign mis-located the residual: orientation, not generator-existence, is the only genuine open piece.** | Boundary moved: *dynamics vs kinematics*. Time = parameter `t∈ℝ` of `U(t)` on fixed `⊗_{x∈Z³}ℂ²`; there is no x₄ to permute, so N4 dissolves *as a question* (campaign already says this). What moves NEW: the campaign claims all three residuals + orientation "funnel to one emergent-dynamics gate." That funnel is too coarse. | N4 genuinely vanishes (no 4th coordinate). The Stone core already gives "unique generator given (T̂², τ)". So in the native frame, "which generator" is supplied by the SAME (R-RP2)/(R-SC2) transfer data the framework already grants at retained_bounded — there is no *additional* generator-existence gap beyond what's retained. | The native frame must explain where the transfer T̂² *came from* without a 4-torus (the transfer is currently RECONSTRUCTED from the Euclidean τ-direction). If T̂² only exists because a Euclidean time direction was chosen, the native frame has not escaped N4 — it has hidden it in "where does U(t)'s generator come from." This is the real test of whether A2 is honest. | **Generator-provenance audit:** separate (i) generator *form* (the staggered Ĥ=Σ E(p)n_p — supplied by retained_bounded RP/SC) from (ii) generator *selection-as-time* (calling THIS the Hamiltonian vs calling some n_p the Hamiltonian — this is N5, not N4). Claim: in the native frame N4 is genuinely empty and the entire residual is N5 (which factor is "the clock") + N2b (its rate) + orientation (past hypothesis). N4 was an artifact of the Euclidean embedding. | Build the staggered free transfer T̂² **without** ever choosing a Euclidean time axis — i.e. from the spatial transfer-matrix / Hamiltonian-lattice (Kogut-Susskind **Hamiltonian**, not Lagrangian) formulation, where time is already continuous and only `Z³` is discretized. If T̂²'s generator Ĥ is constructible from `Z³` + Quantum + the Hamiltonian KS staggering *without* a τ-lattice, then N4 provably never arises and the wall's N4 clause is a presentation artifact. (KS Hamiltonian lattice gauge theory is the canonical such object; Kogut-Susskind 1975.) |
| **A3. "Time as a 4th lattice coordinate" is itself the over-strong premise the keystone should never have adopted — the keystone's S2′ derives codim-1 slices, which already PRESUPPOSES a slicing direction, so the keystone is internally circular on N4.** | Boundary moved: *obstruction vs missing input*. The keystone (S2′) asserts each slice Σ_t={t}×Z³ is codimension-1 Cauchy. But "Σ_t" requires a t to slice along — S2′ consumes the very axis S3′ then admits is undeer. | If true, N4 is not a *missing supplier* the framework must derive; it is a *self-inflicted* premise from choosing the codim-1-slice presentation. Drop the slice presentation (use native U(t) on the whole `Z³`) and N4's premise-status is exposed as optional, not necessary. | Must show the *downstream consumer* (ANOMALY_FORCES_TIME, d_t≤1) does not itself need the codim-1 slice — i.e. that the `d_t≤1` cap survives in the native frame. If the consumer truly needs "number of time directions ≤ 1," that is a count (N-of-axes), not a label (which-axis), and counts are W-invariant (the anomaly firewall already says so). | **Count-not-label promotion:** the keystone's real downstream deliverable is `d_t ≤ 1` (a COUNT). The anomaly-count firewall already establishes that ε=(−1)^{Σx} W-invariance constrains the *number* of temporal directions. So the keystone may only need N4-as-count (≤1 time axis), which A_min's exchange symmetry + a single past-hypothesis boundary *does* fix, NOT N4-as-label (which of 4). The label may be pure gauge. | Audit the 959-row downstream cone: does ANY consumer use the *label* of the time axis (vs the *count* ≤1 and the *orientation*)? If every consumer only needs (count ≤1) + (orientation from past hypothesis), then N4-as-label is gauge and the wall's N4 clause is vacuous downstream. Grep consumers for label-dependence vs count-dependence. First file: `SINGLE_CLOCK_BAXIS_CONSUMER_FIREWALL_COVERAGE_NOTE_2026-06-20.md` (11 consumers already enumerated). |

### B. The second-clock / N5 frame (stress-test of misframing (b))

| Reframe | What moves | Simpler | Harder | New route opened | First decisive test |
|---|---|---|---|---|---|
| **B1. N5 IS a within-sector-vs-central-sector readout distinction (the prompt's hypothesis (b)) — the L_s commuting per-mode "clocks" are within-sector data the Record axiom explicitly does NOT register, so they cannot be physical second clocks.** | Boundary moved: *central sector vs within-sector data*. The N5 countermodel's per-mode occupation records `(⟨n_0⟩,⟨n_1⟩,…)` are the alternate clock's "Record-visible discriminator." But the Record axiom registers only "the K/CPT orbit of the realized **central** sector," and the canonical proposal note (verbatim) says Record supplies **no within-sector data**. | If the per-mode occupations `n_p` are *within-sector* observables (not central-sector outcomes), then they are NOT records in the axiom's sense — so the N5 "Record-visible second clock" is not actually Record-visible. The whole N5 non-vacuity witness (min-dist≈0.40 over swept t) would be measuring a within-sector quantity Record disclaims, collapsing the witness. | Must determine the central-sector decomposition of the staggered transfer surface. Which operators are "central sector" (= the K/CPT-orbit-valued recorded outcome) vs "within-sector"? If the `n_p` ARE the central sectors (occupation number is the pointer basis), B1 fails and N5 stays load-bearing. This is a genuine, decidable algebra question, not a hope. | **Central-sector test of N5:** compute the finite central-sector decomposition (the `{P_k}` of the Record canonical proposal) for the staggered `T̂²` surface. If the per-mode number operators `n_p` lie *within* a single central sector (i.e. they commute with all `P_k` and vary the within-sector content), then by the Record axiom they carry NO recorded outcome, the N5 "distinct durable records" claim is measuring within-sector data, and N5's non-vacuity collapses — the second clocks are gauge *with respect to Record*. | Take the N5 runner's `T̂²=⊗_p diag(1,e^{−2E(p)})`, the K/CPT conjugation, and the central-sector projectors `{P_k}`, and test: do the alternate-clock generators `n_p` (p≠admitted) move the *central-sector* label `argmax_k Tr(P_k ρ)`, or only the *within-sector* content? The N5 runner currently checks "durable occupation record" — but does NOT check whether that record is a central-sector outcome or within-sector data. That check is the missing leg. Reuse `single_clock_n5_irreducibility_factor_clock_2026_06_20.py` + the central-sector machinery from `RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`. |
| **B2. N5's "physical-clock-admission ray" is not a missing DATUM but a missing READOUT-CONTEXT — and Record already requires a supplied readout context, so the admission is the context-choice the axiom already brackets, not a new (L_s−1) parameter.** | Boundary moved: *selector vs admissible dial*. The campaign calls the `(L_s−1)`-parameter admission ray "a missing supplier A_min does not fix." But Record's own text: "A record supplies no **readout context**, decomposition…" — i.e. the readout context is a *bracketed input*, not a *derivation target*. | The "second clock" question becomes: given a readout context (which Record already says must be supplied), is the clock unique *relative to that context*? Stone uniqueness is already "transfer-relative." Add "context-relative" and the admission ray is the context, not an undischarged number. This makes N5 *context-conditional*, paralleling how N2/N4 are *transfer-conditional* — a uniform honest shape, not a special wall. | Must show the readout-context choice and the clock-ray choice are the SAME object (a (L_s−1)-parameter family on both sides). If the readout context has fewer/more parameters than the clock ray, they are not identifiable and B2 fails. | **Context = clock-ray identification:** prove the finite central-sector decomposition (readout context, Record-bracketed) and the positive clock-ray in `span_{≥0}{n_p}` are in bijection. If so, N5 is not "A_min fails to supply a clock" but "Record brackets the readout context, and the clock is unique given it" — exactly the honest conditional shape, and it removes N5 from the "emergent-dynamics gate" and puts it under the *already-granted* Record readout-context bracket. | Parameter-count both: (i) dimension of the space of finite central-sector decompositions compatible with the K/CPT conjugation on the staggered surface; (ii) dimension of the positive clock-ray family `span_{≥0}{n_p}` = L_s−1 (boundary, simplex). If (i)=(ii)=L_s−1 and the map is a bijection, the identification holds. Pure linear-algebra/convex-geometry check; build on the N5 runner. |

### C. The N2b / units frame (stress-test of misframing (c))

| Reframe | What moves | Simpler | Harder | New route opened | First decisive test |
|---|---|---|---|---|---|
| **C1. N2b is PURELY the already-granted scale-reference primitive (prompt hypothesis (c)) — the campaign's "no A_min observable carries 1/time units" IS the scale-reference primitive's reason-for-existence, so N2b is not a wall but a citation to an approved premise.** | Boundary moved: *obstruction vs missing input → already-granted input*. The campaign's sharpened N2b reason: "no A_min observable returns a unit-bearing 1/time number." The scale-reference primitive note says verbatim: "The framework baseline … carries no dimensionful number … its physical unit is undetermined until one dimensionful reference is supplied." These are the SAME statement. | N2b stops being an open clause. The absolute clock unit `a_τ` is fixed *by the same units conversion `a^{−1}=M_Pl` already granted at primitive grade*. `a_τ` (a length/time in lattice units) × the scale reference = a physical time. There is no *additional* missing supplier; N2b's residual is discharged by an approved primitive that "chain-satisfies without bounding." | Must show `a_τ` is dimensionally the SAME scale as the spatial lattice spacing `a` (so the ONE scale reference covers it), NOT an independent second dimensionful number. If the time-block spacing `a_τ` and the spatial spacing `a` are independent dimensionful numbers, the single scale reference covers only one and N2b needs a *ratio* `a_τ/a` — which is exactly what `kinetic_isotropy_primitive` (c_t=c_s) supplies. | **Two-primitive closure of N2b:** N2b = (scale_reference fixes the one dimensionful anchor) + (kinetic_isotropy fixes the dimensionless ratio `a_τ/a` via c_t=c_s). Both are APPROVED primitives that chain-satisfy. If `a_τ` decomposes as `a_τ = (a_τ/a)·a` with the ratio from kinetic-isotropy and `a` from scale-reference, then N2b is closed by two already-granted premises with NO new axiom — the campaign missed this because R-N2b-JOINT used only the rate gates, never the two primitives. | Symbolically verify: under the joint rescaling `a_τ→c·a_τ, Ĥ→Ĥ/c` (the campaign's gauge), does fixing BOTH (the kinetic-form ratio c_t/c_s=1, dimensionless) AND (the scale reference a^{−1}=M_Pl, the one unit) leave any residual freedom in `a_τ`? The campaign's gauge orbit is 1-parameter (`c`). kinetic-isotropy fixes the dimensionless part; scale-reference fixes the dimensionful part. Two constraints on a 1-parameter gauge ⇒ generically rigid. Test whether c_t=c_s + a^{−1}=M_Pl jointly pin `c`. Build on `single_clock_n2b_joint_clock_unit_check_2026_06_20.py`, ADDING the kinetic-isotropy ratio leg and the scale-reference leg the campaign omitted. |
| **C2. N2b is a value-availability question masquerading as a value-derivation question — the framework only ever needs `a_τ` to be *available* (a supplied reference), never *derived*, and "availability" is precisely what a primitive grants.** | Boundary moved: *value derivation vs value availability*. The exercise skill explicitly lists this boundary. The campaign demands `a_τ` be DERIVED (and proves it can't be). But the keystone only needs `a_τ` *supplied/available* to write `H=−(1/2a_τ)log T̂²`. | Reframes the entire N2b "wall" as a category error: deriving a dimensionful unit from dimensionless structure is *provably impossible by dimensional analysis* (the scale-reference note says exactly this: "irreducible by dimensional analysis"). So N2b-as-derivation is not a framework gap — it is a theorem that no theory can do it. The honest status is "available via primitive," and that is already granted. | Must ensure no DOWNSTREAM claim secretly needs `a_τ` *derived* (e.g. a mass-in-seconds prediction with no free scale). If a downstream row claims a dimensionful prediction with zero scale inputs, it is overclaiming regardless of N2b's frame. | **N2b → demote-to-non-wall:** reclassify N2b from "open clause of B-AXIS" to "discharged by scale_reference_primitive (units) — not a derivation target," exactly as `tier_a_admissions.json` already did for the scale reference itself ("the scale reference a^-1 is likewise not a Tier-A admission"). N2b should follow the same path: it is the time-component of the one granted unit. | Confirm the keystone's `1/(2a_τ)` is the ONLY place `a_τ` enters and that every downstream consumer uses only dimensionless ratios of it (the campaign's own [τ-RESCALE] shows all observables are c-invariant ⇒ every downstream number is already dimensionless ⇒ none needs `a_τ` derived). If so, N2b is a non-wall by the campaign's OWN computation. Grep the 959 cone for any dimensionful (1/time-carrying) downstream claim; if none, N2b is closed-as-units. |

### D. Cross-cutting reframes (from combining A/B/C)

| Reframe | What moves | Simpler | Harder | New route opened | First decisive test |
|---|---|---|---|---|---|
| **D1. The wall is mis-decomposed: N2b+N4 are BOTH already discharged by approved primitives (scale-reference + kinetic-isotropy), leaving N5 as the SOLE genuine residual.** | Boundary moved: *obstruction vs missing input*, applied to the whole B-AXIS triple. The campaign's "all three funnel to one emergent-dynamics gate" is replaced by "two are primitive-granted; one (N5) is the real open piece." | Dramatically narrows the wall: instead of a 3-clause obstruction relocating to a giant open gate, it is ONE clause (N5: which commuting factor is the clock) plus orientation (past hypothesis, already a separate residual). The keystone could go from "3 undischarged premises" to "1." | The two primitive-discharges (A1/C1) must both survive their first tests. If either kinetic-isotropy-fixes-the-axis (A1) or scale+isotropy-fix-the-unit (C1) fails, D1 weakens. N5 (B1/B2) must then carry more weight. | **Re-scope the keystone's B-AXIS premise** from {N2,N4,N5} to {N5 + orientation}, with N2b cited to scale_reference + kinetic_isotropy and N4 cited to kinetic_isotropy's 1+3 partition. This is a *reframe that makes most of B-AXIS unnecessary* — the highest-value outcome the exercise allows short of a full proof. | Run A1 + C1 tests first (both are existing-runner extensions). If both crack, draft a keystone re-scope note: B-AXIS = N5-admission + past-hypothesis-orientation only; N2/N4 discharged by approved primitives (no new axiom). Then N5 via B1/B2. |
| **D2. Pre-record vs recorded: the entire B-AXIS construction is being read off the PRE-record transfer T̂², but the framework's only physical-content axiom is RECORD — so the wall may dissolve if read off the record-production layer instead of the transfer.** | Boundary moved: *pre-record vs recorded* (the exercise's first listed boundary) AND *reading dynamics off T̂ vs the generator* (a leaned-on assumption in EXERCISE.md). | If the time axis / clock / unit are properties of the RECORD-PRODUCTION process (which is where the arrow already lives, per the past-hypothesis note), not of the pre-record Euclidean transfer, then the W/S₄ symmetry of the *pre-record* surface is simply irrelevant to N4 — it is symmetry of the wrong object. | Record-production dynamics is an EXPLICIT OPEN GATE (no A_min derivation). So reading the axis off records cannot be a *closed* derivation today. But it could *relocate* the wall to a place where the symmetry argument no longer applies — and the arrow note shows record-production DOES break time-reflection (via the past hypothesis). | **Record-production axis selection:** does the record-production map (redundant pointer broadcast, per the arrow note's explicit model) single out a direction that the pre-record W does NOT transport? The arrow note already shows record monotonicity picks an orientation from the boundary. The new question: does it ALSO pick the axis (not just orientation)? If pointer-broadcast is intrinsically along the evolution direction, the record layer selects the axis where the pre-record transfer cannot. | Extend the arrow note's 6-qubit redundant-broadcast model: check whether the record-production generator `H_k=(π/2)|1⟩⟨1|⊗X_k` is W-transportable. The campaign's R-N4-REGDIR found A_min record-ACCUMULATION is a W-invariant ball; but it tested accumulation, NOT the broadcast *direction*. Test whether the pointer-broadcast *channel* (not the monotone) has a W-covariant image or breaks W intrinsically. Reuse `frontier_arrow_from_record_formation_2026_06_05.py`. |

---

## 2. Most promising new vector (single highest-value)

**Reframe A1 / D1: N4 is discharged by the approved `kinetic_isotropy_primitive`'s
1+3 partition, not "outside A_min."** The campaign's entire N4 no-go rests on
computing S₄-transitivity of the **bare** staggered surface. But `kinetic_isotropy`
is an approved premise node (chain-satisfies without bounding) that *presupposes a
1+3 time/space split* (it equalizes c_t and c_s — a statement that requires a
distinguished t). The stabilizer of a 1+3 partition is S₃-fixing-one — precisely the
"one-axis-selecting" structure the N4 steelman (E7) concluded only a non-A_min
boundary datum could provide. The SPATIAL_CUBIC gate **already proves** the anisotropic
kinetic form `c_t p_τ² + c_s|p_s|²` "fails a time-space swap" (W is broken by the
kinetic form whenever the partition is present), and that O_h *alone* leaves exactly a
2-coefficient invariant space — i.e. the partition is O_h-structural, sitting BELOW the
c_t=c_s choice. The campaign never ran the N4 automorphism computation on the
primitive-enriched (anisotropic-kinetic-form-decorated) surface; it only tested BC
data, reality grading, Laplacian, etc. (E1–E8). **The decisive test is a direct
extension of an existing runner** (`single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`):
add the kinetic quadratic form `Q(p)` as enrichment E9 and compute the joint
stabilizer's axis-image. If it is S₃-fixing-the-time-block, N4-as-label-block is
discharged by an approved premise with no new axiom — a genuine crack. This is the
highest value because it (a) is runnable today on an existing surface, (b) challenges
the load-bearing "outside A_min" classification directly, (c) uses only already-approved
content, and (d) if it holds, collapses two of the three B-AXIS clauses (with C1
handling N2b), leaving N5 as the sole residual (D1).

## 3. What NOT to do next (anti-recommendations)

- **Do NOT** re-run any E1–E8 enrichment, OS/GNS, durability, registration-cone,
  KMS/APBC, Wilson-gauge, anomaly/chirality, or per-axis-Z₂-BC route — all are pruned
  in the NO_GO_LEDGER with residual-0 W-transport. The new vectors deliberately avoid
  every bare-surface enrichment.
- **Do NOT** rebuild the N5 commuting-factor countermodel (T_A⊗I etc.) or re-assert
  "T̂² is maximally factorized" — that is settled. B1/B2 attack a DIFFERENT axis (is
  the factor record central-sector or within-sector), which the existing runner never
  checked.
- **Do NOT** attempt to DERIVE a dimensionful `a_τ` from dimensionless structure
  (C2 shows this is impossible by dimensional analysis — the scale-reference note says
  so verbatim). The move is to cite the primitive, not to defeat the gauge.
- **Do NOT** treat the kinetic-isotropy primitive as supplying dynamics, a Lorentz
  theorem, a spacing-ratio theorem, or an absolute scale — its note and the registry
  forbid this. A1/C1 use ONLY its 1+3 partition structure and its dimensionless ratio,
  which is exactly what it grants.
- **Do NOT** claim closure. Every reframe above is a ROUTE with a first test, not a
  result. The honest deliverable is a sharper attack map: N4 and N2b may be
  primitive-granted (run A1, C1), N5 may be within-sector/context-bracketed (run B1, B2),
  and the genuinely-open piece may shrink to N5 + orientation (D1). No audit verdict,
  no new axiom, no proof is asserted here.

## 4. One-paragraph synthesis

The campaign proved the bare staggered-Dirac surface is S₄-symmetric (no axis label),
maximally factorized (no forced single clock), and scale-gauge (no absolute unit), then
funneled all three residuals to one emergent-dynamics open gate and called the native
one-parameter-group reframe "honest but not fewer admissions." The reframing slice
finds the leak in that conclusion: the wall was computed on the **bare** carrier while
the framework actually grants two **approved primitives** the computation ignored —
`kinetic_isotropy_primitive` (which presupposes a 1+3 time/space split, whose
partition-stabilizer is exactly the S₃-fixes-one axis-selector the N4 steelman sought)
and `scale_reference_primitive` (whose entire purpose is to supply the one dimensionful
unit N2b says is missing). So N4 may be a representation artifact of the Euclidean-4-torus
presentation discharged by the kinetic-isotropy partition (Reframe A1), N2b may be the
already-granted units conversion plus the kinetic-isotropy ratio (Reframe C1), and the
genuinely-open residual may shrink to N5 — which itself may be a within-sector-vs-central-sector
readout distinction the Record axiom explicitly brackets (Reframes B1/B2). The single
highest-value move is to recompute the existing N4 automorphism runner on the
anisotropic-kinetic-form-enriched surface (E9): if the joint stabilizer fixes the time
block, two of three B-AXIS clauses fall to approved premises with no new axiom (D1),
leaving N5 + past-hypothesis orientation as the only live residual. None of this is a
closure; it is a concrete, runnable re-attack that challenges the load-bearing
"outside A_min" and "one undivided emergent-dynamics gate" framings the campaign
treated as settled.
