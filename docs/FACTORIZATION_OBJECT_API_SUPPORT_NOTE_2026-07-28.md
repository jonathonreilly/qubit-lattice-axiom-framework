# Factorization-object API — support note

Date: 2026-07-28

Authority: none

Audit: unset

Status: exact finite-box support contract

Claim type: bounded_theorem

Runner:

- [`frontier_factorization_object_api_2026_07_28.py`](../scripts/frontier_factorization_object_api_2026_07_28.py)

Constitutional effect: none. This module changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status, and it derives no physics.

## What it provides

The landed [Cycle-720 mixed-gauge factorization source
note](RECURRENT_COMPANION_PHYSICAL_M2_UPDATE_LOCAL_CHOI_PREPARATION_CYCLE720_BOUNDED_THEOREM_NOTE_2026-07-27.md)
and its [factorization
runner](../scripts/frontier_cycle720_companion_subsystem_mixed_gauge_factorization_2026_07_27.py)
build a canonical tableau transiently and return only metrics and a
SHA-256 digest. No public API there exposes the encoded generators or
coordinates. This module reconstructs that factorization through the
landed runner's public helpers, following its exact recipe, and returns
one frozen `FactorizationObject`: ordered signed W/V rows for the
physical and target frames; logical/gauge/center counts with the
parity-last convention; per-dictionary-row decoded coordinates; and the
physical-tableau digest.

Binding contract: the reconstruction must reproduce
`F.phase_fixed_factorization(shape)["tableau_digest"]` exactly, or it
raises. That landed digest binds the ordered physical signed-tableau
serialization only. Separate self-test assertions bind source-row
identity, target coordinates, parity-sector phases, and the cross-frame
intertwiner contract. No Cycle-720 file is modified.

## Verified at self-test

Literal digest and count oracles on all seven landed fixtures from
`(2,1,1)` through `(5,3,2)`; dimension and dictionary-cardinality
identities; signed physical and target replay of every dictionary row;
exact source index/family/row association; equality of physical and
target logical coordinates; zero gauge coordinates; parity-last mapping;
even/odd phase formulas and cross-frame phase equality; deep
frozen-dataclass immutability; and build determinism.

## Boundary

Exact finite-box support only: no new physics, no existing claim-status
change, and no landed-source edit. A literal `V_s`-restriction input
compiler remains outside this note, and the linked Cycle-720 source
records that its exhibited canonical tableau is not radius-two bounded on
the tested boxes. Only the independent audit lane may assign this new
claim an audit or effective status.
