# Staggered Dirac Kawamoto-Smit Conditional Realization Rescoping Companion

**Date:** 2026-06-03
**Claim type:** bounded_theorem.
**Runner:** `scripts/frontier_staggered_dirac_kawamoto_smit_conditional_realization_rescoping_companion_verifier.py`.

This companion rescopes the older Kawamoto-Smit forcing statement to a
conditional realization. It does not edit the parent note and does not derive a
new axiom or primitive.

## Conditional Premise

The load-bearing premise is:

```text
H_staggered_chirality:
omega(x) = epsilon(x) omega_global,
epsilon(x) = (-1)^(x_1 + x_2 + x_3).
```

This identifies the local chirality sign with the bipartite lattice parity.
It is a useful and standard-looking staggered choice, but it is an explicit
conditional premise here, not a theorem of Lattice + Quantum + Record.

## Rescoped Statement

Given `H_staggered_chirality`, the finite Kawamoto-Smit phases are

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

The companion does not claim that the staggered chirality assignment is forced.
It only says that, once that assignment is supplied, the standard
Kawamoto-Smit phase surface is internally consistent on the tested finite
lattice samples.

## No-Go Discipline Gate

This gate applies to the narrow negative statement: the baseline axioms do not
by themselves force `H_staggered_chirality`.

### N1 - Alternative route enumeration

| Route | What it attempts | Result |
| --- | --- | --- |
| Local pseudoscalar route | Use the one-site central chirality to force site parity. | Fails for forcing: the one-site object does not choose a site-dependent sign field. |
| Bipartite route | Use `Z^3` bipartition to force chirality. | Narrows only to availability of `epsilon(x)`, not identification with `omega(x)`. |
| Fermion-parity route | Use fermion parity grading to select the staggered sign. | Does not choose between constant, inverse, or staggered local assignments. |
| Naturalness route | Treat the standard staggered assignment as canonical. | Naturalness is not derivation. |
| Gauge route | Use global phase freedom to remove ambiguity. | Global phase does not remove the local parity-assignment choice. |
| Conditional-premise route | State `H_staggered_chirality` explicitly. | Succeeds as the bounded conditional route taken here. |

### N2 - Wall Independence

The collapsed wall set is one premise: `H_staggered_chirality`. Other gauges and
boundary conventions are downstream equivalences, not independent derivation
walls in this companion.

### N3 - Hidden-Wall Scan

The word "standard" is non-load-bearing. The load-bearing sign assignment is
named explicitly as `H_staggered_chirality`.

### N4 - Residual Matching

The residual is exactly the Step-3 chirality/parity identification. This note
does not claim to settle unrelated staggered-Dirac realization gates.

### N5 - Rhetoric Audit

The negative statement is restricted to "not forced by the baseline axioms."
The conditional realization remains useful.

### N6 - Partial-Closure Path Scan

An owner-approved admission, a future derivation from a stronger dynamics, or a
parent rewrite could close the premise. Approved axioms and primitives
chain-satisfy dependencies but are not grade sources for this conditional.

### N7 - Steelman

A hostile reviewer can argue that the staggered assignment is the unique local,
translation-covariant choice compatible with the desired continuum taste
structure. That may be a route for a future theorem, but it is not proved here.

### N8 - Cross-Cycle Echo

The framework has repeatedly repaired forcing claims by isolating the exact
conditional input. This companion follows that pattern: state the input and
verify the conditional realization.

**Gate result:** pass for the narrow conditional rescoping only.
