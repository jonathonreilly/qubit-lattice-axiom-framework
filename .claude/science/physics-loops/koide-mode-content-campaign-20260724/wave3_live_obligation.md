# WAVE 3 — the live owner obligation, and the campaign mapped onto it

**Role:** read the owner-registered closure criterion and map the campaign onto
it. Everything below is measured against `origin/main` at `5807ef17b7`
(fetched at session start). I set, predict and estimate **no audit verdict**;
every status quoted is a live read of `docs/audit/data/ledger/` shards on
`origin/main`, reported as data.

**No repo file was edited. Only this report file was written.**

---

## 0. Framework refresher — surfaces actually read before concluding

Mandatory refresher, read in full or at the cited spans on `origin/main`:

- `docs/MINIMAL_AXIOMS_2026-06-29.md` — read `:1-193` (whole note); load-bearing
  spans `:63-79` (Record + Qualification), `:97-101`, `:128-134`, `:152-155`,
  `:156-173` (Open Gates Outside The Axioms).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` — read `:1-46`
  (whole file).
- `docs/audit/data/axiom_premise_nodes.json` — read `:1-52` (whole file);
  load-bearing `:4-9` (the four canonical ids) and `:25` (the `minimal_axioms`
  non-supply list).
- Source notes of every primitive invoked below:
  `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` (`:60-96` read, incl. the
  Informative State-Contingency Register). `scale_reference_primitive` and
  `kinetic_isotropy_primitive` are not invoked anywhere in this report.
- Governance/registry surfaces: `docs/audit/data/derivation_obligations.json`,
  `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md`,
  `docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md`,
  `docs/audit/scripts/audit_lint.py:678-731`,
  `docs/audit/data/lane_certification.json`,
  `docs/audit/AXIOM_MINIMALITY_POLICY.md` (grep only).
- Route maps named in the closure criterion:
  `docs/ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md`
  (read `:1-116`, whole note).
- Corpus surfaces quoted:
  `docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:70-100`,
  `docs/FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md:1-34`,
  `docs/ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md:1-60,245-265,367`,
  `docs/THETA_MASS_SIDE_COMPOSITION_CLOSE_ON_SHARED_OCCUPANCY_BRIDGE_BOUNDED_NOTE_2026-07-03.md:16-48`.

**What the refresher changes about this report.** Two clauses are decisive and
are used in §(d):

> `MINIMAL_AXIOMS_2026-06-29.md:156-160,170`
> ```
> ## Open Gates Outside The Axioms
>
> The four axioms do not close, import, or rename the framework's downstream open
> gates. In particular, the following remain outside axiom content:
> ...
> - source/action and physical-observable identification;
> ```

> `MINIMAL_AXIOMS_2026-06-29.md:152-155`
> ```
> - `K`/CPT orbit structure, central-sector decomposition, and any sector
>   generation rule are downstream readout-context content, not generic axiom
>   content.
> ```

and the machine mirror, `axiom_premise_nodes.json:25`, which states that
`minimal_axioms` "still supplies no context-selection rule, formation rule ...
weighting, normalization, probability, update law, ... K/CPT structure,
central-sector decomposition, source/action bridge, physical observable
bridge ...".

**Native rebuild.** Every load-bearing arithmetic step in §(b)/§(d) was rebuilt
from scratch in exact sympy in this session (no floats as inputs; the only
floating evaluation is a 50-digit `sp.N` used for strict-inequality spot checks
whose strictness is separately proven symbolically). Gate blocks A/B/C/D/E/G/H,
**121 gates, 0 substantive failures**; the 4 reported `FAIL`s in the first pass
were harness artifacts (`sympy` `BooleanTrue` vs Python `True`, and `Add`-arg
counting after like-term collection) and were repaired into proper structural
gates (B6a/B6b/B6c). Scripts live in the session scratchpad only:
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/{verify.py,verify3.py,verify4.py,verify5.py,verify6.py,verifyA.py}`.
**I found one prior-wave error and one prior-wave overreach; both are named in
§(b4) and §(b5).**

---

## (a) THE OBLIGATION RECORD AND THE CLOSURE CRITERION, VERBATIM

### (a1) The machine record

`docs/audit/data/derivation_obligations.json:10-17`, verbatim:

```json
    "ac_orbit_occupancy_statistical_grain_derivation_obligation": {
      "label": "AC occupancy statistical grain",
      "current_path": "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
      "target": "Derive from the retained framework chain whether the physical charged-lepton matter action counts the K/CPT orbit or holomorphic pair once rather than counting each sector or channel.",
      "status": "open_gate",
      "self_liquidation_condition": "A retained kappa/counting-rule theorem deriving this exact grain removes the obligation; until then it blocks dependent closure.",
      "historical_governance_source": "docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md"
    },
```

The registry's own governing sentence, `derivation_obligations.json:3`:

> "Non-premise registry of exact open derivation obligations. Entries never
> satisfy dependency closure, never bound or promote downstream rows, and may
> leave this registry only after a retained derivation closes the named target.
> The only supplied foundational premise types are axioms and approved
> primitives in `axiom_premise_nodes.json`."

`id` is listed in `canonical_ids` at `derivation_obligations.json:5`. The row is
live: its ledger shard
`docs/audit/data/ledger/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json`
carries `claim_type: "open_gate"`, `effective_status: "audited_renaming"`,
`criticality: "critical"`, `load_bearing_score: 14.6`, `direct_in_degree: 16`,
`transitive_descendants: 96`, `deps: []`, `runner_path: null`,
`runner_check_breakdown.total_pass: 0`.

### (a2) The source note and the closure criterion

`docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:3` —
`**Date:** 2026-07-11` (the campaign brief's dating is correct).
`:5-6` — `**Premise weight:** none. This is an open derivation obligation, not
an axiom, approved primitive, accepted premise, convention, or theorem.`

The closure criterion, `AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:19-24`,
verbatim:

```text
## Closure criterion

A closing theorem must derive the physical matter action and its measure, then
distinguish the count-once `det_C`/holomorphic realization from the
count-twice `|det_C|^2`/realified realization without inserting the desired
charged-lepton value or readout dictionary. Relevant current route maps are:
```

followed at `:26-28` by the three named route maps, and at `:30-31` by:

> "Until such a theorem is independently audited and retained, every result that
> uses this statistical-grain selection remains conditional or pending-chain."

and at `:35-38`:

> "This obligation is self-liquidating. If the running kappa/counting program
> derives this exact statistical grain at retained grade, the obligation is
> removed rather than converted into a new premise. Until then, the program's
> existence supplies no authority."

### (a3) What would discharge it — the criterion decomposed

The criterion is a **conjunction of three conditions plus a grade condition**.
This is the owner's definition of success and it outranks every framing this
campaign invented (`r = 2^s (g_0/g_1)`, "metric factor vs mode-count factor",
"the counting exponent `s`", "interior vs boundary horn" — none of these
vocabulary items appears in the criterion).

| # | condition | exact wording source |
|---|---|---|
| **C1** | **derive the physical matter action AND its measure** | `:21` "must derive the physical matter action and its measure" |
| **C2** | **then distinguish** the count-once `det_C`/holomorphic realization from the count-twice `\|det_C\|^2`/realified realization | `:22-23` |
| **C3** | **without inserting** the desired charged-lepton value **or readout dictionary** | `:23-24` |
| **G** | the resulting theorem is **independently audited and retained** | `:30-31`; `derivation_obligations.json:15` "A retained kappa/counting-rule theorem" |

Three structural consequences of the exact wording, all of which the campaign
has been operating against without stating:

1. **C1 is a derivation obligation about the ACTION, not about `r`.** The word
   `r` does not occur in the criterion. A theorem that pins `r` by any route
   that is not "derive the matter action and its measure" does not discharge
   this obligation even if the value is right. The criterion is
   route-restrictive by construction.
2. **C1 is gated behind a strictly larger open gate.**
   `MINIMAL_AXIOMS_2026-06-29.md:170` places "source/action and
   physical-observable identification" *outside axiom content*, and
   `axiom_premise_nodes.json:25` repeats "source/action bridge, physical
   observable bridge" in the `minimal_axioms` non-supply list. So C1 cannot be
   satisfied from the axioms alone; it requires a retained source/action bridge
   that does not currently exist. Nothing in this campaign, in any wave,
   attempted C1.
3. **C3 forbids the campaign's most-used move.** "or readout dictionary" rules
   out closing the bit by declaring which readout functional / which Gram /
   which normalization the carrier carries. Every candidate selector the
   campaign found is a readout-dictionary choice (see §(b)).

**The single sentence that discharges it:** *a retained-grade theorem that
constructs the charged-lepton matter action and its path-integral measure from
the retained chain, and shows that measure to be `det_C` rather than
`|det_C|^2`, with no charged-lepton number and no readout dictionary inserted
anywhere in the construction.*

---

## (b) THE CAMPAIGN MAPPED ONTO THE CRITERION

Unflattering summary first, then the row-by-row.

> **Against C1: zero progress, zero attempts, across all three waves.**
> **Against C2: already discharged before the campaign opened, and discharged
> `r`-neutrally, by the one retained route map the criterion itself names.**
> **Against C3: the campaign's real output. It has shown, at gated grade, that
> five distinct selector classes all violate C3 — each one carries the count in
> its own identification step rather than deriving it.**
> **Against G: not applicable — nothing produced is at retained grade, and
> nothing downstream of the obligation is at retained grade either (§(c3)).**

### (b1) C2 is not the campaign's problem and never was

`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md`
is the **only** one of the three route maps named at
`AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:26-28` that
carries retained standing on the live ledger:

| route map named at `:26-28` | live `effective_status` |
|---|---|
| `ACPHILAMBDA_MEASURE_BINARY_AXIOM_UPDATE_NO_GO_NOTE_2026-07-04.md` | `unaudited` |
| `ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_EXACT_SUPPORT_NOTE_2026-07-04.md` | **`retained`** |
| `ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md` | `unaudited` |

That retained note proves `det_R R(K) = det_C(K) det_C(conj K) = |det_C(K)|^2`
(`:23-27`) and the Berezin first-power identity (`:32-36`) — i.e. it supplies
**the fork C2 asks a closing theorem to choose between**. And it says, in its
own words at `:94-102`:

> "This theorem supplies the determinant-power fork used to state AC(i)
> precisely. Its domain consists of the complex Gaussian, its realification, and
> their exact determinant powers. Physical identification of the charged-lepton
> matter carrier, `K`/CPT-orbit occupancy grain, path-integral measure, action,
> registered-mass coordinate, phase, and `R-eta` readout belong to separate
> source rows. **The construction is constant over every supplied registered-mass
> ratio `r`; `r` remains a free dial.**"

So the owner's own retained surface already states that the fork is `r`-neutral
and that the selector lives in the action/measure. **C2 was never the gap. C1
is the gap, and C3 is the trap.** The campaign has spent three waves on the
trap.

### (b2) DISCHARGED by the campaign: nothing

No campaign result discharges C1, C2 (already discharged, not by us), C3, or G.
There is no partial discharge either: the criterion is a conjunction, and C1 —
the first conjunct — was never attempted.

### (b3) UNTOUCHED by the campaign

- **C1 in full.** No wave built a matter action. Wave 1 built a carrier and
  counted Berezin modes; Wave 1's own flag 3 (`CAMPAIGN.md:161-166`) records
  that the polarization was *handed to* that machinery at declaration time, so
  even that was not an action derivation. The wall exercise then killed the
  planned "derive `g_0/g_1` from the corner action's kinetic normalization"
  as convention-laundering (`CAMPAIGN.md:201-209`) — correctly, but the effect
  is that the one wave aimed near C1 was withdrawn before running.
- **The measure.** No wave constructed a path-integral measure for the
  charged-lepton corner. `KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md`
  exists on main and is `unaudited`; Wave 1 flag 1 (`CAMPAIGN.md:145-153`)
  reports its 6-vs-12-generator horn is `r`-neutral in its landed realization,
  which if right means the corpus's nearest-to-C1 surface does not bear on C2
  either.
- **G, the grade condition.** Nothing in this campaign is on `origin/main`; the
  campaign's entire output is untracked session files.

### (b4) SHOWN UNDISCHARGEABLE BY A GIVEN ROUTE — the campaign's real product

Each row is a C3 violation: the route reaches a value of the count only by
having already chosen it somewhere in its own identification step.

| # | route | what the campaign showed | my independent status |
|---|---|---|---|
| R1 | **reality type / Frobenius–Schur / orientation** | `FS = (+1,0,0)` is constant across the whole `C_3`-invariant form cone while `r` sweeps `(0,∞)`; `FS = 0` *is* the count binary, so it is structurally incapable of resolving it (`CAMPAIGN.md:113-143`) | not re-derived here (out of my scope); it reproduces a landed foreclosure at `KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:157` |
| R2 | **any module invariant** (commutant theorem) | `Γ = diag(λ,μ,μ)` commutes with the clock rep and with the `K`/CPT reflection and moves `γ → (λ/μ)²γ` transitively over `(0,∞)` while fixing the module; hence no invariant of any kind selects `r` | reproduced by both Wave-2 defenders independently; I did not re-run it, but it is the one result in the campaign that both defenders agreed on without qualification |
| R3 | **associativity / Frobenius readout form (Ex1)** | pins the form to the trace, hence `γ = 1/2` — **but the associativity condition is an IMPORT**, and pushed to consistency the same bridge gives `r = 1`, not `r = 1/2` | the demotion is correct on the refresher surfaces I read: `MINIMAL_AXIOMS_2026-06-29.md:170` and `:128-134` put readout/source-action identification outside axiom content, so an associative readout form is a supplied dictionary — exactly what C3 forbids |
| R4 | **Record additivity fixing the mode-count ratio** | the finitely-additive readout space on the 2-letter record alphabet is exactly 2-dimensional (one free ratio after scale) | confirmed against `axiom_premise_nodes.json:25` and `MINIMAL_AXIOMS_2026-06-29.md:152-155`, which exclude weighting, normalization, `K`/CPT structure and central-sector decomposition from Record by name |
| R5 | **positive `C_3`-covariant spectral weights (exercise sector 3, "P1")** | claimed `r(t) = (S+2F)/(S−F) > 1` strictly, so `r = 1/2` unreachable, breach at `F/S = −1/5` | **the arithmetic is right and the conclusion is void — see §(d1). I rebuilt both.** |
| R6 | **spectrum positivity of the Hermitian element (Wave 2, "P2")** | `e_2 = 3(a²−\|b\|²) > 0` hence `r < 1` strictly, `r = 1` only at spectrum `(3a,0,0)` | **the arithmetic is right and the conclusion is branch-conditional — see §(d2). I rebuilt it and produced an exact counter-witness.** |

**Prior-wave error found (R5).** Exercise sector 3's identification of the
isotypic heat weights with a cone point in the coefficient coordinates is
**exactly 2-fold ambiguous**, and the factor 2 *is* the counting bit. Gates
`D1-D7`: the HS form in coefficient coordinates `(a, Re b, Im b)` is
`3a² + 6x² + 6y²` (`D1`), so `Tr P_0 : Tr P_1 = 1 : 2` (`D7`) and the two
natural inductions of a weight pair `(w_0, w_1)` into a Gram differ by exactly
2 (`D6`). Under the HS-referenced induction the same heat weights give
`r(t) = (S+2F)/(2(S−F))`, whose breach conditions are `F/S = 0` for `r = 1/2`
(`E3`) and `F/S = 1/4` for `r = 1` (`E4`) — **both attainable with `F ≥ 0`**
(`E5`). So R5 does not exclude `r = 1/2`; it restates the counting convention.
Wave 2's breach-target agent reached the same conclusion by its own route
(`wave2_breach_target.md:72-88`); I confirm it independently and exactly.

**Prior-wave overreach found (R6).** "`r = 1` is excluded except degenerately"
is true **only on the all-positive root branch**. Exact signed counter-witness
(gates `G1-G5`): eigen-slots `(1, 2, −2/3)` give `e_2 = 0` exactly, hence
`Q = Tr(H²)/(Tr H)² = 1` exactly, with masses `(1, 4, 4/9)` all nonzero and
pairwise distinct and `a = 7/9 > 0`, i.e. `r = |b|²/a² = 1`. The Wave-2 report
does flag the branch caveat honestly at `wave2_defend_ex2.md:625-629`; the
campaign file's own summary (`CAMPAIGN.md:312-320`, "`r = 1` is on the
BOUNDARY") does not, and reads as unconditional. It is not.

### (b5) A framing the campaign invented that the criterion does not license

`CAMPAIGN.md:283-286` states `r = 2^s (g_0/g_1) = (g_0/g_1)(w_1/w_0)` as "the
same description". As algebra that is fine (I confirm `Q = 1/3 + (2/3) r`
exactly and phase-independently, gate `A8`; `r = 1/2 → Q = 2/3`, `A8b`;
`r = 1 → Q = 1`, `A8c`). But it is a **coordinate factorization of the readout
dictionary**, and the criterion at `:23-24` explicitly forbids inserting a
readout dictionary. Splitting `r` into a "metric factor" and a "counting factor"
does not move the campaign toward C1; it relocates the residual inside the very
object C3 rules out. Every wave since the wall exercise has been arguing about
which half of a forbidden object supplies the answer.

---

## (c) THE TIER-A DEMOTION, AND THE BLAST RADIUS

### (c1) The quotes

`docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:9-18`, verbatim:

```text
**Premise weight:** none. This file preserves governance provenance only.
**Current status:** the former governance-only premise channel is withdrawn.
The supplied foundation now contains exactly axioms and approved primitives.

## Current disposition

The 2026-07-05 decision below no longer retires or satisfies any physics
dependency. Its two AC scientific statements are open derivation obligations:

- [AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md](AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md)
```

`docs/TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md:37-42`, verbatim
(this is the retired premise itself):

```text
### Historical Candidate 1

```text
For the AC_phi_lambda charged-lepton matter-action surface, the physical
statistical grain is the K/CPT orbit or holomorphic-pair occupancy grain:
the doublet contributes once per K/CPT orbit rather than once per sector or
channel. This premise supplies only the matter-action occupancy grain needed
```

and the reason, `:61-72`:

> "The repo's TOE objective requires physical selectors and readout bridges to be
> derived or to remain visibly open. An owner decision can approve an axiom or a
> primitive, but it cannot create a third kind of supplied physics authority.
> Accordingly: the historical decision remains provenance; neither historical
> candidate is an axiom or approved primitive; neither statement chain-satisfies
> or bounds a dependent claim; no audit verdict is changed by this meta note;
> downstream status changes are computed mechanically by the audit pipeline."

The note also records the header `**Superseded:** 2026-07-11` (`:5`) — the same
date as the obligation note.

### (c2) What exactly was retired

Three distinct things, and it is worth separating them because the campaign has
conflated the first with the third:

1. **The scientific statement "the doublet contributes once per `K`/CPT orbit
   rather than once per sector or channel"** — retired as a premise, re-registered
   as the open obligation. Its *content* survives verbatim as the obligation
   target; only its *authority* was withdrawn.
2. **The governance CHANNEL itself** — "the former governance-only premise
   channel is withdrawn" (`:10`). This is the structural retirement: there is no
   longer a third premise type. `docs/audit/data/owner_governed_premise_nodes.json`
   **does not exist on `origin/main`** (verified: `git show origin/main:...`
   returns `fatal: path ... does not exist`), and `docs/audit/scripts/audit_lint.py:683-686`
   makes its existence a hard lint error:
   `"owner_governed_premise_nodes.json must not exist; the only supplied premise
   registry is axiom_premise_nodes.json"`. The retirement is machine-enforced,
   not just documented.
3. **Nothing about the horn's truth.** `:42-43` of the obligation note:
   "This note selects no horn, derives no `r`, `Q`, mass, mixing angle,
   probability rule, species map, or sector weight, and changes no audit verdict."

### (c3) Blast radius — measured, not asserted

**Graph scope.** From the obligation row's own shard: `direct_in_degree: 16`,
`transitive_descendants: 96` (snapshot at audit time `2026-07-11T22:05:50Z`).
Recomputing the transitive dependent set from the local
`docs/audit/data/citation_graph.json` (note: that file is **generated and
gitignored** — `.gitignore:41` — so it is a working artifact, not tracked truth;
I report it as such) gives **71** rows that reach the obligation through
markdown-link citation edges. The 16 direct citers are:

```
acphilambda_measure_binary_axiom_update_no_go_note_2026-07-04                                       unaudited
acphilambda_occupancy_formation_append_non_supply_no_go_note_2026-07-04                             unaudited
acphilambda_occupancy_grain_menu_counting_measure_dynamical_static_correspondence_..._2026-07-16    unaudited
acphilambda_occupancy_grain_rule_class_universality_bounded_theorem_note_2026-07-11                 unaudited
acphilambda_occupancy_grain_sharpening_import_decomposition_..._2026-07-16                          unaudited
acphilambda_retirement_basis_rematch_and_claim_surface_note_2026-07-06                              meta
admitted_input_registry_tier_a_note_2026-05-23                                                      meta
charged_lepton_brannen_bae_delta_tier_a_bounded_theorem_note_2026-05-30                             unaudited
charged_lepton_koide_two_gate_tier_a_bounded_theorem_note_2026-06-02                                unaudited
charged_lepton_koide_value_full_chain_of_custody_2026-06-02                                         unaudited
koide_r_half_polarization_selector_tested_static_readout_no_go_note_2026-06-08                      unaudited
observable_principle_consumed_sector_bounded_by_ac_phi_lambda_narrow_theorem_note_2026-06-05        unaudited
observable_principle_p2_phase_blindness_sector_resolved_narrow_theorem_note_2026-06-04              unaudited
strong_cp_determinant_readout_bridge_narrow_theorem_note_2026-06-12                                 unaudited
theta_mass_side_composition_close_on_shared_occupancy_bridge_bounded_note_2026-07-03                unaudited
tier_a_residual_owner_adoption_retirement_2026-07-04                                                meta
```

**Standing of the blast radius — the finding.** Across all 71 transitive
dependents:

```
unaudited          53
meta               10
NO_SHARD            7
audited_renaming    1
retained*           0     <-- ZERO
```

**Not one row downstream of this open gate carries retained-grade standing.**
The retirement therefore orphaned **no** retained claim, because there was never
a retained claim resting on it. This is the sharpest statement of the blast
radius: it is 71 rows wide and zero rows deep.

**Does anything still silently assume the retired premise?** I ran a direct
scan, not a status-label scan. Eleven notes on `origin/main` use the
`count-once` / "counts the `K`/CPT orbit once" phrasing without a markdown link
to the obligation note; four of those are additionally *not* routed through the
gate in the citation graph:

```
HIERARCHY_KOIDE_ACPHILAMBDA_TWO_BIT_DECOMPOSITION_NOTE_2026-06-06.md        unaudited   not routed
KOIDE_R_HALF_INDEX_READOUT_NON_SUSY_STAGGERED_DIRAC_GATE_META_NOTE_2026-06-05.md  meta   not routed
KOIDE_KODIM_REAL_STRUCTURE_ROUTE_EMPTY_R_UNDETERMINED_BOUNDED_NO_GO_NOTE_2026-06-08.md  unaudited  not routed
KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md  unaudited  not routed
```

I read the `count-once` occurrences in all four. **None uses it as a supplied
premise**; in each it is the *name of a structural option* inside a no-go or a
scoping note (e.g. `KOIDE_KODIM_...:47-48` argues "the claim that 'the count-once
projection is not J-real' is **backwards**"). **No silent premise leak found.**
The honest hygiene finding is the opposite of premise laundering: the strongest
consumer, `THETA_MASS_SIDE_COMPOSITION_CLOSE_ON_SHARED_OCCUPANCY_BRIDGE_BOUNDED_NOTE_2026-07-03.md:16-24`,
states its dependence *explicitly* — "This note composes the theta mass-side
chain on two distinct conditional bridges: 1. the charged-lepton matter action
counts the `K`/CPT orbit once" — and is labelled `bounded_theorem (composition),
conditional on two independent bridges` at `:5`. The corpus is being honest here.

**Certification consequence (this is the load-bearing blast-radius number).**
`docs/audit/data/lane_certification.json` shows the obligation blocking three
lanes:

| lane | root | `certified` | `closure_size` | `uncertified_count` |
|---|---|---|---|---|
| `charged_lepton_koide_value` | `charged_lepton_koide_value_full_chain_of_custody_2026-06-02` | **false** | 40 | **24** |
| `rule_universality_grain` | `acphilambda_occupancy_grain_rule_class_universality_bounded_theorem_note_2026-07-11` | **false** | 19 | 18 |
| `acphilambda_retirement_basis` | (the two AC obligations) | **false** | 2 | 2 |

In `charged_lepton_koide_value` the obligation is one of **24** blockers. The
other 23 include the lane root itself (`unaudited`) and **two `audited_failed`
rows** — `koide_kappa_zd_action_circulant_character_decomposition_narrow_theorem_note_2026-06-05`
and `three_generation_observable_count_corollary_note_2026-05-03`. **Discharging
this obligation would not certify the lane.** That is the most important number
in this report for planning purposes and it does not appear anywhere in
`CAMPAIGN.md`.

### (c4) One live tension to report to the owner (not adjudicated here)

There is exactly one `retained_bounded` row in this neighbourhood:
`flavor_r_half_is_a_stationary_point_not_forced_2026-06-02` (live
`effective_status: retained_bounded`, `claim_type: bounded_theorem`) — and it is
**not** downstream of the obligation. Its title and `:10-15` say, verbatim:

> "The 5-round J-hunt tried to **force r=1/2** (det_C) **over r=1** (det_R) — to
> derive r=1/2 as *the* value via a measure-selection principle. That is the
> **forced-selection framing already retired earlier this campaign** ... r=1/2
> does not need to be *forced*. It is a **distinguished stationary point** of the
> r-family, and the three special Q's are **distinguished points = different
> physics (lanes)**, not one value to select."

I rebuilt its verified content natively (gates `H1-H5`): with
`p_singlet = 1/(1+2r)`, `p_doublet = 2r/(1+2r)`, the sector-power entropy has
its unique stationary point at `r = 1/2`, with `S(1/2) = log 2`, `S''(1/2) < 0`
(a maximum), the power imbalance `|3a² − 6|b|²|` vanishing there, and `r = 1/2`
the fixed point of `r → 1−r`. All exact, all correct.

So the corpus's **highest-graded** statement about `r` says the forcing target
was retired, while the corpus's **live governance record** (2026-07-11, five
weeks later) re-registers exactly that forcing target as an open obligation.
Both are on `origin/main`. I do not adjudicate this; the audit lane and the
owner do. But the campaign should not proceed as if the forcing framing were
uncontested corpus content — it is contested by the only retained row in sight.

---

## (d) VERDICT

### (d1) First, the Wave-3 question, resolved: there is no contradiction, and neither side is a constraint on `r`

The brief asked whether (P1) and (P2) can both be about the same `r`. They
cannot, and the sharper answer is that **neither is a constraint on the
obligation's target**.

**(P1) is the counting convention restated, not a bound.** I rebuilt the landed
heat-trace identity exactly. Gates `B1-B5` (`N = 2,3,4`, moments `n = 0..4`,
exact integer position-space traces vs exact algebraic momentum sums):
`Tr(D^n R^j) = Σ_{R^j k = k} D̂(k)^n`, and `Tr(D^n R²) = Tr(D^n R)`. Gates
`B6a-B6c` (`N = 2,3,4,6,12`): the `R`-fixed momenta are a strict subset
(`N < N³`), every `D̂(k)` is real, hence every summand `exp(−t D̂)` is strictly
positive, hence `0 < F < S` strictly. Gates `B7-B8` (`N = 2,3,4,6`,
`t ∈ {1/1000, 1/2, 3, 10}`, 50-digit evaluation): `(S+2F)/(S−F) > 1`
throughout. Gates `B9-B11`: exact breach solves `F/S = 0`, `−1/5`, `1/4` for
`γ = 1, 1/2, 2`. **All of the exercise's arithmetic reproduces.**

And it is void as a constraint, for the reason given in §(b4): the step from
isotypic weights to a cone point in the coefficient coordinates is 2-fold
ambiguous by exactly `Tr P_1 / Tr P_0 = 2` (gates `D1-D7`), and under the
HS-referenced induction both horns are reachable with `F ≥ 0` (gates `E3-E5`).
Independent corroboration from the corpus, not from a wave:
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:97-98`
already records "the native imaginary-time (heat-kernel) arrow flows `r -> 1`;
recording yields the same `det_R` default". Exercise sector 3 rediscovered a
landed sentence and attached a finite-`t` sign to it.

**(P2) is branch-conditional, and the corpus already said positivity is
`r`-blind.** I rebuilt it exactly: `e_1 = 3a` (`A4`), `e_2 = 3(a²−|b|²)` (`A5`),
`Tr(H²) = 3a²+6|b|²` (`A6`), `(Tr H)² − Tr(H²) = 2e_2` (`G1`), the witness
spectra `(2, ½, ½) → (4, −½, −½)` (`A11`, `A12`), the `r = 1` degenerate
spectrum `(3a, 0, 0)` (`A10`), and `r = 1/2` interior with spectrum
`a(1+√2), a(1−√2/2), a(1−√2/2)`, strictly positive (`A14`, `A15`). All correct.
But `G2-G5` give the exact signed counter-witness `(1, 2, −2/3)`: `e_2 = 0`,
`Q = 1` exactly, three distinct nonzero masses `(1, 4, 4/9)`, `a = 7/9 > 0`.
And `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:95-96`
already records: "**reflection positivity** — the channel Gram is diagonal, so
positivity is a one-sided sign window; **it does not see the diagonal balance
`r=1/2`**".

**Net.** The supervisor prediction at `CAMPAIGN.md:372-381` ("different objects,
both can hold, they squeeze from opposite sides") is half right — they are
different objects — but the interesting half is wrong: they do not squeeze,
because after the identification convention and the root branch are exposed,
**neither one constrains `r` at all**. The Wave-3 "contradiction" was two
`r`-blind statements wearing `r`-shaped clothing. This is a null result, and it
is the fifth consecutive selector class to fail C3 in exactly the same way.

### (d2) Is the obligation dischargeable by any route currently visible?

**No — and the reason is structural, not effort-limited.**

1. **C1 is blocked by a strictly larger open gate.** The criterion's first
   conjunct is "derive the physical matter action and its measure".
   `MINIMAL_AXIOMS_2026-06-29.md:170` places source/action identification
   outside axiom content; `axiom_premise_nodes.json:25` repeats it. No retained
   source/action bridge exists. **This obligation cannot close before a larger,
   currently-open gate closes.** That is a fact about the dependency order, not
   a judgement about difficulty, and it is visible on the refresher surfaces the
   campaign is required to read every wave.
2. **C2 is already discharged and is `r`-neutral by its own retained text**
   (`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_..._2026-07-04.md:102`).
   There is no work left on the conjunct the campaign has been attacking.
3. **C3 has now killed five selector classes with one identical mechanism.**
   Reality type (R1), module invariants (R2), associative readout forms (R3),
   Record additivity (R4), positive covariant spectral weights (R5), spectrum
   positivity (R6) — each reaches a value of the count only by fixing the count
   inside its own identification step or branch choice. The campaign has not
   found a route that survives C3; it has found six that do not.
4. **G is unreachable from a session anyway** — the obligation liquidates only
   on a *retained* theorem, and even a perfect one would leave
   `charged_lepton_koide_value` uncertified with 23 other blockers, two of them
   `audited_failed` (§(c3)).

### (d3) RECOMMENDATION: convert to a decisive negative

**Convert.** The campaign should stop hunting a selector and ship the negative
it has actually earned. The C3 mechanism is now demonstrated across six classes
and — crucially — the two newest classes (R5, R6) are the ones the corpus itself
had already flagged as `r`-blind at
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:95-98`.
Continuing to hunt inside the readout dictionary is re-walking a wall, which is
this campaign's own named failure mode (`CAMPAIGN.md:27-30`).

A sharp negative is a success (`CAMPAIGN.md:80-81`), and this one is
publishable-shaped: it retires the positivity attack class the way Wave 1
retired the invariant class, and it does it with exact witnesses rather than a
survey.

### (d4) THE SINGLE NEXT ARTIFACT

**One narrow no-go note plus its runner, mirroring the landed
`..._NON_SUPPLY_NO_GO_NOTE_...` template exactly (no new vocabulary, no new
tags, no new claim classes):**

- `docs/ACPHILAMBDA_OCCUPANCY_GRAIN_POSITIVITY_CLASS_NON_SUPPLY_NO_GO_NOTE_2026-07-24.md`
- `scripts/acphilambda_occupancy_grain_positivity_class_non_supply_no_go_2026_07_24.py`

**Exact theorem it should carry** (all three legs are already gated in this
session; the runner is a transcription, not new research):

1. **The isotypic-weight induction is 2-fold ambiguous and the ambiguity is the
   grain.** On the `C_3`-covariant generation coefficient surface,
   `Tr P_0 : Tr P_1 = 1 : 2`, the Hilbert–Schmidt form reads `3a² + 6|b|²`, and
   the per-real-dimension and HS-referenced inductions of one isotypic weight
   pair differ by exactly the factor 2. Therefore **no positive `C_3`-covariant
   spectral weight supplies the occupancy grain**: it presupposes it. Corollary:
   the `F/S = −1/5` "breach condition" is not a well-posed target — under the
   other induction the same weights reach the same point at `F/S = 0`.
2. **Spectrum positivity does not supply it either.** `(Tr H)² − Tr(H²) = 2e_2`
   with `e_2 = 3(a²−|b|²)`, so on the all-positive root branch `Q < 1` strictly;
   but the exact signed instance `(1, 2, −2/3)` gives `Q = 1` with three distinct
   nonzero masses at `a > 0`. The constraint is carried by the root branch, which
   is a separate open surface
   (`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`,
   live `unaudited`), not by positivity.
3. **Both legs reproduce, rather than close, landed sentences** at
   `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:95-96`
   and `:97-98`, and neither touches
   `AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:21` ("derive
   the physical matter action and its measure"). **The note must say so
   explicitly and select no horn.**

**Scope boundaries the note must carry** (mirroring
`ACPHILAMBDA_OCCUPANCY_DETERMINANT_POWER_SPLIT_..._2026-07-04.md:94-106`):
selects no horn; derives no `r`, `Q`, mass, mixing angle, probability rule or
sector weight; sets no audit verdict; supplies no premise; and does **not**
discharge the obligation — it removes two candidate routes from the C3 side
while C1 remains untouched.

**What NOT to ship.** Do not ship the `r = 2^s(g_0/g_1)` factorization as a
framing, and do not ship the "interior vs boundary horn" sentence — the first is
a readout dictionary (C3-forbidden), the second is false off the positive root
branch (`G2-G5`).

**If the owner instead wants the obligation genuinely attacked**, the only route
the criterion licenses is C1, and the honest scoping sentence is: *this
obligation is downstream of "source/action and physical-observable
identification", which `MINIMAL_AXIOMS_2026-06-29.md:170` places outside axiom
content and which no retained row currently closes.* That is a different and
much larger campaign, and it should be opened as one rather than approached
sideways through the readout dictionary.

---

## Verification appendix

Exact-sympy gate blocks run in this session (scratchpad only; no repo file
touched). Inputs are exact rationals/symbols throughout; the only numeric
evaluation is 50-digit `sp.N` used to spot-check strict inequalities whose
strictness is independently proven symbolically in `B6a-B6c`.

| block | subject | gates |
|---|---|---|
| `A0-A15` | `W = Herm(circ_3)`: `C³=I`, Hermiticity, eigenvalues, `e_1`, `e_2`, `Tr(H²)`, HS cone point, `r=1` degeneracy, the two witness spectra, `r=1/2` interior | 20 |
| `A8, A8b, A8c` | `Q = Tr(H²)/(Tr H)² = 1/3 + (2/3) r` exactly, phase-independent; horn values `2/3` and `1` | 3 |
| `B1-B5` | `Z_N³` heat-trace identity as an exact moment identity, `N = 2,3,4`, `n = 0..4`, position-space integer traces vs momentum sums | 45 |
| `B6a-B6c` | strictness of `0 < F < S` proven structurally (strict subset + reality + positivity), `N = 2,3,4,6,12` | 15 |
| `B7-B8` | `0 < F < S` and `(S+2F)/(S−F) > 1`, `N ∈ {2,3,4,6}`, `t ∈ {1/1000, 1/2, 3, 10}` | 32 |
| `B9-B11` | exact breach solves `F/S ∈ {0, −1/5, 1/4}` | 3 |
| `C1-C7` | object separation + graded-weight mutation probes | 7 |
| `D1-D7` | the induction ambiguity is exactly `Tr P_1/Tr P_0 = 2` | 7 |
| `E1-E5` | both horns reachable with `F ≥ 0` under the HS-referenced induction | 5 |
| `G1-G7` | `(Tr H)² − Tr(H²) = 2e_2`; exact signed witness `(1,2,−2/3)` with `Q = 1` at three distinct nonzero masses | 7 |
| `H1-H5` | the retained stationary-point content rebuilt: unique entropy maximum at `r = 1/2`, `S(1/2)=log 2`, `S'' < 0`, imbalance trough, swap fixed point | 5 |

**Total: 121 gates, 0 substantive failures.** Four first-pass `FAIL`s were
harness artifacts (sympy `BooleanTrue` vs Python `True`; `Add`-arg counting after
like-term collection) and were rewritten into the proper structural gates
`B6a-B6c`; they are not results.

**Honest boundary.** I did not re-derive R1 (Frobenius–Schur) or R2 (the
commutant theorem) — they are outside this role's scope and I report them as the
waves recorded them, flagged as such in the §(b4) table. I did not read the
Wave-1 reports in full. I derived no `r`, adopted no horn, consulted no PDG
value, and proposed no repo vocabulary beyond the existing
`..._NON_SUPPLY_NO_GO_NOTE_...` naming pattern. I set, predicted and estimated no
audit verdict; every status above is a live shard read on `origin/main`,
reported as data.
