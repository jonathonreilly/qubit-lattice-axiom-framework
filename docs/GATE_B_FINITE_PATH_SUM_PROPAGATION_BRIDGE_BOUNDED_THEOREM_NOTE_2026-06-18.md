# Gate B Finite Path-Sum Propagation Bridge Bounded Theorem Note

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status:** bounded-support source bridge for `GB-S2a`; not a Gate B dynamics
closure and not an audit-ratified effective status.
**Status authority:** independent audit lane only. This note does not edit or
predict an audit verdict.
**Primary runner:** [`scripts/gate_b_finite_path_sum_propagation_bridge_2026_06_18.py`](../scripts/gate_b_finite_path_sum_propagation_bridge_2026_06_18.py)
**Cached output:** [`logs/runner-cache/gate_b_finite_path_sum_propagation_bridge_2026_06_18.txt`](../logs/runner-cache/gate_b_finite_path_sum_propagation_bridge_2026_06_18.txt)
**Helper runner (audit packet must include):** [`scripts/gate_b_connectivity_tolerance.py`](../scripts/gate_b_connectivity_tolerance.py)
— SHA-pinned cache [`logs/runner-cache/gate_b_connectivity_tolerance.txt`](../logs/runner-cache/gate_b_connectivity_tolerance.txt).
The primary runner imports this helper as `gate_b` and verifies the helper's
`_propagate`, `_build_fixed_connectivity`, `_field_for_mass`,
`_blocked_barrier`, `_detector_probs`, and `_mass_window_gain` surfaces against
an independent finite path-sum reconstruction. This helper source plus cache
must be present in the restricted audit packet for the load-bearing runner
calls to be inspectable.

## Purpose

The audited Gate B parent row currently treats `GB-S2`, the
propagation/readout semantics, as supplied row-local data. This note splits
that item.

| ID | Piece | Boundary |
|---|---|---|
| `GB-S2a` | finite complex-amplitude propagation on the supplied layered DAG | proved here as exact finite path-sum algebra for the current runner kernel |
| `GB-S2b` | central-barrier physical semantics, detector-window mass gain, `TOWARD`, and `F~M` readout semantics | still supplied Gate-B runner data |

This is a source-side bridge, not a physical-gravity theorem. It shows that
the runner propagation is not opaque: it is exactly the finite path expansion
of a declared edge kernel. It does not derive why that kernel or detector
readout is the physical Gate B rule.

## The finite propagation statement

Let `Gamma` be one of the finite layered Gate B DAGs used by
`scripts/gate_b_connectivity_tolerance.py`. For each directed edge
`i -> j`, the runner assigns the edge weight

```text
W_ij = exp(i K L_ij (1 - (f_i + f_j)/2)) * exp(-BETA theta_ij^2) / L_ij.
```

Blocked nodes are removed from the propagation. Starting from the declared
source amplitude, the runner recursion

```text
a_j(new) += a_i(old) W_ij
```

therefore equals the finite directed path sum

```text
a_d = sum_{paths source -> d avoiding blocked nodes} product_{edges e in path} W_e
```

for every detector node `d` in the final layer.

## Bounded theorem

The verifier checks four facts on a representative finite Gate B slab.

1. **Runner equality.** The current `_propagate` recursion exactly matches an
   independently enumerated path-sum over all unblocked directed paths.
2. **Linearity.** The transfer is linear in the initial source amplitudes.
3. **Blocked-node deletion.** Paths through blocked nodes contribute zero and
   the blocked-node set is exactly skipped by the path enumerator.
4. **Terminal normalization.** Once a finite detector set is supplied, the
   runner's terminal probability normalizer returns a nonnegative distribution
   summing to one when terminal intensity is nonzero.

These facts are mathematical properties of the finite runner packet. They do
not supply a physical measurement, gravity, or mass-readout theorem.

## Claim boundary

This note supports only:

```text
GB-S2a: the Gate B finite-layer propagation recursion is exact path-sum
algebra on the supplied finite DAG and edge kernel.
```

It does not claim:

- `GB-S2` is fully derived;
- the edge kernel is selected by framework dynamics;
- the central barrier is a physical apparatus theorem;
- detector-window mass gain, `TOWARD`, or `F~M` is a physical gravity readout;
- `GB-S1b` scalar normalization is derived;
- `GB-S3` generated connectivity is derived;
- the parent Gate B dynamics row is closed or promoted;
- a new axiom, Tier-A admission, or audit verdict.

Therefore the parent Gate B dynamics row remains an open gate. A later re-audit
can treat the finite path-sum algebra portion of `GB-S2` as source-supplied by
this theorem packet while continuing to require the physical readout bridge.

## Verification

Run:

```bash
python3 scripts/gate_b_finite_path_sum_propagation_bridge_2026_06_18.py
```

Expected result:

```text
TOTAL: PASS=13 FAIL=0
```
