# Audit Keystone Cycle-Break — Turn the Dependency Graph Into a DAG

**Date:** 2026-06-14
**Type:** meta
**Status:** audit-pipeline infrastructure repair. Sets **no** audit status,
changes **no** audit verdict, proves **no** physics claim. **Status authority:**
the independent audit lane only.
**Runner:** [`scripts/audit_keystone_cycle_break_certificate_2026_06_14.py`](../../scripts/audit_keystone_cycle_break_certificate_2026_06_14.py)
(`TOTAL: PASS=10 FAIL=0`; reproducible against the live committed graph).

## Problem

The audit lane builds a claim **dependency graph** from markdown notes: every
markdown link `[..](OTHER.md)` is treated as a load-bearing dependency edge
(`docs/audit/scripts/build_citation_graph.py`, `LINK_RE`). A row can only be
marked `ready` for audit once **all** its dependencies are at retained-grade,
so a mutual-dependency cycle (strongly-connected component, SCC) **permanently
blocks every row inside it** from ever becoming auditable. This is the single
structural blocker behind the audit backlog drain (see
[`AUDIT_UNLOCK_KEYSTONE_MAP_2026-06-06.md`](AUDIT_UNLOCK_KEYSTONE_MAP_2026-06-06.md)).

On `origin/main` (2026-06-14) the graph carried **two** non-trivial SCCs:

| SCC | size | max downstream fanout | cluster |
|---|---:|---:|---|
| keystone tangle | **219** | **1136** | staggered-Dirac gate / single-clock / observable-principle-P1 |
| hierarchy cluster | **10** | 12 | `hierarchy_alpha_lm_magnitude_delta0` open gate + its δ0 probes |

The 219-node tangle traps the framework's highest-fanout keystones, so the
keystone-first dispatch can **never reach them** until the cycle is cut.

## Diagnosis

Both SCCs were held together purely by **anachronistic pointer edges** — an
*older* note markdown-linking a *strictly later-dated* note. Each such link is
navigational, not a proof dependency, and the citing notes' **own prose says
so**:

- `single_clock …2026-05-03 → …axis_selection…2026-06-11`: *"The follow-up
  source … narrows the route."*
- `hierarchy …2026-05-30 → four δ0 probes …2026-06-11`: *"Two downstream
  probes (one-hop authorities for this sharpening only; **citation direction
  downstream → this gate**)."*
- `axiom_first_lattice_noether …2026-04-29 → staggered_dirac_realization_gate
  …2026-05-03`: *"The historical parent-identity alias … is no longer cited as
  retained one-hop authority … Registered Tier-A carrier route (… not retained
  authority)."*

## What was changed

The **minimal feedback-arc set restricted to pointer edges from source notes
that were unaudited at the time of the cut** — **six** edges across **three**
notes — was demoted
from markdown links to plain back-ticked filenames (visible text preserved,
hyperlink removed, so the builder no longer emits a dependency edge):

| from (unaudited) | demoted pointer to |
|---|---|
| `AXIOM_FIRST_LATTICE_NOETHER_THEOREM_NOTE_2026-04-29` | `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03` |
| `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03` | `SINGLE_CLOCK_AXIS_SELECTION_…_2026-06-11` |
| `HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30` | the four `HIERARCHY_DELTA0_…_2026-06-11` probes |

The cut was **deliberately routed onto then-unaudited source notes only**, and
onto **back-edges into** the gate rather than the gate's genuine **synthesis
dependencies on** its component sub-theorems (e.g. `gate →
staggered_dirac_physical_species_direct` and `gate → …substep4_labeling_no_go`
are real dependencies and are **kept**). Consequences, all verified by the
recompute pipeline at the time of the cut:

- **0** audit-status (verdict) changes;
- **0** effective-status changes (the formerly-trapped rows were already
  `unaudited`; the cut changes their *readiness*, not their status);
- **0** retained-grade demotions;
- **0** hash-drift re-audits (no audited note was edited);
- exactly the **6** named edges removed, **0** added; resulting graph is a
  **DAG** (`build_cycle_inventory.py`: `cycles: 0`).

## Methodology (how the cut was validated)

Every anachronistic intra-SCC edge (31 candidates) was independently
classified by a separate restricted-input reviewer (one per edge) as a
spurious **pointer** / Tier-A **carrier** (demote-eligible) versus a genuine
**load-bearing dependency** (keep), judged only against the citing note's own
prose. The graph math (Tarjan SCC + minimal feedback-arc set) then selected
the smallest pointer-only, unaudited-source cut that yields a DAG. One
classification (the hierarchy `→ b4_attachment` edge) was overridden to
`demote` after direct source review: it is cited identically to its three
already-demoted sibling probes in the same "N1: alternative routes checked"
list of an `open_gate` note, which documents — does not load-bearingly depend
on — its probes.

## Residual (explicitly NOT done here — follow-ups for the drain)

This change does the **minimal** unblock. It does **not** also clean up:

1. **14 further spurious pointer/Tier-A edges from unaudited notes** (CKM,
   PMNS, dm-neutrino, EW, yt-color, and the gate's own `→ ac_phi_lambda` /
   `→ closure_synthesis` pointers) that the classification pass flagged but
   that are not on any remaining cycle. They are graph hygiene, not blockers.
2. **3 spurious edges that originate in *audited_clean* notes** (`cpt_stretch
   → gate`, `pmns_twisted → gate`, `yt_ward → gate`). Demoting these would
   reset clean keystones to `unaudited` via hash-drift, which is
   counterproductive; they should be cleared during those rows' own re-audit
   via the standard `pre_audit_prose_fix` hash-refresh envelope.

## Scope / non-claims

- Sets **no** audit status and changes **no** verdict. It removes spurious
  graph wiring so the independent audit lane can reach the keystones.
- Does **not** assert any keystone will pass audit — only that auditing it is
  now structurally possible (it is no longer trapped in a cycle).
- No physics claim; no new axiom; no import. Reproved by the certificate
  runner; cross-referenced to the 2026-06-06 keystone map for the diagnosis.
