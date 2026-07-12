# Common Propagator Rescaling: Exact Fierz-Channel Negative Boundary

**Date:** 2026-05-02
**Type:** no_go
**Status:** exact negative boundary; independent audit required
**Claim scope:** For any color matrix `G` and scalar `a`, the singlet and
adjoint Fierz functionals are homogeneous of degree two. A nonzero common
propagator rescaling `G -> a G` therefore preserves their relative weight and
cannot select the adjoint channel by relative rescaling. This note does **not** infer
`G_full = u_0 G_V` from the link-level replacement `U -> u_0 V`.
**Loop:** `yt-ew-m-residual-conditional-closure-20260711`
**Runner:** `scripts/yt_ew_m_residual_channel_check.py`
**Log:** `outputs/yt_ew_m_residual_channel_check_2026-05-02.txt`

## Question

The EW matching package needs a rule selecting the adjoint color channel of a
quark-antiquark correlator. An earlier version of this note tried to rule out
selection by Coupling Map Theorem (CMT) mean-field factorization
`U -> u_0 V`. That conclusion used

```text
G_full = u_0 G_V,                                                   (P)
```

but neither the cited source nor the runner derived (P) from the link
replacement. A lattice propagator is an inverse of a link-dependent Dirac
operator and is generally nonlinear in the links. The implication

```text
U -> u_0 V   therefore   G_full = u_0 G_V
```

is not part of this result.

The exact result below answers a narrower question: what follows **if a common
scalar map is specified directly on the propagator**?

## Definitions and explicit premise

For `SU(N_c)` generators normalized by
`Tr(t^A t^B) = delta_AB/2`, define

```text
S(G) = (1/N_c) |Tr G|^2,
C(G) = 2 sum_A |Tr(G t^A)|^2.                                      (1)
```

The Fierz completeness identity gives

```text
Tr(G^dagger G) = S(G) + C(G).                                      (2)
```

The only additional premise used in the no-go is the propagator-level scalar
map

```text
G' = a G,                                                          (3)
```

where `a` is a specified complex scalar. When `a = u_0` is real, equation (3)
has the same algebraic form as (P), but it remains a premise on `G`; it is not
a theorem about the effect of link factorization.

## Exact homogeneity theorem

Linearity of the trace gives

```text
S(aG) = (1/N_c) |a Tr G|^2
      = |a|^2 S(G),

C(aG) = 2 sum_A |a Tr(G t^A)|^2
      = |a|^2 C(G).                                                 (4)
```

Under the explicit propagator premise with real `a = u_0`, both channels
inherit the same u_0² scaling. If `a != 0`, the following channel ratios are
unchanged wherever their denominators are nonzero:

```text
C(aG)/S(aG) = C(G)/S(G),
C(aG)/(S(aG)+C(aG)) = C(G)/(S(G)+C(G)).                             (5)
```

If `a = 0`, both channels vanish; the map erases the correlator rather than
selecting the adjoint channel.

Thus a mechanism whose **entire action on the propagator** is common scalar
multiplication cannot suppress `S` relative to `C` or select `C` by changing
the relative channel weights. This is the exact negative boundary proved here.

## Scope boundary for CMT and the EW matching rule

Equation (4) does not establish how the actual lattice propagator transforms
under `U -> u_0 V`. In particular, this note makes no claim that CMT link
factorization is channel-blind and does not disprove CMT-only adjoint
selection. A link-dependent Dirac operator may induce a nonlinear or
non-scalar map on `G`; such a map lies outside the theorem.

The physical matching rule remains open. It may depend on:

- an explicitly adjoint-projected EW current;
- Wilson-line orientation and Wick-contraction structure;
- a specified renormalization prescription; or
- a non-scalar response of the inverse Dirac operator to link improvement.

Closing that physical rule requires an explicit lattice Dirac/EW-current
construction and a derivation of its induced propagator or correlator map.
None of those ingredients is imported here.

## No-go scope stress test

The negative boundary was attacked through six distinct route classes:

| Route class | Attack | Result/evidence |
|---|---|---|
| algebraic phase/sign | Let `a` be negative or complex | Equation (4) depends only on `|a|^2` |
| singular scalar | Set `a=0` | Both channels vanish; neither is selected |
| exceptional matrix | Take `S=0`, `C=0`, or `G=0` | Equation (4) remains valid; ratios are asserted only for nonzero denominators |
| representation/basis | Change `N_c` or the normalized generator basis | Trace linearity fixes the same degree-two factor; runner Test 2 checks the stated normalization |
| alternative readout | Apply an absolute threshold or channel-specific projector after scaling | Such extra structure can select a channel, but it is not common scalar multiplication alone and lies outside the claim |
| dynamical/non-scalar map | Let the Dirac inverse induce a nonlinear map on `G` | This can change relative weights and is explicitly left open |

The minimal premises are definitions (1), the generator normalization, and
the explicit propagator premise (3). The decisive calculation is (4). The
paired runner checks Fierz completeness, generator normalization, real and
complex homogeneity, ratio invariance, the zero case, and the source scope.
No earlier no-go is used to foreclose a broader physical mechanism.

## What is closed

Closed exactly:

- `S` and `C` are degree-two homogeneous functionals of `G`;
- a common nonzero scalar propagator map preserves their relative weight;
- common scalar multiplication alone cannot select `C` over `S` by changing
  their relative weights.

Not closed:

- `U -> u_0 V` implying `G_full = u_0 G_V`;
- the action of CMT link improvement on a lattice Dirac inverse;
- the framework's physical EW-current matching rule;
- the package-level `9/8` EW correction.

## Assumptions and imports

| Item | Role | Class | Load-bearing? | Disposition |
|---|---|---|---|---|
| Fierz definitions (1) | Defines `S` and `C` | exact algebraic identity | Yes | Derived inline from the cited decomposition |
| `G' = aG` | Defines the route being ruled out | explicit theorem premise | Yes | Kept in claim scope; not attributed to CMT |
| `U -> u_0V` | Motivation only | open physical bridge | No | Excluded from the proof and conclusion |
| EW-current construction | Physical channel selector | unsupported on this note's surface | No | Remains an open gate |

No fitted values, observed targets, or literature inputs enter the proof.

## Cited authority

- [`EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md`](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  supplies the Fierz definitions. Its matching rule (M) is not used as a
  premise or conclusion here.

## Review classification

```yaml
claim_type_author_hint: no_go
claim_scope: "For any color matrix G and scalar a, common propagator rescaling G -> aG multiplies both Fierz channels by |a|^2 and therefore cannot select the adjoint channel by relative rescaling; no link-to-propagator implication is claimed."
actual_current_surface_status: no-go
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "Independent audit must ratify the narrowed no-go before any audit-ratified status is assigned."
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies:
  - ew_current_fierz_channel_decomposition_note_2026-05-01
open_gate: "derive the map induced on G by the explicit lattice Dirac/EW-current construction under U -> u_0 V"
```

The `direct_blocker_closure` trace refers only to the audit repair target:
the unsupported bridge has been removed from the audited claim. Physically,
the theorem prunes the common-scalar propagator route and does not close
matching rule (M).
