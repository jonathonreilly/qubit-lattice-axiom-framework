---
claim_id: yt_c3_orientation_biased_phase_potential_orbit_member_no_go_note_2026-05-27
claim_type: no_go
actual_current_surface_status: no-go / open orientation-biased orbit-member law
trace_class: negative_route_pruning
reachability_to_target: prunes shortcut
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
---

# Y_T C3 Orientation-Biased Phase-Potential Orbit-Member No-Go

**Date:** 2026-05-27
**Status:** no-go for deriving the physical nontrivial top line from a
C3-invariant orientation-biased scalar phase potential alone. This note does
not claim retained or proposed-retained `Y_T` closure.
**Runner:**
`scripts/frontier_yt_c3_orientation_biased_phase_potential_orbit_member_no_go.py`
**Output:**
`outputs/yt_c3_orientation_biased_phase_potential_orbit_member_no_go_2026-05-27.json`

## Question

The current C3 route has already pruned C3-invariant scalar phase-orbit
selection, C3-covariant orbit-member readout, and the existing
dihedral/reflection basepoint shortcut. A plausible stronger premise remains:
add an orientation-biased same-surface phase potential with a reflection-odd
`sin(3 phi)` phase-bias term.

Does that orientation-biased potential supply the missing physical law that
assigns the top pole to a nontrivial C3 character line and therefore gives
`A/sqrt(12)`?

## Answer

No.

For the connected unit C3 base circle

```text
H(phi) = cos(phi) B_x + sin(phi) B_y,
```

the most local orientation-biased C3 scalar harmonic is

```text
V(phi) = c_0 + r cos(3 phi) + s sin(3 phi).
```

The `sin(3 phi)` term is reflection-odd, so it is the expected orientation
bias in this phase coordinate. But the whole potential is still invariant
under

```text
phi -> phi + 2 pi/3.
```

Thus it selects a C3 phase orbit, not a physical member of that orbit.
Equivalently,

```text
r cos(3 phi) + s sin(3 phi) = rho cos(3 phi - delta),
```

and the extrema occur at

```text
phi_n = delta/3 + 2 pi n/3.
```

All three orbit members have the same potential value. The top-line readout
is not constant on the orbit: a generic selected orbit cycles through
`P_0`, `P_omega2`, and `P_omega`. Therefore an orientation-biased C3 scalar
potential still cannot exclude the singlet member without an accepted physical
basepoint/readout law.

## Assumptions / Imports Exercise

Minimal premise set used:

- finite C3 cycle and connected Hermitian tangent basis `B_x, B_y`;
- unit C3 base circle for the same-surface phase operator;
- C3-invariant scalar phase potential with an explicit reflection-odd
  `sin(3 phi)` orientation-bias term;
- finite C3 spectral projectors and top-row response algebra;
- already-derived `B_x` source tangent and same-surface factorization support;
- no observed masses, fitted selectors, or target values.

Load-bearing open imports after the exercise:

- accepted physical basepoint/readout law selecting one member of the selected
  C3 orbit;
- accepted same-surface W/top projectors and source-generator matrix elements;
- strict same-source W/top pole rows with contact, FV/IR, and model-class
  controls.

Forbidden proof inputs are absent: `H_unit`, old Ward authority,
`yt_ward_identity`, `y_t_bare`, observed top/W/Z masses, PDG targets,
`alpha_LM`, plaquette/u0, Planck, alpha_s, fitted selectors, and target value
insertion.

## First-Principles / Elon Exercise

Adversarial checks:

1. **Use reflection oddness.** The `sin(3 phi)` term is genuinely
   reflection-odd, but reflection oddness changes the selected orbit phase; it
   does not choose one member inside the orbit.
2. **Use a generic phase offset.** Writing the potential as
   `rho cos(3 phi - delta)` allows any offset `delta`. This is a phase-law
   parameter, not a top-line law.
3. **Use the selected extrema.** The three extrema
   `delta/3 + 2 pi n/3` are degenerate by C3 invariance. One is a `P_0`
   witness and two are nontrivial witnesses for generic `delta`.
4. **Use pure orientation bias.** The pure `sin(3 phi)` case is just a
   shifted three-member orbit, so it has the same member-selection problem.
5. **Use as closure.** Not allowed. The accepted physical basepoint/readout
   section and W/top matrix elements remain absent.

## Finite Witness

The C3-line eigenvalue functions are

```text
lambda(P_0)      = sqrt(2/3) cos(phi)
lambda(P_omega)  = sqrt(2/3) cos(phi + 2 pi/3)
lambda(P_omega2) = sqrt(2/3) cos(phi - 2 pi/3).
```

For a generic orientation-biased potential with phase offset
`delta = pi/7`, the selected orbit is

```text
phi = pi/21              -> P_0      -> A/sqrt(3)
phi = pi/21 + 2 pi/3     -> P_omega2 -> A/sqrt(12)
phi = pi/21 - 2 pi/3     -> P_omega  -> A/sqrt(12)
```

Changing the orientation sign reflects the orbit but still leaves a `P_0`
member. The pure sine bias gives another strict three-member orbit:

```text
phi = pi/6              -> P_0
phi = pi/6 + 2 pi/3     -> P_omega2
phi = pi/6 - 2 pi/3     -> P_omega
```

So even the explicit orientation-bias premise does not supply an isolated
nontrivial physical top line.

## Stuck Fan-Out

| Attack frame | Outcome |
|---|---|
| Orientation-odd scalar harmonic | `sin(3 phi)` is real and reflection-odd, but remains C3-orbit-valued |
| Generic shifted harmonic | `cos(3 phi - delta)` selects a three-member orbit with equal values |
| Pure sine limit | selects another three-member orbit, not a physical member |
| Existing dihedral/reflection basepoint | existing reflection axis fixes `P_0`; rotated axes are extra basepoint imports |
| Strict pole-row bypass | remains live, but branch artifacts still mark accepted pole rows absent |

## No-Go Audit

This prunes the shortcut:

```text
C3-invariant orientation-biased phase potential
  -> physical nontrivial C3 top-line member
  -> A/sqrt(12).
```

The implication is false on the actual current surface. The potential supplies
an orbit-level phase law. The missing law is a physical member/readout
section, or strict same-source pole rows that bypass the C3 assignment.

## Literature / Math Search

No external numerical, phenomenological, or literature value is load-bearing.
The runner rederives the needed finite C3 Fourier/orbit algebra directly.
Adjacent repo math search was limited to the current phase-orbit selector,
orbit-member covariance, dihedral basepoint, cubic phase-potential, phase-cone,
matrix-element, and strict sparse availability artifacts. Those artifacts are
dependencies, not imported authorities.

## What Remains Open

Positive closure still requires one of:

- accepted strict same-source top/W pole rows; or
- an accepted same-surface physical basepoint/readout law that selects a
  nontrivial orbit member and supplies W/top source-generator matrix elements.

## Non-Claims

This note does not:

- claim retained or proposed-retained `Y_T` closure;
- refute a future accepted orientation/basepoint/readout theorem;
- refute future strict W/top pole rows;
- derive the accepted physical basepoint section;
- isolate the physical top pole;
- supply W/top source-generator matrix elements;
- derive `m_t`, physical-scale `g_2`, or numerical `y_t(v)`;
- use `H_unit`, `yt_ward_identity`, `y_t_bare`, observed W/Z/top masses, PDG
  values, `alpha_LM`, plaquette/u0, Planck, alpha_s, or a fitted selector as
  proof inputs.

## Claim-Status Certificate

```yaml
actual_current_surface_status: no-go / open orientation-biased orbit-member law
trace_class: negative_route_pruning
reachability_to_target: prunes shortcut
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: |
  A C3-invariant orientation-biased phase potential with a reflection-odd
  sin(3 phi) term still selects a three-member C3 phase orbit. Generic
  selected orbits contain a P_0 singlet-row witness and nontrivial target-row
  witnesses, and the pure sine bias has the same orbit-member problem. The actual
  surface does not derive an accepted physical basepoint/readout law, accepted
  W/top matrix elements, or strict pole rows.
bare_retained_allowed: false
audit_required_before_effective_retained: true
next_action: produce accepted strict top/W pole rows, or derive an accepted
  same-surface physical basepoint/readout law with W/top matrix elements
```

## Verification

Run:

```text
python3 scripts/frontier_yt_c3_orientation_biased_phase_potential_orbit_member_no_go.py
```

Expected result:

```text
SUMMARY: PASS=... FAIL=0
```
