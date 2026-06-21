# Foundation Revision CHANGESET — apply-order README (DRAFT — NOT ADOPTED)

> **Key terms used in this doc** are indexed A-Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-06-21
**Type:** meta / governance changeset apply-order checklist.
**Status:** **DRAFT changeset for owner + independent audit-lane review.**
`hypothetical_axiom_status: proposed`; `proposal_allowed=false`. Nothing here is
adopted; the owner plus the independent audit lane are the **sole authority** to
adopt, and the audit lane sets all effective statuses.
**Branch:** `physics-loop/foundation-revision-changeset-block02-20260620`.

This README is the **apply-order checklist** for the foundation-revision
changeset. It does **not** itself apply anything. The substantive OLD->NEW
wording and adversarial re-checks live in
`docs/FOUNDATION_REVISION_PROPOSAL_2026-06-20.md`; the full proposed revised memo
is `docs/MINIMAL_AXIOMS_2026-06-21_PROPOSED.md`; the registry mutation is the
applyable patch
`.claude/science/physics-loops/foundation-revision-proposal/registry_changeset.patch`.

---

## 0. What this changeset contains (files)

| Artifact | Path | Kind | Adopted? |
|---|---|---|---|
| Proposed revised memo | `docs/MINIMAL_AXIOMS_2026-06-21_PROPOSED.md` | new dated memo, supersedes-references 2026-06-05 on approval only | NO (draft) |
| Registry patch | `.claude/science/physics-loops/foundation-revision-proposal/registry_changeset.patch` | git-applyable unified diff | NO (do not apply) |
| This README | `docs/FOUNDATION_REVISION_CHANGESET_README_2026-06-21.md` | apply-order checklist | NO (draft) |
| Claim-status certificate | `.claude/science/physics-loops/foundation-revision-proposal/CLAIM_STATUS_CERTIFICATE_block02.md` | provenance | NO (draft) |
| Loop state | `.claude/science/physics-loops/foundation-revision-proposal/STATE.yaml` | bookkeeping | n/a |
| Upstream proposal (block01) | `docs/FOUNDATION_REVISION_PROPOSAL_2026-06-20.md` | OLD->NEW + re-checks | NO (draft) |

**NOT touched (by hard rule):** `docs/MINIMAL_AXIOMS_2026-06-05.md` (canonical
memo — left byte-for-byte intact); `docs/audit/data/axiom_premise_nodes.json` and
`docs/audit/data/tier_a_admissions.json` (audit-lane authority — changes emitted
as the patch + the human-readable diff in §3, never written).

---

## 1. Apply order (AT ADOPTION ONLY — owner + audit lane execute)

Do **not** run any of these without explicit owner approval (note the P2 reversal,
§4) and independent audit-lane review.

1. **Adopt the memo.** Promote `docs/MINIMAL_AXIOMS_2026-06-21_PROPOSED.md` to the
   new canonical memo (the audit lane re-dates / renames per its own process),
   superseding `docs/MINIMAL_AXIOMS_2026-06-05.md`. The 2026-06-05 memo becomes
   historical (append it to `minimal_axioms.aliased_paths` so existing markdown
   links keep resolving).
2. **Apply the registry patch.** From repo root:
   `git apply .claude/science/physics-loops/foundation-revision-proposal/registry_changeset.patch`
   This (a) removes `kinetic_isotropy_primitive` from
   `axiom_premise_nodes.json` (`canonical_ids` + `nodes`) and (b) adds
   `kinetic_isotropy_renormalized_anisotropy_target_2026-06-21` (label `xi_R`) to
   `tier_a_admissions.json` as the renormalized-anisotropy admitted derivation
   target, bumping `genuine_admitted_input_count` 2 -> 3.
   `git apply --check` has been verified to pass against the current tree.
3. **Update `minimal_axioms` source-path bookkeeping** in
   `axiom_premise_nodes.json` (`current_path` -> the adopted 2026-06-21 memo path;
   prior path appended to `aliased_paths`). *(Not in the patch — depends on the
   final adopted filename, an audit-lane call.)*
4. **Record the P2 reversal + criteria in `AXIOM_MINIMALITY_POLICY.md` §6**
   (see §4 and §6 below).
5. **Hash-guard re-audit (mechanical).** Editing `minimal_axioms` content
   invalidates prior direct `minimal_axioms` audits via the axiom-premise hash
   guard; the audit lane re-audits all direct dependents.
6. **Downstream re-audit / re-cite sweep** (§5).

If the owner selects the **derived-target** route for P2 instead of the
admitted-input route, replace step 2's `tier_a_admissions.json` addition with an
open derived-target registration (the patch entry carries an
`alternative_route_open_derived_target` field describing this); P2-dependent rows
then go **open** rather than `retained_bounded` (§5).

---

## 2. Registry patch — summary

- **Remove** `kinetic_isotropy_primitive` from `axiom_premise_nodes.json`
  `canonical_ids` (line) and its `nodes` block. Approved-primitive count
  **3 -> 2** (`scale_reference_primitive`, `realized_state_primitive` remain;
  P1's keep-vs-convention status is left OPEN — see §7 — and is **not** moved by
  this patch).
- **Add** `kinetic_isotropy_renormalized_anisotropy_target_2026-06-21` to
  `tier_a_admissions.json` `canonical_ids` + `derivation_targets`, with the
  renormalized-`xi_R=1` statement (Karsch-coefficient renormalized dynamical
  tuning; B4-theorem-consistent residual; "free datum / cubic-adjacency
  analogue" withdrawn), and bump `genuine_admitted_input_count` **2 -> 3**.

The patch is the **registry-of-record** (admitted-input route). It carries an
in-entry `alternative_route_open_derived_target` and a `decision_reversal_note`.

---

## 3. Human-readable diff (mirror of the patch — for review without applying)

### `docs/audit/data/axiom_premise_nodes.json`

REMOVE from `canonical_ids`:

```
-    "kinetic_isotropy_primitive",
```

REMOVE the entire `nodes."kinetic_isotropy_primitive"` block:

```
-    "kinetic_isotropy_primitive": {
-      "current_path": "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
-      "aliased_paths": [ "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md" ],
-      "legacy_claim_ids": [],
-      "note": "Explicitly approved framework primitive for the space-time kinetic-form isotropy c_t=c_s ... Dependencies on this primitive chain-satisfy without bounding downstream rows."
-    },
```

Net: `canonical_ids` goes from 4 ids to 3; `nodes` loses one entry. Remaining
approved primitives: `scale_reference_primitive`, `realized_state_primitive`.

### `docs/audit/data/tier_a_admissions.json`

```
-  "genuine_admitted_input_count": 2,
+  "genuine_admitted_input_count": 3,
```

ADD to `canonical_ids`:

```
+    "kinetic_isotropy_renormalized_anisotropy_target_2026-06-21"
```

ADD `derivation_targets."kinetic_isotropy_renormalized_anisotropy_target_2026-06-21"`
(label `xi_R`): renormalized `xi_R=c_t/c_s=1` admitted-input statement (G-TIME /
G-DYN dependency; Euclidean/OS branch; `xi_R != xi_bare` Karsch; B4-consistent
tuning-to-surface + dim-6 residual), `class` = "renormalized anisotropy tuning
condition (demoted from approved primitive)", plus
`alternative_route_open_derived_target` and `decision_reversal_note` fields.

---

## 4. P2 demotion = explicit REVERSAL of the 2026-06-09 owner approval

This is **not housekeeping.** `AXIOM_MINIMALITY_POLICY.md` §6 (entry 2026-06-09)
and `axiom_premise_nodes.json` both record an explicit **owner approval** of
`kinetic_isotropy_primitive` *as a primitive*, on the stated ground that
`c_t = c_s` is "dimensionless **structural** ... of the same category as cubic
adjacency ... **not** dimensionless **dynamical** content." This changeset asserts
the **opposite**: `xi_R = c_t/c_s = 1` is a **renormalized** (`xi_R != xi_bare`,
Karsch-coefficient) **dynamical tuning condition** and the emergent-Lorentz
*output* — content a primitive may not carry.

Therefore adopting this changeset **reverses** the logged 2026-06-09 owner
approval. It **cannot land** without (a) the owner explicitly reversing that
approval and (b) the audit lane re-auditing. The `AXIOM_MINIMALITY_POLICY.md` §6
entry at adoption must record the removal of `kinetic_isotropy_primitive` from
the primitive class **as a reversal**, not as a routine sharpening.

---

## 5. Adoption consequences (downstream)

> These are the status changes that **would** follow adoption. This changeset
> adopts nothing; the audit lane sets all effective statuses.

1. **P2-dependent rows -> `retained_bounded` with active re-audit.** Every row
   whose only otherwise-clean dependency was `kinetic_isotropy_primitive`
   (emergent-Poincaré / kinetic-isotropy theorem cluster, staggered-Dirac
   kinetic-class rows, graviton-isotropy rows) **loses** its free chain-satisfy
   pass. On the admitted-input route they go **`retained_bounded`** (the
   admitted `xi_R` target bounds them); on the derived-target route they go
   **open**. Either way they must be **actively re-audited** — they must **not**
   be left silently at their old axiom-grade status (tier-honesty obligation;
   the registry move is honest only if the downstream ledger is refreshed in the
   same adoption).
2. **A3b consumers re-cite.** Rows that cited "Record" for the **`K`/CPT-orbit
   selector** (generation-sector-count usage; determinant/character
   phase-erasure rows leaning on the `K`/CPT orbit — e.g.
   `docs/P2_KCPT_ORBIT_TEMPORAL_FACTOR_NO_GO_2026-06-06.md`,
   `docs/THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`)
   must re-cite **A3b (conditional)** and carry `E` (center-producing map, via
   G-SECT), `K` (antiunitary existence), the K–E compatibility hypothesis (2′),
   the sector count `m`, and the realized configuration as explicit dependencies.
   Rows using only finite **additivity** keep citing A3a (axiom) and are
   **unaffected**.
3. **A2 Clifford-reading consumers re-audited.** Rows using Clifford generators /
   chirality / real-form conjugation drawn from "the `Cl(3,0)` reading of A2"
   must re-cite the labelled downstream identification and own those choices.
   `M_2(C)`-only rows unaffected.
4. **A1 isotropy-citation sweep.** Any row citing A1 as the source of
   **continuous** spatial isotropy or a Lorentz statement must be corrected; A1
   supplies only `B_3`/`O_h` + the (`O_h`-not-`SO(3)`) `L1` graph metric.
5. **New required-gate dependencies.** Rows using an evolution law, an emergent
   time direction, a center-producing superselection/coarse-graining map, record
   durability, or global-state-space structure beyond the bare factor now carry
   explicit **G-DYN / G-SECT / G-TIME / G-ARROW / G-COMPOSE** open-gate
   dependencies.
6. **Hash-guard re-audit (mechanical).** Editing `minimal_axioms` content
   invalidates prior direct `minimal_axioms` audits via the axiom-premise hash
   guard; all direct dependents re-audited by the independent lane.
7. **Net premise-count effect.** Axioms still 3 by name, but Record is now A3a
   (axiom) + A3b (conditional); approved primitives **3 -> 2** (P1's
   keep-vs-convention call still open, §7); **+5 explicit open gates**
   (G-DYN / G-SECT / G-TIME / G-ARROW / G-COMPOSE) that **replace silent
   presuppositions**. Honest premise content **decreases** while becoming
   auditable.

---

## 6. `AXIOM_MINIMALITY_POLICY.md` §6 update (at adoption)

Record: (a) removal of `kinetic_isotropy_primitive` from the primitive class
**as a reversal** of the logged 2026-06-09 owner approval (a science-level owner
decision, not housekeeping); (b) adoption of the nine first-principles
admissibility criteria (from `docs/FOUNDATION_REVISION_PROPOSAL_2026-06-20.md` §9)
as the admissibility test for future premise proposals; (c) that **no new axiom
is added** — the dynamics/time/center/composition gaps are flagged gates
(G-DYN / G-SECT / G-TIME / G-ARROW / G-COMPOSE), per policy §1/§4.

---

## 7. OPEN OWNER CHOICE — P1 keep-as-primitive vs reclassify-as-convention

Presented as an explicit open choice; **this changeset does not move P1** under
either framing.

- **Framing K (keep-as-primitive):** the Claude clean first-principles panel
  passed P1 cleanly and unanimously at primitive grade (optional hygiene only:
  abstract anchor `M_0`, `= M_Pl` to a gravity gate). P1 stays in
  `axiom_premise_nodes.json`.
- **Framing C (reclassify-as-convention):** the independent Codex cross-check
  flagged P1 as "mostly yes, but better as a convention" — a dimensionful anchor
  with no invariant dimensionless content carries no physical structure on its
  own; only an observable scale bridge (a load-bearing `= M_Planck`) would make
  it an admitted empirical input. Under this framing P1 leaves the
  approved-primitive class and is recorded as a convention (alongside `Y0`/`g0`).

Both framings agree the `= M_Pl` number must not be load-bearing. If the owner
selects Framing C, a **second** small registry patch (remove
`scale_reference_primitive` from `axiom_premise_nodes.json`; record it as a
convention in `tier_a_admissions.json` `conventions`) is needed — **not** drafted
here pending the owner's call, which would drop the approved-primitive count
further (2 -> 1).

---

## 8. Codex cross-check concordance

Two independent models (Claude clean first-principles panel; Codex / gpt-5.5
xhigh) **agree on the two load-bearing findings**:

- **A3 split** (`Record` FAIL -> A3a additivity axiom + A3b conditional
  realized-outcome identification; bare antiunitary `K`, not CPT).
- **P2 re-tier** (`kinetic_isotropy_primitive` FAIL -> demote from primitive to
  admitted input / derived target).

…and on the system-level **dynamics + time under-completeness** (Claude's
G-DYN / G-TIME / G-ARROW; Codex's "add dynamics or state kinematics-only" +
"define time before durability/kinetic-isotropy/CPT").

**Codex adds two items, both folded into this changeset:**

1. **Missing global composition / state-space** (Codex's **#1** change): sites'
   tensor composition + the infinite quasi-local `C*`-algebra / state space were
   **never stated**. Folded into the **Quantum axiom** as the
   composition/state-space clause (finite-region tensor product
   `A_R = M_{2^{|R|}}(C)`; quasi-local `C*`-algebra `A` = UHF/hyperfinite
   inductive limit; state = normalized positive functional on `A`) **and** added
   as gate **G-COMPOSE** for any structure beyond the bare factor `A` + its state
   space. (Note: `A` remains a **factor** — trivial center — so this composition
   clause does **not** by itself create the sectors A3b needs; G-SECT is still
   required.)
2. **P1 -> unit convention** (Codex one notch harsher than the Claude clean
   panel, which passed P1): presented as the explicit **OPEN OWNER CHOICE** in §7
   (keep-as-primitive vs reclassify-as-convention), with both framings stated.

Direction is identical across the two models; Codex is one notch harsher overall
(`unsound as a complete foundation` vs `needs_revision`).

---

## 9. What this changeset does NOT do

- Does **not** edit `docs/MINIMAL_AXIOMS_2026-06-05.md` (canonical memo intact).
- Does **not** edit `docs/audit/data/axiom_premise_nodes.json` or
  `docs/audit/data/tier_a_admissions.json` (changes emitted as the patch + §3
  diff only).
- Does **not** apply the registry patch, adopt the memo, set any audit status,
  reverse the 2026-06-09 approval, or move P1.
- Does **not** add a dynamics axiom (the gaps are flagged gates).

---

*End of changeset README. Adopt nothing without explicit owner approval recorded
in `docs/audit/AXIOM_MINIMALITY_POLICY.md` and the machine registry, and without
independent audit-lane review. `hypothetical_axiom_status: proposed`;
`proposal_allowed=false`.*
