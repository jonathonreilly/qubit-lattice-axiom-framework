# Meron Half-Action Algebra Core From Topological Infrastructure

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support. This note derives only the
action algebra core `S_half = 4*pi^2/g^2` from the bounded topological
instanton infrastructure and an explicit half-charge sector input. It does not
derive the meron regulator, cap, twist, patching, existence, or framework
substrate bridge.
**Trace class:** upstream_support
**Reachability to target:** supports
**Proposal allowed:** false
**Bare retained allowed:** false
**Audit required before effective retained:** true

**Primary runner:** [`scripts/meron_half_action_core_split_2026_06_18.py`](../scripts/meron_half_action_core_split_2026_06_18.py)
**Cached output:** [`logs/runner-cache/meron_half_action_core_split_2026_06_18.txt`](../logs/runner-cache/meron_half_action_core_split_2026_06_18.txt)

## Purpose

The audited parent row
[`MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md`](MERON_HALF_INSTANTON_4PI2_OVER_G2_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-16.md)
was conditional because it mixed a closed half-action algebra calculation with
an open boundary-construction gate. This note splits out the closed algebraic
core.

The open parent gate remains: a framework or external meron/fractional
instanton use still needs a regulator, cap, twist, or patching construction
that supplies a legitimate half-charge sector and action saddle. This note is
not that construction.

## Inputs

| ID | Input | Status |
|---|---|---|
| TIA | [`TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md`](TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md) | bounded Hodge/Bogomolny, BPST `8*pi^2`, and twisted-`T^4` `Q=k/N` arithmetic certificate |
| QH | Half-charge sector value `|Q| = 1/2` | explicit sector input for this action-core calculation; not a proof of meron existence or framework realization |
| YM | Standard Euclidean Yang-Mills action/topological normalization used by TIA | admitted normalization inside the bounded infrastructure certificate |

## Theorem

Assume the bounded topological-instanton infrastructure normalization:

```text
S_E >= (8*pi^2/g^2) |Q|
```

and assume a supplied boundary-conditioned half-charge sector:

```text
|Q| = 1/2.
```

Then the corresponding action scale in this normalization is exactly:

```text
S_half = (8*pi^2/g^2) * (1/2) = 4*pi^2/g^2.
```

Equivalently, if `S_inst = 8*pi^2/g^2` is the supplied charge-one BPST
normalization, then

```text
S_half = (1/2) S_inst.
```

This is finite algebra over the bounded infrastructure normalization and the
explicit `|Q| = 1/2` sector value. It does not prove that any particular
singular meron, meron pair, capped core, twisted lattice configuration, or
framework carrier realizes that sector.

## Numerical Checks

For `g^2 in {1/2, 1, 2}`:

| `g^2` | `S_half` |
|---:|---:|
| `1/2` | `8*pi^2` |
| `1` | `4*pi^2` |
| `2` | `2*pi^2` |

At `g^2 = 1`, `S_half = 4*pi^2 ~= 39.4784176044`.

## Firewalls

This note may be cited only for the half-action algebra core:

```text
bounded topological-instanton normalization + supplied |Q|=1/2
  => S_half = 4*pi^2/g^2.
```

It must not be cited as:

- retained meron existence;
- retained fractional-instanton existence;
- a finite-action theorem for the singular unregularized meron on `R^4`;
- a regulator, cap, twist, or patching construction;
- a framework substrate or observable bridge;
- closure of `alpha_LM^16`, `v/M_Pl`, hierarchy formulas, or any physical
  scale-ratio claim.

## Validation

Run:

```bash
PYTHONPATH=scripts python3 scripts/meron_half_action_core_split_2026_06_18.py
```

Expected:

```text
TOTAL: PASS=19 FAIL=0
```
