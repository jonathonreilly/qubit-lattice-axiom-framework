# Plaquette V=1 Picard-Fuchs ODE — Finite-Runner Certificate Note

**Date:** 2026-05-05 (originally); 2026-05-17 (scope narrowed to finite runner certificate per audited_conditional repair)
**Claim type:** bounded_theorem
**Status:** bounded finite-runner certificate, unaudited.
**Primary runner:** `scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py`

## Scope narrowing (2026-05-17 audited_conditional repair)

The 2026-05-10 audit verdict on this row was `audited_conditional` with
repair class `scope_too_broad`, stating: *"re-audit as clean only after
narrowing this row to the finite runner certificate or after retaining
an all-order proof/dependency that closes the exact physical-integral
Picard-Fuchs and Frobenius-branch claim."*

This revision implements the narrowing. The audited content of this note
is now **only** the finite runner certificate:

- a finite-precision **truncated-series** check that the displayed
  third-order linear ODE annihilates the Taylor coefficients of `J(β)`
  through the runner's tested order, and
- a finite **numerical-agreement** check at the discrete sample points
  `β ∈ {2, 4, 6, 8, 10}` between the ODE-evolved Frobenius branch at
  `β = 0` and direct Weyl-integration evaluations of `J(β)`, with the
  derived single-plaquette readout `J'(6)/J(6) = 0.4225317…` at the
  canonical evaluation point `β = 6`.

The note **does not** claim that the displayed ODE is the exact
Picard-Fuchs equation of the SU(3) single-plaquette integral as an
algebraic identity in `Q[[β]]`, nor that the Frobenius branch identification
holds to all orders. The separate companion row
`PLAQUETTE_V1_PICARD_FUCHS_ODE_ALL_ORDER_PROOF_NOTE_2026-05-09.md` is now
narrowed to the same finite-window boundary family: exact checks through the
runner window, a D-finiteness witness, finite-grid lower-order exclusion, and
conditional Bostan-Salvy-Schost arithmetic if an external all-degree
`R=3,D=2` bridge is supplied. The all-degree bridge remains open.

**Finite-window boundary companion (narrowed 2026-06-08):**
`PLAQUETTE_V1_PICARD_FUCHS_ODE_ALL_ORDER_PROOF_NOTE_2026-05-09.md`
preserves the useful finite-window and conditional arithmetic packet without
claiming standalone all-order closure. The independent audit lane decides
whether that narrowed companion is clean on its repaired scope.
(Backticked to break five nested length-2/3/4 citation cycles in the
plaquette V=1 Picard-Fuchs cluster; citation graph direction is
*all_order_proof -> this_note*, since the historical companion row
consumes this V=1 ODE statement as its target while this bounded
ODE note's truncated-series claim does not consume the downstream
finite-window boundary packet as an input. This single demotion cascades
to break the four longer cycles through `bounded_synthesis_note_2026-05-06`,
`minimality_proof_note_2026-05-06`,
`koutschan_minimality_note_2026-05-06`, and
`rank_bound_citation_note_2026-05-06`, since each runs through the
same `this_note → all_order_proof` back-edge.)

## Claim (audited finite-runner certificate)

For the single-plaquette SU(3) Wilson integral

```text
J(beta) = integral_SU(3) exp(beta Re Tr U / 3) dU,
```

the runner verifies, **at finite truncation order**, that the candidate
third-order linear ODE

```text
6 beta^2 J'''(beta)
+ beta(60 - beta) J''(beta)
+ (-4 beta^2 - 2 beta + 120) J'(beta)
- beta(beta + 10) J(beta) = 0
```

annihilates the truncated Taylor series of `J(β)` at `β = 0` through the
runner's tested order, and that numerical integration of this ODE from
its Frobenius branch at `β = 0` agrees with direct Weyl-integration
evaluations of `J(β)` at the discrete sample points
`β ∈ {2, 4, 6, 8, 10}`. At the canonical evaluation point `β = 6`, the
ODE-evolved readout gives

```text
<P>_V=1(beta=6)  =  J'(6) / J(6)  =  0.422531739650.
```

> **Out of audited scope of this note:** the all-order algebraic claim
> that the displayed ODE *is* the exact Picard-Fuchs equation of the
> SU(3) integral in `Q[[β]]`, and the all-order Frobenius-branch
> identification, are *not* part of this finite-runner certificate.
> The companion row
> `PLAQUETTE_V1_PICARD_FUCHS_ODE_ALL_ORDER_PROOF_NOTE_2026-05-09.md`
> is now only a finite-window boundary packet unless a separate all-degree
> `R=3,D=2` bridge is supplied.

## Scope

This is a bounded single-plaquette **finite-runner certificate** result.
It does not:

- claim the displayed ODE is the exact algebraic Picard-Fuchs equation
  of the SU(3) single-plaquette integral to all orders,
- claim the all-order Frobenius-branch identification of `J(β)` at
  `β = 0`,
- compute the thermodynamic-limit Wilson plaquette value,
- promote any plaquette, bridge, or downstream coupling status, or
- assert agreement at any continuum `β` other than the runner-tested
  discrete sample points `{2, 4, 6, 8, 10}`.

The two broader exploratory notes from PR #541 are not landed here:
their `research_finding` claim type is not canonical for the audit lane,
and they referenced retained plaquette status that current main does not
grant. This note salvages only the runner-backed V=1 ODE truncated-series
and discrete-sample numerical-agreement certificate.

## Audit Consequence

```yaml
claim_id: plaquette_v1_picard_fuchs_ode_note_2026-05-05
note_path: docs/PLAQUETTE_V1_PICARD_FUCHS_ODE_NOTE_2026-05-05.md
runner_path: scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py
claim_type: bounded_theorem
intrinsic_status: unaudited
deps: []
audit_authority: independent audit lane only
```

## Command

```bash
python3 scripts/frontier_su3_v1_picard_fuchs_ode_2026_05_05.py
```

Expected summary:

```text
SUMMARY: THEOREM PASS=4 FAIL=0
```
