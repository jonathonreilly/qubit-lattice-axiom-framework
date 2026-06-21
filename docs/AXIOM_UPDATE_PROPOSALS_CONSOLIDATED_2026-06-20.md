# Axiom-Update Proposals — Consolidated Set (block01, 2026-06-20)

**Date:** 2026-06-20
**Type:** meta / governance proposal (FOR the owner's governance decision — adopts nothing)
**Lane / branch:** `axiom-update-proposals`,
`physics-loop/axiom-update-proposals-block01-20260620`.
**Status authority:** the independent audit lane / owner is the **sole** status
authority. This note sets **no** audit verdict, promotes **no** axiom, and edits
**no** axiom registry. It consolidates three candidate axiom-update proposals and
the no-new-axiom cracks found en route, FOR an external governance decision.

> **`hypothetical_axiom_status` (carried throughout):** *"conditional on accepted
> new axiom; not retained on the actual current surface."* Every "discharges" /
> derivation claim attached to a candidate primitive below is a consequence of an
> **UNADOPTED** primitive. This labelling does **not** promote the primitive; only
> an external owner / governance decision can
> (`docs/audit/AXIOM_MINIMALITY_POLICY.md` §1/§4/§6). No bare
> `retained` / `promoted` appears anywhere in this note.

```yaml
proposal_allowed: false   # owner governance decision required; this note REQUESTS it, does not make it
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
```

---

## 0. What this consolidates

The owner authorized going beyond the no-new-axiom rule to deliver **either**
new no-new-axiom derivations **or** axiom-update PROPOSALS ("don't believe the
no-gos; keep working until we have a set of new derivations or update proposals
for the axioms"). Per the physics-loop posture, every wall got a **genuine
skeptical no-new-axiom re-attack FIRST**; only the residual that still walls was
escalated to a candidate primitive, always the **weakest sufficient** one,
maximizing fanout-unlocked per unit of axiom strength.

Nine walled high/medium-fanout bridges from four campaigns —

- **single-clock B-AXIS** (N2b clock unit, N4 axis label, N5 second clock; ~959),
- **anomaly ABJ** (P-HY, P-COMP, P-REC, P-ABJ; ~1105),
- **Koide** `r=1/2` (equal-block measure + objectivity selector; ~1 direct,
  stack-shared), and
- **observable-principle** (T1-d det-readout identification + FS statistics
  frame; ~909) —

collapse onto exactly **THREE** open gates from
`docs/MINIMAL_AXIOMS_2026-06-05.md`, hence three candidate axiom additions. Each
lands in a gate the memo **already declares outside axiom content**, so each is
**new content in a named open gate, not a reword of an existing axiom** (which
`AXIOM_MINIMALITY_POLICY.md` §1 forbids), recorded as an "unmade science-level
decision" per §1/§4.

**Component deliverables (the deep-dive notes this consolidates):**

| Cluster | Candidate primitive | Proposal note | Runner | TOTAL |
|---|---|---|---|---|
| **C1** Record-Production / Decoherence Dynamics | **(RP-DYN)** | `docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md` | `scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py` | **PASS=34 FAIL=0** |
| **C2** Readout-Context / Objectivity / Sector-Measure | **(READOUT-MEASURE)** | `docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md` | `scripts/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.py` | **PASS=41 FAIL=0** |
| **C3** Gauge-Content / Particle-Content | **(PIN-GAUGE-CONTENT)** | `docs/AXIOM_UPDATE_PROPOSAL_GAUGE_CONTENT_2026-06-20.md` | `scripts/axiom_update_proposal_gauge_content_2026_06_20.py` | **PASS=21 FAIL=0** |
| (map) | wall→gate verification | `.claude/science/physics-loops/axiom-update-proposals/WALL_TO_GATE_MAP.md` | `logs/runner-cache/axiom_update_proposals_wall_to_gate_runner_2026_06_20.py` | **PASS=32 FAIL=0** |

**Aggregate runner result: 34 + 41 + 21 + 32 = 128 checks, FAIL=0.** All four
runners reproduce deterministically (re-run 2026-06-20; numpy + stdlib only; no
empirical import in any load-bearing leg).

**Sourcing caveat (carried from the map).** The exact `…2026-06-20` campaign
notes and exercise packets named in the task prompt
(`SINGLE_CLOCK_BAXIS_…_NO_GO_NOTE`, `ANOMALY_FORCES_TIME_ABJ_…_NOTE`,
`KOIDE_RECORDS_OBJECTIVITY_DERIVATION_ATTEMPT_NOTE`, the OWNER_DECISION_PACKETs,
FRONTIER_RAYS, and `.claude/science/exercises/{baxis-wall-break,abj-walls-break}/`)
**do not exist in this checkout** (verified by exhaustive `find`). The
proposals are reconstructed directly from the **landed** campaign no_go /
bounded-theorem notes that DO exist and that already name the supplier shapes and
gates verbatim. Fanouts are cross-checked against
`docs/audit/data/load_bearing_summary.json` `transitive_descendants`.

---

## 1. The current surface (what the proposals add to)

`A_min` = {**Lattice**, **Quantum**, **Record**} (`MINIMAL_AXIOMS_2026-06-05.md`).
Approved framework primitives = {`scale_reference` (2026-06-04), `kinetic_isotropy`
(2026-06-09), `realized_state` (2026-06-11, Tier-A)}. The memo's **OPEN GATES**
list (explicitly outside axiom content):

1. arrow / measurement / decoherence / record-production dynamics — **largest open gate**;
2. readout context / sector measure / objectivity / occupancy;
3. gauge group / particle content / species;
4. P2 / modulus / log-det;
5. source / action.

Each candidate below sinks into exactly one of gates 1–3 (with gates 4–5 shown to
be largely **theorems** or **sub-clauses** of those, per the cracks in §3).

---

## 2. The three candidate axiom-update proposals (the minimal set)

Each subsection gives: the precise candidate statement; the walls it discharges
(+ fanout); the conditional derivation + runner PASS/FAIL; minimality (what it
does and does **not** grant); falsifiers; and tensions/consistency with retained
no-gos.

### 2.1 CLUSTER 1 — Record-Production / Decoherence-Dynamics primitive (RP-DYN)

> **Candidate (RP-DYN) — UNADOPTED.** There exists a single completely-positive
> trace-preserving (CPTP) **record-production generator** `L` — a one-parameter
> CPTP semigroup `Φ_t = e^{tL}`, `t ≥ 0`, on system ⊗ environment — together with
> a **record-monotone** functional `R` (non-decreasing along the semigroup) and an
> **orientation**, such that for the realized state pointer-basis coherence is
> monotonically suppressed (einselection) and a durable record forms. The
> **registration direction** (which lattice axis carries the produced event order)
> is **this same object**. It asserts **existence + orientation only** — a *slot*
> (the dynamics-gate analogue of `realized_state_primitive`), not *content*
> (no kernel, rate, weight, or boundary state).

**Gate:** arrow / measurement / decoherence / record-production dynamics (the
memo's largest open gate).

**Walls discharged (conditional; runner tags in `…dynamics_cluster…py`):**

| Wall | Discharge given (RP-DYN) | Runner witness |
|---|---|---|
| **record-formation floor** | `\|coh\| → 0` monotonically in #env copies ⇒ durable broadcast record (einselection / Quantum Darwinism) | `\|coh\|(N=1,2,4,16,64) → 0` |
| **B-AXIS N4** (axis label) | the registration direction **is** the produced event-order axis = the **PIN-REG** record-shaped pin the axis-selection no_go names | BC-asymmetry breaks `W` exactly (`8.0`); symmetric BC restores (`0`); relabeling-invariant kernel-dim discriminator (`0` vs `2`) |
| **B-AXIS N5** (one clock) | one generator ⇒ one monotone record order even across two commuting factors ⇒ a single production clock | joint `\|coh\|` monotone under one `L` |
| **B-AXIS N2b-step** (rate exists) | `L` carries a rate `γ` ⇒ a well-defined record half-life (the **dynamics-side** existence of a tick) | well-defined half-life for fixed `γ` |
| **arrow** (existence as a direction) | `R` non-decreasing along `e^{tL}`; orientation = arrow direction; a unitary step has no monotone | record proxy monotone up vs reversibility contrast |

**Fanout unlocked:** the record-formation floor (transitively large; the dynamics
floor sits under B-AXIS-N4 + Koide objectivity + T1-d) **+ ~959** (B-AXIS via the
registration-direction route, which then gates the anomaly cap path,
`anomaly_forces_time_theorem` td = 1049).

**Conditional derivation + runner:** **TOTAL: PASS=34 FAIL=0.** The runner
recomputes the genuine `W`-exchange baseline (periodic surface exactly
`W`-invariant, residual `0`; plain swap fails by `11.3`), the skeptical crack
(chirality `ε` and `{D_hop, ε}` exactly `W`-invariant ⇒ the anomaly chain is
axis-label-blind), the un-cracked walls (`‖H_prod − H_sum‖ = 4.4e-16`,
`[H_A,H_B]=0` for N5; `T` fixes only `τ·H` for N2b), the record-formation floor
(`H=0`/decoupled/eigenstate keep `\|coh\|=0.5`), and the five conditional
discharges with their falsification legs. Every conditional line carries
`hypothetical_axiom_status`.

**Minimality — does NOT grant:** a **past hypothesis** / low-entropy boundary
(the arrow's *sign* stays open — a strictly stronger input
`realized_state_primitive` forbids); any kernel / Kraus map / rate / weight;
**Born weights / probability / normalization** (those live in C2); the
**dimensionful** tick value `2a_τ` (SK-1: `scale_reference × kinetic_isotropy`);
a fourth spatial dimension; the exclusion of commuting algebra in general
(scope-boundary N6 — gauge/redundant tensor factors — stays open; RP-DYN excludes
only a *second record-producing* stream). **Strength: WEAK** (existence of
einselecting dynamics; weaker than a past hypothesis).

**Falsifiers:** a no-new-axiom derivation of record-production existence from
Lattice+Quantum+Record (would moot it); a large-fanout consumer that needs the
axis **label** (not just the count `d_t`) — weakens §3's N4-label crack; failure
of the symmetric-BC restoration leg; a demonstration that one CPTP generator does
**not** give a single monotone record order across commuting factors (breaks N5);
any demonstration that RP-DYN smuggles a weight/probability (breaks minimality).

**Consistency with retained no-gos:** additive, contradicts none. It supplies the
imports the boundaries name as missing — scope-boundary N4 (construction, via the
registration direction) + N5; the axis-selection no_go's **PIN-REG**; the
record-formation no_go's "separate record-production / decoherence model" (its N6
partial-closure path). Consistent with `realized_state_primitive` (supplies the
dynamics slot evaluated at the realized state; no state/measure/typicality). No
boost / Lorentz / SO(4) content touched.

### 2.2 CLUSTER 2 — Readout-Context / Objectivity / Sector-Measure primitive (READOUT-MEASURE)

> **Candidate (READOUT-MEASURE) — UNADOPTED.** A supplied readout context's
> central-sector measure assigns **one statistical slot per irreducible record
> OUTCOME** (`K`/CPT orbit / irreducible Dirac–record factor), **not** per
> central-sector real component; equivalently the physical readout criterion is
> **maximum objective information over the objective outcome alphabet** (count
> `K`-real outcome **labels** / atom-share, not Born/rank/dimension weight); and
> the scalar readout of a sector is one objective scalar of that sector (the
> determinant character on the matter block), with disjoint outcomes registering
> as disjoint records. **In one line: a record counts OUTCOMES, not components.**

**Gate:** readout context / sector measure / objectivity / occupancy.

**Walls discharged (conditional; runner tags R1–R5 in `…readout_context…py`):**

| Wall | Discharge given (READOUT-MEASURE) | Fanout |
|---|---|---|
| **R1** Koide `r=1/2` equal-block measure | equal-block `(1,1)` face ⇒ free ratio `t = w_p/w_s = 1` ⇒ `r* = 1/2` ⇒ `Q = 2/3` (exact) | ~1 direct + koide cone (`charged_lepton_koide_cone_…` td = 327) |
| **R2** Koide `r=1/2` objectivity selector | max-objective-information over 2 labels ⇒ uniform `(1/2,1/2)` ⇒ `r=1/2`; **coincides with R1's `t=1`** | shared koide/flavor readout stack |
| **R3** `W_t`-independence countermodel | the einselection fixed point gives `t=2` (`r=1`), so a **Cluster-1 dynamics axiom does NOT pin the measure** ⇒ a readout-context measure primitive is **exactly** the missing `t=1` pin | demarcation (no extra fanout; fixes minimal content) |
| **R4** observable T1-d det-readout identification | with SKb the det FORM is already a theorem; Record-additivity + the one identification clause ⇒ Cauchy `W(Z₁Z₂)=W(Z₁)+W(Z₂)` ⇒ `W = c log det`, `c=1` | observable identification half of `observable_principle_from_axiom_note` (td = 887) |
| **R5** P-REC single-taste pointer | per-site `γ₅` impossible (`ω = σ₁σ₂σ₃ = iI` central in `M₂(C)`) ⇒ the taste/chirality selector must be a readout-context choice = "one outcome per irreducible Dirac/taste factor" = the same orbit-occupancy choice | shared with anomaly P-REC (C3 supplies the factor *existence*; this supplies only the readout *selection*) |

All five are the **same** binary choice (`t=1` = count outcomes), proved
coincident by the runner's SKc block (two exhibited models `M_sector`
slots/component = 3 ⇒ `r=1`, `M_orbit` slots/outcome = 2 ⇒ `r=1/2`, with the
convention-free occupancy fiber `r_sector/r_orbit = Z_sector/Z_orbit = 2`), so
**one** primitive discharges them.

**Fanout unlocked:** ~1 (Koide direct) + the koide cone (327) + the observable
identification half of 887 + the flavor/CKM-vs-PMNS readout-context rows.

**Conditional derivation + runner:** **TOTAL: PASS=41 FAIL=0.** Lever (landed, no
axiom): `Q = (1+2r)/3`, capacity max `r* = w_p/(2 w_s)`, the maximizer a
continuous function of the FREE ratio `t` (closed form checked vs numeric argmax
at five weight pairs; the two-block pointer fixes #terms = 2, never `t`).
Conditional on the candidate, its faces pin `t=1` ⇒ `r=1/2`, `Q=2/3` (R1/R2); the
contrasting rank/Born `(1,2)` face gives `t=2`, `r=1`, `Q=1` (non-vacuous,
falsifiable); R3 shows the einselection route lands at `t=2`; R4's Cauchy
residual is `4e-16`; R5's exhaustive search finds no on-site anticommutant of the
Pauli triple. Every conditional line carries `hypothetical_axiom_status`.

**Minimality — does NOT grant:** any weight, probability, Born rule,
normalization constant, mixing angle, CP phase `δ` (separate radian-period
admission), mass value; record-PRODUCTION / decoherence dynamics (C1 — and R3
shows those would give the *wrong* value `t=2`); gauge/particle content (C3 — the
*existence* of the irreducible Dirac factor whose outcome R5 selects). Outputs are
exact fractions (`Q ∈ {2/3, 1}`); no fitted number enters. Folds the Koide
conditional note's "two independent inputs" (its N2) into ONE
(atom-share = label-count, runner-verified) — the **SK-4** minimality crack.
**Strength: WEAK–MEDIUM** (a readout criterion; supplies no weights/probabilities/
normalization). Same *category* as the approved `kinetic_isotropy_primitive`
(dimensionless, structural, binary, no fitted number).

**Falsifiers:** a no-new-axiom derivation of `t=1` from the current surface
(would make it unnecessary); the einselection fixed point shown to give `t=1`
(would make C1 sufficient, this redundant); the five faces shown genuinely
independent (breaks "one minimal choice"); a sharpened charged-lepton `Q`
materially off `2/3`; SKb overturned (det form not a theorem after all).

**Consistency with retained no-gos:** none in tension. Every retained no_go in
scope asserts the measure is **not forced**, never **impossible/forbidden**;
several explicitly name the indifference / atom-share rule as a coherent possible
extra principle. Specifically: `FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02`
(N6/N7 name exactly this principle); `KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31`
(its N6 "does not call for a new axiom" leaves the door open);
`KOIDE_ORBIT_OCCUPANCY_…_2026-06-09` (the candidate **is** its stated unadopted
orbit-occupancy premise, same `ξ=1`, same factor-2 fiber);
`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02` (the candidate **respects** it —
places the selector in the readout context precisely because it cannot be
on-site); the Record non-supply clause (the candidate supplies the
occupancy/measure rule Record verbatim declines to supply, as a separate recorded
decision — not a reword).

### 2.3 CLUSTER 3 — Gauge-Content / Particle-Content primitive (PIN-GAUGE-CONTENT)

> **Candidate (PIN-GAUGE-CONTENT) — UNADOPTED.** The emergent matter sector is a
> **gauged chiral gauge theory** with **(i) [P-HY]** the canonical traceless
> `u(1)` eigen-direction `Y_like` supplied by the graph-first construction
> (`NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_…`) **is a gauged `U(1)`** of the
> emergent theory (dynamical, not a global label); and **(ii) [P-COMP]** the matter
> carrier is completed by an **opposite-chirality (right-handed) SU(2)-singlet
> template** — chirality **stipulated** to be opposite to the LH doublet content
> (the chiral completion, **not** the vector-like CPT mirror), neutral singlet
> `Y_{νR}=0`. **Splittable** into P-HY-gauging (i) and P-COMP-chirality (ii).

**Gate:** gauge group / particle content / species (+ source/action when the FS
statistics sub-clause is folded in — see §3 SK-3).

**Walls discharged (conditional; runner tags B1–B4 in `…gauge_content…py`):**

| Wall | Discharged by | Fanout unlocked |
|---|---|---|
| **P-HY** (`Y_like` is gauged) | PIN-GAUGE-CONTENT clause (i) | the gauge-content half of `anomaly_forces_time_theorem` (td = 1049); the abelian/charge half of the native-gauge matter cone (`native_gauge_closure_note` td = 1361) |
| **P-COMP** (opposite-chirality RH-template existence) | PIN-GAUGE-CONTENT clause (ii) | the completion/chirality half of `anomaly_forces_time_theorem`; the one-generation matter-content cone (RH singlet template ⇒ electric-charge set downstream) |

Together these gate `d_t = 1` / signature `(3,1)` and the one-generation matter
cone — the **highest-fanout** cluster of the three. The sibling premises **P-ABJ**
(route (c), SK-2), **P-REC** (taste selector — readout-selection half lives in C2,
factor existence here), and the inherited **B-AXIS** cap (C1) remain; this cluster
discharges the two content predicates it can clear cleanly while showing the
lower-bound half follows. The **observable FS** spin-statistics premise (fermion-
parity superselection / graded locality) is the natural same-gate sub-clause that
discharges the realization half of observable P2 (`Z_matter[J] = det(D+J)`).

**Conditional derivation + runner:** **TOTAL: PASS=21 FAIL=0** (HALF A = skeptical
no-new-axiom re-attack: 4 gauging discriminators blind, 2 vector-like traps,
LH-only anomalous; HALF B = conditional discharge; 3 falsification legs). Banked
exact identities re-verified conditionally:

```text
(i) Y_like gauged => the three LH anomaly traces (Tr[Y^3]=-16/9, Tr[SU3^2 Y]=+1/3,
    SU3^3=+2) are GAUGE anomalies => their nonvanishing is an inconsistency
    (with the sibling P-ABJ implication) => a completion is MANDATORY.
(ii) opposite-chirality RH SU(2)-singlet template => the completion is the CHIRAL
     template (not the vector-like CPT mirror) => a genuine 2nd chirality class
     exists; its banked SHIFT closed form cancels all six conditions exactly
     (SM branch (4/3,-2/3,-2,0) at n_color=3, existence witness);
=> [retained EVEN Clifford theorem CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_…]
   d_s + d_t even; with d_s = 3, d_t ODD => d_t >= 1.
Intersect single-clock cap d_t <= 1 (B-AXIS / Cluster 1) => d_t = 1, signature (3,1).
```

B1: chiral RH template `(4/3,-2/3,-2,0)` cancels all six conditions exactly
(`Tr[Y]=Tr[Y³]=Tr[SU3²Y]=Tr[SU2²Y]=SU3³=0`, Witten even). B2: full content
genuinely chiral (spectrum ≠ CPT conjugate; ≠ inert mirror). B3: SHIFT closed form
parametric in `n_color` (`Y_{uR}+Y_{dR}=2a` for all `nc`); `n_color=3` returns the
witness. B4: gauging makes cancellation a consistency demand + the EVEN theorem
`d_t`-odd lower bound. Every conditional line carries `hypothetical_axiom_status`.

> **Runner caught real bugs (load-bearing-residual pattern held).** The gauge
> runner's first draft had four logic errors — an incorrect self-conjugacy
> vectorization in gauging discriminator #4 and a sign-convention error in the
> CPT-mirror encoding affecting A2/F3 — fixed by switching to an unambiguous
> all-left-handed-frame anomaly encoding and a correct intertwiner test. This is
> the documented runner-exposes-load-bearing-residuals pattern.

**Minimality — the chirality word is load-bearing.** Falsification leg **F3**:
the naive CPT-mirror completion cancels all six anomalies but is chirally **inert**
(vector-like) ⇒ **no** `d_t`-odd lower bound. A primitive asserting only "a
completion exists" would be satisfied by the inert mirror, so "opposite-chirality"
**cannot be dropped**. **Does NOT grant:** the RH hypercharge *values* (forced by
the SHIFT relation, banked exactly as
`ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_…` / `RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES_…`
— the primitive supplies only the template *class*); the `e_R ↔ ν_R` branch
(named discrete convention, F2); `n_color=3` (graph-first SU(3) lane); generation
count; the non-abelian content (already retained in `NATIVE_GAUGE_CLOSURE_NOTE.md`);
P-ABJ (sibling, SK-2-crackable); any coupling/mass/mixing. **Strength: HEAVY**
(asserts gauge content + chirality template, explicitly outside Quantum's text;
splittable into P-HY-gauging / P-COMP-chirality / (folded) FS).

**Falsifiers:** F1 a wrong completion (`Y_{νR}=1` keeping `e_R`) FAILS cancellation
(`Tr[Y]=-1`, `Tr[Y³]=-1`); F2 the `e_R ↔ ν_R` relabelling is the **only** other
consistent branch (a convention, not a second axiom); F3 the vector-like mirror is
chirally inert (why chirality must be stipulated). Broader: a fifth gauging
discriminator selecting is-gauged from the current surface would crack P-HY; the
SK-2 imbalanced-complex route closing P-ABJ would remove the consistency-demand
dependence on the P-ABJ premise.

**Consistency with retained no-gos:** no collision with any retained result.
`NO_PER_SITE_CHIRALITY_THEOREM_2026-05-02` (chirality on the taste-reconstructed
Dirac factor, not per-site); `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_2026-05-30`
(content/chirality template, not the lattice index route);
`REGISTRATION_REINSTATES_CHIRALITY_NO_GO_2026-06-07` (chirality via gauge-content
primitive, **not** via Record — which is *why* a separate primitive is the
vehicle); `FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE_…_2026-06-08` (orthogonal: that is
the generation-sector orientation `Z₂`; this is the matter-content chirality `Z₂`,
a distinct object per `CHIRAL_CONTENT_IS_THE_EPSILON_D_CHIRALITY_IMPORT_…_2026-06-08`).

---

## 3. No-new-axiom CRACKS found en route (HIGHER VALUE than proposals)

Per "don't believe the no-gos," the skeptical re-attacks are reported first-class.
A crack is a **new derivation** (no axiom), strictly more valuable than a
proposal. The exercise has precedent: two over-strong B-AXIS no_gos were already
corrected. Here the re-attacks split into genuine cracks (✅) and walls that
**survive** the attack (⛔ — honestly reported, so the proposals are only for true
residuals).

| Tag | Target wall | Re-attack | Outcome |
|---|---|---|---|
| **N4-LABEL** | B-AXIS N4 axis label (for the ~959 fanout) | the ~959 fanout runs through `ANOMALY_FORCES_TIME_THEOREM` (1049), which imports **only the count `d_t ≤ 1`** and is provably **axis-label-blind** (its own non-circularity text); the runner confirms chirality `ε` and `{D_hop, ε}` are **exactly** `W`-invariant (residuals `0`) | ✅ **CRACK (partial, no axiom).** The *axis-label* half of N4 is over-specified for fanout — it is not in the axiom-bearing residual. (The remaining residual — *existence* of record-producing dynamics — does not crack; that is what RP-DYN targets.) |
| **SK-1** | B-AXIS N2b clock unit `2a_τ` | the scope-boundary no_go says `T` fixes only `τ·H`; but `scale_reference_primitive` (`a⁻¹`, approved 2026-06-04) **×** `kinetic_isotropy_primitive` (`c_t=c_s`, approved 2026-06-09) together fix the time-edge spacing relative to the spatial edge | ✅ **CANDIDATE CRACK (no axiom).** `2a_τ` is plausibly **derivable from the already-approved primitive surface**, so N2b is **NOT a fourth cluster**. ACTION before any proposal: derive `2a_τ` from `scale_reference × kinetic_isotropy`. RP-DYN deliberately proposes only the *dynamics-side existence* of a step, never the dimensionful value. |
| **SK-2** | ABJ P-ABJ internal index | the square-block no_go is narrow (its own N1/N5/N7): it kills only the standard `ε`-index on **equal-sublattice EVEN** tori; the runner confirms an **imbalanced/curved** complex (`χ≠0`, 3×3) gives a NONZERO signed heat trace (`A_t = 0.838`); the no_go itself names this as an open positive-retention route | ✅ **CANDIDATE CRACK (no axiom, route (c)).** If the framework's actual emergent complex is imbalanced/curved (**geometry, not an axiom**), P-ABJ route (c) closes with no new axiom and Cluster 3 shrinks. ACTION: check whether the emergent complex is forced balanced-even. |
| **SK-3** | observable T1-d (fanout 909) | the det-vs-trace **FORM** is already a no-new-axiom theorem (`OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_…`): a scalar character multiplicative under composition is `det^k` (`GL(n)` abelianization), and trace **fails** the character property (runner: det multiplicative under composition + direct sum; trace neither) | ✅ **CRACK (no axiom, FORM half).** The 887-descendant fanout of `observable_principle_from_axiom_note` is **NOT** a missing axiom. Only the thin `Z ↔ record` **identification** clause remains, and it is arguably inside Record's finite additivity once the det form is granted (discharged in C2/R4 by the same readout-context primitive). The genuine standalone new-axiom residual in the observable cluster is **only FS** (spin-statistics, folded into C3). |
| **SK-4** | Koide measure vs objectivity "two inputs" | the conditional note's N2 lists atom-share weighting and label-counting objectivity as two independent inputs; the runner shows they **coincide** (atom-share = label-count) | ✅ **CRACK (minimality, no axiom).** It is **ONE** physical choice, not two — folded into C2, shrinking the wall-count. |
| **SKa** | Koide equal-block measure (is a symmetry forcing it?) | tested `U(3)` (⇒ `I/3` ⇒ **rank** `(1/3,2/3)`, `r=1`, breaks equal-block), `K`/CPT (fixes both projectors, no swap — basis only), `Z₃`-equivariance (circulant **commutes** with the grading, `‖[C,P_s]‖=0` — cannot split the orbit) | ⛔ **WALLS (honest contrast).** No `U(3)`/`K`-CPT/`Z₃` symmetry forces the measure; a readout-context premise is genuinely required. (Here the attack **confirms** the wall — the honest difference from the two corrected B-AXIS no_gos.) |
| **P-HY / P-COMP** | the two gauge/content premises | 4 published gauging discriminators reproduced (all blind/one-sided/circular); 2 vector-like traps reproduced (naive CPT-mirror → vector-like; native taste-cube complementation admits a `γ₅=±I` vector-like survivor); LH content alone is anomalous | ⛔ **WALL.** Neither cracks from the current surface; PIN-GAUGE-CONTENT targets exactly this residual. |
| **record-formation floor** | (the dynamics floor) | `H=0` / decoupled / energy-eigenstate are exact baseline-consistent no-record witnesses; Record **verbatim** excludes decoherence dynamics | ⛔ **WALL.** Genuine dynamics floor; RP-DYN targets it. |

**Net of the cracks:** SK-1 likely removes N2b from the proposal set entirely;
SK-2 may shrink Cluster 3 (P-ABJ); SK-3 + SK-4 collapse the observable FORM and
the Koide "two inputs" so the C2 wall is thinner than the headline 909/1 suggests;
N4-LABEL removes the axis label from the axiom-bearing residual. These should be
**attempted (or banked as derivations) before** any governance decision to adopt
an axiom — a crack always beats a proposal.

---

## 4. Ranked coverage map — candidate axiom → total fanout unlocked

Fanout figures are `transitive_descendants` from
`docs/audit/data/load_bearing_summary.json` (cross-checked): `minimal_axioms`
1564, `anomaly_forces_time_theorem` 1049, `native_gauge_closure_note` 1361,
`observable_principle_from_axiom_note` 887, `staggered_dirac_realization_gate`
(=AC_phi_lambda) 927, `charged_lepton_koide_cone_…` 327,
`koide_circulant_q_two_thirds_…` 186. Headline campaign fanouts (B-AXIS 959, ABJ
1105, observable 909, Koide ~1) are consistent with these and used as given.

| Rank (fanout-per-unit-strength) | Candidate (cluster) | Gate | Walls discharged | Total fanout unlocked (approx) | Strength |
|---|---|---|---|---|---|
| **1** | **C1 (RP-DYN)** record-production / decoherence dynamics | arrow / measurement / decoherence / record-production dynamics | record-formation floor; B-AXIS N4 (registration-direction); B-AXIS N5; B-AXIS N2b-step; arrow existence | record floor (transitive) **+ ~959** (B-AXIS → anomaly cap path 1049) | **WEAK** |
| **1** | **C2 (READOUT-MEASURE)** readout-context / objectivity / sector-measure | readout context / sector measure / objectivity / occupancy | Koide r=1/2 measure (R1); Koide r=1/2 objectivity (R2); T1-d det-readout identification (R4); P-REC readout selection (R5); R3 demarcation | **~1** (Koide direct) + koide cone **327** + observable identification half of **887** + flavor readout rows | **WEAK–MEDIUM** |
| **3** | **C3 (PIN-GAUGE-CONTENT)** gauge-content / particle-content | gauge group / particle content / species (+ source/action via FS) | ABJ P-HY; ABJ P-COMP; (folded) FS; feeds P-ABJ(a/b) consistency + P-REC factor existence | **~1049** (anomaly chain) + native-gauge cone **1361** (abelian/charge half) + AC gate **927** (overlapping) | **HEAVY** |

**Fanout-per-unit-strength ranking: C2 ≈ C1 > C3.** C1 and C2 are weak additions
with large transitive reach; C3 unlocks the most but is the strongest addition.

**Grand total fanout addressed by the set.** The walls span the four campaign
cones — B-AXIS ~959, ABJ ~1105, observable ~909, Koide ~1 direct — but these
cones **overlap heavily** (B-AXIS gates into the ABJ/anomaly cap; the AC gate 927
overlaps the gauge cone; the observable FORM is already a theorem and the Koide
"two inputs" are one choice). So the figures are **not additive**. Using the
distinct top-of-cone nodes as the honest envelope:

- **Distinct downstream envelope ≈ 1361** (`native_gauge_closure_note`, the
  largest single cone C3 reaches), with `anomaly_forces_time_theorem` 1049 and
  `observable_principle_from_axiom_note` 887 and the koide cone 327 substantially
  contained within / adjacent — i.e. the set addresses **the upper end of the
  framework's load-bearing graph** (whose root `minimal_axioms` carries 1564 of
  3383 nodes).
- **Naive (overlap-inclusive) sum of headline campaign fanouts ≈ 959 + 1105 + 909
  + 1 = 2974**, reported only as an *upper bound* — the true distinct count is far
  smaller because the cones intersect (and several "walls" are cracked, not
  axiom-bearing).

**Recommended owner sequencing:** adopt the WEAKEST high-leverage first — **C1
then C2** — and **defer C3** (heaviest) until the **SK-2** no-new-axiom crack on
P-ABJ (and the SK-1 / SK-3 cracks) are attempted, since a crack removes the need
for the corresponding axiom strength.

---

## 5. Consistency with retained results (the governance check)

Every candidate is an **addition** in a declared-open gate; **none contradicts a
retained result, and each only ADDS** (verified per proposal note §6/§3.4/§7):

- No retained no_go in scope asserts the discharged target is **impossible** or
  **symmetry-forbidden** — each asserts only **not forced from the current
  surface**. An addition that supplies it is therefore consistent.
- No candidate rewords Lattice / Quantum / Record (policy §1) — each adds content
  the `MINIMAL_AXIOMS_2026-06-05.md` memo declares **outside** axiom content.
- No candidate is adopted in-lane (policy §1 final bullet / §4): each is recorded
  as an **unmade science-level decision**, with approval routed through
  `AXIOM_MINIMALITY_POLICY.md` §6 exactly as `kinetic_isotropy_primitive` was.
- Nothing is written to `docs/audit/data/` (read-only this lane); no
  `axiom_premise_nodes.json` entry is added; no audit verdict is set.

---

## 6. Honest status (audit-lane handoff)

```yaml
proposed_artifact_type: meta / governance proposal (consolidated set)
proposal_allowed: false   # owner governance decision required
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_registry: false
status_authority: independent audit lane / owner only
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
candidate_set:
  - id: RP-DYN
    cluster: C1
    gate: arrow/measurement/decoherence/record-production dynamics
    strength: weak
    runner_total: "PASS=34 FAIL=0"
  - id: READOUT-MEASURE
    cluster: C2
    gate: readout context/sector measure/objectivity/occupancy
    strength: weak-medium
    runner_total: "PASS=41 FAIL=0"
  - id: PIN-GAUGE-CONTENT
    cluster: C3
    gate: gauge group/particle content/species (+ source/action via FS)
    strength: heavy
    runner_total: "PASS=21 FAIL=0"
aggregate_runner_total: "PASS=128 FAIL=0 (34+41+21+32 across four runners)"
no_new_axiom_cracks_to_attempt_first:
  - N4-LABEL (anomaly chain axis-label-blind; partial crack, landed in C1's re-attack)
  - SK-1 (N2b 2a_tau from scale_reference x kinetic_isotropy)
  - SK-2 (P-ABJ route c on imbalanced/curved emergent complex)
  - SK-3 (T1-d det FORM already a theorem; identification arguably inside Record-additivity)
  - SK-4 (Koide measure/objectivity are one physical choice)
recommended_sequence: "C1 then C2 (weak, high-leverage); defer C3 until SK-2/SK-1/SK-3 attempted"
sourcing_caveat: "the exact 2026-06-20 campaign notes/exercise packets named in the task prompt do not exist in this checkout; reconstructed from the landed campaign no_go/bounded-theorem notes that do exist and that name the supplier shapes verbatim"
```

**Not in scope.** Adopting any candidate; deriving any kernel/rate/weight/value;
deriving the arrow's sign (past hypothesis), Born weights, the dimensionful tick
`2a_τ`, `n_color`, generation count, or any coupling/mass/mixing; editing
`docs/audit/data/` or any axiom file; setting any audit verdict.

---

## 7. Component artifacts and load-bearing sources

**Component proposal notes (this consolidates):**
`docs/AXIOM_UPDATE_PROPOSAL_RECORD_PRODUCTION_DYNAMICS_2026-06-20.md`,
`docs/AXIOM_UPDATE_PROPOSAL_READOUT_CONTEXT_OBJECTIVITY_2026-06-20.md`,
`docs/AXIOM_UPDATE_PROPOSAL_GAUGE_CONTENT_2026-06-20.md`.

**Section files / map:**
`.claude/science/physics-loops/axiom-update-proposals/{block01_section_DYNAMICS.md,
block01_section_READOUT.md, block01_section_GAUGE.md, WALL_TO_GATE_MAP.md}`.

**Runners + caches:**
`scripts/axiom_update_record_production_dynamics_cluster_2026_06_20.py`,
`scripts/axiom_update_proposal_readout_context_objectivity_runner_2026_06_20.py`,
`scripts/axiom_update_proposal_gauge_content_2026_06_20.py`,
`logs/runner-cache/axiom_update_proposals_wall_to_gate_runner_2026_06_20.py`
(+ matching `.txt` caches).

**Surface / policy:** `docs/MINIMAL_AXIOMS_2026-06-05.md`,
`docs/audit/AXIOM_MINIMALITY_POLICY.md`,
`docs/audit/data/load_bearing_summary.json` (fanout cross-check).

**Walling no_go / bounded-theorem sources (per cluster):**
single-clock — `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`,
`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`,
`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md`;
Koide / observable — `KOIDE_RECORDS_OBJECTIVITY_CONDITIONAL_NOTE_2026-05-31.md`,
`FLAVOR_QD_OBJECTIVITY_FIXES_BASIS_NOT_WEIGHT_2026-06-02.md`,
`KOIDE_Q23_BLOCK_WEIGHT_FRONTIER_BOUNDED_NOTE_2026-05-29.md`,
`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`,
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`,
`OBSERVABLE_PRINCIPLE_DET_UNIQUE_MULTIPLICATIVE_CHARACTER_FORM_SELECTION_NARROW_THEOREM_NOTE_2026-05-28.md`,
`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`;
gauge/anomaly — `ANOMALY_FORCES_TIME_THEOREM.md`,
`NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md`,
`GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md`,
`STAGGERED_CHIRALITY_SELECTOR_ENUMERATOR_NARROW_THEOREM_NOTE_2026-06-06.md`,
`ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_NARROW_THEOREM_NOTE_2026-05-10.md`,
`RH_SECTOR_ANOMALY_CANCELLATION_IDENTITIES_NOTE_2026-05-02.md`,
`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`.

---

## BLOCK02 CRACK RESOLUTION (additive, 2026-06-20)

> **Additive dated correction — does not rewrite §3 above.** Block01 §3 flagged
> **SK-1** and **SK-2** as *CANDIDATE* no-new-axiom cracks ("✅ CANDIDATE CRACK")
> each with an explicit ACTION ("attempt the derivation BEFORE proposing"). Block02
> carried out both ACTIONs with dedicated runners. **Result: both WALL.** The
> optimistic "✅ CANDIDATE CRACK" flags in the §3 table are **superseded** by the
> ⛔ outcomes recorded here; the §3 "Net of the cracks" line ("SK-1 likely removes
> N2b … SK-2 may shrink Cluster 3") is **downgraded** accordingly.
> Full resolution: `docs/AXIOM_PROPOSALS_OPEN_CRACKS_RESOLUTION_NOTE_2026-06-20.md`.

```yaml
hypothetical_axiom_status: "not invoked — SK-1 and SK-2 both WALL; the corresponding C1/C3 clauses are CONFIRMED needed, not adopted"
proposal_allowed: false   # owner governance decision required
adopts_axiom: false
sets_audit_verdict: false
status_authority: independent audit lane / owner only
```

| Tag | Block01 flag | Block02 attempt (harder than prior block) | Runner | Block02 outcome |
|---|---|---|---|---|
| **SK-1** | ✅ candidate crack — `2 a_τ` from `scale_reference × kinetic_isotropy`; "likely removes N2b" | the **"same FORM edge object"** join (not the disavowed spacing-ratio identity): does `c_t=c_s` + absolute `a` force `a_τ = a`? | `scripts/sk1_baxis_n2b_kinform_scale_join_2026_06_20.py` **PASS=28 FAIL=0** | ⛔ **WALL STANDS.** `c_t/c_s = 1` is a dimensionless single point true for **every** `a_τ` (`a_τ,a_s` absorbed into physical `ω,k`); the range-1 FORM adjacency topology is identical for `a_τ=a_s` and `a_τ=10 a_s`; the join gives the absolute anchor + the form ratio but **NOT** the spacing ratio `a_τ/a_s`. Both notes reserve spacing to its own derivation row (kinetic_isotropy names the no-diagonal clause as supplier) ⇒ reading FORM as SPACING **mis-cites a primitive** (rule 5). **Banked no-axiom progress:** the factor **2** in `2 a_τ` is the structural 2-step block count (single-step non-positive; `T̂² = T_odd·T_even`, eig `exp(±2E)`), so the axiom-bearing residual shrinks to the single metric edge `a_τ`. |
| **SK-2** | ✅ candidate crack (route c) — imbalanced/curved complex `χ≠0`; "Cluster 3 shrinks" | the **OPEN/boundaried EVALUATION complex** (the path the prior block omitted): all-odd box gives `\|N_+−N_-\|=1` curvature-free | `scripts/frontier_abj_pabj_evaluation_complex_imbalance_2026_06_20.py` **PASS=75 FAIL=0** | ⛔ **WALL STANDS.** The open all-odd box is a live `χ≠0` surface (`A_t = N_+−N_- = +1`, gauge-robust) — but its index **flips** `0 → ±1` across A_min-admissible boundary conditions (open vs periodic) and extent-parity, both **regulator** choices A_min does not supply; the occupied-region imbalance is realized-state **REGISTERED DATA**; the closed all-odd torus is **non-bipartite** (`{ε,D}=0` breaks) so not a valid `ε`-index surface. No primitive supplies the boundary/occupancy selection ⇒ not A_min-native. |

**Net (block02): neither crack lands; no axiom is retired.** The two block01
candidate proposals the cracks would have retired are **CONFIRMED needed** (not
adopted):

- **C1 (RP-DYN) — N2b clause confirmed needed.** SK-1 walls. The absolute clock
  unit `2 a_τ` still requires either a no-axiom spacing-row derivation from the
  no-diagonal clause (untested lead, flagged for a follow-up block) or a primitive.
  **Narrowing (banked, no axiom):** the factor `2` is structural; the residual is
  the single metric edge `a_τ` (equivalently the dimensionless `a_τ/a_s`). C1's own
  minimality (proposes the *dynamics-side existence* of a step, never the
  dimensionful `2 a_τ`) is **vindicated**, and SK-1 confirms the C1↔N2b division of
  labor: the dynamics tick (rate γ, C1) and the metric clock unit (`a_τ`) are
  separate residuals. Weakest sufficient home for `a_τ`, if the no-diagonal lead
  walls: a single time-edge spacing datum (one dimensionless `a_τ/a_s`), strictly
  weaker than C1 and disjoint from the FORM content `kinetic_isotropy` supplies.
- **C3 (PIN-GAUGE-CONTENT) — P-ABJ clause confirmed needed.** SK-2 walls; Cluster 3
  is **unchanged**. The full ABJ fanout (~1105) remains attributed to C3. The
  P-ABJ wall stands on all of routes (a)/(b)/(c); the wall is **sharpened** onto
  the boundary-condition / finite-region / occupancy selection — the
  gauge-/particle-content gate `MINIMAL_AXIOMS_2026-06-05.md` lists as open.

**Recommended owner sequencing is unaffected:** C1 then C2, defer C3. The block01
"a crack always beats a proposal" stance is honored: both cracks were genuinely
attempted and honestly walled, so the C1/C3 residuals are real.

---

## BLOCK04 UNIFICATION (additive, 2026-06-20)

> **Additive dated minimization — does not rewrite §1–§7 above.** Block01 delivered
> the three candidate proposals `{C1, C2, C3}`; block02/03 confirmed the C1-N2b and
> C3-P-ABJ residuals genuinely wall (block03 NODIAG: the no-diagonal-clause spacing
> lead also **walled**, runner `…no_diagonal_spacing_crack…` PASS=17 FAIL=0, so the
> `a_tau/a_s` residual is real). Block04 runs the remaining minimization move —
> **unification**: does **one** operational axiom subsume **both** C1 (dynamics /
> arrow) and C2 (readout-context / objectivity)? **Result: PARTIAL COLLAPSE.** The
> block01 ranked-set §4 ("C1, C2, C3, three weak/heavy axioms") is **refactored**
> here into a strictly-weaker single operational axiom plus two isolated residual
> data; nothing in §1–§7 is deleted.
> Full synthesis:
> `docs/AXIOM_UPDATE_PROPOSAL_UNIFIED_OPERATIONAL_MEASUREMENT_2026-06-20.md`.

```yaml
hypothetical_axiom_status: "conditional on accepted new axiom; not retained on the actual current surface"
proposal_allowed: false   # owner governance decision required
adopts_axiom: false
sets_audit_verdict: false
edits_axiom_premise_nodes: false
status_authority: independent audit lane / owner only
collapse_verdict: partial_collapse
```

**The unified candidate axiom (UNADOPTED).** **(MEAS-REC-READOUT)** — there is a
system–environment measurement interaction that produces durable records and, for
the realized state, supplies **at once**: (a) an einselecting CPTP dynamics
`Φ_t = e^{tL}` with an **orientation** (= C1's dynamics + arrow + registration
direction); (b) the **pointer basis = the central-sector / `K`-CPT decomposition**
(the alphabet of distinguishable record outcomes = C2's readout context); and
(c) the **SBS / quantum-Darwinism objectivity criterion, BASIS ONLY** (the objective
observable is the one redundantly broadcast = C2's objectivity selector, basis
part). **Existence/slot only** — no kernel/rate, no weight/probability/Born rule, no
spacing, no arrow *sign*. *Strength: weak–medium.*

**What collapses (conditional; two runner legs).**

| | folds into U? | runner witness |
|---|---|---|
| **C1 full set** — arrow / B-AXIS N4 (registration-direction) / N5 (single-clock) / N2b-step / record-formation floor | **YES** | clause (a)[+(c)]; periodic `W`-exchange surface recomputed exactly invariant (`0.0`); antiperiodic-`τ` breaks `W` (`8.0`), symmetric BC restores (`0.0`); `|coh|→0` floor |
| **C2 basis / identification half** — T1-d det-readout identification (`W = c log det`); P-REC single-taste pointer; Koide objectivity-**BASIS** (2-outcome alphabet) | **YES** | clauses (b)+(c); Cauchy residual `8.88e-16`; no on-site anticommutant of the Pauli triple; SBS plateau over 2 outcomes |

**What does NOT collapse (two independent residual data — recomputed walls).**

1. **C2-WEIGHT** — the equal-block `(1,1)` sector-MEASURE weight `t = w_p/w_s = 1`
   that pins Koide `r=1/2`, `Q=2/3`. **Decisive (per the koide block02 R2/R3
   weight-blindness finding):** SBS objectivity is **weight-blind** (plateau
   `= H(weights)` for both `(1/2,1/2)` 1.000 bit and `(1/3,2/3)` 0.918 bit) **and**
   the einselection fixed point `I/3 → (1/3,2/3) → r=1` lands at `t=2`, the **wrong**
   value. Neither clause supplies `t=1`; it is a separate max-entropy / indifference
   datum (one dimensionless binary choice).
2. **SPACING** — the N2b time-edge spacing `a_tau/a_s` (Lattice disavows spacing;
   block02 SK-1 + block03 NODIAG walled; 6-NN adjacency metric-blind for
   `a_tau/a_s = 1, 10, 0.137`). One dimensionless ratio.

**Minimality (runner PART [0]/[4]).** U is **strictly weaker** than C1+C2 stated
separately: on the explicit 10-atom consequence lattice,
`Cons(U)` (9 atoms) `⊊ Cons(C1-sep ∧ C2-sep)` (10 atoms), the single distinguishing
atom being `equal_block_weight` (which U is weight-blind to); U admits strictly more
models; the converse derivation fails. `AXIOM_MINIMALITY_POLICY.md` **prefers** U on
all four criteria — weakest sufficient, non-redundant (§2 bounded composition with
named residuals), independent, no-laundering. `{U, W, S}` are proved **mutually
independent** by countermodel, with W and S verified **orthogonal dials**. **C3 does
NOT fold** (gauge representations vs measurement existence = category error / gate 3
vs gates 1/2; measurement witnesses blind to the anomaly traces / chirality template
and vice versa).

**FINAL MINIMAL PROPOSAL SET:** block01 `{C1, C2, C3}` → block04
**`{MEAS-REC-READOUT, C2-WEIGHT, SPACING, PIN-GAUGE-CONTENT}`** — the measurement
act is **one** weak–medium operational axiom, the two things it provably cannot
supply (the sector weight; the metric spacing) are isolated as their own weakest
dimensionless data, and C3 stays the one categorically distinct heavy addition,
**unchanged**.

**Coverage vs the 3-axiom version: SAME coverage, MORE minimal.** The block04 set
discharges the **identical** walls as the block01 `{C1, C2}` pair (no coverage loss,
no over-reach); the difference is purely structural — two operational axioms become
**one strictly-weaker** operational axiom, and the equal-block weight (which C2
silently bundled) plus the spacing (an implicit C1-N2b residual) are **named and
isolated** as the weakest separate data. If the owner's goal is the policy's
weakest-sufficient / non-redundant / independent / no-laundering target, the block04
`{U, W, S, C3}` set **should be preferred** over the block01 `{C1, C2, C3}` set
(C3 identical in both).

| Runner | TOTAL | Reproduced 2026-06-21 |
|---|---|---|
| `scripts/axiom_update_unified_measurement_axiom_sufficiency_2026_06_21.py` | PASS=39 FAIL=0 | yes (exit 0, `-W error` clean) |
| `scripts/axiom_update_unified_axiom_minimality_independence_2026_06_21.py` | PASS=28 FAIL=0 | yes (exit 0, `-W error` clean; caught + fixed a real color-double-counting bug in the LH anomaly trace mid-cycle) |

**Aggregate block04: PASS=67 FAIL=0 (39 + 28).** Both reuse the exact load-bearing
legs of the block01 cluster runners; deterministic; numpy + stdlib only; no
empirical import. All UNADOPTED; no axiom retired; no audit verdict set; the owner /
audit lane is the sole authority.
