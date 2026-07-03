# Corner Mode-Set Fork: The Resolution Layer Is Record Dynamics, Not Registrability

**Date:** 2026-06-12
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set, predict, promote, or demote any audit outcome and does not edit the audit-lane-owned registry or any audit data file.
**Primary runner:** `scripts/frontier_corner_fork_resolution_layer_record_dynamics_2026_06_12.py`

## Boundary

This note proves Y1-Y4 below on the supplied free corner-axis transfer class
only. It does not select the per-channel branch or the per-K-orbit branch; it
does not fix `r`; it does not adopt orbit-occupancy; it does not adopt the R-D
fixedness route; it does not claim the orbit pairing is physically realized;
and it does not resolve the fork.

Firewall: neither fork branch is selected; `r` is never fixed; the binary stays open;
no branch-closing claim is made; the free `U=1` corner-axis class is
supplied in-note. The orbit factor in Y2 is a bookkeeping definition for one
orbit slot, not a physical realization claim.

## The Supplied Class

The supplied class is three decoupled 1+1d staggered channels with circulant
masses

`lambda_k(delta) = a + 2B cos(delta + 2 pi k/3)`, for `k = 0,1,2`,

on the positivity domain `a > 2B > 0`. The per-channel two-step transfer
kernel is the retained free construction

`t_k(p) = exp(-2 E(lambda_k, p))`, with
`sinh(E(lambda_k, p))^2 = lambda_k^2 + sin(p)^2`.

The spatial length used by the runner is `L_s = 2`, with the two APBC momenta
`p = (2n+1) pi/L_s`. The K action swaps the doublet channels: the runner
verifies symbolically that `lambda_2(delta) = lambda_1(-delta)`. The physical
identification of this class rides with the `AC_phi_lambda` admission; here the
class is supplied directly.

## The Theorem

> **Theorem.** On the supplied free corner-axis transfer class, the
> per-channel partition branch and the per-K-orbit partition branch are both
> registrable readouts, but they are generically different. Therefore the
> registrability constraint is blind to the fork. The live resolution layer is
> record dynamics: either durable registration under the retained record-flow
> family or an orbit-occupancy premise, if later adopted, acts at the dynamics
> layer. Nothing here selects a branch.

**Y1 -- per-channel branch registrable.** Define
`D_k = det(1 + t_k) = prod_p (1 + exp(-2 E(lambda_k,p)))` and
`Z_ch = prod_k D_k`. Because the doublet swap only exchanges `D_1` and `D_2`,
`Z_ch` is invariant under K. Because `lambda_0(delta) = lambda_0(-delta)` and
`lambda_1(delta)`/`lambda_2(delta)` are exchanged by `delta -> -delta`,
`Z_ch(delta) = Z_ch(-delta)`. Its logarithm is additive over the three disjoint
record factors: `log Z_ch = sum_k log D_k`. Thus, by the cited registrability
class, finitely additive plus K/CPT-orbit-constant, the per-channel branch is a
registrable readout. [checks Y1a-Y1c]

**Y2 -- per-K-orbit branch registrable.** Define the one-slot orbit
bookkeeping factor by

`D_orb := sqrt(D_1 D_2)`.

This is the symmetrized/geometric orbit-slot bookkeeping of the same doublet
spectral content; it is not a physical realization claim and not a claim that
a physical single-channel kernel has been realized. Define `Z_orb = D_0
D_orb`. The expression is invariant under
the doublet swap, even under `delta -> -delta`, and additive in the log over
the two disjoint record factors `{singlet, orbit}`:
`log Z_orb = log D_0 + log D_orb`. Hence the per-K-orbit branch is also a
registrable readout. [checks Y2a-Y2b]

**Y3 -- the fork is registration-blind.** The runner computes both branches at
`(a,B,delta) = (1,1/4,2/9)` and at a second positivity-domain point. In both
cases `Z_ch` and `Z_orb` are positive and unequal. Since both branches pass
the same additivity and K/CPT-orbit-constancy tests, registrability does not
decide between them. This sharpens the landed independence result: the fork
survives the registration layer. [checks Y3]

**Y4 -- the named resolution layer is record dynamics.** The named live
resolvers act on the dynamics layer: durable registration under the retained
record-flow family (the R-D fixedness route) and the orbit-occupancy premise.
The fork's resolution layer is therefore record dynamics, not registration.
This is a layer statement only, not a branch choice. [check Y4]

## Consequence

The wave-6 corner-extension fork is wired to the R-D lane this way:
registration cannot decide it, because both fork branches are registrable on
the supplied class and differ at generic domain points. Any later branch
discrimination must come from a dynamics-level rule, such as R-D durability or
orbit-occupancy if adopted. This note adds no such rule.

## What This Note Does NOT Claim

- It does not select the per-channel branch.
- It does not select the per-K-orbit branch.
- It does not fix `r`.
- It does not adopt orbit-occupancy.
- It does not adopt the R-D fixedness route.
- It does not claim `D_orb = sqrt(D_1 D_2)` is physically realized as a new
  transfer kernel.
- It does not retire or weaken `AC_phi_lambda`.
- It does not edit any registry, audit ledger, admission, or cache.
- It does not close the binary.

## Dependencies

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
- [`REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md`](REGISTRABLE_READOUT_ADDITIVE_EVEN_PHASE_FREE_NARROW_THEOREM_NOTE_2026-06-10.md)

## Context

Context only, not load-bearing; all facts used here are reproven in the
runner: `wave-6 corner-extension note`, `wave-4 corner companion`,
`wave-5 corner companion`, `KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`,
`KOIDE_R_HALF_DURABILITY_STATIONARITY_CONDITIONAL_CHAIN_BOUNDED_THEOREM_NOTE_2026-06-11.md`.

**No-promotion statement:** this note does not promote, demote, or set the audit status of any dependency, context note, branch, premise, registry entry, or fork outcome. The independent audit lane is the only status authority.
