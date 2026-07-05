# Teleportation Finite Gapped Preparation Path Support

**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Primary runner:** `scripts/teleportation_finite_gapped_preparation_path_support_2026_06_16.py`
**Parent open gate:** `docs/TELEPORTATION_RESOURCE_FROM_POISSON_NOTE.md` (trace target, not a proof dependency of this support artifact)

actual_current_surface_status: bounded-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: finite sampled support only; not a deterministic physical resource theorem; physical preparation/readout and apparatus theorem remain open
audit_required_before_effective_retained: true
bare_retained_allowed: false

## Scope

This note supplies a finite preparation-path support artifact for the
teleportation Poisson/CHSH open gate. It addresses only one part of the
audited blocker:

> The finite Hamiltonian resource had been obtained by offline diagonalization,
> while no native preparation/readout or apparatus theorem realized it as a
> physical deterministic teleportation resource.

The support result here is narrow. On the existing audited finite surfaces
(`1D N=8` and `2D 4x4`, mass zero), the same Poisson/CHSH Hamiltonian family
used by `scripts/frontier_teleportation_resource_from_poisson.py` has an
exactly affine finite-dimensional path

```text
H(G) = H(0) + G W,          0 <= G <= 1000,
```

where `W` is the diagonal two-particle Poisson interaction operator. The new
runner checks that the path is Hermitian, exactly matches the helper
Hamiltonian builder, has positive sampled ground-state gap on the declared
grid, and reaches the same high-fidelity traced retained-axis Bell resource at
`G=1000`.

This is sampled finite-surface support; it is not a deterministic physical
resource theorem in the parent row's audit sense. It does not close physical
detector/readout, durable endogenous records, apparatus dynamics, a
continuum/infinite-volume gap, or a native schedule-selection theorem.

## Finite Path Certificate

For each audited surface, the runner constructs:

- `H0 = H1 x I + I x H1`, with the existing staggered one-particle Hamiltonian;
- `V`, the existing periodic Poisson Green function;
- `W = diag(V(i,j))` on the two-species tensor product basis;
- `H(G) = H0 + G W`;
- the helper-built Hamiltonian `build_H2_tensor(H1, V, G, N)`.

The runner checks equality between the affine form and the helper-built
Hamiltonian at all sampled `G` values:

```text
G in {0, 1e-6, 1e-3, 1e-2, 0.1, 1, 3, 10, 30, 100, 300, 600, 1000}.
```

It then diagonalizes the finite Hermitian matrix and records the gap between
the two lowest eigenvalues. The minimum sampled gaps are:

| surface | minimum sampled gap | location |
| --- | ---: | ---: |
| `1D N=8` | `1.868322783207077e-02` | `G=1000` |
| `2D 4x4` | `2.46378016628003e-01` | `G=1000` |

The finite null endpoint is not a traced Bell resource, while the `G=1000`
endpoint is:

| surface | null Bell overlap | target Bell overlap | target negativity | target ideal teleportation mean fidelity |
| --- | ---: | ---: | ---: | ---: |
| `1D N=8` | `0.500000000000` | `0.997963462171` | `0.497963462171` | `0.998633169681` |
| `2D 4x4` | `0.500000000000` | `0.970283099736` | `0.470283099736` | `0.980738307895` |

## What Moved

This narrows the parent blocker from "the resource is only an offline
diagonalized endpoint" to the following finite-surface statement:

1. the endpoint resource remains the same retained-axis traced Bell resource
   already checked by the parent runner;
2. the finite Hamiltonian can be embedded in an explicit affine Hamiltonian
   path from the null endpoint to the resource endpoint;
3. the sampled path has a positive finite ground-state gap on the audited
   surfaces.

That is useful preparation-path evidence. It makes an adiabatic-style finite
preparation route plausible enough to inspect, but it is not a retained-grade
preparation theorem.

## What Remains Open

The following are still not supplied here:

- an all-`G` analytic gap lower bound between samples;
- an infinite-volume or continuum gap statement;
- a physical clock/schedule theorem selecting the ramp;
- a native detector/readout path for the retained-axis logical bit and Bell
  record;
- durable endogenous record formation for the Bell-measurement outcomes;
- a microscopic apparatus Hamiltonian implementing the ideal logical
  teleportation protocol.

No new axiom, primitive, approved premise, or apparatus theorem is introduced.
The parent row should remain an open gate unless a later independent source
artifact closes the native preparation/readout and apparatus theorem and the
audit lane ratifies that closure.

## Verification

Command:

```bash
python3 scripts/teleportation_finite_gapped_preparation_path_support_2026_06_16.py
```

Expected summary:

```text
TOTAL: PASS=76 FAIL=0
VERDICT: bounded finite preparation-path support passes; physical apparatus/readout remains open.
```
