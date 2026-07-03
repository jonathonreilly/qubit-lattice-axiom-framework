# Flavor Q1: The `C3` Reference Cone Does Not Force the Trace

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes the route "stipulated `C3` generation symmetry alone selects the tracial `1:2` block weighting".
**Bare retained allowed:** false
**Audit required before effective status change:** true
**Runner:** `scripts/flavor_Q1_default_rests_on_PRR_2026_05_30.py` (SCORECARD PASS=4).
**Source:** 6-agent build `wf_9977f75f` (reference-state cone; tracial-vs-Gibbs; observability; PRR steelman).

## Closed Packet

This note proves only the following finite statement:

> Given only the explicit `C3` generation-factor symmetry, the invariant
> reference-state cone is two-dimensional and does not select the tracial
> `1:2` block weighting.

It also checks that the displayed Koide `Q` functional is a spectral function
of the operator parameters and does not use the reference state. Therefore the
reference-state cone alone does not derive either a `Q=1` default or a
`Q=2/3` value.

## Direct Checks

1. **`C3`-invariant states form a two-block cone.** With
   `P_s=J_all/3` and `P_d=I-P_s`, a `C3`-invariant reference state is scalar
   on the singlet and doublet blocks. The tracial state has block masses
   `1:2`, while a non-tracial state can have block masses `1:1`.

2. **The `1:1` state is explicit and admissible.**
   `rho_(1:1)=1/2 P_s + 1/4 P_d` is positive semidefinite, trace one, and
   commutes with the `C3` shift. Thus `C3` covariance alone leaves this state
   in the admissible cone.

3. **Full `U(3)` invariance is a stronger selector.** The normalized trace is
   invariant under sampled `U(3)` conjugations, while `rho_(1:1)` is not. This
   is a mathematical comparison of symmetry strength, not a claim that the repo
   baseline either includes or excludes full `U(3)` on the generation factor.

4. **The reference state is not the displayed `Q` readout.** In the displayed
   formula, `r=|b|^2/a^2` is a spectral parameter of `H`; no `rho` appears.
   Any bridge from reference-state block masses to operator parameter `r` is an
   additional equation of state outside this packet.

## What This Does Not Claim

This packet intentionally does not decide:

- whether framework baseline supplies only `C3` on the generation factor;
- whether a stronger generation-factor symmetry is available elsewhere;
- whether full `U(3)`/PRR is accepted as a baseline principle;
- whether the physical mass readout counts the doublet once or twice;
- whether `Q=1` or `Q=2/3` is selected by the full framework.

The repaired conclusion is only the finite no-go: `C3` covariance by itself
does not force the trace, and reference-state weighting by itself does not fix
the displayed operator readout.

## Provenance

- Projector algebra, admissibility of `rho_(1:1)`, sampled full-`U(3)`
  non-invariance, and the displayed `Q`-formula independence check are verified
  directly by the paired runner.
- No `docs/audit/**` status is updated by this packet.
- No new axiom is introduced.
