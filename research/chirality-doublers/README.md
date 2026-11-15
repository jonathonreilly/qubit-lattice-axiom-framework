# Chirality, doublers and mirror removal: notes on supplied models

Date: 2026-11-14

This is working research on supplied models. It has no audit-ledger rows and no
audit status. Landing it grants no standing. The rule is the row "Research
sections" in `docs/ai_methodology/SETTINGS.md`. Every statement here is argued,
not checked.

## Why these notes are here

The notes came to `docs/` in PR 10131, which consolidates chirality and doubler
results. Its second landing hold (2026-11-14, finding R8) marked them as
mathematics on supplied walks, Hamiltonians or historical candidate rules. No
framework axiom contributes a proof step to them, and some say that the axioms
choose none of the models. Under the SETTINGS row such work lands here. Each
note moved with its runner. The move itself changes no statement. Each note's
earlier repairs are recorded in the note and in the navigation map.

The notes of the same PR that compare a model with the framework axioms stay
under `docs/`. The navigation map
[`docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`](../../docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md)
lists every carried note with its current scope, wherever it lives.

## Words used here

- Frontmatter fields such as `claim_type: bounded_theorem` and
  `upstream_dependencies` are the source notes' working labels. They grant
  nothing here. The entries `minimal_axioms` and `candidate_laws` record what
  the source cited, not a proof step.
- "The register", "CL-1" and similar labels are source labels. Each note
  defines them locally. None is a clause of the current
  `docs/CANDIDATE_LAWS.md`.

## Parts, verification and open obligations

Every part has a compute check: its runner in this folder. Run it from the
repository root, for example
`python3 research/chirality-doublers/tick_update_winding_fixes_net_cone_chirality_at_quasi_energy_zero_and_pi_2026_10_21.py`.
Each runner declares `AUDIT_TIMEOUT_SEC`, prints PASS or FAIL for each check,
and exits nonzero on any failed check. Its committed cache is
`logs/runner-cache/<runner stem>.txt`, which pins the runner and its note by
content hash. A runner checks finite or exact instances of its note's
statements. It does not check the outside inputs listed as open obligations.

| Part | Statement, in short | Verification | Open obligations |
|---|---|---|---|
| [#9863 winding and cones](TICK_UPDATE_WINDING_FIXES_NET_CONE_CHIRALITY_AT_QUASI_ENERGY_ZERO_AND_PI_BOUNDED_THEOREM_NOTE_2026-10-21.md) | For supplied SU(2) walks on Z^3, the local-degree sums at quasi-energy 0 and pi equal -W3; they are Weyl-cone counts when every preimage is nondegenerate; coin and coin-conditioned-shift products have W3 = 0; a supplied quasi-local walk has one cone at 0 | Compute check, 13 checks. Check 4b tests nondegeneracy on every walk used. Check 4c keeps the counterexample and fails if the flattening is removed. Check 4d tests the excluded masses | Whether every finite-range walk has W3 = 0: the source cited SK1(C[Z^3]) = 0 with no checked statement, and nothing here reads it |
| [#9895 record and feedback histories](RECORD_AND_FEEDBACK_HISTORIES_OF_BLOCK_TICKS_HAVE_ZERO_FLOW_INDEX_BOUNDED_THEOREM_NOTE_2026-10-21.md) | Histories of supplied block ticks and frames have flow 0, whatever selects the factors; periodic histories have W3 = 0 | Compute check, 20 checks; the N_nu comparison prints as an uncounted conditional estimate | Integrality of the index (GNVW, Avron-Seiler-Simon), read by the averaging bound; Stinespring uniqueness, read by the register bypass; a proof of the magnetic flow identity, checked numerically only |
| [#9896 wall, pump and mirror-gapping routes](WALL_PUMP_AND_MIRROR_GAPPING_ROUTES_TO_CHIRALITY_UNDER_THE_CANDIDATE_LAWS_BOUNDED_THEOREM_NOTE_2026-10-21.md) | Under the source notes' update rules: the zoom keeps W3; the step pi/2 tick has index 0; circuits of block-local gates have W3 = 0; no free history gaps the mirror alone | Compute check, 17 checks; the estimate line D1 prints uncounted | Non-circuit finite-range unitaries (SK1, not read); 't Hooft anomaly matching for the interacting mirror-gapping step; the existence of a gapped symmetric mirror phase; any interacting test |
| [#9911 light copy and released doublers](LIGHT_COPY_EXACTLY_MASSLESS_YET_MIRROR_GAPPING_RELEASES_VECTOR_LIKE_DOUBLERS_BOUNDED_THEOREM_NOTE_2026-10-21.md) | For the supplied block Hamiltonian, the light copy is exactly decoupled at K = 0 and R, and a gapped mirror leaves 4 left- and 4 right-handed light nodes per sublattice | Compute check, 20 checks; the E1 and E4 estimate lines are labelled | 't Hooft anomaly matching (Statement 2); the Golterman-Shamir hypotheses away from the endpoint; the source's cell-chain formulas behind C1; an interacting infinite-volume mirror gap |

## Provenance

The source notes, runners and caches credit Anthropic Claude Opus 5.5 (the
first landing review retrieved every source commit). The consolidation is
commit a1bced899 on branch `docs/consolidate-chirality-doublers`. The repairs
are commits adc209b31, 4cdc8224d, 54673dd6f and the commits of 2026-11-14
that answer the second hold. They record Anthropic Claude Opus 5.5 in their
Provenance trailers. Two landing reviews by OpenAI gpt-6-astra (low effort),
on 2026-11-13 and 2026-11-14, held the PR. This provenance assigns no standing.

## Index row

`research/README.md` lists the sections. That file is not on this branch's
base, so adding it here would conflict with `main`. When this section lands,
its row is:

```text
| [chirality-doublers/](chirality-doublers/README.md) | Supplied-model notes on chirality, doublers and mirror removal from PR 10131 | compute checks, one runner per part, each exits nonzero on a failed check; open obligations listed there |
```
