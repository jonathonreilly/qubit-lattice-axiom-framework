# Staggered Dirac Kawamoto-Smit Conditional Realization Rescoping Companion

**Date:** 2026-06-03; 2026-06-06 chirality-parity bridge repair
**Claim type:** bounded_theorem.
**Runner:** `scripts/frontier_staggered_dirac_kawamoto_smit_conditional_realization_rescoping_companion_verifier.py`.

This companion rescopes the older Kawamoto-Smit forcing statement to a narrow
bounded realization. It does not edit the parent note and does not derive a new
axiom or primitive.

## 2026-06-06 repair: chirality-parity bridge

The prior version of this companion made the sign assignment

```text
H_staggered_chirality:
omega(x) = epsilon(x) omega_global,
epsilon(x) = (-1)^(x_1 + x_2 + x_3).
```

an explicit conditional premise. The 2026-06-06 repair replaces that free
premise with the narrow chirality-parity bridge
[`STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md`](STAGGERED_DIRAC_CHIRALITY_PARITY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md).
That bridge proves that the scalar nearest-neighbor edge-flip grading on the
`Z^3` coordinate graph is unique up to global sign and equals
`epsilon(x)=(-1)^(x_1+x_2+x_3)`. Combining this sign field with the A1
central pseudoscalar `omega_global=sigma_1 sigma_2 sigma_3=i I` gives
`omega(x)=epsilon(x) omega_global`.

This is a source-side bridge for the specific missing `H_staggered_chirality`
premise. Independent audit still decides whether the updated packet is clean.
The bridge does not close the full staggered-Dirac realization gate,
Grassmann/CAR forcing, or the physical species-label bridge.

## Rescoped Statement

Given the chirality-parity bridge above, the finite Kawamoto-Smit phases are

```text
eta_1(x) = 1,
eta_2(x) = (-1)^x_1,
eta_3(x) = (-1)^(x_1+x_2).
```

The runner verifies on representative `Z^3` sites that:

- `epsilon(x)` flips on nearest-neighbor links;
- the staggered chirality relation gives
  `omega(x) gamma_mu omega(x+e_mu)^(-1) = -gamma_mu` at the scalar sign level;
- the three displayed `eta_mu` functions are stable under the checked global
  phase gauge.

## Boundaries

The companion now claims the narrow scalar chirality sign field is derived by
the branch-local bridge. It still does not claim that the full staggered-Dirac
realization is forced. The result remains bounded to the phase/sign surface:
the complete Grassmann/CAR realization, physical kinetic operator selection,
and species-label interpretation remain outside this packet.

## No-Go Discipline Gate

This gate is retained as a residual scan for the broader forcing rhetoric. The
2026-06-06 bridge resolves the narrow `H_staggered_chirality` sign-field
premise inside this packet; it does not resolve the broader claim that the
baseline axioms force the complete staggered-Dirac realization.

### N1 - Alternative route enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Local pseudoscalar route | Use the one-site central chirality to force site parity. | Fails for forcing: the one-site object does not choose a site-dependent sign field. |
| Bipartite route | Use `Z^3` bipartition to force chirality. | Narrows only to availability of `epsilon(x)`, not identification with `omega(x)`. |
| Fermion-parity route | Use fermion parity grading to select the staggered sign. | Does not choose between constant, inverse, or staggered local assignments. |
| Naturalness route | Treat the standard staggered assignment as canonical. | Naturalness is not derivation. |
| Gauge route | Use global phase freedom to remove ambiguity. | Global phase does not remove the local parity-assignment choice. |
| Bridge route | Derive `H_staggered_chirality` as the unique scalar nearest-neighbor edge-flip grading on `Z^3`, multiplied by the A1 central pseudoscalar. | Succeeds for the narrow sign-field bridge; does not close the full gate. |

### N2 - Wall Independence

The collapsed wall set is now outside this sign-field bridge: full
staggered-Dirac realization, Grassmann/CAR forcing beyond the cited bounded
support, and species-label identification. Other gauges and boundary
conventions are downstream equivalences, not independent derivation walls in
this companion.

### N3 - Hidden-Wall Scan

The word "standard" is non-load-bearing. The load-bearing sign assignment is
now carried by the chirality-parity bridge and the runner's finite
linear-algebra edge-flip uniqueness check.

### N4 - Residual Matching

The prior Step-3 chirality/parity residual is the target of the new bridge.
This note does not claim to settle the full staggered-Dirac realization gate.

### N5 - Rhetoric Audit

The negative statement is restricted to "the full staggered-Dirac realization
is not closed here." The sign-field bridge is positive exact support inside
this narrower packet.

### N6 - Partial-Closure Path Scan

The sign-field premise has a branch-local bridge. The remaining partial-closure
paths are audit of that bridge, audit of the broader staggered-Dirac gate, or a
separate species-label admission/derivation.

### N7 - Steelman

A hostile reviewer can still argue that deriving the scalar sign field is not
the same as deriving the whole kinetic operator or physical taste structure.
This companion accepts that boundary and claims only the sign/phase surface.

### N8 - Cross-Cycle Echo

The framework has repeatedly repaired forcing claims by isolating the exact
conditional input. This companion follows that pattern and then adds the narrow
bridge for that input, while keeping the larger gate outside this packet.

**Gate result:** pass for the narrow sign/phase rescoping only; the full
staggered-Dirac realization gate remains open outside this companion.
