---
claim_id: yt_signed_record_lower_projector_neutral_ray_algebra_core_bounded_note_2026-06-18
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Y_T Signed-Record Lower-Projector Neutral-Ray Algebra Core

**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support.
**Trace class:** upstream_support.
**Reachability:** supports `yt_qubit_neutral_higgs_carrier_ray_bridge_note_2026-05-25`
by isolating the closed algebra from the open same-surface carrier theorem.
**Primary runner:** `scripts/frontier_yt_signed_record_lower_projector_neutral_ray_algebra_core_2026_06_18.py`

## Scope

This note proves the algebraic core that survived audit review of the Y_T
neutral-Higgs carrier packet:

1. inside the one-site signed-record qubit algebra,
   `epsilon = sigma_z = P_+ - P_- = I - 2P_-`, so the signed source is
   affinely equivalent to lower-projector occupation;
2. inside the retained one-Higgs electroweak bookkeeping, the lower doublet ray
   is the neutral ray: `P_- H_0 = H_0` and `Q H_0 = 0`;
3. these facts are bounded support only.  They do not identify the qubit
   readout basis with the EW Higgs doublet basis as the same physical carrier
   surface.

## Cited Authority Surface

Load-bearing one-hop authorities:

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  supplies the one-qubit operator algebra baseline.
- [`YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md`](YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md)
  supplies the signed-record source-action support packet that uses the
  `epsilon` source coordinate.
- [`EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md`](EW_HIGGS_GAUGE_MASS_DIAGONALIZATION_THEOREM_NOTE_2026-04-26.md)
  supplies the one-Higgs electroweak doublet bookkeeping and neutral lower ray.

## Signed-Record Algebra

Let

```text
P_+ = (I + sigma_z) / 2,
P_- = (I - sigma_z) / 2.
```

Then

```text
epsilon = sigma_z = P_+ - P_- = I - 2P_-.
```

For source coordinate `h`,

```text
exp(h epsilon) = exp(h) exp(-2h P_-).
```

The factor `exp(h)` is record-independent and cancels in the normalized source
family, so the normalized signed-record source is the lower-projector
occupation source with affine coordinate `j = -2h`.

## EW Neutral-Ray Bookkeeping

In the retained one-Higgs EW doublet bookkeeping,

```text
T_3 = diag(1/2, -1/2),
Y_H = (1/2) I,
Q = T_3 + Y_H,
H_0 = (0, v/sqrt(2))^T.
```

Therefore

```text
P_- H_0 = H_0,
P_+ H_0 = 0,
Q H_0 = 0.
```

The upper basis ray is charged, `Q(1,0)^T = (1,0)^T`, so the lower doublet ray
is the neutral one-Higgs ray in this bookkeeping.

## Boundary

This note is not a same-surface physical carrier theorem.  The two appearances
of `P_-` above live in their stated two-dimensional algebraic surfaces.  The
runner verifies that the algebra is compatible and citable as bounded support;
it does not derive that the qubit signed-record source is physically the EW
neutral radial source.

Boundary guard: the algebraic facts do not identify the qubit readout basis with the EW Higgs doublet basis, and they do not establish a same physical carrier surface.

Do not cite this note as:

- a retained same-surface qubit/Higgs carrier theorem;
- physical neutral EW/Higgs source-action authority;
- a top/W Feynman-Hellmann response row;
- scalar LSZ normalization;
- hypercharge uniqueness;
- retained physical-scale `g_2(v)`;
- `m_t`, `y_t`, `v = 246 GeV`, or any observed-mass result.

## Review Boundary Certificate

```yaml
actual_current_surface_status: bounded-support
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  The finite lower-projector algebra closes, but the physical same-surface
  theorem identifying the qubit source ray with the EW radial source remains
  open.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Verification

Run:

```text
PYTHONPATH=scripts python3 scripts/frontier_yt_signed_record_lower_projector_neutral_ray_algebra_core_2026_06_18.py
```

Expected result:

```text
TOTAL: PASS=... FAIL=0
```
