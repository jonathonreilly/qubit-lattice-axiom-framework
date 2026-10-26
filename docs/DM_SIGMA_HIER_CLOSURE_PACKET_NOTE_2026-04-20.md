# DM Sigma-Hier Closure Packet

**Type:** meta

**Date:** 2026-04-20  
**Lane:** DM A-BCC sigma-chain / hierarchy-permutation ambiguity  
**Status:** historical proof-chain inventory with current authority withdrawn.
**Current scope:** supplied finite comparisons and named open premises only.
The following historical chain is retained for recovery, not asserted as a
current theorem. Exact chamber exhaustion, physical filter/row selection and
`I12` closure are unestablished in this source packet, not proved impossible.

## What this packet is for

This package contains both:

- an intermediate reduction note,
- and later notes that proposed closing the hierarchy-permutation ambiguity.

This packet records the proposed chain and withdraws its current authority.
The two linked current owners now support only finite supplied diagnostics.
The quoted historical conclusions below cannot be imported as current premises.

## Historical proposed proof chain (not established here)

### 1. Chamber completeness is explicit

Per
[DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md](./DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_THEOREM_NOTE_2026-04-20.md),
the exact active-chamber `chi^2 = 0` set is

```text
{Basin 1 on sigma=(2,1,0), Basin 2 on sigma=(2,1,0), Basin X on sigma=(2,0,1)}.
```

So the active chamber ambiguity is reduced to these explicit survivors.

### 2. The old parity note is only an intermediate reduction

Per
[DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md](./DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md),

```text
J_sigma = parity(sigma) * I_src(H) / Delta,
I_src(H) = Im(H_12 H_23 H_31).
```

That note is important, but it does **not** by itself close the
hierarchy-permutation ambiguity. It only reduces the ambiguity to one parity
bit.

### 3. First actual closeout theorem: upper-octant + source cubic

Per
[DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md](./DM_PMNS_UPPER_OCTANT_SOURCE_CUBIC_SELECTOR_THEOREM_NOTE_2026-04-20.md),
the coefficient-free selector system

```text
sin^2(theta_23) > 1/2,
I_src(H) > 0
```

selects Basin 1 uniquely on the exact chamber root set. Therefore

```text
Basin 1  =>  sigma_hier = (2,1,0)  =>  sin(delta_CP) < 0.
```

This already closes the hierarchy-permutation ambiguity on the active
chamber.

### 4. Cleaner reformulation of the same closure

Per
[DM_SIGMA_HIER_UPPER_OCTANT_SELECTOR_THEOREM_NOTE_2026-04-20.md](./DM_SIGMA_HIER_UPPER_OCTANT_SELECTOR_THEOREM_NOTE_2026-04-20.md),
the closure can be packaged even more cleanly at the pinned chamber point.

The two `9/9`-magnitude-passing permutations are exactly

```text
(2,0,1), (2,1,0).
```

They preserve `sin^2(theta_12)` and `sin^2(theta_13)`, send

```text
sin^2(theta_23) <-> 1 - sin^2(theta_23),
```

and flip the CP sign.

The exact chamber threshold theorem gives

```text
sin^2(theta_23)_min = 0.540969817889... > 1/2.
```

At the pin:

```text
sigma=(2,0,1): sin^2(theta_23) = 0.455000028664... < 0.540969817889...
sigma=(2,1,0): sin^2(theta_23) = 0.544999971336... > 0.540969817889...
```

So only

```text
sigma_hier = (2,1,0)
```

is chamber-compatible. Then

```text
sin(delta_CP) < 0
```

follows automatically.

## Current boundary

The hierarchy-permutation ambiguity is not closed by this packet. The chamber
owner does not certify exact roots or exhaustion; the source-cubic owner
compares three supplied points and stipulated filters. A labeled row-swap
identity does not supply a physical row assignment. The other linked threshold
and selector arguments are preserved for future validation, not accepted here
as independent completion of those missing premises.

The old threshold and pin values above remain historical numerical statements.
They are not new certified enclosures or evidence of a physical selection law.
No impossibility theorem for those open routes is inferred.

## Historical reproduction references

The following commands and counts belong to the historical proposal; they do
not establish its closure claim or represent current cache freshness:

```bash
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py
PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_upper_octant_source_cubic_selector_theorem_2026_04_20.py
PYTHONPATH=scripts python3 scripts/frontier_dm_sigma_hier_upper_octant_selector_theorem_2026_04_20.py
```

Expected:

```text
PASS=11 FAIL=0
PASS=14 FAIL=0
PASS=14 FAIL=0
```

Complete original packet source is preserved at `a8151fb8e39df04925316bedb745a0aa4f36e333` and in repair evidence. This withdrawal changes no numeric predicate, audit verdict or ledger.
