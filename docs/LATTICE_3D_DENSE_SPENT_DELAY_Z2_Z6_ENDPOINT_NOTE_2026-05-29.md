# 3D Dense Spent-Delay `z=2..6` Endpoint Packet

**Date:** 2026-05-29
**Status:** bounded-support positive packet; proposed for independent audit, no effective status change.
**Claim type:** bounded_theorem
**Primary runner:** [`scripts/lattice_3d_dense_z2_z6_endpoint_check.py`](../scripts/lattice_3d_dense_z2_z6_endpoint_check.py)
**Cached runner output:** [`logs/runner-cache/lattice_3d_dense_z2_z6_endpoint_check.txt`](../logs/runner-cache/lattice_3d_dense_z2_z6_endpoint_check.txt)
**Source packet verifier:** [`scripts/lattice_3d_dense_z2_z6_endpoint_source_packet_manifest_2026_06_05.py`](../scripts/lattice_3d_dense_z2_z6_endpoint_source_packet_manifest_2026_06_05.py)
**Cached source packet verifier output:** [`logs/runner-cache/lattice_3d_dense_z2_z6_endpoint_source_packet_manifest_2026_06_05.txt`](../logs/runner-cache/lattice_3d_dense_z2_z6_endpoint_source_packet_manifest_2026_06_05.txt)
(SUMMARY: DENSE ENDPOINT SOURCE PACKET PASS=28 FAIL=0)

## Purpose

This packet repairs the exact missing endpoint named by the audit blocker for
the archived dense spent-delay row. The existing retained-bounded resolution
note already supports the live `z=2..5` finite card through
[`scripts/lattice_3d_dense_10prop.py`](../scripts/lattice_3d_dense_10prop.py).
This packet does not mutate that audited primary runner. Instead it adds a
dedicated endpoint runner that imports the same dense-lattice harness and
checks the previously omitted `z=6` row alongside `z=2..5`.

No new axiom, observed target value, fitted selector, or external comparator is
introduced. The scope is the finite dense spent-delay harness only.

## 2026-06-05 Source Packet Exposure Repair

The current blocker asks for the load-bearing helper source imported by the
endpoint runner. The source packet is now explicit:

- Endpoint checker: [`scripts/lattice_3d_dense_z2_z6_endpoint_check.py`](../scripts/lattice_3d_dense_z2_z6_endpoint_check.py)
- Endpoint checker cache: [`logs/runner-cache/lattice_3d_dense_z2_z6_endpoint_check.txt`](../logs/runner-cache/lattice_3d_dense_z2_z6_endpoint_check.txt)
- Dense helper source: [`scripts/lattice_3d_dense_10prop.py`](../scripts/lattice_3d_dense_10prop.py)
- Dense helper cache: [`logs/runner-cache/lattice_3d_dense_10prop.txt`](../logs/runner-cache/lattice_3d_dense_10prop.txt)

The source packet verifier above checks that every path is linked from this
note, that the endpoint checker imports the dense helper, that the load-bearing
generation, propagation, field, and sign-classification functions are present
in the untruncated helper source, and that both caches are SHA-fresh. This does
not set a verdict; it makes the bounded packet reviewable with the missing
helper source exposed.

Current source-packet output:

```text
SUMMARY: DENSE ENDPOINT SOURCE PACKET PASS=28 FAIL=0
```

For the audit packet dependency scanner, the endpoint checker uses the static
import form `import scripts.lattice_3d_dense_10prop as dense`; this is the form
recognized by `scripts/audit_packet_script_deps.py`, so the next packet build
can populate `helper_runner_paths` with
`scripts/lattice_3d_dense_10prop.py`.

## Live Endpoint Runner

The runner computes detector-centroid shift, near-mass probability gain, and
mass-side bias for `z = 2, 3, 4, 5, 6` in the existing dense `L=12`,
`W=6`, `h=1.0`, 49-edge/node spent-delay harness.

Current live output:

```text
 z     centroid       P_near         bias         sign
 2 +3.101326e-03 +1.469137e-03 +1.070972e-01   ATTRACTIVE
 3 +1.941146e-03 +3.741160e-04 +1.763808e-01   ATTRACTIVE
 4 +1.157377e-03 +6.261414e-04 +1.136756e-01   ATTRACTIVE
 5 +6.932863e-04 +7.148235e-04 +4.860136e-02   ATTRACTIVE
 6 +5.723120e-04 +5.356147e-04 +1.115616e-04   ATTRACTIVE

hierarchy-aligned support: 5/5 points
ASSERTIONS: PASS
```

The `z=6` endpoint is positive on all three finite signs used by the harness:
centroid shift, near-window probability, and side-bias. The side-bias is small
at `z=6`, so the safe read is endpoint support for the finite tested card, not
an asymptotic attraction theorem.

## Claim Boundary

This packet supports only the following bounded positive claim:

> In the existing 3D dense spent-delay harness, the finite endpoint scan
> `z=2..6` has hierarchy-aligned attractive support at every tested point,
> including the previously omitted `z=6` endpoint.

It does not claim:

- attraction for all source distances;
- continuum or asymptotic attraction;
- physical Newtonian gravity;
- a stronger distance-law theorem than the finite printed endpoint scan;
- effective retained status before independent audit.

Independent audit should use this row to decide whether the old z=6 runner
artifact blocker has been repaired by a dedicated endpoint certificate.
