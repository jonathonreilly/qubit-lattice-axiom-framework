## What changed

- Reworked the target note into a scope-pinned external physical-input bridge
  for the high-temperature minimal-Standard-Model inventory.
- Registered exact Husdal and Giovannini authority items with an explicit
  `scope_pinned_external_physical_input` role and zero pre-audit premise
  weight.
- Strengthened the paired runner so it parses the note's inventory rows,
  validates every factor and displayed count, checks exact source locators and
  thermal boundaries, consumes the retained `7/8` dependency, and computes
  `427/4 = 106.75`.
- Added a branch-local physics-loop handoff, trace gate, import audit,
  literature bridge, review history, and claim-status certificate.

## Why

The current `audited_conditional` verdict accepted the finite arithmetic but
identified one missing bridge: the Standard Model state multiplicities and
their interpretation as relativistic thermal states were anonymous external
inputs. This block supplies exact one-hop literature authority within a narrow
ideal-gas/equilibrium/electroweak-restored scope while preserving the boundary
that the particle inventory is not framework-derived.

## Honest status and scope

Status is **exact-support**. Independent audit is still required; this PR does
not author an audit verdict or effective retained status.

In scope: minimal SM with three generations, one complex Higgs doublet, no
thermally populated sterile/right-handed neutrinos, zero-chemical-potential
equilibrium ideal plasma, ultrarelativistic species, and restored electroweak
symmetry.

Excluded: interaction and finite-mass corrections, thresholds/decoupling, BSM
states, arbitrary-temperature applicability, framework derivation of the SM
inventory, and downstream leptogenesis closure.

## Artifacts

- [Target note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/docs/SM_RELATIVISTIC_DOF_COUNT_IMPORT_NOTE_2026-05-17.md)
- [Runner](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/scripts/frontier_sm_relativistic_dof_finite_inventory.py)
- [Handoff](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/.claude/science/physics-loops/sm-relativistic-dof-count-import-closure/HANDOFF.md)
- [Trace gate](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/.claude/science/physics-loops/sm-relativistic-dof-count-import-closure/TRACE_GATE.md)
- [Assumptions and imports](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/.claude/science/physics-loops/sm-relativistic-dof-count-import-closure/ASSUMPTIONS_AND_IMPORTS.md)
- [Literature bridges](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/.claude/science/physics-loops/sm-relativistic-dof-count-import-closure/LITERATURE_BRIDGES.md)
- [Review history](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/.claude/science/physics-loops/sm-relativistic-dof-count-import-closure/REVIEW_HISTORY.md)
- [Claim-status certificate](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/claude/science-fix/sm_relativistic_dof_count_import_note_2026-05-17-80f2235f/.claude/science/physics-loops/sm-relativistic-dof-count-import-closure/CLAIM_STATUS_CERTIFICATE.md)

## Verification

- Target runner: `PASS=94 FAIL=0`
- SHA-pinned runner cache: fresh
- Authority registry companion: `PASS=25 FAIL=0`
- Mutation tests: wrong gluon count, wrong `427/4`, and invalid DOI target each
  force runner failure
- Physics/import post-fix review: PASS
- Code/proof post-fix review: PASS
- Governance/audit post-fix review: PASS
- Full audit pipeline plus strict audit lint: no errors
- Vocabulary lint, Python compile, JSON parse, portable-link gate, and
  `git diff --check`: PASS
- Generated audit ledger/queue/publication outputs were used for validation
  only and are not included in this framework PR

## Remaining action

Independently inspect the cited source items and re-audit the same target note
with the refreshed runner packet.
