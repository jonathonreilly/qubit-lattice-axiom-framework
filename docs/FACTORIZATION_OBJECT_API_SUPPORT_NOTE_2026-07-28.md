# Factorization-object API — support note

Date: 2026-07-28

Authority: none

Audit: unset

Status: exact support (infrastructure)

Claim type: meta

Runner:

- [`frontier_factorization_object_api_2026_07_28.py`](../scripts/frontier_factorization_object_api_2026_07_28.py)

Constitutional effect: none. This module changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status, and it derives no physics.

## What it provides

The landed Cycle-720 mixed-gauge factorization
(`frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py`)
builds its canonical tableau transiently and returns only metrics and a
SHA-256 digest; no public API exposes the encoded generators or
coordinates, which has kept the `V_s`-restriction input compiler open
since Cycle 721. This module reconstructs the factorization through the
landed module's own public helpers, following its exact recipe, and
returns one frozen `FactorizationObject` (ordered signed W/V rows for the
physical and target frames; logical/gauge/center counts with the
parity-last convention; per-dictionary-row decoded coordinates; the
tableau digest).

Binding contract: the reconstruction must reproduce
`F.phase_fixed_factorization(shape)["tableau_digest"]` exactly, or it
raises — byte-faithfulness is anchored by the landed digest, and no
Cycle-720 file is modified (their receipts pin their bytes).

## Verified at self-test

Digest equality on `(2,2,2)`, `(3,2,2)`, `(3,3,2)` (`e83b7b24...`,
`10ec1180...`, `5850ef...`); dimension identities against the landed
counts (`47+19+6=72`, `71+27+10=108`, `107+38+17=162`); signed coordinate
replay of every dictionary row; frozen-dataclass immutability; build
determinism.

## Boundary

Exact support infrastructure only: no new physics, no claim-status
change, no landed-file edit. Its intended consumer — a literal
`V_s`-restriction input compiler — remains open, with the measured
locality ceiling (canonical tableau not radius-two bounded on the tested
boxes) recorded in the Cycle-721 note. Independent audit governs any
future use.
