---
claim_id: yt_c3_phase_ordering_cone_support_boundary_note_2026-05-27
claim_type: support_boundary
actual_current_surface_status: exact-support / open phase-ordering import
trace_class: upstream_support
reachability_to_target: supports
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
---

# Y_T C3 Phase-Ordering Cone Support Boundary

**Date:** 2026-05-27  
**Status:** exact support for the residual C3 phase-ordering condition; no
retained or proposed-retained `Y_T` closure.  
**Runner:** `scripts/frontier_yt_c3_phase_ordering_cone_support_boundary.py`  
**Output:** `outputs/yt_c3_phase_ordering_cone_support_boundary_2026-05-27.json`

## Question

After the C3 source derivative is fixed to

```text
dH/dell = B_x = (C+C^2)/sqrt(6),
```

what exact same-surface base-dynamics condition would make the physical top
line a nontrivial C3 character line rather than the singlet?

## Answer

For the connected Hermitian C3-circulant base operator

```text
H_0 = x_0 B_x + y_0 B_y,
B_y = i(C-C^2)/sqrt(6),
```

the three C3 character eigenvalues are

```text
lambda_0      =  2 x_0 / sqrt(6),
lambda_omega  = -x_0 / sqrt(6) - y_0 / sqrt(2),
lambda_omega2 = -x_0 / sqrt(6) + y_0 / sqrt(2).
```

Thus an isolated nontrivial top line under largest-eigenvalue ordering is
equivalent to the phase-ordering cone

```text
P_omega2 top  <=>  y_0 > 0  and  y_0 > sqrt(3) x_0,
P_omega  top  <=>  y_0 < 0  and -y_0 > sqrt(3) x_0.
```

The singlet region is

```text
P_0 top <=> x_0 > 0 and |y_0| < sqrt(3) x_0.
```

The degeneracy walls are

```text
P_omega2 = P_omega  <=>  y_0 = 0,
P_omega2 = P_0      <=>  y_0 =  sqrt(3) x_0,
P_omega  = P_0      <=>  y_0 = -sqrt(3) x_0.
```

This is the exact residual condition.  If a future accepted same-surface
microscopic theorem derives that the physical top base operator lies in one
of the two nontrivial cones, then the already-derived source derivative gives

```text
Tr(P_omega B_x) = Tr(P_omega2 B_x) = -1/sqrt(6),
```

and the radial factorization row gives the target magnitude `A/sqrt(12)`.

This note does not derive that phase-ordering cone from first principles. It
turns the remaining C3 route into a concrete certificate target.

## First-Principles / Elon Exercise

Minimal premise set used here:

- finite C3 spectral projectors;
- connected C3 Hermitian base dynamics `x_0 B_x + y_0 B_y`;
- derived C3 source tangent `B_x`;
- largest-eigenvalue ordering as an explicit conditional ordering rule;
- same-surface matrix-element factorization from the current stack.

Adversarial checks:

1. **Set `y_0=0`.** The nontrivial block is degenerate, so no isolated
   nontrivial top pole is derived.
2. **Set `x_0>0` and small `|y_0|`.** The singlet remains largest.
3. **Use positive real transfer/Perron selection.** This lands in the singlet
   case already pruned by the Perron no-go.
4. **Use the cone as a new axiom.** That would be conditional support only
   until a same-surface dynamics theorem derives it.

Forbidden proof inputs are absent: `H_unit`, old Ward authority,
`yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG targets,
`alpha_LM`, plaquette/u0, Planck, alpha_s, fitted selectors, and target value
insertion.

## Relation To Current Stack

This support boundary is downstream of:

- [`YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md`](YT_C3_CIRCULANT_DYNAMICS_ORDERING_SOURCE_LAW_BOUNDARY_NOTE_2026-05-27.md)
- [`YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md`](YT_C3_POSITIVE_TRANSFER_PERRON_TOP_LINE_NO_GO_NOTE_2026-05-27.md)
- [`YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md`](YT_SAME_SURFACE_TOP_MATRIX_ELEMENT_FACTORIZATION_BOUNDARY_NOTE_2026-05-27.md)

It does not supersede those boundaries.  It states the precise inequality
target a new microscopic dynamics/orientation theorem would need to derive.

## Non-Claims

This note does not:

- claim retained or proposed-retained `Y_T` closure;
- derive the accepted same-surface base C3 operator;
- derive the sign or magnitude of `y_0`;
- prove that the physical top pole is `P_omega` or `P_omega2`;
- supply strict W/top pole rows;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: exact-support / open phase-ordering import
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: "A/sqrt(12) follows if accepted same-surface dynamics derives the nontrivial C3 phase-ordering cone"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  The exact nontrivial C3 phase-ordering cone is characterized, but the actual
  current surface does not derive that the accepted physical top base operator
  lies in the cone. The phase/order law and strict pole rows remain open.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: derive the phase-ordering cone from accepted microscopic dynamics,
  or produce strict same-source top/W pole rows.
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_phase_ordering_cone_support_boundary.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
