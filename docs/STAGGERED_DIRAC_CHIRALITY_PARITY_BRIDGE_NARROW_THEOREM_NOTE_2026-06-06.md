# Staggered-Dirac Chirality-Parity Bridge Narrow Theorem Note

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Runner:** [`scripts/staggered_dirac_chirality_parity_bridge_2026_06_06.py`](../scripts/staggered_dirac_chirality_parity_bridge_2026_06_06.py)
**Cached output:** [`logs/runner-cache/staggered_dirac_chirality_parity_bridge_2026_06_06.txt`](../logs/runner-cache/staggered_dirac_chirality_parity_bridge_2026_06_06.txt)

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This source-side bridge retires the free H_staggered_chirality sign-field premise for the Kawamoto-Smit rescoping companion. It does not close the full staggered-Dirac realization gate or propose an audit-effective retained status."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Targeted Blocker

The conditional audit of
`STAGGERED_DIRAC_KAWAMOTO_SMIT_CONDITIONAL_REALIZATION_RESCOPING_COMPANION_NOTE_2026-06-03.md`
identified one load-bearing premise:

```text
H_staggered_chirality:
Omega(x) = epsilon(x) Omega_global,
epsilon(x) = (-1)^(x_1+x_2+x_3).
```

This note supplies the narrow bridge for that premise. It does not prove the
full staggered-Dirac realization gate, the physical species-label bridge, or a
numerical value.

The companion note above is referenced as the **consumer this bridge serves**,
not as a proof input: this theorem's `epsilon(x)` uniqueness result is
self-contained on the `Z^3` coordinate-edge graph and consumes none of that
note's content. The reference is therefore a plain (non-link) citation, so the
genuine one-directional dependency (companion → this bridge, which retires the
companion's free `H_staggered_chirality` premise) does not form a spurious
audit-graph 2-cycle.

## Theorem

Let `Z^3` carry its nearest-neighbor coordinate-edge graph. Let `s(x)` be a
scalar `Z_2` sign field satisfying the edge-flip condition

```text
s(x+e_mu) = -s(x)  for each coordinate direction mu.
```

Then, on every connected component of the nearest-neighbor `Z^3` graph,

```text
s(x) = s(0) (-1)^(x_1+x_2+x_3).
```

Thus, after the basepoint orientation choice `s(0)=+1`, the unique scalar
nearest-neighbor chirality grading is

```text
epsilon(x) = (-1)^(x_1+x_2+x_3).
```

Axiom 1 supplies the per-site `Cl(3)` pseudoscalar

```text
Omega_global = sigma_1 sigma_2 sigma_3 = i I_2
```

up to the global orientation sign. Therefore the local staggered chirality
field forced by the scalar nearest-neighbor edge-flip grading is

```text
Omega(x) = epsilon(x) Omega_global.
```

Equivalently, multiplication by `epsilon` anticommutes edgewise with every
nearest-neighbor odd kinetic stencil:

```text
Gamma_epsilon D + D Gamma_epsilon = 0
```

for arbitrary link weights on coordinate nearest-neighbor edges.

## Proof

For any path from `0` to `x`, the edge-flip rule changes the sign once for
each coordinate step. The parity of the number of steps is
`x_1+x_2+x_3 mod 2`, independent of the chosen coordinate path because every
coordinate square has four edges and hence an even number of flips. This gives
`s(x)=s(0)(-1)^(x_1+x_2+x_3)`.

The Pauli realization of the A1 local `Cl(3)` carrier has
`sigma_1 sigma_2 sigma_3 = i I_2`, which is central. Multiplying that central
pseudoscalar by the unique normalized scalar edge-flip grading gives
`Omega(x)=epsilon(x) Omega_global`.

For a nearest-neighbor kinetic matrix `D`, every nonzero entry connects
opposite parity sites, so

```text
(Gamma_epsilon D + D Gamma_epsilon)_{xy}
  = (epsilon(x)+epsilon(y)) D_{xy}
  = 0.
```

The runner checks the finite linear-algebra certificate for open boxes,
the central Pauli pseudoscalar identity, and the edgewise anticommutation
formula for arbitrary sample weights.

## Boundary

This bridge is intentionally narrower than the full staggered-Dirac gate:

- it derives the `H_staggered_chirality` sign field used by the
  Kawamoto-Smit rescoping companion;
- it does not force Grassmann/CAR statistics rather than a compatible
  hard-core boson presentation;
- it does not derive the whole staggered kinetic operator from A1+A2;
- it does not close the BZ-corner species-label bridge;
- it introduces no new axiom, selector, observed target value, or fitted
  convention.

The already-landed eta-holonomy base-flux note provides the companion
spin-diagonal connection identity
`T(x)^dag sigma_mu T(x+e_mu)=eta_mu(x) I_2`; the present note supplies the
missing scalar chirality/parity sign field that was left conditional in the
2026-06-03 rescoping companion.
